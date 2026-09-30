## absd

> `/usr/sbin/absd`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0x26a8bc
+  __TEXT.__text: 0x2c4538
   __TEXT.__auth_stubs: 0x1f0
   __TEXT.__cstring: 0x31
-  __TEXT.__const: 0x44ab0
+  __TEXT.__const: 0x44df0
   __TEXT.__unwind_info: 0x558
-  __TEXT.__eh_frame: 0x1578
+  __TEXT.__eh_frame: 0x1458
   __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x16388
+  __DATA_CONST.__const: 0x15388
   __DATA_CONST.__cfstring: 0x40
-  __DATA.__data: 0x4d0
-  __DATA.__common: 0x1458
+  __DATA.__data: 0x550
+  __DATA.__common: 0x1450
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  Functions: 244
+  Functions: 262
   Symbols:   94
   CStrings:  4
 
Symbols:
+ _os_release
+ _os_transaction_create
- _xpc_transaction_begin
- _xpc_transaction_end

```
