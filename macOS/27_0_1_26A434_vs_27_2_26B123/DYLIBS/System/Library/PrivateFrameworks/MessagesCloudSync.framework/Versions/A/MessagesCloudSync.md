## MessagesCloudSync

> `/System/Library/PrivateFrameworks/MessagesCloudSync.framework/Versions/A/MessagesCloudSync`

```diff

-1491.100.1.1.13
-  __TEXT.__text: 0xfee30
+1491.200.101.1.3
+  __TEXT.__text: 0x1072d8
   __TEXT.__objc_methlist: 0xcb0
-  __TEXT.__const: 0x98a0
-  __TEXT.__cstring: 0x3fc1
-  __TEXT.__constg_swiftt: 0x2c00
-  __TEXT.__swift5_typeref: 0x2826
-  __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x2ffa
-  __TEXT.__swift5_fieldmd: 0x3358
-  __TEXT.__swift5_assocty: 0x5b8
-  __TEXT.__oslogstring: 0x5723
-  __TEXT.__swift5_proto: 0x750
-  __TEXT.__swift5_types: 0x2d8
+  __TEXT.__const: 0x9bb0
+  __TEXT.__cstring: 0x40b1
+  __TEXT.__constg_swiftt: 0x2c60
+  __TEXT.__swift5_typeref: 0x28de
+  __TEXT.__swift5_builtin: 0x154
+  __TEXT.__swift5_reflstr: 0x30aa
+  __TEXT.__swift5_fieldmd: 0x33d8
+  __TEXT.__swift5_assocty: 0x618
+  __TEXT.__oslogstring: 0x5b23
+  __TEXT.__swift5_proto: 0x770
+  __TEXT.__swift5_types: 0x2e0
   __TEXT.__swift5_capture: 0xfd8
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0x90
-  __TEXT.__swift_as_entry: 0x430
-  __TEXT.__swift_as_ret: 0x4cc
-  __TEXT.__swift_as_cont: 0x96c
-  __TEXT.__unwind_info: 0x3710
-  __TEXT.__eh_frame: 0x9b2c
+  __TEXT.__swift_as_entry: 0x458
+  __TEXT.__swift_as_ret: 0x520
+  __TEXT.__swift_as_cont: 0xa04
+  __TEXT.__unwind_info: 0x38c8
+  __TEXT.__eh_frame: 0xa154
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xff0
+  __DATA_CONST.__objc_selrefs: 0x1048
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x7d8
-  __AUTH_CONST.__const: 0x8d89
+  __AUTH_CONST.__const: 0x8ea9
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x2758
+  __AUTH_CONST.__objc_const: 0x2768
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0xf48
-  __AUTH_CONST.__auth_ptr: 0x8d0
+  __AUTH_CONST.__auth_got: 0xfd0
+  __AUTH_CONST.__auth_ptr: 0x9d0
   __AUTH.__objc_data: 0x3d8
   __AUTH.__data: 0x508
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0xff0
-  __DATA.__bss: 0x8100
+  __DATA.__data: 0xfd8
+  __DATA.__bss: 0x8200
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x618
-  __DATA_DIRTY.__data: 0x26e8
-  __DATA_DIRTY.__bss: 0x4b00
+  __DATA_DIRTY.__data: 0x2770
+  __DATA_DIRTY.__bss: 0x4c80
   __DATA_DIRTY.__common: 0x270
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3819
+  Functions: 3928
   Symbols:   387
-  CStrings:  855
+  CStrings:  871
 
CStrings:
+ "Attachment reconcile aborting after batch due to: %@"
+ "Attachment reconcile already finished, skipping (%s)"
+ "Attachment reconcile disabled by server bag, skipping (%s)"
+ "Attachment reconcile drained for %s, marking finished (%s)"
+ "Attachment reconcile error writing record in zone "
+ "Attachment reconcile probe: no server asset for %s: %@"
+ "Attachment reconcile: error handling save for %@: %@"
+ "Attachment reconcile: writing %ld records to %s, %ld metadata-only (%s)"
+ "CloudKitAttachmentReconcileVersion"
+ "Encountered error moving recoverable message for guid %s %@"
+ "Error encountered marking orphaned/stray recoverable record for cloud deletion for guid %s %@"
+ "Failed to rebuild record from system fields when stripping assets; falling back to new record for %@"
+ "Missing recordName or zoneName for recoverable record guid %s; cannot validate, skipping"
+ "None of the %lld attachments in batch yielded a record ID, continuing to older messages"
+ "Transfer %s: could not size the record's asset at %s; not adopting the cloud copy"
+ "Transfer %s: could not size the record's asset at %s; not preferring the local copy"
+ "Transfer %s: incoming has unknown pgen state, but local is valid. Incoming stored pgen state %ld, resolved %ld, attributionInfo %s. Existing stored pgen state %ld, resolved %ld, attributionInfo %s"
+ "Transfer %s: local data newer than cloud; marking fieldsToSync %s to update server"
+ "attachmentDownloadTimeFrame"
+ "mdd-attachment-reconcile-enabled"
+ "resetRecoverableMessageChangeTokenVersion"
- "All %lld attachments in batch filtered by date, continuing to older messages"
- "Encountered error moving recoverable message part for guid %s %@"
- "Error encountered moving recoverable message %@"
- "Transfer %s: incoming has unknown pgen state, but local progressed past that, it is newer than cloud"
- "Transfer %s: local data newer than cloud; marking dirty to update server"
```
