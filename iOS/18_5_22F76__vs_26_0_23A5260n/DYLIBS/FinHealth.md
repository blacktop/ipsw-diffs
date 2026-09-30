## FinHealth

> `/System/Library/PrivateFrameworks/FinHealth.framework/FinHealth`

```diff

-1.7.4.1.0
-  __TEXT.__text: 0x9344
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_methlist: 0x71c
-  __TEXT.__const: 0x80
+1.8.1.44.0
+  __TEXT.__text: 0xbedc
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_methlist: 0x7c0
+  __TEXT.__const: 0x1be
   __TEXT.__gcc_except_tab: 0x4ec
-  __TEXT.__oslogstring: 0x29f
-  __TEXT.__cstring: 0xd25
-  __TEXT.__unwind_info: 0x228
-  __TEXT.__objc_classname: 0xac
-  __TEXT.__objc_methname: 0x1d0c
-  __TEXT.__objc_methtype: 0x6fe
-  __TEXT.__objc_stubs: 0x1380
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x310
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x8
+  __TEXT.__oslogstring: 0x2f7
+  __TEXT.__cstring: 0xf68
+  __TEXT.__swift5_typeref: 0x95
+  __TEXT.__swift5_reflstr: 0x41
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__constg_swiftt: 0x54
+  __TEXT.__swift5_fieldmd: 0x50
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x10
+  __TEXT.__unwind_info: 0x310
+  __TEXT.__eh_frame: 0x110
+  __TEXT.__objc_classname: 0xbd
+  __TEXT.__objc_methname: 0x1e41
+  __TEXT.__objc_methtype: 0x79a
+  __TEXT.__objc_stubs: 0x13e0
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x3e0
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e0
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0x620
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x208
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0xa40
+  __AUTH_CONST.__objc_const: 0xb08
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0xf0
+  __AUTH.__objc_data: 0x1b0
+  __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x90
-  __DATA.__data: 0x60
+  __DATA.__data: 0x100
+  __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF04CF20-CB6C-30BD-9CFB-ADA09BCA542B
-  Functions: 162
-  Symbols:   708
-  CStrings:  470
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 32C75B17-0EFF-3B4C-B6A7-0662DE479E00
+  Functions: 247
+  Symbols:   889
+  CStrings:  501
 
Symbols:
+ -[FHSearchSuggestionController generatePredictionWithModelType:withModelPathComponent:completion:]
+ -[FHSearchSuggestionController predictionsByModelName:modelVersion:completion:]
+ -[FHSearchSuggestionController transactionsByGroupID:completion:]
+ GCC_except_table66
+ _FHDaemonServiceName
+ _OBJC_CLASS_$_FHTransaction
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$__TtC9FinHealth20FHInsightsController
+ _OBJC_METACLASS_$__TtC9FinHealth20FHInsightsController
+ __Block_copy
+ __Block_release
+ __DATA__TtC9FinHealth20FHInsightsController
+ __INSTANCE_METHODS__TtC9FinHealth20FHInsightsController
+ __IVARS__TtC9FinHealth20FHInsightsController
+ __METACLASS_DATA__TtC9FinHealth20FHInsightsController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FHDaemonProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FHDaemonProtocol
+ __OBJC_LABEL_PROTOCOL_$_FHDaemonProtocol
+ __OBJC_PROTOCOL_$_FHDaemonProtocol
+ ___52-[FHSearchSuggestionController _newClientConnection]_block_invoke.116
+ ___60-[FHSearchSuggestionController _sendAllTransactionFeatures:]_block_invoke.102
+ ___61-[FHSearchSuggestionController reevaluateTransactionFeatures]_block_invoke.100
+ ___65-[FHSearchSuggestionController transactionsByGroupID:completion:]_block_invoke
+ ___67-[FHPaymentRingSuggestionController generatePaymentRingSuggestion:]_block_invoke.89
+ ___79-[FHSearchSuggestionController predictionsByModelName:modelVersion:completion:]_block_invoke
+ ___98-[FHSearchSuggestionController generatePredictionWithModelType:withModelPathComponent:completion:]_block_invoke
+ ___NSArray0__struct
+ ___block_literal_global.104
+ ___block_literal_global.109
+ ___chkstk_darwin
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_FinHealth
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_FinHealth
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_FinHealth
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_FinHealth
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_FinHealth
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_FinHealth
+ __swift_stdlib_malloc_size
+ _associated conformance 9FinHealth17UpdateRequestTypeOSHAASQ
+ _block_copy_helper
+ _block_copy_helper.11
+ _block_copy_helper.15
+ _block_copy_helper.18
+ _block_copy_helper.2
+ _block_copy_helper.5
+ _block_copy_helper.8
+ _block_descriptor
+ _block_descriptor.10
+ _block_descriptor.13
+ _block_descriptor.17
+ _block_descriptor.20
+ _block_descriptor.4
+ _block_descriptor.7
+ _block_destroy_helper
+ _block_destroy_helper.12
+ _block_destroy_helper.16
+ _block_destroy_helper.19
+ _block_destroy_helper.3
+ _block_destroy_helper.6
+ _block_destroy_helper.9
+ _flat unique So16FHDaemonProtocol_p
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$allInsightsForDateRange:endDate:insightTypeItems:trendWindow:sourceId:accountType:completion:
+ _objc_msgSend$generatePredictionWithModelType:withModelPathComponent:completion:
+ _objc_msgSend$predictionsByModelName:modelVersion:completion:
+ _objc_msgSend$transactionsByGroupID:completion:
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _swift_allocBox
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _symbolic $sSY
+ _symbolic SS
+ _symbolic ScCyyt_____G s5NeverO
+ _symbolic ScCyyt______pG s5ErrorP
+ _symbolic So15NSXPCConnectionC
+ _symbolic So8NSObjectC
+ _symbolic _____ 9FinHealth17UpdateRequestTypeO
+ _symbolic _____ 9FinHealth20FHInsightsControllerC
+ _symbolic ______p So16FHDaemonProtocolP
+ _symbolic ______p s5ErrorP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- GCC_except_table54
- ___52-[FHSearchSuggestionController _newClientConnection]_block_invoke.110
- ___60-[FHSearchSuggestionController _sendAllTransactionFeatures:]_block_invoke.96
- ___61-[FHSearchSuggestionController reevaluateTransactionFeatures]_block_invoke.94
- ___67-[FHPaymentRingSuggestionController generatePaymentRingSuggestion:]_block_invoke.83
- ___block_literal_global.103
- ___block_literal_global.98
- _objc_msgSend$allInsightsForDateRange:endDate:insightTypeItems:trendWindow:completion:
CStrings:
+ "-[FHSearchSuggestionController allFeatureInsightsWithStartDate:endDate:insightTypeItems:trendWindow:completion:]"
+ "-[FHSearchSuggestionController generatePredictionWithModelType:withModelPathComponent:completion:]"
+ "-[FHSearchSuggestionController predictionsByModelName:modelVersion:completion:]"
+ "-[FHSearchSuggestionController transactionsByGroupID:completion:]"
+ "FHDaemonProtocol"
+ "Group Id cannot be nil %s"
+ "Interrupted"
+ "Invalidated"
+ "_TtC9FinHealth20FHInsightsController"
+ "_createCheckedContinuation(_:)"
+ "_createCheckedThrowingContinuation(_:)"
+ "allInsightsForDateRange:endDate:insightTypeItems:trendWindow:sourceId:accountType:completion:"
+ "backgroundDelivery"
+ "didReceiveInsightChangeUpdate:"
+ "error = %s"
+ "generatePredictionWithModelType:withModelPathComponent:completion:"
+ "initWithMachServiceName:options:"
+ "modelName cannot be nil %s"
+ "predictionsByModelName:modelVersion:completion:"
+ "server"
+ "transactionsByGroupID:completion:"
+ "userInitiated"
+ "v24@0:8@?<v@?>16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
+ "v72@0:8@\"NSDate\"16@\"NSDate\"24@\"NSArray\"32q40@\"NSString\"48q56@?<v@?@\"NSArray\">64"
+ "v72@0:8@16@24@32q40@48q56@?64"
+ "writeEntityGroups:"
+ "writeIncomeInsights:"
+ "writePredictedTransactionInsights:"
- "allInsightsForDateRange:endDate:insightTypeItems:trendWindow:completion:"
- "v56@0:8@\"NSDate\"16@\"NSDate\"24@\"NSArray\"32q40@?<v@?@\"NSArray\">48"

```
