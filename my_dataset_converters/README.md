chmod 777 convert_IBM_to_ascii.py

chmod 777 convert_IBM_to_TitanicOR.py 

./convert_IBM_to_ascii.py T100_I50.data T200_I50.data T300_I50.data T400_I50.data T500_I50.data

./convert_IBM_to_TitanicOR.py T100_I50.data -o titanic_T100_I50.data
./convert_IBM_to_TitanicOR.py T200_I50.data -o titanic_T200_I50.data
./convert_IBM_to_TitanicOR.py T300_I50.data -o titanic_T300_I50.data
./convert_IBM_to_TitanicOR.py T400_I50.data -o titanic_T400_I50.data
./convert_IBM_to_TitanicOR.py T500_I50.data -o titanic_T500_I50.data


./convert_IBM_to_ascii.py T300_I40.data T300_I45.data T300_I50.data T300_I55.data T300_I60.data

./convert_IBM_to_TitanicOR.py T300_I40.data -o titanic_T300_I40.data
./convert_IBM_to_TitanicOR.py T300_I45.data -o titanic_T300_I45.data
./convert_IBM_to_TitanicOR.py T300_I50.data -o titanic_T300_I50.data
./convert_IBM_to_TitanicOR.py T300_I55.data -o titanic_T300_I55.data
./convert_IBM_to_TitanicOR.py T300_I60.data -o titanic_T300_I60.data
