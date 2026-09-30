## PSVR2HIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/PSVR2HIDServicePlugin.plugin/Contents/MacOS/PSVR2HIDServicePlugin`

```diff

-  __TEXT.__text: 0x4a94
-  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__text: 0x4b70
+  __TEXT.__auth_stubs: 0x5c0
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
   __TEXT.__unwind_info: 0x168

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x88
   __DATA.__objc_const: 0x698
   __DATA.__objc_selrefs: 0x2f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 89
-  Symbols:   120
-  CStrings:  296
+  Symbols:   121
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
~ sub_e60 : 192 -> 412
~ sub_f20 -> sub_ffc : 1036 -> 68
~ sub_132c -> sub_1040 : 68 -> 1036
~ sub_5180 -> sub_525c : 60 -> 20
~ sub_51f8 -> sub_52ac : 52 -> 60
~ sub_5260 -> sub_531c : 144 -> 52
~ sub_52f0 -> sub_5350 : 148 -> 144
~ sub_5384 -> sub_53e0 : 120 -> 148
~ sub_53fc -> sub_5474 : 52 -> 120
~ sub_54cc -> sub_5588 : 20 -> 52
CStrings:
+ "%{public}@ probe <%{public}@ %#010llx> (%zi)"

```
