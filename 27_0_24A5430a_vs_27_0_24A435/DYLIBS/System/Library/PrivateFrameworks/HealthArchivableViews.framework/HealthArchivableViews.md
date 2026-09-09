## HealthArchivableViews

> `/System/Library/PrivateFrameworks/HealthArchivableViews.framework/HealthArchivableViews`

```diff

 7027.0.72.2.7
-  __TEXT.__text: 0x9eb0
-  __TEXT.__swift5_typeref: 0x2e0
-  __TEXT.__swift5_capture: 0x74
-  __TEXT.__swift5_reflstr: 0xab
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__const: 0x454
-  __TEXT.__constg_swiftt: 0x204
-  __TEXT.__swift5_fieldmd: 0x11c
-  __TEXT.__cstring: 0x1f4
-  __TEXT.__swift5_proto: 0x10
-  __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__text: 0x2a408
+  __TEXT.__objc_methlist: 0x4dc
+  __TEXT.__const: 0x1364
+  __TEXT.__gcc_except_tab: 0x7c
+  __TEXT.__cstring: 0x906
+  __TEXT.__oslogstring: 0x6f3
+  __TEXT.__swift5_typeref: 0x85e
+  __TEXT.__swift5_capture: 0x20c
+  __TEXT.__constg_swiftt: 0x5b0
+  __TEXT.__swift5_reflstr: 0x3f3
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__swift5_fieldmd: 0x3d0
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_proto: 0x7c
+  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_cont: 0x24
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__unwind_info: 0xae8
+  __TEXT.__eh_frame: 0x81c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x2f8
-  __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__auth_got: 0x5a0
-  __AUTH.__data: 0x228
-  __DATA.__data: 0x460
+  __DATA_CONST.__objc_selrefs: 0x438
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__got: 0x810
+  __AUTH_CONST.__const: 0xc58
+  __AUTH_CONST.__cfstring: 0x300
+  __AUTH_CONST.__objc_const: 0xb88
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0xe88
+  __AUTH.__objc_data: 0x378
+  __AUTH.__data: 0x438
+  __DATA.__objc_ivar: 0x60
+  __DATA.__data: 0xd58
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/Charts.framework/Charts
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI

   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/HealthUtilities.framework/HealthUtilities
   - /System/Library/PrivateFrameworks/HeartRateCoordinator.framework/HeartRateCoordinator
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 223
-  Symbols:   144
-  CStrings:  11
+  Functions: 916
+  Symbols:   711
+  CStrings:  105
 
Symbols:
+ +[HAVFakeHeartRateGenerator sharedGenerator]
+ +[HAVHeartRateDailyRangeTextProvider supportsSecureCoding]
+ +[HAVHeartRateTextProvider supportsSecureCoding]
+ +[_HAVHeartRateCoordinator sharedCoordinator]
+ -[HAVFakeHeartRateGenerator .cxx_destruct]
+ -[HAVFakeHeartRateGenerator _startIfNeeded]
+ -[HAVFakeHeartRateGenerator _stopTimer]
+ -[HAVFakeHeartRateGenerator _tick]
+ -[HAVFakeHeartRateGenerator addCallback:forOwner:]
+ -[HAVFakeHeartRateGenerator dealloc]
+ -[HAVFakeHeartRateGenerator init]
+ -[HAVFakeHeartRateGenerator recentHistoryForDuration:interval:]
+ -[HAVFakeHeartRateGenerator removeCallbackForOwner:]
+ -[HAVHeartRateDailyRangeTextProvider .cxx_destruct]
+ -[HAVHeartRateDailyRangeTextProvider _endSession]
+ -[HAVHeartRateDailyRangeTextProvider _sessionAttributedTextForIndex:withStyle:]
+ -[HAVHeartRateDailyRangeTextProvider _sessionCacheKey]
+ -[HAVHeartRateDailyRangeTextProvider _startSessionWithDate:]
+ -[HAVHeartRateDailyRangeTextProvider _updateFrequency]
+ -[HAVHeartRateDailyRangeTextProvider _validate]
+ -[HAVHeartRateDailyRangeTextProvider accessibilityLabel]
+ -[HAVHeartRateDailyRangeTextProvider commonInitWithPlaceholder:]
+ -[HAVHeartRateDailyRangeTextProvider encodeWithCoder:]
+ -[HAVHeartRateDailyRangeTextProvider fetchHistoricalRange]
+ -[HAVHeartRateDailyRangeTextProvider heartRateCoordinatorDidUpdateHeartRate:]
+ -[HAVHeartRateDailyRangeTextProvider initPrivate]
+ -[HAVHeartRateDailyRangeTextProvider initWithCoder:]
+ -[HAVHeartRateDailyRangeTextProvider initWithPlaceholder:]
+ -[HAVHeartRateTextProvider .cxx_destruct]
+ -[HAVHeartRateTextProvider _endSession]
+ -[HAVHeartRateTextProvider _initWithJSONObjectRepresentation:]
+ -[HAVHeartRateTextProvider _relativeStaleTimeAttributedStringWithStyle:dateStyle:timestamp:]
+ -[HAVHeartRateTextProvider _sessionAttributedTextForIndex:withStyle:]
+ -[HAVHeartRateTextProvider _sessionCacheKey]
+ -[HAVHeartRateTextProvider _startSessionWithDate:]
+ -[HAVHeartRateTextProvider _updateFrequency]
+ -[HAVHeartRateTextProvider _validate]
+ -[HAVHeartRateTextProvider accessibilityLabel]
+ -[HAVHeartRateTextProvider dealloc]
+ -[HAVHeartRateTextProvider encodeWithCoder:]
+ -[HAVHeartRateTextProvider heartRateCoordinatorDidUpdateHeartRate:]
+ -[HAVHeartRateTextProvider initPrivate]
+ -[HAVHeartRateTextProvider initWithCoder:]
+ -[HAVHeartRateTextProvider initWithShowsBPMSuffix:fontWeight:isPlaceholder:]
+ -[HAVHeartRateTextProvider init]
+ -[_HAVHeartRateCoordinator .cxx_destruct]
+ -[_HAVHeartRateCoordinator _applyHeartRateData:]
+ -[_HAVHeartRateCoordinator _notifyConsumers]
+ -[_HAVHeartRateCoordinator _registerConsumerOnMain:]
+ -[_HAVHeartRateCoordinator _scheduleNextStaleUpdate]
+ -[_HAVHeartRateCoordinator _switchDataSource:]
+ -[_HAVHeartRateCoordinator cachedHeartRate]
+ -[_HAVHeartRateCoordinator dealloc]
+ -[_HAVHeartRateCoordinator handleFilteredHeartRate:]
+ -[_HAVHeartRateCoordinator handleMostRecentHighConfidenceHeartRate:]
+ -[_HAVHeartRateCoordinator init]
+ -[_HAVHeartRateCoordinator isStale]
+ -[_HAVHeartRateCoordinator lastHeartRateTimestamp]
+ -[_HAVHeartRateCoordinator registerConsumer:]
+ GCC_except_table15
+ GCC_except_table2
+ GCC_except_table5
+ GCC_except_table6
+ _CLKRelativeDateStyleRelative
+ _CLKRelativeDateStyleRelativeShort
+ _CTFontHasExuberatedLineHeight
+ _HKLogHeartRateCategory
+ _HKQuantityTypeIdentifierHeartRate
+ _NSFontAttributeName
+ _NSForegroundColorAttributeName
+ _NSStringFromClass
+ _OBJC_CLASS_$_CLKDevice
+ _OBJC_CLASS_$_CLKDeviceMetrics
+ _OBJC_CLASS_$_CLKFont
+ _OBJC_CLASS_$_CLKRelativeDateTextProvider
+ _OBJC_CLASS_$_CLKTextProvider
+ _OBJC_CLASS_$_HAVFakeHeartRateGenerator
+ _OBJC_CLASS_$_HAVHeartRateDailyRangeTextProvider
+ _OBJC_CLASS_$_HAVHeartRateTextProvider
+ _OBJC_CLASS_$_HKHealthStore
+ _OBJC_CLASS_$_HKHeartRateSummaryQuery
+ _OBJC_CLASS_$_HKQuantityType
+ _OBJC_CLASS_$_HKQuery
+ _OBJC_CLASS_$_HKStatisticsQuery
+ _OBJC_CLASS_$_HKUnit
+ _OBJC_CLASS_$_HRCHeartRateData
+ _OBJC_CLASS_$_HRCHeartRateRequestor
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_UIGraphicsImageRenderer
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$__HAVHeartRateCoordinator
+ _OBJC_CLASS_$__TtC21HealthArchivableViews21LiveHeartRateReceiver
+ _OBJC_CLASS_$__TtC21HealthArchivableViews37HAVHeartRateObservableBoolUserDefault
+ _OBJC_IVAR_$_HAVFakeHeartRateGenerator._callbacks
+ _OBJC_IVAR_$_HAVFakeHeartRateGenerator._currentBPM
+ _OBJC_IVAR_$_HAVFakeHeartRateGenerator._timer
+ _OBJC_IVAR_$_HAVHeartRateDailyRangeTextProvider._bundle
+ _OBJC_IVAR_$_HAVHeartRateDailyRangeTextProvider._fontSize
+ _OBJC_IVAR_$_HAVHeartRateDailyRangeTextProvider._hasRange
+ _OBJC_IVAR_$_HAVHeartRateDailyRangeTextProvider._healthStore
+ _OBJC_IVAR_$_HAVHeartRateDailyRangeTextProvider._isPlaceholder
+ _OBJC_IVAR_$_HAVHeartRateDailyRangeTextProvider._maximumBPM
+ _OBJC_IVAR_$_HAVHeartRateDailyRangeTextProvider._minimumBPM
+ _OBJC_IVAR_$_HAVHeartRateTextProvider._bundle
+ _OBJC_IVAR_$_HAVHeartRateTextProvider._fontSize
+ _OBJC_IVAR_$_HAVHeartRateTextProvider._fontWeight
+ _OBJC_IVAR_$_HAVHeartRateTextProvider._hasCustomFontWeight
+ _OBJC_IVAR_$_HAVHeartRateTextProvider._isPlaceholder
+ _OBJC_IVAR_$_HAVHeartRateTextProvider._showsBPMSuffix
+ _OBJC_IVAR_$__HAVHeartRateCoordinator._cachedHeartRate
+ _OBJC_IVAR_$__HAVHeartRateCoordinator._consumers
+ _OBJC_IVAR_$__HAVHeartRateCoordinator._fakeHeartRatesPreferenceObserver
+ _OBJC_IVAR_$__HAVHeartRateCoordinator._hasConfiguredDataSource
+ _OBJC_IVAR_$__HAVHeartRateCoordinator._heartRateRequestor
+ _OBJC_IVAR_$__HAVHeartRateCoordinator._lastHeartRateTimestamp
+ _OBJC_IVAR_$__HAVHeartRateCoordinator._staleUpdateTimer
+ _OBJC_IVAR_$__HAVHeartRateCoordinator._usingFakeData
+ _OBJC_METACLASS_$_CLKTextProvider
+ _OBJC_METACLASS_$_HAVFakeHeartRateGenerator
+ _OBJC_METACLASS_$_HAVHeartRateDailyRangeTextProvider
+ _OBJC_METACLASS_$_HAVHeartRateTextProvider
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$__HAVHeartRateCoordinator
+ _OBJC_METACLASS_$__TtC21HealthArchivableViews21LiveHeartRateReceiver
+ _OBJC_METACLASS_$__TtC21HealthArchivableViews37HAVHeartRateObservableBoolUserDefault
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _UIFontWeightRegular
+ _UIFontWeightSemibold
+ __Block_copy
+ __Block_release
+ __DATA__TtC21HealthArchivableViews21LiveHeartRateReceiver
+ __DATA__TtC21HealthArchivableViews25LiveHeartRateSummaryCache
+ __DATA__TtC21HealthArchivableViews37HAVHeartRateObservableBoolUserDefault
+ __HKCacheIndexFromDate
+ __HKInitializeLogging
+ __INSTANCE_METHODS__TtC21HealthArchivableViews21LiveHeartRateReceiver
+ __INSTANCE_METHODS__TtC21HealthArchivableViews37HAVHeartRateObservableBoolUserDefault
+ __IVARS__TtC21HealthArchivableViews21LiveHeartRateReceiver
+ __IVARS__TtC21HealthArchivableViews25LiveHeartRateSummaryCache
+ __IVARS__TtC21HealthArchivableViews37HAVHeartRateObservableBoolUserDefault
+ __METACLASS_DATA__TtC21HealthArchivableViews21LiveHeartRateReceiver
+ __METACLASS_DATA__TtC21HealthArchivableViews25LiveHeartRateSummaryCache
+ __METACLASS_DATA__TtC21HealthArchivableViews37HAVHeartRateObservableBoolUserDefault
+ __MergedGlobals
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_HAVFakeHeartRateGenerator
+ __OBJC_$_CLASS_METHODS_HAVHeartRateDailyRangeTextProvider
+ __OBJC_$_CLASS_METHODS_HAVHeartRateTextProvider
+ __OBJC_$_CLASS_METHODS__HAVHeartRateCoordinator
+ __OBJC_$_CLASS_PROP_LIST__HAVHeartRateCoordinator
+ __OBJC_$_INSTANCE_METHODS_HAVFakeHeartRateGenerator
+ __OBJC_$_INSTANCE_METHODS_HAVHeartRateDailyRangeTextProvider
+ __OBJC_$_INSTANCE_METHODS_HAVHeartRateTextProvider
+ __OBJC_$_INSTANCE_METHODS__HAVHeartRateCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_HAVFakeHeartRateGenerator
+ __OBJC_$_INSTANCE_VARIABLES_HAVHeartRateDailyRangeTextProvider
+ __OBJC_$_INSTANCE_VARIABLES_HAVHeartRateTextProvider
+ __OBJC_$_INSTANCE_VARIABLES__HAVHeartRateCoordinator
+ __OBJC_$_PROP_LIST_HAVHeartRateDailyRangeTextProvider
+ __OBJC_$_PROP_LIST_HAVHeartRateTextProvider
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST__HAVHeartRateCoordinator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HRCHeartRateOutputDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__HAVHeartRateConsumer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HRCHeartRateOutputDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES__HAVHeartRateConsumer
+ __OBJC_$_PROTOCOL_REFS_HRCHeartRateOutputDelegate
+ __OBJC_$_PROTOCOL_REFS__HAVHeartRateConsumer
+ __OBJC_CLASS_PROTOCOLS_$_HAVHeartRateDailyRangeTextProvider
+ __OBJC_CLASS_PROTOCOLS_$_HAVHeartRateTextProvider
+ __OBJC_CLASS_PROTOCOLS_$__HAVHeartRateCoordinator
+ __OBJC_CLASS_RO_$_HAVFakeHeartRateGenerator
+ __OBJC_CLASS_RO_$_HAVHeartRateDailyRangeTextProvider
+ __OBJC_CLASS_RO_$_HAVHeartRateTextProvider
+ __OBJC_CLASS_RO_$__HAVHeartRateCoordinator
+ __OBJC_LABEL_PROTOCOL_$_HRCHeartRateOutputDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$__HAVHeartRateConsumer
+ __OBJC_METACLASS_RO_$_HAVFakeHeartRateGenerator
+ __OBJC_METACLASS_RO_$_HAVHeartRateDailyRangeTextProvider
+ __OBJC_METACLASS_RO_$_HAVHeartRateTextProvider
+ __OBJC_METACLASS_RO_$__HAVHeartRateCoordinator
+ __OBJC_PROTOCOL_$_HRCHeartRateOutputDelegate
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$__HAVHeartRateConsumer
+ __PROTOCOLS__TtC21HealthArchivableViews21LiveHeartRateReceiver
+ __Unwind_Resume
+ ___32-[_HAVHeartRateCoordinator init]_block_invoke
+ ___32-[_HAVHeartRateCoordinator init]_block_invoke_2
+ ___43-[HAVFakeHeartRateGenerator _startIfNeeded]_block_invoke
+ ___44+[HAVFakeHeartRateGenerator sharedGenerator]_block_invoke
+ ___45+[_HAVHeartRateCoordinator sharedCoordinator]_block_invoke
+ ___45-[_HAVHeartRateCoordinator registerConsumer:]_block_invoke
+ ___46-[_HAVHeartRateCoordinator _switchDataSource:]_block_invoke
+ ___52-[_HAVHeartRateCoordinator _scheduleNextStaleUpdate]_block_invoke
+ ___58-[HAVHeartRateDailyRangeTextProvider fetchHistoricalRange]_block_invoke
+ ___CFConstantStringClassReference
+ ___NSArray0__struct
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e56_v32?0"HKStatisticsQuery"8"HKStatistics"16"NSError"24ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8lw32l8
+ ___block_descriptor_40_e8_32w_e19_v24?0d8"NSDate"16lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global
+ ___isPlatformVersionAtLeast
+ ___objc_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift__destructor
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_memcpy16_8
+ ___swift_memcpy17_8
+ ___swift_memcpy25_8
+ ___swift_memcpy50_8
+ ___swift_mutable_project_boxed_opaque_existential_1
+ ___swift_project_boxed_opaque_existential_1
+ __availability_version_check
+ __dispatch_main_q
+ __initializeAvailabilityCheck
+ __os_log_error_impl
+ __os_log_impl
+ __swiftImmortalRefCount
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _arc4random_uniform
+ _associated conformance 21HealthArchivableViews35LiveHeartRateComplicationCornerViewV7SwiftUI0I0AA4BodyAdEP_AdE
+ _associated conformance 21HealthArchivableViews35LiveHeartRateComplicationInlineViewV7SwiftUI0I0AA4BodyAdEP_AdE
+ _associated conformance 21HealthArchivableViews37LiveHeartRateComplicationCircularViewV10CodingKeys33_2F0179CF772F80582CDEB846138D09F9LLOSHAASQ
+ _associated conformance 21HealthArchivableViews37LiveHeartRateComplicationCircularViewV10CodingKeys33_2F0179CF772F80582CDEB846138D09F9LLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 21HealthArchivableViews37LiveHeartRateComplicationCircularViewV10CodingKeys33_2F0179CF772F80582CDEB846138D09F9LLOs0J3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 21HealthArchivableViews37LiveHeartRateComplicationCircularViewV7SwiftUI01_bI0AASE
+ _associated conformance 21HealthArchivableViews37LiveHeartRateComplicationCircularViewV7SwiftUI01_bI0AASe
+ _associated conformance 21HealthArchivableViews37LiveHeartRateComplicationCircularViewV7SwiftUI01_bI0AaD0I0
+ _associated conformance 21HealthArchivableViews37LiveHeartRateComplicationCircularViewV7SwiftUI0I0AA4BodyAdEP_AdE
+ _associated conformance 21HealthArchivableViews40LiveHeartRateComplicationRectangularViewV10CodingKeys33_A1BB28541FED4F6554BE5AC996FE1815LLOSHAASQ
+ _associated conformance 21HealthArchivableViews40LiveHeartRateComplicationRectangularViewV10CodingKeys33_A1BB28541FED4F6554BE5AC996FE1815LLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 21HealthArchivableViews40LiveHeartRateComplicationRectangularViewV10CodingKeys33_A1BB28541FED4F6554BE5AC996FE1815LLOs0J3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 21HealthArchivableViews40LiveHeartRateComplicationRectangularViewV7SwiftUI01_bI0AASE
+ _associated conformance 21HealthArchivableViews40LiveHeartRateComplicationRectangularViewV7SwiftUI01_bI0AASe
+ _associated conformance 21HealthArchivableViews40LiveHeartRateComplicationRectangularViewV7SwiftUI01_bI0AaD0I0
+ _associated conformance 21HealthArchivableViews40LiveHeartRateComplicationRectangularViewV7SwiftUI0I0AA4BodyAdEP_AdE
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _compatibilityInitializeAvailabilityCheck
+ _dispatch_async
+ _dispatch_once
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fmod
+ _fopen
+ _fread
+ _free
+ _fseek
+ _ftell
+ _get_enum_tag_for_layout_string 7SwiftUI11EnvironmentV7ContentOy12CoreGraphics7CGFloatV_G
+ _get_enum_tag_for_layout_string 7SwiftUI11EnvironmentV7ContentOySb_G
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOQr
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOqd__AaBHC
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA4ViewPAAE10unredactedQryFQOyAA6VStackVyAA05TupleD0VyAA08ModifiedD0VyAA4TextVAA12_FrameLayoutVG_ALyALy21HealthArchivableViews25HeartRateRectangularChartVyAR0pq5BasicS0VGAA05_FlexkL0VGAA31AccessibilityAttachmentModifierVGQPGG_Qo_AeAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAeAE16privacySensitiveyQrSbFQOyAHyAJyALyAR0pqr6HeaderE0VAPG_AeAE27accessibilityRepresentation14representationQrqd__yXE_tAaDRd__lFQOyALyAA5GroupVyACyALyATy6Charts07BuilderH0VyAV_A19_0sD0PA19_E6symbolA24_Qrqd__yXE_tAaDRd__lFQOyA23_A19_E6zIndexyQrSdFQOyA19_9PointMarkV_Qo__ACyAA6ZStackVyAJyALyAA06_ShapeE0VyAA6CircleVAA5ColorVGAPG_A38_QPGGA30_yAJyALyALyA34_AA016_ForegroundStyleX0VyA36_GGAPG_ALyALyA37_AA16_BlendModeEffectVGAPGQPGGGQo_SgQPGGAA010_AnimationX0VySdSgGGAWGGAYG_AR0pqS16AXRepresentationVQo_QPGG_Qo__Qo_GAaDHPqd__AaDHD2_A4_HO_qd__AaDHD2_A71_HOHC
+ _get_witness_table qd0__7SwiftUI4ViewHD3_AaBP9WidgetKitE11widgetLabel5labelQrqd__yXE_tAaBRd__lFQOyAA5GroupVyAA19_ConditionalContentVyAcDE0f6CurvesK0yQrSbFQOyAA4TextV_Qo_ANGG_AJyA2MGQo_HO
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBP9WidgetKitE16widgetAccentableyQrSbFQOyAA5LabelVyAA19_ConditionalContentVyAA4TextVAKGAA5ImageVG_Qo_HO
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA15ModifiedContentVyAKyAcAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyAA6ZStackVyAA05TupleJ0Vy9WidgetKit09AccessoryS10BackgroundV_AA012_ConditionalJ0VyAA6VStackVyASyAKyAA4TextVAA14_PaddingLayoutVG_AcAE16privacySensitiveyQrSbFQOyAKyAKyA0_AA18_AnimationModifierVySdGGA2_G_Qo_AcAEA4_yQrSbFQOyA0__Qo_QPGGAcAE10unredactedQryFQOyAKyAKyAcTE16widgetAccentableyQrSbFQOyAA5ImageV_Qo_AA18_AspectRatioLayoutVGA2_G_Qo_GQPGG_Qo_AA0N18AttachmentModifierVGAA12_FrameLayoutVG_Qo_HO
+ _initializeAvailabilityCheck
+ _kHKHASharedUserDefaultsIdentifier
+ _kHKInternalSettingsKeyFakeLiveHeartRates
+ _malloc
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_alloc
+ _objc_allocWithZone
+ _objc_alloc_init
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_applyHeartRateData:
+ _objc_msgSend$_attributedStringWithOtherAttributesFromStyle:
+ _objc_msgSend$_notifyConsumers
+ _objc_msgSend$_registerConsumerOnMain:
+ _objc_msgSend$_relativeStaleTimeAttributedStringWithStyle:dateStyle:timestamp:
+ _objc_msgSend$_scheduleNextStaleUpdate
+ _objc_msgSend$_sessionAttributedTextForIndex:withStyle:
+ _objc_msgSend$_startIfNeeded
+ _objc_msgSend$_startSessionWithDate:
+ _objc_msgSend$_stopTimer
+ _objc_msgSend$_switchDataSource:
+ _objc_msgSend$_tick
+ _objc_msgSend$_update
+ _objc_msgSend$activityCacheIndex
+ _objc_msgSend$addAttribute:value:range:
+ _objc_msgSend$addCallback:forOwner:
+ _objc_msgSend$addObject:
+ _objc_msgSend$allDayStatistics
+ _objc_msgSend$allObjects
+ _objc_msgSend$allValues
+ _objc_msgSend$appendAttributedString:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$cachedHeartRate
+ _objc_msgSend$confidenceLevel
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$countUnit
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$currentDevice
+ _objc_msgSend$date
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$doubleValueForUnit:
+ _objc_msgSend$drawInRect:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$executeQuery:
+ _objc_msgSend$hashTableWithOptions:
+ _objc_msgSend$heartRate
+ _objc_msgSend$heartRateCoordinatorDidUpdateHeartRate:
+ _objc_msgSend$imageNamed:inBundle:compatibleWithTraitCollection:
+ _objc_msgSend$imageWithActions:
+ _objc_msgSend$init
+ _objc_msgSend$initPrivate
+ _objc_msgSend$initWithDelegate:onQueue:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithPlaceholder:
+ _objc_msgSend$initWithQuantityType:quantitySamplePredicate:options:completionHandler:
+ _objc_msgSend$initWithShowsBPMSuffix:fontWeight:isPlaceholder:
+ _objc_msgSend$initWithSize:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$initWithString:attributes:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithSuiteName:key:defaultValue:onChange:
+ _objc_msgSend$initWithUpdateHandler:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isMainThread
+ _objc_msgSend$isStale
+ _objc_msgSend$lastHeartRateTimestamp
+ _objc_msgSend$length
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$maximumQuantity
+ _objc_msgSend$metricsWithDevice:identitySizeClass:
+ _objc_msgSend$minimumQuantity
+ _objc_msgSend$minuteUnit
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$opportunisticUpdatesEnabled
+ _objc_msgSend$predicateForSamplesWithStartDate:endDate:options:
+ _objc_msgSend$quantityTypeForIdentifier:
+ _objc_msgSend$recentHistoryForDuration:interval:
+ _objc_msgSend$registerConsumer:
+ _objc_msgSend$removeCallbackForOwner:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$scaledValue:
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setOpportunisticUpdatesEnabled:
+ _objc_msgSend$sharedCoordinator
+ _objc_msgSend$sharedGenerator
+ _objc_msgSend$startOfDayForDate:
+ _objc_msgSend$stopQuery:
+ _objc_msgSend$stringValue
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$systemFontOfSize:weight:
+ _objc_msgSend$systemRedColor
+ _objc_msgSend$textProviderWithDate:style:units:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$timestamp
+ _objc_msgSend$unitDividedByUnit:
+ _objc_msgSend$valueWithNonretainedObject:
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_release
+ _objc_release_x1
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_retain_x9
+ _objc_storeStrong
+ _os_log_type_enabled
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _rewind
+ _sharedCoordinator.onceToken
+ _sharedCoordinator.shared
+ _sharedGenerator.onceToken
+ _sharedGenerator.shared
+ _sscanf
+ _swift_allocBox
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease_n
+ _swift_coroFrameAlloc
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getAtKeyPath
+ _swift_getEnumCaseMultiPayload
+ _swift_getForeignTypeMetadata
+ _swift_getMetatypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjectType
+ _swift_getTupleTypeMetadata3
+ _swift_isEscapingClosureAtFileLocation
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_makeBoxUnique
+ _swift_once
+ _swift_release_x19
+ _swift_release_x24
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x9
+ _swift_retain_n
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x26
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_getMainExecutor
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _symbolic $s21HealthArchivableViews19HeartRateContainingP
+ _symbolic $s21HealthArchivableViews19HeartRateRequestingP
+ _symbolic $sSY
+ _symbolic SS
+ _symbolic SbIeghy_
+ _symbolic SbSg
+ _symbolic ScA_pSg
+ _symbolic ScTyyt_____GSg s5NeverO
+ _symbolic SdSg
+ _symbolic So13HKHealthStoreC
+ _symbolic So23HKHeartRateSummaryQueryC
+ _symbolic So30UIGraphicsImageRendererContextCIgg_
+ _symbolic So7NSTimerCSg
+ _symbolic So7UIImageC
+ _symbolic So8NSObjectC
+ _symbolic _____ 10Foundation8CalendarV
+ _symbolic _____ 11Observation0A9RegistrarV
+ _symbolic _____ 21HealthArchivableViews21DatedHeartRateSummaryV
+ _symbolic _____ 21HealthArchivableViews21LiveHeartRateReceiverC
+ _symbolic _____ 21HealthArchivableViews22HAVHeartRateFakeSourceO
+ _symbolic _____ 21HealthArchivableViews25LiveHeartRateSummaryCacheC
+ _symbolic _____ 21HealthArchivableViews35LiveHeartRateComplicationCornerViewV
+ _symbolic _____ 21HealthArchivableViews35LiveHeartRateComplicationInlineViewV
+ _symbolic _____ 21HealthArchivableViews37HAVHeartRateObservableBoolUserDefaultC
+ _symbolic _____ 21HealthArchivableViews37LiveHeartRateComplicationCircularViewV
+ _symbolic _____ 21HealthArchivableViews37LiveHeartRateComplicationCircularViewV10CodingKeys33_2F0179CF772F80582CDEB846138D09F9LLO
+ _symbolic _____ 21HealthArchivableViews40LiveHeartRateComplicationRectangularViewV
+ _symbolic _____ 21HealthArchivableViews40LiveHeartRateComplicationRectangularViewV10CodingKeys33_A1BB28541FED4F6554BE5AC996FE1815LLO
+ _symbolic _____ 2os6LoggerV
+ _symbolic _____ 7SwiftUI16RedactionReasonsV
+ _symbolic _____ 7SwiftUI5ImageV
+ _symbolic _____ 9WidgetKit0A13RenderingModeV
+ _symbolic _____ So18HRCConfidenceLevelV
+ _symbolic _____ So6CGSizeV
+ _symbolic _____ s5Int64V
+ _symbolic _____ s5UInt8V
+ _symbolic _____IeyBhy_ 10ObjectiveC8ObjCBoolV
+ _symbolic _____SgXw 21HealthArchivableViews21LiveHeartRateReceiverC
+ _symbolic _____SgXwz_Xx 21HealthArchivableViews21LiveHeartRateReceiverC
+ _symbolic ______pSg 21HealthArchivableViews19HeartRateRequestingP
+ _symbolic _____ySbG 15HealthUtilities21ObservableUserDefaultC
+ _symbolic _____ySbG 7SwiftUI11EnvironmentV
+ _symbolic _____ySbGSg 15HealthUtilities21ObservableUserDefaultC
+ _symbolic _____y_____G 7SwiftUI11EnvironmentV 10Foundation8CalendarV
+ _symbolic _____y_____G 7SwiftUI11EnvironmentV 12CoreGraphics7CGFloatV
+ _symbolic _____y_____G 7SwiftUI11EnvironmentV 9WidgetKit0D13RenderingModeV
+ _symbolic _____y_____G 7SwiftUI11EnvironmentV AA16RedactionReasonsV
+ _symbolic _____y_____SgG 15Synchronization5MutexVAARi_zrlE 21HealthArchivableViews21DatedHeartRateSummaryV
+ _symbolic _____y_____SgG 7SwiftUI5StateV 21HealthArchivableViews21LiveHeartRateReceiverC
+ _symbolic _____y_____SgG 7SwiftUI9LazyStateV 21HealthArchivableViews21LiveHeartRateReceiverC
+ _symbolic _____y_____SgG 7SwiftUI9LazyStateV 9HealthKit19HeartRateDaySummaryV
+ _symbolic _____y_____Sg_G ScS12ContinuationV 21HealthArchivableViews21DatedHeartRateSummaryV
+ _symbolic _____y_____yAAy_____y_____y_____y___________y_____yACyAAy__________G______yAAyAAyAG_____ySdGGAHG_Qo______yAG_Qo_QPGG_____yAAyAAy_____y______Qo______GAHG_Qo_GQPGG_Qo______G_____G_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV AcAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQO AA6ZStackV AA05TupleJ0V 9WidgetKit09AccessoryS10BackgroundV AA012_ConditionalJ0V AA6VStackV AA4TextV AA14_PaddingLayoutV AcAE16privacySensitiveyQrSbFQO AA18_AnimationModifierV AcAEA3_yQrSbFQO AcAE10unredactedQryFQO AcTE16widgetAccentableyQrSbFQO AA5ImageV AA18_AspectRatioLayoutV AA0N18AttachmentModifierV AA12_FrameLayoutV
+ _symbolic _____y_____y_____y_____ACG_____G_Qo_ 7SwiftUI4ViewP9WidgetKitE16widgetAccentableyQrSbFQO AA5LabelV AA19_ConditionalContentV AA4TextV AA5ImageV
+ _symbolic _____y_____y_____y_____y______Qo_ADGG_AByA2CGQo_ 7SwiftUI4ViewP9WidgetKitE11widgetLabel5labelQrqd__yXE_tAaBRd__lFQO AA5GroupV AA19_ConditionalContentV AcDE0f6CurvesK0yQrSbFQO AA4TextV
+ _symbolic _____y_____y_____y_____y_____y__________G_ADyADy_____y_____G_____G_____GQPGG_Qo______y_____yAByACyADy_____AFG______yADy_____yAAyADyAHy_____yAI______y_____y______Qo__AAy_____yACyADy_____y__________GAFG_A1_QPGGAXyACyADyADyAZ_____yA_GGAFG_ADyADyA0______GAFGQPGGGQo_SgQPGG_____ySdSgGGAJGGAKG______Qo_QPGG_Qo__Qo_G 7SwiftUI19_ConditionalContentV AA4ViewPAAE10unredactedQryFQO AA6VStackV AA05TupleD0V AA08ModifiedD0V AA4TextV AA12_FrameLayoutV 21HealthArchivableViews25HeartRateRectangularChartV AQ0pq5BasicS0V AA05_FlexkL0V AA31AccessibilityAttachmentModifierV AeAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AeAE16privacySensitiveyQrSbFQO AQ0pqr6HeaderE0V AeAE27accessibilityRepresentation14representationQrqd__yXE_tAaDRd__lFQO AA5GroupV 6Charts07BuilderH0V A11_0sD0PA11_E6symbolA16_Qrqd__yXE_tAaDRd__lFQO A15_A11_E6zIndexyQrSdFQO A11_9PointMarkV AA6ZStackV AA06_ShapeE0V AA6CircleV AA5ColorV AA016_ForegroundStyleX0V AA16_BlendModeEffectV AA010_AnimationX0V AQ0pqS16AXRepresentationV
+ _symbolic ytIeAgHr_
+ _symbolic yt______pIgrzo_ s5ErrorP
+ _type_layout_string 21HealthArchivableViews35LiveHeartRateComplicationCornerViewV
+ _type_layout_string 21HealthArchivableViews35LiveHeartRateComplicationInlineViewV
+ _type_layout_string 21HealthArchivableViews37LiveHeartRateComplicationCircularViewV
+ _type_layout_string So6CGSizeV
CStrings:
+ ""
+ "%.0f"
+ "%.0f-%.0f"
+ "%@-stale-h-%ld"
+ "%@-stale-m-%ld"
+ "%d.%d.%d"
+ ", "
+ "-"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "1"
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "Complication - Circular"
+ "Complication - Extra Large"
+ "Complication - Utilitarian - Small"
+ "Fatal error"
+ "HEART_RATE_AX_NO_DATA"
+ "HEART_RATE_AX_READING"
+ "HEART_RATE_DAILY_RANGE"
+ "HEART_RATE_DAILY_RANGE_AX_READING"
+ "HEART_RATE_ICON_VALUE"
+ "HEART_RATE_READING"
+ "HEART_RATE_TITLE"
+ "HealthArchivableViews.HAVHeartRateObservableBoolUserDefault"
+ "HealthArchivableViews/LiveHeartRateComplicationCircularView.swift"
+ "HealthArchivableViews/LiveHeartRateComplicationCornerView.swift"
+ "HealthArchivableViews/LiveHeartRateComplicationInlineView.swift"
+ "HealthArchivableViews/LiveHeartRateComplicationRectangularView.swift"
+ "HealthArchivableViews/LiveHeartRateReceiver.swift"
+ "Heart rate summary query error: %{public}@"
+ "Incorrect actor executor assumption; Expected same executor as "
+ "LiveHeartRateComplication"
+ "LiveHeartRateComplicationRectangular"
+ "Localizable-LiveHeartRateComplications"
+ "NO_BPM"
+ "ProductVersion"
+ "RedactionReasons"
+ "View.task @ HealthArchivableViews/LiveHeartRateComplicationCircularView.swift:"
+ "View.task @ HealthArchivableViews/LiveHeartRateComplicationRectangularView.swift:"
+ "WidgetRenderingMode"
+ "[%{public}@] Historical range fetch failed: %{public}@"
+ "[%{public}@] Historical range — min: %{private}.0f, max: %{private}.0f"
+ "[%{public}@] Live update — min: %{private}.0f, max: %{private}.0f"
+ "[%{public}@] Starting with initial BPM: %{public}.0f"
+ "[%{public}@] Synthesized %{public}lu backfill samples over %{public}.0fs ending at %{public}.0f BPM"
+ "[%{public}@] Tick: %{public}.0f BPM"
+ "[%{public}@] _endSession"
+ "[%{public}@] _startSession"
+ "[%{public}@] commonInit"
+ "[%{public}@] commonInit (placeholder)"
+ "[%{public}@] dealloc"
+ "[%{public}s] Initialized with HeartRateRequesting-conformed object"
+ "[%{public}s] Initialized, observing fake heart rate preference"
+ "[%{public}s] Received heart rate: %{private}f BPM, confidence: %{private}s. Filtering out low-confidence sample."
+ "[%{public}s] Received heart rate: %{private}f BPM, confidence: %{private}s. Will update receiver with this value."
+ "[%{public}s] Switched to fake heart rate generator"
+ "[%{public}s] Switched to heart rate requestor"
+ "[%{public}s] handleFilteredHeartRate called!"
+ "[%{public}s] handleMostRecentHighConfidenceHeartRate called!"
+ "[%{public}s] updateReceiver received nil heart rate data, not updating receiver."
+ "[_HAVHeartRateCoordinator] Filtering out low-confidence sample."
+ "[_HAVHeartRateCoordinator] applied heart rate %{private}.0f BPM, elapsed: %.1fs, isStale: %d"
+ "[_HAVHeartRateCoordinator] registered consumer %p (now %lu live)"
+ "[_HAVHeartRateCoordinator] switched to fake heart rate generator"
+ "[_HAVHeartRateCoordinator] switched to heart rate requestor"
+ "bpm"
+ "bpm timestamp "
+ "com.apple.Health"
+ "fontWeight"
+ "hasCustomFontWeight"
+ "init()"
+ "isPlaceholder"
+ "isPreview"
+ "kCFAllocatorNull"
+ "no_data"
+ "placeholder"
+ "q"
+ "r"
+ "showsBPMSuffix"
+ "stale_no_data"
+ "timestamp"
+ "v12@?0B8"
+ "v16@?0@\"NSTimer\"8"
+ "v24@?0d8@\"NSDate\"16"
+ "v32@?0@\"HKStatisticsQuery\"8@\"HKStatistics\"16@\"NSError\"24"
+ "v8@?0"
```
