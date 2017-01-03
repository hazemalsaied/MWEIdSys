##Sentence No. 12079
**Text:** Mais cette procédure déplait à Matignon qui lui demande à présent de faire le nécessaire pour que les orientations du ministère de l' industrie soient mises en oeuvre .
###Existing MWEs: 
**MWE No.:** 3
**Text:** mises en oeuvre



###Identified MWEs: 
**MWE No.:** 1
**Text:** à Matignon


**MWE No.:** 2
**Text:** à présent


**MWE No.:** 3
**Text:** faire ministère de


**MWE No.:** 4
**Text:** mises en oeuvre


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Mais .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Mais]   ; buffer = [cette .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [cette .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [cette]   ; buffer = [procédure .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [procédure .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [procédure]   ; buffer = [déplait .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [déplait .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [déplait]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [Matignon .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, Matignon]   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, Matignon, qui]   ; buffer = [lui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, Matignon]   ; buffer = [lui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, Matignon, lui]   ; buffer = [demande .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, Matignon]   ; buffer = [demande .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, Matignon, demande]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, Matignon]   ; buffer = [à .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[à, Matignon]]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [présent .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, présent]   ; buffer = [de .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[à, présent]]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [faire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [faire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire]   ; buffer = [le .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire, le]   ; buffer = [nécessaire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire]   ; buffer = [nécessaire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire, nécessaire]   ; buffer = [pour .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire]   ; buffer = [pour .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire, pour]   ; buffer = [que .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire]   ; buffer = [que .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire, que]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire]   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire, les]   ; buffer = [orientations .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire]   ; buffer = [orientations .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire, orientations]   ; buffer = [du .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire]   ; buffer = [du .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire, du]   ; buffer = [ministère .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire]   ; buffer = [ministère .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire, ministère]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [faire, ministère, de]   ; buffer = [l' .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[faire, ministère, de]]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [industrie .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [industrie .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [industrie]   ; buffer = [soient .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [soient .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [soient]   ; buffer = [mises .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [mises .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mises]   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mises, en]   ; buffer = [oeuvre .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mises, en, oeuvre]   ; buffer = [.]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[mises, en, oeuvre]]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12080
**Text:** Autrement dit : retirez votre procédure de classement .
###Existing MWEs: 
**MWE No.:** 0
**Text:** Autrement dit



###Identified MWEs: 
**MWE No.:** 1
**Text:** Autrement dit


**MWE No.:** 2
**Text:** retirez classement


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Autrement .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Autrement]   ; buffer = [dit .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Autrement, dit]   ; buffer = [: .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[Autrement, dit]]   ; buffer = [: .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [: .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [:]   ; buffer = [retirez .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [retirez .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [retirez]   ; buffer = [votre .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [retirez, votre]   ; buffer = [procédure .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [retirez]   ; buffer = [procédure .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [retirez, procédure]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [retirez]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [retirez, de]   ; buffer = [classement .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [retirez]   ; buffer = [classement .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [retirez, classement]   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [retirez, classement, .]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [retirez, classement]   ; buffer = [ ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[retirez, classement]]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12095
**Text:** Cette mesure , qui a été accueillie favorablement par les militants des organisations de lutte contre le sida , fait suite à la publication , en juillet dernier , d' une étude montrant que des doses réduites d' AZT ne diminuent pas l' efficacité du médicament , mais qu' en revanche elles réduisent ses effets secondaires .
###Existing MWEs: 
**MWE No.:** 0
**Text:** fait suite



###Identified MWEs: 
**MWE No.:** 1
**Text:** fait suite


**MWE No.:** 2
**Text:** en revanche


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Cette .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Cette]   ; buffer = [mesure .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [mesure .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mesure]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [qui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qui]   ; buffer = [a .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [a .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [a]   ; buffer = [été .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [été .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [été]   ; buffer = [accueillie .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [accueillie .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [accueillie]   ; buffer = [favorablement .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [favorablement .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [favorablement]   ; buffer = [par .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [par .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [par]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [militants .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [militants .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [militants]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [organisations .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [organisations .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [organisations]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [lutte .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [lutte .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lutte]   ; buffer = [contre .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [contre .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [contre]   ; buffer = [le .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [le .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [le]   ; buffer = [sida .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sida .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sida]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [fait .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [fait .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [suite .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, suite]   ; buffer = [à .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[fait, suite]]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [la]   ; buffer = [publication .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [publication .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [publication]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [en .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [juillet .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [juillet .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [juillet]   ; buffer = [dernier .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dernier .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dernier]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [d' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [d' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [d']   ; buffer = [une .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [une .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [une]   ; buffer = [étude .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [étude .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [étude]   ; buffer = [montrant .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [montrant .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [montrant]   ; buffer = [que .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [que .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [que]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [doses .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [doses .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [doses]   ; buffer = [réduites .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [réduites .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [réduites]   ; buffer = [d' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [d' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [d']   ; buffer = [AZT .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [AZT .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [AZT]   ; buffer = [ne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ne]   ; buffer = [diminuent .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [diminuent .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [diminuent]   ; buffer = [pas .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pas .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pas]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [efficacité .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [efficacité .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [efficacité]   ; buffer = [du .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [du .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [du]   ; buffer = [médicament .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [médicament .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [médicament]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [mais .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [mais .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mais]   ; buffer = [qu' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qu' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qu']   ; buffer = [en .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [revanche .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, revanche]   ; buffer = [elles .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[en, revanche]]   ; buffer = [elles .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [elles .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [elles]   ; buffer = [réduisent .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [réduisent .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [réduisent]   ; buffer = [ses .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ses .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ses]   ; buffer = [effets .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [effets .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [effets]   ; buffer = [secondaires .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [secondaires .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [secondaires]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12097
**Text:** Cette annonce arrive à point nommé au moment où les autorités sanitaires de différents pays s' interrogent sur l' opportunité de recommander - et donc , dans un pays comme la France , de rembourser - la prise d' AZT à l' ensemble des personnes séropositives .
###Existing MWEs: 
**MWE No.:** 0
**Text:** à point nommé



###Identified MWEs: 
**MWE No.:** 1
**Text:** à point


**MWE No.:** 2
**Text:** recommander - France


**MWE No.:** 3
**Text:** rembourser - prise


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Cette .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Cette]   ; buffer = [annonce .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [annonce .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [annonce]   ; buffer = [arrive .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [arrive .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [arrive]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [point .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, point]   ; buffer = [nommé .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[à, point]]   ; buffer = [nommé .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [nommé .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [nommé]   ; buffer = [au .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [au .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [au]   ; buffer = [moment .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [moment .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [moment]   ; buffer = [où .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [où .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [où]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [autorités .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [autorités .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [autorités]   ; buffer = [sanitaires .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sanitaires .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sanitaires]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [différents .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [différents .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [différents]   ; buffer = [pays .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pays .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pays]   ; buffer = [s' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [s' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [s']   ; buffer = [interrogent .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [interrogent .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [interrogent]   ; buffer = [sur .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sur .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sur]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [opportunité .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [opportunité .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [opportunité]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [recommander .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [recommander .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander]   ; buffer = [- .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -]   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -, et]   ; buffer = [donc .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -]   ; buffer = [donc .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -, donc]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -]   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -, ,]   ; buffer = [dans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -]   ; buffer = [dans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -, dans]   ; buffer = [un .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -]   ; buffer = [un .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -, un]   ; buffer = [pays .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -]   ; buffer = [pays .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -, pays]   ; buffer = [comme .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -]   ; buffer = [comme .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -, comme]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -]   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -, la]   ; buffer = [France .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -]   ; buffer = [France .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [recommander, -, France]   ; buffer = [, .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[recommander, -, France]]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [rembourser .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [rembourser .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [rembourser]   ; buffer = [- .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [rembourser, -]   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [rembourser, -, la]   ; buffer = [prise .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [rembourser, -]   ; buffer = [prise .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [rembourser, -, prise]   ; buffer = [d' .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[rembourser, -, prise]]   ; buffer = [d' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [d' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [d']   ; buffer = [AZT .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [AZT .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [AZT]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [ensemble .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ensemble .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ensemble]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [personnes .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [personnes .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [personnes]   ; buffer = [séropositives .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [séropositives .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [séropositives]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12116
**Text:** Les progrès réalisés dans ce domaine , par exemple la libre circulation des biens et des capitaux , ne doivent pas être remis en cause si l' union économique et monétaire veut s' inscrire dans la durée .
###Existing MWEs: 
**MWE No.:** 1
**Text:** remis en cause



###Identified MWEs: 
**MWE No.:** 1
**Text:** remis en cause


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Les]   ; buffer = [progrès .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [progrès .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [progrès]   ; buffer = [réalisés .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [réalisés .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [réalisés]   ; buffer = [dans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dans]   ; buffer = [ce .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ce .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ce]   ; buffer = [domaine .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [domaine .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [domaine]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [par .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [par .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [par]   ; buffer = [exemple .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [exemple .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [exemple]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [la]   ; buffer = [libre .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [libre .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [libre]   ; buffer = [circulation .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [circulation .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [circulation]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [biens .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [biens .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [biens]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [capitaux .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [capitaux .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [capitaux]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [ne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ne]   ; buffer = [doivent .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [doivent .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [doivent]   ; buffer = [pas .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pas .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pas]   ; buffer = [être .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [être .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [être]   ; buffer = [remis .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [remis .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [remis]   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [remis, en]   ; buffer = [cause .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [remis, en, cause]   ; buffer = [si .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[remis, en, cause]]   ; buffer = [si .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [si .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [si]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [union .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [union .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [économique .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, économique]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, et]   ; buffer = [monétaire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [monétaire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, monétaire]   ; buffer = [veut .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [veut .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, veut]   ; buffer = [s' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [s' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, s']   ; buffer = [inscrire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [inscrire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, inscrire]   ; buffer = [dans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [dans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, dans]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, la]   ; buffer = [durée .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [durée .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, durée]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, .]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12119
**Text:** Son organisation doit tenir compte des espoirs que suscite dans les Etats membres une future union économique et monétaire : dans les pays dotés d' une monnaie stable , l' espoir que la stabilité du pouvoir d' achat ne disparaisse pas avec l' union économique et monétaire ; dans les pays qui connaissent une dépréciation plus ou moins forte de leur monnaie , l' espoir que l' union économique et monétaire y mette un terme définitif .
###Existing MWEs: 
**MWE No.:** 0
**Text:** tenir compte



###Identified MWEs: 
**MWE No.:** 1
**Text:** tenir compte


**MWE No.:** 2
**Text:** Etats membres monétaire


**MWE No.:** 3
**Text:** union monétaire


**MWE No.:** 4
**Text:** union monétaire y mette


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Son .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Son]   ; buffer = [organisation .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [organisation .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [organisation]   ; buffer = [doit .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [doit .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [doit]   ; buffer = [tenir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [tenir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenir]   ; buffer = [compte .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenir, compte]   ; buffer = [des .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[tenir, compte]]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [espoirs .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [espoirs .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [espoirs]   ; buffer = [que .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [que .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [que]   ; buffer = [suscite .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [suscite .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [suscite]   ; buffer = [dans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dans]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [Etats .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Etats .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats]   ; buffer = [membres .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres]   ; buffer = [une .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres, une]   ; buffer = [future .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres]   ; buffer = [future .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres, future]   ; buffer = [union .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres]   ; buffer = [union .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres, union]   ; buffer = [économique .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres]   ; buffer = [économique .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres, économique]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres]   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres, et]   ; buffer = [monétaire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres]   ; buffer = [monétaire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, membres, monétaire]   ; buffer = [: .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[Etats, membres, monétaire]]   ; buffer = [: .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [: .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [:]   ; buffer = [dans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dans]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [pays .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pays .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pays]   ; buffer = [dotés .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dotés .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dotés]   ; buffer = [d' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [d' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [d']   ; buffer = [une .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [une .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [une]   ; buffer = [monnaie .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [monnaie .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [monnaie]   ; buffer = [stable .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [stable .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [stable]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [espoir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [espoir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [espoir]   ; buffer = [que .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [que .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [que]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [la]   ; buffer = [stabilité .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [stabilité .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [stabilité]   ; buffer = [du .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [du .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [du]   ; buffer = [pouvoir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pouvoir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pouvoir]   ; buffer = [d' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [d' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [d']   ; buffer = [achat .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [achat .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [achat]   ; buffer = [ne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ne]   ; buffer = [disparaisse .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [disparaisse .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [disparaisse]   ; buffer = [pas .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pas .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pas]   ; buffer = [avec .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [avec .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avec]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [union .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [union .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [économique .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, économique]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, et]   ; buffer = [monétaire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [monétaire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, monétaire]   ; buffer = [; .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[union, monétaire]]   ; buffer = [; .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [; .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [;]   ; buffer = [dans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dans]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [pays .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pays .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pays]   ; buffer = [qui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qui]   ; buffer = [connaissent .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [connaissent .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [connaissent]   ; buffer = [une .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [une .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [une]   ; buffer = [dépréciation .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dépréciation .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dépréciation]   ; buffer = [plus .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [plus .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [plus]   ; buffer = [ou .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ou .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ou]   ; buffer = [moins .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [moins .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [moins]   ; buffer = [forte .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [forte .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [forte]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [leur .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [leur .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [leur]   ; buffer = [monnaie .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [monnaie .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [monnaie]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [espoir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [espoir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [espoir]   ; buffer = [que .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [que .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [que]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [union .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [union .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [économique .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, économique]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, et]   ; buffer = [monétaire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union]   ; buffer = [monétaire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, monétaire]   ; buffer = [y .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, monétaire, y]   ; buffer = [mette .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [union, monétaire, y, mette]   ; buffer = [un .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[union, monétaire, y, mette]]   ; buffer = [un .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [un .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [un]   ; buffer = [terme .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [terme .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [terme]   ; buffer = [définitif .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [définitif .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [définitif]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12126
**Text:** Mais , fait plus important encore , seul un institut d' émission indépendant est en mesure de conduire une politique monétaire adaptée aux besoins à moyen et long terme .
###Existing MWEs: 
**MWE No.:** 1
**Text:** est en mesure



###Identified MWEs: 
**MWE No.:** 1
**Text:** fait institut d'


**MWE No.:** 2
**Text:** en conduire


**MWE No.:** 3
**Text:** long terme


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Mais .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Mais]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [fait .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [fait .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [plus .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, plus]   ; buffer = [important .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [important .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, important]   ; buffer = [encore .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [encore .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, encore]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, ,]   ; buffer = [seul .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [seul .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, seul]   ; buffer = [un .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [un .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, un]   ; buffer = [institut .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [institut .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, institut]   ; buffer = [d' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, institut, d']   ; buffer = [émission .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[fait, institut, d']]   ; buffer = [émission .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [émission .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [émission]   ; buffer = [indépendant .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [indépendant .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [indépendant]   ; buffer = [est .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [est .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [est]   ; buffer = [en .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [mesure .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, mesure]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, de]   ; buffer = [conduire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [conduire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, conduire]   ; buffer = [une .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[en, conduire]]   ; buffer = [une .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [une .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [une]   ; buffer = [politique .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [politique .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [politique]   ; buffer = [monétaire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [monétaire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [monétaire]   ; buffer = [adaptée .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [adaptée .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [adaptée]   ; buffer = [aux .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [aux .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [aux]   ; buffer = [besoins .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [besoins .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [besoins]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [moyen .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [moyen .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [moyen]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [long .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [long .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [long]   ; buffer = [terme .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [long, terme]   ; buffer = [.]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[long, terme]]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12137
**Text:** L' indépendance passe également par l' indépendance personnelle et professionnelle des membres des organes du système , c' est à dire des gouverneurs des banques centrales nationales comme des membres de l' organe supérieur de direction , à savoir du conseil de banques centrales européen .
###Existing MWEs: 
**MWE No.:** 0
**Text:** c' est à dire


**MWE No.:** 2
**Text:** à savoir



###Identified MWEs: 
**MWE No.:** 1
**Text:** à dire


**MWE No.:** 2
**Text:** banques centrales


**MWE No.:** 3
**Text:** savoir conseil de


**MWE No.:** 4
**Text:** banques centrales


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [L' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [L']   ; buffer = [indépendance .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [indépendance .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [indépendance]   ; buffer = [passe .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [passe .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [passe]   ; buffer = [également .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [également .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [également]   ; buffer = [par .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [par .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [par]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [indépendance .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [indépendance .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [indépendance]   ; buffer = [personnelle .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [personnelle .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [personnelle]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [professionnelle .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [professionnelle .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [professionnelle]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [membres .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [membres .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [membres]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [organes .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [organes .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [organes]   ; buffer = [du .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [du .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [du]   ; buffer = [système .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [système .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [système]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [c' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [c' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [c']   ; buffer = [est .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [est .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [est]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [dire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, dire]   ; buffer = [des .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[à, dire]]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [gouverneurs .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [gouverneurs .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [gouverneurs]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [banques .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [banques .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banques]   ; buffer = [centrales .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banques, centrales]   ; buffer = [nationales .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[banques, centrales]]   ; buffer = [nationales .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [nationales .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [nationales]   ; buffer = [comme .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [comme .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comme]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [membres .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [membres .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [membres]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [organe .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [organe .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [organe]   ; buffer = [supérieur .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [supérieur .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [supérieur]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [direction .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [direction .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [direction]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [savoir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [savoir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir]   ; buffer = [du .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, du]   ; buffer = [conseil .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir]   ; buffer = [conseil .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, conseil]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, conseil, de]   ; buffer = [banques .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[savoir, conseil, de]]   ; buffer = [banques .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [banques .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banques]   ; buffer = [centrales .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banques, centrales]   ; buffer = [européen .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[banques, centrales]]   ; buffer = [européen .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [européen .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [européen]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12138
**Text:** L' indépendance personnelle des membres des organes peut être garantie de la manière suivante : les personnalités nommées par les gouvernements -LRB- les gouverneurs des banques centrales -RRB- et par le Conseil -LRB- les membres du directoire -RRB- seraient en place pour une durée suffisamment longue -LRB- quatorze ans aux Etats - Unis , huit ans en Allemagne fédérale -RRB- et ne pourraient être démis de leur fonction au cours de cette période .
###Existing MWEs: 
**MWE No.:** 1
**Text:** seraient en place



###Identified MWEs: 
**MWE No.:** 1
**Text:** peut être garantie


**MWE No.:** 2
**Text:** banques centrales


**MWE No.:** 3
**Text:** en longue


**MWE No.:** 4
**Text:** Etats - Unis


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [L' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [L']   ; buffer = [indépendance .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [indépendance .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [indépendance]   ; buffer = [personnelle .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [personnelle .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [personnelle]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [membres .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [membres .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [membres]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [organes .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [organes .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [organes]   ; buffer = [peut .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [peut .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [peut]   ; buffer = [être .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [peut, être]   ; buffer = [garantie .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [peut, être, garantie]   ; buffer = [de .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[peut, être, garantie]]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [la]   ; buffer = [manière .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [manière .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [manière]   ; buffer = [suivante .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [suivante .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [suivante]   ; buffer = [: .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [: .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [:]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [personnalités .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [personnalités .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [personnalités]   ; buffer = [nommées .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [nommées .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [nommées]   ; buffer = [par .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [par .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [par]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [gouvernements .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [gouvernements .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [gouvernements]   ; buffer = [-LRB- .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [-LRB- .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [-LRB-]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [gouverneurs .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [gouverneurs .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [gouverneurs]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [banques .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [banques .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banques]   ; buffer = [centrales .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banques, centrales]   ; buffer = [-RRB- .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[banques, centrales]]   ; buffer = [-RRB- .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [-RRB- .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [-RRB-]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [par .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [par .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [par]   ; buffer = [le .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [le .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [le]   ; buffer = [Conseil .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Conseil .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Conseil]   ; buffer = [-LRB- .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [-LRB- .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [-LRB-]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [membres .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [membres .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [membres]   ; buffer = [du .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [du .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [du]   ; buffer = [directoire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [directoire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [directoire]   ; buffer = [-RRB- .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [-RRB- .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [-RRB-]   ; buffer = [seraient .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [seraient .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [seraient]   ; buffer = [en .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [place .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, place]   ; buffer = [pour .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [pour .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, pour]   ; buffer = [une .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [une .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, une]   ; buffer = [durée .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [durée .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, durée]   ; buffer = [suffisamment .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [suffisamment .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, suffisamment]   ; buffer = [longue .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [longue .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, longue]   ; buffer = [-LRB- .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[en, longue]]   ; buffer = [-LRB- .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [-LRB- .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [-LRB-]   ; buffer = [quatorze .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [quatorze .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [quatorze]   ; buffer = [ans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ans]   ; buffer = [aux .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [aux .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [aux]   ; buffer = [Etats .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Etats .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats]   ; buffer = [- .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, -]   ; buffer = [Unis .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats, -, Unis]   ; buffer = [, .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[Etats, -, Unis]]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [huit .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [huit .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [huit]   ; buffer = [ans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ans]   ; buffer = [en .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [Allemagne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Allemagne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Allemagne]   ; buffer = [fédérale .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [fédérale .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fédérale]   ; buffer = [-RRB- .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [-RRB- .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [-RRB-]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [ne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ne]   ; buffer = [pourraient .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pourraient .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pourraient]   ; buffer = [être .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [être .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [être]   ; buffer = [démis .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [démis .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [démis]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [leur .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [leur .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [leur]   ; buffer = [fonction .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [fonction .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction]   ; buffer = [au .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction, au]   ; buffer = [cours .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction]   ; buffer = [cours .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction, cours]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction, de]   ; buffer = [cette .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction]   ; buffer = [cette .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction, cette]   ; buffer = [période .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction]   ; buffer = [période .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction, période]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction]   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction, .]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fonction]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12141
**Text:** Il s' agit tout compte fait de ce que Adolf Weber qualifiait de " continuité de l' expérience , de la responsabilité et de la compétence " dans la discussion concernant la nouvelle loi sur la Bundesbank au début des années 50 .
###Existing MWEs: 
**MWE No.:** 0
**Text:** tout compte fait



###Identified MWEs: 
**MWE No.:** 1
**Text:** fait loi


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Il .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Il]   ; buffer = [s' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [s' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [s']   ; buffer = [agit .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [agit .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [agit]   ; buffer = [tout .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [tout .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tout]   ; buffer = [compte .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [compte .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [compte]   ; buffer = [fait .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [fait .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, de]   ; buffer = [ce .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [ce .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, ce]   ; buffer = [que .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [que .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, que]   ; buffer = [Adolf .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [Adolf .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, Adolf]   ; buffer = [Weber .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [Weber .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, Weber]   ; buffer = [qualifiait .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [qualifiait .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, qualifiait]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, de]   ; buffer = [" .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [" .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, "]   ; buffer = [continuité .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [continuité .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, continuité]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, de]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, l']   ; buffer = [expérience .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [expérience .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, expérience]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, ,]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, de]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, la]   ; buffer = [responsabilité .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [responsabilité .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, responsabilité]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, et]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, de]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, la]   ; buffer = [compétence .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [compétence .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, compétence]   ; buffer = [" .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [" .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, "]   ; buffer = [dans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [dans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, dans]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, la]   ; buffer = [discussion .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [discussion .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, discussion]   ; buffer = [concernant .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [concernant .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, concernant]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, la]   ; buffer = [nouvelle .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [nouvelle .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, nouvelle]   ; buffer = [loi .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [loi .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, loi]   ; buffer = [sur .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[fait, loi]]   ; buffer = [sur .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sur .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sur]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [la]   ; buffer = [Bundesbank .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Bundesbank .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Bundesbank]   ; buffer = [au .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [au .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [au]   ; buffer = [début .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [début .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [début]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [années .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [années .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [années]   ; buffer = [50 .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [50 .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [50]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12143
**Text:** ...tant donné qu' il ne peut y avoir pour la Communauté dans son ensemble qu' une politique monétaire d' un seul tenant , autrement dit que la politique monétaire ne peut pas tenir compte des exigences particulières de chaque Etat et de chaque région , les gouverneurs et les membres des directoires des banques centrales doivent se sentir obligés de servir l' intérêt commun et non celui des différents Etats ou régions , et cela doit tenir lieu de règle lors des prises de décisions .
###Existing MWEs: 
**MWE No.:** 0
**Text:** ...tant donné qu'


**MWE No.:** 2
**Text:** autrement dit


**MWE No.:** 4
**Text:** tenir compte


**MWE No.:** 6
**Text:** tenir lieu



###Identified MWEs: 
**MWE No.:** 1
**Text:** donné peut y avoir


**MWE No.:** 2
**Text:** tenant tenir compte


**MWE No.:** 3
**Text:** banques centrales


**MWE No.:** 4
**Text:** tenir lieu


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [...tant .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [...tant]   ; buffer = [donné .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [donné .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [donné]   ; buffer = [qu' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [donné, qu']   ; buffer = [il .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [donné]   ; buffer = [il .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [donné, il]   ; buffer = [ne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [donné]   ; buffer = [ne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [donné, ne]   ; buffer = [peut .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [donné]   ; buffer = [peut .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [donné, peut]   ; buffer = [y .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [donné, peut, y]   ; buffer = [avoir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [donné, peut, y, avoir]   ; buffer = [pour .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[donné, peut, y, avoir]]   ; buffer = [pour .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pour .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pour]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [la]   ; buffer = [Communauté .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Communauté .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Communauté]   ; buffer = [dans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dans]   ; buffer = [son .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [son .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [son]   ; buffer = [ensemble .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ensemble .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ensemble]   ; buffer = [qu' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qu' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qu']   ; buffer = [une .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [une .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [une]   ; buffer = [politique .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [politique .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [politique]   ; buffer = [monétaire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [monétaire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [monétaire]   ; buffer = [d' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [d' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [d']   ; buffer = [un .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [un .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [un]   ; buffer = [seul .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [seul .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [seul]   ; buffer = [tenant .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [tenant .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant]   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, ,]   ; buffer = [autrement .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant]   ; buffer = [autrement .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, autrement]   ; buffer = [dit .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, autrement, dit]   ; buffer = [que .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, autrement]   ; buffer = [que .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, autrement, que]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, autrement]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant]   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, la]   ; buffer = [politique .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant]   ; buffer = [politique .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, politique]   ; buffer = [monétaire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant]   ; buffer = [monétaire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, monétaire]   ; buffer = [ne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant]   ; buffer = [ne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, ne]   ; buffer = [peut .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant]   ; buffer = [peut .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, peut]   ; buffer = [pas .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant]   ; buffer = [pas .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, pas]   ; buffer = [tenir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant]   ; buffer = [tenir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, tenir]   ; buffer = [compte .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenant, tenir, compte]   ; buffer = [des .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[tenant, tenir, compte]]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [exigences .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [exigences .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [exigences]   ; buffer = [particulières .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [particulières .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [particulières]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [chaque .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [chaque .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [chaque]   ; buffer = [Etat .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Etat .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etat]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [chaque .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [chaque .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [chaque]   ; buffer = [région .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [région .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [région]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [gouverneurs .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [gouverneurs .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [gouverneurs]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [membres .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [membres .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [membres]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [directoires .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [directoires .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [directoires]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [banques .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [banques .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banques]   ; buffer = [centrales .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banques, centrales]   ; buffer = [doivent .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[banques, centrales]]   ; buffer = [doivent .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [doivent .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [doivent]   ; buffer = [se .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [se .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [se]   ; buffer = [sentir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sentir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sentir]   ; buffer = [obligés .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [obligés .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [obligés]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [servir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [servir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [servir]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [intérêt .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [intérêt .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [intérêt]   ; buffer = [commun .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [commun .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [commun]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [non .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [non .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [non]   ; buffer = [celui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [celui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [celui]   ; buffer = [des .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [des]   ; buffer = [différents .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [différents .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [différents]   ; buffer = [Etats .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Etats .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Etats]   ; buffer = [ou .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ou .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ou]   ; buffer = [régions .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [régions .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [régions]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [cela .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [cela .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [cela]   ; buffer = [doit .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [doit .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [doit]   ; buffer = [tenir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [tenir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenir]   ; buffer = [lieu .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tenir, lieu]   ; buffer = [de .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[tenir, lieu]]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [règle .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [règle .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [règle]   ; buffer = [lors .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [lors .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors]   ; buffer = [des .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors, des]   ; buffer = [prises .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors]   ; buffer = [prises .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors, prises]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors, de]   ; buffer = [décisions .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors]   ; buffer = [décisions .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors, décisions]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors]   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors, .]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lors]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12144
**Text:** Il convient avant tout de garantir l' autonomie du système en ce qui concerne l' emploi de ses instruments , c' est à dire sa capacité d' accomplir sans entraves sa mission , qui consiste à préserver la stabilité monétaire en utilisant les instruments nécessaires .
###Existing MWEs: 
**MWE No.:** 1
**Text:** en ce qui concerne


**MWE No.:** 2
**Text:** c' est à dire



###Identified MWEs: 
**MWE No.:** 1
**Text:** avant autonomie


**MWE No.:** 2
**Text:** en concerne


**MWE No.:** 3
**Text:** à dire


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Il .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Il]   ; buffer = [convient .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [convient .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [convient]   ; buffer = [avant .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [avant .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avant]   ; buffer = [tout .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avant, tout]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avant]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avant, de]   ; buffer = [garantir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avant]   ; buffer = [garantir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avant, garantir]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avant]   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avant, l']   ; buffer = [autonomie .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avant]   ; buffer = [autonomie .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [avant, autonomie]   ; buffer = [du .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[avant, autonomie]]   ; buffer = [du .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [du .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [du]   ; buffer = [système .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [système .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [système]   ; buffer = [en .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [ce .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, ce]   ; buffer = [qui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, qui]   ; buffer = [concerne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [concerne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, concerne]   ; buffer = [l' .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[en, concerne]]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [emploi .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [emploi .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [emploi]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [ses .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ses .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ses]   ; buffer = [instruments .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [instruments .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [instruments]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [c' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [c' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [c']   ; buffer = [est .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [est .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [est]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [dire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à, dire]   ; buffer = [sa .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[à, dire]]   ; buffer = [sa .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sa .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sa]   ; buffer = [capacité .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [capacité .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [capacité]   ; buffer = [d' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [d' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [d']   ; buffer = [accomplir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [accomplir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [accomplir]   ; buffer = [sans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sans]   ; buffer = [entraves .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [entraves .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [entraves]   ; buffer = [sa .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sa .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sa]   ; buffer = [mission .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [mission .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mission]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [qui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qui]   ; buffer = [consiste .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [consiste .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [consiste]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [préserver .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [préserver .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [préserver]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [la]   ; buffer = [stabilité .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [stabilité .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [stabilité]   ; buffer = [monétaire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [monétaire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [monétaire]   ; buffer = [en .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [utilisant .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [utilisant .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [utilisant]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [instruments .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [instruments .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [instruments]   ; buffer = [nécessaires .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [nécessaires .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [nécessaires]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12148
**Text:** Mais la panoplie d' instruments doit aussi comprendre tous les autres moyens dont une banque centrale moderne a besoin pour mener son action , qu' ils soient ou non mis en oeuvre à l' heure actuelle dans les différents pays .
###Existing MWEs: 
**MWE No.:** 1
**Text:** a besoin


**MWE No.:** 2
**Text:** mis en oeuvre



###Identified MWEs: 
**MWE No.:** 1
**Text:** banque centrale


**MWE No.:** 2
**Text:** mener ils soient mis en oeuvre


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Mais .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Mais]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [la]   ; buffer = [panoplie .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [panoplie .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [panoplie]   ; buffer = [d' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [d' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [d']   ; buffer = [instruments .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [instruments .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [instruments]   ; buffer = [doit .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [doit .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [doit]   ; buffer = [aussi .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [aussi .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [aussi]   ; buffer = [comprendre .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [comprendre .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comprendre]   ; buffer = [tous .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [tous .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [tous]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [autres .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [autres .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [autres]   ; buffer = [moyens .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [moyens .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [moyens]   ; buffer = [dont .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dont .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dont]   ; buffer = [une .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [une .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [une]   ; buffer = [banque .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [banque .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banque]   ; buffer = [centrale .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banque, centrale]   ; buffer = [moderne .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[banque, centrale]]   ; buffer = [moderne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [moderne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [moderne]   ; buffer = [a .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [a .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [a]   ; buffer = [besoin .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [besoin .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [besoin]   ; buffer = [pour .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pour .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pour]   ; buffer = [mener .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [mener .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener]   ; buffer = [son .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, son]   ; buffer = [action .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener]   ; buffer = [action .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, action]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener]   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, ,]   ; buffer = [qu' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener]   ; buffer = [qu' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, qu']   ; buffer = [ils .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener]   ; buffer = [ils .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, ils]   ; buffer = [soient .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, ils, soient]   ; buffer = [ou .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, ils, soient, ou]   ; buffer = [non .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, ils, soient]   ; buffer = [non .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, ils, soient, non]   ; buffer = [mis .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, ils, soient]   ; buffer = [mis .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, ils, soient, mis]   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, ils, soient, mis, en]   ; buffer = [oeuvre .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [mener, ils, soient, mis, en, oeuvre]   ; buffer = [à .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[mener, ils, soient, mis, en, oeuvre]]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [l']   ; buffer = [heure .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [heure .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [heure]   ; buffer = [actuelle .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [actuelle .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [actuelle]   ; buffer = [dans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dans]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [différents .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [différents .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [différents]   ; buffer = [pays .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pays .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pays]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12158
**Text:** Je n' en veux pour preuve que les réactions , parfois très critiques , qui se sont fait entendre à propos du rapport Delors , surtout en ce qui concerne les propositions relatives à la deuxième étape , qui sont en effet restées plutôt vagues et qui posent plus de questions qu' elles n' apportent de réponses .
###Existing MWEs: 
**MWE No.:** 0
**Text:** fait entendre


**MWE No.:** 2
**Text:** en ce qui concerne



###Identified MWEs: 
**MWE No.:** 1
**Text:** en réactions


**MWE No.:** 2
**Text:** fait entendre


**MWE No.:** 3
**Text:** rapport Delors


**MWE No.:** 4
**Text:** en relatives


**MWE No.:** 5
**Text:** en plutôt


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Je .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Je]   ; buffer = [n' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [n' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [n']   ; buffer = [en .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [veux .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, veux]   ; buffer = [pour .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [pour .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, pour]   ; buffer = [preuve .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [preuve .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, preuve]   ; buffer = [que .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [que .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, que]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, les]   ; buffer = [réactions .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [réactions .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, réactions]   ; buffer = [, .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[en, réactions]]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [parfois .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [parfois .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [parfois]   ; buffer = [très .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [très .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [très]   ; buffer = [critiques .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [critiques .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [critiques]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [qui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qui]   ; buffer = [se .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [se .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [se]   ; buffer = [sont .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sont .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sont]   ; buffer = [fait .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [fait .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait]   ; buffer = [entendre .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [fait, entendre]   ; buffer = [à .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[fait, entendre]]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [propos .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [propos .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [propos]   ; buffer = [du .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [du .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [du]   ; buffer = [rapport .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [rapport .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [rapport]   ; buffer = [Delors .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [rapport, Delors]   ; buffer = [, .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[rapport, Delors]]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [surtout .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [surtout .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [surtout]   ; buffer = [en .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [ce .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, ce]   ; buffer = [qui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, qui]   ; buffer = [concerne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [concerne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, concerne]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, les]   ; buffer = [propositions .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [propositions .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, propositions]   ; buffer = [relatives .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [relatives .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, relatives]   ; buffer = [à .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[en, relatives]]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [la]   ; buffer = [deuxième .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [deuxième .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [deuxième]   ; buffer = [étape .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [étape .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [étape]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [qui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qui]   ; buffer = [sont .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sont .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sont]   ; buffer = [en .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [en .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [effet .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, effet]   ; buffer = [restées .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [restées .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, restées]   ; buffer = [plutôt .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en]   ; buffer = [plutôt .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [en, plutôt]   ; buffer = [vagues .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[en, plutôt]]   ; buffer = [vagues .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [vagues .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [vagues]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [qui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qui]   ; buffer = [posent .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [posent .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [posent]   ; buffer = [plus .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [plus .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [plus]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [questions .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [questions .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [questions]   ; buffer = [qu' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qu' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qu']   ; buffer = [elles .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [elles .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [elles]   ; buffer = [n' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [n' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [n']   ; buffer = [apportent .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [apportent .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [apportent]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [réponses .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [réponses .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [réponses]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12159
**Text:** Ne lit -on pas au sujet de la deuxième étape : " à ce stade , le comité ne juge pas possible de proposer un projet détaillé pour l' accomplissement de cette transition " , à savoir le passage de la première à la deuxième étape dans le domaine monétaire .
###Existing MWEs: 
**MWE No.:** 2
**Text:** à savoir



###Identified MWEs: 
**MWE No.:** 1
**Text:** comité accomplissement transition


**MWE No.:** 2
**Text:** savoir passage deuxième


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Ne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Ne]   ; buffer = [lit .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [lit .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [lit]   ; buffer = [-on .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [-on .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [-on]   ; buffer = [pas .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [pas .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [pas]   ; buffer = [au .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [au .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [au]   ; buffer = [sujet .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [sujet .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [sujet]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [la]   ; buffer = [deuxième .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [deuxième .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [deuxième]   ; buffer = [étape .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [étape .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [étape]   ; buffer = [: .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [: .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [:]   ; buffer = [" .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [" .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = ["]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [ce .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ce .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [ce]   ; buffer = [stade .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [stade .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [stade]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [le .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [le .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [le]   ; buffer = [comité .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [comité .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [ne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, ne]   ; buffer = [juge .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [juge .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, juge]   ; buffer = [pas .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [pas .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, pas]   ; buffer = [possible .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [possible .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, possible]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, de]   ; buffer = [proposer .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [proposer .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, proposer]   ; buffer = [un .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [un .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, un]   ; buffer = [projet .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [projet .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, projet]   ; buffer = [détaillé .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [détaillé .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, détaillé]   ; buffer = [pour .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [pour .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, pour]   ; buffer = [l' .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [l' .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, l']   ; buffer = [accomplissement .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité]   ; buffer = [accomplissement .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, accomplissement]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, accomplissement, de]   ; buffer = [cette .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, accomplissement]   ; buffer = [cette .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, accomplissement, cette]   ; buffer = [transition .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, accomplissement]   ; buffer = [transition .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [comité, accomplissement, transition]   ; buffer = [" .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[comité, accomplissement, transition]]   ; buffer = [" .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [" .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = ["]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [à]   ; buffer = [savoir .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [savoir .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir]   ; buffer = [le .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, le]   ; buffer = [passage .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir]   ; buffer = [passage .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage]   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage, de]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage]   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage, la]   ; buffer = [première .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage]   ; buffer = [première .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage, première]   ; buffer = [à .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage]   ; buffer = [à .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage, à]   ; buffer = [la .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage]   ; buffer = [la .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage, la]   ; buffer = [deuxième .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage]   ; buffer = [deuxième .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [savoir, passage, deuxième]   ; buffer = [étape .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[savoir, passage, deuxième]]   ; buffer = [étape .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [étape .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [étape]   ; buffer = [dans .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [dans .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [dans]   ; buffer = [le .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [le .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [le]   ; buffer = [domaine .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [domaine .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [domaine]   ; buffer = [monétaire .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [monétaire .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [monétaire]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


##Sentence No. 12169
**Text:** Il y a une autre question qui a souvent été soulevée par les Français et les Britanniques , et qui concerne le " contrôle démocratique " du système européen de banques centrales .
###Existing MWEs: 
**MWE No.:** 0
**Text:** Il y a



###Identified MWEs: 
**MWE No.:** 1
**Text:** Il y a


**MWE No.:** 2
**Text:** banques centrales


Trans&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp;Configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Il .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Il]   ; buffer = [y .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Il, y]   ; buffer = [a .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Il, y, a]   ; buffer = [une .. ]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[Il, y, a]]   ; buffer = [une .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [une .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [une]   ; buffer = [autre .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [autre .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [autre]   ; buffer = [question .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [question .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [question]   ; buffer = [qui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qui]   ; buffer = [a .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [a .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [a]   ; buffer = [souvent .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [souvent .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [souvent]   ; buffer = [été .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [été .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [été]   ; buffer = [soulevée .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [soulevée .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [soulevée]   ; buffer = [par .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [par .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [par]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [Français .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Français .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Français]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [les .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [les .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [les]   ; buffer = [Britanniques .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [Britanniques .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [Britanniques]   ; buffer = [, .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [, .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [,]   ; buffer = [et .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [et .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [et]   ; buffer = [qui .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [qui .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [qui]   ; buffer = [concerne .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [concerne .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [concerne]   ; buffer = [le .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [le .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [le]   ; buffer = [" .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [" .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = ["]   ; buffer = [contrôle .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [contrôle .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [contrôle]   ; buffer = [démocratique .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [démocratique .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [démocratique]   ; buffer = [" .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [" .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = ["]   ; buffer = [du .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [du .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [du]   ; buffer = [système .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [système .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [système]   ; buffer = [européen .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [européen .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [européen]   ; buffer = [de .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [de .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [de]   ; buffer = [banques .. ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [banques .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banques]   ; buffer = [centrales .. ]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [banques, centrales]   ; buffer = [.]

**MERGE**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [[banques, centrales]]   ; buffer = [.]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [.]

SHIFT&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = [.]   ; buffer = [ ]

COMPLETE&nbsp;&nbsp;&nbsp;>&nbsp;&nbsp;&nbsp; stack = []   ; buffer = [ ]


