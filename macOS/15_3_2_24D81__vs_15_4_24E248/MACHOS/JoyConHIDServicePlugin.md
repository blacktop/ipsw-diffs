## JoyConHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/JoyConHIDServicePlugin.plugin/Contents/MacOS/JoyConHIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x1801c
-  __TEXT.__auth_stubs: 0x5d0
+12.4.12.0.0
+  __TEXT.__text: 0x18044
+  __TEXT.__auth_stubs: 0x580
   __TEXT.__objc_stubs: 0x1a40
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x9a0
-  __TEXT.__cstring: 0xb9b
-  __TEXT.__objc_classname: 0x2b3
-  __TEXT.__objc_methname: 0x26f9
-  __TEXT.__objc_methtype: 0x1622
-  __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x1c54
-  __TEXT.__oslogstring: 0x18fd
-  __TEXT.__unwind_info: 0x8e8
-  __DATA_CONST.__auth_got: 0x300
+  __TEXT.__objc_methlist: 0xdac
+  __TEXT.__cstring: 0xbf5
+  __TEXT.__objc_classname: 0x2ed
+  __TEXT.__objc_methname: 0x2722
+  __TEXT.__objc_methtype: 0x16a6
+  __TEXT.__const: 0x1e4
+  __TEXT.__gcc_except_tab: 0x1d20
+  __TEXT.__oslogstring: 0x1709
+  __TEXT.__unwind_info: 0x990
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x7e8
-  __DATA_CONST.__cfstring: 0x1260
+  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__cfstring: 0x12e0
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2248
-  __DATA.__objc_selrefs: 0x8a8
+  __DATA.__objc_const: 0x1bc8
+  __DATA.__objc_selrefs: 0x9a8
   __DATA.__objc_ivar: 0x180
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x780
-  __DATA.__bss: 0xc9
+  __DATA.__data: 0x840
+  __DATA.__bss: 0xb9
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
-  UUID: 795EEA14-DF73-3165-B981-D3CAD910456F
-  Functions: 494
-  Symbols:   139
-  CStrings:  1079
+  UUID: 4761E2A2-6E30-390A-848C-7FBCBE10B014
+  Functions: 532
+  Symbols:   138
+  CStrings:  1081
 
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
