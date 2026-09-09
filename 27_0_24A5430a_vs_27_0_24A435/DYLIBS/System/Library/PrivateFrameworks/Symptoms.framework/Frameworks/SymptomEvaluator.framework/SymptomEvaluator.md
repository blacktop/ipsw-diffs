## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

 2394.0.4.0.0
-  __TEXT.__text: 0x2a0bd0
-  __TEXT.__objc_methlist: 0x18cb0
-  __TEXT.__cstring: 0x278d0
+  __TEXT.__text: 0x2a1080
+  __TEXT.__objc_methlist: 0x18cf8
+  __TEXT.__cstring: 0x27970
   __TEXT.__const: 0x1268
-  __TEXT.__oslogstring: 0x47e45
+  __TEXT.__oslogstring: 0x47eb5
   __TEXT.__gcc_except_tab: 0x52c8
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x38d

   __TEXT.bb_MAV_clp: 0x89e0
   __TEXT.bb_INT_clp: 0x6d20
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x7aa0
+  __TEXT.__unwind_info: 0x7ab0
   __TEXT.__eh_frame: 0x7d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6fe8
+  __DATA_CONST.__const: 0x7058
   __DATA_CONST.__objc_classlist: 0x8b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd508
+  __DATA_CONST.__objc_selrefs: 0xd548
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x5d8
   __DATA_CONST.__objc_arraydata: 0x980
   __DATA_CONST.__got: 0x10c0
   __AUTH_CONST.__const: 0x3230
-  __AUTH_CONST.__cfstring: 0x1f400
-  __AUTH_CONST.__objc_const: 0x41ae0
+  __AUTH_CONST.__cfstring: 0x1f560
+  __AUTH_CONST.__objc_const: 0x41b80
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0xa00

   __AUTH_CONST.__auth_got: 0x1790
   __AUTH.__objc_data: 0x11c8
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x31a8
+  __DATA.__objc_ivar: 0x31b8
   __DATA.__data: 0x1f20
   __DATA.__crash_info: 0x148
   __DATA.__common: 0xa8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12233
-  Symbols:   25106
-  CStrings:  12219
+  Functions: 12241
+  Symbols:   25126
+  CStrings:  12231
 
Symbols:
+ -[MotionStateRelay deviceStatePropertyB]
+ -[MotionStateRelay setDeviceStatePropertyB:]
+ -[MotionStateRelay startDeviceStatePropertyBMonitoring]
+ -[MotionStateRelay stopDeviceStatePropertyBMonitoring]
+ -[SFDeviceReport deviceStatePropertyB]
+ -[SFDeviceReport setDeviceStatePropertyB:]
+ _OBJC_IVAR_$_MotionStateRelay._deviceStateManager
+ _OBJC_IVAR_$_MotionStateRelay._deviceStateOperationQueue
+ _OBJC_IVAR_$_MotionStateRelay._deviceStatePropertyB
+ _OBJC_IVAR_$_SFDeviceReport._deviceStatePropertyB
+ ___55-[MotionStateRelay startDeviceStatePropertyBMonitoring]_block_invoke
+ ___block_descriptor_40_e8_32s_e40_v24?0"CMDeviceStateEvent"8"NSError"16ls32l8
+ _cmDeviceStateManagerClass
+ _isDeviceStateAvailable
+ _objc_msgSend$deviceStatePropertyB
+ _objc_msgSend$isAvailable
+ _objc_msgSend$propertyB
+ _objc_msgSend$setDeviceStatePropertyB:
+ _objc_msgSend$startDeviceStatePropertyBMonitoring
+ _objc_msgSend$startUpdatesToQueue:withHandler:
+ _objc_msgSend$stopDeviceStatePropertyBMonitoring
+ _objc_msgSend$stopUpdates
- _objc_msgSend$observeSetupAssistantFinished
- _objc_msgSend$requireUserNotification
CStrings:
+ "<NWDeviceReport:\n\tTimestamp Bucket:\t\t%u\n\tBattery Percentage:\t\t\t%u\n\tBattery Current Capacity:\t\t%u\n\tBattery Maximum Capacity:\t\t%u\n\tBattery Design Capacity:\t\t%u\n\tBattery Absolute Capacity:\t\t%u\n\tBattery Voltage:\t\t\t%u\n\tBattery Time Remaining:\t\t\t%u\n\tBattery Temperature:\t\t\t%u\n\tBattery External Power Is Connected:\t%u\n\tBattery Fully Charged:\t\t\t%u\n\tBattery At Warn Level:\t\t\t%u\n\tBattery At Critical Level:\t\t%u\n\tRNF Enabled:\t\t\t\t%u\n\tDevice Plugged In:\t\t\t%u\n\tDevice Screen On:\t\t\t%u\n\tDevice Screen Brightness:\t\t%u\n\tMotion State:\t\t\t\t%u\n\tDevice Orientation:\t\t\t%u\n\tDevice State Property B:\t\t\t%u\n\tThermal Pressure:\t\t\t%u\n\tQUIC Experimentally Enabled:\t\t%u\n\tUnified HTTP Stack Experimentally Enabled:\t\t%u\n\tPrivacy Proxy Service Status:\t\t%u\n\tPrivacy Proxy User Tier:\t\t%u\n\tPrivacy Proxy Networks:\t\t%@\n\tPrivacy Proxy Traffic:\t\t%@\n>"
+ "Ambiguous"
+ "CMDeviceStateManager"
+ "D"
+ "E"
+ "F"
+ "G"
+ "H"
+ "MotionDeviceStateQueue"
+ "MotionStateRelay: Device state changed to %ld"
+ "MotionStateRelay: motion activity class for device state is %@available."
+ "deviceStatePropertyB"
+ "v24@?0@\"CMDeviceStateEvent\"8@\"NSError\"16"
+ "\xb6"
- "<NWDeviceReport:\n\tTimestamp Bucket:\t\t%u\n\tBattery Percentage:\t\t\t%u\n\tBattery Current Capacity:\t\t%u\n\tBattery Maximum Capacity:\t\t%u\n\tBattery Design Capacity:\t\t%u\n\tBattery Absolute Capacity:\t\t%u\n\tBattery Voltage:\t\t\t%u\n\tBattery Time Remaining:\t\t\t%u\n\tBattery Temperature:\t\t\t%u\n\tBattery External Power Is Connected:\t%u\n\tBattery Fully Charged:\t\t\t%u\n\tBattery At Warn Level:\t\t\t%u\n\tBattery At Critical Level:\t\t%u\n\tRNF Enabled:\t\t\t\t%u\n\tDevice Plugged In:\t\t\t%u\n\tDevice Screen On:\t\t\t%u\n\tDevice Screen Brightness:\t\t%u\n\tMotion State:\t\t\t\t%u\n\tDevice Orientation:\t\t\t%u\n\tThermal Pressure:\t\t\t%u\n\tQUIC Experimentally Enabled:\t\t%u\n\tUnified HTTP Stack Experimentally Enabled:\t\t%u\n\tPrivacy Proxy Service Status:\t\t%u\n\tPrivacy Proxy User Tier:\t\t%u\n\tPrivacy Proxy Networks:\t\t%@\n\tPrivacy Proxy Traffic:\t\t%@\n>"
- "\xa6"
```
