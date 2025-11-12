## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1399.2.0.0.0
-  __TEXT.__text: 0x22da8c
-  __TEXT.__auth_stubs: 0x3370
-  __TEXT.__init_offsets: 0x160
+1399.4.0.0.0
+  __TEXT.__text: 0x228aa0
+  __TEXT.__auth_stubs: 0x32c0
+  __TEXT.__init_offsets: 0x150
   __TEXT.__objc_methlist: 0x52c
-  __TEXT.__const: 0xf638
-  __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__gcc_except_tab: 0x3566c
-  __TEXT.__cstring: 0x81b0
-  __TEXT.__oslogstring: 0xbfc9
-  __TEXT.__unwind_info: 0xa3d8
+  __TEXT.__const: 0xf558
+  __TEXT.__dlopen_cstrs: 0x52
+  __TEXT.__gcc_except_tab: 0x34b78
+  __TEXT.__cstring: 0x7f96
+  __TEXT.__oslogstring: 0xbdef
+  __TEXT.__unwind_info: 0xa2a8
   __TEXT.__objc_classname: 0x13c
   __TEXT.__objc_methname: 0x1605
   __TEXT.__objc_methtype: 0x12b1
   __TEXT.__objc_stubs: 0x12c0
-  __DATA_CONST.__got: 0x2298
-  __DATA_CONST.__const: 0x2168
+  __DATA_CONST.__got: 0x2260
+  __DATA_CONST.__const: 0x20e8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x660
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x19c8
-  __AUTH_CONST.__const: 0xebf8
-  __AUTH_CONST.__cfstring: 0x980
+  __AUTH_CONST.__auth_got: 0x1970
+  __AUTH_CONST.__const: 0xeb28
+  __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0xa68
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x4c
-  __DATA.__data: 0x580
+  __DATA.__data: 0x538
   __DATA.__bss: 0x4d0
   __DATA.__common: 0xa
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x630
-  __DATA_DIRTY.__common: 0xd8
-  __DATA_DIRTY.__bss: 0x2ca
+  __DATA_DIRTY.__data: 0x5d8
+  __DATA_DIRTY.__common: 0xd0
+  __DATA_DIRTY.__bss: 0x28a
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 882911BF-C4FE-3C28-AD85-97D894C63EF9
-  Functions: 6147
-  Symbols:   18846
-  CStrings:  2901
+  UUID: 76587314-DBFD-3659-9BB9-5991AD0F1F71
+  Functions: 6125
+  Symbols:   18722
+  CStrings:  2869
 
Symbols:
+ GCC_except_table218
+ GCC_except_table224
+ GCC_except_table251
+ GCC_except_table271
+ GCC_except_table286
+ GCC_except_table289
+ GCC_except_table301
+ GCC_except_table330
+ GCC_except_table348
+ GCC_except_table359
+ GCC_except_table364
+ GCC_except_table367
+ GCC_except_table398
+ GCC_except_table406
+ GCC_except_table419
+ GCC_except_table460
+ GCC_except_table462
+ GCC_except_table479
+ _MAEGetActivationStateWithError
+ ____ZN10BootModule13shutdown_syncEN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEE_block_invoke.135
+ ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.113
+ ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.114
+ ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.124
+ ____ZN10BootModule21handleBootFailed_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke.99
+ ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.69
+ ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.73
+ ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.77
+ ____ZN10BootModule28updateNetworkCampStatus_syncEb_block_invoke.191
+ ____ZN10BootModule9boot_syncEv_block_invoke.145
+ ____ZN10BootModule9boot_syncEv_block_invoke.147
+ ____ZN10BootModule9boot_syncEv_block_invoke.164
+ ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke.14
+ ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke.16
+ ____ZZN8FSModule18requestFSSync_syncEvENK3$_0clEv_block_invoke.127
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.145
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.149
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.155
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.159
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.163
+ ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.167
+ ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke.153
+ ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke.159
+ ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke_2.154
+ ___block_descriptor_tmp.103
+ ___block_descriptor_tmp.106
+ ___block_descriptor_tmp.107
+ ___block_descriptor_tmp.113
+ ___block_descriptor_tmp.119
+ ___block_descriptor_tmp.121
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.134
+ ___block_descriptor_tmp.143
+ ___block_descriptor_tmp.157
+ ___block_descriptor_tmp.163
+ ___block_descriptor_tmp.171
+ ___block_descriptor_tmp.175
+ ___block_descriptor_tmp.178
+ ___block_descriptor_tmp.244
+ ___block_descriptor_tmp.250
+ ___block_descriptor_tmp.261
+ ___block_descriptor_tmp.264
+ ___block_descriptor_tmp.278
+ ___block_literal_global.257
+ ___block_literal_global.86
+ ___copy_helper_block_e8_32c35_ZTSNSt3__18weak_ptrI10BootModuleEE
+ ___cxx_global_var_init.198
+ ___cxx_global_var_init.199
+ ___cxx_global_var_init.34
+ ___cxx_global_var_init.35
+ ___cxx_global_var_init.38
+ ___cxx_global_var_init.39
+ ___cxx_global_var_init.66
+ ___destroy_helper_block_e8_32c35_ZTSNSt3__18weak_ptrI10BootModuleEE
+ _isDeviceActivated
+ _kMAActivationStateActivated
- GCC_except_table221
- GCC_except_table236
- GCC_except_table270
- GCC_except_table280
- GCC_except_table288
- GCC_except_table292
- GCC_except_table298
- GCC_except_table349
- GCC_except_table390
- GCC_except_table396
- GCC_except_table407
- GCC_except_table413
- GCC_except_table417
- GCC_except_table427
- GCC_except_table446
- GCC_except_table458
- GCC_except_table461
- GCC_except_table465
- GCC_except_table478
- _CFUserNotificationDisplayNotice
- _TelephonyBasebandWatchdogStartWithStackshot
- _TelephonyUtilTriggerNMI
- _TelephonyUtilWriteStackshot
- __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
- __ZL26audit_stringSetupAssistant
- __ZN10DataModule20setDataProperty_syncEN3xpc4dictEN8dispatch5blockIU13block_pointerFviS1_EEE
- __ZN12capabilities3abs17shouldBlockResetsEv
- __ZN12capabilities3abs24kKeyDataPowerSaveEnabledE
- __ZN12capabilities3abs26kKeyDataFlowControlEnabledE
- __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
- __ZN12capabilities3abs27kKeyDataAggregationProtocolE
- __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
- __ZN12capabilities3abs31kKeyDataAggregationMaxSizeBytesE
- __ZN12capabilities3abs35kKeyDataAggregationDatagramMaxCountE
- __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
- __ZN3ctu23PthreadMutexGuardPolicyI21CapabilitiesOverridesED1Ev
- __ZN3ctu23PthreadMutexGuardPolicyI21CapabilitiesOverridesED2Ev
- __ZN3ctu2cf6insertIPK10__CFStringS4_EEbP14__CFDictionaryT_T0_PK13__CFAllocator
- __ZN3ctu5power7manager20simulateNotificationEjb
- __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
- __ZN7support2uiL17gNotificationLockE
- __ZN7support2uiL9isAllowedEv
- __ZN9Overrides13getPreferenceIbEEbRKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERT_
- __ZN9Overrides13setPreferenceIbEEbRKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_b
- __ZNKSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE13__get_deleterERKSt9type_info
- __ZNSt3__110shared_ptrI21CapabilitiesOverridesED1B8ne200100Ev
- __ZNSt3__110shared_ptrI21CapabilitiesOverridesED2B8ne200100Ev
- __ZNSt3__110shared_ptrIN3ctu5power7managerEED2B8ne200100Ev
- __ZNSt3__110unique_ptrI21CapabilitiesOverridesNS_14default_deleteIS1_EEED2B8ne200100Ev
- __ZNSt3__110unique_ptrIZNK3ctu20SharedSynchronizableI9SimulatorE15execute_wrappedIZZNS3_26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEEUlvE_EEvOT_EUlvE_NS_14default_deleteISE_EEED1B8ne200100Ev
- __ZNSt3__110unique_ptrIZZN9Simulator26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEEUlvE_NS_14default_deleteIS7_EEED1B8ne200100Ev
- __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEED1Ev
- __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
- __ZTINSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
- __ZTSNSt3__110shared_ptrI21CapabilitiesOverridesE27__shared_ptr_default_deleteIS1_S1_EE
- __ZTSNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
- __ZTVNSt3__120__shared_ptr_pointerIP21CapabilitiesOverridesNS_10shared_ptrIS1_E27__shared_ptr_default_deleteIS1_S1_EENS_9allocatorIS1_EEEE
- __ZZN9ABMServer10getProfileEvE11sABMProfile
- __ZZN9ABMServer10getProfileEvE9onceToken
- ____ZL25SetupAssistantLibraryCorePPc_block_invoke
- ____ZL38getBYSetupAssistantNeedsToRunSymbolLocv_block_invoke
- ____ZN10BootModule13shutdown_syncEN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEE_block_invoke.139
- ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.117
- ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.122
- ____ZN10BootModule14softReset_syncE9ResetInfoN8dispatch5blockIU13block_pointerFviNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEE_block_invoke.128
- ____ZN10BootModule21handleBootFailed_syncENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke.101
- ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.71
- ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.75
- ____ZN10BootModule28registerCommandHandlers_syncEv_block_invoke.79
- ____ZN10BootModule28updateNetworkCampStatus_syncEb_block_invoke.195
- ____ZN10BootModule9boot_syncEv_block_invoke.149
- ____ZN10BootModule9boot_syncEv_block_invoke.155
- ____ZN10BootModule9boot_syncEv_block_invoke.168
- ____ZN10DataModule28registerCommandHandlers_syncEv_block_invoke.12
- ____ZN10DataModule28registerCommandHandlers_syncEv_block_invoke_2.13
- ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke.17
- ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke.21
- ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke.24
- ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke_2.25
- ____ZN19QMITransportService13enterLowPowerEN8dispatch13group_sessionE_block_invoke_3
- ____ZN9ABMServer10getProfileEv_block_invoke
- ____ZZN8FSModule18requestFSSync_syncEvENK3$_0clEv_block_invoke.128
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.147
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.153
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.157
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.161
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.165
- ____ZZZN12TraceManager26registerEventHandlers_syncEvENK3$_0clEN8dispatch13group_sessionEN3xpc4dictEENKUlvE_clEv_block_invoke.169
- ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke.160
- ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke.166
- ____ZZZN19QMITransportService12exitLowPowerEN8dispatch13group_sessionEEUb1_ENK3$_7clEb_block_invoke_2.161
- ___block_descriptor_tmp.105
- ___block_descriptor_tmp.114
- ___block_descriptor_tmp.115
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.133
- ___block_descriptor_tmp.142
- ___block_descriptor_tmp.153
- ___block_descriptor_tmp.156
- ___block_descriptor_tmp.159
- ___block_descriptor_tmp.164
- ___block_descriptor_tmp.168
- ___block_descriptor_tmp.169
- ___block_descriptor_tmp.172
- ___block_descriptor_tmp.173
- ___block_descriptor_tmp.198
- ___block_descriptor_tmp.201
- ___block_descriptor_tmp.249
- ___block_descriptor_tmp.265
- ___block_descriptor_tmp.269
- ___block_descriptor_tmp.280
- ___block_descriptor_tmp.283
- ___block_descriptor_tmp.91
- ___block_literal_global.262
- ___block_literal_global.40
- ___block_literal_global.88
- ___cxx_global_var_init.205
- ___cxx_global_var_init.206
- ___cxx_global_var_init.207
- ___cxx_global_var_init.208
- ___cxx_global_var_init.209
- ___cxx_global_var_init.42
- ___cxx_global_var_init.43
- ___cxx_global_var_init.44
- ___cxx_global_var_init.45
- ___cxx_global_var_init.69
- _deviceIsInSetupAssistant
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dlerror
- _dlsym
CStrings:
+ "#N Airplane mode enabled due to 3FR"
+ "#N Device boot detected, 3FR check - shouldDetect:%{bool}d isGreenTea:%{bool}d isActivated:%{bool}d"
+ "-l 0xffffffff -v 0 -N"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1399.4"
+ "AppleBasebandServices_Manager-1399.4"
- "#D     %s"
- "#D Enumerating HealthEvents to be written to disk:"
- "#D HealthEvents dictionary representation to be written to disk: %@"
- "#I Simulated notification: %s"
- "#I Triggering stackshot"
- "#I Triggering stackshot  -- done"
- "#I blocking reset until user signals"
- "#N Device boot detected, 3FR check - shouldDetect:%{bool}d isGreenTea:%{bool}d"
- "#N Performing 3FR check"
- "#N Putting the device in Airplane mode due to 3FR detection"
- ", reason "
- "-l 0xffffffff -v 99 -N"
- "AppleBasebandManager-AppleBasebandServices_Manager-1399.2"
- "AppleBasebandServices_Manager-1399.2"
- "BYSetupAssistantNeedsToRun"
- "Baseband Firmware Not Found"
- "Baseband Hard-Reset: "
- "Capability %s returning overridden value"
- "Did you forget to check update baseband or set permissions if you used a custom build?"
- "Incompatible Baseband firmware."
- "Invalid property type"
- "OK"
- "PANIC: %s"
- "PanicString"
- "QMI low power, please file radar in Purple Telephony - 1.0"
- "ServiceManager sleep timeout"
- "ServiceManager wake timeout"
- "Setup Assistant needs to run: %{bool}d"
- "SetupAssistant framework not available"
- "Triggering stackshot, goes with "
- "Unexpected behavior may occur. Please upgrade to a newer firmware."
- "Unsupported ABM profile, check your plist!"
- "com.apple.telephony.capabilities"
- "softlink:r:path:/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"

```
