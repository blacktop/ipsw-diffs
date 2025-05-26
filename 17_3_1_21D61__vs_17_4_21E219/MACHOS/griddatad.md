## griddatad

> `/usr/libexec/griddatad`

```diff

-62.0.0.0.0
+65.0.0.0.0
   __TEXT.__text: 0x2afc
   __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_stubs: 0x980

   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0xb8
   __TEXT.__cstring: 0x380
-  __TEXT.__objc_methname: 0xd1f
-  __TEXT.__oslogstring: 0x3dc
+  __TEXT.__objc_methname: 0xd33
+  __TEXT.__oslogstring: 0x400
   __TEXT.__objc_classname: 0x6c
   __TEXT.__objc_methtype: 0x534
   __TEXT.__unwind_info: 0x100

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA.__objc_const: 0x910
   __DATA.__objc_selrefs: 0x2d8
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xa0
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180

   - /usr/lib/libobjc.A.dylib
   Functions: 66
   Symbols:   105
-  CStrings:  271
+  CStrings:  272
 
CStrings:
+ "Coordinate (%{private}f,%{private}f) inside %@ %@"
+ "Looking for (%{private}lf, %{private}lf)"
+ "T@\"NSString\",?,R,C"
- "Coordinate (%f,%f) inside %@ %@"
- "Looking for (%lf, %lf)"

```
