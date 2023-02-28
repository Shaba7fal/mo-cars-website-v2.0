from sqlalchemy import create_engine, text
import pandas as pd

db_connection_string="mysql+pymysql://3l658kwqa3hq43capb9o:pscale_pw_mGo8RQjyEIvaLWJJJ4xPANNP69FVlPkt68amktfCPVX@us-east.connect.psdb.cloud/carsrepo?charset=utf8mb4"

engine = create_engine(
    db_connection_string, 
    connect_args= {
    "ssl":{
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})

def load_cars_from_db():
   with engine.connect() as connection:
    result = connection.execute(text("select * from cars"))
    result_all=result.all()
 
    cars = pd.DataFrame(result_all, columns = ['id','title','location','price', 'currency','horesepower'])
    
    cars_list= cars.to_dict('records')
    print(cars_list)
    return cars_list
   

def load_car_from_db():
    with engine.connect() as connection:
        result = connection.execute(
            text("select * from cars WHERE id = :val"),
            val=id)
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])
    
    
