## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-849.40.2.502.1
-  __TEXT.__text: 0x6df7c
-  __TEXT.__objc_methlist: 0x4b90
+849.40.4.0.1
+  __TEXT.__text: 0x6e030
+  __TEXT.__objc_methlist: 0x4ba0
   __TEXT.__const: 0x100
   __TEXT.__cstring: 0x10831
   __TEXT.__oslogstring: 0x885d

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2458
+  __DATA_CONST.__objc_selrefs: 0x2470
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x120
-  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__got: 0x518
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__cfstring: 0x6480
   __AUTH_CONST.__objc_const: 0xd440

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2277
-  Symbols:   4032
+  Functions: 2278
+  Symbols:   4037
   CStrings:  1929
 
Symbols:
+ +[IXAppInstallCoordinator(IXAppReplacement) _appIsHidden:]
+ GCC_except_table19
+ _OBJC_CLASS_$_APApplication
+ _objc_msgSend$_appIsHidden:
+ _objc_msgSend$applicationWithBundleIdentifier:
+ _objc_msgSend$bundleRecordForApplicationIdentifier:error:
+ _objc_msgSend$isLocked
- GCC_except_table12
- _objc_msgSend$bundleRecordWithApplicationIdentifier:error:
```
