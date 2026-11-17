## SiriUI

> `/System/Library/PrivateFrameworks/SiriUI.framework/SiriUI`

```diff

-3610.10.1.0.0
-  __TEXT.__text: 0x44080
+3610.17.2.0.0
+  __TEXT.__text: 0x440b0
   __TEXT.__objc_methlist: 0x7374
   __TEXT.__const: 0x4f8
   __TEXT.__cstring: 0x382e

   __DATA_CONST.__objc_superrefs: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__got: 0xa60
-  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__cfstring: 0x2040
   __AUTH_CONST.__objc_const: 0xb848
   __AUTH_CONST.__objc_intobj: 0x2d0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2104
-  Symbols:   4346
+  Functions: 2106
+  Symbols:   4349
   CStrings:  532
 
Symbols:
+ GCC_except_table74
+ _MGGetLogicalDeviceDisplayCount
+ _SiriUIDeviceIsV68.isV68
+ _SiriUIDeviceIsV68.onceToken
+ ___SiriUIDeviceIsV68_block_invoke
- GCC_except_table73
- _MGGetProductType
Functions:
~ _SiriUIDeviceIsV68 : 68 -> 56
+ ___SiriUIDeviceIsV68_block_invoke
+ _SiriUIDeviceHasSideButton.cold.1
```
