## init_featureflags

> `/usr/libexec/init_featureflags`

```diff

-85.0.0.0.0
+86.0.0.0.0
   __TEXT.__text: 0x12cc
   __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_stubs: 0x3e0

   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x40
   __DATA.__objc_selrefs: 0xf8
-  __DATA.__objc_classrefs: 0x38
   __DATA.__data: 0x18
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 886FEF82-0110-3C2F-BB58-83C909560734
+  UUID: 6733835E-0E02-3D50-9867-1991E256F18E
   Functions: 8
   Symbols:   57
   CStrings:  72

```
