from sqlalchemy import create_engine, text

## In order to print the returned results,
## each query must contain the following columns:
## FLIGHT_ID, ORIGIN_AIRPORT, DESTINATION_AIRPORT, AIRLINE, and DELAY

QUERY_FLIGHT_BY_ID = """
SELECT 
    flights.*,
    airlines.airline,
    flights.ID as FLIGHT_ID, 
    flights.DEPARTURE_DELAY as DELAY
FROM flights
JOIN airlines
ON flights.airline = airlines.id
WHERE flights.ID = :id
;
"""

QUERY_FLIGHT_BY_DATE = """
SELECT
	ID,
	AIRLINE,
	ORIGIN_AIRPORT,
	DESTINATION_AIRPORT,
	DEPARTURE_DELAY AS DELAY
FROM flights
WHERE
	DAY = :day
	AND MONTH = :month
	AND YEAR = :year
ORDER BY ID
;
"""

QUERY_DELAYED_FLIGHT_BY_AIRLINE = """
SELECT
    flights.ID AS ID,
    airlines.AIRLINE AS AIRLINE,
    flights.ORIGIN_AIRPORT AS ORIGIN_AIRPORT,
    flights.DESTINATION_AIRPORT AS DESTINATION_AIRPORT,
    flights.DEPARTURE_DELAY AS DELAY
FROM flights
JOIN airlines
ON flights.AIRLINE = airlines.ID
WHERE DEPARTURE_DELAY > 0
    AND airlines.AIRLINE = :airline
;
"""

QUERY_DELAYED_FLIGHT_BY_ORIGIN_AIRPORT = """
SELECT
    flights.ID AS ID,
    airlines.AIRLINE AS AIRLINE,
    flights.ORIGIN_AIRPORT AS ORIGIN_AIRPORT,
    flights.DESTINATION_AIRPORT AS DESTINATION_AIRPORT,
    flights.DEPARTURE_DELAY AS DELAY
FROM flights
JOIN airlines
ON flights.AIRLINE = airlines.ID
WHERE DEPARTURE_DELAY > 0
    AND flights.ORIGIN_AIRPORT = :airport
;
"""

class FlightData:
    """
    The FlightData class is a Data Access Layer (DAL) object that provides an
    interface to the flight data in the SQLITE database. When the object is created,
    the class forms connection to the sqlite database file, which remains active
    until the object is destroyed.
    """

    def __init__(self, db_uri):
        """
        Initialize a new engine using the given database URI
        """
        self._engine = create_engine(db_uri)

    def _execute_query(self, query, params):
        """
        Execute an SQL query with the params provided in a dictionary,
        and returns a list of records (dictionary-like objects).
        If an exception was raised, print the error, and return an empty list.
        """
        ## Since the engine is already created,
        ## it just needs to connect to the database
        ## and execute the query.
        with self._engine.connect() as connection:
            try:
                result = connection.execute(text(query), params)
                rows = result.fetchall()
                return rows
            except Exception as e:
                print(f"Error: {e}")
                return []


    def get_flight_by_id(self, flight_id):
        """
        Searches for flight details using flight ID.
        If the flight was found, returns a list with a single record.
        """
        params = {'id': flight_id}
        return self._execute_query(QUERY_FLIGHT_BY_ID, params)


    def get_flights_by_date(self, day, month, year):
        """
        Searches for flights using the given date.
        If the flight was found, returns a list with the records.
        """
        params = {'day': day, 'month': month, 'year': year}
        return self._execute_query(QUERY_FLIGHT_BY_DATE, params)


    def get_delayed_flights_by_airline(self, airline):
        """
        Searches for delayed flights using the given airline.
        If the flight was found, returns a list with the records.
        """
        params = {'airline': airline}
        return self._execute_query(QUERY_DELAYED_FLIGHT_BY_AIRLINE, params)


    def get_delayed_flights_by_airport(self, airport):
        """
        Searches for delayed flights using the given airport.
        If the flight was found, returns a list with the records.
        """
        params = {'airport': airport}
        return self._execute_query(QUERY_DELAYED_FLIGHT_BY_ORIGIN_AIRPORT, params)


    def __del__(self):
        """
        Closes the connection to the databse when the object is about to be destroyed
        """
        self._engine.dispose()
