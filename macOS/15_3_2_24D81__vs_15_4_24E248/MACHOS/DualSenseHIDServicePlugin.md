## DualSenseHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/DualSenseHIDServicePlugin.plugin/Contents/MacOS/DualSenseHIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0xc288
-  __TEXT.__auth_stubs: 0x570
+12.4.12.0.0
+  __TEXT.__text: 0xc30c
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x17c0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x948
-  __TEXT.__cstring: 0x78d
-  __TEXT.__objc_classname: 0x2b4
-  __TEXT.__objc_methname: 0x2659
-  __TEXT.__objc_methtype: 0x12b0
-  __TEXT.__const: 0x570
+  __TEXT.__objc_methlist: 0xd54
+  __TEXT.__cstring: 0x7e7
+  __TEXT.__objc_classname: 0x2ee
+  __TEXT.__objc_methname: 0x2682
+  __TEXT.__objc_methtype: 0x1334
+  __TEXT.__const: 0x550
   __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__oslogstring: 0xe95
-  __TEXT.__unwind_info: 0x348
-  __DATA_CONST.__auth_got: 0x2d0
+  __TEXT.__oslogstring: 0xca1
+  __TEXT.__unwind_info: 0x350
+  __DATA_CONST.__auth_got: 0x2a8
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x490
-  __DATA_CONST.__cfstring: 0xd00
+  __DATA_CONST.__const: 0x470
+  __DATA_CONST.__cfstring: 0xd80
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2450
-  __DATA.__objc_selrefs: 0x868
+  __DATA.__objc_const: 0x1dd0
+  __DATA.__objc_selrefs: 0x918
   __DATA.__objc_ivar: 0x194
   __DATA.__objc_data: 0x140
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
-  UUID: 16081E7A-76D5-3AC1-B738-939046ED5086
-  Functions: 298
-  Symbols:   125
-  CStrings:  917
+  UUID: BB11F841-75A9-348C-AA38-CE15D514A3F5
+  Functions: 332
+  Symbols:   124
+  CStrings:  919
 
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
