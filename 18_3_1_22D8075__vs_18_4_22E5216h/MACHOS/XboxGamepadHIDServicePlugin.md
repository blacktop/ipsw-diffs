## XboxGamepadHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/XboxGamepadHIDServicePlugin.plugin/XboxGamepadHIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x7edc
-  __TEXT.__auth_stubs: 0x600
+12.4.10.0.0
+  __TEXT.__text: 0x7c38
+  __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_stubs: 0x1400
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x8c8
-  __TEXT.__objc_classname: 0x358
-  __TEXT.__objc_methname: 0x20ca
-  __TEXT.__objc_methtype: 0xbbe
-  __TEXT.__cstring: 0x4a4
-  __TEXT.__const: 0x10c
+  __TEXT.__objc_methlist: 0xcd4
+  __TEXT.__objc_classname: 0x392
+  __TEXT.__objc_methname: 0x20f3
+  __TEXT.__objc_methtype: 0xc42
+  __TEXT.__cstring: 0x4fe
+  __TEXT.__const: 0xfc
   __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__oslogstring: 0x688
+  __TEXT.__oslogstring: 0x494
   __TEXT.__unwind_info: 0x2f0
-  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x340
-  __DATA_CONST.__cfstring: 0x6e0
+  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__cfstring: 0x760
   __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2b58
-  __DATA.__objc_selrefs: 0x730
+  __DATA.__objc_const: 0x24d8
+  __DATA.__objc_selrefs: 0x848
   __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0x2d0
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
-  Functions: 259
-  Symbols:   134
-  CStrings:  636
+  Functions: 276
+  Symbols:   133
+  CStrings:  634
 
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
