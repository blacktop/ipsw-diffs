## Accessory Updater Service

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service`

```diff

 3196.140.9.0.0
-  __TEXT.__text: 0x746c8
-  __TEXT.__auth_stubs: 0x1870
+  __TEXT.__text: 0x74688
+  __TEXT.__auth_stubs: 0x1880
   __TEXT.__objc_stubs: 0x2ce0
   __TEXT.__objc_methlist: 0x2e64
   __TEXT.__const: 0x5c80
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x163b1
+  __TEXT.__cstring: 0x1639b
   __TEXT.__objc_methname: 0x364e
   __TEXT.__objc_classname: 0xb12
   __TEXT.__objc_methtype: 0xd02
-  __TEXT.__oslogstring: 0x150c
-  __TEXT.__unwind_info: 0x1808
-  __DATA_CONST.__auth_got: 0xc48
+  __TEXT.__oslogstring: 0x1508
+  __TEXT.__unwind_info: 0x1800
+  __DATA_CONST.__auth_got: 0xc50
   __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x2378
-  __DATA_CONST.__cfstring: 0xf500
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__const: 0x2338
+  __DATA_CONST.__cfstring: 0xf4c0
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x58

   __DATA.__objc_selrefs: 0xf58
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
-  UUID: 6E93A7CD-D0FC-3ED0-B469-E3550588B942
-  Functions: 2444
-  Symbols:   1800
-  CStrings:  6470
+  UUID: 3E071F4C-0BF8-3337-B49B-0B60105A7C00
+  Functions: 2443
+  Symbols:   1802
+  CStrings:  6467
 
Symbols:
+ _taDFU_AppleKIS_enabled
+ _taDFU_deviceinterfaced_enabled
+ _tadfu_transport_client_usable
- _taDFU_useKISKext
Functions (modified):
~ _taDFU_startDeviceDiscoveryForVIDPID : 160 -> 100

Functions (added):
+ _taDFU_deviceinterfaced_enabled
+ sub_100047ecc
+ _taDFU_AppleKIS_enabled
+ sub_100050074

Functions (removed):
- sub_10004e90c
- sub_100058b34
- sub_10005c68c
- sub_10005fc78
- sub_1000721a8
CStrings:
+ "%s Overriding behavior with boot-arg, KIS kext is forced: %s"
+ "%s deviceinterfaced enabled: %s."
+ "KIS kext is %s"
+ "applekis.enabled"
+ "taDFU_AppleKIS_enabled"
- "%s Overriding behavior with boot-arg, using kext: %d"
- "EnableDeviceInterfaceDaemon"
- "com.apple.libDFU"
- "deviceinterfaced enabled: %d."
- "deviceinterfaced is forced %s"
- "taDFU_useKISKext"

```
