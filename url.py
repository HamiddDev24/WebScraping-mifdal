import requests
list = [
{"name": "1", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/0.png"},
{"name": "2", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/1.png"},
{"name": "3", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/2.png"},
{"name": "4", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/3.png"},
{"name": "5", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/4.png"},
{"name": "6", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/5.png"},
{"name": "7", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/6.png"},
{"name": "8", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/7.png"},
{"name": "9", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/8.png"},
{"name": "10", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/9.png"},
{"name": "11", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/10.png"},
{"name": "12", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/11.png"},
{"name": "13", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/12.png"},
{"name": "14", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/13.png"},
{"name": "15", "chapter": 960, "img": "https://3asq.org/wp-content/uploads/WP-manga/data/manga_5ca2daf920c76/335cc2d968d9372179577161f79b2fa2/14.png"}
]
for s in list:
    r = requests.get(s['img'])
    with open(s['chapters/name']+".jpg", "wb") as file:
	    file.write(r.content)