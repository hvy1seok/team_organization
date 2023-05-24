import random

photo_members = ['원석', '세원', '예진', '유림', '성현', '희권']  # 포토멤버 리스트
team_count_2 = 4  # 2명인 팀 개수 설정
team_count_3 = 2  # 3명인 팀 개수 설정

model_parts = ['김경원', '김선혁', '김예인', '김지한', '나다애', '박세연', '이윤채', '장연조', '조서영', '한서진', '이시형', '김현진', '남의정', '안기백']  # 모델파트 멤버 리스트
other_parts = []  # 다른 파트 멤버 리스트

random.shuffle(photo_members)  # 포토멤버 리스트를 랜덤하게 섞음

# 팀 나누기
teams = [photo_members[i:i + (len(photo_members) // team_count_2)] for i in
         range(0, len(photo_members), len(photo_members) // team_count_2)]

# 팀에 팀장 포토멤버, 모든 모델파트 및 다른 파트 멤버 배정
for i, team in enumerate(teams):
    team_leader = team[0]  # 팀의 첫 번째 멤버를 팀장으로 설정
    if i < team_count_3:
        model_per_team = min(3, len(model_parts))  # 팀당 모델파트 멤버 수 (3명인 팀)
    else:
        model_per_team = min(2, len(model_parts))  # 팀당 모델파트 멤버 수 (2명인 팀)
    model_part = random.sample(model_parts, model_per_team)  # 팀에 배정될 모델파트 멤버 랜덤 선택
    for member in model_part:
        model_parts.remove(member)  # 배정된 모델파트 멤버 리스트에서 삭제
    #other_parts_count = len(team) - 1 - len(model_part)  # 팀장과 모델파트 멤버를 제외한 다른 파트 멤버 수 계산
    #other_parts = random.sample(other_parts, other_parts_count)  # 다른 파트 멤버들 랜덤 선택
    teams[i] = {'Team Leader': team_leader, 'Model Part': model_part, 'Other Parts': other_parts}

# 결과 출력
for i, team in enumerate(teams):
    print(f'Team {i + 1}:')
    print('Team Leader:', team['Team Leader'])
    print('Model Part:', team['Model Part'])
    # print('Other Parts:', team['Other Parts'])
    print()