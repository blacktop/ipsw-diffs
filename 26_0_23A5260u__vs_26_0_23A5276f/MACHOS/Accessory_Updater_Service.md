## Accessory Updater Service

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service`

```diff

-3476.0.6.0.1
-  __TEXT.__text: 0x774d0
+3476.0.29.0.0
+  __TEXT.__text: 0x7733c
   __TEXT.__auth_stubs: 0x1860
   __TEXT.__objc_stubs: 0x2d00
   __TEXT.__objc_methlist: 0x2e8c
   __TEXT.__const: 0x5c90
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x1701b
+  __TEXT.__cstring: 0x16f52
   __TEXT.__objc_methname: 0x3672
   __TEXT.__objc_classname: 0xb12
   __TEXT.__objc_methtype: 0xd01
   __TEXT.__oslogstring: 0x1562
-  __TEXT.__unwind_info: 0x1878
+  __TEXT.__unwind_info: 0x1868
   __DATA_CONST.__auth_got: 0xc40
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x2ac8
-  __DATA_CONST.__cfstring: 0x10f40
+  __DATA_CONST.__cfstring: 0x10f20
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x58

   __DATA.__objc_ivar: 0x37c
   __DATA.__objc_data: 0x14f0
   __DATA.__data: 0xaf8
-  __DATA.__bss: 0xa00
+  __DATA.__bss: 0x9f8
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: DD05C204-5D52-3EFB-B79D-3C5CD5548232
-  Functions: 2477
-  Symbols:   1836
-  CStrings:  6906
+  UUID: 9A032778-F539-31F9-A7BF-4B8B6F4FECAB
+  Functions: 2475
+  Symbols:   1835
+  CStrings:  6897
 
Symbols:
+ _AMSupportPlatformCopyURLToNewTempDirectory
+ _AMSupportPlatformGetURLForTempDirectoryRoot
- _AMAuthInstallPlatformGetURLForTempDirectoryRoot
- _CFURLCreateFromFileSystemRepresentation
- _mkdtemp
CStrings:
+ "libauthinstall_device-1104.0.3"
- "/tmp"
- "/tmp/%s"
- "AMAuthInstallPlatform.c"
- "AMAuthInstallPlatformCopyURLToNewTempDirectory"
- "_AMAuthInstallPlatformTempDirURLInitialize"
- "_tempDirURL != NULL"
- "failed to create tmp dir: %s"
- "libauthinstall_device-1104.0.0.0.1"
- "tmp dir template: %s"

```
