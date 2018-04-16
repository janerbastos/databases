# -*- coding:UTF-8 -*-

CHOOSE_TIPO_CONTENT = (
    ('', 'Informe um tipo de conteúdo'),
    ('ATPagina', 'Páginas'),
    ('ATNoticia', 'Notícias'),
    ('ATInforme', 'Informes'),
    ('ATLink', 'Links'),
    ('ATImagem', 'Imagens'),
    ('ATBanner', 'Banners'),
    ('ATEvento', 'Eventos'),
    ('ATAgenda', 'Agendas'),
    ('ATArquivo', 'Arquivo'),
    ('ATServico', 'Servico'),
)

CHOOSE_LISTA_CONTENTS = {
    'ATNoticia': 'Noticia',
    'ATPagina': 'Pagina',
    'ATPasta': 'Pasta',
    'ATArquivo': 'Arquivo',
    'ATEvento': 'Evento',
    'ATAgenda': 'Agenda',
    'ATImagem': 'Imagem',
    'ATBanner': 'Banner',
    'ATInforme': 'Informe',
    'ATLink': 'Link',
    'ATServico': 'Servico'
}

CHOOCE_LISTA_PAPEIS = {
    'create': 'Criar',
    'delete': 'Apagar',
    'update': 'Atualizar',
    'workflow':'Publicar',
}

CHOOSE_WORKFLOW = (
    ('Privado', 'Privado'),
    ('Publicado', 'Publicado'),
)

CHOOSE_CATEGORIA = {
    ('privado', 'Privado'),
    ('publico', 'Publico')
}

CHOOSE_STATUS = (
    (False, 'Bloqueado'),
    (True, 'Habilitado'),
)