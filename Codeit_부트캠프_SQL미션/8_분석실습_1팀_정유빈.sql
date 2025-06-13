USE `fandom-k`;

# 사용자 정보 테이블 (사용자의 기본 정보)
CREATE TABLE `users` (						-- users 테이블 생성
	`u_id` INT AUTO_INCREMENT,				-- 사용자 고유번호
    `u_name` VARCHAR(50) NOT NULL UNIQUE,	-- 사용자 이름
    `u_credits` INT NOT NULL,				-- 사용자 크레딧
    PRIMARY KEY(`u_id`)
);

# 크레딧 로그 테이블 (사용자의 크래딧 사용/충전 내역 기록)
CREATE TABLE `credit_log` (									 -- credit_log 테이블 생성
	`cl_id` INT AUTO_INCREMENT,								 -- 크레딧로그 고유번호
    `cl_amount` INT NOT NULL,								 -- 크레딧로그 변화량
    `cl_type` ENUM('charge', 'vote', 'tribute') NOT NULL,	 -- 크레딧로그 사용타입 (충전, 투표, 조공)
    `cl_time` DATETIME NOT NULL,							 -- 크레딧로그 사용시간
    `u_id` INT NOT NULL,								     -- FK: u_id 설정
    PRIMARY KEY(`cl_id`),
    FOREIGN KEY(`u_id`) REFERENCES users(`u_id`)			 -- users 테이블에서 u_id 가져옴
		ON UPDATE CASCADE									 -- users.u_id 업데이트 시 해당 credit_log.u_id도 같이 업데이트
        ON DELETE CASCADE									 -- users.u_id 삭제 시 헤당 credit_log.u_id row 삭제
);

# 아티스트 테이블 (아티스트(아이돌) 정보 저장)
CREATE TABLE `artists` (						-- artists 테이블 생성
	`a_id`INT AUTO_INCREMENT, 					-- 아티스트 고유번호
    `a_name` VARCHAR(100) NOT NULL, 			-- 아티스트 이름 (동명이인 존재 가능성)
    `a_gender` ENUM('M', 'F') NOT NULL, 		-- 아티스트 성별
    `a_birth_date` DATE NOT NULL, 				-- 아티스트 생년월일
    `a_group_info` VARCHAR(100) NOT NULL,		-- 아티스트 소속그룹정보
    PRIMARY KEY(`a_id`)
);

# 투표 테이블 생성 (사용자가 아티스트에게 투표한 내역 저장)
CREATE TABLE `vote` (									-- vote 테이블 생성
	`v_id` INT AUTO_INCREMENT,							-- 투표 고유번호
    `v_start` DATE NOT NULL,						    -- 투표 시작 일자
    `v_end` DATE NOT NULL,								-- 투표 종료 일자
    `v_count` INT NOT NULL,								-- 투표 득표 수
    `u_id` INT NOT NULL,								-- FK: u_id 설정
    `a_id` INT NOT NULL,								-- FK: a_id 설정
    PRIMARY KEY(`v_id`),
    FOREIGN KEY(`u_id`) REFERENCES users(`u_id`)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY(`a_id`) REFERENCES artists(`a_id`)
		ON UPDATE CASCADE
        ON DELETE CASCADE
);

# 팔로우 테이블 생성 (사용자가 팔로우한 아티스트 정보 저장)
CREATE TABLE `follow` (									-- follow 테이블 생성
	`f_id` INT AUTO_INCREMENT,							-- 팔로우 고유번호
    `u_id` INT NOT NULL,								-- FK: u_id 설정
    `a_id` INT NOT NULL,								-- FK: a_id 설정
    PRIMARY KEY(`f_id`),
    FOREIGN KEY(`u_id`) REFERENCES users(`u_id`)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY(`a_id`) REFERENCES artists(`a_id`)
		ON UPDATE CASCADE
        ON DELETE CASCADE
);

# 소식 테이블 생성 (아티스트 관련 소식 제공)
CREATE TABLE `feed` (									-- feed 테이블 생성
	`fd_id` INT AUTO_INCREMENT,							-- 소식 고유번호
    `fd_type` VARCHAR(50) NOT NULL,						-- 소식 타입(생일, 앨범출시, 컴백...)
    `fd_title` VARCHAR(100) NOT NULL,					-- 소식 제목
    `fd_contents` TEXT NOT NULL,						-- 소식 내용
    `a_id` INT NOT NULL,								-- FK: a_id 설정
    PRIMARY KEY(`fd_id`),
    FOREIGN KEY(`a_id`) REFERENCES artists(`a_id`)
		ON UPDATE CASCADE
        ON DELETE CASCADE
);


# 차트 테이블 생성 (월간 이달의 아이돌 순위 저장(1 ~ 10위))
CREATE TABLE `chart` (														-- chart 테이블 생성		
	`ch_id` INT AUTO_INCREMENT,												-- 차트 고유번호
    `ch_category` ENUM('이달의 여자 아이돌', '이달의 남자 아이돌') NOT NULL,			-- 차트 카테고리 (이달의 여자 / 남자 아이돌)
    `ch_aotm_date` DATE NOT NULL,											-- 차트 이달의 아티스트 선전 날짜
    `ch_aotm_votes` INT NOT NULL,											-- 차트 이달의 아티스트 득표 수
    `ch_rank` TINYINT NOT NULL,												-- 차트 순위
    `a_id` INT NOT NULL,													-- FK: a_id 설정
    PRIMARY KEY(`ch_id`),
    CONSTRAINT `chk_rank_range` CHECK (ch_rank BETWEEN 1 AND 10),							 -- # 제약 추가 1: 순위는 1 ~ 10위 까지만 저장
    CONSTRAINT `uniq_artist_month_category` UNIQUE (ch_aotm_date, ch_category, a_id),		 -- # 제약 추가 2: 한 달에 한 아티스트가 중복으로 나오지 않도록 안전벨트 생성
    FOREIGN KEY(`a_id`) REFERENCES artists(`a_id`)
		ON UPDATE CASCADE
		ON DELETE CASCADE
); 


# 조공(후원) 테이블 생성 (아티스트 조공(후원 이벤트) 캠페인 정보 저장)
CREATE TABLE `tribute` (								-- tribute 테이블 생성
	`t_id` INT AUTO_INCREMENT,							-- 조공 고유번호
    `t_category` VARCHAR(50) NOT NULL,					-- 조공 카테고리 (지하철 옥외 광고, 생일 이벤트...)
    `t_start` DATE NOT NULL,							-- 조공 후원모금 시작 일자
    `t_end` DATE NOT NULL,								-- 조공 후원모금 종료 일자
    `t_target` INT NOT NULL,							-- 조공 목표 후원금
    `t_is_completed` TINYINT(1) NOT NULL,				-- 조공 목표 후원금 달성여부 (불린식 0 = 진행 중, 1 = 달성)
    `a_id` INT NOT NULL,								-- FK: a_id 설정
    PRIMARY KEY(`t_id`),
    FOREIGN KEY(`a_id`) REFERENCES artists(`a_id`)
		ON UPDATE CASCADE
        ON DELETE CASCADE
);

# 조공지원 테이블 생성 (사용자가 조공 캠패인에 후원한 내역 저장)
CREATE TABLE `tribute_support` (						-- tribute_support 테이블 생성
	`s_id` INT AUTO_INCREMENT,							-- 조공지원 고유번호
    `s_amount` INT NOT NULL,							-- 조공지원 크레딧량
    `s_time` DATETIME NOT NULL,							-- 조공지원 후원시간
    `u_id` INT NOT NULL,								-- FK: u_id 설정
    `a_id` INT NOT NULL,								-- FK: a_id 설정
    PRIMARY KEY(`s_id`),
    FOREIGN KEY(`u_id`) REFERENCES users(`u_id`)
		ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY(`a_id`) REFERENCES artists(`a_id`)
		ON UPDATE CASCADE
        ON DELETE CASCADE
);