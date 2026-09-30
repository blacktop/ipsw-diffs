## MessagesCloudSync

> `/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync`

```diff

-  __TEXT.__text: 0xf4c3c
-  __TEXT.__auth_stubs: 0x1f90
+  __TEXT.__text: 0xf7328
+  __TEXT.__auth_stubs: 0x1fa0
   __TEXT.__objc_methlist: 0xb50
-  __TEXT.__const: 0x9680
+  __TEXT.__const: 0x96a0
   __TEXT.__cstring: 0x3e11
   __TEXT.__constg_swiftt: 0x2b88
   __TEXT.__swift5_typeref: 0x2728

   __TEXT.__swift5_reflstr: 0x2faa
   __TEXT.__swift5_fieldmd: 0x32fc
   __TEXT.__swift5_assocty: 0x5a0
-  __TEXT.__oslogstring: 0x5103
+  __TEXT.__oslogstring: 0x5293
   __TEXT.__swift5_proto: 0x728
   __TEXT.__swift5_types: 0x2d4
   __TEXT.__swift5_capture: 0xef4
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0x8c
-  __TEXT.__swift_as_entry: 0x42c
-  __TEXT.__swift_as_ret: 0x4b8
-  __TEXT.__unwind_info: 0x35a0
-  __TEXT.__eh_frame: 0x985c
+  __TEXT.__swift_as_entry: 0x430
+  __TEXT.__swift_as_ret: 0x4bc
+  __TEXT.__unwind_info: 0x3598
+  __TEXT.__eh_frame: 0x989c
   __TEXT.__objc_classname: 0x752
   __TEXT.__objc_methname: 0x3321
   __TEXT.__objc_methtype: 0x944

   __DATA_CONST.__objc_selrefs: 0xeb8
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xfd0
+  __AUTH_CONST.__auth_got: 0xfd8
   __AUTH_CONST.__const: 0x8b09
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x2598

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3724
+  Functions: 3725
   Symbols:   407
-  CStrings:  1550
+  CStrings:  1556
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
CStrings:
+ "Business chat is not supported for message %s, dropping"
+ "Dropped %ld/%ld records of type %s during import from syncStore! Failed GUIDs: %s"
+ "Error importing transfer %s - %@"
+ "Error importing: %@ for recordType %s, guid = %s, record.recordType %s, record.recordName = %s)"
+ "Existing item with no guid, dropping"
+ "Failed to generate IMMessageItem %s, dropping"
+ "Import was .unsupported for recordType %s, guid %s"
+ "Item is an emojiTapBack but emojiTapbacks are not enabled, dropping"
+ "Item is not compatible with MIC %s"
+ "Item is not compatible with MIC %s, dropping"
+ "No record type for recordType %s guid %s"
+ "Record is .unknown for recordType %s guid %s"
+ "Should not store message record for %s, account or alias mismatch, dropping"
- "Business chat is not supported, do not import message %s"
- "Error importing: %@ for record(guid = %s, recordType = %s, recordName = %s)"
- "Existing item with no guid, do not store"
- "Failed to generate IMMessageItem %s"
- "Found %ld records without GUIDs!"
- "No record type for record guid %s"
- "Should not store message record for %s, account or alias mismatch"

```
