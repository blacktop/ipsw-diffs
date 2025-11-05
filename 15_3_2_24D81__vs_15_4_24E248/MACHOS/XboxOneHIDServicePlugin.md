## XboxOneHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/Contents/MacOS/XboxOneHIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x7a68
-  __TEXT.__auth_stubs: 0x540
+12.4.12.0.0
+  __TEXT.__text: 0x77a4
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x1420
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x810
-  __TEXT.__objc_classname: 0x2ac
-  __TEXT.__objc_methname: 0x215a
-  __TEXT.__objc_methtype: 0xc4f
-  __TEXT.__cstring: 0x4c2
-  __TEXT.__const: 0x130
+  __TEXT.__objc_methlist: 0xc1c
+  __TEXT.__objc_classname: 0x2e6
+  __TEXT.__objc_methname: 0x2183
+  __TEXT.__objc_methtype: 0xcd3
+  __TEXT.__cstring: 0x51c
+  __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__oslogstring: 0x865
-  __TEXT.__unwind_info: 0x298
-  __DATA_CONST.__auth_got: 0x2b8
+  __TEXT.__oslogstring: 0x671
+  __TEXT.__unwind_info: 0x2a0
+  __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x2f0
-  __DATA_CONST.__cfstring: 0x760
+  __DATA_CONST.__const: 0x2d0
+  __DATA_CONST.__cfstring: 0x7e0
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1f50
-  __DATA.__objc_selrefs: 0x738
+  __DATA.__objc_const: 0x18d0
+  __DATA.__objc_selrefs: 0x850
   __DATA.__objc_ivar: 0x12c
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
-  UUID: A1734765-66C2-3328-BED1-38B7D0D7CB47
-  Functions: 243
-  Symbols:   124
-  CStrings:  721
+  UUID: 50779C71-2CE2-35B3-A274-FDFCFD7B8DC3
+  Functions: 259
+  Symbols:   123
+  CStrings:  723
 
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
