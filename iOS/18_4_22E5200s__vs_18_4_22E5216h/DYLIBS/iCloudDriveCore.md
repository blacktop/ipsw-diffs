## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-3437.100.323.0.5
-  __TEXT.__text: 0x2f019c
+3437.100.360.0.0
+  __TEXT.__text: 0x2f0c8c
   __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0x18f4c
+  __TEXT.__objc_methlist: 0x18fbc
   __TEXT.__const: 0x4d8
-  __TEXT.__cstring: 0x79e2a
-  __TEXT.__oslogstring: 0x3acd8
-  __TEXT.__gcc_except_tab: 0x19a94
+  __TEXT.__cstring: 0x7a2c7
+  __TEXT.__oslogstring: 0x3aec0
+  __TEXT.__gcc_except_tab: 0x19a7c
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9950
+  __TEXT.__unwind_info: 0x9978
   __TEXT.__objc_classname: 0x269f
-  __TEXT.__objc_methname: 0x40d6b
-  __TEXT.__objc_methtype: 0x87e6
-  __TEXT.__objc_stubs: 0x2c780
+  __TEXT.__objc_methname: 0x40f8b
+  __TEXT.__objc_methtype: 0x8807
+  __TEXT.__objc_stubs: 0x2c8c0
   __DATA_CONST.__got: 0x16f8
-  __DATA_CONST.__const: 0x8db8
+  __DATA_CONST.__const: 0x8e08
   __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdbb8
+  __DATA_CONST.__objc_selrefs: 0xdc08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x878
   __DATA_CONST.__objc_arraydata: 0xe40
   __AUTH_CONST.__auth_got: 0xdc0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x2908
-  __AUTH_CONST.__cfstring: 0x21e20
-  __AUTH_CONST.__objc_const: 0x3b1b8
+  __AUTH_CONST.__const: 0x2958
+  __AUTH_CONST.__cfstring: 0x21f20
+  __AUTH_CONST.__objc_const: 0x3b1c8
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0

   __DATA.__bss: 0x240
   __DATA_DIRTY.__objc_data: 0x3ac0
   __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x3a0
+  __DATA_DIRTY.__bss: 0x3b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13086
-  Symbols:   15979
-  CStrings:  22567
+  Functions: 13103
+  Symbols:   15995
+  CStrings:  22595
 
Symbols:
+ _CKUnderlyingErrorHTTPStatusKey
- _OBJC_CLASS_$_NSThread
CStrings:
+ " upload_error:%@"
+ "-[BRCClientZone _learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:basedOnOriginalVersion:]"
+ "-[BRCClientZone _learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:basedOnOriginalVersion:]_block_invoke"
+ "-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:reply:]"
+ "-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:reply:]_block_invoke"
+ "-[BRCFSUploader uploadDocument:withContents:baseVersion:basedOnOriginalVersion:reply:]_block_invoke_2"
+ "-[BRCLocalItem extendedAttributes]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _uploadItemIdentifier:locatedLocalItem:itemLocationError:withContents:baseVersion:basedOnOriginalVersion:parentProgress:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) _uploadItemIdentifier:locatedLocalItem:itemLocationError:withContents:baseVersion:basedOnOriginalVersion:parentProgress:reply:]_block_invoke"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:reply:]"
+ "-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:reply:]_block_invoke"
+ "<%@: %p ctxID:%@ source:%@ reachedCap:%d, minSignalTime:%lld>"
+ "SAVE_SHARE_ERROR"
+ "ShareSave"
+ "UPDATE client_items SET version_upload_error = NULL, item_notifs_rank = bump_notifs_rank_and_trigger_notifs(rowid) WHERE version_upload_error NOT NULL AND call_block(%p, version_upload_error)"
+ "UPDATE client_uploads SET transfer_queue = '_prepare', transfer_record = NULL, transfer_stage = NULL, transfer_operation = NULL, throttle_state = 1, upload_error = NULL, retry_count = 0 WHERE throttle_state = 33 AND call_block(%p, upload_error)"
+ "UPDATE client_uploads SET upload_error = ci.version_upload_error FROM client_uploads AS cu LEFT JOIN client_items as ci ON cu.throttle_id = ci.rowid WHERE cu.upload_error NOT NULL AND ci.version_upload_error NOT NULL AND cu.throttle_state = 33"
+ "[CRIT] UNREACHABLE: Got a nil xattr name while building xattr for %@, xattr value %@%@"
+ "[CRIT] UNREACHABLE: unable to flush client state, exit to maintain consistency%@"
+ "[DEBUG] Don't fetch recents and favorites before initial sync-down of %@%@"
+ "[DEBUG] Ignoring the old etag as we uploaded a version which is not equivalent to the old etag and local change count%@"
+ "[DEBUG] Signaling downloadStream %@ , context identifier = %@, with nextTry = %lld%@"
+ "[DEBUG] ┣%llx %@ - waiting sync down to complete for item %@%@"
+ "[NOTICE] Recovered %lld stuck upload jobs on CKErrorServerRejectedRequest from client_items%@"
+ "[NOTICE] Recovered %lld stuck upload jobs on CKErrorServerRejectedRequest from client_uploads%@"
+ "_learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:basedOnOriginalVersion:"
+ "_newTelemetryEventWithError:"
+ "_uploadItemIdentifier:locatedLocalItem:itemLocationError:withContents:baseVersion:basedOnOriginalVersion:parentProgress:reply:"
+ "addChild:withPendingUnitCount:"
+ "brc_isCloudKitErrorServerRejectedRequest"
+ "learnCKInfoAfterCollaborationUploadFromRecord:basedOnOriginalVersion:"
+ "newShareSaveEventWithError:"
+ "registerAndSendShareSaveError:analyticsReporter:"
+ "report-share-save-errors"
+ "reportShareSaveErrors"
+ "setFileOperationKind:"
+ "suspended (%d)"
+ "uploadDocument:withContents:baseVersion:basedOnOriginalVersion:reply:"
+ "uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:reply:"
+ "upload_error"
+ "v76@0:8@16@24@32@40@48B56@60@?68"
- "-[BRCClientZone learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:]"
- "-[BRCClientZone learnCKInfosFromSavedRecords:isOutOfBandModifyRecords:]_block_invoke"
- "-[BRCFSUploader uploadDocument:withContents:baseVersion:reply:]"
- "-[BRCFSUploader uploadDocument:withContents:baseVersion:reply:]_block_invoke"
- "-[BRCFSUploader uploadDocument:withContents:baseVersion:reply:]_block_invoke_2"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:reply:]"
- "-[BRCXPCRegularIPCsClient(FPFSAdditions) uploadItemIdentifier:withContents:baseVersion:reply:]_block_invoke"
- "UPDATE client_uploads SET transfer_queue = '_prepare', transfer_record = NULL, transfer_stage = NULL, transfer_operation = NULL, throttle_state = 1 WHERE throttle_state = 33 AND upload_error LIKE '%%(CKErrorDomain:15)%%'"
- "[DEBUG] Don't fetch recents and favorites before initial sync-down of %@.\n%@%@"
- "[DEBUG] ┣%llx waiting sync down to complete for item %@%@"
- "[NOTICE] Recovered %lld stuck upload jobs on CKErrorServerRejectedRequest%@"
- "uploadDocument:withContents:baseVersion:reply:"
- "uploadItemIdentifier:withContents:baseVersion:reply:"

```
