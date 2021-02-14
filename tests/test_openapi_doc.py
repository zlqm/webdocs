from webdocs.openapi_doc import OPENAPI


def test_default_doc():
    doc = OPENAPI().as_dict()
    assert isinstance(doc, dict)
    assert doc['openapi'] == '3.0.0'
    assert 'info' in doc
    assert 'title' in doc['info']
    assert 'description' in doc['info']


def test_from_obj():
    class MockDoc:
        OPENAPI_SERVERS = [{"url": "/api/v3"}]
        OPENAPI_TAGS = [
            {
                "name": "store",
                "description": "Operations about user"
            },
        ]

    doc = OPENAPI()
    doc.from_obj(MockDoc)
    doc = doc.as_dict()
    assert doc['servers'] == MockDoc.OPENAPI_SERVERS
    assert doc['tags'] == MockDoc.OPENAPI_TAGS
