## Accessory Updater Service

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service`

```diff

-3196.100.145.0.3
-  __TEXT.__text: 0x7460c
-  __TEXT.__auth_stubs: 0x1860
+3196.100.158.0.1
+  __TEXT.__text: 0x746c8
+  __TEXT.__auth_stubs: 0x1870
   __TEXT.__objc_stubs: 0x2ce0
   __TEXT.__objc_methlist: 0x2e64
   __TEXT.__const: 0x5c80
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x163e0
+  __TEXT.__cstring: 0x163c5
   __TEXT.__objc_methname: 0x364e
   __TEXT.__objc_classname: 0xb12
   __TEXT.__objc_methtype: 0xd02
   __TEXT.__oslogstring: 0x150c
-  __TEXT.__unwind_info: 0x1800
-  __DATA_CONST.__auth_got: 0xc40
+  __TEXT.__unwind_info: 0x1808
+  __DATA_CONST.__auth_got: 0xc48
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x2320
-  __DATA_CONST.__cfstring: 0xf4e0
+  __DATA_CONST.__const: 0x2338
+  __DATA_CONST.__cfstring: 0xf500
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x58

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2441
-  Symbols:   1798
-  CStrings:  4518
+  Functions: 2443
+  Symbols:   1800
+  CStrings:  4519
 
Symbols:
+ _AMAuthInstallBundleSetEntryEnabled
+ __registryIDToDevice
+ _dispatch_queue_attr_make_with_autorelease_frequency
- __locationIDToDevice
CStrings:
+ "%s failed to convert file path to CFURL"
+ "Adding OptionalFirmware: %@"
+ "OptionalFirmware"
+ "a device with a duplicate registry id was connected!"
+ "com.apple.purplerestore.device_notification"
+ "libauthinstall_device-1049.100.22"
- "Tried to create a location ID for a disconnecting device but failed."
- "a device with a duplicate location id was connected!"
- "a device with no location id was connected!"
- "com.apple.purplerestore.device_notificaion"
- "libauthinstall_device-1049.100.21"

```
