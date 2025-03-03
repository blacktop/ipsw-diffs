## XboxOneHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/XboxOneHIDServicePlugin.plugin/XboxOneHIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x6e48
-  __TEXT.__auth_stubs: 0x5a0
+12.4.10.0.0
+  __TEXT.__text: 0x6bdc
+  __TEXT.__auth_stubs: 0x550
   __TEXT.__objc_stubs: 0x13a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x7e0
-  __TEXT.__objc_classname: 0x2ab
-  __TEXT.__objc_methname: 0x2036
-  __TEXT.__objc_methtype: 0xbf4
-  __TEXT.__cstring: 0x4ae
-  __TEXT.__const: 0x124
+  __TEXT.__objc_methlist: 0xbec
+  __TEXT.__objc_classname: 0x2e5
+  __TEXT.__objc_methname: 0x205f
+  __TEXT.__objc_methtype: 0xc78
+  __TEXT.__cstring: 0x508
+  __TEXT.__const: 0xf4
   __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__oslogstring: 0x71f
-  __TEXT.__unwind_info: 0x278
-  __DATA_CONST.__auth_got: 0x2e8
+  __TEXT.__oslogstring: 0x52b
+  __TEXT.__unwind_info: 0x280
+  __DATA_CONST.__auth_got: 0x2c0
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x2c8
-  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__cfstring: 0x7c0
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
-  __DATA.__objc_const: 0x1e90
-  __DATA.__objc_selrefs: 0x700
+  __DATA.__objc_const: 0x1810
+  __DATA.__objc_selrefs: 0x818
   __DATA.__objc_ivar: 0x114
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
-  Functions: 229
-  Symbols:   128
-  CStrings:  638
+  Functions: 245
+  Symbols:   127
+  CStrings:  636
 
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
