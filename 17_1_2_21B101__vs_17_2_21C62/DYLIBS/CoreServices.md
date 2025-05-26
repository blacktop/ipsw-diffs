## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1299.2.2.0.0
-  __TEXT.__text: 0x16fc10
+1299.2.3.1.0
+  __TEXT.__text: 0x16febc
   __TEXT.__auth_stubs: 0x3250
   __TEXT.__objc_methlist: 0xa864
   __TEXT.__const: 0x758
-  __TEXT.__cstring: 0x1db90
-  __TEXT.__oslogstring: 0x11219
-  __TEXT.__gcc_except_tab: 0x1be5c
+  __TEXT.__cstring: 0x1db72
+  __TEXT.__oslogstring: 0x11284
+  __TEXT.__gcc_except_tab: 0x1bed8
   __TEXT.__ustring: 0x132
-  __TEXT.__unwind_info: 0x935c
+  __TEXT.__unwind_info: 0x9354
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x18c9
   __TEXT.__objc_methname: 0x1a310
   __TEXT.__objc_methtype: 0x8ef1
   __TEXT.__objc_stubs: 0xe480
   __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x62b8
+  __DATA_CONST.__const: 0x62d8
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_const: 0xcfa8
   __DATA_CONST.__objc_selrefs: 0x5488
   __DATA_CONST.__objc_arraydata: 0x140
-  __AUTH_CONST.__cfstring: 0x14a80
-  __AUTH_CONST.__const: 0x2b70
+  __AUTH_CONST.__cfstring: 0x14a60
+  __AUTH_CONST.__const: 0x2bb0
   __AUTH_CONST.__auth_ptr: 0x60
   __AUTH_CONST.__objc_intobj: 0x750
   __AUTH_CONST.__objc_const: 0x5150

   __DATA.__objc_superrefs: 0x480
   __DATA.__objc_ivar: 0x96c
   __DATA.__data: 0x1788
-  __DATA.__bss: 0x590
+  __DATA.__bss: 0x5a0
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__data: 0xd8

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7530
-  Symbols:   24162
-  CStrings:  9597
+  Functions: 7532
+  Symbols:   24170
+  CStrings:  9601
 
Symbols:
+ __LSOpenLog
+ __LSOpenLog.once
+ __LSOpenLog.result
+ ____LSOpenLog_block_invoke
+ ___block_descriptor_32_e15_v32?0816^B24l
+ ___block_literal_global.28
+ ___block_literal_global.520
- ___block_literal_global.31
CStrings:
+ "open"
+ "pid %ld issuing open of %@ by %@, doc %@ on behalf of %ld"
+ "pid %ld opening app link %@ %@"
+ "pid %ld opening user activity %@ of type %@"
+ "pid %ld requests to open %@"
+ "pid %ld requests to open application with identifier %@"
- "Marking %{private}@ as .requiresSecureLaunch because it has a com.apple.developer.launchservices. entitlement"
- "com.apple.developer.launchservices"

```
