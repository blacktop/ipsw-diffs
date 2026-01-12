## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

```diff

-684.80.5.0.0
-  __TEXT.__text: 0x5fda4
+684.80.6.0.2
+  __TEXT.__text: 0x60244
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0x591c
+  __TEXT.__objc_methlist: 0x5924
   __TEXT.__const: 0x9e8
   __TEXT.__cstring: 0x4b7c
-  __TEXT.__oslogstring: 0x42ba
+  __TEXT.__oslogstring: 0x4350
   __TEXT.__gcc_except_tab: 0xcfc
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x74

   __TEXT.__unwind_info: 0x1898
   __TEXT.__eh_frame: 0x858
   __TEXT.__objc_classname: 0xdbf
-  __TEXT.__objc_methname: 0x9da2
+  __TEXT.__objc_methname: 0x9de3
   __TEXT.__objc_methtype: 0x12de
-  __TEXT.__objc_stubs: 0x7ea0
+  __TEXT.__objc_stubs: 0x7f00
   __DATA_CONST.__got: 0x818
   __DATA_CONST.__const: 0x1238
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2518
+  __DATA_CONST.__objc_selrefs: 0x2530
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x108

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6BDB1B65-83FD-3B95-AE78-326AF9517E8B
-  Functions: 2446
-  Symbols:   7756
-  CStrings:  3586
+  UUID: 98AEB611-8913-318C-B4F1-51D9F748456D
+  Functions: 2447
+  Symbols:   7761
+  CStrings:  3591
 
Symbols:
+ -[_DPDediscoReporter removeExpiredRecords:forKey:storage:]
+ _objc_msgSend$array
+ _objc_msgSend$removeExpiredRecords:forKey:storage:
+ _objc_msgSend$timeIntervalSince1970
Functions:
~ -[_DPDediscoReporter directlyUploadDediscoRecords:forKey:keyProperties:storage:] : 612 -> 648
+ -[_DPDediscoReporter removeExpiredRecords:forKey:storage:]
CStrings:
+ "%@: Filtered out %lu expired records for key=%@"
+ "%@: Record (expiration: %f) is expired or will be expired within %.0fs skipping submission for key=%@"
+ "array"
+ "removeExpiredRecords:forKey:storage:"
+ "timeIntervalSince1970"

```
