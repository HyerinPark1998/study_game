import random
import time

# 캐릭터의 모체가 되는 클래쓰


class Character:
    def __init__(self, name, hp, mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = random.randint(10, 15)
        self.m_power = random.randint(15, 20)

    def attack(self, other, damage, skill):
        other.hp = max(other.hp - damage, 0)
        print(
            f"\n{self.job} {self.name}의 {skill} 공격!!!\n{other.name}에게 {damage}의 데미지를 입혔습니다.")
        print(" ")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def magic_attack(self, other, damage, skill):
        other.hp = max(other.hp - damage, 0)
        self.mp -= 5
        print(
            f"\n{self.job} {self.name}의 {skill} 공격!!!\n마력 5를 소모하여 {other.name}에게 {damage}의 데미지를 입혔습니다.")
        print(" ")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print("------------------------")
        print(
            f"{self.name}의 상태 \n HP {self.hp}/{self.max_hp}   MP {self.mp}/{self.max_mp}")


# 직업별 캐릭터
class Warrior(Character):
    def __init__(self, name, job, hp, mp):
        self.job = job
        super().__init__(name, hp, mp)

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        skill = '슬래시 블러스트(일반)'
        return super().attack(other, damage, skill)

    def magic_attack(self, other):
        damage = random.randint(self.m_power - 2, self.m_power + 2)
        skill = '레이지 업라이징(마법)'
        return super().magic_attack(other, damage, skill)


class Magician(Character):
    def __init__(self, name, job, hp, mp):
        self.job = job
        super().__init__(name, hp, mp)

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        skill = '에너지 볼트(일반)'
        return super().attack(other, damage, skill)

    def magic_attack(self, other):
        damage = random.randint(self.m_power - 2, self.m_power + 2)
        skill = '블리자드(마법)'
        return super().magic_attack(other, damage, skill)


# 몬스터의 모체가 되는 클래쓰
class Monster:
    def __init__(self, hp):
        self.max_hp = hp
        self.hp = hp

    def attack(self, other, skill):
        damage = random.randint(15, 25)
        other.hp = max(other.hp - damage, 0)
        print(" ")
        print(f"{self.name}의 {skill} 공격!!!\n{other.name}에게 {damage}의 데미지를 입혔습니다.")
        print(" ")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(
            f"{self.name}의 상태 \n HP {self.hp}/{self.max_hp}")
        print("------------------------")


# 몬스터 종류
class PinkMonster(Monster):
    def __init__(self, hp):
        self.name = '핑크빈'
        super().__init__(hp)

    def attack(self, other):
        skill = '데굴데굴'
        return super().attack(other, skill)


class SlimeMonster(Monster):
    def __init__(self, hp):
        self.name = '슬라임'
        super().__init__(hp)

    def attack(self, other):
        skill = '몸통박치기!'
        return super().attack(other, skill)


class SnowMonster(Monster):
    def __init__(self, hp):
        self.name = '예티'
        super().__init__(hp)

    def attack(self, other):
        skill = '예티! 스매시!'
        return super().attack(other, skill)


# 캐릭터 생성하기
print('이름을 입력해 주세요: ')
player_name = str(input(" "))
player_job = str(input('직업을 입력해 주세요. 1. 전사  2. 마법사:  '))
while True:
    if player_job == '전사':
        hp = 120
        mp = 20
        player = Warrior(player_name, player_job, hp, mp)
        print(
            f'\n{player_name}님의 캐릭터가 생성되었습니다!\n\n[체력: {player.hp}, 마나: {player.mp}, 공격력: {player.power}, 마력: {player.m_power}]')
        break
    elif player_job == '마법사':
        hp = 100
        mp = 40
        player = Magician(player_name, player_job, hp, mp)
        print(
            f'{player_job} {player_name}님의 캐릭터가 생성되었습니다!\n[체력: {player.hp}, 마나: {player.mp}, 공격력: {player.power}, 마력: {player.m_power}]')
        break
    else:
        player_job = str(input('직업의 이름을 입력해 주세요. 1. 전사  2. 마법사:  '))
        continue


# 전투 시작하기
time.sleep(1)
print(" ")
print("-------------------")
print("전투를 시작합니다.")
print("-------------------")
print(" ")


# 몬스터 생성
pink_monster = PinkMonster(100)
slime_monster = SlimeMonster(100)
snow_monster = SnowMonster(100)

monsters = [pink_monster, slime_monster, snow_monster]
m = random.choice(monsters)

time.sleep(1)
print(f'{m.name}이(가) 앞을 막아섰습니다.')

# 전투 진행하기
while True:

    time.sleep(1)
    print(" ")
    print("------------------------------------------")
    print(f"{player_job} {player_name}님의 공격을 시작합니다.")
    print("------------------------------------------")
    print(" ")

    # 플레이어의 공격
    attack_input = str(input('공격 번호를 선택하세요.\t 1.일반공격 2.마법공격:  '))

    if attack_input == '1':
        player.attack(m)
        player.show_status()
        m.show_status()
    elif player.mp >= 5 and attack_input == '2':
        player.magic_attack(m)
        player.show_status()
        m.show_status()
    elif player.mp < 5 and attack_input == '2':
        print(" ")
        print("MP가 부족하여 더이상 마법공격을 할 수 없습니다.")
        while True:
            attack_input = str(input('일반공격을 진행하시겠습니까? 1.일반공격: '))
            if attack_input == '1':
                player.attack(m)
                print("-------------------")
                player.show_status()
                m.show_status()
                break
            else:
                print('\n숫자를 입력해 주세요.')
                continue
    else:
        if attack_input != '1' or attack_input != '2':
            print('공격 번호를 바르게 입력해주세요.')
            continue

     # 전투 결과 - 플레이어 승리
    if m.hp == 0:
        time.sleep(1)
        print("------------------------")
        print('축하합니다! 전투에서 승리하였습니다.')
        break

    time.sleep(1)

    # 몬스터의 공격
    print(" ")
    print("-------------------------------")
    print(f"{m.name}이(가) 공격을 시작하였습니다.")
    print("-------------------------------")
    print(" ")
    time.sleep(1)

    m.attack(player)
    player.show_status()
    m.show_status()

    # 전투 결과 - 몬스터 승리
    if player.hp == 0:
        time.sleep(1)
        print("------------------------")
        print('전투에서 패배하였습니다. 다시 시작하시겠습니까?\n 1.예 2.아니오')
        answer = str(input(''))
        if answer == '1' or answer == '예':
            player.hp = hp
            player.mp = mp
            m.hp = 100
            continue
        elif answer == '2' or answer == '아니오':
            break
        else:
            break
