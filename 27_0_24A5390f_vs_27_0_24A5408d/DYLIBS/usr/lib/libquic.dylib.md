## libquic.dylib

> `/usr/lib/libquic.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__oslogstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-6681.0.514.502.1
-  __TEXT.__text: 0xd0174
+6681.2.2.0.0
+  __TEXT.__text: 0xd01cc
   __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x3b5
-  __TEXT.__cstring: 0x87e1
+  __TEXT.__cstring: 0x8823
   __TEXT.__oslogstring: 0x12459
-  __TEXT.__unwind_info: 0xd28
+  __TEXT.__unwind_info: 0xd30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2590
+  __DATA_CONST.__const: 0x25b0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8

   __AUTH_CONST.__const: 0xcd0
   __AUTH_CONST.__cfstring: 0x1320
   __AUTH_CONST.__objc_const: 0xf8
-  __AUTH_CONST.__auth_got: 0xdd0
+  __AUTH_CONST.__auth_got: 0xdd8
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x118
   __DATA.__objc_ivar: 0xc

   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x520
   __DATA_DIRTY.__data: 0x1c
-  __DATA_DIRTY.__bss: 0x670
+  __DATA_DIRTY.__bss: 0x660
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1153
-  Symbols:   1708
-  CStrings:  2604
+  Functions: 1156
+  Symbols:   1711
+  CStrings:  2606
 
Symbols:
+ _nw_parameters_is_fallback
+ _quic_conn_is_cellular_fallback
+ _quic_path_set_is_preferred_address
CStrings:
+ "quic_conn_is_cellular_fallback"
+ "quic_path_set_is_preferred_address"
```
