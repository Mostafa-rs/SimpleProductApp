"""
Product APIs
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

import traceback
from rest_framework.views import APIView

# Local
from products.models import Product
from products.serializers import ProductSerializer
from utils.response import get_response
from utils.messages import Message
from utils.permissions import IsAuthenticatedOrReadonly
from utils.redis import get_product_cache, Key
from log.defines import save_log


class ProductListCreateAPI(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadonly,)
    api_name = 'ProductListCreateAPI'

    def get(self, request):
        try:
            products = get_product_cache(Key.PRODUCT_LIST)
            srz = self.serializer_class(products, many=True)

            return get_response(srz.data)
        except Exception as e:
            save_log(request, 'ERR_GET', self.api_name, f'{e}\n{traceback.format_exc()}')
            return get_response(errors={'detail': Message.ERR_TRY})

    def post(self, request):
        try:
            data = request.data
            srz = self.serializer_class(data=data)

            if srz.is_valid():
                srz.save()

                return get_response(srz.data)

            return get_response(errors=srz.errors)

        except Exception as e:
            save_log(request, 'ERR_POST', self.api_name, f'{e}\n{traceback.format_exc()}')
            return get_response(errors={'detail': Message.ERR_TRY})


class ProductRetrieveUpdateDeleteAPI(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadonly,)
    api_name = 'ProductRetrieveUpdateDeleteAPI'

    def get(self, request, pk):
        try:
            product = get_product_cache(Key.PRODUCT_DETAILS, pk)

            if not product:
                return get_response(errors={'detail': Message.ERR_PRODUCT_NOT_FOUND})

            srz = self.serializer_class(product)

            return get_response(srz.data)

        except Exception as e:
            save_log(request, 'ERR_GET', self.api_name, f'{e}\n{traceback.format_exc()}')
            return get_response(errors={'detail': Message.ERR_TRY})

    def put(self, request, pk):
        try:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return get_response(errors={'detail': Message.ERR_PRODUCT_NOT_FOUND})

            data = request.data
            srz = self.serializer_class(product, data=data, partial=True)

            if srz.is_valid():
                obj = srz.save()

                return get_response(self.serializer_class(obj).data)

            return get_response(errors=srz.errors)

        except Exception as e:
            save_log(request, 'ERR_PUT', self.api_name, f'{e}\n{traceback.format_exc()}')
            return get_response(errors={'detail': Message.ERR_TRY})

    def delete(self, request, pk):
        try:
            try:
                product = Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return get_response(errors={'detail': Message.ERR_PRODUCT_NOT_FOUND})

            product.delete()
            return get_response({'detail': Message.OK_PRODUCT_DELETED})

        except Exception as e:
            save_log(request, 'ERR_DELETE', self.api_name, f'{e}\n{traceback.format_exc()}')
            return get_response(errors={'detail': Message.ERR_TRY})
