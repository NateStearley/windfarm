import requests
import pandas as pd
import urllib.parse
import time

API_KEY = "pLusKcjyQAq5ifT6GpGCLjYp0dIDEO0B3Xf4TZu4"
EMAIL = "natestearley@gmail.com"
BASE_URL = "https://developer.nrel.gov/api/wind-toolkit/v2/wind/wtk-led-conus-download.json?"
POINTS = ['1552328']

def main():
    input_data = {
        'attributes': 'boundary_layer_height,friction_velocity_2m,inversemoninobukhovlength_2m,latent_heat_flux,precipitation_0m,pressure_0m,pressure_100m,pressure_200m,pressure_500m,relativehumidity_2m,sensible_heat_flux,skin_temperature,temperature_1000m,temperature_100m,temperature_200m,temperature_20m,temperature_2m,temperature_300m,temperature_40m,temperature_500m,temperature_60m,temperature_80m,vertical_windspeed_120m,vertical_windspeed_200m,vertical_windspeed_20m,vertical_windspeed_40m,vertical_windspeed_500m,vertical_windspeed_80m,virtual_potential_temperature_1000m,virtual_potential_temperature_100m,virtual_potential_temperature_200m,virtual_potential_temperature_20m,virtual_potential_temperature_2m,virtual_potential_temperature_300m,virtual_potential_temperature_40m,virtual_potential_temperature_500m,virtual_potential_temperature_60m,virtual_potential_temperature_80m,winddirection_1000m,winddirection_100m,winddirection_10m,winddirection_120m,winddirection_140m,winddirection_160m,winddirection_180m,winddirection_200m,winddirection_20m,winddirection_250m,winddirection_300m,winddirection_40m,winddirection_500m,winddirection_60m,winddirection_80m,windspeed_1000m,windspeed_100m,windspeed_10m,windspeed_120m,windspeed_140m,windspeed_160m,windspeed_180m,windspeed_200m,windspeed_20m,windspeed_250m,windspeed_300m,windspeed_40m,windspeed_500m,windspeed_60m,windspeed_80m',
        'interval': '60',
        
        'api_key': API_KEY,
        'email': EMAIL,
    }
    for name in ['2019','2020']:
        print(f"Processing name: {name}")
        for id, location_ids in enumerate(POINTS):
            input_data['names'] = [name]
            input_data['location_ids'] = location_ids
            print(f'Making request for point group {id + 1} of {len(POINTS)}...')

            if '.csv' in BASE_URL:
                url = BASE_URL + urllib.parse.urlencode(data, True)
                # Note: CSV format is only supported for single point requests
                # Suggest that you might append to a larger data frame
                data = pd.read_csv(url)
                print(f'Response data (you should replace this print statement with your processing): {data}')
                # You can use the following code to write it to a file
                # data.to_csv('SingleBigDataPoint.csv')
            else:
                headers = {
                  'x-api-key': API_KEY
                }
                data = get_response_json_and_handle_errors(requests.post(BASE_URL, input_data, headers=headers))
                download_url = data['outputs']['downloadUrl']
                # You can do with what you will the download url
                print(data['outputs']['message'])
                print(f"Data can be downloaded from this url when ready: {download_url}")

                # Delay for 1 second to prevent rate limiting
                time.sleep(1)
            print(f'Processed')


def get_response_json_and_handle_errors(response: requests.Response) -> dict:
    """Takes the given response and handles any errors, along with providing
    the resulting json

    Parameters
    ----------
    response : requests.Response
        The response object

    Returns
    -------
    dict
        The resulting json
    """
    if response.status_code != 200:
        print(f"An error has occurred with the server or the request. The request response code/status: {response.status_code} {response.reason}")
        print(f"The response body: {response.text}")
        exit(1)

    try:
        response_json = response.json()
    except:
        print(f"The response couldn't be parsed as JSON, likely an issue with the server, here is the text: {response.text}")
        exit(1)

    if len(response_json['errors']) > 0:
        errors = '\n'.join(response_json['errors'])
        print(f"The request errored out, here are the errors: {errors}")
        exit(1)
    return response_json

if __name__ == "__main__":
    main()