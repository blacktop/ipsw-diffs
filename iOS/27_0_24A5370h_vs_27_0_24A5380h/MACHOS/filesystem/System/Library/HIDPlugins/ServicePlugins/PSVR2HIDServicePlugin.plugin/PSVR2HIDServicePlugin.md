## PSVR2HIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/PSVR2HIDServicePlugin.plugin/PSVR2HIDServicePlugin`

```diff

-  __TEXT.__text: 0x4884
-  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__text: 0x4954
+  __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_stubs: 0x580
   __TEXT.__objc_methlist: 0x460
-  __TEXT.__const: 0x50
+  __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x88
+  __TEXT.__oslogstring: 0x963
   __TEXT.__cstring: 0x167
   __TEXT.__objc_methname: 0xa03
-  __TEXT.__oslogstring: 0x936
   __TEXT.__objc_classname: 0xaa
   __TEXT.__objc_methtype: 0x8ff
   __TEXT.__unwind_info: 0x160

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x388
+  __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0x88
   __DATA.__objc_const: 0x698
   __DATA.__objc_selrefs: 0x2f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 83
-  Symbols:   140
-  CStrings:  296
+  Symbols:   141
+  CStrings:  297
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _IOObjectCopyClass
Functions:
~ sub_e20 : 184 -> 392
~ sub_ed8 -> sub_fa8 : 1000 -> 68
~ sub_12c0 -> sub_fec : 68 -> 1000
~ sub_4f50 -> sub_5020 : 60 -> 20
~ sub_4fc8 -> sub_5070 : 52 -> 60
~ sub_5030 -> sub_50e0 : 140 -> 52
~ sub_5148 -> sub_51a0 : 116 -> 140
~ sub_51bc -> sub_522c : 52 -> 116
~ sub_528c -> sub_533c : 20 -> 52
CStrings:
+ "%{public}@ probe <%{public}@ %#010llx> (%zi)"

```
