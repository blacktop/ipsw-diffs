## DualShock4HIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/DualShock4HIDServicePlugin.plugin/DualShock4HIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x94c4
-  __TEXT.__auth_stubs: 0x5e0
+12.4.10.0.0
+  __TEXT.__text: 0x9478
+  __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_stubs: 0x15c0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x858
-  __TEXT.__objc_classname: 0x2b3
-  __TEXT.__objc_methname: 0x2350
-  __TEXT.__objc_methtype: 0xe28
-  __TEXT.__cstring: 0x6d2
-  __TEXT.__const: 0x538
+  __TEXT.__objc_methlist: 0xc64
+  __TEXT.__objc_classname: 0x2ed
+  __TEXT.__objc_methname: 0x2379
+  __TEXT.__objc_methtype: 0xeac
+  __TEXT.__cstring: 0x72c
+  __TEXT.__const: 0x520
   __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__oslogstring: 0xa58
-  __TEXT.__unwind_info: 0x2d8
-  __DATA_CONST.__auth_got: 0x308
+  __TEXT.__oslogstring: 0x864
+  __TEXT.__unwind_info: 0x2f0
+  __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x388
-  __DATA_CONST.__cfstring: 0xb60
+  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__cfstring: 0xbe0
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x21e0
-  __DATA.__objc_selrefs: 0x798
+  __DATA.__objc_const: 0x1b60
+  __DATA.__objc_selrefs: 0x890
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x780
-  __DATA.__bss: 0xd0
+  __DATA.__data: 0x840
+  __DATA.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation
   - /System/Library/PrivateFrameworks/HID.framework/HID
-  - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 258
-  Symbols:   130
-  CStrings:  731
+  Functions: 289
+  Symbols:   129
+  CStrings:  729
 
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
+ "\x02\x11\xf0\xf0\xf0\xf0\x15\x83!\x11"
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
- "\x02\x11\xf0\xf0\xf0\xf0$\x83!\x11"
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
