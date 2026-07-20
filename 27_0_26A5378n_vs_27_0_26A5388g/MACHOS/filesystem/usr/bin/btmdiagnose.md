## btmdiagnose

> `/usr/bin/btmdiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-365.0.0.0.0
-  __TEXT.__text: 0x25860
+368.0.0.0.0
+  __TEXT.__text: 0x259fc
   __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_stubs: 0x35a0
+  __TEXT.__objc_stubs: 0x3620
   __TEXT.__objc_methlist: 0x171c
   __TEXT.__const: 0x122
   __TEXT.__gcc_except_tab: 0x418
-  __TEXT.__objc_methname: 0x41c7
-  __TEXT.__cstring: 0x1793
+  __TEXT.__objc_methname: 0x4235
+  __TEXT.__cstring: 0x17b3
   __TEXT.__oslogstring: 0x1dbc
   __TEXT.__objc_classname: 0x176
   __TEXT.__objc_methtype: 0xfb1

   __TEXT.__unwind_info: 0x768
   __TEXT.__eh_frame: 0x260
   __DATA_CONST.__const: 0x800
-  __DATA_CONST.__cfstring: 0x1ac0
+  __DATA_CONST.__cfstring: 0x1b40
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__auth_ptr: 0x48
   __DATA.__objc_const: 0x2370
-  __DATA.__objc_selrefs: 0x11b8
+  __DATA.__objc_selrefs: 0x11d8
   __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x430

   - /usr/lib/swift/libswiftos.dylib
   Functions: 681
   Symbols:   269
-  CStrings:  1301
+  CStrings:  1309
 
Functions:
~ sub_10000b2b4 : 64 -> 476
CStrings:
+ "*"
+ "/Users/"
+ "/Users/%@"
+ "/Users/Shared/"
+ "componentsJoinedByString:"
+ "componentsSeparatedByString:"
+ "fileSystemRepresentation"
+ "setObject:atIndexedSubscript:"
```
