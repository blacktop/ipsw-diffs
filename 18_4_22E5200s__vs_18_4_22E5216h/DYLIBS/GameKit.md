## GameKit

> `/System/Library/Frameworks/GameKit.framework/GameKit`

```diff

-819.4.25.2.1
-  __TEXT.__text: 0x2f11c
-  __TEXT.__auth_stubs: 0x1400
-  __TEXT.__objc_methlist: 0x620
+819.4.37.0.0
+  __TEXT.__text: 0x3452c
+  __TEXT.__auth_stubs: 0x1560
+  __TEXT.__objc_methlist: 0x68c
   __TEXT.__const: 0x668
-  __TEXT.__cstring: 0xe16
-  __TEXT.__swift5_typeref: 0x81d
-  __TEXT.__swift5_capture: 0x29c
-  __TEXT.__oslogstring: 0x24
+  __TEXT.__cstring: 0xf16
+  __TEXT.__swift5_typeref: 0x861
+  __TEXT.__swift5_capture: 0x32c
+  __TEXT.__oslogstring: 0x2b8
   __TEXT.__constg_swiftt: 0x1ec
   __TEXT.__swift5_fieldmd: 0x11c
   __TEXT.__swift5_reflstr: 0x106

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x40
-  __TEXT.__swift_as_entry: 0xc0
-  __TEXT.__swift_as_ret: 0xe8
-  __TEXT.__unwind_info: 0xc60
-  __TEXT.__eh_frame: 0x2084
+  __TEXT.__swift_as_entry: 0xe0
+  __TEXT.__swift_as_ret: 0x104
+  __TEXT.__unwind_info: 0xda8
+  __TEXT.__eh_frame: 0x25bc
   __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0xf33
-  __TEXT.__objc_methtype: 0x88
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x1a8
+  __TEXT.__objc_methname: 0x10aa
+  __TEXT.__objc_methtype: 0x93
+  __TEXT.__objc_stubs: 0x3a0
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x458
-  __AUTH_CONST.__auth_got: 0xa08
-  __AUTH_CONST.__auth_ptr: 0x2b0
-  __AUTH_CONST.__const: 0x880
+  __DATA_CONST.__objc_selrefs: 0x4d0
+  __AUTH_CONST.__auth_got: 0xab8
+  __AUTH_CONST.__auth_ptr: 0x2c8
+  __AUTH_CONST.__const: 0x9e8
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0xdf0
+  __AUTH_CONST.__objc_const: 0xe30
   __AUTH.__objc_data: 0x580
   __AUTH.__data: 0xf0
-  __DATA.__data: 0x798
+  __DATA.__data: 0x860
   __DATA.__bss: 0xee8
-  __DATA.__common: 0x50
+  __DATA.__common: 0x68
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/ReplayKit.framework/ReplayKit
   - /System/Library/Frameworks/SceneKit.framework/SceneKit
   - /System/Library/Frameworks/SpriteKit.framework/SpriteKit
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation
   - /System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI
   - /System/Library/PrivateFrameworks/GameCenterUICore.framework/GameCenterUICore

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 785
-  Symbols:   249
-  CStrings:  294
+  Functions: 853
+  Symbols:   262
+  CStrings:  331
 
Symbols:
+ _OBJC_CLASS_$_AMSMediaArtwork
+ _OBJC_CLASS_$_GKMatch
+ _OBJC_CLASS_$_GKMatchRequest
+ _OBJC_CLASS_$_GKMatchmaker
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
CStrings:
+ "@100@0:8@16@24@32@40B48@52@60@68@76@84q92"
+ "@188@0:8@16@24@32Q40@48@56@64@72@80d88@96@104@112B120@124@132@140@148@156@164@172^@180"
+ "@24@0:8^@16"
+ "@32@0:8@16^@24"
+ "@40@0:8@16@24^@32"
+ "Cannot cast loaded activities to [GKGameActivity]."
+ "Failed to end game activity: last resume date is nil."
+ "Failed to initialize GKGameActivity: %@"
+ "Failed to pause game activity: last resume date is nil."
+ "Failed to report achievements on activity end, due to error: %s"
+ "Failed to report score on activity end for leaderboard %s, due to error: %s"
+ "Invalid game activity definition."
+ "Invalid party code provided."
+ "Invalid progress complete value provided."
+ "Invalid referral found for game activity."
+ "Party code is not supported for this activity."
+ "T@\"NSURL\",N,R,VimageUrl"
+ "Tq,N,R,VplayStyle"
+ "Unknown referral found for game activity."
+ "consumptionState"
+ "findMatchForRequest:withCompletionHandler:"
+ "findPlayersForHostedMatchWithCompletionHandler:"
+ "findPlayersForHostedRequest:withCompletionHandler:"
+ "gameHasProcessedGameActivity:"
+ "getScoreOnLeaderboard:"
+ "imageUrl"
+ "initWithActivityIdentifier:activityDefinition:properties:state:partyCode:creationDate:startDate:lastResumeDate:endDate:duration:associatedAchievements:associatedLeaderboardScores:creator:initiatedByApple:referralLeaderboard:referralAchievement:participants:participantStates:shortGroupID:consumptionState:support:error:"
+ "initWithIdentifier:groupIdentifier:title:details:attemptLimitOptions:durationOptions:leaderboard:imageUrl:"
+ "initWithIdentifier:groupIdentifier:title:details:supportPartyCode:fallbackURL:maxPlayers:minPlayers:defaultProperties:imageTemplateURL:playStyle:"
+ "loadGameActivityDefinitionsWith:completionHandler:"
+ "loadGameActivityDefinitionsWithIDs:completionHandler:"
+ "markAsProcessed"
+ "removeAchievements:"
+ "removeScoresFromLeaderboards:"
+ "setAchievementCompleted:"
+ "setPlayerGroup:"
+ "setProgressOnAchievement:toPercentComplete:"
+ "setScoreOnLeaderboard:toScore:"
+ "setScoreOnLeaderboard:toScore:context:"
+ "setupMatchRequestAndReturnError:"
+ "sharedMatchmaker"
+ "shortGroupID"
+ "startWithDefinition:error:"
+ "startWithDefinition:partyCode:error:"
+ "v24@0:8@?<v@?@\"GKMatch\"@\"NSError\">16"
+ "v24@?0@\"GKMatch\"8@\"NSError\"16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@16d24"
+ "v32@0:8@16q24"
+ "v40@0:8@16q24q32"
- "@172@0:8@16@24@32Q40@48@56@64@72@80d88@96@104@112B120@124@132@140@148@156^@164"
- "@92@0:8@16@24@32@40B48@52@60@68@76@84"
- "initWithActivityIdentifier:activityDefinition:properties:state:partyCode:creationDate:startDate:lastResumeDate:endDate:duration:associatedAchievements:associatedLeaderboardScores:creator:initiatedByApple:referralLeaderboard:referralAchievement:participants:participantStates:support:error:"
- "initWithIdentifier:groupIdentifier:title:details:attemptLimitOptions:durationOptions:leaderboard:imageTemplateURL:"
- "initWithIdentifier:groupIdentifier:title:details:supportPartyCode:fallbackURL:maxPlayers:minPlayers:defaultProperties:imageTemplateURL:"
- "removeAchievements:forPlayer:"
- "removeScoresFromLeaderboards:forPlayer:"
- "setAchievementCompleted:forPlayer:"
- "setProgressOnAchievement:toPercentComplete:forPlayer:"
- "setScoreOnLeaderboard:toScore:forPlayer:"
- "setScoreOnLeaderboard:toScore:withContext:forPlayer:"
- "start(definition:partyCode:support:)"
- "startWithDefinition:completionHandler:"
- "startWithDefinition:partyCode:completionHandler:"
- "v32@0:8@16@24"
- "v40@0:8@16d24@32"
- "v40@0:8@16q24@32"

```
