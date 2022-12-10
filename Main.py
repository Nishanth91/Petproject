import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import time
import numpy as np
import os
import emoji
import math
from streamlit_option_menu import option_menu

#from tinydb import TinyDB Disabled data collect functionality
#db = TinyDB ('collected_data.json')

#To set page title
#img= st.image("https://raw.githubusercontent.com/Nishanth91/Petproject/main/img/nish1.jpg")
st. set_page_config(layout="wide",page_title='Canada-perks-nish') 
                    #page_icon=img)

#To remove Streamlit header & Footer
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden; }
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)        


with st.sidebar:
  selected = option_menu(
   menu_title="Main Menu",
   options=["Canada","Regions","Average Income","Tax Calculator","Feedback","About Me"],
   icons=["sunrise","signpost-2","currency-exchange","folder-fill","mailbox","file-earmark-person"],
   menu_icon="shop",
   default_index=0,
  )
  

if selected == "Regions":
  st.header('Canadian Provinces & Territories')
  choice = st.radio("Make a selection,",('Provinces','Territories'))

  if choice == 'Provinces':
      
      tab1 , tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Ontario","Manitoba","Saskatchewan","Alberta","British Columbia","Quebec","PEI","New Brunswick","Nfl & Labrador","Nova Scotia"])

      with tab1:
          st.header("Ontario")
          col1, col2 = st.columns([2,2])
          with col2: 
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_Ontario.svg/1920px-Flag_of_Ontario.svg.png",width=400)
          with col1:  
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Ontario_in_Canada_2.svg/1024px-Ontario_in_Canada_2.svg.png", width=400)
          st.write("Ontario is one of the thirteen provinces and territories of Canada. Located in Central Canada, it is Canada's most populous province, with 38.3 percent of the country's population, and is the second-largest province by total area (after Quebec).Ontario is Canada's fourth-largest jurisdiction in total area when the territories of the Northwest Territories and Nunavut are included. It is home to the nation's capital city, Ottawa, and the nation's most populous city, Toronto, which is Ontario's provincial capital.")
          st.write("Ontario is bordered by the province of Manitoba to the west, Hudson Bay and James Bay to the north, and Quebec to the east and northeast, and to the south by the U.S. states of (from west to east) Minnesota, Michigan, Ohio, Pennsylvania, and New York. Almost all of Ontario's 2,700 km (1,678 mi) border with the United States follows inland waterways: from the westerly Lake of the Woods, eastward along the major rivers and lakes of the Great Lakes/Saint Lawrence River drainage system. There is only about 1 km (0.6 mi) of actual land border, made up of portages including Height of Land Portage on the Minnesota border")
          st.write("The great majority of Ontario's population and arable land is in Southern Ontario. In contrast, Northern Ontario is sparsely populated with cold winters and heavy forestation")
          st.write("Official website: https://www.ontario.ca/") 
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Ont.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top 10 cities in Ontario!")  # add a title
          st.write(df)
      with tab2:
          st.header("Manitoba") 
          col1, col2 = st.columns([2,2])  
          with col2:  
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Flag_of_Manitoba.svg/1920px-Flag_of_Manitoba.svg.png",width=400)
          with col1:  
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Manitoba_in_Canada_2.svg/800px-Manitoba_in_Canada_2.svg.png",width=400)
          """
          Manitoba (/ˌmænɪˈtoʊbə/ (listen) MAN-ih-TOH-bə) is a province of Canada at the longitudinal centre of the country. It is Canada's fifth-most populous province, with a population of 1,342,153 as of 2021, of widely varied landscape, from arctic tundra and the Hudson Bay coastline in the north to dense boreal forest, large freshwater lakes, and prairie grassland in the central and southern regions.

          Indigenous peoples have inhabited what is now Manitoba for thousands of years. In the early 17th century, British and French fur traders began arriving in the area and establishing settlements. The Kingdom of England secured control of the region in 1673 and created a territory named Rupert's Land, which was placed under the administration of the Hudson's Bay Company. Rupert's Land, which included all of present-day Manitoba, grew and evolved from 1673 until 1869 with significant settlements of Indigenous and Métis people in the Red River Colony. In 1869, negotiations with the Government of Canada for the creation of the province of Manitoba commenced. During the negotiations, several factors led to an armed uprising of the Métis people against the Government of Canada, a conflict known as the Red River Rebellion. The resolution of the conflict and further negotiations led to Manitoba becoming the fifth province to join Canadian Confederation, when the Parliament of Canada passed the Manitoba Act on July 15, 1870.

          Manitoba's capital and largest city is Winnipeg, the seventh most populous municipality in Canada. Winnipeg is the seat of government, home to the Legislative Assembly of Manitoba and the Provincial Court. Four of the province's five universities, all four of its professional sports teams, and most of its cultural activities (including Festival du Voyageur and Folklorama) are located in Winnipeg. The city has train and bus stations and an international airport; a Canadian Forces base, CFB Winnipeg, operates from the airport and is the regional headquarters of the North American Aerospace Defense Command. 
          """
          st.write("Official website: https://www.gov.mb.ca/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Mab.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top 10 cities in Manitoba!")  # add a title
          st.write(df)
      with tab3:
          st.header("Saskatchewan")   
          col1, col2 = st.columns([2,2])
          with col2:                        
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Flag_of_Saskatchewan.svg/1920px-Flag_of_Saskatchewan.svg.png",width=400)
          with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Saskatchewan_in_Canada_2.svg/1024px-Saskatchewan_in_Canada_2.svg.png",width=400)
          """
          Saskatchewan (/səˈskætʃəwən, sæ-, -wɒn/ sə-SKATCH-ə-wən; Canadian French: [saskatʃəwan]) is a province in western Canada, bordered on the west by Alberta, on the north by the Northwest Territories, on the east by Manitoba, to the northeast by Nunavut, and on the south by the U.S. states of Montana and North Dakota. Saskatchewan and Alberta are the only landlocked provinces of Canada. In 2022, Saskatchewan's population was estimated at 1,194,803. Nearly 10% of Saskatchewan’s total area of 651,900 square kilometres (251,700 sq mi) is fresh water, mostly rivers, reservoirs and lakes.

          Residents primarily live in the southern prairie half of the province, while the northern half is mostly forested and sparsely populated. Roughly half live in the province's largest city Saskatoon or the provincial capital Regina. Other notable cities include Prince Albert, Moose Jaw, Yorkton, Swift Current, North Battleford, Melfort, and the border city Lloydminster. English is the primary language of the province, with 82.4% of Saskatchewanians speaking English as their first language.

          Saskatchewan has been inhabited for thousands of years by indigenous groups. Europeans first explored the area in 1690 and first settled in the area in 1774. It became a province in 1905, carved out from the vast North-West Territories, which had until then included most of the Canadian Prairies. In the early 20th century, the province became known as a stronghold for Canadian social democracy; North America's first social-democratic government was elected in 1944. The province's economy is based on agriculture, mining, and energy.

          Saskatchewan is presently governed by premier Scott Moe, a member of the Saskatchewan Party which has been in power since 2007.

          In 1992, the federal and provincial governments signed a historic land claim agreement with First Nations in Saskatchewan. The First Nations received compensation which they could use to buy land on the open market for the bands. They have acquired about 3,079 square kilometres (761,000 acres; 1,189 sq mi), new reserve lands under this process. Some First Nations have used their settlement to invest in urban areas, including Regina and Saskatoon.
          """
          st.write("Official website: https://www.saskatchewan.ca/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Sas.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top 10 cities in Saskatchewan!")  # add a title
          st.write(df)
      with tab4:
          st.header("Alberta")  
          col1, col2 = st.columns([2,2])
          with col2:                         
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Flag_of_Alberta.svg/1920px-Flag_of_Alberta.svg.png",width=400)
          with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Alberta_in_Canada_2.svg/1024px-Alberta_in_Canada_2.svg.png",width=400)
          """
          Alberta (/ælˈbɜːrtə/ al-BUR-tə) is one of the thirteen provinces and territories of Canada. It is part of Western Canada and is one of the three prairie provinces. Alberta is bordered by British Columbia to the west, Saskatchewan to the east, the Northwest Territories (NWT) to the north, and the U.S. state of Montana to the south. It is one of the only two landlocked provinces in Canada (Saskatchewan being the other). The eastern part of the province is occupied by the Great Plains, while the western part borders the Rocky Mountains. The province has a predominantly continental climate but experiences quick temperature changes due to air aridity. Seasonal temperature swings are less pronounced in western Alberta due to occasional Chinook winds.

          Alberta is the fourth largest province by area at 661,848 square kilometres (255,541 square miles) and the fourth most populous, being home to 4,262,635 people. Alberta's capital is Edmonton, while Calgary is its largest city. The two are Alberta's largest census metropolitan areas. More than half of Albertans live in either Edmonton or Calgary, which contributes to continuing the rivalry between the two cities. English is the official language of the province. In 2016, 76.0% of Albertans were anglophone, 1.8% were francophone and 22.2% were allophone

          Alberta's economy is based on hydrocarbons, petrochemical industries, livestock and agriculture. The oil and gas industry has been a pillar of Alberta's economy since 1947, when substantial oil deposits were discovered at Leduc No. 1 well. It has also become a part of the province's identity. Since Alberta is the province most rich in hydrocarbons, it provides 70% of the oil and natural gas exploited on Canadian soil. In 2018, Alberta's output was CA$338.2 billion, 15.27% of Canada's GDP.

          In the past, Alberta's political landscape hosted parties like the centre-left Liberals and the agrarian United Farmers of Alberta. Today, Alberta is generally perceived as a conservative province. The right-wing Social Credit Party held office continually from 1935 to 1971 before the centre-right Progressive Conservatives held office continually from 1971 to 2015, the latter being the longest unbroken run in government at the provincial or federal level in Canadian history.

          Before becoming part of Canada, Alberta was home to several First Nations like Plain Indians and Woodland Cree. It was also a territory used by fur traders of the rival companies HBC and NWC. The Dominion of Canada bought the lands that would become Alberta as part of the NWT in 1870. From the late 1800s to early 1900s, many immigrants arrived to prevent the prairies from being annexed by the US. Growing wheat and cattle ranching also became very profitable. In 1905, the Alberta Act was passed, creating the province of Alberta. Massive oil reserves were discovered in 1947. The exploitation of oil sands began in 1967.

          Alberta is renowned for its natural beauty, richness in fossils and for housing important nature reserves. Alberta is home to six UNESCO designated World Heritage Sites: The Canadian Rocky Mountain Parks, Dinosaur Provincial Park, the Head-Smashed-In Buffalo Jump, Waterton-Glacier International Peace Park, Wood Buffalo National Park and Writing-on-Stone Provincial Park. Other popular sites include Banff National Park, Elk Island National Park, Jasper National Park, Waterton Lakes National Park, and Drumheller. 
          """
          st.write("Official website: https://www.alberta.ca/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Alb.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top 10 cities in Alberta!")  # add a title
          st.write(df)
      with tab5:
          st.header("British Columbia")  
          col1, col2 = st.columns([2,2])
          with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Flag_of_British_Columbia.svg/800px-Flag_of_British_Columbia.svg.png",width=400)
          with col1:  
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/British_Columbia_in_Canada_2.svg/1024px-British_Columbia_in_Canada_2.svg.png",width=400)
          """
          British Columbia (BC; French: Colombie-Britannique) is the westernmost province of Canada, situated between the Pacific Ocean and the Rocky Mountains. It has a diverse geography, with rugged landscapes that include rocky coastlines, sandy beaches, forests, lakes, mountains, inland deserts and grassy plains and borders the province of Alberta to the east and the Yukon and Northwest Territories to the north. With an estimated population of 5.3 million as of 2022, it is Canada's third-most populous province. The capital of British Columbia is Victoria and its largest city is Vancouver. Vancouver is the third-largest metropolitan area in Canada; the 2021 census recorded 2.6 million people in Metro Vancouver.

          The first known human inhabitants of the area settled in British Columbia at least 10,000 years ago. Such groups include the Coast Salish, Tsilhqotʼin, and Haida peoples, among many others. One of the earliest British settlements in the area was Fort Victoria, established in 1843, which gave rise to the city of Victoria, the capital of the Colony of Vancouver Island. The Colony of British Columbia (1858–1866) was subsequently founded by Richard Clement Moody and by the Royal Engineers, Columbia Detachment, in response to the Fraser Canyon Gold Rush. Moody selected the site for and founded the mainland colony's capital New Westminster. The colonies of Vancouver Island and British Columbia were incorporated in 1866, subsequent to which Victoria became the united colony's capital. In 1871, British Columbia entered Confederation as the sixth province of Canada, in enactment of the British Columbia Terms of Union.

          British Columbia is a diverse and cosmopolitan province, drawing on a plethora of cultural influences from its British Canadian, European, and Asian diasporas, as well as the Indigenous population. Though the province's ethnic majority originates from the British Isles, many British Columbians also trace their ancestors to continental Europe, East Asia, and South Asia. Indigenous Canadians constitute about 6 percent of the province's total population. Christianity is the largest religion in the region. English is the common language of the province, although Punjabi, Mandarin Chinese, and Cantonese also have a large presence in the Metro Vancouver region. The Franco-Columbian community is an officially recognized linguistic minority, and around one percent of British Columbians claim French as their mother tongue. British Columbia is home to at least 34 distinct Indigenous languages.

          Major sectors of British Columbia's economy include forestry, mining, filmmaking and video production, tourism, real estate, construction, wholesale, and retail. Its main exports include lumber and timber, pulp and paper products, copper, coal, and natural gas. British Columbia exhibits high property values and is a significant centre for maritime trade: the Port of Vancouver is the largest port in Canada and the most diversified port in North America. Although less than 5 percent of the province's territory is arable land, significant agriculture exists in the Fraser Valley and Okanagan due to the warmer climate. British Columbia is home to 45% of all publicly listed companies in Canada. 
          """
          st.write("Official website: https://www2.gov.bc.ca/gov/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Bc.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top 10 cities in British Columbia!")  # add a title
          st.write(df)
      with tab6:
          st.header("Quebec")  
          col1, col2 = st.columns([2,2])
          with col2:                                   
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/1280px-Flag_of_Quebec.svg.png",width=400)
          with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Quebec_in_Canada_2.svg/1024px-Quebec_in_Canada_2.svg.png",width=400)
          """
          Quebec (/k(w)ɪˈbɛk/ k(w)ih-BEK; French: Québec [kebɛk]) is one of the thirteen provinces and territories of Canada. It is the largest province by area and the second-largest by population. Much of the population lives in urban areas along the St. Lawrence River, between the most populous city, Montreal, and the provincial capital, Quebec City. Quebec is the home of the Québécois nation. Located in Central Canada, the province shares land borders with Ontario to the west, Newfoundland and Labrador to the northeast, New Brunswick to the southeast, and a coastal border with Nunavut; in the south it borders Maine, New Hampshire, Vermont, and New York in the United States.

          Between 1534 and 1763, Quebec was called Canada and was the most developed colony in New France. Following the Seven Years' War, Quebec became a British colony: first as the Province of Quebec (1763–1791), then Lower Canada (1791–1841), and lastly Canada East (1841–1867), as a result of the Lower Canada Rebellion. It was confederated with Ontario, Nova Scotia, and New Brunswick in 1867, beginning the Dominion of Canada. Until the early 1960s, the Catholic Church played a large role in the social and cultural institutions in Quebec. However, the Quiet Revolution of the 1960s to 1980s increased the role of the Government of Quebec in l'État québécois (the state of Quebec).

          The Government of Quebec functions within the context of a Westminster system and is both a liberal democracy and a constitutional monarchy. The Premier of Quebec, presently François Legault, acts as head of government. Québécois political culture mostly differs on a nationalist-vs-federalist continuum, rather than a left-vs-right continuum. Independence debates have played a large role in politics. Quebec society's cohesion and specificity is based on three of its unique statutory documents: the Quebec Charter of Human Rights and Freedoms, the Charter of the French Language, and the Civil Code of Quebec. Furthermore, unlike elsewhere in Canada, law in Quebec is mixed: private law is exercised under a civil-law system, while public law is exercised under a common-law system.

          Quebec's official language is French; Québécois French is the regional variety. The economy of Quebec is mainly supported by its large service sector and varied industrial sector. For exports, it leans on the key industries of aeronautics, hydroelectricity, mining, pharmaceuticals, aluminum, wood and paper. Quebec is well known for producing maple syrup, for its comedy, and for making hockey one of the most popular sports in Canada. It is also renowned for its culture; the province produces literature, music, films, TV shows, festivals, folklore, and more. 
          """
          st.write("Official website: https://www.quebec.ca/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Que.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top 10 cities in Quebec!")  # add a title
          st.write(df)  
      with tab7:
          st.header("Prince Edward Island")   
          col1, col2 = st.columns([2,2])
          with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Flag_of_Prince_Edward_Island.svg/1280px-Flag_of_Prince_Edward_Island.svg.png",width=400)
          with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Prince_Edward_Island_in_Canada_%28special_marker%29_2.svg/1024px-Prince_Edward_Island_in_Canada_%28special_marker%29_2.svg.png",width=400)
          """
          Prince Edward Island (PEI; French: Île-du-Prince-Édouard) is one of the thirteen provinces and territories of Canada. It is the smallest province in terms of land area and population, but the most densely populated. The island has several nicknames: "Garden of the Gulf", "Birthplace of Confederation" and "Cradle of Confederation". Its capital and largest city is Charlottetown. It is one of the three Maritime provinces and one of the four Atlantic provinces.

          Part of the traditional lands of the Miꞌkmaq, it was colonized by the French in 1604 as part of the colony of Acadia. The island was ceded to the British at the conclusion of the French and Indian War in 1763 and became part of the colony of Nova Scotia, and in 1769 the island became its own British colony. Prince Edward Island hosted the Charlottetown Conference in 1864 to discuss a union of the Maritime provinces; however, the conference became the first in a series of meetings which led to Canadian Confederation in 1867. Prince Edward Island initially balked at Confederation but, facing bankruptcy from the Land Question and construction of a railroad, joined as Canada's seventh province in 1873.

          According to Statistics Canada, the province of Prince Edward Island had 158,717 residents in 2019. The backbone of the island economy is farming; it produces 25% of Canada's potatoes. Other important industries include the fisheries, tourism, aerospace, bio-science, IT, and renewable energy. As Prince Edward Island is one of Canada's older settlements, its population still reflects some of the earliest settlers, with Canadien, Scottish, Irish, and English surnames being dominant.

          Prince Edward Island is located in the Gulf of St. Lawrence, about 200 kilometres (120 miles) north of Halifax and 600 kilometres (370 miles) east of Quebec City, and has a land area of 5,686.03 km2 (2,195.39 sq mi). The main island is 5,620 km2 (2,170 sq mi) in size. It is the 104th-largest island in the world, Canada's 23rd-largest island, and the only Canadian province consisting solely of an island. 
          """
          st.write("Official website: https://www.princeedwardisland.ca/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Pei.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top 10 cities in Prince Edward Island!")  # add a title
          st.write(df)         
      with tab8:
          st.header("New Brunswick")  
          col1, col2 = st.columns([2,2])
          with col2: 
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Flag_of_New_Brunswick.svg/1280px-Flag_of_New_Brunswick.svg.png",width=400)
          with col1:  
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/New_Brunswick_in_Canada_2.svg/1024px-New_Brunswick_in_Canada_2.svg.png",width=400)
          """
          New Brunswick (French: Nouveau-Brunswick, pronounced [nuvo bʁœnswik], locally [nuvo bʁɔnzwɪk]) is one of the thirteen provinces and territories of Canada. It is one of the three Maritime provinces and one of the four Atlantic provinces. It is the only province with both English and French as its official languages.

          New Brunswick is bordered by Quebec to the north, Nova Scotia to the east, the Gulf of Saint Lawrence to the northeast, the Bay of Fundy to the southeast, and the U.S. state of Maine to the west. New Brunswick is about 83% forested and its northern half is occupied by the Appalachians. The province's climate is continental with snowy winters and temperate summers.

          New Brunswick has a surface area of 72,908 km2 (28,150 sq mi) and 775,610 inhabitants (2021 census). Atypically for Canada, only about half of the population lives in urban areas. New Brunswick's largest cities are Moncton and Saint John, while its capital is Fredericton.

          In 1969, New Brunswick passed the Official Languages Act which began recognizing French as an official language, along with English. New Brunswickers have the right to receive provincial government services in the official language of their choice. About 2⁄3 of the population are anglophone and 1⁄3 are francophone. New Brunswick is home to most of the cultural region of Acadia and most Acadians. New Brunswick's variety of French is called Acadian French and 7 regional accents can be found.

          New Brunswick was first inhabited by First Nations like the Miꞌkmaq and Maliseet. In 1604, Acadia, the first New France colony, was founded with the creation of Port-Royal. For 150 years afterwards, Acadia changed hands a few times due to numerous conflicts between France and the United Kingdom. From 1755 to 1764, the British deported Acadians en masse, an event known as the Great Upheaval. This, along with the Treaty of Paris, solidified Acadia as British property. In 1784, following the arrival of many loyalists fleeing the American Revolution, the colony of New Brunswick was officially created, separating it from what is now Nova Scotia. In the early 1800s, New Brunswick prospered and the population grew rapidly. In 1867, New Brunswick decided to confederate with Nova Scotia and the Province of Canada (now Quebec and Ontario) to form Canada. After Confederation, shipbuilding and lumbering declined, and protectionism disrupted trade with New England.

          From the mid-1900s onwards, New Brunswick was one of the poorest regions of Canada, a fact eventually mitigated by transfer payments. However, the province has seen the highest eastward migration in 45 years in both rural and urban areas, as people living in Ontario and other parts of Canada migrate to the area. As of 2002, the provincial GDP was derived as follows: services (about half being government services and public administration) 43%; construction, manufacturing, and utilities 24%; real estate rental 12%; wholesale and retail 11%; agriculture, forestry, fishing, hunting, mining, oil and gas extraction 5%; transportation and warehousing 5%. A powerful corporate concentration of large companies in New Brunswick, including most newspapers, are owned by the Irving Group of Companies. The province's 2019 output was CA$38.236 billion, which is 1.65% of Canada's GDP.

          Tourism accounts for 9% of the labour force either directly or indirectly. Popular destinations include the Hopewell Rocks, Fundy National Park, Magnetic Hill, Kouchibouguac National Park and Roosevelt Campobello International Park. 
          """
          st.write("Official website: https://www2.gnb.ca/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Nbw.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top 10 cities in New Brunswick!")  # add a title
          st.write(df) 
      with tab9:
          st.header("Newfoundland and Labrador")  
          col1, col2 = st.columns([2,2])
          with col2: 
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Flag_of_Newfoundland_and_Labrador.svg/1920px-Flag_of_Newfoundland_and_Labrador.svg.png",width=400)
          with col1:  
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Newfoundland_and_Labrador_in_Canada_2.svg/1024px-Newfoundland_and_Labrador_in_Canada_2.svg.png",width=400)
          """
          Newfoundland and Labrador (/njuːfənˈlænd  ...  læbrəˈdɔːr/; frequently abbreviated as NL) is the easternmost province of Canada, in the country's Atlantic region. The province comprises the island of Newfoundland and the continental region of Labrador, having a total size of 405,212 square kilometres (156,500 sq mi). In 2021, the population of Newfoundland and Labrador was estimated to be 521,758. The island of Newfoundland (and its smaller neighbouring islands) is home to around 94 per cent of the province's population, with more than half residing in the Avalon Peninsula.

          According to the 2016 census, 97.0 per cent of residents reported English as their native language, making Newfoundland and Labrador Canada's most linguistically homogeneous province despite its association as "the most Irish place outside Ireland."

          St. John's, the capital and largest city of Newfoundland and Labrador, is Canada's 22nd-largest census metropolitan area and it is home to about 40% of the province's population. As the seat of government, St. John's is home to the House of Assembly of Newfoundland and Labrador as well as the jurisdiction's highest court, the Newfoundland and Labrador Court of Appeal.

          Once known as the Dominion of Newfoundland, and before that as the Newfoundland Colony, it surrendered its independence to the British Empire in 1933, following substantial economic suffering caused by the Great Depression and the aftermath of Newfoundland's participation in World War I. On March 31, 1949, it became the 10th and newest province to join the Canadian Confederation as "Newfoundland." On December 6, 2001, the Constitution of Canada was amended to change the province's name to "Newfoundland and Labrador".
          """
          st.write("Official website 1: https://www.gov.nl.ca/")
          st.write("Official website 2 : https://www.newfoundlandlabrador.com/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Nfl.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top 10 cities in Newfoundland and Labrador!")  # add a title
          st.write(df)         
      with tab10:
          st.header("Nova Scotia")  
          col1, col2 = st.columns([2,2])
          with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Nova_Scotia_in_Canada_2.svg/1024px-Nova_Scotia_in_Canada_2.svg.png",width=400)
          with col2:  
            st.image("hhttps://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Nova_Scotia_flag.svg/800px-Nova_Scotia_flag.svg.png",width=400)
            
          """
          Nova Scotia (/ˌnoʊvə ˈskoʊʃə/ NOH-və SKOH-shə; French: Nouvelle-Écosse; Scottish Gaelic: Alba Nuadh) is one of the thirteen provinces and territories of Canada. It is one of the three Maritime provinces and one of the four Atlantic provinces. Nova Scotia is Latin for "New Scotland".

          Most of the population are native English-speakers, and the province's population is 969,383 according to the 2021 Census. It is the most populous of Canada's Atlantic provinces. It is the country's second-most densely populated province and second-smallest province by area, both after Prince Edward Island. Its area of 55,284 square kilometres (21,345 sq mi) includes Cape Breton Island and 3,800 other coastal islands. The Nova Scotia peninsula is connected to the rest of North America by the Isthmus of Chignecto, on which the province's land border with New Brunswick is located. The province borders the Bay of Fundy and Gulf of Maine to the west and the Atlantic Ocean to the south and east, and is separated from Prince Edward Island and the island of Newfoundland by the Northumberland and Cabot straits, respectively.

          The land that comprises what is now Nova Scotia was inhabited by the Miꞌkmaq people at the time of European exploration. In 1605, Acadia—France's first New France colony—was founded with the creation of Acadia's capital, Port-Royal. Britain fought France for the territory on numerous occasions for over a century afterwards. The Fortress of Louisbourg was a key focus point in the battle for control. Subsequent to the Great Upheaval (1755–1763) where the British deported the Acadians en masse, the Conquest of New France (1758–1760) by the British, and the Treaty of Paris (1763), France had to surrender Acadia to the British Empire. During the American Revolutionary War (1775–1783), thousands of Loyalists settled in Nova Scotia. In 1848, Nova Scotia became the first British colony to achieve responsible government, and it federated in July 1867 with New Brunswick and the Province of Canada (now Ontario and Quebec) to form what is now the country of Canada.

          Nova Scotia's capital and largest municipality is Halifax, which is home to over 45% of the province's population as of the 2021 census. Halifax is the thirteenth-largest census metropolitan area in Canada the largest municipality in Atlantic Canada, and Canada's second-largest coastal municipality after Vancouver. 
          """
          st.write("Official website: https://www.novascotia.com/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Ns.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top 10 cities in Newfoundland and Labrador!")  # add a title
          st.write(df)        

  elif choice == 'Territories':
      tab1 , tab2, tab3 = st.tabs(["Nunavut","Northwest Territories","Yukon"])    
      with tab1:
          st.header("Nunavut") 
          col1, col2 = st.columns([2,2])
          with col2:  
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Flag_of_Nunavut.svg/1280px-Flag_of_Nunavut.svg.png",width=400)
          with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Nunavut_in_Canada_2.svg/1024px-Nunavut_in_Canada_2.svg.png",width=450)
          """
          Nunavut (/ˈnʊnəvʊt/ NUU-nə-vuut, /ˈnuːnəvuːt/ NOO-nə-voot; Inuktitut: ᓄᓇᕗᑦ [nunaˈvut], lit. 'our land'; French: [nunavut]) is the largest and northernmost territory of Canada. It was separated officially from the Northwest Territories on April 1, 1999, via the Nunavut Act and the Nunavut Land Claims Agreement Act which provided this territory to the Inuit for independent government. The boundaries had been drawn in 1993. The creation of Nunavut resulted in the first major change to Canada's political map in half a century since the province of Newfoundland was admitted in 1949.

          Nunavut comprises a major portion of Northern Canada and most of the Arctic Archipelago. Its vast territory makes it the fifth-largest country subdivision in the world, as well as North America's second-largest (after Greenland). The capital Iqaluit (formerly Frobisher Bay), on Baffin Island in the east, was chosen by a capital plebiscite in 1995. Other major communities include the regional centres of Rankin Inlet and Cambridge Bay.

          Nunavut also includes Ellesmere Island to the far north, as well as the eastern and southern portions of Victoria Island in the west, and all islands in Hudson, James and Ungava bays, including Akimiski Island far to the southeast of the rest of the territory. It is Canada's only geo-political region that is not connected to the rest of North America by highway.

          Nunavut is the least populous of Canada's provinces and territories. One of the world's most remote, sparsely settled regions, Nunavut has a population of 39,589 (2021 figure, up from 35,944 in 2016) consisting mostly of Inuit. The population occupies a land area of just over 1,877,787 km2 (725,018 sq mi), or slightly smaller than Mexico (excluding water surface area). Nunavut is also home to the world's northernmost permanently inhabited place, Alert. Eureka, a weather station on Ellesmere Island, has the lowest average annual temperature of any Canadian weather station. 
          """
          st.write("Official website: https://www.gov.nu.ca/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Nun.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Top cities in Nunavut!")  # add a title
          st.write(df)
      with tab2:
          st.header("Northwest Territories")  
          col1, col2 = st.columns([2,2]) 
          with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Flag_of_the_Northwest_Territories.svg/1920px-Flag_of_the_Northwest_Territories.svg.png",width=400)
          with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Northwest_Territories_in_Canada_2.svg/1024px-Northwest_Territories_in_Canada_2.svg.png",width=400)
          """
          The Northwest Territories (abbreviated NT or NWT; French: Territoires du Nord-Ouest, formerly North-Western Territory and North-West Territories and namely shortened as Northwest Territory) is a federal territory of Canada. At a land area of approximately 1,144,000 km2 (442,000 sq mi) and a 2016 census population of 41,790, it is the second-largest and the most populous of the three territories in Northern Canada. Its estimated population as of 2022 is 45,605. Yellowknife is the capital, most populous community, and only city in the territory; its population was 19,569 as of the 2016 census. It became the territorial capital in 1967, following recommendations by the Carrothers Commission.

          The Northwest Territories, a portion of the old North-Western Territory, entered the Canadian Confederation on July 15, 1870. Since then, the territory has been divided four times to create new provinces and territories or enlarge existing ones. Its current borders date from April 1, 1999, when the territory's size was decreased again by the creation of a new territory of Nunavut to the east, through the Nunavut Act and the Nunavut Land Claims Agreement. While Nunavut is mostly Arctic tundra, the Northwest Territories has a slightly warmer climate and is both boreal forest (taiga) and tundra, and its most northern regions form part of the Arctic Archipelago.

          The Northwest Territories is bordered by Canada's two other territories, Nunavut to the east and Yukon to the west, and by the provinces of British Columbia, Alberta, and Saskatchewan to the south; it also touches Manitoba to the southeast at a quadripoint that includes Nunavut and Saskatchewan. The land area of the Northwest Territories is vast enough to be roughly equal to France, Portugal and Spain combined, although its overall area is even larger because of its vast lakes that freeze over in winter. 
          """
          st.write("Official website: https://www.gov.nt.ca/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Nwt.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Cities & Towns in Northwest Territories!")  # add a title
          st.write(df)          
      with tab3:
          st.header("Yukon")   
          col1, col2 = st.columns([2,2])
          with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Flag_of_Yukon.svg/1920px-Flag_of_Yukon.svg.png",width=400)
          with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Yukon_in_Canada_2.svg/1024px-Yukon_in_Canada_2.svg.png",width=400)
          """
          The Northwest Territories (abbreviated NT or NWT; French: Territoires du Nord-Ouest, formerly North-Western Territory and North-West Territories and namely shortened as Northwest Territory) is a federal territory of Canada. At a land area of approximately 1,144,000 km2 (442,000 sq mi) and a 2016 census population of 41,790, it is the second-largest and the most populous of the three territories in Northern Canada. Its estimated population as of 2022 is 45,605. Yellowknife is the capital, most populous community, and only city in the territory; its population was 19,569 as of the 2016 census. It became the territorial capital in 1967, following recommendations by the Carrothers Commission.

          The Northwest Territories, a portion of the old North-Western Territory, entered the Canadian Confederation on July 15, 1870. Since then, the territory has been divided four times to create new provinces and territories or enlarge existing ones. Its current borders date from April 1, 1999, when the territory's size was decreased again by the creation of a new territory of Nunavut to the east, through the Nunavut Act and the Nunavut Land Claims Agreement. While Nunavut is mostly Arctic tundra, the Northwest Territories has a slightly warmer climate and is both boreal forest (taiga) and tundra, and its most northern regions form part of the Arctic Archipelago.

          The Northwest Territories is bordered by Canada's two other territories, Nunavut to the east and Yukon to the west, and by the provinces of British Columbia, Alberta, and Saskatchewan to the south; it also touches Manitoba to the southeast at a quadripoint that includes Nunavut and Saskatchewan. The land area of the Northwest Territories is vast enough to be roughly equal to France, Portugal and Spain combined, although its overall area is even larger because of its vast lakes that freeze over in winter. 
          """
          st.write("Official website: https://yukon.ca/")
          url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/Yuk.csv'
          df = pd.read_csv(url,index_col=0)
          st.title("Cities & Towns in Yukon!")  # add a title
          st.write(df)   


if selected == "Canada":
    st.header(f"About Canada") 
    df = pd.DataFrame(
        np.random.randn(1,1) / [50, 50] + [43.66, -79.4],
        columns=['lat', 'lon'])
    st.map(df)
    
    """
    
    Canada is a country in North America popularly referred as the "*__Great White North__*". Its ten provinces and three territories extend from the Atlantic Ocean to the Pacific Ocean and northward into the Arctic Ocean, covering over __9.98 million square kilometres__ (__3.85 million square miles__), making it the world's second-largest country by total area. Its southern and western border with the United States, stretching __8,891 kilometres__ (__5,525 mi__), is the world's longest binational land border. Canada's capital is Ottawa, and its three largest metropolitan areas are Toronto, Montreal, and Vancouver.

    Indigenous peoples have continuously inhabited what is now Canada for thousands of years. Beginning in the 16th century, British and French expeditions explored and later settled along the Atlantic coast. As a consequence of various armed conflicts, France ceded nearly all of its colonies in North America in __1763__. In __1867__, with the union of three British North American colonies through Confederation, Canada was formed as a federal dominion of four provinces. This began an accretion of provinces and territories and a process of increasing autonomy from the United Kingdom. This widening autonomy was highlighted by the *Statute of Westminster 1931* and culminated in the __Canada Act 1982__, which severed the vestiges of legal dependence on the Parliament of the United Kingdom.

    Canada is a parliamentary democracy and a constitutional monarchy in the Westminster tradition. The country's head of government is the prime minister, who holds office by virtue of their ability to command the confidence of the elected House of Commons, and is appointed by the governor general, representing the monarch of Canada, the head of state. The country is a Commonwealth realm and is officially bilingual (__English__ and __French__) at the federal level. It ranks among the highest in international measurements of government transparency, civil liberties, quality of life, economic freedom, education, gender equality and environmental sustainability. It is one of the world's most ethnically diverse and multicultural nations, the product of large-scale immigration. Canada's long and complex relationship with the United States has had a significant impact on its economy and culture.

    A highly developed country, Canada has the 24th highest nominal per capita income globally and the *sixteenth*-highest ranking on the Human Development Index. Its advanced economy is the *eighth*-largest in the world, relying chiefly upon its abundant natural resources and well-developed international trade networks. Canada is part of several major international and intergovernmental institutions or groupings including the *United Nations*, *NATO, the G7, the Group of Ten, the G20, the Organisation for Economic Co-operation and Development (OECD), the World Trade Organization (WTO), the Commonwealth of Nations, the Arctic Council, the Organisation internationale de la Francophonie, the Asia-Pacific Economic Cooperation forum, and the Organization of American States.* 
    """

if selected == "Feedback":
    select = st.radio("Do you like my website?", ('Yes','No','Maybe'), horizontal=True,)
    if select == "Yes":
      st.subheader("\N{grinning face} Thank you. Hope you had fun. Do share it with friends!")
    if select == "No":
      st.subheader("\N{unamused face} Sorry to know! I will try my best to improve this project") 
    if select =="Maybe":
      st.subheader(" 👍 Feel free to write and share your experience & improvements")
    
    st.write("")    
    st.write("")
    st.subheader(":mailbox: *Get In Touch With Me!*")
    contact_form = """
    <form action="https://formsubmit.co/NISHANTH91.DBA@GMAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")
    
if selected == "About Me":
    col1, col2 = st.columns([4,2])

    with col1:
     st.header("Hey there! I'm Nishanth.")
     st.subheader("I'm an Oracle database administrator & Devops admin. Also a newbee in python programming & Devops beginner")    
     st.write("App work in progress, not complete yet")
    with col2:
     st.image("https://raw.githubusercontent.com/Nishanth91/Petproject/main/img/nish.jpg",width=250)


if selected == "Average Income":
    st.header("Average income across Canada")  
    """
    The average household hourly rate in Canada is __36.28 CAD__ and has remained relatively consistent in *__2022__*. That number if multiplied by 8-hour brings the average household daily wage to __290.20 CAD__ or __1,451 CAD__ average household weekly wage. This means that the average household bi-weekly salary is around __2,902 CAD__, the average household monthly salary around __6,287.67 CAD__.
    
    This equates to an annual average household income of a little over __$75,452__. Do keep in mind that factors such as longer or shorter work hours play a big role in how these numbers are calculated. Salary growth is projected to be on the rise, with most Canadian, middle class employees earning more than they did a year ago.
    """
    st.write("")
    url='https://raw.githubusercontent.com/Nishanth91/Petproject/main/csv/NAvg.csv'
    df = pd.read_csv(url,index_col=0)
    st.write(df)
    st.subheader(" Household & Individual income - Provinces")
    df = pd.DataFrame(
        [["Alberta", 61865, 80449], ["British Columbia", 53416,72000],["Manitoba",49661,84130],["NFL",55508,82540],["Nova Scotia",48470,53000],["New Brunswick",49511,59000],["Ontario",55524,80322],["PEI",45912,78000],["Quebec",51735,87080],["Saskatchewan",54371,78000]],
        columns=["Provinces", "Average Individual Income", "Average Household Income"]
    )
    fig = px.bar(df, x="Provinces", y=["Average Household Income", "Average Individual Income"], barmode='group', height=400)
    st.plotly_chart(fig)

    st.subheader("Household income - Cities")
    df2 = pd.DataFrame(
        [["Edmonton", 97800], ["Vancouver", 80000],["Winnipeg",79813],["St.John",59000],["Halifax",55000],["Fredericton",60000],["Toronto",78373],["Charlottetown",78000],["Montreal",82589],["Regina",81000]],
        columns=["Cities", "Average Household Income"]
    )
    fig2 = px.bar(df2, x="Cities", y="Average Household Income", barmode='group', height=400)
    st.plotly_chart(fig2)

    st.subheader("Individual income - Territories")
    df1 = pd.DataFrame(
        [["Yukon", 61812], ["Nunavut", 87355],["Northwest Territories",77670]],
        columns=["Territorries", "Average Individual Income"]
    )
    fig1 = px.bar(df1, x="Territorries", y="Average Individual Income", barmode='group', height=400)
    st.plotly_chart(fig1)
     
if selected == "Tax Calculator":
  st.markdown("<h1 style='text-align: center; color: red;'>Income Tax calculator - Canada</h1>", unsafe_allow_html=True)
  #st.title("Income Tax calculator - Canada")
  
  Province = st.selectbox('Select a Province or Territorry that you work for: ', ('Choose from dropdown ▼','Ontario','Manitoba','Saskatchewan','Alberta','British Columbia','Quebec','Newfoundland & Labrador','New Brunswick','Prince Edward Island','Nova Scotia','Yukon','Northwest Territories','Nunavut'))
  Inc = st.number_input("Enter your annual gross income in CAD: ")
  Pay=  st.selectbox('How are you getting paid?',('Select ▼','Monthly','Bi-weekly','Semi-monthly'))
  time.sleep(0.1)

  #Pension & Employee Insurance contribution
  if Inc < 65000:
      CPP=(Inc * 5.26)/100
      EI=(Inc * 1.46)/100
  else:
      CPP=3500 # max CCP per year 2022
      EI=953 # max Employee contribution per year 2022
      
  #Federal tax calculation
  #source - https://www.wealthsimple.com/en-ca/learn/tax-brackets-canada#how_to_identify_your_tax_bracket
  if Inc <= 50197:
      Fed= Inc * 0.15
  elif  Inc > 50197 and Inc <= 100392:
      Fed=((Inc - 50197) * 0.205) + 7530
  elif Inc > 100392 and Inc <= 155625:
      Fed=((Inc - 100392) * 0.26) + 17820
  elif Inc > 155625 and Inc <= 221708:
      Fed=((Inc - 155625) * 0.29) + 32180
  elif Inc > 221708:
      Fed=((Inc - 221708) * 0.33) + 51344

  #Provincial tax calculation
  #source - https://www.moneysense.ca/save/taxes/tax-brackets-in-canada/
  if Province == 'Ontario':
      if Inc <= 46626:
          Tx= Inc * 0.0505
      elif  Inc > 46226 and Inc <= 92454:
          Tx= ((Inc - 46626) * 0.0915) + 2334
      elif Inc > 92454 and Inc <= 150000:
          Tx= ((Inc- 92454)* 0.1116) + 6564
      elif Inc > 150000 and Inc <= 220000:
          Tx= ((Inc- 150000)* 0.1216) + 13006
      elif Inc > 220000:
          Tx=((Inc - 220000) * 0.1316) + 21518
  #Surtax only for Ontario - https://www.moneysense.ca/save/taxes/tax-brackets-in-canada/#surtax
      if Tx > 4991 and Tx <= 6387: 
          Surt = Tx * 0.2
          Stt = Tx + Surt
      elif Tx > 6387:
          Surt = ((Tx - 6387) * 0.36) + 1227  
          Stt = Tx + Surt       

  if Province == 'Alberta':
      if Inc <= 131220:
          Stt= Inc * 0.1
      elif  Inc > 131220 and Inc <= 157464:
          Stt= ((Inc- 131220)* 0.12) + 13122
      elif Inc > 157464 and Inc <= 209952:
          Stt= ((Inc- 157464)* 0.13) + 16271
      elif Inc > 209952 and Inc <= 314928:
          Stt= ((Inc- 209952)* 0.14) + 23094
      elif Inc > 314928:
          Stt=((Inc - 314928) * 0.15) + 37792
          
  if Province == 'British Columbia':
      if Inc <= 43070:
          Stt= Inc * 0.0506
      elif  Inc > 43070 and Inc <= 86141:
          Stt= ((Inc- 43070)* 0.077) + 2179
      elif Inc > 86141 and Inc <= 98901:
          Stt= ((Inc- 86141)* 0.105) + 5495
      elif Inc > 98901 and Inc <= 120094:
          Stt= ((Inc- 98901)* 0.1229) + 6835
      elif Inc > 120094 and Inc <= 162832:
          Stt= ((Inc- 120094)* 0.147) + 9440
      elif Inc > 162832 and Inc <= 227091:
          Stt= ((Inc- 209952)* 0.168) + 15722
      elif Inc > 227091:
          Stt=((Inc - 314928) * 0.205) + 26518        

  if Province == 'Manitoba':
      if Inc <= 34431:
          Stt= Inc * 0.108
      elif  Inc > 34431 and Inc <= 74416:
          Stt= ((Inc- 34431)* 0.1275) + 3719
      elif Inc > 74416:
          Stt=((Inc - 74416) * 0.174) + 8817
          
  if Province == 'New Brunswick':
      if Inc <= 44887:
          Stt= Inc * 0.094
      elif  Inc > 44887 and Inc <= 89775:
          Stt= ((Inc- 44887)* 0.1482) + 4219
      elif Inc > 89775 and Inc <= 145955:
          Stt= ((Inc- 89775)* 0.1652) + 10871
      elif Inc > 145955 and Inc <= 166280:
          Stt= ((Inc- 209952)* 0.1784) + 20152
      elif Inc > 166280:
          Stt=((Inc - 166280) * 0.203) + 23778
          
  if Province == 'Newfoundland & Labrador':
      if Inc <= 39147:
          Stt= Inc * 0.087
      elif  Inc > 39147 and Inc <= 78294:
          Stt= ((Inc- 39147)* 0.145) + 3406
      elif Inc > 78294 and Inc <= 139780:
          Stt= ((Inc- 78294)* 0.158) + 9082
      elif Inc > 139780 and Inc <= 195693:
          Stt= ((Inc- 139780)* 0.178) + 18797
      elif Inc > 195693 and Inc <= 250000:
          Stt= ((Inc- 195693)* 0.198) + 28750
      elif Inc > 250000 and Inc <= 500000:
          Stt= ((Inc- 250000)* 0.208) + 39503
      elif Inc > 500000 and Inc <= 1000000:
          Stt= ((Inc- 500000)* 0.213) + 91503
      elif Inc > 1000000:
          Stt=((Inc - 1000000) * 0.218) + 158500
          
  if Province == 'Northwest Territories':
      if Inc <= 45462:
          Stt= Inc * 0.059
      elif  Inc > 45462 and Inc <= 90927:
          Stt= ((Inc- 45462)* 0.086) + 2682
      elif Inc > 90927 and Inc <= 147826:
          Stt= ((Inc- 90927)* 0.122) + 6592
      elif Inc > 147826:
          Stt=((Inc - 147826) * 0.1405) + 13534

  if Province == 'Nunavut':
      if Inc <= 29590:
          Stt= Inc * 0.0879
      elif  Inc > 29590 and Inc <= 59180:
          Stt= ((Inc- 29590)* 0.1495) + 2601
      elif Inc > 59180 and Inc <= 93000:
          Stt= ((Inc- 59180)* 0.1667) + 7025
      elif Inc > 150000:
          Stt=((Inc - 150000) * 0.21) + 22638
          
  if Province == 'Nova Scotia':
      if Inc <= 47862:
          Stt= Inc * 0.04
      elif  Inc > 47862 and Inc <= 95724:
          Stt= ((Inc- 47862)* 0.07) + 1914
      elif Inc > 95724 and Inc <= 155625:
          Stt= ((Inc- 95724)* 0.09) + 5264
      elif Inc > 155625:
          Stt=((Inc - 155625) * 0.115) + 10655
          
  if Province == 'Prince Edward island':
      if Inc <= 31984:
          Tx1= Inc * 0.098
      elif  Inc > 31984 and Inc <= 63969:
          Tx1= ((Inc- 31984)* 0.138) + 3134
      elif Inc > 63969:
          Tx1=((Inc - 63969) * 0.167) + 7548
      if Tx1 > 12500:
          Surt = Tx1 * 0.1
          Stt = Tx1 + Surt     
              
          
  if Province == 'Quebec':
      if Inc <= 46295:
          Stt= Inc * 0.15
      elif  Inc > 46295 and Inc <= 92580:
          Stt= ((Inc- 46295)* 0.2) + 6944
      elif Inc > 92580 and Inc <= 112655:
          Stt= ((Inc- 92580)* 0.24) + 16201
      elif Inc > 112655:
          Stt=((Inc - 112655) * 0.2575) + 21019
          
  if Province == 'Saskatchewan':
      if Inc <= 46773:
          Stt= Inc * 0.105
      elif  Inc > 46773 and Inc <= 133638:
          Stt= ((Inc- 46773)* 0.125) + 4911
      elif Inc > 133638:
          Stt=((Inc - 133638) * 0.145) + 15769
          
  if Province == 'Yukon':
      if Inc <= 50197:
          Stt= Inc * 0.064
      elif  Inc > 50197 and Inc <= 100392:
          Stt= ((Inc- 50197)* 0.09) + 3213
      elif Inc > 100392 and Inc <= 155625:
          Stt= ((Inc- 100392)* 0.109) + 7731
      elif Inc > 155625 and Inc <= 500000:
          Stt= ((Inc- 155625)* 0.128) + 13751
      elif Inc > 500000:
          Stt=((Inc - 500000) * 0.15) + 57831
          
  if Province =='Select ▼':
      st.subheader("Select a Province or Territory to calculate taxes")

  if Inc and Province:
      st.subheader (f"*__Approx Tax calculation for {Province} - 2022__*",)
      Deductions = Stt + CPP + EI + Fed
      Inhand= Inc - Deductions
      Monthly= Inhand/12
      col1, col2 = st.columns([4,4])
      with col1:
          st.write("Gross pay")                
          st.write("Canada Pension plan")      
          st.write("Employee Insurance")       
          st.write("Federal Tax")              
          st.write("Provincial Tax")   
          st.write("Net Pay")                  
          st.write("Total deductions") 
          if Pay == 'Monthly':
              st.write("Monthly pay after Taxes")  
          elif Pay == 'Bi-weekly':
              st.write("Bi Weekly pay after Taxes")
          elif Pay == 'Semi-monthly':
              st.write("Semi Monthly pay after Taxes")
      with col2:
          st.write(f"__💰{Inc:,.0f}__")
          st.write(f"__${CPP:,}__")
          st.write(f"__${EI:,}__")
          st.write(f"__${Fed:,.2f}__")
          st.write(f"__${Stt:,.2f}__")
          st.write(f"__${Inhand:,.2f}__")
          st.write(f" __${Deductions:,.2f}__")
          if Pay == 'Monthly':
              st.write(f"__${Monthly:,.2f}__")
          elif Pay == 'Bi-weekly':
              sal = Inhand/26
              st.write(f"__${sal:,.2f}__")
          elif Pay == 'Semi-monthly':
              sal = Inhand/24
              st.write(f"__${sal:,.2f}__")  
  
      labels = 'EI', 'Provincial Tax', 'Net Pay', 'CPP','Federal tax'
      sizes = [EI, Stt, Inhand, CPP, Fed]
      explode = (0, 0, 0.1, 0, 0) 
      fig1, ax1 = plt.subplots()
      ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
      ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
      st.pyplot(fig1)



  