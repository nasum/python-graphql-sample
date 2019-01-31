import graphene


class Ship(graphene.ObjectType):
    name = graphene.String()
    completion = graphene.String()
    captain = graphene.String()


class ShipInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    completion = graphene.String(required=True)
    captain = graphene.String(required=True)


class CreateShip(graphene.Mutation):
    class Arguments:
        ship_data = ShipInput(required=True)

    Output = Ship

    @staticmethod
    def mutate(self, info, ship_data=None):
        ship = Ship(
            name=ship_data.name,
            completion=ship_data.completion,
            captain=ship_data.captain
        )
        return ship


class MyMutations(graphene.ObjectType):
    create_ship = CreateShip.Field()


class Query(graphene.ObjectType):
    ship = graphene.Field(Ship)


schema = graphene.Schema(mutation=MyMutations)

query = '''
    mutation myMutations {
        createShip(shipData:{name:"kongoumk2",completion:"2019/01/31",captain:"nasum"}) {
            name
            completion
            captain
            __typename
        }
    }
'''

if __name__ == '__main__':
    result = schema.execute(query)
    print(result.data['createShip'])
