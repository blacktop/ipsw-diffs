## symptomsd-diag

> `/usr/libexec/symptomsd-diag`

```diff

-411.120.4.0.0
-  __TEXT.__text: 0x470
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_stubs: 0xa0
+460.0.0.0.0
+  __TEXT.__text: 0x4cc
+  __TEXT.__auth_stubs: 0x1b0
+  __TEXT.__objc_stubs: 0xc0
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x26
-  __TEXT.__oslogstring: 0x99
-  __TEXT.__objc_methname: 0x42
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xf0
-  __DATA_CONST.__got: 0x40
+  __TEXT.__oslogstring: 0xcd
+  __TEXT.__objc_methname: 0x59
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x28
+  __DATA_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x38
+  __DATA.__objc_selrefs: 0x30
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F409F02C-4D3F-3558-AB32-A5D010491A2D
+  UUID: B972EBDE-4DB1-39D7-A5CE-5C61E3295274
   Functions: 9
-  Symbols:   41
-  CStrings:  12
+  Symbols:   38
+  CStrings:  14
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ sub_100000998 : 84 -> 68
~ sub_100000a30 -> sub_100000a20 : 336 -> 408
~ sub_100000b80 -> sub_100000bb8 : 316 -> 336
~ sub_100000cc0 -> sub_100000d0c : 204 -> 224
~ sub_100000da4 -> sub_100000e04 : 100 -> 96
CStrings:
+ "Asked to run in unsupported environment. Bailing..."
+ "isSupportedEnvironment"

```
