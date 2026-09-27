
"""
NARUTO ULTIMATE BATTLE ARENA
- 28 characters
- Unique abilities
- Armor, burn, stun, confuse, heal, power-up
- Dodge (E) / Counter (C) on projectile attacks
- Pure text version (no images required)
"""

import random
import time
import os
import sys

# ---------------------------------------------------------------------------
# Optional timed keypress (for Dodge / Counter)
# ---------------------------------------------------------------------------
def timed_keypress(timeout=2.2):
    """Return pressed key (lowercase) or None on timeout."""
    if sys.platform == "win32":
        try:
            import msvcrt
            start = time.time()
            while time.time() - start < timeout:
                if msvcrt.kbhit():
                    return msvcrt.getch().decode("utf-8", errors="ignore").lower()
                time.sleep(0.05)
        except Exception:
            pass
        return None

   


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(msg="Press Enter..."):
    input(f"\n{msg}")

CHARACTERS = {
    "Naruto Uzumaki": {
        "health": 210, "max_armor": 0, "dodge_bonus": 0.10,
        "desc": "Hyperactive ninja with huge chakra and never-give-up spirit.",
        "abilities": [
            {"name": "Rasengan", "dmg": 42, "type": "attack", "desc": "Spinning chakra sphere."},
            {"name": "Shadow Clone", "dmg": 28, "type": "special", "effect": "confuse", "desc": "Confuses enemy."},
            {"name": "Rasenshuriken", "dmg": 75, "type": "heavy", "cooldown": 2, "desc": "Huge wind Rasengan.", "self_skip": True},
            {"name": "Sage Mode", "dmg": 35, "type": "buff", "effect": "power_up", "desc": "+15 dmg next 2 attacks."},
            {"name": "Kurama Mode", "dmg": 55, "type": "heavy", "cooldown": 2, "desc": "Nine-Tails cloak + heal.", "heal": 15},
        ],
    },
    "Sasuke Uchiha": {
        "health": 185, "max_armor": 150, "dodge_bonus": 0.15,
        "desc": "Last Uchiha. EMS, Rinnegan, black flames.",
        "abilities": [
            {"name": "Chidori", "dmg": 48, "type": "attack", "desc": "Lightning blade."},
            {"name": "Amaterasu", "dmg": 32, "type": "special", "effect": "burn", "burn": 12, "desc": "Black flames + burn."},
            {"name": "Susanoo", "dmg": 38, "type": "defense", "effect": "susanoo", "duration": 3, "desc": "150 armor for 3 turns."},
            {"name": "Indra's Arrow", "dmg": 90, "type": "heavy", "cooldown": 3, "desc": "Ultimate lightning arrow."},
            {"name": "Kunai Throw", "dmg": 22, "type": "projectile", "desc": "Fast kunai – REACTABLE!", "can_react": True},
            {"name": "Amenotejikara", "dmg": 0, "type": "special", "effect": "swap", "desc": "Space-time dodge prep."},
        ],
    },
    "Itachi Uchiha": {
        "health": 155, "max_armor": 120, "dodge_bonus": 0.20,
        "desc": "Uchiha genius. Genjutsu and Mangekyo master.",
        "abilities": [
            {"name": "Amaterasu", "dmg": 30, "type": "special", "effect": "burn", "burn": 12, "desc": "Black flames."},
            {"name": "Tsukuyomi", "dmg": 18, "type": "special", "effect": "stun", "stun_chance": 0.75, "desc": "High chance stun.", "cooldown": 1},
            {"name": "Susanoo (Totsuka)", "dmg": 42, "type": "defense", "effect": "susanoo", "duration": 2, "desc": "Armored Susanoo."},
            {"name": "Yasaka Magatama", "dmg": 58, "type": "attack", "desc": "Black flame orbs."},
            {"name": "Crow + Kunai", "dmg": 25, "type": "projectile", "desc": "REACTABLE kunai.", "can_react": True},
        ],
    },
    "Kakashi Hatake": {
        "health": 170, "max_armor": 0, "dodge_bonus": 0.18,
        "desc": "Copy Ninja. Sharingan and 1000 jutsu.",
        "abilities": [
            {"name": "Raikiri", "dmg": 52, "type": "attack", "desc": "Lightning Cutter."},
            {"name": "Kamui", "dmg": 0, "type": "defense", "effect": "dodge_ready", "desc": "Space-time dodge.", "cooldown": 1},
            {"name": "Clone + Raikiri", "dmg": 38, "type": "attack", "desc": "Clone assist."},
            {"name": "Copy Ninja", "dmg": 45, "type": "special", "desc": "Copies a technique."},
            {"name": "Kunai Barrage", "dmg": 28, "type": "projectile", "desc": "REACTABLE kunai.", "can_react": True},
        ],
    },
    "Sakura Haruno": {
        "health": 155, "max_armor": 0, "dodge_bonus": 0.08,
        "desc": "Tsunade's student. Super strength + medical ninjutsu.",
        "abilities": [
            {"name": "Super Punch", "dmg": 58, "type": "attack", "desc": "Ground-shattering punch."},
            {"name": "Medical Ninjutsu", "dmg": 0, "type": "heal", "heal": 45, "desc": "Heals 45 HP.", "cooldown": 1},
            {"name": "Cherry Blossom Impact", "dmg": 72, "type": "heavy", "cooldown": 2, "desc": "Huge punch, self 12 dmg.", "self_dmg": 12},
            {"name": "Katsuyu Summon", "dmg": 22, "type": "special", "heal": 25, "desc": "Slug support."},
        ],
    },
    "Madara Uchiha": {
        "health": 240, "max_armor": 180, "dodge_bonus": 0.12,
        "desc": "Legendary Uchiha. Perfect Susanoo + Rinnegan.",
        "abilities": [
            {"name": "Perfect Susanoo", "dmg": 50, "type": "defense", "effect": "susanoo", "duration": 4, "desc": "180 armor, 4 turns."},
            {"name": "Meteor", "dmg": 80, "type": "heavy", "cooldown": 3, "desc": "Tengai Shinsei."},
            {"name": "Limbo", "dmg": 40, "type": "special", "effect": "stun", "stun_chance": 0.55, "desc": "Shadow stun."},
            {"name": "Wood Release", "dmg": 35, "type": "attack", "desc": "Deep forest."},
            {"name": "Kunai + Fireball", "dmg": 30, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Obito Uchiha": {
        "health": 190, "max_armor": 100, "dodge_bonus": 0.25,
        "desc": "Kamui dimension + Rinnegan.",
        "abilities": [
            {"name": "Kamui Intangible", "dmg": 0, "type": "defense", "effect": "dodge_ready", "desc": "Phase through attacks.", "cooldown": 1},
            {"name": "Kamui Crush", "dmg": 55, "type": "attack", "desc": "Dimension crush."},
            {"name": "Human Path", "dmg": 45, "type": "special", "effect": "stun", "stun_chance": 0.4, "desc": "Soul technique."},
            {"name": "Wood Spike", "dmg": 38, "type": "attack", "desc": "Wood spikes."},
            {"name": "Kamui Kunai", "dmg": 26, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Minato Namikaze": {
        "health": 175, "max_armor": 0, "dodge_bonus": 0.30,
        "desc": "Yellow Flash. Fastest Hokage.",
        "abilities": [
            {"name": "Rasengan", "dmg": 48, "type": "attack", "desc": "Original Rasengan."},
            {"name": "Flying Thunder God", "dmg": 0, "type": "special", "effect": "dodge_ready", "desc": "Teleport dodge.", "cooldown": 1},
            {"name": "Hiraishin Slash", "dmg": 60, "type": "attack", "desc": "Teleport slash."},
            {"name": "Kunai Barrage", "dmg": 35, "type": "projectile", "desc": "REACTABLE marked kunai.", "can_react": True},
            {"name": "Contract Seal", "dmg": 20, "type": "special", "effect": "stun", "stun_chance": 0.5, "desc": "Seal movement."},
        ],
    },
    "Hashirama Senju": {
        "health": 250, "max_armor": 80, "dodge_bonus": 0.05,
        "desc": "First Hokage. God of Shinobi. Wood Release.",
        "abilities": [
            {"name": "Flowering Trees", "dmg": 55, "type": "attack", "desc": "Giant forest attack."},
            {"name": "Wood Dragon", "dmg": 48, "type": "attack", "desc": "Chakra-draining dragon.", "extra": 10},
            {"name": "Sage Mode", "dmg": 40, "type": "buff", "effect": "power_up", "desc": "Power boost."},
            {"name": "Regeneration", "dmg": 0, "type": "heal", "heal": 50, "desc": "Senju regen.", "cooldown": 1},
            {"name": "Wood Golem", "dmg": 30, "type": "defense", "effect": "susanoo", "duration": 2, "desc": "Wood armor."},
        ],
    },
    "Tobirama Senju": {
        "health": 180, "max_armor": 0, "dodge_bonus": 0.15,
        "desc": "Second Hokage. Water Release + Hiraishin.",
        "abilities": [
            {"name": "Water Dragon", "dmg": 50, "type": "attack", "desc": "Massive water dragon."},
            {"name": "Flying Thunder God", "dmg": 0, "type": "special", "effect": "dodge_ready", "desc": "Original Hiraishin.", "cooldown": 1},
            {"name": "Water Needle", "dmg": 38, "type": "attack", "desc": "High-pressure needles."},
            {"name": "Edo Partial", "dmg": 25, "type": "special", "effect": "confuse", "desc": "Confusion."},
            {"name": "Kunai Throw", "dmg": 24, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Gaara": {
        "health": 195, "max_armor": 100, "dodge_bonus": 0.05,
        "desc": "Kazekage. Absolute sand defense.",
        "abilities": [
            {"name": "Sand Burial", "dmg": 55, "type": "attack", "desc": "Crushing sand."},
            {"name": "Shield of Sand", "dmg": 0, "type": "defense", "effect": "susanoo", "duration": 3, "desc": "100 armor, 3 turns."},
            {"name": "Sand Tsunami", "dmg": 48, "type": "attack", "desc": "Wave of sand."},
            {"name": "Shukaku Form", "dmg": 35, "type": "heavy", "cooldown": 2, "desc": "Partial bijuu + armor.", "effect": "susanoo", "duration": 2},
            {"name": "Sand Shuriken", "dmg": 28, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Rock Lee": {
        "health": 165, "max_armor": 0, "dodge_bonus": 0.12,
        "desc": "Taijutsu genius. Eight Gates.",
        "abilities": [
            {"name": "Primary Lotus", "dmg": 50, "type": "attack", "desc": "High-speed combo."},
            {"name": "Hidden Lotus", "dmg": 70, "type": "heavy", "cooldown": 2, "desc": "Gates open, self 10.", "self_dmg": 10},
            {"name": "Drunken Fist", "dmg": 40, "type": "special", "effect": "confuse", "desc": "Confuses enemy."},
            {"name": "Konoha Hurricane", "dmg": 35, "type": "attack", "desc": "Spinning kicks."},
            {"name": "Dynamic Entry", "dmg": 30, "type": "projectile", "desc": "REACTABLE flying kick.", "can_react": True},
        ],
    },
    "Might Guy": {
        "health": 175, "max_armor": 0, "dodge_bonus": 0.10,
        "desc": "Green Beast. Master of Eight Gates.",
        "abilities": [
            {"name": "Dynamic Entry", "dmg": 38, "type": "attack", "desc": "Signature kick."},
            {"name": "Primary Lotus", "dmg": 52, "type": "attack", "desc": "Taijutsu finisher."},
            {"name": "Evening Elephant", "dmg": 75, "type": "heavy", "cooldown": 2, "desc": "Sixth Gate."},
            {"name": "Night Guy", "dmg": 95, "type": "heavy", "cooldown": 3, "desc": "7th Gate, self 35.", "self_dmg": 35},
            {"name": "Leaf Whirlwind", "dmg": 32, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Killer Bee": {
        "health": 200, "max_armor": 60, "dodge_bonus": 0.12,
        "desc": "Eight-Tails jinchuriki. Raps while fighting.",
        "abilities": [
            {"name": "Lariat", "dmg": 55, "type": "attack", "desc": "Chakra clothesline."},
            {"name": "Bijuu Mode", "dmg": 45, "type": "buff", "effect": "power_up", "desc": "Cloak + armor.", "effect2": "susanoo", "duration": 2},
            {"name": "Tailed Beast Bomb", "dmg": 80, "type": "heavy", "cooldown": 3, "desc": "Bijuu dama."},
            {"name": "Samehada Slash", "dmg": 40, "type": "attack", "desc": "Chakra-absorbing slash."},
            {"name": "Acrobat Kunai", "dmg": 26, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Pain (Nagato)": {
        "health": 185, "max_armor": 0, "dodge_bonus": 0.10,
        "desc": "Rinnegan. Six Paths of Pain.",
        "abilities": [
            {"name": "Almighty Push", "dmg": 50, "type": "attack", "desc": "Shinra Tensei."},
            {"name": "Universal Pull", "dmg": 30, "type": "special", "effect": "stun", "stun_chance": 0.5, "desc": "Bansho Tenin."},
            {"name": "Chibaku Tensei", "dmg": 70, "type": "heavy", "cooldown": 3, "desc": "Planetary Devastation."},
            {"name": "Missile Barrage", "dmg": 42, "type": "attack", "desc": "Asura Path missiles."},
            {"name": "Black Receiver", "dmg": 25, "type": "projectile", "desc": "REACTABLE rods.", "can_react": True},
        ],
    },
    "Jiraiya": {
        "health": 190, "max_armor": 0, "dodge_bonus": 0.10,
        "desc": "Toad Sage. Legendary Sannin.",
        "abilities": [
            {"name": "Rasengan", "dmg": 45, "type": "attack", "desc": "Classic Rasengan."},
            {"name": "Sage Mode", "dmg": 40, "type": "buff", "effect": "power_up", "desc": "Toad Sage Mode."},
            {"name": "Gamabunta", "dmg": 55, "type": "heavy", "cooldown": 2, "desc": "Giant toad summon."},
            {"name": "Flame Bomb", "dmg": 38, "type": "attack", "desc": "Massive fire."},
            {"name": "Needle Jizo", "dmg": 20, "type": "defense", "effect": "susanoo", "duration": 2, "desc": "Hair armor."},
        ],
    },
    "Tsunade": {
        "health": 180, "max_armor": 0, "dodge_bonus": 0.08,
        "desc": "Fifth Hokage. Medical ninja + monstrous strength.",
        "abilities": [
            {"name": "Heavenly Foot", "dmg": 65, "type": "attack", "desc": "Devastating kick."},
            {"name": "Creation Rebirth", "dmg": 0, "type": "heal", "heal": 60, "desc": "Ultimate regen.", "cooldown": 2},
            {"name": "Katsuyu Network", "dmg": 25, "type": "special", "heal": 30, "desc": "Slug heal + acid."},
            {"name": "Punch Barrage", "dmg": 48, "type": "attack", "desc": "Super strength punches."},
            {"name": "Healing Palm", "dmg": 0, "type": "heal", "heal": 35, "desc": "Quick heal.", "cooldown": 1},
        ],
    },
    "Orochimaru": {
        "health": 170, "max_armor": 40, "dodge_bonus": 0.15,
        "desc": "Snake Sannin. Immortal body modifications.",
        "abilities": [
            {"name": "Snake Binding", "dmg": 35, "type": "special", "effect": "stun", "stun_chance": 0.55, "desc": "Constrict + stun."},
            {"name": "Kusanagi", "dmg": 48, "type": "attack", "desc": "Sword from mouth."},
            {"name": "Eight-Headed Serpent", "dmg": 60, "type": "heavy", "cooldown": 2, "desc": "Giant snake form."},
            {"name": "Body Replace", "dmg": 0, "type": "defense", "effect": "dodge_ready", "desc": "Shed skin dodge.", "cooldown": 1},
            {"name": "Snake Hands", "dmg": 28, "type": "projectile", "desc": "REACTABLE snakes.", "can_react": True},
        ],
    },
    "Kabuto Yakushi": {
        "health": 175, "max_armor": 50, "dodge_bonus": 0.12,
        "desc": "Orochimaru's right hand. Sage Mode later.",
        "abilities": [
            {"name": "Chakra Scalpel", "dmg": 42, "type": "attack", "desc": "Internal cut."},
            {"name": "Sage Mode", "dmg": 38, "type": "buff", "effect": "power_up", "desc": "Dragon Sage."},
            {"name": "Edo Assist", "dmg": 30, "type": "special", "effect": "confuse", "desc": "Edo distraction."},
            {"name": "Healing Jutsu", "dmg": 0, "type": "heal", "heal": 40, "desc": "Self heal.", "cooldown": 1},
            {"name": "Snake Projectile", "dmg": 26, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Shikamaru Nara": {
        "health": 145, "max_armor": 0, "dodge_bonus": 0.08,
        "desc": "Genius strategist. Shadow Possession.",
        "abilities": [
            {"name": "Shadow Possession", "dmg": 15, "type": "special", "effect": "stun", "stun_chance": 0.85, "desc": "Very high stun chance.", "cooldown": 1},
            {"name": "Shadow Strangle", "dmg": 40, "type": "attack", "desc": "Strangle after possession."},
            {"name": "Shadow Sewing", "dmg": 35, "type": "attack", "desc": "Shadow tendrils."},
            {"name": "Exploding Trap", "dmg": 50, "type": "heavy", "cooldown": 2, "desc": "Tag trap."},
            {"name": "Kunai Setup", "dmg": 22, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Hinata Hyuga": {
        "health": 150, "max_armor": 0, "dodge_bonus": 0.15,
        "desc": "Hyuga princess. Byakugan + Gentle Fist.",
        "abilities": [
            {"name": "Gentle Fist", "dmg": 38, "type": "attack", "desc": "Chakra point strikes.", "extra": 8},
            {"name": "Twin Lion Fists", "dmg": 55, "type": "attack", "desc": "Chakra lions."},
            {"name": "64 Palms", "dmg": 48, "type": "heavy", "cooldown": 2, "desc": "Classic barrage."},
            {"name": "Byakugan Insight", "dmg": 0, "type": "buff", "effect": "power_up", "desc": "Power up."},
            {"name": "Air Palm", "dmg": 30, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Neji Hyuga": {
        "health": 160, "max_armor": 30, "dodge_bonus": 0.18,
        "desc": "Hyuga genius. Rotation + Gentle Fist.",
        "abilities": [
            {"name": "Rotation", "dmg": 20, "type": "defense", "effect": "susanoo", "duration": 2, "desc": "Absolute defense."},
            {"name": "64 Palms", "dmg": 52, "type": "attack", "desc": "Full sequence."},
            {"name": "Internal Damage", "dmg": 40, "type": "attack", "desc": "Tenketsu focus.", "extra": 10},
            {"name": "Air Palm Barrage", "dmg": 35, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
            {"name": "Byakugan Focus", "dmg": 0, "type": "buff", "effect": "power_up", "desc": "Sharpen attacks."},
        ],
    },
    "Deidara": {
        "health": 155, "max_armor": 0, "dodge_bonus": 0.12,
        "desc": "Art is an explosion!",
        "abilities": [
            {"name": "C1 Clay Birds", "dmg": 35, "type": "attack", "desc": "Small bombs."},
            {"name": "C2 Dragon", "dmg": 55, "type": "attack", "desc": "Clay dragon."},
            {"name": "C3 Giant Bomb", "dmg": 75, "type": "heavy", "cooldown": 2, "desc": "Village-scale bomb."},
            {"name": "C4 Karura", "dmg": 45, "type": "special", "effect": "burn", "burn": 15, "desc": "Micro bombs."},
            {"name": "Clay Kunai", "dmg": 24, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Kisame Hoshigaki": {
        "health": 200, "max_armor": 40, "dodge_bonus": 0.08,
        "desc": "Monster of the Mist. Samehada.",
        "abilities": [
            {"name": "Samehada Slash", "dmg": 48, "type": "attack", "desc": "Chakra-absorbing sword."},
            {"name": "Water Prison", "dmg": 25, "type": "special", "effect": "stun", "stun_chance": 0.65, "desc": "Water sphere trap."},
            {"name": "Shark Bombs", "dmg": 50, "type": "attack", "desc": "Water sharks."},
            {"name": "Great Shark Bullet", "dmg": 65, "type": "heavy", "cooldown": 2, "desc": "Giant shark."},
            {"name": "Samehada Throw", "dmg": 30, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Konan": {
        "health": 150, "max_armor": 0, "dodge_bonus": 0.20,
        "desc": "Angel of Akatsuki. Paper + 600 billion tags.",
        "abilities": [
            {"name": "Paper Storm", "dmg": 40, "type": "attack", "desc": "Cutting paper."},
            {"name": "Paper Person", "dmg": 0, "type": "defense", "effect": "dodge_ready", "desc": "Body to paper.", "cooldown": 1},
            {"name": "600 Billion Tags", "dmg": 85, "type": "heavy", "cooldown": 3, "desc": "Ultimate paper bombs."},
            {"name": "Paper Shuriken", "dmg": 32, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
            {"name": "Paper Bind", "dmg": 20, "type": "special", "effect": "stun", "stun_chance": 0.5, "desc": "Restrain."},
        ],
    },
    "Temari": {
        "health": 155, "max_armor": 0, "dodge_bonus": 0.12,
        "desc": "Sand sibling. Giant fan + wind.",
        "abilities": [
            {"name": "Sickle Weasel", "dmg": 48, "type": "attack", "desc": "Cutting wind."},
            {"name": "Kamatari", "dmg": 55, "type": "heavy", "cooldown": 2, "desc": "Giant weasel tornado."},
            {"name": "Wind Wall", "dmg": 15, "type": "defense", "effect": "susanoo", "duration": 2, "desc": "Wind armor."},
            {"name": "Fan Throw", "dmg": 30, "type": "projectile", "desc": "REACTABLE boomerang.", "can_react": True},
            {"name": "Dust Wind", "dmg": 28, "type": "special", "effect": "confuse", "desc": "Blinding wind."},
        ],
    },
    "Sai": {
        "health": 150, "max_armor": 0, "dodge_bonus": 0.14,
        "desc": "Root ANBU. Super Beast Drawing.",
        "abilities": [
            {"name": "Ink Lion", "dmg": 42, "type": "attack", "desc": "Ink beast."},
            {"name": "Ink Birds", "dmg": 35, "type": "attack", "desc": "Flying ink birds."},
            {"name": "Ink Snake Bind", "dmg": 25, "type": "special", "effect": "stun", "stun_chance": 0.5, "desc": "Restrain."},
            {"name": "Sealing Ink", "dmg": 20, "type": "special", "effect": "stun", "stun_chance": 0.4, "desc": "Seal formula."},
            {"name": "Ink Kunai", "dmg": 26, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
    "Yamato": {
        "health": 165, "max_armor": 50, "dodge_bonus": 0.10,
        "desc": "Hashirama cells. Wood Release captain.",
        "abilities": [
            {"name": "Wood Locking Wall", "dmg": 20, "type": "defense", "effect": "susanoo", "duration": 2, "desc": "Wooden dome."},
            {"name": "Wood Dragon", "dmg": 45, "type": "attack", "desc": "Suppressing dragon."},
            {"name": "Four-Pillar Prison", "dmg": 30, "type": "special", "effect": "stun", "stun_chance": 0.6, "desc": "Wood prison."},
            {"name": "Wood Spike Field", "dmg": 40, "type": "attack", "desc": "Ground spikes."},
            {"name": "Wood Shuriken", "dmg": 25, "type": "projectile", "desc": "REACTABLE.", "can_react": True},
        ],
    },
}


class Fighter:
    def __init__(self, label, char_name, is_player=False):
        self.label = label
        self.char_name = char_name
        base = CHARACTERS[char_name]
        self.max_hp = base["health"]
        self.hp = base["health"]
        self.armor = 0
        self.max_armor = base.get("max_armor", 0)
        self.abilities = [dict(a) for a in base["abilities"]]
        self.is_player = is_player
        self.dodge_bonus = base.get("dodge_bonus", 0.10)
        self.desc = base["desc"]

        self.burn = 0
        self.stunned = False
        self.confused = False
        self.dodge_ready = False
        self.power_up_turns = 0
        self.power_up_bonus = 0
        self.susanoo_turns = 0
        self.skip_next = False
        self.cooldowns = {a["name"]: 0 for a in self.abilities}

    def status(self):
        parts = [f"HP {self.hp}/{self.max_hp}"]
        if self.armor > 0:
            parts.append(f"Armor {self.armor}")
        flags = []
        if self.burn:
            flags.append(f"BURN({self.burn})")
        if self.stunned:
            flags.append("STUNNED")
        if self.confused:
            flags.append("CONFUSED")
        if self.dodge_ready:
            flags.append("DODGE-READY")
        if self.power_up_turns:
            flags.append(f"POWER+{self.power_up_bonus}")
        if self.susanoo_turns:
            flags.append(f"SUSANOO({self.susanoo_turns})")
        if flags:
            parts.append(" | ".join(flags))
        return "   ".join(parts)

    def choose_ability(self):
        if self.is_player:
            print("\n  Your abilities:")
            for i, ab in enumerate(self.abilities):
                cd = self.cooldowns[ab["name"]]
                tag = "READY" if cd <= 0 else f"CD {cd}"
                react = " [REACTABLE]" if ab.get("can_react") else ""
                print(f"    {i+1}. {ab['name']:<28} DMG:{ab.get('dmg',0):<3} [{tag}]{react}")
                print(f"        {ab['desc']}")
            while True:
                try:
                    choice = int(input("\n  Choose number: ").strip()) - 1
                    if 0 <= choice < len(self.abilities):
                        ab = self.abilities[choice]
                        if self.cooldowns[ab["name"]] <= 0:
                            return ab
                        print("  On cooldown!")
                    else:
                        print("  Invalid.")
                except ValueError:
                    print("  Enter a number.")
        else:
            ready = [a for a in self.abilities if self.cooldowns[a["name"]] <= 0]
            if not ready:
                ready = self.abilities
            if self.hp < self.max_hp * 0.35:
                heals = [a for a in ready if a.get("type") == "heal"]
                if heals:
                    return random.choice(heals)
            strong = [a for a in ready if a.get("dmg", 0) >= 50]
            if strong and random.random() < 0.5:
                return random.choice(strong)
            react = [a for a in ready if a.get("can_react")]
            if react and random.random() < 0.3:
                return random.choice(react)
            return random.choice(ready)

    def apply(self, ability, opponent):
        print(f"\n  >>> {self.label} ({self.char_name}) uses 【{ability['name']}】!")
        time.sleep(0.4)

        if ability.get("cooldown", 0) > 0:
            self.cooldowns[ability["name"]] = ability["cooldown"] + 1

        # Heal
        if ability.get("type") == "heal" or "heal" in ability:
            heal = ability.get("heal", 0)
            old = self.hp
            self.hp = min(self.max_hp, self.hp + heal)
            print(f"  Healed {self.hp - old} HP → {self.hp}/{self.max_hp}")

        if ability.get("effect") == "power_up":
            self.power_up_turns = 2
            self.power_up_bonus = 15
            print("  Power up! +15 damage for 2 turns.")

        if ability.get("effect") == "dodge_ready":
            self.dodge_ready = True
            print("  Ready to dodge the next attack!")

        if ability.get("effect") == "susanoo" or ability.get("effect2") == "susanoo":
            dur = ability.get("duration", 2)
            self.armor = self.max_armor if self.max_armor > 0 else 60
            self.susanoo_turns = dur
            print(f"  Armor activated! {self.armor} armor for {dur} turns.")

        dmg = ability.get("dmg", 0)
        if self.power_up_turns > 0 and dmg > 0:
            dmg += self.power_up_bonus
            print(f"  (Power-up +{self.power_up_bonus})")
        if ability.get("extra"):
            dmg += ability["extra"]

        # ----- REACTABLE (Dodge / Counter) -----
        if dmg > 0 and ability.get("can_react") and opponent.is_player:
            print("\n  ⚡ PROJECTILE / PHYSICAL ATTACK INCOMING! ⚡")
            print("  Press  E  to DODGE     or     C  to COUNTER")
            print("  You have ~2.2 seconds...")
            key = timed_keypress(2.2)
            if key == "e":
                chance = 0.55 + opponent.dodge_bonus
                if random.random() < chance:
                    print(f"  ★ SUCCESSFUL DODGE! ({int(chance*100)}%)")
                    dmg = 0
                else:
                    print("  Dodge failed...")
            elif key == "c":
                print("  You attempt a COUNTER!")
                if random.random() < 0.45:
                    counter = int(dmg * 0.6)
                    print(f"  ★ COUNTER SUCCESS! You deal {counter} back!")
                    self._take(counter)
                    dmg = int(dmg * 0.4)
                else:
                    print("  Counter failed! Extra damage.")
                    dmg = int(dmg * 1.1)
            else:
                print("  Too slow! Full hit.")

        # Computer can also sometimes dodge projectiles
        if dmg > 0 and ability.get("can_react") and not opponent.is_player:
            if random.random() < 0.25 + opponent.dodge_bonus:
                print(f"  {opponent.label} narrowly dodged!")
                dmg = 0

        # Prepared dodge
        if dmg > 0 and opponent.dodge_ready:
            chance = 0.55 + opponent.dodge_bonus
            if random.random() < chance:
                print(f"  {opponent.label} completely avoids the attack!")
                opponent.dodge_ready = False
                dmg = 0
            else:
                print("  Prepared dodge failed!")
                opponent.dodge_ready = False

        # Confusion miss
        if dmg > 0 and self.confused and random.random() < 0.28:
            print(f"  {self.label} is confused and misses!")
            self.confused = False
            dmg = 0

        if dmg > 0:
            opponent._take(dmg)

        # Special effects
        effect = ability.get("effect")
        if effect == "burn":
            opponent.burn = ability.get("burn", 10)
            print(f"  Burn {opponent.burn} will hit next turn!")
        elif effect == "stun":
            if random.random() < ability.get("stun_chance", 0.5):
                opponent.stunned = True
                print(f"  ★ {opponent.label} is STUNNED!")
            else:
                print("  Stun resisted.")
        elif effect == "confuse":
            opponent.confused = True
            print(f"  {opponent.label} is CONFUSED!")
        elif effect == "swap":
            self.dodge_ready = True
            print("  Space-time dodge prepared.")

        if ability.get("self_dmg"):
            print(f"  Self damage / gate cost: {ability['self_dmg']}")
            self._take(ability["self_dmg"])
        if ability.get("self_skip"):
            self.skip_next = True
            print("  Needs recovery next turn.")

    def _take(self, dmg):
        if self.armor > 0:
            absorbed = min(self.armor, dmg)
            self.armor -= absorbed
            dmg -= absorbed
            print(f"  Armor absorbed {absorbed} → armor left {self.armor}")
        if dmg > 0:
            self.hp = max(0, self.hp - dmg)
            print(f"  {self.label} takes {dmg} damage! HP now {self.hp}/{self.max_hp}")

    def end_turn(self):
        for k in self.cooldowns:
            if self.cooldowns[k] > 0:
                self.cooldowns[k] -= 1
        if self.susanoo_turns > 0:
            self.susanoo_turns -= 1
            if self.susanoo_turns <= 0:
                self.armor = 0
                print(f"  {self.label}'s armor / Susanoo fades...")
        if self.power_up_turns > 0:
            self.power_up_turns -= 1
            if self.power_up_turns <= 0:
                self.power_up_bonus = 0
                print(f"  {self.label}'s power-up wears off.")
        if self.burn > 0:
            print(f"  {self.label} suffers {self.burn} burn damage!")
            self._take(self.burn)
            self.burn = 0
        self.stunned = False



def main():
    clear()
    print("=" * 60)
    print("     NARUTO ULTIMATE BATTLE ARENA")
    print("=" * 60)
    print(f"\n  Characters available: {len(CHARACTERS)}")
    print("  When enemy uses a projectile/kunai you get 2.2 seconds:")
    print("      E  →  Dodge")
    print("      C  →  Counter")
    print()
    pause("Press Enter to start...")

    names = list(CHARACTERS.keys())
    random.shuffle(names)
    player = Fighter("YOU", names[0], is_player=True)
    computer = Fighter("COMPUTER", names[1], is_player=False)

    clear()
    print("=" * 60)
    print(f"  YOU → {player.char_name}")
    print(f"  {player.desc}")
    print(f"  HP: {player.max_hp}   Dodge bonus: +{int(player.dodge_bonus*100)}%")
    print()
    print(f"  COMPUTER → {computer.char_name}")
    print(f"  {computer.desc}")
    print(f"  HP: {computer.max_hp}")
    print("=" * 60)
    pause("Press Enter to BATTLE!")

    turn = 1
    while True:
        clear()
        print("=" * 60)
        print(f"  TURN {turn}")
        print("=" * 60)
        print(f"\n  YOU ({player.char_name})")
        print(f"  {player.status()}")
        print(f"\n  COMPUTER ({computer.char_name})")
        print(f"  {computer.status()}")
        print()

        if player.hp <= 0:
            print("\n  ★★★  YOU HAVE BEEN DEFEATED  ★★★")
            print(f"  Winner: COMPUTER – {computer.char_name}")
            break
        if computer.hp <= 0:
            print("\n  ★★★  VICTORY! YOU WIN!  ★★★")
            print(f"  Winner: YOU – {player.char_name}")
            break

        # Player turn
        if player.skip_next:
            print("\n  YOU are recovering. Turn skipped.")
            player.skip_next = False
        elif player.stunned:
            print("\n  YOU are STUNNED!")
        else:
            ab = player.choose_ability()
            player.apply(ab, computer)

        if computer.hp <= 0:
            print("\n  ★★★  VICTORY! YOU WIN!  ★★★")
            break

        time.sleep(0.8)

        # Computer turn
        if computer.skip_next:
            print("\n  COMPUTER is recovering.")
            computer.skip_next = False
        elif computer.stunned:
            print("\n  COMPUTER is STUNNED!")
        else:
            print("\n  --- Computer is thinking... ---")
            time.sleep(0.7)
            ab = computer.choose_ability()
            computer.apply(ab, player)

        player.end_turn()
        computer.end_turn()

        turn += 1
        pause("Press Enter for next turn...")

    print("\n" + "=" * 60)
    print("  Thanks for playing!")
    print("=" * 60)
    pause("Press Enter to exit...")


if __name__ == "__main__":
    main()
