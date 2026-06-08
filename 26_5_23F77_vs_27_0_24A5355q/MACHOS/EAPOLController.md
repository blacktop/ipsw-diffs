## EAPOLController

> `/System/Library/SystemConfiguration/EAPOLController.bundle/EAPOLController`

```diff

-368.120.2.0.1
-  __TEXT.__text: 0x5214
-  __TEXT.__auth_stubs: 0x710
+382.0.0.0.0
+  __TEXT.__text: 0x535c
+  __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_stubs: 0xa0
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x1e9
-  __TEXT.__oslogstring: 0x654
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0x22f
+  __TEXT.__oslogstring: 0x666
   __TEXT.__objc_methname: 0x47
-  __TEXT.__unwind_info: 0x150
-  __DATA_CONST.__auth_got: 0x390
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3e0
+  __TEXT.__unwind_info: 0x160
+  __DATA_CONST.__const: 0x468
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__got: 0xa0
   __DATA.__objc_selrefs: 0x28
-  __DATA.__data: 0x10
+  __DATA.__data: 0x14
   __DATA.__bss: 0x39
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X
+  - /System/Library/PrivateFrameworks/IPConfiguration.framework/IPConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4AF22B11-3064-30B1-9E5D-0FDF6CFCB027
-  Functions: 83
-  Symbols:   187
-  CStrings:  92
+  UUID: AA2F1B9A-74E1-3291-A93F-90D3469DC866
+  Functions: 86
+  Symbols:   176
+  CStrings:  98
 
Symbols:
+ _IPConfigurationCopyConfiguredInterfaces
+ _SCDynamicStoreSetDispatchQueue
+ _SCPreferencesSetDispatchQueue
+ __dispatch_source_type_read
+ _audit_token_to_au32
+ _dispatch_activate
+ _dispatch_mach_cancel
+ _dispatch_mach_connect
+ _dispatch_mach_create
+ _dispatch_mach_mig_demux
+ _dispatch_mach_msg_get_msg
+ _dispatch_once
+ _dispatch_release
+ _dispatch_set_qos_class_fallback
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_cancel_handler
+ _dispatch_source_set_event_handler
+ _server_create_client_channel
- _CFMachPortCreateRunLoopSource
- _CFMachPortGetPort
- _CFMachPortInvalidate
- _CFRunLoopAddSource
- _CFRunLoopGetCurrent
- _CFRunLoopPerformBlock
- _CFRunLoopRun
- _CFRunLoopWakeUp
- _CFSocketCreateRunLoopSource
- _CFSocketCreateWithNative
- _CFSocketInvalidate
- _CFStringCreateArrayBySeparatingStrings
- _SCDynamicStoreCopyMultiple
- _SCDynamicStoreCreateRunLoopSource
- _SCPreferencesScheduleWithRunLoop
- __SC_CFMachPortCreateWithPort
- ___chkstk_darwin
- __dispatch_main_q
- _audit_token_to_pid
- _kCFRunLoopCommonModes
- _kCFRunLoopDefaultMode
- _kSCPropNetInterfaceDeviceName
- _kSCPropNetInterfaceType
- _kSCValNetInterfaceTypeEthernet
- _pthread_attr_destroy
- _pthread_attr_init
- _pthread_attr_setdetachstate
- _pthread_create
- _server_handle_request
- _server_register
CStrings:
+ "Created channel for port %d context %p"
+ "Destroying port %d context %p"
+ "EAPOLController server started"
+ "EAPOLController: %s closing %d"
+ "EAPOLController: %s opened %d"
+ "EAPOLController: failed to create source for %s"
+ "EAPOLControllerClientSession"
+ "EAPOLControllerQueue"
+ "configured ethernet: %@"
+ "configured wifi: %@"
+ "dispatch_mach_create(%s) failed"
+ "system mode configurations: %@"
+ "system mode iflist: %@"
+ "v28@?0Q8^{dispatch_mach_msg_s=}16i24"
- "ControllerThread"
- "EAPOLController: failed create CFRunLoopSource for %s"
- "EAPOLController: failed create CFSocket over %s"
- "EAPOLController: mach_msg(send): %s"
- "EAPOLController: pthread_attr_init failed %d"
- "EAPOLController: pthread_attr_setdetachstate failed %d"
- "EAPOLController: pthread_create failed %d"
- "EAPOLController: unknown message ID (%d)"

```
