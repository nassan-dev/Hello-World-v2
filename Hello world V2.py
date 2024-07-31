import webbrowser
import random
from fuzzywuzzy import process


# Dictionary to hold Wikipedia URLs for countries and programming languages
CATEGORIES = {
    "Countries": {
        "Afghanistan": "https://en.wikipedia.org/wiki/Afghanistan",
        "Albania": "https://en.wikipedia.org/wiki/Albania",
        "Algeria": "https://en.wikipedia.org/wiki/Algeria",
        "Andorra": "https://en.wikipedia.org/wiki/Andorra",
        "Angola": "https://en.wikipedia.org/wiki/Angola",
        "Antigua and Barbuda": "https://en.wikipedia.org/wiki/Antigua_and_Barbuda",
        "Argentina": "https://en.wikipedia.org/wiki/Argentina",
        "Armenia": "https://en.wikipedia.org/wiki/Armenia",
        "Australia": "https://en.wikipedia.org/wiki/Australia",
        "Austria": "https://en.wikipedia.org/wiki/Austria",
        "Azerbaijan": "https://en.wikipedia.org/wiki/Azerbaijan",
        "Bahamas": "https://en.wikipedia.org/wiki/Bahamas",
        "Bahrain": "https://en.wikipedia.org/wiki/Bahrain",
        "Bangladesh": "https://en.wikipedia.org/wiki/Bangladesh",
        "Barbados": "https://en.wikipedia.org/wiki/Barbados",
        "Belarus": "https://en.wikipedia.org/wiki/Belarus",
        "Belgium": "https://en.wikipedia.org/wiki/Belgium",
        "Belize": "https://en.wikipedia.org/wiki/Belize",
        "Benin": "https://en.wikipedia.org/wiki/Benin",
        "Bhutan": "https://en.wikipedia.org/wiki/Bhutan",
        "Bolivia": "https://en.wikipedia.org/wiki/Bolivia",
        "Bosnia and Herzegovina": "https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina",
        "Botswana": "https://en.wikipedia.org/wiki/Botswana",
        "Brazil": "https://en.wikipedia.org/wiki/Brazil",
        "Brunei": "https://en.wikipedia.org/wiki/Brunei",
        "Bulgaria": "https://en.wikipedia.org/wiki/Bulgaria",
        "Burkina Faso": "https://en.wikipedia.org/wiki/Burkina_Faso",
        "Burundi": "https://en.wikipedia.org/wiki/Burundi",
        "Cabo Verde": "https://en.wikipedia.org/wiki/Cape_Verde",
        "Cambodia": "https://en.wikipedia.org/wiki/Cambodia",
        "Cameroon": "https://en.wikipedia.org/wiki/Cameroon",
        "Canada": "https://en.wikipedia.org/wiki/Canada",
        "Central African Republic": "https://en.wikipedia.org/wiki/Central_African_Republic",
        "Chad": "https://en.wikipedia.org/wiki/Chad",
        "Chile": "https://en.wikipedia.org/wiki/Chile",
        "China": "https://en.wikipedia.org/wiki/China",
        "Colombia": "https://en.wikipedia.org/wiki/Colombia",
        "Comoros": "https://en.wikipedia.org/wiki/Comoros",
        "Congo, Democratic Republic of the": "https://en.wikipedia.org/wiki/Democratic_Republic_of_the_Congo",
        "Congo, Republic of the": "https://en.wikipedia.org/wiki/Republic_of_the_Congo",
        "Costa Rica": "https://en.wikipedia.org/wiki/Costa_Rica",
        "Croatia": "https://en.wikipedia.org/wiki/Croatia",
        "Cuba": "https://en.wikipedia.org/wiki/Cuba",
        "Cyprus": "https://en.wikipedia.org/wiki/Cyprus",
        "Czech Republic": "https://en.wikipedia.org/wiki/Czech_Republic",
        "Denmark": "https://en.wikipedia.org/wiki/Denmark",
        "Djibouti": "https://en.wikipedia.org/wiki/Djibouti",
        "Dominica": "https://en.wikipedia.org/wiki/Dominica",
        "Dominican Republic": "https://en.wikipedia.org/wiki/Dominican_Republic",
        "Ecuador": "https://en.wikipedia.org/wiki/Ecuador",
        "Egypt": "https://en.wikipedia.org/wiki/Egypt",
        "El Salvador": "https://en.wikipedia.org/wiki/El_Salvador",
        "Equatorial Guinea": "https://en.wikipedia.org/wiki/Equatorial_Guinea",
        "Eritrea": "https://en.wikipedia.org/wiki/Eritrea",
        "Estonia": "https://en.wikipedia.org/wiki/Estonia",
        "Eswatini": "https://en.wikipedia.org/wiki/Eswatini",
        "Ethiopia": "https://en.wikipedia.org/wiki/Ethiopia",
        "Fiji": "https://en.wikipedia.org/wiki/Fiji",
        "Finland": "https://en.wikipedia.org/wiki/Finland",
        "France": "https://en.wikipedia.org/wiki/France",
        "Gabon": "https://en.wikipedia.org/wiki/Gabon",
        "Gambia": "https://en.wikipedia.org/wiki/The_Gambia",
        "Georgia": "https://en.wikipedia.org/wiki/Georgia_(country)",
        "Germany": "https://en.wikipedia.org/wiki/Germany",
        "Ghana": "https://en.wikipedia.org/wiki/Ghana",
        "Greece": "https://en.wikipedia.org/wiki/Greece",
        "Grenada": "https://en.wikipedia.org/wiki/Grenada",
        "Guatemala": "https://en.wikipedia.org/wiki/Guatemala",
        "Guinea": "https://en.wikipedia.org/wiki/Guinea",
        "Guinea-Bissau": "https://en.wikipedia.org/wiki/Guinea-Bissau",
        "Guyana": "https://en.wikipedia.org/wiki/Guyana",
        "Haiti": "https://en.wikipedia.org/wiki/Haiti",
        "Honduras": "https://en.wikipedia.org/wiki/Honduras",
        "Hungary": "https://en.wikipedia.org/wiki/Hungary",
        "Iceland": "https://en.wikipedia.org/wiki/Iceland",
        "India": "https://en.wikipedia.org/wiki/India",
        "Indonesia": "https://en.wikipedia.org/wiki/Indonesia",
        "Iran": "https://en.wikipedia.org/wiki/Iran",
        "Iraq": "https://en.wikipedia.org/wiki/Iraq",
        "Ireland": "https://en.wikipedia.org/wiki/Ireland",
        "Israel": "https://en.wikipedia.org/wiki/Israel",
        "Italy": "https://en.wikipedia.org/wiki/Italy",
        "Jamaica": "https://en.wikipedia.org/wiki/Jamaica",
        "Japan": "https://en.wikipedia.org/wiki/Japan",
        "Jordan": "https://en.wikipedia.org/wiki/Jordan",
        "Kazakhstan": "https://en.wikipedia.org/wiki/Kazakhstan",
        "Kenya": "https://en.wikipedia.org/wiki/Kenya",
        "Kiribati": "https://en.wikipedia.org/wiki/Kiribati",
        "Korea, North": "https://en.wikipedia.org/wiki/North_Korea",
        "Korea, South": "https://en.wikipedia.org/wiki/South_Korea",
        "Kosovo": "https://en.wikipedia.org/wiki/Kosovo",
        "Kuwait": "https://en.wikipedia.org/wiki/Kuwait",
        "Kyrgyzstan": "https://en.wikipedia.org/wiki/Kyrgyzstan",
        "Laos": "https://en.wikipedia.org/wiki/Laos",
        "Latvia": "https://en.wikipedia.org/wiki/Latvia",
        "Lebanon": "https://en.wikipedia.org/wiki/Lebanon",
        "Lesotho": "https://en.wikipedia.org/wiki/Lesotho",
        "Liberia": "https://en.wikipedia.org/wiki/Liberia",
        "Libya": "https://en.wikipedia.org/wiki/Libya",
        "Liechtenstein": "https://en.wikipedia.org/wiki/Liechtenstein",
        "Lithuania": "https://en.wikipedia.org/wiki/Lithuania",
        "Luxembourg": "https://en.wikipedia.org/wiki/Luxembourg",
        "Madagascar": "https://en.wikipedia.org/wiki/Madagascar",
        "Malawi": "https://en.wikipedia.org/wiki/Malawi",
        "Malaysia": "https://en.wikipedia.org/wiki/Malaysia",
        "Maldives": "https://en.wikipedia.org/wiki/Maldives",
        "Mali": "https://en.wikipedia.org/wiki/Mali",
        "Malta": "https://en.wikipedia.org/wiki/Malta",
        "Marshall Islands": "https://en.wikipedia.org/wiki/Marshall_Islands",
        "Mauritania": "https://en.wikipedia.org/wiki/Mauritania",
        "Mauritius": "https://en.wikipedia.org/wiki/Mauritius",
        "Mexico": "https://en.wikipedia.org/wiki/Mexico",
        "Micronesia": "https://en.wikipedia.org/wiki/Micronesia",
        "Moldova": "https://en.wikipedia.org/wiki/Moldova",
        "Monaco": "https://en.wikipedia.org/wiki/Monaco",
        "Mongolia": "https://en.wikipedia.org/wiki/Mongolia",
        "Montenegro": "https://en.wikipedia.org/wiki/Montenegro",
        "Morocco": "https://en.wikipedia.org/wiki/Morocco",
        "Mozambique": "https://en.wikipedia.org/wiki/Mozambique",
        "Myanmar": "https://en.wikipedia.org/wiki/Myanmar",
        "Namibia": "https://en.wikipedia.org/wiki/Namibia",
        "Nauru": "https://en.wikipedia.org/wiki/Nauru",
        "Nepal": "https://en.wikipedia.org/wiki/Nepal",
        "Netherlands": "https://en.wikipedia.org/wiki/Netherlands",
        "New Zealand": "https://en.wikipedia.org/wiki/New_Zealand",
        "Nicaragua": "https://en.wikipedia.org/wiki/Nicaragua",
        "Niger": "https://en.wikipedia.org/wiki/Niger",
        "Nigeria": "https://en.wikipedia.org/wiki/Nigeria",
        "North Macedonia": "https://en.wikipedia.org/wiki/North_Macedonia",
        "Norway": "https://en.wikipedia.org/wiki/Norway",
        "Oman": "https://en.wikipedia.org/wiki/Oman",
        "Pakistan": "https://en.wikipedia.org/wiki/Pakistan",
        "Palau": "https://en.wikipedia.org/wiki/Palau",
        "Palestine": "https://en.wikipedia.org/wiki/State_of_Palestine",
        "Panama": "https://en.wikipedia.org/wiki/Panama",
        "Papua New Guinea": "https://en.wikipedia.org/wiki/Papua_New_Guinea",
        "Paraguay": "https://en.wikipedia.org/wiki/Paraguay",
        "Peru": "https://en.wikipedia.org/wiki/Peru",
        "Philippines": "https://en.wikipedia.org/wiki/Philippines",
        "Poland": "https://en.wikipedia.org/wiki/Poland",
        "Portugal": "https://en.wikipedia.org/wiki/Portugal",
        "Qatar": "https://en.wikipedia.org/wiki/Qatar",
        "Romania": "https://en.wikipedia.org/wiki/Romania",
        "Russia": "https://en.wikipedia.org/wiki/Russia",
        "Rwanda": "https://en.wikipedia.org/wiki/Rwanda",
        "Saint Kitts and Nevis": "https://en.wikipedia.org/wiki/Saint_Kitts_and_Nevis",
        "Saint Lucia": "https://en.wikipedia.org/wiki/Saint_Lucia",
        "Saint Vincent and the Grenadines": "https://en.wikipedia.org/wiki/Saint_Vincent_and_the_Grenadines",
        "Samoa": "https://en.wikipedia.org/wiki/Samoa",
        "San Marino": "https://en.wikipedia.org/wiki/San_Marino",
        "Sao Tome and Principe": "https://en.wikipedia.org/wiki/Sao_Tome_and_Principe",
        "Saudi Arabia": "https://en.wikipedia.org/wiki/Saudi_Arabia",
        "Senegal": "https://en.wikipedia.org/wiki/Senegal",
        "Serbia": "https://en.wikipedia.org/wiki/Serbia",
        "Seychelles": "https://en.wikipedia.org/wiki/Seychelles",
        "Sierra Leone": "https://en.wikipedia.org/wiki/Sierra_Leone",
        "Singapore": "https://en.wikipedia.org/wiki/Singapore",
        "Slovakia": "https://en.wikipedia.org/wiki/Slovakia",
        "Slovenia": "https://en.wikipedia.org/wiki/Slovenia",
        "Solomon Islands": "https://en.wikipedia.org/wiki/Solomon_Islands",
        "Somalia": "https://en.wikipedia.org/wiki/Somalia",
        "South Africa": "https://en.wikipedia.org/wiki/South_Africa",
        "South Sudan": "https://en.wikipedia.org/wiki/South_Sudan",
        "Spain": "https://en.wikipedia.org/wiki/Spain",
        "Sri Lanka": "https://en.wikipedia.org/wiki/Sri_Lanka",
        "Sudan": "https://en.wikipedia.org/wiki/Sudan",
        "Suriname": "https://en.wikipedia.org/wiki/Suriname",
        "Sweden": "https://en.wikipedia.org/wiki/Sweden",
        "Switzerland": "https://en.wikipedia.org/wiki/Switzerland",
        "Syria": "https://en.wikipedia.org/wiki/Syria",
        "Taiwan": "https://en.wikipedia.org/wiki/Taiwan",
        "Tajikistan": "https://en.wikipedia.org/wiki/Tajikistan",
        "Tanzania": "https://en.wikipedia.org/wiki/Tanzania",
        "Thailand": "https://en.wikipedia.org/wiki/Thailand",
        "Timor-Leste": "https://en.wikipedia.org/wiki/East_Timor",
        "Togo": "https://en.wikipedia.org/wiki/Togo",
        "Tonga": "https://en.wikipedia.org/wiki/Tonga",
        "Trinidad and Tobago": "https://en.wikipedia.org/wiki/Trinidad_and_Tobago",
        "Tunisia": "https://en.wikipedia.org/wiki/Tunisia",
        "Turkey": "https://en.wikipedia.org/wiki/Turkey",
        "Turkmenistan": "https://en.wikipedia.org/wiki/Turkmenistan",
        "Tuvalu": "https://en.wikipedia.org/wiki/Tuvalu",
        "Uganda": "https://en.wikipedia.org/wiki/Uganda",
        "Ukraine": "https://en.wikipedia.org/wiki/Ukraine",
        "United Arab Emirates": "https://en.wikipedia.org/wiki/United_Arab_Emirates",
        "United Kingdom": "https://en.wikipedia.org/wiki/United_Kingdom",
        "United States": "https://en.wikipedia.org/wiki/United_States",
        "Uruguay": "https://en.wikipedia.org/wiki/Uruguay",
        "Uzbekistan": "https://en.wikipedia.org/wiki/Uzbekistan",
        "Vanuatu": "https://en.wikipedia.org/wiki/Vanuatu",
        "Vatican City": "https://en.wikipedia.org/wiki/Vatican_City",
        "Venezuela": "https://en.wikipedia.org/wiki/Venezuela",
        "Vietnam": "https://en.wikipedia.org/wiki/Vietnam",
        "Yemen": "https://en.wikipedia.org/wiki/Yemen",
        "Zambia": "https://en.wikipedia.org/wiki/Zambia",
        "Zimbabwe": "https://en.wikipedia.org/wiki/Zimbabwe"
    },
     "Programming Languages": {
        "Python": "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "JavaScript": "https://en.wikipedia.org/wiki/JavaScript",
        "Java": "https://en.wikipedia.org/wiki/Java_(programming_language)",
        "C++": "https://en.wikipedia.org/wiki/C%2B%2B",
        "C#": "https://en.wikipedia.org/wiki/C_Sharp_(programming_language)",
        "Ruby": "https://en.wikipedia.org/wiki/Ruby_(programming_language)",
        "PHP": "https://en.wikipedia.org/wiki/PHP",
        "Swift": "https://en.wikipedia.org/wiki/Swift_(programming_language)",
        "Go": "https://en.wikipedia.org/wiki/Go_(programming_language)",
        "Kotlin": "https://en.wikipedia.org/wiki/Kotlin_(programming_language)",
        "Rust": "https://en.wikipedia.org/wiki/Rust_(programming_language)",
        "TypeScript": "https://en.wikipedia.org/wiki/TypeScript",
        "R": "https://en.wikipedia.org/wiki/R_(programming_language)",
        "MATLAB": "https://en.wikipedia.org/wiki/MATLAB",
        "Perl": "https://en.wikipedia.org/wiki/Perl",
        "Scala": "https://en.wikipedia.org/wiki/Scala_(programming_language)",
        "Dart": "https://en.wikipedia.org/wiki/Dart_(programming_language)",
        "Elixir": "https://en.wikipedia.org/wiki/Elixir_(programming_language)",
        "Haskell": "https://en.wikipedia.org/wiki/Haskell_(programming_language)",
        "Lua": "https://en.wikipedia.org/wiki/Lua_(programming_language)",
        "Objective-C": "https://en.wikipedia.org/wiki/Objective-C",
        "F#": "https://en.wikipedia.org/wiki/F_Sharp_(programming_language)",
        "Erlang": "https://en.wikipedia.org/wiki/Erlang_(programming_language)",
        "Clojure": "https://en.wikipedia.org/wiki/Clojure",
        "Scheme": "https://en.wikipedia.org/wiki/Scheme_(programming_language)",
        "Common Lisp": "https://en.wikipedia.org/wiki/Common_Lisp",
        "Julia": "https://en.wikipedia.org/wiki/Julia_(programming_language)",
        "Groovy": "https://en.wikipedia.org/wiki/Apache_Groovy",
        "Prolog": "https://en.wikipedia.org/wiki/Prolog",
        "Smalltalk": "https://en.wikipedia.org/wiki/Smalltalk"
    }
}
ALIASES = {
    "UK": "United Kingdom",
    "USA": "United States",
    "UAE": "United Arab Emirates",
    "JS": "JavaScript",
    "Py": "Python",
    "C#": "C Sharp"
}

def get_best_match(category, query):
    all_items = list(CATEGORIES[category].keys()) + list(ALIASES.keys())
    best_match, score = process.extractOne(query, all_items)
    if best_match in ALIASES:
        best_match = ALIASES[best_match]
    return best_match, score

def open_wikipedia_page(category, item):
    if item in CATEGORIES[category]:
        webbrowser.open(CATEGORIES[category][item])
        print(f"Opening Wikipedia page for {item}...")
    else:
        print(f"Could not find a Wikipedia page for {item}.")

def choose_random(category):
    item = random.choice(list(CATEGORIES[category].keys()))
    open_wikipedia_page(category, item)

def main_menu():
    categories = list(CATEGORIES.keys())
    
    while True:
        print("\nHello World! - Please choose a category:")
        for idx, cat in enumerate(categories, start=1):
            print(f"{idx}. {cat}")
        print("0. Exit")

        try:
            category_choice = int(input("Enter the number of the category: ")) - 1
            if category_choice == -1:
                print("Goodbye, world!")
                break
            if category_choice not in range(len(categories)):
                raise ValueError
            chosen_category = categories[category_choice]
            
            while True:
                print("\nSub-Menu:")
                print(f"1. Search for a {chosen_category.lower()}")
                print(f"2. Choose a random {chosen_category.lower()}")
                print("3. Back to main menu")
                print("4. Close program")

                sub_choice = int(input("Enter your choice: "))
                if sub_choice == 3:
                    break
                elif sub_choice == 4:
                    print("Goodbye, world!")
                    return
                elif sub_choice == 1:
                    item = input(f"Enter the name of a {chosen_category.lower()}: ").strip()
                    best_match, score = get_best_match(chosen_category, item)
                    
                    if score >= 80:
                        open_wikipedia_page(chosen_category, best_match)
                    else:
                        print(f"'{item}' not found. Best match: {best_match} with score {score}. Please try again.")
                elif sub_choice == 2:
                    choose_random(chosen_category)
                else:
                    print("Invalid choice. Please try again.")
        
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()