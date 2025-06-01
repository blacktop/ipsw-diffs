## MessagesCloudSync

> `/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync`

```diff

-1261.100.4.2.35
-  __TEXT.__text: 0xfc4b4
-  __TEXT.__auth_stubs: 0x1c00
-  __TEXT.__objc_methlist: 0x4fc
-  __TEXT.__const: 0x6960
-  __TEXT.__cstring: 0x6a67
-  __TEXT.__constg_swiftt: 0x24b4
-  __TEXT.__swift5_typeref: 0x23c4
+1261.200.71.2.16
+  __TEXT.__text: 0x103008
+  __TEXT.__auth_stubs: 0x1cc0
+  __TEXT.__objc_methlist: 0x524
+  __TEXT.__const: 0x6870
+  __TEXT.__cstring: 0x6c57
+  __TEXT.__constg_swiftt: 0x24e8
+  __TEXT.__swift5_typeref: 0x238a
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x2b9a
-  __TEXT.__swift5_fieldmd: 0x2f08
+  __TEXT.__swift5_reflstr: 0x2bfa
+  __TEXT.__swift5_fieldmd: 0x2f2c
   __TEXT.__swift5_assocty: 0x5a0
-  __TEXT.__swift5_proto: 0x680
+  __TEXT.__swift5_proto: 0x670
   __TEXT.__swift5_types: 0x264
-  __TEXT.__swift5_capture: 0xab0
+  __TEXT.__swift5_capture: 0xa74
   __TEXT.__swift5_mpenum: 0x48
   __TEXT.__swift5_protos: 0x88
-  __TEXT.__unwind_info: 0x3d20
-  __TEXT.__eh_frame: 0x8434
+  __TEXT.__unwind_info: 0x4020
+  __TEXT.__eh_frame: 0x864c
   __TEXT.__objc_classname: 0x1a0
-  __TEXT.__objc_methname: 0x212e
-  __TEXT.__objc_methtype: 0x4bf
-  __TEXT.__objc_stubs: 0x2e0
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x1b0
+  __TEXT.__objc_methname: 0x2198
+  __TEXT.__objc_methtype: 0x4bc
+  __TEXT.__objc_stubs: 0x300
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x21b0
-  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_const: 0x21f0
+  __DATA_CONST.__objc_selrefs: 0xb10
   __AUTH_CONST.__objc_const: 0x240
-  __AUTH_CONST.__const: 0x8648
-  __AUTH_CONST.__auth_got: 0xe08
+  __AUTH_CONST.__const: 0x8518
+  __AUTH_CONST.__auth_got: 0xe68
   __AUTH.__objc_data: 0x5e0
-  __AUTH.__data: 0x12c0
+  __AUTH.__data: 0x1320
   __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0x260
+  __DATA.__objc_classrefs: 0x270
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x88
-  __DATA.__data: 0x42c0
-  __DATA.__bss: 0xbd50
+  __DATA.__data: 0x4218
+  __DATA.__bss: 0xbb50
   __DATA.__common: 0x118
   __DATA_DIRTY.__objc_data: 0x258
-  __DATA_DIRTY.__data: 0x5a8
+  __DATA_DIRTY.__data: 0x5c8
   __DATA_DIRTY.__bss: 0x280
   __DATA_DIRTY.__common: 0xa0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6A393466-7F2A-3AB5-9B25-B907F7002443
-  Functions: 4506
-  Symbols:   354
-  CStrings:  1195
+  UUID: 6EC762E2-E417-3579-9588-0E53E61D0400
+  Functions: 4544
+  Symbols:   363
+  CStrings:  1213
 
Symbols:
+ _IMCloudKitDefinesSyncAfterAccountUpdateKey
+ _IMCloudKitDefinesSyncAfterAccountUpdatePhaseKey
+ _IMCloudKitDefinesSyncAfterIdentityUpdateKey
+ _IMCloudKitDefinesSyncAfterIdentityUpdatePhaseKey
+ _IMCloudKitLastSyncErrors
+ _IMDCKMIC2MessageUpdateErrorDomain
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_CKFetchRecordZonesOperation
+ _OBJC_CLASS_$_IMSharedUtilitiesProtoCloudKitEncryptedMessageUpdateT3
+ _swift_initEnumMetadataSinglePayload
- _objc_retain_x9
CStrings:
+ "Bad chatID found in message %s, marking for resync"
+ "CloudKitAttachmentDownloadCompletedDate"
+ "CloudKitAttachmentDownloadFirstCompletedDate"
+ "Error completing write batch for zone "
+ "Error re-associating existing item: %s"
+ "Error re-associating existing message item: %s"
+ "Error scheduling for date %s from %@, was marked done and waiting for next sync"
+ "Failed to find %s in batch map for guid update, when we detected it was in the batch more than once!"
+ "ForceAbortBeforeRead"
+ "ForceAbortBeforeWrite"
+ "Import Step summary for job: %s, %s"
+ "MIC2 Read - Forced Abort due to default ForceAbortBeforeWrite"
+ "MIC2 Write - Forced Abort due to default ForceAbortBeforeWrite"
+ "No parentChatID to add this message to"
+ "No retryAfter date for reschedule from %@, marking done and waiting for next sync"
+ "Record %s was duplicated in the batch to %s"
+ "UT3"
+ "Unable to apply message update %s, couldn't generate record from the data"
+ "Unrecognized update type, %s. Ignoring"
+ "appendError:"
+ "chatid"
+ "checkForManateeKeys(with:errorAnalyzer:)"
+ "doubleValue"
+ "errorReassociatingExistingIMMessageItem"
+ "hasChatid"
+ "initWithRecordZoneIDs:"
+ "isSyncing"
+ "messageUpdateHandleFailure"
+ "messageUpdateRecordFailure"
+ "messageUpdateUnsupportedType"
+ "readServerCountsFromDefaults"
+ "resetFetchState"
+ "v24@0:8@\"NSError\"16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
+ "verifyAllPreReqsWithRequireEnablement:completionHandler:"
+ "wasDuplicateRecordFound:"
+ "wasMissingKeys:"
- "CloudKitFullPartialSyncCompletedDate"
- "CloudKitFullPartialSyncFirstCompletedDate"
- "Could not create CKRecord for T1 message update: %s"
- "Could not create CKRecord for T2 message update: %s"
- "Failed to find %s in batch map for guid update!!"
- "Failed to find %s in batch map for guid update, when we detected it was already saved!!"
- "No protodata for message update t1"
- "No protodata for message update t2"
- "No valid update type for this message update."
- "Not performing %s, Messages in iCloud not enabled."
- "Not performing %s, another sync is in progress: %s"
- "Record %s was already saved to %s, marking synced"
- "SyncAfterAccountUpdate"
- "SyncAfterIdentityUpdate"
- "Wrote %s to %s"
- "fetchServerCounts"
- "setSyncStatusForGUIDs:toStatus:"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v32@0:8@\"NSArray\"16q24"
- "verifyAllPreReqsWithCompletionHandler:"
- "wasRecordAlreadySaved:"

```
