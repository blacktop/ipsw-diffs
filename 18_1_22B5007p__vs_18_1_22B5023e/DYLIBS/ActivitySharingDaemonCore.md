## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-813.0.0.0.0
-  __TEXT.__text: 0x7a2b8
+819.0.0.0.0
+  __TEXT.__text: 0x7b8f8
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x39a4
-  __TEXT.__const: 0x1e0
+  __TEXT.__objc_methlist: 0x3a1c
+  __TEXT.__const: 0x1d8
   __TEXT.__cstring: 0x2dd7
-  __TEXT.__gcc_except_tab: 0x1034
-  __TEXT.__oslogstring: 0xe4c3
-  __TEXT.__unwind_info: 0x1b60
+  __TEXT.__gcc_except_tab: 0x1040
+  __TEXT.__oslogstring: 0xe752
+  __TEXT.__unwind_info: 0x1ba8
   __TEXT.__objc_classname: 0xa39
-  __TEXT.__objc_methname: 0x10dea
-  __TEXT.__objc_methtype: 0x2c1c
-  __TEXT.__objc_stubs: 0xc020
-  __DATA_CONST.__got: 0x980
-  __DATA_CONST.__const: 0x3a28
+  __TEXT.__objc_methname: 0x110e8
+  __TEXT.__objc_methtype: 0x2c1f
+  __TEXT.__objc_stubs: 0xc1a0
+  __DATA_CONST.__got: 0x998
+  __DATA_CONST.__const: 0x3a50
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3458
+  __DATA_CONST.__objc_selrefs: 0x34c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH_CONST.__const: 0xd20
+  __AUTH_CONST.__const: 0xd60
   __AUTH_CONST.__cfstring: 0x1d00
-  __AUTH_CONST.__objc_const: 0xf810
+  __AUTH_CONST.__objc_const: 0xf890
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x5c4
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x5d4
   __DATA.__data: 0xea0
-  __DATA.__bss: 0xe0
-  __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0x48
+  __DATA.__bss: 0x80
+  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__bss: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2304
-  Symbols:   3010
-  CStrings:  3922
+  Functions: 2324
+  Symbols:   3034
+  CStrings:  3950
 
Symbols:
+ _ASCloudKitMetadataZoneName
+ _OBJC_CLASS_$_CKRecordZoneSubscription
+ _kASFetchDateCacheDefaultsKey
CStrings:
+ "\x02\x12"
+ "\b\xe1"
+ "Adding response to pending list %!@(MISSING)"
+ "CloudKit push received for metadata_zone, clearing fetch date."
+ "CompetitionManager received secure cloud competition to clean up"
+ "Creating subscription to zone with name %!{(MISSING)public}@ in database %!{(MISSING)public}@"
+ "Fetched additional records successfully in zone %!@(MISSING), for date %!@(MISSING)"
+ "Fetched changes successfully in zone %!@(MISSING), serverChangeToken %!@(MISSING)"
+ "No changes in database %!{(MISSING)public}@, not fetching. %!{(MISSING)public}@"
+ "Processing pending responses %!@(MISSING)"
+ "RelationshipManager received non primary relationship to process (NEW: %!@(MISSING)\nLOCAL: %!@(MISSING)\nPRIMARY: %!@(MISSING)\nPRIMARY REMOTE: %!@(MISSING))"
+ "Removed legacy competitions that have been migrated (success %!{(MISSING)BOOL}d, error: %!@(MISSING))"
+ "Removed secure cloud competitions that have been downgraded (success %!{(MISSING)BOOL}d, error: %!@(MISSING))"
+ "Removing secure cloud competition lists that have been downgraded %!@(MISSING)"
+ "Skipping fetch of metadata_zone"
+ "_fetchChangesInZones:additionalZonesToFetch:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:"
+ "_pendingResponses"
+ "_queue_cleanUpSecureCloudCompetitionLists:activity:cloudKitGroup:"
+ "_queue_processEndRelationshipIfNeededForPreviousRemoteRelationship:newRemoteRelationship:contact:xpcActivity:cloudKitGroup:processGroup:"
+ "_readyToProcessResponses"
+ "_secureCloudCompetitionListsToCleanUp"
+ "_shouldSkipLocalSecureCloudCompetitionList:"
+ "_subscribeToChangesInDatabase:subscriptionPrefix:recordTypes:zoneNames:recordTypesToDelete:completion:"
+ "_zoneFetchDateByZoneID"
+ "additionalZoneIDsToFetchWithServerChangeTokenChange:"
+ "competitionManager:deleteCompetitionLists:group:completion:"
+ "fetchDateForRecordZoneID:"
+ "handleSavedRecords:forContact:completion:"
+ "initWithZoneID:subscriptionID:"
+ "isPaused"
+ "processPendingResponses"
+ "processResponse:"
+ "relationshipManager:acceptedInviteForFriend:completion:"
+ "secureCloudNeedsRepair"
+ "secureCloudReady"
+ "setFetchDate:forRecordZoneID:"
+ "setIgnoreDeletedObjects:"
+ "v84@0:8@16@24@32@40q48B56@60@68@?76"
+ "\x8b\x12"
- "\x02\x11"
- "\b\xd1"
- "Fetched changes successfully in zone %!@(MISSING)"
- "No changes in database %!{(MISSING)public}@, not fetching."
- "Removed legacy competitions that have been migrated (success %!{(MISSING)BOOL}d, error: %!@(MISSING), record count %!l(MISSING)d)"
- "_fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:"
- "_subscribeToChangesInDatabase:subscriptionPrefix:recordTypes:recordTypesToDelete:completion:"
- "additionalLegacyZoneIDs"
- "paused"
- "v76@0:8@16@24@32q40B48@52@60@?68"
- "\x8b\x11"

```
