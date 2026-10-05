## LocalAuthenticationCoreUI

> `/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`

```diff

-2319.40.35.0.1
-  __TEXT.__text: 0x99948
-  __TEXT.__objc_methlist: 0x30bc
-  __TEXT.__const: 0x6f54
-  __TEXT.__cstring: 0x2fd6
-  __TEXT.__oslogstring: 0xf8d
-  __TEXT.__gcc_except_tab: 0x14c
+2319.40.43.0.0
+  __TEXT.__text: 0x9a504
+  __TEXT.__objc_methlist: 0x317c
+  __TEXT.__const: 0x6f64
+  __TEXT.__cstring: 0x3026
+  __TEXT.__oslogstring: 0x108d
+  __TEXT.__gcc_except_tab: 0x16c
   __TEXT.__swift5_typeref: 0x101a2
-  __TEXT.__constg_swiftt: 0x22b8
+  __TEXT.__constg_swiftt: 0x22c8
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_reflstr: 0x1131
   __TEXT.__swift5_fieldmd: 0x1410
   __TEXT.__swift5_assocty: 0x468
-  __TEXT.__swift5_proto: 0x19c
+  __TEXT.__swift5_proto: 0x1a0
   __TEXT.__swift5_types: 0x17c
   __TEXT.__swift5_capture: 0xfb0
   __TEXT.__swift5_mpenum: 0x10

   __TEXT.__swift_as_entry: 0x54
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift_as_cont: 0x114
-  __TEXT.__unwind_info: 0x3480
-  __TEXT.__eh_frame: 0x1650
+  __TEXT.__unwind_info: 0x34b8
+  __TEXT.__eh_frame: 0x1678
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9f8
-  __DATA_CONST.__objc_classlist: 0x2c0
-  __DATA_CONST.__objc_protolist: 0x220
+  __DATA_CONST.__const: 0xa20
+  __DATA_CONST.__objc_classlist: 0x2c8
+  __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d48
+  __DATA_CONST.__objc_selrefs: 0x1d98
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0xdc8
-  __AUTH_CONST.__const: 0x4250
-  __AUTH_CONST.__cfstring: 0xe20
-  __AUTH_CONST.__objc_const: 0xc320
+  __AUTH_CONST.__const: 0x4280
+  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__objc_const: 0xc7b8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x16c8
-  __AUTH.__objc_data: 0x738
-  __AUTH.__data: 0x1d0
-  __DATA.__objc_ivar: 0x210
-  __DATA.__data: 0x23c0
+  __AUTH_CONST.__auth_got: 0x16d8
+  __AUTH.__objc_data: 0x788
+  __AUTH.__data: 0x1c0
+  __DATA.__objc_ivar: 0x21c
+  __DATA.__data: 0x2430
   __DATA.__objc_stublist: 0x10
   __DATA.__common: 0x58
-  __DATA_DIRTY.__objc_data: 0x1fa8
-  __DATA_DIRTY.__data: 0x2180
+  __DATA_DIRTY.__objc_data: 0x1fc0
+  __DATA_DIRTY.__data: 0x21a0
   __DATA_DIRTY.__bss: 0xd90
   __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4555
-  Symbols:   10523
-  CStrings:  403
+  Functions: 4569
+  Symbols:   10562
+  CStrings:  409
 
Symbols:
+ -[LACUITouchIDSensorReachabilityMonitor .cxx_destruct]
+ -[LACUITouchIDSensorReachabilityMonitor _applyDeviceStateEvent:]
+ -[LACUITouchIDSensorReachabilityMonitor _sensorOutOfReachInDeviceStateEvent:]
+ -[LACUITouchIDSensorReachabilityMonitor dealloc]
+ -[LACUITouchIDSensorReachabilityMonitor isSensorOutOfReach]
+ -[LACUITouchIDSensorReachabilityMonitor sensorReachabilityDidChangeHandler]
+ -[LACUITouchIDSensorReachabilityMonitor setSensorReachabilityDidChangeHandler:]
+ -[LACUITouchIDSensorReachabilityMonitor start]
+ -[LACUITouchIDSensorReachabilityMonitor stop]
+ _$s25LocalAuthenticationCoreUI30LACUIPasscodeHostingController33_9C68DDE9F839077839CBDD25F7AE3B54LLC21viewDidLayoutSubviewsyyFTo
+ _$s25LocalAuthenticationCoreUI30LACUIPasscodeHostingController33_9C68DDE9F839077839CBDD25F7AE3B54LLCAA0e4ViewG11ConfiguringA2aEP17configureMaxWidth10windowSizeySo6CGSizeV_tFTW
+ _$s25LocalAuthenticationCoreUI30LACUIPasscodeHostingController33_9C68DDE9F839077839CBDD25F7AE3B54LLCAA0e4ViewG11ConfiguringA2aEP20configureBodyPadding4withySo012UINavigationG0CSg_tFTW
+ _$s25LocalAuthenticationCoreUI30LACUIPasscodeHostingController33_9C68DDE9F839077839CBDD25F7AE3B54LLCAA0e4ViewG11ConfiguringA2aEP25pullDownGestureRecognizer3forSo09UIGestureT0CSgSo06UIViewG0CSg_tFTW
+ _$s25LocalAuthenticationCoreUI30LACUIPasscodeHostingController33_9C68DDE9F839077839CBDD25F7AE3B54LLCAA0e4ViewG11ConfiguringA2aEP29configurePreferredContentSize4withySo6CGSizeV_tFTW
+ _$s25LocalAuthenticationCoreUI30LACUIPasscodeHostingController33_9C68DDE9F839077839CBDD25F7AE3B54LLCAA0e4ViewG11ConfiguringA2aEP9viewModelAA0eoR0CvgTW
+ _$s25LocalAuthenticationCoreUI30LACUIPasscodeHostingController33_9C68DDE9F839077839CBDD25F7AE3B54LLCAA0e4ViewG11ConfiguringAAMc
+ _$s25LocalAuthenticationCoreUI30LACUIPasscodeHostingController33_9C68DDE9F839077839CBDD25F7AE3B54LLCAA0e4ViewG11ConfiguringAAWP
+ _$s25LocalAuthenticationCoreUI38LACUIPasscodeViewControllerConfiguringPAASo06UIViewG0CRbzrlE20configureBodyPadding4withySo012UINavigationG0CSg_tFAA0e7HostingG033_9C68DDE9F839077839CBDD25F7AE3B54LLC_Tg5
+ _$s25LocalAuthenticationCoreUI38LACUIPasscodeViewControllerConfiguringPAASo06UIViewG0CRbzrlE20configureBodyPadding4withySo012UINavigationG0CSg_tFSo0e7ServicefG0C_Tg5
+ _$s7SwiftUI19UIHostingControllerC8rootViewxvgTj
+ _OBJC_CLASS_$_CMDeviceStateManager
+ _OBJC_CLASS_$_LACUITouchIDSensorReachabilityMonitor
+ _OBJC_IVAR_$_LACUITouchIDSensorReachabilityMonitor._deviceStateManager
+ _OBJC_IVAR_$_LACUITouchIDSensorReachabilityMonitor._sensorOutOfReach
+ _OBJC_IVAR_$_LACUITouchIDSensorReachabilityMonitor._sensorReachabilityDidChangeHandler
+ _OBJC_METACLASS_$_LACUITouchIDSensorReachabilityMonitor
+ __OBJC_$_INSTANCE_METHODS_LACUITouchIDSensorReachabilityMonitor
+ __OBJC_$_INSTANCE_VARIABLES_LACUITouchIDSensorReachabilityMonitor
+ __OBJC_$_PROP_LIST_LACUITouchIDSensorReachabilityMonitor
+ __OBJC_$_PROP_LIST_LACUITouchIDSensorReachabilityMonitoring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUITouchIDSensorReachabilityMonitoring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUITouchIDSensorReachabilityMonitoring
+ __OBJC_$_PROTOCOL_REFS_LACUITouchIDSensorReachabilityMonitoring
+ __OBJC_CLASS_PROTOCOLS_$_LACUITouchIDSensorReachabilityMonitor
+ __OBJC_CLASS_RO_$_LACUITouchIDSensorReachabilityMonitor
+ __OBJC_LABEL_PROTOCOL_$_LACUITouchIDSensorReachabilityMonitoring
+ __OBJC_METACLASS_RO_$_LACUITouchIDSensorReachabilityMonitor
+ __OBJC_PROTOCOL_$_LACUITouchIDSensorReachabilityMonitoring
+ ___46-[LACUITouchIDSensorReachabilityMonitor start]_block_invoke
+ ___block_descriptor_40_e8_32w_e40_v24?0"CMDeviceStateEvent"8"NSError"16lw32l8
+ _dispatch_assert_queue$V2
- _$s25LocalAuthenticationCoreUI38LACUIPasscodeViewControllerConfiguringPAASo06UIViewG0CRbzrlE20configureBodyPadding4withySo012UINavigationG0CSg_tFSo0e7ServicefG0C_Tg5Tm
- _$s25LocalAuthenticationCoreUI38LACUIPasscodeViewControllerConfiguringPAASo06UIViewG0CRbzrlE20configureBodyPadding4withySo012UINavigationG0CSg_tFSo0efG0C_Tg5
CStrings:
+ "%{public}@ could not start tracking, the sensor is assumed to be within reach"
+ "%{public}@ has nothing to track, the sensor is assumed to be within reach"
+ "%{public}@ observed A:%ld B:%ld, sensor out of reach: %d"
+ "Failed to read the device state: %{public}@"
+ "LocalAuthenticationUIService"
+ "v24@?0@\"CMDeviceStateEvent\"8@\"NSError\"16"
```
