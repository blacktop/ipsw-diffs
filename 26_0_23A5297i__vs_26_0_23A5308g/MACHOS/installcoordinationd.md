## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-772.0.0.0.0
-  __TEXT.__text: 0xa3ba8
+775.0.0.0.0
+  __TEXT.__text: 0xa6b64
   __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_stubs: 0xaf80
-  __TEXT.__objc_methlist: 0x5d4c
+  __TEXT.__objc_stubs: 0xafe0
+  __TEXT.__objc_methlist: 0x5d74
   __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x18c23
-  __TEXT.__objc_methname: 0x10e0b
+  __TEXT.__cstring: 0x18c65
+  __TEXT.__objc_methname: 0x10e99
   __TEXT.__objc_classname: 0xa21
   __TEXT.__objc_methtype: 0x23a7
-  __TEXT.__oslogstring: 0xdf07
-  __TEXT.__gcc_except_tab: 0x2b2c
+  __TEXT.__oslogstring: 0xdf1a
+  __TEXT.__gcc_except_tab: 0x32fc
   __TEXT.__ustring: 0x1a68
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x2528
+  __TEXT.__unwind_info: 0x26a8
   __DATA_CONST.__auth_got: 0x8a8
   __DATA_CONST.__got: 0x458
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2bf8
+  __DATA_CONST.__const: 0x2d38
   __DATA_CONST.__cfstring: 0x9d60
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0xc4d0
-  __DATA.__objc_selrefs: 0x33c0
+  __DATA.__objc_selrefs: 0x33d8
   __DATA.__objc_ivar: 0x4b0
   __DATA.__objc_data: 0x1720
   __DATA.__data: 0x6b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C517EDC6-84E1-399E-B8D4-252EFC0A7153
-  Functions: 3310
+  UUID: 4F026EB0-049D-38F5-8421-CA8F1513215E
+  Functions: 3357
   Symbols:   429
-  CStrings:  6826
+  CStrings:  6830
 
CStrings:
+ "%s: %@: set importance to %@"
+ "%s: Ignoring attempt to set a placeholder promise with bundle ID %@ on coordinator with different bundle ID %@ : %@"
+ "%s: Unknown reason: %d"
+ "-[IXSCoordinatedAppInstall _internal_setAppAssetPromise:performExternalActions:]"
+ "-[IXSCoordinatedAppInstall _internal_setInstallOptionsPromise:performExternalActions:]"
+ "-[IXSCoordinatedAppInstall awakeFromSerializationWithError:]_block_invoke_3"
+ "03:38:46"
+ "Ignoring attempt to set a placeholder promise with bundle ID %@ on coordinator with different bundle ID %@"
+ "Jul 22 2025"
+ "_internal_setAppAssetPromise:performExternalActions:"
+ "_internal_setInstallOptionsPromise:performExternalActions:"
+ "_runWithExternalPropertyLock:"
- "%s: %@: setting importance to %@"
- "%s: Ignoring attempt to set a placeholder promise with bundle ID %@ on coordinator with different bundle id %@ : %@"
- "-[IXSCoordinatedAppInstall awakeFromSerializationWithError:]_block_invoke_2"
- "-[IXSCoordinatedAppInstall setAppAssetPromise:]"
- "-[IXSCoordinatedAppInstall setInstallOptionsPromise:]"
- "21:47:18"
- "Ignoring attempt to set a placeholder promise with bundle ID %@ on coordinator with different bundle id %@"
- "Jul 11 2025"

```
