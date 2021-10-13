BEGIN TRANSACTION;
DROP TABLE IF EXISTS "user_access";
CREATE TABLE IF NOT EXISTS "user_access" (
	"username"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("username")
);
DROP TABLE IF EXISTS "reply";
CREATE TABLE IF NOT EXISTS "reply" (
	"reply_UUID"	INTEGER NOT NULL UNIQUE,
	"original_post_id"	INTEGER NOT NULL,
	"reply_content"	TEXT NOT NULL,
	"reply_user"	TEXT NOT NULL,
	"reply_date"	TEXT NOT NULL,
	PRIMARY KEY("reply_UUID"),
	FOREIGN KEY("original_post_id") REFERENCES "post"("UUID")
);
DROP TABLE IF EXISTS "post";
CREATE TABLE IF NOT EXISTS "post" (
	"title"	TEXT NOT NULL,
	"content"	TEXT NOT NULL,
	"posting_user"	TEXT NOT NULL,
	"posted_date"	TEXT NOT NULL,
	"community"	TEXT NOT NULL,
	"UUID"	INTEGER NOT NULL UNIQUE,
	"tally"	INTEGER NOT NULL,
	PRIMARY KEY("UUID")
);
DROP TABLE IF EXISTS "user";
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT NOT NULL UNIQUE,
	"avatar"	TEXT DEFAULT bee_avatar.png,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"communities"	TEXT,
	"users_following"	TEXT,
	"tagline"	TEXT,
	"date_joined"	TEXT NOT NULL,
	"summary"	TEXT,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "community";
CREATE TABLE IF NOT EXISTS "community" (
	"community_id"	INTEGER NOT NULL,
	"community_name"	TEXT NOT NULL DEFAULT '"test',
	"community_tagline"	TEXT NOT NULL DEFAULT test,
	"community_content"	TEXT NOT NULL DEFAULT test,
	"community_image"	TEXT NOT NULL DEFAULT test,
	"community_datejoined"	TEXT NOT NULL,
	PRIMARY KEY("community_id")
);
INSERT INTO "user_access" ("username","password") VALUES ('steve','432c19c7ecdc9ef6884d01b21bd306ddd4b21d4ee139f10358cf5c1b7f113904');
INSERT INTO "user_access" ("username","password") VALUES ('francis','432c19c7ecdc9ef6884d01b21bd306ddd4b21d4ee139f10358cf5c1b7f113904');
INSERT INTO "user_access" ("username","password") VALUES ('daphne','432c19c7ecdc9ef6884d01b21bd306ddd4b21d4ee139f10358cf5c1b7f113904');
INSERT INTO "user_access" ("username","password") VALUES ('jane','432c19c7ecdc9ef6884d01b21bd306ddd4b21d4ee139f10358cf5c1b7f113904');
INSERT INTO "user_access" ("username","password") VALUES ('emily','ffbe87bd1cf4123490b88ad35fb40819c0bfaf9026ec1e801d0b7d62aed45e08');
INSERT INTO "reply" ("reply_UUID","original_post_id","reply_content","reply_user","reply_date") VALUES (1,1,'Replyyyyiiiiinggg!','jane','2021-09-28 11:08:38.835803');
INSERT INTO "reply" ("reply_UUID","original_post_id","reply_content","reply_user","reply_date") VALUES (2,3,'Nickle','steve','2021-10-10 02:17:08.425172');
INSERT INTO "post" ("title","content","posting_user","posted_date","community","UUID","tally") VALUES ('Second','Post','francis','2021-09-27 11:08:38.835803','test',1,0);
INSERT INTO "post" ("title","content","posting_user","posted_date","community","UUID","tally") VALUES ('Tastey','Treats','steve','2021-09-27 11:11:17.934762','test',2,0);
INSERT INTO "post" ("title","content","posting_user","posted_date","community","UUID","tally") VALUES ('nitrogen','sickness','jane','2021-09-27 11:12:34.648271','test',3,0);
INSERT INTO "post" ("title","content","posting_user","posted_date","community","UUID","tally") VALUES ('Title','content test','steve','2021-10-10 01:55:49.726935','Test Community',4,0);
INSERT INTO "post" ("title","content","posting_user","posted_date","community","UUID","tally") VALUES ('Hi there','Apple Computers are mediocre at best','steve','2021-10-10 02:16:40.508560','Test Community',5,0);
INSERT INTO "user" ("id","username","avatar","first_name","last_name","communities","users_following","tagline","date_joined","summary") VALUES (1,'steve','lion_avatar.png','','','','','new tag for steve','2021-09-27 11:08:38.835803','test1');
INSERT INTO "user" ("id","username","avatar","first_name","last_name","communities","users_following","tagline","date_joined","summary") VALUES (2,'francis','whale_avatar.png','','','','','this is francis','2021-09-27 11:08:38.835803','test2');
INSERT INTO "user" ("id","username","avatar","first_name","last_name","communities","users_following","tagline","date_joined","summary") VALUES (3,'daphne','spider_avatar.png',NULL,NULL,NULL,NULL,'this is daphne','2021-09-27 11:08:38.835803','test3');
INSERT INTO "user" ("id","username","avatar","first_name","last_name","communities","users_following","tagline","date_joined","summary") VALUES (4,'jane','koala_avatar.png',NULL,NULL,NULL,NULL,'this is jane','2021-09-27 11:08:38.835803','test4');
INSERT INTO "user" ("id","username","avatar","first_name","last_name","communities","users_following","tagline","date_joined","summary") VALUES (5,'emily','elephant_avatar.png',NULL,NULL,NULL,NULL,'new tagline','2021-10-10 03:42:04.147910','test5');
INSERT INTO "community" ("community_id","community_name","community_tagline","community_content","community_image","community_datejoined") VALUES (1,'Books are Best','reading is love,  reading is life','If you like to read, this is the group for you! Post about your favorite books and we can share our literary journey together','bee_avatar.png','2021-09-27 11:08:38.835803');
INSERT INTO "community" ("community_id","community_name","community_tagline","community_content","community_image","community_datejoined") VALUES (2,'Coffee Lovers International','coffee is life!','The world runs on hot, caffienated bean juice, and so do we','koala_avatar.png','2021-09-27 11:08:38.835803');
INSERT INTO "community" ("community_id","community_name","community_tagline","community_content","community_image","community_datejoined") VALUES (3,'Movie Fanatics','cinema fans unite','Let''s talk about the latest films, cinematic art at it''s finest is loved by us!','lion_avatar.png','2021-09-27 11:08:38.835803');
INSERT INTO "community" ("community_id","community_name","community_tagline","community_content","community_image","community_datejoined") VALUES (4,'SportsBall','this group loves sportsball','Round, flat, or in between, join us in cheering or booing teams, sportsball or nothing!','frog_avatar.png','2021-09-27 11:08:38.835803');
INSERT INTO "community" ("community_id","community_name","community_tagline","community_content","community_image","community_datejoined") VALUES (5,'Code Center','help.exe','Share your code, get your burning questions answered!','macaw_avatar.png','2021-09-27 11:08:38.835803');
COMMIT;
