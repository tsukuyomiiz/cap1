label episode_01:

    $ _game_menu_screen = "save"

    $ quick_menu = True

label aiden_01:    

    pause 2.0    

    scene black with diss

    "The year is 2595 A.N." with Dissolve(0.6)

    "For as long as I've been alive, the world has been in trouble."

    play snd "sounds/footsteps_double_stomp_01.ogg"

    "The last remnants of the Empire have all but withered away." 

    "Every day, things get harder and harder for us people under the disks."

    "Corruption and crime run rampant, completely dominating the life of innocent citizens."

    play snd "sounds/suit_movement_01.ogg"

    "But if you think I'm going to take that lying down, you've got another thing coming."

    play music "music/addictive_waveform.ogg" volume 0.8

    play snd "sounds/punch_06.ogg"

    scene nox_warehouse 

    show aiden suit_gun serious at off

    show letterbox

    with hp

    a "Take that, asshole."

    "Honestly, to call this guy an asshole is practically a compliment."

    "He's not just any ordinary asshole. He's a Nox asshole. A member of their damned crime syndicate."

    "Thieving, prostitution, chem peddling, arms deals... If it's illegal and makes money, they got a piece of the action."

    "They're the syndicate that made an orphan out of me, and the one that I'll spend the rest of my life trying to stamp out."

    "Well, that's if they last that long, that is."

    "I'll do my best to make sure that isn't the case."

    "Thankfully, I'm not alone. I've got the best support an agent could want."

    play snd "sounds/radio_receiver_01.ogg"

    n "Status report, Nightwatcher?"

    "The voice in my ear is Nevin, my intel agent. He's my eye in the sky, making sure I'm informed and safe when infiltrating tough spots like these."

    a "I've made it in. Just sent a guard to sleep."

    play snd "sounds/footsteps_boots_01.ogg"

    scene nox_warehouse:

        align (0.5, 0.5)
        zoom 1.1

    show letterbox  

    show aiden suit serious at off

    with diss

    "I whisper into my comm-link as I sneak further into the dark warehouse, keeping my eyes and ears peeled for any more Nox grunts standing guard."

    n "Perfect. You're really close to the target."
    
    a "Directions?"

    n "According to the schematics, there should be a hallway to your right."

    a "Got it."

    play snd "sounds/footsteps_boots_01_fast.ogg"

    scene hallway_13_n

    show letterbox  

    show aiden suit serious at off

    with dis 

    "Sticking to the shadows, I enter the hallway, descending further into this maze of a warehouse."

    play snd "sounds/radio_receiver_01.ogg"

    n "About halfway down there should be a door to your left."

    a "I see it."

    n "In there."

    a "Roger."

    play snd "sounds/door_lock_04.ogg"

    "I try to open the door, but it's not quite so easy as that."

    a "Locked."

    "Quite a lock too. A fancy one."

    qa "Looks like our intel was good, those Nox bastards must have something pretty special hidden in here."

    qa "Still, a lock like this is no match for me."

    play snd "sounds/lockpick_01.ogg"

    "Whipping out my pick, I make quick work of their security efforts."

    stop snd fadeout 0.2

    play snd "sounds/door_unlock_01.ogg"

    a "Unlocked."

    n "Okay great. Now, careful in this next room, it's likely guarded, so stay hidden." 
    
    n "Just ID the payload and backup will be on the way."

    a "Roger."

    play snd "sounds/door_open_slow_01.ogg"

    scene cargo_bay at hs

    show letterbox  

    show aiden suit serious at off

    with dis 

    "Opening the door as quietly as I can, I take a peek inside before entering the large loading bay."

    "Just as we suspected, that's where they are keeping the shipment."

    qa "But... I don't see any guards. Strange."

    qa "Then again, we're catching them before transit. Their security should be weaker than usual."

    play snd "sounds/footsteps_boots_02.ogg"

    scene cargo_bay

    show aiden suit serious at off

    with dis 

    "I take out my jammer and scan the room for any alarm systems I can find. Once I'm convinced they're disabled, I take a step inside."

    qa "No blaring alarms... That's good."

    "Still, I stick to the darkness as I risk a closer look at the shipping containers."

    a "They seem like... chems of some sort..."

    play snd "sounds/radio_receiver_01.ogg"

    n "Recreational?"

    a "I don't think so..."

    a "Maybe medical? Or war-chems... Either way there's a lot of them."

    n "Roger. Any indication where they are being sent?"

    a "Looks like they are ready to be loaded onto a train to... looks like Schela is the final destination."

    n "Out of the state then..."

    a "Yup."

    n "Okay then. Sending a recovery team."

    a "Sounds good, I'll--"

    "As I'm giving him the all-clear, some movement catches my eye."

    a "Hold on, I think we have company."

    "Receding further into the darkness, I see a couple of shadowy figures walk into the warehouse."

    "One is a massive beast of a man. I don't believe I've ever seen him before."

    "The other... The other I recognize."

    $ unlock_codex_entry("character_aiden_furin")

    $ unlock_codex_entry("character_zeph")

    $ unlock_codex_entry("location_schela")

    $ unlock_codex_entry("location_nuria")

    a "I think that's... Is that Zeph?"

    n "Zeph?!"

    scene cargo_bay at bgz

    show zeph base neutral:

        xalign 0.5 yalign 0.2 zoom 1.2
        anchor (0.5, 0.15)

    with dis

    "As he gets closer, there's clearly no mistaking the Nox sub-boss."

    show aiden suit serious at off

    a "It's him."

    n "Are you sure?!"

    a "His scar is hard to miss..."

    n "R-right..."

    n "Anyway, what the heck is he doing there of all places?"

    a happy "I don't know, but this is our lucky day."

    qa "Catching a Nox sub-boss at the scene of the crime... I can't remember the last time we've had such a lucky break."

    qa "Now to not squander it."

    scene cargo_bay 
    
    show aiden suit serious at off
    
    with dis

    a serious "I'll lie low."

    "I whisper to Nevin as quietly as I can."

    play snd "sounds/cock_submachine_01.ogg"

    noxtrooper "Hey you!"

    qa "Not quietly enough, it seems."

    a sigh "So much for that..."

    scene cargo_bay at bgz

    show letterbox

    show aiden suit serious at off

    with diss

    $ unlock_codex_entry("lore_aegis")

    noxtrooper "Sound the alarm! They're here! AEGIS is here!"

    a serious "Got that right!"

    "If Nox is a virus, which it is, AEGIS is the cure."

    "A tiny speck of light in the darkness which is Neo-Elysian life, providing hope for the people."

    "The last government agency dedicated to stomping out violent crime rings like them."

    "Put short: We're the good guys. They're the bad guys. Enough said."

    play snd "sounds/punch_07.ogg"

    play amb "<silence 2.5>"

    queue amb "ambient/base_alarm_01.ogg" fadein 0.5 volume 0.6

    with vp

    pause 0.3

    with hp

    stop music fadeout 4.0

    "Rushing the goon, I take him out before he can make more of a commotion, but it's too late."

    "The alarm is already blaring."

    a upset "Shit!"

    play sound "sounds/footsteps_military_squad_01.ogg"

    play snd1 "<silence 2.2>"

    play snd2 "<silence 2.3>"

    play snd3 "<silence 2.4>"

    play snd4 "<silence 2.5>"

    queue snd1 "sounds/cock_submachine_01.ogg"

    queue snd2 "sounds/cock_submachine_02.ogg"

    queue snd3 "sounds/cock_shotgun_01.ogg"

    queue snd4 "sounds/cock_shotgun_02.ogg"

    "Before I know it, a dozen fully armed Nox soldiers have rushed into the cargo bay to surround me."

    "They aren't the only ones who have come by to greet me though."

    play music "music/dread_unseen.ogg" fadein 3.0

    stop amb fadeout 1.2

    zeph "What do we have here?"

    a "Hey Zeph..."

    play snd "sounds/footsteps_boots_03.ogg"

    scene cargo_bay

    show aiden suit serious at off

    show zeph base neutral at pos5 
    
    with diss

    zeph "It seems my reputation precedes me..."

    a "You've made quite a name for yourself, that's true."

    zeph "Of that, I am proud."

    zeph "I can't say the same for... whoever the hell you are."

    a "Me? I'm nobody."

    zeph "You will be shortly, yes."

    "The smug, sinister tone of his voice is more intimidating than I imagined it might be."

    "But I keep my nerve, trying my best to not show fear."

    zeph "I see you are here all by your lonesome."

    a "Yup, just me... Against all of you..."

    zeph "That doesn't seem fair, does it?"

    zeph "By all means, attempt to call your pathetic AEGIS compatriots."

    "Just for the sake of theater... and buying time before reinforcements arrive, I try to do as he asks."

    a "Damn, doesn't work."

    zeph "Such a shame. It seems someone must be jamming your communications device."

    zeph "Who knows how long it will be before your friends realize your absence?"

    qa "The only thing that makes that condescending voice tolerable is the fact that this idiot really seems to be unaware backup is already on its way."

    qa "At least I've got that in my favor."

    qa "Now to play the cards I have to my advantage and burn time..."

    a serious "So, what do you have here?"

    "I say, gesturing to the stockpile of chems."

    zeph "Wouldn't you like to know."

    a "I would, actually."

    a "Quite a lot of them for a small fry like you."

    zeph serious "Small fry, huh? Trying to get on my nerves, I see."

    a "Just stating the truth."

    zeph "Don't take me for a fool, AEGIS scum."

    a "Really? Why not? You seem like a fool to me."

    a "It was a real stroke of genius to incriminate yourself by personally accompanying your illegal chem shipment."
    
    a "Boss Hevlan's death must have really amped up your greed. Gunning for his spot, are you?"

    "Suddenly not so amused, Zeph points to me with that metallic hand of his."

    zeph neutral "Men, take him alive. I have use for him."

    stop amb

    play snd "sounds/footsteps_military_squad_02.ogg"

label s01:

    if _in_replay:
        play music "music/dread_unseen.ogg" fadein 3.0

    scene cargo_bay at bgz

    show letterbox

    show aiden suit serious at off

    with dis 

    "In completely synchronized motion, the soldiers begin to rush me."

    "Ducking back into the darkness, I try to dodge their attacks as best I can."

    "I know I can't take all of them out. Strong as I am, there's simply too many of them."

    "But that's not the goal here."

    "The only goal is to survive until help arrives."

    play snd "sounds/gunshot_laser_02_sequence.ogg"

    $ unlock_codex_entry("lore_laser_pistol")

    "I start off by using my laser pistol, set to stun."

    "It's always AEGIS protocol to use non-lethal force when possible. Besides, by the time they wake up, backup will have already mopped things up."

    "However, the laser pistol can only hold them off so long."

    stop amb

    play snd1 "sounds/fight_01.ogg"

    play snd2 "<silence 1.5>"

    queue snd2 "sounds/gunshot_laser_01.ogg"

    play snd3 "<silence 4.0>"

    queue snd3 "sounds/gunshot_laser_02.ogg"

    scene cargo_bay at fight:

        zoom 1.3
        align (0.5, 0.5)

    show letterbox at fight

    with dis

    show aiden suit serious at off

    "Once they get close enough, I start swinging at them with my fists and feet, attempting to regain some distance." 

    "I dodge and block as many attacks as possible, occasionally taking out the soldiers that come too close with a well-timed punch or kick."

    show zeph base neutral at off

    zeph "Come on, you idiots! How many of you useless pieces of shit does it require to take down one mere agent of AEGIS?"

    qa "That's his mistake."

    qa "Thinking I'm just a mere agen--"

    scene cargo_bay at bgz

    show letterbox

    show aiden suit serious at off

    stop snd1 fadeout 0.1

    stop snd2 fadeout 0.1

    stop snd3 fadeout 0.1

    play snd "sounds/hit_brass.ogg"

    queue snd "sounds/blood_01.ogg"
        
    with hp

    a pain "UGH!!!"

    "Blood flies out of my mouth as a Nox flunky's brass knuckles make hard contact with my jaw, causing me to tumble to the ground.."

    qa "Fuck, that hurts!!!"

    qa "Ugh..."

    qa "Could be worse though. At least I'm still conscious."

    play snd "sounds/footsteps_military_squad_01.ogg" volume 1.0

    play snd1 "<silence 1.5>"

    queue snd1 "sounds/touching_body_01.ogg"

    queue snd "sounds/rope_01.ogg"

    queue snd "sounds/rope_02.ogg"

    "Before I'm able to rally myself, the soldiers dogpile me into place, tying my hands behind my back, shortly followed by them fastening my legs together."

    "I'm completely immobile..."

    play snd "sounds/footsteps_boots_03.ogg"

    show zeph base neutral at cz 

    show aiden suit serious at off

    with diss

    zeph "There we are."

    zeph "I'm sorry for the rough treatment, friend."

    stop snd1 fadeout 0.2

    a "I can't imagine you're very sorry."

    zeph "Correct. I'm not really your friend, either." 
    
    zeph "Nonetheless, it had to be done. You're our ticket out of here."

    a "How do you think that?"

    zeph "I think your friends outside will have to let us through, or else they won't be getting you back in one piece, so to speak..."

    a "Are you threatening the dismemberment of a government official?"

    zeph "First of all, you are an AEGIS official."

    zeph "We make special exceptions for you pests, after all the pain you cause..."

    a "Good to know we're doing our job."

    zeph "Alas, as much of a pleasure as it might be to indulge in such barbaric behavior... I am not actually going to have you dismembered... As hungry for vengeance as I might be..."

    zeph "No, instead I have something a lot more civilized in mind."

    a smile "Nox? Civilized? Don't make me laugh."

    zeph "You offend me... Null, perhaps teach this smug bastard a lesson while I get his medicine ready?"

    null "With pleasure, boss."

    play snd "sounds/footsteps_boots_04.ogg"

    hide zeph with diss

    "That hulking brute of a man I spotted accompanying Zeph before approaches me and--"

    play snd "sounds/hit_head.ogg"

    queue snd "sounds/blood_01.ogg"
        
    with hp

    "WHAAAAAAAAAAAAAACK!!!"

    a upset blood "URGHHHHHH!!!"

    qa "Fuck, that hurts!!!"

    play snd "sounds/spit_01.ogg"

    show zeph base at off

    zeph neutral "Heh... There... I see that Null has managed to wipe that insufferable smile off your face."

    a evil -blood "What smile?"

    "I respond as smugly as I can, showing him the biggest shit-eating grin I can muster."

    zeph "Oh? Still have spirit, do you?"

    a "If you thought you could stomp that out with your weak bullshit, you don't know much about AEGIS... or me..."

    zeph "Hmmm... Is that so? What is there to learn about you?"

    a "That I'm not going to ever stop until you scumbags are--"

    play snd "sounds/hit_brass.ogg"

    with hp

    a pain "OOOOOOOOOOH!!!"

    qa "DAMN THAT FUCKING HURTS..."

    qa "But what I said is true..."

    qa "He won't break me..."

    qa "Not now... Not ever..."

    zeph "Still feel like smiling?"

    a evil "You can still both fuck right off..."

    "Zeph shakes his head."

    play snd "sounds/footsteps_boots_05.ogg"

    show zeph base at cz with diss

    zeph "Well, no matter."

    zeph "To let you in on a secret, I was going to get Null here to give you some special attention whether you were smiling or not."

    zeph "After all, you AEGIS pigs have been costing us a lot of money... So much money..."

    zeph "But not tonight."

    play snd "sounds/syringe_01.ogg"

    "He picks up a syringe and fills it with a weird silvery liquid from some fancy-looking vial."

    play snd "sounds/syringe_flicking_01.ogg"

    "It doesn't look good, that is for damn sure..."

    zeph "See this?"

    "He says, flashing that damn needle in my face."

    a smile "Nope..."

    show zeph serious

    "He grimaces. I guess he hoped that line would land better."

    zeph "This is our insurance policy."

    play snd "sounds/injection_01.ogg"

    "Zeph brings the needle right to my neck, barely pricking my skin."

    zeph "If you don't do exactly what we say, then--"

    play snd "sounds/body_hit_01.ogg"

    queue snd "sounds/body_fall_01.ogg"

    stop music fadeout 5.0

    null "UGH!!!" with vp

    "All of a sudden, the big bruiser that was just punching me in the face unceremoniously falls to the ground."

    play snd "sounds/footsteps_single_01.ogg"

    "Probably wondering what the hell is going on, Zeph spins around, turning his attention away from me and to the commotion."

    zeph "What the heck are you doing?!"

    stop music fadeout 2.0

    null "Something hit me in the head..."

    zeph neutral "Hit you? Are you...?" 
    
    zeph "No..."

    "Terrified, Zeph looks upwards into the darkness, straining his eyes to see what's there."

    play snd "sounds/dramatic_hit_01.ogg"

    show silencer_flash with Dissolve(0.1)
    hide silencer_flash

    m "Run."

    "A cold, malevolent voice echoes through the warehouse."

    "One that turns the blood of all the Nox members to ice, but fills me with relief."

    play music "music/cyberpunk.ogg" fadein 2.0

    "Backup is here."

    zeph "Wh-what the..."

    zeph "They're here already?! How?!"

    null "Who cares?! Let's get out of here!!!"

    "The flunky screams back, scrambling to his feet."

    show silencer_flash with Dissolve(0.1)
    hide silencer_flash

    play snd "sounds/dramatic_hit_02.ogg"

    m "RUN!!!" with vp

    play snd1 "sounds/footsteps_running_away_crowd_01.ogg"

    "They obey."

    "I can't blame them."

    "Why? Because they know they're finished."

    "It's every man for himself."

    "In a complete panic, the Nox members start fleeing every which way."

    play snd "sounds/footsteps_boots_04_fast.ogg"

    play snd1 "<silence 0.5>"

    queue snd1 "sounds/glass_shattering_01.ogg"

    hide zeph with dis

    "As Zeph runs, he drops the needle, pricking my skin a bit more before it falls to the ground, shattering and spilling its foul smelling contents all over the floor."

    "I do my best to roll away from it, but I can't make it far."

    "I'm still helpless."

    "But not for long..."

    "Because it's not just ordinary, run-of-the-mill backup I'm receiving."

    "She's here."

    play snd "<silence 0.5>"

    play snd1 "<silence 0.5>"

    queue snd "sounds/footsteps_running_away_crowd_01.ogg"

    queue snd1 "sounds/footsteps_military_squad_01_away.ogg"

    show silencer_flash with Dissolve(0.1)
    hide silencer_flash

    scene cg01_01 at subtle_life:
        
        zoom 0.5
        
    with dis

    noxgrunt "RUN!!! RUN!!!"

    noxgrunt "IT'S HER!!! SILENCER!!!"

    "Silencer."

    "The codename that instills fear in every syndicate member on the south coast."

    "And seeing her from this angle, I can't exactly blame them for that."

    "She's a terrifying, powerful presence, but at the same time agile and graceful."

    "Her reputation precedes her for good reason."

    "She's been the bane of the syndicate for years now."

    "AEGIS's heavy artillery."

    qa "Thank goodness she's here to rescue me... I'd hate to be her enemy."

    play snd "<silence 0.2>"

    queue snd "sounds/impact_ground.ogg"

    scene cargo_bay at bgz

    show luna mask at cz

    with vp

    show luna mask_gun at cz with Dissolve(0.4)

    pause 0.1

    play snd1 "sounds/gunshot_blaster_01.ogg"

    play snd2 "<silence 0.4>"

    play snd3 "<silence 0.9>"

    play snd4 "<silence 1.2>"

    queue snd2 "sounds/gunshot_blaster_02.ogg"

    queue snd3 "sounds/gunshot_blaster_01.ogg"

    queue snd4 "sounds/gunshot_blaster_02.ogg"

    "Swooping down from the rafters, she immediately takes charge of the situation, methodically dismantling thug after thug."

    "Most with her laser pistol, but some particularly lucky grunts get some extra-special treatment."

    stop snd1

    stop snd2

    stop snd3

    stop snd4

    play snd "sounds/heavy_punch_gore_03.ogg"

    show luna mask_gun:

        xalign 0.5 yalign 0.2 zoom 0.8
        hit("left", 0.2)

    with Dissolve(0.01)    

    "A well-timed strike to the face."

    "That's lights out for them."

    "If not, no big deal. They just get another."

    flunky "She's a demon!!!"

    silencer "Silence, Nox scum!"

    play snd "sounds/heavy_kick_01.ogg"

    show luna mask_gun:

        xalign 0.5 yalign 0.2 zoom 0.8
        hit("left", 0.2)

    with Dissolve(0.01)  

    pause 0.4

    play snd "sounds/heavy_kick_02.ogg"

    show luna mask_gun:

        xalign 0.5 yalign 0.2 zoom 0.8
        hit("right", 0.2)

    with Dissolve(0.01)  

    "She roars, only increasing the sense of anxiety as the grunts flee from her, as she easily dispatches opponent after opponent."

    play snd "sounds/footsteps_military_squad_02.ogg"

    play snd1 "sounds/footsteps_military_squad_01.ogg"

    play snd2 "sounds/gunshot_laser_rapid_fire_01.ogg"

    play snd3 "sounds/gunshot_laser_rapid_fire_02.ogg"

    play snd4 "<silence 0.7>"

    queue snd4 "sounds/gunshot_laser_rapid_fire_03.ogg"

    "Taking advantage of the chaos, other AEGIS agents pour into the cargo bay, taking down the fleeing Nox members with ease."

    "Eventually, all but one syndicate member has been taken down."

    play snd "sounds/footsteps_three_steps_heels_01.ogg"

    scene cargo_bay

    show luna mask_gun at pos2

    show zeph base neutral at pos8

    with diss

    silencer "Zeph, I presume?"

    stop snd fadeout 0.1

    stop snd1 fadeout 0.1

    stop snd2 fadeout 0.1

    stop snd3 fadeout 0.1

    stop snd4 fadeout 0.1

    zeph "Fuck you, bitch."

    silencer "Just as charming as I remember you."

    zeph "Suck my dick, you rancid cow."

    qa "Big mistake..."

    play snd "sounds/footsteps_single_heels_01.ogg"

    play snd1 "sounds/footsteps_single_heels_02.ogg"

    pause 0.1

    play snd2 "sounds/heavy_kick_03_gore.ogg"

    scene cargo_bay at bgz

    show letterbox

    show luna mask_gun at cz

    with hp

    pause 0.2

    play snd "sounds/footsteps_single_heels_05.ogg"

    play snd5 "sounds/body_fall_03.ogg"

    "Flying into action, Silencer perfectly executes a roundhouse kick to the face, making perfect contact with his nose."

    show luna mask_gun at cz

    show zeph base pain blood at off

    zeph "RAAAAAGH!"

    "Zeph falls to the ground, blood pouring out of his nose and mouth."

    play snd "<silence 0.3>"

    queue snd "sounds/handcuffs_01.ogg"

    show luna mask with Dissolve(0.5)

    "Before he can get his wits about him, she cuffs his hands and legs."

    silencer "What did you call me, you disgusting pig?"

    zeph "Uuuuuuuugh..."

    silencer "I thought so."

    play snd "sounds/radio_receiver_02.ogg"

    silencer luna mask_alt "Operator? This is Silencer, reporting in. I have secured the primary and secondary target."

    show aiden suit neutral at off

    a "Nice job."

    play snd "sounds/footsteps_four_steps_heels_01.ogg"

    "Before responding to my compliment, she does her duty and double-checks the perimeter to make sure all the enemies have been subdued."

    stop snd fadeout 0.1
    
    $ persistent.unlocks.add("s01")

    $ renpy.end_replay()  

label s02:

    if _in_replay:
        play music "music/cyberpunk.ogg" fadein 4.0

    scene cg02a_01

    show luna mask at off

    show aiden suit neutral at off
        
    with diss

    silencer "Thank you, Nightwatcher."

    a "Couldn't have cut it any closer, could you?"

    silencer "Well, I wasn't expecting you to get caught."

    silencer "Sloppy of you."

    a nervous "Easy for you to say. You weren't the one infiltrating the base."

    silencer "As I remember it, you were the one who insisted on being the point man."

    a cheeky "What can I say? Nobody else volunteered..."

    silencer "Rewriting history, are you? That's not how I remember it."

    silencer "I remember putting my name forward and being shouted down by a certain Nightwatcher."

    a seductive "Well, I couldn't let my precious Lulu be exposed to such danger."

    silencer "Not here..."

    a cheeky "What?"

    silencer "You know what."

    "I know she hates it when I call her by her nickname in front of other people, especially during a mission."

    a seductive "Is something the matter, Lulu?"

    stop music fadeout 3.0

    play music1 "music/future_relaxation_zone.ogg" fadein 5.0

    play snd "sounds/mask_removal_01.ogg"

    scene cg02a_02 

    hide luna

    show luna suit neutral at off

    show aiden suit nervous at off
    
    with Dissolve(1.5)

    $ unlock_codex_entry("character_luna_virelith")

    silencer "You know, if you keep that up, I think I might leave you here."

    "She says, pulling off her mask, and revealing the beauty within."

    "My wife and the love of my life, Luna."

    "I spot the smallest hint of a smile on her lips as she teases me."

    "She's never been too keen on being lovey-dovey in public, but small hints like that are always cute to see."

    "Despite wanting to project a cold, professional exterior, she still has that part of her that shines through."

    a "Oh, come on, you don't want to do that."

    l "I don't?"

    a smile "No way you could leave your partner tied to the floor, could you, Lulu?"

    l "Don't tempt me."

    a nervous "Come on... Don't tease me..."

    l "It's fun, though..."

    a sigh "Lulu..."

    "She shakes her head."

    l "Fine..."

    play snd "sounds/footsteps_single_heels_01.ogg"

    queue snd "sounds/knife_01.ogg"

    queue snd "sounds/clothes_movement_01.ogg"

    show cg02a_02:

        zoom 1.5

    with Dissolve(1.2)    

    "Unholstering her knife, she makes quick work of the straps the Nox grunts used to tie me down."

    a "Thanks! Those were really starting to itch."

    l "Were they now?"

    a sad "Yeah, although my mind was mostly elsewhere."

    a happy "It's mostly nice to be free again."

    $ persistent.unlocks.add("s02")

    $ renpy.end_replay()

    play snd "<silence 0.3>"

    queue snd "sounds/footsteps_boots_single_01.ogg"

    scene cargo_bay

    show luna suit neutral at pos5

    show aiden suit neutral at off

    with vshake((0, 0, 0, 0), 0.2, dist=20)

    "After stretching briefly, I spring back up onto my feet in one fluid motion, even taking Luna by surprise."

    "...However, the impressive gymnastic feat isn't without consequence."

    scene cargo_bay

    show luna suit neutral at pos5

    show aiden suit neutral at off

    $ renpy.music.set_volume(0.2, delay=0.8, channel="music1")
    $ renpy.music.set_pan(-0.8, delay=0.6, channel="music1")
    pause 0.3
    $ renpy.music.set_pan(0.8, delay=0.6, channel="music1")

    show layer master:
        zoom 1.05
        align (0.5, 0.5)
        blur_vision(15)
        ease 1.0 xoffset 10 yoffset 5
        ease 1.0 xoffset -10 yoffset -5
        ease 1.0 xoffset 5 yoffset -8

    with diss

    $ renpy.music.set_pan(0.0, delay=1.0, channel="music1")
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music1")

    scene cargo_bay

    show luna suit neutral at pos5

    show aiden suit neutral at off

    with diss

    a serious "W-whoa..."

    play snd "<silence 0.7>"

    queue snd "sounds/wall_hit_01.ogg"

    scene cargo_bay at bgz

    show letterbox

    with dis

    "Feeling somewhat faint, I prop myself up against the nearby wall as I regain my fortitude."

    play snd "sounds/footsteps_single_heels_07.ogg"

    queue snd "<silence 0.3>"

    queue snd "sounds/footsteps_single_heels_04.ogg"

    show luna suit neutral at cz

    show aiden suit neutral at off

    with Dissolve(0.8)

    l "Hmm? You alright?"

    a neutral "Totally... I just guess the blood rushed away from my head, that's all..."

    l "Is that so?"

    "She asks, seemingly doubting my explanation."

    a surprised "I think so?"

    a "Is something wrong?"

    "She seems to think on it for a second before shaking her head."
    
    show luna suit_alt happy

    l "Of course not."

    l sigh  "I was simply concerned."

    a neutral "No worries, it's all good."

    a happy "I'll be back to 100%% in just a sec."

    l suit neutral "Good. While you gather yourself, I'll aid with the cleanup."

    a neutral "Thanks, I'll just be a sec."

    play snd "sounds/footsteps_three_steps_heels_01.ogg"

    hide luna with diss

    "After waiting another second to make sure I'm fine, she leaves me alone and helps the others."

    "She isn't the only one showing concern though."

    play snd "sounds/radio_receiver_01.ogg"

    scene cargo_bay

    show aiden suit serious at off
    
    with Dissolve(0.9)

    n "Nightwatcher, do you copy?"

    a look "Yes, I do..."

    n "Phew... That's good news..."

    n "When you went silent I have to admit, I was worried..."

    a neutral "I'm fine, they just jammed my comms."

    n "Good to hear you're safe and sound!"

    a look "Yeah I'm fine, just slightly light-headed."

    n "Did something happen?"

    a embarrassed "I just got up too quickly..."

    n "I see..."

    n "Well, when your comms re-established, your vitals did seem strange for a moment..."

    a neutral "It's probably nothing. Just a comms error."

    n "Maybe..."

    n "We'll give you a quick physical when you check in. Can't be too careful!"

    a sigh "Whatever helps you sleep at night."

    n "It's protocol."

    a look "All good, I'll make sure I will. Now I gotta get back to it."

    n "Understood."

    qa "They really are overreacting..."

    qa "Anyway, that's for later, I have a mission to complete."

    $ unlock_codex_entry("location_neo_elysia")

    $ unlock_codex_entry("lore_nox_syndicate")

    $ unlock_codex_entry("lore_chem")

    stop music1 fadeout 1.0

    scene black with pixellate

    pause 0.5

    play music "music/breaking_headlines_news.ogg"

    scene edric_quarters at bgz

    show letterbox
    
    show aiden suit look at off
    
    show luna suit neutral at lz

    show edric base neutral at rz
    
    with pixellate

    a "Agent Furin and Agent Virelith reporting in."
    
    e "Ah, good. The triumphant heroes have returned."

    e "Does it feel good?"

    a "I feel lucky, more than anything."

    e "Well, as they say, better lucky than good."

    e "I can't believe that after all this time, we managed to catch Zeph in a Nox warehouse during a chem deal..."

    e "Incredible."

    l "I have to admit, cuffing him did feel quite satisfying..."

    e "I only wish I had managed to do exactly that in my younger years."

    e "Alas, such is life..."

    e "So, what kind of cargo did we catch them with?"

    l "Synth-chems, mostly. Headed to Schela."

    e "Schela? Huh..."

    e "That's not Zeph's usual MO."

    a serious "It's out of the ordinary, no doubt." 
    
    a "But what's stranger is I don't think they're actually going to be flipped on the black market or anything like that."

    e "Then what purpose would they have for material like that?"

    a look "I think they planned to manufacture it somehow..."

    e surprised  "Manufacture it? Into what?"

    a serious "I don't know... Maybe some kind of war-chem?"

    a "Zeph tried to stick me with something before backup showed up."

    a look "He didn't have the chance, but it didn't look like anything I've seen before."

    e serious "Did you manage to get a sample of it?"

    l "A small one, yes."

    e "Good. I presume it's being analyzed?"

    l "Yes, sir. As we speak."

    e smirk "Excellent."

    "He smiles that cunning, vicious smile that often comes across his lips when he discusses the syndicates."

    e "Just one day closer to the day we put a permanent end to those bastards."

    l "Absolutely."

    a neutral "I can't wait."

    e serious "You aren't the only ones..."

    e "I'm sure every one of the people on this base feels the same way."

    e "And hell, maybe we don't have to wait too much longer."

    e "After all, ever since Boss Hevlan kicked the bucket last month, they've been flailing."

    e "Every sub-boss in the state has been trying to take a bigger piece of the pie and stepping on each other's toes."

    $ unlock_codex_entry("character_boss_hevlan")

    a cheeky "Who'd have thought that a bunch of unloyal, striving freaks wouldn't be the most loyal allies once the man keeping them in charge shuffles off?"

    e "It is sadly predictable, isn't it?"

    l suit_alt "I can't say I'm disappointed."

    l "Less work for us."

    a neutral "And the sooner our work is done, the better."

    l suit "Indeed."

    e neutral "Well, although it might only be temporary. I'm prepared to say your work is done for now."

    e "Enjoy some R&R. You're both dismissed."

    e "Report back on Wednesday at 0800 for your next briefing."

    a look "Yes, sir!"

    l "Yes, sir!"

    scene edric_quarters
        
    with dis

    qa "Whoa! That's way more of a break than I anticipated."

    qa "Not that I'm complaining."

    "It's a welcome reprieve, as we've been going at it pretty hard ever since Boss Hevlan met an unexpected end, a death that is still a mystery to AEGIS as a whole."

    "As much as we were gunning for an arrest on the guy, and frankly, don't mind seeing him bite the dust, it's something we had absolutely nothing to do with."

    "Just one of life's little moments."

    "Still, being so unexpected, it created a hell of a lot of chaos as the whole Nox syndicate was thrown into a crisis of leadership."

    "Apparently, Boss Hevlan died without an heir apparent, causing a ton of in-fighting between the sub-bosses."

    "A problem for them, but a big boon to us. One that has kept us very busy."

    "Some rest and relaxation is exactly what the doctor ordered, and I know exactly what the first stop is going to be."

    $ unlock_codex_entry("character_captain_edric")

    stop music fadeout 2.0

    scene black with diss

    pause 0.5

    play music1 "music/imagine_the_future_underscore.ogg" fadein 1.0

    scene aegis_cafeteria at bgz
    
    show aiden suit surprised at off
    
    show luna suit neutral at cz
    
    with diss

    a "Finally, I was starving."

    l "You're always starving..."

    a sad "Nah, come on, you know that ain't true."

    l "Alright, technically true."

    l "Only most of the time."

    a embarrassed "Okay, maybe that's closer to the truth."

    a neutral "I wonder what they're serving tonight?"

    l "I'm curious myself..."

    scene black with circuit_in

    scene aegis_cafeteria at hs with circuit_out

    "As it turns out, the nightly menu is one of the AEGIS staples, meatloaf ration with root vegetable paste."

    "The root vegetables might be simulated, but it's still one of my personal favorites."

    scene aegis_cafeteria at bgz
    
    show aiden suit happy at off
    
    show luna suit neutral at cz
    
    with diss

    a "That hits the spot."

    l "It certainly satisfies."

    a neutral "Do you want seconds?"

    l smile "No thank you, what I had was sufficient. You go ahead though."

    a joyous "Don't mind if I do!"

    play snd "<silence 0.3>"

    queue snd "sounds/footsteps_double_01.ogg" volume 0.7

    scene aegis_cafeteria with Dissolve(0.8)

    "Heading back up to the counter, I take a second helping of meatloaf and simulated vegetables."

    "But, while I'm there, I spot something that I didn't see the first time around."

    show aiden suit surprised at off

    a "Oh damn, did that just come out of the oven?"

    $ unlock_codex_entry("lore_mineral_cake")

    chef "The mineral cake? It certainly did."

    a neutral "I'll take a slice of it. An extra-large one."

    chef "Heh... Sure you don't want to finish those seconds first, Aiden? Make sure you have room?"

    a sigh "Please, sir... First of all, you know me better than that. I always have room."

    a neutral "Second, that slice is for my wife."

    chef "Ha... Say no more."

    play snd "sounds/plate_01.ogg"

    "The chef cuts me off a substantial piece for Luna."

    scene black with diss

    "I thank him and then scurry back off towards the table with her dessert in hand."

    scene aegis_cafeteria at bgz
    
    show aiden suit happy at off
    
    show luna suit neutral at cz
    
    with diss   

    a "Here you go, Lulu."

    l shocked "W-what?! There was mineral cake?!"

    a happy "It just came out of the oven. I thought you might like a slice."

    l "Th-thank you! It looks delicious!"

    play snd "sounds/plate_02.ogg"

    queue snd "sounds/fork_01.ogg"

    show luna neutral

    "As soon as I set it before her, she takes a forkful and stuffs it in her mouth."

    l happy "Mmm..."

    l "It's pretty good today!"

    a "Well, if anyone could make that judgment, it would be you."

    l neutral "Hmm? What do you mean?"

    a joyous "Come on... You're a cake connoisseur."

    a surprised "I'm not quite sure I know anyone here that eats as much of the stuff as you do."

    l neutral "Well... I guess you're right..."

    l "We don't have that many sweets around here though, so I enjoy them when I can."

    scene aegis_cafeteria

    show black_overlay

    show letterbox

    with dis

    "What she says is true."

    "Although AEGIS takes care of us and provides us with pretty nutritious meals, they are rather basic."

    "Not many fancy desserts, that's for sure."

    "Even the ones they provide, like this mineral cake, are especially formulated to keep us healthy."

    "Everything a good agent needs to keep them going, and Luna's as good as an agent gets."

    "She deserves a treat every once in a while, and now's the perfect occasion."

    scene aegis_cafeteria at bgz
    
    show aiden suit neutral at off
    
    show luna suit neutral at cz

    with diss 

    a "You were outstanding tonight."

    l "I wasn't really. I was just doing my duty."

    a joyous "You were, and I'm saying you are really good at it."

    a neutral "I know the Captain said something like that, but I just thought I'd say it again."

    a "Thanks for showing up and saving my ass."

    l "Ha..."

    l "I wouldn't be much of a wife if I left you in such trouble, would I?"

    a cheeky "It might cause some marital issues, yeah."

    a "But hey, no need to worry about that."

    a "You showed up right on time."

    l blush_01 "More or less..."

    play snd "sounds/cutlery_01.ogg"

    "She blushes, turning her attention back to the cake."

    a neutral "You were definitely a sight for sore eyes."

    l sigh -blush_01 "I'm glad..."

    a "Especially wearing that suit."

    l shocked_upset "W-what?! What do you mean by that?!"

    qa "Heh... It's almost too easy to get a reaction from her."

    l "C-come on Aiden, don't say things like that..."

    a "What? Is a husband not allowed to pay a compliment to his wife?"

    l embarrassed "N-not in public, come on."

    a joyous "Okay, okay..."

    a neutral "I'll save my compliments for when we're in private."

    a "But I don't want any complaints then. You better let me shower you with compliments!"

    l neutral "Okay... If you insist..."

    "Even in private, Luna really isn't the type of girl that wants that sort of attention."

    "Still, I can't resist. She is objectively beautiful, as much as anyone can be in this world."

    qa "I have to indulge myself every once in a while."

    qa "Even if she doesn't like to admit it, she deserves it."

    play snd "sounds/footsteps_two_01.ogg"

    scene aegis_cafeteria
    
    show aiden suit neutral at off
    
    show luna suit neutral at pos4

    show nevin aegis happy at pos6
    
    with dis  

    $ unlock_codex_entry("character_nevin_moresly")

    n "Guys! Really nice work out there!"

    a "Hey Nevin!"

    n "Aiden, so nice to see you back here in one piece... My heart was beating like crazy when you cut off."

    a "It's all good man."

    n embarrassed "And Luna! How could I be so rude?!{nw=0.5}"

    show nevin aegis joyous 
    
    extend " I didn't mean to ignore you! How could I? You really are always a sight to behold!"

    n "The way you took care of Zeph like that!"

    n happy "When you got that knockout blow and called him a disgusting pig, I was like, cheering in the operations room."

    n pout "Everyone kinda stared at me, but I don't really care, I was just so psyched!"

    l "Hello Nevin..."

    show nevin aegis joyous at vertical_shake(5, 0.05, 3)

    n "It was beautiful! You were beautiful!"

    l "Ah... Well..."

    l embarrassed "As I've mentioned before, there's no need for such... colorful compliments."

    n surprised "Ah! I totally apologize!"

    n sigh "You totally did say that! I'm so sorry, my bad!!!"

    n joyous "I just see you in action, being all badass like that and my heart takes over and I totally forget!!!"

    n embarrassed blush_03 "You're so amazing... It blows my mind..."

    l sigh "Right... If you say so..."

    scene aegis_cafeteria 
    
    show black_overlay
    
    with Dissolve(0.8)

    "Seeing this display, it certainly does put Luna's discomfort with compliments into context."
    
    "Particularly when they are coming from an overly enthusiastic source like Nevin. Not that he means anything by it."

    scene aegis_cafeteria at bgz
    
    show aiden suit neutral at off
    
    show luna suit_alt neutral at lz

    show nevin aegis happy at rz
    
    with dis  

    l "Regardless, we appreciate your assistance."

    n happy "My complete pleasure!"

    n -blush_03 "It's always a complete pleasure working with you two! You guys are the best!"

    a "Thanks, man. Appreciate it."

    n sad "Again, I apologize for that close call. I totally wasn't picking up anything on my sensors..."

    n "They got me working on this completely archaic equipment..."

    n "I keep telling them we need upgrades, but they keep saying the budget--"

    a "Dude, it's cool. It's not your fault. They took me completely by surprise too."

    n sigh "Yes... You're right..."

    n happy "I'm just glad nothing too bad happened."

    n sigh sweat "If only we could use some of the tech we confiscate rather than just put it into evidence, things would be a lot easier."

    a "Yeah, you're right. That's the AEGIS life though, isn't it?" 

    show nevin aegis neutral -sweat

    a "Fighting against better equipped enemies, but being so good that it doesn't matter, am I right?"

    l simper "Heh... True."

    n happy "I can't disagree! Especially when we got champions like both of you taking point!"

    show nevin aegis joyous at vertical_shake(5, 0.05, 3)

    n "I mean, how can we lose? We got Silencer on our side!"

    l nervous "It's nothing..."

    l sigh sweat "What's important is that we intercepted and secured that shipment."

    a happy "And what's more, we arrested Zeph as a bonus. Huge win that he's behind bars."

    l neutral -sweat "Indeed."

    l "With any luck, that coward will provide us with something useful during his interrogation."

    n neutral "Heh, when it comes to that, don't worry. The intelligence department is already hard at work on that."

    a neutral "How is that going?"

    n "The usual. We have him dead to rights, but he's still staying quiet and waiting for whoever is going to bail him out."

    show luna sigh

    "Luna rolls her eyes and shakes her head."

    l "Of course."

    l neutral "We shouldn't have expected anything else."

    n look "It will take some time, but you both know how it is."

    n "He has information we want, and we have reduced prison time that he wants."

    n "He's going to flip, it's only a matter of time."

    n "Especially with their civil war in full swing, there's really nothing holding him back from getting the best deal for himself that he can."

    l "Typical..."

    l "Still, it's frustrating..."

    l "If we play his game, he'll be back on the street in no time..."

    a sigh "It is what it is. That's not AEGIS's fault."

    show luna sigh

    "She sighs and nods."

    l "You're right."

    l neutral "One day we'll strike a killing blow to these syndicates and their stranglehold over the government..."

    l "Until then, we do the best we can..."

    a look "Exactly, Lulu..."

    a happy "For the first time in a long while, things are looking our way, aren't they?"

    l "True... They are on their back foot..."

    a "Definitely. Trust me, that day you're dreaming about. It's coming soon."

    l "You're right... I feel it too."

    l simper "We just need to keep at it."

    n joyous "And I'm sure you will!"

    show luna neutral

    n happy "But for now, you guys relax. After tonight, you deserve it."

    a neutral "Trust me, we're already in relaxation mode."

    show luna suit 

    "As if to indicate exactly what I'm talking about, I take Luna's hand and give it a tender squeeze."

    n surprised blush_03 "O-oh! Sorry! I didn't mean to bother you."

    l "It's quite alright."

    show nevin aegis look

    l "Please let us know if there is any progress with Zeph's questioning or the rest of the investigation."

    n "Absolutely! Although, speaking practically, I don't think we'll get much until tomorrow!"

    a "We'll see then."

    n sweat "Y-yes, absolutely! I'll leave you two to it then!"

    n joyous -blush_03 "Enjoy your cake!"

    l nervous "Th-thank you..."

    n joyous "Later!"

    play snd "sounds/footsteps_two_01.ogg" volume 0.7

    scene aegis_cafeteria at bgz
    
    show aiden suit happy at off
    
    show luna suit neutral at cz
    
    with Dissolve(0.9)     

    "Nevin and his ridiculous moustache shuffles off, finally leaving us alone."

    show luna sigh

    "Luna shrugs."

    l "That guy..."

    a "I know, he can be quite a character, huh?"

    l "That's one way of putting it..."

    l nervous "He is quite excitable..."

    a joyous "At least he doesn't talk like that during missions."

    l sigh "No, thankfully not."

    a "He's better than Becca, remember her?"

    l "I do..."

    l neutral "To be truthful, Nevin is one of the more competent operators we've had."

    a neutral "Agreed."

    a "Everyone's got their quirks, I suppose."

    a "Except me, of course."

    show luna sigh sweat

    "She lets out an unexpectedly loud laugh. A guffaw that seems to even take her by surprise."

    l "Ha... Right..."

    show luna neutral -sweat

    a "Anyway, on an unrelated note, I am thinking of going up for more food." 

    l "You're done already?"

    a "What can I say, Nevin talked a while."

    l "Not particularly..."

    a "While I'm up there, you want another slice of mineral cake?"

    l look "Hmmm..."

    "Much to my surprise, she seems to actually consider the somewhat sarcastic offer."

    l embarrassed "No, I really shouldn't."

    a cheeky "Suit yourself."

    play snd "<silence 0.3>"

    queue snd "sounds/chair_01.ogg"

    scene aegis_cafeteria
    
    show aiden suit happy at off
    
    show luna suit neutral at pos5

    with dis

    "I shoot out of my seat, but must have done so too quickly because..."

    $ renpy.music.set_volume(0.1, delay=0.8, channel="music1")
    $ renpy.music.set_pan(-0.9, delay=0.8, channel="music1")
    pause 0.3
    $ renpy.music.set_pan(0.9, delay=0.5, channel="music1")

    show layer master:
        zoom 1.05
        align (0.5, 0.5)
        blur_vision(18)
        ease 1.0 xoffset 10 yoffset 5
        ease 1.0 xoffset -10 yoffset -5
        ease 1.0 xoffset 5 yoffset -8

    with diss

    $ renpy.music.set_pan(0.0, delay=0.7, channel="music1")
    $ renpy.music.set_volume(1.0, delay=1.3, channel="music1")

    scene aegis_cafeteria
    
    show aiden suit happy at off
    
    show luna suit neutral at pos5

    with Dissolve(0.8) 

    a pain "Whoa..."

    l "Aiden?"

    a "Luna... I..."

    a "Damn, that felt weird..."

    l "Is everything okay?"

    a sigh "Yeah, I just got a bit light-headed..."

    l "Hmmm..."

    play snd "sounds/fork_02.ogg"

    "She looks at me with suspicion before putting her fork down."

    l "You take a seat, I'll get your plate."

    a look "What? No, I'm fine."

    l "Please, it's no effort, really."

    l "Besides, I need some more water to finish off this cake. I'll get some for you while I'm up."

    a "Okay, thanks."

    play snd "<silence 0.3>"

    queue snd "sounds/chair_02.ogg"

    scene aegis_cafeteria at bgz

    show letterbox

    with Dissolve(0.9)

    "I sit back down, knowing better than to argue with Luna when she gets that defiant look in her eye."

    "When she's like that, she's unstoppable."

    "Better men than me have tried."

    "Well, more determined men, at least..."

    stop music1 fadeout 1.0

    scene black with pixellate

    pause 1.0

    play music "music/climate_report.ogg" fadein 1.0

    scene aegis_bedroom with pixellate

    "After polishing off another plate of food, the two of us head back to our room."

    "While AEGIS doesn't provide the most elaborate accommodation, it's a comfy spot to call our own."

    $ unlock_codex_entry("lore_the_source")

    "Its got a nice view of the source in the morning, which is always something nice to wake up to."

    scene aegis_bedroom

    show aiden suit neutral at off

    show luna suit neutral at pos5

    with dis

    a "Home sweet home..."

    l "Yeah..."

    l "That was quite an exhausting day..."

    a "Yeah, kinda long, I agree..."

    a "Still, that's its own reward, in a way."

    l "It's true... It does feel nice to come home after a hard day, knowing that we actually made a difference."

    a "Exactly."

    a "Days like today are why I joined AEGIS."

    a serious "Knowing that maybe I prevented..."

    a sigh "Well, you know."

    play snd "<silence 0.3>"

    queue snd "sounds/hug_01.ogg"

    scene aegis_bedroom at bgz(z=1.6, x=0.5, y=0.0)

    show aiden suit neutral at off

    show luna suit neutral at cz

    with Dissolve(0.8)

    "She nods softly and hugs me."

    "She knows what I mean better than anyone."

    "After all, she lost her parents to the syndicates even younger than I did."

    "She doesn't even remember them..."

    "At least I knew mine before they were... taken away..."

    l "One day, we'll avenge them."

    a "We will..."

    a "But in the meantime, we live..."

    play snd "<silence 0.3>"

    queue snd "sounds/suit_deflate_01.ogg"

    play snd1 "<silence 1.0>"

    queue snd1 "sounds/suit_removing_01.ogg"

    queue snd1 "sounds/laundry_01.ogg"

    scene aegis_bedroom

    show aiden underwear neutral at off

    with dis

    "Casually stripping off my tactical suit, I place it in the laundry bin."

    stop snd1 fadeout 0.5

    stop snd fadeout 0.5

    a "Oh, that feels nice..."

    "I say, stretching my arms into the air."

    play snd "<silence 0.3>"

    queue snd "sounds/suit_deflate_02.ogg" volume 0.7
    
    queue snd "sounds/suit_removing_02.ogg"

    "Luna chuckles and then takes off her uniform as well."

    scene aegis_bedroom at bgz(z=1.6, x=0.5, y=0.0)

    show aiden underwear joyous at off

    show luna underwear neutral at cz

    with Dissolve(0.8)

    "As she does, I can't take my eyes off her..."

    "The sight of my wife undressing isn't exactly unfamiliar to me, but still..."

    "As they say, one can see the great mountains of Nuria every day, but their spectacle never tires."

    "The earrings, which I got her as a wedding gift, glimmer in the dimming simulated sunset of the source."

    "I'm glad she likes them as much as she does, wearing them every day."

    "As agents, we are forbidden from wearing rings. It would give too much away if we were captured, they say."

    "This is more than an acceptable substitute though."

    l "What are you looking at?"

    a "The most beautiful girl I've ever seen."

    show luna sigh

    "She rolls her eyes."

    l "Aiden..."

    a surprised "Hey! I promised that I wouldn't hold back when we were alone, didn't I?"

    play snd "sounds/laundry_01.ogg"

    scene aegis_bedroom

    show aiden underwear sad at off

    show luna underwear neutral at pos5

    with Dissolve(0.8)

    "Shaking her head, she turns away, suddenly seeming quite interested in folding her infiltration outfit before putting it in the laundry hamper."

    l "You did, but come on."

    l "Don't be a pervert..."

    a "Alright, alright..."

    a "I'll hold back all those perverted thoughts I'm having about my wife."

    a sigh "It's inappropriate to be having those."

    l "Oh, give me a break, there's no need to tease me..."

    a happy "You're right, it's fun though..."

    show luna simper

    "She smirks."

    l "I see..."

    l "Well... Turnabout is fair play, I suppose..."

    a neutral "I think so."

    scene aegis_bedroom:

        zoom 1.8
        align (1.0, 0.5)
        
    with dis    

    "Still smiling and feeling pretty pleased with myself, I turn my attention to a potted plant near the window."

    show aiden underwear happy at off

    a "Heh... This little guy is coming along nicely. Looks like he's about to bloom."

    a "With any luck, we might even get a few peppers."

    play snd "sounds/watering_can_01.ogg"

    "I pick up the small watering can I leave on the floor, feel the soil to see how moist it is, and then carefully sprinkle a small amount of water into the pot."

    stop snd fadeout 1.0

    scene aegis_bedroom

    show aiden underwear surprised at off

    show luna underwear simper at pos5

    with Dissolve(0.8)    

    "Once I'm satisfied, I put the can down and turn around, only to see Luna staring at me."

    a "W-what is it?"

    l "Nothing important."

    l "You look cute doing that stuff."

    a look "I do?"

    l "Mhmmm..."

    a neutral "I see..."

    play snd "<silence 0.3>"

    queue snd "sounds/body_01.ogg"

    scene aegis_bedroom at bgz(z=1.6, x=0.5, y=0.0)

    show aiden underwear neutral at off

    show luna underwear simper at cz

    with Dissolve(0.8)  

    "Making my way across the room, I take her into my arms."

    a "Then you know how I feel when I look at you."

    l "Is that so?"

    a "I reckon."

    l "I see..."

    "She hugs me tight."

    "Despite the long, action-filled day, she still has a sweet smell to her."

    "Her scent."

    "It's a beautiful, enchanting aroma that I can't get enough of."

    l "You know I love you, right?"

    a "Most definitely. I love you too."

label s03:

    stop music fadeout 3.0

    play snd "<silence 0.4>"

    queue snd "sounds/kiss_01.ogg" volume 0.9

    scene aegis_bedroom

    show cg00_01 at cgz

    with dis

    play music "music/just_us.ogg" fadein 5.0

    "Leaning forward, I pull her into a kiss." 

    "She doesn't resist. In fact, she kisses back."

    "The kiss lasts longer than usual as our lips softly press against each other."

    scene aegis_bedroom at bgz(z=1.6, x=0.5, y=0.0)

    show aiden underwear neutral at off

    show luna underwear simper at cz

    with Dissolve(0.8)

    "By the time it finally comes to an end, I feel desperate for more."

    "I don't know what it is today... Maybe it's the mental image of her rescuing me the way she did..."

    "I just need her so badly..."

    "So badly that just from looking at me, she knows."

    l "Aiden..."

    a "Please, Luna, I need to show you--"

    "She presses her finger against my lips."

    l "Shhh..."

    l "It's okay..."

    l "I want you too..."

    "Hearing that drives me even crazier."

    "How the heck did I ever get so lucky to have a girl like her?"

    "The truth is that it felt inevitable ever since I met her for the first time..."

    "The fact that we would be each other's first... The fact that we would marry each other..."

    "It all seemed like destiny."

    "It still does."

    scene aegis_bedroom at bgz(z=1.5, x=0.5, y=1.0)

    show aiden underwear neutral at czb

    with Dissolve(0.8)

    pause 0.15

    play snd "sounds/undressing_21.ogg"

    show aiden hard neutral at czb

    with Dissolve(0.8)
    
    "Desperate to make her feel exactly how, I practically rip off my underwear, revealing a dick so hard that it almost hurts."

    show luna underwear simper at off

    l "Oh wow..."

    l "You're..."

    "She stares at it, strangely fascinated."

    a "Excited?"

    l horny "Maybe a little..."

    "There is something almost devilish about her smile."

    "She really really is getting hot and bothered."

    scene aegis_bedroom at bgz(z=1.6, x=0.5, y=0.0)

    show aiden hard neutral at off

    show luna underwear simper at cz

    with Dissolve(0.8)

    "Itching to progress things, I start to tug at Luna's underwear."

    l "Heh... In a hurry?"

    a "Not going to lie. Yes."

    a nervous "If I keep waiting I'm going to explode."
   
    l "Alright then. I give you permission."

    "She whispers."

    play snd "sounds/undressing_panties_02.ogg"

    scene aegis_bedroom

    show aiden hard neutral at off

    show luna sport_bra simper at pos5

    with Dissolve(0.8)

    "Happy to oblige, I pull her underwear down, revealing the treasure underneath."

    l "You're staring."

    a "But it's so cute."

    "She's right though. Now's not the time to stare."

    "I don't have the patience to do so for long anyway."

    play snd "sounds/bed_17.ogg"

    scene aegis_bedroom at bgz with dis

    "Taking charge, I gently push Luna onto our bed. She goes down without a fight."

    "Staring back up at me, she smiles."

    show aiden hard neutral at off

    show luna sport_bra simper at off

    l "What are you waiting for, soldier?"

    a surprised "N-nothing!"

    l "Then get to it."

    a seductive "Y-yes ma'am!"

    play snd "sounds/bed_creaking_noise_01.ogg"

    play sex "<silence 0.3>"

    queue sex "sex/insertion_weak_13.ogg"

    $ update_status("emotional_status", _("AROUSED, AT EASE"), notify=False)

    $ set_xray_image("02")

    scene cg03_01 at cgz with dis

    "Excited as all hell, I get on top of her, grab her thighs and stick my dick inside."

    "Seeming somewhat amused, Luna pulls a pillow behind her head to help keep her steady."

    l "You're so cute when you're excited."

    a "Don't you mean to say \"I'm so handsome?\""

    l "Heh... No..."

    l "Don't worry though, cute is good in this situation."

    l "Besides, you are a handsome man as well. You can be both."

    a "I knew it. I saw that look in your eye and I knew you were thinking \"look at that hot piece of ass over there watering his plant.\""

    a "\"I'd love to have him tend to my flower.\""

    show cg03_02 at cgz with tdis

    l "Aiden..."

    a "Yes, Lulu?"

    l "Please be quiet and fuck me before I cringe to death."

    a "Haha... Okay, if you insist."

    play sexl "sex/frottage_04.ogg"

    scene cg03a_01                                                              #2
    
    with dis

    "Knowing that I've pushed my luck teasing her as much as I possibly can, I begin thrusting."

    a "Ohhhh..."

    l "Mmmmm..."

    qa "A-amazing..."

    "The way her folds feel as I slide in and out of her..."

    "So warm and inviting..."

    "And being able to hold on to these thick, powerful thighs while I'm at it..."

    qa "Can it get any better?"

    "Probably..."

    "I'd love it if she took that bra off and I could see those spectacular tits of hers bouncing around."

    "I don't force her though."

    "Not only because I couldn't even if I wanted to try, but also because I know doing so is annoying to her."

    "To me, those tits are an amazing work of art, but to her, they're just a nuisance she'd probably be happier without."

    "As she told me one time \"they just get in the way of me doing my job.\""

    "It sucks, to be honest." 
    
    "It would be better if she loved her body completely, but that's not always how life is, I suppose."
    
    "That's okay though, I love her body more than enough for the two of us."

    "In fact, thinking about how much I love that body..."

    stop sexl fadeout 1.0

    play sexl1 "sex/sex_01_faster.ogg"

    show cg03a_02                                                               #1
    
    with dis

    "I want to please it even more than ever!"

    "With that in mind, I increase my pace dramatically, putting my all into it."

    l "Oh..."

    l "Putting in quite an effort today, are you?"

    a "I see you and I can't resist!"

    a "I want to make you feel so good!"

    l "Hehe... Well, it does feel pretty good..."

    "Hearing that is all the reward I need, but that doesn't stop me."

    "If anything, it makes me increase my efforts."

    "I do have a growing headache, perhaps because of the strain, but I ignore it."

    "I'll have time to rest later."

    "Now's about showing my woman how I feel about her."

    l "That being said... I don't need this... Being close to you is all I really want."

    "Hearing that... I can't help but smile."

    "To tell the truth, I feel the same way."

    "The sex is nice... but to be honest, I'm looking forward to the cuddling afterwards even more..."

    l "I love you..."

    a "I love you too!"

    qa "Nnnngh! Fuck, that did it!" 
    
    qa "I can't keep this up much longer!"
    
    qa "Why am I feeling so lightheaded?"

    qa "Whatever, I just--"

    play sex "sex/cum_single_48.ogg"

    with hpunch

    $ set_xray_image("03")

    a "NNNNGH!!!"

    "Unable to hold myself together any longer, I cum inside her, hoping that I've done enough."

    stop sexl1 fadeout 1.0

    $ increase_stat("aiden_sex", 1)

    $ increase_stat("aiden_kisses", 1)

    scene cg03_02 at cgz with diss                                              #3

    "After composing myself once more, I look down to see Luna smiling contentedly."

    qa "She's so beautiful..."

    qa "But not just that..."

    qa "She's always been so kind..."

    qa "And soft..."

    qa "And..."

    a "Oh..."

    l "Yes, it was nice."

    stop music fadeout 2.0

    play sndl "sounds/heartbeat_100bpm_01.ogg"

    if persistent.flash_enabled:

        with flash(color="#d21717", max_alpha=0.9, fade_in=0.1, hold=0.2, fade_out=0.4)

    show layer master:
        zoom 1.02
        align (0.5, 0.5)
        blur_vision(20)
        ease 1.0 xoffset 10 yoffset 5
        ease 1.0 xoffset -10 yoffset -5
        ease 1.0 xoffset 5 yoffset -8
        repeat

    with diss

    qa "What is that feeling?!"

    qa "I feel nauseous and... oh fuck!!!"

    qa "This hurts like hell!"

    qa "What the hell is going on?!"

    qa "What the--?!"

    a "L-Luna..."

    $ set_status_experience_image("Vagina", "luna_vagina_01", show_notification=False)

    $ persistent.unlocks.add("s03")

    $ renpy.end_replay()

    stop sndl

    play snd "sounds/fall_03.ogg"

    scene black with Dissolve(0.1)

    pause 1.5

    if perspective_mode == "solo":

        jump aiden_02

    show lpc

    show pov_change_letterbox

    show luna sport_bra neutral behind pov_change_letterbox at pov_change:
        matrixcolor TintMatrix("#000000") * SaturationMatrix(0.0)

    pause 0.8

    hide luna sport_bra neutral

    show luna sport_bra neutral behind pov_change_letterbox at pov_change 
    
    with diss

    pause 1.0

    play music "music/just_us.ogg" fadein 5.0

    scene cg03_02 at cgz with diss                                

    ql "He really is so cute when he's like this..."

    ql "I know he hates it when I say stuff like that, but it's the truth."

    a "L-Luna..."

    play snd "sounds/fall_03.ogg"

    scene aegis_bedroom with dis

    ql "Hehehe... Look at him."

    ql "He's so exhausted that he needs to have a little rest on me."

    show aiden hard pain at off

    show luna sport_bra neutral at off

    a "Agh!!!"

    a "Luna, p-please!"

    ql "What the heck? Something seems wrong."

    l "Aiden? What is it?"

    a "H-help Me!"

    l "Help you? What's happening?"

    stop music fadeout 2.0

    ql "What the hell? He seems in agony."

    l shocked "Are you okay? What's going on?"

    l "...Aiden? Aiden!?"

    $ update_status("emotional_status", _("ANXIOUS, SCARED"), notify=False)

    ql "He's fainted!"

    play snd "sounds/body_02.ogg"

    play music "music/outbreak_of_the_meme.ogg" fadein 3.0

    $ set_xray_image("04")

    "Carefully but urgently pushing him off of me, it's clear from his lack of response that he must be completely unconscious."

    "I check his pulse."

    "It's there... but it's weak..."

    $ update_status("aiden_feelings", _("No! Something's wrong! If something happens to him... I can't imagine what I'd do... I need to do everything I can to help him!"))

    ql "Shit."

    ql "Something really is wrong."

    ql "I could call the medics, but who knows how long they'll take."

    ql "I can't risk it. I need to take matters into my own hands. I don't have a moment to spare!"

    ql "He's Aiden... My only..."

    "I attempt to pick him up, but his whole body suddenly spasms, preventing me from doing so."

    play snd "sounds/body_catch_01.ogg"

    scene aegis_bedroom at bgz

    with dis

    ql "Seeing him struggling like this... No..."
 
    "More determined than ever to help him, I finally get a good hold on him and head right to the door."

    scene black with dis

    play snd "sounds/footsteps_barefoot_run_02.ogg"

    $ set_xray_image("01")

    scene aegis_hallway at movement with dis

    "Speeding off towards the med-bay as fast as I can safely carry him, I realize I'm catching the attention of a lot of agents walking through the halls."

    "It's only then that I realize I'm not wearing any panties."

    "Most respond to the unusual sight with absolute shock, a few smile, one even whistles."

    ql "Ugh... Typical..."

    ql "How could someone care about that at a time like this?"

    play snd "sounds/footsteps_barefoot_run_02.ogg"

    ql "That's not what's important right now, idiots!"

    play snd "<silence 0.3>"

    queue snd "sounds/door_slam_06.ogg"

    scene aegis_medical_bay with hshake((0, 0, 0, 0), 0.2, dist=20)

    "I rush into the medical bay so quickly and with such urgency that the doctor on duty almost drops the clipboard he's carrying out of shock."

    doctor "What the--!?"

    show luna serious sport_bra at off 

    l "Doctor, hurry."

    doctor "What happened?"

    l "We were in bed together and he collapsed."

    doctor "Were you doing anything strenuous?"

    l "He was."

    doctor "I see..."

    "The doctor seems to almost smile before thinking better of it."

    "Good move, I'd hate to have to skin him alive as retribution."

    doctor "Put him on this bed here, please. Then, if you want, you can get dressed. I can take care of it from here."

    l "I'm not leaving until I know he'll be alright."

    play snd "sounds/bed_18.ogg"
    
    show luna sport_bra serious at pos5
    
    with dis

    "I say, placing him on the bed. The doctor nods."

    doctor "Understood."

    play snd "<silence 0.3>"

    queue snd "sounds/medical_beep.ogg"

    "Using his stethoscope, he quickly listens to Aiden's heart before connecting him to a diagnostic tool."

    doctor "Okay, let's see..."

    l "How is he? What happened?"

    doctor "I don't know, but..."

    doctor "Hell above..."

    doctor "He's in rough shape..."

    l "Will he survive?"

    doctor "I... It's too early to tell..."

    doctor "Not this second, it seems."

    ql "Thank goodness..."

    ql "There's hope..."

    doctor "Give us some time, we'll figure out what's wrong..."

    l "Of course. Thank you, doctor."

    doctor "My pleasure, Agent Virelith..."

    doctor "Now, while we're waiting for the diagnostic, would you like me to give you a gown?"

    l sigh "Yes, thank you..."

    scene black with circuit_in

    scene aegis_medical_bay at bgz
    
    show luna suit neutral at lz
    
    show nevin aegis sad at rz
    
    with circuit_out
    
    n "Any change?"

    l "None so far. Still unconscious."

    n "Damn..."

    l "Thank you for dropping off the change of clothes before."

    n "N-no problem..."

    n sigh "It felt weird going into your quarters without you guys there... I didn't want to invade your privacy."

    l "That's an interesting thing to say as an intelligence officer."

    n sad "Funny..."

    n "I guess it feels different when it's the bad guys."

    l serious "Yes..."

    l "The bad guys... Nox..."

    n "In this case, yes."

    l "What did those animals do to him?"

    doctor "It seems like it might have been some kind of poison."

    l "Poison?"

    show nevin surprised

    "Nevin's eyes grow wide."

    ql "He must be thinking the same thing I am."

    n "Weren't they about to inject him with something when you rescued him?"

    l "Yes, but he told me that they didn't manage to."

    n sad "Weird... Maybe he got some trace amounts."

    doctor "Perhaps, but that seems unlikely to me."

    doctor "He mentioned the possible injection when we gave him his post-mission physical, so we took a blood sample and inspected the fluid."

    doctor "There was no trace of the poison at that stage and the fluid seemed inert."

    n "Strange..."

    doctor "Are you sure he didn't consume anything from outside the compound in the meantime?"

    l "No, we only ate from the mess hall."

    n look "He even ate the same thing as me."

    doctor "Then, I doubt it's that..."

    doctor "I'll take a look at his blood work again and take another sample. Perhaps there's something we missed."

    doctor "I don't suppose we have a sample of this fluid he was almost injected with, do we? I obviously need to test that again."

    n serious "We certainly do. I'll be right back with that."

    doctor "Thank you."

    n "I'll just be a sec."

    play snd "<silence 0.3>"

    queue snd "sounds/body_01.ogg"

    "Nevin pauses for a moment and then touches my shoulder."

    n "We'll do what we can, Luna."

    l "Thanks Nevin..."

    l "I just... It's so annoying only being able to sit here and do nothing..."

    n "You're not doing nothing, you're supporting him..."

    l "By standing here? I don't think so..."

    n "He'll be happy to see you when he wakes up."

    l "Not as happy as I will be to see him wake up."

    n "I understand what you mean..."

    n "I'll be back soon."

    play snd "sounds/footsteps_two_sneakers_05.ogg"

    scene aegis_medical_bay

    show letterbox

    with diss

    "After touching my shoulder once more, Nevin departs."

    "The room once again goes quiet, a silence only punctuated by the beeping of medical equipment."

    "All the while, Aiden lies there, motionless."

    "It's so hard to look at him, not knowing why this is happening."

    ql "It's scary..."

    "But I'm relieved I'm not facing this situation alone. Everyone is trying to help him."

    scene aegis_medical_bay at bgz
    
    show luna suit neutral at cz
    
    with diss

    l "Thank you very much, doctor. For all of this..."

    doctor "Aiden has always been one of our most loyal and dedicated agents... I'll do everything I can..."

    l "Thank you..."

    "He jots down a few notes before beginning to back away."

    doctor "Now, if you'll excuse me, I will get started on that analysis right away."

    l "Of course."

    l "I'll stay here if you don't mind."

    doctor "Not at all."

    play snd "sounds/sitting_01.ogg"

    scene aegis_medical_bay at hs

    show letterbox

    with diss

    "He leaves and I take my seat once more."
    
    "Staring at Aiden connected to all sorts of tubes, I can't help but fidget with anger."

    ql "Those bastards. First they take away his family, and now this?"

    ql "I'll never forgive them..."

    l "Fucking Nox..."

    l "They'll pay for what they did..."

    l "THEY'LL PAY!!!"

    play snd "sounds/table_slam_01.ogg"

    scene aegis_medical_bay

    with vpunch

    "Letting my anger get the best of me, I slam the table next to me, denting it and causing a sharp pain in my hand."

    "The anger quickly comes back under my control and is replaced with a deep regret when I realize I've done nothing but injure myself."

    ql "That's stupid and unproductive..."

    ql "I let my temper get the better of me."

    ql "I should save the rest of my rage for those that are responsible."

    ql "Nothing's going to get between me and taking down the Nox Syndicate."

    ql "I'll do anything... Anything it takes..."

    stop music fadeout 2.5

    scene black with Dissolve(1.0)

    pause 0.5

    show apc

    show pov_change_letterbox

    show aiden naked look behind pov_change_letterbox at pov_change:
        matrixcolor TintMatrix("#000000") * SaturationMatrix(0.0)

    pause 0.8

    hide aiden naked look

    show aiden naked look behind pov_change_letterbox at pov_change 
    
    with diss

    pause 1.0

label aiden_02:

    if perspective_mode == "solo":

        $ update_status("aiden_feelings", _("No! Something's wrong! If something happens to him... I can't imagine what I'd do... I need to do everything I can to help him!"))

    $ set_xray_image("01")

    play music "music/base_launched_5_minutes_ago.ogg" fadein 5.0    

    scene black with Dissolve(1.0)

    $ update_status("emotional_status", _("RELIEVED, CONCERNED"), notify=False)

    l "Aiden?"

    play snd "sounds/medical_machine_01.ogg" volume 0.8

    l "Are you awake?"

    qa "It's Luna..."

    qa "I can hear her..."

    play snd "sounds/medical_machine_02.ogg" volume 0.8

    qa "What are all these weird other noises..."

    qa "Are they machines? What's going on?"

    scene aegis_medical_bay_xray at bgz 
    
    show aiden underwear look at off
    
    show luna suit neutral at cz 
    
    with eye_open

    a "Where am I?"

    l "You're in the med-bay."

    l "You collapsed..."

    a "I did, didn't I?"

    l sigh "Yes. You're safe now though..."

    "She exhales with relief, the hint of a warm smile appearing on the edge of her lips."

    show luna neutral

    "She might not be the most expressive partner, but small hints like that cracking through her generally serious exterior are everything I need to make my chest feel tight."

    a "What happened to me?"

    l "You were poisoned."

    a surprised "I was?"

    l "When we were at the warehouse last night, they tried to inject you with something, right?"

    a serious "He tried, but he didn't succeed."
    
    a look "He only pricked me for like a second before you got the drop on him."

    show luna sigh

    "She winces, as though in terrible pain."

    l upset "Damn it..."

    l "I was too late..."

    a "What are you talking about?"

    a neutral "You saved my life..."

    a "I'd have been finished..."

    play snd "sounds/latex_01.ogg"

    "She clenches her fist, clearly trying to hold back a deep anger."

    l "DAMN IT!" with vpunch

    "She's not entirely successful."

    a "It's okay, Luna..."

    "I whisper softly, trying to calm her down."

    a "No one can change the past. No need to dwell on it."

    a "Let's concentrate on now."

    show luna sigh

    "She nods."

    l serious "That's part of what's so upsetting..."

    a surprised "What do you mean?"

    "She stammers for a second with uncharacteristic indecisiveness before gesturing to a doctor standing on the other side of my bed."

    l sigh "Perhaps it would be better if he explained."

    show luna serious

    doctor "Maybe so." 
    
    "The doctor approaches me and examines me a bit before proceeding."

    doctor "First of all, how are you feeling, Agent Furin?"

    a look "Fine doc, thanks..."

    doctor "That's good. Any muscle weakness or aching?"

    a "Uhhh... Nothing major, maybe a little?"

    doctor "Good to hear. At least our treatments have been somewhat effective."

    a "Somewhat?"

    doctor "Yes, I wish I had better news..."

    a "News?"

    doctor "Agent Furin, we believe that you've been exposed to some kind of synthetic poison. One of unknown origin."

    a serious "Didn't Nox develop it?"

    doctor "Perhaps. They have developed poisons and other chemical weapons in the past, but this one is unlike any we've ever encountered."

    doctor "It seems you've been infected with a small number of highly toxic synthetic organisms."

    a "What do you mean?"

    doctor "I'm saying that whatever was in that vial was created to sneak into your bloodstream, remain inert and undetectable for a time." 
    
    doctor "But then, once activated, they convert healthy blood cells into a highly poisonous material."

    doctor "One that seems to lead to a particularly painful death."

    a pout "That explains why it felt like my heart was going to explode..."

    a "So you managed to fix the problem?"

    "His expression sours."

    doctor "Not as well as I would have liked..."

    a look "Oh... That doesn't sound good..."

    doctor "It isn't..."

    doctor "Although we were able to neutralize the toxins created by the synthetics, we are unable to remove them entirely."

    a "What does that mean?"

    doctor "It means that the poisoning is very likely to occur again."

    a "Oh..."

    a "What will happen then?"

    doctor "We have prepared an anti-venom which can be taken orally in order to continue neutralizing the poison. Nonetheless, it will be quite painful."

    a "I can't say I'm looking forward to that..."

    doctor "I can't imagine you are."

    a "Is there any way to permanently cure this?"

    doctor "That's what we're attempting to find out now."

    show luna serious
    
    doctor "Speaking honestly, I hope there is... because if not..."

    a sad "If not what?"

    doctor "Truth be told, I don't know how bad it will be."

    doctor "I suspect that the treatment's effectiveness isn't guaranteed..."

    a serious "You're acting like this is going to be terminal... Is that the case?"

    doctor "The truth is, I don't know..."

    doctor "But I doubt your body could take this punishment forever... and a permanent cure is frankly beyond my abilities..."

    a look "Well, that doesn't really matter if I can just deal with it as it comes."
    
    a "I feel fine for now, at least."

    doctor "That is very good to hear!"

    doctor "That buys us time!"

    l "What about Nox? Do they have some cure for this?"

    "The doctor shrugs."

    doctor "Considering our previous experience with them, it wouldn't surprise me if someone in the Nox Syndicate had an effective treatment." 

    doctor "I really hope they do, because..." 
    
    "The doctor trails off."

    a "Because what?"

    doctor "I was just thinking about what could happen if they used this more broadly..."

    a "What do you mean?"

    doctor "Well, think about it."

    doctor "A tiny amount of it got in your bloodstream and did this."

    doctor "They could put it in the water supply and hold the whole population hostage."

    a "Oh shit..."

    l "That's..."

    doctor "Monstrous?"

    l "Beyond unforgivable..."

    doctor "I hate to say it, but according to the reports, we found no documentation regarding that poison when securing the warehouse, so I'm not sure where we might find such a thing."

    l "I don't know either..."

    l "But I know who might..."

    stop music fadeout 2.0

    scene black with pixellate

    play music1 "music/end.ogg" fadein 3.0

    scene edric_quarters at bgz

    show letterbox
    
    show aiden suit look at off
    
    show luna suit_alt serious at lz

    show edric base serious at rz
    
    with pixellate

    $ update_status("aiden_feelings", _("It can't be... For this to happen to him, just like that because I was too late... Not him... It's impossible. I won't allow it. I {i}will{/i} do something."))

    e "He still hasn't said a word."

    l "Are you serious?"

    e "Unfortunately so."

    e "Try as we might to put pressure on him, all he does is smile and ask to be freed."

    l "Then do it. If that's what it takes, do it."

    e "Absolutely not."

    play snd "sounds/footsteps_single_heels_09.ogg"

    show luna suit_alt serious at vertical_shake(25, 0.1, 1)

    l "But Captain!?" 

    e "I'm sorry, but my decision is final."

    l "But this is his life we're talking about..."

    e "I know."

    e "But do you have any idea how much carnage Zeph has caused over the years?" 
    
    l "I know all too well... You know that."

    e "My apologies..."

    e "But, if anything, that strife you know he's caused can't be risked again for the sake of one single agent."

    l "An agent who has given you everything!" with vshake((0, 0, 0, 0), 0.2, dist=20)

    l "Aiden has devoted his life to AEGIS!"

    "Captain Edric sighs."

    e "I know..." 
    
    e "You think I don't realize that? That makes all of this so much harder..."

    e "Think about what you're asking me to do."

    l "Then we keep up our assault on Nox territory until we find something that can help him!"

    e "Agent Virelith! The only Nox-controlled buildings we are aware of are completely above-board!"

    e "So we'd need legal grounds to enter... and you know more than anyone how we've tried to make something stick to them."

    l "We can take it by force."

    e surprised "Sending a strike team to assault a legal Nox stronghold?!"

    e "Not only is that outside of our legal capability, it's outside of our military capability."

    e "They would certainly fight back, and we barely have enough active men to take one of their outposts, let alone a fully manned fortress."

    e serious "And even if we did have the men, what location would we even strike?"

    e "The information we need could be in any number of locations..."

    e  "I'm sorry, Agent Virelith... Agent Furin... I wish there was more I could do..."

    e "If you have a valid target to strike, I'd be happy to do so, but until then..."

    e "Well, I'm afraid there's little I can directly do about this."

    "The fact that he's reacting this way is a bitter pill to swallow..."

    "But what am I to do? I can't force him to do anything..."

    "At the end of the day... He's right..."

    a "It's okay. Sometimes bad things happen in the line of duty."

    "He shakes his head."

    e "I'd rather that not be the case, but it is."

    e "Regardless, we'll do our best to accommodate your current situation."

    e "If you aren't capable of full active-duty, perhaps you can serve as part of our support staff."

    a "I feel fine, I swear. Don't bench me because of this. You know we need all the help we can get right now."

    e "Perhaps..."

    e "I will look at what our doctors recommend."

    qa "It's not exactly what I wanted to hear, but it's better than nothing, I suppose."

    a "Appreciated, sir."

    e "If they give you the all-clear, you'll be deployed again immediately. I promise."

    a neutral "I'll hold you to that."

    e "As I would always expect from you..."

    e "For now though, please take some time to rest."

    e "And Agent Virelith...  You will be given additional time off to help your husband deal with these matters."

    l sigh "Thank you, sir."

    e "Please... It's what you deserve... After everything both of you have done for us..."

    e "Those years of service..."

    e "It's only right..."

    stop music1 fadeout 2.0

    if perspective_mode == "solo":

        scene black with Dissolve(1.5)

        pause 1.0

        jump aiden_02extra

    scene black with Dissolve(1.0)

    pause 1.5    

    show lpc

    show pov_change_letterbox

    show luna mask behind pov_change_letterbox at pov_change:
        matrixcolor TintMatrix("#000000") * SaturationMatrix(0.0)

    pause 0.8

    hide luna mask

    show luna mask behind pov_change_letterbox at pov_change 
    
    with diss

    pause 1.0

    play music "music/flash_shadow.ogg" fadein 2.0

    scene nox_warehouse_inside_01

    show luna mask_gun at pos5

    with dis

    $ update_status("emotional_status", _("FOCUSED"), notify=False)

    "As kind as Captain Edric's offer may be, I can't just bring myself to take too much time off."
    
    "Aiden certainly feels similar."

    "After a few days of nursing him back to health, he practically begged me to get back to work."

    "As much as he'd love me around taking care of him, he knows there are bigger concerns in the world."

    "Just because he isn't feeling well, it doesn't mean Nox is taking a day off."

    "And if they aren't taking a day off, neither am I."

    play snd "sounds/radio_receiver_01.ogg"

    n "Silencer, my scanners are picking up two around the corner."

    l "Are they jammed?"

    n "Almost... I think that should only be a few more seconds..."

    n "Got it, go."

    "Having given the all clear, I listen for my opening."

    play snd "sounds/movement_swift_01.ogg"

    queue snd "<silence 0.3>"

    queue snd "sounds/body_fall_05.ogg"

    scene nox_warehouse_inside_01 at bgz

    show luna mask at cz

    with dis

    "Once the footsteps begin to get more silent, I slip around the corner and silently take them both out."

    l "Done."

    n "There's a group of four to watch out for three doors down. The target should be at the end of the hallway."

    l "I copy."

    scene nox_warehouse_inside_01

    show letterbox

    with dis

    "Sneaking down the hallway, I pay particular attention to not make any noise outside the door Nevin pointed out."

    "My efforts go off without a hitch and I make it to the end of the hall."

    scene nox_warehouse_inside_01 at bgz

    show luna mask at cz

    with dis

    l "I've arrived."

    n "Good, there should be a tablet with the data we're looking for right around this corner."

    l "Any people?"

    n "None on the scan, but it's very fuzzy. I'm trying to jam the area just in case, but be cautious."

    l "Will do."

    $ renpy.music.set_volume(0.5, delay=0.8, channel="music")

    "Before turning the corner, I stay silent and listen."

    "There's some definite movement nearby."

    ql "It sounds like someone is pacing about..."

    ql "Someone that is, hopefully, unarmed."

    "Although I hope, there's no way to know."

    "There's always that risk."

    "But it's a risk worth taking."

    "If it means a better world at the end of the day, it's always worth it."

    "There's a cost to everything in life... one only needs to have the courage to pay it."

    ql "Here goes nothing..."

    $ renpy.music.set_volume(1.0, delay=0.8, channel="music")

    "Slowly and silently, I peek around the corner to see a large man pacing around."

    "He seems to be on his comm."

    noxunderboss "Sure, almost done... The shipment will be ready to go tomorrow."

    noxunderboss "They're refining it as we speak."

    noxunderboss "Don't worry about the quality, it will be more than enough to meet your flamed out customers. And if they aren't flamed out, they will be soon."

    ql "Asshole..."

    ql "Talking about citizens like that..."

    noxunderboss "Who's there?!"

    ql "Damn it... He must have heard me..."

    noxunderboss "Show yourself!!!"

    ql "That's not on the agenda."

    play snd "sounds/metal_ball_rolling_01.ogg"

    "Reaching into my tool belt, I pull out a small, metal pill-like object and toss it around the corner."

    stop snd

    play snd1 "sounds/explosion_02.ogg"

    play snd2 "sounds/smoke_grenade_01.ogg"

    pause 0.2

    show smoke_01 
    
    with Dissolve(1.4)

    "Despite its small size, it begins rapidly emitting vast amounts of smoke."

    play snd "sounds/footsteps_single_heels_09.ogg" volume 0.5

    queue snd "sounds/footsteps_single_heels_08.ogg" volume 0.5

    "Once the hallway is filled, I jump around the corner."

    "My mask filtering out the gas, I am completely unimpeded as I rush over to the man and tackle him onto the ground."

    play snd "sounds/body_fall_04.ogg"

    noxunderboss "UGH!!!"

    "He grunts in pain as he slams into the floor."

    l "Where's the tablet!!!" with vpunch

    "I scream into his ear."

    noxunderboss "Tablet?"

    l "With the shipping route!!!"

    noxunderboss "What?! In there!!!"

    l "Thank you."

    play snd "sounds/punch_08.ogg"

    pause 0.18

    with vpunch

    "Then, with a single punch, he's knocked out cold."

    play snd1 "sounds/footsteps_single_heels_01.ogg" volume 0.5

    play snd2 "<silence 0.5>"

    queue snd2 "sounds/footsteps_single_heels_03.ogg" volume 0.5

    scene nox_warehouse_inside_01

    show luna mask at pos5

    with dis

    "Getting up, I search inside the nearby closet to find the thing I'm looking for."

    play amb "ambient/base_alarm_02.ogg" volume 0.3

    "Just in the nick of time, too."

    "Already I can hear alarms in the distance."

    ql "Time to get out of here..."

    show letterbox behind luna

    m "{size=-8}H-help...{/size}"

    ql "Wait!"

    ql "Did I just hear a voice?"

    ql "It's weak, but I can hear--"

    m "H-Help!!!"

    l "My goodness..."

    scene nox_warehouse_inside_01 at bgz

    show letterbox

    show luna mask at cz

    with dis    

    "When I see the source of the noise deeper in the dark closet, I can't help but be appalled."

    "It's a young woman, one who has certainly seen better days, chained to the wall."

    "She's beaten up and thin as a rail."

    l "I'm coming."

    youngwoman "Oh please! Please come and help me!"

    show luna mask_gun

    play snd "sounds/gunshot_blaster_01.ogg"

    play snd1 "sounds/item_breaking_01.ogg"

    "Rushing to her aid, I use my laser pistol to disintegrate her chain."

    l "It's okay, I'm with AEGIS... You're safe now."

    youngwoman "Thank you! Thank you! He was horrible, he kept--"

    l "Don't worry now... It's over..."

    l "I'll bring you to safety."

    youngwoman "Thank you so much..."

    play snd "sounds/body_fall_04.ogg"

    show luna mask

    "She mutters before practically collapsing into my arms."

    play snd1 "sounds/footsteps_single_heels_08.ogg"

    scene nox_warehouse_inside_01

    show luna mask at pos5

    with dis

    "Tenderly hoisting her over my shoulder, I stand up."

    "Those distant alarms are now accompanied by the sound of approaching footsteps."

    "We won't be alone for much longer."

    play snd "sounds/radio_receiver_01.ogg"

    l "Alright, Silencer is exiting."

    l "But I've got company. A captive."

    n "He had a captive?"

    l "A woman... For his own uses."

    n "Scumbag."

    l "Indeed."

    ql "If only I could carry him out too..."

    ql "I could kill him of course, but he deserves worse..."

    ql "He deserves justice..."

    l "What's my best exit route with company?"

    n "Uhhh... One second... Checking..."

    "In the background, I can hear keys clacking around as he desperately searches for what options I might have."

    n "The window!"

    l "Thanks."

    play snd "sounds/window_sliding_open_01.ogg"

    scene nox_warehouse_inside_01 at bgz

    show letterbox

    show luna mask at cz

    with dis   

    "Opening up the window, I see it opens up onto a flat roof."

    stop amb fadeout 4.0

    $ renpy.music.set_volume(0.7, delay=0.8, channel="music")

    play snd "sounds/landing_ground_01.ogg"

    scene black with dis

    play snd1 "sounds/footsteps_single_heels_04.ogg" volume 0.5

    play snd2 "<silence 0.25>"

    queue snd2 "sounds/footsteps_single_heels_05.ogg" volume 0.4

    play snd3 "<silence 0.5>"

    queue snd3 "sounds/footsteps_single_heels_06.ogg" volume 0.3

    play snd4 "<silence 0.75>"

    queue snd4 "sounds/footsteps_single_heels_07.ogg" volume 0.2

    "I climb out onto it and begin sprinting as fast as my legs can carry me."

    play snd "sounds/gunshot_distant_01.ogg"

    "In the distance behind me, I eventually hear some shots ring out."

    "They miss me by a mile."

    ql "Useless cretins."

    "They never stood a chance..."

    stop snd fadeout 0.4

    stop music fadeout 1.0

    scene black with Dissolve(1.2)

    scene edric_quarters at bgz

    show letterbox

    play music1 "music/breaking_headlines_news.ogg"
    
    show luna suit neutral at pos3

    show edric base serious at pos7
    
    with Dissolve(1.2)

    e "Good work today, Silencer."

    l "Thank you, sir."

    e "We'll make sure that poor girl receives the help she needs."

    l "Most appreciated."

    e "It's not much when compared to your valiant effort."

    l "It's nothing, really..."

    e "Not true. That was above and beyond."

    l "It's what was right, simple as that."

    l "That's why I'm here... That's what I'm fighting for."

    show edric neutral

    "Edric smiles."

    e "It's true..."
    
    e "Always good to be reminded what we're fighting for..."

    e "Thank you, Luna. Now please, take some time for yourself."

    e "That's an order."

    l sigh "If you insist..."

    stop music1 fadeout 2.5

    scene black with Dissolve(1.0)

    pause 0.5

    show apc

    show pov_change_letterbox

    show aiden suit look behind pov_change_letterbox at pov_change:
        matrixcolor TintMatrix("#000000") * SaturationMatrix(0.0)

    pause 0.8

    hide aiden suit look

    show aiden suit look behind pov_change_letterbox at pov_change 
    
    with diss

    pause 1.0    

label aiden_02extra:

    play music "music/town_06_old_castle.ogg"

    play sndl "sounds/footsteps_running_01.ogg" volume 0.7

    scene building_09_n_l at running(zoom_level=1.05, down_time1=0.5, up_time1=0.5, down_time2=0.5, up_time2=0.5, down_offset1=3, up_offset1=-2, down_offset2=3, up_offset2=-2)
                                    
    with Dissolve(1.5)

    $ update_status("emotional_status", _("RELIEVED, CONCERNED"), notify=False)

    "In the days after the incident, I do my best to cope with the situation."

    "Part of that is trying to keep up with as much of my daily life as I can, including training."

    show luna suit neutral at off

    show aiden suit neutral at off

    l "Alright, let's keep it up. Three more laps!!!"

    a joyous sweat "R-right on..."

    "Resistance training, combat training, cardio, I'm not skimping on anything."

    "The doc keeps telling me to stop pushing myself, but I can't just sit there and rest."

    "I can tell if I stop, I'll start losing my strength."

    qa "I can't have that."

    qa "I can't let anyone down..."

    l "You're doing great."

    a neutral "Thanks, Lulu..."

    a "I wouldn't be able to do it without you."

    l "Not true. You got this."

    a "I hope so."

    l "...Are you scared?"

    a look "About what?" 
    
    l "What happened to you..."

    a "Am I scared of being... whatever you call this? \"Sick?\" Not at all."

    l "Good..."

    a "Are you?"

    l "Scared? No..."

    l "Concerned, maybe a little..." 
    
    l "Or a bit more than a little."

    a happy "It's funny. If you were the one who was \"sick,\" I bet you wouldn't bat an eyelash, but me..."

    l neutral "It is what it is."
    
    l "I suppose we are similar in that regard."

    l "I just wish there was something I could do..."

    a look "Same."

    l sigh "I can only imagine."

    a "It's not just that I want to get rid of this... poison."

    l neutral "What else then?"

    a serious "It's the fact that Nox has access to something like this at all."

    a "A syndicate like them... Who knows what they plan to do with it?"
    
    a "All I know for sure is that it isn't good. They can do a lot of harm with it, even at the tiniest dosages... as we've learned."

    l "That is certainly true."

    a "Knowing that... I want to do something to stop them..."

    a "No, I need to do something to stop them."

    l "You are... You've dedicated your life to fighting them."

    a sigh "Yeah, sure..."

    a look "But apart from what I normally do, you know?"

    l "I do know... Frankly, I feel the same way..."

    l "The question is, what can we do? Not even just us, AEGIS as a whole?"

    m "I m-might have an idea or two!"

    "A voice from behind us calls out to us."

    a "Huh?"

    "Looking behind us, I see Nevin trailing not far behind us."

    stop sndl fadeout 1.0

    scene building_09_n_l
    
    show luna suit neutral at pos4

    show aiden suit neutral at off

    show nevin aegis sigh sweat at pos6
                                    
    with Dissolve(1.5)

    "We come to a quick stop, allowing him to catch up."

    a "Nevin? How long have you been there?"

    n "J-just a m-moment..."

    "He wheezes, trying to catch his breath."

    l "Attempting to spy on us?"

    n "If I am... I'm not doing it well..."

    a "Okay, okay... Take it easy and breathe."

    n "Y-yes... Th-thank you..."

    show nevin aegis look -sweat

    "After a moment to compose himself, Nevin finally speaks again."

    show aiden look

    n "I came here because I wanted to talk to you guys about something off the record."

    n "No comms involved."

    l "Sounds shady..."

    n "I don't mean it that way..."

    n "I'm just not supposed to share this stuff outside my department."

    a "Share what?"

    n "Some intel..."

    n "I tried to propose a new project, but it got blocked by my boss..."

    a "Really? Any idea why?"

    n "I can't say for certain, that does happen sometimes."

    n "Not always with good reason, at least in my humble opinion."

    a "Gotcha..."

    l "So what is this intel?"

    n "Not here... I don't even have it with me."

    n "In private."

    a "Okay... How about our room?"

    n "Sounds good..."

    n "I'll be there at 2000."

    l "That works with us."

    n "Good..."

    n nervous "Alright, sorry to interrupt your workout."

    a neutral "All good. Want to join us for the rest of the jog?"

    n nervous "N-nope! I'm all good..."

    a "If you insist. Alright, later man."

    n neutral "Yup, bye! See you at 2000."

    l "Until then, Nevin."

    play snd "sounds/footsteps_two_sneakers_08.ogg"

    scene building_09_n_l at bgz

    show letterbox
    
    show luna suit neutral at cz

    show aiden suit look at off
                                    
    with dis

    "As quickly as he came, but less silently, Nevin heads back towards the HQ."

    l "Strange..."

    a "You're telling me."

    a "Still, I say we hear him out."

    l "No doubt. I'm happy to have any help we can at this point."

    l "In the meantime, shall we get back to our regiment?"

    a neutral "For sure."

    play sndl "sounds/footsteps_running_01.ogg" volume 0.7

    scene building_09_n_l at running(zoom_level=1.05, down_time1=0.5, up_time1=0.5, down_time2=0.5, up_time2=0.5, down_offset1=3, up_offset1=-2, down_offset2=3, up_offset2=-2)
                                    
    with diss

    "The two of us slowly begin to jog again."

    "Everything is going well, when..."

    stop sndl

    play snd "sounds/heartbeat_100bpm_01.ogg"

    $ renpy.music.set_volume(0.1, delay=0.8, channel="music")

    scene building_09_n_l

    if persistent.flash_enabled:

        with flash(color="#d21717", max_alpha=0.9, fade_in=0.1, hold=0.2, fade_out=0.4)

    pause 0.3

    show layer master:
        zoom 1.05
        align (0.5, 0.5)
        blur_vision(15)
        ease 1.0 xoffset 10 yoffset 5
        ease 1.0 xoffset -10 yoffset -5
        ease 1.0 xoffset 5 yoffset -8

    with dis
    
    qa "Hnnngh!"

    show luna suit shocked at off

    show aiden suit look at off

    l "Aiden? Are you okay?"

    "Luna instantly calls out to me as I come to a sudden stop that luckily isn't a tumble onto the track."

    stop snd fadeout 1.2

    $ renpy.music.set_pan(0.0, delay=1.2, channel="music")
    $ renpy.music.set_volume(1.0, delay=1.2, channel="music")

    scene building_09_n_l with Dissolve(1.2)

    show luna suit shocked at off

    show aiden suit pain at off

    a "I'm fine! I'm fine!"

    qa "Not really... But..."

    qa "I can't let this hold me back..."

    l "Are you sure? Maybe we should go to the med-bay."

    a "Please, Luna. Don't. It's nothing. I'll go after the job."

    l "Aiden, the doctor said--"

    a "He said a lot of things, Lulu."

    a "And I am saying it won't hold me back." 
    
    l neutral "I'm glad to hear that, I am."

    l "Still, this isn't the first time I've noticed you have an episode like this."
    
    l "I've seen you when you thought I haven't been looking."

    l "I see you struggling with the pain."

    a sigh "That isn't all the time though. Just once every day or two."

    l "Are you sure?"

    a look "Positive. I will go to the med-bay as soon as we're done, but I won't let it keep me down."

    l "But we're just exercising, we don't need to--"

    a "I need to keep doing what I'm doing. I can't let this stop me from fighting Nox."

    a serious "I can't let them use this thing on innocent people."

    a look "Now, stop doting on me. How would you feel if our positions were switched?"

    l sigh "I'd tell you to shove it."

    a neutral "Exactly. And you'd be right to."

    l "Okay, okay... I understand your point."

    a "Good."

    a "Because, my pride aside, I love you."

    l simper "Ha! Is that so?"
    
    a "Yeah..."

    a "And, you know... since I love you and all... promise me you won't get hurt on my account."

    l "Not hurt? Impossible... I'm an agent of AEGIS."
    
    l "How about not getting hurt too badly?"

    a cheeky "Well, you're a badass, I guess you can take a little punishment."

    a "To say otherwise would be insulting."

    l "You have that right."

    play snd "sounds/kiss_02.ogg"

    "She laughs and then kisses me."

    l simper "Okay... Now that's settled, can we finish this jog so we can get you to the med-bay?"

    a neutral "Yes, yes... Two more laps?"

    l "How about one?"

    "Given the look in her eyes, I don't think I should question her..."

    a "...Okay, deal."

    stop music fadeout 2.7

    scene black with Dissolve(1.5)

    pause 1.2
    
    "After our jog, we head back to the medical station for a few more tests, as I promised." with dis
    
    "Thankfully, the news is good." 
    
    "Despite that little incident on the track, it seems the temporary treatment is working, and the poison is taking a lot longer to build up in my bloodstream than before."

    "Still, I can't deny it, the poison has left me feeling more exhausted than usual."

    play music1 "music/bad_day.ogg" fadein 2.0

    scene aegis_bedroom at bgz 

    show aiden suit look at off

    show luna suit neutral at cz

    with dis

    "We have dinner and then head back to our room where we wait for Nevin."

    l "He said he would be here at 2000?"

    a "That's what he said."

    l serious "He's late."

    a "I wouldn't sweat it."

    a "If he's late, he probably just got held up."

    l sigh "Or he was caught downloading those documents..."

    a serious "I doubt it. He's probably just being extra careful, as usual."
    
    l neutral "That would be like him..."

    l "I hope that's the case."

    a "It is."

    show luna simper

    "She smiles."

    l "Always so optimistic, even in a grim situation like this."

    a "That's me."

    l "It really is..."

    "She takes my hand and squeezes it tightly."

    play snd "sounds/knock_metal_01.ogg"

    show luna neutral

    "Looking into her eyes, I want to kiss her again, but before I can make a move, I'm interrupted by a knock at the door."

    l "That must be him."

    scene aegis_bedroom 

    show aiden suit look at off

    with dis    

    play snd "sounds/door_tech_open_01.ogg"

    "Nodding, I walk over to the door and open it."

    show nevin aegis look at pos5 with dis

    a "Hey man."

    n "Aiden, hey..."

    "He looks from side to side before looking back at me."

    n "I brought the files you wanted."

    "Gesturing for him to come inside, I step aside."

    play snd "<silence 0.7>"

    queue snd "sounds/door_tech_close_01.ogg"

    scene aegis_bedroom with Dissolve(0.5)

    "He quickly walks in and I shut the door, locking it."

    scene aegis_bedroom at bgz

    show aiden suit look at off

    show nevin aegis look at rz

    show luna suit_alt neutral at lz

    with dis

    n "Is this a secure room?"

    l "We turned off our voice assistants, so there's no chance of anyone listening."

    n "Good..."

    n "I won't bury the lead then, I found something."

    a "What did you find?"

    n "It's quite a story, allow me to explain."

    n "After what Captain Edric said the other day, I've been trying to find some clue... some hint of where we can focus our efforts."
    
    n "And, as I was looking at all the manifests of the shipments we've secured and focusing on the poisons and other chemical weapons, I think I managed to narrow down the potential sources to one or two factions within Nox."

    n "Narrowing that further and looking at which ones we've seen that have connections to Zeph's faction, I think I've figured out a possible starting point."

    l "And what starting point might that be?"

    n "The Koldrak faction."

    a "Koldrak? Isn't he a small fry?"

    n "Historically yes, he hasn't really been a power player."

    n "He hasn't gotten as much attention from us because he's stayed away from violent crime and mostly stuck to chem production and supply."

    l "I see..."

    n "Things have changed though..."

    a "How so?"

    n "With Boss Hevlan's death and the shakeup of the syndicate, he's been one of the players on the move."

    n "He's made a play for a lot more territory lately."

    n "A lot of the rumblings of discontent we've encountered lately has been as a direct result of his organization attempting to assert itself as a larger part of the syndicate."

    a "He's not making friends."

    n "No, but he needs them..."

    l "What do you mean?"

    n "I'm saying that despite his posturing, it seems his organization is weak in terms of muscle."

    n "Makes sense considering how much he's been concentrated on production over the years."

    n "Anyway, his desperation is our opportunity."

    a "How is that?"

    n "We got an invitation in."

    l "We did?"

    n "Well, not us directly..."

    play snd "sounds/barcharge_04_short.ogg"

    "Activating his touch-pad, Nevin opens up a document containing a long exchange of messages."

    n "These are communications we found on one of the comm devices we confiscated at Zeph's warehouse."

    a "What are they about?"

    n "About defecting."

    l "Defecting? From one faction to another?"

    n "Yes, look."

    n "These guys, no more than lowly grunts, were working out a deal with the Koldrak operation, which was offering them a much better cut of the loot for their services in exchange for ripping off some of Zeph's tech."

    l "Buying loyalty... despicable..."

    a "No kidding..."

    n "I'm not going to argue... but it's definitely a great opportunity for us."

    a "In what way?"

    n "Well, as you can see from these messages, it's a pretty shady affair."

    n "The grunts made anonymous contact with one of Koldrak's higher ups and were feeling each other out, hoping to jump ship."

    n "They were going to have their first meet in a few days."

    l luna suit neutral "So they've never met before..."

    "She strokes her chin, immediately catching on to his suggestion."

    l "That's the opportunity of which you speak of."

    n "Yes..."

    n "If we wanted to, we could send some agents undercover to join their organization and infiltrate their facility, then perhaps we could figure out details about the poison... but that's just the start of it."

    a "Yeah... This opportunity is a lot bigger than just the poison."

    a "If we could stick some of our intelligence agents in there, we'd be able to wreak havoc."

    l "Absolutely."

    n "I agree, and I was hoping to get your support when I bring this to Captain Edric's attention."

    n "Particularly after my request got denied the first time, I want all the backup I can get."

    n "I know it's a risky plan. After all, this could be an ambush by the Koldrak organization."

    n "Still I think it's worth a shot, and can benefit AEGIS as a whole." 
    
    l "Absolutely. Captain Edric is a reasonable man. I have no doubt that he will at least consider it."

    stop music1 fadeout 2.0

    scene black with circuit_in

    play music "music/end.ogg" fadein 4.0

    scene edric_quarters at bgz

    show letterbox
    
    show aiden suit look at off
    
    show luna suit_alt serious at pos3

    show edric base serious at pos7

    show nevin aegis serious at pos5
    
    with circuit_out

    e "I'm sorry, we simply can't afford the men."

    l "How?"

    e "It's quite simple. Because they are otherwise occupied, Agent Virelith."

    l "But do you not see this opportunity?"

    e "I do... I did the first time it was sent to my desk."
    
    l "So you knew already?"

    e "Obviously... I'm the one who denied the approval of all such operations--"

    l "WHAT?!"

    e "Allow me to finish."

    e "I denied them on a temporary basis."
    
    e "This isn't forever. Perhaps we can get to it, but right now we are stretched far too thin."

    n "Sir, I really appreciate that you are working with limited resources, however this seems to be a rather limited-time opportunity."

    n "The rendezvous with these recruits is scheduled for the day after tomorrow."

    n "If we go through with it we can learn some of the corps through which they do business through, the locations of those businesses, the full identity of their leadership..."
    
    n "So much potential information that could help us..."

    n "We simply can't afford to wait on this."

    e "I understand, Agent Moresly."

    e "But even if I were to approve this incredibly risky plan, which could very well be some sort of trap orchestrated by the Koldrak camp, which men would I assign to it?"

    e "All of our best infiltration agents have already been deployed."

    l "Send me then!"

    e "You? Absolutely not."

    l "Why not?"

    e "Because, simply put, you aren't a spy."

    e "You can sneak, you can fight, but have you ever had rudimentary training for infiltrating enemy organizations?"

    "Luna, clearly not happy to hear what she's hearing, shakes her head."

    l "No, sir."

    e "Then please, stick to your lane, and leave the decision-making to me."

    show nevin surprised

    l "I can't, sir."

    e surprised "...What?"

    "Captain Edric asks, in complete disbelief."

    l "I can't just stand by and do nothing here..."

    l "If you don't send me... I'll be going on my own."

    e "Agent Virelith, please, be serious!"

    l "I'm serious..."

    l "I've already been given time off, by you, to assist Aiden with his medical situation."

    show nevin nervous sweat

    l "I plan on doing just that."

    e serious "I see..."

    "Captain Edric shakes his head."

    e "Then I see there's nothing I can do to stop you..."

    l "No, I don't think so."

    l "There's a reason I joined AEGIS, which is to do what's right, no matter the cost."

    l "It has always supported me in that goal, until now."

    show nevin surprised -sweat

    e "Stop, please..."

    l neutral "Sir?"

    e "You're right."

    e "This opportunity is too good to pass up, and standing in the way due to... bureaucratic concerns and external pressure is not right..."

    n look "External pressure? What do you mean, sir?"

    "He sighs."

    e "I've said too much already..."

    a "Is something wrong?"

    e "Potentially so..."

    e "Look, all of you, I wish I could officially sign off on what you're proposing, I really do."

    e "But the fact of the matter is that I was given an order from those above me that we have to cut back wherever we can."

    l "Why?"

    e "Because, once again, our funding is being cut."

    e "While we are thankfully able to run independently from the rest of the government, we still need their financial support."

    e "It was fine for a time, but with the syndicates sneaking their tendrils into the governor's pocket more and more every year, a complete collapse only feels like a matter of time."

    l "I see... They're trying to starve us out..."

    e "They can try."

    e "But as long as there are good people like you, they won't be able to succeed."

    a "Are you saying what I think you're saying?"

    $ update_status("emotional_status", _("FOCUSED, DETERMINED"), notify=False)

    e "Yes. Go undercover if you wish, Luna."

    e "You have my blessing... but unfortunately, not my support."

    e "I wish I could, but if it were to be discovered that I endorsed this plan..."

    l "Understood. Say no more."

    l "I'll manage on my own."

    a "I'm sure you can... but that won't be necessary."

    l "How so?"

    a "I'm going to come with you."

    show luna dubious

    "She recoils."

    l "Aiden, no... Please..."

    a "Luna, you promised." 
    
    a "I might not be 100%%, but with the anti-venom they're pumping me with, I'm not so bad."

    l "Okay..."

    "She gives in, slightly begrudgingly."

    a "Thank you. I need to go, otherwise I'd be sitting on my ass. I can't let you do all the work!"

    show luna neutral

    n shocked "N-neither can I!"

    a surprised "Huh?"

    n "I'm going to come too."

    a "W-what? Are you crazy?"

    n serious "Not at all!"

    n "I know I'm not a field operative, but you're going to need someone with a bit more technical know-how on your side if you want this mission to succeed!"

    a "Nevin!"

    show luna simper

    n "I'm serious! Like, what if you needed to crack into a database or something?"

    "I turn to Luna, who smiles and shrugs."

    l "He does have a point."

    a "Are you serious? I thought I'd at least have your back on this!"

    l neutral "If it were up to me, I'd be doing this alone."

    l "But, if I were to have some help, someone with those sorts of skills would be helpful."

    "I sigh deeply and then nod."

    a sigh "You're right..."

    l simper "Not so fun when someone else does it to you, is it?"

    a "No..."

    a neutral "Okay Nevin, you're in."

    show luna neutral

    e "No one more though. I draw the line at you three."
 
    e "Things will be tight as they are."

    l "Understood."

    e "You can bring weapons and other basic supplies, but not much more than that."

    e "Do what you can. Find an antidote. Disrupt that Nox faction as much as possible."

    a serious "Will do."

    e "Then best of luck... I'll provide you as much cover as I can without doing anything official."

    l "Much appreciated."

    e "It's the least I can do."

    e "After all, we are AEGIS. It's our duty to protect everyone. If we can't even protect our own... What good are we?"

    stop music fadeout 2.0

    scene black with pixellate

    pause 0.7

    play music1 "music/electric_equipment_connection.ogg" fadein 2.0

    scene aegis_bedroom at bgz
    
    show aiden suit look at off
    
    show luna suit serious at lz
    
    show nevin aegis serious at rz
    
    with pixellate

    "Heartened by Captain Edric's unofficial approval, we spend the next 24 hours hastily learning what we can about the Koldrak faction in order to better prepare ourselves."

    "Since the operation is unusually clandestine, we avoid discussing it in any of AEGIS's public facilities, resorting to having meetings in our quarters."

    "That doesn't stop Luna from taking this any less seriously than a normal operation though."

    l "So, our primary mission is to disrupt their production of the synthetic poison and find a treatment for Aiden's condition."

    l "Those take precedence over everything else."

    n "Agreed. While we will have plenty of opportunity to sabotage some of Nox's operations in some ways, you're my bud. I can't let you..."

    n sigh "Well, I don't want anything bad to happen to you."

    l neutral "We're in agreement about that. Any objections?"

    show nevin look

    a sigh "I guess not. As long as disabling their supply is the top priority."

    n "Finding a treatment would help too."

    l suit_alt "Excellent."

    l "Now, to move on to our secondary objectives."

    l "First, to uncover any additional information we can about Nox's inner workings."

    "That kinda goes without saying, but is certainly true."

    "With all the sway Nox has managed to get over governing bodies in recent years, it would be helpful to know how they've managed it."

    l "Second, as Captain Edric emphasized, to hinder any operations that the Koldrak organization is attempting to execute."

    l "I would personally expand this to any aspect of the Nox Syndicate in general."

    a neutral "Business as usual then."

    l "In a manner of speaking."

    l "Nevin, did you have any intelligence you wanted to share about Koldrak?"

    n "Unfortunately, we don't know that much about him."

    n "The guy himself goes by Vargas Koldrak. Appeared on the scene about fifteen years ago."

    n "Made a name for himself as muscle for the Sutili organization before striking out on his own and starting up a chem running business."

    $ unlock_codex_entry("character_sutili")

    $ update_status("vargas_feelings", _("Sounds like a real piece of work. What else could I expect from a Nox sub-boss? I can't wait to take him down."))

    a serious "Sutili, huh?"

    n "Yeah, sorry to bring them up..."

    a "It's okay... It's been a long time..."

    qa "Besides, it's not like a day goes by where I don't think of that name..."

    qa "The name that took my parents from me..."

    "I feel a warm hand on my shoulder."

    l "It's okay..."

    l "He can't hurt you now..."

    a neutral "Thanks to you."

    "She nods solemnly and I reach up to touch her hand."

    a "It's okay Nevin, you can continue."

    n nervous "A-alright..."

    l "You were saying that this guy isn't from a major family?"

    n surprised "Y-yes! As far as I can tell, the Koldrak family isn't exactly a famous bloodline in the Nox syndicate."

    n look "He's really only been a bit player up until the time of Boss Hevlan's death, at which point he started trying to consolidate power."

    a look "I wonder what he plans on doing with that power... Maybe take over some of Zeph's old territory?"

    l "It would be a smart move, but he'll have to move fast. He certainly isn't the only one who would be aiming to fill the void."

    n "Definitely not. In fact, there's already been all sorts of rumbling from our sources, things are going to get pretty rough over the next while, at least from the looks of things."

    a neutral "Guess we're coming in at a pretty fortunate time to put a wrench in things."

    n neutral "Absolutely!"

    a look "Hmmm..."

    show luna surprised

    "Luna turns towards me, eyebrow raised."

    show nevin look

    l "Is something the matter?"

    show luna neutral

    a "It's nothing much..."

    a "I was just thinking... While we're there, perhaps preventing his expansion wouldn't be the smartest move."

    l "Really? How so?"

    a "Well, think about it."

    a "As Nevin said, Zeph's territory is getting swallowed up by someone in the Nox syndicate, no matter what."

    a "So, if another organization grabs it, that might honestly be even worse."

    a "At the very least we can try to minimize any bloodshed or casualties that the Koldrak organization perpetrates."

    l "That is true."

    n "Yeah, good point..."

    a "I have to admit, once we've completed our objectives as best we can, we can arrest or neutralize Koldrak. Then, after he's gone, those same players will probably scoop up that land anyway."

    a "But in the meantime, we can make that territory a safer place for citizens to live."

    "Luna nods in agreement."

    l "A worthy goal..."

    n "That could work."

    l "Okay, let's see if that's a viable approach."

    a "Yeah, we'll see, I suppose."

    l "Indeed..."

    l suit "In the meantime, we have one last piece of business I'd like to address."

    a neutral "What's that?"

    l "How we will be addressing each other while undercover."

    a "Maybe it would be best if we didn't use our real names."

    l "I agree, that would be prudent."

    n sigh "Yeah... I'm not used to being called by an alias though."

    a "Does \"operator\" not count?"

    n look "Technically, but you know what I mean..."

    l "How about I go by Claire, Aiden goes by Liam and Nevin goes by Fred?"

    a "I don't see a problem with that."

    n "Me neither..."

    n sigh sweat "I just hope I don't screw it up!"

    a happy "Don't worry, you won't."

    a look "And if you do..."

    l "Better not to."

    n nervous "Y-yeah..."

    stop music1 fadeout 1.2

    scene black with Dissolve(1.2)

    play music "music/imagine_the_future_underscore.ogg" fadein 1.2

    scene aegis_cafeteria
    
    show aiden suit surprised at off
    
    show luna suit neutral at pos6

    show nevin aegis look at pos4
    
    with Dissolve(1.2)

    "After an uneasy night's sleep and another day of prep, the three of us meet up in the cafeteria for one last dinner before we head out."

    n "Meatloaf ration again?"

    a "I'm not complaining."

    n "Why would you? You love this stuff..."

    a surprised "You don't?"

    n "Not my favorite..."

    l "At least there is mineral cake for dessert."

    n pout "Yummy..."

    a "You don't like mineral cake?!"

    show luna shocked_upset
    
    n "Not really..."

    l "Sacrilegious..."

    n look "If you say so..."

    show luna neutral

    a cheeky "Maybe once you've eaten whatever slop Nox feeds its grunts, you'll be a lot more grateful next time you have a meal here."

    n sigh "Whenever that is..."

    a look "That's true... Who knows how long it will be until we eat here again."

    l "Hopefully not too long..."

    show luna simper

    "Luna softly smiles."

    l "After all... This place is home..."

    l "I'm going to miss it."

    a neutral "Yeah, I think we all are..."

    n look "Definitely..."

    n nervous "Not the food, though."

    a cheeky "Speak for yourself."

    n pout "I am."

    l "Heh..."

    l "At least I have you two by my side."

    l joyous "I was prepared to do this on my own, but it's better this way."

    play snd "sounds/glass_01.ogg"

    show luna simper

    "She lifts her glass of water up into the air."

    l "To taking down Nox from the inside."

    play snd "sounds/glass_02.ogg"

    "Nevin and I raise our glasses in the same fashion."

    a neutral "And to a safe mission. We best all make it home in one piece."

    a "If something happens to either one of you on my account..."

    a "Well, just don't."

    n smile "I'll do my best!"

    l "Don't worry. We'll be fine."

    l joyous "I promise."

    stop music fadeout 2.0

    scene black with cubes_in

    pause 1.1

    play music1 "music/criminals.ogg" fadein 2.0

    scene neo_elysia_alley with cubes_out

    $ update_status("aiden_feelings", _("Seeing him fight like this... Putting the safety of others before his own... I'm not sure I've ever felt more in love... I need to protect him."))

    "After dinner, we leave the AEGIS base for the last time in who knows how long."

    "Unlike usual, we don't leave in a transport, but on foot instead."

    "Making sure we aren't being followed, we make our way through the maze-like streets of Neo Elysia to the rendezvous point that was outlined in the recruitment message, with Zeph's stolen tech in-hand."

    "As we do, we pass by person after person, bundled up in blankets, sleeping in whatever alley they can find."

    "Some are chem-addicts, others simply jobless."

    "All of them struggling to live another day."

    "Seeing them fighting for their survival causes the fire in me to grow."

    "I might not be at my best, but I need to do this... for them."

    scene black with fblinds

    scene neo_elysia_alley at bgz with fblinds

    "We approach our destination early and with caution, trying to sniff out any potential ambushes."

    "Despite getting there a couple of hours early though, we aren't the first ones to arrive."

    scene neo_elysia_alley at bgz

    play snd "sounds/footsteps_boots_02.ogg"

    queue snd "sounds/cock_pistol_02.ogg"

    show rogue base neutral at cz

    show luna nox_01 neutral at off

    show nevin nox_01 look at off

    show aiden nox_01 look at off

    with dis

    noxgrunt "Hands up! What are you doing here?"

    "A grunt yells, popping out of the shadows with a gun pointed right at us."

    "The three of us immediately comply."

    a "It's all good, we're cool. We were Zeph's guys..." 
    
    l "We were told to meet you here. We brought the package." 
    
    noxgrunt "Good... Let me see it."

    play snd "sounds/case_01.ogg"

    "Snatching the case out of Luna's hands, he opens it and peers inside."

    noxgrunt "Heh, yeah... That's the stuff."
    
    noxgrunt "Zeph won't miss that shit anymore, will he? Poor old bastard got popped."

    a "Sure did. Your boss' message came at just the right time."

    noxgrunt "That's one way of putting it."

    noxgrunt "Y'all are early."

    a "We aren't exactly busy these days."

    noxgrunt "True..."

    noxgrunt "Alright, come on. Let's get out of here."

    a "Lead the way."

    play snd "sounds/footsteps_sneakers_01.ogg"

    scene black with diss

    "He leads us into a dark alley that I'm only half-sure that we'll make it to the other side of alive."

    "Luckily we do." 
    
    "Once we reach the end of it, we see a couple more grunts in front of a transport."

    noxgrunt "They showed up early. Let's get back to base."

    play snd "sounds/car_door_01.ogg"

    "The other grunts nod and open up the door to the transport, allowing us inside."

    "One of the grunts gets into the driver's seat while the other two get in the back with us."

    play snd "sounds/car_door_02.ogg"

    scene vehicle_02_a:

        xalign 0.5 yalign 0.5
        zoom 1.05 
        
    with diss

    "The door locks into place behind us."

    play amb "ambient/vehicle_driving_01.ogg" volume 0.8 fadein 1.0

    hide vehicle_02_a

    show vehicle_02_a at car_shake:

        zoom 1.05 

    "Suddenly things start to feel a lot more claustrophobic."

    "The fact that they are pointing their guns at us doesn't exactly help ease my discomfort."

    "We travel in a tense silence, each of us staring straight ahead into space for a while.{nw}"

    show jin base neutral at cz
    
    extend " However, that is disrupted when one of the grunts leans forward and stares at me right in the face."

    "As much as I'd like to keep my trap shut, it's such a strange and uncomfortable situation that I can't help but comment on it."

    show aiden nox_01 look at off

    show luna nox_01 neutral at off

    show nevin nox_01 look at off

    a "What's up?"

    noxgrunt "This is going to sound really strange..."

    a "What is?"

    stop music1 fadeout 0.3

    play snd "sounds/heartbeat_100bpm_01.ogg"

    noxgrunt "Did you go to the academy?"

    "A cold shiver goes down my spine."

    qa "Shit! What do I say?!"

    qa "Do I tell him the truth? If he knows I did and I lie, we're dead!"

    qa "I have to just roll with it."

    a "Uh... Yeah, how do you know?"

    noxgrunt "Heh..."

    show jin base smile

    noxgrunt "This is a strange spot for a class reunion, but I was with you there for a couple years before I dropped out."

    $ unlock_codex_entry("character_jin")

    $ unlock_codex_entry("lore_the_academy")

    jin "The name's Jin."

    qa "Oh... Jin..."

    stop snd fadeout 0.3

    qa "I remember you... Without that scar though..."

    qa "Shady as all hell... No wonder you ended up in Nox..."

    jin "And you were... don't tell me..."

    qa "Maybe he'll forget..."

    jin "Aiden, right?"

    qa "Shit."

    a smile "Y-yeah... That's right..."

    jin "Damn... Who'd have imagined two academy boys in this situation? Right?"

    a "Life is strange sometimes, isn't it?"

    qa "Fucking hell... My first undercover mission and my cover is blown just like that..."

    play music1 "music/criminals.ogg" fadein 2.0

    qa "At least he doesn't know I've been in AEGIS..."

    jin "What made you quit the academy? You were doing well..."

    qa "I might as well play along as best I can."

    qa "What would strike a chord with this kind of asshole?"

    qa "Actually, it doesn't take too much thought. I know just the thing."

    a look "Honestly? The pay..."

    "He sighs and nods."

    jin neutral "I'm right there with you, my man."

    jin "Those government douchebags ask for your loyalty and give you peanuts in return."

    jin "Not worth it at all."

    qa "Yeah, forget about duty and justice..."

    qa "All about the money with this asshole. I hit the nail right on the head."

    jin smile "When we were together in the academy you were such a straight arrow, but you were smart, so it honestly makes sense."

    jin neutral "Cops are all dumbasses..."

    a "You said it..."

    jin "That being said, Zeph man? Really?"

    jin "That was a bad move..."

    jin "Hell, even I ended up in a better crew than you."

    a sigh "Well, maybe..."

    qa "Now he's rubbing it in with this shit?"

    qa "I swear, when I'm done with this asshole..."

    jin "Eh, I'm just busting your balls, man..."

    jin "It's cool, don't worry. You're on the winning side now." 
    
    jin smile "We'll be making a lot of money together."

    jin "Vargas has got big plans for the syndicate. You'll see."

    a look "If everything works out, I suppose."

    jin "Ha... No need to worry about that."

    jin "I know you're a solid dude. It's cool."

    jin neutral "Who else you got with you?"

    "He says, turning his attention to the others."

    l "I'm--"

    jin surprised "Holy shit!"

    jin "I just recognized you too!"

    l surprised "You did?"

    "Luna reacts with genuine surprise."

    l neutral "I'm sorry, I don't believe we've ever met."

    jin smile "No, no! We haven't!"

    jin "I remember that face though."

    jin "This dork over here used to carry your picture around with him all the time in the academy."

    jin "It was his viewscreen background."

    l neutral blush_02 "R-really?"

    a embarrassed blush_02 "Uh... Yeah..."

    qa "How the hell does he remember that?!"

    qa "Never thought that would come back to bite me in the ass, especially in this way..."

    qa "Sure guys would tease me at the time... but all these years later..."

    jin smile "Yeah, he wouldn't shut up about you..."

    jin neutral "Oh hell, what was your name? Lindsey, right?"

    "Luna looks at me with slight frustration and then shakes her head."

    jin "Fuck... I'm close though... I know it."

    jin "Lana? Laura? I'm close, right?"

    l serious -blush_02 "It's Luna!"

    show jin smile

    "She gives up in frustration, and I don't blame her."

    "After all, even if he didn't get it right this second, he might have remembered her name in a day or two, so why complicate matters and even introduce the idea of deception?"

    jin "Yes, that's right! Luna!"

    jin "Wow..."

    jin "So, are you two together?"

    jin "You must be if you're here together all these years later, right?"

    "She sighs and then nods once more."

    l "We're together..."

    jin surprised "Damn!"

    "Jin extends his fist towards me."

    jin smile "Dude, props... That shit is wild."

    jin "Never in a million years did I think you'd bag her."

    a look -blush_02 "Uh... Thanks?"

    "I say, begrudgingly bumping my fist against his."

    jin "Not that she looks too wild about it."

    l serious "No!"

    "Luna practically shouts."

    "I can tell that she's had enough of this."

    l "It's not that. I just prefer keeping things private."

    jin "Yeah, no kidding."

    jin "You did always seem like an ice queen."

    jin "To see you rolling down here with the rest of us criminals."

    jin "You must have really loved this dude to follow him out here."

    "Knowing Luna as well as I do, I am surprised she has managed to restrain herself from choking him to death."

    l neutral "I do..."

    "Is all she says, seemingly spending her energy attempting to maintain her composure."

    jin "Well hey... How romantic..."

    jin "You don't see that much of that kinda stuff back at base."

    jin "I've heard that Zeph's different, but this just shows it."

    jin neutral "I don't think we have any couples on the whole compound. None that last long, anyway..."

    jin smile "Well, now we do."

    jin "Will be interesting to see how the boss reacts to that."

    a "What do you mean?"

    jin neutral "It's nothing, you'll see..."

    qa "That's not the most reassuring..."

    qa "I wonder what's up with this Vargas guy."

    jin smile "Anyway, so Aiden and Luna I know. What about you, little guy?"

    "Nevin rolls his eyes."

    n "I'm Fred."

    "Luna and I immediately look at each other with relief."

    "Although we didn't manage to stick to the plan, at least Nevin is able to."

    jin "You an academy boy too?"

    n "Yeah, a few years after..."

    jin "Are all three of you in some kinda thing together?"

    a "What do you mean?"

    jin "I dunno... Like some kinda poly thing?"

    n surprised "Huh?"

    l shocked_upset "No!"

    "Jin shrugs."

    jin "I didn't think it was so ridiculous."

    jin "You're just the third wheel then?"

    "Nevin winces."

    n smirk "Sure, I guess so..."

    jin "Ha! At least he's honest about it."

    jin "Anyway, sorry for talking your ears off. You guys relax. We'll be at the base in just a few."

    a "Thanks..."

    hide jin with dis

    qa "We're off to a great start..." with dis

    qa "That quite possibly couldn't have gone worse."

    qa "...At least we're still alive. That really would be worse."

    scene black with diss

    "We are blessed with relative silence for the rest of the ride over."

    "I don't risk attempting to communicate anything to Luna or Nevin. Not with the three grunts listening to everything and still pointing their guns at us."

    stop amb fadeout 1.0

    play snd "sounds/car_brake_01.ogg"

    scene vehicle_02_a:

        xalign 0.5 yalign 0.5
        zoom 1.05 
    
    with diss

    "Eventually though, the transport stops in front of a somewhat inconspicuous-looking corporate building."

    scene black with dis

    scene vargas_base at hs(zoom_amount=1.5, y_anchor=0.3, duration=20.0, start_x=0.2, end_x=0.6)

    show letterbox

    show aiden nox_01 look at off

    show luna nox_01 neutral at off

    show nevin nox_01 look at off

    show jin base neutral at off

    with dis

    jin "Okay, we're here."

    l "Good."

    qa "She can't wait to get out of here..."

    jin "Once you're inside, we're going to bring you right to the boss man."

    jin "He'll definitely want to meet you himself. Make a decision."

    n "W-what decision?"

    "Jin simply laughs."

    jin smile "What do you think?"

    "Nevin stares back. I'm pretty sure he doesn't know what to think."

    "I do though..."

    qa "He's going to decide whether we live or die..."

    jin "I wouldn't worry about it though."

    jin "Unless you piss him off, you're golden."

    jin "He's definitely gonna want to keep you around."

    "He says pointing at us... or is he just pointing at Luna?"

    "It's hard to tell..."

    jin "Come on, I'll take ya inside..."

    play snd "sounds/footsteps_two_sneakers_06.ogg"

    stop music1 fadeout 3.0

    scene black with cor_in

    pause 1.0

    play music "music/nox_tension.ogg" fadein 2.0

    scene nox_hallway_vargas at bgz(z=1.1, x=0.5, y=-1.0)
    
    show letterbox
    
    with cor_out

    "Jin takes us inside, accompanied by the two other armed grunts and guides us through a labyrinth of hallways to an office door."

    show jin base neutral at off

    jin "Alright, give me a sec."

    play snd "sounds/door_open_vargas_01.ogg"

    "He knocks on the door and is buzzed inside, leaving us in the care of the two remaining grunts as we await our fate."

    "Desperately, I wish I could talk to Luna or Nevin openly, but I simply can't."

    "We need to continue rolling with the punches until we know for certain that we are alone."

    play snd "sounds/door_open_04.ogg"

    "Before long, the door opens once more."

    jin "Okay, come on in guys."

    play snd "sounds/footsteps_two_sneakers_01.ogg"

    scene black with diss

    scene vargas_office at hs 
    
    show letterbox

    stop music fadeout 3.0
    
    with diss

    "We walk into an ornate office with big bay windows overlooking the commercial district."
    
    "The whole thing, from the grandeur of the view to the expensive wooden desk, projects a somewhat sophisticated aura that is severely undermined by the man sitting behind it, the pack of goons standing around him and the large Nox logo on the wall."

    play music1 "music/warning_level_3.ogg" fadein 2.0

    scene vargas_office at bgz 
    
    show vargas nox neutral at vcz
    
    with diss

    "This must be that Vargas that Jin was speaking of..."

    "He's an intimidating, fit, muscular man who looks slightly older than myself."

    "Although he's wearing a rather fancy-looking shirt, the fact that it is half-unbuttoned and his sleeves are rolled up, exposing his chest and arm tattoo respectively, paints a very different sort of picture."

    "His rough, unshaven face, scarred eyebrow and slimy smile seal the deal."

    "There is no doubt what sort of man this is."

    "He's a criminal."

    "The worst sort."

    "In case there was any doubt, he even hung the damn Nox logo on his wall, as if he doesn't care if people know or not..."

    "And even without any of those hints, there's no way a nobody like him could have accrued this kind of wealth without doing unspeakable things."

    "The kind of things I pledged my life to put an end to."

    "But here I am, having to swallow my pride and get into his good books..."

    show aiden nox_01 look at off

    qa "Let's give this a try..."

    a "Hello, Vargas Koldrak, I presu--"

    "He holds up his hand, clearly in an attempt to silence me."

    "I heed his gesture."

    play snd "sounds/chair_getting_up_01.ogg"

    scene vargas_office

    show luna nox_01 neutral at pos2

    show nevin nox_01 look at pos4

    show jin base neutral at pos6

    show vargas nox neutral at pos8

    show aiden nox_01 look at off

    with dis

    "Getting up from his seat, he silently looks us up and down."

    "Then, turning to Jin, he points at us."

    $ persistent.vargas_revealed = True

    $ update_status("vargas_relationship", _("SWORN ENEMY"))

    $ unlock_codex_entry("character_vargas_koldrak")

    stop music1 fadeout 0.5

    show jin surprised sweat

    show nevin surprised

    play music "music/nox_clock.ogg" fadein 2.0

    v upset "What the fuck, man?!" with vpunch

    "His sudden look of frustration and loud, gruff tone of voice takes me aback."

    "I'm not the only one, either."

    "Jin seems utterly terrified."

    "This doesn't seem like a good start..."

    "I glance at Luna, who seems at high alert."

    "She understands this as well as I do. This guy seems unstable..." 
    
    "He certainly isn't someone we can take it easy around."

    jin "W-what, boss?"

    show vargas happy

    "All of a sudden, Vargas' anger turns to a raucous joy."

    stop music fadeout 1.0

    show luna surprised

    show nevin nervous

    $ update_status("emotional_status", _("DETERMINED, ANNOYED"), notify=False)

    v "You didn't tell me that the delivery girl was such a fine piece of ass!"

    play music "music/false_sky.ogg" fadein 2.0

    qa "What the hell?!"

    qa "That's what that outburst was about?!"

    scene vargas_office at bgz

    show letterbox

    show luna nox_01 surprised at cz

    with diss

    "I sneak another peek at Luna and catch her in a rare moment of shock."

    "She doesn't seem angry yet, although I know that will come."

    "No way she would ever take a comment like that lying down."

    "She's earned too much respect for that kind of thing to go uncommented on."

    "Instead, for now, she's staying silent, attempting to compose herself."

    "Meanwhile, Jin seems utterly relieved, realizing that his life doesn't seem to be in danger."

    show jin base surprised sweat at off

    jin "Oh, sorry man, I figured that--"

    show luna serious

    show jin base neutral at off

    show vargas nox smirk at off

    v "Thought you'd keep it as a surprise?"

    "Vargas says, both interrupting him and turning his gaze back to Luna at the same time."

    v smile "It's okay. I forgive you."

    scene vargas_office

    show luna nox_01 serious at pos2

    show nevin nox_01 look at pos4

    show jin base smile at pos6

    show vargas nox neutral at pos8

    show aiden nox_01 look at off

    with dis

    v  happy "It's always nice to have little surprises like this in life."

    "Falling silent and still, he shamelessly stares right at my wife for a few moments, before shaking himself back to life."

    v "Sorry boys, got stuck there for a second. Was letting my imagination run wild."

    $ update_status("vargas_feelings", _("Hell... I had low expectations, but he's even worse than I imagined. What an absolute scumbag. Taking him down is going to be a pleasure."))

    "Him and the rest of his entourage burst into laughter."

    "There's no wondering what he was thinking of..."

    show jin smile -sweat

    qa "How fucking humiliating..."

    qa "A piece of shit like this guy, openly fantasizing about my wife... and what do I have to say for it?"

    qa "I can't exactly tell him to fuck off..."

    qa "I certainly feel like it though..."

    qa "What I'd give to shove my gun in his ass right now and pull the trigger."

    qa "Laugh it up while you can, asshole. I am not going to forget this..."

    qa "And, more dangerous for you, neither is Luna..."

    qa "When she gets her hands on you, it's going to be curtains..."

    v "Man, can't wait to get my hands on--"

    stop music fadeout 0.2

    show luna surprised

    show nevin surprised

    show jin surprised

    show vargas neutral

    a upset "Okay, that's enough!" with vpunch

    "I shout out without even thinking. It just came out."

    "I tried not to, but that was getting to be too much."

    "Everyone in the room immediately falls silent."

    "The grunts all look at me stunned and Vargas almost seems confused."

    play music "music/decaying_ruins.ogg" fadein 2.0

    v "Enough what? Do you have a problem?"

    l serious "Why wouldn't he have a problem? You're treating me like a piece of meat. Like I'm not even here!"

    l "What the hell is wrong with you?!"

    "Vargas looks back at his grunts for a moment before turning to Luna, seeming even more confused than before."

    v happy "Nothing? I'm just being honest."

    v "Would you rather I pretend you look like an ugly bitch?"

    l "I'd rather you say nothing about that stuff!"

    v "Hahaha..."

    v "Yeah, good one."

    v neutral "Look, what's your name?"

    l "Luna..."

    "The venom dripping from that one word is nakedly obvious, but Vargas goes on as if he doesn't notice it at all."

    v "Okay Luna, I don't know what you've heard about me, but I tell it like it is."

    v "I'm not into the fucking bullshit a lot of these other jackass crime lord bosses are into."

    v "In my crew, I give it to you straight."

    v "Some people respond well to that. Some don't. I don't give a shit."

    v "And I especially don't give two shits what two new fucking turncloak recruits from Zeph's flaming garbage pile of an organization think, got it?"

    "Luna doesn't respond at all. Instead, she stares at him, right in his eyes with a look that seems as though it could pierce a man's soul."

    v "Oh, so that's how it is..."

    play snd "sounds/footsteps_two_vargas_01.ogg"

    scene vargas_office at bgz

    show letterbox

    show luna nox_01 serious at vlz

    show vargas nox neutral at vrz

    show aiden nox_01 look at off

    with dis    

    "Vargas shakes his head, walks around his desk and approaches Luna."

    v "I've met your type before."

    v "Waltzing in here, walking tall like they own the place and deserve respect."

    v "If you want respect, you're going to have to earn it, like I have."

    v "Got it?"

    "By now, Vargas is deep within Luna's personal space."

    "They stare at each other, noses almost touching until..."

    hide letterbox

    show luna nox_01 serious:

        xalign 0.3 yalign 0.2 zoom 0.8         
        anchor (0.5, 0.15)
        hit("right", 0.2, final_pos=0.3)

    stop music

    play snd "sounds/punch_08.ogg"

    play snd1 "sounds/impact_wood_01.ogg"

    hide vargas

    with vpunch

    "Luna decks him right in the face, sending him reeling back onto his desk."

    play music "music/nox_tension.ogg" fadein 3.0

    qa "Hell yes!"

    "While such an action is just about the worst thing Luna could have done given the circumstances, I have nothing but respect for it."

    "This pompous asshole of a guy deserves so much worse than this." 
    
    "Unfortunately, that good deed certainly doesn't go unpunished."

    play snd "<silence 0.3>"

    queue snd "sounds/cock_submachine_01.ogg"

    play snd1 "<silence 0.6>"

    queue snd1 "sounds/cock_submachine_02.ogg"

    play snd2 "sounds/cock_shotgun_01.ogg"

    play snd3 "<silence 0.6>"

    queue snd3 "sounds/cock_pistol_01.ogg"

    "Immediately the grunts leap into action, drawing their weapons."

    show jin base surprised sweat at off

    jin "What the fuck, guys?!"

    grunt "On the ground, now!!!"

    play snd "sounds/body_floor_01.ogg"

    "Nevin immediately follows orders, dropping."

    "I, like Luna, stay standing."

    "If this is how it ends, I'll stand with her."

    "However, it doesn't quite come to that..."

    show vargas nox happy at off

    v "HA!!!"

    "Vargas laughs loudly as he pops back off his desk."

    scene vargas_office

    show luna nox_01 serious at pos4

    show vargas nox happy at pos8

    show aiden nox_01 serious at off

    show letterbox

    with dis    

    "Massaging his jaw, he practically giggles as he takes another look at Luna."

    v "Damn..."

    v "Never had that one before."

    $ update_status("vargas_feelings", _("I really should have kept my cool, but hearing him talk about me in that way... He deserved getting hit... He deserved worse..."))

    v "What did you say your name was again? Looney?"

    l "Luna."

    v "Right, that was it. How could I forget..."

    v "I guess you knocked it right out of my mind."

    v "Don't worry, I won't ever forget that name again."

    v "First woman who's ever shown me that kind of spine before... or man, for that matter."

    v "Wow... What a temper on you."

    v "That packed a punch. Like a supernova going off in my face."

    v "Respect to you, supernova."

    l "Ugh..."

    v "Oh damn, she doesn't like that."

    v neutral_evil "Shouldn't have let me know that, supernova."

    l "Whatever..."

    show vargas happy at pos7 

    play snd "sounds/package_01.ogg"

    "Chuckling to himself, he reaches for the package on his desk."

    v "So, you guys are the ones who have been contacting my friend Jin here."

    l "Yes..."

    a "It was me."

    v "Right on..."

    v "And you guys were hoping to jump ship, right?"

    a "Yup."

    v "We don't normally let random assholes join up."

    v "We run a tight crew over here."

    v "To be 100%% fucking honest with you, I had a real mind to just take your little gift here and show you the door."

    v "Then maybe show you our basement if you had a problem with it."

    v "But I gotta say, I've taken a little shine to you..."

    v "Or rather, your little beauty over there."

    v "She's got big fucking balls on her."

    v "And before you punch me again, I mean that as like a... metaphor, or whatever you call it."

    show vargas neutral

    l "I know... I was thinking of punching you again anyway."

    v "Don't push your luck, supernova. Once was new and exciting."

    v "Twice... Well, it could get tiring very quickly."

    v "Anyway, look, I'll just say that little incident was us getting off on the wrong foot."

    v "Us getting to know each other. Our quirks. You know how it can be when two hotheads meet each other for the first time, Nova."

    v "It can be fireworks."

    stop music fadeout 3.0

    v "It wasn't exactly the fireworks I was hoping for, but they were entertaining enough for me to give you a second look."

    play music1 "music/false_sky.ogg" fadein 3.0

    v "Between that surprise and this gift here, I'm willing to give you guys a chance to prove yourselves."

    v "With the turf war coming up, some extra help definitely wouldn't be bad."

    v "Do well for yourself and you'll find yourself well-rewarded."

    v "As these boys can tell you, I can be generous when I'm happy."

    v "Wouldn't surprise me if you managed to earn a hell of a lot more than you did under Zeph, that cheapskate prick."

    v "Not that you have much choice these days."

    v "Lucky for you, the ball was already rolling before he got what was coming to him."

    v "I'm not taking any more of his fucking refugees."

    v "We got enough mouths to feed and loot to split."

    v happy "I take it you guys are still interested? No hard feelings, right?"

    scene vargas_office

    show luna nox_01 serious at pos4

    show vargas nox happy at pos7

    show nevin nox_01 look at pos1

    show jin base neutral sweat at pos9

    show aiden nox_01 look at off

    with diss

    "Luna, Nevin and I all exchange looks and nod."

    a "Yeah, we're good."

    v "Uh huh..."

    l "Yes, we should be fine."

    v "Perfect!"

    jin "So we're good?"

    v "Yeah, I'd say so."

    jin "So... That thing you were saying before?"

    v neutral "Nah, we're good. I changed my mind."

    jin "O-okay..."

    jin -sweat "Shall I show them around?"

    v "Yeah, good call."

    jin "A-alright guys, follow me and--"

    v "Actually, wait a second, Jin."

    v "I'll show them around myself."

    jin "Boss?"

    v "Did I stutter?"

    jin sweat "No, it's just you don't usually--"

    v "I know. I don't give a fuck. I decided I wanna stretch my legs, so I might as well be useful while I'm at it."

    v "You get their quarters ready, okay?"

    jin "Okay..."

    v happy "Alright then... Let's head out!"

    stop music1 fadeout 2.0

    scene black with cor_in

    pause 1.0

    play music "music/the_complex.ogg"

    scene nox_hallway_red
    
    show letterbox
    
    with cor_out

    "Once in the hallway, Vargas takes the lead and begins guiding us throughout the base."

    show vargas nox happy at pos5

    with dis

    v "Don't mind the entourage."

    "He says, referring to the coterie of guards following closely behind us, arms at the ready."

    v "You guys are still unproven, after all."

    show luna nox_01 neutral_serious at off

    l "Worried we are going to stab you in the back?"

    v "Well, yeah? It would hurt like a bitch."

    v "But it would be a hell of a lot worse for you, so I'd rest easy."

    scene black with diss

    play amb "ambient/laboratory_01.ogg" fadein 1.0

    scene nox_lab 
    
    show letterbox

    show luna nox_01 neutral_serious at off

    show vargas nox happy at pos5

    show nevin nox_01 look at off

    show aiden nox_01 look at off
    
    with diss

    v "Here we are..."

    v "The lifeblood of our operation."

    "Vargas says upon entering the lab."

    "Throughout the massive room are dozens of scientists tinkering at their workstation, processing a variety of chemicals."

    "It's hard to tell, but I'm pretty sure these scientists in particular seem to be processing recreational chems."

    qa "Darn..."

    qa "Was hoping it might have been weapons research. Might have given me a place to start looking."

    v "We got three labs like this."

    l "That many?"

    v "Yeah, we just finished building the third one last year."

    v "What can I say, demand is booming."

    v "Rec-chems, war-chems, med-chems, we do them all."

    qa "Bingo."

    qa "They do have a war-chem lab here after all."

    qa "That's where I should start my search."

    $ unlock_codex_entry("lore_flamer")

    v "This lab is mostly Flamer."

    qa "Wonderful... Highly addictive and dangerous..."

    qa "I should burn this place to the ground."

    qa "But for now, I play along."

    a "It's good business?"

    v "Amazing. That shit has great margins and is cheap as fuck to make."

    v "In fact, to be honest with you, the only issue is that we got more chems than we can move."

    v "Not enough demand in our territory."

    v "Which is where you guys are going to come in."

    n "You want us to distribute it?"

    v "Hell no. We got all the pushers we need."

    v "What we need is territory."

    l neutral "I see."

    a "So you want some extra muscle taking over Zeph's old turf?"

    v "Definitely. That's just to start though."

    v "We're taking a bigger slice of the pie than that."

    a "You want to go to war?"

    v "Heh... You say that like the war hasn't started."

    v "It might not be guns blazing, but the other bosses know what's up."

    v neutral "Tens and Kama have been probing us for weeks, trying to step on our toes. They're idiots though."

    v "Spleegic's the only one that's been taking this as serious as I have been."
    
    $ unlock_codex_entry("character_tens")

    $ unlock_codex_entry("character_kama")

    $ unlock_codex_entry("character_spleegic")

    v "Actually poaching and recruiting the good ones."

    v "He sees the big picture."

    v "Only a matter of time before we take things to the next level."

    v "You guys ready for that?"

    a "No doubt."

    qa "Although it might not end exactly how you want it to..."

    v happy "Good. I have high hopes."

    l "You won't be disappointed."

    show vargas seductive

    "He smirks."

    v "I better not be..."

    play snd "sounds/footsteps_two_sneakers_01.ogg"

    scientist "Uh... Boss? Can I run something by you?"

    show vargas neutral

    "One of the scientists says, approaching our group."

    "Vargas rolls his eyes."

    v "Can it wait?"

    scientist "Well..."

    v "Okay, okay. I get it."

    v "Give me a sec, gang. Our chief lab rat has been out for a few days and this whole place is already falling apart."

    play snd "sounds/footsteps_two_sneakers_02.ogg"

    scene nox_lab with dis

    "Vargas, clearly not pleased by the situation, leaves us to go deal with his subordinate."

    "As we wait around, I try to scan the room for as many potential points of interest as possible."

    "Ways in and out, weak points, and such."

    show luna nox_01 neutral_serious at off

    show nevin nox_01 look at off

    show aiden nox_01 look at off

    n "This place is well-run."

    l "Yes, it's quite disconcerting, isn't it?"

    show rogue base neutral at off

    grunt "What do you mean?"

    "One of the grunts pipes up, intruding in our conversation."

    a "She means that compared to Zeph's lab, this is..."

    n "It would be at home in any of the major med-corps."

    "The grunt shrugs."

    grunt "If you say so."

    grunt "I don't know anything about them. I do know that they spent a hell of a lot of money on this shit though."

    n "It shows..."

    "Vargas might be a newcomer to the game, and somewhat weak in terms of muscle, but he's clearly very ambitious..."

    qa "Better snuff out his flame before it gets too bright..."

    play snd "sounds/footsteps_two_sneakers_03.ogg"

    scene nox_lab at bgz
    
    show letterbox

    show luna nox_01 neutral at off

    show vargas nox neutral at vcz

    show aiden nox_01 look at off
    
    with diss

    v "Alright guys, done with that bullshit."

    v "Some people just need to be told what to do all the damn time, I swear..."

    v sigh "Think for yourself once in a while... Hell..."

    v happy "Anyway, what do you think?"

    a "Impressive."

    v neutral "I was asking her."

    "Luna, not particularly enjoying being the center of attention, shrugs."

    l "It's more than adequate."

    v happy "Heh..."

    v "That's one way of putting it."

    v neutral "Anyway, it doesn't matter what you think, you won't be spending much time here at all. You'll be out on the field, mostly."

    v "When you aren't... That's on you. There's plenty of shit here to keep you occupied."

    v look "We just have one rule."

    a "What's that?"

    v neutral "Don't sample the product."

    qa "Really?"

    v "I need you sharp."

    v happy "Not saying you can't party. Don't worry, we'll fucking party when the time's right."

    v neutral "But even then, you don't want to touch this stuff."

    v "Will fucking burn your brain, trust me."

    l "So you sell a product you wouldn't consume yourself?"

    v "One-hundred percent."

    v "This shit is for the fucking burnouts."

    v "I'm not a burnout."

    v "You aren't either. I don't have to ask, you still have all your teeth."

    v "Anyway, even if you're curious. Don't."

    v "Fastest way to get fired."

    v "And you don't want to see how we fire people."

    qa "I get the feeling it might be literal..."

    qa "This guy doesn't exactly seem like the subtle type."

    v "Anyway, whatever to all that bullshit. You guys don't really seem like you are into that kinda shit anyway."

    v "Just figured I'd say it, just because."

    v happy "Now that that's out of the way, let me show you the facilities."

    v "It's not just our labs that are state-of-the-art."

    v "I got us set up nice..."

    v "Follow me."

    stop amb fadeout 2.0

    scene black with cor_in

    pause 1.0

    scene nox_hallway_white
    
    show letterbox

    show vargas nox neutral at pos5

    with cor_out

    "All of us follow him down a few floors to a less secure part of the building."

    "A lot more Nox members are dressed casually, talking with each other as if they are off duty."

    "We pass by lounges full of people relaxing and hanging out."

    "The whole atmosphere of the building feels a lot more like a tech-corp than some of the seedy dens of scum that I've been in."

    play snd "sounds/footsteps_two_sneakers_04.ogg"

    scene black with dis

    play amb "ambient/treadmill_01.ogg" volume 0.8 fadein 1.0

    play amb1 "ambient/cable_machine_01.ogg" volume 0.8 fadein 1.0

    play amb2 "ambient/punching_bag_boxing_01.ogg" volume 0.8 fadein 1.0

    scene nox_training_room

    show letterbox

    show luna nox_01 neutral_serious at off

    show vargas nox happy at pos5

    show nevin nox_01 look at off

    show aiden nox_01 look at off

    with dis

    "Turning off from the main hall, we find ourselves in a massive gymnasium."

    v "This is my second-favorite spot in the place. The training room."

    "Truth be told, I can see why."

    "It's a nice training room. Even better than the one at AEGIS HQ."

    qa "What the hell?"

    qa "You hate to see crime paying off..."

    "I can't help but be a little jealous seeing all the NOX members exercising with what seems like brand new equipment."

    v "You guys like sparring?"

    a "Yup. Gotta stay sharp."

    v "Exactly."

    v "You can't be slow at all out there on the field. AEGIS will fuck you up if you're lucky, and if you're unlucky it'll be some other syndicate shithead."

    l "Hm?"

    v "What? You seem surprised."

    l "I am a little."

    l "You go out on the field?"

    v "All the time. I ain't sending one of my dudes on a suicide run I'm not willing to go on myself." 
    
    v "What's life without a little danger and thrill?"

    l "You seek out those things?"

    v neutral_evil  "Hell yeah! I love a good fight! Why else you think I got in the game?"

    l "Isn't that dangerous?"

    v "Yeah, so?"

    l "You're putting your whole organization at risk when you do that."

    show vargas happy

    "He chuckles."

    v "What, you think I'll get picked off like that coward Zeph?"

    v "Nah. That ain't me. Trust me."

    l "Sure..."

    v "You don't seem impressed... Hehe..."

    l "I'm just surprised..."

    v "Nah, you're pissed."

    v "But it's all good. You're just ignorant."

    l "How so?"

    v "You've never actually seen me in action."

    l "I suppose that's true."

    v "If you want, we can throw down right now and you can see for yourself."

    a "I don't think that will be necessary. We're going to have plenty of opportunities, won't we?"

    "Luna nods, clearly excited about the prospect of fighting him in a very different circumstance."

    l "I hope to see you in action soon."

    show vargas neutral_evil

    "Vargas smirks."

    v "Heh... Soon enough, soon enough."

    v happy "Anyway, if you ever are pissed at me, you can take it out on me here..."

    v "Well, you can try, anyway..."

    v "Now follow me. I'll show you where you're going to end up when you fail."

    stop amb fadeout 1.0

    stop amb1 fadeout 1.0

    stop amb2 fadeout 1.0

    scene black with diag_in

    scene nox_medbay_open

    show letterbox

    show luna nox_01 neutral_serious at off

    show vargas nox happy at pos5

    show nevin nox_01 look at off

    show aiden nox_01 look at off

    with diag_out

    n "Ah... I see... The med-bay..."

    n "I didn't really plan on challenging you to a fight, so I will hopefully avoid this place..."

    v neutral "I was talking about the other two."

    v happy "If an egghead like you challenged me, you'd probably just end up in an early grave instead."

    "It's certainly insulting, but probably true."

    "Nevin is not exactly a heavyweight fighter, and Vargas... He seems like a killer."

    n nervous "R-right..."

    n "Anyway, this place seems well equipped."

    v "I wouldn't have it any other way."

    v "Gotta get patched up after a tussle."

    v happy "Don't want this beautiful face to get all scarred up like Jin's, right boys?"

    "A few of his entourage of grunts burst out laughing."

    v "Also, sometimes I come by for a check-up, just for fun."

    scene nox_medbay_open at bgz with dis

    "While I'm initially puzzled by the comment, one look at the med-bay staff quickly puts that mystery to bed."

    "It seems to be employed exclusively by young, thin, busty women."

    "While they certainly aren't as pretty as Luna, I have to admit that they are attractive."

    "Not wanting to cause any jealousy issues, I quickly avert my gaze."

    scene nox_medbay_open

    show letterbox

    show luna nox_01 neutral_serious at off

    show vargas nox happy at pos5

    show nevin nox_01 look at off

    show aiden nox_01 look at off

    with dis    

    "Luna, noticing my unsubtle efforts, smiles."

    v "Oh, find that funny, huh?"

    "Vargas asks, probably thinking she was reacting to him."

    l "Uh... Yes?"

    "She plays along."

    v "Wow, you really do have a little spice to you... Nice..."

    v seductive "You'll fit right in."

    "I really do not like the look he's giving her right now..."

    "Although it's just a misunderstanding, he's practically drooling while looking at her. It's honestly kinda pathetic..."

    "He isn't stopping too... This is kinda getting creepy..."

    a "So, where to next?"

    v neutral "Huh? Oh right... Kinda got distracted by all the pretty sights..."

    "Luna, clearly unimpressed, shakes her head and starts heading towards the door."

    scene black with cor_in

    pause 1.0

    scene nox_hallway_red 
    
    show letterbox

    show luna nox_01 neutral_serious at off

    show vargas nox neutral at pos5
    
    show nevin nox_01 look at off

    show aiden nox_01 look at off

    with cor_out

    "As we make our way through the hallway to our next stop on the tour, Vargas points out a particularly solid-looking door."

    v "There we have the security office."

    v "I suggest you don't try to get in there until you get the right security clearance, even by accident."

    v "The security team might take it the wrong way and burn a hole through your skull."

    n "Y-yes... We would hate to have that happen."

    v "Yeah, that would be a real damn shame..."

    v "Anyway, let's keep going."

    l "Yes, please..."

    play snd "sounds/footsteps_two_sneakers_07.ogg"

    scene nox_hallway_red at bgz

    show aiden nox_01 look at off

    show nevin nox_01 look at cz

    with dis

    "Vargas and Luna start walking, but I notice Nevin linger near the security door."

    a "Everything okay?"

    n "Yeah, I'll be a sec. You can go on ahead."

    scene nox_hallway_red at bgz

    show letterbox

    with dis

    menu:

        "..."

        "Wait for Nevin.":

            $ ep_01_wait_for_nevin = True

            scene nox_hallway_red at bgz

            show aiden nox_01 look at off

            show nevin nox_01 look at cz

            show rogue base neutral at off

            with dis

            a "Nah, it's okay, I'll wait for you."

            show nevin nox_01 nervous at cz

            n "O-okay..."

            scene nox_hallway_red

            show aiden nox_01 look at off

            show nevin nox_01 surprised at pos4

            show rogue base neutral at pos6

            with dis

            grunt "What's going on here?"

            "One of Vargas' grunts asks, hand hovering over his pistol."

            n "It's nothing, I just realized my boot wasn't secure, just going to tighten it."

            grunt "Do it then, we gotta move."

            n "O-of course!!!"

            hide nevin with Dissolve(0.5)

            "Nevin bends down to secure his boot, but that's not all he does." with Dissolve(0.5)

            "I see him subtly tap his wrist comm."

            "He's up to something, that's for sure."

            show nevin nox_01 neutral at pos4

            n "Okay, done, let's go!"

            grunt "About time."

            play snd "sounds/footsteps_two_sneakers_07.ogg"

            scene nox_hallway_red at bgz

            show letterbox

            show aiden nox_01 look at off

            show nevin nox_01 look at cz

            with dis

            "As we start catching up to Vargas, Nevin leans in close and whispers."

            n "A full MAGS sweep network... A central helix database... These guys are set up nicely..."

            a "Damn..."

            qa "That's impressive..."

            qa "How the heck did they get their hands on this tech?"

            qa "Even more importantly, how are we going to accomplish our mission while working around it?"

            qa "We'll have to see..."

            m "Hey boys..."

            "A sultry voice calls out in our direction, pulling me back to reality."

            n surprised blush_04 "H-hey there!"

            "Before I even see what Nevin is looking at, I notice his eyes are practically popping out of his skull."

            scene nox_hallway_red

            show letterbox

            show aiden nox_01 look at off

            show nevin nox_01 surprised blush_04 at pos4

            show girl base neutral at pos6

            with diss

            qa "Oh... That makes sense..."

            qa "I should have expected someone like Vargas would have women like that parading around his base."
            
            wew "Never seen you guys around these parts. Who are you? New recruits?"

            n "Yes, ma'am. Just getting the tour right now."

            wew "Heh... Ma'am..."

            wew "You're cute!"

            $ update_status("emotional_status", _("UNCOMFORTABLE, ANNOYED"), notify=False)

            $ update_status("vargas_feelings", _("Did he really just do that?! The nerve of this guy! I should break his hand for that and teach him a lesson!!! But... No... I need to keep my cool..."))

            n nervous "I am?"

            n happy "I mean... Thanks!!!"

            wew "Hahaha... Adorable."

            wew "Well, if you ever want a little release, let me know."

            wew "It's what I'm here for."

            n surprised "R-really?"

            wew "Absolutely..."

            wew cheeky "First ride's free."

            "She winks at Nevin before flashing me a nice bright smile."

            show nevin look

            wew "Same offer for you, handsome."

            "Instantly, I shake my head."

            a nervous sweat "That's alright, I'm taken."

            wew surprised "Oh really? Damn... Haha..."

            wew "I was looking forward to you."

            wew neutral "She must be a lucky woman."

            a neutral -sweat "Not as lucky as I am."

            wew "Heh... Charming too..."

            wew "She really is lucky."

            wew "Well, even so, look me up if you're feeling frisky, fellas."

            n "W-will do!"
            
            a smile "Thank you for the offer, but again, no thanks."

            wew "Tsk... You're no fun."

            show rogue base neutral at off
            
            grunt "If you're looking for fun--"

            "The grunt escorting us finally inserts himself into the conversation, but the busty woman has other ideas."

            wew surprised "Shut up, Charlie. You know you're cut off."

            grunt "Come on, I was just--"

            wew "You're cut off. End of story."

            wew neutral "Anyway... I'm sure Vargas doesn't want you to fall too far behind, so you fellas better get a move on."

            "Giving Nevin one last wink, she steps out of our way."

            wew cheeky "I'll be seeing you soon."

            n embarrassed "Y-yeah..."

            a look "Later."

            play snd "sounds/footsteps_single_heels_09.ogg" volume 0.5

            queue snd "sounds/footsteps_single_heels_08.ogg" volume 0.5

            scene black with dis

            scene nox_hallway_purple with dis

            "With a parting wave from the woman, the three of us hurry off towards Vargas and Luna, who are all the way down the hall by now."

            scene nox_hallway_purple at bgz

            show aiden nox_01 look at off

            show nevin nox_01 surprised at lz

            show rogue base neutral at rz
            
            with dis

            n "Gosh she was hot..."

            grunt "Yeah, a real fine piece of ass..."

            grunt "Into the sickest shit, too..."

            n "R-really?"

            grunt "Yeah... Mean as hell in the sack..."

            n sweat "N-no way..."

            grunt "Yeah way... But the second you pay back some of that violence, she pulls that victim crap..."

            grunt "It was just a drop of blood, she was being a pussy..."

            a "I see..."

            qa "Good to know that Vargas' men are as terrible as I imagined they might be."

            scene nox_hallway_purple with dis

            "Just the thought that I left Luna alone with Vargas and a few of his other men makes me feel uneasy..."

            "Although, that being said, if that other woman can stand up to them, Luna could do way worse."

            "I'm sure the second one of them laid a hand on her, she'd have torn it off."

            scene nox_hallway_purple

            show luna nox_01 neutral_serious at pos2

            show vargas nox neutral at pos4
            
            show nevin nox_01 surprised at pos6

            show aiden nox_01 look at off

            show rogue base neutral at pos8

            with dis

            v "What took you guys so long?"

            "Before we can answer, the grunt does in our stead."

            grunt "One of your disgusting whores rolled out the red carpet for them."

        "Go on ahead.":

            $ ep_01_insert = True

            show aiden nox_01 look at off

            a "Okay, sure."

            play snd "sounds/footsteps_two_sneakers_10.ogg"

            scene black with dis

            label s03_insert_01:

                if _in_replay:

                    play music "music/the_complex.ogg" fadein 1.0

                scene nox_hallway_purple

                show letterbox

                show vargas nox happy at off

                show luna nox_01 serious at off

                with dis

                "Not wanting to leave Luna alone with that thug, I hurry up and catch up to them."

                v "So, Luna, what do you think of my operation so far? Impressed?"

                l "It's... elaborate..."

                v neutral "That doesn't sound like you're impressed."

                l "I wouldn't say that."

                v happy "Heh... You really do play it cool, don't you?"

                stop music fadeout 1.5

                play music1 "music/nox_tension.ogg" fadein 3.0

                show cg03_insert_01:
                
                    zoom 0.52
                    align (0.5, 0.5)
                    
                with Dissolve(1.5)

                $ update_status("emotional_status", _("UNCOMFORTABLE, ANNOYED"), notify=False)

                $ update_status("vargas_feelings", _("Did he really just do that?! The nerve of this guy! I should break his hand for that and teach him a lesson!!! But... No... I need to keep my cool..."))

                "Out of nowhere, Vargas casually places his hand on the small of her back."

                qa "What the fuck does he think he's doing?!"

                qa "He can't do that!"

                qa "Piece of shit!"

                show cg03_insert_01:
                
                    zoom 0.25
                    align (0.5, 0.5)
                    
                with diss

                show aiden nox_01 upset at off

                a "Vargas."

                "I say to him, sternly."

                "He doesn't turn around though. Instead, he keeps talking to Luna."

                v "Wait until you see some of the stuff I got--"

                l "What the hell do you think you're doing?"

                v "Heh... What am I doing?"

                stop music1 fadeout 1.0

                l "Get your hand off me."

                v sigh "Okay! Geez..."

                play music "music/ticking_tension_02.ogg" fadein 3.0

                scene nox_hallway_purple

                show letterbox

                show vargas nox sad at pos6

                show luna nox_01 serious at pos4

                with dis

                "He does as she asks and takes a step back."

                v "You know, I'm starting to get the impression that you don't like me very much."

                l "I..."

                v sigh  "It's okay. You don't need to."

                v "I don't like most of my flunkies."

                v neutral "But I don't need to like them, you know why?"

                l neutral_serious "Why?"

                v "Because they earn."

                v "Because they do their jobs."

                v "And we all make a shit-ton of money."

                v happy "Who cares if we like each other? That's what I say."

                l "Well... I'm glad we're clear..."

                v "Me too."

                v "Like I said in my office, I like your spunk."

                v seductive "It makes you so fun to tease..."

                "I can tell that last comment pisses Luna off, but she bites her tongue."

                show vargas happy

                "Vargas notices as well and smiles."

                v "Heh... We're going to get along great, I can tell..."

                v "Just give it time."

                l "Sure..."

                qa "The nerve of this guy..."

                play snd "sounds/footsteps_two_sneakers_08.ogg"

                stop music fadeout 2.0     

                scene nox_hallway_purple

                show luna nox_01 neutral_serious at pos2

                show vargas nox neutral at pos4
                
                show nevin nox_01 surprised at pos6

                show aiden nox_01 look at off

                show rogue base neutral at pos8

                with dis
                
                n "S-sorry!"

                "Nevin practically shouts as he rushes to our side."

                play music "music/the_complex.ogg" fadein 2.0 

                v "What took you guys so long?"

                grunt "One of your disgusting whores rolled out the red carpet for him."

                $ persistent.unlocks.add("s03_insert_01")

    v happy "Hahaha..."

    show nevin look

    v "I'm guessing I know the one based on your salty-as-fuck reaction, Charlie."

    grunt "Maybe..."

    v "Dude, get over it. Your fault for being a dumbass."

    grunt "Whatever..."

    v sigh "Whatever..."

    "Vargas repeats in a mocking tone."

    v neutral "I swear, sometimes I work with children."

    v happy "I've got a good feeling about you guys though."

    v "Made of better stuff than some of these rejects."

    "The grunt sighs, looking at the ceiling and the floor. Basically anywhere but Vargas."

    v neutral "...Fuck, Charlie. I'm just kidding."

    v happy "Why you being all thin-skinned about this?"

    grunt "Nah boss, you're right..."

    v "No shit..."

    v "Now let's get to the mess. We're almost done."

    l "Good."

    v "Heh... Still all business with this girl."

    v "That's cool... No worries."

    v "It's like I said, as long as you earn, I don't give a fuck."

    v "Anyway, let's go. We have a last couple places to get to."

    $ renpy.end_replay()  

    play snd "sounds/footsteps_two_sneakers_11.ogg"

    scene black with cor_in

    scene nox_cafeteria with cor_out

    "Vargas brings us to the mess hall, as promised."

    "At first glance, it looks somewhat similar to the one at AEGIS HQ. Maybe some more seating."

    "However, upon closer inspection, I realize there is something quite different."

    show luna nox_01 neutral_serious at off

    show vargas nox neutral at pos5

    show aiden nox_01 look at off

    with dis

    a "You serve alcohol here?"

    show vargas shocked

    "Vargas looks at me with genuine shock."

    v "Why the hell wouldn't we?"

    v "Are you telling me Zeph didn't?"

    "Realizing that I don't actually know whether he did or not, I try to think of a lie to get me out of the situation."

    a "Oh, it's not that, I'm just surprised that you do, given what you said before about needing us sharp."

    show vargas neutral

    "He scoffs."

    v "Come on man. There's a big fucking difference between a couple drinks to loosen up after a fight and flaming out."

    v "Don't pretend otherwise."

    a "You're right, boss. I got you."

    "My gambit to get back in his good graces doesn't go unnoticed."

    v neutral_evil "Heh... You think I didn't notice that \"boss,\" you brown noser?"

    v "Maybe you can take some notes from him, Nova."

    l pout "My name isn't Nova, you idiot..."

    v happy "Really? Does this look like a face that cares?"

    l "Ugh..."

    "Luna rolls her eyes in disgust, but that doesn't seem to bother Vargas."

    v "Oh come on! I was kidding."

    v "Don't you know by now that I'm kinda into that attitude?"

    v "I'd be disappointed if you dropped it so easily."

    v "It's all part of the game, right?"

    l upset "Whatever..."

    v neutral_evil "I love it when they play hard to get..."

    "Vargas says out loud, perhaps to me, perhaps to himself."

    v neutral "Anyway, bottom line, yeah we serve alcohol."

    v "Not to say the best stuff."

    v happy "I save that for myself and some of my top men."

    v "A special reward for my best earners, you can say."

    v "Gives guys something to shoot for."

    v "Or ladies, you know. I don't mind sharing with them either."

    v "I kinda like sharing with them more."

    "Luna doesn't dignify that with a response."

    v "Until you earn anything better though, you can eat here."

    a "Sounds good."

    v neutral "Alright, one last stop."

    scene black with cor_in

label s04:

    if _in_replay:
        play music "music/the_complex.ogg" fadein 2.0    

    scene nox_bedroom 

    show luna nox_01 neutral at pos3

    show jin base neutral at pos7

    show vargas nox neutral at pos5

    show aiden nox_01 look at off

    if _in_replay:
        with dis
    else:
        with cor_out

    v "Hell... Jin, this is all you could find for them?"

    jin surprised "We don't have that many more empty rooms!"

    v "This looks like shit..."

    "He's not wrong."

    "This place looks way worse than our old AEGIS digs."

    "No windows, no light."

    "Also there's barely enough room for two of us, let alone three."

    v "You're putting them all in the same room? You couldn't give the lady some privacy?"

    v "What are we doing here, you idiot?"

    jin neutral "Well, I figured that--"

    l "It's fine. Thank you."

    show vargas sigh

    "Vargas, looking a little disappointed, shakes his head."

    v "If you say so..."

    v neutral "I suppose you're going to be forcing those two to share a bed."

    "Luna and I both say nothing. It will probably come out eventually, but based on Vargas' previous statements, I don't really want to expose our marriage."

    v "Whatever, if you're worth a damn I'll make sure you're in better digs soon."

    v "I'd like to say I reward excellence, but with the competition you're up against, it's more like that I reward competence."

    v "Even that is kinda hard to find these days."

    a "You won't have to worry about us, we're solid."

    v "Yeah, I hear that a lot. We'll see though."

    v "Anyway, I gotta get back to it."

    v "I look forward to working with all of you."

    stop music fadeout 1.0

    v happy "Especially you, Nova."

    play music1 "music/nox_dark.ogg" fadein 1.0

    scene cg04_01 at cgz with dis

    $ update_status("emotional_status", _("FURIOUS"), notify=False)

    $ update_status("vargas_feelings", _("No way he's doing that now?! That's even worse!!! This guy just thinks he can just do whatever he wants to get a reaction from me?! Well... I'll show him... He's done for!!! A dead man!!!"))

    "Sporting a massive grin, Vargas brushes up against Luna as he says that, causing her to appear quite uncomfortable."

    qa "Wait, what is he doing?"

    qa "The way his arm is..."

    qa "It seems like..."

    qa "There's no way. Is he touching her butt in front of me?"

    qa "He can't be."

    qa "Absolutely not."

    qa "If he was, Luna would have ripped his damn throat out already."

    qa "No way a woman like her would put up with abuse like that."

    if ep_01_insert:

        "First he's touching her back right in front of me and now this?"

    qa "I must be seeing things wrong..."

    qa "But why risk it? Let's get this creep out of here."

    show aiden nox_01 serious at off

    a "Alright boss, I think we're good for now. Thanks for the tour."

    a "It's probably best if we rest now. It's kinda been a long day."

    v "Right..."

    v "If you say so, bud..."

    qa "Why isn't he budging?"

    qa "Take the hint already."

    stop music1 fadeout 0.3    

    play snd "sounds/footsteps_boots_single_03.ogg"

    play amb "ambient/room_01.ogg" fadein 2.0 volume 0.6

    scene nox_bedroom

    show letterbox

    show aiden nox_01 look at off

    show luna nox_01 shocked_upset sweat at pos2

    show vargas nox happy at pos5

    with hpunch

    l "That's enough!" 

    "Luna jumps away from him and over to my side."

    v "Is there a problem?"

    "A slew of emotions appear on Luna's face."

    "Indignation, frustration, and finally defeat."

    l serious -sweat "Whatever..."

    l "Just leave us..."

    v sigh "Whatever you say, Nova."

    l upset "That isn't my name!!!" with hpunch

    v happy "Sorry, didn't hear that."

    "Vargas transparently lies with a big smile on his face."

    v "Whatever, doesn't matter I'm sure."

    v "I'll see you guys tomorrow. It'll be a big day. Trial by fire."

    v "Later!"

    v "Let's go, boys."

    stop amb fadeout 4.0

    play music1 "music/demon_notes.ogg" fadein 4.0

    $ persistent.unlocks.add("s04")

    $ renpy.end_replay()

    play snd "<silence 0.6>"

    queue snd "sounds/footsteps_two_sneakers_05.ogg"

    play snd1 "sounds/footsteps_two_sneakers_12.ogg"

    queue snd1 "sounds/footsteps_two_sneakers_13.ogg"

    scene nox_bedroom with dis

    "With all the confidence and bravado in the world, Vargas saunters out of our quarters with the rest of his posse following closely behind."

    stop snd1

    play snd "sounds/door_metal_close_01.ogg"

    "As soon as they are done and the door automatically slides shut behind them, Luna lets out a guttural roar."

    scene nox_bedroom at bgz 

    show aiden nox_01 look at off

    show luna nox_01 upset at vertical_shake(max_offset=15, speed=0.02, loops=8):

        xalign 0.5 yalign 0.2 zoom 0.8
        anchor (0.5, 0.2)

    with dis

    l "UUUUUUUUUAAAAH!!!" 

    play snd "sounds/impact_metal_04.ogg"

    with hpunch

    "In a display of pure rage, Luna crashes her fist against the wall."

    "If that hurt her, she doesn't show it."

    l "That piece of shit..."

    a serious "Are you okay? Did he do what I think he did?"

    l "It doesn't matter. I'll be okay."

    "Luna responds with drive and confidence."

    qa "So he did touch her like that..."

    qa "Asshole..."

    qa "I'll put an end to him myself when we can..."

    l "We're going to get you better... Then, when you're safe... We're going to make this guy pay..."

    a sigh "Agreed."

    a serious "He's going to go down."

    "It's not just that he's Nox."

    "It's personal."

    "I hate him."

    if perspective_mode == "solo":

        stop music1 fadeout 2.0

        jump episode_02

    stop music1 fadeout 2.5

    scene black with Dissolve(1.0)

    pause 1.5

    show lpc

    show pov_change_letterbox

    show luna nox_01 neutral behind pov_change_letterbox at pov_change:
        matrixcolor TintMatrix("#000000") * SaturationMatrix(0.0)

    pause 0.8

    hide luna nox_01 neutral

    show luna nox_01 neutral behind pov_change_letterbox at pov_change 
    
    with diss

    pause 1.0

    scene black with dis

    pause 0.5

    show text "{font=gui/fonts/Orbitron-VariableFont_wght.ttf}5 minutes earlier{/font}" at truecenter with dis

    $ update_status("emotional_status", _("UNCOMFORTABLE, ANNOYED"), notify=False)

    $ update_status("vargas_feelings", _("Did he really just do that?! The nerve of this guy! I should break his hand the next time he does that!"), notify=False)

    pause 1.0

label s05:    

    play music "music/the_complex.ogg" fadein 3.0

    scene nox_bedroom 

    show luna nox_01 neutral at pos6

    show vargas nox neutral at pos8

    show aiden nox_01 look at pos2

    with dis

    v "I'd like to say I reward excellence, but with the competition you're up against, it's more like that I reward competence."

    v "Even that is kinda hard to find these days."

    ql "Of course he'd say that, denigrating his own supporters."

    ql "Just terrible..."

    a "You won't have to worry about us, we're solid."

    "Although I know Aiden is playing a role, it still causes my spine to tingle."

    ql "Having to appease this... brute..."

    ql "It's horrible..."

    v "Yeah, I hear that a lot. We'll see though."

    v "Anyway, I gotta get back to it."

    v "I look forward to working with all of you."

    v happy "Especially you, Nova."

    ql "That nickname..."

    ql "So stupid."

    ql "Would he just let it go already?" 
    
    ql "Maybe if I don't respond to it then he will--"

    stop music fadeout 0.3

    play music1 "music/demon_notes.ogg" fadein 3.0

    play snd "sounds/body_grab_01.ogg"

    scene cg05_01 at cgz with Dissolve(0.5)

    $ update_status("emotional_status", _("FURIOUS"), notify=False)

    $ update_status("vargas_feelings", _("No way he's doing that now?! That's even worse!!! This guy just thinks he can just do whatever he wants to get a reaction from me?! Well... I'll show him... He's done for!!! A dead man!!!"))

    ql "WHAT THE HELL?!"

    ql "No way is he doing this right now."

    ql "I want to tear his throat out."

    ql "But I can't kill him. I really shouldn't."

    ql "Yelling at him only seems to encourage him too."

    ql "What the hell do I do?"

    ql "He's just a... a bully."

    ql "The complete scum of Neo Elysia."

    ql "What the heck do I do?"

    ql "Give him the attention he wants or suffer the indignity..."

    ql "I don't give him what he wants... But..."

    ql "He wins either way, doesn't he?"

    a "Alright boss, I think we're good for now. Thanks for the tour."

    a "It's probably best if we rest now. It's kinda been a long day."

    v "Right..."

    v "If you say so, bud..."

    "Finally, noticing what's happening, Aiden comes to my rescue and tries to get him out of the room."

    "Using the conversation as an opportunity to escape, I try to shimmy away from him, but his grip doesn't slip."

    play snd "sounds/body_squeeze_01.ogg"

    pause 0.3

    with vshake((0, 0, 0, 0), 0.2, dist=20)

    "No, if anything, he tightens it, keeping me there."

    "Squeezing."

    "I feel those fingers digging deeper and deeper, clawing their way into my flesh."

    "And it feels wrong."

    "I can't take this anymore."

    play snd "sounds/footsteps_boots_single_03.ogg"

    scene nox_bedroom

    show letterbox

    show aiden nox_01 look at pos1

    show luna nox_01 shocked_upset sweat at pos3

    show vargas nox happy at pos6

    with hpunch

    l "That's enough!"

    "No longer attempting to subtly pull myself away, I tear my butt away from his hand, leaving him grasping air."

    v "Is there a problem?"

    ql "..."

    ql "The absolute nerve of this piece of shit."

    ql "I should kill him. I should kill him right now in front of everyone."

    ql "Tear his head from his neck and go down in a blaze of glory."

    ql "But... That would kill all three of us."

    ql "I've already risked enough today, punching him in the face."

    ql "I suppose that in a way he is right, saying I'm a hothead."

    ql "I hate that though..."

    ql "I can't give him the satisfaction of being right about me..."

    ql "I can't..."

    "Doing my best to calm myself down, I silently mutter my pathetic response under my breath."

    l serious -sweat "Whatever..."

    l "Just leave us..."

    v sigh "Whatever you say, Nova."

    ql "OKAY, THAT'S IT!!!"

    ql "I CAN'T TAKE THIS ASSHOLE!!!"

    l upset "That isn't my name!!!" with hpunch

    v happy "Sorry, didn't hear that."

    ql "THIS... THIS..."

    ql "I HAVE NO WORDS FOR THIS MAN!!!"

    "In a blind rage, I can't even listen to the words coming out of his mouth."

    play snd "<silence 0.6>"

    queue snd "sounds/footsteps_two_sneakers_05.ogg"

    play snd1 "sounds/footsteps_two_sneakers_12.ogg"

    queue snd1 "sounds/footsteps_two_sneakers_13.ogg"

    queue snd1 "sounds/door_metal_close_01.ogg"

    hide vargas with diss

    "Lucky for him and for our lifespans, he quickly leaves, allowing me to finally unleash my full rage." with dis

    stop snd fadeout 0.3

    stop snd1 fadeout 0.3

    $ persistent.unlocks.add("s05")

    $ renpy.end_replay()

    show luna nox_01 upset at vertical_shake(max_offset=15, speed=0.02, loops=8):

        xalign 0.3 yalign 0 zoom 0.3    
        anchor (0.5, 0.0)

    l "UUUUUUUUUAAAAH!!!"

    scene nox_bedroom at bgz

    show aiden nox_01 serious at lz

    show luna nox_01 upset at rz

    play snd "sounds/impact_metal_04.ogg"

    with hpunch

    "In my rage, I punch the wall with all my strength."

    "The impact creates a sharp pain in my knuckles, as well as a loud, but distinctly unsatisfying thump."

    "A noise completely symbolic of my impotent anger."

    ql "This isn't doing anything. It's completely unproductive."

    ql "I just can't help myself though..."

    l "That piece of shit..."

    a serious "Are you okay? Did he do what I think he did?"

    "I can hear the genuine concern in Aiden's voice."

    "It comforts me... even though with everything that's happening, I should be the one comforting him."

    ql "I need to be strong for him."

    l "It doesn't matter. I'll be okay."

    l "We're going to get you better... Then, when you're safe... We're going to make this guy pay..."

    ql "I promise..."

    a sigh "Agreed."

    a serious "He's going to go down."

    ql "We're together on that... Good..."

    ql "Taking this guy out is going to be so satisfying."

    ql "I can't wait to see his face when all is said and done."

    ql "He'll never know what hit him..."

    ql "Time to show him what Luna Virelith is capable of."

    # End of Episode 1

    stop music1 fadeout 2.5

    scene black with Dissolve(1.0)

    pause 1.5

    show apc

    show pov_change_letterbox

    show aiden nox_01 neutral behind pov_change_letterbox at pov_change:
        matrixcolor TintMatrix("#000000") * SaturationMatrix(0.0)

    pause 0.8

    hide aiden nox_01 neutral

    show aiden nox_01 neutral behind pov_change_letterbox at pov_change 
    
    with diss

    pause 1.0

    jump episode_02