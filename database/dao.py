from database.DB_connect import DBConnect
from model.anno import Anno
from model.team import Team


class DAO:

    @staticmethod
    def get_anno_filtrato() -> list[Anno]:
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print('Errore connessione database')
            return None
        cursor = cnx.cursor(dictionary=True)
        query = '''SELECT DISTINCT(year)
                    FROM team
                    WHERE year >= 1980'''
        try:
            cursor.execute(query)
            for row in cursor:
                anno = Anno(
                    anno_partecipazione=row['year'],
                )
                result.append(anno)
                print(anno)
        except Exception as e:
            print(f'Errore nella query: {e}')
        finally:
            cursor.close()
            cnx.close()
        return result
    def get_squadre_per_anno(anno) -> list[Team]:
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print('Errore connessione database')
            return None
        cursor = cnx.cursor(dictionary=True)
        query = '''SELECT id,year,team_code,name
                            FROM team
                            WHERE year = %s'''
        try:
            cursor.execute(query,(anno,))
            for row in cursor:
                team = Team(
                    id =row['id'],
                    year = row['year'],
                    team_code = row['team_code'],
                    name = row['name'],
                )
                result.append(team)
                print(team)
        except Exception as e:
            print(f'Errore nella query: {e}')
        finally:
            cursor.close()
            cnx.close()
        return result
    def get_salario_per_squadra(anno) :
        cnx = DBConnect.get_connection()
        result = {}
        if cnx is None:
            print('Errore connessione database')
            return None
        cursor = cnx.cursor(dictionary=True)
        query = '''SELECT team_code,SUM(salary) AS salario
                    FROM salary
                    WHERE year = %s 
                    GROUP BY team_code'''
        try:
            cursor.execute(query, (anno,))
            for row in cursor:

                result[row['team_code']] = row['salario']
            print(result)

        except Exception as e:
            print(f'Errore nella query: {e}')
        finally:
            cursor.close()
            cnx.close()
        return result
