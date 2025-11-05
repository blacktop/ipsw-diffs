## LunaHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/LunaHIDServicePlugin.plugin/Contents/MacOS/LunaHIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x6aac
-  __TEXT.__auth_stubs: 0x540
+12.4.12.0.0
+  __TEXT.__text: 0x6790
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__objc_stubs: 0x12c0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x798
-  __TEXT.__cstring: 0x468
-  __TEXT.__objc_classname: 0x2a9
-  __TEXT.__objc_methname: 0x2008
-  __TEXT.__objc_methtype: 0xbfb
-  __TEXT.__const: 0xd0
+  __TEXT.__objc_methlist: 0xba4
+  __TEXT.__cstring: 0x4c2
+  __TEXT.__objc_classname: 0x2e3
+  __TEXT.__objc_methname: 0x2031
+  __TEXT.__objc_methtype: 0xc7f
+  __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__oslogstring: 0x697
-  __TEXT.__unwind_info: 0x278
-  __DATA_CONST.__auth_got: 0x2b8
+  __TEXT.__oslogstring: 0x4a3
+  __TEXT.__unwind_info: 0x280
+  __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x2f0
-  __DATA_CONST.__cfstring: 0x660
+  __DATA_CONST.__const: 0x2d0
+  __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1e48
-  __DATA.__objc_selrefs: 0x700
+  __DATA.__objc_const: 0x17c8
+  __DATA.__objc_selrefs: 0x818
   __DATA.__objc_ivar: 0x10c
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
-  UUID: EDA86B8E-71E1-3855-841D-856D56BA34FA
-  Functions: 231
-  Symbols:   122
-  CStrings:  675
+  UUID: CB3638BA-870E-3C7F-A12B-0E8FB2F44A2D
+  Functions: 248
+  Symbols:   121
+  CStrings:  677
 
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
