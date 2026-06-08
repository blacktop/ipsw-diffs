## Diagnostic-3745

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3745.appex/Diagnostic-3745`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0xc40
-  __TEXT.__auth_stubs: 0x190
+1351.0.0.0.0
+  __TEXT.__text: 0xb40
+  __TEXT.__auth_stubs: 0x1c0
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0xe8
-  __TEXT.__cstring: 0xaa
-  __TEXT.__objc_classname: 0x51
+  __TEXT.__cstring: 0xac
+  __TEXT.__objc_classname: 0x4f
   __TEXT.__objc_methname: 0x32e
   __TEXT.__objc_methtype: 0x6f
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x38
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x38
   __DATA.__objc_const: 0x2c8
   __DATA.__objc_selrefs: 0x130
   __DATA.__objc_ivar: 0x10

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6514559B-B154-36D4-81F9-F6914DA16A10
+  UUID: 9796F3F1-75C7-3D7C-A95B-84081D5D6938
   Functions: 23
-  Symbols:   55
+  Symbols:   58
   CStrings:  90
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
Functions:
~ sub_100000d28 : 148 -> 136
~ sub_100000dfc -> sub_100000df0 : 140 -> 132
~ sub_100000e88 -> sub_100000e74 : 264 -> 268
~ sub_100000f90 -> sub_100000f80 : 452 -> 412
~ sub_10000115c -> sub_100001124 : 64 -> 12
~ sub_1000011a4 -> sub_100001138 : 64 -> 12
~ _stringOrNull : 100 -> 92
~ _numberOrNull : 100 -> 92
~ _dictionaryOrNull : 100 -> 92
~ sub_1000013f0 -> sub_100001338 : 856 -> 816
~ sub_100001760 -> sub_100001680 : 520 -> 488

```
