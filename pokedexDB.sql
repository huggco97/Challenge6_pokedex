DROP DATABASE IF EXISTS pokedexDB ;

CREATE DATABASE pokedexDB ;

USE pokedexDB ;
CREATE TABLE Pokemon (
	id_pokemon int NOT NULL auto_increment primary key,
    nombre_poke varchar (50) NOT NULL,
    tipo varchar (50) NOT NULL,
    habilidad varchar (150) NOT NULL,
    estadisticas float NOT NULL
); 

CREATE TABLE Entrenador (
	id_entrenador int NOT NULL auto_increment primary key,
    nombre_entr varchar (100) NOT NULL,
    ciudad varchar (50) NOT NULL,
    edad int NOT NULL
);

CREATE TABLE Batalla (
	id_batalla int NOT NULL auto_increment primary key,
	id_entrenador int NOT NULL,
    id_pokemon int NOT NULL,
    nombre_poke varchar (50) NOT NULL,
    nombre_entr varchar (100) NOT NULL,
    fecha date NULL,
    resultado int NOT NULL,
    
    foreign key(id_entrenador) references Entrenador (id_entrenador),
    foreign key(id_pokemon) references Pokemon (id_pokemon)
    );
    
CREATE TABLE Intermedia (
	id_entrenador int NOT NULL,
    id_pokemon int NOT NULL,
    nombre_entr varchar (100) NOT NULL,
    
    primary key ( id_entrenador, id_pokemon),
    foreign key (id_entrenador) references Entrenador (id_entrenador),
    foreign key (id_pokemon) references Pokemon (id_pokemon)
);