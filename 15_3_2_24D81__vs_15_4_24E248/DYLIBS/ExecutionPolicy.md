## ExecutionPolicy

> `/System/Library/Frameworks/ExecutionPolicy.framework/Versions/A/ExecutionPolicy`

```diff

-620.81.1.0.0
-  __TEXT.__text: 0x168c
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_methlist: 0xf8
+620.100.82.0.0
+  __TEXT.__text: 0x1688
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_methlist: 0x2a4
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__oslogstring: 0x78
   __TEXT.__cstring: 0x228
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__unwind_info: 0x108
   __TEXT.__objc_classname: 0x36
-  __TEXT.__objc_methname: 0x778
-  __TEXT.__objc_methtype: 0x4ce
+  __TEXT.__objc_methname: 0x798
+  __TEXT.__objc_methtype: 0x508
   __TEXT.__objc_stubs: 0x1e0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe0
+  __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x108
+  __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__const: 0x1f0
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x6a0
+  __AUTH_CONST.__objc_const: 0x370
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x68

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 963FEF65-6187-375B-9E1B-7910A6C1AC5D
-  Functions: 60
-  Symbols:   183
-  CStrings:  140
+  UUID: E5C40754-BD77-33C2-B3F8-76D24DD7153F
+  Functions: 67
+  Symbols:   191
+  CStrings:  142
 
Symbols:
+ +[SPLog exec].cold.1
+ +[SPLog generic].cold.1
+ +[SPLog kext].cold.1
+ +[SPLog measurements].cold.1
+ +[SPLog sampling].cold.1
+ +[SPLog signposts].cold.1
+ +[SPLog verboseLoggingEnabled].cold.1
+ _os_variant_allows_internal_security_policies
CStrings:
+ "reportEvent:withData:withReply:"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?B@\"NSError\">32"

```
