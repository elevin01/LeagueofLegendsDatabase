CREATE TABLE SUMMONER_SPELL (
 name varchar(255), description varchar(255), cooldown int, primary key(name)
);

CREATE TABLE GAMEMODE (
  name varchar(255), release_date date, player_no int, primary key(name)
);

CREATE TABLE TOURNAMENT (
  name varchar(255), organizer  varchar(255), t_date date, gamemode varchar(255), 
  primary key (name, t_date), foreign key(gamemode) references GAMEMODE(name)
);

CREATE TABLE LOCATION (
  name varchar(255), main_race varchar(255), primary key(name)
);

CREATE TABLE MONSTER (
  name varchar(255), location varchar(255), type varchar(255), 
  foreign key (location) references LOCATION(name), primary key(name)
);

CREATE TABLE ITEM (
 name varchar(255), cost int, type varchar(255), description varchar(255), 
 primary key(name)
);

CREATE TABLE RUNE (
 name varchar(255), path varchar(255), is_keystone bool, description varchar(255), 
 primary key(name)
);

CREATE TABLE CHAMPION (
  name varchar(255), race varchar(255), BE_cost int, location varchar(255), class varchar(255), 
  best_item varchar(255), best_rune varchar(255),  
  foreign key (location) references LOCATION(name),  
  foreign key (best_item) references ITEM(name), 
  foreign key (best_rune) references RUNE(name), primary key(name)
);

CREATE TABLE SKIN (
 name varchar(255), RP_cost int, event varchar(255), champ varchar(255), 
 foreign key (champ) references CHAMPION(name), primary key(name)
);


CREATE TABLE PLAYER (
 username varchar(255), id char(4), main_lane varchar(255), ranks varchar(255), lvl int, main_champ varchar(255), 
 foreign key (main_champ) references CHAMPION(name), primary key(username, id)
);

CREATE TABLE GUILD (
 creator varchar(255), creator_id char(4), name varchar(255), lvl int, 
 foreign key (creator) references PLAYER(username), 
 primary key(creator, creator_id, name)
);

ALTER TABLE PLAYER ADD guild varchar(255);
ALTER TABLE PLAYER ADD foreign key(guild) references GUILD(name);

CREATE TABLE I_USABLE (
  gamemode varchar(255), item varchar(255), primary key (gamemode ,item), 
  foreign key(gamemode ) references GAMEMODE(name), foreign key(item) references ITEM(name)
);

CREATE TABLE BELONG (
 gamemode  varchar(255), monster varchar(255), primary key(gamemode, monster), 
 foreign key(gamemode) references GAMEMODE(name), foreign key(monster) references MONSTER(name)
);

CREATE TABLE SS_USABLE (
  gamemode  varchar(255), spell varchar(255), primary key (spell, gamemode), 
  foreign key(spell) references SUMMONER_SPELL(name), foreign key (gamemode) references GAMEMODE(name)
);

CREATE TABLE CHAMP_LANE (
  champ varchar(255), lane varchar(255), primary key (champ), 
  foreign key(champ) references CHAMPION(name)
);

CREATE TABLE OWN (
  player varchar(255), player_id char(4), skin varchar(255), primary key (player, player_id, skin), 
  foreign key(player) references PLAYER(username), 
  foreign key(skin) references SKIN(name) 
);

