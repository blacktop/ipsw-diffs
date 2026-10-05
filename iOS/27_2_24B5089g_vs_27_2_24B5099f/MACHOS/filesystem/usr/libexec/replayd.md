## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-765.11.1.0.0
-  __TEXT.__text: 0xb96d0
+765.14.1.0.0
+  __TEXT.__text: 0xb9740
   __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_stubs: 0xf320
-  __TEXT.__objc_methlist: 0x74a0
+  __TEXT.__objc_stubs: 0xf340
+  __TEXT.__objc_methlist: 0x74b0
   __TEXT.__const: 0x3e4
   __TEXT.__gcc_except_tab: 0xfc8
-  __TEXT.__objc_methname: 0x15f58
+  __TEXT.__objc_methname: 0x15f73
   __TEXT.__oslogstring: 0x167e9
-  __TEXT.__cstring: 0x17cf7
+  __TEXT.__cstring: 0x17d0c
   __TEXT.__objc_classname: 0xa44
   __TEXT.__objc_methtype: 0x43f5
-  __TEXT.__unwind_info: 0x33e0
+  __TEXT.__unwind_info: 0x33e8
   __DATA_CONST.__const: 0x2b00
-  __DATA_CONST.__cfstring: 0x5d20
+  __DATA_CONST.__cfstring: 0x5d40
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x130

   __DATA_CONST.__auth_got: 0xca0
   __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x11388
-  __DATA.__objc_selrefs: 0x4720
+  __DATA.__objc_const: 0x11398
+  __DATA.__objc_selrefs: 0x4728
   __DATA.__objc_ivar: 0xd84
   __DATA.__objc_data: 0x18b0
   __DATA.__data: 0xe54

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3682
+  Functions: 3683
   Symbols:   802
-  CStrings:  7387
+  CStrings:  7389
 
CStrings:
+ "RPEnableEdgeLightDev"
+ "edgeLightDevOverrideActive"
```
