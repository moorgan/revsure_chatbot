from flask import Flask, request
import requests
import json
import sys, locale

#print(sys.getfilesystemencoding())
#print(locale.getpreferredencoding())

app = Flask(__name__)


@app.route('/')  # this is the home page route
def hello_world(
):  # this is the home page function that generates the page code
	return "Hello world!"


@app.route('/webhook', methods=['POST'])
def webhook():

	req = request.get_json(silent=True, force=True)

	api_request_headers = {
	 "cookie":
	 "rs_sid=eyJraWQiOiJoUDltRmtwOWtQOW1TcnlzN3IwREd4SEdiRDRpUWJ5TWFpVnB2bVI4ZFQ0IiwidHlwIjoiSldUIiwiYWxnIjoiRVM1MTIifQ.eyJzdWIiOiI2MjE5YmZiNS0xMGJiLTQxMzctYmYxYS01MjAzZjY5OTUxOGEiLCJhdWQiOiI2MjE5YmZiNS0xMGJiLTQxMzctYmYxYS01MjAzZjY5OTUxOGEiLCJpc3MiOiJSZXZTdXJlLkFJIiwiZXhwIjoxNjc4MjkxMTE5LCJpYXQiOjE2NzgyNDc5MTksImp0aSI6IjkxZjZiODkxLTI4ZjktNGRjMi05NTJkLTM2ZDYzYmM5ZDJiNyIsInRpZCI6IjEwMjY1OGY0LWE0ZWMtNDkxMi05NzJjLTVmNGQ2NWZmNjUzMSIsInNpZCI6Ijc1OWNiYjNhLTRkY2MtNGEwNC04OGU5LTNiYTI5NWY3YjgwMyJ9.AJd3u-wsS5CVx-HYiajon-z81buelMeAMZ_pPIAQLJGsZkdoHqcbyCNtqYki3x2HgOclE2wKTLSXl2woaM-lT6e-AMG9TngUg8wl6yp56spsbaF2jBvu9VJxPzoPuBQGgub9-dzRVzpsItxo6JqF2e6MfYq_QYE_dsiVskZc2paB9oGh",
	 "authority": "dt1.revsure-staging.cloud",
	 "content-type": "application/json"
	}
	text = ''
	fulfillmentText = ''

	query_result = req.get('queryResult')

	print(query_result.get('action'))

	if query_result.get('action') == 'funnel.headline.metrics':

		filters = {
		 "dateFilter": "lastYear",
		 "dateGroup": "quarter",
		 "funnelType": "snapshot"
		}
		api_url = "https://dt1.revsure-staging.cloud/api/v2/section/funnel-performance/funnel"
		api_response = requests.post(api_url,
		                             headers=api_request_headers,
		                             json=filters)
		#print(api_response.status_code)

		if api_response.status_code == 200:
			response = api_response.json()
			#print(response)

			#tofu_label = response['data'][0]['label']
			lead_name = response['data'][0]['cards'][0]['name']
			lead_current_value = response['data'][0]['cards'][0]['currentValue']
			lead_diff = response['data'][0]['cards'][0]['diff']
			lead_diff_percentage = response['data'][0]['cards'][0]['diffPercent']
			lead_diff_percent = lead_diff_percentage.split("%")[0] + "%"
			lead_trend = response['data'][0]['cards'][0]['trend']
			lead_trend_emojy = ''
			if lead_trend == 'down':
				lead_trend_emojy = ":arrow_down:"
			elif lead_trend == "up":
				lead_trend_emojy = ":arrow_up:"

			mql_name = response['data'][0]['cards'][1]['name']
			mql_current_value = response['data'][0]['cards'][1]['currentValue']
			#mql_last_value = response['data'][0]['cards'][1]['lastValue']
			mql_diff = response['data'][0]['cards'][1]['diff']
			mql_diff_percentage = response['data'][0]['cards'][1]['diffPercent']
			mql_diff_percent = mql_diff_percentage.split("%")[0] + "%"
			mql_trend = response['data'][0]['cards'][1]['trend']
			mql_trend_emojy = ''
			if mql_trend == 'down':
				mql_trend_emojy = ":arrow_down:"
			elif mql_trend == "up":
				mql_trend_emojy = ":arrow_up:"

			sal_name = response['data'][0]['cards'][2]['name']
			sal_current_value = response['data'][0]['cards'][2]['currentValue']
			#sal_last_value = response['data'][0]['cards'][2]['lastValue']
			sal_diff = response['data'][0]['cards'][2]['diff']
			sal_diff_percentage = response['data'][0]['cards'][2]['diffPercent']
			sal_diff_percent = sal_diff_percentage.split("%")[0] + "%"
			sal_trend = response['data'][0]['cards'][2]['trend']
			sal_trend_emojy = ''
			if sal_trend == 'down':
				sal_trend_emojy = ":arrow_down:"
			elif sal_trend == "up":
				sal_trend_emojy = ":arrow_up:"

			sql_name = response['data'][1]['cards'][0]['name']
			sql_current_value = response['data'][1]['cards'][0]['currentValue']
			sql_diff = response['data'][1]['cards'][0]['diff']
			sql_diff_percentage = response['data'][1]['cards'][0]['diffPercent']
			sql_diff_percent = sql_diff_percentage.split("%")[0] + "%"
			sql_trend = response['data'][1]['cards'][0]['trend']
			sql_trend_emojy = ''
			if sql_trend == 'down':
				sql_trend_emojy = ":arrow_down:"
			elif sql_trend == "up":
				sql_trend_emojy = ":arrow_up:"

			pipeline_name = response['data'][1]['cards'][1]['name']
			pipeline_current_value = response['data'][1]['cards'][1]['currentValue']
			pipeline_diff = response['data'][1]['cards'][1]['diff']
			pipeline_diff_percentage = response['data'][1]['cards'][1]['diffPercent']
			pipeline_diff_percent = pipeline_diff_percentage.split("%")[0] + "%"
			pipeline_trend = response['data'][1]['cards'][1]['trend']
			pipeline_trend_emojy = ''
			if pipeline_trend == 'down':
				pipeline_trend_emojy = ":arrow_down:"
			elif pipeline_trend == "up":
				pipeline_trend_emojy = ":arrow_up:"

			won_name = response['data'][2]['cards'][0]['name']
			won_current_value = response['data'][2]['cards'][0]['currentValue']
			won_diff = response['data'][2]['cards'][0]['diff']
			won_diff_percentage = response['data'][2]['cards'][0]['diffPercent']
			won_diff_percent = won_diff_percentage.split("%")[0] + "%"
			won_trend = response['data'][2]['cards'][0]['trend']
			won_trend_emojy = ''
			if won_trend == 'down':
				won_trend_emojy = ":arrow_down:"
			elif won_trend == "up":
				won_trend_emojy = ":arrow_up:"

			fulfillmentText = {
			 "fulfillmentMessages": [{
			  "payload": {
			   "slack": {
			    "text":
			    "Response from dt1.revsure-staging.cloud",
			    "attachments": [{
			     "blocks": [{
			      "type": "section",
			      "text": {
			       "type": "mrkdwn",
			       "text": "*Funnel Key Metrics*"
			      },
			      "accessory": {
			       "type": "button",
			       "text": {
			        "type": "plain_text",
			        "text": "Go to Revsure Application"
			       },
			       "value": "click_me_123",
			       "url":
			       "https://dt1.revsure-staging.cloud/app/sales-pipeline-readiness/unified-funnel-and-pipeline",
			       "action_id": "button-action"
			      }
			     }, {
			      "type": "divider"
			     }, {
			      "type": "section",
			      "text": {
			       "type": "mrkdwn",
			       "text": "*Top of the Funnel*"
			      }
			     }, {
			      "type": "section",
			      "text": {
			       "type":
			       "mrkdwn",
			       "text":
			       "- " + "*" + str(lead_name) + "*" + " |  Current Value = " + "*" +
			       str(lead_current_value) + "*" + " | diff = " + "*" + str(lead_diff) +
			       "*" + " ( " + "_" + str(lead_diff_percent) + "_" + " ) " +
			       str(lead_trend_emojy) + "\n" + "- " + "*" + str(mql_name) + "*" +
			       " |  Current Value = " + "*" + str(mql_current_value) + "*" +
			       " | diff = " + "*" + str(mql_diff) + "*" + " ( " + "_" +
			       str(mql_diff_percent) + "_" + " ) " + str(mql_trend_emojy) + "\n" +
			       "- " + "*" + str(sal_name) + "*" + " |  Current Value = " + "*" +
			       str(sal_current_value) + "*" + " | diff = " + "*" + str(sal_diff) +
			       "*" + " ( " + "_" + str(sal_diff_percent) + "_" + " ) " +
			       str(sal_trend_emojy)
			      }
			     }, {
			      "type": "divider"
			     }, {
			      "type": "section",
			      "text": {
			       "type": "mrkdwn",
			       "text": "*Middle of the Funnel*"
			      }
			     }, {
			      "type": "section",
			      "text": {
			       "type":
			       "mrkdwn",
			       "text":
			       "- " + "*" + str(sql_name) + "*" + " |  Current Value = " + "*" +
			       str(sql_current_value) + "*" + " | diff = " + "*" + str(sql_diff) +
			       "*" + " ( " + "_" + str(sql_diff_percent) + "_" + " ) " +
			       str(sql_trend_emojy) + "\n" + "- " + "*" + str(pipeline_name) + "*" +
			       " |  Current Value = " + "*" + str(pipeline_current_value) + "*" +
			       " | diff = " + "*" + str(pipeline_diff) + "*" + " ( " + "_" +
			       str(pipeline_diff_percent) + "_" + " ) " + str(pipeline_trend_emojy)
			      }
			     }, {
			      "type": "divider"
			     }, {
			      "type": "section",
			      "text": {
			       "type": "mrkdwn",
			       "text": "*Bottom of the Funnel*"
			      }
			     }, {
			      "type": "section",
			      "text": {
			       "type":
			       "mrkdwn",
			       "text":
			       "- " + "*" + str(won_name) + "*" + " |  Current Value = " + "*" +
			       str(won_current_value) + "*" + " | diff = " + "*" + str(won_diff) +
			       "*" + " ( " + "_" + str(won_diff_percent) + "_" + " ) " +
			       str(won_trend_emojy)
			      }
			     }]
			    }]
			   }
			  },
			  "platform": "SLACK"
			 }, {
			  "text": {
			   "text": []
			  }
			 }]
			}

	if query_result.get('action') == 'pipeline.generation.headline.metrics':
		api_url = "https://dt1.revsure-staging.cloud/api/v1/projections/performance/generation"
		filters = {
		 "funnelView": "value",
		 "dateGroup": "month",
		 "createdTime": "thisQuarter",
		 "closingTime": "anyTime"
		}
		api_response = requests.post(api_url,
		                             headers=api_request_headers,
		                             json=filters)
		#print(api_response.status_code)

		if api_response.status_code == 200:
			response = api_response.json()
			print(response)

			pg_main_label = response[0]['label']
			pg_trend_label = response[0]['trendLabel']
			pg_generated_pipeline_name = response[0]['cards'][0]['name']
			pg_generated_pipeline_current_value = response[0]['cards'][0][
			 'currentValue']
			pg_seen_projection_name = response[0]['cards'][1]['name']
			pg_seen_projection_current_value = response[0]['cards'][1]['currentValue']
			pg_unseen_projection_name = response[0]['cards'][2]['name']
			pg_unseen_projection_current_value = response[0]['cards'][2]['currentValue']
			pg_total_projection_name = response[0]['cards'][3]['name']
			pg_total_projection_current_value = response[0]['cards'][3]['currentValue']

		api_url = "https://dt1.revsure-staging.cloud/api/v1/projections/generation/winrate"
		filters = {
		 "funnelView": "value",
		 "dateGroup": "month",
		 "createdTime": "thisQuarter",
		 "closingTime": "anyTime",
		 "trendStart": "q0"
		}
		api_response = requests.post(api_url,
		                             headers=api_request_headers,
		                             json=filters)
		#print(api_response.status_code)

		if api_response.status_code == 200:
			response = api_response.json()
			print(response)

			pg_generated_pipeline_winrate = response['winRates'][0]['winRate'].split(
			 "%")[0] + "%"
			pg_seen_projection_winrate = response['winRates'][1]['winRate'].split(
			 "%")[0] + "%"
			pg_unseen_projection_winrate = response['winRates'][2]['winRate'].split(
			 "%")[0] + "%"
			pg_total_projection_winrate = response['winRates'][3]['winRate'].split(
			 "%")[0] + "%"

		fulfillmentText = {
		 "fulfillmentMessages": [{
		  "payload": {
		   "slack": {
		    "text":
		    "Response from dt1.revsure-staging.cloud",
		    "attachments": [{
		     "blocks": [{
		      "type": "section",
		      "text": {
		       "type": "mrkdwn",
		       "text": "*Pipeline Generation Headline Metrics*"
		      },
		      "accessory": {
		       "type": "button",
		       "text": {
		        "type": "plain_text",
		        "text": "Go to Revsure"
		       },
		       "value": "click_me_123",
		       "url":
		       "https://dt1.revsure-staging.cloud/app/sales-pipeline-readiness/pipeline-projections?tab=generation",
		       "action_id": "button-action"
		      }
		     }, {
		      "type": "divider"
		     }, {
		      "type": "section",
		      "text": {
		       "type":
		       "mrkdwn",
		       "text":
		       "*" + str(pg_main_label) + "*"
		      }
		     }, {
		      "type": "section",
		      "text": {
		       "type":
		       "mrkdwn",
		       "text":
		       "- " + "*" + str(pg_generated_pipeline_name) + "*" +
		       " |  Current Value = " + "*" +
		       str(pg_generated_pipeline_current_value) + "*" + " ( " + "_" +
		       str(pg_generated_pipeline_winrate) + "_" + " ) " + "\n" + "- " + "*" +
		       str(pg_seen_projection_name) + "*" + " |  Current Value = " + "*" +
		       str(pg_seen_projection_current_value) + "*" + " ( " + "_" +
		       str(pg_seen_projection_winrate) + "_" + " ) " + "\n" + "- " + "*" +
		       str(pg_unseen_projection_name) + "*" + " |  Current Value = " + "*" +
		       str(pg_unseen_projection_current_value) + "*" + " ( " + "_" +
		       str(pg_unseen_projection_winrate) + "_" + " ) " + "\n" + "- " + "*" +
		       str(pg_total_projection_name) + "*" + " |  Current Value = " + "*" +
		       str(pg_total_projection_current_value) + "*" + " ( " + "_" +
		       str(pg_total_projection_winrate) + "_" + " ) "
		      }
		     }]
		    }]
		   }
		  },
		  "platform": "SLACK"
		 }, {
		  "text": {
		   "text": []
		  }
		 }]
		}

	if query_result.get('action') == 'pipeline.readiness.headline.metrics':
		filters = {
		 "dateFilter": "lastYear",
		 "dateGroup": "quarter",
		 "funnelType": "snapshot"
		}
		api_url = "https://dt1.revsure-staging.cloud/api/v2/section/funnel-performance/funnel"

		# Declaring all variables to be used in the final response

		current_quarter_display_name = ''
		next_quarter_display_name = ''

		# Variables for pipline value current quarter
		current_pipeline_value_current_quarter = ''
		seen_projection_value_current_quarter = ''
		unseen_projection_value_current_quarter = ''
		total_projection_value_current_quarter = ''
		current_pipeline_value_next_quarter = ''
		seen_projection_value_next_quarter = ''
		unseen_projection_value_next_quarter = ''
		total_projection_value_next_quarter = ''

		## Variables for Win Rate value current quarter

		current_pipeline_winrate_value_current_quarter = ''
		seen_projection_winrate_value_current_quarter = ''
		unseen_projection_winrate_value_current_quarter = ''
		total_projection_winrate_value_current_quarter = ''
		current_pipeline_winrate_value_next_quarter = ''
		seen_projection_winrate_value_next_quarter = ''
		unseen_projection_winrate_value_next_quarter = ''
		total_projection_winrate_value_next_quarter = ''

		# Variables for volume current quarter
		current_pipeline_volume_current_quarter = ''
		seen_projection_volume_current_quarter = ''
		unseen_projection_volume_current_quarter = ''
		total_projection_volume_current_quarter = ''
		current_pipeline_volume_next_quarter = ''
		seen_projection_volume_next_quarter = ''
		unseen_projection_volume_next_quarter = ''
		total_projection_volume_next_quarter = ''

		## Variables for winrates volume current quarter

		current_pipeline_winrate_volume_current_quarter = ''
		seen_projection_winrate_volume_current_quarter = ''
		unseen_projection_winrate_volume_current_quarter = ''
		total_projection_winrate_volume_current_quarter = ''
		current_pipeline_winrate_volume_next_quarter = ''
		seen_projection_winrate_volume_next_quarter = ''
		unseen_projection_winrate_volume_next_quarter = ''
		total_projection_winrate_volume_next_quarter = ''

		filters = {
		 "funnelView": "value",
		 "dateGroup": "quarter",
		 "createdTime": "thisQuarter",
		 "closingTime": "thisQuarter"
		}

		api_url = "https://dt1.revsure-staging.cloud/api/v1/projections/performance/pipeline"
		api_response = requests.post(api_url,
		                             headers=api_request_headers,
		                             json=filters)
		print(api_response.status_code)

		if api_response.status_code == 200:
			response = api_response.json()
			#print(response)

			current_quarter_display_name = response[0]['label']
			next_quarter_display_name = response[1]['label']

			current_pipeline_value_current_quarter = response[0]['cards'][0][
			 'currentValue']
			seen_projection_value_current_quarter = response[0]['cards'][1][
			 'currentValue']
			unseen_projection_value_current_quarter = response[0]['cards'][2][
			 'currentValue']
			total_projection_value_current_quarter = response[0]['cards'][3][
			 'currentValue']

			current_pipeline_value_next_quarter = response[1]['cards'][0][
			 'currentValue']
			seen_projection_value_next_quarter = response[1]['cards'][1]['currentValue']
			unseen_projection_value_next_quarter = response[1]['cards'][2][
			 'currentValue']
			total_projection_value_next_quarter = response[1]['cards'][3][
			 'currentValue']
		else:
			print('Could not get response from ' + str(api_url))

			#  'formattedValue']
			#text = 'The total projected value for this qurter is ' + str(total_projection_value_current_quarter)

	#    response = {
	#      "slack": {
	#        "text": "Response from Revsure",
	#        "attachments": []
	#      }
	#    }
	#  else:
	#    text = "Could not get proper api response"

	# Get the projected winrates for pipeline readiness by value for current quarter
		api_url = "https://dt1.revsure-staging.cloud/api/v1/projections/pipeline/winrate"
		filters = {"funnelView": "value", "dateGroup": "quarter", "trendStart": "q0"}
		api_response = requests.post(api_url,
		                             headers=api_request_headers,
		                             json=filters)
		#print(api_response.status_code)

		if api_response.status_code == 200:
			response = api_response.json()
			#print(response)
			current_pipeline_winrate_value_current_quarter = response['winRates'][0][
			 'winRate']
			current_pipeline_winrate_value_current_quarter = current_pipeline_winrate_value_current_quarter.split(
			 "%")[0] + "%"
			seen_projection_winrate_value_current_quarter = response['winRates'][1][
			 'winRate']
			seen_projection_winrate_value_current_quarter = seen_projection_winrate_value_current_quarter.split(
			 "%")[0] + "%"
			unseen_projection_winrate_value_current_quarter = response['winRates'][2][
			 'winRate']
			unseen_projection_winrate_value_current_quarter = unseen_projection_winrate_value_current_quarter.split(
			 "%")[0] + "%"
			total_projection_winrate_value_current_quarter = response['winRates'][3][
			 'winRate']
			total_projection_winrate_value_current_quarter = total_projection_winrate_value_current_quarter.split(
			 "%")[0] + "%"
		else:
			print('Could not get response from ' + str(api_url))

		api_url = "https://dt1.revsure-staging.cloud/api/v1/projections/pipeline/winrate"
		filters = {"funnelView": "value", "dateGroup": "quarter", "trendStart": "q1"}
		api_response = requests.post(api_url,
		                             headers=api_request_headers,
		                             json=filters)
		#print(api_response.status_code)

		if api_response.status_code == 200:
			response = api_response.json()

			current_pipeline_winrate_value_next_quarter = response['winRates'][0][
			 'winRate']
			current_pipeline_winrate_value_next_quarter = current_pipeline_winrate_value_next_quarter.split(
			 "%")[0] + "%"
			seen_projection_winrate_value_next_quarter = response['winRates'][1][
			 'winRate']
			seen_projection_winrate_value_next_quarter = seen_projection_winrate_value_next_quarter.split(
			 "%")[0] + "%"
			unseen_projection_winrate_value_next_quarter = response['winRates'][2][
			 'winRate']
			unseen_projection_winrate_value_next_quarter = unseen_projection_winrate_value_next_quarter.split(
			 "%")[0] + "%"
			total_projection_winrate_value_next_quarter = response['winRates'][3][
			 'winRate']
			total_projection_winrate_value_next_quarter = total_projection_winrate_value_next_quarter.split(
			 "%")[0] + "%"
		else:
			print('Could not get response from ' + str(api_url))

		api_url = "https://dt1.revsure-staging.cloud/api/v1/projections/performance/pipeline"
		filters = {
		 "funnelView": "volume",
		 "dateGroup": "quarter",
		 "createdTime": "thisQuarter",
		 "closingTime": "thisQuarter"
		}
		api_response = requests.post(api_url,
		                             headers=api_request_headers,
		                             json=filters)
		#print(api_response.status_code)
		if api_response.status_code == 200:
			response = api_response.json()
			print(response)
			current_pipeline_volume_current_quarter = response[0]['cards'][0][
			 'currentValue']
			seen_projection_volume_current_quarter = response[0]['cards'][1][
			 'currentValue']
			unseen_projection_volume_current_quarter = response[0]['cards'][2][
			 'currentValue']
			total_projection_volume_current_quarter = response[0]['cards'][3][
			 'currentValue']

			current_pipeline_volume_next_quarter = response[1]['cards'][0][
			 'currentValue']
			seen_projection_volume_next_quarter = response[1]['cards'][1][
			 'currentValue']
			unseen_projection_volume_next_quarter = response[1]['cards'][2][
			 'currentValue']
			total_projection_volume_next_quarter = response[1]['cards'][3][
			 'currentValue']
		else:
			print('Could not get response from ' + str(api_url))

		# Get the projected winrates for pipeline readiness by value for current quarter
		api_url = "https://dt1.revsure-staging.cloud/api/v1/projections/pipeline/winrate"
		filters = {
		 "funnelView": "volume",
		 "dateGroup": "quarter",
		 "trendStart": "q0"
		}
		api_response = requests.post(api_url,
		                             headers=api_request_headers,
		                             json=filters)
		print(api_response.status_code)

		if api_response.status_code == 200:
			response = api_response.json()
			#print(response)
			current_pipeline_winrate_volume_current_quarter = response['winRates'][0][
			 'winRate']
			current_pipeline_winrate_volume_current_quarter = current_pipeline_winrate_volume_current_quarter.split(
			 "%")[0] + "%"
			seen_projection_winrate_volume_current_quarter = response['winRates'][1][
			 'winRate']
			seen_projection_winrate_volume_current_quarter = seen_projection_winrate_volume_current_quarter.split(
			 "%")[0] + "%"
			unseen_projection_winrate_volume_current_quarter = response['winRates'][2][
			 'winRate']
			unseen_projection_winrate_volume_current_quarter = unseen_projection_winrate_volume_current_quarter.split(
			 "%")[0] + "%"
			total_projection_winrate_volume_current_quarter = response['winRates'][3][
			 'winRate']
			total_projection_winrate_volume_current_quarter = total_projection_winrate_volume_current_quarter.split(
			 "%")[0] + "%"
		else:
			print('Could not get response from ' + str(api_url))

		api_url = "https://dt1.revsure-staging.cloud/api/v1/projections/pipeline/winrate"
		filters = {
		 "funnelView": "volume",
		 "dateGroup": "quarter",
		 "trendStart": "q1"
		}
		api_response = requests.post(api_url,
		                             headers=api_request_headers,
		                             json=filters)
		#print(api_response.status_code)

		if api_response.status_code == 200:
			response = api_response.json()

			current_pipeline_winrate_volume_next_quarter = response['winRates'][0][
			 'winRate']
			current_pipeline_winrate_volume_next_quarter = current_pipeline_winrate_volume_next_quarter.split(
			 "%")[0] + "%"
			seen_projection_winrate_volume_next_quarter = response['winRates'][1][
			 'winRate']
			seen_projection_winrate_volume_next_quarter = seen_projection_winrate_volume_next_quarter.split(
			 "%")[0] + "%"
			unseen_projection_winrate_volume_next_quarter = response['winRates'][2][
			 'winRate']
			unseen_projection_winrate_volume_next_quarter = unseen_projection_winrate_volume_next_quarter.split(
			 "%")[0] + "%"
			total_projection_winrate_volume_next_quarter = response['winRates'][3][
			 'winRate']
			total_projection_winrate_volume_next_quarter = total_projection_winrate_volume_next_quarter.split(
			 "%")[0] + "%"

		else:
			print('Could not get response from ' + str(api_url))

		fulfillmentText = {
		 "fulfillmentMessages": [{
		  "payload": {
		   "slack": {
		    "text":
		    "Response from dt1.revsure-staging.cloud",
		    "attachments": [{
		     "blocks": [{
		      "type": "section",
		      "text": {
		       "type": "mrkdwn",
		       "text": "*Pipeline Readiness Key Metrics*"
		      },
		      "accessory": {
		       "type": "button",
		       "text": {
		        "type": "plain_text",
		        "text": "Go to Revsure Application"
		       },
		       "value": "click_me_123",
		       "url":
		       "https://dt1.revsure-staging.cloud/app/sales-pipeline-readiness/pipeline-projections?tab=pipeline",
		       "action_id": "button-action"
		      }
		     }, {
		      "type": "divider"
		     }, {
		      "type": "section",
		      "text": {
		       "type":
		       "mrkdwn",
		       "text":
		       "Pipeline Readiness for Current Quarter - " + "*" +
		       str(current_quarter_display_name) + "*"
		      }
		     }, {
		      "type": "section",
		      "text": {
		       "type":
		       "mrkdwn",
		       "text":
		       "- Current Pipeline |  Value = " + "*" +
		       str(current_pipeline_value_current_quarter) + "*" + " ( " + "_" +
		       str(current_pipeline_winrate_value_current_quarter) + "_" + " ) " +
		       " | Volume = " + "*" + str(current_pipeline_volume_current_quarter) +
		       "*" + " ( " + "_" +
		       str(current_pipeline_winrate_volume_current_quarter) + "_" + " ) " +
		       "\n" + "- Seen Projection | Value = " + "*" +
		       str(seen_projection_value_current_quarter) + "*" + " ( " + "_" +
		       str(seen_projection_winrate_value_current_quarter) + "_" + " ) " +
		       " | Volume = " + "*" + str(seen_projection_volume_current_quarter) +
		       "*" + " ( " + "_" +
		       str(seen_projection_winrate_volume_current_quarter) + "_" + " ) " +
		       "\n" + "- Unseen Projection | Value = " + "*" +
		       str(unseen_projection_value_current_quarter) + "*" + " ( " + "_" +
		       str(unseen_projection_winrate_value_current_quarter) + "_" + " ) "
		       " | Volume = " + "*" + str(unseen_projection_volume_current_quarter) +
		       "*" + " ( " + "_" +
		       str(unseen_projection_winrate_volume_current_quarter) + "_" + " ) "
		       "\n" + "- Total Projection | Value = " + "*" +
		       str(total_projection_value_current_quarter) + "*" + " ( " + "_" +
		       str(total_projection_winrate_value_current_quarter) + "_" + " ) "
		       " | Volume = " + "*" + str(total_projection_volume_current_quarter) +
		       "*" + " ( " + "_" +
		       str(total_projection_winrate_volume_current_quarter) + "_" + " ) "
		      }
		     }, {
		      "type": "section",
		      "text": {
		       "type":
		       "mrkdwn",
		       "text":
		       "Pipeline Readiness for Next Quarter - " + "*" +
		       str(next_quarter_display_name) + "*"
		      }
		     }, {
		      "type": "section",
		      "text": {
		       "type":
		       "mrkdwn",
		       "text":
		       "- Current Pipeline |  Value = " + "*" +
		       str(current_pipeline_value_next_quarter) + "*" + " ( " + "_" +
		       str(current_pipeline_winrate_value_next_quarter) + "_" + " ) " +
		       " | Volume = " + "*" + str(current_pipeline_volume_next_quarter) +
		       "*" + " ( " + "_" +
		       str(current_pipeline_winrate_volume_next_quarter) + "_" + " ) " +
		       "\n" + "- Seen Projection | Value = " + "*" +
		       str(seen_projection_value_next_quarter) + "*" + " ( " + "_" +
		       str(seen_projection_winrate_value_next_quarter) + "_" + " ) " +
		       " | Volume = " + "*" + str(seen_projection_volume_next_quarter) +
		       "*" + " ( " + "_" + str(seen_projection_winrate_volume_next_quarter) +
		       "_" + " ) " + "\n" + "- Unseen Projection | Value = " + "*" +
		       str(unseen_projection_value_next_quarter) + "*" + " ( " + "_" +
		       str(unseen_projection_winrate_value_next_quarter) + "_" + " ) " +
		       " | Volume = " + "*" + str(unseen_projection_volume_next_quarter) +
		       "*" + " ( " + "_" +
		       str(unseen_projection_winrate_volume_next_quarter) + "_" + " ) " +
		       "\n" + "- Total Projection | Value = " + "*" +
		       str(total_projection_value_next_quarter) + "*" + " ( " + "_" +
		       str(total_projection_winrate_value_next_quarter) + "_" + " ) " +
		       " | Volume = " + "*" + str(total_projection_volume_next_quarter) + "*"
		       " ( " + "_" + str(total_projection_winrate_volume_next_quarter) +
		       "_" + " ) "
		      }
		     }]
		    }]
		   }
		  },
		  "platform": "SLACK"
		 }, {
		  "text": {
		   "text": [
		    "- " + "The current pipeline by value for Q1 2023 is " +
		    str(current_pipeline_value_current_quarter),
		    "- " + "The total projection value for Q1 2023 is " +
		    str(total_projection_value_current_quarter)
		   ]
		  }
		 }]
		}

	print(fulfillmentText)
	return fulfillmentText

	#print(response)
	#return response


if __name__ == '__main__':
	app.run(host='0.0.0.0',
	        port=8080)  # This line is required to run Flask on repl.it
