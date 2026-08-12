## MarkupUI

> `/System/Library/PrivateFrameworks/MarkupUI.framework/MarkupUI`

```diff

-581.0.0.0.0
-  __TEXT.__text: 0x28ca8
+582.0.0.0.0
+  __TEXT.__text: 0x28cf8
   __TEXT.__objc_methlist: 0x3d64
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
   __AUTH_CONST.__objc_const: 0x4a40
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libobjc.A.dylib
   Functions: 1018
   Symbols:   3296
-  CStrings:  396
+  CStrings:  398
 
Functions:
~ -[MUPayloadEncryption decryptData:] : 392 -> 472
CStrings:
+ "MUPayloadEncryption: %lu bytes is not a valid encrypted payload length. Returning nil."
+ "MUPayloadEncryption: decrypted %lu bytes, too few to contain the salt prefix. Returning nil."
```
