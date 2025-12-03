
import random as rd
class Child:
    def __init__(self,name):
        self.name=name
        self.age=0
        self.health=100
        self.happiness=0
        self.stress_level=0
        self.self_background='Rich by heart'
        self.family_background=rd.choice(['poor','middle-class','rich'])
        self.innocence=100
        self.emotions=0
        self.maturity=0
        self.money_spent=0
        self.history=[]
        self.skills={
            "communication": 0,
            "creativity": 0,
            "emotional_intelligence": 0,
            "discipline": 0,
            "financial_literacy": 0,
            "social_helping": 0,
            "fitness": 0,
            "knowledge": 0,
            "cooking": 0,
            "time_management": 0,
            "problem_solving": 0,
            "sports":0
        } 


    def childhood(self):

        print("------🚼 AGE FROM 0-12--------")

        events = {
            "first_birthday": {"desc":"Cake cutting function and celebration","happiness":5,"stress_level":0,"innocence":100,"money_spent":10000},
            "play_cartoon": {"desc":"Watch cartoons and play with family","happiness":5,"stress_level":0,"skills":{"knowledge":0}},
            "play_school": {"desc":"Joined Play school","happiness":5,"stress_level":0,"health":2,"money_spent":25000},
            "make_friends": {"desc":"make friends","happiness":5,"stress_level":0,"skills":{"communication":3}},
            "joined_school": {"desc":"Joined in School","happiness":1,"stress_level":1,"skills":{"knowledge":2},"innocence":-1,"maturity":1,"money_spent":400000},
            "exam_failed": {"desc":"failed in exams","happiness":-8,"stress_level":2,"emotions":2},
            "Punishment": {"desc":"Punishment at school","happiness":-8,"stress_level":1,"maturity":1,"skills":{"discipline":2}},
            "went_tuition": {"desc":"Went Tuition","skills":{"knowledge":2},"stress_level":-1,"money_spent":1000},
            "won_sports": {"desc":"Won a sports competition","happiness":6,"stress_level":2,"skills":{"sports":3}},
            "minor_accident": {"desc":"minor accident","happiness":-10,"stress_level":4,"health":-50,"money_spent":"random"},
            "helped_someone": {"desc":"helped someone","happiness":4,"stress_level":-7,"skills":{"emotional_intelligence":2,"social_helping":5}},
            "learned_new": {"desc":"learned something new","happiness":3,"skills":{"knowledge":3},"maturity":2},
            "family_difficulty": {"desc":"Difficulty in family situation","happiness":-18,"stress_level":1,"skills":{"financial_literacy":5},"emotions":2}
        }

        age_events = {
                0: ["first_birthday"],
                1: ["play_cartoon"],
                2: ["play_cartoon"],
                3: ["play_cartoon", "play_school", "make_friends"],
                4: ["play_cartoon", "make_friends"],
                5: ["joined_school", "make_friends"],
                6: ["went_tuition", "make_friends", "won_sports","exam_failed","Punishment","family_difficulty"],
                7: ["went_tuition", "make_friends", "won_sports","exam_failed","Punishment","family_difficulty"],
                8: ["went_tuition", "make_friends", "won_sports","exam_failed","Punishment","learned_new","family_difficulty"],
                9: ["went_tuition", "make_friends", "won_sports","exam_failed","Punishment","learned_new","family_difficulty"],
                10: ["went_tuition", "make_friends", "won_sports","exam_failed","Punishment","helped_someone","learned_new","family_difficulty"],
                11: ["went_tuition", "make_friends", "won_sports","exam_failed","Punishment","minor_accident","helped_someone","learned_new","family_difficulty"],
                12: ["went_tuition", "make_friends", "won_sports","exam_failed","Punishment","minor_accident","helped_someone","learned_new","family_difficulty"]
            }
      
        done_events={
            "play_school":False,
            "joined_school":False,
            "first_birthday":False
        }
        event_log=[]
        
        for age in range(0,13):
            self.age=age
            yearly_events=[]
            added_keys=[]

            if not done_events["first_birthday"] and age==0:
                yearly_events.append(events["first_birthday"])
                added_keys.append("first_birthday")
                done_events["first_birthday"]=True 

            if not done_events["play_school"] and age==3:
                yearly_events.append(events["play_school"])
                added_keys.append("play_school")
                done_events['play_school']=True
            
            if not done_events["joined_school"] and age==5:
                yearly_events.append(events["joined_school"])
                added_keys.append("joined_school")
                done_events["joined_school"]=True   

            possible_events=age_events[age]
            
            random_events_key=rd.choice(possible_events)

            if random_events_key not in added_keys:
                yearly_events.append(events[random_events_key])
                added_keys.append(random_events_key)
            
            event_log.append((age, events[random_events_key]['desc']))  

            for occur in yearly_events:
            
                self.apply_event(occur)

                if self.health<=0:
                    print('--------------REST IN PEACE--------------')
                    print("The child Is unlucky and ended early due to health issues🪦")
                    break

        for h in self.history:
            print(f"Age {h['age']} | Event: {h['event']}")

            if "happiness" in h:
                print(f"  Happiness: {h['happiness']}")

            if "stress_level" in h:
                print(f"  Stress: {h['stress_level']}")

            if "health" in h:
                print(f"  Health: {h['health']}")

            if "money_spent" in h:
                print(f"  Money spent: {h['money_spent']}")

            if "skills" in h:
                print(f"  Skills: {h['skills']}")

        print('-'*50+"CHILDHOOD PHASE ENDS"+'-'*50)


    def apply_event(self, event):

        old_state = {
            "happiness": self.happiness,
            "stress_level": self.stress_level,
            "health": self.health,
            "money_spent": self.money_spent,
            "skills": self.skills.copy()
        }

        # Update happiness
        if 'happiness' in event:
            self.happiness += event['happiness']
            self.happiness = max(0, min(80, self.happiness))

        # Update stress
        if 'stress_level' in event:
            self.stress_level += event['stress_level']
            self.stress_level = max(0, min(80, self.stress_level))

        # Update health
        if 'health' in event:
            self.health += event['health']
            self.health = max(0, min(90, self.health))

        # Update money spent
        if 'money_spent' in event:
            money_this_event = event.get("money_spent", 0)
            if money_this_event == 'random':
                money_this_event = rd.randint(2000, 5000)
            self.money_spent += money_this_event

        # Update skills
        if 'skills' in event:
            for skill, value in event['skills'].items():
                self.skills[skill] += value
                self.skills[skill] = max(0, min(100, self.skills[skill]))

        # Update innocence
        if "innocence" in event:
            self.innocence += event['innocence']
            self.innocence = max(0, min(80, self.innocence))

        # Update maturity
        if "maturity" in event:
            self.maturity += event['maturity']
            self.maturity = max(0, min(90, self.maturity))

        # Update emotions
        if 'emotions' in event:
            self.emotions += event['emotions']
            self.emotions = max(0, min(80, self.emotions))

        # Record changes
        changes = {"age": self.age, "event": event["desc"]}

        if self.happiness != old_state["happiness"]:
            changes["happiness"] = self.happiness

        if self.stress_level != old_state["stress_level"]:
            changes["stress_level"] = self.stress_level

        if self.health != old_state["health"]:
            changes["health"] = self.health

        if self.money_spent != old_state["money_spent"]:
            changes["money_spent"] = self.money_spent - old_state["money_spent"]

        skill_diff = {}
        for k in self.skills:
            if self.skills[k] != old_state["skills"][k]:
                skill_diff[k] = self.skills[k]
        if skill_diff:
            changes["skills"] = skill_diff

        self.history.append(changes)
        return changes

class Adult_to_matured(Child):

    def __init__(self,name):
        Child.__init__(self,name)
        self.respect=100
        self.love=0
        self.lust=0
        self.interest_in_life=100
        self.responsibility=0
        self.adult_events = {

    "sslc_exam_pass":{
        "desc": "Passed 10th with very high marks",
        "stress_level": -12,
        "happiness": +20,
        "emotions": +10,
        "respect": +25
    },

    "sslc_exam_fail":{
        "desc": "Failed in SSLC exam badly",
        "stress_level": +15,
        "happiness": -18,
        "emotions": -15,
        "respect": -20
    },

    "Hsc_exam_pass":{
        "desc": "Passed 12th with distinction",
        "stress_level": -10,
        "happiness": +25,
        "emotions": +10,
        "respect": +30
    },

    "Hsc_exam_fail":{
        "desc": "Failed in 12th board exams",
        "stress_level": +20,
        "happiness": -15,
        "emotions": -18,
        "respect": -15
    },

    "career_confusion": {
        "desc": "Severe confusion about career and future",
        "stress_level": +15,
        "maturity": +10,
        "innocence": -20
    },

    "college_strict_pressure": {
        "desc": "Heavy college workload, semester pressure",
        "happiness": -12,
        "stress_level": +5,
        "skills": {"discipline": 10, "knowledge": 18, "communication": 10},
        "maturity": +10,
        "money_spent": 500000
    },

    "love_phase": {
        "desc": "Intense love/crush phase",
        "happiness": +30,
        "emotions": +20,
        "money_spent": 50000,
        "love": +25,
        "lust": +18,
        "health": +10,
        "stress_level": -15
    },

    "breakup": {
        "desc": "Devastating breakup and emotional damage",
        "emotions": -25,
        "maturity": +20,
        "love": -35,
        "lust": -20,
        "interest_in_life": -5,
        "happiness": -50,
        "health": -3,
        "stress_level": 20
    },

    "financial_struggle": {
        "desc": "Large financial struggles",
        "stress_level": 5,
        "maturity": +15,
        "happiness": -2,
        "responsibility": +3,
        "health": -3
    },

    "Job_searching":{
        "desc": "Desperate job searching phase",
        "stress_level": +5,
        "maturity": +10,
        "interest_in_life": -8,
        "respect": -15,
        "happiness": -3,
        "responsibility": +2,
        "money_spent": 25000
    },

    "Joined_in_job":{
        "desc": "Got a good job finally",
        "stress_level": -40,
        "maturity": +15,
        "interest_in_life": +10,
        "respect": +35,
        "responsibility": +10,
        "happiness": +20
    },

    "skill_boost_in_career": {
        "desc": "Major skill development phase",
        "skills": {"communication": 10, "knowledge": 15, "cooking": 8,
                   "time_management": 12, "fitness": 10, "discipline": 10},
        "happiness":10,
        "health":15
    },

    "friend_circle_change": {
        "desc": "Big change in friend circle",
        "emotions": +8,
        "maturity": +6,
        "happiness": -5,
        "love": +10
    },

    "Marriage": {
        "desc": "Marriage with high responsibilities",
        "stress_level": -10,
        "happiness": +5,
        "maturity": +20,
        "love": +20,
        "responsibility": +10,
        "money_spent": 1200000
    },

    "Family_responsibility":{
        "desc": "Heavy expenses for family & children",
        "stress_level": +1,
        "happiness": -3,
        "maturity": +8,
        "responsibility": +3,
        "money_spent": 2500000
    },

    "family_expectation": {
        "desc": "Family expectations rise heavily",
        "stress_level": +1,
        "maturity": +5
    },

    "overthinking": {
        "desc": "Strong overthinking phase",
        "stress_level": +5,
        "happiness": -3,
        "fitness": -1,
        "maturity": -4
    },

    "job_pressure":{
        "desc": "Extreme job pressure from company",
        "stress_level": +2,
        "happiness": -1,
        "responsibility": +1,
        "health": -4
    }
}



       


        self.age_events = {
        15: [], 
        16: ["career_confusion", "friend_circle_change"],
        17: [], 
        18: ["college_strict_pressure", "friend_circle_change"],
        19: ["college_strict_pressure", "love_phase", "friend_circle_change"],
        20: ["college_strict_pressure", "financial_struggle", "love_phase", "skill_boost_in_career","breakup"],
        21: ["college_strict_pressure", "Job_searching", "financial_struggle", "love_phase"],
        22: ["Job_searching","financial_struggle", "love_phase", "skill_boost_in_career","Joined_in_job"],
        23: ["Job_searching","love_phase", "skill_boost_in_career","Joined_in_job","breakup"],
        24: ["Job_searching", "financial_struggle", "love_phase", "skill_boost_in_career","Joined_in_job","breakup"],
        25: ["Job_searching", "financial_struggle", "love_phase", "skill_boost_in_career","Marriage","Joined_in_job","breakup"],
        26: ["Marriage","Joined_in_job","family_expectation"],
        27: ["Family_responsibility", "financial_struggle","Marriage"],
        28: ["job_pressure","Marriage"],
        29: ["Family_responsibility", "financial_struggle","Marriage"],
        30: ["Family_responsibility", "financial_struggle", "overthinking","family_expectation"],
        31: ["job_pressure", "overthinking", "skill_boost_in_career",],
        32: ["job_pressure", "overthinking", "skill_boost_in_career","family_expectation"],
        33: ["job_pressure", "overthinking", "skill_boost_in_career","family_expectation"],
        34: ["job_pressure", "skill_boost_in_career"],
        35: ["job_pressure", "skill_boost_in_career","Family_responsibility"],
        36: ["job_pressure", "overthinking", "skill_boost_in_career"],
        37: ["job_pressure", "overthinking", "skill_boost_in_career","family_expectation"],
        38: ["job_pressure", "skill_boost_in_career"],
        39: ["job_pressure", "overthinking", "skill_boost_in_career"],
        40: ["job_pressure", "skill_boost_in_career","Family_responsibility"],
        41: ["job_pressure", "overthinking", "skill_boost_in_career"],
        42: ["job_pressure", "overthinking"],
        43: ["job_pressure", "skill_boost_in_career"],
        44: ["job_pressure", "overthinking", "skill_boost_in_career"],
        45: ["job_pressure","family_expectation","Family_responsibility"],
        46: ["job_pressure", "overthinking","Family_responsibility"],
        47: ["job_pressure", "overthinking"],
        48: ["job_pressure", "skill_boost_in_career"],
        49: ["job_pressure", "skill_boost_in_career"],
        50: ["job_pressure", "skill_boost_in_career","Family_responsibility"]
    }
   
    def adult(self):

        print('-'*50+'Age from 15 to 100'+'-'*50)

        done_events = {
            "sslc_exam_pass": False,
            "sslc_exam_fail": False,
            "Hsc_exam_pass": False,
            "Hsc_exam_fail": False,
            "love_phase": False,     
            "breakup": False,         
            "Job_searching": False,   
            "Joined_in_job": False,   
            "Marriage": False,        
        }

        for age in range(15, 51):
            self.age = age
            yearly_events = []
            added_keys = []

            if age == 15 and not (done_events["sslc_exam_pass"] or done_events["sslc_exam_fail"]):
                exam_result = rd.choice(["sslc_exam_pass", "sslc_exam_fail"])
                yearly_events.append((exam_result, self.adult_events[exam_result]))
                done_events[exam_result] = True
                added_keys.append(exam_result)


            if age == 17 and not (done_events["Hsc_exam_pass"] or done_events["Hsc_exam_fail"]):
                exam_result = rd.choice(["Hsc_exam_pass", "Hsc_exam_fail"])
                yearly_events.append((exam_result, self.adult_events[exam_result]))
                done_events[exam_result] = True
                added_keys.append(exam_result)
            
            

            possible_events = self.age_events.get(age, [])

            if possible_events:
                rd_key = rd.choice(possible_events)

                if rd_key == "love_phase" and not done_events["love_phase"]:
                    yearly_events.append((rd_key, self.adult_events[rd_key]))
                    added_keys.append(rd_key)
                    done_events["love_phase"] = True

                if rd_key not in added_keys:

                    if rd_key == "breakup" and not done_events["love_phase"]:
                        pass


                    elif rd_key == "Job_searching" and done_events["Joined_in_job"]:
                        pass

                   
                    elif rd_key == "Marriage" and done_events["Marriage"]:
                        pass

                    else:
                        yearly_events.append((rd_key, self.adult_events[rd_key]))
                        added_keys.append(rd_key)

                        
                        if rd_key in done_events:
                            done_events[rd_key] = True

            print(f"\nAge {age} :")

            print('-' * 90)

            if not yearly_events:
              print("No major events happened this year.")
            else:
                for key, event in yearly_events:
                    self.apply_event(event)


                for h in self.history[-len(yearly_events):]:  # only this year's events
                    print(f"Event: {h['event']}")

                    if "happiness" in h:
                        print(f"  Happiness: {h['happiness']}")

                    if "stress_level" in h:
                        print(f"  Stress: {h['stress_level']}")

                    if "health" in h:
                        print(f"  Health: {h['health']}")

                    if "money_spent" in h:
                        print(f"  Money spent: {h['money_spent']}")

                    if "skills" in h:
                        print(f"  Skills: {h['skills']}")

                    if "love" in h:
                        print(f"  Love: {h['love']}")

                    if "lust" in h:
                        print(f"  Lust: {h['lust']}")

                    if "interest_in_life" in h:
                        print(f"  Interest in life: {h['interest_in_life']}")

                    if "responsibility" in h:
                        print(f"  Responsibility: {h['responsibility']}")
                    print("-"*80)

    def apply_event(self, event):

        child_changes = Child.apply_event(self, event)


        if child_changes:
            final_changes = child_changes.copy()
        else:
            final_changes = {}

        

        adult_attrs = ["love", "lust", "interest_in_life", "responsibility"]
        adult_changes = {}

        for attr in adult_attrs:
            if attr in event:
                old_val = getattr(self, attr)
                new_val = max(0, min(100, old_val + event[attr]))
                setattr(self, attr, new_val)
                adult_changes[attr] = new_val

        final_changes.update(adult_changes)

        final_changes["age"] = self.age

        final_changes["event"] = event["desc"]

        if child_changes:
            self.history[-1].update(adult_changes)

        return final_changes
    
    def simulate_life(self):
        print(f"🌟------ Life simulation for {self.name} begins! 🌟-----")
        self.childhood()   
        self.adult()       
        print(f"\n🏁------ Life simulation completed for {self.name}!-------")
       
class OldAge(Adult_to_matured):
    def __init__(self, name):
        super().__init__(name)
        self.life_satisfaction=0
        self.mental_health=0
        self.financial_security=0
        self.social_connections=0
        self.mobility=0
        self.hobbies=0
        self.cognitive_health=0
        self.community_involvement=0

        self.old_age_events = {
            "retirement": {
                "desc": "Retired from work, adjusting to a new routine",
                "happiness": +15,
                "stress_level": -20,
                "responsibility": -80,
                "money_spent": 50000,
                "interest_in_life": +5,
                "life_satisfaction": +10,
                "mental_health": +5,
                "maturity":2,
            },
            "health_decline": {
                "desc": "Facing age-related health issues",
                "health": -25,
                "stress_level": +10,
                "happiness": -10,
                "money_spent": 100000,
                "mental_health": -3
            },
            "grandchildren": {
                "desc": "Joy from grandchildren",
                "happiness": +20,
                "stress_level": -5,
                "love": +3,
                "interest_in_life": +10,
                "life_satisfaction": +15,
                "social_connections": +2,
                
            },
            "family_responsibility_old": {
                "desc": "Supporting family and managing finances",
                "responsibility": +1,
                "stress_level": +5,
                "money_spent": 200000,
                "financial_security": -10,
                "interest_in_life": -50,
            },
            "loneliness": {
                "desc": "Feeling lonely as peers age",
                "happiness": -20,
                "stress_level": +10,
                "emotions": -10,
                "social_connections": -15,
                "life_satisfaction": -10,
                "mental_health": -10,
                "interest_in_life": -5,

            },
            "travel_or_hobby": {
                "desc": "Spending time on hobbies or travel",
                "happiness": +10,
                "stress_level": -5,
                "health": +5,
                "mobility": +5,
                "cognitive_health": +5,
                "hobbies": +10,
                "community_involvement": +5
            },
            "community_service": {
                "desc": "Participating in volunteering or local groups",
                "happiness": +10,
                "stress_level": -5,
                "social_connections": +10,
                "community_involvement": +15,
                "life_satisfaction": +10
            },
            "health_recovery": {
                "desc": "Recovering from illness or improving lifestyle",
                "health": +4,
                "mobility": +10,
                "cognitive_health": +5,
                "mental_health": +10,
                "stress_level": -5
            },
            "death":{
                "desc": "-----REST IN PEACE------"
            }
        }
        self.age_events_old = {
            60: ["retirement"],
            61: ["health_decline", "travel_or_hobby"],
            62: ["grandchildren", "travel_or_hobby","health_decline"],
            63: ["community_service", "health_decline"],
            64: ["family_responsibility_old", "travel_or_hobby"],
            65: ["grandchildren", "community_service"],
            66: ["health_decline", "travel_or_hobby"],
            67: ["grandchildren", "community_service"],
            68: ["health_decline", "travel_or_hobby"],
            69: ["family_responsibility_old", "community_service"],
            70: ["grandchildren", "travel_or_hobby"],
            71: ["health_decline", "community_service"],
            72: ["grandchildren", "travel_or_hobby"],
            73: ["family_responsibility_old", "community_service"],
            74: ["health_decline", "travel_or_hobby"],
            75: ["grandchildren", "community_service"],
            76: ["health_decline", "travel_or_hobby",'death'],
            77: ["family_responsibility_old", "community_service"],
            78: ["grandchildren", "travel_or_hobby",'death'],
            79: ["loneliness", "community_service",'death'],
            80: ["health_decline", "grandchildren", "travel_or_hobby",'death']
        }
    def old(self):
        print()
        print('-'*50+'IT CONTINUES THE SAME UPTO 60'+'-'*38)
        print()
        print('-'*50+'Age from 60 to 80'+'-' *50)

        for age in range(60, 81):  
            self.age = age
            yearly_events = []
            event_key = self.age_events_old.get(age, [])


            
            if age == 60:
                event_key = "retirement"
            else:

                possible_events = self.age_events_old.get(age, list(self.old_age_events.keys()))
                if "retirement" in possible_events:
                    possible_events.remove("retirement")
                event_key = rd.choice(possible_events)

            if event_key == "death":
                print()
                print('-------------- THANKYOU FOR EVERYTHING ------------')
                print(f"\nAge {age} : {self.old_age_events['death']['desc']}")
                print('-'*80)
                break

            yearly_events.append((event_key, self.old_age_events[event_key]))
            self.apply_old_age_event(self.old_age_events[event_key])

            print(f"\nAge {age} :")
            print('-'*90)
            
            if not yearly_events:
              print("No major events happened this year.")
            else:

                for key, event in yearly_events:
                    self.apply_old_age_event(event)



            for h in self.history[-len(yearly_events):]:
                print(f"Event: {h['event']}")

                if "happiness" in h:
                    print(f"  Happiness: {h['happiness']}")
                
                if "stress_level" in h:
                    print(f"  Stress: {h['stress_level']}")

                if "health" in h:
                    print(f"  Health: {h['health']}")

                if "money_spent" in h:
                    print(f"  Money spent: {h['money_spent']}")
                
                if "skills" in h:
                    print(f"  Skills: {h['skills']}")

                if "love" in h:
                    print(f"  Love: {h['love']}")
                
                if "lust" in h:
                    print(f"  Lust: {h['lust']}")

                if "interest_in_life" in h:
                    print(f"  Interest in life: {h['interest_in_life']}")
                
                if "responsibility" in h:
                    print(f"  Responsibility: {h['responsibility']}")
                
                if "life_satisfaction" in h:
                    print(f"  Life satisfaction: {h['life_satisfaction']}")
                
                if "mental_health" in h:
                    print(f"  Mental health: {h['mental_health']}")

                if "financial_security" in h:
                    print(f"  Financial security: {h['financial_security']}")
                
                if "social_connections" in h:
                    print(f"  Social connections: {h['social_connections']}")
                
                if "mobility" in h:
                    print(f"  Mobility: {h['mobility']}")
                
                if "hobbies" in h:
                    print(f"  Hobbies: {h['hobbies']}")
            
        print('-'*80)
        print(f"\nFinal stats at age {age}:")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")
        print(f"Stress: {self.stress_level}")
        print(f"Love: {self.love}")
        print(f"Interest in Life: {self.interest_in_life}")
        print(f"Responsibility: {self.responsibility}")
        print(f"Money Spent: {self.money_spent}")
        print(f"Maturity: {self.maturity}")
        print(f"Life satisfaction: {self.life_satisfaction}")
        print(f"Mental health: {self.mental_health}")
        print(f"Financial security: {self.financial_security}")
        print(f"Social connections: {self.social_connections}")
        print(f"Mobility: {self.mobility}")
        print(f"Cognitive health: {self.cognitive_health}")
        print(f"Hobbies: {self.hobbies}")
        print(f"Community involvement: {self.community_involvement}")   
    
    def apply_old_age_event(self, event):
   
        self.apply_event(event)

    
        old_age_attrs = ["life_satisfaction", "mental_health", "financial_security",
                        "social_connections", "mobility", "hobbies", "cognitive_health",
                        "community_involvement"]

        for attr in old_age_attrs:
            if attr in event:
                old_val = getattr(self, attr)
                new_val = max(0, min(100, old_val + event[attr]))
                setattr(self, attr, new_val)
    
                if self.history:
                    if new_val != old_val:
                        self.history[-1][attr] = new_val

        
    def simulated_life(self):
        print(f"🌟------ Life simulation for {self.name} begins! 🌟-----")
        
        # Childhood (0–12)
        self.childhood()
        
        # Adulthood (15–50)
        self.adult()
        
        # Old Age (60–80)
        self.old()
        
        print(f"\n🏁------ Life simulation completed for {self.name}!-------")
                
            


    

a=OldAge('Mohana Ganesh')
a.simulated_life()








            

            

            
        


              
        
        
        


