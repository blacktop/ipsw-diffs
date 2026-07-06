## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-  __TEXT.__text: 0x3700c4
-  __TEXT.__auth_stubs: 0x55a0
-  __TEXT.__objc_methlist: 0x19cfc
-  __TEXT.__const: 0x6f08
-  __TEXT.__cstring: 0x12f2c
+  __TEXT.__text: 0x36f044
+  __TEXT.__auth_stubs: 0x55b0
+  __TEXT.__objc_methlist: 0x19d0c
+  __TEXT.__const: 0x6ec8
+  __TEXT.__cstring: 0x12ebc
   __TEXT.__gcc_except_tab: 0x22188
-  __TEXT.__oslogstring: 0x4fa47
+  __TEXT.__oslogstring: 0x4f997
   __TEXT.__ustring: 0x32c
   __TEXT.__dlopen_cstrs: 0x246
-  __TEXT.__swift5_typeref: 0x30ca
+  __TEXT.__swift5_typeref: 0x30a0
   __TEXT.__constg_swiftt: 0x2434
   __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_reflstr: 0x141f
-  __TEXT.__swift5_fieldmd: 0x16b0
+  __TEXT.__swift5_reflstr: 0x13ff
+  __TEXT.__swift5_fieldmd: 0x16a4
   __TEXT.__swift5_assocty: 0x6b8
   __TEXT.__swift5_capture: 0x1368
   __TEXT.__swift5_proto: 0x338

   __TEXT.__swift_as_ret: 0x414
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xd928
-  __TEXT.__eh_frame: 0x7a4c
+  __TEXT.__unwind_info: 0xd908
+  __TEXT.__eh_frame: 0x7a14
   __TEXT.__objc_classname: 0x44f1
-  __TEXT.__objc_methname: 0x517c7
+  __TEXT.__objc_methname: 0x51777
   __TEXT.__objc_methtype: 0xb34f
-  __TEXT.__objc_stubs: 0x32ba0
-  __DATA_CONST.__got: 0x3348
+  __TEXT.__objc_stubs: 0x32b80
+  __DATA_CONST.__got: 0x3350
   __DATA_CONST.__const: 0x66a8
   __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x778
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfed8
+  __DATA_CONST.__objc_selrefs: 0xfed0
   __DATA_CONST.__objc_protorefs: 0x278
   __DATA_CONST.__objc_superrefs: 0x5d8
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__auth_got: 0x2ae0
+  __AUTH_CONST.__auth_got: 0x2ae8
   __AUTH_CONST.__const: 0x8518
-  __AUTH_CONST.__cfstring: 0xe7c0
-  __AUTH_CONST.__objc_const: 0x21368
+  __AUTH_CONST.__cfstring: 0xe740
+  __AUTH_CONST.__objc_const: 0x21348
   __AUTH_CONST.__objc_intobj: 0xab0
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x3428
-  __AUTH.__data: 0x5f0
+  __AUTH.__data: 0x5e0
   __DATA.__objc_ivar: 0x124c
-  __DATA.__data: 0x5890
+  __DATA.__data: 0x5860
   __DATA.__bss: 0x5200
   __DATA.__common: 0x178
-  __DATA_DIRTY.__objc_data: 0x31b8
+  __DATA_DIRTY.__objc_data: 0x31b0
   __DATA_DIRTY.__data: 0x28f0
   __DATA_DIRTY.__bss: 0x19b0
   __DATA_DIRTY.__common: 0x1b8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13174
-  Symbols:   3028
-  CStrings:  21702
+  Functions: 13173
+  Symbols:   3031
+  CStrings:  21689
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _IMContactUtilitiesDisplayNameKey
+ _IMContactUtilitiesShortNameKey
+ _IMDCNDisplayNameAndShortNameForHandleID
+ _IMSharedBalloonPreviewSummaryForCustomAcknowledgementMessageWithSenderMap
+ _IMSharedBalloonPreviewSummaryForPollAddChoiceMessageWithSenderMap
- _IMSharedBalloonPreviewSummaryForCustomAcknowledgementMessage
- _IMSharedBalloonPreviewSummaryForPollAddChoiceMessage
CStrings:
+ "Clearing recoverable message tombstones for recordIDs: %s"
+ "storeRecoverableMessagePartWithBody:forMessageWithGUID:deleteDate:"
- "Clearing %ld/%ld recoverable message tombstones"
- "Clearing rowid %lld for %s"
- "Couldn't find ROWID for recordName %s %s"
- "Couldn't find local unsynced_removed_recoverable_messages row to delete, for reflected cloudkit record %@"
- "MiC.DASCheckpointBalancedVersion"
- "MiC.SyncResumeBatchProgress"
- "MiC.SyncResumeCompletedStepIndex"
- "MiC.SyncResumePhase"
- "clearRecoverableMessageTombStonesForRowIDs:"
- "storeRecoverableMessagePartWithBody:forMessageWithGUID:deleteDate:fromSync:"
- "tombstoneRowIDByRecordName"

```
