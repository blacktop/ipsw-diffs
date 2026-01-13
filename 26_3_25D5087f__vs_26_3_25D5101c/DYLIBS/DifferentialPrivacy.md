## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/Versions/A/DifferentialPrivacy`

```diff

-684.80.5.0.0
-  __TEXT.__text: 0x6793c
+684.80.6.0.2
+  __TEXT.__text: 0x67e4c
   __TEXT.__auth_stubs: 0x1020
-  __TEXT.__objc_methlist: 0x58bc
+  __TEXT.__objc_methlist: 0x58c4
   __TEXT.__const: 0x9e8
   __TEXT.__cstring: 0x4bcc
-  __TEXT.__oslogstring: 0x4175
+  __TEXT.__oslogstring: 0x420b
   __TEXT.__gcc_except_tab: 0xb48
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x74

   __TEXT.__unwind_info: 0x18e0
   __TEXT.__eh_frame: 0x858
   __TEXT.__objc_classname: 0xdbf
-  __TEXT.__objc_methname: 0x9cde
+  __TEXT.__objc_methname: 0x9d1f
   __TEXT.__objc_methtype: 0x12de
-  __TEXT.__objc_stubs: 0x7d00
+  __TEXT.__objc_stubs: 0x7d60
   __DATA_CONST.__got: 0x838
   __DATA_CONST.__const: 0x8b8
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24d8
+  __DATA_CONST.__objc_selrefs: 0x24f0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x108

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D7148C90-ADAC-341D-9ABB-8D4511688D0E
-  Functions: 2467
-  Symbols:   5573
-  CStrings:  3572
+  UUID: 341DA8B0-D0C5-3174-A467-0B2A95E06624
+  Functions: 2468
+  Symbols:   5577
+  CStrings:  3577
 
Symbols:
+ -[_DPDediscoReporter removeExpiredRecords:forKey:storage:]
+ _objc_msgSend$array
+ _objc_msgSend$removeExpiredRecords:forKey:storage:
+ _objc_msgSend$timeIntervalSince1970
Functions:
~ -[_DPDediscoReporter directlyUploadDediscoRecords:forKey:keyProperties:storage:] : 688 -> 724
+ -[_DPDediscoReporter removeExpiredRecords:forKey:storage:]
CStrings:
+ "%@: Filtered out %lu expired records for key=%@"
+ "%@: Record (expiration: %f) is expired or will be expired within %.0fs skipping submission for key=%@"
+ "array"
+ "removeExpiredRecords:forKey:storage:"
+ "timeIntervalSince1970"

```
