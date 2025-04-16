-- 郵件：驗證郵件Token表
CREATE TABLE student_verifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    student_id VARCHAR(50),
    token VARCHAR(64),
    token_expiry BIGINT,
    verified BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 郵件：學校地址表
CREATE TABLE school_domains (
    id INT AUTO_INCREMENT PRIMARY KEY,
    domain VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL
);

-- 留言板：留言表
CREATE TABLE board_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    school VARCHAR(100) NOT NULL,
    author_name VARCHAR(100), -- 若匿名，為 NULL
    likes INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 留言板：回覆表
CREATE TABLE board_replies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message_id INT NOT NULL,
    content TEXT NOT NULL,
    school VARCHAR(100) NOT NULL,
    author_name VARCHAR(100), -- 若匿名，為 NULL
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (message_id) REFERENCES board_messages(id) ON DELETE CASCADE
);