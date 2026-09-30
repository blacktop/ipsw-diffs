## GenericGamepadHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/GenericGamepadHIDServicePlugin.plugin/GenericGamepadHIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0xd2a4
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_stubs: 0x1b80
+12.4.10.0.0
+  __TEXT.__text: 0xdc3c
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_stubs: 0x1d00
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x828
-  __TEXT.__cstring: 0xde2
-  __TEXT.__objc_classname: 0x2f0
-  __TEXT.__objc_methname: 0x250e
-  __TEXT.__objc_methtype: 0xc4c
+  __TEXT.__objc_methlist: 0xcbc
+  __TEXT.__cstring: 0xe52
+  __TEXT.__objc_classname: 0x362
+  __TEXT.__objc_methname: 0x2668
+  __TEXT.__objc_methtype: 0xdc8
   __TEXT.__const: 0x115
-  __TEXT.__gcc_except_tab: 0x5a8
-  __TEXT.__oslogstring: 0x811
-  __TEXT.__unwind_info: 0x3c8
-  __DATA_CONST.__auth_got: 0x3b0
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x8c0
-  __DATA_CONST.__cfstring: 0xa40
+  __TEXT.__gcc_except_tab: 0x5ac
+  __TEXT.__oslogstring: 0x7a6
+  __TEXT.__unwind_info: 0x3d0
+  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x830
+  __DATA_CONST.__cfstring: 0xbc0
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1f80
-  __DATA.__objc_selrefs: 0x8f8
-  __DATA.__objc_ivar: 0x128
+  __DATA.__objc_const: 0x1930
+  __DATA.__objc_selrefs: 0xa70
+  __DATA.__objc_ivar: 0x130
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x7e0
-  __DATA.__bss: 0xc9
+  __DATA.__data: 0x900
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
-  Functions: 310
-  Symbols:   177
-  CStrings:  762
+  Functions: 347
+  Symbols:   178
+  CStrings:  796
 
Symbols:
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$__GCHapticEvent
+ _OBJC_METACLASS_$__GCHapticEvent
+ _hexStringFromByteArray
+ _isPartnerSupportEnabled
+ _memcmp
- _BTDeviceAddressFromString
- _BTDeviceDisconnect
- _BTDeviceFromAddress
- _BTSessionAttachWithQueue
- _BTSessionDetachWithQueue
CStrings:
+ "\x02\x11\xf0\xf0\xf0\xf0\x15\x83!\x11"
+ "#ERROR Caught an exception while applying configuration: %@"
+ "#ERROR Error applying configuration: %@"
+ "@\"<GCIdleServiceClientInterface>\""
+ "@\"GCHIDInputElement\"24@0:8@\"NSString\"16"
+ "@\"HIDElement\"24@0:8@\"NSString\"16"
+ "@40@0:8@\"GCGenericDeviceDataProcessorExpressionModel\"16@?<v@?d>24o^@32"
+ "@40@0:8@16@?24o^@32"
+ "@?32@0:8@16o^@24"
+ "@?<d@?>32@0:8@\"GCGenericDeviceDataProcessorExpressionModel\"16o^@24"
+ "GCGenericDeviceDataProcessorExpressionCompilationContext"
+ "GCIdleServiceClientInterface"
+ "GCIdleServiceServerInterface"
+ "HIDRMOverride"
+ "Has accelerometer."
+ "Has gyro."
+ "IOHIDDeviceForceInterfaceRematch"
+ "IOHIDDeviceSuspend"
+ "Invalid accelerometerXExpression field"
+ "Invalid accelerometerYExpression field"
+ "Invalid accelerometerZExpression field"
+ "Invalid gyroXExpression field"
+ "Invalid gyroYExpression field"
+ "Invalid gyroZExpression field"
+ "MaxReportBufferCount"
+ "No motor with name '%@'."
+ "Processing motion accelerometerX expression %@"
+ "Processing motion accelerometerY expression %@"
+ "Processing motion accelerometerZ expression %@"
+ "Processing motion gyroPitch expression %@"
+ "Processing motion gyroRoll expression %@"
+ "Processing motion gyroYaw expression %@"
+ "Register"
+ "ReportBufferEntrySize"
+ "_idleClient"
+ "_lastMotionState"
+ "accelerometerXExpression"
+ "accelerometerYExpression"
+ "accelerometerZExpression"
+ "buildExpression:error:"
+ "buildExpressionWithContext:error:"
+ "buildReactiveExpression:consumer:error:"
+ "buildReactiveExpressionWithContext:consumer:error:"
+ "connectToIdleServiceWithClient:reply:"
+ "elementWithIdentifier:"
+ "gyroXExpression"
+ "gyroYExpression"
+ "gyroZExpression"
+ "inputElementWithIdentifier:"
+ "motion"
+ "null"
+ "requestIdleDiconnect:"
+ "v24@0:8@\"NSString\"16"
+ "v32@0:8@\"<GCIdleServiceClientInterface>\"16@?<v@?@\"<GCIdleServiceServerInterface>\"@\"NSError\">24"
- "\x02\x11\xf0\xf0\xf0\xf0$\x83!\x11"
- "@?<d@?>24@?0@\"GCGenericDeviceDataInputElementAttributeExpressionModel\"8^@16"
- "@?<d@?>24@?0@\"GCGenericDeviceDataProcessorExpressionModel\"8^@16"
- "@?<d@?>24@?0@\"GCGenericDeviceDataRumbleMotorValueExpressionModel\"8^@16"
- "BTSessionEventCallback: attached session = %p"
- "BTSessionEventCallback: detached session = %p"
- "BTSessionEventCallback: failed session = %p"
- "BTSessionEventCallback: terminated session = %p"
- "GCHIDLog::disconnect: SUCCESS"
- "GCHIDLog::disconnect: error code = %d"
- "GCHIDLog::disconnect: unable to get BTDevice; error code = %d"
- "GCHIDLog::disconnect: unable to get BTDevice; no valid BTSession"
- "GCHIDLog::disconnect: unable to get device address from %s; errCode = %d"
- "No motor with name %@"
- "^{BTSessionImpl=}"
- "_session"
- "buildPullExpressionWithOverrideBuilder:error:"
- "cStringUsingEncoding:"
- "registering for BTSessionCallbacks sessionEvent"

```
