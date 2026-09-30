## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x5da10
-  __TEXT.__auth_stubs: 0x13f0
-  __TEXT.__objc_methlist: 0x555c
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x627b
-  __TEXT.__gcc_except_tab: 0x29c4
-  __TEXT.__oslogstring: 0x2edb
+12.4.10.0.0
+  __TEXT.__text: 0x6bf58
+  __TEXT.__auth_stubs: 0x1420
+  __TEXT.__objc_methlist: 0x6604
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x3350
+  __TEXT.__cstring: 0x6a87
+  __TEXT.__oslogstring: 0x305b
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x1db0
-  __TEXT.__objc_classname: 0x1684
-  __TEXT.__objc_methname: 0x7d16
-  __TEXT.__objc_methtype: 0x24fa
-  __TEXT.__objc_stubs: 0x4ce0
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x18e8
-  __DATA_CONST.__objc_classlist: 0x440
-  __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x148
+  __TEXT.__unwind_info: 0x2040
+  __TEXT.__eh_frame: 0x48
+  __TEXT.__objc_classname: 0x1753
+  __TEXT.__objc_methname: 0x889a
+  __TEXT.__objc_methtype: 0x2977
+  __TEXT.__objc_stubs: 0x51c0
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__const: 0x1b18
+  __DATA_CONST.__objc_classlist: 0x460
+  __DATA_CONST.__objc_catlist: 0x70
+  __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xff90
-  __DATA_CONST.__objc_selrefs: 0x19e0
-  __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_classrefs: 0x430
-  __DATA_CONST.__objc_superrefs: 0x408
-  __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__cfstring: 0x64e0
-  __AUTH_CONST.__objc_const: 0x4178
-  __AUTH_CONST.__objc_intobj: 0x228
-  __AUTH_CONST.__const: 0x548
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x50
+  __DATA_CONST.__objc_selrefs: 0x1c68
+  __DATA_CONST.__objc_protorefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_arraydata: 0x140
+  __AUTH_CONST.__auth_got: 0xa28
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xa10
-  __AUTH.__objc_data: 0x2210
+  __AUTH_CONST.__const: 0x548
+  __AUTH_CONST.__cfstring: 0x6ac0
+  __AUTH_CONST.__objc_const: 0x13f40
+  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH.__objc_data: 0x28a0
   __AUTH.__data: 0x10b0
-  __DATA.__objc_ivar: 0x748
-  __DATA.__data: 0xf60
+  __DATA.__objc_ivar: 0x7e0
+  __DATA.__data: 0x1080
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x100
-  __DATA_DIRTY.__objc_data: 0x870
-  __DATA_DIRTY.__bss: 0x78
+  __DATA.__bss: 0x130
+  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2426
-  Symbols:   3205
-  CStrings:  3148
+  Functions: 2753
+  Symbols:   3623
+  CStrings:  3338
 
Symbols:
+ _CFDictionaryRemoveAllValues
+ _IOHIDEventSystemClientActivate
+ _IOHIDEventSystemClientCancel
+ _IOHIDEventSystemClientCopyServiceForRegistryID
+ _IOHIDEventSystemClientCopyServices
+ _IOHIDEventSystemClientCreateWithType
+ _IOHIDEventSystemClientRegisterDeviceMatchingCallback
+ _IOHIDEventSystemClientRegisterEventCallback
+ _IOHIDEventSystemClientSetCancelHandler
+ _IOHIDEventSystemClientSetDispatchQueue
+ _IOHIDEventSystemClientSetMatchingMultiple
+ _IOHIDServiceClientRegisterRemovalCallback
+ _OBJC_CLASS_$_GCDisposable
+ _OBJC_CLASS_$_GCGenericDeviceMotionEventDriverModel
+ _OBJC_CLASS_$_GCGenericDeviceMotionEventDriverModelBuilder
+ _OBJC_CLASS_$_GCHIDEventSystemClient
+ _OBJC_CLASS_$_NSValue
+ _OBJC_METACLASS_$_GCDisposable
+ _OBJC_METACLASS_$_GCGenericDeviceMotionEventDriverModel
+ _OBJC_METACLASS_$_GCGenericDeviceMotionEventDriverModelBuilder
+ _OBJC_METACLASS_$_GCHIDEventSystemClient
+ __Block_object_assign
+ _objc_storeWeakOrNil
CStrings:
+ "\x11\x11"
+ "#WARNING Duplicate HID Service Matched: serviceID='%#010llx'"
+ "#WARNING Un-tracked HID Service Removed: serviceID='%#010llx'"
+ "(?=\"object\"@\"handler\"@?)"
+ "*** Client is not configured to receive events.  The callback will never be invoked."
+ "*** This property may not be mutated after client activation."
+ "<%@ %p> {\n\t accelerometerXExpression = %@\n\t accelerometerYExpression = %@\n\t accelerometerZExpression = %@\n\t gyroXExpression = %@\n\t gyroYExpression = %@\n\t gyroZExpression = %@\n}"
+ "<%@ %p> {\n\t elements = %@\n\t properties = %@\n\t input = %@\n\t motion = %@\n\t rumble = %@\n}"
+ "@\"<GCHIDSystemServiceInfo>\"24@0:8Q16"
+ "@\"GCGenericDeviceMotionEventDriverModel\""
+ "@\"GCHIDEventSystemClient\""
+ "@\"GCHIDServiceInfo\"24@?0@8Q16"
+ "@\"GCHIDServiceInfo\"8@?0"
+ "@\"NSNumber\"24@0:8@\"NSString\"16"
+ "@\"NSObject<OS_dispatch_queue>\"16@0:8"
+ "@\"NSSet\"16@0:8"
+ "@24@0:8@?<v@?^{__IOHIDEvent=}@?<@\"<GCHIDSystemServiceInfo>\"@?>>16"
+ "@24@0:8Q16"
+ "@28@0:8@?16B24"
+ "@28@0:8@?<v@?@\"NSSet\"@\"NSArray\"@\"NSArray\">16B24"
+ "@32@0:8@\"NSString\"16#24"
+ "@36@0:8@16i24@28"
+ "@40@0:8@16@?24o^@32"
+ "@40@0:8^{__IOHIDServiceClient=}16@24r^{GCHIDServiceClientFunctions=^?^?^?}32"
+ "@44@0:8@16i24@28@36"
+ "@44@0:8@16i24@28r^{GCHIDEventSystemClientFunctions=^?^?^?^?^?^?^?^?^?^?^{GCHIDServiceClientFunctions}}36"
+ "@80@0:8{?=[4]}16"
+ "@?32@0:8@16o^@24"
+ "AccelerometerXExpression"
+ "AccelerometerYExpression"
+ "AccelerometerZExpression"
+ "Context is tot tracking any elements."
+ "Context is tot tracking any input elements."
+ "Element with identifier '%@' does not have a '%@' attribute."
+ "Element with identifier '%@' has an '%@' attribute, but it's not a number."
+ "Failed to build expression closure for '%@'."
+ "GCDisposable"
+ "GCGenericDeviceMotionEventDriverModel"
+ "GCGenericDeviceMotionEventDriverModelBuilder"
+ "GCHIDEventSystemClient"
+ "GCHIDEventSystemClient.m"
+ "GCHIDSystemEventProviding"
+ "GCHIDSystemServiceInfo"
+ "GCHIDSystemServiceProviding"
+ "GyroXExpression"
+ "GyroYExpression"
+ "GyroZExpression"
+ "HID Service Matched: serviceID='%#010llx'"
+ "HID Service Removed: serviceID='%#010llx'"
+ "Invalid 'Element Exists' expression."
+ "Invalid 'Input Element Attribute' expression."
+ "Invalid 'Input Element Value' expression."
+ "Motion"
+ "Motion Event Driver"
+ "Not tracking any element with identifier %@"
+ "PressedValueThreshold"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_accelerometerXExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_accelerometerYExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_accelerometerZExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_gyroXExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_gyroYExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",C,N,V_gyroZExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_accelerometerXExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_accelerometerYExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_accelerometerZExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_gyroXExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_gyroYExpression"
+ "T@\"GCGenericDeviceDataProcessorExpressionModel\",R,C,V_gyroZExpression"
+ "T@\"GCGenericDeviceMotionEventDriverModel\",C,N,V_motion"
+ "T@\"GCGenericDeviceMotionEventDriverModel\",R,C,V_motion"
+ "T@\"NSObject<OS_dispatch_queue>\",R"
+ "T@\"NSSet\",R"
+ "T@\"NSSet\",R,V_services"
+ "Td,N,V_pressedThreshold"
+ "Td,N,V_touchedThreshold"
+ "Td,R,V_pressedThreshold"
+ "Td,R,V_touchedThreshold"
+ "Tf,N,V_touchedThreshold"
+ "The 'falseExpression' sub-expression failed to build."
+ "The 'inputExpression' sub-expression failed to build."
+ "The 'inputMaxExpression' sub-expression failed to build."
+ "The 'inputMinExpression' sub-expression failed to build."
+ "The 'leftExpression' sub-expression failed to build."
+ "The 'maskExpression' sub-expression failed to build."
+ "The 'maxExpression' sub-expression failed to build."
+ "The 'minExpression' sub-expression failed to build."
+ "The 'outputMaxExpression' sub-expression failed to build."
+ "The 'outputMinExpression' sub-expression failed to build."
+ "The 'rightExpression' sub-expression failed to build."
+ "The 'trueExpression' sub-expression failed to build."
+ "TouchedValueSource"
+ "TouchedValueThreshold"
+ "Tq,N,V_sourcePressedValueExtendedEventFieldIndex"
+ "Tq,N,V_sourceTouchedValueExtendedEventFieldIndex"
+ "Tq,R,V_sourcePressedValueExtendedEventFieldIndex"
+ "Tq,R,V_sourceTouchedValueExtendedEventFieldIndex"
+ "T{?=[4]},R"
+ "Unsupported valueType."
+ "[HID Event System Client] Activate"
+ "[HID Event System Client] Cancelled"
+ "[HID Event System Client] Notify HID Service Matched"
+ "[HID Event System Client] Notify HID Service Removed"
+ "^{__IOHIDEventSystemClient=}"
+ "__GCHIDSystemObservation"
+ "_accelerometerXExpression"
+ "_accelerometerYExpression"
+ "_accelerometerZExpression"
+ "_client"
+ "_eventObservations"
+ "_functions"
+ "_gyroXExpression"
+ "_gyroYExpression"
+ "_gyroZExpression"
+ "_isEventMonitor"
+ "_listEntry"
+ "_motion"
+ "_observer"
+ "_observerIsBlock"
+ "_serviceObservations"
+ "_services"
+ "_sourcePressedValueExtendedEventFieldIndex"
+ "_sourceTouchedValueExtendedEventFieldIndex"
+ "_touchedThreshold"
+ "accelerometerXExpression"
+ "accelerometerYExpression"
+ "accelerometerZExpression"
+ "anyObject"
+ "buildExpression:error:"
+ "buildExpressionWithContext:error:"
+ "buildReactiveExpression:consumer:error:"
+ "buildReactiveExpressionWithContext:consumer:error:"
+ "elementWithIdentifier:"
+ "gc_arrayByRemovingObject:"
+ "gc_member:"
+ "gc_peerBundleIdentifier"
+ "gc_peerTeamIdentifier"
+ "gc_simdFloat4x4Value"
+ "gc_valueWithSimdFloat4x4:"
+ "getValue:size:"
+ "gyroXExpression"
+ "gyroYExpression"
+ "gyroZExpression"
+ "handleHIDEvent:from:"
+ "initWithKey:sourceBundle:table:"
+ "initWithObjects:"
+ "initWithQueue:type:attributes:"
+ "initWithQueue:type:attributes:environment:"
+ "initWithQueue:type:attributes:functions:"
+ "initWithService:queue:functions:"
+ "inputElementWithIdentifier:"
+ "motion"
+ "r^{GCHIDEventSystemClientFunctions=^?^?^?^?^?^?^?^?^?^?^{GCHIDServiceClientFunctions}}"
+ "r^{GCHIDServiceClientFunctions=^?^?^?}"
+ "registerEventHandler:"
+ "registerEventObserver:"
+ "registerServicesChangedHandler:notifyExisting:"
+ "registerServicesChangedObserver:notifyExisting:"
+ "serviceForRegistryID:"
+ "serviceID"
+ "services"
+ "servicesDidChange:withAddedServices:removedServices:"
+ "setAccelerometerXExpression:"
+ "setAccelerometerYExpression:"
+ "setAccelerometerZExpression:"
+ "setEventCallBack:target:context:"
+ "setGyroXExpression:"
+ "setGyroYExpression:"
+ "setGyroZExpression:"
+ "setMatching:"
+ "setMatchingMultiple:"
+ "setMotion:"
+ "setServicesChangedCallback:target:context:"
+ "setSourcePressedValueExtendedEventFieldIndex:"
+ "setSourceTouchedValueExtendedEventFieldIndex:"
+ "setTouchedThreshold:"
+ "sourcePressedValueExtendedEventFieldIndex"
+ "sourceTouchedValueExtendedEventFieldIndex"
+ "touchedThreshold"
+ "unregisterEventObserver:"
+ "unregisterServicesChangedObserver:notifyExisting:"
+ "v16@?0d8"
+ "v24@0:8@\"<GCHIDSystemEventObserver>\"16"
+ "v28@0:8@\"<GCHIDSystemServiceMatchObserver>\"16B24"
+ "v32@?0@\"GCHIDInputElement\"8^{__IOHIDValue=}16d24"
+ "v40@0:8^?16^v24^v32"
+ "valueWithBytes:objCType:"
+ "withCleanupHandler:"
+ "{?=\"tqe_next\"@\"__GCHIDSystemObservation\"\"tqe_prev\"^@}"
+ "{?=[4]}16@0:8"
+ "{HIDSystemObservationList=\"lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"count\"I\"tqh_first\"@\"__GCHIDSystemObservation\"\"tqh_last\"^@\"primaryHandler\"{?=\"callback\"^v\"target\"Q\"context\"Q}}"
+ "{simd_float4x4_layout=[4{simd_float4_layout=ffff}]}"
- "\x01\x11"
- "<%@ %p> {\n\t elements = %@\n\t properties = %@\n\t input = %@\n\t rumble = %@\n}"
- "@?32@0:8@?16o^@24"
- "Tq,N,V_sourceExtendedEventFieldIndex"
- "Tq,R,V_sourceExtendedEventFieldIndex"
- "_GCDisposable"
- "_buildPullExpressionWithOverrideBuilder:error:"
- "_sourceExtendedEventFieldIndex"
- "buildPullExpressionWithOverrideBuilder:error:"
- "setSourceExtendedEventFieldIndex:"
- "sourceExtendedEventFieldIndex"

```
