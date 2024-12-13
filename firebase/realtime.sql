-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uid VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    display_name VARCHAR(255),
    photo_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create posts table
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Create comments table
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Create a table for storing user authentication information if necessary
CREATE TABLE user_auth (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    provider VARCHAR(255) NOT NULL,
    provider_uid VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Create a table for storing user settings
CREATE TABLE user_settings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    settings JSONB,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO users (uid, email, display_name, photo_url) VALUES
('UID_123', 'user1@example.com', 'User One', 'http://example.com/photos/user1.jpg'),
('UID_456', 'user2@example.com', 'User Two', 'http://example.com/photos/user2.jpg');

INSERT INTO posts (user_id, title, content) VALUES
(1, 'First Post', 'This is the content of the first post'),
(2, 'Second Post', 'This is the content of the second post');

INSERT INTO comments (post_id, user_id, content) VALUES
(1, 2, 'This is a comment on the first post by the second user'),
(2, 1, 'This is a comment on the second post by the first user');
