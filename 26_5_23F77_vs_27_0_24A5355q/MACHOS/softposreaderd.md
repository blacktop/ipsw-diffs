## softposreaderd

> `/usr/libexec/softposreaderd`

```diff

-44.13.0.0.0
-  __TEXT.__text: 0x378328
-  __TEXT.__auth_stubs: 0x3900
-  __TEXT.__objc_stubs: 0x2120
-  __TEXT.__objc_methlist: 0xae4
-  __TEXT.__const: 0x83200
-  __TEXT.__cstring: 0xd81b
-  __TEXT.__swift5_typeref: 0x1c32
-  __TEXT.__objc_methtype: 0x1035
-  __TEXT.__oslogstring: 0xb45e
+50.27.0.0.0
+  __TEXT.__text: 0x419478
+  __TEXT.__auth_stubs: 0x4220
+  __TEXT.__objc_stubs: 0x20a0
+  __TEXT.__objc_methlist: 0xe7c
+  __TEXT.__const: 0x88260
+  __TEXT.__swift5_typeref: 0x24cc
+  __TEXT.__cstring: 0x1130b
+  __TEXT.__objc_methtype: 0x1535
+  __TEXT.__oslogstring: 0xcbee
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x59f0
-  __TEXT.__swift5_proto: 0x9f4
-  __TEXT.__swift5_types: 0x408
-  __TEXT.__objc_methname: 0x3b1d
-  __TEXT.__objc_classname: 0x12e3
-  __TEXT.__swift5_protos: 0xdc
-  __TEXT.__swift_as_entry: 0x18
-  __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x3710
-  __TEXT.__eh_frame: 0x82f8
-  __DATA_CONST.__auth_got: 0x1c88
-  __DATA_CONST.__got: 0xbe0
-  __DATA_CONST.__auth_ptr: 0xbd8
-  __DATA_CONST.__const: 0x142e0
-  __DATA_CONST.__objc_classlist: 0x2c0
-  __DATA_CONST.__objc_protolist: 0x140
+  __TEXT.__constg_swiftt: 0x78f4
+  __TEXT.__swift5_proto: 0xcd4
+  __TEXT.__swift5_types: 0x528
+  __TEXT.__objc_classname: 0x1a13
+  __TEXT.__objc_methname: 0x429d
+  __TEXT.__swift_as_entry: 0x188
+  __TEXT.__swift_as_ret: 0x188
+  __TEXT.__swift_as_cont: 0x39c
+  __TEXT.__swift5_protos: 0x138
+  __TEXT.__unwind_info: 0x4da8
+  __TEXT.__eh_frame: 0xc890
+  __DATA_CONST.__const: 0x18170
+  __DATA_CONST.__objc_classlist: 0x390
+  __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA.__objc_const: 0x7050
-  __DATA.__objc_selrefs: 0xac8
-  __DATA.__objc_data: 0x18b8
-  __DATA.__data: 0x97d8
-  __DATA.__common: 0x660
-  __DATA.__bss: 0x10f60
+  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__auth_got: 0x2118
+  __DATA_CONST.__got: 0xde0
+  __DATA_CONST.__auth_ptr: 0xe28
+  __DATA.__objc_const: 0x91b8
+  __DATA.__objc_selrefs: 0xb18
+  __DATA.__objc_data: 0x21b0
+  __DATA.__data: 0xc778
+  __DATA.__common: 0x898
+  __DATA.__bss: 0x15be0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/DeviceCheck.framework/DeviceCheck
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F97D2ACE-19A7-31C8-8BE9-B7E2E8F8E7DB
-  Functions: 4550
-  Symbols:   1464
-  CStrings:  3011
+  UUID: DFDEF81D-F896-356A-A4B0-92B2BD6A1216
+  Functions: 6108
+  Symbols:   1681
+  CStrings:  3551
 
Symbols:
+ _$s10Foundation13__DataStorageC12_deallocatorySv_SitcSgvg
+ _$s10Foundation4DataV7SPRCoreE4uuidAA4UUIDVSgvg
+ _$s10Foundation4DataV7SPRCoreE4uuidAcA4UUIDV_tcfC
+ _$s10Foundation4DataV7SPRCoreE8toUInt3210endiannesss0E0VAcDE10EndiannessO_tF
+ _$s10Foundation4DateV2eeoiySbAC_ACtFZ
+ _$s10Foundation4UUIDV2eeoiySbAC_ACtFZ
+ _$s10Foundation4UUIDV7SPRCoreE10halfDigestAA4DataVvg
+ _$s10Foundation4UUIDV7SPRCoreE16normalizedStringSSvg
+ _$s10Foundation4UUIDV7SPRCoreE9hexStringACSgSS_tcfC
+ _$s10Foundation4UUIDV7SPRCoreE9hexStringSSvg
+ _$s10Foundation8TimeZoneV14secondsFromGMT3forSiAA4DateV_tF
+ _$s10Foundation8TimeZoneV19autoupdatingCurrentACvgZ
+ _$s10Foundation8TimeZoneVMa
+ _$s15Synchronization5MutexVMa
+ _$s15Synchronization5MutexVMn
+ _$s15Synchronization5_CellVMa
+ _$s20KernelManagerLibrary10BeeServiceC12DeletionModeO6normalyA2EmFWC
+ _$s20KernelManagerLibrary10BeeServiceC12DeletionModeO8recoveryyA2EmFWC
+ _$s20KernelManagerLibrary10BeeServiceC12DeletionModeOMa
+ _$s20KernelManagerLibrary10BeeServiceC14evaluateAssets4with6assetsAA0G10EvaluationVAA17KMSessionProtocol_p_AA0dG0VtKFTj
+ _$s20KernelManagerLibrary10BeeServiceC14getDeviceState4with4typeAA07ProductH0VyAA0dH0VGAA17KMSessionProtocol_p_AA0gH4TypeOtKFTj
+ _$s20KernelManagerLibrary10BeeServiceC18executeServerAsset4with6assets8progressyAA17KMSessionProtocol_p_AA16AssetsEvaluationVySictYaKFTjTu
+ _$s20KernelManagerLibrary10BeeServiceC18getDefaultSEFWPath10Foundation3URLVyKFTj
+ _$s20KernelManagerLibrary10BeeServiceC18getMemoryFootprint4withAA12SEMemoryInfoVAA17KMSessionProtocol_p_tKFTj
+ _$s20KernelManagerLibrary10BeeServiceC18removeUnusedAssets4with4sefwyAA17KMSessionProtocol_p_10Foundation3URLVtKFTj
+ _$s20KernelManagerLibrary10BeeServiceC6delete4with4mode4sefwyAA17KMSessionProtocol_p_AC12DeletionModeO10Foundation3URLVtKFTj
+ _$s20KernelManagerLibrary10BeeServiceCACycfc
+ _$s20KernelManagerLibrary10BeeServiceCMa
+ _$s20KernelManagerLibrary10OasisStateV07stingerE0AA07StingerE0Vvg
+ _$s20KernelManagerLibrary10OasisStateV15configurationId10Foundation4DataVSgvg
+ _$s20KernelManagerLibrary10OasisStateV6statusAA12AppletStatusOvg
+ _$s20KernelManagerLibrary10OasisStateV7versionSSSgvg
+ _$s20KernelManagerLibrary10OasisStateVMa
+ _$s20KernelManagerLibrary10OasisStateVMn
+ _$s20KernelManagerLibrary11OasisAssetsV4sefw13configuration07stingerE0AC10Foundation3URLVSg_AjA07StingerE0VSgtcfC
+ _$s20KernelManagerLibrary11OasisAssetsVMa
+ _$s20KernelManagerLibrary12AppletStatusO10terminatedyA2CmFWC
+ _$s20KernelManagerLibrary12AppletStatusO11needsRepairyA2CmFWC
+ _$s20KernelManagerLibrary12AppletStatusO2eeoiySbAC_ACtFZ
+ _$s20KernelManagerLibrary12AppletStatusOMa
+ _$s20KernelManagerLibrary12AppletStatusOMn
+ _$s20KernelManagerLibrary12AppletStatusOs23CustomStringConvertibleAAMc
+ _$s20KernelManagerLibrary12KMTranscoderO11APDUCommandP10encodeAPDU10Foundation4DataVyKFTj
+ _$s20KernelManagerLibrary12KMTranscoderO12APDUResponseC4data10Foundation4DataVvg
+ _$s20KernelManagerLibrary12KMTranscoderO12APDUResponseC4fromAE10Foundation4DataV_tKcfc
+ _$s20KernelManagerLibrary12KMTranscoderO12APDUResponseC9isSuccessSbvgTj
+ _$s20KernelManagerLibrary12KMTranscoderO12APDUResponseCMa
+ _$s20KernelManagerLibrary12KMTranscoderO5OasisO19StartSessionCommandC6panKek03pinJ014allowedAIDList18additionalTagsListAG10Foundation4DataV_ANSayANGSgSays6UInt16VGSgtKcfc
+ _$s20KernelManagerLibrary12KMTranscoderO5OasisO19StartSessionCommandCAC11APDUCommandAAWP
+ _$s20KernelManagerLibrary12KMTranscoderO5OasisO19StartSessionCommandCMa
+ _$s20KernelManagerLibrary12OasisServiceC14evaluateAssets4with6assetsAA0G10EvaluationVAA17KMSessionProtocol_p_AA0dG0VtKFTj
+ _$s20KernelManagerLibrary12OasisServiceC14getDeviceState4withAA07ProductH0VyAA0dH0VGAA17KMSessionProtocol_p_tKFTj
+ _$s20KernelManagerLibrary12OasisServiceC18executeServerAsset4with6assetsyAA17KMSessionProtocol_p_AA16AssetsEvaluationVtYaKFTjTu
+ _$s20KernelManagerLibrary12OasisServiceCACycfc
+ _$s20KernelManagerLibrary12OasisServiceCMa
+ _$s20KernelManagerLibrary12ProductStateV5statexvg
+ _$s20KernelManagerLibrary12ProductStateV6seInfoAA6SEInfoVvg
+ _$s20KernelManagerLibrary12ProductStateV6statusAA0D6StatusOvg
+ _$s20KernelManagerLibrary12ProductStateVMn
+ _$s20KernelManagerLibrary12StingerStateV15configurationId10Foundation4DataVSgvg
+ _$s20KernelManagerLibrary12StingerStateV6statusAA12AppletStatusOvg
+ _$s20KernelManagerLibrary12StingerStateV7versionSSSgvg
+ _$s20KernelManagerLibrary12StingerStateVMa
+ _$s20KernelManagerLibrary12StingerStateVMn
+ _$s20KernelManagerLibrary13KMFeatureFlagO24isServiceProductionReadySbvgZ
+ _$s20KernelManagerLibrary13ProductStatusO2eeoiySbAC_ACtFZ
+ _$s20KernelManagerLibrary13ProductStatusO5readyyA2CmFWC
+ _$s20KernelManagerLibrary13ProductStatusOMa
+ _$s20KernelManagerLibrary13StingerAssetsV4sefw13configurationAC10Foundation3URLVSg_AItcfC
+ _$s20KernelManagerLibrary13StingerAssetsVMa
+ _$s20KernelManagerLibrary13StingerAssetsVMn
+ _$s20KernelManagerLibrary15DeviceStateTypeO6normalyA2CmFWC
+ _$s20KernelManagerLibrary15DeviceStateTypeO7minimalyA2CmFWC
+ _$s20KernelManagerLibrary15DeviceStateTypeOMa
+ _$s20KernelManagerLibrary16AssetsEvaluationV14requiredMemoryAA12SEMemoryInfoVvg
+ _$s20KernelManagerLibrary16AssetsEvaluationVMa
+ _$s20KernelManagerLibrary17KMSessionProtocolMp
+ _$s20KernelManagerLibrary17KMSessionProtocolP10transceivey10Foundation4DataVAGKFTj
+ _$s20KernelManagerLibrary17KMSessionProtocolP10transceivey10Foundation4DataVAGKFTq
+ _$s20KernelManagerLibrary6SEInfoV12hardwareTypeSivg
+ _$s20KernelManagerLibrary6SEInfoV19jsblSequenceCounterSSvg
+ _$s20KernelManagerLibrary6SEInfoVMa
+ _$s20KernelManagerLibrary8BeeStateV07stingerE0AA07StingerE0Vvg
+ _$s20KernelManagerLibrary8BeeStateV15configurationId10Foundation4DataVSgvg
+ _$s20KernelManagerLibrary8BeeStateV16terminalProfilesSay10Foundation4DataVGSgvg
+ _$s20KernelManagerLibrary8BeeStateV5capksSDys5UInt8V10Foundation4DataVGSgvg
+ _$s20KernelManagerLibrary8BeeStateV6statusAA12AppletStatusOvg
+ _$s20KernelManagerLibrary8BeeStateVMa
+ _$s20KernelManagerLibrary8BeeStateVMn
+ _$s20KernelManagerLibrary9BeeAssetsV4sefw12updatedAsset9kernelMap19configurationScript11capkScripts015terminalProfileN007stingerE0AC10Foundation3URLV_SbAK4DataVAMSgSayAMGSgSayAA0pL0VGSgAA07StingerE0VSgtcfC
+ _$s20KernelManagerLibrary9BeeAssetsVMa
+ _$s20KernelManagerLibrary9BeeAssetsVMn
+ _$s7SPRCore3TLVV3tag5uint8AcA6TLVTagV_s5UInt8VtcfC
+ _$s7SPRCore6TLVTagV21eventPICCResponseTimeACvgZ
+ _$s7SPRCore6TLVTagV30provisionAppletAttestationDataACvgZ
+ _$s8Dispatch0A11SpecificKeyCACyxGycfc
+ _$s8Dispatch0A11SpecificKeyCMn
+ _$s8Dispatch0A12TimeIntervalO7secondsyACSicACmFWC
+ _$s8Dispatch0A4TimeVSLAAMc
+ _$s8Dispatch1poiyAA0A4TimeVAD_AA0aB8IntervalOtF
+ _$sSC16SPRHTTPErrorCodeLeV13SoftPosReaderE12serverReasonSSSgvg
+ _$sSL1goiySbx_xtFZTj
+ _$sSS21_builtinStringLiteral17utf8CodeUnitCount7isASCIISSBp_BwBi1_tcfC
+ _$sSS7SPRCoreE9shortenedySSSi_SitF
+ _$sScA15unownedExecutorScevgTq
+ _$sScAMp
+ _$sScC12continuation8functionScCyxq_GSccyxq_G_SStcfC
+ _$sScC6resume8throwingyq_n_tF
+ _$sScC6resume9returningyxn_tF
+ _$sScT6cancelyyF
+ _$sScT6results6ResultOyxq_Gvg
+ _$sScT6results6ResultOyxq_GvgTu
+ _$sScTss5NeverORszABRs_rlE11isCancelledSbvgZ
+ _$sScTss5NeverORszABRs_rlE5sleep11nanosecondsys6UInt64V_tYaKFZ
+ _$sScTss5NeverORszABRs_rlE5sleep11nanosecondsys6UInt64V_tYaKFZTu
+ _$sScg4next9isolationxSgScA_pSgYi_tYaKF
+ _$sScg4next9isolationxSgScA_pSgYi_tYaKFTu
+ _$sScg9cancelAllyyF
+ _$sScs12ContinuationV11YieldResultOMn
+ _$sScs12ContinuationV15BufferingPolicyO9unboundedyADyxq___GAFms5ErrorR_r0_lFWC
+ _$sScs12ContinuationV15BufferingPolicyOMn
+ _$sScs12ContinuationV5yieldyAB11YieldResultOyxq___GxnF
+ _$sScs12ContinuationV6finish8throwingyq_Sgn_tF
+ _$sScs12ContinuationVMn
+ _$sScs12ContinuationVyxq__GSQsMc
+ _$sScs17makeAsyncIteratorScs0C0Vyxq__GyF
+ _$sScs8IteratorV4nextxSgyYaKF
+ _$sScs8IteratorV4nextxSgyYaKFTu
+ _$sScs8IteratorVMn
+ _$sScs_15bufferingPolicy_Scsyxs5Error_pGxm_Scs12ContinuationV09BufferingB0OyxsAB_p__GyAEyxsAB_p_GXEtcsAB_pRs_rlufC
+ _$sSd7SPRCoreE9shortWaitSdvgZ
+ _$sSo12NSURLSessionC10FoundationE8download3for8delegateAC3URLV_So13NSURLResponseCtAC10URLRequestV_So0A12TaskDelegate_pSgtYaKF
+ _$sSo12NSURLSessionC10FoundationE8download3for8delegateAC3URLV_So13NSURLResponseCtAC10URLRequestV_So0A12TaskDelegate_pSgtYaKFTu
+ _$sSo17NFHardwareManagerC7SPRCoreE018startSecureElementB7Session7timeoutSo08NFSecurefbG0CSd_tYaKF
+ _$sSo17NFHardwareManagerC7SPRCoreE018startSecureElementB7Session7timeoutSo08NFSecurefbG0CSd_tYaKFTu
+ _$sSo17NFHardwareManagerC7SPRCoreE31startSecureElementReaderSession7timeoutSo08NFSecurefgH0CSd_tYaKF
+ _$sSo17NFHardwareManagerC7SPRCoreE31startSecureElementReaderSession7timeoutSo08NFSecurefgH0CSd_tYaKFTu
+ _$sSo17OS_dispatch_queueC8DispatchE11getSpecific3keyxSgAC0dF3KeyCyxG_tlFZ
+ _$sSo17OS_dispatch_queueC8DispatchE11setSpecific3key5valueyAC0dF3KeyCyxG_xSgtlF
+ _$sSo17OS_dispatch_queueCSch8DispatchMc
+ _$sSo24OS_dispatch_queue_serialC8DispatchE10AttributesVMa
+ _$sSo24OS_dispatch_queue_serialC8DispatchE10AttributesVMn
+ _$sSo24OS_dispatch_queue_serialC8DispatchE10AttributesVs10SetAlgebraACMc
+ _$sSo24OS_dispatch_queue_serialC8DispatchE5label3qos10attributes20autoreleaseFrequency6targetABSS_AC0E3QoSVAbCE10AttributesVSo0a1_b1_C0CACE011AutoreleaseJ0OANSgtcfC
+ _$sSo33OS_dispatch_queue_serial_executorC8DispatchE23asUnownedSerialExecutorSceyF
+ _$sSo9SPRLoggerC7SPRCoreE13unifiedReader2os6LoggerVvgZ
+ _$sSo9SPRLoggerC7SPRCoreE6logger8category2os6LoggerVSS_tFZ
+ _$sSo9SPRLoggerC7SPRCoreE9inspector2os6LoggerVvgZ
+ _$sSp12deinitialize5countSvSi_tF
+ _$ss15ContinuousClockV7InstantVMa
+ _$ss15ContinuousClockV7InstantVs0C8ProtocolsMc
+ _$ss15ContinuousClockVMa
+ _$ss15ContinuousClockVs0B0sMc
+ _$ss15InstantProtocolP8advanced2byx8DurationQz_tFTj
+ _$ss21withThrowingTaskGroup2of9returning9isolation4bodyq_xm_q_mScA_pSgYiq_Scgyxs5Error_pGzYaKXEtYaKs8SendableRzr0_lF
+ _$ss21withThrowingTaskGroup2of9returning9isolation4bodyq_xm_q_mScA_pSgYiq_Scgyxs5Error_pGzYaKXEtYaKs8SendableRzr0_lFTu
+ _$ss22KeyedDecodingContainerV6decode_6forKeys6UInt16VAFm_xtKF
+ _$ss22KeyedEncodingContainerV6encode_6forKeyys6UInt16V_xtKF
+ _$ss5ClockP3now7InstantQzvgTj
+ _$ss5ClockP5sleep5until9tolerancey7InstantQz_8DurationQzSgtYaKFTj
+ _$ss5ClockP5sleep5until9tolerancey7InstantQz_8DurationQzSgtYaKFTjTu
+ _$ss5ClockPss010ContinuousA0VRszrlE10continuousADvgZ
+ _$ss5Int32Vs7CVarArgsWP
+ _$ss5NeverOMn
+ _$ss5NeverON
+ _$ss5NeverOs5ErrorsWP
+ _$ss6ResultOMn
+ _$ss6UInt64VSUsMc
+ _$ss8DurationV7secondsyABSdFZ
+ _DCErrorDomain
+ _MobileActivationErrorDomain
+ _NFCDErrorDomain
+ _OBJC_CLASS_$_CTTelephonyNetworkInfo
+ _OBJC_CLASS_$_CWFInterface
+ _OBJC_CLASS_$_OS_dispatch_queue_serial
+ _OBJC_CLASS_$_SPRCellSignalMonitor
+ _OBJC_CLASS_$_SPRUnifiedReaderAppletStatus
+ _OBJC_CLASS_$_SPRUnifiedReaderPINData
+ _OBJC_CLASS_$_SPRUnifiedReaderPINParameter
+ _OBJC_CLASS_$_SPRUnifiedReaderReadParameters
+ _OBJC_CLASS_$_SPRUnifiedReaderTransactionData
+ _SPRCardReaderBlobAuthToken
+ _SPRErrorUserInfoKeyDeviceProtectionTimerDuration
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
+ _SecItemUpdate
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _kSecAttrAccessGroup
+ _kSecAttrAccessible
+ _kSecAttrAccount
+ _kSecAttrLabel
+ _kSecAttrService
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecMatchLimit
+ _kSecMatchLimitAll
+ _kSecMatchLimitOne
+ _kSecReturnAttributes
+ _kSecReturnData
+ _kSecValueData
+ _localtime
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_resume
+ _swift_deallocUninitializedObject
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedAsyncMethodErrorTu
+ _swift_dynamicCastObjCProtocolConditional
+ _swift_getDynamicType
+ _swift_release_x1
+ _swift_release_x13
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x3
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x1
+ _swift_retain_x10
+ _swift_retain_x13
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_task_addCancellationHandler
+ _swift_task_removeCancellationHandler
+ _swift_unknownObjectWeakAssign
- _$s10Foundation10CocoaErrorV19fileWriteFileExistsAC4CodeVvgZ
- _$s10Foundation12DateIntervalV5start8durationAcA0B0V_SdtcfC
- _$s10Foundation12DateIntervalV8durationSdvg
- _$s10Foundation4DataV15_RepresentationOys5UInt8VSicis
- _$s10Foundation4DateVSQAAMc
- _$s10Foundation6LocaleV10identifierACSS_tcfC
- _$s10Foundation6LocaleV19_bridgeToObjectiveCSo8NSLocaleCyF
- _$s20KernelManagerLibrary0aB0C13useLegacyFlowSbvgTj
- _$s20KernelManagerLibrary0aB0C18getDefaultSEFWPath12isProductionSSSb_tFZ
- _$s20KernelManagerLibrary12BeeStateInfoC12SystemStatusO11descriptionSSvg
- _$s9SEService10SESnapshotC18ProposedKernelInfoV11descriptionSSvg
- _$s9SEService10SESnapshotC18ProposedKernelInfoVMn
- _$sSL2geoiySbx_xtFZTj
- _$sSS6insert_2atySJ_SS5IndexVtF
- _$sSW10Foundation15ContiguousBytesAAWP
- _$sSayxG10Foundation15ContiguousBytesABs5UInt8VRszlMc
- _$sSo25SPRPaymentApplicationTypeV13SoftPosReaderE11descriptionSSvg
- _$sSw10Foundation15ContiguousBytesAAWP
- _$sSwN
- _$ss11_MergeErrorON
- _$ss11_MergeErrorOs0B0sWP
- _$ss11_StringGutsV16_slowWithCStringyxxSPys4Int8VGKXEKlF
- _$ss15CollectionOfOneVyxG10Foundation15ContiguousBytesADs5UInt8VRszlMc
- _$ss15ContiguousArrayV28_allocateBufferUninitialized15minimumCapacitys01_abD0VyxGSi_tFZ
- _$ss22_minimumMergeRunLengthyS2iF
- _OBJC_CLASS_$_NSDateFormatter
- _OBJC_CLASS_$_NSPersistentStore
- _OBJC_METACLASS_$_NSManagedObject
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _swift_stdlib_isStackAllocationSafe
CStrings:
+ " Error on GET provision attestation data: "
+ " Error on GET provision data blob: "
+ " disruptPersistence="
+ "$__lazy_storage_$_baaUnifiedReader"
+ "$__lazy_storage_$_encryptedPayloadsUnifiedReader"
+ "$__lazy_storage_$_migrationManager"
+ "$defaultActor"
+ "%s does not support %s SEFW targets"
+ "%s event ignored while EMV polling"
+ "%s isDailyCollectionEnabled: %{bool}d"
+ "%s isProductionAnalytics: %{bool}d"
+ "%s key: %s expired, was removed"
+ "%s removed value for key: %s"
+ "%s updated value for key: %s"
+ "%s updated value for key: %s with lifetime: %f s"
+ "%s.%s Unified Reader using QA5 for Dev SE device"
+ "%s.%s [already in queue]"
+ "%s.%s error: %s"
+ "%s.%s primary verifier failed: %@, trying fallback"
+ "%s.%s using PIN context with transactionID: %s"
+ "%s: Client attached. currentAttachCount: (%ld)"
+ "%s: Detaching client. currentAttachCount: (%ld)"
+ "%s: Error starting TimeTokenManager instance: %@"
+ "%s: Found active cellular RAT=%s"
+ "%s: Missing MPOCMonitorManager instance: %@"
+ "%s: TimeTokenManager %s"
+ ", aaaCertificateAutoRefreshOverride="
+ ", allowExpiredCertificates="
+ ", baaCertificateAutoRefreshOverride="
+ ", beeAppletScript: "
+ ", certificateExpirationThreshold="
+ ", enableTrustedWallTime="
+ ", osVersionHistory: "
+ ", seabaasCertificateAutoRefreshOverride="
+ ", stingerAppletScript: "
+ ", stingerConfig: "
+ ", transactionIDHalf: "
+ ", unifiedReaderBaaCertificateAutoRefreshOverride="
+ ", wallTimeOffsetForUnifiedReaderTimeKeeper="
+ "-----BEGIN CERTIFICATE-----\nMIID3zCCA4WgAwIBAgIIUYtb0WaKqTcwCgYIKoZIzj0EAwIwfzEzMDEGA1UEAwwq\nVGVzdCBBcHBsZSBBcHBsaWNhdGlvbiBJbnRlZ3JhdGlvbiBDQSAtIEczMSYwJAYD\nVQQLDB1BcHBsZSBDZXJ0aWZpY2F0aW9uIEF1dGhvcml0eTETMBEGA1UECgwKQXBw\nbGUgSW5jLjELMAkGA1UEBhMCVVMwHhcNMjMwOTEyMTU1MDM2WhcNMjUxMDExMTU1\nMDM1WjBfMRQwEgYDVQQDDAtoaXZlaHBrZXFhMjElMCMGA1UECwwcMS4yLjg0MC4x\nMTM2MzUuMTAwLjYuNjQuMTIuMTETMBEGA1UECgwKQXBwbGUgSW5jLjELMAkGA1UE\nBhMCVVMwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATtXFxXGyYnxy5S+5+2miJW\nmuk5YZi0qc1SLJC7vBaq/3yykMzUyp4qyUkWWEoHNGr6ZX896ohCC6PBqStiCAKw\no4ICCTCCAgUwDAYDVR0TAQH/BAIwADAfBgNVHSMEGDAWgBS5BBqVW2uRBDnqcCpH\nt6hJNuRN2zBNBggrBgEFBQcBAQRBMD8wPQYIKwYBBQUHMAGGMWh0dHA6Ly9vY3Nw\nLXVhdC5jb3JwLmFwcGxlLmNvbS9vY3NwMDMtdHNhYWljYWczMDgwggEDBgNVHSAE\ngfswgfgwgfUGCSqGSIb3Y2QFATCB5zCBrAYIKwYBBQUHAgIwgZ8MgZxSZWxpYW5j\nZSBvbiB0aGlzIGNlcnRpZmljYXRlIGJ5IGFueSBwYXJ0eSBpcyBzdWJqZWN0IHRv\nIHRoZSBDZXJ0aWZpY2F0ZSBQb2xpY3ksIENlcnRpZmljYXRpb24gUHJhY3RpY2Ug\nU3RhdGVtZW50LCBhbmQgdGhlIHRlcm1zIG9mIGFueSBhcHBsaWNhYmxlIGFncmVl\nbWVudC4wNgYIKwYBBQUHAgEWKmh0dHA6Ly93d3cuYXBwbGUuY29tL2NlcnRpZmlj\nYXRlYXV0aG9yaXR5LzA8BgNVHR8ENTAzMDGgL6AthitodHRwOi8vY3JsLXVhdC5j\nb3JwLmFwcGxlLmNvbS90c2FhaWNhZzMuY3JsMB0GA1UdDgQWBBSWaSKme5t08ywQ\n3jppFujlEOnWvjAOBgNVHQ8BAf8EBAMCAygwEQYLKoZIhvdjZAZADAEEAgUAMAoG\nCCqGSM49BAMCA0gAMEUCICxoqq6zg0pGDGt4cPc0PAatNUVTQQJMhGXDMmxwgYgE\nAiEAyLyDxl+yCGmAEACqk9LPS/0ZIZJCLUf5QGMlQyZXEq8=\n-----END CERTIFICATE-----"
+ "-----BEGIN CERTIFICATE-----\nMIIDFzCCAp6gAwIBAgIIW33OkDJ3NNYwCgYIKoZIzj0EAwMwbDEgMB4GA1UEAwwX\nVGVzdCBBcHBsZSBSb290IENBIC0gRzMxJjAkBgNVBAsMHUFwcGxlIENlcnRpZmlj\nYXRpb24gQXV0aG9yaXR5MRMwEQYDVQQKDApBcHBsZSBJbmMuMQswCQYDVQQGEwJV\nUzAeFw0xNzA1MzAyMTM1NTVaFw0zMjA1MjYyMTM1NTVaMH8xMzAxBgNVBAMMKlRl\nc3QgQXBwbGUgQXBwbGljYXRpb24gSW50ZWdyYXRpb24gQ0EgLSBHMzEmMCQGA1UE\nCwwdQXBwbGUgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkxEzARBgNVBAoMCkFwcGxl\nIEluYy4xCzAJBgNVBAYTAlVTMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE+tzM\nERB0ezDEad1lw9qhVd/rCVwp0FA+HAo0+oOxeUlNnbO5RqHJQ2ezA0XTpAFgw1jb\nmIMZMs7Fo2g4tspNY6OCARUwggERMFMGCCsGAQUFBwEBBEcwRTBDBggrBgEFBQcw\nAYY3aHR0cDovL29jc3AtdWF0LmNvcnAuYXBwbGUuY29tL29jc3AwNC10ZXN0YXBw\nbGVyb290Y2FnMzAdBgNVHQ4EFgQUuQQalVtrkQQ56nAqR7eoSTbkTdswEgYDVR0T\nAQH/BAgwBgEB/wIBADAfBgNVHSMEGDAWgBT8RtiDbB/m8tzfp5kXrgtEZxcbRjBE\nBgNVHR8EPTA7MDmgN6A1hjNodHRwOi8vY3JsLXVhdC5jb3JwLmFwcGxlLmNvbS90\nZXN0YXBwbGVyb290Y2FnMy5jcmwwDgYDVR0PAQH/BAQDAgEGMBAGCiqGSIb3Y2QG\nAg4EAgUAMAoGCCqGSM49BAMDA2cAMGQCMGomDSqAzWkz71C7eLwXTM2ma4bihtPn\nPcOPAdiD5sgcfed4yv0p1foyY5jbZRcuBQIwTdcxMvoXc1CctgQdyqYfYApyWW1/\nyVuTShNAYK5sE0PSccLdMqqQqcXi3TIjL6ra\n-----END CERTIFICATE-----"
+ ".appendEvent(%s), hex: %s"
+ "01010202030304040505060607070D0D0E0E0F0F2A02E00DE202E303E402E502E603E70FE802E905EA02EB06EC03ED0FEF01EE01"
+ "041111111111111111111111111111111111111111111111"
+ "1.2.840.113635.100.19.1.1.3.5"
+ "35679898-f99b-4c4f-9e9b-186ee2d41c0f"
+ "485773EED56EFD3DFB948F04133C37446D062281E36AD5A8AD4177DA485B6154"
+ "485773EED56EFD3DFB948F04133C37446D062281E36AD5A8AD4177DA485B6155"
+ "70fae92b-643d-4904-8fc3-16ed2d6b85c7"
+ "@24@0:8@?16"
+ "@24@0:8@?<v@?@\"NSError\">16"
+ "ATTESTATION"
+ "Aborting identity #%lld renewal. Could not get secure now from UnifiedReaderTimeKeeper"
+ "Amount was too many digits"
+ "An applet is %s installed. payAppletConfigID: %s, encryptionAppletConfigID: %s, profileID: %s, 2nd profile ID: %s"
+ "Backend communication"
+ "BeeServiceWrapperProtocol"
+ "BeeServiceWrapperProtocol: independent"
+ "CALoggerProtocol: independent"
+ "CAPDU (START SESSION): %{public}s"
+ "CONFIGURATION"
+ "CTRadioAccessTechnology"
+ "Cannot decode backend response"
+ "Cannot decode backend response: %@"
+ "Cannot get a trusted wall time and there was no persisted time data to infer from"
+ "Cannot parse backend response"
+ "Cannot parse backend response: %@"
+ "Cannot parse provisionDataBlob for analytics: %@"
+ "Card provisioning applet Config ID: %{public}s"
+ "Certificate is expired but can be used"
+ "Certificate verification failed: %s"
+ "Certificate(s) expire before time required for SAF: %ld seconds. Begin renewal."
+ "CertificateManagerProtocol: independent"
+ "CertificateVerifierFactoryProtocol: independent"
+ "Cleaning the SE"
+ "Communicate with backend failed after "
+ "ComponentAuditorFactoryProtocol: independent"
+ "ConfiguratorAnalytics: independent"
+ "ConfiguratorBackendProtocol: independent"
+ "Content-Type"
+ "Core Data migration failed: %s"
+ "Core Data to Keychain migration completed successfully"
+ "Could not calculate secure now. Missing trusted time and time token."
+ "Could not decode Kernel Type"
+ "Could not encode date and time into BCD"
+ "Could not get cpu time from token claims"
+ "Could not get secure now"
+ "Could not get secure time from secureTimeKeeper, scheduling immediate renewal"
+ "Could not parse JSBLSequenceCounter from "
+ "Could not parse or store the certificate"
+ "Could not provide the device protection timer duration: %@"
+ "Create Secure Reader Blob Failed"
+ "Created SEFW file at: %s"
+ "Creating keychain persistence with service: %s"
+ "DISRUPT_DELETE_KEY"
+ "DISRUPT_LOAD_KEY"
+ "DISRUPT_SAVE_KEY"
+ "DefaultAsyncSecureChannelHTTP.download network error: %@"
+ "DefaultAsyncSecureChannelHTTP.download: Received HTTP error %ld"
+ "DefaultAsyncSecureChannelHTTP.download: Success. Received location"
+ "DefaultSecureChannelHTTP.data network error: %@"
+ "DefaultSecureChannelHTTP.data: Received HTTP error %ld"
+ "DefaultSecureChannelHTTP.data: Success. Received payload"
+ "DefaultSecureChannelHTTP.downloadTask network error: %@"
+ "DefaultSecureChannelHTTP.downloadTask: Success. Received payload"
+ "DefaultSecureChannelHTTP.ownloadTask: Received HTTP error %ld"
+ "Delete failed: %@"
+ "Deleted legacy Core Data file: %s"
+ "Deleted maformed identity: %@"
+ "Device rebooted, could not infer from previous time pairing data"
+ "Device.Compute.Zap"
+ "DeviceTimeAnalytics"
+ "DeviceTimeAnalytics: independent"
+ "EnableAsyncImplementation"
+ "EnableKernelManagerV2"
+ "EnableOasisAppletV2"
+ "Encrypted payloads cert fingerprint: %s"
+ "Encrypted payloads certificate not available from cache: %@"
+ "EnvironmentProtocol: independent"
+ "Error calculating secure time using the time token: %@"
+ "Error during request to backend: %@"
+ "Error from NSFileManager.removeItem: %@"
+ "Error from clearTransactionData: %@"
+ "Error from generatePINBlock: %@"
+ "Error from session stopEMV: %@"
+ "Error from startEMV: "
+ "Error re-signing universal secure channel request: %s"
+ "Error refreshing signer: %@"
+ "Error refreshing signer: network error"
+ "Error related to Secure Element"
+ "Error signing universal secure channel request: %s"
+ "Failed to convert key string to data: %s"
+ "Failed to delete BAA key and certificate: %@"
+ "Failed to delete legacy Core Data file %s: %s"
+ "Failed to delete maformed identity: %@"
+ "Failed to delete stored SES key. %@"
+ "Failed to delete the applets from the SE. %@"
+ "Failed to delete the identity"
+ "Failed to delete the identity: %@"
+ "Failed to encode persistence key for %s"
+ "Failed to encode request: "
+ "Failed to encode request: %@"
+ "Failed to execute install scripts"
+ "Failed to execute install scripts: %@"
+ "Failed to get product state: %@"
+ "Failed to get secure time: %@"
+ "Failed to migrate key %s: %s"
+ "Failed to parse certificate chain"
+ "Failed to parse stored certificate chain from PEM"
+ "Failed to refresh AsyncSecureChannel crypto: %@"
+ "Failed to remove file %s: %@"
+ "Failed to resolve ECDSA certificate from secure element"
+ "Failed to retrieve stored time data: %@"
+ "Failed to store secure time data: %@"
+ "Found saved temp SEFW for %s at: %s"
+ "Generating new Kernel assets:\nPay applet updated asset: %{bool}d Encryption applet updated asset: %{bool}d"
+ "Get certificate from SESKeyAttest failed"
+ "Get certificate from SESKeyAttest failed: %@"
+ "HCI event: OUT_OPS_UIRD: OPS only: %s"
+ "HTTP error: %@, server code: %s, user info: %s"
+ "Install scripts executed successfully"
+ "Install scripts provided, executing..."
+ "Invalid PAN KEK format in LRP config"
+ "Invalid PAN KEK hash"
+ "Invalid PIN KEK format in LRP config"
+ "Invalid PIN KEK hash"
+ "Invalid URL response"
+ "Invalid or empty install script data"
+ "Key data is not valid UTF-8"
+ "Key not found in Core Data, skipping: %s"
+ "Keychain deleteAfterUpdate failed with status: "
+ "Keychain deletion failed with status: "
+ "Keychain item already exists for key: "
+ "Keychain item not found for key: %s"
+ "Keychain retrieval failed with status: "
+ "Keychain storage failed with status: "
+ "Keychain update failed with status: "
+ "KeychainManager initialized with service: %s"
+ "KeychainManager: independent"
+ "KeychainWrapper: Deletion error for key: %s, status: %d"
+ "KeychainWrapper: Failed to delete key: %s, status: %d"
+ "KeychainWrapper: Failed to retrieve data for key: \"%s\""
+ "KeychainWrapper: Retrieval error for key: %s, status: %d"
+ "KeychainWrapper: Storage error for key: %s, status: %d"
+ "KeychainWrapper: Update error for key: %s, status: %d"
+ "KeychainWrapper: Using persistent keychain storage with service: %s"
+ "KeychainWrapper: deleteAfterUpdate error, status: %d"
+ "KeychainWrapper: key: \"%s\" does not exist, cannot delete"
+ "LRPConfig is not available"
+ "LaunchFeedbackFrameworkProtocol: independent"
+ "Legacy Core Data store found, starting migration to Keychain"
+ "MFD.PersistApplets"
+ "MONITORING"
+ "MPOCAttestationDataProtocol: independent"
+ "MPOCAttestationManagerProtocol: independent"
+ "MPOCAttestationOfflineVerifierProtocol: independent"
+ "MPOCMonitorBackendProtocol: independent"
+ "MPOCMonitorLoggerProtocol: independent"
+ "MPOCMonitorManagerProtocol: independent"
+ "MUIRFIELD"
+ "ManagedDictionaryProtocol: independent"
+ "Mastercard PayPass"
+ "Mismatched transaction ID"
+ "Missing config in the OTA response for the encryption applet."
+ "Missing config in the OTA response for the pay applet."
+ "Missing persisted wall time, using current secureWallTime"
+ "Missing transaction data"
+ "MonitorAnalytics: independent"
+ "NF session ended in endPINCapture()"
+ "NSXPCProxyCreating"
+ "No URL for target: %s, type: %s"
+ "No cached product state, fetching fresh state"
+ "No destination URL for %s"
+ "No destination for target: %s, type: %s"
+ "No encryption applet config update available"
+ "No encryption applet update available"
+ "No install scripts provided"
+ "No legacy Core Data files found, skipping migration"
+ "No managed dictionary instance"
+ "No pay applet config update available"
+ "No pay applet update available"
+ "No previous system version found, storing current version: %s"
+ "No saved temp SEFW file found for %s"
+ "No secure wall time available"
+ "No stored %s certificate found"
+ "OASIS"
+ "OS version history: %s"
+ "OS_os_transaction"
+ "OasisServiceWrapperProtocol"
+ "OasisServiceWrapperProtocol: independent"
+ "OasisState(version: "
+ "OpenSessionRequest("
+ "OpenSessionResponse("
+ "Overriding #%lld certificate renewal time."
+ "PAN KEK must be between 20 and 32 bytes, got "
+ "PICC Response Time: type=%hhu, responseTime=%u, kernelId=%hhu"
+ "PIN Context after MANAGE TAP: %s"
+ "PIN Context in Capture PIN: %s"
+ "PIN KEK must be between 20 and 32 bytes, got "
+ "PIN context coming from managed data"
+ "PIN context coming from parameters"
+ "PIN context was not decodable"
+ "PIN context was not retrievable"
+ "PIN timer already started"
+ "PIN timer started"
+ "PIN_CONTROLLER"
+ "PayAppletScript: %{public}s, PayAppletConfig: %{public}s, PartnerConfig: %{public}s, PartnerSAFConfig: %{public}s, EncryptionAppletScript: %{public}s, EncryptionAppletConfig: %{public}s,"
+ "PayAppletTagParserProtocol: independent"
+ "Payload too large"
+ "Performing an SE cleanup"
+ "Persistence %s was disrupted!!"
+ "Persistence cleared and system version updated"
+ "Persistence.Volatile.DisruptPersistence"
+ "PersistenceFactory initialized with keychain service: %s"
+ "PersistenceFactoryProtocol: independent"
+ "Primer.attach() SecureElement error: %@"
+ "Processing Encryption applet config (%ld chars), id: %s"
+ "Processing Encryption applet script (%ld chars)"
+ "Processing Unified Reader applet config (%ld chars), id: %s"
+ "Processing Unified Reader applet script (%ld chars)"
+ "Product state retrieved: %s, %s"
+ "ProfileManagerProtocol: independent"
+ "Provision operation cancelled: %s"
+ "READER"
+ "RSSI"
+ "ReaderAnalytics: independent"
+ "Received MFD event notification (ignored)"
+ "Received a malformed payload certificate"
+ "Received malformed pin certificates"
+ "Removed temporary file: %s"
+ "Removing %s firmware of type %s"
+ "Request payload size: %ld bytes"
+ "Request signed with %s. traceId: %{public}s, spanId: %{public}s"
+ "Response decoded: %s"
+ "Response received in %s.%s"
+ "SE-SEP is not paired"
+ "SECURE_CHANNEL"
+ "SEManagerSession(nfSession: "
+ "SEReaderSession(nfSession: "
+ "SESnapshotWrapperProtocol: independent"
+ "SPRFeatures.EnableOasisAppletV2 not enabled"
+ "SPRMPOCMonitorManagerXPCProxy"
+ "SPRUnifiedReaderDelegate"
+ "SPRUnifiedReaderFoundationXPCProxy"
+ "SPRUnifiedReaderPINControllerXPCProxy"
+ "SPRUnifiedReaderXPCProxy"
+ "STINGER"
+ "Saved %s firmware to %s"
+ "Secure Wall Time is: %s"
+ "Secure wall time not available"
+ "SecureChannelCryptoFactoryProtocol: independent"
+ "SecureChannelFactoryProtocol: independent"
+ "SecureChannelHTTPFactoryProtocol"
+ "SecureChannelHTTPFactoryProtocol: independent"
+ "SecureElementProtocol: independent"
+ "SecureElementTransceiver+PIN trxIdHalf: %s"
+ "SecureTimeKeeper: independent"
+ "SecureTimeProvider returned: %s"
+ "Security.AllowExpiredCertificates"
+ "Security.CertificateExpirationThreshold"
+ "Security.CertificateRenewalPeriod.AAA.AutoRefreshOverride"
+ "Security.CertificateRenewalPeriod.BAA.AutoRefreshOverride"
+ "Security.CertificateRenewalPeriod.BAA.UnifiedReader.AutoRefreshOverride"
+ "Security.CertificateRenewalPeriod.SEABAAS.AutoRefreshOverride"
+ "SecurityAnalytics: independent"
+ "Sending open session request to authorization endpoint"
+ "Session startedByApplet - onUpdate(with: .cardTear)"
+ "Session startedByReader - onUpdate(with: .ready)"
+ "SignerFactoryProtocol: independent"
+ "SoftPosReader.sqlite-shm"
+ "SoftPosReader.sqlite-wal"
+ "StingerState(version: "
+ "Stinger_OTA.sefw"
+ "Storage folder created at: %s"
+ "Storing UnifiedReader certificate chain, leaf fingerprint: %s"
+ "Successfully deleted %ld legacy Core Data files: %s"
+ "Successfully retrieved keychain value for key: %s, size: %ld bytes"
+ "Successfully stored keychain value for key: %s"
+ "Successfully updated keychain value for key: %s"
+ "Suite '%s' dictionary has no settings"
+ "Suite '%s' settings: %s"
+ "System version changed from %s to %s, clearing persistence"
+ "System version unchanged: %s"
+ "SystemInfoProtocol: independent"
+ "TMGetReferenceTime is unreliable and inferred wall time cannot be obtained due to a device reboot"
+ "Testing.WallTimeOffsetForUnifiedReaderTimeKeeper"
+ "The %s SEFW file is located at: %s"
+ "TimeKeeper: independent"
+ "TimeTokenManagerFactoryProtocol"
+ "TimeTokenManagerFactoryProtocol: independent"
+ "TrustedWallTime.Enabled"
+ "Unable to obtain secure wall time for retry"
+ "Unable to retrieve device state from Secure Element"
+ "Unable to retrieve reliable wall time from SecureTimeProvider"
+ "Unexpected ErrorIndication length"
+ "Unexpected JSON object"
+ "Unified reader certificate chain length: %ld"
+ "UnifiedReaderAnalytics"
+ "UnifiedReaderAnalytics: independent"
+ "UnifiedReaderBAASigner[owner: "
+ "UnifiedReaderBAASigner[role: "
+ "UnifiedReaderBackendProtocol"
+ "UnifiedReaderBackendProtocol: independent"
+ "UnifiedReaderCertificateManagerProtocol"
+ "UnifiedReaderCertificateManagerProtocol: independent"
+ "UnifiedReaderPINCapture"
+ "UnifiedReaderPINContext(\ntransactionID: "
+ "UnifiedReaderPINController[isPINCaptureInProgress="
+ "UnifiedReaderTimeKeeper"
+ "UnifiedReaderTimeKeeper\nBase Secure Wall Time: %s"
+ "UnifiedReaderTimeKeeper: independent"
+ "UnifiedReaderTimeKeeperState"
+ "UniversalSecureChannel.securingRequest(url: %s, %sstrategy: %s\n)"
+ "UniversalSecureChannelFactoryProtocol"
+ "UniversalSecureChannelFactoryProtocol: independent"
+ "Using cached product state"
+ "Using the legacy kernel manager to perform an install..."
+ "VTIDIdentityManagerProtocol"
+ "VTIDIdentityManagerProtocol: independent"
+ "VTIDIdentityManager_cache"
+ "Vv24@0:8@?<v@?@\"<SPRMPOCMonitorManagerXPCProxy>\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"<SPRUnifiedReaderFoundationXPCProxy>\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"<SPRUnifiedReaderPINControllerXPCProxy>\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"<SPRUnifiedReaderXPCProxy>\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"SPRMemoryInfo\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"SPRUnifiedReaderAppletStatus\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"SPRUnifiedReaderPINData\"@\"NSError\">16"
+ "Vv28@0:8B16@?<v@?B@\"NSError\">20"
+ "Vv32@0:8@\"<SPRNFSessionProxyInterface>\"16@?<v@?@\"SPRMemoryInfo\"@\"NSError\">24"
+ "Vv32@0:8@\"NSDictionary\"16@?<v@?@\"<SPRUnifiedReaderFoundationXPCProxy>\"@\"NSDictionary\"@\"NSError\">24"
+ "Vv32@0:8@\"SPRUnifiedReaderPINParameter\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"@\"NSError\">24"
+ "Vv36@0:8B16@\"<SPRNFSessionProxyInterface>\"20@?<v@?B@\"NSError\">28"
+ "Vv36@0:8B16@20@?28"
+ "Vv40@0:8@\"SPRUnifiedReaderReadParameters\"16@\"<SPRUnifiedReaderDelegate>\"24@?<v@?@\"SPRUnifiedReaderTransactionData\"@\"NSError\">32"
+ "Vv56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"<SPRUnifiedReaderDelegate>\"40@?<v@?@\"NSString\"@\"NSError\">48"
+ "Wall time offset %f is set for QA testing - skipping validation and persistence"
+ "X-Apple-Secure-Wall-Time"
+ "X-B3-SpanId"
+ "X-B3-TraceId"
+ "_TtC14softposreaderd13UnifiedReader"
+ "_TtC14softposreaderd15KeychainManager"
+ "_TtC14softposreaderd15KeychainWrapper"
+ "_TtC14softposreaderd15SEReaderSession"
+ "_TtC14softposreaderd16SEManagerSession"
+ "_TtC14softposreaderd17BeeServiceWrapper"
+ "_TtC14softposreaderd19DeviceTimeAnalytics"
+ "_TtC14softposreaderd19OasisServiceWrapper"
+ "_TtC14softposreaderd19RemoteUnifiedReader"
+ "_TtC14softposreaderd19VTIDIdentityManager"
+ "_TtC14softposreaderd20UnifiedReaderBackend"
+ "_TtC14softposreaderd22UnifiedReaderAnalytics"
+ "_TtC14softposreaderd22UnifiedReaderBAASigner"
+ "_TtC14softposreaderd22UniversalSecureChannel"
+ "_TtC14softposreaderd23AsyncBAASigningIdentity"
+ "_TtC14softposreaderd23TimeTokenManagerFactory"
+ "_TtC14softposreaderd24CoreDataMigrationManager"
+ "_TtC14softposreaderd24RemoteMPOCMonitorManager"
+ "_TtC14softposreaderd24SecureChannelHTTPFactory"
+ "_TtC14softposreaderd26UnifiedReaderPINController"
+ "_TtC14softposreaderd27UnifiedReaderOfflineBackend"
+ "_TtC14softposreaderd27UnifiedReaderPINAppletProxy"
+ "_TtC14softposreaderd28UnifiedReaderUtilityProvider"
+ "_TtC14softposreaderd29DefaultAsyncSecureChannelHTTP"
+ "_TtC14softposreaderd29RemoteUnifiedReaderFoundation"
+ "_TtC14softposreaderd29UniversalSecureChannelFactory"
+ "_TtC14softposreaderd30DefaultUnifiedReaderTimeKeeper"
+ "_TtC14softposreaderd31UnifiedReaderCertificateManager"
+ "_TtC14softposreaderd32RemoteUnifiedReaderPINController"
+ "_TtC14softposreaderd35UnifiedReaderAuthenticationStrategy"
+ "_TtC14softposreaderd35UnifiedReaderOasisV2UtilityProvider"
+ "_TtCC14softposreaderd19RemoteUnifiedReader10TaskRunner"
+ "_TtCC14softposreaderd24CoreDataMigrationManagerP33_CC3BFC9975B94E81874B626998A079F113CoreDataStore"
+ "_prepare(appBundleId:virtualTerminalId:partnerToken:)"
+ "accessGroup"
+ "activate"
+ "after transaction complete"
+ "after transaction error"
+ "allowExpiredCertificates"
+ "allowedAIDList"
+ "api/v1/authorization/lightreader/sessions"
+ "api/v4/kernelconfigurator/ota"
+ "appletService"
+ "attachCount"
+ "authenticationStrategy"
+ "autoRefreshOverride"
+ "avgEnterDigitInterval"
+ "b276318a-bad2-4de7-a35a-d4db7deaee1a"
+ "beeConfigId"
+ "beeService"
+ "beeServiceWrapper"
+ "beeStatus"
+ "beeVersion"
+ "before start EMV mode"
+ "before starting polling"
+ "begin network time for prepare"
+ "begin post processing"
+ "begin secure reader blob generation"
+ "begin total time for readCard"
+ "c8527c1f-85ce-411b-8c13-3faa6f8faef7"
+ "cachedProductState"
+ "cancelCardReadWithReply:"
+ "cannot obtain NFC session"
+ "capture(parameters:)"
+ "capturePINTime"
+ "captureWithParameters:reply:"
+ "cardReadTaskIDs"
+ "casd"
+ "cellSignalMonitor"
+ "cellularActiveBands"
+ "cellularRAT"
+ "cellularRSRP"
+ "cellularRSRQ"
+ "cellularSNR"
+ "certificateExpirationThreshold"
+ "certificateNotFound"
+ "certificatePEMs: %s"
+ "cleaned up identity for VTID: %s"
+ "clearTransactionData(session:)"
+ "collectNetworkMetrics()"
+ "com.apple.softposreader.deviceTimeEvent"
+ "com.apple.softposreader.keychain"
+ "com.apple.softposreader.keychain."
+ "com.apple.softposreader.keychain.temporary"
+ "com.apple.softposreader.keychain.temporary."
+ "com.apple.softposreader.keychain.volatile"
+ "com.apple.softposreader.signerEvent"
+ "com.apple.softposreader.unifiedReader.generateBlobEvent"
+ "com.apple.softposreader.unifiedReader.pinEvent"
+ "com.apple.softposreader.unifiedReader.prepareEvent"
+ "com.apple.softposreader.unifiedReader.readEvent"
+ "com.apple.softposreader:"
+ "com.apple.softposreaderd.sendmonitoringlogs"
+ "com.apple.softposreaderd.unifiedreader"
+ "completeOperation(error:)"
+ "component"
+ "connectionType"
+ "container"
+ "continuation"
+ "continuationStorage"
+ "core"
+ "couldNotStoreCertificates"
+ "couldNotStoreRotationDeadline"
+ "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"
+ "dGhpcyBpcyBhIG1lc3NhZ2UgdG8gdGVzdCBmb3IgdmFsaWQgYmFzZTY0IGlucHV0Lg=="
+ "dataServiceIdentifier"
+ "defaultReaderType"
+ "deleteAllKM_V1(session:forRecovery:)"
+ "deleteIdentity(identity:)"
+ "deleteStoredSESKeys(role:)"
+ "deviceTimeResult"
+ "diagnosticMode"
+ "didReceiveThermalIndication"
+ "disruptPersistence"
+ "doubleValue"
+ "download(for:progressHandler:)"
+ "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+ "enableTrustedWallTime"
+ "encryption applet config id: %s"
+ "encryption applet update available"
+ "encryptionAppletConfig"
+ "encryptionAppletScript"
+ "encryptionAppletVersion"
+ "end network time for prepare"
+ "end post processing for readCard"
+ "end secure reader blob generation"
+ "end total time for readCard"
+ "endCaptureWithReply:"
+ "enterDigitTimestamp"
+ "error from kernel manager %@."
+ "errorIndication(string:rawValue:)"
+ "errorType"
+ "evaluateBeeAssets(session:beeAssets:)"
+ "evaluateBeeAssetsKM_V1(session:beeAssets:)"
+ "evict VTID: %s"
+ "evicted VTID: %s"
+ "executeBeeAssets(session:assetsEvaluation:progress:)"
+ "executeBeeAssetsKM_V1(session:assetsEvaluation:progress:)"
+ "executeInstallScripts(transceiver:stingerConfig:oasisConfig:stingerApplet:oasisApplet:)"
+ "expectedBurnoutProtectionTimer:"
+ "failed to delete identity for VTID %s: %@"
+ "failed to encode date"
+ "failed to encode date and time"
+ "failed to encode persistence key for VTID: %s"
+ "failed to encode time"
+ "failed to make proxy: %@"
+ "failed to remove unused assets"
+ "failed to update VTID cache with error: %@"
+ "fetchSEFirmware(target:)"
+ "generateBeeAssets(payload:)"
+ "generateBeeAssetsKM_V1(payload:)"
+ "get payload attestation data failed"
+ "getActiveBands"
+ "getCertificate(role:)"
+ "getDeviceStateKM_V1(session:)"
+ "getInferredSecureTime(currentCpuTime:currentRtcResetCount:storedData:)"
+ "getMemoryInfo(session:)"
+ "getPayloadAttestation(kernelIdentityKeyIdentifier:)"
+ "getPayloadCertFingerprint()"
+ "getProductState(transceiver:)"
+ "getSignalMeasurements"
+ "getTapToPayMemoryInfo:"
+ "getTapToPayMemoryInfoWithSessionProxy:reply:"
+ "getUnifiedReaderCertificate()"
+ "got BAA Identity from Persisting"
+ "handleSessionDidReceiveData(_:applet:session:)"
+ "httpFactory"
+ "https://pos-qa3-raccoon.apay.apple.com/"
+ "identityRenewalRetryCount"
+ "inQueueKey"
+ "incorrect kek length"
+ "iniPINCapture in proxy trxIdHalf: %s"
+ "init(authenticationStrategy:signer:secureElement:http:resourceTimeout:)"
+ "init(backend:certificateManager:profileManager:attestationManager:monitorManager:auditor:systemInfo:managedData:signerFactory:secureTimeKeeper:analytics:secureElement:timeTokenManager:enforceJCOPVersion:launchFeedbackFramework:safCertificateValidity:certificateExpirationThreshold:beeServiceWrapper:sesnapshotWrapper:vtidIdentityManager:)"
+ "init(bound:secureElement:)"
+ "init(component:monitorLogger:attestationManager:monitorAnalytics:)"
+ "init(environment:systemInfo:keyChainManager:)"
+ "init(mpocMonitorManager:mpocAttestationManager:safAllowedDuration:queue:certificateManager:signerFactory:secureTimeKeeper:auditor:analytics:managedData:systemInfo:secureElement:enforceJCOPVersion:profileManager:vtidIdentityManager:launchFeedbackFramework:payAppletTagParser:appletService:)"
+ "init(oasisServiceWrapper:backend:unifiedReaderCertificateManager:managedData:secureElement:systemInfo:timekeeper:signerFactory:analytics:enforceJCOPVersion:)"
+ "init(owner:role:disallowsCreate:persist:auditor:certificateVerifier:analytics:systemInfo:secureTimeKeeper:seid:dispatchQueue:accessControl:oids:randomNumberGenerator:autoRefreshOverride:)"
+ "init(owner:role:disallowsCreate:persistenceKeySuffix:persist:auditor:certificateVerifier:analytics:secureTimeKeeper:dispatchQueue:randomNumberGenerator:validity:autoRefreshOverride:)"
+ "init(owner:role:disallowsCreate:persistenceKeySuffix:persist:auditor:certificateVerifier:analytics:systemInfo:secureTimeKeeper:seid:dispatchQueue:accessControl:oids:randomNumberGenerator:validity:autoRefreshOverride:)"
+ "init(owner:role:persistenceKeySuffix:persist:certificateVerifier:systemInfo:unifiedReaderTimeKeeper:analytics:seid:accessControl:oids:randomNumberGenerator:validity:autoRefreshOverride:)"
+ "init(resourceTimeout:)"
+ "init(storage:certificateVerifier:allowExpiredCertificates:)"
+ "init(transactionDataLifetime:appletProxy:managedData:secureElement:systemInfo:analytics:)"
+ "init(universalSecureChannelFactory:backendURL:)"
+ "init(uuid:accessControl:keyTimestamp:oids:nonce:validity:)"
+ "initWithCipherBlob:keyBlob:casd:appletAttestationData:kekHash:"
+ "initWithIsSupported:"
+ "initWithKernelsInstalled:countryCode:safStorageDuration:brandAIDs:safBrandAIDs:"
+ "initWithTransactionPayloadDataBlob:transactionPayloadAttestationData:applicationIdentifierRID:transactionID:ecdsaCertificate:panKekId:pinContext:"
+ "installRemoteScripts(token:tpid:saftpid:payload:launchSEStorageSheet:seStorageSheetBundleID:seStorageSheetSceneID:delegate:completion:)"
+ "invalidComponent"
+ "invalidExpirationDate"
+ "invalidSecureTime"
+ "isIssuerRequestPIN"
+ "isTimerStarted"
+ "jsblSequenceCounter: "
+ "jti from auth token empty"
+ "kernel token nil"
+ "kernelCleanup"
+ "keyChainManager"
+ "lastTransactionIdHalf"
+ "lockedCaptureInProgress"
+ "lockedUnifiedReaderBAASigner"
+ "lrpConfig"
+ "lrpConfig: %s"
+ "malformedCertificate"
+ "mpocMonitorManagerProxy(reply:)"
+ "mpocMonitorManagerProxyWithReply:"
+ "muirfieldDefaultSefwURL"
+ "muirfieldDefaultTempSefwURL"
+ "muirfieldOtaTempSefwURL"
+ "networkTime"
+ "nfSession"
+ "no VTID LRU cache found, starting fresh"
+ "no response from server when installing remote scripts"
+ "no saftpid"
+ "noValidCertificates"
+ "non hexadecimal string"
+ "nonce"
+ "not started: MPOCOperationMode is not online"
+ "oasisAppletScript"
+ "oasisAppletScript: "
+ "oasisService"
+ "oasisServiceWrapper"
+ "oasisTempSefwURL"
+ "openSession(requestPayload:)"
+ "operationState"
+ "operationType"
+ "osVersionHistory"
+ "panKEK"
+ "pay applet config id: %s"
+ "pay applet update available"
+ "payAppletConfig"
+ "payAppletScript"
+ "payAppletVersion"
+ "pendingTasks"
+ "persisted wall time: %f\nfresh wall time: %f\nTime going backward detected, using most forward time: %s"
+ "persistedCputime: %f\ncurrentCputime: %f\npersistedWallTime: %s\ninferredTime: %s\npersistedRTCResetCount: %u\ncurrentRTCResetCount: %u"
+ "persistentDomainForName:"
+ "persisting"
+ "piccGPOResponseTime"
+ "piccGenACResponseTime"
+ "pin-validation-certs"
+ "pinAction"
+ "pinBlockGenerationTime"
+ "pinCaptureIntervalState"
+ "pinContext"
+ "pinEntryResult"
+ "pinKEK"
+ "pollingDidRestart()"
+ "pollingDidStart()"
+ "pollingMode"
+ "pollingTime"
+ "postOTA(token:payload:progressHandler:completion:)"
+ "postProvisionReadProcessing(appletStatus:session:)"
+ "prepare(appBundleId:virtualTerminalId:partnerToken:)"
+ "prepareWithAppBundleId:virtualTerminalId:partnerToken:delegate:reply:"
+ "preprocessing(session:)"
+ "productStatus"
+ "read VTID LRU cache: %s"
+ "readCancelReason"
+ "readCard(parameters:delegate:)"
+ "readCardWithParameters:delegate:reply:"
+ "readTime"
+ "readerBlobSigner certificate expires before time required for SAF: %ld seconds. Begin renewal."
+ "receive picc response time: %s"
+ "recordVTIDUsage(_:)"
+ "remoteObjectProxy"
+ "remoteObjectProxyWithErrorHandler:"
+ "removePINDigitCount"
+ "removeSEFirmware(target: %s, type: %s)"
+ "removeTapToPayWithForce:reply:"
+ "removeTapToPayWithForce:sessionProxy:reply:"
+ "removeUnusedAssetsKM_V1(session:)"
+ "renewTask"
+ "safSigner certificate expires before time required for SAF: %ld seconds. Begin renewal."
+ "saveSEFirmware(target: %s, type: %s)"
+ "secondsBeforeIdentityRenewal"
+ "secure-payload-cert"
+ "secureChannelCryptoFactory"
+ "secureChannelHTTPFactory"
+ "secureDownload(for:contentType:progressHandler:)"
+ "secureNow using the time token: %s"
+ "secureNow using trusted wall time: %s"
+ "secureReaderBlobTimeTaken"
+ "secureTimeProvider"
+ "secureTranslateCertThumbPrint"
+ "secureTranslateCertThumbPrint: "
+ "secureTranslateCertificateChain"
+ "secureTranslateCertificateChain: "
+ "secureWallTimeString"
+ "sefwHash"
+ "sendLogsWithReply:"
+ "sendMonitoringLogs"
+ "serverErrorCode"
+ "service"
+ "serviceCurrentRadioAccessTechnology"
+ "session ended unexpectedly"
+ "sharedUnifiedReaderFoundationProxy(reply:)"
+ "sharedUnifiedReaderFoundationProxyWithReply:"
+ "signerType"
+ "softposreaderd.RemoteMPOCMonitorManager"
+ "softposreaderd.RemoteUnifiedReader"
+ "softposreaderd.RemoteUnifiedReaderFoundation"
+ "softposreaderd.RemoteUnifiedReaderPINController"
+ "softposreaderd.SEManagerSession"
+ "softposreaderd.SEReaderSession"
+ "softposreaderd.UnifiedReaderPINAppletProxy"
+ "softposreaderd/JSONWebToken.swift"
+ "softposreaderd/UnifiedReader.swift"
+ "softposreaderd/UnifiedReaderOfflineBackend.swift"
+ "startProvision(amount:transactionID:nonce:transactionType:currencyCode:countryCode:secureWallTime:)"
+ "startTransaction(session:)"
+ "stingerAppletScript"
+ "stingerAppletScript: "
+ "stingerConfigID"
+ "stingerConfigId"
+ "stingerConfigId: "
+ "stingerOtaTempSefwURL"
+ "stingerStatus"
+ "stingerTempSefwURL"
+ "stingerVersion"
+ "stingerVersion: "
+ "stopPayment(session:isClearingTransaction:)"
+ "storeUnifiedReaderCertificates(_:)"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "targetDiscovered()"
+ "taskRunner"
+ "telephonyNetworkInfo"
+ "timeTokenManagerFactory"
+ "timekeeper"
+ "timeout"
+ "totalPINEntryTime"
+ "transactionComplete(session:)"
+ "transactionError(session:)"
+ "transactionID"
+ "transactionIDHalf"
+ "trying deleteAllApplets()"
+ "unified-reader-network-time"
+ "unified-reader-polling-time"
+ "unified-reader-post-processing"
+ "unified-reader-read-time"
+ "unified-reader-secure-blob-time"
+ "unified-reader-total-time"
+ "unifiedReader"
+ "unifiedReaderBackendURL"
+ "unifiedReaderCertificateManager"
+ "unifiedReaderFoundationProxy(configuration:reply:)"
+ "unifiedReaderFoundationProxyWithConfiguration:reply:"
+ "unifiedReaderPINContext"
+ "unifiedReaderPINControllerProxyWithReply:"
+ "unifiedReaderProxyWithReply:"
+ "unifiedReaderTimeKeeper"
+ "unified_pin_controller"
+ "unified_reader_baa_setup"
+ "universalSecureChannelFactory"
+ "unpredictableNumber invalid"
+ "using persisted BAA Identity"
+ "utilityProvider"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8q16"
+ "v36@0:8B16@20@?28"
+ "validate(_:renewalBuffer:)"
+ "validateDeviceReboot(_:persistedResetCount:)"
+ "validateTimeNotGoingBackward(_:against:)"
+ "valueForKey:"
+ "valuesMutex"
+ "verifyCertificateList(_:)"
+ "virtualTerminalId"
+ "virtualTerminalId: "
+ "vtidIdentityManager"
+ "waitForThermalContinuation(timeout:)"
+ "wifiInterface"
+ "wifiRSSI"
+ "wrong length for PICC Response Time"
+ "wrote VTID LRU cache: %s"
- "$__lazy_storage_$_context"
- "$__lazy_storage_$_quietSecureChannel"
- "$__lazy_storage_$_sharedSecureChannel"
- "%s is readable"
- "%s.%s - NOT FOR RELEASE"
- "%s.%s result: %s"
- "%s.%s: client error when renewing certificates: %s"
- "%s: Client attached. currentAttachCount: (%lu)"
- "%s: Detaching client. currentAttachCount: (%lu)"
- "%s: TimeTokenManager started"
- "*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***\nSLAMSwift.performScript(): %s\n*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***"
- ", globalKernelConfig: "
- ", kernelAppletScript: "
- ", non-9000 RAPDUS: "
- ".appendEvent(%s"
- ".cxx_construct"
- "@32@0:8@16@24"
- "An applet is %s installed. globalID: %s, profileID: %s, 2nd profile ID: %s"
- "Attestation token expires at or earlier than token validity start date"
- "C-APDU (RESET KEY): %s"
- "Cannot switch offline - no time token"
- "Certificate for %s will be renewed immediately"
- "Certificate(s) expire before time required for SAF: %ld hour(s). Begin renewal."
- "Configurator.renewCertificates() cannotRenewCertificate: Could not get certificates from backend (possibly SecureChannelError) or\nmalformed response."
- "Configurator.renewCertificates() connectionProblem"
- "Configurator.renewCertificates() internal error"
- "Configurator.renewCertificates() operationNotAuthorized"
- "Configurator.renewCertificates() unexpected error: %s"
- "CoreDataWrapper: Insert data for key: \"%s\""
- "CoreDataWrapper: deleted after update"
- "CoreDataWrapper: key:\n\"%s\" does not exist, cannot delete"
- "Could not calculate secure now when switching to offline mode"
- "Could not decode Kernel Type, "
- "Could not get SEID"
- "Could not get cpu time from claims"
- "Could not get the kernel manager, setting legacy flow to true %@"
- "Could not get the kernel manager, setting legacy flow to true."
- "Could not perform script, error: %@"
- "Could not persist MPOCOperationMode: %s"
- "DefaultManagedDictionary Found workItem for key: %s. Cancelling it..."
- "DefaultManagedDictionary cancel workitem for key: %s"
- "DefaultManagedDictionary removed value for key: %s"
- "DefaultManagedDictionary updateValue duration: %f"
- "DefaultManagedDictionary updated value for key: %s"
- "DefaultTimeTokenManager: Already in %s mode."
- "EnableOTAV3Endpoint"
- "Error calculating secure time: %@"
- "Error when sending logs: %@"
- "Failed to clear PAN: NFC disabled"
- "Failed to copy configuration: %s"
- "Failed to delete BAA key and certificate: %s"
- "Failed to remove %s: %@"
- "Failed to send MPOC logs after readCard with an unexpected error %@"
- "Failed to send MPOC logs after readCard: %s"
- "Found invalid mode data in persistence. Using .online"
- "Get certificate from SESKeyAttest failed: %s"
- "HTTP error when renewing certificates: %@"
- "Install global config: failed to reset keys."
- "Install global config: reset CAPK and CRL."
- "KERNEL_UNKNOWN, "
- "KernelManagerWrapperProtocol"
- "LoadAndInstall: %{public}s, GlobalConfig: %{public}s, PartnerConfig: %{public}s, PartnerSAFConfig: %{public}s,"
- "Logging"
- "MPOC logs sent after readCard"
- "ManualSendMonitoringLogs"
- "ManualSendMonitoringLogs (Feature Flag) is Enabled"
- "Mastercard PayPass, "
- "Mode is %hhu, using default renewal time: %f"
- "No applet update available"
- "No coreConfig update available"
- "No globalKernelConfig update available"
- "No valid certificates"
- "Optional<SecureElementProtocol>"
- "Partner Profile ID: %{public}s"
- "Pay applet cannot be selected: Prohibit timer or not installed"
- "PerformOnlyScriptInSEFW:seHandle:logSink:"
- "PerformScript:seHandle:logSink:"
- "PerformScript:sefwPath:seHandle:logSink:"
- "PerformScriptWithName:seHandle:logSink:"
- "PerformScriptWithName:sefwPath:seHandle:logSink:"
- "Previous firmware of type %s exists, removing and replacing"
- "Primer.attach() Could not get SecureElement from depot"
- "Provision Config ID: %{public}s"
- "QUIET_SECURE_CHANNEL"
- "Received notification to send the monitoring logs now"
- "Removing firmware of type %s"
- "SE-SEP is not paired, trying deleteAllApplets()"
- "Save %s"
- "SecureChannel.httpData: Received HTTP error %ld"
- "SecureChannel.httpData: Success. Received payload"
- "SecureChannel.httpDownloadTask: Received HTTP error %ld"
- "SecureChannel.httpDownloadTask: Success. Received payload"
- "SecureChannelHTTPProtocol"
- "Storage folder created"
- "Swift/Dictionary.swift"
- "T@\"NSData\",N,D,C"
- "TB,N,D"
- "Time token has invalid validity duration"
- "TimeTokenManager"
- "TimeTokenManagerMode"
- "Unexpected value from date string"
- "_TtC14softposreaderd15CoreDataManager"
- "_TtC14softposreaderd15CoreDataWrapper"
- "_TtC14softposreaderd18MockPINAppletProxy"
- "_TtC14softposreaderd20KernelManagerWrapper"
- "api/v2/kernelconfigurator/ota"
- "applet update available"
- "begin cleanup SLAM"
- "begin global config SLAM"
- "begin install kernel SLAM"
- "begin partner online profile SLAM"
- "begin partner saf profile SLAM"
- "cannot decode server response"
- "cannot select applet %@"
- "cannot select applet %{public}@"
- "casdCertificate"
- "componentName"
- "config-install-cleanupSLAM"
- "config-install-global"
- "config-install-kernel"
- "config-install-profile"
- "coreConfig id: %s"
- "coreDataManager"
- "couldn't access AVSC"
- "defaultSefwURL"
- "defaultTempSefwURL"
- "deleteObject:"
- "end cleanup SLAM"
- "end global config SLAM"
- "end install kernel SLAM"
- "end partner online profile SLAM"
- "end partner saf profile SLAM"
- "endpoint"
- "entityName"
- "error"
- "error from kernel manager %@. use legacy flow"
- "error when fetching global id: %s"
- "error when fetching profiles: %s"
- "error when install: %@"
- "evaluateKernelAsset(session:kernelAsset:)"
- "executeKernelAsset(session:assets:progress:)"
- "executeLegacy(payload:tpid:saftpid:launchSEStorageSheet:seStorageSheetBundleID:seStorageSheetSceneID:delegate:)"
- "external store not found"
- "failed to execute cleanup script"
- "failed to select applet"
- "failed to select applet after removing unused assets"
- "failed to send reset key"
- "generateKernelAsset(payload:)"
- "globalConfigId"
- "globalKernelConfig"
- "globalKernelConfig id: %s"
- "hasChanges"
- "history"
- "https://pos-device-stage.apple.com/"
- "init(backend:certificateManager:profileManager:attestationManager:monitorManager:auditor:systemInfo:managedData:signerFactory:secureTimeKeeper:analytics:secureElement:timeTokenManager:enforceJCOPVersion:launchFeedbackFramework:safCertificateValidity:kernelManagerWrapper:sesnapshotWrapper:)"
- "init(componentName:monitorLogger:attestationManager:monitorAnalytics:)"
- "init(dictionary:)"
- "init(environment:systemInfo:coreDataManager:)"
- "init(mpocMonitorManager:mpocAttestationManager:safAllowedDuration:queue:certificateManager:signerFactory:secureTimeKeeper:auditor:analytics:managedData:systemInfo:secureElement:enforceJCOPVersion:profileManager:launchFeedbackFramework:payAppletTagParser:)"
- "init(owner:role:disallowsCreate:persist:auditor:certificateVerifier:analytics:systemInfo:secureTimeKeeper:seid:dispatchQueue:accessControl:oids:randomNumberGenerator:)"
- "init(owner:role:disallowsCreate:persistenceKeySuffix:persist:auditor:certificateVerifier:analytics:secureTimeKeeper:dispatchQueue:randomNumberGenerator:validity:)"
- "init(owner:role:disallowsCreate:persistenceKeySuffix:persist:auditor:certificateVerifier:analytics:systemInfo:secureTimeKeeper:seid:dispatchQueue:accessControl:oids:randomNumberGenerator:validity:)"
- "initWithBool:"
- "initWithContext:"
- "initWithEntity:insertIntoManagedObjectContext:"
- "initWithKernelsInstalled:countryCode:safStorageDuration:"
- "installRemoteScripts(token:tpid:saftpid:payload:isUsingLegacyFlow:launchSEStorageSheet:seStorageSheetBundleID:seStorageSheetSceneID:delegate:completion:)"
- "isDailyCollectionEnabled: %{bool}d"
- "isProductionAnalytics: %{bool}d"
- "isReadableFileAtPath:"
- "isUsingLegacyFlow(session:)"
- "isValidSEPairing: %{bool}d"
- "kSoftPOSReaderSendMonitoringLogs"
- "kernel manager flow"
- "kernel token nil or has no saftpid"
- "kernelLoadAndInstall"
- "kernelManagerWrapper"
- "lastAttestation"
- "lockedAttachCount"
- "manager"
- "moc has not changed"
- "no global id"
- "no response from server"
- "no secure element found"
- "non 200 level status code"
- "nothing was installed, skip profile activation"
- "otaTempSefwURL"
- "performScript(name:)"
- "performScript(path:)"
- "performScript(path:name:)"
- "performScript(path:scriptID:)"
- "performScript(scriptID:)"
- "persistentContainer"
- "persistentStoreCoordinator"
- "persistentStores"
- "postOTA(token:payload:isUsingLegacyFlow:progressHandler:completion:)"
- "readerBlobSigner certificate expires before time required for SAF: %ld hour(s). Begin renewal."
- "removeFirmware(type:)"
- "removePersistentStore:error:"
- "reset"
- "reset CAPK and CRL for the old kernel"
- "safSigner certificate expires before time required for SAF: %ld hour(s). Begin renewal."
- "save:"
- "saveNewFirmware(_:type:)"
- "seStateInfo"
- "secureNow(from:)"
- "setDateFormat:"
- "setLocale:"
- "setReturnsObjectsAsFaults:"
- "setStoredKey:"
- "setStoredValue:"
- "setWillBeRemovedAfterUpdate:"
- "softposreaderd.CoreDataWrapper"
- "stateInfo: %s\nglobal: %s\nprofiles: %s"
- "storedKey"
- "storedValue"
- "stringFromDate:"
- "user default: %s"
- "using legacy flow"
- "using legacy flow for persistDownloadedScripts"
- "using the legacy flow"
- "willBeRemovedAfterUpdate == %@"

```
