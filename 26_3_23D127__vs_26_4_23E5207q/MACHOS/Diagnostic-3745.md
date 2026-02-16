## Diagnostic-3745

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3745.appex/Diagnostic-3745`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0xb40
-  __TEXT.__auth_stubs: 0x1c0
+1066.100.26.0.0
+  __TEXT.__text: 0xc40
+  __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0xe8
   __TEXT.__cstring: 0xaa

   __TEXT.__objc_methtype: 0x6f
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xf0
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0xd8
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x180

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D33C7B7F-9EE4-3CB4-B133-DCE61573B4EF
+  UUID: 5DD0DD3D-4117-3736-9120-7C29DC5C0897
   Functions: 23
-  Symbols:   58
+  Symbols:   55
   CStrings:  90
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x24
Functions:
~ sub_100000d28 : 136 -> 148
~ sub_100000df0 -> sub_100000dfc : 132 -> 140
~ sub_100000e74 -> sub_100000e88 : 268 -> 264
~ sub_100000f80 -> sub_100000f90 : 412 -> 452
~ sub_100001124 -> sub_10000115c : 12 -> 64
~ sub_100001138 -> sub_1000011a4 : 12 -> 64
~ _stringOrNull : 92 -> 100
~ _numberOrNull : 92 -> 100
~ _dictionaryOrNull : 92 -> 100
~ sub_100001338 -> sub_1000013f0 : 816 -> 856
~ sub_100001680 -> sub_100001760 : 488 -> 520

```
