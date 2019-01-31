import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(description="hello")

    def resolve_hello(self, info):
        """
        hello respolver
        """
        return 'world'


schema = graphene.Schema(query=Query)

query = '''
    query SayHello {
      hello
    }
'''

if __name__ == '__main__':
    result = schema.execute(query)
    print(result.data['hello'])
