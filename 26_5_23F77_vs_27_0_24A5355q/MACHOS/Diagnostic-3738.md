## Diagnostic-3738

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3738.appex/Diagnostic-3738`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0xbb4
-  __TEXT.__auth_stubs: 0x190
+1351.0.0.0.0
+  __TEXT.__text: 0xab4
+  __TEXT.__auth_stubs: 0x1c0
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0xe8
-  __TEXT.__cstring: 0x9c
+  __TEXT.__cstring: 0x9e
   __TEXT.__objc_methname: 0x32e
-  __TEXT.__objc_classname: 0x46
+  __TEXT.__objc_classname: 0x44
   __TEXT.__objc_methtype: 0x6f
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x38
+  __TEXT.__unwind_info: 0xa8
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
-  UUID: 3F78DAD6-A038-3093-88DB-BDC9776F37FF
+  UUID: 29437895-4571-30C2-8682-B28928D7D56E
   Functions: 22
-  Symbols:   54
+  Symbols:   57
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
~ sub_100000d28 : 264 -> 268
~ sub_100000e30 -> sub_100000e34 : 452 -> 412
~ sub_100000ffc -> sub_100000fd8 : 64 -> 12
~ sub_100001044 -> sub_100000fec : 64 -> 12
~ sub_100001164 -> sub_1000010d8 : 856 -> 808
~ sub_1000014d4 -> sub_100001418 : 480 -> 448
~ _stringOrNull : 100 -> 92
~ _numberOrNull : 100 -> 92
~ sub_10000177c -> sub_100001690 : 148 -> 136
~ sub_100001850 -> sub_100001758 : 140 -> 132

```
