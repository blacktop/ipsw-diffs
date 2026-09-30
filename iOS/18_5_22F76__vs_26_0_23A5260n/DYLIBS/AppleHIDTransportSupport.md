## AppleHIDTransportSupport

> `/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport`

```diff

-8150.1.0.0.0
-  __TEXT.__text: 0x4184
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x524
+9100.28.0.0.0
+  __TEXT.__text: 0x433c
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_methlist: 0x534
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x3f8
+  __TEXT.__cstring: 0x410
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__unwind_info: 0x178
   __TEXT.__objc_classname: 0x3f
-  __TEXT.__objc_methname: 0x981
+  __TEXT.__objc_methname: 0x9a1
   __TEXT.__objc_methtype: 0x1ba
-  __TEXT.__objc_stubs: 0x780
+  __TEXT.__objc_stubs: 0x7a0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x330
+  __DATA_CONST.__objc_selrefs: 0x340
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x540
+  __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__objc_const: 0x6a0
   __DATA.__objc_ivar: 0x4c
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 957F32CD-40FB-3B54-A14F-1C30B8D8C344
-  Functions: 113
-  Symbols:   460
-  CStrings:  270
+  UUID: C70F2329-B5C0-33C1-AD22-973570684DF9
+  Functions: 114
+  Symbols:   464
+  CStrings:  274
 
Symbols:
+ +[AHTBootLoader allBootloaders]
+ _IOServiceGetState
+ _objc_msgSend$isEqualToNumber:
Functions:
~ -[AHTCommon open] : 60 -> 112
+ +[AHTBootLoader allBootloaders]
~ -[AHTLoader initWithService:] : 392 -> 404
~ -[AHTLoader loadImage:payloadOnly:options:error:] : 352 -> 516
CStrings:
+ "AHTBootloadLoadImageEnd"
+ "allBootloaders"
+ "isEqualToNumber:"

```
