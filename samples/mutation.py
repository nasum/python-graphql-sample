import data
import graphene


class Ship(graphene.ObjectType):
    name = graphene.String()
    completion = graphene.String()
    captain = graphene.String()


class ShipInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    completion = graphene.String(required=True)
    captain = graphene.String(required=True)


class CreateKongouType(graphene.Mutation):
    class Arguments:
        ship_data = ShipInput(required=True)

    ok = graphene.Boolean()
    ship = graphene.Field(lambda: Ship)

    @staticmethod
    def mutate(self, info, ship_data=None):
        ship = Ship(
            name=ship_data.name,
            completion=ship_data.completion,
            captain=ship_data.captain
        )
        ok = True
        data.kanmusu['kongou_type'].append(ship.__dict__)
        return CreateKongouType(ok=ok, ship=ship)


class MyMutations(graphene.ObjectType):
    create_kongou_type = CreateKongouType.Field()


class Query(graphene.ObjectType):
    ship = graphene.Field(Ship)


schema = graphene.Schema(query=Query, mutation=MyMutations)

query = '''
    mutation myMutations {
        createKongouType(shipData:{name:"kongoumk2",completion:"2019/01/31",captain:"nasum"}) {
            ship {
                name
                completion
                captain
            }
            ok
        }
    }
'''

if __name__ == '__main__':
    print(data.kanmusu['kongou_type'])
    result = schema.execute(query)
    print(result.data['createKongouType'])
    print(data.kanmusu['kongou_type'])
