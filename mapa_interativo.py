import folium
from geopy.geocoders import Nominatim

# Função para obter as coordenadas a partir do endereço com CEP
def obter_coordenadas(endereco):
    geolocator = Nominatim(user_agent="seu_app")
    location = geolocator.geocode(endereco)
    if location:
        return [location.latitude, location.longitude]
    else:
        return None

# Coordenadas para os hidrantes
coordenadas_hidrante1 = [-10.976132141370861, -37.04019434920116]
coordenadas_hidrante2 = [-10.96809443275006, -37.040378833587376]

# Coordenadas para a polilinha verde
coordenada_inicio = (-10.969013323607975, -37.035995622922506)
coordenada_fim = (-10.967622987765827, -37.04159607522356)
# Coordenadas para as outras polilinhas
coordenadas_polilinhas = [
    [(-10.97044242898231, -37.036187099031146), (-10.969226075165793, -37.04185634652291)],
    [(-10.971760014119607, -37.0371237347742), (-10.970642847850792, -37.0421687124545)],
    [(-10.973035420684011, -37.03799233349632), (-10.97207694532363, -37.04245552919985)],
    [(-10.974380218759768, -37.03886752612216), (-10.973536013014643, -37.0427673488265)],
    [(-10.975658028751717, -37.03986011047044), (-10.974928539023296, -37.04314607186862)],
    [(-10.977003751622256, -37.04071523874908), (-10.976422749327975, -37.04343778260043)],
    [(-10.97831636764081, -37.04159567407577), (-10.977795910924526, -37.043753808927804)],
    [(-10.979578735694487, -37.04249792064486), (-10.979230295494828, -37.04408777777479)],
    [(-10.980991785225802, -37.043503734120044), (-10.980739994485763, -37.044519093802144)],
    [(-10.98233191980575, -37.0444298267704), (-10.982209036121342, -37.04485087377785)],
    [(-10.983617100898904, -37.04533635981469), (-10.98347249747134, -37.04586649724244), (-10.982050895809136, -37.045525199126175)],
    [(-10.984926476367097, -37.046183058079805), (-10.983514275548531, -37.045857708478366)],
    [(-10.982184885289625, -37.04483050706267), (-10.967805835417701, -37.04152177836711)],
    [(-10.997231265167077, -37.0556548074778), (-10.988394865916408, -37.049479230408465)],
    [(-10.982208745912992, -37.04485501338347), (-10.982056638605437, -37.04551197962649)],
    [(-10.984920681303048, -37.04622950118364), (-10.984775972960282, -37.04700339965255)],

    [(-10.989625450134943, -37.04946802735592), (-10.98923150788465, -37.0500569498383)],
    [(-10.990285430141801, -37.049942292379946), (-10.989881256522361, -37.05052079145557)],
    [(-10.99146213501766, -37.05088039901587), (-10.991114240158423, -37.0513859342441)],
    [(-10.992715576352895, -37.05174554179622), (-10.992383031217983, -37.05228234724478)],
    [(-10.99394343210074, -37.0526575899146), (-10.993605772289563, -37.05312143151578)],
    [(-10.99637354816024, -37.05446083931941), (-10.996122863433472, -37.054846505369824)],
    [(-10.997555344715646, -37.05530513526761), (-10.997279081010046, -37.05566995450449)],
    

    [(-10.986801834198491, -37.04744455246613), (-10.986362387160737, -37.04801659647231), (-10.984775678441848, -37.04701244376948)],
    [(-10.988024632123782, -37.04824822140336), (-10.98773881919962, -37.04898276320556), (-10.986371808624735, -37.048037415969944)],
    [(-10.988475187203699, -37.04865741346479), (-10.98821960359452, -37.04931045231707), (-10.987735698291102, -37.048982425614476)]
]
# Coordenadas para a última polilinha pontilhada vermelha e branca
coordenadas_polilinha_pontilhada = [
    [(-10.997047697422264, -37.05470294848087), (-10.99225125181562, -37.051165228719846)],
    [(-10.99108478227558, -37.05033135613324), (-10.983511126762362, -37.044992674907135)],
    [(-10.982344622692162, -37.04421091938616), (-10.979455258494378, -37.04204566149381)],
    [(-10.978247807793135, -37.041263905974404), (-10.97299889274109, -37.037587456511226)],
    [(-10.971556059400497, -37.03661807968181), (-10.969161554452684, -37.03564870284287)]
]

# Coordenadas reais para a orla de Aracaju
coordenadas_aracaju = obter_coordenadas("Orla de Aracaju, SE, Brasil")

# Criar um mapa centrado nas coordenadas da orla de Aracaju
mapa = folium.Map(location=coordenadas_aracaju, zoom_start=14)

# Adicionar ícones para representar os hidrantes
folium.Marker(location=coordenadas_hidrante1, popup='Hidrante 1', icon=folium.CustomIcon(icon_image="D:\desal\Mapa Interativo\IMG\hidrante.png", icon_size=(30, 30))).add_to(mapa)
folium.Marker(location=coordenadas_hidrante2, popup='Hidrante 2', icon=folium.CustomIcon(icon_image="D:\desal\Mapa Interativo\IMG\hidrante.png", icon_size=(30, 30))).add_to(mapa)


# Adicionar polilinha verde conectando as coordenadas de início e fim
folium.PolyLine(locations=[coordenada_inicio, coordenada_fim], color='green', weight=5, opacity=0.7).add_to(mapa)
# Adicionar outras polilinhas
for coordenadas_polilinha in coordenadas_polilinhas:
    folium.PolyLine(locations=coordenadas_polilinha, color='green', weight=5, opacity=0.7).add_to(mapa)
# Adicionar polilinha pontilhada vermelha e branca
for coordenadas_segmento in coordenadas_polilinha_pontilhada:
    folium.PolyLine(
        locations=coordenadas_segmento,
        color='red',
        weight=5,
        opacity=0.7,
        dash_array='10, 5'  # Configuração para tornar a linha pontilhada
    ).add_to(mapa)
# Exibir o mapa
mapa

# Salvar o mapa como um arquivo HTML
mapa.save("mapa_interativo.html")
