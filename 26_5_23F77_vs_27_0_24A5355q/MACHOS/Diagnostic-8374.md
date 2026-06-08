## Diagnostic-8374

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8374.appex/Diagnostic-8374`

```diff

 1251.0.0.0.0
-  __TEXT.__text: 0xedc
-  __TEXT.__auth_stubs: 0x1f0
+  __TEXT.__text: 0xdd8
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x380
   __TEXT.__objc_methlist: 0x70
   __TEXT.__const: 0x80
   __TEXT.__objc_methname: 0x25d
   __TEXT.__oslogstring: 0x46d
-  __TEXT.__cstring: 0x168
-  __TEXT.__objc_classname: 0x3b
+  __TEXT.__cstring: 0x16c
+  __TEXT.__objc_classname: 0x37
   __TEXT.__objc_methtype: 0x4f
   __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0xc8
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x18
   __DATA.__objc_const: 0x190
   __DATA.__objc_selrefs: 0x110
   __DATA.__objc_ivar: 0xc

   - /System/Library/PrivateFrameworks/NPTKit.framework/NPTKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24255103-4F35-36A8-A867-0ECDC2B920DF
+  UUID: 72211B45-0C62-3326-80C0-4C1CA9B8846A
   Functions: 13
   Symbols:   51
   CStrings:  85
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
Functions:
~ sub_100000d48 : 932 -> 852
~ sub_1000010ec -> sub_10000109c : 704 -> 700
~ sub_1000013ac -> sub_100001358 : 384 -> 328
~ sub_1000017b8 -> sub_10000172c : 420 -> 364
~ sub_100001aa8 -> sub_1000019e4 : 360 -> 296

```
