## DumpPanicRecoveryOS

> `/usr/libexec/DumpPanicRecoveryOS`

```diff

-  __TEXT.__text: 0x281a0
+  __TEXT.__text: 0x280a0
   __TEXT.__auth_stubs: 0xbb0
   __TEXT.__objc_stubs: 0x2000
   __TEXT.__objc_methlist: 0x70c

   __TEXT.__oslogstring: 0x4a7b
   __TEXT.__objc_classname: 0xda
   __TEXT.__objc_methtype: 0x52b
-  __TEXT.__gcc_except_tab: 0xaf4
+  __TEXT.__gcc_except_tab: 0xad4
   __TEXT.__unwind_info: 0x830
   __DATA_CONST.__const: 0x690
   __DATA_CONST.__cfstring: 0x2140

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__auth_got: 0x5f0
-  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0xca8
   __DATA.__objc_selrefs: 0x958

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 818
-  Symbols:   265
+  Symbols:   266
   CStrings:  1497
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ __os_log_default
Functions:
~ sub_10000383c : 6656 -> 6612
~ sub_100006264 -> sub_100006238 : 5352 -> 5308
~ sub_10000b610 -> sub_10000b5b8 : 2988 -> 2928
~ sub_1000175e4 -> sub_100017550 : 240 -> 232
~ sub_100018508 -> sub_10001846c : 40 -> 36
~ sub_100018e48 -> sub_100018da8 : 384 -> 296
~ sub_100019190 -> sub_100019098 : 16 -> 24
~ sub_10001b040 -> sub_10001af50 : 128 -> 112

```
