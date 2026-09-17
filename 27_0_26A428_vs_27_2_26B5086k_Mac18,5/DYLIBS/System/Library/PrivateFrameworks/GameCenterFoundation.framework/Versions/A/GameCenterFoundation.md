## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/Versions/A/GameCenterFoundation`

```diff

-821.0.25.0.0
-  __TEXT.__text: 0x1747f4
-  __TEXT.__objc_methlist: 0x1219c
-  __TEXT.__cstring: 0x194d0
+821.1.8.0.0
+  __TEXT.__text: 0x17924c
+  __TEXT.__objc_methlist: 0x125b4
+  __TEXT.__cstring: 0x19660
   __TEXT.__const: 0x65f8
-  __TEXT.__gcc_except_tab: 0x12e0
-  __TEXT.__oslogstring: 0xdb4b
+  __TEXT.__gcc_except_tab: 0x131c
+  __TEXT.__oslogstring: 0xdbeb
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__swift5_typeref: 0x2056

   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift_as_cont: 0x3f4
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x8048
+  __TEXT.__unwind_info: 0x81d8
   __TEXT.__eh_frame: 0x59c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2b48
-  __DATA_CONST.__objc_classlist: 0x808
+  __DATA_CONST.__objc_classlist: 0x820
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x84b8
+  __DATA_CONST.__objc_selrefs: 0x84c8
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x4e8
+  __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0x2a8
-  __DATA_CONST.__got: 0x1058
-  __AUTH_CONST.__const: 0xaa08
+  __DATA_CONST.__got: 0x1070
+  __AUTH_CONST.__const: 0xaa58
   __AUTH_CONST.__cfstring: 0x11840
-  __AUTH_CONST.__objc_const: 0x244c8
+  __AUTH_CONST.__objc_const: 0x24bd8
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__auth_got: 0x1340
-  __AUTH.__objc_data: 0x2af0
+  __AUTH.__objc_data: 0x2be0
   __AUTH.__data: 0x1088
-  __DATA.__objc_ivar: 0xfb8
+  __DATA.__objc_ivar: 0xfdc
   __DATA.__data: 0x3a30
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2c40

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11312
-  Symbols:   15171
-  CStrings:  4202
+  Functions: 11426
+  Symbols:   15316
+  CStrings:  4211
 
Symbols:
+ +[GCFAchievement descriptionForAchievement:achievementDescriptions:]
+ +[GCFAchievement instanceMethodSignatureForSelector:]
+ +[GCFAchievement instancesRespondToSelector:]
+ +[GCFAchievement loadAchievementWithID:forGame:players:complete:]
+ +[GCFAchievement loadAchievementsForGameV2:player:includeUnreported:includeHidden:withCompletionHandler:]
+ +[GCFAchievement loadAchievementsForGameV2:players:includeUnreported:includeHidden:withCompletionHandler:]
+ +[GCFAchievement loadAchievementsWithCompletionHandler:]
+ +[GCFAchievement reportAchievements:whileScreeningChallenges:withEligibleChallenges:withCompletionHandler:]
+ +[GCFAchievement reportAchievements:withCompletionHandler:]
+ +[GCFAchievement resetAchievementsWithCompletionHandler:]
+ +[GCFAchievement shouldShowBannerOnReport:achievementDescription:reportedAchievements:]
+ +[GCFAchievement shouldShowBannerOnReport:achievementDescription:reportedAchievements:uiFrameworkMethodsRequired:]
+ +[GCFAchievement shouldShowBannerOnReport:reportedAchievements:]
+ +[GCFAchievement shouldShowBannerOnReport:reportedAchievements:uiFrameworkMethodsRequired:]
+ +[GCFAchievement showBannerIsSupported]
+ +[GCFAchievement supportsSecureCoding]
+ +[GCFAchievementDescription _achievementDescriptionFromGame:propertyListDictionary:]
+ +[GCFAchievementDescription _loadLocalAchievementDescriptionsForGame:]
+ +[GCFAchievementDescription instanceMethodSignatureForSelector:]
+ +[GCFAchievementDescription instancesRespondToSelector:]
+ +[GCFAchievementDescription loadAchievementDescriptionsForGame:withCompletionHandler:]
+ +[GCFAchievementDescription loadAchievementDescriptionsWithCompletionHandler:]
+ +[GCFAchievementDescription supportsSecureCoding]
+ -[GCFAchievement .cxx_destruct]
+ -[GCFAchievement copyWithZone:]
+ -[GCFAchievement description]
+ -[GCFAchievement encodeWithCoder:]
+ -[GCFAchievement forwardingTargetForSelector:]
+ -[GCFAchievement game]
+ -[GCFAchievement hash]
+ -[GCFAchievement initWithCoder:]
+ -[GCFAchievement initWithIdentifier:]
+ -[GCFAchievement initWithIdentifier:forPlayer:]
+ -[GCFAchievement initWithIdentifier:player:]
+ -[GCFAchievement initWithIdentifier:player:percentComplete:lastReportedDate:]
+ -[GCFAchievement initWithInternalRepresentation:]
+ -[GCFAchievement initWithInternalRepresentation:playerID:]
+ -[GCFAchievement init]
+ -[GCFAchievement internal]
+ -[GCFAchievement isCompleted]
+ -[GCFAchievement isEqual:]
+ -[GCFAchievement methodSignatureForSelector:]
+ -[GCFAchievement playerID]
+ -[GCFAchievement player]
+ -[GCFAchievement reportAchievementWithCompletionHandler:]
+ -[GCFAchievement respondsToSelector:]
+ -[GCFAchievement setGame:]
+ -[GCFAchievement setInternal:]
+ -[GCFAchievement setShowsCompletionBanner:]
+ -[GCFAchievement setValue:forUndefinedKey:]
+ -[GCFAchievement showsCompletionBanner]
+ -[GCFAchievement valueForUndefinedKey:]
+ -[GCFAchievement(GCFAchievementDescription) _achievementDescription]
+ -[GCFAchievementDescription .cxx_destruct]
+ -[GCFAchievementDescription description]
+ -[GCFAchievementDescription encodeWithCoder:]
+ -[GCFAchievementDescription forwardingTargetForSelector:]
+ -[GCFAchievementDescription game]
+ -[GCFAchievementDescription hash]
+ -[GCFAchievementDescription imageNameForIcon]
+ -[GCFAchievementDescription image]
+ -[GCFAchievementDescription initWithCoder:]
+ -[GCFAchievementDescription initWithInternalRepresentation:]
+ -[GCFAchievementDescription init]
+ -[GCFAchievementDescription internal]
+ -[GCFAchievementDescription isEqual:]
+ -[GCFAchievementDescription methodSignatureForSelector:]
+ -[GCFAchievementDescription respondsToSelector:]
+ -[GCFAchievementDescription setImage:]
+ -[GCFAchievementDescription setInternal:]
+ -[GCFAchievementDescription setValue:forUndefinedKey:]
+ -[GCFAchievementDescription valueForUndefinedKey:]
+ -[GCFLocalizedAchievementDescription .cxx_destruct]
+ -[GCFLocalizedAchievementDescription _localizedStringFromKey:]
+ -[GCFLocalizedAchievementDescription achievedDescription]
+ -[GCFLocalizedAchievementDescription game]
+ -[GCFLocalizedAchievementDescription iconImageName]
+ -[GCFLocalizedAchievementDescription imageNameForIcon]
+ -[GCFLocalizedAchievementDescription setGame:]
+ -[GCFLocalizedAchievementDescription setIconImageName:]
+ -[GCFLocalizedAchievementDescription title]
+ -[GCFLocalizedAchievementDescription unachievedDescription]
+ -[GKAchievementChallenge gcfAchievement]
+ -[GKAchievementChallenge setGcfAchievement:]
+ OBJC_IVAR_$_GCFAchievement._game
+ OBJC_IVAR_$_GCFAchievement._internal
+ OBJC_IVAR_$_GCFAchievement._player
+ OBJC_IVAR_$_GCFAchievement._showsCompletionBanner
+ OBJC_IVAR_$_GCFAchievementDescription._image
+ OBJC_IVAR_$_GCFAchievementDescription._internal
+ OBJC_IVAR_$_GCFLocalizedAchievementDescription._game
+ OBJC_IVAR_$_GCFLocalizedAchievementDescription._iconImageName
+ OBJC_IVAR_$_GKAchievementChallenge._gcfAchievement
+ OBJC_IVAR_$_GKAchievementChallenge._publicAchievement
+ _OBJC_CLASS_$_GCFAchievement
+ _OBJC_CLASS_$_GCFAchievementDescription
+ _OBJC_CLASS_$_GCFLocalizedAchievementDescription
+ _OBJC_METACLASS_$_GCFAchievement
+ _OBJC_METACLASS_$_GCFAchievementDescription
+ _OBJC_METACLASS_$_GCFLocalizedAchievementDescription
+ __106+[GCFAchievement loadAchievementsForGameV2:players:includeUnreported:includeHidden:withCompletionHandler:]_block_invoke
+ __107+[GCFAchievement reportAchievements:whileScreeningChallenges:withEligibleChallenges:withCompletionHandler:]_block_invoke
+ __107+[GCFAchievement reportAchievements:whileScreeningChallenges:withEligibleChallenges:withCompletionHandler:]_block_invoke_2
+ __65+[GCFAchievement loadAchievementWithID:forGame:players:complete:]_block_invoke
+ __86+[GCFAchievementDescription loadAchievementDescriptionsForGame:withCompletionHandler:]_block_invoke
+ __OBJC_$_CLASS_METHODS_GCFAchievement
+ __OBJC_$_CLASS_METHODS_GCFAchievementDescription
+ __OBJC_$_CLASS_PROP_LIST_GCFAchievement
+ __OBJC_$_CLASS_PROP_LIST_GCFAchievementDescription
+ __OBJC_$_INSTANCE_METHODS_GCFAchievement(GCFAchievementDescription)
+ __OBJC_$_INSTANCE_METHODS_GCFAchievementDescription
+ __OBJC_$_INSTANCE_METHODS_GCFLocalizedAchievementDescription
+ __OBJC_$_INSTANCE_VARIABLES_GCFAchievement
+ __OBJC_$_INSTANCE_VARIABLES_GCFAchievementDescription
+ __OBJC_$_INSTANCE_VARIABLES_GCFLocalizedAchievementDescription
+ __OBJC_$_PROP_LIST_GCFAchievement
+ __OBJC_$_PROP_LIST_GCFAchievementDescription
+ __OBJC_$_PROP_LIST_GCFLocalizedAchievementDescription
+ __OBJC_CLASS_PROTOCOLS_$_GCFAchievement
+ __OBJC_CLASS_PROTOCOLS_$_GCFAchievementDescription
+ __OBJC_CLASS_RO_$_GCFAchievement
+ __OBJC_CLASS_RO_$_GCFAchievementDescription
+ __OBJC_CLASS_RO_$_GCFLocalizedAchievementDescription
+ __OBJC_METACLASS_RO_$_GCFAchievement
+ __OBJC_METACLASS_RO_$_GCFAchievementDescription
+ __OBJC_METACLASS_RO_$_GCFLocalizedAchievementDescription
+ ___105+[GCFAchievement loadAchievementsForGameV2:player:includeUnreported:includeHidden:withCompletionHandler:]_block_invoke
+ ___106+[GCFAchievement loadAchievementsForGameV2:players:includeUnreported:includeHidden:withCompletionHandler:]_block_invoke
+ ___106+[GCFAchievement loadAchievementsForGameV2:players:includeUnreported:includeHidden:withCompletionHandler:]_block_invoke_2
+ ___106+[GCFAchievement loadAchievementsForGameV2:players:includeUnreported:includeHidden:withCompletionHandler:]_block_invoke_3
+ ___106+[GCFAchievement loadAchievementsForGameV2:players:includeUnreported:includeHidden:withCompletionHandler:]_block_invoke_4
+ ___107+[GCFAchievement reportAchievements:whileScreeningChallenges:withEligibleChallenges:withCompletionHandler:]_block_invoke
+ ___107+[GCFAchievement reportAchievements:whileScreeningChallenges:withEligibleChallenges:withCompletionHandler:]_block_invoke_2
+ ___107+[GCFAchievement reportAchievements:whileScreeningChallenges:withEligibleChallenges:withCompletionHandler:]_block_invoke_3
+ ___107+[GCFAchievement reportAchievements:whileScreeningChallenges:withEligibleChallenges:withCompletionHandler:]_block_invoke_4
+ ___114+[GCFAchievement shouldShowBannerOnReport:achievementDescription:reportedAchievements:uiFrameworkMethodsRequired:]_block_invoke
+ ___39+[GCFAchievement showBannerIsSupported]_block_invoke
+ ___56+[GCFAchievement loadAchievementsWithCompletionHandler:]_block_invoke
+ ___57+[GCFAchievement resetAchievementsWithCompletionHandler:]_block_invoke
+ ___65+[GCFAchievement loadAchievementWithID:forGame:players:complete:]_block_invoke
+ ___65+[GCFAchievement loadAchievementWithID:forGame:players:complete:]_block_invoke_2
+ ___70+[GCFAchievementDescription _loadLocalAchievementDescriptionsForGame:]_block_invoke
+ ___78+[GCFAchievementDescription loadAchievementDescriptionsWithCompletionHandler:]_block_invoke
+ ___86+[GCFAchievementDescription loadAchievementDescriptionsForGame:withCompletionHandler:]_block_invoke
+ ___block_descriptor_49_e8_32s40r_e31_v32?0"GCFAchievement"8Q16^B24l
+ _objc_msgSend$gcfAchievement
+ _objc_msgSend$setGcfAchievement:
- -[GKAchievementChallenge setAchievement:]
- OBJC_IVAR_$_GKAchievementChallenge._achievement
CStrings:
+ "+[GCFAchievement loadAchievementWithID:forGame:players:complete:]"
+ "+[GCFAchievement loadAchievementsForGameV2:players:includeUnreported:includeHidden:withCompletionHandler:]"
+ "+[GCFAchievement reportAchievements:whileScreeningChallenges:withEligibleChallenges:withCompletionHandler:]"
+ "-[GCFAchievement initWithIdentifier:forPlayer:]"
+ "-[GCFAchievement playerID]"
+ "<GCFAchievement %p> has a nil or invalid internal player, will return a nil player"
+ "GCFAchievement.m"
+ "[%@]Not eligible for onboarding UI -- excluded bundle identifier."
+ "v32@?0@\"GCFAchievement\"8Q16^B24"
```
