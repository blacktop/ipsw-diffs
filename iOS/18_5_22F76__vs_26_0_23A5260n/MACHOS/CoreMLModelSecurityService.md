## CoreMLModelSecurityService

> `/System/Library/Frameworks/CoreML.framework/XPCServices/CoreMLModelSecurityService.xpc/CoreMLModelSecurityService`

```diff

-3405.2.1.0.0
-  __TEXT.__text: 0x6abc
+3500.25.1.0.0
+  __TEXT.__text: 0x6d04
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0xd00
+  __TEXT.__objc_stubs: 0xda0
   __TEXT.__objc_methlist: 0xa64
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x72c
   __TEXT.__objc_classname: 0x1ca
-  __TEXT.__objc_methname: 0x139c
+  __TEXT.__objc_methname: 0x13d3
   __TEXT.__objc_methtype: 0x78e
   __TEXT.__cstring: 0x3a7
   __TEXT.__oslogstring: 0x5ac
   __TEXT.__unwind_info: 0x308
   __DATA_CONST.__auth_got: 0x240
-  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x50

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x1050
-  __DATA.__objc_selrefs: 0x590
+  __DATA.__objc_selrefs: 0x5b8
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x2a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BCE05D5F-37D0-32D2-898E-2ABBBC2181C0
+  UUID: B6D36D90-60B6-3E4E-B3B4-C5C28F7960AC
   Functions: 206
-  Symbols:   158
-  CStrings:  418
+  Symbols:   154
+  CStrings:  423
 
Symbols:
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
Functions:
~ _ModelKeyServerAPIFetchKeyResultReadFrom : 844 -> 992
~ _ModelKeyServerAPIFetchKeyResponseReadFrom : 728 -> 876
~ _ModelKeyServerAPIFetchKeyRequestReadFrom : 660 -> 792
~ _ModelKeyServerAPIRawKeyReadFrom : 436 -> 488
~ _ModelKeyServerAPISignedKeyReadFrom : 392 -> 444
~ _ModelKeyServerAPIResultErrorReadFrom : 392 -> 444
CStrings:
+ "_setError"
+ "getBytes:range:"
+ "length"
+ "position"
+ "setPosition:"

```
