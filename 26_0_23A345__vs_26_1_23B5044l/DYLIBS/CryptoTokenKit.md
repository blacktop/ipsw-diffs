## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

```diff

-805.0.21.0.0
-  __TEXT.__text: 0x4689c
-  __TEXT.__auth_stubs: 0xc20
+805.40.2.0.0
+  __TEXT.__text: 0x468a4
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__delay_helper: 0x1b4
   __TEXT.__objc_methlist: 0x452c
   __TEXT.__gcc_except_tab: 0x1670
   __TEXT.__const: 0x280
-  __TEXT.__cstring: 0x2b48
+  __TEXT.__cstring: 0x2bd5
   __TEXT.__oslogstring: 0x3487
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__unwind_info: 0x16a0

   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0xaa0
   __AUTH_CONST.__cfstring: 0x2560
   __AUTH_CONST.__objc_const: 0x8610

   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x570
-  __DATA.__data: 0xe48
+  __DATA.__data: 0xe50
   __DATA.__bss: 0x1c8
   __DATA_DIRTY.__objc_data: 0x19a0
   __DATA_DIRTY.__bss: 0x2b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 222E8D5F-03DC-3A07-9899-D8E524ED5ABC
+  UUID: D65DC1B1-D69D-3B24-B1B0-0FF0E00CBDD8
   Functions: 1940
-  Symbols:   6887
-  CStrings:  3064
+  Symbols:   6895
+  CStrings:  3066
 
Symbols:
+ _dlopen
+ _dlopenHelper$LocalAuthentication
+ _dlopenHelper$PlugInKit
+ _dlopenHelperFlag$LocalAuthentication
+ _dlopenHelperFlag$PlugInKit
+ _gotLoadHelper_x19$_OBJC_CLASS_$_PKService
+ _gotLoadHelper_x8$_LAErrorDomain
+ _gotLoadHelper_x8$_OBJC_CLASS_$_LAContext
Functions:
~ -[TKTokenConnection listener:shouldAcceptNewConnection:] : 156 -> 164
CStrings:
+ "/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication"
+ "/System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit"

```
