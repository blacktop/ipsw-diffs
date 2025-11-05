## GenericGamepadHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/GenericGamepadHIDServicePlugin.plugin/Contents/MacOS/GenericGamepadHIDServicePlugin`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0xefac
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x1c00
+12.4.12.0.0
+  __TEXT.__text: 0xfa70
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x1d80
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x858
-  __TEXT.__cstring: 0xdf6
-  __TEXT.__objc_classname: 0x2f1
-  __TEXT.__objc_methname: 0x2629
-  __TEXT.__objc_methtype: 0xca7
+  __TEXT.__objc_methlist: 0xcec
+  __TEXT.__cstring: 0xe66
+  __TEXT.__objc_classname: 0x363
+  __TEXT.__objc_methname: 0x2783
+  __TEXT.__objc_methtype: 0xe23
   __TEXT.__const: 0x11d
-  __TEXT.__gcc_except_tab: 0x5ac
-  __TEXT.__oslogstring: 0x957
-  __TEXT.__unwind_info: 0x440
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x980
-  __DATA_CONST.__cfstring: 0xa60
+  __TEXT.__gcc_except_tab: 0x5b0
+  __TEXT.__oslogstring: 0x8ec
+  __TEXT.__unwind_info: 0x450
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x8e0
+  __DATA_CONST.__cfstring: 0xbe0
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
-  __DATA.__objc_const: 0x2040
-  __DATA.__objc_selrefs: 0x928
-  __DATA.__objc_ivar: 0x140
+  __DATA.__objc_const: 0x19f0
+  __DATA.__objc_selrefs: 0xaa0
+  __DATA.__objc_ivar: 0x148
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x7e0
-  __DATA.__bss: 0xc9
+  __DATA.__data: 0x900
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
-  UUID: CD711924-FB85-36BE-962D-7A95E628FFF9
-  Functions: 352
-  Symbols:   163
-  CStrings:  867
+  UUID: 325DE27C-B7DC-392F-BD2F-FAF9ACEED604
+  Functions: 391
+  Symbols:   164
+  CStrings:  913
 
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
