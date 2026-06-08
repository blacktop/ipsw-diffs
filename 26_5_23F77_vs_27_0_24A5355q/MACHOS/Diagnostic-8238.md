## Diagnostic-8238

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8238.appex/Diagnostic-8238`

```diff

-1418.1.0.0.0
-  __TEXT.__text: 0xe30
+1563.0.0.0.0
+  __TEXT.__text: 0xcfc
   __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_stubs: 0x260
   __TEXT.__objc_methlist: 0x274
-  __TEXT.__cstring: 0x6c
-  __TEXT.__objc_classname: 0x88
+  __TEXT.__cstring: 0x6e
+  __TEXT.__objc_classname: 0x86
   __TEXT.__objc_methtype: 0x24f
-  __TEXT.__gcc_except_tab: 0x5c
+  __TEXT.__gcc_except_tab: 0x54
   __TEXT.__const: 0x78
   __TEXT.__objc_methname: 0x416
   __TEXT.__oslogstring: 0x1fa
   __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x8
   __DATA.__objc_const: 0x4d8
   __DATA.__objc_selrefs: 0x190
   __DATA.__objc_ivar: 0x14

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F59A2A8E-C7B4-3AA5-A474-86900555C703
+  UUID: 6B8C8B6A-9277-35FD-BE37-A961DDB7FD0B
   Functions: 24
-  Symbols:   52
+  Symbols:   51
   CStrings:  119
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x3
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
Functions:
~ sub_1000010d8 : 240 -> 196
~ sub_1000011c8 -> sub_10000119c : 188 -> 144
~ sub_100001284 -> sub_10000122c : 508 -> 452
~ sub_100001540 -> sub_1000014b0 : 796 -> 728
~ sub_10000185c -> sub_100001788 : 16 -> 20
~ sub_10000186c -> sub_10000179c : 80 -> 20
~ sub_100001910 -> sub_100001804 : 240 -> 196
~ sub_100001a10 -> sub_1000018d8 : 252 -> 260
~ sub_100001bb8 -> sub_100001a88 : 140 -> 136

```
