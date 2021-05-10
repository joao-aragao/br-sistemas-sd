import folium
import psycopg2
import pandas as pd
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap


# Create your views here.


@login_required
def index(request):
    con = psycopg2.connect(host='vmi216992.contaboserver.net', database='dbi3perform',
                           user='puk', password='Ym3.1GsP')
    cur = con.cursor()

    sql = """
        select
        cliente.id as id,
        razao as nome,
        latitude,
        longitude,
        round(sum(vl),2)::numeric as valor
        from perform.venda_dados
        join perform.cliente on parceiro_id=cliente.id
        where latitude is not null and latitude<>'erro' and latitude<>'2.8241392'
        group by cliente.id,nome,latitude,longitude
        limit 100
    """
    cur.execute(sql)
    recset = cur.fetchall()
    # print("Total rows are:  ", len(recset))

    dados = pd.DataFrame.from_records(recset, columns=[
                                      'id', 'nome', 'latitude', 'longitude', 'valor'], coerce_float=True)
    dados.info()
    dados.rename(columns={'id': 'Id', 'nome': 'Nome', 'latitude': 'Lat',
                          'longitude': 'Lng', 'valor': 'Valor'}, inplace=True)
    # dados.head()

    lat = dados.Lat.tolist()
    lng = dados.Lng.tolist()

    # gerando mapa de markerCluster
    marker = folium.Map(
        location=[-15.783490, -47.891856],
        tiles='Stamen Terrain',
        zoom_start=5
    )

    # gerando mapa 
    heat = folium.Map(
        location=[-15.783490, -47.891856],
        tiles='Stamen Terrain',
        zoom_start=5
    )

    # adicionando mapa de calor 
    HeatMap(list(zip(lat, lng))).add_to(heat)


    mc = MarkerCluster()

    for index, row in dados.iterrows():
        mc.add_child(folium.Marker([row['Lat'], row['Lng']],
                                   popup=(str(row['Nome'])),
                                   tooltip=row['Nome'],
                                   icon=folium.Icon(icon='book'))).add_to(marker)


    # adicionando filtros do mapa
    folium.TileLayer(tiles='openstreetmap').add_to(marker)
    folium.LayerControl(collapsed=True).add_to(marker)


    # passando mapa para ser exibido em HTML
    marker = marker._repr_html_()  # updated
    heat = heat._repr_html_()  # updated


    context = {'mc_map': marker, 'heat_map': heat}

    return render(request, 'app/index.html', context)
