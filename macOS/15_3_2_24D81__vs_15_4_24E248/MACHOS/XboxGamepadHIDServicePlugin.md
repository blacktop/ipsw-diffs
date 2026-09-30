## XboxGamepadHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/XboxGamepadHIDServicePlugin.plugin/Contents/MacOS/XboxGamepadHIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x8bd0
-  __TEXT.__auth_stubs: 0x580
+12.4.12.0.0
+  __TEXT.__text: 0x88dc
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_stubs: 0x14a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x8f8
-  __TEXT.__objc_classname: 0x359
-  __TEXT.__objc_methname: 0x21ee
-  __TEXT.__objc_methtype: 0xc19
-  __TEXT.__cstring: 0x4b8
-  __TEXT.__const: 0x10c
+  __TEXT.__objc_methlist: 0xd04
+  __TEXT.__objc_classname: 0x393
+  __TEXT.__objc_methname: 0x2217
+  __TEXT.__objc_methtype: 0xc9d
+  __TEXT.__cstring: 0x512
+  __TEXT.__const: 0xfc
   __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__oslogstring: 0x7ce
+  __TEXT.__oslogstring: 0x5da
   __TEXT.__unwind_info: 0x318
-  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__cfstring: 0x700
+  __DATA_CONST.__const: 0x360
+  __DATA_CONST.__cfstring: 0x780
   __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2c18
-  __DATA.__objc_selrefs: 0x768
+  __DATA.__objc_const: 0x2598
+  __DATA.__objc_selrefs: 0x880
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x780
-  __DATA.__bss: 0xd0
+  __DATA.__data: 0x840
+  __DATA.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/Frameworks/IOBluetooth.framework/Versions/A/IOBluetooth
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/Versions/A/GameControllerFoundation
   - /System/Library/PrivateFrameworks/HID.framework/Versions/A/HID
-  - /System/Library/PrivateFrameworks/MobileBluetooth.framework/Versions/A/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB23F5F8-4246-31E8-8769-870E513A9D5C
-  Functions: 275
-  Symbols:   128
-  CStrings:  716
+  UUID: 14915393-A1A2-33BE-BD14-A42AE9D46460
+  Functions: 292
+  Symbols:   127
+  CStrings:  718
 
Symbols:
+ _OBJC_CLASS_$__GCHapticEvent
+ _OBJC_METACLASS_$__GCHapticEvent
+ _hexStringFromByteArray
+ _isPartnerSupportEnabled
- _BTDeviceAddressFromString
- _BTDeviceDisconnect
- _BTDeviceFromAddress
- _BTSessionAttachWithQueue
- _BTSessionDetachWithQueue
CStrings:
+ "@\"<GCIdleServiceClientInterface>\""
+ "GCIdleServiceClientInterface"
+ "GCIdleServiceServerInterface"
+ "IOHIDDeviceForceInterfaceRematch"
+ "IOHIDDeviceSuspend"
+ "MaxReportBufferCount"
+ "ReportBufferEntrySize"
+ "_idleClient"
+ "connectToIdleServiceWithClient:reply:"
+ "requestIdleDiconnect:"
+ "v24@0:8@\"NSString\"16"
+ "v32@0:8@\"<GCIdleServiceClientInterface>\"16@?<v@?@\"<GCIdleServiceServerInterface>\"@\"NSError\">24"
- "BTSessionEventCallback: attached session = %p"
- "BTSessionEventCallback: detached session = %p"
- "BTSessionEventCallback: failed session = %p"
- "BTSessionEventCallback: terminated session = %p"
- "GCHIDLog::disconnect: SUCCESS"
- "GCHIDLog::disconnect: error code = %d"
- "GCHIDLog::disconnect: unable to get BTDevice; error code = %d"
- "GCHIDLog::disconnect: unable to get BTDevice; no valid BTSession"
- "GCHIDLog::disconnect: unable to get device address from %s; errCode = %d"
- "^{BTSessionImpl=}"
- "_session"
- "cStringUsingEncoding:"
- "registering for BTSessionCallbacks sessionEvent"

```
