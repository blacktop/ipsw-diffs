## libfaceCore.dylib

> `/System/Library/Frameworks/Vision.framework/libfaceCore.dylib`

```diff

-8.0.30.0.0
+8.0.32.2.0
   __TEXT.__text: 0x804930
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_methlist: 0x408

   __TEXT.__cstring: 0x10bb
   __TEXT.__unwind_info: 0x13c8
   __TEXT.__eh_frame: 0x1520
-  __TEXT.__objc_classname: 0x5b
+  __TEXT.__objc_classname: 0x5d
   __TEXT.__objc_methname: 0xb66
   __TEXT.__objc_methtype: 0x676
   __TEXT.__objc_stubs: 0xb80

   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x1e34e8
   __DATA.__common: 0x841
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x340
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
Symbols:
+ +[VNFaceCoreExceptionUtils throwInvalidArgumentException:]
+ +[VNFaceCoreExceptionUtils throwRuntimeErrorException:]
+ _OBJC_CLASS_$_VNFaceCoreExceptionUtils
+ _OBJC_METACLASS_$_VNFaceCoreExceptionUtils
+ __OBJC_$_CLASS_METHODS_VNFaceCoreExceptionUtils
+ __OBJC_CLASS_RO_$_VNFaceCoreExceptionUtils
+ __OBJC_METACLASS_RO_$_VNFaceCoreExceptionUtils
- +[FaceCoreExceptionUtils throwInvalidArgumentException:]
- +[FaceCoreExceptionUtils throwRuntimeErrorException:]
- _OBJC_CLASS_$_FaceCoreExceptionUtils
- _OBJC_METACLASS_$_FaceCoreExceptionUtils
- __OBJC_$_CLASS_METHODS_FaceCoreExceptionUtils
- __OBJC_CLASS_RO_$_FaceCoreExceptionUtils
- __OBJC_METACLASS_RO_$_FaceCoreExceptionUtils

```
