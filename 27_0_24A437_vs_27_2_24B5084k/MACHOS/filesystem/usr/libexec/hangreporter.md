## hangreporter

> `/usr/libexec/hangreporter`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-426.0.0.0.0
-  __TEXT.__text: 0x257d0
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_stubs: 0x3480
-  __TEXT.__objc_methlist: 0x136c
-  __TEXT.__const: 0x2e0
-  __TEXT.__cstring: 0x431b
-  __TEXT.__oslogstring: 0x4d4f
+430.0.0.0.0
+  __TEXT.__text: 0x2622c
+  __TEXT.__auth_stubs: 0xf30
+  __TEXT.__objc_stubs: 0x3460
+  __TEXT.__objc_methlist: 0x1374
+  __TEXT.__const: 0x2b0
+  __TEXT.__cstring: 0x4378
+  __TEXT.__oslogstring: 0x4d97
   __TEXT.__objc_classname: 0x183
-  __TEXT.__objc_methname: 0x5c9a
+  __TEXT.__objc_methname: 0x5c96
   __TEXT.__objc_methtype: 0x8f8
-  __TEXT.__gcc_except_tab: 0xc94
-  __TEXT.__unwind_info: 0x8e0
-  __DATA_CONST.__const: 0x1680
-  __DATA_CONST.__cfstring: 0x5320
+  __TEXT.__gcc_except_tab: 0xcc4
+  __TEXT.__unwind_info: 0x900
+  __DATA_CONST.__const: 0x16f8
+  __DATA_CONST.__cfstring: 0x5340
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__auth_got: 0x7a8
   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x2eb8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 757
-  Symbols:   334
-  CStrings:  2137
+  Functions: 766
+  Symbols:   335
+  CStrings:  2141
 
Symbols:
+ _objc_retain_x5
CStrings:
+ "Failed to open tailspin file %@ to write App Launch extended attributes"
+ "allTaskingPrefNames"
+ "hangtracer.event_end"
+ "hangtracer.event_start"
+ "hangtracer.event_type"
+ "v16@?0@?<v@?@\"NSString\"@\"NSString\">8"
+ "v24@?0@\"NSString\"8@\"NSString\"16"
- "hangtracer.hang_end"
- "hangtracer.hang_start"
- "setDisplayKernelFrames:"
```
