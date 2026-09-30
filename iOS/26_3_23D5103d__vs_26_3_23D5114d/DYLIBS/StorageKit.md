## StorageKit

> `/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit`

```diff

-1024.80.3.0.0
-  __TEXT.__text: 0x2bf54
+1024.80.4.0.0
+  __TEXT.__text: 0x2c6d4
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x352c
+  __TEXT.__objc_methlist: 0x3564
   __TEXT.__const: 0x10a
-  __TEXT.__oslogstring: 0x142a
-  __TEXT.__cstring: 0x309c
-  __TEXT.__gcc_except_tab: 0x13b8
+  __TEXT.__oslogstring: 0x1493
+  __TEXT.__cstring: 0x316c
+  __TEXT.__gcc_except_tab: 0x13f8
   __TEXT.__swift5_typeref: 0x56
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__constg_swiftt: 0x74
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xc38
+  __TEXT.__unwind_info: 0xc58
   __TEXT.__objc_classname: 0x697
-  __TEXT.__objc_methname: 0x6ca2
-  __TEXT.__objc_methtype: 0xfa1
-  __TEXT.__objc_stubs: 0x62c0
+  __TEXT.__objc_methname: 0x6d27
+  __TEXT.__objc_methtype: 0xff9
+  __TEXT.__objc_stubs: 0x6300
   __DATA_CONST.__got: 0x328
   __DATA_CONST.__const: 0x908
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1db0
+  __DATA_CONST.__objc_selrefs: 0x1dc8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x588
   __AUTH_CONST.__cfstring: 0x35a0
-  __AUTH_CONST.__objc_const: 0x7b10
+  __AUTH_CONST.__objc_const: 0x7b20
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 86F6E3A8-FC81-319B-8D03-BB4981065C1E
-  Functions: 1194
-  Symbols:   4558
-  CStrings:  2740
+  UUID: A66064E3-CFC1-3B75-AEAE-8CF5EBACA387
+  Functions: 1200
+  Symbols:   4573
+  CStrings:  2753
 
Symbols:
+ -[SKHelperClient diskForPath:blocking:withCallbackBlock:]
+ -[SKHelperClient diskForPath:withCallbackBlock:]
+ -[SKManager _diskForPath:isNetworkMount:]
+ -[SKManager _diskForString:isNetworkMount:]
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table56
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table81
+ GCC_except_table83
+ GCC_except_table91
+ ___25-[SKManager diskForPath:]_block_invoke
+ ___57-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke
+ ___57-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke_2
+ ___57-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke_3
+ _objc_msgSend$_diskForPath:isNetworkMount:
+ _objc_msgSend$_diskForString:isNetworkMount:
+ _objc_msgSend$diskForPath:blocking:withCallbackBlock:
+ _objc_msgSend$diskForPath:withCompletionUUID:
- -[SKManager _diskForPath:]
- -[SKManager _diskForString:]
- GCC_except_table30
- GCC_except_table34
- GCC_except_table40
- GCC_except_table42
- GCC_except_table51
- GCC_except_table54
- GCC_except_table58
- GCC_except_table59
- GCC_except_table62
- GCC_except_table66
- GCC_except_table74
- GCC_except_table80
- GCC_except_table82
- GCC_except_table86
- _objc_msgSend$_diskForPath:
- _objc_msgSend$_diskForString:
CStrings:
+ "%s: %@ is a network mount point"
+ "%s: Cannot find disk for path %@, syncing disks with daemon"
+ "%s: Found %@"
+ "-[SKHelperClient diskForPath:blocking:withCallbackBlock:]"
+ "-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke_3"
+ "-[SKManager _diskForPath:isNetworkMount:]"
+ "-[SKManager diskForPath:]"
+ "@32@0:8@16^B24"
+ "_diskForPath:isNetworkMount:"
+ "_diskForString:isNetworkMount:"
+ "diskForPath:blocking:withCallbackBlock:"
+ "diskForPath:withCallbackBlock:"
+ "diskForPath:withCompletionUUID:"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"SKDisk\">24"
- "_diskForPath:"
- "_diskForString:"

```
