## ActivitySharingServices

> `/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices`

```diff

-821.0.0.0.0
-  __TEXT.__text: 0x124f68
-  __TEXT.__auth_stubs: 0x1e30
-  __TEXT.__objc_methlist: 0x354
-  __TEXT.__const: 0x4d28
-  __TEXT.__cstring: 0x434e
-  __TEXT.__swift5_typeref: 0x3020
-  __TEXT.__swift5_fieldmd: 0x2ab8
-  __TEXT.__constg_swiftt: 0x2764
-  __TEXT.__oslogstring: 0x53b8
+822.5.0.0.0
+  __TEXT.__text: 0x12e0a0
+  __TEXT.__auth_stubs: 0x1e90
+  __TEXT.__objc_methlist: 0x374
+  __TEXT.__const: 0x4d38
+  __TEXT.__cstring: 0x461e
+  __TEXT.__swift5_typeref: 0x30a0
+  __TEXT.__swift5_fieldmd: 0x2b18
+  __TEXT.__constg_swiftt: 0x279c
+  __TEXT.__oslogstring: 0x59c3
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x3e14
+  __TEXT.__swift5_reflstr: 0x3f04
   __TEXT.__swift5_assocty: 0x210
   __TEXT.__swift5_protos: 0x130
   __TEXT.__swift5_proto: 0x318
   __TEXT.__swift5_types: 0x234
-  __TEXT.__swift5_capture: 0x1998
+  __TEXT.__swift5_capture: 0x1a04
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x5a48
-  __TEXT.__eh_frame: 0x12f48
+  __TEXT.__unwind_info: 0x5bc8
+  __TEXT.__eh_frame: 0x13470
   __TEXT.__objc_classname: 0x1b9
-  __TEXT.__objc_methname: 0x3923
-  __TEXT.__objc_methtype: 0x11fe
-  __DATA_CONST.__got: 0x748
+  __TEXT.__objc_methname: 0x3b12
+  __TEXT.__objc_methtype: 0x12e6
+  __DATA_CONST.__got: 0x758
   __DATA_CONST.__const: 0x9b8
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb0
+  __DATA_CONST.__objc_selrefs: 0xc18
   __DATA_CONST.__objc_protorefs: 0x80
-  __AUTH_CONST.__auth_got: 0xf18
-  __AUTH_CONST.__auth_ptr: 0x11c0
-  __AUTH_CONST.__const: 0x78a8
-  __AUTH_CONST.__objc_const: 0x5a48
+  __AUTH_CONST.__auth_got: 0xf48
+  __AUTH_CONST.__auth_ptr: 0xe10
+  __AUTH_CONST.__const: 0x7928
+  __AUTH_CONST.__objc_const: 0x5b40
   __AUTH.__objc_data: 0x318
   __AUTH.__data: 0x798
-  __DATA.__data: 0x2990
+  __DATA.__data: 0x2a18
   __DATA.__bss: 0x2e00
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x658
-  __DATA_DIRTY.__data: 0x1138
+  __DATA_DIRTY.__objc_data: 0x670
+  __DATA_DIRTY.__data: 0x1140
   __DATA_DIRTY.__common: 0x48
   __DATA_DIRTY.__bss: 0x980
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4707
-  Symbols:   462
-  CStrings:  1307
+  Functions: 4770
+  Symbols:   461
+  CStrings:  1354
 
Symbols:
+ _OBJC_CLASS_$_ASCloudKitFetchConfiguration
+ _NSStringFromASCloudType
- _ASCloudKitGroupCoreDuetTriggered
CStrings:
+ "Clearing collected cloud devices"
+ "saveRelationship:contact:extraRecordsToSave:extraRecordIDsToDelete:cloudKitGroup:activity:completion:"
+ "Clearing stored cloud devices"
+ "Finished handling invitation request"
+ "v72@0:8@\"ASCloudKitManager\"16@\"ASCloudKitServerChangeTokenCache\"24q32@\"<OS_xpc_object>\"40@\"CKOperationGroup\"48@\"NSDictionary\"56@?<v@?B@\"NSError\"@\"NSArray\">64"
+ "Found secure cloud relationships to consolidate: %!s(MISSING)"
+ "upgradeRelationshipsIfNeeded(xpcActivity:)"
+ "handleLostManateeIdentity(error:xpcActivity:)"
+ "updateFriendsNeedingConsolidation(group:xpcActivity:)"
+ "Downgrade backoff for %!s(MISSING) completion: %!{(MISSING)bool}d, acknowledgement: %!{(MISSING)bool}d"
+ "Relationship migration %!s(MISSING) backing off previous completion: %!{(MISSING)bool}d"
+ "Failed to make relationship shares: %!@(MISSING)"
+ "deleteZonesIfNeeded(xpcActivity:)"
+ "cloudDeviceStore"
+ "fetchChangesInPrivateDatabaseWithServerChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:"
+ "Relationship migration %!s(MISSING) backing off started attempt: %!{(MISSING)bool}d"
+ "Updated cloud devices from merge %!s(MISSING)"
+ "Found legacy relationships to consolidate: %!s(MISSING)"
+ "Rate limiting push for consolidation, last attempt %!s(MISSING)"
+ "Retrying message immediately %!s(MISSING)"
+ "fixUpLegacyRelationships(contacts:xpcActivity:)"
+ "Upgrade %!s(MISSING) backing off availability change: %!{(MISSING)bool}d"
+ "v48@0:8@\"ASPeriodicUpdateManager\"16@\"CKOperationGroup\"24@\"NSObject<OS_xpc_object>\"32@?<v@?B@\"NSError\">40"
+ "allFinalizedFriendUUIDs"
+ "Running consolidation task."
+ "saveRelationship:contact:cloudKitGroup:activity:completion:"
+ "No secure cloud relationships to consolidate"
+ "migrateContactsIfNeeded(xpcActivity:)"
+ "v32@0:8@\"ASCloudKitManager\"16@\"CKOperationGroup\"24"
+ "Error fetching account info %!@(MISSING)"
+ "handleAcknowledgedDowngradeRequests(xpcActivity:)"
+ "Not process activity data preview for an already handled invitation with date: %!{(MISSING)public}s"
+ "dateForLatestDowngradeCompleted"
+ "Attempting to save legacy relationships to secure cloud container %!s(MISSING)"
+ "periodicUpdateManager:fetchDidFailWithError:activity:completion:"
+ "periodicUpdateManager(_:fetchDidFailWithError:activity:)"
+ "addFinalizedFriendUUIDs:"
+ "periodicUpdateManager:runSecureCloudTasksWithGroup:activity:completion:"
+ "updateSupportedFeatures(group:xpcActivity:)"
+ "requestDowngradeIfNeeded(xpcActivity:)"
+ "handleDowngradeRequests(xpcActivity:)"
+ "cloudKitManager(_:didHandleServerPushWithCloudKitGroup:)"
+ "periodicUpdateManager(_:requestChangedRecordsPushWith:activity:)"
+ "cloudKitManager:fetchPrivateDatabaseChangesWithCache:priority:activity:group:fetchConfigurations:completion:"
+ "removeAllFinalizedFriendUUIDs"
+ "v48@0:8@\"ASPeriodicUpdateManager\"16@\"NSError\"24@\"NSObject<OS_xpc_object>\"32@?<v@?B@\"NSError\">40"
+ "dateForLatestMigrationCompleted"
+ "Updated cloud devices from apply %!s(MISSING)"
+ "dateForLatestUpgradeAvailableUnavailableChange"
+ "Failed to create Activity Sharing user defaults"
+ "updateContactsWithUpgradeAvailability(_:xpcActivity:)"
+ "fitnessMode"
+ "Error pushing activity data for new relationship %!@(MISSING)"
+ "SecureCloudDowngradeRetryBackoff"
+ "v72@0:8@\"ASCloudKitManager\"16@\"ASCloudKitServerChangeTokenCache\"24q32@\"NSObject<OS_xpc_object>\"40@\"CKOperationGroup\"48@\"NSDictionary\"56@?<v@?B@\"NSError\"@\"NSArray\">64"
+ "Pushing activity data for new relationships %!s(MISSING)"
+ "No legacy relationships to consolidate"
+ "periodicUpdateManager:requestChangedRecordsPushWithGroup:activity:completion:"
+ "dateForLatestDowngradeNeedsAcknowledgement"
+ "Processing activity data preview for an already handled invitation with date: %!{(MISSING)public}s"
+ "fixUpSecureCloudRelationships(xpcActivity:)"
+ "LastAttemptToPushConsolidation"
+ "saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:"
+ "Destination %!s(MISSING) does not have a matching legacy participant"
+ "v72@0:8@16@24q32@40@48@56@?64"
+ "Not pushing activity data updates to CloudKit, apple watch: %!{(MISSING)bool}d, standalone phone %!{(MISSING)bool}d"
+ "pushAllUpdates(group:xpcActivity:)"
+ "periodicUpdateManager(_:runSecureCloudTasksWith:activity:)"
+ "dateForLatestRelationshipStart"
+ "secureCloudCoalescer"
+ "modificationDate"
+ "Backing off push for consolidation %!s(MISSING), mod date %!s(MISSING) type %!s(MISSING)"
+ "requestDowngrade(for:xpcActivity:)"
+ "v48@0:8@\"ASPeriodicUpdateManager\"16@\"CKOperationGroup\"24@\"<OS_xpc_object>\"32@?<v@?B@\"NSError\">40"
+ "cloudKitManager:didHandleServerPushWithCloudKitGroup:"
+ "needsPushForConsolidation"
+ "sendUpgradeRequest(_:xpcActivity:)"
+ "v48@0:8@\"ASPeriodicUpdateManager\"16@\"NSError\"24@\"<OS_xpc_object>\"32@?<v@?B@\"NSError\">40"
- "periodicUpdateManager(_:requestChangedRecordsPushWith:)"
- "handleAcknowledgedDowngradeRequests()"
- "updateContactsWithUpgradeAvailability(_:)"
- "requestDowngradeIfNeeded()"
- "saveRelationships:extraRecordsToSave:cloudKitGroup:completion:"
- "Cloud devices unchanged"
- "periodicUpdateManager(_:fetchDidFailWithError:)"
- "v32@0:8@16@?24"
- "updateSupportedFeatures(group:)"
- "periodicUpdateManager:fetchDidFailWithError:completion:"
- "handleDowngradeRequests()"
- "periodicUpdateManagerRequestsSecureCloudTasksToRun(_:)"
- "v40@0:8@\"ASPeriodicUpdateManager\"16@\"NSError\"24@?<v@?B@\"NSError\">32"
- "pushAllUpdates(group:)"
- "periodicUpdateManager:requestChangedRecordsPushWithGroup:completion:"
- "v40@0:8@\"ASPeriodicUpdateManager\"16@\"CKOperationGroup\"24@?<v@?B@\"NSError\">32"
- "handleLostManateeIdentity(error:)"
- "saveRelationship:contact:cloudKitGroup:completion:"
- "saveRelationship:contact:extraRecordsToSave:extraRecordIDsToDelete:cloudKitGroup:completion:"
- "periodicUpdateManager:requestsSecureCloudTasksToRunWithCompletion:"
- "fixUpLegacyRelationships(contacts:)"
- "cloudKitManager:fetchPrivateDatabaseChangesWithCache:priority:activity:group:completion:"
- "upgradeRelationshipsIfNeeded()"
- "fixUpSecureCloudRelationships()"
- "migrateContactsIfNeeded()"
- "v32@0:8@\"ASPeriodicUpdateManager\"16@?<v@?B@\"NSError\">24"
- "fetchChangesInPrivateDatabaseWithServerChangeTokenCache:priority:activity:group:completion:"
- "sendUpgradeRequest(_:)"
- "deleteZonesIfNeeded()"

```
