## BTLEServer

> `/usr/sbin/BTLEServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2700.38.0.0.0
-  __TEXT.__text: 0x7f744
+2700.39.0.0.0
+  __TEXT.__text: 0x7f8e4
   __TEXT.__auth_stubs: 0x10f0
   __TEXT.__objc_stubs: 0xcf80
   __TEXT.__objc_methlist: 0x7e94
   __TEXT.__const: 0x900
   __TEXT.__cstring: 0x363c
   __TEXT.__objc_methname: 0x13364
-  __TEXT.__oslogstring: 0xd852
+  __TEXT.__oslogstring: 0xd8d6
   __TEXT.__objc_classname: 0x900
   __TEXT.__objc_methtype: 0x318a
   __TEXT.__gcc_except_tab: 0x13c4

   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x890
-  __DATA_CONST.__got: 0x9b8
+  __DATA_CONST.__got: 0x9b0
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0xfcb8
   __DATA.__objc_selrefs: 0x42f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3165
+  Functions: 3167
   Symbols:   572
-  CStrings:  5255
+  CStrings:  5257
 
CStrings:
+ "DoAP codec list read length (%lu) exceeded data length (%lu)"
+ "DoAP stream client header read length (%lu) exceeded data length (%lu)"
```
