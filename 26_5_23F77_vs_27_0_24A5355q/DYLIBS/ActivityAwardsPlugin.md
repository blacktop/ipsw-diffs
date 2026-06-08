## ActivityAwardsPlugin

> `/System/Library/Health/Plugins/ActivityAwardsPlugin.bundle/ActivityAwardsPlugin`

```diff

-2026.5.2.0.0
-  __TEXT.__text: 0x1944
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_methlist: 0x53c
+2027.0.18.0.0
+  __TEXT.__text: 0x1600
+  __TEXT.__objc_methlist: 0x544
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x88
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__cstring: 0x2c
   __TEXT.__oslogstring: 0x197
-  __TEXT.__cstring: 0x24
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0x1e7
-  __TEXT.__objc_methname: 0xd16
-  __TEXT.__objc_methtype: 0x557
-  __TEXT.__objc_stubs: 0x6c0
-  __DATA_CONST.__got: 0x120
+  __TEXT.__unwind_info: 0x108
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x388
+  __DATA_CONST.__objc_selrefs: 0x390
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x120
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0xae8
+  __AUTH_CONST.__objc_const: 0xaf0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x5a0
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 295F46F1-51F4-3CCA-AEA5-EED8F5A0A7CA
-  Functions: 53
-  Symbols:   83
-  CStrings:  223
+  UUID: 70BE4BE8-C73A-3254-B98F-F76C807D6793
+  Functions: 51
+  Symbols:   84
+  CStrings:  13
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- _objc_retain
- _objc_retain_x20
- _objc_retain_x21
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HDDatabaseSchemaProvider>\""
- "@\"<HDHealthDaemonExtension>\"24@0:8@\"<HDHealthDaemon>\"16"
- "@\"<HDProfileExtension>\"24@0:8@\"HDProfile\"16"
- "@\"AACAwardsClient\""
- "@\"AAPTriggerGenerator\""
- "@\"ACHEarnedInstanceEntityWrapper\""
- "@\"ACHMobileAssetProvider\""
- "@\"ACHTemplateEntityWrapper\""
- "@\"HDProfile\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8q16"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCListenerEndpoint\"32@0:8@\"HDXPCClient\"16^@24"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "AAPTriggerGenerator"
- "ACHAwardsPlugin"
- "ACHAwardsProfileExtending"
- "ACHAwardsProfileExtension"
- "ACHEarnedInstanceEntityJournalEntryAppliedObserver"
- "ACHEarnedInstanceEntitySyncedEarnedInstancesObserver"
- "ACHTemplateEntitySyncedTemplatesObserver"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<HDHealthDaemon>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSArray\"16q24"
- "B32@0:8@16q24"
- "HDCurrentActivitySummaryHelperObserver"
- "HDDataObserver"
- "HDDatabaseProtectedDataObserver"
- "HDDatabaseSchemaProvider"
- "HDHealthDaemonReadyObserver"
- "HDPlugin"
- "HDProfileExtension"
- "HDProfileReadyObserver"
- "HDSyncEntityProvider"
- "HDTaskServerClassProvider"
- "NSObject"
- "Q16@0:8"
- "Q32@0:8@16Q24"
- "T#,R"
- "T@\"<HDDatabaseSchemaProvider>\",&,N,V_schemaProvider"
- "T@\"AAPTriggerGenerator\",&,N,V_triggerGenerator"
- "T@\"ACHEarnedInstanceEntityWrapper\",&,N,V_earnedInstanceEntityWrapper"
- "T@\"ACHMobileAssetProvider\",&,N,V_mobileAssetProvider"
- "T@\"ACHTemplateEntityWrapper\",&,N,V_templateEntityWrapper"
- "T@\"HDProfile\",W,N,V_profile"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_databaseQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "TQ,R"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_awardsClient"
- "_databaseQueue"
- "_earnedInstanceEntityWrapper"
- "_isDataLoading"
- "_mobileAssetProvider"
- "_notifyForUpdatedSummary:changedFields:"
- "_profile"
- "_schemaProvider"
- "_templateEntityWrapper"
- "_triggerGenerator"
- "_triggersForSummary:changedFields:"
- "activeEnergyBurned"
- "activeEnergyBurnedGoal"
- "activityMoveMode"
- "addObserver:"
- "addObserver:forDataType:"
- "addObserver:selector:name:object:"
- "addProtectedDataObserver:"
- "appleExerciseTime"
- "appleExerciseTimeGoal"
- "appleMoveTime"
- "appleMoveTimeGoal"
- "appleStandHours"
- "appleStandHoursGoal"
- "arrayWithObjects:count:"
- "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
- "autorelease"
- "behavior"
- "categoryTypeForIdentifier:"
- "class"
- "conformsToProtocol:"
- "countUnit"
- "currentActivitySummaryHelper"
- "currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:"
- "currentActivitySummaryHelper:didUpdateYesterdayActivitySummary:changedFields:"
- "currentSchemaVersionForProtectionClass:"
- "daemon"
- "daemonReady:"
- "dataManager"
- "database:protectedDataDidBecomeAvailable:"
- "database:protectedDataDidBecomeAvailable:dueToLockout:"
- "databaseEntitiesForProtectionClass:"
- "databaseQueue"
- "debugDescription"
- "defaultCenter"
- "description"
- "didAddSamplesOfTypes:anchor:"
- "doubleValueForUnit:"
- "earnedInstanceEntityDidApplyJournalEntriesInsertedEarnedInstances:removedEarnedInstances:"
- "earnedInstanceEntityDidReceiveSyncedEarnedInstances:provenance:"
- "earnedInstanceEntityWrapper"
- "extensionForHealthDaemon:"
- "extensionForProfile:"
- "handleDatabaseObliteration"
- "hash"
- "init"
- "initWithArray:"
- "initWithDaemon:mobileAssetProvider:"
- "initWithProfile:"
- "initWithProfile:awardsClient:"
- "insertEarnedInstances:provenance:useLegacySyncIdentity:profile:databaseContext:error:"
- "insertTemplates:provenance:useLegacySyncIdentity:profile:databaseContext:error:"
- "invalidateAndWait"
- "isAppleWatch"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isStandalonePhoneFitnessMode"
- "keyValuePairsDidUpdate:"
- "kilocalorieUnit"
- "listenerEndpointForClient:error:"
- "minuteUnit"
- "mobileAssetProvider"
- "orderedSyncEntities"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginIdentifier"
- "prepareForObliteration"
- "profile"
- "profileDidBecomeReady:"
- "profileType"
- "q24@0:8q16"
- "registerDaemonReadyObserver:queue:"
- "registerMigrationStepsForProtectionClass:migrator:"
- "registerProfileReadyObserver:queue:"
- "release"
- "requestAwardingWithTriggers:completion:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "samplesAdded:anchor:"
- "samplesJournaled:type:"
- "samplesMapWereRemoved:anchor:"
- "samplesOfTypesWereRemoved:anchor:"
- "schemaName"
- "schemaProvider"
- "self"
- "setDatabaseQueue:"
- "setEarnedInstanceEntityWrapper:"
- "setJournalEntryAppliedObserver:"
- "setMobileAssetProvider:"
- "setProfile:"
- "setSchemaProvider:"
- "setSyncedEarnedInstancesObserver:"
- "setSyncedTemplatesObserver:"
- "setTemplateEntityWrapper:"
- "setTriggerGenerator:"
- "sharedBehavior"
- "shouldLoadPluginForDaemon:"
- "superclass"
- "syncSchemaIdentifier"
- "taskServerClasses"
- "templateEntityDidReceiveSyncedTemplates:provenance:"
- "templateEntityWrapper"
- "triggerGenerator"
- "v16@0:8"
- "v24@0:8@\"<HDHealthDaemon>\"16"
- "v24@0:8@\"HDProfile\"16"
- "v24@0:8@16"
- "v28@0:8@\"<HDHealthDatabase>\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"<HDHealthDatabase>\"16B24B28"
- "v32@0:8@\"NSArray\"16@\"HKSampleType\"24"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@\"NSArray\"16@\"NSNumber\"24"
- "v32@0:8@\"NSArray\"16q24"
- "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
- "v32@0:8@\"NSSet\"16@\"NSNumber\"24"
- "v32@0:8@16@24"
- "v32@0:8@16B24B28"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v32@0:8q16@\"HDDatabaseMigrator\"24"
- "v32@0:8q16@24"
- "v40@0:8@\"HDCurrentActivitySummaryHelper\"16@\"HKActivitySummary\"24Q32"
- "v40@0:8@16@24Q32"
- "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
- "v64@0:8@16@24Q32Q40@48@56"
- "workoutType"
- "zone"

```
