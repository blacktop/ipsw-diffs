## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon`

```diff

-991.0.0.0.0
-  __TEXT.__text: 0x70f1c
+991.2.0.0.0
+  __TEXT.__text: 0x71010
   __TEXT.__auth_stubs: 0x1520
   __TEXT.__objc_methlist: 0x3254
   __TEXT.__const: 0x726
-  __TEXT.__oslogstring: 0x810f
+  __TEXT.__oslogstring: 0x817f
   __TEXT.__cstring: 0x3d13
-  __TEXT.__gcc_except_tab: 0x2594
+  __TEXT.__gcc_except_tab: 0x25e4
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__swift5_typeref: 0x2aa
   __TEXT.__swift5_capture: 0xa8

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x48
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x19b8
+  __TEXT.__unwind_info: 0x19c0
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_classname: 0x601
-  __TEXT.__objc_methname: 0xafb0
+  __TEXT.__objc_methname: 0xafbd
   __TEXT.__objc_methtype: 0x2444
-  __TEXT.__objc_stubs: 0x8fa0
+  __TEXT.__objc_stubs: 0x8fc0
   __DATA_CONST.__got: 0xce0
   __DATA_CONST.__const: 0x16a8
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2770
+  __DATA_CONST.__objc_selrefs: 0x2778
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x50

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2041
-  Symbols:   2710
-  CStrings:  3040
+  Functions: 2040
+  Symbols:   2709
+  CStrings:  3042
 
CStrings:
+ "\"Our ACDAccountStore got dealloced before we could call renewCredentials - likely our client went away early.\""
+ "defaultStore"

```
