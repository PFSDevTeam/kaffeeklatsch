BEGIN TRANSACTION;
DROP TABLE IF EXISTS "user_access";
CREATE TABLE IF NOT EXISTS "user_access" (
	"username"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("username")
);
DROP TABLE IF EXISTS "community";
CREATE TABLE IF NOT EXISTS "community" (
	"community"	TEXT NOT NULL,
	PRIMARY KEY("community")
);
DROP TABLE IF EXISTS "post";
CREATE TABLE IF NOT EXISTS "post" (
	"title"	TEXT NOT NULL,
	"content"	TEXT NOT NULL,
	"posting_user"	TEXT NOT NULL,
	"posted_date"	TEXT NOT NULL,
	"community"	TEXT NOT NULL,
	"UUID"	INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("UUID")
);
DROP TABLE IF EXISTS "user";
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT NOT NULL UNIQUE,
	"avatar"	TEXT,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"communities"	TEXT,
	"users_following"	TEXT,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "reply";
CREATE TABLE IF NOT EXISTS "reply" (
	"reply_UUID"	INTEGER NOT NULL UNIQUE,
	"original_post_id"	INTEGER NOT NULL,
	"reply_content"	TEXT NOT NULL,
	"reply_user"	TEXT NOT NULL,
	"reply_date"	TEXT NOT NULL,
	FOREIGN KEY("original_post_id") REFERENCES "post"("UUID"),
	PRIMARY KEY("reply_UUID")
);
INSERT INTO "user_access" ("username","password") VALUES ('steve','432c19c7ecdc9ef6884d01b21bd306ddd4b21d4ee139f10358cf5c1b7f113904');
INSERT INTO "user_access" ("username","password") VALUES ('francis','432c19c7ecdc9ef6884d01b21bd306ddd4b21d4ee139f10358cf5c1b7f113904');
INSERT INTO "user_access" ("username","password") VALUES ('daphne','432c19c7ecdc9ef6884d01b21bd306ddd4b21d4ee139f10358cf5c1b7f113904');
INSERT INTO "user_access" ("username","password") VALUES ('jane','432c19c7ecdc9ef6884d01b21bd306ddd4b21d4ee139f10358cf5c1b7f113904');
INSERT INTO "community" ("community") VALUES ('test');
INSERT INTO "post" ("title","content","posting_user","posted_date","community","UUID") VALUES ('Second','Post','francis','2021-09-27 11:08:38.835803','test',1);
INSERT INTO "post" ("title","content","posting_user","posted_date","community","UUID") VALUES ('Tastey','Treats','steve','2021-09-27 11:11:17.934762','test',2);
INSERT INTO "post" ("title","content","posting_user","posted_date","community","UUID") VALUES ('nitrogen','sickness','jane','2021-09-27 11:12:34.648271','test',3);
INSERT INTO "user" ("id","username","avatar","first_name","last_name","communities","users_following") VALUES (1,'steve','','','','','');
INSERT INTO "user" ("id","username","avatar","first_name","last_name","communities","users_following") VALUES (2,'francis',NULL,NULL,NULL,NULL,NULL);
INSERT INTO "user" ("id","username","avatar","first_name","last_name","communities","users_following") VALUES (3,'daphne',NULL,NULL,NULL,NULL,NULL);
INSERT INTO "user" ("id","username","avatar","first_name","last_name","communities","users_following") VALUES (4,'jane',NULL,NULL,NULL,NULL,NULL);
INSERT INTO "reply" ("reply_UUID","original_post_id","reply_content","reply_user","reply_date") VALUES (1,1,'Replyyyyiiiiinggg!','jane','2021-09-28 11:08:38.835803');
COMMIT;
