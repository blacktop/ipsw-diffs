## EAPOLController

> `/System/Library/SystemConfiguration/EAPOLController.bundle/EAPOLController`

```diff

-354.40.2.0.0
-  __TEXT.__text: 0x5320
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1c5
-  __TEXT.__oslogstring: 0x631
-  __TEXT.__unwind_info: 0x14c
-  __DATA_CONST.__auth_got: 0x3a8
-  __DATA_CONST.__got: 0xc8
+354.100.3.0.0
+  __TEXT.__text: 0x510c
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0xa0
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x1e9
+  __TEXT.__oslogstring: 0x610
+  __TEXT.__objc_methname: 0x49
+  __TEXT.__unwind_info: 0x150
+  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3e8
+  __DATA_CONST.__const: 0x3c0
   __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x8
+  __DATA.__objc_selrefs: 0x28
   __DATA.__data: 0x10
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x39
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 4D5496A3-E192-318E-8DCF-6E8728C284D5
-  Functions: 85
-  Symbols:   189
-  CStrings:  84
+  - /usr/lib/libobjc.A.dylib
+  UUID: DBEB90CF-18C3-34ED-941B-FDA02547FD71
+  Functions: 82
+  Symbols:   187
+  CStrings:  91
 
Symbols:
+ _EAPWiFiMonitorPowerStatus
+ _OBJC_CLASS_$_CWFInterface
+ _objc_alloc_init
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend
- _WiFiDeviceClientGetPower
- _WiFiDeviceClientRegisterPowerCallback
- _WiFiManagerClientCopyDevices
- _WiFiManagerClientCreate
- _WiFiManagerClientRegisterDeviceAttachmentCallback
- _WiFiManagerClientScheduleWithRunLoop
- _dispatch_once
- _kCFAllocatorDefault
CStrings:
+ "EAP WiFi Interface Queue"
+ "OFF"
+ "ON"
+ "activate"
+ "power state changed to %s"
+ "powerOn"
+ "setEventHandler:"
+ "startMonitoringEventType:error:"
+ "type"
+ "v16@?0@\"CWFEvent\"8"
- "EAP WiFi Power"
- "Failed to create WiFiManager client"
- "Wi-Fi device attached."

```
