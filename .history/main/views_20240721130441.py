from django.shortcuts import render


def products(request):
    person = [
        {'img': 'data:image/webp;base64,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',
        'name': 'Dwayne Jonson',
        'hwo':'Actor', 
        'info': 'Dueyn Duglas Jonson - amerikalik kino aktyori, tadbirkor, musiqachi, qo`shiqchi va kurashchi. Barcha davrlarning eng buyuk kurashchilaridan biri hisoblangan u aktyorlik faoliyatini boshlashdan oldin sakkiz yil davomida WWE da qatnashgan.' },
        {'img': '',
        'name': 'Dwayne Jonson',
        'hwo':'Actor', 
        'info': '' },
    ]
    return render(request, 'product.html')

