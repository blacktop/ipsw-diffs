## FeedbackLogger

> `/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger`

```diff

-3303.5.1.0.0
-  __TEXT.__text: 0xb83c
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0xd70
-  __TEXT.__const: 0x78
+3304.72.1.0.0
+  __TEXT.__text: 0x1dbec
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0xeb8
+  __TEXT.__const: 0x1348
+  __TEXT.__cstring: 0x2400
+  __TEXT.__swift5_typeref: 0x40f
+  __TEXT.__swift5_fieldmd: 0x330
+  __TEXT.__constg_swiftt: 0x1c8
+  __TEXT.__swift5_capture: 0x74
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0x108
+  __TEXT.__swift5_reflstr: 0x23f
+  __TEXT.__swift5_assocty: 0xc0
+  __TEXT.__swift5_types: 0x2c
   __TEXT.__gcc_except_tab: 0x140
-  __TEXT.__cstring: 0x1762
-  __TEXT.__oslogstring: 0x15b3
-  __TEXT.__unwind_info: 0x364
-  __TEXT.__objc_classname: 0x126
-  __TEXT.__objc_methname: 0x2956
-  __TEXT.__objc_methtype: 0x672
-  __TEXT.__objc_stubs: 0x1c00
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x328
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__oslogstring: 0x1688
+  __TEXT.__unwind_info: 0x9dc
+  __TEXT.__eh_frame: 0x5a8
+  __TEXT.__objc_classname: 0x134
+  __TEXT.__objc_methname: 0x2be4
+  __TEXT.__objc_methtype: 0x6a3
+  __TEXT.__objc_stubs: 0x1e00
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1750
-  __DATA_CONST.__objc_selrefs: 0x9c0
+  __DATA_CONST.__objc_const: 0x1930
+  __DATA_CONST.__objc_selrefs: 0xa80
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__objc_const: 0xd8
-  __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__const: 0x5d0
+  __AUTH_CONST.__auth_ptr: 0x18
+  __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__cfstring: 0x860
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x378
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0x114
-  __DATA.__data: 0x120
-  __DATA.__bss: 0x20
+  __AUTH_CONST.__auth_got: 0x790
+  __AUTH.__objc_data: 0x1f0
+  __AUTH.__data: 0x448
+  __DATA.__objc_ivar: 0x11c
+  __DATA.__data: 0x6c0
+  __DATA.__common: 0x108
+  __DATA.__bss: 0x20b0
   __DATA_DIRTY.__const: 0x20
   __DATA_DIRTY.__objc_const: 0x2c8
-  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 311
-  Symbols:   1200
-  CStrings:  799
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 971
+  Symbols:   1605
+  CStrings:  938
 
Symbols:
+ +[FLLoggingContext isInternalBuild]
+ -[FLDPGBatch .cxx_destruct]
+ -[FLDPGBatch bundleID]
+ -[FLDPGBatch initWithBundleID:payload:]
+ -[FLDPGBatch payload]
+ -[FLDPGBatch setBundleID:]
+ -[FLDPGBatch setPayload:]
+ -[FLLogger categoryForSiriPayload:autoBugHelper:]
+ -[FLLogger closeOpenBatchesAndStores]
+ -[FLLogger readSiriCategoryFrom:recursive:autoBugHelper:]
+ -[FLLogger reportDataPlatformBatchedEvent:forBundleID:ofSchema:completion:]
+ -[FLLogger reportDataPlatformSingleEvent:forBundleID:ofSchema:completion:]
+ -[FLLoggingContext autoBugCapture]
+ -[FLLoggingContext initWithFileManager:userDefaults:autoBugCapture:]
+ -[FLLoggingContext setAutoBugCapture:]
+ -[FLSQLitePersistence setUser:]
+ -[FLSQLitePersistence user]
+ -[FLSQLitePersistence(BatchManager) metadataForBatch:bundleID:]
+ -[FLSQLitePersistence(SchemaManager) shouldIgnoreQuota]
+ GCC_except_table211
+ GCC_except_table235
+ GCC_except_table295
+ GCC_except_table52
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table64
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table96
+ _FLIgnoreQuotaFilename
+ _MGCopyAnswer
+ _OBJC_CLASS_$_FLAutoBugCapture
+ _OBJC_CLASS_$_FLAutoBugHelper
+ _OBJC_CLASS_$_FLDPGBatch
+ _OBJC_CLASS_$_FLDPGBatchFactory
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_SDRDiagnosticReporter
+ _OBJC_IVAR_$_FLDPGBatch._bundleID
+ _OBJC_IVAR_$_FLDPGBatch._payload
+ _OBJC_IVAR_$_FLLoggingContext._autoBugCapture
+ _OBJC_IVAR_$_FLSQLitePersistence._user
+ _OBJC_METACLASS_$_FLAutoBugCapture
+ _OBJC_METACLASS_$_FLAutoBugHelper
+ _OBJC_METACLASS_$_FLDPGBatch
+ _OBJC_METACLASS_$_FLDPGBatchFactory
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __Block_copy
+ __Block_release
+ __DATA_FLAutoBugCapture
+ __DATA_FLAutoBugHelper
+ __DATA_FLDPGBatchFactory
+ __IVARS_FLAutoBugCapture
+ __IVARS_FLAutoBugHelper
+ __METACLASS_DATA_FLAutoBugCapture
+ __METACLASS_DATA_FLAutoBugHelper
+ __METACLASS_DATA_FLDPGBatchFactory
+ __OBJC_$_CLASS_METHODS_FLDPGBatchFactory
+ __OBJC_$_CLASS_METHODS_FLLoggingContext
+ __OBJC_$_INSTANCE_METHODS_FLAutoBugCapture
+ __OBJC_$_INSTANCE_METHODS_FLAutoBugHelper
+ __OBJC_$_INSTANCE_METHODS_FLDPGBatch
+ __OBJC_$_INSTANCE_METHODS_FLDPGBatchFactory
+ __OBJC_$_INSTANCE_VARIABLES_FLDPGBatch
+ __OBJC_$_PROP_LIST_FLDPGBatch
+ __OBJC_$_PROP_LIST_FLLoggingContext.114
+ __OBJC_$_PROP_LIST_NSObject.779
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.780
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.781
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.782
+ __OBJC_CLASS_RO_$_FLDPGBatch
+ __OBJC_METACLASS_RO_$_FLDPGBatch
+ ___31-[FeedbackLoggerFBFClient init]_block_invoke.50
+ ___35+[FLLoggingContext isInternalBuild]_block_invoke
+ ___37-[FLLogger closeOpenBatchesAndStores]_block_invoke
+ ___74-[FLLogger reportDataPlatformSingleEvent:forBundleID:ofSchema:completion:]_block_invoke
+ ___Block_byref_object_copy_.395
+ ___Block_byref_object_dispose_.396
+ ___block_literal_global.414
+ ___block_literal_global.510
+ ___block_literal_global.608
+ ___block_literal_global.788
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_getEnumTagSinglePayload
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_memcpy1_1
+ ___swift_memcpy9_8
+ ___swift_noop_void_return
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ ___swift_storeEnumTagSinglePayload
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_FeedbackLogger
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_FeedbackLogger
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_FeedbackLogger
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_FeedbackLogger
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_FeedbackLogger
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_FeedbackLogger
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_FeedbackLogger
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ __unnamed_array_storage.94
+ _associated conformance 14FeedbackLogger32Com_Apple_Ve_Common_BuildVariantO21InternalSwiftProtobuf4EnumAASH
+ _associated conformance 14FeedbackLogger32Com_Apple_Ve_Common_BuildVariantO21InternalSwiftProtobuf4EnumAASY
+ _associated conformance 14FeedbackLogger32Com_Apple_Ve_Common_BuildVariantOSHAASQ
+ _associated conformance 14FeedbackLogger32Com_Apple_Ve_Common_BuildVariantOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 14FeedbackLogger41Com_Apple_Aiml_Dpg_Service_V1_PayloadTypeO21InternalSwiftProtobuf4EnumAASH
+ _associated conformance 14FeedbackLogger41Com_Apple_Aiml_Dpg_Service_V1_PayloadTypeO21InternalSwiftProtobuf4EnumAASY
+ _associated conformance 14FeedbackLogger41Com_Apple_Aiml_Dpg_Service_V1_PayloadTypeOSHAASQ
+ _associated conformance 14FeedbackLogger41Com_Apple_Aiml_Dpg_Service_V1_PayloadTypeOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 14FeedbackLogger43Com_Apple_Aiml_Dpg_Service_V1_PublishStatusO21InternalSwiftProtobuf4EnumAASH
+ _associated conformance 14FeedbackLogger43Com_Apple_Aiml_Dpg_Service_V1_PublishStatusO21InternalSwiftProtobuf4EnumAASY
+ _associated conformance 14FeedbackLogger43Com_Apple_Aiml_Dpg_Service_V1_PublishStatusOSHAASQ
+ _associated conformance 14FeedbackLogger43Com_Apple_Aiml_Dpg_Service_V1_PublishStatusOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 14FeedbackLogger44Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
+ _associated conformance 14FeedbackLogger44Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0O0
+ _associated conformance 14FeedbackLogger44Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
+ _associated conformance 14FeedbackLogger44Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorVSHAASQ
+ _associated conformance 14FeedbackLogger45Com_Apple_Ve_Common_Headers_IngestEnvironmentV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
+ _associated conformance 14FeedbackLogger45Com_Apple_Ve_Common_Headers_IngestEnvironmentV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0M0
+ _associated conformance 14FeedbackLogger45Com_Apple_Ve_Common_Headers_IngestEnvironmentV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
+ _associated conformance 14FeedbackLogger45Com_Apple_Ve_Common_Headers_IngestEnvironmentVSHAASQ
+ _associated conformance 14FeedbackLogger46Com_Apple_Aiml_Dpg_Service_V1_DataEventMessageV21InternalSwiftProtobuf01_K18ImplementationBaseAASH
+ _associated conformance 14FeedbackLogger46Com_Apple_Aiml_Dpg_Service_V1_DataEventMessageV21InternalSwiftProtobuf01_K18ImplementationBaseAaD0K0
+ _associated conformance 14FeedbackLogger46Com_Apple_Aiml_Dpg_Service_V1_DataEventMessageV21InternalSwiftProtobuf0K0AAs28CustomDebugStringConvertible
+ _associated conformance 14FeedbackLogger46Com_Apple_Aiml_Dpg_Service_V1_DataEventMessageVSHAASQ
+ _associated conformance 14FeedbackLogger47Com_Apple_Aiml_Dpg_Service_V1_DataEventMetadataV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
+ _associated conformance 14FeedbackLogger47Com_Apple_Aiml_Dpg_Service_V1_DataEventMetadataV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0O0
+ _associated conformance 14FeedbackLogger47Com_Apple_Aiml_Dpg_Service_V1_DataEventMetadataV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
+ _associated conformance 14FeedbackLogger47Com_Apple_Aiml_Dpg_Service_V1_DataEventMetadataVSHAASQ
+ _associated conformance 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorCodeO21InternalSwiftProtobuf4EnumAASH
+ _associated conformance 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorCodeO21InternalSwiftProtobuf4EnumAASY
+ _associated conformance 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorCodeOSHAASQ
+ _associated conformance 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorCodeOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataPayloadMessageV21InternalSwiftProtobuf01_K18ImplementationBaseAASH
+ _associated conformance 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataPayloadMessageV21InternalSwiftProtobuf01_K18ImplementationBaseAaD0K0
+ _associated conformance 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataPayloadMessageV21InternalSwiftProtobuf0K0AAs28CustomDebugStringConvertible
+ _associated conformance 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataPayloadMessageVSHAASQ
+ _associated conformance 14FeedbackLogger49Com_Apple_Aiml_Dpg_Service_V1_BatchPublishRequestV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
+ _associated conformance 14FeedbackLogger49Com_Apple_Aiml_Dpg_Service_V1_BatchPublishRequestV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0O0
+ _associated conformance 14FeedbackLogger49Com_Apple_Aiml_Dpg_Service_V1_BatchPublishRequestV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
+ _associated conformance 14FeedbackLogger49Com_Apple_Aiml_Dpg_Service_V1_BatchPublishRequestVSHAASQ
+ _associated conformance 14FeedbackLogger50Com_Apple_Aiml_Dpg_Service_V1_BatchPublishResponseV21InternalSwiftProtobuf26_MessageImplementationBaseAASH
+ _associated conformance 14FeedbackLogger50Com_Apple_Aiml_Dpg_Service_V1_BatchPublishResponseV21InternalSwiftProtobuf26_MessageImplementationBaseAaD0O0
+ _associated conformance 14FeedbackLogger50Com_Apple_Aiml_Dpg_Service_V1_BatchPublishResponseV21InternalSwiftProtobuf7MessageAAs28CustomDebugStringConvertible
+ _associated conformance 14FeedbackLogger50Com_Apple_Aiml_Dpg_Service_V1_BatchPublishResponseVSHAASQ
+ _block_copy_helper
+ _block_copy_helper.15
+ _block_copy_helper.18
+ _block_descriptor
+ _block_descriptor.17
+ _block_descriptor.20
+ _block_destroy_helper
+ _block_destroy_helper.16
+ _block_destroy_helper.19
+ _isInternalBuild.onceToken
+ _isInternalBuild.osVariantIsInternal
+ _kSymptomDiagnosticActionGetNetworkInfo
+ _kSymptomDiagnosticErrorDailyLimitExceeded
+ _kSymptomDiagnosticErrorDisabled
+ _kSymptomDiagnosticErrorHourlyLimitExceeded
+ _kSymptomDiagnosticErrorRandomizedSuppression
+ _kSymptomDiagnosticErrorRequestThrottled
+ _kSymptomDiagnosticKeyEventName
+ _kSymptomDiagnosticKeyEventValue
+ _kSymptomDiagnosticKeyTimestamp
+ _kSymptomDiagnosticReplyReason
+ _kSymptomDiagnosticReplyReasonString
+ _kSymptomDiagnosticReplySessionID
+ _kSymptomDiagnosticReplySuccess
+ _malloc_size
+ _memcmp
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$autoBugCapture
+ _objc_msgSend$bundleID
+ _objc_msgSend$categoryForSiriPayload:autoBugHelper:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$initWithAutoBugCapture:bundleID:eventValue:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithFileManager:
+ _objc_msgSend$initWithFileManager:userDefaults:autoBugCapture:
+ _objc_msgSend$isDPGBundleID:
+ _objc_msgSend$isDataSentToProd
+ _objc_msgSend$isInternalBuild
+ _objc_msgSend$makeBatchWithPayload:bundleID:schema:
+ _objc_msgSend$payload
+ _objc_msgSend$readSiriCategoryFrom:recursive:autoBugHelper:
+ _objc_msgSend$setUser:
+ _objc_msgSend$shouldIgnoreQuota
+ _objc_msgSend$standardizedURL
+ _objc_msgSend$triggerABCWithSubtype:
+ _objc_msgSend$user
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x27
+ _os_variant_has_internal_content
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deallocObject
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_initStaticObject
+ _swift_initStructMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic $s14FeedbackLogger13FLABCReporterP
+ _symbolic $sSY
+ _symbolic $ss12CaseIterableP
+ _symbolic SDyS2SG
+ _symbolic SDySSypG
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic Say_____G 14FeedbackLogger32Com_Apple_Ve_Common_BuildVariantO
+ _symbolic Say_____G 14FeedbackLogger41Com_Apple_Aiml_Dpg_Service_V1_PayloadTypeO
+ _symbolic Say_____G 14FeedbackLogger43Com_Apple_Aiml_Dpg_Service_V1_PublishStatusO
+ _symbolic Say_____G 14FeedbackLogger44Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorV
+ _symbolic Say_____G 14FeedbackLogger46Com_Apple_Aiml_Dpg_Service_V1_DataEventMessageV
+ _symbolic Say_____G 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorCodeO
+ _symbolic Say_____G 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataPayloadMessageV
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic Sb
+ _symbolic Sd
+ _symbolic Si
+ _symbolic Si______t 21InternalSwiftProtobuf8_NameMapV0D11DescriptionO
+ _symbolic So16FLAutoBugCaptureC
+ _symbolic So16FLAutoBugCaptureCSgXw
+ _symbolic So16FLAutoBugCaptureCSgXwz_Xx
+ _symbolic So16FLAutoBugCaptureCXDXMT
+ _symbolic So19NSMutableDictionaryCSg
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 14FeedbackLogger32Com_Apple_Ve_Common_BuildVariantO
+ _symbolic _____ 14FeedbackLogger41Com_Apple_Aiml_Dpg_Service_V1_PayloadTypeO
+ _symbolic _____ 14FeedbackLogger43Com_Apple_Aiml_Dpg_Service_V1_PublishStatusO
+ _symbolic _____ 14FeedbackLogger44Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorV
+ _symbolic _____ 14FeedbackLogger45Com_Apple_Ve_Common_Headers_IngestEnvironmentV
+ _symbolic _____ 14FeedbackLogger46Com_Apple_Aiml_Dpg_Service_V1_DataEventMessageV
+ _symbolic _____ 14FeedbackLogger47Com_Apple_Aiml_Dpg_Service_V1_DataEventMetadataV
+ _symbolic _____ 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorCodeO
+ _symbolic _____ 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataPayloadMessageV
+ _symbolic _____ 14FeedbackLogger49Com_Apple_Aiml_Dpg_Service_V1_BatchPublishRequestV
+ _symbolic _____ 14FeedbackLogger50Com_Apple_Aiml_Dpg_Service_V1_BatchPublishResponseV
+ _symbolic _____ 21InternalSwiftProtobuf14UnknownStorageV
+ _symbolic _____ s5Int32V
+ _symbolic _____ s5Int64V
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg 14FeedbackLogger32Com_Apple_Ve_Common_BuildVariantO
+ _symbolic _____Sg 14FeedbackLogger47Com_Apple_Aiml_Dpg_Service_V1_DataEventMetadataV
+ _symbolic _____Sg 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataPayloadMessageV
+ _symbolic _____Sg_ABt 14FeedbackLogger47Com_Apple_Aiml_Dpg_Service_V1_DataEventMetadataV
+ _symbolic _____Sg_ABt 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataPayloadMessageV
+ _symbolic ______p 14FeedbackLogger13FLABCReporterP
+ _symbolic _____ySDySSypGG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySi______tG s23_ContiguousArrayStorageC 21InternalSwiftProtobuf8_NameMapV0G11DescriptionO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 14FeedbackLogger32Com_Apple_Ve_Common_BuildVariantO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 14FeedbackLogger41Com_Apple_Aiml_Dpg_Service_V1_PayloadTypeO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 14FeedbackLogger43Com_Apple_Aiml_Dpg_Service_V1_PublishStatusO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataEventErrorCodeO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 14FeedbackLogger48Com_Apple_Aiml_Dpg_Service_V1_DataPayloadMessageV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC s11AnyHashableV
+ _symbolic _____yypG s23_ContiguousArrayStorageC
+ _symbolic x
+ _symbolic ypSg
- +[FLLogger categoryForSiriPayload:]
- +[FLLogger readSiriCategoryFrom:recursive:]
- -[FLLogger _nextStoreCacheTimerFireDateForManagedProcess]
- -[FLLogger _nextStoreCacheTimerFireDateForUnmanagedProcess]
- -[FLLogger managedProcessPersistentStoreCacheTTLInSeconds]
- -[FLLogger mostRecentWriteTransactionExpiry]
- -[FLLogger setManagedProcessPersistentStoreCacheTTLInSeconds:]
- -[FLLogger setMostRecentWriteTransactionExpiry:]
- -[FLSQLitePersistence(BatchManager) metadataForBatch:]
- GCC_except_table203
- GCC_except_table227
- GCC_except_table282
- GCC_except_table53
- GCC_except_table57
- GCC_except_table59
- GCC_except_table63
- GCC_except_table77
- GCC_except_table79
- GCC_except_table95
- _OBJC_IVAR_$_FLLogger._managedProcessPersistentStoreCacheTTLInSeconds
- _OBJC_IVAR_$_FLLogger._mostRecentWriteTransactionExpiry
- __OBJC_$_PROP_LIST_FLLoggingContext.99
- __OBJC_$_PROP_LIST_NSObject.747
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.748
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.749
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.750
- ___31-[FeedbackLoggerFBFClient init]_block_invoke.49
- ___Block_byref_object_copy_.385
- ___Block_byref_object_dispose_.386
- ___block_literal_global.403
- ___block_literal_global.575
- ___block_literal_global.756
- __unnamed_array_storage.112
- _objc_msgSend$_nextStoreCacheTimerFireDateForManagedProcess
- _objc_msgSend$_nextStoreCacheTimerFireDateForUnmanagedProcess
- _objc_msgSend$categoryForSiriPayload:
- _objc_msgSend$managedProcessPersistentStoreCacheTTLInSeconds
- _objc_msgSend$mostRecentWriteTransactionExpiry
- _objc_msgSend$readSiriCategoryFrom:recursive:
CStrings:
+ "\x02"
+ "\x06"
+ "\x17\x11"
+ ".com.apple.feedbacklogger.ignore_quota"
+ "@\"FLAutoBugCapture\""
+ "@\"FLAutoBugCapture\"16@0:8"
+ "@36@0:8@16B24@28"
+ "AnyEventTypeFoundButValueSizeZero_nonrecursive"
+ "AnyEventTypeFoundButValueSizeZero_recursive"
+ "AnyEventTypeNeverFound_nonrecursive"
+ "AnyEventTypeNeverFound_recursive"
+ "AnyEventTypePayloadSizeZero"
+ "AnyEventTypeReaderHasError_nonrecursive"
+ "AnyEventTypeReaderHasError_recursive"
+ "AnyEventTypeReaderNil"
+ "Can't open a connection for unknown user."
+ "Closing all open database connections."
+ "EVENT_BODY_INVALID"
+ "EVENT_BODY_TOO_LARGE"
+ "EVENT_HEADERS_INVALID"
+ "EVENT_PRODUCER_FAILED"
+ "EVENT_SCHEMA_UNKNOWN"
+ "EVENT_TIMEOUT"
+ "EVENT_UNSUPPORTED"
+ "Error with PBReader with payload having outer event AnyOrderedEventType"
+ "FAILED_ALL"
+ "FAILED_PARTIAL"
+ "FLAutoBugCapture"
+ "FLAutoBugHelper"
+ "FLDPGBatch"
+ "FLDPGBatchFactory"
+ "Fatal error"
+ "FeedbackLogger_Private.FLAutoBugHelper"
+ "Ignoring FeedbackLogger DB size quota."
+ "InnerAnyEventTypeFoundButPlaceMarkError"
+ "InnerAnyEventTypeNeverFound"
+ "InnerSkipTagButValueSizeZero"
+ "Insufficient space allocated to copy string contents"
+ "OK"
+ "PAYLOAD_AVRO_RECORD"
+ "PAYLOAD_PROTO_RECORD"
+ "PAYLOAD_UNKNOWN"
+ "PayloadFoundButValueSizeZero_nonrecursive"
+ "PayloadFoundButValueSizeZero_recursive"
+ "Received notification to close all stores and any open batches, closing"
+ "SkipTagButValueSizeZero_nonrecursive"
+ "SkipTagButValueSizeZero_recursive"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "SymptomDiagnosticReporter couldn't parse signature: %s"
+ "SymptomDiagnosticReporter reporter returned no response"
+ "SymptomDiagnosticReporter snapshot accepted with sessionID %@"
+ "SymptomDiagnosticReporter snapshot rejected with expected reason %ld %s"
+ "SymptomDiagnosticReporter snapshot rejected with unexpected reason %ld %s"
+ "SymptomDiagnosticReporter throttled since currentTime (%f) <= nextTime (%f)"
+ "SymptomDiagnosticReporter updated nextTimeToTrigger %f"
+ "SymptomDiagnosticReporter updated nextTimeToTrigger with cooldown %f"
+ "T@\"FLAutoBugCapture\",&,N,V_autoBugCapture"
+ "T@\"FLAutoBugCapture\",R,N"
+ "T@\"NSData\",&,N,V_payload"
+ "T@\"NSString\",&,N,V_bundleID"
+ "T@\"NSString\",?,R,C"
+ "Ti,N,V_user"
+ "URLByAppendingPathComponent:"
+ "URLByDeletingLastPathComponent"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "_autoBugCapture"
+ "_bundleID"
+ "_user"
+ "autoBugCapture"
+ "body"
+ "buildVariant"
+ "bundleID"
+ "categoryForSiriPayload:autoBugHelper:"
+ "closeOpenBatchesAndStores"
+ "com.apple.aiml.dpg.service.v1.BatchPublishRequest"
+ "com.apple.aiml.dpg.service.v1.BatchPublishResponse"
+ "com.apple.aiml.dpg.service.v1.DataEventError"
+ "com.apple.aiml.dpg.service.v1.DataEventMessage"
+ "com.apple.aiml.dpg.service.v1.DataEventMetadata"
+ "com.apple.aiml.dpg.service.v1.DataPayloadMessage"
+ "com.apple.feedbackLogger.abc"
+ "com.apple.feedbacklogger.write.dpg.data"
+ "com.apple.ve.common.headers.IngestEnvironment"
+ "errors"
+ "eventValue"
+ "events"
+ "fileExistsAtPath:"
+ "fileURLWithPath:"
+ "fqn"
+ "headers"
+ "index"
+ "initWithAutoBugCapture:bundleID:eventValue:"
+ "initWithBundleID:payload:"
+ "initWithDomain:code:userInfo:"
+ "initWithFileManager:userDefaults:autoBugCapture:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isDPGBundleID:"
+ "isDataSentToProd"
+ "isInternalBuild"
+ "legacyHeaders"
+ "makeBatchWithPayload:bundleID:schema:"
+ "message"
+ "metadata"
+ "metadataForBatch:bundleID:"
+ "nextTimeToTrigger"
+ "payload_type"
+ "processInfo"
+ "processName"
+ "readSiriCategoryFrom:recursive:autoBugHelper:"
+ "reportDataPlatformBatchedEvent:forBundleID:ofSchema:completion:"
+ "reportDataPlatformSingleEvent:forBundleID:ofSchema:completion:"
+ "request_id"
+ "schema_fingerprint"
+ "schema_name"
+ "setAutoBugCapture:"
+ "setBundleID:"
+ "setUser:"
+ "shouldIgnoreQuota"
+ "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
+ "snapshotWithSignature:delay:events:payload:actions:reply:"
+ "source_cluster"
+ "standardizedURL"
+ "status"
+ "stream"
+ "timestamp_ms"
+ "topic_override"
+ "triggerABCWithSubtype:"
+ "triggerABCWithSubtype:additionalEventName:"
+ "triggerABCWithSubtype:bundleID:eventName:eventValue:"
+ "user"
+ "v16@?0@\"NSDictionary\"8"
+ "v48@0:8@16@24@32@40"
- "\x14\x13\x12"
- "@28@0:8@16B24"
- "Received notification to close all stores, closing"
- "T@\"NSDate\",&,N,V_mostRecentWriteTransactionExpiry"
- "TQ,N,V_managedProcessPersistentStoreCacheTTLInSeconds"
- "_managedProcessPersistentStoreCacheTTLInSeconds"
- "_mostRecentWriteTransactionExpiry"
- "_nextStoreCacheTimerFireDateForManagedProcess"
- "_nextStoreCacheTimerFireDateForUnmanagedProcess"
- "categoryForSiriPayload:"
- "managedProcessPersistentStoreCacheTTLInSeconds"
- "metadataForBatch:"
- "mostRecentWriteTransactionExpiry"
- "readSiriCategoryFrom:recursive:"
- "setManagedProcessPersistentStoreCacheTTLInSeconds:"
- "setMostRecentWriteTransactionExpiry:"

```
