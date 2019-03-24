import random

adjectives = ["aback","alcoholic","alert","alike","annoyed","annoying","anxious","auspicious","automatic","available","bashful","bawdy","beautiful","befitting","belligerent","beneficial","cautious","ceaseless","certain","changeable","charming","cheap","cheerful","chemical","chief","childlike","chilly","chivalrous","chubby","chunky","clammy","imperfect","impolite","important","imported","impossible","incandescent","incompetent","inconclusive","industrious","incredible","inexpensive","infamous","innate","innocent","inquisitive","insidious","instinctive","intelligent","interesting","internal","invincible","irate","irritating","itchy","jaded","jagged","jazzy","jealous","jittery","jobless","jolly","joyous","judicious","juicy","jumbled","jumpy","juvenile","kaput","keen","kind","kindhearted","kindly","knotty","knowing","knowledgeable","known","labored","lackadaisical","lacking","lame","lamentable","languid","large","last","late","laughable","lavish","lazy","lean","learned","left","legal","lethal","level","lewd","light","like","likeable","limping","literate","little","lively","lively","living","lonely","long","longing","long-term","loose","lopsided","loud","loutish","lovely","loving","low","lowly","lucky","ludicrous","lumpy","lush","luxuriant","lying","lyrical","macabre","macho","maddening","madly","magenta","magical","magnificent","majestic","makeshift","male","malicious","mammoth","maniacal","many","marked","massive","married","marvelous","material","materialistic","mature","mean","measly","meaty","medical","meek","mellow","melodic","melted","merciful","mere","messy","mighty","military","milky","mindless","miniature","minor","miscreant","misty","mixed","moaning","modern","moldy","momentous","pumped","puny","purple","purring","pushy","puzzled","puzzling","quack","quaint","snotty","soft","soggy","solid","somber","sophisticated","sordid","sore","sore","sour","sparkling","special","spectacular","spicy","spiffy","spiky","spiritual","spiteful","splendid","spooky","spotless","spotted","spotty","spurious","squalid","wild","willing","windy","wiry","wise","wistful","witty","woebegone","womanly","wonderful","wooden","woozy","workable","worried","worthless","wrathful","wretched","wrong","wry","xenophobic","yellow","yielding","young","youthful","yummy","zany","zealous","zesty","zippy","zonked"]

#verbs = ["accept", "add", "admire", "admit", "advise", "afford", "agree", "alert", "allow", "amuse", "analyse", "announce", "annoy", "answer", "apologise", "appear", "applaud", "appreciate", "approve", "argue", "arrange", "arrest", "arrive", "ask", "attach", "attack", "attempt", "attend", "attract", "avoid", "back", "bake", "balance", "ban", "bang", "bare", "bat", "bathe", "battle", "beam", "beg", "behave", "belong", "bleach", "bless", "blind", "blink", "blot", "blush", "boast", "boil", "bolt", "bomb", "book", "bore", "borrow", "bounce", "bow", "box", "brake", "branch", "breathe", "bruise", "brush", "bubble", "bump", "burn", "bury", "buzz", "calculate", "call", "camp", "care", "carry", "carve", "cause", "challenge", "change", "charge", "chase", "cheat", "check", "cheer", "chew", "choke", "chop", "claim", "clap", "clean", "clear", "clip", "close", "coach", "coil", "collect", "colour", "comb", "command", "communicate", "compare", "compete", "complain", "complete", "concentrate", "concern", "confess", "confuse", "connect", "consider", "consist", "contain", "continue", "copy", "correct", "cough", "count", "cover", "crack", "crash", "crawl", "cross", "crush", "cry", "cure", "curl", "curve", "cycle", "dam", "damage", "dance", "dare", "decay", "deceive", "decide", "decorate", "delay", "delight", "deliver", "depend", "describe", "desert", "deserve", "destroy", "detect", "develop", "disagree", "disappear", "disapprove", "disarm", "discover", "dislike", "divide", "double", "doubt", "drag", "drain", "dream", "dress", "drip", "drop", "drown", "drum", "dry", "dust", "earn", "educate", "embarrass", "employ", "empty", "encourage", "end", "enjoy", "enter", "entertain", "escape", "examine", "excite", "excuse", "exercise", "exist", "expand", "expect", "explain", "explode", "extend", "face", "fade", "fail", "fancy", "fasten", "fax", "fear", "fence", "fetch", "file", "fill", "film", "fire", "fit", "fix", "flap", "flash", "float", "flood", "flow", "flower", "fold", "follow", "fool", "force", "form", "found", "frame", "frighten", "fry", "gather", "gaze", "glow", "glue", "grab", "grate", "grease", "greet", "grin", "grip", "groan", "guarantee", "guard", "guess", "guide", "hammer", "hand", "handle", "hang", "happen", "harass", "harm", "hate", "haunt", "head", "heal", "heap", "heat", "help", "hook", "hop", "hope", "hover", "hug", "hum", "hunt", "hurry", "identify", "ignore", "imagine", "impress", "improve", "include", "increase", "influence", "inform", "inject", "injure", "instruct", "intend", "interest", "interfere", "interrupt", "introduce", "invent", "invite", "irritate", "itch", "jail", "jam", "jog", "join", "joke", "judge", "juggle", "jump", "kick", "kill", "kiss", "kneel", "knit", "knock", "knot", "label", "land", "last", "laugh", "launch", "learn", "level", "license", "lick", "lie", "lighten", "like", "list", "listen", "live", "load", "lock", "long", "look", "love", "man", "manage", "march", "mark", "marry", "match", "mate", "matter", "measure", "meddle", "melt", "memorise", "mend", "mess up", "milk", "mine", "miss", "mix", "moan", "moor", "mourn", "move", "muddle", "mug", "multiply", "murder", "nail", "name", "need", "nest", "nod", "note", "notice", "number", "obey", "object", "observe", "obtain", "occur", "offend", "offer", "open", "order", "overflow", "owe", "own", "pack", "paddle", "paint", "park", "part", "pass", "paste", "pat", "pause", "peck", "pedal", "peel", "peep", "perform", "permit", "phone", "pick", "pinch", "pine", "place", "plan", "plant", "play", "please", "plug", "point", "poke", "polish", "pop", "possess", "post", "pour", "practise", "pray", "preach", "precede", "prefer", "prepare", "present", "preserve", "press", "pretend", "prevent", "prick", "print", "produce", "program", "promise", "protect", "provide", "pull", "pump", "punch", "puncture", "punish", "push", "question", "queue", "race", "radiate", "rain", "raise", "reach", "realise", "receive", "recognise", "record", "reduce", "reflect", "refuse", "regret", "reign", "reject", "rejoice", "relax", "release", "rely", "remain", "remember", "remind", "remove", "repair", "repeat", "replace", "reply", "report", "reproduce", "request", "rescue", "retire", "return", "rhyme", "rinse", "risk", "rob", "rock", "roll", "rot", "rub", "ruin", "rule", "rush", "sack", "sail", "satisfy", "save", "saw", "scare", "scatter", "scold", "scorch", "scrape", "scratch", "scream", "screw", "scribble", "scrub", "seal", "search", "separate", "serve", "settle", "shade", "share", "shave", "shelter", "shiver", "shock", "shop", "shrug", "sigh", "sign", "signal", "sin", "sip", "ski", "skip", "slap", "slip", "slow", "smash", "smell", "smile", "smoke", "snatch", "sneeze", "sniff", "snore", "snow", "soak", "soothe", "sound", "spare", "spark", "sparkle", "spell", "spill", "spoil", "spot", "spray", "sprout", "squash", "squeak", "squeal", "squeeze", "stain", "stamp", "stare", "start", "stay", "steer", "step", "stir", "stitch", "stop", "store", "strap", "strengthen", "stretch", "strip", "stroke", "stuff", "subtract", "succeed", "suck", "suffer", "suggest", "suit", "supply", "support", "suppose", "surprise", "surround", "suspect", "suspend", "switch", "talk", "tame", "tap", "taste", "tease", "telephone", "tempt", "terrify", "test", "thank", "thaw", "tick", "tickle", "tie", "time", "tip", "tire", "touch", "tour", "tow", "trace", "trade", "train", "transport", "trap", "travel", "treat", "tremble", "trick", "trip", "trot", "trouble", "trust", "try", "tug", "tumble", "turn", "twist", "type", "undress", "unfasten", "unite", "unlock", "unpack", "untidy", "use", "vanish", "visit", "wail", "wait", "walk", "wander", "want", "warm", "warn", "wash", "waste", "watch", "water", "wave", "weigh", "welcome", "whine", "whip", "whirl", "whisper", "whistle", "wink", "wipe", "wish", "wobble", "wonder", "work", "worry", "wrap", "wreck", "wrestle", "wriggle", "x-ray", "yawn", "yell", "zip", "zoom"]

nouns = ["accelerator", "accordion", "account", "accountant", "advice", "afghanistan", "africa", "aftermath", "afternoon", "aftershave", "afterthought", "age", "agenda", "agreement", "air", "airbus", "bongo", "bonsai", "book","bracket", "brain", "brake", "branch", "brand", "brandy", "brass", "brazil", "bread", "break", "breakfast", "breath", "brian", "brick", "bridge", "british", "broccoli", "brochure", "broker", "bronze", "brother", "cabbage", "cabinet", "cable", "cactus", "cafe", "cake", "calculator", "calculus", "calendar", "calf", "call", "camel", "camera", "camp", "can", "canada", "canadian", "cancer", "candle", "cannon", "canoe", "canvas", "cap", "capital","health", "hearing", "heart", "heat", "heaven", "hedge", "height", "helen", "helicopter", "helium", "hell", "helmet", "help", "hemp", "hen", "heron", "herring", "hexagon", "hill", "himalayan", "hip", "hippopotamus", "history", "hobbies", "hockey", "hoe", "hole", "holiday", "home", "honey", "hood", "hook", "hope", "horn", "horse", "hose", "hospital", "hot", "hour", "hourglass", "house", "hovercraft", "hub", "hubcap", "humidity", "humor", "hurricane", "hyacinth", "imprisonment", "insulation", "insurance", "interactive", "interest", "internet", "interviewer", "intestine", "invention", "inventory", "invoice", "iran", "iraq", "iris", "iron", "island", "israel", "italian", "italy", "jacket", "jaguar", "jail", "jam", "james", "january", "japan", "japanese", "jar", "jasmine", "jason", "jaw", "jeans", "jeep", "jeff", "jelly", "jellyfish", "jennifer", "jet", "jewel", "jogging", "john", "join", "joke", "joseph", "journey", "judge", "judo", "juice", "july", "jumbo", "jump", "jumper", "june", "jury", "justice", "jute", "kale", "kamikaze", "kangaroo", "karate", "karen", "kayak", "kendo", "kenneth","mailbox", "mailman", "makeup", "malaysia", "male", "mall", "mallet", "man", "manager", "mandolin", "manicure", "manx", "map", "maple", "maraca", "marble", "march", "margaret", "margin", "maria", "marimba", "mark", "market", "married", "mary", "mascara", "mask", "mass", "match", "math", "mattock", "may", "mayonnaise", "meal", "measure", "meat", "mechanic", "medicine", "pan", "pancake", "pancreas", "panda", "pansy", "panther", "panties", "pantry", "pants", "panty", "pantyhose", "paper", "paperback", "parade", "parallelogram", "parcel", "parent", "parentheses", "park", "parrot", "parsnip", "part", "particle", "partner", "partridge", "party", "passbook", "passenger", "passive", "sailor", "salad", "salary", "sale", "salesman", "salmon", "salt", "sampan", "samurai", "sand", "sandra", "sandwich", "santa", "sarah", "sardine", "satin", "saturday", "sauce", "saudi arabia", "sausage", "save", "saw", "saxophone", "scale", "scallion", "scanner", "scarecrow", "scarf", "scene", "scent", "schedule", "school", "science", "scissors", "scooter", "scorpio", "scorpion", "scraper", "screen", "screw", "screwdriver", "time", "timer", "timpani", "tin", "tip", "tire", "titanium", "title", "toad", "toast", "toe", "toenail", "toilet", "tom-tom", "tomato", "ton", "tongue"]

def genConvo(randInt,word):
  '''
  :param randInt: random integer for response type
  :param word: seed word
  :return: result response and adjective integer for decoding
  '''

  randAdj = random.randint(0,len(adjectives) - 1)
  randNn = random.randint(0,len(nouns) - 1)

  nn = nouns[randNn]
  adj = adjectives[randAdj]
  # TODO: change to template types
  if(randInt == 0):
      text = 'I think that {} is very {}'.format(word,adj)
  elif(randInt == 1):
      text = 'wow {} is really {}'.format(word,adj)
  elif(randInt == 2):
      text = 'I dont agree, but {} is {}'.format(word,adj)
  elif(randInt == 3):
      text = 'Man forget about {}, {} will be {}'.format(word,nn,adj)
  elif(randInt == 4):
      text = 'This {} will be {}'.format(word,adj)
  elif(randInt == 5):
      text = 'Yea {} is really {} today'.format(word,adj)
  elif(randInt == 6):
      text = '{} more like {} {}'.format(word,adj,word)
  elif(randInt == 7):
      text = 'cant wait for this {} {}'.format(adj,word)
  elif(randInt == 8):
      text = 'I think {} is more {} than {}'.format(nn,adj,word)
  elif(randInt == 9):
      text = 'This is going to be a {} {}'.format(adj,nn)
  elif(randInt == 10):
      text = 'cant wait for a {} {}'.format(adj,nn)
  elif(randInt == 11):
      text = '{} cant believe the {} {}'.format(word,adj,nn)
  elif(randInt == 12):
      text = '{} has made a {} impact'.format(word,adj)
  elif(randInt == 13):
      text = 'remember how {} was {}'.format(word,adj)



  return text,adj,nn


def retConvo(typeconvo,word,adj,nn):
  '''

  :param typeconvo: number of convo type to result
  :param word: seed word
  :param adj: seed adjective
  :return: full text
  '''
  #@TODO change to template types
  if(typeconvo == 0):
      text = 'I think that {} is very {}'.format(word, adj)
  elif(typeconvo == 1):
      text = 'wow {} is really {}'.format(word,adj)
  elif(typeconvo == 2):
      text = 'I dont agree, but {} is {}'.format(word,adj)
  elif(typeconvo == 3):
      text = 'Man forget about {}, {} will be {}'.format(word, nn, adj)
  elif(typeconvo == 4):
      text = 'This {} will be {}'.format(word,adj)
  elif(typeconvo == 5):
      text = 'Yea {} is really {} today'.format(word,adj)
  elif(typeconvo == 6):
      text = '{} more like {} {}'.format(word,adj,word)
  elif (typeconvo == 7):
      text = 'cant wait for this {} {}'.format(adj, word)
  elif (typeconvo == 8):
      text = 'I think {} is more {} than {}'.format(nn, adj, word)
  elif (typeconvo == 9):
      text = 'This is going to be a {} {}'.format(adj, nn)
  elif (typeconvo == 10):
      text = 'cant wait for a {} {}'.format(adj, nn)
  elif (typeconvo == 11):
      text = '{} cant believe the {} {}'.format(word, adj, nn)
  elif (typeconvo == 12):
      text = '{} has made a {} impact'.format(word, adj)
  elif (typeconvo == 13):
      text = 'remember how {} was {}'.format(word, adj)

  return text