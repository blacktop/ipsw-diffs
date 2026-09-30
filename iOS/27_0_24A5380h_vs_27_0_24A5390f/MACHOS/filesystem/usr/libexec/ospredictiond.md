## ospredictiond

> `/usr/libexec/ospredictiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-282.0.0.0.0
-  __TEXT.__text: 0x66bb8
+284.0.0.0.0
+  __TEXT.__text: 0x66d50
   __TEXT.__auth_stubs: 0x910
   __TEXT.__objc_stubs: 0x97e0
   __TEXT.__objc_methlist: 0x92d0
   __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x558f
+  __TEXT.__cstring: 0x55a0
   __TEXT.__objc_methname: 0x15177
-  __TEXT.__oslogstring: 0x717b
+  __TEXT.__oslogstring: 0x71ee
   __TEXT.__objc_classname: 0xe10
   __TEXT.__objc_methtype: 0x2456
-  __TEXT.__gcc_except_tab: 0x868
+  __TEXT.__gcc_except_tab: 0x870
   __TEXT.__ustring: 0x2a
-  __TEXT.__unwind_info: 0x1488
-  __DATA_CONST.__const: 0x10b0
+  __TEXT.__unwind_info: 0x1490
+  __DATA_CONST.__const: 0x10d0
   __DATA_CONST.__cfstring: 0x62a0
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA.__objc_ivar: 0xdbc
   __DATA.__objc_data: 0x27b0
   __DATA.__data: 0x780
-  __DATA.__bss: 0x1e0
+  __DATA.__bss: 0x1f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3299
+  Functions: 3304
   Symbols:   285
-  CStrings:  4763
+  CStrings:  4766
 
CStrings:
+ "Alarm query timed out after 5s — alarm snap disabled for this prediction query"
+ "Next alarm fire date: %{time_t}ld"
+ "inactivity.alarm"
```
