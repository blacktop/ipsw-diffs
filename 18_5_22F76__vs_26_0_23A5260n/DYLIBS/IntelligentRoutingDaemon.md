## IntelligentRoutingDaemon

> `/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon`

```diff

-96.0.6.0.1
-  __TEXT.__text: 0x69ea8
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x71ec
-  __TEXT.__oslogstring: 0x5de3
-  __TEXT.__cstring: 0x8426
-  __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x18f4
-  __TEXT.__unwind_info: 0x1890
-  __TEXT.__objc_classname: 0xed4
-  __TEXT.__objc_methname: 0x16737
-  __TEXT.__objc_methtype: 0x1e16
-  __TEXT.__objc_stubs: 0xdf20
-  __DATA_CONST.__got: 0x7a0
-  __DATA_CONST.__const: 0x1be8
-  __DATA_CONST.__objc_classlist: 0x428
+96.0.18.0.0
+  __TEXT.__text: 0x6bfc4
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x6f34
+  __TEXT.__gcc_except_tab: 0x1900
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x82fd
+  __TEXT.__oslogstring: 0x5e38
+  __TEXT.__swift5_typeref: 0x9b
+  __TEXT.__unwind_info: 0x1910
+  __TEXT.__eh_frame: 0x110
+  __TEXT.__objc_classname: 0xe33
+  __TEXT.__objc_methname: 0x16198
+  __TEXT.__objc_methtype: 0x1de7
+  __TEXT.__objc_stubs: 0xdcc0
+  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__const: 0x1bc8
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xf8
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e20
-  __DATA_CONST.__objc_superrefs: 0x2d0
+  __DATA_CONST.__objc_selrefs: 0x3d80
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x438
-  __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0x6440
-  __AUTH_CONST.__objc_const: 0xdbd0
-  __AUTH_CONST.__objc_intobj: 0x360
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__const: 0x728
+  __AUTH_CONST.__cfstring: 0x62a0
+  __AUTH_CONST.__objc_const: 0xd580
+  __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x928
-  __DATA.__data: 0xba0
+  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH.__objc_data: 0x7f0
+  __AUTH.__data: 0x30
+  __DATA.__objc_ivar: 0x8e4
+  __DATA.__data: 0xc60
   __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x2120
+  __DATA_DIRTY.__objc_data: 0x2030
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B3379C8E-95A9-3322-A0CB-4DBF94E0DF2E
-  Functions: 2559
-  Symbols:   9322
-  CStrings:  5547
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 92FE8DDB-6964-3E01-B692-F6A9856256C6
+  Functions: 2561
+  Symbols:   9385
+  CStrings:  5491
 
Symbols:
+ +[IRCandidateClassificationDetectorSameSpace isSameSpaceForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:]
+ +[IREventDO(extension) eventDOWithHomeType:]
+ +[IREventDO(extension) homeUserInteractionEvents]
+ +[IRMiloLslPredictionDO miloLslPredictionDOWithPredictionId:isPredictionValid:isMapValid:isMotionDetected:scores:predictionTime:]
+ +[IRServiceLogPrefix queueSpecific]
+ +[IRServiceStore fetchAllServicesContainingClientIdentifier:persistenceManager:]
+ -[IRBackgroundActivitiesManager queue]
+ -[IRBackgroundActivitiesManager scheduler]
+ -[IRBackgroundActivitiesManager setQueue:]
+ -[IRBackgroundActivitiesManager setScheduler:]
+ -[IRMiLoProvider _locationOfInterestToIRLocationSemantic:]
+ -[IRMiLoProvider _miloServiceStatusLogStringFromMap:]
+ -[IRMiLoProvider addLabelWithName:]
+ -[IRMiLoProvider addObserver:withToken:isLowLatency:]
+ -[IRMiLoProvider addObserver:withToken:isLowLatency:].cold.1
+ -[IRMiLoProvider connectionDidUpdateMap:]
+ -[IRMiLoProvider connectionDidUpdatePredictionContext:]
+ -[IRMiloLslPredictionDO copyWithReplacementIsMapValid:]
+ -[IRMiloLslPredictionDO copyWithReplacementIsMotionDetected:]
+ -[IRMiloLslPredictionDO copyWithReplacementIsPredictionValid:]
+ -[IRMiloLslPredictionDO initWithPredictionId:isPredictionValid:isMapValid:isMotionDetected:scores:predictionTime:]
+ -[IRMiloLslPredictionDO isMapValid]
+ -[IRMiloLslPredictionDO isMotionDetected]
+ -[IRMiloLslPredictionDO isPredictionValid]
+ -[IRMiloLslPredictionDO(Extension) scoreForPredictionEventEvent:]
+ -[IRSessionConnection _requestCurrentContextWithReply:]
+ -[IRSessionServer analyticsManager]
+ -[IRSessionServer cleanupManager]
+ -[IRSessionServer mobileAssetManager]
+ -[IRSessionServer setAnalyticsManager:]
+ -[IRSessionServer setCleanupManager:]
+ -[IRSessionServer setMobileAssetManager:]
+ GCC_except_table22
+ GCC_except_table24
+ GCC_except_table26
+ GCC_except_table50
+ _$s10Foundation4DateV19_bridgeToObjectiveCSo6NSDateCyF
+ _$s10Foundation4DateV36_unconditionallyBridgeFromObjectiveCyACSo6NSDateCSgFZ
+ _$s10Foundation4DateVMa
+ _$s2os32getNullTerminatedUTF8PointerImpl_21storingStringOwnersInSVSS_SpyypGSgztF
+ _$s2os6LoggerV24IntelligentRoutingDaemonE3log4type6prefix_ySo0a1_f1_G2_ta_S2StFZ
+ _$s2os6LoggerV24IntelligentRoutingDaemonE3log4type6prefix_ySo0a1_f1_G2_ta_S2StFZTf4nnnd_n
+ _$s2os6LoggerV24IntelligentRoutingDaemonE6logger33_B882461EA72BEADEBBE2EBBCD6F741B0LLACvpZ
+ _$s2os6LoggerV24IntelligentRoutingDaemonE6logger33_B882461EA72BEADEBBE2EBBCD6F741B0LL_WZ
+ _$s2os6LoggerV24IntelligentRoutingDaemonE6logger33_B882461EA72BEADEBBE2EBBCD6F741B0LL_Wz
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s2os6LoggerVMa
+ _$sSD10FoundationE19_bridgeToObjectiveCSo12NSDictionaryCyF
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSS_So9IRContextCTt0g5Tf4g_nTm
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSS4hash4intoys6HasherVz_tF
+ _$sSS6appendyySSF
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSSN
+ _$sSSSHsWP
+ _$sSS_So9IRContextCtMD
+ _$sSS_So9IRContextCtWOh
+ _$sSTsE10compactMapySayqd__Gqd__Sg7ElementQzKXEKlFShySo13IRCandidateDOCG_So27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE14ValidCandidate33_3480749DF8EC54F4C39A8B4AFF1FC6DFLLVTg506$sSo27fghi3C24jkl258E23generateClassifications22withCandiatesContainer11systemState013historyEventsL014miloPrediction012nearbyDeviceL014fillInspection4dateSbSo012IRCandidatesL2DOC_So08IRSystemnY0CSo09IRHistoryplY0CSo09IRMiloLslrY0CSgSo08IRNearbytlY0CSb10Foundation4DateVtFAbCE14m19Candidate33_3480749opqrstuv12DFLLVSgSo011D8Y0CXEfU_Tf1cn_n
+ _$sSTsE8contains5whereS2b7ElementQzKXE_tKFSaySSG_Tg5
+ _$sSTsSQ7ElementRpzrlE8containsySbABFSbABXEfU_SaySSG_TG5TA
+ _$sSa034_makeUniqueAndReserveCapacityIfNotB0yyFyXl_Ts5
+ _$sSa10FoundationE19_bridgeToObjectiveCSo7NSArrayCyF
+ _$sSa10FoundationE36_unconditionallyBridgeFromObjectiveCySayxGSo7NSArrayCSgFZ
+ _$sSa16_createNewBuffer14bufferIsUnique15minimumCapacity13growForAppendySb_SiSbtFyXl_Ts5
+ _$sSa37_appendElementAssumeUniqueAndCapacity_03newB0ySi_xntFyXl_Ts5
+ _$sSa6append10contentsOfyqd__n_t7ElementQyd__RszSTRd__lFs5UInt8V_SayAFGTgq5
+ _$sSh10FoundationE19_bridgeToObjectiveCSo5NSSetCyF
+ _$sSh10FoundationE36_unconditionallyBridgeFromObjectiveCyShyxGSo5NSSetCSgFZ
+ _$sSh15minimumCapacityShyxGSi_tcfC
+ _$sSh21_nonEmptyArrayLiteralShyxGSayxG_tcfCSo17IRCandidateResultC_Tt0g5Tf4g_n
+ _$sSh2eeoiySbShyxG_ABtFZSo17IRCandidateResultC_Tt1g5
+ _$sSh8IteratorV6_cocoaAByx_Gs10__CocoaSetVAACn_tcfC
+ _$sSh8IteratorV8_VariantOySo13IRCandidateDOC__GWOe
+ _$sSh8_VariantV6insertySb8inserted_x17memberAfterInserttxnFSo17IRCandidateResultC_Tg5
+ _$sShyShyxGqd__nc7ElementQyd__RszSTRd__lufCSo17IRCandidateResultC_SayAEGTt0g5Tf4g_n
+ _$sSiN
+ _$sSis23CustomStringConvertiblesWP
+ _$sSlsE3mapySayqd__Gqd__7ElementQzqd_0_YKXEqd_0_YKs5ErrorRd_0_r0_lFSaySo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE14ValidCandidate33_3480749DF8EC54F4C39A8B4AFF1FC6DFLLVG_So17IRCandidateResultCs5NeverOTg5
+ _$sSo13IRCandidateDOCML
+ _$sSo13IRCandidateDOCSo8NSObjectCSH10ObjectiveCWL
+ _$sSo13os_log_type_ta0A0E7defaultABvgZ
+ _$sSo16IRHistoryEventDOCML
+ _$sSo17IRCandidateResultCML
+ _$sSo17IRCandidateResultCMaTm
+ _$sSo17IRCandidateResultCSo8NSObjectCSH10ObjectiveCWL
+ _$sSo17IRCandidateResultCSo8NSObjectCSH10ObjectiveCWlTm
+ _$sSo18IRPolicyInspectionCML
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE13filterHistory_23withCandidatesContainerSo015IRHistoryEventsL2DOCAG_So012IRCandidateslO0CtF
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE13filterHistory_23withCandidatesContainerSo015IRHistoryEventsL2DOCAG_So012IRCandidateslO0CtFTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE17policyInspectionsSDySSSo18IRPolicyInspectionCGvg
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE17policyInspectionsSDySSSo18IRPolicyInspectionCGvgTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE17policyInspectionsSDySSSo18IRPolicyInspectionCGvpMV
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE17shouldRejectEvent_26withHistoryEventsContainer0K11SystemState12forCandidate4dateSbSo9IREventDOC_So09IRHistorymnU0CSo08IRSystempU0CSo011IRCandidateU0C10Foundation4DateVtF
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE17shouldRejectEvent_26withHistoryEventsContainer0K11SystemState12forCandidate4dateSbSo9IREventDOC_So09IRHistorymnU0CSo08IRSystempU0CSo011IRCandidateU0C10Foundation4DateVtFTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE19shouldConsiderEvent21forSignificantBundlesSbSo9IREventDOC_tF
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE19shouldConsiderEvent21forSignificantBundlesSbSo9IREventDOC_tFTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE21getSignificantBundles14withCandidates11fromHistoryShySo8IRBundleCGSo23IRCandidatesContainerDOC_So015IRHistoryEventsqR0CtF
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE21getSignificantBundles14withCandidates11fromHistoryShySo8IRBundleCGSo23IRCandidatesContainerDOC_So015IRHistoryEventsqR0CtFTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE23generateClassifications22withCandiatesContainer11systemState013historyEventsL014miloPrediction012nearbyDeviceL014fillInspection4dateSbSo012IRCandidatesL2DOC_So08IRSystemnY0CSo09IRHistoryplY0CSo09IRMiloLslrY0CSgSo08IRNearbytlY0CSb10Foundation4DateVtF
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE23generateClassifications22withCandiatesContainer11systemState013historyEventsL014miloPrediction012nearbyDeviceL014fillInspection4dateSbSo012IRCandidatesL2DOC_So08IRSystemnY0CSo09IRHistoryplY0CSo09IRMiloLslrY0CSgSo08IRNearbytlY0CSb10Foundation4DateVtFSo17IRCandidateResultCAbCE14ValidCandidate33_3480749DF8EC54F4C39A8B4AFF1FC6DFLLVXEfU0_
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE23generateClassifications22withCandiatesContainer11systemState013historyEventsL014miloPrediction012nearbyDeviceL014fillInspection4dateSbSo012IRCandidatesL2DOC_So08IRSystemnY0CSo09IRHistoryplY0CSo09IRMiloLslrY0CSgSo08IRNearbytlY0CSb10Foundation4DateVtFSo17IRCandidateResultCAbCE14ValidCandidate33_3480749DF8EC54F4C39A8B4AFF1FC6DFLLVXEfU0_TA
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE23generateClassifications22withCandiatesContainer11systemState013historyEventsL014miloPrediction012nearbyDeviceL014fillInspection4dateSbSo012IRCandidatesL2DOC_So08IRSystemnY0CSo09IRHistoryplY0CSo09IRMiloLslrY0CSgSo08IRNearbytlY0CSb10Foundation4DateVtFTf4ndnnddnn_n
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE23generateClassifications22withCandiatesContainer11systemState013historyEventsL014miloPrediction012nearbyDeviceL014fillInspection4dateSbSo012IRCandidatesL2DOC_So08IRSystemnY0CSo09IRHistoryplY0CSo09IRMiloLslrY0CSgSo08IRNearbytlY0CSb10Foundation4DateVtFTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE6PREFIX33_3480749DF8EC54F4C39A8B4AFF1FC6DFLLSSvgTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE6PREFIX33_3480749DF8EC54F4C39A8B4AFF1FC6DFLLSSvpWvd
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE7context33_3480749DF8EC54F4C39A8B4AFF1FC6DFLLSo9IRContextCvgTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE7context33_3480749DF8EC54F4C39A8B4AFF1FC6DFLLSo9IRContextCvpWvd
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE7context33_3480749DF8EC54F4C39A8B4AFF1FC6DFLLSo9IRContextCvsTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE8contextsSDySSSo9IRContextCGvg
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE8contextsSDySSSo9IRContextCGvgTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE8contextsSDySSSo9IRContextCGvpMV
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE9shouldAsk17forLowLatencyMiLo16historyEventsAscSbSo23IRCandidatesContainerDOC_SaySo014IRHistoryEventT0CGtF
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE9shouldAsk17forLowLatencyMiLo16historyEventsAscSbSo23IRCandidatesContainerDOC_SaySo014IRHistoryEventT0CGtFTf4nnd_n
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonE9shouldAsk17forLowLatencyMiLo16historyEventsAscSbSo23IRCandidatesContainerDOC_SaySo014IRHistoryEventT0CGtFTo
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonEABycfC
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonEABycfc
+ _$sSo27IRServicePackageAdapterHomeC24IntelligentRoutingDaemonEABycfcTo
+ _$sSo27IRServicePackageAdapterHomeCML
+ _$sSo27IRServicePackageAdapterHomeCMa
+ _$sSo27IRServicePackageAdapterHomeCfETo
+ _$sSo8IRBundleCML
+ _$sSo8IRBundleCSo8NSObjectCSH10ObjectiveCWL
+ _$sSo8NSObjectC10ObjectiveCE13_rawHashValue4seedS2i_tF
+ _$sSo8NSObjectC10ObjectiveCE2eeoiySbAB_ABtFZ
+ _$sSo8NSObjectCSH10ObjectiveCMc
+ _$sSo9IRContextCML
+ _$ss018_bridgeAnyObjectToB0yypyXlSgF
+ _$ss10_HashTableV8nextHole9atOrAfterAB6BucketVAF_tF
+ _$ss10_NativeSetV13copyAndResize8capacityySi_tFSo17IRCandidateResultC_Tg5
+ _$ss10_NativeSetV16_unsafeInsertNewyyxnFSo17IRCandidateResultC_Tg5
+ _$ss10_NativeSetV4copyyyFSo17IRCandidateResultC_Tg5
+ _$ss10_NativeSetV6resize8capacityySi_tFSo17IRCandidateResultC_Tg5
+ _$ss10_NativeSetV7isEqual2toSbs07__CocoaB0V_tFSo17IRCandidateResultC_Tg5
+ _$ss10_NativeSetV9insertNew_2at8isUniqueyxn_s10_HashTableV6BucketVSbtFSo17IRCandidateResultC_Tg5
+ _$ss10_NativeSetV_8capacityAByxGs07__CocoaB0Vn_SitcfCSo17IRCandidateResultC_Tt1g5
+ _$ss10__CocoaSetV12makeIteratorAB0D0CyF
+ _$ss10__CocoaSetV5countSivg
+ _$ss10__CocoaSetV6member3foryXlSgyXl_tF
+ _$ss10__CocoaSetV7isEqual2toSbAB_tF
+ _$ss10__CocoaSetV8IteratorC4nextyXlSgyF
+ _$ss10__CocoaSetV8containsySbyXlF
+ _$ss11_SetStorageC4copy8originalAByxGs05__RawaB0C_tFZ
+ _$ss11_SetStorageC6resize8original8capacity4moveAByxGs05__RawaB0C_SiSbtFZ
+ _$ss11_SetStorageC7convert_8capacityAByxGs07__CocoaA0V_SitFZ
+ _$ss11_SetStorageC8allocate8capacityAByxGSi_tFZ
+ _$ss11_SetStorageCMn
+ _$ss11_SetStorageCySo17IRCandidateResultCGMD
+ _$ss11_StringGutsV16_deconstructUTF87scratchyXlSg5owner_xSi6lengthSb11usesScratchSb15allocatedMemorytSwSg_ts8_PointerRzlFSV_Tgq5
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsV23_allocateForDeconstructyXl5owner_SVSi6lengthtyF
+ _$ss11_StringGutsV23_allocateForDeconstructyXl5owner_SVSi6lengthtyFTv_r
+ _$ss11_StringGutsV4growyySiF
+ _$ss11_StringGutsVN
+ _$ss12_ArrayBufferV19_getElementSlowPathyyXlSiFyXl_Ts5
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFSS_Tg5
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFs5UInt8V_Tgq5
+ _$ss13_StringObjectV10sharedUTF8SRys5UInt8VGvg
+ _$ss15ContiguousArrayV034_makeUniqueAndReserveCapacityIfNotD0yyFyXl_Ts5
+ _$ss15ContiguousArrayV12_endMutationyyFyXl_Ts5
+ _$ss15ContiguousArrayV15reserveCapacityyySiFyXl_Ts5
+ _$ss15ContiguousArrayV36_reserveCapacityAssumingUniqueBuffer8oldCountySi_tFyXl_Ts5
+ _$ss15ContiguousArrayV37_appendElementAssumeUniqueAndCapacity_03newD0ySi_xntFyXl_Ts5
+ _$ss18_CocoaArrayWrapperV8endIndexSivg
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss18_DictionaryStorageCySSSo18IRPolicyInspectionCGMD
+ _$ss18_DictionaryStorageCySSSo9IRContextCGMD
+ _$ss20__StaticArrayStorageCN
+ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tt1gq5
+ _$ss22__RawDictionaryStorageC4find_9hashValues10_HashTableV6BucketV6bucket_Sb5foundtx_SitSHRzlFSS_Tg5
+ _$ss22__RawDictionaryStorageC4findys10_HashTableV6BucketV6bucket_Sb5foundtxSHRzlFSS_Tg5
+ _$ss23CustomStringConvertibleP11descriptionSSvgTj
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss23_ContiguousArrayStorageCySSGMD
+ _$ss23_ContiguousArrayStorageCySS_So9IRContextCtGMD
+ _$ss23_ContiguousArrayStorageCys5UInt8VGMD
+ _$ss26DefaultStringInterpolationV06appendC0yyxlF
+ _$ss27_stringCompareWithSmolCheck__9expectingSbs11_StringGutsV_ADs01_G16ComparisonResultOtF
+ _$ss32_copyCollectionToContiguousArrayys0dE0Vy7ElementQzGxSlRzlFSS8UTF8ViewV_Tgq5
+ _$ss50ELEMENT_TYPE_OF_SET_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ _$ss5UInt8VMn
+ _$ss6HasherV5_seedABSi_tcfC
+ _$ss6HasherV9_finalizeSiyF
+ _$syXlN
+ _$sypWOb
+ _$sypWOc
+ _IRContextHomeKey
+ _IRHomeEventSubTypeToString
+ _IRHomeEventTypeToString
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_IRBundle
+ _OBJC_CLASS_$_IRHomeEvent
+ _OBJC_CLASS_$_IRServicePackageAdapterHome
+ _OBJC_CLASS_$_ULLabel
+ _OBJC_IVAR_$_IRBackgroundActivitiesManager._queue
+ _OBJC_IVAR_$_IRBackgroundActivitiesManager._scheduler
+ _OBJC_IVAR_$_IRMiloLslPredictionDO._isMapValid
+ _OBJC_IVAR_$_IRMiloLslPredictionDO._isMotionDetected
+ _OBJC_IVAR_$_IRMiloLslPredictionDO._isPredictionValid
+ _OBJC_IVAR_$_IRSessionServer._analyticsManager
+ _OBJC_IVAR_$_IRSessionServer._cleanupManager
+ _OBJC_IVAR_$_IRSessionServer._mobileAssetManager
+ _OBJC_METACLASS_$_IRServicePackageAdapterHome
+ _ULMapItemTypeClientGenerated
+ __DATA_IRServicePackageAdapterHome
+ __INSTANCE_METHODS_IRServicePackageAdapterHome
+ __IVARS_IRServicePackageAdapterHome
+ __METACLASS_DATA_IRServicePackageAdapterHome
+ __OBJC_$_CLASS_METHODS_IRNearbyDeviceContainerMO(Access|CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_IRServiceLogPrefix
+ __OBJC_$_INSTANCE_METHODS_IRNearbyDeviceContainerMO(Access|CoreDataProperties)
+ __PROPERTIES_IRServicePackageAdapterHome
+ __PROTOCOLS_IRServicePackageAdapterHome
+ __PROTOCOLS_IRServicePackageAdapterHome.2
+ ___140-[IRBackgroundActivitiesManager registerForRepeatingBackgroundXPCActivityWithIdentifier:interval:isDiskIntensive:isMemoryIntensive:handler:]_block_invoke.18
+ ___140-[IRBackgroundActivitiesManager registerForRepeatingBackgroundXPCActivityWithIdentifier:interval:isDiskIntensive:isMemoryIntensive:handler:]_block_invoke.cold.1
+ ___140-[IRBackgroundActivitiesManager registerForRepeatingBackgroundXPCActivityWithIdentifier:interval:isDiskIntensive:isMemoryIntensive:handler:]_block_invoke.cold.2
+ ___140-[IRBackgroundActivitiesManager registerForRepeatingBackgroundXPCActivityWithIdentifier:interval:isDiskIntensive:isMemoryIntensive:handler:]_block_invoke_2
+ ___167-[IRClassificationGenerator generateClassificationsWithCandiatesContainer:systemState:historyEventsContainer:miloPrediction:nearbyDeviceContainer:fillInspection:date:]_block_invoke.34
+ ___32-[IRBiomeBridge subscribeEvent:]_block_invoke.27
+ ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.20
+ ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.20.cold.1
+ ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.21
+ ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.21.cold.1
+ ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.23
+ ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.26
+ ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.27
+ ___41-[IRMiLoProvider connectionDidUpdateMap:]_block_invoke
+ ___45-[IRCleanupManager _handleCleanupXPCActivity]_block_invoke.42
+ ___48-[IRDisplayMonitor _didUpdateMainDisplayLayout:]_block_invoke.29
+ ___49-[IRProxcontrolBridge _createProxControlObserver]_block_invoke.35
+ ___49-[IRProxcontrolBridge _createProxControlObserver]_block_invoke.35.cold.1
+ ___49-[IRProxcontrolBridge _createProxControlObserver]_block_invoke.36
+ ___49-[IRProxcontrolBridge _createProxControlObserver]_block_invoke.36.cold.1
+ ___53-[IRAnalyticsManager _handleCoreAnalyticsXPCActivity]_block_invoke.51
+ ___55-[IRMiLoProvider connectionDidUpdatePredictionContext:]_block_invoke
+ ___55-[IRMiLoProvider connectionDidUpdatePredictionContext:]_block_invoke.52
+ ___55-[IRProximityProvider didBridgeSuspendStartedWithName:]_block_invoke.71
+ ___55-[IRProximityProvider didBridgeSuspendStartedWithName:]_block_invoke.72
+ ___56-[IRBiomeBridge fetchLatestEventsOfEventType:numEvents:]_block_invoke.32
+ ___79+[IRServiceStore idendifyAndDeleteDuplicateServicesWithWithPersistenceManager:]_block_invoke.59
+ ___80-[IRServicePackageAdapterMedia getSignificantBundlesWithCandidates:fromHistory:]_block_invoke.45
+ ___82-[IRSystemStateManager _checkAndStartPDRFenceLogicIfNeededWithEvent:andCandidate:]_block_invoke.35
+ ___block_descriptor_32_e24_v16?0"IRMiLoProvider"8l
+ ___block_descriptor_40_e8_32s_e19_16?0"ULMapItem"8ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e22_v16?0"BGSystemTask"8lw48l8s32l8s40l8
+ ___block_descriptor_66_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.110
+ ___block_literal_global.143
+ ___block_literal_global.146
+ ___block_literal_global.204
+ ___block_literal_global.22
+ ___block_literal_global.249
+ ___block_literal_global.25
+ ___block_literal_global.27
+ ___block_literal_global.30
+ ___block_literal_global.31
+ ___block_literal_global.55
+ ___block_literal_global.57
+ ___block_literal_global.59
+ ___block_literal_global.65
+ ___block_literal_global.66
+ ___block_literal_global.71
+ ___block_literal_global.96
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_IntelligentRoutingDaemon
+ __swift_stdlib_malloc_size
+ _bzero
+ _kIREventNameHome
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$_locationOfInterestToIRLocationSemantic:
+ _objc_msgSend$_miloServiceStatusLogStringFromMap:
+ _objc_msgSend$addLabel:
+ _objc_msgSend$addLabelWithName:
+ _objc_msgSend$addObserver:withToken:isLowLatency:
+ _objc_msgSend$currentMap
+ _objc_msgSend$eventDOWithHomeType:
+ _objc_msgSend$fetchAllServicesContainingClientIdentifier:persistenceManager:
+ _objc_msgSend$homeUserInteractionEvents
+ _objc_msgSend$initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithPredictionId:isPredictionValid:isMapValid:isMotionDetected:scores:predictionTime:
+ _objc_msgSend$isMapValid
+ _objc_msgSend$isMotionDetected
+ _objc_msgSend$isPredictionValid
+ _objc_msgSend$isSameSpaceForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:
+ _objc_msgSend$locationOfInterest
+ _objc_msgSend$locationOfInterestType
+ _objc_msgSend$locationOfInterestUUID
+ _objc_msgSend$mapItemType
+ _objc_msgSend$mapItems
+ _objc_msgSend$miloLslPredictionDOWithPredictionId:isPredictionValid:isMapValid:isMotionDetected:scores:predictionTime:
+ _objc_msgSend$miloLslSingleScoreDOWithScore:eventID:
+ _objc_msgSend$numberOfLabelsInSameSpaceForMapItem:
+ _objc_msgSend$predictionContext
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$resources
+ _objc_msgSend$scheduler
+ _objc_msgSend$scoreForPredictionEventEvent:
+ _objc_msgSend$setExpirationHandler:
+ _objc_msgSend$setInterval:
+ _objc_msgSend$setIsMapValid:
+ _objc_msgSend$setIsMotionDetected:
+ _objc_msgSend$setIsPredictionValid:
+ _objc_msgSend$setMinDurationBetweenInstances:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setRequiresUserInactivity:
+ _objc_msgSend$setResourceIntensive:
+ _objc_msgSend$setResources:
+ _objc_msgSend$setScheduler:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$submitTaskRequest:error:
+ _objc_msgSend$taskRequestForIdentifier:
+ _objc_msgSend$uniqueIdentifier
+ _objc_opt_self
+ _objc_retain_x9
+ _swift_allocObject
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_dynamicCast
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _symbolic SS_So9IRContextCt
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySSSo18IRPolicyInspectionCG s18_DictionaryStorageC
+ _symbolic _____ySSSo9IRContextCG s18_DictionaryStorageC
+ _symbolic _____ySS_So9IRContextCtG s23_ContiguousArrayStorageC
+ _symbolic _____ySo17IRCandidateResultCG s11_SetStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- +[IRMiLoNearbyDeviceDO miLoNearbyDeviceDOWithHasBleRssi:deviceIdentifier:]
- +[IRMiLoNearbyDeviceDO supportsSecureCoding]
- +[IRMiLoNearbyDeviceMO miLoNearbyDeviceMOWithMiLoNearbyDeviceDO:miloPrediction:inManagedObjectContext:]
- +[IRMiLoNearbyDeviceMO setPropertiesOfMiLoNearbyDeviceMO:withIRMiLoNearbyDeviceDO:]
- +[IRMiLoNearbyDeviceMO(CoreDataProperties) fetchRequest]
- +[IRMiLoProvider highConfidenceValue]
- +[IRMiLoProvider isConfidenceValid:]
- +[IRMiLoProvider isInMotion:]
- +[IRMiLoProvider isQualityValid:]
- +[IRMiloLslPredictionDO miloLslPredictionDOWithPredictionId:miLoServiceQuality:miLoServiceQualityReasonBitmap:scores:nearbyDevices:predictionTime:confidence:confidenceReasonBitmap:]
- +[IRServiceStore fetchAllServicesForClientIdentifier:persistenceManager:]
- -[IRBackgroundActivitiesManager analyticsManager]
- -[IRBackgroundActivitiesManager cleanupManager]
- -[IRBackgroundActivitiesManager mobileAssetManager]
- -[IRBackgroundActivitiesManager setAnalyticsManager:]
- -[IRBackgroundActivitiesManager setCleanupManager:]
- -[IRBackgroundActivitiesManager setMobileAssetManager:]
- -[IRBackgroundActivitiesManager setUserDefaultsRefreshToken:]
- -[IRBackgroundActivitiesManager userDefaultsRefreshToken]
- -[IRCandidateClassificationDetectorSameSpace _isSameSpaceForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:]
- -[IRMiLoNearbyDeviceDO .cxx_destruct]
- -[IRMiLoNearbyDeviceDO copyWithReplacementDeviceIdentifier:]
- -[IRMiLoNearbyDeviceDO copyWithReplacementHasBleRssi:]
- -[IRMiLoNearbyDeviceDO copyWithZone:]
- -[IRMiLoNearbyDeviceDO description]
- -[IRMiLoNearbyDeviceDO deviceIdentifier]
- -[IRMiLoNearbyDeviceDO encodeWithCoder:]
- -[IRMiLoNearbyDeviceDO hasBleRssi]
- -[IRMiLoNearbyDeviceDO hash]
- -[IRMiLoNearbyDeviceDO initWithCoder:]
- -[IRMiLoNearbyDeviceDO initWithHasBleRssi:deviceIdentifier:]
- -[IRMiLoNearbyDeviceDO init]
- -[IRMiLoNearbyDeviceDO isEqual:]
- -[IRMiLoNearbyDeviceDO isEqualToMiLoNearbyDeviceDO:]
- -[IRMiLoNearbyDeviceMO convert]
- -[IRMiLoProvider _bitmapFromServiceQualityReasonArray:]
- -[IRMiLoProvider _locationTypeToIRLocationSemantic:]
- -[IRMiLoProvider _miloServiceStatusLogStringFromStatus:]
- -[IRMiLoProvider addObserver:withToken:withLegacyServiceUUID:isLowLatency:]
- -[IRMiLoProvider addObserver:withToken:withLegacyServiceUUID:isLowLatency:].cold.1
- -[IRMiLoProvider connection:didUpdatePrediction:]
- -[IRMiLoProvider connection:didUpdateServiceStatus:]
- -[IRMiLoProvider labelPredictionUuid:withEventUuid:]
- -[IRMiLoProvider legacyServiceUUID]
- -[IRMiLoProvider miLoServiceQualityReasonBitmap]
- -[IRMiLoProvider miLoServiceQuality]
- -[IRMiLoProvider recoverServiceIfRequired]
- -[IRMiLoProvider setLegacyServiceUUID:]
- -[IRMiLoProvider setMiLoServiceQuality:]
- -[IRMiLoProvider setMiLoServiceQualityReasonBitmap:]
- -[IRMiLoProviderLslPredictionResults .cxx_destruct]
- -[IRMiLoProviderLslPredictionResults _bitmapFromConfidenceReasonArray:]
- -[IRMiLoProviderLslPredictionResults confidenceReasonBitmap]
- -[IRMiLoProviderLslPredictionResults confidence]
- -[IRMiLoProviderLslPredictionResults initWithMiloPrediction:withMiLoServiceQuality:withMiLoServiceQualityReasonBitmap:]
- -[IRMiLoProviderLslPredictionResults miLoServiceQualityReasonBitmap]
- -[IRMiLoProviderLslPredictionResults miLoServiceQuality]
- -[IRMiLoProviderLslPredictionResults predictedEvents]
- -[IRMiLoProviderLslPredictionResults predictionId]
- -[IRMiLoProviderLslPredictionResults predictionTime]
- -[IRMiLoProviderLslPredictionResults setConfidence:]
- -[IRMiLoProviderLslPredictionResults setConfidenceReasonBitmap:]
- -[IRMiLoProviderLslPredictionResults setMiLoServiceQuality:]
- -[IRMiLoProviderLslPredictionResults setMiLoServiceQualityReasonBitmap:]
- -[IRMiLoProviderLslPredictionResults setPredictedEvents:]
- -[IRMiLoProviderLslPredictionResults setPredictionId:]
- -[IRMiLoProviderLslPredictionResults setPredictionTime:]
- -[IRMiLoProviderLslSingleEventScore .cxx_destruct]
- -[IRMiLoProviderLslSingleEventScore eventId]
- -[IRMiLoProviderLslSingleEventScore score]
- -[IRMiLoProviderLslSingleEventScore setEventId:]
- -[IRMiLoProviderLslSingleEventScore setScore:]
- -[IRMiloLslPredictionDO confidenceReasonBitmap]
- -[IRMiloLslPredictionDO confidence]
- -[IRMiloLslPredictionDO copyWithReplacementConfidence:]
- -[IRMiloLslPredictionDO copyWithReplacementConfidenceReasonBitmap:]
- -[IRMiloLslPredictionDO copyWithReplacementMiLoServiceQuality:]
- -[IRMiloLslPredictionDO copyWithReplacementMiLoServiceQualityReasonBitmap:]
- -[IRMiloLslPredictionDO copyWithReplacementNearbyDevices:]
- -[IRMiloLslPredictionDO initWithPredictionId:miLoServiceQuality:miLoServiceQualityReasonBitmap:scores:nearbyDevices:predictionTime:confidence:confidenceReasonBitmap:]
- -[IRMiloLslPredictionDO miLoServiceQualityReasonBitmap]
- -[IRMiloLslPredictionDO miLoServiceQuality]
- -[IRMiloLslPredictionDO nearbyDevices]
- -[IRMiloLslPredictionDO(Extension) isInMotion]
- -[IRMiloLslPredictionDO(Extension) scoreForPredictionId:andLabel:]
- -[IRRuleOutputSystemState .cxx_destruct]
- -[IRRuleOutputSystemState evaluateRuleOutputWithCandidateIdentifier:]
- -[IRRuleOutputSystemState setValue:]
- -[IRRuleOutputSystemState value]
- -[IRRuleSystemState .cxx_destruct]
- -[IRRuleSystemState _attributeValueForAttributeKey:systemState:miloPrediction:]
- -[IRRuleSystemState _headsetRoutedOrAirPodsPredictedToBeRoutedForSystemState:]
- -[IRRuleSystemState executeRuleWithCandiatesContainer:systemStatus:historyContainer:miloPrediction:nearbyDeviceContainer:date:]
- -[IRRuleSystemState initWithAttributeKey:]
- -[IRServiceStore fetchMiLoServiceUuid]
- -[IRServiceStore updateMiloServiceWithMiloUuidString:]
- -[IRSystemStateManager _miloLslPredictionToDO:]
- -[IRSystemStateManager deleteLegacyServiceIdentifier]
- GCC_except_table23
- GCC_except_table25
- GCC_except_table27
- GCC_except_table30
- GCC_except_table39
- GCC_except_table41
- GCC_except_table44
- GCC_except_table53
- _OBJC_CLASS_$_IRMiLoNearbyDeviceDO
- _OBJC_CLASS_$_IRMiLoNearbyDeviceMO
- _OBJC_CLASS_$_IRMiLoProviderLslPredictionResults
- _OBJC_CLASS_$_IRMiLoProviderLslSingleEventScore
- _OBJC_CLASS_$_IRRuleOutputSystemState
- _OBJC_CLASS_$_IRRuleSystemState
- _OBJC_CLASS_$_NSUUID
- _OBJC_IVAR_$_IRBackgroundActivitiesManager._analyticsManager
- _OBJC_IVAR_$_IRBackgroundActivitiesManager._cleanupManager
- _OBJC_IVAR_$_IRBackgroundActivitiesManager._mobileAssetManager
- _OBJC_IVAR_$_IRBackgroundActivitiesManager._userDefaultsRefreshToken
- _OBJC_IVAR_$_IRMiLoNearbyDeviceDO._deviceIdentifier
- _OBJC_IVAR_$_IRMiLoNearbyDeviceDO._hasBleRssi
- _OBJC_IVAR_$_IRMiLoProvider._legacyServiceUUID
- _OBJC_IVAR_$_IRMiLoProvider._miLoServiceQuality
- _OBJC_IVAR_$_IRMiLoProvider._miLoServiceQualityReasonBitmap
- _OBJC_IVAR_$_IRMiLoProviderLslPredictionResults._confidence
- _OBJC_IVAR_$_IRMiLoProviderLslPredictionResults._confidenceReasonBitmap
- _OBJC_IVAR_$_IRMiLoProviderLslPredictionResults._miLoServiceQuality
- _OBJC_IVAR_$_IRMiLoProviderLslPredictionResults._miLoServiceQualityReasonBitmap
- _OBJC_IVAR_$_IRMiLoProviderLslPredictionResults._predictedEvents
- _OBJC_IVAR_$_IRMiLoProviderLslPredictionResults._predictionId
- _OBJC_IVAR_$_IRMiLoProviderLslPredictionResults._predictionTime
- _OBJC_IVAR_$_IRMiLoProviderLslSingleEventScore._eventId
- _OBJC_IVAR_$_IRMiLoProviderLslSingleEventScore._score
- _OBJC_IVAR_$_IRMiloLslPredictionDO._confidence
- _OBJC_IVAR_$_IRMiloLslPredictionDO._confidenceReasonBitmap
- _OBJC_IVAR_$_IRMiloLslPredictionDO._miLoServiceQuality
- _OBJC_IVAR_$_IRMiloLslPredictionDO._miLoServiceQualityReasonBitmap
- _OBJC_IVAR_$_IRMiloLslPredictionDO._nearbyDevices
- _OBJC_IVAR_$_IRRuleOutputSystemState._value
- _OBJC_IVAR_$_IRRuleSystemState._attributeKey
- _OBJC_METACLASS_$_IRMiLoNearbyDeviceDO
- _OBJC_METACLASS_$_IRMiLoNearbyDeviceMO
- _OBJC_METACLASS_$_IRMiLoProviderLslPredictionResults
- _OBJC_METACLASS_$_IRMiLoProviderLslSingleEventScore
- _OBJC_METACLASS_$_IRRuleOutputSystemState
- _OBJC_METACLASS_$_IRRuleSystemState
- _XPC_ACTIVITY_DISK_INTENSIVE
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL
- _XPC_ACTIVITY_MEMORY_INTENSIVE
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP
- __OBJC_$_CLASS_METHODS_IRMiLoNearbyDeviceDO
- __OBJC_$_CLASS_METHODS_IRMiLoNearbyDeviceMO(CoreDataProperties)
- __OBJC_$_CLASS_METHODS_IRNearbyDeviceContainerMO(CoreDataProperties|Access)
- __OBJC_$_CLASS_PROP_LIST_IRMiLoNearbyDeviceDO
- __OBJC_$_INSTANCE_METHODS_IRMiLoNearbyDeviceDO
- __OBJC_$_INSTANCE_METHODS_IRMiLoNearbyDeviceMO
- __OBJC_$_INSTANCE_METHODS_IRMiLoProviderLslPredictionResults
- __OBJC_$_INSTANCE_METHODS_IRMiLoProviderLslSingleEventScore
- __OBJC_$_INSTANCE_METHODS_IRNearbyDeviceContainerMO(CoreDataProperties|Access)
- __OBJC_$_INSTANCE_METHODS_IRRuleOutputSystemState
- __OBJC_$_INSTANCE_METHODS_IRRuleSystemState
- __OBJC_$_INSTANCE_VARIABLES_IRMiLoNearbyDeviceDO
- __OBJC_$_INSTANCE_VARIABLES_IRMiLoProviderLslPredictionResults
- __OBJC_$_INSTANCE_VARIABLES_IRMiLoProviderLslSingleEventScore
- __OBJC_$_INSTANCE_VARIABLES_IRRuleOutputSystemState
- __OBJC_$_INSTANCE_VARIABLES_IRRuleSystemState
- __OBJC_$_PROP_LIST_IRMiLoNearbyDeviceDO
- __OBJC_$_PROP_LIST_IRMiLoProviderLslPredictionResults
- __OBJC_$_PROP_LIST_IRMiLoProviderLslSingleEventScore
- __OBJC_$_PROP_LIST_IRRuleOutputSystemState
- __OBJC_CLASS_PROTOCOLS_$_IRMiLoNearbyDeviceDO
- __OBJC_CLASS_RO_$_IRMiLoNearbyDeviceDO
- __OBJC_CLASS_RO_$_IRMiLoNearbyDeviceMO
- __OBJC_CLASS_RO_$_IRMiLoProviderLslPredictionResults
- __OBJC_CLASS_RO_$_IRMiLoProviderLslSingleEventScore
- __OBJC_CLASS_RO_$_IRRuleOutputSystemState
- __OBJC_CLASS_RO_$_IRRuleSystemState
- __OBJC_METACLASS_RO_$_IRMiLoNearbyDeviceDO
- __OBJC_METACLASS_RO_$_IRMiLoNearbyDeviceMO
- __OBJC_METACLASS_RO_$_IRMiLoProviderLslPredictionResults
- __OBJC_METACLASS_RO_$_IRMiLoProviderLslSingleEventScore
- __OBJC_METACLASS_RO_$_IRRuleOutputSystemState
- __OBJC_METACLASS_RO_$_IRRuleSystemState
- ___107+[IRMiLoLSLPredictionMO setPropertiesOfMiLoLSLPredictionMO:withMiLoLSLPredictionDO:inManagedObjectContext:]_block_invoke_2
- ___119-[IRMiLoProviderLslPredictionResults initWithMiloPrediction:withMiLoServiceQuality:withMiLoServiceQualityReasonBitmap:]_block_invoke
- ___128+[IRCandidateClassificationDetectorSameSpace sameSpaceMiLoScoresForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:]_block_invoke_3
- ___167-[IRClassificationGenerator generateClassificationsWithCandiatesContainer:systemState:historyEventsContainer:miloPrediction:nearbyDeviceContainer:fillInspection:date:]_block_invoke.33
- ___32-[IRBiomeBridge subscribeEvent:]_block_invoke.9
- ___32-[IRMiLoLSLPredictionMO convert]_block_invoke_2
- ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.10
- ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.11
- ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.4
- ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.4.cold.1
- ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.5
- ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.5.cold.1
- ___39-[IRCompanionLinkClient startDiscovery]_block_invoke.7
- ___45-[IRCleanupManager _handleCleanupXPCActivity]_block_invoke.6
- ___47-[IRSystemStateManager _miloLslPredictionToDO:]_block_invoke
- ___48-[IRDisplayMonitor _didUpdateMainDisplayLayout:]_block_invoke.11
- ___49-[IRMiLoProvider connection:didUpdatePrediction:]_block_invoke
- ___49-[IRProxcontrolBridge _createProxControlObserver]_block_invoke.17
- ___49-[IRProxcontrolBridge _createProxControlObserver]_block_invoke.17.cold.1
- ___49-[IRProxcontrolBridge _createProxControlObserver]_block_invoke.18
- ___49-[IRProxcontrolBridge _createProxControlObserver]_block_invoke.18.cold.1
- ___52-[IRMiLoProvider connection:didUpdateServiceStatus:]_block_invoke
- ___53-[IRAnalyticsManager _handleCoreAnalyticsXPCActivity]_block_invoke.33
- ___54-[IRServiceStore updateMiloServiceWithMiloUuidString:]_block_invoke
- ___55-[IRProximityProvider didBridgeSuspendStartedWithName:]_block_invoke.53
- ___55-[IRProximityProvider didBridgeSuspendStartedWithName:]_block_invoke.54
- ___56-[IRBiomeBridge fetchLatestEventsOfEventType:numEvents:]_block_invoke.14
- ___79+[IRServiceStore idendifyAndDeleteDuplicateServicesWithWithPersistenceManager:]_block_invoke.38
- ___80-[IRServicePackageAdapterMedia getSignificantBundlesWithCandidates:fromHistory:]_block_invoke.27
- ___82-[IRSystemStateManager _checkAndStartPDRFenceLogicIfNeededWithEvent:andCandidate:]_block_invoke.19
- ___block_descriptor_32_e17_16?0"ULPlace"8l
- ___block_descriptor_32_e43_16?0"IRMiLoProviderLslSingleEventScore"8l
- ___block_descriptor_40_e8_32s_e32_B16?0"IRMiloLslSingleScoreDO"8ls32l8
- ___block_descriptor_40_e8_32s_e34_v24?0"IRMiLoNearbyDeviceMO"8^B16ls32l8
- ___block_descriptor_48_e8_32s40bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e12_v24?08^B16ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
- ___block_literal_global.11
- ___block_literal_global.12
- ___block_literal_global.125
- ___block_literal_global.128
- ___block_literal_global.13
- ___block_literal_global.15
- ___block_literal_global.17
- ___block_literal_global.186
- ___block_literal_global.23
- ___block_literal_global.231
- ___block_literal_global.29
- ___block_literal_global.37
- ___block_literal_global.39
- ___block_literal_global.4
- ___block_literal_global.48
- ___block_literal_global.9
- ___block_literal_global.90
- ___block_literal_global.97
- _kIRRuleSystemStateHeadsetRoutedOrAirPodsPredictedToBeRoutedKey
- _kIRRuleSystemStateHomeLOIKey
- _kIRRuleSystemStateMiLoAvailableKey
- _kIRRuleSystemStateOutsideOfAppInFocusWindow
- _objc_msgSend$_attributeValueForAttributeKey:systemState:miloPrediction:
- _objc_msgSend$_bitmapFromConfidenceReasonArray:
- _objc_msgSend$_bitmapFromServiceQualityReasonArray:
- _objc_msgSend$_headsetRoutedOrAirPodsPredictedToBeRoutedForSystemState:
- _objc_msgSend$_isSameSpaceForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:
- _objc_msgSend$_locationTypeToIRLocationSemantic:
- _objc_msgSend$_miloLslPredictionToDO:
- _objc_msgSend$_miloServiceStatusLogStringFromStatus:
- _objc_msgSend$addCandidateResult:
- _objc_msgSend$addObserver:withToken:withLegacyServiceUUID:isLowLatency:
- _objc_msgSend$confidence
- _objc_msgSend$confidenceReasonBitmap
- _objc_msgSend$confidenceReasonEnum
- _objc_msgSend$confidenceReasons
- _objc_msgSend$currentLocationOfInterestType
- _objc_msgSend$currentLocationOfInterestUuid
- _objc_msgSend$deleteLegacyServiceIdentifier
- _objc_msgSend$fetchAllServicesForClientIdentifier:persistenceManager:
- _objc_msgSend$fetchMiLoServiceUuid
- _objc_msgSend$hasBleRssi
- _objc_msgSend$highConfidenceValue
- _objc_msgSend$initWithHasBleRssi:deviceIdentifier:
- _objc_msgSend$initWithMiloPrediction:withMiLoServiceQuality:withMiLoServiceQualityReasonBitmap:
- _objc_msgSend$initWithPredictionId:miLoServiceQuality:miLoServiceQualityReasonBitmap:scores:nearbyDevices:predictionTime:confidence:confidenceReasonBitmap:
- _objc_msgSend$initWithUUIDString:
- _objc_msgSend$isConfidenceValid:
- _objc_msgSend$isInMotion
- _objc_msgSend$isInMotion:
- _objc_msgSend$isQualityValid:
- _objc_msgSend$labelPredictionUuid:withEventUuid:
- _objc_msgSend$labelRequestIdentifier:withPlaceIdentifier:
- _objc_msgSend$legacyServiceUUID
- _objc_msgSend$locationType
- _objc_msgSend$miLoNearbyDeviceMOWithMiLoNearbyDeviceDO:miloPrediction:inManagedObjectContext:
- _objc_msgSend$miLoServiceQuality
- _objc_msgSend$miLoServiceQualityReasonBitmap
- _objc_msgSend$miloLslPredictionDOWithPredictionId:miLoServiceQuality:miLoServiceQualityReasonBitmap:scores:nearbyDevices:predictionTime:confidence:confidenceReasonBitmap:
- _objc_msgSend$places
- _objc_msgSend$predictedEvents
- _objc_msgSend$qualityReasonEnum
- _objc_msgSend$recoverServiceIfRequired
- _objc_msgSend$requestIdentifier
- _objc_msgSend$scoreForPredictionId:andLabel:
- _objc_msgSend$serviceDescriptor
- _objc_msgSend$serviceQuality
- _objc_msgSend$serviceQualityInfo
- _objc_msgSend$serviceQualityReasons
- _objc_msgSend$setConfidence:
- _objc_msgSend$setConfidenceReasonBitmap:
- _objc_msgSend$setDeviceIdentifier:
- _objc_msgSend$setHasBleRssi:
- _objc_msgSend$setLegacyServiceUUID:
- _objc_msgSend$setMiLoServiceQuality:
- _objc_msgSend$setMiLoServiceQualityReasonBitmap:
- _objc_msgSend$setPredictedEvents:
- _objc_msgSend$setPropertiesOfMiLoNearbyDeviceMO:withIRMiLoNearbyDeviceDO:
- _objc_msgSend$setPropertiesOfMiLoServiceMO:withMiLoServiceUuidString:
- _objc_msgSend$setValue:
- _objc_msgSend$time
- _objc_msgSend$updateBundleIdentifier:
- _objc_msgSend$updateIsBannerClassificationUnavailable:
- _objc_msgSend$updateLegacyServiceIdentifier:
- _objc_msgSend$updateMiloServiceWithMiloUuidString:
- _objc_msgSend$value
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_dictionary_create
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
CStrings:
+ " predictionId: %@\n isLowLatency: %@\n isPredictionValid: %@\n predictionTime: %@ \n isMotionDetected: %@"
+ "#background-activity-manager, Task %@ already submitted, bailing out"
+ "#background-activity-manager, Task %@ expired"
+ "#background-activity-manager, Task %@ registered and submitted"
+ "#background-activity-manager, Task %@ started at %@"
+ "#background-activity-manager, [ErrorId - Task already registered] Task %@ already registered, something went wrong!"
+ "#background-activity-manager, [ErrorId - Task cannot submit] Task %@ could not be submitted with error %@"
+ "#service-package-adapter-home, "
+ "%K CONTAINS[cd] %@"
+ "%s"
+ "%s[%@], Adding MiLo observer with token: %@, isLowLatency: %@"
+ "%s[%@], MiLo prediction received, uniqueIdentifier: %@, isPredictionValid: %@, isMapValid: %@"
+ "%s[%@], Received MiLo prediction: %@"
+ "%s[%@], [ErrorId - Milo location type unsupported] Milo provided LOI type not handled %@"
+ "%s[%@], addLabelWithName: name: %@"
+ ", validCandidates: "
+ "-[IRMiLoProvider addObserver:withToken:isLowLatency:]"
+ "<IRMiloLslPredictionDO | predictionId:%@ isPredictionValid:%@ isMapValid:%@ isMotionDetected:%@ scores:%@ predictionTime:%@>"
+ "@\"BGSystemTaskScheduler\""
+ "@16@?0@\"ULMapItem\"8"
+ "@52@0:8@16B24B28B32@36@44"
+ "Generating classifications with candidates: "
+ "IRServicePackageAdapterHome"
+ "MiLo State:\n State: %@\n Suspend reasons: %@\n isMapValid: %@\n locationOfInterest: %@\n"
+ "Missing serialized value for IRMiloLslPredictionDO.isMapValid"
+ "Missing serialized value for IRMiloLslPredictionDO.isMotionDetected"
+ "Missing serialized value for IRMiloLslPredictionDO.isPredictionValid"
+ "PREFIX"
+ "RequestWithReply"
+ "T@\"BGSystemTaskScheduler\",&,N,V_scheduler"
+ "T@\"IRContext\",N,&,Vcontext"
+ "T@\"NSDictionary\",N,R"
+ "T@\"NSString\",N,R"
+ "TB,R,N,V_isMapValid"
+ "TB,R,N,V_isMotionDetected"
+ "TB,R,N,V_isPredictionValid"
+ "[self.name isEqual:kIREventNameAppleTVControl] || [self.name isEqual:kIREventNameMedia] || [self.name isEqual:kIREventNameHome]"
+ "_isMapValid"
+ "_isMotionDetected"
+ "_isPredictionValid"
+ "_locationOfInterestToIRLocationSemantic:"
+ "_miloServiceStatusLogStringFromMap:"
+ "_requestCurrentContextWithReply:"
+ "_scheduler"
+ "a"
+ "addLabel:"
+ "addLabelWithName:"
+ "addObserver:withToken:isLowLatency:"
+ "com.apple.intelligentrouting"
+ "com.apple.intelligentroutingd.IRBackgroundActivitiesManager"
+ "connectionDidUpdateMap:"
+ "connectionDidUpdatePredictionContext:"
+ "copyWithReplacementIsMapValid:"
+ "copyWithReplacementIsMotionDetected:"
+ "copyWithReplacementIsPredictionValid:"
+ "currentMap"
+ "eventDOWithHomeType:"
+ "fetchAllServicesContainingClientIdentifier:persistenceManager:"
+ "homeUserInteractionEvents"
+ "initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:"
+ "initWithIdentifier:"
+ "initWithPredictionId:isPredictionValid:isMapValid:isMotionDetected:scores:predictionTime:"
+ "isMapValid"
+ "isMotionDetected"
+ "isPredictionValid"
+ "isSameSpaceForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:"
+ "locationOfInterest"
+ "locationOfInterestType"
+ "locationOfInterestUUID"
+ "mapItemType"
+ "mapItems"
+ "miloLslPredictionDOWithPredictionId:isPredictionValid:isMapValid:isMotionDetected:scores:predictionTime:"
+ "numberOfLabelsInSameSpaceForMapItem:"
+ "predictionContext"
+ "queueSpecific"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "resources"
+ "scheduler"
+ "scoreForPredictionEventEvent:"
+ "setContext:"
+ "setExpirationHandler:"
+ "setInterval:"
+ "setIsMapValid:"
+ "setIsMotionDetected:"
+ "setIsPredictionValid:"
+ "setMinDurationBetweenInstances:"
+ "setPriority:"
+ "setRequiresUserInactivity:"
+ "setResourceIntensive:"
+ "setResources:"
+ "setScheduler:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "submitTaskRequest:error:"
+ "taskRequestForIdentifier:"
+ "uniqueIdentifier"
+ "v16@?0@\"BGSystemTask\"8"
+ "v24@0:8@\"IRMiloLslPredictionDO\"16"
+ "v24@0:8@?<v@?@\"IRContext\"@\"NSError\">16"
- " predictionId: %@\n isLowLatency: %@\n confidence: %@\n predictionTime: %@ \n confidenceReasons: %@"
- "#"
- "#background-activity-manager, XPC activity %@, called with state = %ld"
- "#background-activity-manager, XPC activity registered: %@"
- "%s[%@], Adding MiLo observer with token: %@, legacyServiceUUID: %@, isLowLatency: %@"
- "%s[%@], Labeling MiLo observation: predictionUuid: %@, eventUuid: %@"
- "%s[%@], MiLo prediction received, request ID is: %@, num events is: %@"
- "%s[%@], Received MiLo prediction: %@ with quality: %@ and reason: %@, confidence: %@, Confidence Reason: %@, Num Evets = %@"
- "%s[%@], [ErrorId - Milo Save error] Could not update milo service to nil in DB"
- "%s[%@], [ErrorId - Milo location type unsupported] Milo provided LOI type not handled [%lu]"
- "%s[%@], deleteLegacyServiceIdentifier"
- "-[IRMiLoProvider addObserver:withToken:withLegacyServiceUUID:isLowLatency:]"
- "<IRMiLoNearbyDeviceDO | hasBleRssi:%@ deviceIdentifier:%@>"
- "<IRMiloLslPredictionDO | predictionId:%@ miLoServiceQuality:%@ miLoServiceQualityReasonBitmap:%@ scores:%@ nearbyDevices:%@ predictionTime:%@ confidence:%@ confidenceReasonBitmap:%@>"
- "@16@?0@\"IRMiLoProviderLslSingleEventScore\"8"
- "@16@?0@\"ULPlace\"8"
- "@40@0:8@16q24q32"
- "@80@0:8@16q24q32@40@48@56q64q72"
- "B16@?0@\"IRMiloLslSingleScoreDO\"8"
- "B24@0:8Q16"
- "IRMiLoNearbyDeviceDO"
- "IRMiLoNearbyDeviceDOOCNTErrorDomain"
- "IRMiLoNearbyDeviceMO"
- "IRMiLoProviderLslPredictionResults"
- "IRMiLoProviderLslSingleEventScore"
- "IRRuleOutputSystemState"
- "IRRuleSystemState"
- "MiLo State:\n milo service id: %@\n State: %@\n Suspend reasons:%@\n Quality index:%@\n error:%@\n currentGroupId %@\n"
- "Missing serialized value for IRMiLoNearbyDeviceDO.hasBleRssi"
- "Missing serialized value for IRMiloLslPredictionDO.confidence"
- "Missing serialized value for IRMiloLslPredictionDO.confidenceReasonBitmap"
- "Missing serialized value for IRMiloLslPredictionDO.miLoServiceQuality"
- "Missing serialized value for IRMiloLslPredictionDO.miLoServiceQualityReasonBitmap"
- "T@\"IRRuleOutputEvaluation\",&,N,V_value"
- "T@\"NSArray\",&,N,V_predictedEvents"
- "T@\"NSDate\",&,N,V_predictionTime"
- "T@\"NSNumber\",&,N,V_score"
- "T@\"NSString\",R,N,V_deviceIdentifier"
- "T@\"NSUUID\",&,N,V_eventId"
- "T@\"NSUUID\",&,N,V_legacyServiceUUID"
- "T@\"NSUUID\",&,N,V_predictionId"
- "TB,R,N,V_hasBleRssi"
- "TQ,D,N"
- "Tq,N,V_confidence"
- "Tq,N,V_confidenceReasonBitmap"
- "Tq,N,V_miLoServiceQuality"
- "Tq,N,V_miLoServiceQualityReasonBitmap"
- "Tq,R,N,V_confidence"
- "Tq,R,N,V_confidenceReasonBitmap"
- "Tq,R,N,V_miLoServiceQuality"
- "Tq,R,N,V_miLoServiceQualityReasonBitmap"
- "Unarchived unexpected class for IRMiLoNearbyDeviceDO key \"deviceIdentifier\" (expected %@, decoded %@)"
- "[self.name isEqual:kIREventNameAppleTVControl] || [self.name isEqual:kIREventNameMedia]"
- "_attributeValueForAttributeKey:systemState:miloPrediction:"
- "_bitmapFromConfidenceReasonArray:"
- "_bitmapFromServiceQualityReasonArray:"
- "_confidence"
- "_confidenceReasonBitmap"
- "_deviceIdentifier"
- "_eventId"
- "_hasBleRssi"
- "_headsetRoutedOrAirPodsPredictedToBeRoutedForSystemState:"
- "_isSameSpaceForCandidate:basedOnMiLoPrediction:andHistoryEventsAsc:andDate:"
- "_legacyServiceUUID"
- "_locationTypeToIRLocationSemantic:"
- "_miLoServiceQuality"
- "_miLoServiceQualityReasonBitmap"
- "_miloLslPredictionToDO:"
- "_miloServiceStatusLogStringFromStatus:"
- "_predictedEvents"
- "_value"
- "addCandidateResult:"
- "addObserver:withToken:withLegacyServiceUUID:isLowLatency:"
- "confidence"
- "confidenceReasonBitmap"
- "confidenceReasonEnum"
- "confidenceReasons"
- "connection:didUpdatePrediction:"
- "connection:didUpdateServiceStatus:"
- "copyWithReplacementConfidence:"
- "copyWithReplacementConfidenceReasonBitmap:"
- "copyWithReplacementDeviceIdentifier:"
- "copyWithReplacementHasBleRssi:"
- "copyWithReplacementMiLoServiceQuality:"
- "copyWithReplacementMiLoServiceQualityReasonBitmap:"
- "currentLocationOfInterestType"
- "currentLocationOfInterestUuid"
- "d32@0:8@16@24"
- "deleteLegacyServiceIdentifier"
- "fetchAllServicesForClientIdentifier:persistenceManager:"
- "fetchMiLoServiceUuid"
- "hasBleRssi"
- "highConfidenceValue"
- "initWithAttributeKey:"
- "initWithHasBleRssi:deviceIdentifier:"
- "initWithMiloPrediction:withMiLoServiceQuality:withMiLoServiceQualityReasonBitmap:"
- "initWithPredictionId:miLoServiceQuality:miLoServiceQualityReasonBitmap:scores:nearbyDevices:predictionTime:confidence:confidenceReasonBitmap:"
- "initWithUUIDString:"
- "isConfidenceValid:"
- "isInMotion"
- "isInMotion:"
- "isQualityValid:"
- "kIRRuleSystemStateHeadsetRoutedOrAirPodsPredictedToBeRoutedKey"
- "kIRRuleSystemStateHomeLOIKey"
- "kIRRuleSystemStateMiLoAvailableKey"
- "kIRRuleSystemStateOutsideOfAppInFocusWindow"
- "labelPredictionUuid:withEventUuid:"
- "labelRequestIdentifier:withPlaceIdentifier:"
- "legacyServiceUUID"
- "locationType"
- "miLoNearbyDeviceDOWithHasBleRssi:deviceIdentifier:"
- "miLoNearbyDeviceMOWithMiLoNearbyDeviceDO:miloPrediction:inManagedObjectContext:"
- "miLoPredictionConfidence"
- "miLoPredictionConfidenceReasonsBitmap"
- "miLoServiceQuality"
- "miLoServiceQualityReasonBitmap"
- "miloLslPredictionDOWithPredictionId:miLoServiceQuality:miLoServiceQualityReasonBitmap:scores:nearbyDevices:predictionTime:confidence:confidenceReasonBitmap:"
- "places"
- "predictedEvents"
- "qualityReasonEnum"
- "recoverServiceIfRequired"
- "requestIdentifier"
- "scoreForPredictionId:andLabel:"
- "serviceDescriptor"
- "serviceQuality"
- "serviceQualityInfo"
- "serviceQualityReasons"
- "setConfidence:"
- "setConfidenceReasonBitmap:"
- "setDeviceIdentifier:"
- "setHasBleRssi:"
- "setLegacyServiceUUID:"
- "setMiLoServiceQuality:"
- "setMiLoServiceQualityReasonBitmap:"
- "setPredictedEvents:"
- "setPropertiesOfMiLoNearbyDeviceMO:withIRMiLoNearbyDeviceDO:"
- "setValue:"
- "time"
- "updateBundleIdentifier:"
- "updateIsBannerClassificationUnavailable:"
- "updateLegacyServiceIdentifier:"
- "updateMiloServiceWithMiloUuidString:"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "v24@0:8@\"IRMiLoProviderLslPredictionResults\"16"
- "v24@?0@\"IRMiLoNearbyDeviceMO\"8^B16"
- "v24@?0@8^B16"
- "v32@0:8@\"NSUUID\"16@\"NSUUID\"24"
- "v44@0:8@16@24@32B40"
- "value"
- "\x91"

```
