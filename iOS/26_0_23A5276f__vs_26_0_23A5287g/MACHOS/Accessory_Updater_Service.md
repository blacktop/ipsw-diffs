## Accessory Updater Service

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service`

```diff

 3476.0.29.0.0
   __TEXT.__text: 0x7733c
-  __TEXT.__auth_stubs: 0x1860
+  __TEXT.__auth_stubs: 0x1870
   __TEXT.__objc_stubs: 0x2d00
   __TEXT.__objc_methlist: 0x2e8c
   __TEXT.__const: 0x5c90
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x16f52
+  __TEXT.__cstring: 0x16f3c
   __TEXT.__objc_methname: 0x3672
   __TEXT.__objc_classname: 0xb12
   __TEXT.__objc_methtype: 0xd01
-  __TEXT.__oslogstring: 0x1562
-  __TEXT.__unwind_info: 0x1868
-  __DATA_CONST.__auth_got: 0xc40
+  __TEXT.__oslogstring: 0x155e
+  __TEXT.__unwind_info: 0x1860
+  __DATA_CONST.__auth_got: 0xc48
   __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x2ac8
-  __DATA_CONST.__cfstring: 0x10f20
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__const: 0x2a88
+  __DATA_CONST.__cfstring: 0x10ee0
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x58

   __DATA.__objc_selrefs: 0xf68
   __DATA.__objc_ivar: 0x37c
   __DATA.__objc_data: 0x14f0
-  __DATA.__data: 0xaf8
-  __DATA.__bss: 0x9f8
+  __DATA.__data: 0xaf0
+  __DATA.__bss: 0x9f0
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9A032778-F539-31F9-A7BF-4B8B6F4FECAB
-  Functions: 2475
-  Symbols:   1835
-  CStrings:  6897
+  UUID: 31DE2007-EB71-3D14-B2B3-DF1E39F517BE
+  Functions: 2474
+  Symbols:   1837
+  CStrings:  6894
 
Symbols:
+ _taDFU_AppleKIS_enabled
+ _taDFU_deviceinterfaced_enabled
+ _tadfu_transport_client_usable
- _taDFU_useKISKext
CStrings:
+ "%s Overriding behavior with boot-arg, KIS kext is forced: %s"
+ "%s deviceinterfaced enabled: %s."
+ "KIS kext is %s"
+ "applekis.enabled"
+ "libauthinstall_device-1104.0.5"
+ "taDFU_AppleKIS_enabled"
- "%s Overriding behavior with boot-arg, using kext: %d"
- "EnableDeviceInterfaceDaemon"
- "com.apple.libDFU"
- "deviceinterfaced enabled: %d."
- "deviceinterfaced is forced %s"
- "libauthinstall_device-1104.0.3"
- "taDFU_useKISKext"

```
