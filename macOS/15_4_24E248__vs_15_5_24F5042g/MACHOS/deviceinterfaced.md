## deviceinterfaced

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Support/deviceinterfaced`

```diff

-205.0.0.0.0
-  __TEXT.__text: 0xe1a4
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_stubs: 0x3e0
+208.120.5.0.0
+  __TEXT.__text: 0xe870
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_stubs: 0x400
   __TEXT.__objc_methlist: 0x320
-  __TEXT.__oslogstring: 0x2d5b
-  __TEXT.__cstring: 0xd39
-  __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0x1613
+  __TEXT.__oslogstring: 0x2dcf
+  __TEXT.__cstring: 0xe07
+  __TEXT.__objc_classname: 0x1b
+  __TEXT.__objc_methname: 0x1624
   __TEXT.__objc_methtype: 0x65c
-  __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__cfstring: 0xa0
+  __TEXT.__unwind_info: 0xf8
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x5b0
-  __DATA.__objc_selrefs: 0x210
+  __DATA.__objc_selrefs: 0x218
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x3
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x40
   - /Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface
   - /Library/Apple/System/Library/PrivateFrameworks/DeviceInterfaceClient.framework/Versions/A/DeviceInterfaceClient
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 109
-  Symbols:   58
-  CStrings:  408
+  Functions: 116
+  Symbols:   82
+  CStrings:  419
 
Symbols:
+ _CFRelease
+ _IOIteratorNext
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortSetDispatchQueue
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperty
+ _IOServiceAddMatchingNotification
+ _IOServiceMatching
+ _OBJC_CLASS_$_NSNumber
+ __NSConcreteStackBlock
+ __dispatch_source_type_signal
+ _dispatch_async
+ _dispatch_get_global_queue
+ _dispatch_resume
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _kCFAllocatorDefault
+ _kIOMainPortDefault
+ _notify_post
+ _objc_autoreleaseReturnValue
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _signal
CStrings:
+ "%s controller found %d version %d"
+ "%s: %d"
+ "AppleRSMChannelController"
+ "AppleRSMChannelControllerMajorVersion"
+ "IOServiceFirstPublish"
+ "OS version too old, not supported."
+ "Posting notification for daemon starting"
+ "com.apple.deviceinterfaced.started"
+ "deviceinterfaced is forced %s"
+ "deviceinterfaced received SIGTERM, exiting."
+ "deviceinterfaced_can_start"
+ "deviceinterfaced_requires_async_start"
+ "off"
+ "on"
+ "rsm_channel_controller_services_discovered"
+ "start_deviceinterfaced"
+ "unsignedIntValue"
- "%s OS is supported: %d"
- "%s deviceinterfaced enabled: %d"
- "%s dispatch_main();"
- "enable_deviceinterfaced"
- "is_current_os_supported"
- "main"

```
