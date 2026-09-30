## Diagnostic-6001

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6001.appex/Diagnostic-6001`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0x7f0
-  __TEXT.__auth_stubs: 0x170
+1066.100.26.0.0
+  __TEXT.__text: 0x87c
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_stubs: 0x240
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0x28

   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methname: 0x192
   __TEXT.__objc_methtype: 0x39
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xc0
+  __TEXT.__unwind_info: 0x88
+  __DATA_CONST.__auth_got: 0xc8
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x80

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 212D863D-9837-354C-B57B-2DA9FD1772C7
+  UUID: 9A29508C-271A-3877-9A95-C0459061AED5
   Functions: 9
-  Symbols:   40
+  Symbols:   41
   CStrings:  46
 
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x21
Functions:
~ sub_100000c90 : 668 -> 692
~ sub_100000f2c -> sub_100000f44 : 452 -> 468
~ sub_1000010f0 -> sub_100001118 : 168 -> 180
~ sub_100001198 -> sub_1000011cc : 468 -> 492
~ sub_10000137c -> sub_1000013c8 : 20 -> 80
~ sub_1000013e8 -> sub_100001470 : 152 -> 156

```
