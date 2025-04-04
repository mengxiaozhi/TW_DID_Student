CREATE TABLE student_verifications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  student_id VARCHAR(50),
  token VARCHAR(64),
  token_expiry BIGINT,
  verified BOOLEAN DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
