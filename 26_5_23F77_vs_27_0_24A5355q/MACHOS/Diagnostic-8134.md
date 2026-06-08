## Diagnostic-8134

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8134.appex/Diagnostic-8134`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x3dc
-  __TEXT.__auth_stubs: 0x100
+1351.0.0.0.0
+  __TEXT.__text: 0x30c
+  __TEXT.__auth_stubs: 0xe0
   __TEXT.__objc_stubs: 0x220
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__objc_classname: 0x5a
+  __TEXT.__objc_classname: 0x56
   __TEXT.__objc_methname: 0x395
   __TEXT.__objc_methtype: 0x115
-  __TEXT.__cstring: 0x46
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x88
-  __DATA_CONST.__got: 0x28
+  __TEXT.__cstring: 0x4a
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0x78
+  __DATA_CONST.__got: 0x28
   __DATA.__objc_const: 0x340
   __DATA.__objc_selrefs: 0x158
   __DATA.__objc_ivar: 0xc

   - /System/Library/PrivateFrameworks/EnhancedLogging.framework/EnhancedLogging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1B75263E-6707-3D61-AF70-9A2BF07D97B4
+  UUID: F6196004-CDA8-3BD4-8B24-10D2309EACDB
   Functions: 12
-  Symbols:   35
+  Symbols:   33
   CStrings:  86
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ sub_100000c20 : 64 -> 12
~ sub_100000c68 -> sub_100000c34 : 64 -> 12
~ sub_100000cf0 -> sub_100000c88 : 600 -> 552
~ sub_100000f48 -> sub_100000eb0 : 16 -> 20
~ sub_100000f58 -> sub_100000ec4 : 80 -> 20

```
