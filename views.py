from django.shortcuts import render, get_object_or_404

def clubes(request):
    clubes = {
        'Deportes': [
            {'nombre': 'Club de Fútbol', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 25},
            {'nombre': 'Club de Baloncesto', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 18},
            {'nombre': 'Club de Voleibol', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 20},
            {'nombre': 'Club de Natación', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 15},
            {'nombre': 'Club de Atletismo', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 22},
        ],
        'Ciencia': [
            {'nombre': 'Club de Robótica', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 30},
            {'nombre': 'Club de Astronomía', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 22},
            {'nombre': 'Club de Matemáticas', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 25},
            {'nombre': 'Club de Química', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 18},
            {'nombre': 'Club de Física', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211', 'integrantes': 19},
        ],
    }

    return render(request, 'clubes.html', {'clubes': clubes})

def detalle_club(request, nombre):
    clubes = {
        'Club de Fútbol': {
            'imagenes': [
                'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211',
            ],
            'videos': [
                'https://media.istockphoto.com/id/1213127417/es/v%C3%ADdeo/joven-abrazando-gatito.mp4?s=mp4-640x640-is&k=20&c=ykt-tUF2Bgn7FoPlcTHPew8Kmjrn-Eb1iY-kYGsF0hY=',
            ],
            'descripcion': ' Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam tenetur aut ipsum? Quibusdam eligendi nihil laborum sed sapiente? Laudantium hic soluta iure aspernatur asperiores unde dolore ab quos, maiores nam?Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam tenetur aut ipsum? Quibusdam eligendi nihil laborum sed sapiente? Laudantium hic soluta iure aspernatur asperiores unde dolore ab quos, maiores nam?'
        },
        # añadir más clubes
    }

    club = get_object_or_404(clubes, nombre)

    publicaciones = [
        {'titulo': f'Publicación {i+1}', 'contenido': f'Contenido de la publicación {i+1}', 'imagenes': ['https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211'], 'videos': []} 
        for i in range(20)
    ]

    miembros = [
        {'nombre': f'Miembro {i+1}', 'imagen': 'https://clubmontesur.com.mx/cdn/shop/articles/club-deportivo-y-social.jpg?v=1700095211'}
        for i in range(10)
    ]

    return render(request, 'detallesClub.html', {
        'nombre': nombre,
        'imagenes': club['imagenes'],
        'videos': club['videos'],
        'descripcion': club['descripcion'],
        'publicaciones': publicaciones,
        'miembros': miembros
    })
