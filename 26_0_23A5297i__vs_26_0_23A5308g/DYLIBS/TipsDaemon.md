## TipsDaemon

> `/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon`

```diff

-818.0.0.0.0
-  __TEXT.__text: 0x7fc10
-  __TEXT.__auth_stubs: 0x1e10
-  __TEXT.__objc_methlist: 0x32f0
-  __TEXT.__const: 0x2228
-  __TEXT.__oslogstring: 0x1fb7
-  __TEXT.__cstring: 0x3868
-  __TEXT.__gcc_except_tab: 0x1214
-  __TEXT.__swift5_typeref: 0xd08
-  __TEXT.__swift5_fieldmd: 0x67c
-  __TEXT.__constg_swiftt: 0x9a0
-  __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x3de
+822.0.0.0.0
+  __TEXT.__text: 0x8377c
+  __TEXT.__auth_stubs: 0x2030
+  __TEXT.__objc_methlist: 0x33c8
+  __TEXT.__const: 0x23c8
+  __TEXT.__oslogstring: 0x1fd2
+  __TEXT.__cstring: 0x3d68
+  __TEXT.__gcc_except_tab: 0x11ec
+  __TEXT.__swift5_typeref: 0xd94
+  __TEXT.__swift5_fieldmd: 0x6f4
+  __TEXT.__constg_swiftt: 0xb10
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_reflstr: 0x40e
   __TEXT.__swift5_assocty: 0x1a0
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_proto: 0x190
-  __TEXT.__swift5_types: 0xbc
-  __TEXT.__swift5_capture: 0x4ec
+  __TEXT.__swift5_types: 0xd8
+  __TEXT.__swift5_capture: 0x530
   __TEXT.__swift_as_entry: 0x104
   __TEXT.__swift_as_ret: 0x16c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x24b0
+  __TEXT.__unwind_info: 0x2540
   __TEXT.__eh_frame: 0x3d3c
-  __TEXT.__objc_classname: 0xf0c
-  __TEXT.__objc_methname: 0x8eab
-  __TEXT.__objc_methtype: 0xb57
-  __TEXT.__objc_stubs: 0x74a0
-  __DATA_CONST.__got: 0xc00
+  __TEXT.__objc_classname: 0xef3
+  __TEXT.__objc_methname: 0x8f6c
+  __TEXT.__objc_methtype: 0xb5a
+  __TEXT.__objc_stubs: 0x7440
+  __DATA_CONST.__got: 0xc60
   __DATA_CONST.__const: 0x1be0
-  __DATA_CONST.__objc_classlist: 0x4b0
+  __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2390
+  __DATA_CONST.__objc_selrefs: 0x23d0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0xf18
-  __AUTH_CONST.__const: 0x1db0
-  __AUTH_CONST.__cfstring: 0x26a0
-  __AUTH_CONST.__objc_const: 0x77b8
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__auth_got: 0x1028
+  __AUTH_CONST.__const: 0x1ef0
+  __AUTH_CONST.__cfstring: 0x26e0
+  __AUTH_CONST.__objc_const: 0x7920
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xb10
-  __AUTH.__data: 0xa0
+  __AUTH.__objc_data: 0xf40
+  __AUTH.__data: 0x140
   __DATA.__objc_ivar: 0x220
-  __DATA.__data: 0x788
+  __DATA.__data: 0x7d8
   __DATA.__bss: 0x1ad0
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2a68
-  __DATA_DIRTY.__data: 0xc80
+  __DATA_DIRTY.__objc_data: 0x2af8
+  __DATA_DIRTY.__data: 0xd10
   __DATA_DIRTY.__bss: 0x15f0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/HomeKit.framework/HomeKit
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F68B9C9D-269B-3313-9247-E747C5F50DB6
-  Functions: 2652
-  Symbols:   5878
-  CStrings:  2703
+  UUID: D9D74FDC-1C32-3765-8B02-6A23494CCBB0
+  Functions: 2718
+  Symbols:   5920
+  CStrings:  2743
 
Symbols:
+ -[TPSTipsManager contentFromOrigin:systemEducationRequest:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]
+ _OBJC_CLASS_$_ASDSubscriptionEntitlement
+ _OBJC_CLASS_$_SupportFlowSessionProcessor
+ _OBJC_CLASS_$_TPSAppleArcadeSubscriptionValidation
+ _OBJC_CLASS_$_TPSAppleFitnessPlusSubscriptionValidation
+ _OBJC_CLASS_$_TPSAppleNewsPlusSubscriptionValidation
+ _OBJC_CLASS_$_TPSAppleSubscriptionValidation
+ _OBJC_CLASS_$_TPSAppleTVPlusSubscriptionValidation
+ _OBJC_METACLASS_$_SupportFlowSessionProcessor
+ _OBJC_METACLASS_$_TPSAppleArcadeSubscriptionValidation
+ _OBJC_METACLASS_$_TPSAppleFitnessPlusSubscriptionValidation
+ _OBJC_METACLASS_$_TPSAppleNewsPlusSubscriptionValidation
+ _OBJC_METACLASS_$_TPSAppleSubscriptionValidation
+ _OBJC_METACLASS_$_TPSAppleTVPlusSubscriptionValidation
+ __DATA_SupportFlowSessionProcessor
+ __DATA_TPSAppleArcadeSubscriptionValidation
+ __DATA_TPSAppleFitnessPlusSubscriptionValidation
+ __DATA_TPSAppleNewsPlusSubscriptionValidation
+ __DATA_TPSAppleSubscriptionValidation
+ __DATA_TPSAppleTVPlusSubscriptionValidation
+ __INSTANCE_METHODS_SupportFlowSessionProcessor
+ __INSTANCE_METHODS_TPSAppleArcadeSubscriptionValidation
+ __INSTANCE_METHODS_TPSAppleFitnessPlusSubscriptionValidation
+ __INSTANCE_METHODS_TPSAppleNewsPlusSubscriptionValidation
+ __INSTANCE_METHODS_TPSAppleSubscriptionValidation
+ __INSTANCE_METHODS_TPSAppleTVPlusSubscriptionValidation
+ __IVARS_TPSAppleSubscriptionValidation
+ __METACLASS_DATA_SupportFlowSessionProcessor
+ __METACLASS_DATA_TPSAppleArcadeSubscriptionValidation
+ __METACLASS_DATA_TPSAppleFitnessPlusSubscriptionValidation
+ __METACLASS_DATA_TPSAppleNewsPlusSubscriptionValidation
+ __METACLASS_DATA_TPSAppleSubscriptionValidation
+ __METACLASS_DATA_TPSAppleTVPlusSubscriptionValidation
+ ___212-[TPSTipsManager contentFromOrigin:systemEducationRequest:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke
+ ___212-[TPSTipsManager contentFromOrigin:systemEducationRequest:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_2
+ ___212-[TPSTipsManager contentFromOrigin:systemEducationRequest:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_3
+ ___212-[TPSTipsManager contentFromOrigin:systemEducationRequest:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_4
+ ___212-[TPSTipsManager contentFromOrigin:systemEducationRequest:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_5
+ ___212-[TPSTipsManager contentFromOrigin:systemEducationRequest:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_6
+ ___block_literal_global.290
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_TipsDaemon
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_TipsDaemon
+ _kTPSCapabilityAppleFitnessPlusSubscription
+ _kTPSCapabilityAppleNewsPlusSubscription
+ _kTPSCapabilityAppleTVPlusSubscription
+ _objc_msgSend$contentFromOrigin:systemEducationRequest:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic So27ASDSubscriptionEntitlementsC
+ _symbolic _____ 10TipsDaemon27AppleSubscriptionValidationC
+ _symbolic _____ 10TipsDaemon27SupportFlowSessionProcessorC
+ _symbolic _____ 10TipsDaemon33AppleArcadeSubscriptionValidationC
+ _symbolic _____ 10TipsDaemon36TPSAppleTVPlusSubscriptionValidationC
+ _symbolic _____ 10TipsDaemon38AppleFitnessPlusSubscriptionValidationC
+ _symbolic _____ 10TipsDaemon38TPSAppleNewsPlusSubscriptionValidationC
+ _symbolic _____ So34ASDSubscriptionEntitlementsSegmentV
+ _symbolic _____Sg 10Foundation12DateIntervalV
+ _symbolic _____Sg 15SupportFlowCore07ContactA6WindowO
+ _symbolic _____SgXw 10TipsDaemon27AppleSubscriptionValidationC
+ _symbolic _____SgXwz_Xx 10TipsDaemon27AppleSubscriptionValidationC
+ _symbolic _____y_____G s11_SetStorageC s5Int64V
- -[TPSAppleArcadeValidation validateWithCompletion:]
- -[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]
- _OBJC_CLASS_$_TPSAppleArcadeValidation
- _OBJC_METACLASS_$_TPSAppleArcadeValidation
- __OBJC_$_INSTANCE_METHODS_TPSAppleArcadeValidation
- __OBJC_CLASS_RO_$_TPSAppleArcadeValidation
- __OBJC_METACLASS_RO_$_TPSAppleArcadeValidation
- ___189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke
- ___189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_2
- ___189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_3
- ___189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_4
- ___189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_5
- ___189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_6
- ___51-[TPSAppleArcadeValidation validateWithCompletion:]_block_invoke
- ___51-[TPSAppleArcadeValidation validateWithCompletion:]_block_invoke.cold.1
- ___block_descriptor_64_e8_32s40bs48r56r_e32_v28?0"NSArray"8B16"NSError"20lr48l8s32l8s40l8r56l8
- ___block_literal_global.278
- _objc_msgSend$contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:
- _objc_msgSend$familyID
- _objc_msgSend$getSubscriptionEntitlementsForSegment:ignoreCaches:withResultHandler:
- _objc_msgSend$offerID
- _objc_retain_x7
CStrings:
+ " to process HMT lookback analytics. Time remaining: "
+ " with no userInfo"
+ ") is newer than longest require interval of ("
+ "?"
+ "AppleFitnessPlusSubscription"
+ "AppleNewsPlusSubscription"
+ "AppleTVPlusSubscription"
+ "Could not load OnDeviceSupportBrands.plist"
+ "Creating lookback event with abandon: "
+ "Failed to decode SupportFlowSession from userInfo: "
+ "Lookback multiplier: "
+ "No HMT sessions found to process lookback in interval: "
+ "OnDeviceSupportBrands"
+ "One day duration: "
+ "One hour duration: "
+ "One week duration: "
+ "Previous processed date: "
+ "Skipping lookback analysis - for session "
+ "TPSAppleArcadeSubscriptionValidation"
+ "TPSAppleFitnessPlusSubscriptionValidation"
+ "TPSAppleSubscriptionValidation"
+ "Threshold to process events: "
+ "TipsDaemon.AppleArcadeSubscriptionValidation"
+ "TipsDaemon.AppleFitnessPlusSubscriptionValidation"
+ "TipsDaemon.TPSAppleNewsPlusSubscriptionValidation"
+ "TipsDaemon.TPSAppleTVPlusSubscriptionValidation"
+ "Was not able to load support numbers from plist"
+ "com.apple.tipsd.supportFlow.session-processing"
+ "contentFromOrigin:systemEducationRequest:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:"
+ "eventBody"
+ "getSubscriptionEntitlementsForSegment:ignoreCaches:isBackground:requestingBundleId:withCacheInfoResultHandler:"
+ "inAppAdamID"
+ "init(targetContext:)"
+ "initWithContentsOfFile:"
+ "longLongValue"
+ "mainBundle"
+ "pathForResource:ofType:"
+ "performLookbackAnalysis"
+ "segment"
+ "subscriptionEntitlements"
+ "timestamp"
+ "update content from origin: %d systemEducationRequest: %d contextualEligibility:%d widgetEligibility:%d notificationEligibility: %d preferredNotificationIdentifiers: %@"
+ "v32@?0@\"NSArray\"8B16B20@\"NSError\"24"
+ "v64@0:8B16B20B24B28B32B36@40@?48@?56"
- "TPSAppleArcadeValidation"
- "contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:"
- "getSubscriptionEntitlementsForSegment:ignoreCaches:withResultHandler:"
- "update content from origin: %d contextualEligibility:%d widgetEligibility:%d notificationEligibility: %d preferredNotificationIdentifiers: %@"
- "v28@?0@\"NSArray\"8B16@\"NSError\"20"
- "v60@0:8B16B20B24B28B32@36@?44@?52"

```
