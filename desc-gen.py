import random

#Christian, Individualist, Socialist, Conservative, Reactionary, Liberal, Anarcho-Liberal, Communist, Fascist

adjectives = ["radical", "revolutionary", "militant", "subversive"]
names = ["Yantinato", "Guineux", "Northern Bulwarks", "Stalwarts", "Mugwumps", "Tertium Quids", "Essex Junto", "Half-breeds", "Lily-whites"]
types_of_gov = ["absolute monarchy", "paternalist constitutionalism", "social constitutionalism", "democracy", "presidential dictatorship", "dictatorship of the proletariat", "bourgeois dictatorship", "fascist dictatorship"]
#put into dictionary form
beliefs = ["the erasure of the separation of church and state", "a multicultural cosmopolitan society", "the inherent inferiority of animals", "the inherent evils of lust"]
goals = ["total global hegemony", "a utopian society", "a separatist state"]
enemies = ["the ancien regime", "the deep state", "breakway groups"]
methods = ["acts of terrorism", "rabid evangelism", "mass political subversion"]

def generate_fac_desc(adjs, names, governments, core_beliefs, goals, enemies, methods):
    description_templates = [f"A {{adj}} group advocating for {{government}}, the {{name}} believe in {{core_belief}}. They wish to accomplish {{goal}} via {{method}}. However, they face great animosity from {{enemy}}."]

    chosen_template = random.choice(description_templates)
    return chosen_template.replace("{adj}", random.choice(adjs))\
        .replace("{name}", random.choice(names))\
        .replace("{government}", random.choice(governments))\
        .replace("{core_belief}", random.choice(core_beliefs))\
        .replace("{goal}", random.choice(goals))\
        .replace("{enemy}", random.choice(enemies))\
        .replace("{method}", random.choice(methods))

print(generate_fac_desc(adjectives, names, types_of_gov, beliefs, goals, enemies, methods))