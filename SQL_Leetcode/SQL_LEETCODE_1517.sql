
SELECT *
FROM Users
WHERE mail COLLATE utf8mb3_bin
  REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$';

-- Redone: In MySQL you can use BINARY with REGEXP to force case sensitivity,
-- but on LeetCode the Users.mail column uses a utf8mb3/utf8mb4 collation.
-- Mixing BINARY with REGEXP causes a charset conflict.
-- Instead, apply a case-sensitive collation (e.g., utf8mb3_bin / utf8mb4_bin)
-- directly to the column to avoid mixing character sets.
