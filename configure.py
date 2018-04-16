# -*- coding:UTF-8 -*-
from databases.constants import CHOOSE_LISTA_CONTENTS, CHOOCE_LISTA_PAPEIS
from mamba.models import ContentType
from manager.models import Papel


def inicialize():
    count = ContentType.objects.all().count()
    if count <= 0:
        print 'Criando os tipos de conteúdos do site'
        for key, value in CHOOSE_LISTA_CONTENTS.iteritems():
            content_type = ContentType(tipo=key, descricao=value)
            content_type.save()

    count = Papel.objects.all().count()
    if count <= 0:
        print 'Criando os papeis do site.'
        contents_type = ContentType.objects.all()
        for content in contents_type:
            for key, value in CHOOCE_LISTA_PAPEIS.iteritems():
                papel = Papel(nome=value, cod_name=key, content_type=content)
                papel.save()

