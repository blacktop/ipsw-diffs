## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1397.0.0.0.0
-  __TEXT.__text: 0x225fe8
-  __TEXT.__auth_stubs: 0x31e0
-  __TEXT.__init_offsets: 0x14c
-  __TEXT.__objc_methlist: 0x46c
-  __TEXT.__const: 0xf458
-  __TEXT.__gcc_except_tab: 0x34850
-  __TEXT.__cstring: 0x7e80
-  __TEXT.__oslogstring: 0xbb07
-  __TEXT.__unwind_info: 0xa190
-  __TEXT.__objc_classname: 0x10d
-  __TEXT.__objc_methname: 0x13df
-  __TEXT.__objc_methtype: 0x10f0
-  __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0x21e0
-  __DATA_CONST.__const: 0x2098
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x28
+1399.2.0.0.0
+  __TEXT.__text: 0x22da8c
+  __TEXT.__auth_stubs: 0x3370
+  __TEXT.__init_offsets: 0x160
+  __TEXT.__objc_methlist: 0x52c
+  __TEXT.__const: 0xf638
+  __TEXT.__dlopen_cstrs: 0xac
+  __TEXT.__gcc_except_tab: 0x3566c
+  __TEXT.__cstring: 0x81b0
+  __TEXT.__oslogstring: 0xbfc9
+  __TEXT.__unwind_info: 0xa3d8
+  __TEXT.__objc_classname: 0x13c
+  __TEXT.__objc_methname: 0x1605
+  __TEXT.__objc_methtype: 0x12b1
+  __TEXT.__objc_stubs: 0x12c0
+  __DATA_CONST.__got: 0x2298
+  __DATA_CONST.__const: 0x2168
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b0
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1900
-  __AUTH_CONST.__const: 0xea58
-  __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0x918
+  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x19c8
+  __AUTH_CONST.__const: 0xebf8
+  __AUTH_CONST.__cfstring: 0x980
+  __AUTH_CONST.__objc_const: 0xa68
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x4d8
-  __DATA.__bss: 0x4c8
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x4c
+  __DATA.__data: 0x580
+  __DATA.__bss: 0x4d0
   __DATA.__common: 0xa
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x5d8
-  __DATA_DIRTY.__common: 0xd0
-  __DATA_DIRTY.__bss: 0x25a
+  __DATA_DIRTY.__data: 0x630
+  __DATA_DIRTY.__common: 0xd8
+  __DATA_DIRTY.__bss: 0x2ca
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libATCommandStudioDynamic.dylib
   - /usr/lib/libBBUpdaterDynamic.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: F6B93111-0767-38AA-AF3C-2CBDC5E057C7
-  Functions: 6079
-  Symbols:   18545
-  CStrings:  2799
+  UUID: 882911BF-C4FE-3C28-AD85-97D894C63EF9
+  Functions: 6147
+  Symbols:   18846
+  CStrings:  2901
 
Symbols:
+ -[AirplaneModeObserver .cxx_construct]
+ -[AirplaneModeObserver .cxx_destruct]
+ -[AirplaneModeObserver airplaneModeChanged]
+ -[AirplaneModeObserver dealloc]
+ -[AirplaneModeObserver initWithNotification:]
+ -[AirplaneModeObserver notification]
+ -[AirplaneModeObserver queue]
+ -[AirplaneModeObserver radioPrefs]
+ -[AirplaneModeObserver setNotification:]
+ -[AirplaneModeObserver setQueue:]
+ -[AirplaneModeObserver setRadioPrefs:]
+ -[AirplaneModeObserver startMonitoring]
+ -[AirplaneModeObserver stopMonitoring]
+ GCC_except_table206
+ GCC_except_table221
+ GCC_except_table236
+ GCC_except_table263
+ GCC_except_table280
+ GCC_except_table298
+ GCC_except_table299
+ GCC_except_table347
+ GCC_except_table349
+ GCC_except_table358
+ GCC_except_table363
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table400
+ GCC_except_table409
+ GCC_except_table410
+ GCC_except_table413
+ GCC_except_table417
+ GCC_except_table427
+ GCC_except_table428
+ GCC_except_table446
+ GCC_except_table458
+ GCC_except_table461
+ GCC_except_table465
+ GCC_except_table478
+ _CFUserNotificationCancel
+ _CFUserNotificationCreate
+ _CFUserNotificationDisplayNotice
+ _CFUserNotificationReceiveResponse
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperties
+ _IOServiceGetMatchingService
+ _IOServiceMatching
+ _OBJC_CLASS_$_AirplaneModeObserver
+ _OBJC_CLASS_$_SBSUserNotificationSystemApertureContentDefinition
+ _OBJC_IVAR_$_AirplaneModeObserver._notification
+ _OBJC_IVAR_$_AirplaneModeObserver._queue
+ _OBJC_IVAR_$_AirplaneModeObserver._radioPrefs
+ _OBJC_METACLASS_$_AirplaneModeObserver
+ _SBSIsSystemApertureAvailable
+ _SBUserNotificationDismissOnLock
+ _SBUserNotificationDontDismissOnUnlock
+ _SBUserNotificationSystemApertureContentDefinitionKey
+ _SBUserNotificationSystemAperturePresentationKey
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyUtilTriggerNMI
+ _TelephonyUtilWriteStackshot
+ __OBJC_$_INSTANCE_METHODS_AirplaneModeObserver
+ __OBJC_$_INSTANCE_VARIABLES_AirplaneModeObserver
+ __OBJC_$_PROP_LIST_AirplaneModeObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RadiosPreferencesDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RadiosPreferencesDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AirplaneModeObserver
+ __OBJC_CLASS_RO_$_AirplaneModeObserver
+ __OBJC_LABEL_PROTOCOL_$_RadiosPreferencesDelegate
+ __OBJC_METACLASS_RO_$_AirplaneModeObserver
+ __OBJC_PROTOCOL_$_RadiosPreferencesDelegate
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZL22audit_stringAppSupport
+ __ZL25getRadiosPreferencesClassv
+ __ZL26audit_stringSetupAssistant
+ __ZN10BootModule19copyPMUService_syncEPj
+ __ZN10BootModule22releasePMUService_syncEPj
+ __ZN10BootModule39isUser3FingerResetSequenceDetected_syncEv
+ __ZN10DataModule20setDataProperty_syncEN3xpc4dictEN8dispatch5blockIU13block_pointerFviS1_EEE
+ __ZN12capabilities3abs17shouldBlockResetsEv
+ __ZN12capabilities3abs24kKeyDataPowerSaveEnabledE
+ __ZN12capabilities3abs24shouldDetect3FingerResetEv
+ __ZN12capabilities3abs26kKeyDataFlowControlEnabledE
+ __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
+ __ZN12capabilities3abs27kKeyDataAggregationProtocolE
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN12capabilities3abs31kKeyDataAggregationMaxSizeBytesE
+ __ZN12capabilities3abs35kKeyDataAggregationDatagramMaxCountE
+ __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
+ __ZN3ctu23PthreadMutexGuardPolicyI21CapabilitiesOverridesED1Ev
+ __ZN3ctu23PthreadMutexGuardPolicyI21CapabilitiesOverridesED2Ev
+ __ZN3ctu2cf11CFSharedRefI20__CFUserNotificationED1Ev
+ __ZN3ctu2cf6insertIPK10__CFStringS4_EEbP14__CFDictionaryT_T0_PK13__CFAllocator
+ __ZN3ctu5power7manager20simulateNotificationEjb
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN7support2ui28displayAlertWithUserResponseERKNS0_12AlertContentEPK10__CFStringP16dispatch_queue_sNSt3__18functionIFvNS0_19AlertButtonResponseEEEE
+ __ZN7support2ui34displayAlertWithUserResponseLegacyEPK10__CFStringS3_
+ __ZN7support2uiL17gNotificationLockE
+ __ZN7support2uiL9isAllowedEv
+ __ZN9Overrides13getPreferenceIbEEbRKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERT_
+ __ZN9Overrides13setPreferenceIbEEbRKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_b
+ __ZNKSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_E11target_typeEv
+ __ZNKSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_E6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_E7__cloneEPNS0_6__baseIS5_EE
+ __ZNKSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_E7__cloneEv
+ __ZNKSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info
+ __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_E18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_E7destroyEv
+ __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_ED0Ev
+ __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_ED1Ev
+ __ZNSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_EclEOS4_
+ __ZNSt3__110shared_ptrI21CapabilitiesOverridesED1B8ne200100Ev
+ __ZNSt3__110shared_ptrI21CapabilitiesOverridesED2B8ne200100Ev
+ __ZNSt3__110shared_ptrIN3ctu5power7managerEED2B8ne200100Ev
+ __ZNSt3__110unique_ptrI21CapabilitiesOverridesNS_14default_deleteIS1_EEED2B8ne200100Ev
+ __ZNSt3__110unique_ptrIZN7support2ui28displayAlertWithUserResponseERKNS2_12AlertContentEPK10__CFStringP16dispatch_queue_sNS_8functionIFvNS2_19AlertButtonResponseEEEEE3$_0NS_14default_deleteISF_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZN7support2ui28displayAlertWithUserResponseERKNS2_12AlertContentEPK10__CFStringP16dispatch_queue_sNS_8functionIFvNS2_19AlertButtonResponseEEEEE3$_1NS_14default_deleteISF_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZNK3ctu20SharedSynchronizableI9SimulatorE15execute_wrappedIZZNS3_26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEEUlvE_EEvOT_EUlvE_NS_14default_deleteISE_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZZN7support2ui28displayAlertWithUserResponseERKNS2_12AlertContentEPK10__CFStringP16dispatch_queue_sNS_8functionIFvNS2_19AlertButtonResponseEEEEENK3$_1clEvEUlvE_NS_14default_deleteISG_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZZN9Simulator26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEEUlvE_NS_14default_deleteIS7_EEED1B8ne200100Ev
+ __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED1Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__18functionIFvN7support2ui19AlertButtonResponseEEED2Ev
+ __ZTINSt3__110__function6__baseIFvN7support2ui19AlertButtonResponseEEEE
+ __ZTINSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_EE
+ __ZTINSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
+ __ZTIU13block_pointerFvN7support2ui19AlertButtonResponseEE
+ __ZTSNSt3__110__function6__baseIFvN7support2ui19AlertButtonResponseEEEE
+ __ZTSNSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_EE
+ __ZTSNSt3__110shared_ptrI21CapabilitiesOverridesE27__shared_ptr_default_deleteIS1_S1_EE
+ __ZTSNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
+ __ZTSU13block_pointerFvN7support2ui19AlertButtonResponseEE
+ __ZTVNSt3__110__function6__funcIU8__strongU13block_pointerFvN7support2ui19AlertButtonResponseEENS_9allocatorIS7_EES5_EE
+ __ZTVNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
+ __ZZ37show3FingerResetAlertWithUserResponseE9onceToken
+ __ZZN8dispatch5asyncIZN7support2ui28displayAlertWithUserResponseERKNS2_12AlertContentEPK10__CFStringP16dispatch_queue_sNSt3__18functionIFvNS2_19AlertButtonResponseEEEEE3$_0EEvSA_NSB_10unique_ptrIT_NSB_14default_deleteISI_EEEEENUlPvE_8__invokeESM_
+ __ZZN8dispatch5asyncIZN7support2ui28displayAlertWithUserResponseERKNS2_12AlertContentEPK10__CFStringP16dispatch_queue_sNSt3__18functionIFvNS2_19AlertButtonResponseEEEEE3$_1EEvSA_NSB_10unique_ptrIT_NSB_14default_deleteISI_EEEEENUlPvE_8__invokeESM_
+ __ZZN8dispatch5asyncIZZN7support2ui28displayAlertWithUserResponseERKNS2_12AlertContentEPK10__CFStringP16dispatch_queue_sNSt3__18functionIFvNS2_19AlertButtonResponseEEEEENK3$_1clEvEUlvE_EEvSA_NSB_10unique_ptrIT_NSB_14default_deleteISJ_EEEEENUlPvE_8__invokeESN_
+ __ZZN9ABMServer10getProfileEvE11sABMProfile
+ __ZZN9ABMServer10getProfileEvE9onceToken
+ ____ZL21AppSupportLibraryCorePPc_block_invoke
+ ____ZL25SetupAssistantLibraryCorePPc_block_invoke
+ ____ZL25getRadiosPreferencesClassv_block_invoke
+ ____ZL38getBYSetupAssistantNeedsToRunSymbolLocv_block_invoke
+ ____ZN10BootModule13shutdown_syncEN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEE_block_invoke.139
+ ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.117
+ ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.118
+ ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.122
+ ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.128
+ ____ZN10BootModule17shutdownWithStageE13ShutdownStageN8dispatch13group_sessionE_block_invoke.34
+ ____ZN10BootModule17shutdownWithStageE13ShutdownStageN8dispatch13group_sessionE_block_invoke.35
+ ____ZN10BootModule17shutdownWithStageE13ShutdownStageN8dispatch13group_sessionE_block_invoke.45
+ ____ZN10BootModule17shutdownWithStageE13ShutdownStageN8dispatch13group_sessionE_block_invoke.48
+ ____ZN10BootModule21handleBootFailed_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke.101
+ ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.67
+ ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.71
+ ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.75
+ ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.79
+ ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke_2.61
+ ____ZN10BootModule28updateNetworkCampStatus_syncEb_block_invoke.195
+ ____ZN10BootModule9boot_syncEv_block_invoke.149
+ ____ZN10BootModule9boot_syncEv_block_invoke.151
+ ____ZN10BootModule9boot_syncEv_block_invoke.168
+ ____ZN10DataModule28registerCommandHandlers_syncEv_block_invoke.12
+ ____ZN10DataModule28registerCommandHandlers_syncEv_block_invoke_2.13
+ ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke.17
+ ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke.21
+ ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke.24
+ ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke_2.25
+ ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke_3
+ ____ZN9ABMServer10getProfileEv_block_invoke
+ ____ZZN8FSModule18requestFSSync_syncEvENK3$_0clEv_block_invoke.128
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.147
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.153
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.157
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.161
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.165
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.169
+ ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke.160
+ ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke.166
+ ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke_2.161
+ ___block_descriptor_100_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c30_ZTSN8dispatch13group_sessionE64c38_ZTSNSt3__18functionIFvbN3xpc4dictEEEE_e151_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40l
+ ___block_descriptor_296_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c67_ZTSZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEE3$_5_e151_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40l
+ ___block_descriptor_40_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_ea8_32r_e8_v12?0i8lr32l8
+ ___block_descriptor_56_e8_32c35_ZTSNSt3__18weak_ptrI10LogTrackerEE48c31_ZTSKN8dispatch13group_sessionE_e151_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40l
+ ___block_descriptor_56_e8_40c35_ZTSNSt3__18weak_ptrI10CPMSModuleEE_e678_v32?0{BudgetData={map<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>, std::less<abm::BasebandCPMSPowerBudgetScale>, std::allocator<std::pair<const abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>={__tree<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::__map_value_compare<abm::BasebandCPMSPowerBudgetScale, std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::less<abm::BasebandCPMSPowerBudgetScale>>, std::allocator<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}}8l
+ ___block_descriptor_56_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE_e151_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40l
+ ___block_descriptor_57_e8_40c35_ZTSNSt3__18weak_ptrI10CPMSModuleEE_e144_v32?0{vector<abm::ThermalSensorData, std::allocator<abm::ThermalSensorData>>=^{ThermalSensorData}^{ThermalSensorData}{?=^{ThermalSensorData}}}8l
+ ___block_descriptor_64_e8_40c30_ZTSN8dispatch13group_sessionE48c46_ZTSNSt3__110shared_ptrIN3abm12HelperClientEEE_e151_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40l
+ ___block_descriptor_64_e8_40c35_ZTSNSt3__18weak_ptrI10CPMSModuleEE56c54_ZTSN8dispatch5blockIU13block_pointerFviN3xpc4dictEEEE_e154_v32?0{vector<abm::PowerMitigationData, std::allocator<abm::PowerMitigationData>>=^{PowerMitigationData}^{PowerMitigationData}{?=^{PowerMitigationData}}}8l
+ ___block_descriptor_64_e8_40c35_ZTSNSt3__18weak_ptrI10CPMSModuleEE56c54_ZTSN8dispatch5blockIU13block_pointerFviN3xpc4dictEEEE_e90_v32?0{vector<abm::BasebandThermalID, std::allocator<abm::BasebandThermalID>>=^C^C{?=^C}}8l
+ ___block_descriptor_64_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c31_ZTSKN8dispatch13group_sessionE_e151_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40l
+ ___block_descriptor_72_e8_32c46_ZTSNSt3__110shared_ptrIN3abm12HelperClientEEE48c15_ZTSN3xpc4dictE56c79_ZTSN8dispatch8callbackIU13block_pointerFvN12TelephonyXPC6ResultEN3xpc4dictEEEE_e151_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40l
+ ___block_descriptor_72_e8_40c30_ZTSN8dispatch13group_sessionE48c35_ZTSNSt3__18weak_ptrI10CPMSModuleEE64c54_ZTSN8dispatch5blockIU13block_pointerFviN3xpc4dictEEEE_e678_v32?0{BudgetData={map<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>, std::less<abm::BasebandCPMSPowerBudgetScale>, std::allocator<std::pair<const abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>={__tree<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::__map_value_compare<abm::BasebandCPMSPowerBudgetScale, std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::less<abm::BasebandCPMSPowerBudgetScale>>, std::allocator<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}}8l
+ ___block_descriptor_80_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c66_ZTSNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_e151_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40l
+ ___block_descriptor_96_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c31_ZTSKN8dispatch13group_sessionE64c27_ZTSNSt3__18functionIFvbEEE_e151_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40l
+ ___block_descriptor_tmp.105
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.115
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.130
+ ___block_descriptor_tmp.131
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.142
+ ___block_descriptor_tmp.153
+ ___block_descriptor_tmp.159
+ ___block_descriptor_tmp.160
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.169
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.173
+ ___block_descriptor_tmp.198
+ ___block_descriptor_tmp.201
+ ___block_descriptor_tmp.255
+ ___block_descriptor_tmp.265
+ ___block_descriptor_tmp.269
+ ___block_descriptor_tmp.280
+ ___block_descriptor_tmp.283
+ ___block_descriptor_tmp.41
+ ___block_descriptor_tmp.91
+ ___block_literal_global.262
+ ___block_literal_global.40
+ ___block_literal_global.62
+ ___block_literal_global.88
+ ___cxx_global_var_init.205
+ ___cxx_global_var_init.206
+ ___cxx_global_var_init.207
+ ___cxx_global_var_init.208
+ ___cxx_global_var_init.209
+ ___cxx_global_var_init.42
+ ___cxx_global_var_init.43
+ ___cxx_global_var_init.44
+ ___cxx_global_var_init.45
+ ___cxx_global_var_init.69
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ ___show3FingerResetAlertWithUserResponse_block_invoke
+ ___show3FingerResetAlertWithUserResponse_block_invoke.54
+ __dispatch_main_q
+ __sl_dlopen
+ _abort_report_np
+ _deviceIsInSetupAssistant
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dlerror
+ _dlsym
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlertTopMostKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _kIOMainPortDefault
+ _objc_getClass
+ _objc_msgSend$airplaneMode
+ _objc_msgSend$build
+ _objc_msgSend$delegate
+ _objc_msgSend$dictionary
+ _objc_msgSend$initWithNotification:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$setAirplaneModeWithoutMirroring:
+ _objc_msgSend$setAlertHeader:
+ _objc_msgSend$setAlertMessage:
+ _objc_msgSend$setAlternateButtonTitle:
+ _objc_msgSend$setDefaultButtonTitle:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setPreventsAutomaticDismissal:
+ _objc_msgSend$startMonitoring
+ _objc_msgSend$stopMonitoring
+ _objc_retain_x9
+ _setAirplaneMode
+ _show3FingerResetAlertWithUserResponse
- GCC_except_table256
- GCC_except_table269
- GCC_except_table271
- GCC_except_table286
- GCC_except_table321
- GCC_except_table335
- GCC_except_table336
- GCC_except_table351
- GCC_except_table359
- GCC_except_table360
- GCC_except_table393
- GCC_except_table394
- GCC_except_table403
- GCC_except_table404
- GCC_except_table412
- GCC_except_table421
- GCC_except_table423
- GCC_except_table452
- GCC_except_table455
- GCC_except_table472
- GCC_except_table476
- __ZN7support2ui28displayAlertWithUserResponseEPK10__CFStringS3_
- ____ZN10BootModule13shutdown_syncEN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEE_block_invoke.126
- ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.104
- ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.105
- ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.109
- ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.115
- ____ZN10BootModule17shutdownWithStageE13ShutdownStageN8dispatch13group_sessionE_block_invoke.25
- ____ZN10BootModule17shutdownWithStageE13ShutdownStageN8dispatch13group_sessionE_block_invoke.26
- ____ZN10BootModule17shutdownWithStageE13ShutdownStageN8dispatch13group_sessionE_block_invoke.36
- ____ZN10BootModule17shutdownWithStageE13ShutdownStageN8dispatch13group_sessionE_block_invoke.39
- ____ZN10BootModule21handleBootFailed_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke.90
- ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.49
- ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.51
- ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.64
- ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.68
- ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke_2.52
- ____ZN10BootModule28updateNetworkCampStatus_syncEb_block_invoke.182
- ____ZN10BootModule9boot_syncEv_block_invoke.136
- ____ZN10BootModule9boot_syncEv_block_invoke.138
- ____ZN10BootModule9boot_syncEv_block_invoke.142
- ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke.14
- ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke.16
- ____ZZN8FSModule18requestFSSync_syncEvENK3$_0clEv_block_invoke.127
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.145
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.149
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.155
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.159
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.163
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.167
- ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke.153
- ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke.159
- ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke_2.154
- ___block_descriptor_100_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c30_ZTSN8dispatch13group_sessionE64c38_ZTSNSt3__18functionIFvbN3xpc4dictEEEE_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
- ___block_descriptor_296_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c67_ZTSZN10LogTracker30postLogCollectionInternal_syncEN3xpc4dictEE3$_5_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
- ___block_descriptor_56_e8_32c35_ZTSNSt3__18weak_ptrI10LogTrackerEE48c31_ZTSKN8dispatch13group_sessionE_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
- ___block_descriptor_56_e8_40c35_ZTSNSt3__18weak_ptrI10CPMSModuleEE_e670_v32?0{BudgetData={map<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>, std::less<abm::BasebandCPMSPowerBudgetScale>, std::allocator<std::pair<const abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>={__tree<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::__map_value_compare<abm::BasebandCPMSPowerBudgetScale, std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::less<abm::BasebandCPMSPowerBudgetScale>>, std::allocator<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}}8l
- ___block_descriptor_56_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
- ___block_descriptor_57_e8_40c35_ZTSNSt3__18weak_ptrI10CPMSModuleEE_e140_v32?0{vector<abm::ThermalSensorData, std::allocator<abm::ThermalSensorData>>=^{ThermalSensorData}^{ThermalSensorData}^{ThermalSensorData}}8l
- ___block_descriptor_64_e8_40c30_ZTSN8dispatch13group_sessionE48c46_ZTSNSt3__110shared_ptrIN3abm12HelperClientEEE_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
- ___block_descriptor_64_e8_40c35_ZTSNSt3__18weak_ptrI10CPMSModuleEE56c54_ZTSN8dispatch5blockIU13block_pointerFviN3xpc4dictEEEE_e150_v32?0{vector<abm::PowerMitigationData, std::allocator<abm::PowerMitigationData>>=^{PowerMitigationData}^{PowerMitigationData}^{PowerMitigationData}}8l
- ___block_descriptor_64_e8_40c35_ZTSNSt3__18weak_ptrI10CPMSModuleEE56c54_ZTSN8dispatch5blockIU13block_pointerFviN3xpc4dictEEEE_e86_v32?0{vector<abm::BasebandThermalID, std::allocator<abm::BasebandThermalID>>=^C^C^C}8l
- ___block_descriptor_64_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c31_ZTSKN8dispatch13group_sessionE_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
- ___block_descriptor_72_e8_32c46_ZTSNSt3__110shared_ptrIN3abm12HelperClientEEE48c15_ZTSN3xpc4dictE56c79_ZTSN8dispatch8callbackIU13block_pointerFvN12TelephonyXPC6ResultEN3xpc4dictEEEE_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
- ___block_descriptor_72_e8_40c30_ZTSN8dispatch13group_sessionE48c35_ZTSNSt3__18weak_ptrI10CPMSModuleEE64c54_ZTSN8dispatch5blockIU13block_pointerFviN3xpc4dictEEEE_e670_v32?0{BudgetData={map<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>, std::less<abm::BasebandCPMSPowerBudgetScale>, std::allocator<std::pair<const abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>={__tree<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::__map_value_compare<abm::BasebandCPMSPowerBudgetScale, std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::less<abm::BasebandCPMSPowerBudgetScale>>, std::allocator<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}}8l
- ___block_descriptor_80_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c66_ZTSNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
- ___block_descriptor_96_e8_40c35_ZTSNSt3__18weak_ptrI10LogTrackerEE56c31_ZTSKN8dispatch13group_sessionE64c27_ZTSNSt3__18functionIFvbEEE_e147_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40l
- ___block_descriptor_tmp.102
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.121
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.134
- ___block_descriptor_tmp.137
- ___block_descriptor_tmp.143
- ___block_descriptor_tmp.151
- ___block_descriptor_tmp.157
- ___block_descriptor_tmp.163
- ___block_descriptor_tmp.171
- ___block_descriptor_tmp.175
- ___block_descriptor_tmp.178
- ___block_descriptor_tmp.234
- ___block_descriptor_tmp.238
- ___block_descriptor_tmp.243
- ___block_descriptor_tmp.252
- ___block_descriptor_tmp.94
- ___block_literal_global.245
- ___block_literal_global.77
- ___copy_helper_block_e8_32c35_ZTSNSt3__18weak_ptrI10BootModuleEE
- ___cxx_global_var_init.189
- ___cxx_global_var_init.190
- ___cxx_global_var_init.191
- ___cxx_global_var_init.192
- ___cxx_global_var_init.193
- ___cxx_global_var_init.194
- ___cxx_global_var_init.34
- ___cxx_global_var_init.35
- ___cxx_global_var_init.38
- ___cxx_global_var_init.39
- ___cxx_global_var_init.66
- ___destroy_helper_block_e8_32c35_ZTSNSt3__18weak_ptrI10BootModuleEE
CStrings:
+ "#D     %s"
+ "#D Enumerating HealthEvents to be written to disk:"
+ "#D HealthEvents dictionary representation to be written to disk: %@"
+ "#I Simulated notification: %s"
+ "#I Triggering stackshot"
+ "#I Triggering stackshot  -- done"
+ "#I blocking reset until user signals"
+ "#N Boot Fault Info value: %{public}s"
+ "#N Device boot detected, 3FR check - shouldDetect:%{bool}d isGreenTea:%{bool}d"
+ "#N Performing 3FR check"
+ "#N Putting the device in Airplane mode due to 3FR detection"
+ "#N User Three Finger Reset Detected"
+ ", reason "
+ "-l 0xffffffff -v 99 -N"
+ "3FingerReset_Airplane_Mode_On"
+ "3FingerReset_Airplane_Mode_On_Details"
+ "3FingerReset_Button_Airplane_Mode_Off"
+ "@\"RadiosPreferences\""
+ "@24@0:8{CFSharedRef<__CFUserNotification>=^{__CFUserNotification}}16"
+ "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16"
+ "Airplane mode set to %{bool}d"
+ "AirplaneModeObserver"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1399.2"
+ "AppleBasebandServices_Manager-1399.2"
+ "B136@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}16@88{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}96"
+ "BYSetupAssistantNeedsToRun"
+ "Baseband Firmware Not Found"
+ "Baseband Hard-Reset: "
+ "Capability %s returning overridden value"
+ "Did you forget to check update baseband or set permissions if you used a custom build?"
+ "Failed to allocate matching dictionary to match against PMU"
+ "Failed to create subDict"
+ "Failed to locate primary PMU service"
+ "IOPMUBootFaultInfo"
+ "IOPMUPrimary"
+ "IOPropertyMatch"
+ "IOService"
+ "Incompatible Baseband firmware."
+ "Invalid property type"
+ "OK"
+ "PANIC: %s"
+ "PanicString"
+ "QMI low power, please file radar in Purple Telephony - 1.0"
+ "RadiosPreferences"
+ "RadiosPreferences class not available"
+ "RadiosPreferencesDelegate"
+ "ServiceManager sleep timeout"
+ "ServiceManager wake timeout"
+ "Setup Assistant needs to run: %{bool}d"
+ "SetupAssistant framework not available"
+ "T@\"RadiosPreferences\",&,N,V_radioPrefs"
+ "T^{dispatch_queue_s=},N,V_queue"
+ "Triggering stackshot, goes with "
+ "T{CFSharedRef<__CFUserNotification>=^{__CFUserNotification}},N,V_notification"
+ "Unable to find class %s"
+ "Unable to read out PMU properties"
+ "Unexpected behavior may occur. Please upgrade to a newer firmware."
+ "Unsupported ABM profile, check your plist!"
+ "^{dispatch_queue_s=}"
+ "^{dispatch_queue_s=}16@0:8"
+ "_notification"
+ "_queue"
+ "_radioPrefs"
+ "airplaneMode"
+ "airplaneModeChanged"
+ "airplaneModeChanged: Airplane mode changed to %{bool}d"
+ "airplaneModeChanged: Airplane mode disabled externally, dismissing alert"
+ "airplaneModeChanged: _notification is nil, ignoring callback"
+ "boot.mod.airplane"
+ "build"
+ "com.apple.telephony.capabilities"
+ "dealloc"
+ "delegate"
+ "dictionary"
+ "initWithNotification:"
+ "initWithNotification: Failed to create RadiosPreferences instance"
+ "initWithNotification: RadiosPreferences class NOT found"
+ "initWithQueue:"
+ "queue"
+ "radioPrefs"
+ "setAirplaneModeWithoutMirroring:"
+ "setAlertHeader:"
+ "setAlertMessage:"
+ "setAlternateButtonTitle:"
+ "setDefaultButtonTitle:"
+ "setNotification:"
+ "setObject:forKeyedSubscript:"
+ "setPreventsAutomaticDismissal:"
+ "setQueue:"
+ "setRadioPrefs:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"
+ "startMonitoring"
+ "stopMonitoring"
+ "v116@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}20{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}44{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}68{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}92"
+ "v128@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}16{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}88"
+ "v24@0:8^{dispatch_queue_s=}16"
+ "v24@0:8{CFSharedRef<__CFUserNotification>=^{__CFUserNotification}}16"
+ "v32@?0{BudgetData={map<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>, std::less<abm::BasebandCPMSPowerBudgetScale>, std::allocator<std::pair<const abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>={__tree<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::__map_value_compare<abm::BasebandCPMSPowerBudgetScale, std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::less<abm::BasebandCPMSPowerBudgetScale>>, std::allocator<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}}8"
+ "v32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8"
+ "v32@?0{vector<abm::BasebandThermalID, std::allocator<abm::BasebandThermalID>>=^C^C{?=^C}}8"
+ "v32@?0{vector<abm::PowerMitigationData, std::allocator<abm::PowerMitigationData>>=^{PowerMitigationData}^{PowerMitigationData}{?=^{PowerMitigationData}}}8"
+ "v32@?0{vector<abm::ThermalSensorData, std::allocator<abm::ThermalSensorData>>=^{ThermalSensorData}^{ThermalSensorData}{?=^{ThermalSensorData}}}8"
+ "v36@?0i8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}12"
+ "v36@?0{map<const char *, std::list<std::pair<unsigned long long, unsigned int>>, std::less<const char *>, std::allocator<std::pair<const char *const, std::list<std::pair<unsigned long long, unsigned int>>>>>={__tree<std::__value_type<const char *, std::list<std::pair<unsigned long long, unsigned int>>>, std::__map_value_compare<const char *, std::__value_type<const char *, std::list<std::pair<unsigned long long, unsigned int>>>, std::less<const char *>>, std::allocator<std::__value_type<const char *, std::list<std::pair<unsigned long long, unsigned int>>>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}8I32"
+ "v44@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}20"
+ "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40"
+ "v48@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{CFSharedRef<const __CFDictionary>=^{__CFDictionary}}32{block<void (^)()>=@?}40"
+ "v68@?0{MetricInfo=iiiiiBB{optional<int>=(?=ci)B}}8I40{vector<unsigned char, std::allocator<unsigned char>>=**{?=*}}44"
+ "{CFSharedRef<__CFUserNotification>=\"fRef\"^{__CFUserNotification}}"
+ "{CFSharedRef<__CFUserNotification>=^{__CFUserNotification}}16@0:8"
+ "{map<std::string, CallBackData, std::less<std::string>, std::allocator<std::pair<const std::string, CallBackData>>>=\"__tree_\"{__tree<std::__value_type<std::string, CallBackData>, std::__map_value_compare<std::string, std::__value_type<std::string, CallBackData>, std::less<std::string>>, std::allocator<std::__value_type<std::string, CallBackData>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}64@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}40"
- "-l 0xffffffff -v 0 -N"
- "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16"
- "AppleBasebandManager-AppleBasebandServices_Manager-1397"
- "AppleBasebandServices_Manager-1397"
- "B136@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@88{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}96"
- "v116@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}20{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}44{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}68{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}92"
- "v128@0:8{NotificationInfo={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16{CallBackData=@?{queue={object=^{dispatch_object_s}}}{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}88"
- "v32@?0{BudgetData={map<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>, std::less<abm::BasebandCPMSPowerBudgetScale>, std::allocator<std::pair<const abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>={__tree<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::__map_value_compare<abm::BasebandCPMSPowerBudgetScale, std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>, std::less<abm::BasebandCPMSPowerBudgetScale>>, std::allocator<std::__value_type<abm::BasebandCPMSPowerBudgetScale, std::optional<unsigned int>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}}8"
- "v32@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}8"
- "v32@?0{vector<abm::BasebandThermalID, std::allocator<abm::BasebandThermalID>>=^C^C^C}8"
- "v32@?0{vector<abm::PowerMitigationData, std::allocator<abm::PowerMitigationData>>=^{PowerMitigationData}^{PowerMitigationData}^{PowerMitigationData}}8"
- "v32@?0{vector<abm::ThermalSensorData, std::allocator<abm::ThermalSensorData>>=^{ThermalSensorData}^{ThermalSensorData}^{ThermalSensorData}}8"
- "v36@?0i8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}12"
- "v36@?0{map<const char *, std::list<std::pair<unsigned long long, unsigned int>>, std::less<const char *>, std::allocator<std::pair<const char *const, std::list<std::pair<unsigned long long, unsigned int>>>>>={__tree<std::__value_type<const char *, std::list<std::pair<unsigned long long, unsigned int>>>, std::__map_value_compare<const char *, std::__value_type<const char *, std::list<std::pair<unsigned long long, unsigned int>>>, std::less<const char *>>, std::allocator<std::__value_type<const char *, std::list<std::pair<unsigned long long, unsigned int>>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}8I32"
- "v44@0:8i16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}20"
- "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8{dict={object=^v}}40"
- "v48@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}8{CFSharedRef<const __CFDictionary>=^{__CFDictionary}}32{block<void (^)()>=@?}40"
- "v68@?0{MetricInfo=iiiiiBB{optional<int>=(?=ci)B}}8I40{vector<unsigned char, std::allocator<unsigned char>>=***}44"
- "{map<std::string, CallBackData, std::less<std::string>, std::allocator<std::pair<const std::string, CallBackData>>>=\"__tree_\"{__tree<std::__value_type<std::string, CallBackData>, std::__map_value_compare<std::string, std::__value_type<std::string, CallBackData>, std::less<std::string>>, std::allocator<std::__value_type<std::string, CallBackData>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
- "{vector<std::string, std::allocator<std::string>>=^v^v^v}64@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}40"

```
