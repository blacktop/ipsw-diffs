## init_featureflags

> `/usr/libexec/init_featureflags`

```diff

-103.0.0.0.0
-  __TEXT.__text: 0x1048
-  __TEXT.__auth_stubs: 0x260
+107.0.0.0.0
+  __TEXT.__text: 0xfec
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x68

   __TEXT.__objc_methtype: 0x8
   __TEXT.__objc_methname: 0x28d
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x60
   __DATA.__objc_const: 0x40
   __DATA.__objc_selrefs: 0xf8
   __DATA.__data: 0x20

   - /System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D8F3D88-03FA-358F-BCE5-00F969334472
+  UUID: C7668BAC-4684-310D-B506-E2F3D7870EFE
   Functions: 14
-  Symbols:   57
+  Symbols:   56
   CStrings:  71
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x21
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x25
- _objc_retain_x26
Functions:
~ sub_100000b04 : 156 -> 148
~ sub_100000ba0 -> sub_100000b98 : 3308 -> 3224

```
