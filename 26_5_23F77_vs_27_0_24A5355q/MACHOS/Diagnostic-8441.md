## Diagnostic-8441

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Diagnostic-8441`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x46c
+1351.0.0.0.0
+  __TEXT.__text: 0x41c
   __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x20

   __TEXT.__objc_methname: 0xf9
   __TEXT.__objc_methtype: 0x8
   __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__auth_got: 0xa0
+  __DATA_CONST.__got: 0x30
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x68
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 67F6B7A2-8657-3D68-9FF9-F0B39C98445D
+  UUID: 379CECE9-910D-37FF-BE01-623B3E350A3D
   Functions: 4
   Symbols:   36
   CStrings:  24
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
Functions:
~ sub_100000c40 : 340 -> 324
~ sub_100000d94 -> sub_100000d84 : 544 -> 528
~ sub_100000fb4 -> sub_100000f94 : 96 -> 92
~ sub_100001014 -> sub_100000ff0 : 152 -> 108

```
