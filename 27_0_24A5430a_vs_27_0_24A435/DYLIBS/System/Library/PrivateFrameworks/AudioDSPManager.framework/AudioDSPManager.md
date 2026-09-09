## AudioDSPManager

> `/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager`

```diff

 241.110.0.0.0
-  __TEXT.__text: 0xbe264
+  __TEXT.__text: 0xc008c
   __TEXT.__realtime: 0x170
   __TEXT.__init_offsets: 0x10
-  __TEXT.__objc_methlist: 0x7c8
-  __TEXT.__const: 0xef98
+  __TEXT.__objc_methlist: 0x8f0
+  __TEXT.__const: 0xf008
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__swift5_typeref: 0x27f8
-  __TEXT.__swift5_fieldmd: 0x18fc
-  __TEXT.__constg_swiftt: 0x1d80
+  __TEXT.__swift5_typeref: 0x2898
+  __TEXT.__swift5_fieldmd: 0x1918
+  __TEXT.__constg_swiftt: 0x1dbc
   __TEXT.__swift5_protos: 0x58
   __TEXT.__swift5_proto: 0x574
-  __TEXT.__swift5_types: 0x228
-  __TEXT.__swift5_reflstr: 0x149c
+  __TEXT.__swift5_types: 0x22c
+  __TEXT.__swift5_reflstr: 0x14ac
   __TEXT.__swift5_assocty: 0x548
-  __TEXT.__cstring: 0x6500
+  __TEXT.__cstring: 0x65f1
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift_as_cont: 0x64
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x54
-  __TEXT.__swift5_capture: 0x2cc
-  __TEXT.__gcc_except_tab: 0x7158
-  __TEXT.__oslogstring: 0x3b89
-  __TEXT.__unwind_info: 0x3ba0
-  __TEXT.__eh_frame: 0x3618
+  __TEXT.__swift5_capture: 0x31c
+  __TEXT.__gcc_except_tab: 0x7300
+  __TEXT.__oslogstring: 0x3c59
+  __TEXT.__unwind_info: 0x3ca8
+  __TEXT.__eh_frame: 0x37f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc48
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__const: 0xc98
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0x578
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0x5c0
-  __AUTH_CONST.__const: 0x7ed0
-  __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x1078
+  __DATA_CONST.__objc_selrefs: 0x608
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__got: 0x5d8
+  __AUTH_CONST.__const: 0x7fe0
+  __AUTH_CONST.__cfstring: 0x1000
+  __AUTH_CONST.__objc_const: 0x14c8
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__auth_got: 0x1540
-  __AUTH.__objc_data: 0x4d8
-  __AUTH.__data: 0x560
-  __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0x1560
+  __AUTH_CONST.__auth_got: 0x1588
+  __AUTH.__objc_data: 0x618
+  __AUTH.__data: 0x600
+  __DATA.__objc_ivar: 0x70
+  __DATA.__data: 0x1590
   __DATA.__cf_except_bt: 0x2000
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x30

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3598
-  Symbols:   4454
-  CStrings:  1233
+  Functions: 3643
+  Symbols:   4567
+  CStrings:  1245
 
Symbols:
+ +[CMAngleManagerShim isAvailable]
+ +[CMAngleManagerShim isClassAvailable]
+ +[CMDeviceStateManagerShim isAvailable]
+ +[CMDeviceStateManagerShim isClassAvailable]
+ +[CMDeviceStateManagerShim shared]
+ -[CMAngleManagerShim .cxx_destruct]
+ -[CMAngleManagerShim angleUpdateInterval]
+ -[CMAngleManagerShim init]
+ -[CMAngleManagerShim setAngleUpdateInterval:]
+ -[CMAngleManagerShim startAngleUpdatesToQueue:handler:]
+ -[CMAngleManagerShim stopAngleUpdates]
+ -[CMAngleShim angleDegrees]
+ -[CMAngleShim initWithAngle:]
+ -[CMAngleShim isAngleValid]
+ -[CMDeviceStateEventShim initWithEvent:]
+ -[CMDeviceStateEventShim propertyA]
+ -[CMDeviceStateManagerShim .cxx_destruct]
+ -[CMDeviceStateManagerShim init]
+ -[CMDeviceStateManagerShim startUpdatesToQueue:handler:]
+ -[CMDeviceStateManagerShim stopUpdates]
+ GCC_except_table14
+ GCC_except_table1753
+ GCC_except_table1756
+ GCC_except_table1757
+ GCC_except_table1760
+ GCC_except_table1764
+ GCC_except_table1767
+ GCC_except_table1768
+ GCC_except_table1769
+ GCC_except_table24
+ _NSClassFromString
+ _OBJC_CLASS_$_CMAngleManagerShim
+ _OBJC_CLASS_$_CMAngleShim
+ _OBJC_CLASS_$_CMDeviceStateEventShim
+ _OBJC_CLASS_$_CMDeviceStateManagerShim
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_IVAR_$_CMAngleManagerShim._manager
+ _OBJC_IVAR_$_CMAngleShim._angleDegrees
+ _OBJC_IVAR_$_CMAngleShim._angleValid
+ _OBJC_IVAR_$_CMDeviceStateEventShim._propertyA
+ _OBJC_IVAR_$_CMDeviceStateManagerShim._manager
+ _OBJC_METACLASS_$_CMAngleManagerShim
+ _OBJC_METACLASS_$_CMAngleShim
+ _OBJC_METACLASS_$_CMDeviceStateEventShim
+ _OBJC_METACLASS_$_CMDeviceStateManagerShim
+ __DATA__TtC20AudioDSPManagerSwift16CancellationFlag
+ __IVARS__TtC20AudioDSPManagerSwift16CancellationFlag
+ __METACLASS_DATA__TtC20AudioDSPManagerSwift16CancellationFlag
+ __OBJC_$_CLASS_METHODS_CMAngleManagerShim
+ __OBJC_$_CLASS_METHODS_CMDeviceStateManagerShim
+ __OBJC_$_CLASS_PROP_LIST_CMAngleManagerShim
+ __OBJC_$_CLASS_PROP_LIST_CMDeviceStateManagerShim
+ __OBJC_$_INSTANCE_METHODS_CMAngleManagerShim
+ __OBJC_$_INSTANCE_METHODS_CMAngleShim
+ __OBJC_$_INSTANCE_METHODS_CMDeviceStateEventShim
+ __OBJC_$_INSTANCE_METHODS_CMDeviceStateManagerShim
+ __OBJC_$_INSTANCE_VARIABLES_CMAngleManagerShim
+ __OBJC_$_INSTANCE_VARIABLES_CMAngleShim
+ __OBJC_$_INSTANCE_VARIABLES_CMDeviceStateEventShim
+ __OBJC_$_INSTANCE_VARIABLES_CMDeviceStateManagerShim
+ __OBJC_$_PROP_LIST_CMAngleManagerShim
+ __OBJC_$_PROP_LIST_CMAngleShim
+ __OBJC_$_PROP_LIST_CMDeviceStateEventShim
+ __OBJC_CLASS_RO_$_CMAngleManagerShim
+ __OBJC_CLASS_RO_$_CMAngleShim
+ __OBJC_CLASS_RO_$_CMDeviceStateEventShim
+ __OBJC_CLASS_RO_$_CMDeviceStateManagerShim
+ __OBJC_METACLASS_RO_$_CMAngleManagerShim
+ __OBJC_METACLASS_RO_$_CMAngleShim
+ __OBJC_METACLASS_RO_$_CMDeviceStateEventShim
+ __OBJC_METACLASS_RO_$_CMDeviceStateManagerShim
+ __ZZ34+[CMDeviceStateManagerShim shared]E8instance
+ __ZZ34+[CMDeviceStateManagerShim shared]E9onceToken
+ ___34+[CMDeviceStateManagerShim shared]_block_invoke
+ ___55-[CMAngleManagerShim startAngleUpdatesToQueue:handler:]_block_invoke
+ ___56-[CMDeviceStateManagerShim startUpdatesToQueue:handler:]_block_invoke
+ ___block_descriptor_40_ea8_32bs_e17_v16?0"CMAngle"8ls32l8
+ ___block_descriptor_40_ea8_32bs_e40_v24?0"CMDeviceStateEvent"8"NSError"16ls32l8
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _objc_msgSend$angleDegrees
+ _objc_msgSend$angleUpdateInterval
+ _objc_msgSend$initWithAngle:
+ _objc_msgSend$initWithEvent:
+ _objc_msgSend$isAngleValid
+ _objc_msgSend$isAvailable
+ _objc_msgSend$isClassAvailable
+ _objc_msgSend$propertyA
+ _objc_msgSend$setAngleUpdateInterval:
+ _objc_msgSend$setName:
+ _objc_msgSend$setQualityOfService:
+ _objc_msgSend$shared
+ _objc_msgSend$sharedManager
+ _objc_msgSend$startAngleUpdatesToQueue:handler:
+ _objc_msgSend$startUpdatesToQueue:handler:
+ _objc_msgSend$startUpdatesToQueue:withHandler:
+ _objc_msgSend$stopAngleUpdates
+ _objc_msgSend$stopUpdates
+ _objc_release_x1
+ _objc_retainBlock
+ _objc_retain_x3
+ _swift_retain_x2
+ _symbolic So18CMAngleManagerShimC
+ _symbolic So24CMDeviceStateManagerShimC
+ _symbolic _____ 20AudioDSPManagerSwift16CancellationFlagC
+ _symbolic _____ySbG 15Synchronization6AtomicV
+ _symbolic _____ySf_G ScS12ContinuationV
+ _symbolic _____ySf__G ScS12ContinuationV11YieldResultO
+ _symbolic _____ySf__G ScS12ContinuationV15BufferingPolicyO
+ _symbolic _____y______G ScS12ContinuationV s5Int32V
+ _symbolic _____y_______G ScS12ContinuationV11YieldResultO s5Int32V
+ _symbolic _____y_______G ScS12ContinuationV15BufferingPolicyO s5Int32V
CStrings:
+ "Angle manager reports itself as unavailable"
+ "CMAngleManager"
+ "CMDeviceStateManager"
+ "Device angle update dropped (cancelled)"
+ "Device angle update error: invalid angle"
+ "Device pose update dropped (cancelled)"
+ "Device pose update error: %@"
+ "Device pose update: no event"
+ "State manager reports itself as unavailable"
+ "com.apple.AudioDSPManager.deviceAngle"
+ "com.apple.AudioDSPManager.devicePose"
+ "v16@?0@\"CMAngle\"8"
+ "v24@?0@\"CMDeviceStateEvent\"8@\"NSError\"16"
- "Feature not built in this configuration"
```
