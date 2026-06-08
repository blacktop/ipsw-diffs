## powerexceptionsd

> `/usr/libexec/powerexceptionsd`

```diff

-4.100.50.0.0
-  __TEXT.__text: 0xdc
+145.0.0.0.0
+  __TEXT.__text: 0xd0
   __TEXT.__auth_stubs: 0x80
   __TEXT.__objc_stubs: 0x60
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x1a
   __TEXT.__objc_methname: 0x31
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x48
-  __DATA_CONST.__got: 0x18
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x48
+  __DATA_CONST.__got: 0x18
   __DATA.__objc_selrefs: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B40D753-1DC4-3408-B36B-777358A2D441
+  UUID: F9921EFF-6DD7-3762-8BA6-D17DEE41CF86
   Functions: 1
   Symbols:   15
   CStrings:  5
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_100000828 : 220 -> 208

```
