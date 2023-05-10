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
  g1_creator varchar(255), g1_cid char(4), g1_name varchar(255),
  g2_creator varchar(255), g2_cid char(4), g2_name varchar(255),
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
  skin varchar(255), primary key (player, player_id, skin), 
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
INSERT INTO LOCATION VALUES ('Piltover', 'Human');

INSERT INTO MONSTER VALUES ('Baron Nashor', 'Summoner''s Rift', 'Epic Monster');
INSERT INTO MONSTER VALUES ('Dragon', 'Summoner''s Rift', 'Epic Monster');
INSERT INTO MONSTER VALUES ('Rift Herald', 'Summoner''s Rift', 'Epic Monster');
INSERT INTO MONSTER VALUES ('Elder Dragon', 'Summoner''s Rift', 'Epic Monster');
INSERT INTO MONSTER VALUES ('Lane Minion', 'Summoner''s Rift', 'Creep');
INSERT INTO MONSTER VALUES ('Poro', 'Freljord', 'Pet');
INSERT INTO MONSTER VALUES ('Blue Sentinel', 'Summoner''s Rift', 'Buff Monster');

INSERT INTO ITEM VALUES ('Infinity Edge', 3400, 'Marksman', 'Increases critical strike damage');
INSERT INTO ITEM VALUES ('Zhonya''s Hourglass', 2900, 'Mage', 'Provides a stasis effect');
INSERT INTO ITEM VALUES ('Guardian Angel', 2800, 'Fighter', 'Revives your champion upon death');
INSERT INTO ITEM VALUES ('Thornmail', 2900, 'Tank', 'Reflects damage taken from basic attacks');
INSERT INTO ITEM VALUES ('Trinity Force', 3733, 'Fighter', 'Provides various stats and sheen attack');
INSERT INTO ITEM VALUES ('Duskblade of Draktharr', 2900, 'Assassin', 'Provides lethality and burst damage');
INSERT INTO ITEM VALUES ('Sunfire Aegis', 3200, 'Tank', 'Grants bonus health and deals damage to nearby enemies');
INSERT INTO ITEM VALUES ('Manamune', 2400, 'Marksman', 'Provides bonus attack damage and mana');
INSERT INTO ITEM VALUES ('Luden''s Echo', 3200, 'Mage', 'Grants ability power and bonus burst damage');
INSERT INTO ITEM VALUES ('Guardian''s Blade', 3200, 'Fighter', 'Gives good stats to start with');


INSERT INTO RUNE VALUES ('Conqueror', 'Precision', true, 'Gain stacks of AD or AP when damaging enemy champions');
INSERT INTO RUNE VALUES ('Electrocute', 'Domination', true, 'Deal bonus damage after hitting an enemy with 3 separate abilities or attacks');
INSERT INTO RUNE VALUES ('Aftershock', 'Resolve', true, 'Gain bonus resistances after immobilizing an enemy champion');
INSERT INTO RUNE VALUES ('Arcane Comet', 'Sorcery', true, 'Deal damage to enemy champions with abilities, periodically');
INSERT INTO RUNE VALUES ('Grasp of the Undying', 'Resolve', true, 'Gain bonus health and deal damage to enemy champions with basic attacks');
INSERT INTO RUNE VALUES ('First Strike', 'Inspiration', true, 'Grants bonus damage and some gold if you hit an enemy before you are hit');


INSERT INTO CHAMPION VALUES ('Ashe', 'Human', 450, 'Freljord', 'Marksman', 'Infinity Edge', 'Conqueror');
INSERT INTO CHAMPION VALUES ('Lux', 'Human', 3150, 'Demacia', 'Mage', 'Zhonya''s Hourglass', 'Arcane Comet');
INSERT INTO CHAMPION VALUES ('Darius', 'Human', 4800, 'Noxus', 'Fighter', 'Guardian Angel', 'Conqueror');
INSERT INTO CHAMPION VALUES ('Nautilus', 'Void Being', 4800, 'Bilgewater', 'Tank', 'Thornmail', 'Aftershock');
INSERT INTO CHAMPION VALUES ('Garen', 'Human', 450, 'Demacia', 'Fighter', 'Trinity Force', 'Grasp of the Undying');
INSERT INTO CHAMPION VALUES ('Zed', 'Human', 6300, 'Ionia', 'Assassin', 'Duskblade of Draktharr', 'Electrocute');
INSERT INTO CHAMPION VALUES ('Sion', 'Undead', 1350, 'Noxus', 'Tank', 'Sunfire Aegis', 'Grasp of the Undying');
INSERT INTO CHAMPION VALUES ('Draven', 'Human', 6300, 'Noxus', 'Marksman', 'Infinity Edge', 'Conqueror');
INSERT INTO CHAMPION VALUES ('Ezreal', 'Human', 4800, 'Piltover', 'Marksman', 'Manamune', 'Conqueror');
INSERT INTO CHAMPION VALUES ('LeBlanc', 'Human', 3150, 'Noxus', 'Mage', 'Luden''s Echo', 'Electrocute');


INSERT INTO SKIN VALUES ('Freljord Ashe', 1350, 'Winter Event', 'Ashe');
INSERT INTO SKIN VALUES ('Elementalist Lux', 3250, 'Legendary Event', 'Lux');
INSERT INTO SKIN VALUES ('Dreadnova Darius', 1350, 'Space-themed Event', 'Darius');
INSERT INTO SKIN VALUES ('Abyssal Nautilus', 1350, 'Underwater Event', 'Nautilus');
INSERT INTO SKIN VALUES ('Steel Legion Garen', 975, 'Military-themed Event', 'Garen');

INSERT INTO PLAYER VALUES ('Faker', '1234', 'Mid', 'Challenger', 765, 'Zed', 'Faker', '1234');
INSERT INTO PLAYER VALUES ('thebausffs', '5678', 'Top', 'Grandmaster', 468, 'Sion', 'Faker', '1234');
INSERT INTO PLAYER VALUES ('Tyler1', '9012', 'ADC', 'Challenger', 840, 'Draven', 'Tyler1', '9012');
INSERT INTO PLAYER VALUES ('Doublelift', '3456', 'ADC', 'Grandmaster', 648, 'Ezreal', 'Tyler1', '9012');
INSERT INTO PLAYER VALUES ('Caps', '7890', 'Mid', 'Challenger', 234, 'LeBlanc', 'Tyler1', '9012');
INSERT INTO PLAYER VALUES ('XxZazaDemonxX', '4200', 'Support', 'Bronze', 34, 'Nautilus', 'XxZazaDemonxX', '4200');
INSERT INTO PLAYER VALUES ('JuiceLord', '6969', 'ADC', 'Platinum', 34, 'Ashe', 'XxZazaDemonxX', '4200');

INSERT INTO GUILD VALUES ('Faker', '1234', 'SKT T1', 10);
INSERT INTO GUILD VALUES ('Tyler1', '9012', 'Alpha Draven', 8);
INSERT INTO GUILD VALUES ('XxZazaDemonxX', '4200', 'Trash', 1);

INSERT INTO TOURNAMENT VALUES ('World Championship', '2023-11-01', 'Summoner''s Rift', 'Faker', '1234', 'SKT T1', 'Tyler1', '9012', 'Alpha Draven');
INSERT INTO TOURNAMENT VALUES ('Grand Slam Tournament', '2023-09-15', 'ARAM', 'Faker', '1234', 'SKT T1', 'XxZazaDemonxX', '4200', 'Trash');
INSERT INTO TOURNAMENT VALUES ('Draven Showdown', '2023-10-10', 'One for All', 'Tyler1', '9012', 'Alpha Draven', 'XxZazaDemonxX', '4200', 'Trash');

INSERT INTO I_USABLE VALUES 
('Summoner''s Rift', 'Infinity Edge'), ('Summoner''s Rift', 'Zhonya''s Hourglass'),
('Summoner''s Rift', 'Guardian Angel'),('Summoner''s Rift', 'Thornmail'), ('Summoner''s Rift', 'Trinity Force'),
('Summoner''s Rift', 'Duskblade of Draktharr'), ('Summoner''s Rift', 'Sunfire Aegis'),
('Summoner''s Rift', 'Manamune'), ('Summoner''s Rift', 'Luden''s Echo'),
('ARAM', 'Infinity Edge'), ('ARAM', 'Zhonya''s Hourglass'), ('ARAM', 'Thornmail'),
('ARAM', 'Trinity Force'), ('ARAM', 'Duskblade of Draktharr'), ('ARAM', 'Sunfire Aegis'),
('ARAM', 'Manamune'), ('ARAM', 'Luden''s Echo'), ('ARAM', 'Guardian''s Blade'),
('Twisted Treeline', 'Infinity Edge'), ('Twisted Treeline', 'Zhonya''s Hourglass'),
('Twisted Treeline', 'Guardian Angel'), ('Twisted Treeline', 'Thornmail'),
('Twisted Treeline', 'Trinity Force'), ('Twisted Treeline', 'Duskblade of Draktharr'),
('Twisted Treeline', 'Sunfire Aegis'), ('Twisted Treeline', 'Manamune'),
('Twisted Treeline', 'Luden''s Echo'), ('Urf', 'Infinity Edge'),
('Urf', 'Zhonya''s Hourglass'), ('Urf', 'Guardian Angel'), ('Urf', 'Thornmail'),
('Urf', 'Trinity Force'), ('Urf', 'Duskblade of Draktharr'), ('Urf', 'Sunfire Aegis'),
('Urf', 'Manamune'), ('Urf', 'Luden''s Echo'),
('One for All', 'Infinity Edge'), ('One for All', 'Zhonya''s Hourglass'),
('One for All', 'Guardian Angel'), ('One for All', 'Thornmail'),
('One for All', 'Trinity Force'), ('One for All', 'Duskblade of Draktharr'),
('One for All', 'Sunfire Aegis'), ('One for All', 'Manamune'), ('One for All', 'Luden''s Echo');

INSERT INTO BELONG VALUES ('Summoner''s Rift', 'Baron Nashor');
INSERT INTO BELONG VALUES ('Summoner''s Rift', 'Dragon');
INSERT INTO BELONG VALUES ('Summoner''s Rift', 'Rift Herald');
INSERT INTO BELONG VALUES ('Summoner''s Rift', 'Elder Dragon');
INSERT INTO BELONG VALUES ('Summoner''s Rift', 'Blue Sentinel');
INSERT INTO BELONG VALUES ('Summoner''s Rift', 'Lane Minion');
INSERT INTO BELONG VALUES ('ARAM', 'Poro');
INSERT INTO BELONG VALUES ('ARAM', 'Lane Minion');

INSERT INTO SS_USABLE VALUES 
('Summoner''s Rift', 'Flash'),('Summoner''s Rift', 'Ignite'), ('Summoner''s Rift', 'Barrier'),
('Summoner''s Rift', 'Smite'), ('Summoner''s Rift', 'Ghost'),('Summoner''s Rift', 'Heal'),
('Summoner''s Rift', 'Cleanse'),('Summoner''s Rift', 'Exhaust'), ('Summoner''s Rift', 'Teleport'),
('ARAM', 'Heal'), ('ARAM', 'Ignite'), ('ARAM', 'Flash'), ('ARAM', 'Ghost'), ('ARAM', 'Barrier'),
('ARAM', 'Mark'), ('ARAM', 'Cleanse'), ('ARAM', 'Exhaust'), ('ARAM', 'Clarity'),
('Twisted Treeline', 'Flash'), ('Twisted Treeline', 'Ghost'), ('Twisted Treeline', 'Heal'),
('Twisted Treeline', 'Ignite'), ('Twisted Treeline', 'Barrier'), 
('Urf', 'Heal'), ('Urf', 'Ghost'), ('Urf', 'Flash'),
('Urf', 'Ignite'), ('Urf', 'Barrier'),
('One for All', 'Flash'), ('One for All', 'Ghost'), ('One for All', 'Heal'), 
('One for All', 'Ignite'),('One for All', 'Barrier');

INSERT INTO CHAMP_LANE VALUES 
('Ashe', 'ADC'), ('Ashe', 'Sup'), ('Ashe', 'Mid'),
('Lux', 'Sup'), ('Lux', 'Mid'),
('Darius', 'Top'), ('Darius', 'Jungle'),
('Nautilus', "Jungle"), ('Nautilus', "Sup"),
('Garen', 'Top'), ('Garen', 'Mid'),
('Zed', 'Jungle'), ('Zed', 'Mid'),
('Sion', 'Top'), ('Sion', 'Sup'), ('Sion', 'Mid'), ('Sion', 'Jungle'),
('Draven', 'ADC'), 
('Ezreal', 'ADC'), ('Ezreal', 'Mid'),
('LeBlanc', 'Mid');

INSERT INTO OWN VALUES 
('Faker', '1234', 'Freljord Ashe'), ('Faker', '1234', 'Elementalist Lux'),
('Faker', '1234', 'Dreadnova Darius'), ('Faker', '1234', 'Abyssal Nautilus'),
('Faker', '1234', 'Steel Legion Garen'),
('thebausffs', '5678', 'Elementalist Lux'),
('Tyler1', '9012', 'Abyssal Nautilus'),('Tyler1', '9012', 'Dreadnova Darius'), 
('XxZazaDemonxX', '4200', 'Abyssal Nautilus'),('XxZazaDemonxX', '4200', 'Elementalist Lux'),
('JuiceLord', '6969', 'Freljord Ashe'), 
('Doublelift', '3456', 'Freljord Ashe'),
('Caps', '7890', 'Dreadnova Darius'), ('Caps', '7890', 'Steel Legion Garen');

