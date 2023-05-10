CREATE TABLE SUMMONER_SPELL (
 name varchar(255), description varchar(255), cooldown int, primary key(name)
);

CREATE TABLE GAMEMODE (
  name varchar(255), release_date date, player_no int, primary key(name)
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
  name varchar(255), race varchar(255), BE_cost int, 
  location varchar(255), class varchar(255), 
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
 username varchar(255), id char(4), main_lane varchar(255), 
 ranks varchar(255), lvl int, main_champ varchar(255), 
 g_creator varchar(255),
 g_cid char(4),
 foreign key (main_champ) references CHAMPION(name), 
 foreign key (g_creator) references PLAYER(username),
 foreign key (g_cid) references PLAYER(id),
 primary key(username, id)
);

CREATE TABLE GUILD (
 creator varchar(255), creator_id char(4),
 name varchar(255), lvl int, 
 foreign key (creator) references PLAYER(username), 
 foreign key (creator_id) references PLAYER(id), 
 primary key(creator, name, creator_id)
);

CREATE TABLE TOURNAMENT (
  name varchar(255), t_date date, gamemode varchar(255), 
  g1_creator varchar(255), g1_name varchar(255), g1_cid char(4),
  g2_creator varchar(255), g2_name varchar(255), g2_cid char(4),
  primary key (name, t_date), 
  foreign key(gamemode) references GAMEMODE(name),
  foreign key(g1_creator, g1_cid, g1_name) references GUILD(creator, creator_id, name), 
  foreign key(g2_creator, g2_cid, g2_name) references GUILD(creator, creator_id, name)
);

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
  champ varchar(255), lane varchar(255), primary key (champ, lane), 
  foreign key(champ) references CHAMPION(name)
);

CREATE TABLE OWN (
  player varchar(255), player_id char(4), 
  skin varchar(255), primary key (player, skin), 
  foreign key(player) references PLAYER(username), 
  foreign key(player_id) references PLAYER(id), 
  foreign key(skin) references SKIN(name) 
);

INSERT INTO SUMMONER_SPELL  VALUES ('Heal', 'Heals yourself and an ally', 240);
INSERT INTO SUMMONER_SPELL  VALUES ('Ghost', 'Gives movement speed and ignores unit collision, resets on kill', 210);
INSERT INTO SUMMONER_SPELL  VALUES ('Barrier', 'Gives a shield', 180);
INSERT INTO SUMMONER_SPELL  VALUES ('Mark', 'Throws a snowball that can recast to', 180);
INSERT INTO SUMMONER_SPELL VALUES ('Cleanse', 'Removes all crowd control debuffs and summoner spell debuffs', 210);
INSERT INTO SUMMONER_SPELL VALUES ('Ignite', 'Deals true damage over time and reduces healing effects', 180);
INSERT INTO SUMMONER_SPELL VALUES ('Exhaust', 'Reduces the target enemy champion''s damage output and slows them', 210);
INSERT INTO SUMMONER_SPELL VALUES ('Flash', 'Teleports your champion a short distance towards the cursor', 300);
INSERT INTO SUMMONER_SPELL VALUES ('Teleport', 'Teleports your champion to an allied turret, minion, or ward', 360);
INSERT INTO SUMMONER_SPELL VALUES ('Smite', 'Deals true damage to monsters or enemy minions, healing you and granting bonus gold', 15);
INSERT INTO SUMMONER_SPELL VALUES ('Clarity', 'Restores mana to you and nearby allies', 240);


INSERT INTO GAMEMODE VALUES ('Summoner''s Rift', '2009-10-27', 10);
INSERT INTO GAMEMODE VALUES ('ARAM', '2010-06-29', 10);
INSERT INTO GAMEMODE VALUES ('Twisted Treeline', '2009-10-27', 6);
INSERT INTO GAMEMODE VALUES ('Urf', '2010-04-01', 10);
INSERT INTO GAMEMODE VALUES ('One for All', '2013-05-29', 10);

INSERT INTO LOCATION VALUES ('Summoner''s Rift', 'None');
INSERT INTO LOCATION VALUES ('Freljord', 'Human');
INSERT INTO LOCATION VALUES ('Demacia', 'Human');
INSERT INTO LOCATION VALUES ('Ionia', 'Vastayan');
INSERT INTO LOCATION VALUES ('Icathia', 'Void being');
INSERT INTO LOCATION VALUES ('Bandle City', 'Yordle');
INSERT INTO LOCATION VALUES ('Bilgewater', 'Mixed');
INSERT INTO LOCATION VALUES ('Noxus', 'Human');

INSERT INTO MONSTER VALUES ('Baron Nashor', 'Summoner''s Rift', 'Epic Monster');
INSERT INTO MONSTER VALUES ('Dragon', 'Summoner''s Rift', 'Epic Monster');
INSERT INTO MONSTER VALUES ('Rift Herald', 'Summoner''s Rift', 'Epic Monster');
INSERT INTO MONSTER VALUES ('Elder Dragon', 'Summoner''s Rift', 'Epic Monster');
INSERT INTO MONSTER VALUES ('Blue Sentinel', 'Summoner''s Rift', 'Buff Monster');

INSERT INTO ITEM VALUES ('Infinity Edge', 3400, 'Marksman', 'Increases critical strike damage');
INSERT INTO ITEM VALUES ('Zhonya''s Hourglass', 2900, 'Mage', 'Provides a stasis effect');
INSERT INTO ITEM VALUES ('Guardian Angel', 2800, 'Fighter', 'Revives your champion upon death');
INSERT INTO ITEM VALUES ('Thornmail', 2900, 'Tank', 'Reflects damage taken from basic attacks');
INSERT INTO ITEM VALUES ('Trinity Force', 3733, 'Fighter', 'Provides various stats and sheen attack');

INSERT INTO RUNE VALUES ('Conqueror', 'Precision', true, 'Gain stacks of AD or AP when damaging enemy champions');
INSERT INTO RUNE VALUES ('Electrocute', 'Domination', true, 'Deal bonus damage after hitting an enemy with 3 separate abilities or attacks');
INSERT INTO RUNE VALUES ('Aftershock', 'Resolve', true, 'Gain bonus resistances after immobilizing an enemy champion');
INSERT INTO RUNE VALUES ('Arcane Comet', 'Sorcery', true, 'Deal damage to enemy champions with abilities, periodically');
INSERT INTO RUNE VALUES ('Grasp of the Undying', 'Resolve', true, 'Gain bonus health and deal damage to enemy champions with basic attacks');

INSERT INTO CHAMPION VALUES ('Ashe', 'Human', 450, 'Freljord', 'Marksman', 'Infinity Edge', 'Conqueror');
INSERT INTO CHAMPION VALUES ('Lux', 'Human', 3150, 'Demacia', 'Mage', 'Zhonya''s Hourglass', 'Arcane Comet');
INSERT INTO CHAMPION VALUES ('Darius', 'Human', 4800, 'Noxus', 'Fighter', 'Guardian Angel', 'Conqueror');
INSERT INTO CHAMPION VALUES ('Nautilus', 'Void Being', 4800, 'Bilgewater', 'Tank', 'Thornmail', 'Aftershock');
INSERT INTO CHAMPION VALUES ('Garen', 'Human', 450, 'Demacia', 'Fighter', 'Trinity Force', 'Grasp of the Undying');










































