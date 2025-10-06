## SocialConversationFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin`

```diff

-3300.80.1.0.0
-  __TEXT.__text: 0x2eb04
-  __TEXT.__auth_stubs: 0x1d40
-  __TEXT.__cstring: 0x22cd
-  __TEXT.__const: 0x11e2
-  __TEXT.__constg_swiftt: 0xcf0
-  __TEXT.__swift5_typeref: 0x68a
-  __TEXT.__swift5_reflstr: 0x613
-  __TEXT.__swift5_fieldmd: 0x6f4
+3302.12.1.0.0
+  __TEXT.__text: 0x3e68c
+  __TEXT.__auth_stubs: 0x2130
+  __TEXT.__cstring: 0x377d
+  __TEXT.__const: 0x1522
+  __TEXT.__constg_swiftt: 0xf30
+  __TEXT.__swift5_typeref: 0x7ae
+  __TEXT.__swift5_reflstr: 0x6c2
+  __TEXT.__swift5_fieldmd: 0x850
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0x8c
-  __TEXT.__swift5_types: 0x88
+  __TEXT.__swift5_proto: 0xa8
+  __TEXT.__swift5_types: 0xac
   __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0x48b
+  __TEXT.__objc_methname: 0x4a3
   __TEXT.__objc_methtype: 0x1a8
-  __TEXT.__swift5_capture: 0xdc
+  __TEXT.__swift5_capture: 0xfc
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x95c
-  __TEXT.__eh_frame: 0x12d0
-  __DATA_CONST.__auth_got: 0xea0
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x1018
-  __DATA_CONST.__objc_classlist: 0xa8
+  __TEXT.__unwind_info: 0x11cc
+  __TEXT.__eh_frame: 0x1688
+  __DATA_CONST.__auth_got: 0x1098
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__auth_ptr: 0xb0
+  __DATA_CONST.__const: 0x1420
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1928
-  __DATA.__objc_selrefs: 0x110
+  __DATA.__objc_const: 0x1be8
+  __DATA.__objc_selrefs: 0x120
   __DATA.__objc_protorefs: 0x50
   __DATA.__objc_classrefs: 0x90
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x23e8
-  __DATA.__common: 0x100
-  __DATA.__bss: 0xf80
+  __DATA.__data: 0x3c30
+  __DATA.__common: 0x108
+  __DATA.__bss: 0x1300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents

   - /System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration
   - /System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology
   - /System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf
+  - /System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers
   - /System/Library/PrivateFrameworks/SiriSocialConversation.framework/SiriSocialConversation
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F0BA1E3F-24AB-31F0-AF54-9A55F9C3613F
-  Functions: 723
-  Symbols:   147
-  CStrings:  328
+  UUID: BF0AF3AF-AD26-32C5-AAA7-EE42C54A7E3E
+  Functions: 888
+  Symbols:   149
+  CStrings:  478
 
Symbols:
+ _swift_retain_n
+ _swift_stdlib_random
CStrings:
+ "%s returning a match for event %s"
+ "Attempting to access allGames before initialzing PlayWithMe"
+ "Attempting to reinitialize PlayWithMeData!"
+ "Could not convert user dialog act to tasks: %s"
+ "Failed to donate variable state: %s"
+ "Failed to encode flow variables for persisting"
+ "Failed to restore donated variable state: %@"
+ "NLv4 producer returning a value SDA for %s"
+ "NLv4 supported intent: %s"
+ "Name does not match: %s vs %s"
+ "Name matched: %s"
+ "No previously donated variable state found for %s"
+ "No task in userDialogAct. Will not parse: %s"
+ "No valid configuration found for NLv4 producer for %s. Returning empty UsoGraph."
+ "Not a USO Parse...will not process"
+ "Overwriting greeting intents"
+ "Retrieved donated state for %ld variable(s)"
+ "Successfully donated variable state for %s"
+ "USO entityName match failed: %s vs %s"
+ "USO entityName matched: %s"
+ "USO search qualifier defined value match failed: %s vs %s"
+ "USO search qualifier defined value matched: %s"
+ "USO verb match failed: %s vs %s"
+ "USO verb matched: %s"
+ "Unable to convert [String: Any] to [String: JSONValue]"
+ "Unable to convert [String: JSONValue] to [String: Any] for %s"
+ "Unable to get unique UDA from userParse. Will not parse: %s"
+ "Unable to write USO protobuf graph: %s"
+ "Unrecognized condition: %s"
+ "Unsupported graphName found in NLv4 producer: %s"
+ "_TtC36SocialConversationFlowDelegatePlugin14PlayWithMeData"
+ "_TtC36SocialConversationFlowDelegatePlugin19NLv4UserInputParser"
+ "_TtCC36SocialConversationFlowDelegatePlugin14PlayWithMeData9Constants"
+ "alwaysListeningToMe"
+ "askSiriAQuestion"
+ "canIDoViolentAction"
+ "dalAlSalamAleykoum"
+ "dalAnswerYoureWelcome"
+ "dalAprilFoolsPranks"
+ "dalAprilFoolsSiri"
+ "dalAreYouAlwaysListening"
+ "dalAreYouFasting"
+ "dalAreYouWorking"
+ "dalAskMeSomething"
+ "dalAssistantGoodJob"
+ "dalCanITellYouAJoke"
+ "dalChineseNewYearGreetings"
+ "dalCongratulations"
+ "dalDeckTheHallsWithBoughsOfHolly"
+ "dalDoSomethingBadToYou"
+ "dalDoYouForgiveMe"
+ "dalDoYouRespectMe"
+ "dalDoYouWantToKissMe"
+ "dalDoYouWorkForApple"
+ "dalFlipACoinSeriously"
+ "dalGamesUnderConstruction"
+ "dalGenderProfanityAtSiri"
+ "dalGiveMeACompliment"
+ "dalGoodAfternoon"
+ "dalHappyBirthday"
+ "dalHappyBirthdayToSiri"
+ "dalHappyBlackHistoryMonth"
+ "dalHappyHolidays"
+ "dalHelloHowAreYou"
+ "dalHelloOtherAssistant"
+ "dalInappropriateSexualityGender"
+ "dalKnockKnockAdvanced"
+ "dalKnockKnockJoke"
+ "dalKnockKnockRedirect"
+ "dalLetsWashHands"
+ "dalLookAfterYourself"
+ "dalLunarNewYearGreetings"
+ "dalMerryChristmas"
+ "dalNiceToMeetYou"
+ "dalPhilosophyJokes"
+ "dalProfanityAtSiri"
+ "dalPromptedAdmonishment"
+ "dalRandomPalindrome"
+ "dalRespectPrivacy"
+ "dalRockPaperScissor"
+ "dalSexualRequest"
+ "dalSexuallyHarassSiri"
+ "dalSpeakHalloweenPoetry"
+ "dalSpeakValentinesDayPoetry"
+ "dalSpeakWinterHolidayPoetry"
+ "dalTalkLikeAPirate"
+ "dalTalkLikeShakespeare"
+ "dalTellABedtimeStory"
+ "dalTellAScaryStory"
+ "dalTellAScaryStoryFollowUp"
+ "dalTellMeARiddle"
+ "dalTellMeASonnet"
+ "dalTellMeYourSecret"
+ "dalTellMyHoroscope"
+ "dalTongueTwister"
+ "dalValentinesDayRap"
+ "dalWhatAreYouDoing"
+ "dalWhyDidTheChicken"
+ "dalWillYouMarryMe"
+ "dalWinterHolidayRap"
+ "doSomethingBadToSiri"
+ "flipACoinSeriously"
+ "fullSpeak"
+ "gameSets"
+ "games"
+ "genderProfanityAtSiri"
+ "genericHappyHolidays"
+ "genericProfanity"
+ "happyBirthdayToYou"
+ "happyBlackHistoryMonth"
+ "happyChineseNewYear"
+ "happyLunarNewYear"
+ "hearKnockknockjoke"
+ "helloOtherAssistant"
+ "impossibleActionForSiri"
+ "impossibleRequest"
+ "initialized"
+ "knockKnockWhosThere"
+ "like_common_SiriContent"
+ "makeGraph(responseId:sourceIdentifier:parameters:)"
+ "moreContinuation"
+ "notProfaneSexualAction"
+ "perform_common_SiriSocialAction"
+ "playRockPaperScissors"
+ "playUncategorizedGame"
+ "playWithMeData"
+ "playWithMeSection"
+ "possibleActionForSiri"
+ "presentedIndex"
+ "profaneSexualAction"
+ "salutationPhrase"
+ "searchQualifierDefinedValue"
+ "setFullSpeak:"
+ "shakespeareTalklike"
+ "shuffledGameSets"
+ "shuffledGames"
+ "siriHurtMyFeelings"
+ "siriSocialAction"
+ "socialInterjectionPhrase"
+ "tell_common_SiriContent"
+ "uncategorizedViolentAction"
+ "unlike_common_SiriContent"
+ "userSocialAction"
+ "usoSearchQualifier"
+ "valentinesDayJoke"
+ "valentinesDayPoem"
+ "valentinesDayRap"
+ "violentActionToSiri"
+ "whyDidTheChicken"
+ "winterHolidayPoem"
+ "winterHolidayRap"
- "Executing new greeting flow"

```
