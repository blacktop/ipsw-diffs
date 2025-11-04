## DeviceSharingServices

> `/System/Library/PrivateFrameworks/DeviceSharingServices.framework/DeviceSharingServices`

```diff

-38.40.4.0.0
-  __TEXT.__text: 0x213c4
-  __TEXT.__auth_stubs: 0x1060
+38.60.2.0.0
+  __TEXT.__text: 0x217dc
+  __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_methlist: 0x624
-  __TEXT.__const: 0x372c
-  __TEXT.__cstring: 0x13e7
-  __TEXT.__oslogstring: 0xb31
-  __TEXT.__swift5_typeref: 0x95d
-  __TEXT.__constg_swiftt: 0x910
-  __TEXT.__swift5_reflstr: 0x9cc
-  __TEXT.__swift5_fieldmd: 0x858
+  __TEXT.__const: 0x379c
+  __TEXT.__cstring: 0x1427
+  __TEXT.__oslogstring: 0xca1
+  __TEXT.__swift5_typeref: 0x9a9
+  __TEXT.__constg_swiftt: 0xa00
+  __TEXT.__swift5_reflstr: 0x9fc
+  __TEXT.__swift5_fieldmd: 0x8a8
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0x318
-  __TEXT.__swift5_types: 0xe8
+  __TEXT.__swift5_proto: 0x31c
+  __TEXT.__swift5_types: 0xec
+  __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_capture: 0x64
   __TEXT.__swift_as_entry: 0x5c
-  __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0xd68
-  __TEXT.__eh_frame: 0x1860
+  __TEXT.__unwind_info: 0xd78
+  __TEXT.__eh_frame: 0x1868
   __TEXT.__objc_classname: 0x11a
   __TEXT.__objc_methname: 0xdab
   __TEXT.__objc_methtype: 0x226
   __TEXT.__objc_stubs: 0x680
   __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x298
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x428
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x838
-  __AUTH_CONST.__const: 0x18c8
+  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__const: 0x1868
   __AUTH_CONST.__cfstring: 0xbc0
-  __AUTH_CONST.__objc_const: 0x1088
+  __AUTH_CONST.__objc_const: 0x1210
   __AUTH.__objc_data: 0x3b8
-  __AUTH.__data: 0x218
+  __AUTH.__data: 0x3b0
   __DATA.__objc_ivar: 0x68
-  __DATA.__data: 0xa88
+  __DATA.__data: 0xa28
   __DATA.__bss: 0x5ed0
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x78

   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DeviceSharingServicesCore.framework/DeviceSharingServicesCore
-  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F4E82C7E-CA0B-3A52-9C38-8C6E484770F5
-  Functions: 1098
-  Symbols:   966
-  CStrings:  565
+  UUID: 6D315C0C-CE15-3E52-B1EB-E3BA77FBB67E
+  Functions: 1117
+  Symbols:   971
+  CStrings:  568
 
Symbols:
+ __DATA__TtC21DeviceSharingServices23AirPlayReceiverSettings
+ __DATA__TtC21DeviceSharingServices26AirPlayReceiverCoordinator
+ __IVARS__TtC21DeviceSharingServices26AirPlayReceiverCoordinator
+ __METACLASS_DATA__TtC21DeviceSharingServices23AirPlayReceiverSettings
+ __METACLASS_DATA__TtC21DeviceSharingServices26AirPlayReceiverCoordinator
+ _associated conformance 21DeviceSharingServices26AirPlayReceiverCoordinatorC0deF12SettingState33_E81D4AD4631DF37915A0013C695C773BLLOSHAASQ
+ _symbolic $s21DeviceSharingServices32AirPlayReceiverSettingsProvidingP
+ _symbolic _____ 21DeviceSharingServices23AirPlayReceiverSettingsC
+ _symbolic _____ 21DeviceSharingServices26AirPlayReceiverCoordinatorC
+ _symbolic _____ 21DeviceSharingServices26AirPlayReceiverCoordinatorC0deF12SettingState33_E81D4AD4631DF37915A0013C695C773BLLO
+ _symbolic ______p 21DeviceSharingServices32AirPlayReceiverSettingsProvidingP
- ___swift_destroy_boxed_opaque_existential_0Tm
- _associated conformance 21DeviceSharingServices20CompanionAppFeaturesOSHAASQ
- _symbolic _____ 21DeviceSharingServices20CompanionAppFeaturesO
- _symbolic _____ 21DeviceSharingServices26AirPlayReceiverCoordinatorV
- _type_layout_string 21DeviceSharingServices26AirPlayReceiverCoordinatorV
CStrings:
+ "[%{public}s] AirPlayReceiver is already enabled by user"
+ "[%{public}s] AirPlayReceiver is disabled by user; temporarily enabling for Guest User session"
+ "[%{public}s] AirPlayReceiver setting already matches user's preference prior to Guest User session"
+ "[%{public}s] AirPlayReceiver setting disabled to match user's preference prior to Guest User session"
+ "[%{public}s] AirPlayReceiver setting was already checked"
+ "[%{public}s] Disabling AirPlayReceiver if needed..."
+ "[%{public}s] Enabling AirPlayReceiver if needed..."
+ "_TtC21DeviceSharingServices23AirPlayReceiverSettings"
+ "_TtC21DeviceSharingServices26AirPlayReceiverCoordinator"
+ "airPlayReceiverSettingsManager"
+ "previousAirPlayReceiverState"
- "AirPlayReceiver"
- "Tetsuo"
- "[%{public}s] AirPlayReceiver already enabled"
- "[%{public}s] AirPlayReceiver enabled"
- "[%{public}s] AirPlayReceiver not reset"
- "[%{public}s] AirPlayReceiver reset back to disabled"
- "airplayreceiver-private://guestUserHandoverRequestViewMirroring"
- "com.apple.airplayreceiver"

```
