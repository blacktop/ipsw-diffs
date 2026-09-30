## SafariBookmarksSyncAgent

> `/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent`

```diff

-7622.2.11.10.8
-  __TEXT.__text: 0xd1250
-  __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_stubs: 0xfa00
-  __TEXT.__objc_methlist: 0x6104
+7623.1.12.10.4
+  __TEXT.__text: 0xd0510
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__objc_stubs: 0xf940
+  __TEXT.__objc_methlist: 0x608c
   __TEXT.__const: 0x238
   __TEXT.__gcc_except_tab: 0x54a8
-  __TEXT.__cstring: 0x75aa
-  __TEXT.__objc_methname: 0x18931
-  __TEXT.__oslogstring: 0x19ef4
-  __TEXT.__objc_classname: 0xdb9
-  __TEXT.__objc_methtype: 0x2908
-  __TEXT.__unwind_info: 0x3650
-  __DATA_CONST.__auth_got: 0x500
-  __DATA_CONST.__got: 0x8f8
-  __DATA_CONST.__const: 0x63f0
-  __DATA_CONST.__cfstring: 0x4b40
+  __TEXT.__cstring: 0x6fdf
+  __TEXT.__objc_methname: 0x1882c
+  __TEXT.__oslogstring: 0x19e57
+  __TEXT.__objc_classname: 0xd95
+  __TEXT.__objc_methtype: 0x2917
+  __TEXT.__unwind_info: 0x3608
+  __DATA_CONST.__auth_got: 0x540
+  __DATA_CONST.__got: 0x8e0
+  __DATA_CONST.__const: 0x6280
+  __DATA_CONST.__cfstring: 0x4600
   __DATA_CONST.__objc_classlist: 0x250
-  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8

   __DATA_CONST.__objc_arraydata: 0x330
   __DATA_CONST.__objc_arrayobj: 0x300
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xcf00
-  __DATA.__objc_selrefs: 0x4408
+  __DATA.__objc_const: 0xcec0
+  __DATA.__objc_selrefs: 0x43d8
   __DATA.__objc_ivar: 0x860
   __DATA.__objc_data: 0x1720
   __DATA.__data: 0xba0
-  __DATA.__bss: 0x300
+  __DATA.__bss: 0x260
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore
   - /System/Library/Frameworks/SharedWithYou.framework/SharedWithYou

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: CDDB19E1-36B0-3D40-A8A0-91F2D32CF88F
-  Functions: 3750
-  Symbols:   465
-  CStrings:  6142
+  UUID: 4CD5019D-077D-38BD-A4F0-67D90923D157
+  Functions: 3713
+  Symbols:   470
+  CStrings:  6043
 
Symbols:
+ _WBSOSLogCloudBookmarks
+ _WBSOSLogCloudExtensions
+ _WBSOSLogCloudSettings
+ _WBSOSLogCloudTabs
+ _WBSOSLogDiagnosticExtension
+ _WBSOSLogKeyedArchiver
+ _WBSOSLogScribbleFeedback
+ _WBSOSLogSiriLink
+ _WBSOSLogTabGroup
+ _WBSOSLogWebCompatibilityFeedback
- _CKErrorUserDidResetEncryptedDataKey
- _CKUnderlyingErrorDomain
- _CKUnderlyingFunctionErrorKey
- _os_log_create
- _stringForCKErrorCode
CStrings:
+ "@28@0:8q16B24"
+ "_beginMigrationFromDAVWithXPCActivity:"
+ "_beginSyncingWithOperationGroup:isLocalChange:completionHandler:"
+ "_createOperationGroupWithKind:"
+ "beginSyncingWithOperationGroupKind:isLocalChange:completionHandler:"
+ "createOperationGroupOfKind:"
+ "createOperationGroupWithKind:useLargerExpectedSendSize:"
+ "deviceIdentifierManagerForCloudKitWithCollectionType:generateIfNeeded:"
+ "generateChangesForAllRecordsWithDatabase:"
+ "reportSyncOperationDidBeginWithGroup:"
+ "reportSyncOperationDidFinishWithResult:error:inOperationGroup:"
+ "safari_operationGroupWithKind:"
+ "safari_operationGroupWithKind:qualityOfService:xpcActivity:"
+ "v36@0:8q16B24@?28"
+ "••• TabGroups sync failed for manager %{public}@ with result <Aborted>, %{public}@"
- "@40@0:8@16q24@32"
- "Cloud Bookmark Migration From DAV"
- "Cloud Bookmark Migration State Check"
- "Cloud Bookmark Subscription Request"
- "Cloud Extension Device Deleting"
- "Cloud Extension State Fetching"
- "Cloud Extension State Saving"
- "Cloud Settings Background Image Deletion"
- "Cloud Settings Background Image Saving"
- "Cloud Settings Fetch Setting Changes Immediately"
- "Cloud Settings Fix Per-Profile Per-Site Settings for 116544661"
- "Cloud Settings PCS Identity Changed"
- "Cloud Settings Per-Site Settings Sync Up"
- "Cloud Settings Received Push Notification"
- "Cloud Settings Safari Settings Sync Up"
- "Cloud Settings User Account Added"
- "Cloud Settings User Account Modified"
- "Cloud Settings User Did Update Per-Site Settings"
- "Cloud Settings User Did Update Settings"
- "Cloud Tab Close Requests Deleting"
- "Cloud Tab Close Requests Saving"
- "Cloud Tab Data Fetching"
- "Cloud Tab Data Saving"
- "Cloud Tab Devices Deleting"
- "Cloud Tab Groups Accept Share"
- "Cloud Tab Groups Accept Shared Tab Group"
- "Cloud Tab Groups Add Participants"
- "Cloud Tab Groups Migration"
- "Cloud Tab Groups Setup Shared Tab Group"
- "Cloud Tab Groups Sync (%@)"
- "Cloud Tab Groups Update Tab Group Presence"
- "Cloud Tab Zone Deleting"
- "CloudBookmarkCKOperationGroupExtras"
- "CloudBookmarks"
- "CloudKit Subscription Request"
- "DiagnosticExtension"
- "Ignoring push notification %{public}@ because it does not match any known subscription"
- "KeyedArchiver"
- "Push Notification Database Changes Check"
- "ScribbleFeedback"
- "SiriLink"
- "Tab Groups Subscription Request"
- "WebCompatibilityFeedback"
- "_beginMigrationFromDAVInOperationGroup:"
- "_beginSyncingForTrigger:isLocalChange:group:completionHandler:"
- "_createOperationGroupWithName:"
- "_reportSyncOperationFinishedWithError:result:inOperationGroup:"
- "beginMergingChangesWithDatabase:"
- "beginSyncingForTrigger:isLocalChange:completionHandler:"
- "ckErrorCode"
- "ckErrorDescription"
- "ckErrorName"
- "ckErrorUserDidResetEncryptedDataKey"
- "com.apple.SafariShared"
- "createMigrationFromDAVOperationGroupWithXPCActivity:"
- "createMigrationStateCheckOperationGroupWithXPCActivity:qualityOfService:"
- "createOperationGroupWithName:qualityOfService:xpcActivity:"
- "createOperationGroupWithName:useLargerExpectedSendSize:"
- "createSubscriptionRequestOperationGroupWithQualityOfService:xpcActivity:"
- "deviceIdentifierForCloudKitWithCollectionType:generateIfNeeded:"
- "finishMergingChangesWithDatabase:"
- "operationGroupName"
- "periodicCount"
- "reportTabGroupSyncFinishedWithInfo:"
- "safari_matchesErrorDomain:"
- "safari_operationGroupWithName:qualityOfService:xpcActivity:"
- "setXPCActivity:"
- "setXpcActivity:"
- "syncResult"
- "underlyingErrorCode"
- "••• Starting TabGroups sync for manager %{public}@ with trigger: %{public}@"
- "••• TabGroups sync failed for manager %{public}@ with result <Aborted>"

```
