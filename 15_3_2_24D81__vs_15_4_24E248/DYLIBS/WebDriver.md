## WebDriver

> `/System/Library/PrivateFrameworks/WebDriver.framework/Versions/A/WebDriver`

```diff

-620.2.4.11.6
-  __TEXT.__text: 0x806b8
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x50d4
-  __TEXT.__cstring: 0x9de3
-  __TEXT.__oslogstring: 0x327c
-  __TEXT.__const: 0x5192
-  __TEXT.__gcc_except_tab: 0x6dac
+621.1.15.11.10
+  __TEXT.__text: 0x82490
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_methlist: 0x5a88
+  __TEXT.__cstring: 0x9f36
+  __TEXT.__const: 0x51b2
+  __TEXT.__gcc_except_tab: 0x7070
+  __TEXT.__oslogstring: 0x3436
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2648
+  __TEXT.__unwind_info: 0x2700
   __TEXT.__objc_classname: 0xa7d
-  __TEXT.__objc_methname: 0xc71c
+  __TEXT.__objc_methname: 0xc76e
   __TEXT.__objc_methtype: 0x244a
-  __TEXT.__objc_stubs: 0xa440
-  __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0x14d0
+  __TEXT.__objc_stubs: 0xa480
+  __DATA_CONST.__got: 0x5d8
+  __DATA_CONST.__const: 0x1650
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33f0
+  __DATA_CONST.__objc_selrefs: 0x34c0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x238
-  __AUTH_CONST.__auth_got: 0x6d8
-  __AUTH_CONST.__const: 0x1e10
-  __AUTH_CONST.__cfstring: 0x9220
-  __AUTH_CONST.__objc_const: 0xa180
+  __AUTH_CONST.__auth_got: 0x718
+  __AUTH_CONST.__const: 0x1e60
+  __AUTH_CONST.__cfstring: 0x9280
+  __AUTH_CONST.__objc_const: 0x8f98
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F20AFAA7-24B4-3AE7-BC9E-37C3473C905C
-  Functions: 2393
-  Symbols:   6001
-  CStrings:  5355
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  UUID: FFBF9FE0-1FBB-3124-B09E-A491C8234157
+  Functions: 2478
+  Symbols:   6205
+  CStrings:  5386
 
Symbols:
+ +[HTTPConnection initialize].cold.1
+ +[HTTPServer executeBonjourBlock:].cold.1
+ +[WDDiagnosticUtilities sharedInstance].cold.1
+ +[WDProtocolTypeConversions(AutomationDomain) _parseWebExtensionResourceOptions:fromPayload:]
+ -[DDAbstractDatabaseLogger deleteInterval].cold.1
+ -[DDAbstractDatabaseLogger deleteInterval].cold.2
+ -[DDAbstractDatabaseLogger deleteOnEverySave].cold.1
+ -[DDAbstractDatabaseLogger deleteOnEverySave].cold.2
+ -[DDAbstractDatabaseLogger maxAge].cold.1
+ -[DDAbstractDatabaseLogger maxAge].cold.2
+ -[DDAbstractDatabaseLogger saveInterval].cold.1
+ -[DDAbstractDatabaseLogger saveInterval].cold.2
+ -[DDAbstractDatabaseLogger saveThreshold].cold.1
+ -[DDAbstractDatabaseLogger saveThreshold].cold.2
+ -[DDAbstractDatabaseLogger setDeleteInterval:].cold.1
+ -[DDAbstractDatabaseLogger setDeleteOnEverySave:].cold.1
+ -[DDAbstractDatabaseLogger setMaxAge:].cold.1
+ -[DDAbstractDatabaseLogger setSaveInterval:].cold.1
+ -[DDAbstractDatabaseLogger setSaveThreshold:].cold.1
+ -[DDAbstractLogger logFormatter].cold.1
+ -[DDAbstractLogger logFormatter].cold.2
+ -[DDAbstractLogger setLogFormatter:].cold.1
+ -[DDAbstractLogger setLogFormatter:].cold.2
+ -[DDFileLogger rollLogFile].cold.1
+ -[DDFileLogger setMaximumFileSize:].cold.1
+ -[DDFileLogger setMaximumFileSize:].cold.2
+ -[DDFileLogger setRollingFrequency:].cold.1
+ -[DDFileLogger setRollingFrequency:].cold.2
+ -[GCDAsyncReadPacket readLengthForNonTermWithHint:].cold.1
+ -[GCDAsyncReadPacket readLengthForNonTermWithHint:].cold.2
+ -[GCDAsyncReadPacket readLengthForTermWithHint:shouldPreBuffer:].cold.1
+ -[GCDAsyncReadPacket readLengthForTermWithHint:shouldPreBuffer:].cold.2
+ -[GCDAsyncReadPacket readLengthForTermWithPreBuffer:found:].cold.1
+ -[GCDAsyncReadPacket readLengthForTermWithPreBuffer:found:].cold.2
+ -[GCDAsyncReadPacket searchForTermAfterPreBuffering:].cold.1
+ -[GCDAsyncSocket closeWithError:].cold.1
+ -[GCDAsyncSocket completeCurrentRead].cold.1
+ -[GCDAsyncSocket completeCurrentWrite].cold.1
+ -[GCDAsyncSocket connectWithAddress4:address6:error:].cold.1
+ -[GCDAsyncSocket didConnect:].cold.1
+ -[GCDAsyncSocket didNotConnect:error:].cold.1
+ -[GCDAsyncSocket doReadData].cold.1
+ -[GCDAsyncSocket doReadData].cold.2
+ -[GCDAsyncSocket flushSSLBuffers].cold.1
+ -[GCDAsyncSocket initWithDelegate:delegateQueue:socketQueue:].cold.1
+ -[GCDAsyncSocket initWithDelegate:delegateQueue:socketQueue:].cold.2
+ -[GCDAsyncSocket initWithDelegate:delegateQueue:socketQueue:].cold.3
+ -[GCDAsyncSocket lookup:didFail:].cold.1
+ -[GCDAsyncSocket lookup:didSucceedWithAddress4:address6:].cold.1
+ -[GCDAsyncSocket lookup:didSucceedWithAddress4:address6:].cold.2
+ -[GCDAsyncSocket maybeClose].cold.1
+ -[GCDAsyncSocket maybeDequeueRead].cold.1
+ -[GCDAsyncSocket maybeDequeueWrite].cold.1
+ -[GCDAsyncSocket preConnectWithInterface:error:].cold.1
+ -[HTTPConnection dateAsString:].cold.1
+ -[HTTPConnection replyToHTTPRequest].cold.1
+ -[HTTPConnection socket:didWriteDataWithTag:].cold.1
+ -[HTTPServer publishBonjour].cold.1
+ -[HTTPServer unpublishBonjour].cold.1
+ -[RoutingConnection initWithAsyncSocket:configuration:].cold.1
+ -[WDHTTPDriverInterface httpServer]
+ -[WDProtocolAutomationCookie setSameSite:].cold.1
+ -[WDProtocolAutomationInputSource setSourceType:].cold.1
+ -[WDProtocolAutomationInputSourceState pressedVirtualKeys].cold.2
+ -[WDProtocolAutomationInputSourceState setMouseInteraction:].cold.1
+ -[WDProtocolAutomationInputSourceState setOrigin:].cold.1
+ -[WDProtocolAutomationInputSourceState setPressedButton:].cold.1
+ -[WDProtocolAutomationInteractionStep states].cold.2
+ -[WDProtocolAutomationKeyboardInteraction key].cold.2
+ -[WDProtocolAutomationKeyboardInteraction setKey:].cold.1
+ -[WDProtocolAutomationKeyboardInteraction setType:].cold.1
+ -[WDProtocolAutomationSessionPermissionData permission].cold.1
+ -[WDProtocolAutomationSessionPermissionData setPermission:].cold.1
+ -[WDProtocolAutomationVirtualAuthenticatorConfiguration extensions].cold.2
+ -[WDProtocolAutomationVirtualAuthenticatorConfiguration setProtocol:].cold.1
+ -[WDProtocolAutomationVirtualAuthenticatorConfiguration setTransport:].cold.1
+ -[WDProtocolAutomationVirtualAuthenticatorConfiguration uvm].cold.2
+ -[WDProtocolBackendProxy sendCommand:parameters:responseHandler:].cold.1
+ -[WDProtocolBackendProxy sendCommand:parameters:responseHandler:].cold.2
+ -[WDProtocolBackendProxy sendCommand:parameters:responseHandler:].cold.3
+ -[WDProtocolModel encodedMessageForCommand:withParameters:].cold.2
+ -[WDProtocolModel encodedMessageForCommand:withParameters:].cold.3
+ -[WDProtocolType encodedValueForInstance:].cold.1
+ -[WDRemoteSessionManager _initializeSimulatorSupport].cold.2
+ -[WDRemoteSessionManager findSimulatorHostsMatchingCriteria:completionHandler:].cold.1
+ -[WebSocket readRequestBody].cold.1
+ -[WebSocket sendResponseBody:].cold.1
+ -[WebSocket sendResponseBody:].cold.2
+ GCC_except_table317
+ GCC_except_table333
+ GCC_except_table337
+ GCC_except_table345
+ GCC_except_table48
+ OBJC_IVAR_$_WDHTTPDriverInterface._httpServer
+ WDLoggingInitializeIfNecessary.cold.1
+ WDOSLogLauncher.cold.1
+ WDOSLogProtocol.cold.1
+ WDOSLogRouting.cold.1
+ WDOSLogSession.cold.1
+ WDOSLogTestHost.cold.1
+ WDOSLogValidation.cold.1
+ WDOSLogWebService.cold.1
+ WDOSLogXPCService.cold.1
+ WDSafariDriverMain.cold.5
+ WDSafariDriverMain.cold.6
+ WDSafariDriverMain.cold.7
+ WDSafariDriverMain.cold.8
+ _OBJC_CLASS_$_NSXPCListener
+ _OUTLINED_FUNCTION_7
+ _WBSEnableSandboxStyleFileQuarantine
+ _WDErrorDomain
+ _WDXPCServiceMain
+ _ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESI_LSL_0EE6rehashEjPSB_.cold.1
+ __42-[HTTPAsyncFileResponse readDataOfLength:]_block_invoke.cold.1
+ __50-[WDHTTPService destroySession:completionHandler:]_block_invoke.92
+ __74-[WDRemoteSession performInteractions:withInputSources:completionHandler:]_block_invoke_3.cold.1
+ __MergedGlobals
+ __ZL20sessionStateToString24WDRemoteSessionHostState
+ __ZN3WTF17HashMapTranslatorINS_7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENSD_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESC_E9translateIRKS2_NS_12KeyValuePairIS2_SA_EEZNSI_9inlineAddISN_NS3_INS4_10ObjectBaseENS6_ISR_EENS8_ISR_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_SP_NS_24KeyValuePairKeyExtractorISP_EESC_SJ_SE_LSH_0EEES2_SP_SZ_SC_SJ_SE_EEEEOT_OT0_EUlvE_EEvRS15_S14_RKT1_
+ __ZN3WTF17HashMapTranslatorINS_7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENSD_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESC_E9translateIRKS2_NS_12KeyValuePairIS2_SA_EEZNSI_9inlineAddISN_SA_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_SP_NS_24KeyValuePairKeyExtractorISP_EESC_SJ_SE_LSH_0EEES2_SP_SV_SC_SJ_SE_EEEEOT_OT0_EUlvE_EEvRS11_S10_RKT1_
+ __ZN3WTF20initializeMainThreadEv
+ __ZN3WTF7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS1_EENS_10HashTraitsIS1_EENSC_IS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE9inlineSetIRKS1_NS2_INS3_10ObjectBaseENS5_ISL_EENS7_ISL_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS1_NS_12KeyValuePairIS1_S9_EENS_24KeyValuePairKeyExtractorIST_EESB_NSH_18KeyValuePairTraitsESD_LSG_0EEES1_ST_SV_SB_SW_SD_EEEEOT_OT0_
+ __ZN3WTF7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS1_EENS_10HashTraitsIS1_EENSC_IS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE9inlineSetIRKS1_S9_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS1_NS_12KeyValuePairIS1_S9_EENS_24KeyValuePairKeyExtractorISP_EESB_NSH_18KeyValuePairTraitsESD_LSG_0EEES1_SP_SR_SB_SS_SD_EEEEOT_OT0_
+ __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESI_LSL_0EE17lookupForReinsertERKS1_
+ __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESI_LSL_0EE6expandEPSB_
+ __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE18KeyValuePairTraitsESI_LSL_0EE6rehashEjPSB_
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ __ZNSt3__123__lower_bound_bisectingB8sn190102INS_17_ClassicAlgPolicyEPKNS_4pairIN3WTF28ComparableASCIISubsetLiteralILNS3_11ASCIISubsetE0EEE30WDProtocolAutomationVirtualKeyEENS3_20ComparableStringViewENS_10__identityEZNKS3_14SortedArrayMapIA70_S8_E6tryGetINS3_6StringEEEPKS7_RKT_EUlRSK_RT0_E_EESO_SO_RKT1_NS_15iterator_traitsISO_E15difference_typeERT3_RT2_
+ __ZNSt3__123__lower_bound_bisectingB8sn190102INS_17_ClassicAlgPolicyEPKNS_4pairIN3WTF28ComparableASCIISubsetLiteralILNS3_11ASCIISubsetE0EEE32WDProtocolAutomationErrorMessageEENS3_20ComparableStringViewENS_10__identityEZNKS3_14SortedArrayMapIA22_S8_E6tryGetINS3_6StringEEEPKS7_RKT_EUlRSK_RT0_E_EESO_SO_RKT1_NS_15iterator_traitsISO_E15difference_typeERT3_RT2_
+ __ZNSt3__127__throw_bad_optional_accessB8sn190102Ev
+ __ZZL17isInternalInstallvE10isInternal
+ __ZZL17isInternalInstallvE9onceToken
+ __ZZN9Inspector18fromProtocolStringI47WDProtocolAutomationWebExtensionResourceOptionsEENSt3__18optionalIT_EERKN3WTF6StringEE8mappings
+ ___61-[WDHTTPService requestSessionWithOptions:completionHandler:]_block_invoke
+ ___ZL25getSimServiceContextClassv_block_invoke.cold.1
+ ____ZL17isInternalInstallv_block_invoke
+ ___block_descriptor_40_ea8_32bs_e33_v24?0"NSError"8"<WDSession>"16l
+ ___chkstk_darwin
+ ___swift_reflection_version
+ __block_literal_global.101
+ __block_literal_global.103
+ __set_user_dir_suffix
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_WebDriver
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_WebDriver
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_WebDriver
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_math_$_WebDriver
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_signal_$_WebDriver
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_stdio_$_WebDriver
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftsys_time_$_WebDriver
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_FORCE_LOAD_$_swiftunistd_$_WebDriver
+ _confstr
+ _getenv
+ _objc_msgSend$httpServer
+ _objc_msgSend$serviceListener
+ _payloadTypeToJSONString
+ _realpath$DARWIN_EXTSN
+ _sandbox_free_error
+ _sandbox_init_with_parameters
+ isInternalInstall.cold.1
- -[WDHTTPDriverInterface server]
- GCC_except_table316
- GCC_except_table332
- GCC_except_table336
- GCC_except_table344
- OBJC_IVAR_$_WDHTTPDriverInterface._server
- __50-[WDHTTPService destroySession:completionHandler:]_block_invoke.89
- __ZGVZL19setUpSignalHandlersP23WDSafariDriverXPCClientE12sighupSource
- __ZGVZL19setUpSignalHandlersP23WDSafariDriverXPCClientE12sigintSource
- __ZGVZL19setUpSignalHandlersP23WDSafariDriverXPCClientE13sigtermSource
- __ZN3WTF17HashMapTranslatorINS_7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENSD_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESC_E9translateIRKS2_NS_12KeyValuePairIS2_SA_EEZNSH_9inlineAddISM_NS3_INS4_10ObjectBaseENS6_ISQ_EENS8_ISQ_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_SO_NS_24KeyValuePairKeyExtractorISO_EESC_SI_SE_EES2_SO_SY_SC_SI_SE_EEEEOT_OT0_EUlvE_EEvRS14_S13_RKT1_
- __ZN3WTF17HashMapTranslatorINS_7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENSD_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESC_E9translateIRKS2_NS_12KeyValuePairIS2_SA_EEZNSH_9inlineAddISM_SA_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_SO_NS_24KeyValuePairKeyExtractorISO_EESC_SI_SE_EES2_SO_SU_SC_SI_SE_EEEEOT_OT0_EUlvE_EEvRS10_SZ_RKT1_
- __ZN3WTF7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS1_EENS_10HashTraitsIS1_EENSC_IS9_EENS_15HashTableTraitsEE9inlineSetIRKS1_NS2_INS3_10ObjectBaseENS5_ISK_EENS7_ISK_EEEEEENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS1_NS_12KeyValuePairIS1_S9_EENS_24KeyValuePairKeyExtractorISS_EESB_NSG_18KeyValuePairTraitsESD_EES1_SS_SU_SB_SV_SD_EEEEOT_OT0_
- __ZN3WTF7HashMapINS_6StringENS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS1_EENS_10HashTraitsIS1_EENSC_IS9_EENS_15HashTableTraitsEE9inlineSetIRKS1_S9_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS1_NS_12KeyValuePairIS1_S9_EENS_24KeyValuePairKeyExtractorISO_EESB_NSG_18KeyValuePairTraitsESD_EES1_SO_SQ_SB_SR_SD_EEEEOT_OT0_
- __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESI_E17lookupForReinsertERKS1_
- __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESI_E6expandEPSB_
- __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NS_3RefINS_8JSONImpl5ValueENS_12RawPtrTraitsIS5_EENS_21DefaultRefDerefTraitsIS5_EEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS1_EENS_7HashMapIS1_SA_SF_NS_10HashTraitsIS1_EENSH_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESI_E6rehashEjPSB_
- __ZNSt3__113__lower_boundB8sn180100INS_17_ClassicAlgPolicyEPKNS_4pairIN3WTF28ComparableASCIISubsetLiteralILNS3_11ASCIISubsetE0EEE30WDProtocolAutomationVirtualKeyEESA_NS3_20ComparableStringViewENS_10__identityEZNKS3_14SortedArrayMapIA70_S8_E6tryGetINS3_6StringEEEPKS7_RKT_EUlRSK_RT0_E_EESO_SO_T1_RKT2_RT4_RT3_
- __ZNSt3__127__throw_bad_optional_accessB8sn180100Ev
- __ZZL19setUpSignalHandlersP23WDSafariDriverXPCClientE12sighupSource
- __ZZL19setUpSignalHandlersP23WDSafariDriverXPCClientE12sigintSource
- __ZZL19setUpSignalHandlersP23WDSafariDriverXPCClientE13sigtermSource
- __block_literal_global.100
- __block_literal_global.98
- _abort
CStrings:
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/HTTPConnection.m"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/HTTPServer.m"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/Mime/MultipartFormDataParser.m"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/Mime/MultipartMessageHeader.m"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/Mime/MultipartMessageHeaderField.m"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPAsyncFileResponse.m"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPFileResponse.m"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/Framework/WDDiagnosticUtilities.m"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/Framework/WDRemoteSessionHost.mm"
+ "/AppleInternal/Library/BuildRoots/e3e14635-06d1-11f0-88e4-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/Framework/WDSafariDriverMain.mm"
+ "/Applications/Xcode.app/Contents/Developer"
+ "20621.1.15.11.10"
+ "APPLICATION_DIR"
+ "ArchivePath"
+ "Base64"
+ "Could not initialize the sandbox, error: %{public}s."
+ "Couldn't enable sandbox style file quarantine."
+ "Couldn't retrieve private cache directory path: %d."
+ "Couldn't retrieve private temporary directory path: %d."
+ "DARWIN_USER_CACHE_DIR"
+ "DARWIN_USER_TEMP_DIR"
+ "DEVELOPER_DIR"
+ "Error calling realpath on the home directory."
+ "Error calling realpath on the private cache directory path: %d."
+ "Error calling realpath on the private temporary directory path: %d."
+ "FRAMEWORKS_DIR"
+ "HOME"
+ "HOME_DIR"
+ "NoSuchExtension"
+ "Path"
+ "Started HTTP server, listening on %{public}@:%hu"
+ "T@\"WDHTTPServer\",R,N,V_httpServer"
+ "UnableToLoadExtension"
+ "UnableToUnloadExtension"
+ "WebExtensionResourceOptions"
+ "Whitelisting relocatable app bundle located at path: %@"
+ "_httpServer"
+ "_parseWebExtensionResourceOptions:fromPayload:"
+ "bad_optional_access was thrown in -fno-exceptions mode"
+ "com.apple.WebInspector"
+ "httpServer"
+ "serviceListener"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/HTTPConnection.m"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/HTTPServer.m"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/Mime/MultipartFormDataParser.m"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/Mime/MultipartMessageHeader.m"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/Mime/MultipartMessageHeaderField.m"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPAsyncFileResponse.m"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/External/HTTPServer/CocoaHTTPServer/Core/Responses/HTTPFileResponse.m"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/Framework/WDDiagnosticUtilities.m"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/Framework/WDRemoteSessionHost.mm"
- "/AppleInternal/Library/BuildRoots/d69f892e-f9f0-11ef-9008-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/WebDriver/Framework/WDSafariDriverMain.mm"
- "20620.2.4.11.6"
- "Started HTTP server, listening on %{public}@:%lu"
- "T@\"WDHTTPServer\",R,N,V_server"
- "_server"

```
