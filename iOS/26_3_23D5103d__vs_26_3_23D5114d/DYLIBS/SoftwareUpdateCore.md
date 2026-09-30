## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.80.7.0.1
-  __TEXT.__text: 0xa5f58
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x7ab4
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x15484
-  __TEXT.__oslogstring: 0xc661
+2422.80.9.0.2
+  __TEXT.__text: 0xaa7e8
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x7b84
+  __TEXT.__const: 0x192
+  __TEXT.__cstring: 0x154aa
+  __TEXT.__oslogstring: 0xc7a3
   __TEXT.__gcc_except_tab: 0x758
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x1790
-  __TEXT.__objc_classname: 0x73b
-  __TEXT.__objc_methname: 0x15ba4
+  __TEXT.__constg_swiftt: 0x50
+  __TEXT.__swift5_typeref: 0x43
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x17f8
+  __TEXT.__objc_classname: 0x778
+  __TEXT.__objc_methname: 0x15c85
   __TEXT.__objc_methtype: 0xff8
-  __TEXT.__objc_stubs: 0xeb40
-  __DATA_CONST.__got: 0x968
-  __DATA_CONST.__const: 0x2320
-  __DATA_CONST.__objc_classlist: 0x1e8
+  __TEXT.__objc_stubs: 0xec20
+  __DATA_CONST.__got: 0xa80
+  __DATA_CONST.__const: 0x23d0
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44c0
-  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_selrefs: 0x4508
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x4b0
-  __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x12ca0
-  __AUTH_CONST.__objc_const: 0xa908
+  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__const: 0x4e8
+  __AUTH_CONST.__cfstring: 0x12c60
+  __AUTH_CONST.__objc_const: 0xaba0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x9c4
-  __DATA.__data: 0x360
-  __DATA.__bss: 0x48
+  __AUTH.__objc_data: 0x750
+  __AUTH.__data: 0xc0
+  __DATA.__objc_ivar: 0x9d0
+  __DATA.__data: 0x398
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
+  - /System/Library/PrivateFrameworks/AppleIntelligenceReporting.framework/AppleIntelligenceReporting
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3C4DB06-08AF-3CDB-8C5D-FD301D83DC41
-  Functions: 3039
-  Symbols:   10313
-  CStrings:  9051
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 057D9CA4-11EE-371C-B934-8787DA6B3963
+  Functions: 3084
+  Symbols:   10604
+  CStrings:  9078
 
Symbols:
+ -[SUCoreBiomeEventPayloadPSUSState .cxx_destruct]
+ -[SUCoreBiomeEventPayloadPSUSState errors]
+ -[SUCoreBiomeEventPayloadPSUSState init]
+ -[SUCoreBiomeEventPayloadPSUSState psusOpType]
+ -[SUCoreBiomeEventPayloadPSUSState setErrors:]
+ -[SUCoreBiomeEventPayloadPSUSState setPsusOpType:]
+ -[SUCoreBiomeEventPayloadPSUSState setUpdateType:]
+ -[SUCoreBiomeEventPayloadPSUSState updateType]
+ -[SUCoreScan _biomePayloadForUpdate:error:]
+ -[SUCoreUpdateDownloader _biomePayloadForUpdate:error:]
+ -[SUCoreUpdateDownloader _emitNotPerformingPSUSDownloadToBiome:]
+ -[SUCoreUpdateDownloader _isPreSUStagingEnabled:]
+ -[SUCoreUpdateDownloader _shouldStageOptionalPSUSAssets:]
+ GCC_except_table101
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLC27_emitAppleIntelligenceEvent12eventPayload12functionName0J5BlockySo011SUCoreBiomemO4BaseCSg_SSy0kL9Reporting0M8ReporterC_AL0klM0OtKXEtFZ04$s18ab23Core11AIRReporter33_109efghi9LLC26emitkl25Event12eventPayloadySo011s8BiomemO4u24CSg_tFZy0kL9Reporting0M8W17C_AJ0klM0OtKXEfU_Tf1nncn_nTf4nnd_n
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLC27_emitAppleIntelligenceEvent12eventPayload12functionName0J5BlockySo011SUCoreBiomemO4BaseCSg_SSy0kL9Reporting0M8ReporterC_AL0klM0OtKXEtFZ04$s18ab23Core11AIRReporter33_109efghi9LLC29emitkl28EndEvent12eventPayloadySo011s8BiomenP4u24CSg_tFZy0kL9Reporting0N8W17C_AJ0klN0OtKXEfU_Tf1nncn_nTf4nnd_n
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLC27_emitAppleIntelligenceEvent12eventPayload12functionName0J5BlockySo011SUCoreBiomemO4BaseCSg_SSy0kL9Reporting0M8ReporterC_AL0klM0OtKXEtFZ04$s18ab23Core11AIRReporter33_109efghi9LLC31emitkl30StartEvent12eventPayloadySo011s8BiomenP4u24CSg_tFZy0kL9Reporting0N8W17C_AJ0klN0OtKXEfU_Tf1nncn_nTf4nnd_n
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLC8reporter26AppleIntelligenceReporting13EventReporterCSgvpZ.0
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLC8reporter_WZ
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLC8reporter_Wz
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLCMF
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLCMXX
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLCMa
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLCMf
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLCMm
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLCMn
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLCN
+ _$s18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLCfD
+ _$s18SoftwareUpdateCore6logger33_109DF3E415A26EAA056866113706C948LL2os6LoggerVvp
+ _$s18SoftwareUpdateCore6logger33_109DF3E415A26EAA056866113706C948LL_WZ
+ _$s18SoftwareUpdateCore6logger33_109DF3E415A26EAA056866113706C948LL_Wz
+ _$s18SoftwareUpdateCoreMXM
+ _$s26AppleIntelligenceReporting07GeneralaB5ErrorC5errorACs0E0_p_tcfC
+ _$s26AppleIntelligenceReporting07GeneralaB5ErrorCMa
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV0F4TypeO33softwareUpdateControllerPSUSEventyAeC08SoftwareiJ9PSUSStateVcAEmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV0F4TypeOMa
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV18SoftwareUpdateCoreE4fromACSo011SUCoreBiomeF16PayloadPSUSStateC_tc33_109DF3E415A26EAA056866113706C948LlfC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV0H4TypeO11incrementalyA2GmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV0H4TypeO12notSpecifiedyA2GmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV0H4TypeO16criticalCellularyA2GmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV0H4TypeO4fullyA2GmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV0H4TypeO7unknownyA2GmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV0H4TypeO8criticalyA2GmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV0H4TypeO9emergencyyA2GmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV0H4TypeOMa
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV13OperationTypeO12psusDownloadyA2GmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV13OperationTypeO13psusDetermineyA2GmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV13OperationTypeO7unknownyA2GmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV13OperationTypeOMa
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateV9operation6updateA2E13OperationTypeO_AE0hN0OtcfC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateVMa
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateVMn
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateVN
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateVSEAAMc
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateVSQAAMc
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV33SoftwareUpdateControllerPSUSStateVSeAAMc
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV9SubsystemO24softwareUpdateControlleryA2EmFWC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV9SubsystemOMa
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventV9subsystem17useCaseIdentifier18resourceSpecifiers19assetSetIdentifiers6errors4typeA2C9SubsystemO_AA0ab3UseI0VSgSaySSGSgAPSayAA07GeneralaB5ErrorCGAC0F4TypeOtcfC
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVMa
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVMn
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVN
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVSEAAMc
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVSQAAMc
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVSeAAMc
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVSgMR
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVSgMd
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVSgWOb
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVSgWOc
+ _$s26AppleIntelligenceReporting0aB18AssetDeliveryEventVSgWOhTm
+ _$s26AppleIntelligenceReporting0aB5EventO13assetDeliveryyAcA0ab5AssetfD0VcACmFWC
+ _$s26AppleIntelligenceReporting0aB5EventOMa
+ _$s26AppleIntelligenceReporting0aB5EventOMn
+ _$s26AppleIntelligenceReporting0aB5EventON
+ _$s26AppleIntelligenceReporting0aB5EventOSEAAMc
+ _$s26AppleIntelligenceReporting0aB5EventOSeAAMc
+ _$s26AppleIntelligenceReporting0aB7UseCaseVMa
+ _$s26AppleIntelligenceReporting0aB7UseCaseVMn
+ _$s26AppleIntelligenceReporting0aB7UseCaseVSgMR
+ _$s26AppleIntelligenceReporting0aB7UseCaseVSgMd
+ _$s26AppleIntelligenceReporting0abC5ErrorOACs0D0AAWL
+ _$s26AppleIntelligenceReporting0abC5ErrorOACs0D0AAWl
+ _$s26AppleIntelligenceReporting0abC5ErrorOMa
+ _$s26AppleIntelligenceReporting0abC5ErrorOs0D0AAMc
+ _$s26AppleIntelligenceReporting13EventReporterC04emitab3EndD09eventInfo05startD10IdentifieryAA0abD0O_AA14UUIDIdentifierVSgtAA0abC5ErrorOYKF
+ _$s26AppleIntelligenceReporting13EventReporterC04emitab5StartD09eventInfoAA14UUIDIdentifierVAA0abD0O_tAA0abC5ErrorOYKF
+ _$s26AppleIntelligenceReporting13EventReporterC04emitabD09eventInfoyAA0abD0O_tAA0abC5ErrorOYKF
+ _$s26AppleIntelligenceReporting13EventReporterCACyKcfC
+ _$s26AppleIntelligenceReporting13EventReporterCMa
+ _$s26AppleIntelligenceReporting13EventReporterCMm
+ _$s26AppleIntelligenceReporting13EventReporterCMn
+ _$s26AppleIntelligenceReporting13EventReporterCMo
+ _$s26AppleIntelligenceReporting13EventReporterCN
+ _$s26AppleIntelligenceReporting14UUIDIdentifierVMa
+ _$s26AppleIntelligenceReporting14UUIDIdentifierVMn
+ _$s26AppleIntelligenceReporting14UUIDIdentifierVSgMR
+ _$s26AppleIntelligenceReporting14UUIDIdentifierVSgMd
+ _$s2os32getNullTerminatedUTF8PointerImpl_21storingStringOwnersInSVSS_SpyypGSgztF
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s2os6LoggerVMa
+ _$sBoWV
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSa10FoundationE36_unconditionallyBridgeFromObjectiveCySayxGSo7NSArrayCSgFZ
+ _$sSa6append10contentsOfyqd__n_t7ElementQyd__RszSTRd__lFs5UInt8V_SayAFGTgq5
+ _$sSo11SUCoreBiomeC18SoftwareUpdateCoreE11recordEventyySo0abG11PayloadBaseCFZTo
+ _$sSo11SUCoreBiomeC18SoftwareUpdateCoreE14recordEndEventyySo0abH11PayloadBaseCFZTo
+ _$sSo11SUCoreBiomeC18SoftwareUpdateCoreE16recordStartEventyySo0abH11PayloadBaseCFZTo
+ _$sSo11SUCoreBiomeC18SoftwareUpdateCoreEABycfC
+ _$sSo11SUCoreBiomeC18SoftwareUpdateCoreEABycfc
+ _$sSo11SUCoreBiomeC18SoftwareUpdateCoreEABycfcTo
+ _$sSo11SUCoreBiomeCML
+ _$sSo11SUCoreBiomeCMa
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
+ _$sSo13os_log_type_ta0A0E5errorABvgZ
+ _$sSo8NSObjectCSgMR
+ _$sSo8NSObjectCSgMd
+ _$ss11_StringGutsV16_deconstructUTF87scratchyXlSg5owner_xSi6lengthSb11usesScratchSb15allocatedMemorytSwSg_ts8_PointerRzlFSV_Tgq5
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsV23_allocateForDeconstructyXl5owner_SVSi6lengthtyF
+ _$ss11_StringGutsV23_allocateForDeconstructyXl5owner_SVSi6lengthtyFTv_r
+ _$ss11_StringGutsVN
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFs5UInt8V_Tgq5
+ _$ss13_StringObjectV10sharedUTF8SRys5UInt8VGvg
+ _$ss15ContiguousArrayV034_makeUniqueAndReserveCapacityIfNotD0yyFyXl_Ts5
+ _$ss15ContiguousArrayV12_endMutationyyFyXl_Ts5
+ _$ss15ContiguousArrayV15reserveCapacityyySiFyXl_Ts5
+ _$ss15ContiguousArrayV36_reserveCapacityAssumingUniqueBuffer8oldCountySi_tFyXl_Ts5
+ _$ss15ContiguousArrayV37_appendElementAssumeUniqueAndCapacity_03newD0ySi_xntFyXl_Ts5
+ _$ss20__StaticArrayStorageCN
+ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tt1gq5
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss23_ContiguousArrayStorageCys5UInt8VGMR
+ _$ss23_ContiguousArrayStorageCys5UInt8VGMd
+ _$ss32_copyCollectionToContiguousArrayys0dE0Vy7ElementQzGxSlRzlFSS8UTF8ViewV_Tgq5
+ _$ss5ErrorMp
+ _$ss5Error_pMR
+ _$ss5Error_pMd
+ _$ss5UInt8VMn
+ _$ss9_typeName_9qualifiedSSypXp_SbtF
+ _$sypN
+ _$sypWOc
+ _OBJC_CLASS_$_SUCoreBiome
+ _OBJC_CLASS_$_SUCoreBiomeEventPayloadBase
+ _OBJC_CLASS_$_SUCoreBiomeEventPayloadPSUSState
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_SUCoreBiomeEventPayloadPSUSState._errors
+ _OBJC_IVAR_$_SUCoreBiomeEventPayloadPSUSState._psusOpType
+ _OBJC_IVAR_$_SUCoreBiomeEventPayloadPSUSState._updateType
+ _OBJC_METACLASS_$_SUCoreBiome
+ _OBJC_METACLASS_$_SUCoreBiomeEventPayloadBase
+ _OBJC_METACLASS_$_SUCoreBiomeEventPayloadPSUSState
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __CLASS_METHODS_SUCoreBiome
+ __DATA_SUCoreBiome
+ __DATA__TtC18SoftwareUpdateCoreP33_109DF3E415A26EAA056866113706C94811AIRReporter
+ __INSTANCE_METHODS_SUCoreBiome
+ __METACLASS_DATA_SUCoreBiome
+ __METACLASS_DATA__TtC18SoftwareUpdateCoreP33_109DF3E415A26EAA056866113706C94811AIRReporter
+ __OBJC_$_INSTANCE_METHODS_SUCoreBiomeEventPayloadPSUSState
+ __OBJC_$_INSTANCE_VARIABLES_SUCoreBiomeEventPayloadPSUSState
+ __OBJC_$_PROP_LIST_SUCoreBiomeEventPayloadPSUSState
+ __OBJC_CLASS_RO_$_SUCoreBiomeEventPayloadBase
+ __OBJC_CLASS_RO_$_SUCoreBiomeEventPayloadPSUSState
+ __OBJC_METACLASS_RO_$_SUCoreBiomeEventPayloadBase
+ __OBJC_METACLASS_RO_$_SUCoreBiomeEventPayloadPSUSState
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.651
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.654
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.655
+ ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.658
+ ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.374
+ ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.389
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.400
+ ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.402
+ ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.990
+ ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1077
+ ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1064
+ ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1062
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1117
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1121
+ ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1121.cold.1
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1109
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1110
+ ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1110.cold.1
+ ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1088
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1101
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1102
+ ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1102.cold.1
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.579
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.580
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.569
+ ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.577
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1106
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1110
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1117
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1167
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1168
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.542
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.542.cold.1
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.544
+ ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.544.cold.1
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.489
+ ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.542
+ ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.580
+ ___63-[SUCoreScan _shouldPerformPSUSScanFromFoundDescriptor:policy:]_block_invoke
+ ___64-[SUCoreUpdateDownloader _emitNotPerformingPSUSDownloadToBiome:]_block_invoke
+ ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.344
+ ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.548
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.351
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.354
+ ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.356
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.338
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.343
+ ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.353
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.624
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.625
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.628
+ ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.631
+ ___83-[SUCorePolicyDDMConfiguration invalidateAllInvalidDeclarationsReturningAllInvalid]_block_invoke.343
+ ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.391
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.474
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.480
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.486
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.492
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.498
+ ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.504
+ ___NSArray0__struct
+ ___block_literal_global.340
+ ___block_literal_global.345
+ ___block_literal_global.347
+ ___block_literal_global.352
+ ___block_literal_global.410
+ ___block_literal_global.413
+ ___block_literal_global.470
+ ___block_literal_global.476
+ ___block_literal_global.482
+ ___block_literal_global.488
+ ___block_literal_global.494
+ ___block_literal_global.500
+ ___block_literal_global.506
+ ___block_literal_global.541
+ ___block_literal_global.551
+ ___block_literal_global.572
+ ___block_literal_global.580
+ ___block_literal_global.583
+ ___block_literal_global.630
+ ___block_literal_global.653
+ ___block_literal_global.657
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_SoftwareUpdateCore
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_SoftwareUpdateCore
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$_biomePayloadForUpdate:error:
+ _objc_msgSend$_emitNotPerformingPSUSDownloadToBiome:
+ _objc_msgSend$_isPreSUStagingEnabled:
+ _objc_msgSend$_shouldStageOptionalPSUSAssets:
+ _objc_msgSend$recordEndEvent:
+ _objc_msgSend$recordStartEvent:
+ _objc_msgSend$setErrors:
+ _objc_msgSend$setPsusOpType:
+ _objc_msgSend$setUpdateType:
+ _objc_opt_self
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCastObjCClass
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 18SoftwareUpdateCore11AIRReporter33_109DF3E415A26EAA056866113706C948LLC
+ _symbolic _____Sg 26AppleIntelligenceReporting0aB18AssetDeliveryEventV
+ _symbolic _____Sg 26AppleIntelligenceReporting0aB7UseCaseV
+ _symbolic _____Sg 26AppleIntelligenceReporting14UUIDIdentifierV
+ _symbolic ______p s5ErrorP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- -[SUCoreUpdateDownloader _isPreSUStagingEnabled]
- -[SUCoreUpdateDownloader _shouldStageOptionalPSUSAssets]
- GCC_except_table100
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.642
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.645
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.646
- ___127-[SUCorePolicy selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke_2.649
- ___129+[SUCoreSpace checkAvailableSpace:allowPurgeWithUrgency:purgingFromBase:minimalRequiredFreeSpace:withCompletionQueue:completion:]_block_invoke.365
- ___141-[SUCorePolicyMacUpdateBrain selectSoftwareUpdateMajorPrimaryAsset:majorSecondaryAsset:minorPrimaryAsset:minorSecondaryAsset:fromAssetQuery:]_block_invoke.380
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.391
- ___150-[MSUUpdateBrainAssetLoader(SUCoreBorderMSUUpdateBrainAssetLoader) SUCoreBorder_loadUpdateBrainWithMAOptions:clientOptionsFromPolicy:progressHandler:]_block_invoke.393
- ___33-[SUCoreMSU _operationLoadBrain:]_block_invoke.981
- ___35-[SUCoreMSU _operationApplyUpdate:]_block_invoke.1068
- ___36-[SUCoreMSU _operationSuspendUpdate]_block_invoke.1055
- ___37-[SUCoreMSU _operationPrepareUpdate:]_block_invoke.1053
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1108
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1112
- ___43-[SUCoreMSU _operationRollbackUpdateApply:]_block_invoke.1112.cold.1
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1100
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1101
- ___44-[SUCoreMSU _operationRollbackUpdateResume:]_block_invoke.1101.cold.1
- ___45-[SUCoreMSU _operationRollbackUpdatePrepare:]_block_invoke.1079
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1092
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1093
- ___45-[SUCoreMSU _operationRollbackUpdateSuspend:]_block_invoke.1093.cold.1
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.566
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.567
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.560
- ___53-[SUCoreConfigServer actionConfigScheduleScan:error:]_block_invoke.568
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1097
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1101
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1108
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1158
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1159
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.533
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.533.cold.1
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.535
- ___55-[SUCoreConfigServer actionConfigAdjustSettings:error:]_block_invoke.535.cold.1
- ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.476
- ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.529
- ___63+[SUCoreSpace mobileAssetResumeWithCompletionQueue:completion:]_block_invoke.571
- ___67+[SUCorePurge checkForAssetsOfType:withCompletionQueue:completion:]_block_invoke.335
- ___69-[SUCoreConfigServer _stateSafeInformDelegatesOfConfiguration:error:]_block_invoke.539
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.342
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.345
- ___75+[SUCorePurge removeAllUpdateContentWithPolicy:completionQueue:completion:]_block_invoke.347
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.329
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.334
- ___78-[SUCorePolicyExtensionCompanionCompatibility filterSoftwareUpdateAssetArray:]_block_invoke.335
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.615
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.616
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke.619
- ___79-[SUCorePolicy selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery:]_block_invoke_2.622
- ___83-[SUCorePolicyDDMConfiguration invalidateAllInvalidDeclarationsReturningAllInvalid]_block_invoke.334
- ___96+[SUCoreSpace checkAvailableFreeSpace:checkingFromBase:withIdentifier:userInitiated:completion:]_block_invoke.382
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.465
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.471
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.477
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.483
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.489
- ___96-[SUCoreConfigServer _stateSafeSelectBestAssetFromMultipleAssetArray:bestAsset:selectionReason:]_block_invoke.495
- ___block_literal_global.331
- ___block_literal_global.336
- ___block_literal_global.338
- ___block_literal_global.343
- ___block_literal_global.392
- ___block_literal_global.404
- ___block_literal_global.461
- ___block_literal_global.467
- ___block_literal_global.473
- ___block_literal_global.479
- ___block_literal_global.485
- ___block_literal_global.491
- ___block_literal_global.497
- ___block_literal_global.532
- ___block_literal_global.542
- ___block_literal_global.563
- ___block_literal_global.571
- ___block_literal_global.574
- ___block_literal_global.621
- ___block_literal_global.644
- ___block_literal_global.648
- _objc_msgSend$_isPreSUStagingEnabled
- _objc_msgSend$_shouldStageOptionalPSUSAssets
CStrings:
+ "EventReporter not available"
+ "Failed to create EventReporter: %@"
+ "SUCoreBiome"
+ "SUCoreBiomeEventPayloadBase"
+ "SUCoreBiomeEventPayloadPSUSState"
+ "T@\"NSArray\",&,N,V_errors"
+ "Tq,N,V_psusOpType"
+ "[%s] Failed to emit event: %@"
+ "[%s] Invalid event payload type: %s"
+ "[%s] No event payload"
+ "[%s] No event reporter"
+ "[%s] No event to emit"
+ "[%s] Not available"
+ "[%s] Successfully emitted event"
+ "[PreSUStaging] No need to remove PSUS assets (%@)"
+ "[PreSUStaging] disabled (%@); skip downloading assets"
+ "[PreSUStaging] not staging optional assets: %@"
+ "_TtC18SoftwareUpdateCoreP33_109DF3E415A26EAA056866113706C94811AIRReporter"
+ "_biomePayloadForUpdate:error:"
+ "_emitNotPerformingPSUSDownloadToBiome:"
+ "_errors"
+ "_isPreSUStagingEnabled:"
+ "_psusOpType"
+ "_shouldStageOptionalPSUSAssets:"
+ "disabled by udpate-metadata"
+ "emitAppleIntelligenceEndEvent(eventPayload:)"
+ "emitAppleIntelligenceEvent(eventPayload:)"
+ "emitAppleIntelligenceStartEvent(eventPayload:)"
+ "errors"
+ "no optional assets to stage"
+ "no space allowed"
+ "psusOpType"
+ "recordEndEvent:"
+ "recordEvent:"
+ "recordStartEvent:"
+ "setErrors:"
+ "setPsusOpType:"
- "[PreSUStaging] %@: %@"
- "[PreSUStaging] No need to remove PSUS assets (disabled)"
- "[PreSUStaging] disabled; skip downloading assets"
- "[PreSUStaging] no optional assets to stage"
- "[PreSUStaging] should stage optional assets"
- "[PreSUStaging] staging optional assets is disabled because no space is allowed"
- "[PreSUStaging] staging optional assets is disabled by policy"
- "[PreSUStaging] staging optional assets is disabled by server (through the update)"
- "_isPreSUStagingEnabled"
- "_shouldStageOptionalPSUSAssets"

```
