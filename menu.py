main_menu = [
	
    {
        "name": "Porte",
		"desc": [],
        "option": [
			"Ouvrir la porte",
        	"Fermer la porte"
		]
    },
    {
        "name": "Nombre de poules",
        "desc": ["Indiquez votre nombre de poule"],
        "option": " - {} + poule(s)"
    },
    {
        "name": "Ouverture porte",
		"desc": [],
        "option": [
			"Automatique",
			{
            	"name": "Avec horaires",
				"desc": [],
				"option": [
					{
                		"name": "Ouverture à",
                		"desc": ["La porte s'ouvrira à"],
                		"switch": True,
                		"option": [
							" - {} + :{}",
							" {}: - {} +"
						]
					},
            		{
                		"name": "Fermeture à",
                		"desc": ["La porte se fermera à"],
						"switch": True,
                		"option": [
							" - {} + :{}",
							" {}: - {} +"
						]
					}
				]
			}
		]
    },
    {
        "name": "Suivi des poules",
		"desc": [],
		"option": [
			{
				"name": "Consulter",
				"option": [],
				"desc": [
					"Entrées journalières : {} poule(s)",
					"Sorties journalières : {} poule(s)",
					"..."
				]

			},
			{
				"name": "Exporter sur USB",
				"desc": ["Exporter un suivi détaillé des poules ?"],
        		"option": [
					{
						"choise": True,
						"name": None,
						"isYes": [
							"Veuillez brancher",
							"une clé USB ..."
						],
						"isNo": None
					}
				]
			}
		]
    },
	{
		"name": "Date/heure",
		"desc": [],
		"option": [
			{
				"name": "Date",
				"desc": ["Indiquez la date de la machine"],
				"switch": True,
				"option": [
					" - {} + /{}/{}",
					" {}/ - {} + /{}",
					" {}/{}/ - {} +"
				]
			},
			{
				"name": "Heure",
				"desc": ["Indiquez l'heure de la machine"],
				"switch": True,
				"option": [
					" - {} + :{}",
					" {}: - {} +"
				]
			}
		]
	},
    {
        "name": "Statut machine",
		"option": [],
		"desc": [
			"Batterie chargé à {}%",
			"Production : {} Watts",
			"Consommation : {} Watts",
			"Total d'entrées : {} poules",
			"Total de sortis : {} poules"
		]
    }
]
