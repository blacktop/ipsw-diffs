## JoyConHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/JoyConHIDServicePlugin.plugin/JoyConHIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x15ca4
-  __TEXT.__auth_stubs: 0x6c0
+12.4.10.0.0
+  __TEXT.__text: 0x15d90
+  __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0x19a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x970
-  __TEXT.__cstring: 0xb87
-  __TEXT.__objc_classname: 0x2b2
-  __TEXT.__objc_methname: 0x25d5
-  __TEXT.__objc_methtype: 0x15c7
-  __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x1c3c
-  __TEXT.__oslogstring: 0x17b7
-  __TEXT.__unwind_info: 0x898
-  __DATA_CONST.__auth_got: 0x378
+  __TEXT.__objc_methlist: 0xd7c
+  __TEXT.__cstring: 0xbe1
+  __TEXT.__objc_classname: 0x2ec
+  __TEXT.__objc_methname: 0x25fe
+  __TEXT.__objc_methtype: 0x164b
+  __TEXT.__const: 0x1e4
+  __TEXT.__gcc_except_tab: 0x1d0c
+  __TEXT.__oslogstring: 0x15c3
+  __TEXT.__unwind_info: 0x940
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x720
-  __DATA_CONST.__cfstring: 0x1240
+  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__cfstring: 0x12c0
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2188
-  __DATA.__objc_selrefs: 0x870
+  __DATA.__objc_const: 0x1b08
+  __DATA.__objc_selrefs: 0x970
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x780
-  __DATA.__bss: 0xc9
+  __DATA.__data: 0x840
+  __DATA.__bss: 0xb9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation
   - /System/Library/PrivateFrameworks/HID.framework/HID
-  - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 461
-  Symbols:   152
-  CStrings:  909
+  Functions: 499
+  Symbols:   149
+  CStrings:  907
 
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
- _objc_retain_x24
- _objc_retain_x27
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
