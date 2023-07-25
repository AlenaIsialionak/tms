CREATE UNIQUE INDEX "users_personal_info_unique" ON users (name, age, gender, nationality);
CREATE INDEX "like_2" ON likes (user_id, post_id);