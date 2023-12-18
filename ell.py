import cdstoolbox as ct

# Initialise the application
@ct.application(title='Extract time-series at multiple points')

# Define a download output for the application
@ct.output.download()

# Define application function
def application():
    """Define a function that extracts hourly Near Surface Air Temperature in 2018
    for two points and provides a download link.

    Application main steps:

    - retrieve temperature gridded data
    - extract data at given locations using ct.observation.interp_from_grid()
    - return extracted data
    """

    # Retrieve hourly surface temperature
    data = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels',
        {
            'variable': '2m_temperature',
            'product_type': 'reanalysis',
            'year': 2018,
            'month': list(range(1, 13)),
            'day': list(range(1, 32)),
            'time': [
                '00:00', '01:00', '02:00', '03:00',
                '04:00', '05:00', '06:00', '07:00',
                '08:00', '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00', '15:00',
                '16:00', '17:00', '18:00', '19:00',
                '20:00', '21:00', '22:00', '23:00',
            ],
            'grid':['1', '1']
        }
    )

    # Interpolate data for two points
    points = ct.observation.interp_from_grid(data, lat=[10., 65.], lon=[32., 45.])

    print(points)

    return points
