## MessagesCloudSync

> `/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync`

```diff

-  __TEXT.__text: 0xfc370
+  __TEXT.__text: 0xfc1a8
   __TEXT.__objc_methlist: 0xcb0
   __TEXT.__const: 0x98b0
-  __TEXT.__cstring: 0x3ec1
+  __TEXT.__cstring: 0x3e01
   __TEXT.__constg_swiftt: 0x2c00
-  __TEXT.__swift5_typeref: 0x2842
+  __TEXT.__swift5_typeref: 0x2826
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_reflstr: 0x2ffa
   __TEXT.__swift5_fieldmd: 0x3358
   __TEXT.__swift5_assocty: 0x5b8
-  __TEXT.__oslogstring: 0x5703
+  __TEXT.__oslogstring: 0x5763
   __TEXT.__swift5_proto: 0x750
   __TEXT.__swift5_types: 0x2d8
-  __TEXT.__swift5_capture: 0x1014
+  __TEXT.__swift5_capture: 0xfd8
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0x90
-  __TEXT.__swift_as_entry: 0x42c
-  __TEXT.__swift_as_ret: 0x4c8
+  __TEXT.__swift_as_entry: 0x430
+  __TEXT.__swift_as_ret: 0x4cc
   __TEXT.__swift_as_cont: 0x96c
-  __TEXT.__unwind_info: 0x3738
-  __TEXT.__eh_frame: 0x9d94
+  __TEXT.__unwind_info: 0x3720
+  __TEXT.__eh_frame: 0x9cf4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xff8
+  __DATA_CONST.__objc_selrefs: 0xff0
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x7d8
+  __DATA_CONST.__got: 0x7e0
   __AUTH_CONST.__const: 0x8d59
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x2758
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x10d8
+  __AUTH_CONST.__auth_got: 0x10e0
   __AUTH.__objc_data: 0x3d8
   __AUTH.__data: 0x508
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x10a0
-  __DATA.__bss: 0x8400
-  __DATA.__common: 0x28
+  __DATA.__data: 0xff0
+  __DATA.__bss: 0x8100
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x618
-  __DATA_DIRTY.__data: 0x26a0
-  __DATA_DIRTY.__bss: 0x4800
-  __DATA_DIRTY.__common: 0x258
+  __DATA_DIRTY.__data: 0x2710
+  __DATA_DIRTY.__bss: 0x4b00
+  __DATA_DIRTY.__common: 0x270
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3822
-  Symbols:   441
-  CStrings:  863
+  Functions: 3817
+  Symbols:   442
+  CStrings:  859
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_cont : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _IMCloudKitAttachmentDownloadHistoryFinished
CStrings:
+ "Business chat is not supported for message %s, dropping"
+ "Dropped %ld/%ld records of type %s during import from syncStore! Failed GUIDs: %s"
+ "Error importing transfer %s - %@"
+ "Error importing: %@ for recordType %s, guid = %s, record.recordType %s, record.recordName = %s)"
+ "Existing item with no guid, dropping"
+ "Import was .unsupported for recordType %s, guid %s"
+ "Item is an emojiTapBack but emojiTapbacks are not enabled, dropping"
+ "Item is not compatible with MIC %s"
+ "Item is not compatible with MIC %s, dropping"
+ "No record type for recordType %s guid %s"
+ "Record is .unknown for recordType %s guid %s"
+ "Should not store message record for %s, account or alias mismatch, dropping"
- "Business chat is not supported, do not import message %s"
- "Clearing stale resume state from phase %s (now running %s)"
- "Error importing: %@ for record(guid = %s, recordType = %s, recordName = %s)"
- "Existing item with no guid, do not store"
- "Failed to report stopped to BackgroundSystemTasks: %@"
- "Found %ld records without GUIDs!"
- "MiC.DASCheckpointBalancedVersion"
- "MiC.SyncResumeBatchProgress"
- "MiC.SyncResumeCompletedStepIndex"
- "MiC.SyncResumePhase"
- "No record type for record guid %s"
- "Resuming %s from batch %lld/%ld"
- "Resuming sync from step %ld, skipping %ld completed steps"
- "Should not store message record for %s, account or alias mismatch"
- "Skipping save: persistent store coordinator has no stores attached"
- "com.apple.messages.sync.Initial"

```
