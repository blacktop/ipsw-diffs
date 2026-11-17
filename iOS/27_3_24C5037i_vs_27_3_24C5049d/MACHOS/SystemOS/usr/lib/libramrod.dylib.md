## libramrod.dylib

> `/usr/lib/libramrod.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-3696.40.14.0.1
-  __TEXT.__text: 0xee0ec
+3696.60.5.0.0
+  __TEXT.__text: 0xee31c
   __TEXT.__objc_methlist: 0x119c
-  __TEXT.__cstring: 0x2bdaa
+  __TEXT.__cstring: 0x2bddf
   __TEXT.__const: 0x79130
   __TEXT.__gcc_except_tab: 0xb6c
   __TEXT.__oslogstring: 0xb92

   __TEXT.__objc_classname: 0x18b
   __TEXT.__objc_methname: 0x29fe
   __TEXT.__objc_methtype: 0xb58
-  __DATA_CONST.__const: 0x1f88
+  __DATA_CONST.__const: 0x1f98
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_selrefs: 0xcd8
   __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0x20b8
-  __AUTH_CONST.__cfstring: 0xc440
+  __AUTH_CONST.__cfstring: 0xc4a0
   __AUTH_CONST.__objc_const: 0x1ad0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib
-  Functions: 2870
-  Symbols:   1894
-  CStrings:  6379
+  Functions: 2872
+  Symbols:   1895
+  CStrings:  6383
 
Symbols:
+ _ramrod_hardware_partition_supports_hinge
CStrings:
+ "%@/hinge"
+ "%@/pet"
+ "BLOCK_SWITCH"
+ "hinge-hw-partition-size"
```
