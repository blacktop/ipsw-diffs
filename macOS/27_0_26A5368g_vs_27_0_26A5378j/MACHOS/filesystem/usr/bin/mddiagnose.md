## mddiagnose

> `/usr/bin/mddiagnose`

```diff

-  __TEXT.__text: 0x10dec
+  __TEXT.__text: 0x10d98
   __TEXT.__auth_stubs: 0xf60
   __TEXT.__objc_stubs: 0x1400
   __TEXT.__objc_methlist: 0x32c

   __DATA_CONST.__objc_arrayobj: 0x5b8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__auth_got: 0x7c0
-  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x30
   __DATA.__objc_const: 0x360
   __DATA.__objc_selrefs: 0x548
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100001fb0 : 956 -> 900
~ sub_100003bfc -> sub_100003bc4 : 684 -> 704
~ sub_10000ca8c -> sub_10000ca68 : 52 -> 36
~ sub_10000cb00 -> sub_10000cacc : 132 -> 124
~ sub_10000cbcc -> sub_10000cb90 : 144 -> 120

```
