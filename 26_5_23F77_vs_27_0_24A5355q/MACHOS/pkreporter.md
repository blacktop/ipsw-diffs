## pkreporter

> `/usr/libexec/pkreporter`

```diff

-498.0.0.0.0
-  __TEXT.__text: 0x960
-  __TEXT.__auth_stubs: 0x1f0
+510.0.0.0.0
+  __TEXT.__text: 0x938
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_stubs: 0x220
   __TEXT.__cstring: 0x287
   __TEXT.__oslogstring: 0xf5
   __TEXT.__objc_methname: 0x126
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x48
   __DATA.__objc_selrefs: 0x88
   __DATA.__common: 0x8
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1FA37A6-0833-3A09-BF06-4F379826CB48
+  UUID: DF0D9C53-116E-328F-9294-A0282C045FFE
   Functions: 4
-  Symbols:   46
+  Symbols:   44
   CStrings:  71
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x8
- _objc_release_x23
- _objc_release_x26
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x28
Functions:
~ sub_100000a18 : 280 -> 272
~ sub_100000b30 -> sub_100000b28 : 2044 -> 2012

```
