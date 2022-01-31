
install:
	cp ./examples/pg_service.conf_example ./backend/.pg_service.conf
	cp ./examples/pgpass_example ./backend/.pgpass
	chmod 400 ./backend/.pgpass
