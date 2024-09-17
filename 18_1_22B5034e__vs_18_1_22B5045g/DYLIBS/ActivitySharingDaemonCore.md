## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-821.0.0.0.0
-  __TEXT.__text: 0x7b944
+822.5.0.0.0
+  __TEXT.__text: 0x7c878
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x3a1c
+  __TEXT.__objc_methlist: 0x3abc
   __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x2dd7
-  __TEXT.__gcc_except_tab: 0x1040
-  __TEXT.__oslogstring: 0xe752
-  __TEXT.__unwind_info: 0x1ba8
-  __TEXT.__objc_classname: 0xa39
-  __TEXT.__objc_methname: 0x110e8
-  __TEXT.__objc_methtype: 0x2c1f
-  __TEXT.__objc_stubs: 0xc1a0
-  __DATA_CONST.__got: 0x998
+  __TEXT.__cstring: 0x2e07
+  __TEXT.__gcc_except_tab: 0x104c
+  __TEXT.__oslogstring: 0xe880
+  __TEXT.__unwind_info: 0x1bd8
+  __TEXT.__objc_classname: 0xa56
+  __TEXT.__objc_methname: 0x11446
+  __TEXT.__objc_methtype: 0x2c9a
+  __TEXT.__objc_stubs: 0xc2c0
+  __DATA_CONST.__got: 0x9a0
   __DATA_CONST.__const: 0x3a50
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34c8
+  __DATA_CONST.__objc_selrefs: 0x3530
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x7a0
   __AUTH_CONST.__const: 0xd60
-  __AUTH_CONST.__cfstring: 0x1d00
-  __AUTH_CONST.__objc_const: 0xf890
+  __AUTH_CONST.__cfstring: 0x1d20
+  __AUTH_CONST.__objc_const: 0xfad0
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x5d4
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x5e8
   __DATA.__data: 0xea0
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0xbe0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2324
-  Symbols:   3034
-  CStrings:  3950
+  Functions: 2339
+  Symbols:   3051
+  CStrings:  3983
 
Symbols:
+ _OBJC_METACLASS_$_ASCloudKitFetchConfiguration
+ _OBJC_CLASS_$_ASCloudKitFetchConfiguration
CStrings:
+ "shouldSkip"
+ "cloudKitManager:didHandleServerPushWithCloudKitGroup:"
+ "@52@0:8@16@24@32@40B48"
+ "removeAllFinalizedFriendUUIDs"
+ "validatedSamplesFromAchievements:workouts:activitySnapshots:friendListManager:isInvitationData:"
+ "%!@(MISSING), skip: %!d(MISSING), coalesce %!d(MISSING), allowed mod date: %!@(MISSING)"
+ "_shouldCoalesce"
+ "_recordType"
+ "allFinalizedFriendUUIDs"
+ "_shouldSkip"
+ "periodicUpdateManager:runSecureCloudTasksWithGroup:activity:completion:"
+ "_oldestAllowedModificationDate"
+ "addFinalizedFriendUUIDs:"
+ "T@\"NSDate\",R,N,V_oldestAllowedModificationDate"
+ "Placeholder contact storage %!@(MISSING) replacing %!@(MISSING)"
+ "_unhiddenSamplesInFilterableSamples:friendTimeZones:friendListManager:isInvitationData:"
+ "Record too old: %!{(MISSING)public}@ from %!{(MISSING)public}@ in database: %!{(MISSING)public}@"
+ "Skipping %!{(MISSING)public}@ from %!{(MISSING)public}@ in database: %!{(MISSING)public}@)"
+ "_fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:"
+ "TB,R,N,V_shouldSkip"
+ "recordName"
+ "T@\"NSString\",R,N,V_recordType"
+ "saveRelationship:contact:cloudKitGroup:activity:completion:"
+ "_finalizedFriendUUIDs"
+ "periodicUpdateManager:fetchDidFailWithError:activity:completion:"
+ "periodicUpdateManager:requestChangedRecordsPushWithGroup:activity:completion:"
+ "v92@0:8@16@24@32@40@48q56B64@68@76@?84"
+ "shouldCoalesce"
+ "v88@0:8@16@24q32@40@48@56@64@72@?80"
+ "_queue_handleFetchError:activity:"
+ "\x01\x13"
+ "fetchChangesInSharedDatabaseWithServerChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:"
+ "TB,R,N,V_shouldCoalesce"
+ "cloudKitManager:fetchPrivateDatabaseChangesWithCache:priority:activity:group:fetchConfigurations:completion:"
+ "Using fetch configurations %!{(MISSING)public}@ %!{(MISSING)public}@ database in %!{(MISSING)public}@"
+ "saveActivitySnapshots:workouts:achievements:isInvitationData:"
+ "oldestAllowedModificationDate"
+ "initWithRecordType:shouldSkip:"
+ "@40@0:8@16B24B28@32"
+ "saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:"
+ "_queue_saveFitnessFriendActivitySnapshots:workouts:achievements:isInvitationData:"
+ "Invitation data: %!d(MISSING)"
+ "secureCloudPrivateDatabaseFetchConfigurations"
+ "v80@0:8@16q24@32@40@48@56@64@?72"
+ "_observerQueue_notifyObserversOfServerPushHandledWithCloudKitGroup:"
+ "fetchChangesInPrivateDatabaseWithServerChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:"
+ "initWithRecordType:shouldSkip:shouldCoalesce:oldestAllowedModificationDate:"
+ "CloudKit Manager handled server push."
+ "_fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:"
+ "saveRelationship:contact:extraRecordsToSave:extraRecordIDsToDelete:cloudKitGroup:activity:completion:"
+ "@44@0:8@16@24@32B40"
+ "ASCloudKitFetchConfiguration"
+ "v32@0:8@\"ASCloudKitManager\"16@\"CKOperationGroup\"24"
- "v72@0:8@16q24@32@40@48@56@?64"
- "v80@0:8@16@24q32@40@48@56@64@?72"
- "_unhiddenSamplesInFilterableSamples:friendTimeZones:friendListManager:"
- "fetchChangesInSharedDatabaseWithServerChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:completion:"
- "fetchChangesInPrivateDatabaseWithServerChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:completion:"
- "cloudKitManager:fetchPrivateDatabaseChangesWithCache:priority:activity:group:completion:"
- "saveRelationships:extraRecordsToSave:cloudKitGroup:completion:"
- "_queue_handleFetchError:"
- "\x01\x12"
- "saveRelationship:contact:cloudKitGroup:completion:"
- "periodicUpdateManager:fetchDidFailWithError:completion:"
- "validatedSamplesFromAchievements:workouts:activitySnapshots:friendListManager:"
- "_queue_saveFitnessFriendActivitySnapshots:workouts:achievements:"
- "periodicUpdateManager:requestChangedRecordsPushWithGroup:completion:"
- "saveRelationship:contact:extraRecordsToSave:extraRecordIDsToDelete:cloudKitGroup:completion:"
- "periodicUpdateManager:requestsSecureCloudTasksToRunWithCompletion:"
- "_fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:completion:"
- "saveActivitySnapshots:workouts:achievements:"
- "v84@0:8@16@24@32@40q48B56@60@68@?76"
- "_fetchChangesInZones:additionalZonesToFetch:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:"

```
