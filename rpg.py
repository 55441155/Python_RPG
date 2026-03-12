import random

# 직업과 몬스터 설정
jobs = ["전사", "궁수", "마법사", "도적"]
job = random.choice(jobs)
print("직업:", job)

monsters = ["슬라임", "좀비", "스켈레톤", "블레이즈"]
monster = random.choice(monsters)
print(monster, "을(를) 만났습니다!")

# 체력 설정
player_hp = 100
monster_hp = random.randint(20, 40)

# 경험치 / 레벨
xp = 0
level = 1

# 공격력 설정
if job == "전사":
    attack = 15
elif job == "궁수":
    attack = 12
elif job == "마법사":
    attack = 18
elif job == "도적":
    attack = 20

print("내 공격력:", attack)
print("내 체력:", player_hp)
print(monster, "체력:", monster_hp)

# 🔹 직업별 스킬 설정
if job == "마법사":
    skill = "화염구"
    skill_damage = attack + 5
elif job == "도적":
    skill = "암살"
    skill_damage = attack + 7
else:
    skill = "없음"
    skill_damage = attack

# 🔹 전투 반복 시작
while monster_hp > 0 and player_hp > 0:

    action = input("1 공격 2 스킬 3 도망 > ")

    if action == "1":
        # 일반 공격
        monster_hp -= attack
        print("공격!")
        print
        (monster, "남은 체력:", monster_hp)

    elif action == "2":
        if skill != "없음":
            monster_hp -= skill_damage
            print(skill, "사용!")
            print(monster, "남은 체력:", monster_hp)
        else:
            print("스킬이 없습니다. 일반 공격이 됩니다.")
            monster_hp -= attack
            print("공격!")
            print(monster, "남은 체력:", monster_hp)

    elif action == "3":
        print("도망쳤습니다!")
        break

    # 몬스터 처치 확인
    if monster_hp <= 0:
        print(monster, "처치!")
        gained_xp = random.randint(5, 20)
        xp += gained_xp
        print("경험치 +", gained_xp)
        if xp >= 20:
            level += 1
            xp = 0
            print("레벨업! 현재 레벨:", level)
        break

    # 몬스터 반격
    monster_attack = random.randint(5, 15)
    player_hp -= monster_attack
    print(monster, "공격!")
    print("내 체력:", player_hp)

    # 플레이어 패배 확인
    if player_hp <= 0:
        print("패배했습니다!")
        break