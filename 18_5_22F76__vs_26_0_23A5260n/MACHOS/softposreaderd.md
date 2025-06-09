## softposreaderd

> `/usr/libexec/softposreaderd`

```diff

-35.1.0.0.0
-  __TEXT.__text: 0x2bb118
-  __TEXT.__auth_stubs: 0x34c0
+40.22.0.0.0
+  __TEXT.__text: 0x28d738
+  __TEXT.__auth_stubs: 0x3880
   __TEXT.__objc_stubs: 0x100
-  __TEXT.__objc_methlist: 0xa78
-  __TEXT.__const: 0x870f0
-  __TEXT.__cstring: 0x10b55
-  __TEXT.__swift5_typeref: 0x1a2b
-  __TEXT.__objc_methname: 0x1e54
-  __TEXT.__oslogstring: 0xae1c
+  __TEXT.__objc_methlist: 0xae4
+  __TEXT.__const: 0x84380
+  __TEXT.__cstring: 0x10635
+  __TEXT.__swift5_typeref: 0x1be0
+  __TEXT.__objc_methname: 0x1fb5
+  __TEXT.__oslogstring: 0xb0ae
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x51b4
-  __TEXT.__swift5_proto: 0x9a4
-  __TEXT.__swift5_types: 0x3a0
-  __TEXT.__objc_classname: 0x186
-  __TEXT.__objc_methtype: 0xb5b
-  __TEXT.__swift5_protos: 0xb8
-  __TEXT.__swift_as_entry: 0x8
-  __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x3568
-  __TEXT.__eh_frame: 0x7c48
-  __DATA_CONST.__auth_got: 0x1a68
-  __DATA_CONST.__got: 0xb20
-  __DATA_CONST.__auth_ptr: 0xe50
-  __DATA_CONST.__const: 0x14680
-  __DATA_CONST.__objc_classlist: 0x278
-  __DATA_CONST.__objc_protolist: 0x120
+  __TEXT.__constg_swiftt: 0x592c
+  __TEXT.__swift5_proto: 0x9d8
+  __TEXT.__swift5_types: 0x3fc
+  __TEXT.__objc_classname: 0x1b6
+  __TEXT.__objc_methtype: 0xc22
+  __TEXT.__swift5_protos: 0xd8
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__unwind_info: 0x3758
+  __TEXT.__eh_frame: 0x8368
+  __DATA_CONST.__auth_got: 0x1c48
+  __DATA_CONST.__got: 0xbb8
+  __DATA_CONST.__auth_ptr: 0xb20
+  __DATA_CONST.__const: 0x15390
+  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x90
-  __DATA.__objc_const: 0x6780
-  __DATA.__objc_selrefs: 0xa68
-  __DATA.__objc_data: 0x17b8
-  __DATA.__data: 0x8b60
-  __DATA.__common: 0x628
-  __DATA.__bss: 0x105d8
+  __DATA_CONST.__objc_protorefs: 0xa0
+  __DATA.__objc_const: 0x6f80
+  __DATA.__objc_selrefs: 0xad8
+  __DATA.__objc_data: 0x18c0
+  __DATA.__data: 0x9650
+  __DATA.__common: 0x650
+  __DATA.__bss: 0x10ce8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks

   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService
+  - /System/Library/PrivateFrameworks/KernelManagerLibrary.framework/KernelManagerLibrary
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /System/Library/PrivateFrameworks/SPRCore.framework/SPRCore
   - /System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSCLM.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_StringProcessing.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 09EE1063-6F42-32F4-82C8-96945A51A5C1
-  Functions: 4509
-  Symbols:   1377
-  CStrings:  2963
+  UUID: A06DE052-20D8-3AC4-9974-5B9C74AA7983
+  Functions: 4581
+  Symbols:   1456
+  CStrings:  3024
 
Symbols:
+ _$s10Foundation10CocoaErrorV19fileWriteFileExistsAC4CodeVvgZ
+ _$s10Foundation11JSONEncoderC16OutputFormattingVMn
+ _$s10Foundation11JSONEncoderC16OutputFormattingVs10SetAlgebraAAMc
+ _$s10Foundation12DateIntervalV5start8durationAcA0B0V_SdtcfC
+ _$s10Foundation12DateIntervalV8durationSdvg
+ _$s10Foundation12DateIntervalVs23CustomStringConvertibleAAMc
+ _$s10Foundation13__DataStorageC27ensureUniqueBufferReference9growingTo5clearySi_SbtF
+ _$s10Foundation3URLV13DirectoryHintO03notC0yA2EmFWC
+ _$s10Foundation3URLV7SPRCoreE20generateSHA256DigestAA4DataVyKF
+ _$s10Foundation4DateVSEAAMc
+ _$s10Foundation4DateVSeAAMc
+ _$s20KernelManagerLibrary0A15AssetEvaluationV14requiredMemoryAA12SEMemoryInfoVvg
+ _$s20KernelManagerLibrary0A15AssetEvaluationVMa
+ _$s20KernelManagerLibrary0A5AssetV07updatedD09kernelMap19configurationScript11capkScripts015terminalProfileK0ACSb_10Foundation4DataVAI3URLVSgSayAMGSgSayAA0mI0VGSgtcfC
+ _$s20KernelManagerLibrary0A5AssetVMa
+ _$s20KernelManagerLibrary0A5AssetVMn
+ _$s20KernelManagerLibrary0aB0C13useLegacyFlowSbvgTj
+ _$s20KernelManagerLibrary0aB0C14getDeviceStateyAA03BeeF4InfoCAC0eF4TypeOKFTj
+ _$s20KernelManagerLibrary0aB0C15DeviceStateTypeO6normalyA2EmFWC
+ _$s20KernelManagerLibrary0aB0C15DeviceStateTypeO7minimalyA2EmFWC
+ _$s20KernelManagerLibrary0aB0C15DeviceStateTypeOMa
+ _$s20KernelManagerLibrary0aB0C18executeServerAsset_8progressyAA0aF10EvaluationV_ySictKFTj
+ _$s20KernelManagerLibrary0aB0C18getDefaultSEFWPath12isProductionSSSb_tFZ
+ _$s20KernelManagerLibrary0aB0C18removeUnusedAssetsyyKFTj
+ _$s20KernelManagerLibrary0aB0C19evaluateServerAssetyAA0aF10EvaluationVAA0aF0VKFTj
+ _$s20KernelManagerLibrary0aB0C9deleteAll11forRecoveryySb_tKFTj
+ _$s20KernelManagerLibrary0aB0C9seWrapper4sefwAcA09SESessionE0V_10Foundation3URLVtKcfc
+ _$s20KernelManagerLibrary0aB0CMa
+ _$s20KernelManagerLibrary12BeeStateInfoC12SystemStatusO10terminatedyA2EmFWC
+ _$s20KernelManagerLibrary12BeeStateInfoC12SystemStatusO11descriptionSSvg
+ _$s20KernelManagerLibrary12BeeStateInfoC12SystemStatusO11needsRepairyA2EmFWC
+ _$s20KernelManagerLibrary12BeeStateInfoC12SystemStatusO2eeoiySbAE_AEtFZ
+ _$s20KernelManagerLibrary12BeeStateInfoC12SystemStatusOMa
+ _$s20KernelManagerLibrary12BeeStateInfoC12SystemStatusOMn
+ _$s20KernelManagerLibrary12BeeStateInfoC12hardwareTypeSivg
+ _$s20KernelManagerLibrary12BeeStateInfoC15configurationId10Foundation4DataVSgvg
+ _$s20KernelManagerLibrary12BeeStateInfoC16terminalProfilesSay10Foundation4DataVGSgvg
+ _$s20KernelManagerLibrary12BeeStateInfoC19jsblSequenceCounterSSvg
+ _$s20KernelManagerLibrary12BeeStateInfoC22loadAndInstallBundleIdSSvg
+ _$s20KernelManagerLibrary12BeeStateInfoC5capksSDys5UInt8V10Foundation4DataVGSgvg
+ _$s20KernelManagerLibrary12BeeStateInfoC6statusAC12SystemStatusOvg
+ _$s20KernelManagerLibrary12SEMemoryInfoV3codSuvg
+ _$s20KernelManagerLibrary12SEMemoryInfoV3corSuvg
+ _$s20KernelManagerLibrary12SEMemoryInfoV3idxSuvg
+ _$s20KernelManagerLibrary12SEMemoryInfoV3nvmSuvg
+ _$s20KernelManagerLibrary12SEMemoryInfoVMa
+ _$s20KernelManagerLibrary13ProfileScriptV07profileE4Path17kernelIdentifiersAC10Foundation3URLV_Says5UInt8VGtcfC
+ _$s20KernelManagerLibrary13ProfileScriptVMa
+ _$s20KernelManagerLibrary13ProfileScriptVMn
+ _$s20KernelManagerLibrary16SESessionWrapperV4seid12isProduction7sessionACSS_SbSo015NFSecureElementB7SessionCtcfC
+ _$s20KernelManagerLibrary16SESessionWrapperVMa
+ _$s7SPRCore6TLVTagV11asn1BooleanACvgZ
+ _$s7SPRCore6TLVTagV11asn1IntegerACvgZ
+ _$s7SPRCore6TLVTagV13asn1BitStringACvgZ
+ _$s9SEService10SESnapshotC18ProposedKernelInfoV11descriptionSSvg
+ _$s9SEService10SESnapshotC18ProposedKernelInfoV3nvm3cod3cor3idxAESi_S3itcfC
+ _$s9SEService10SESnapshotC18ProposedKernelInfoVMa
+ _$s9SEService10SESnapshotC18ProposedKernelInfoVMn
+ _$s9SEService10SESnapshotC18getCurrentSnapshot4with4seidACSo29NFSecureElementManagerSessionC_SStYaKFZ
+ _$s9SEService10SESnapshotC18getCurrentSnapshot4with4seidACSo29NFSecureElementManagerSessionC_SStYaKFZTu
+ _$s9SEService10SESnapshotC6canFit18proposedKernelInfo18reclaimUnusedSpace7sessionSbAC08ProposedfG0V_SbSo29NFSecureElementManagerSessionCSgtYaKFZ
+ _$s9SEService10SESnapshotC6canFit18proposedKernelInfo18reclaimUnusedSpace7sessionSbAC08ProposedfG0V_SbSo29NFSecureElementManagerSessionCSgtYaKFZTu
+ _$s9SEService10SESnapshotCMa
+ _$s9SEService24SEStorageManagementSheetV19deviceConfiguration12provisioningA2C018ProvisioningDeviceF0O_SayAC22ProposedCredentialTypeOGtcfC
+ _$s9SEService24SEStorageManagementSheetV22ProposedCredentialTypeO9muirfieldyAeA10SESnapshotC0E10KernelInfoV_tcAEmFWC
+ _$s9SEService24SEStorageManagementSheetV22ProposedCredentialTypeOMa
+ _$s9SEService24SEStorageManagementSheetV22ProposedCredentialTypeOMn
+ _$s9SEService24SEStorageManagementSheetV31ProvisioningDeviceConfigurationO07currentF0yAeA10SESnapshotC_tcAEmFWC
+ _$s9SEService24SEStorageManagementSheetV31ProvisioningDeviceConfigurationOMa
+ _$s9SEService24SEStorageManagementSheetV7present23overSceneWithIdentifier013inApplicationH8BundleIDSbSS_SStYaAC9ErrorCodeOYKF
+ _$s9SEService24SEStorageManagementSheetV7present23overSceneWithIdentifier013inApplicationH8BundleIDSbSS_SStYaAC9ErrorCodeOYKFTu
+ _$s9SEService24SEStorageManagementSheetV7present25inApplicationWithBundleIDSbSS_tYaAC9ErrorCodeOYKF
+ _$s9SEService24SEStorageManagementSheetV7present25inApplicationWithBundleIDSbSS_tYaAC9ErrorCodeOYKFTu
+ _$s9SEService24SEStorageManagementSheetV9ErrorCodeOMa
+ _$s9SEService24SEStorageManagementSheetV9ErrorCodeOs0E0AAMc
+ _$s9SEService24SEStorageManagementSheetVMa
+ _$sSJ12isMathSymbolSbvg
+ _$sSJ8isNumberSbvg
+ _$sSTsE6reduce4into_qd__qd__n_yqd__z_7ElementQztKXEtKlF
+ _$sSY8rawValue03RawB0QzvgTj
+ _$sSa5countSivg
+ _$sSa9_getCountSiyF
+ _$sScP3lowScPvgZ
+ _$sSd7SPRCoreE8longWaitSdvgZ
+ _$sSo17NFHardwareManagerC7SPRCoreE018startSecureElementB7Session8deadlineSo08NFSecurefbG0C8Dispatch0J4TimeV_tKF
+ _$sSo17OS_dispatch_groupC8DispatchE4wait7timeoutAC0D13TimeoutResultOAC0D4TimeV_tF
+ _$sSo17OS_dispatch_groupC8DispatchE4waityyF
+ _$sSo9SPRLoggerC7SPRCoreE13kernelManager2os6LoggerVvgZ
+ _$sSo9SPRLoggerC7SPRCoreE17sesnapshotWrapper2os6LoggerVvgZ
+ _$sSs8UTF8ViewV8distance4from2toSiSS5IndexV_AGtF
+ _$ss10_HashTableV11startBucketAB0D0Vvg
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss12CaseIterableP8allCases03AllD0QzvgZTj
+ _$ss12CaseIterableTL
+ _$ss17CodingUserInfoKeyVMa
+ _$ss17CodingUserInfoKeyVMn
+ _$ss17CodingUserInfoKeyVSHsWP
+ _$ss17CodingUserInfoKeyVSQsWP
+ _$ss18_DictionaryStorageCMa
+ _$sytWV
+ _OBJC_CLASS_$_SPRApplicationRecord
+ _OBJC_CLASS_$_SPRMemoryInfo
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _objc_release_x1
- _$s10Foundation11JSONDecoderC7SPRCoreE11decodeClean_4from8userInfoxxm_AA4DataVSDys010CodingUserH3KeyVypGtKSeRzlFZfA1_
- _$s10Foundation11JSONEncoderC7SPRCoreE11encodeClean_16outputFormattingAA4DataVx_AC06OutputG0VtKSERzlFZfA0_
- _$s10Foundation4DataV15_RepresentationOys5UInt8VSicis
- _$s10Foundation4DataV7SPRCoreE16base64urlEncoded7optionsACSgSS_So27NSDataBase64DecodingOptionsVtcfcfA0_
- _$s10Foundation4DataV7SPRCoreE22base64urlEncodedString7optionsSSSo27NSDataBase64EncodingOptionsV_tFfA_
- _$s10Foundation4DataV8IteratorVMa
- _$s10Foundation4DataV8IteratorVStAAMc
- _$s10Foundation4DataV8IteratorV_2atAeC_SitcfC
- _$s7SPRCore3TLVV3tag11octetStringAcA6TLVTagV_10Foundation4DataVtcfcfA_
- _$s7SPRCore3TLVV3tag7booleanAcA6TLVTagV_SbtcfcfA_
- _$s7SPRCore3TLVV3tag7integerAcA6TLVTagV_xtcs17FixedWidthIntegerRzSZRzlufcfA_
- _$s7SPRCore3TLVV3tag9bitStringAcA6TLVTagV_AA03BitE0VtcfcfA_
- _$s7SPRCore9BitStringV4data10unusedBitsAC10Foundation4DataV_s5UInt8VtcfcfA0_
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfC
- _$sSiSEsWP
- _$sSl17_StringProcessingSQ7ElementRpzrlE8containsySbqd__SlRd__ABQyd__ACRSlF
- _$sSn7SPRCoreE7includeySbSnyxGF
- _$sSnyxGSEsSERzrlMc
- _$sSnyxGSesSeRzrlMc
- _$sSt4next7ElementQzSgyFTj
- _$ss18EnumeratedSequenceV8IteratorVMn
- _$ss38_bridgeAnythingNonVerbatimToObjectiveCyyXlxnlF
- _OBJC_CLASS_$_NFRemoteAdminManager
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _swift_unknownObjectRelease_n
CStrings:
+ "%s - Handler was registered (for daily core analytics)"
+ "%s - registerForTask() returned NO"
+ "%s.%s - NOT FOR RELEASE"
+ "%s.%s - Operation was in progress: client must have crashed"
+ "%s.%s - User Defaults is nil"
+ "%s.%s - isDailyCollectionEnabled: false"
+ "%s.cumulate - Appended value \"%s\" for field \"%s\""
+ "%s.cumulate - Field \"%s\" is already stored with value: %s"
+ ", configuredKernels: "
+ ", detectedSEFWUpdate: "
+ ", kernelAppletScript: "
+ "ATTEMPTED_TO_SEND_BATCH"
+ "ATTESTATION_FAILED"
+ "AnalyticsSendEventLazy - event name: %s, payload: %s"
+ "AttestationError#"
+ "BIT_STRING_INDICATOR"
+ "Background Attestation cannot be started"
+ "CBOR library is not available"
+ "Calling canFit with reclaimUnusedSpace"
+ "Cannot refresh (crypto)"
+ "Cannot refresh (persistence)"
+ "Cannot refresh (server)"
+ "Certificate is invalid"
+ "Challenge Certificate invalid"
+ "Checkpoint invalid"
+ "Clock not set to Automatic"
+ "Component disabled"
+ "Could not calculate app usage time"
+ "Could not check SE storage"
+ "Could not evaluate kernel asset: %s"
+ "Could not generate kernel asset: %s"
+ "Could not get SE snapshot to present storage sheet"
+ "Could not get SEID"
+ "Could not get an SE snapshot"
+ "Could not get an SE snapshot %@"
+ "Could not get the kernel manager, setting legacy flow to true %@"
+ "Could not get the kernel manager, setting legacy flow to true."
+ "Could not read the monitoring file %@.\nAttempting to remove the stored files."
+ "Could not refresh time token: %@"
+ "Could not register"
+ "Could not start background"
+ "DEVICE_BANNED FOR ("
+ "Detected a fresh install of kernels. Using the default SLAM."
+ "Detected an SEFW update. Querying minimal device state."
+ "Detected an iOS update. Will use the default SLAM."
+ "Device ID Mismatch"
+ "Device Model not supported"
+ "EnableOTAV3Endpoint"
+ "Entry cannot be decrypted"
+ "Entry cannot be encrypted"
+ "Evaluated kernel asset: %s"
+ "Failed to clear PAN: %@"
+ "Failed to clear the SE"
+ "Failed to delete: %@"
+ "Failed to delete: Session Busy"
+ "Failed to execute kernel assets %@"
+ "Failed to remove muirfield: NFC disabled"
+ "Failed to remove muirfield: Session Busy"
+ "Failed to select applet to clear transaction: %@"
+ "Forcing time token refresh"
+ "Found an existing default SE FW file. Will check for OTA patches."
+ "Found nil bundleID for storage management sheet."
+ "Generating a kernel asset with updatedAsset: %{bool}d"
+ "HostConfiguration(bypass_aid: "
+ "INTEGER_INDICATOR"
+ "INVALID_SOFTWARE"
+ "Initializing a KernelManager at %s"
+ "Invalid action"
+ "Invalid checkpoint"
+ "Invalid configuration item"
+ "KCSOTAResponse(capks: "
+ "Kernel asset will not fit on the SE"
+ "KernelConfig(id: "
+ "KernelManager indicated deletion required. forRecovery: %{bool}d"
+ "KernelManagerWrapperProtocol"
+ "Launching SE storage management sheet"
+ "LoadAndInstallBundle_DEFAULT.sefw"
+ "LoadAndInstallBundle_OTA.sefw"
+ "ManualPostCADaily (Feature Flag) is Enabled"
+ "ManualSendMonitoringLogs (Feature Flag) is Enabled"
+ "Missing component"
+ "Missing configuration item"
+ "MonitorManager got a %s event"
+ "MonitorManager is at the %s state"
+ "NFSecureElementManagerSession ended in %s"
+ "NFSecureElementManagerSession started"
+ "No Attestation Token"
+ "No Delegate. Install Progress: %ld"
+ "No capks update available"
+ "No coreConfig update available"
+ "No kernel map provided"
+ "No post-processing for last applet status: \n%s"
+ "No response received from Secure Element"
+ "Non-nil bundleId cannot be empty"
+ "Not refreshing time token"
+ "OBJECT_INDICATOR"
+ "OCTET_STRING_INDICATOR"
+ "ONE_BYTE_LEN_INDICATOR"
+ "OS not supported"
+ "PAYLOAD %s"
+ "PRINTABLE_STRING_INDICATOR"
+ "Passcode is disabled"
+ "Prepare failed because Time Token Refresh Failed"
+ "Prepare failed because Time Token is Outside Validity"
+ "Previous firmware of type %s exists, removing and replacing"
+ "Primer.attach() Validating SE pairing"
+ "Profile(hostConfiguration: "
+ "RETRIED_SENDING_THE_SAME_BATCH"
+ "Refreshing time token: %@"
+ "Removing firmware of type %s"
+ "Report invalid data"
+ "SE not supported"
+ "SEQUENCE_ELEMENT_0_INDICATOR"
+ "SEQUENCE_ELEMENT_1_INDICATOR"
+ "SEQUENCE_INDICATOR"
+ "SESnapshotWrapperProtocol"
+ "SET_INDICATOR"
+ "SPRInspectorXPCProxy"
+ "SPRNFSessionProxyInterface"
+ "STORED_COMPLETE_ATTESTATION_AND_ATTEMPTED_TO_SEND_BATCH"
+ "SUCCESS_WITHOUT_TOKEN"
+ "SUCCESS_WITH_TOKEN"
+ "Save %s"
+ "Server cannot report"
+ "TIME_SYNC_FAILED"
+ "TWO_BYTES_LEN_INDICATOR"
+ "There are %ld batch(s) in the monitoring file."
+ "Time Token Outside Validity"
+ "Time Token Refresh Failed"
+ "Time out waiting for the new certificate."
+ "Time token has invalid validity duration"
+ "Time token not available"
+ "Time token outside of validity period. Validity period: "
+ "Timed out waiting for deviceCheckService.generateKey."
+ "Too many instances"
+ "Using wall time to verify the kernel token."
+ "Vv24@0:8@?<v@?@\"<SPRInspectorXPCProxy>\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?@\"NSArray\">16"
+ "Vv24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "Vv32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "Vv60@0:8@\"NSString\"16B24@\"NSString\"28@\"NSString\"36@\"<SPRInstallDelegate>\"44@?<v@?@\"SPRInstallData\"@\"NSError\">52"
+ "Vv60@0:8@16B24@28@36@44@?52"
+ "_TtC14softposreaderd10DERDecoder"
+ "_TtC14softposreaderd10SystemInfo"
+ "_TtC14softposreaderd10Terminator"
+ "_TtC14softposreaderd11ATTESTATION"
+ "_TtC14softposreaderd11Environment"
+ "_TtC14softposreaderd11GlobalState"
+ "_TtC14softposreaderd11NullAuditor"
+ "_TtC14softposreaderd12Configurator"
+ "_TtC14softposreaderd12TaggedObject"
+ "_TtC14softposreaderd13ReadOperation"
+ "_TtC14softposreaderd13SecureChannel"
+ "_TtC14softposreaderd13SecureElement"
+ "_TtC14softposreaderd13SignerFactory"
+ "_TtC14softposreaderd14ProfileManager"
+ "_TtC14softposreaderd15CoreDataManager"
+ "_TtC14softposreaderd15CoreDataWrapper"
+ "_TtC14softposreaderd15ProvisionReader"
+ "_TtC14softposreaderd15ReaderAnalytics"
+ "_TtC14softposreaderd15RemoteInspector"
+ "_TtC14softposreaderd15StatusInspector"
+ "_TtC14softposreaderd16ComponentAuditor"
+ "_TtC14softposreaderd16MPOCMonitorStore"
+ "_TtC14softposreaderd16MonitorAnalytics"
+ "_TtC14softposreaderd16NFSESessionBlock"
+ "_TtC14softposreaderd17DefaultTimeKeeper"
+ "_TtC14softposreaderd17PayAppletResponse"
+ "_TtC14softposreaderd17ReadDelegateRelay"
+ "_TtC14softposreaderd17SESnapshotWrapper"
+ "_TtC14softposreaderd17SecurityAnalytics"
+ "_TtC14softposreaderd18AAASigningIdentity"
+ "_TtC14softposreaderd18BAASigningIdentity"
+ "_TtC14softposreaderd18CertificateManager"
+ "_TtC14softposreaderd18MockPINAppletProxy"
+ "_TtC14softposreaderd18NullAuditorFactory"
+ "_TtC14softposreaderd18PersistenceFactory"
+ "_TtC14softposreaderd18ProvisionAnalytics"
+ "_TtC14softposreaderd18SESSigningIdentity"
+ "_TtC14softposreaderd18VolatilePersisting"
+ "_TtC14softposreaderd19ConfiguratorBackend"
+ "_TtC14softposreaderd19DefaultStateMachine"
+ "_TtC14softposreaderd19ReaderConfiguration"
+ "_TtC14softposreaderd20DefaultPINController"
+ "_TtC14softposreaderd20KCSOTAResponseParser"
+ "_TtC14softposreaderd20KernelManagerWrapper"
+ "_TtC14softposreaderd20SecureChannelFactory"
+ "_TtC14softposreaderd21ConfiguratorAnalytics"
+ "_TtC14softposreaderd21DefaultPINAppletProxy"
+ "_TtC14softposreaderd21PrimaryAccountWatcher"
+ "_TtC14softposreaderd22ProvisionReadOperation"
+ "_TtC14softposreaderd23ComponentAuditorFactory"
+ "_TtC14softposreaderd23DefaultSecureTimeKeeper"
+ "_TtC14softposreaderd23DefaultTimeTokenManager"
+ "_TtC14softposreaderd23LaunchFeedbackFramework"
+ "_TtC14softposreaderd24DefaultManagedDictionary"
+ "_TtC14softposreaderd24DefaultSecureChannelHTTP"
+ "_TtC14softposreaderd24MPOCDefaultMonitorLogger"
+ "_TtC14softposreaderd25MPOCDefaultMonitorBackend"
+ "_TtC14softposreaderd25MPOCDefaultMonitorManager"
+ "_TtC14softposreaderd25MPOCOfflineMonitorBackend"
+ "_TtC14softposreaderd25MPOCVolatileMonitorLogger"
+ "_TtC14softposreaderd26CertificateVerifierFactory"
+ "_TtC14softposreaderd26DefaultSecureChannelCrypto"
+ "_TtC14softposreaderd26MPOCDefaultAttestationData"
+ "_TtC14softposreaderd26OfflineConfiguratorBackend"
+ "_TtC14softposreaderd26SecureChannelCryptoFactory"
+ "_TtC14softposreaderd26VolatilePersistenceFactory"
+ "_TtC14softposreaderd29MPOCDefaultAttestationManager"
+ "_TtC14softposreaderd31SecureElementTransceiverAdaptor"
+ "_TtC14softposreaderd37MPOCDefaultAttestationOfflineVerifier"
+ "_TtC14softposreaderd5Depot"
+ "_TtC14softposreaderd6Primer"
+ "_TtC14softposreaderd6Reader"
+ "_TtC14softposreaderd7Monitor"
+ "_TtC14softposreaderd8CALogger"
+ "_TtC14softposreaderd8Provider"
+ "_TtC14softposreaderd9AAASigner"
+ "_TtC14softposreaderd9BAASigner"
+ "_TtC14softposreaderd9Inspector"
+ "_TtC14softposreaderd9SESSigner"
+ "_TtC14softposreaderd9SLAMSwift"
+ "_sendLogsWithError()"
+ "api/v3/kernelconfigurator/ota"
+ "bundleID"
+ "bundleIdentifier"
+ "cannot remove unused assets %@"
+ "cannot select applet %@"
+ "capks"
+ "capks: %s"
+ "casdCertificate"
+ "cod"
+ "coding key missing"
+ "collectValue(_:for:)"
+ "com.apple.softposreader.daily.provision"
+ "com.apple.softposreader.test.daily"
+ "configuredKernels"
+ "copyApplicationRecords:"
+ "cor"
+ "coreAnalyticsEventName"
+ "coreConfig id: %s"
+ "coreConfigId"
+ "cumulate(field:value:prod:)"
+ "defaultSefwURL"
+ "defaultTempSefwURL"
+ "deleteAll(session:forRecovery:)"
+ "detectedSEFWUpdate"
+ "error from kernel manager %@. use legacy flow"
+ "errorAppletSelect"
+ "errorReaderModeProtection"
+ "evaluateKernelAsset(session:kernelAsset:)"
+ "execute(payload:tpid:saftpid:launchSEStorageSheet:seStorageSheetBundleID:seStorageSheetSceneID:delegate:)"
+ "executeKernelAsset(session:assets:progress:)"
+ "executeLegacy(payload:tpid:saftpid:launchSEStorageSheet:seStorageSheetBundleID:seStorageSheetSceneID:delegate:)"
+ "expect ], }, : or string after whitespace"
+ "expecting \" in string"
+ "expecting ','"
+ "expecting '['"
+ "expecting ']'"
+ "expecting '{'"
+ "expecting JSON value"
+ "expecting `:`"
+ "expecting string"
+ "extract(fields:)"
+ "failed to execute kernel assets"
+ "failed to generate kernel asset"
+ "failed to select applet after removing unused assets"
+ "generateKernelAsset(payload:)"
+ "getBatchCountEstimate()"
+ "getDeviceState(session:)"
+ "getKernelManager(session:)"
+ "globalConfigId"
+ "gotRemoveCard"
+ "gotSeePhone"
+ "hardwareType"
+ "history"
+ "idx"
+ "increment(fields:prod:)"
+ "incrementCount(fields:)"
+ "init(backend:certificateManager:profileManager:attestationManager:monitorManager:auditor:systemInfo:managedData:signerFactory:secureTimeKeeper:analytics:secureElement:timeTokenManager:enforceJCOPVersion:launchFeedbackFramework:safCertificateValidity:kernelManagerWrapper:sesnapshotWrapper:)"
+ "init(dictionary:)"
+ "init(mode:defaultSendRate:safAttestationPeriod:persistence:secureTimeKeeper:secureElement:signer:monitorLogger:monitorBackend:attestationManager:monitorAnalytics:profileManager:delegate:)"
+ "init(timeTokenManager:secureTimeKeeper:secureElement:crypto:http:resourceTimeout:launchFeedbackFramework:)"
+ "initState"
+ "initWithBundleID:"
+ "initWithBundleID:lastUsedDate:"
+ "initWithNvm:cor:cod:idx:"
+ "initWithProvisionDataBlob:casdCertificate:rid:"
+ "inspectorProxy(reply:)"
+ "inspectorProxyWithReply:"
+ "install(token:launchSEStorageSheet:delegate:seStorageSheetBundleID:seStorageSheetSceneID:completion:)"
+ "install(token:tpid:saftpid:delegate:launchSEStorageSheet:seStorageSheetBundleID:seStorageSheetSceneID:completion:)"
+ "installRemoteScripts(token:tpid:saftpid:payload:isUsingLegacyFlow:launchSEStorageSheet:seStorageSheetBundleID:seStorageSheetSceneID:delegate:completion:)"
+ "installWithToken:launchSEStorageSheet:seStorageSheetBundleID:seStorageSheetSceneID:delegate:reply:"
+ "invalid JSON: %s"
+ "invalid cursor"
+ "isUsingLegacyFlow(session:)"
+ "jsblSequenceCounter"
+ "kForceDailyAnalyticsPOS"
+ "kForceDailyAnalyticsProvision"
+ "kernel manager flow"
+ "kernelManagerWrapper"
+ "lastAttestation"
+ "loadAndInstallBundleHash"
+ "lockedCurrState"
+ "monitorManagerState"
+ "no kernel manager"
+ "no secure element found"
+ "nvm"
+ "onFailure(error: %s, mode: %s)"
+ "otaTempSefwURL"
+ "outcomeStatusApproved"
+ "outcomeStatusDeclined"
+ "outcomeStatusEmpty"
+ "outcomeStatusEndApplication"
+ "outcomeStatusNA"
+ "outcomeStatusOnlineRequest"
+ "outcomeStatusSelectNext"
+ "outcomeStatusTryAgain"
+ "outcomeStatusTryAnotherInterface"
+ "performCleanupIfNoClients(force:)"
+ "pollingTracker"
+ "postOTA(token:payload:isUsingLegacyFlow:progressHandler:completion:)"
+ "producedError"
+ "producedResult"
+ "proxy"
+ "removeFirmware(type:)"
+ "removeUnusedAssets(session:)"
+ "saveNewFirmware(_:type:)"
+ "seStateInfo"
+ "sesnapshotWrapper"
+ "session busy %@"
+ "softposreaderd received CFNotification \"%@\",\nsending CoreAnalytics daily event now"
+ "softposreaderd.CoreDataWrapper"
+ "softposreaderd.DefaultPINAppletProxy"
+ "softposreaderd.ProvisionReadOperation"
+ "softposreaderd.ReadOperation"
+ "softposreaderd.RemoteInspector"
+ "softposreaderd/CertificateRole.swift"
+ "softposreaderd/Environment.swift"
+ "softposreaderd/Reader.swift"
+ "softposreaderd/SecureElementTransceiver.swift"
+ "startSecureElementManagerSessionAndReturnError:"
+ "startSecureElementManagerSessionWithTimeout:error:"
+ "startSecureElementReaderSessionAndReturnError:"
+ "stateInformationWithReply:"
+ "systemStatus"
+ "thermalIndicationFalse"
+ "thermalIndicationTrue"
+ "transceiveWithCapdu:reply:"
+ "unexpected JSON object"
+ "unexpected char %s"
+ "user default: %s"
+ "userCancelled"
+ "using legacy flow"
+ "using legacy flow for persistDownloadedScripts"
+ "using settings: %s"
+ "using streaming type custom decoder: %s"
+ "using the legacy flow"
+ "v60@0:8@16B24@28@36@44@?52"
+ "waiting for NFSecureElementManagerSession..."
- "\nclearOnDeselectMemory: "
- "\nclearOnResetMemory: "
- "%s SecureElementManagerSession ended"
- "%s startSecureElementManagerSession"
- "-----BEGIN CERTIFICATE-----\nMIIDDjCCArSgAwIBAgIIFAcxykcyQLwwCgYIKoZIzj0EAwIwdzErMCkGA1UEAwwi\nVGVzdCBBcHBsZSBTeXN0ZW0gSW50ZWdyYXRpb24gQ0EgNDEmMCQGA1UECwwdQXBw\nbGUgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkxEzARBgNVBAoMCkFwcGxlIEluYy4x\nCzAJBgNVBAYTAlVTMB4XDTIyMDQxODIwNTk0MVoXDTI0MDUxNzIxMDEwNlowRTEh\nMB8GA1UEAwwYcmV3cmFwLnRyZXgucWEuYXBwbGUuY29tMRMwEQYDVQQKDApBcHBs\nZSBJbmMuMQswCQYDVQQGEwJVUzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABH7W\npOA+xnhanLxWrxYWoWVyelVignfo1Tf0twZA6rsz7AJLfuqdPBRnjbqgaGMcoo6S\nGLU+gfqSmmPRlG44pHSjggFaMIIBVjAMBgNVHRMBAf8EAjAAMB8GA1UdIwQYMBaA\nFOmeXZBZYKCpAHokbTYKAxvnH8s1MEwGCCsGAQUFBwEBBEAwPjA8BggrBgEFBQcw\nAYYwaHR0cDovL29jc3AtdWF0LmNvcnAuYXBwbGUuY29tL29jc3AwNC10ZXN0YXNp\nY2E0MIGWBgNVHSAEgY4wgYswgYgGCSqGSIb3Y2QFATB7MHkGCCsGAQUFBwICMG0M\na1RoaXMgY2VydGlmaWNhdGUgaXMgdG8gYmUgdXNlZCBleGNsdXNpdmVseSBmb3Ig\nZnVuY3Rpb25zIGludGVybmFsIHRvIEFwcGxlIFByb2R1Y3RzIGFuZC9vciBBcHBs\nZSBwcm9jZXNzZXMuMB0GA1UdDgQWBBRZT+vFLq4RmdkO2IHmJhdgfSfZUzAOBgNV\nHQ8BAf8EBAMCB4AwDwYJKoZIhvdjZAwqBAIFADAKBggqhkjOPQQDAgNIADBFAiEA\nq2X2znUOjJwmj6QsgoK2URvFpUbVJxjxiqyY+wNznOMCID7YblL+aYHpRig6AMcC\n6nv+OxG3MRN9FJEHAYVWZuFs\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIDDDCCApOgAwIBAgIIA7no8mzsqqMwCgYIKoZIzj0EAwMwbDEgMB4GA1UEAwwX\nVGVzdCBBcHBsZSBSb290IENBIC0gRzMxJjAkBgNVBAsMHUFwcGxlIENlcnRpZmlj\nYXRpb24gQXV0aG9yaXR5MRMwEQYDVQQKDApBcHBsZSBJbmMuMQswCQYDVQQGEwJV\nUzAeFw0xNzAyMjEwMDMyMzBaFw0zMjAyMjEwMDMyMzBaMHcxKzApBgNVBAMMIlRl\nc3QgQXBwbGUgU3lzdGVtIEludGVncmF0aW9uIENBIDQxJjAkBgNVBAsMHUFwcGxl\nIENlcnRpZmljYXRpb24gQXV0aG9yaXR5MRMwEQYDVQQKDApBcHBsZSBJbmMuMQsw\nCQYDVQQGEwJVUzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABHEW/GTXJS94YltG\nXwQ+xlcWUo5wAzDc+3tIlOEMd0+UdNiavML8vxtMUzWCdkHzMpaaLSQ6zcSiwlI8\nhq78j+WjggESMIIBDjBTBggrBgEFBQcBAQRHMEUwQwYIKwYBBQUHMAGGN2h0dHA6\nLy9vY3NwLXVhdC5jb3JwLmFwcGxlLmNvbS9vY3NwMDMtdGVzdGFwcGxlcm9vdGNh\nZzMwHQYDVR0OBBYEFOmeXZBZYKCpAHokbTYKAxvnH8s1MA8GA1UdEwEB/wQFMAMB\nAf8wHwYDVR0jBBgwFoAU/EbYg2wf5vLc36eZF64LRGcXG0YwRAYDVR0fBD0wOzA5\noDegNYYzaHR0cDovL2NybC11YXQuY29ycC5hcHBsZS5jb20vdGVzdGFwcGxlcm9v\ndGNhZzMuY3JsMA4GA1UdDwEB/wQEAwIBBjAQBgoqhkiG92NkBgIRBAIFADAKBggq\nhkjOPQQDAwNnADBkAjAFc7NL/amfWuDjE3viRqZv2P9ru/pmfIly8YSkS6JC8wta\n/emIp34C4XnWXJyV6bYCMHXPZp6yaSK4EnbAyTHGqcMHZdw2nq1HTSLMbQKk0SSS\n9TOwIxx45GQCFTcsr6l6gw==\n-----END CERTIFICATE-----"
- "A0000008585353448100"
- "AnalyticsSendEventLazy: %s has payload: %s)"
- "BAA device identifiers is nil"
- "Badly formed object"
- "CADailyLogger.cumulate - CADailyEventField: %s already stored with value: %s"
- "CADailyLogger.cumulate - Stored CADailyEventField: %s, value: %s"
- "CADailyLogger.cumulate - User Defaults is nil"
- "CADailyLogger.extract - User Defaults is nil"
- "CADailyLogger.increment - User Defaults is nil"
- "CALogger.cumulate - daily collection disabled"
- "CALogger.incrementCount - daily collection disabled"
- "CALoggerProtocol: "
- "CALoggerProtocol: dependent"
- "CALoggerProtocol: independent"
- "CertificateManagerProtocol: "
- "CertificateManagerProtocol: dependent"
- "CertificateManagerProtocol: independent"
- "CertificateVerifierFactoryProtocol: "
- "CertificateVerifierFactoryProtocol: dependent"
- "CertificateVerifierFactoryProtocol: independent"
- "ComponentAuditorFactoryProtocol: "
- "ComponentAuditorFactoryProtocol: dependent"
- "ComponentAuditorFactoryProtocol: independent"
- "ConfiguratorAnalytics: "
- "ConfiguratorAnalytics: dependent"
- "ConfiguratorAnalytics: independent"
- "ConfiguratorBackendProtocol: "
- "ConfiguratorBackendProtocol: dependent"
- "ConfiguratorBackendProtocol: independent"
- "CoreDataManager: "
- "CoreDataManager: dependent"
- "CoreDataManager: independent"
- "Could not perform cleanup script"
- "Could not perform cleanup script: %@"
- "Could not refresh time token"
- "Could not start SecureElementManagerSession to clear PAN: %@"
- "EnvironmentProtocol: "
- "EnvironmentProtocol: dependent"
- "EnvironmentProtocol: independent"
- "Error from startSecureElementManagerSession: %@"
- "Error from startSecureElementReaderSession: %s"
- "Failed to Select PIN applet to clear PAN"
- "Failed to remove applets: NFC disabled"
- "Feature Flag Enabled: Manual Post CA Daily"
- "Feature Flag Enabled: Manual Send Monitoring Logs"
- "GlobalConfigSLAMLoadStatus"
- "GlobalConfigSLAMLoadTime"
- "GlobalConfigSLAMSize"
- "GlobalID"
- "HostConfiguration: %{public}s"
- "Invalid monitoring instruction"
- "JSON base64 string value doesn't start and end with \"."
- "KCSOTAResponse: %s"
- "Kernel Config Not Valid"
- "KernelSLAMLoadStatus"
- "KernelSLAMLoadTime"
- "KernelSLAMSize"
- "LaunchFeedbackFrameworkProtocol: "
- "LaunchFeedbackFrameworkProtocol: dependent"
- "LaunchFeedbackFrameworkProtocol: independent"
- "MPOCAttestationDataProtocol: "
- "MPOCAttestationDataProtocol: dependent"
- "MPOCAttestationDataProtocol: independent"
- "MPOCAttestationManagerProtocol: "
- "MPOCAttestationManagerProtocol: dependent"
- "MPOCAttestationManagerProtocol: independent"
- "MPOCAttestationOfflineVerifierProtocol: "
- "MPOCAttestationOfflineVerifierProtocol: dependent"
- "MPOCAttestationOfflineVerifierProtocol: independent"
- "MPOCMonitorBackendProtocol: "
- "MPOCMonitorBackendProtocol: dependent"
- "MPOCMonitorBackendProtocol: independent"
- "MPOCMonitorLoggerProtocol: "
- "MPOCMonitorLoggerProtocol: dependent"
- "MPOCMonitorLoggerProtocol: independent"
- "MPOCMonitorManagerProtocol: "
- "MPOCMonitorManagerProtocol: dependent"
- "MPOCMonitorManagerProtocol: independent"
- "MPOCMonitorResponse"
- "ManagedDictionaryProtocol: "
- "ManagedDictionaryProtocol: dependent"
- "ManagedDictionaryProtocol: independent"
- "MonitorAnalytics: "
- "MonitorAnalytics: dependent"
- "MonitorAnalytics: independent"
- "NFSecureElementManagerSession started from %s"
- "NFSecureElementReaderSession started"
- "Number of clients changed from %ld to %ld, removing applets now..."
- "Optional<SecureElementProtocol>: "
- "Optional<SecureElementProtocol>: dependent"
- "Optional<SecureElementProtocol>: independent"
- "PayResultOther"
- "PayResultUnknown"
- "PerformSECleanup"
- "PersistenceFactoryProtocol: "
- "PersistenceFactoryProtocol: dependent"
- "PersistenceFactoryProtocol: independent"
- "Prepare failed because Kernel Config is Invalid"
- "Prepare failed because of Full Memory"
- "ProfileManagerProtocol: "
- "ProfileManagerProtocol: dependent"
- "ProfileManagerProtocol: independent"
- "ProfileSLAMLoadStatus"
- "ProfileSLAMLoadTime"
- "ProfileSLAMSize"
- "ProvisionReader deinit but operation in progress: client must have crashed"
- "ReaderAnalytics: "
- "ReaderAnalytics: dependent"
- "ReaderAnalytics: independent"
- "Received CFNotification to post the CA daily event now"
- "SE memory: %{public}s"
- "SLAMDeleteBee"
- "SLAMDeleteBeeLegacy"
- "SPREngine.CoreDataWrapper"
- "SPREngine.DefaultPINAppletProxy"
- "SPREngine.ProvisionReadOperation"
- "SPREngine.ReadOperation"
- "SPREngine/CertificateRole.swift"
- "SPREngine/Environment.swift"
- "SPREngine/Reader.swift"
- "SecureChannelCryptoFactoryProtocol: "
- "SecureChannelCryptoFactoryProtocol: dependent"
- "SecureChannelCryptoFactoryProtocol: independent"
- "SecureChannelFactoryProtocol: "
- "SecureChannelFactoryProtocol: dependent"
- "SecureChannelFactoryProtocol: independent"
- "SecureChannelHTTPProtocol: "
- "SecureChannelHTTPProtocol: dependent"
- "SecureChannelHTTPProtocol: independent"
- "SecureElementProtocol: "
- "SecureElementProtocol: dependent"
- "SecureElementProtocol: independent"
- "SecureTimeKeeper: "
- "SecureTimeKeeper: dependent"
- "SecureTimeKeeper: independent"
- "SecurityAnalytics: "
- "SecurityAnalytics: dependent"
- "SecurityAnalytics: independent"
- "Session ended"
- "SignerFactoryProtocol: "
- "SignerFactoryProtocol: dependent"
- "SignerFactoryProtocol: independent"
- "SystemInfoProtocol: "
- "SystemInfoProtocol: dependent"
- "SystemInfoProtocol: independent"
- "The given data was not valid JSON.\nNo string key for value in object"
- "TimeKeeper: dependent"
- "TimeKeeper: independent"
- "TimeTokenManager: "
- "TimeTokenManager: dependent"
- "TimeTokenManager: independent"
- "Unescaped control character.\nmissing ending \" in string"
- "Unescaped control character.\nmissing startng \" in string"
- "Unescaped control character. Missing ending \" in string"
- "Unescaped control character. Missing starting \" in base64"
- "Vv44@0:8@\"NSString\"16B24@\"<SPRInstallDelegate>\"28@?<v@?@\"SPRInstallData\"@\"NSError\">36"
- "Vv44@0:8@16B24@28@?36"
- "_TtC9SPREngine10SystemInfo"
- "_TtC9SPREngine10Terminator"
- "_TtC9SPREngine11Environment"
- "_TtC9SPREngine11GlobalState"
- "_TtC9SPREngine11NullAuditor"
- "_TtC9SPREngine12Configurator"
- "_TtC9SPREngine12TaggedObject"
- "_TtC9SPREngine13CADailyLogger"
- "_TtC9SPREngine13ReadOperation"
- "_TtC9SPREngine13SecureChannel"
- "_TtC9SPREngine13SecureElement"
- "_TtC9SPREngine13SignerFactory"
- "_TtC9SPREngine14ProfileManager"
- "_TtC9SPREngine15CoreDataManager"
- "_TtC9SPREngine15CoreDataWrapper"
- "_TtC9SPREngine15ProvisionReader"
- "_TtC9SPREngine15ReaderAnalytics"
- "_TtC9SPREngine15StatusInspector"
- "_TtC9SPREngine16ComponentAuditor"
- "_TtC9SPREngine16MPOCMonitorStore"
- "_TtC9SPREngine16MonitorAnalytics"
- "_TtC9SPREngine16NFSESessionBlock"
- "_TtC9SPREngine17DefaultTimeKeeper"
- "_TtC9SPREngine17PayAppletResponse"
- "_TtC9SPREngine17ReadDelegateRelay"
- "_TtC9SPREngine17SecurityAnalytics"
- "_TtC9SPREngine18AAASigningIdentity"
- "_TtC9SPREngine18BAASigningIdentity"
- "_TtC9SPREngine18CertificateManager"
- "_TtC9SPREngine18NullAuditorFactory"
- "_TtC9SPREngine18PersistenceFactory"
- "_TtC9SPREngine18ProvisionAnalytics"
- "_TtC9SPREngine18SESSigningIdentity"
- "_TtC9SPREngine18VolatilePersisting"
- "_TtC9SPREngine19ConfiguratorBackend"
- "_TtC9SPREngine19ReaderConfiguration"
- "_TtC9SPREngine20DefaultPINController"
- "_TtC9SPREngine20KCSOTAResponseParser"
- "_TtC9SPREngine20SecureChannelFactory"
- "_TtC9SPREngine21ConfiguratorAnalytics"
- "_TtC9SPREngine21DefaultPINAppletProxy"
- "_TtC9SPREngine21PrimaryAccountWatcher"
- "_TtC9SPREngine22ProvisionReadOperation"
- "_TtC9SPREngine23ComponentAuditorFactory"
- "_TtC9SPREngine23DefaultSecureTimeKeeper"
- "_TtC9SPREngine23DefaultTimeTokenManager"
- "_TtC9SPREngine23LaunchFeedbackFramework"
- "_TtC9SPREngine24DefaultManagedDictionary"
- "_TtC9SPREngine24DefaultSecureChannelHTTP"
- "_TtC9SPREngine24MPOCDefaultMonitorLogger"
- "_TtC9SPREngine25MPOCDefaultMonitorBackend"
- "_TtC9SPREngine25MPOCDefaultMonitorManager"
- "_TtC9SPREngine25MPOCOfflineMonitorBackend"
- "_TtC9SPREngine25MPOCVolatileMonitorLogger"
- "_TtC9SPREngine26CertificateVerifierFactory"
- "_TtC9SPREngine26DefaultSecureChannelCrypto"
- "_TtC9SPREngine26MPOCDefaultAttestationData"
- "_TtC9SPREngine26OfflineConfiguratorBackend"
- "_TtC9SPREngine26SecureChannelCryptoFactory"
- "_TtC9SPREngine26VolatilePersistenceFactory"
- "_TtC9SPREngine29MPOCDefaultAttestationManager"
- "_TtC9SPREngine37MPOCDefaultAttestationOfflineVerifier"
- "_TtC9SPREngine5Depot"
- "_TtC9SPREngine6Primer"
- "_TtC9SPREngine6Reader"
- "_TtC9SPREngine7Monitor"
- "_TtC9SPREngine8CALogger"
- "_TtC9SPREngine8Provider"
- "_TtC9SPREngine9AAASigner"
- "_TtC9SPREngine9BAASigner"
- "_TtC9SPREngine9SESSigner"
- "_TtC9SPREngine9SLAMSwift"
- "_sendLogsWithError(sendAll:)"
- "an empty JSON value, missing coding key"
- "applet cannot be found"
- "attestService"
- "availablePersistent"
- "availablePersistent: "
- "clearOnDeselectMemory"
- "clearOnResetMemory"
- "connectToServer:initialClientRequestInfo:callback:"
- "decoding %s"
- "decoding %s: %s"
- "decoding host config"
- "delete applet: %@"
- "delete legacy applet: %@"
- "deletePayApplet()"
- "execute(payload:tpid:saftpid:isAvailableMemoryLow:delegate:)"
- "failed to perform SE cleanup %@.\nApple Pay Servers Environment wasn't set.\nNo instances to clean up"
- "hostConfiguration: "
- "init(backend:certificateManager:profileManager:attestationManager:monitorManager:auditor:systemInfo:managedData:signerFactory:secureTimeKeeper:analytics:secureElement:timeTokenManager:enforceJCOPVersion:launchFeedbackFramework:safCertificateValidity:)"
- "init(mode:defaultSendRate:safAttestationPeriod:persistence:secureTimeKeeper:secureElement:signer:monitorLogger:monitorBackend:attestationManager:monitorAnalytics:profileManager:)"
- "init(timeTokenManager:secureTimeKeeper:secureElement:crypto:http:resourceTimeout:)"
- "initWithProvisionDataBlob:casdCertificate:"
- "install(token:delegate:completion:)"
- "install(token:tpid:saftpid:delegate:completion:isPerformSECleanup:)"
- "installRemoteScripts(token:tpid:saftpid:payload:isAvailableMemoryLow:delegate:completion:)"
- "installWithToken:force:delegate:reply:"
- "invalid JSON string with non utf8 encoding"
- "invalid range %s"
- "kSoftPOSReaderCADailyForcePost"
- "kernelAppletScript: "
- "nil session"
- "no pending session"
- "no post-processing for applet status \"\n%s"
- "null"
- "null host config"
- "null profile"
- "null script"
- "onFailure(error: %s"
- "performCleanupIfNoClients()"
- "performCleanupScript()"
- "pollingActiveA"
- "pollingActiveB"
- "pollingRestart"
- "pollingRestartByApplet"
- "postOTA(token:payload:progressHandler:completion:)"
- "safValidationCertificate"
- "session ended for remove applets"
- "session not available to remove applets: %@"
- "sharedRemoteAdminManager"
- "snapshot: %s"
- "softposreaderd main: SecureElementManagerSession ended"
- "softposreaderd.%s"
- "startReaderSession(): start timed out"
- "startSecureElementManagerSession error: %s"
- "startSecureElementReaderSession() TIMED OUT"
- "successfully perform SE cleanup"
- "timeout to get session for status inspector"
- "timeout, fail to obtain manager session"
- "try perform SE cleanup and try again"
- "using streaming type custom decoder"
- "v16@?0@\"NSError\"8"
- "v44@0:8@16B24@28@?36"
- "waiting for NFSecureElementManagerSession ..."
- "waiting for NFSession ..."
- "waiting for eSE..."

```
