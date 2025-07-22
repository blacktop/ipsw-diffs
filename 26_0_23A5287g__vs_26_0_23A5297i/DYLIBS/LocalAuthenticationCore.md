## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-2005.0.40.0.0
-  __TEXT.__text: 0xf8bd0
+2005.0.49.0.0
+  __TEXT.__text: 0xf8c10
   __TEXT.__auth_stubs: 0x2400
-  __TEXT.__objc_methlist: 0x9a98
+  __TEXT.__objc_methlist: 0x9a90
   __TEXT.__const: 0x4b14
   __TEXT.__gcc_except_tab: 0x1a8c
   __TEXT.__oslogstring: 0x6841

   __TEXT.__unwind_info: 0x43d8
   __TEXT.__eh_frame: 0x2310
   __TEXT.__objc_classname: 0x2260
-  __TEXT.__objc_methname: 0xfbc5
+  __TEXT.__objc_methname: 0xfba6
   __TEXT.__objc_methtype: 0x48d2
-  __TEXT.__objc_stubs: 0xa760
+  __TEXT.__objc_stubs: 0xa740
   __DATA_CONST.__got: 0xb08
   __DATA_CONST.__const: 0x49e0
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_protolist: 0x630
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b88
+  __DATA_CONST.__objc_selrefs: 0x3b80
   __DATA_CONST.__objc_protorefs: 0x270
   __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x1210
   __AUTH_CONST.__const: 0x3a38
   __AUTH_CONST.__cfstring: 0x65a0
-  __AUTH_CONST.__objc_const: 0x39bc0
+  __AUTH_CONST.__objc_const: 0x39c08
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x3218

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DEDB90F2-09EC-38CA-9D13-039BE6AD051F
-  Functions: 6375
-  Symbols:   22145
-  CStrings:  6860
+  UUID: 376737F8-8F08-338E-81E4-1FB7AD61B6A6
+  Functions: 6374
+  Symbols:   22142
+  CStrings:  6859
 
Symbols:
+ GCC_except_table45
+ GCC_except_table54
+ GCC_except_table62
- +[LACSecureStorage isKeyAvailableForDataExchange:]
- GCC_except_table46
- GCC_except_table53
- GCC_except_table55
- GCC_except_table60
- GCC_except_table63
- GCC_except_table65
- _objc_msgSend$isKeyAvailableForDataExchange:
Functions:
~ -[LACSecureStorage setObject:forRequest:completionHandler:] : 1428 -> 1440
~ +[LACSecureStorage isKeyAvailable:] : 116 -> 188
- +[LACSecureStorage isKeyAvailableForDataExchange:]
CStrings:
+ "%@ XPC target UID: %u (UI)"
- "%@ XPC target UID: %d (UI)"
- "isKeyAvailableForDataExchange:"

```
