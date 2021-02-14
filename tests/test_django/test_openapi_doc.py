import tempfile
from django.core import management
from webdocs.django.openapi_doc import DjangoOPENAPI
import yaml
from . import docs, views


def test_default_path_parameter():
    doc = DjangoOPENAPI()
    doc = doc.as_dict()
    assert len(doc['paths']['/pets/{pet_id}']['parameters']) == 1
    assert doc['paths']['/pets/{pet_id}']['parameters'][0]['name'] == 'pet_id'
    assert doc['paths']['/pets/{pet_id}']['parameters'][0]['in'] == 'path'

    assert len(doc['paths']['/pets/{pet_id}/images']['parameters']) == 1
    assert doc['paths']['/pets/{pet_id}/images']['parameters'][0][
        'name'] == 'pet_id'
    assert doc['paths']['/pets/{pet_id}/images']['parameters'][0][
        'in'] == 'path'
    assert doc['paths']['/pets/{pet_id}/images']['parameters'][0][
        'schema'] == {
            'type': 'integer'
        }


def test_doc_string():
    doc = DjangoOPENAPI()
    doc = doc.as_dict()
    assert doc['paths']['/pets']['post'] == \
            yaml.safe_load(views.PetsView.post.__doc__)
    assert doc['paths']['/pets/{pet_id}']['get'] == \
            yaml.safe_load(views.PetView.get.__doc__.split('--api-doc--')[-1])


def test_from_settings():
    doc = DjangoOPENAPI()
    doc_dct = doc.as_dict()
    assert 'tags' not in doc_dct
    assert 'components' not in doc_dct
    doc.from_settings()
    doc_dct = doc.as_dict()
    assert doc_dct['tags'] == yaml.safe_load(docs.OPENAPI_TAGS)
    assert doc_dct['components'] == yaml.safe_load(docs.OPENAPI_COMPONENTS)


def test_generate_command():
    with tempfile.TemporaryFile('w') as f:
        management.call_command('generate_api_doc', f.name)
