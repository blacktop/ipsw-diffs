## Diagnostic-8374

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8374.appex/Diagnostic-8374`

```diff

 1251.0.0.0.0
-  __TEXT.__text: 0xe84
-  __TEXT.__auth_stubs: 0x210
+  __TEXT.__text: 0xedc
+  __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_stubs: 0x380
   __TEXT.__objc_methlist: 0x70
   __TEXT.__const: 0x80

   __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methtype: 0x4f
   __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__cfstring: 0xc0

   - /System/Library/PrivateFrameworks/NPTKit.framework/NPTKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63F42E24-B368-3175-86DF-687B301842FD
+  UUID: 042B45F3-3379-33D7-9BAF-5AD644A1102B
   Functions: 13
-  Symbols:   53
+  Symbols:   51
   CStrings:  85
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ sub_100000d48 : 896 -> 932
~ sub_1000010c8 -> sub_1000010ec : 700 -> 704
~ sub_100001384 -> sub_1000013ac : 372 -> 384
~ sub_100001784 -> sub_1000017b8 : 408 -> 420
~ sub_1000019ac -> sub_1000019ec : 184 -> 188
~ sub_100001a64 -> sub_100001aa8 : 340 -> 360

```
