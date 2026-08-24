## MarkupUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/MarkupUI.framework/Versions/A/MarkupUI`

```diff

-581.0.0.0.0
-  __TEXT.__text: 0x288c8
+582.0.0.0.0
+  __TEXT.__text: 0x28918
   __TEXT.__objc_methlist: 0x3d3c
   __TEXT.__const: 0x120
   __TEXT.__gcc_except_tab: 0x5c0
-  __TEXT.__cstring: 0x29c4
+  __TEXT.__cstring: 0x2a78
   __TEXT.__dlopen_cstrs: 0x112
   __TEXT.__unwind_info: 0xad8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0x6d0
   __AUTH_CONST.__const: 0x130
-  __AUTH_CONST.__cfstring: 0x2620
+  __AUTH_CONST.__cfstring: 0x2660
   __AUTH_CONST.__objc_const: 0x4a10
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libobjc.A.dylib
   Functions: 1015
   Symbols:   3283
-  CStrings:  396
+  CStrings:  398
 
Functions:
~ -[MUPayloadEncryption decryptData:] : 388 -> 468
CStrings:
+ "MUPayloadEncryption: %lu bytes is not a valid encrypted payload length. Returning nil."
+ "MUPayloadEncryption: decrypted %lu bytes, too few to contain the salt prefix. Returning nil."
```
