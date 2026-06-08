## ActivitySharingAwardsPlugin

> `/System/Library/Fitness/Plugins/ActivitySharingAwardsPlugin.bundle/ActivitySharingAwardsPlugin`

```diff

-2026.5.1.0.0
-  __TEXT.__text: 0x100c
-  __TEXT.__auth_stubs: 0x2b0
+2027.0.11.0.0
+  __TEXT.__text: 0xe94
   __TEXT.__objc_methlist: 0x2cc
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__cstring: 0x2d
+  __TEXT.__cstring: 0x31
   __TEXT.__oslogstring: 0x136
-  __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x5a0
-  __TEXT.__objc_methtype: 0x29a
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x70
+  __TEXT.__unwind_info: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x70
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x770
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/Fitness.framework/Fitness
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C513FD4-04EC-3A0B-BF4B-DD92EA79B58C
-  Functions: 34
-  Symbols:   66
-  CStrings:  121
+  UUID: D925BFFE-7F9F-3CDD-9177-B8344C3CEEC2
+  Functions: 32
+  Symbols:   70
+  CStrings:  11
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ACHAchievementProgressProviding>\"16@0:8"
- "@\"<ACHTemplateAssetSource>\"16@0:8"
- "@\"ASActivitySharingClient\""
- "@\"ASActivitySharingFriendQuery\""
- "@\"HKHealthStore\""
- "@\"NSDictionary\"32@0:8@\"ACHTemplate\"16^@24"
- "@\"NSObject<ACHTemplateAssetSourceDelegate>\""
- "@\"NSObject<ACHTemplateAssetSourceDelegate>\"16@0:8"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\"24@0:8@\"ACHTemplate\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "ACHAwardPlugin"
- "ACHTemplateAssetSource"
- "ASActivitySharingAwardPlugin"
- "ASActivitySharingTemplateAssetSource"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSObject<ACHTemplateAssetSourceDelegate>\",?,W,N"
- "T@\"NSObject<ACHTemplateAssetSourceDelegate>\",?,W,N,VassetSourceDelegate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,N"
- "TQ,R"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activitySharingClient"
- "_allFriends"
- "_competitionForVictoryTemplate:"
- "_friendForVictoryTemplate:"
- "_friendListQueue"
- "_friendQuery"
- "_healthStore"
- "_queue_friendWithUUID:"
- "_queue_updateWithFriends:"
- "_startFriendsQuery"
- "_updateWithFriends:"
- "activateWithCompletionHandler:"
- "assetSourceDelegate"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "contact"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "currentCompetition"
- "currentOrMostRecentCompetition"
- "customPlaceholderValuesForTemplate:error:"
- "debugDescription"
- "description"
- "dictionary"
- "displayName"
- "friendWithUUID:"
- "hash"
- "identifier"
- "init"
- "initWithActivitySharingClient:updateHandler:"
- "initWithHealthStore:"
- "initWithUUIDString:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastDayOfCompetition"
- "localizationBundleURLForTemplate:"
- "mobileAssetVersionForTemplate:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginIdentifier"
- "predicate"
- "progressProvider"
- "propertyListBundleURLForTemplate:"
- "q24@0:8@\"ACHTemplate\"16"
- "q24@0:8@16"
- "release"
- "resourceBundleURLForTemplate:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAssetSourceDelegate:"
- "setObject:forKeyedSubscript:"
- "shouldLoadPlugin"
- "stickerBundleURLForTemplate:"
- "superclass"
- "templateAssetSource"
- "templateAssetSourceDidUpdateAssets:"
- "uniqueName"
- "v16@0:8"
- "v24@0:8@\"NSObject<ACHTemplateAssetSourceDelegate>\"16"
- "v24@0:8@16"
- "victoryBadgeStyle"
- "zone"

```
