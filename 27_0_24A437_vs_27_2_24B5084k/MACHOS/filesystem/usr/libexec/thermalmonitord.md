## thermalmonitord

> `/usr/libexec/thermalmonitord`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2083.0.0.0.0
-  __TEXT.__text: 0x51e24
-  __TEXT.__auth_stubs: 0x13d0
-  __TEXT.__objc_stubs: 0x4f00
+2087.40.7.0.0
+  __TEXT.__text: 0x51f70
+  __TEXT.__auth_stubs: 0x13e0
+  __TEXT.__objc_stubs: 0x4f20
   __TEXT.__objc_methlist: 0x4014
   __TEXT.__const: 0x1560
   __TEXT.__objc_classname: 0x1303
   __TEXT.__objc_methtype: 0x1b05
-  __TEXT.__objc_methname: 0x8388
+  __TEXT.__objc_methname: 0x839a
   __TEXT.__cstring: 0x4df6
   __TEXT.__gcc_except_tab: 0x3ac
-  __TEXT.__oslogstring: 0x9d54
-  __TEXT.__unwind_info: 0x1b40
+  __TEXT.__oslogstring: 0x9e28
+  __TEXT.__unwind_info: 0x1b48
   __DATA_CONST.__const: 0x1458
   __DATA_CONST.__cfstring: 0x6780
   __DATA_CONST.__objc_classlist: 0x520

   __DATA_CONST.__objc_dictobj: 0x730
   __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__auth_got: 0xa00
+  __DATA_CONST.__auth_got: 0xa08
   __DATA_CONST.__got: 0x630
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0xc948
-  __DATA.__objc_selrefs: 0x1988
+  __DATA.__objc_selrefs: 0x1990
   __DATA.__objc_ivar: 0xa30
   __DATA.__objc_data: 0x3340
   __DATA.__data: 0x370

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2000
-  Symbols:   416
-  CStrings:  3744
+  Functions: 2001
+  Symbols:   417
+  CStrings:  3748
 
Symbols:
+ _objc_retain_x20
CStrings:
+ "<Error> Thermal config: %s exists but could not be loaded, falling back to device class default"
+ "<Notice> Thermal config source: device class default (%s)"
+ "<Notice> Thermal config source: product-specific plist %s"
+ "fileExistsAtPath:"
```
