# -*- coding: utf-8 -*-

main_menu = [

    {
        "name": "Porte",
		"desc": [],
        "option": [
			"Ouvrir la porte",
        	"Fermer la porte"
		],
		"setAction": "doorStatut"
    },
    {
        "name": "Nombre de poules",
        "desc": ["Indiquez votre nombre de poule"],
        "option": " - {} + poule(s)",
		"setAction": "chickenNumber"
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
                		"switchable": True,
						"switch": [
							" - {} + :{}",
							" {}: - {} +"
						],
						"setAction": "openHour"
					},
            		{
                		"name": "Fermeture à",
                		"desc": ["La porte se fermera à"],
						"switchable": True,
						"switch": [
							" - {} + :{}",
							" {}: - {} +"
						],
						"setAction": "closeHour"
					}
				]
			}
		],
		"setAction": "hoursType"
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
						"isYes": {
							"waiting": True,
							"wait": [
								"Veuillez brancher",
								"une clé USB ..."
							],
							"confirm": "Fichier exporter avec succès !",
							"denied": "Erreur : fichier non exporter !"
						},
						"isNo": None
					}
				],
				"setAction": "chickenLogs"
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
				"option": [],
				"switchable": True,
				"switch": [
					" - {} + /{}/{}",
					" {}/ - {} + /{}",
					" {}/{}/ - {} +"
				]
			},
			{
				"name": "Heure",
				"desc": ["Indiquez l'heure de la machine"],
				"option": [],
				"switchable": True,
				"switch": [
					" - {} + :{}",
					" {}: - {} +"
				]
			}
		],
		"setAction": "timeSet"
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