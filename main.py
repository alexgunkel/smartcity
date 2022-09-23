import plotly.express as px
import pandas as pd

categories = dict(
    Gesamt=dict(
        # Gesamt=["Verwaltung", "IT und Kommunikation", "Energie und Umwelt", "Mobilität", "Gesellschaft"],
        dresden=dict(
            y2021=[75.29, 67.18, 47.15, 76.48, 91.34],
            y2022=[]
        ),
        leipzig=dict(
            y2021=[62.62, 56.33, 45.22, 67.71, 90.48],
            y2022=[]
        ),
        chemnitz=dict(
            y2021=[43.07, 41.36, 41.79, 30.19, 82.41],
            y2022=[]
        )
    ),
    Verwaltung=dict(
        # Verwaltung=["Interne Prozesse", "Payment", "Online-Terminvergabe", "Online-Dienstleistungen",
        #             "Webseite und Social Media", "Bevölkerungsanliegen", "Serviceportal", "Weitere Pilotprojekte"],
        dresden=dict(
            y2021=[75.00, 96.30, 63.27, 27.18, 87.50, 83.97, 85.19, 35.00],
            y2022=[]
        ),
        leipzig=dict(
            y2021=[75.00, 37.04, 100.00, 15.53, 51.97, 83.33, 74.07, 23.33],
            y2022=[]
        ),
        chemnitz=dict(
            y2021=[87.50, 18.52, 38.78, 34.95, 76.57, 29.49, 7.41, 23.33],
            y2022=[]
        )
    ),
    IT_und_Kommunikation=dict(
        # IT_und_Kommunikation=["Breitband", "Glasfaser", "Mobilfunk", "Public WLAN", "IoT Netzwerk", "Datenplattform",
        #                       "Weitere Pilotprojekte"],
        dresden=dict(
            y2021=[71.43, 13.48, 81.25, 100.00, 62.09, 75.00, 20.00],
            y2022=[]
        ),
        leipzig=dict(
            y2021=[71.43, 11.24, 64.58, 92.59, 40.02, 75.00, 0.00],
            y2022=[]
        ),
        chemnitz=dict(
            y2021=[71.43, 80.90, 41.67, 18.52, 10.53, 37.50, 0.00],
            y2022=[]
        )
    ),
    Energie_und_Umwelt=dict(
        # Energie_und_Umwelt=["Intelligente Straßenbeleuchtung", "Energielösungen", "Smart Waste", "Anteil E-Fahrzeuge",
        #                     "Ladeinfrastruktur", "Emissionsarme Busse", "Weitere Pilotprojekte"],
        dresden=dict(
            y2021=[75.00, 57.64, 0.00, 17.50, 80.23, 36.67, 30.00],
            y2022=[]
        ),
        leipzig=dict(
            y2021=[37.50, 70.24, 0.00, 31.20, 45.94, 70.00, 30.00],
            y2022=[]
        ),
        chemnitz=dict(
            y2021=[12.50, 84.65, 0.00, 12.50, 83.61, 70.00, 0.00],
            y2022=[]
        )
    ),
    Mobilität=dict(
        # Mobilität=["Parken", "Smartes Verkehrsmanagement", "Smarter ÖPNV", "Sharing-Angebote", "Multimodalität",
        #            "Letzte Meile Logistik", "Weitere Pilotprojekte"],
        dresden=dict(
            y2021=[100.00, 100.00, 86.36, 57.59, 87.88, 20.00, 30.00],
            y2022=[]
        ),
        leipzig=dict(
            y2021=[87.50, 37.50, 81.82, 71.87, 87.88, 40.00, 20.00],
            y2022=[]
        ),
        chemnitz=dict(
            y2021=[50.00, 12.50, 54.55, 53.13, 0.00, 0.00, 20.00],
            y2022=[]
        )
    ),
    Gesellschaft=dict(
        # Gesellschaft=["Öffentlichkeitsbeteiligung", "FabLabs und CoWorking", "Digital-Szene", "Open-Data-Plattform",
        #               "Geo-Datenplattform", "Lokaler Handel und Startup-Hubs", "Weitere Pilotprojekte"]
        dresden=dict(
            y2021=[94.87, 75.00, 100.00, 88.89, 96.67, 100.00, 20.00],
            y2022=[]
        ),
        leipzig=dict(
            y2021=[66.67, 100.00, 93.33, 100.00, 100.00, 100.00, 10.00],
            y2022=[]
        ),
        chemnitz=dict(
            y2021=[83.33, 62.50, 93.33, 83.33, 96.67, 100.00, 0.00],
            y2022=[]
        )
    ),
)
headings = dict(
    Gesamt=["Verwaltung", "IT und Kommunikation", "Energie und Umwelt", "Mobilität", "Gesellschaft"],
    Verwaltung=["Interne Prozesse", "Payment", "Online-Terminvergabe", "Online-Dienstleistungen",
                "Webseite und Social Media", "Bevölkerungsanliegen", "Serviceportal", "Weitere Pilotprojekte"],
    IT_und_Kommunikation=["Breitband", "Glasfaser", "Mobilfunk", "Public WLAN", "IoT Netzwerk", "Datenplattform",
                          "Weitere Pilotprojekte"],
    Energie_und_Umwelt=["Intelligente Straßenbeleuchtung", "Energielösungen", "Smart Waste", "Anteil E-Fahrzeuge",
                        "Ladeinfrastruktur", "Emissionsarme Busse", "Weitere Pilotprojekte"],
    Mobilität=["Parken", "Smartes Verkehrsmanagement", "Smarter ÖPNV", "Sharing-Angebote", "Multimodalität",
               "Letzte Meile Logistik", "Weitere Pilotprojekte"],
    Gesellschaft=["Öffentlichkeitsbeteiligung", "FabLabs und CoWorking", "Digital-Szene", "Open-Data-Plattform",
                  "Geo-Datenplattform", "Lokaler Handel und Startup-Hubs", "Weitere Pilotprojekte"]
)

idx = 0

for category in categories:
    for city in categories[category]:
        idx = idx + 1
        df = pd.DataFrame(dict(
            r=categories[category][city]["y2021"]
        ))
        fig = px.line_polar(df, r='r', theta=headings[category], line_close=True, range_r=[0, 100])
        fig.write_image('./build/' + str(idx) + '_' + category + '_' + city + '.jpg')
