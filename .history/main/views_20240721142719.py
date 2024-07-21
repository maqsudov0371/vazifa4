from django.shortcuts import render


def products(request):
    person = [
        {'img': 'data:image/webp;base64,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',
        'name': 'Dwayne Jonson',
        'hwo':'Actor', 
        'info': 'Dueyn Duglas Jonson - amerikalik kino aktyori, tadbirkor, musiqachi, qo`shiqchi va kurashchi. Barcha davrlarning eng buyuk kurashchilaridan biri hisoblangan u aktyorlik faoliyatini boshlashdan oldin sakkiz yil davomida WWE da qatnashgan.',
        'age': '1972 yil 2 may (52 yosh)'},

        {'img': 'data:image/jpeg;base64,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',
        'name': 'Cristiano Ronaldo',
        'hwo':'Futbol o`yinchisi', 
        'info': 'Krishtianu Ronaldu dos Santos Aveyru — portugaliyalik futbolchi, hujumchi, Saudiya Arabistonining “Al-Nasr” klubi va Portugaliya terma jamoasi sardori. Yevropa chempioni. Barcha davrlarning eng yaxshi futbolchilaridan biri hisoblangan.',
        'age': '1985 yil 5-fevral (39 yosh)'},
    
        {'img': 'data:image/jpeg;base64,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',
        'name': 'Shoxruz Nazarov',
        'hwo':'Gamer', 
        'info': '“Bu mening ikkinchi uyim”, deydi PUBG mobil oʻyinining rasmiy geymeri va Oʻzbekistondagi eng yaxshi oʻyinchilardan biri, oʻz jamoasida Yakudza nomi bilan mashhur boʻlgan 15 yoshli Shohruz Nazarov.(2020-yildagi malulmotlar!)',
        'age': '2004 yil (19 yosh)'},
    ]
    context = {
        'list3':'Dasturlash turlari',
        'programming': users
    }
    return render(request, 'product.html')

