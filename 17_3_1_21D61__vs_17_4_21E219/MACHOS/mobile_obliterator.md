## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-299.40.2.0.0
-  __TEXT.__text: 0x12d30
+303.0.0.0.0
+  __TEXT.__text: 0x12d04
   __TEXT.__auth_stubs: 0x1350
   __TEXT.__objc_stubs: 0x120
-  __TEXT.__cstring: 0x8133
+  __TEXT.__cstring: 0x812b
   __TEXT.__const: 0x688
   __TEXT.__gcc_except_tab: 0x110
   __TEXT.__objc_methname: 0xdb

   __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__cfstring: 0xd20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x10
   __DATA.__objc_selrefs: 0x48
-  __DATA.__objc_classrefs: 0x10
   __DATA.__data: 0x510
   __DATA.__common: 0x200
   __DATA.__bss: 0x488
CStrings:
+ "%s: Skipping safe attempt, returning 0 to try normal boot (also clearing NVRAM Key indicating obliteration should run)"
- "%s: Skipping safe attempt, returning ECANCELED to try normal boot (also clearing NVRAM Key indicating obliteration should run)"

```
