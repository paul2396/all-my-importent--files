class County:
    def __init__(self, name, population, region, major_towns, famous_for, reference):
        self.name = name
        self.full_name = name 
        self.population = int(population.replace(",", ""))  # Convert population to an integer
        self.region = region
        self.major_towns = major_towns
        self.famous_for = famous_for
        self.reference = reference


# Create instances of the County class

Bedfordshire = County("Bedfordshire", "911,403", "East", ["Bedford", "Dunstable"],
                     ["Bedford Castle", "Woburn Abbey"],
                     "https://www.bing.com/search?q=what+is+Bedfordshire+famous+for")
#!========================================================================================

Berkshire = County("Berkshire", "911,403", "South East", ["Newbury", "Ascot"],
                   ["Ascot Racecourse", "Royal seat at Windsor Castle, Quaint villages"],
                   "https://www.bing.com/search?q=what+is+Berkshire+famous+for")

#!====================================================================================================

Bristol = County("Bristol", "472,500", "South West", ["Kingswood", "Clifton Suspension Bridge", "Victoria rooms"],
                ["Greater Bristol"],
                "https://en.wikipedia.org/wiki/Greater_Bristol")

#!===========================================================================================

Buckinghamshire = County("Buckinghamshire", "808,666", "South East", ["Milton Keynes", "Aylesbury"],
                        ["Bletchley Park in Milton Keynes is the site of World War II British codebreaking",
                         "Chiltern Open Air Museum"],
                        "https://www.bing.com/search?q=what+is+Buckinghamshire+famous+for")
#!==========================================================================================================

Cambridgeshire = County("Cambridgeshire", "145,700", "East", ["Cambridge", "Chatteris"],
                        ["The home of the University of Cambridge", "The Norman Cathedral at Ely"],
                        "https://www.bing.com/search?q=what+is+Cambridgeshire+famous+for")
#!=======================================================================================================

Cheshire = County("Cheshire", "1059,271", "North West", ["Chester", "Warrington"],
                  ["Cheshire cheese", "White plaster and black timber-frame houses."],
                  "https://www.bing.com/search?q=what+is+Cheshire+famous+for")
#!==================================================================================================

Cornwall = County("Cornwall", "568,210", "South West England", ["Penzance", "Newquay"],
                  ["Stunning Coastline", "beautiful beaches"],
                  "https://www.bing.com/search?q=what+is+Cornwall+famous+for")
#!=================================================================================================



Cumbria = County("Cumbria", "498,000", "North West England", ["Kendal", "Penrith"],
                ["Lake District National Park: picturesque lakes, rugged mountains, and charming villages"],
                "https://en.wikipedia.org/wiki/Cumbria")
#

#!===========================================================================================================

Derbyshire = County("Derbyshire", "1,087,900", "East Midlands", ["Derby", "Chesterfield"],
                    ["Peak District National Park", "historical towns and villages"],
                    "https://en.wikipedia.org/wiki/Derbyshire")
#!
#!========================================================================================================

Devon = County("Devon", "1,194,166", "South West", ["Exeter", "Torquay"],
               ["Dartmoor National Park", "Spectacular Coastline"],
               "https://en.wikipedia.org/wiki/Devon#Cities,_towns_and_villages")
#!============================================================================================

Dorset = County("Dorset", "772,268", "South West", ["Bournemouth", "Dorchester"],
                ["Jurassic coastline a world heritage site", "Durdle door a natural limestone arch"],
                "https://en.wikipedia.org/wiki/Dorset#Cities,_towns_and_villages")
#!==============================================================================================


Durham  = County("Durham","528,100","North East",["Durham, Darlington"],
                 [" Durham Cathedral, Durham University"],
                 "https://en.wikipedia.org/wiki/Dorset#Cities,_towns_and_villages")
#!===========================================================================================


East_Riding_of_Yorkshire = County("East Riding of Yorkshire", "597,000", "Yorkshire and the Humber",
                ["Hull", "Beverley"],
                ["Humber Bridge, Beverley Minster"],
                "https://en.wikipedia.org/wiki/East_riding_of_yorkshire#Cities,_towns_and_villages")

#!=================================================================================================================


East_Sussex = County("East_Sussex", "808,400", "South East", ["Brighton", "Eastbourne"],
                    ["Brighton Pier, the South Downs"],
                    "https://en.wikipedia.org/wiki/East_Sussex#Cities,_towns_and_villages")
#!========================================================================================


Isle_of_Wight = County("Isle_of_Wight", "140,600", "South East", ["Ryde", "Cowes"],
                      ["Scenic coastline, seaside resorts"],
                      "https://en.wikipedia.org/wiki/Isle_of_Wight")
#!
#!=========================================================================================================

Kent = County("Kent", "1,982,100", "South East", ["Canterbury", "Ashford"],
             ["The White Cliffs of Dover, Canterbury Cathedral"],
             "https://en.wikipedia.org/wiki/Kent")
#!=================================================================================================

Lancashire = County("Lancashire", "1,498,200", "North West", ["Manchester", "Preston"],
                   ["Blackpool Tower, Pendle Witch Trials"],
                   "https://en.wikipedia.org/wiki/Lancashire")
#!==========================================================================================================


Leicestershire = County("Leicestershire", "1,028,600", "East Midlands", ["Leicester", "Loughborough"],
                        ["Leicester City Football Club, Richard III"],
                        "https://en.wikipedia.org/wiki/Leicestershire")
#!==========================================================================================


Lincolnshire = County("Lincolnshire", "1,028,600", "East Midlands", ["Lincoln, Grimsby"],
                        ["Lincoln Cathedral, agricultural heritage"],
                        "https://en.wikipedia.org/wiki/Lincolnshire")
#!===========================================================================================



Merseyside = County("Merseyside", "1,416,600", "North West", ["Liverpool, Birkenhead"],
                   ["The Beatles, Liverpool waterfront"],
                   "https://en.wikipedia.org/wiki/Merseyside")

#!=================================================================================================


Norfolk = County("Norfolk", "907,100", "East of England", ["Norwich, King's Lynn"],
                   ["Norfolk Broads, historic architecture"],
                   "https://en.wikipedia.org/wiki/Norfolk")
#!====================================================================================



North_Yorkshire = County("North Yorkshire", "640,300", "Yorkshire and the Humber", ["Harrogate, Scarborough"],
                        ["York Minster, the Yorkshire Dales"],
                        "https://en.wikipedia.org.org/wiki/North_Yorkshire")

#!==========================================================================================================


Nottinghamshire = County("Nottinghamshire", "828,200", "East Midlands", ["Nottingham, Mansfield"],
                    ["Robin Hood, Nottingham Castle"],
                    "https://en.wikipedia.org/wiki/Nottinghamshire")


#!================================================================================================


Northumberland = County("Northumberland", "323,600", "North East", ["Newcastle upon Tyne"],
                        ["Alnwick Castle, Hadrian's Wall"],
                        "https://en.wikipedia.org/wiki/Northumberland")

#!======================================================================


Nottinghamshire = County("Notinghamshire", "828,200", "East Midlands", ["Nottingham, Mansfield,"],
                    ["Robin Hood, Nottingham Castle"],
                    "https://en.wikipedia.org/wiki/NotinghamshireCities,_towns_and_villages")

#!======================================================================================================

Oxfordshire = County("Oxfordshire", "693,500", "South East", ["Oxford, Banbury"],
                   ["University of Oxford, historic architecture"],
                   "https://en.wikipedia.org/wiki/Oxfordshire")

#!================================================================================
Rutland = County("Rutland", "40,900", "East Midlands", ["Oakham, Uppingham"],
                ["Smallest historic county in England"],
                "https://en.wikipedia.org/wiki/Rutland")

#!======================================================================================

Shropshire = County("Shropshire", "501,000", "West Midlands", ["Shrewsbury, Telford"],
                   ["Ironbridge Gorge, historic market towns"],
                   "https://en.wikipedia.org/wiki/Shropshire")

#!==========================================================================
Somerset = County("Somerset", "565,500", "South West", ["Taunton, Bath"],
                   ["Glastonbury Festival, Cheddar Gorge"],
                   "https://en.wikipedia.org/wiki/Somerset")

#!==========================================================================================

South_Yorkshire = County("South Yorkshire", "1,409,400", "Yorkshire and the Humber", ["Sheffield, Rotherham"],
                        ["Steel industry, Crucible Theatre"],
                        "https://en.wikipedia.org/wiki/South_Yorkshire")


#!================================================================================================

Staffordshire = County("Staffordshire", "1,163,600", "West Midlands", ["Stoke-on-Trent, Stafford"],
                   ["Pottery industry, Alton Towers"],
                   "https://en.wikipedia.org/wiki/Staffordshire")

#!==============================================================================



#!=======================================================================================

Worcestershire = County("Worcestershire", "591,800", "West Midlands", ["Worcester, Redditch"],
                      ["Worcester Cathedral, historic towns, and Worcestershire sauce."],
                      "https://en.wikipedia.org/wiki/Worcestershire")


#!=======================================================================================

Suffolk = County("Suffolk", "761,000", "East of England", ["Ipswich, Bury St. Edmunds"],
                ["Historic market towns, beautiful countryside, and the Sutton Hoo burial site."],
                "https://en.wikipedia.org/wiki/Suffolk")
#!==============================================================================
Surrey = County("Surrey", "1,189,700", "South East", ["Guildford, Woking"],
               ["Stunning landscapes, historic towns, and the RHS Garden Wisley."],
               "https://en.wikipedia.org/wiki/Surrey")
#!====================================================================================
Tyne_and_Wear = County("Tyne and Wear", "1,129,500", "North East", ["Newcastle upon Tyne, Sunderland"],
                       ["Newcastle's vibrant nightlife, cultural attractions, and the Angel of the North"],
                       "https://en.wikipedia.org/wiki/Tyne_and_Wear")
#!==================================================================================

Warwickshire = County("Warwickshire", "569,200", "West Midlands", ["Warwick, Coventry"],
                     ["Warwick Castle, Shakespeare's birthplace in Stratford-upon-Avon, and historic market towns."],
                     "https://en.wikipedia.org/wiki/Warwickshire")
#!=======================================================================================

West_Midlands = County("West Midlands", "2,916,000", "West Midlands", ["Birmingham, Coventry"],
                      ["Birmingham's industrial heritage, diverse culture, and the Birmingham Museum and Art Gallery."],
                      "https://en.wikipedia.org/wiki/West_Midlands")
#!==============================================================================

West_Sussex = County("West Sussex", "858,800", "South East", ["Chichester, Crawley"],
                    ["Chichester Cathedral, beautiful coastal areas, and the Goodwood Estate."],
                    "https://en.wikipedia.org/wiki/West_Sussex")
#!============================================================================================

West_Yorkshire = County("West Yorkshire", "2,320,700", "Yorkshire and the Humber", ["Leeds, Bradford"],
                        ["Leeds' vibrant arts scene, historic market towns, and the Brontë Parsonage Museum in Haworth."],
                        "https://en.wikipedia.org/wiki/West_Yorkshire")
#!==================================================================================================

Wiltshire = County("Wiltshire", "498,800", "South West", ["Salisbury, Swindon"],
                   ["Stonehenge, Salisbury Cathedral, and picturesque countryside."],
                   "https://en.wikipedia.org/wiki/Wiltshire")
#!========================================================================================================

Worcestershire = County("Worcestershire", "591,800", "West Midlands", ["Worcester, Redditch"],
                        ["Worcester Cathedral, historic towns, and Worcestershire sauce."],
                        "https://en.wikipedia.org/wiki/Worcestershire")
#!==================================================================================================

counties_list = [Bedfordshire, Berkshire, Bristol, Buckinghamshire, Cambridgeshire, Cheshire, Cornwall, Cumbria, Derbyshire,
                  Devon, Dorset, Durham, East_Riding_of_Yorkshire, East_Sussex, Isle_of_Wight, Kent, Lancashire, Leicestershire,
                    Lincolnshire, Merseyside, Norfolk, North_Yorkshire, Nottinghamshire, 
                    Northumberland, Oxfordshire, Rutland, Shropshire, Somerset, South_Yorkshire, 
                    Staffordshire, Suffolk, Surrey, Tyne_and_Wear, Warwickshire, West_Midlands,
                      West_Sussex, West_Yorkshire, Wiltshire, Worcestershire]

for county in counties_list:
    print("Name:", county.name)
    print("Region:", county.region)
    print()
//?====================================================================================================================================


