from django.http import JsonResponse
from django.views import View


class PetsView(View):
    def post(self):
        '''
        tags:
          - pet
        summary: Add a new pet to the store
        description: Add a new pet to the store
        operationId: addPet
        requestBody:
          description: Create a new pet in the store
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Pet'
            application/xml:
              schema:
                $ref: '#/components/schemas/Pet'
            application/x-www-form-urlencoded:
              schema:
                $ref: '#/components/schemas/Pet'
          required: true
        responses:
          '200':
            description: Successful operation
            content:
              application/xml:
                schema:
                  $ref: '#/components/schemas/Pet'
              application/json:
                schema:
                  $ref: '#/components/schemas/Pet'
          '405':
            description: Invalid input
        security:
          - petstore_auth:
              - 'write:pets'
              - 'read:pets' 
        '''
        return JsonResponse({})


class PetView(View):
    def get(self, request, pet_id):
        '''
        foo bar foo bar
        foo bar foo bar
        foo bar foo bar
        foo bar foo bar
        --api-doc--
        tags:
        - pet
        summary: Find pet by ID
        description: Returns a single pet
        operationId: getPetById
        responses:
          '200':
            description: successful operation
            content:
              application/xml:
                schema:
                  $ref: '#/components/schemas/Pet'
              application/json:
                schema:
                  $ref: '#/components/schemas/Pet'
          '400':
            description: Invalid ID supplied
          '404':
            description: Pet not found
        security:
          - api_key: []
          - petstore_auth:
              - 'write:pets'
              - 'read:pets'
        '''
        return JsonResponse({})

    def delete(self, request, pet_id):
        '''
        tags:
          - pet
        summary: Deletes a pet
        description: ''
        operationId: deletePet
        parameters:
          - name: api_key
            in: header
            description: ''
            required: false
            schema:
              type: string
        responses:
          '400':
            description: Invalid pet value
        security:
          - petstore_auth:
              - 'write:pets'
              - 'read:pets'
        '''
        return JsonResponse({})


class PetImageView(View):
    '''
    parameters:
    - in: path
      name: pet_id
      schema:
        type: integer
      required: true
    '''
    def post(self, request, pet_id):
        '''
        tags:
          - pet
        summary: uploads an image
        description: ''
        operationId: uploadFile
        parameters:
          - name: additionalMetadata
            in: query
            description: Additional Metadata
            required: false
            schema:
              type: string
        requestBody:
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
        responses:
          '200':
            description: successful operation
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ApiResponse'
        security:
          - petstore_auth:
              - 'write:pets'
              - 'read:pets'
        '''
        return JsonResponse({})
