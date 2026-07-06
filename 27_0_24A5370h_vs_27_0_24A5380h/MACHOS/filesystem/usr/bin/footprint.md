## footprint

> `/usr/bin/footprint`

```diff

-  __TEXT.__text: 0x1fa48
+  __TEXT.__text: 0x1fae0
   __TEXT.__auth_stubs: 0xc40
   __TEXT.__objc_stubs: 0x23e0
   __TEXT.__objc_methlist: 0x124c
   __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x2ceb
+  __TEXT.__cstring: 0x2d73
   __TEXT.__objc_methname: 0x24d3
   __TEXT.__objc_classname: 0x1db
   __TEXT.__objc_methtype: 0x7f9

   __TEXT.__oslogstring: 0x21
   __TEXT.__unwind_info: 0x4a0
   __DATA_CONST.__const: 0x708
-  __DATA_CONST.__cfstring: 0x10e0
+  __DATA_CONST.__cfstring: 0x1100
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x630
-  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__got: 0x248
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x30b0
   __DATA.__objc_selrefs: 0xa28

   - /usr/lib/libutil.dylib
   Functions: 434
   Symbols:   3556
-  CStrings:  1210
+  CStrings:  1212
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ +[FPSystemMem getBootCarveoutSize] : 268 -> 276
~ +[FPProcess _nameForBsdInfo:] : 424 -> 440
~ _main : 8472 -> 8600
CStrings:
+ "--forkCorpse is not compatible with --sample because a corpse's memory state is frozen at fork time and will not change between samples"

```
