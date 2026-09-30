## BTLEServer

> `/usr/sbin/BTLEServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2700.38.0.0.0
-  __TEXT.__text: 0x49824
+2700.39.0.0.0
+  __TEXT.__text: 0x499dc
   __TEXT.__auth_stubs: 0xc70
   __TEXT.__objc_stubs: 0x7180
   __TEXT.__objc_methlist: 0x487c

   __TEXT.__cstring: 0x1f82
   __TEXT.__const: 0x680
   __TEXT.__objc_methname: 0xaed7
-  __TEXT.__oslogstring: 0x702a
+  __TEXT.__oslogstring: 0x70ae
   __TEXT.__gcc_except_tab: 0x10a8
   __TEXT.__ustring: 0xbe
   __TEXT.__unwind_info: 0x1130

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x650
-  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__got: 0x510
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x9a78
   __DATA.__objc_selrefs: 0x26a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1799
+  Functions: 1802
   Symbols:   366
-  CStrings:  3071
+  CStrings:  3073
 
CStrings:
+ "DoAP codec list read length (%lu) exceeded data length (%lu)"
+ "DoAP stream client header read length (%lu) exceeded data length (%lu)"
```
