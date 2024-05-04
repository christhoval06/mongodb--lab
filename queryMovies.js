db = connect( 'mongodb://localhost/films' );
printjson( db.movies.find( {} ) );