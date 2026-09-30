## DualShock4HIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/DualShock4HIDServicePlugin.plugin/Contents/MacOS/DualShock4HIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0xa2f8
-  __TEXT.__auth_stubs: 0x550
+12.4.12.0.0
+  __TEXT.__text: 0xa2b0
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_stubs: 0x1660
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x888
-  __TEXT.__objc_classname: 0x2b4
-  __TEXT.__objc_methname: 0x2474
-  __TEXT.__objc_methtype: 0xe83
-  __TEXT.__cstring: 0x6fc
-  __TEXT.__const: 0x548
+  __TEXT.__objc_methlist: 0xc94
+  __TEXT.__objc_classname: 0x2ee
+  __TEXT.__objc_methname: 0x249d
+  __TEXT.__objc_methtype: 0xf07
+  __TEXT.__cstring: 0x756
+  __TEXT.__const: 0x530
   __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__oslogstring: 0xb9e
-  __TEXT.__unwind_info: 0x300
-  __DATA_CONST.__auth_got: 0x2c0
+  __TEXT.__oslogstring: 0x9aa
+  __TEXT.__unwind_info: 0x318
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x3d0
-  __DATA_CONST.__cfstring: 0xba0
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__cfstring: 0xc20
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x22a0
-  __DATA.__objc_selrefs: 0x7d0
+  __DATA.__objc_const: 0x1c20
+  __DATA.__objc_selrefs: 0x8c8
   __DATA.__objc_ivar: 0x180
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
-  UUID: 2AC5656E-34D4-31E7-A6C0-A62B18C2635A
-  Functions: 274
-  Symbols:   123
-  CStrings:  849
+  UUID: FC1E20B3-1193-32ED-B20D-DA167820D109
+  Functions: 305
+  Symbols:   122
+  CStrings:  851
 
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
