import random
from ngram import CC, CD, DT,EX, FW,IN,JJ,JJR,JJS,LS,MD,NN,NNS,NNP,NNPS,PDT,POS,PRP,PRPD,RB,RBR,RP,TO,UH,VB,VBD,VBG,VBZ,VBP,WDT,WP,WPD,WRB,VBN
from ngram import CC_elemtweetidx,CD_elemtweetidx,DT_elemtweetidx,EX_elemtweetidx,FW_elemtweetidx,IN_elemtweetidx,JJ_elemtweetidx,JJR_elemtweetidx,JJS_elemtweetidx,LS_elemtweetidx,MD_elemtweetidx,NN_elemtweetidx,NNS_elemtweetidx,NNP_elemtweetidx,NNPS_elemtweetidx,PDT_elemtweetidx,POS_elemtweetidx,PRP_elemtweetidx,PRPD_elemtweetidx,RB_elemtweetidx,RBR_elemtweetidx,RBS_elemtweetidx,RP_elemtweetidx,TO_elemtweetidx,UH_elemtweetidx,VB_elemtweetidx,VBD_elemtweetidx,VBG_elemtweetidx,VBN_elemtweetidx,VBP_elemtweetidx,VBZ_elemtweetidx,WDT_elemtweetidx,WP_elemtweetidx,WPD_elemtweetidx,WRB_elemtweetidx
from ngram import templates
from ngram import genTemplate, sentencePos

genTemplate("Obama")

def genConvo(randInt,word):
  '''
  :param randInt: random integer for response type
  :param word: seed word
  :return: result response and adjective integer for decoding
  '''
  seedWordType = sentencePos(word)
  templateType = templates[randInt]
  text = [None] * len(templateType)
  try:
    seedWordType = seedWordType[0][1]
    for i in range(len((templateType))):
        if(templateType[i] == seedWordType):
             text[i] = word
             break
  except IndexError:
      pass

  for i in range(len(templateType)):
      if (templateType[i] == 'CC' and text[i] is None):
          text[i] = CC[random.randint(0,len(CC) - 1)]
      elif (templateType[i] == 'CD' and text[i] is None):
          text[i] = (CD[random.randint(0, len(CD) - 1)])
      elif (templateType[i] == 'DT' and text[i] is None):
          text[i] = (DT[random.randint(0, len(DT) - 1)])
      elif (templateType[i] == 'EX' and text[i] is None):
          text[i] = (EX[random.randint(0, len(EX) - 1)])
      elif (templateType[i] == 'FW' and text[i] is None):
          text[i] = (FW[random.randint(0, len(FW) - 1)])
      elif (templateType[i] == 'IN' and text[i] is None):
          text[i] = (IN[random.randint(0, len(IN) - 1)])
      elif (templateType[i] == 'JJ' and text[i] is None):
          text[i] = (JJ[random.randint(0, len(JJ) - 1)])
      elif (templateType[i] == 'JJR' and text[i] is None):
          text[i] = (JJR[random.randint(0, len(JJR) - 1)])
      elif (templateType[i] == 'JJS' and text[i] is None):
          text[i] = (JJS[random.randint(0, len(JJS) - 1)])
      elif (templateType[i] == 'LS' and text[i] is None):
          text[i] = (LS[random.randint(0, len(LS) - 1)])
      elif (templateType[i] == 'MD' and text[i] is None):
          text[i] = (MD[random.randint(0, len(MD) - 1)])
      elif (templateType[i] == 'NN' and text[i] is None):
          text[i] = (NN[random.randint(0, len(NN) - 1)])
      elif (templateType[i] == 'NNS' and text[i] is None):
          text[i] = (NNS[random.randint(0, len(NNS) - 1)])
      elif (templateType[i] == 'NNP' and text[i] is None):
          text[i] = (NNP[random.randint(0, len(NNP) - 1)])
      elif (templateType[i] == 'NNPS' and text[i] is None):
          text[i] = (NNPS[random.randint(0, len(NNPS) - 1)])
      elif (templateType[i] == 'PDT' and text[i] is None):
          text[i] = (PDT[random.randint(0, len(PDT) - 1)])
      elif (templateType[i] == 'POS' and text[i] is None):
          text[i] = (POS[random.randint(0, len(POS) - 1)])
      elif (templateType[i] == 'PRP' and text[i] is None):
          text[i] = (PRP[random.randint(0, len(PRP) - 1)])
      elif (templateType[i] == 'PRP$' and text[i] is None):
          text[i] = (PRPD[random.randint(0, len(PRPD) - 1)])
      elif (templateType[i] == 'RB' and text[i] is None):
          text[i] = (RB[random.randint(0, len(RB) - 1)])
      elif (templateType[i] == 'RBR' and text[i] is None):
          text[i] = (RBR[random.randint(0, len(RBR) - 1)])
      elif (templateType[i] == 'RBS' and text[i] is None):
          text[i] = (RBS[random.randint(0, len(RBS) - 1)])
      elif (templateType[i] == 'RP' and text[i] is None):
          text[i] = (RP[random.randint(0, len(RP) - 1)])
      elif (templateType[i] == 'TO' and text[i] is None):
          text[i] = (TO[random.randint(0, len(TO) - 1)])
      elif (templateType[i] == 'UH' and text[i] is None):
          text[i] = (UH[random.randint(0, len(UH) - 1)])
      elif (templateType[i] == 'VB' and text[i] is None):
          text[i] = (VB[random.randint(0, len(VB) - 1)])
      elif (templateType[i] == 'VBD' and text[i] is None):
          text[i] = (VBD[random.randint(0, len(VBD) - 1)])
      elif (templateType[i] == 'VBN' and text[i] is None):
          text[i] = (VBN[random.randint(0, len(VBN) - 1)])
      elif (templateType[i] == 'VBP' and text[i] is None):
          text[i] = (VBP[random.randint(0, len(VBP) - 1)])
      elif (templateType[i] == 'VBZ' and text[i] is None):
          text[i] = (VBZ[random.randint(0, len(VBZ) - 1)])
      elif (templateType[i] == 'VBG' and text[i] is None):
          text[i] = (VBG[random.randint(0, len(VBG) - 1)])
      elif (templateType[i] == 'WDT' and text[i] is None):
          text[i] = (WDT[random.randint(0, len(WDT) - 1)])
      elif (templateType[i] == 'WP' and text[i] is None):
          text[i] = (WP[random.randint(0, len(WP) - 1)])
      elif (templateType[i] == 'WP$' and text[i] is None):
          text[i] = (WPD[random.randint(0, len(WPD) - 1)])
      elif (templateType[i] == 'WRB' and text[i] is None):
          text[i] = (WRB[random.randint(0, len(WRB) - 1)])

  result = ' '.join(text)
  return result



def retConvo(randInt,prevword,text):
  '''

  :param typeconvo: number of convo type to result
  :param word: seed word
  :param adj: seed adjective
  :return: full text
  '''
  return text