## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-217.30.4.0.0
-  __TEXT.__text: 0x4c314
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x1c70
-  __TEXT.__const: 0x258
-  __TEXT.__cstring: 0x143a5
+217.41.1.0.0
+  __TEXT.__text: 0x51698
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x215c
+  __TEXT.__const: 0x268
+  __TEXT.__cstring: 0x153af
   __TEXT.__gcc_except_tab: 0xf8
   __TEXT.__oslogstring: 0x3bc
-  __TEXT.__unwind_info: 0xb50
-  __TEXT.__objc_classname: 0x21e
-  __TEXT.__objc_methname: 0x9876
-  __TEXT.__objc_methtype: 0xe52
-  __TEXT.__objc_stubs: 0x6380
+  __TEXT.__unwind_info: 0xc68
+  __TEXT.__objc_classname: 0x275
+  __TEXT.__objc_methname: 0xa0de
+  __TEXT.__objc_methtype: 0xf2d
+  __TEXT.__objc_stubs: 0x6940
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x11b8
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__const: 0x1268
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x58a8
-  __DATA_CONST.__objc_selrefs: 0x1ec0
-  __DATA_CONST.__objc_arraydata: 0x1c8
-  __AUTH_CONST.__cfstring: 0x3980
-  __AUTH_CONST.__objc_const: 0x540
-  __AUTH_CONST.__const: 0x620
+  __DATA_CONST.__objc_const: 0x6050
+  __DATA_CONST.__objc_selrefs: 0x20b8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_arraydata: 0x218
+  __AUTH_CONST.__cfstring: 0x3e20
+  __AUTH_CONST.__objc_const: 0x6f0
+  __AUTH_CONST.__const: 0x680
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_dictobj: 0x320
+  __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x1c8
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH.__objc_data: 0x370
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH.__objc_data: 0x460
   __AUTH.__data: 0x288
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x220
-  __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x78c
-  __DATA.__data: 0x820
+  __DATA.__objc_ivar: 0x82c
+  __DATA.__data: 0x960
   __DATA.__common: 0x10
-  __DATA.__bss: 0x4d8
+  __DATA.__bss: 0x518
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: A85A4245-371F-3E58-A1AC-C5DDE56002E1
-  Functions: 1116
-  Symbols:   4295
-  CStrings:  4643
+  UUID: EE1F1D53-A128-3F3E-A8AA-1B465595E566
+  Functions: 1248
+  Symbols:   4706
+  CStrings:  4928
 
Symbols:
+ +[HDSDefaults getBoolForKey:defaultValue:]
+ +[HDSDefaults getDoubleForKey:defaultValue:]
+ +[HDSDefaults getIntegerForKey:defaultValue:]
+ +[HDSDefaults setBoolForKey:newValue:]
+ +[HDSDefaults setSysDropMode:]
+ +[HDSDefaults sharedDefaults]
+ +[HDSDefaults sharedInstance]
+ +[HDSDefaults sysDropEnabled]
+ +[HDSDefaults sysDropForceErrorEarlyEnabled]
+ +[HDSDefaults sysDropForceErrorLateEnabled]
+ +[SysDropService signpostLog]
+ +[SysDropSession signpostLog]
+ -[HDSDefaults .cxx_destruct]
+ -[HDSDefaults defaults]
+ -[HDSDefaults init]
+ -[HDSDefaults setDefaults:]
+ -[HDSSetupService _handleStartSysDrop:responseHandler:]
+ -[HDSSetupService setSysDropService:]
+ -[HDSSetupService sysDropService]
+ -[HDSSetupSession _isPreflightError:]
+ -[HDSSetupSession _logWiFiRetryMetrics:]
+ -[HDSSetupSession _startSysDropMode:]
+ -[HDSSetupSession _startSysDropSysdiagnoseRequest:]
+ -[HDSSetupSession fetchLocationServicesEnabled]
+ -[HDSSetupSession presentingChildViewController]
+ -[HDSSetupSession setPresentingChildViewController:]
+ -[HDSSetupSession setSysDropMode:]
+ -[HDSSetupSession setSysDropSession:]
+ -[HDSSetupSession startAirDropSysdiagnose]
+ -[HDSSetupSession sysDropEnabled]
+ -[HDSSetupSession sysDropSession]
+ -[SysDropService .cxx_destruct]
+ -[SysDropService _activate]
+ -[SysDropService _cleanup]
+ -[SysDropService _handleAirDropRequest:responseHandler:]
+ -[SysDropService _handlePreCheckRequest:responseHandler:]
+ -[SysDropService _handleRawRequest:flags:responseHandler:]
+ -[SysDropService _handleSessionEnded:]
+ -[SysDropService _handleSessionStarted:]
+ -[SysDropService _invalidate]
+ -[SysDropService _sfServiceStart]
+ -[SysDropService _sysdiagnoseStart]
+ -[SysDropService activate]
+ -[SysDropService dealloc]
+ -[SysDropService dispatchQueue]
+ -[SysDropService init]
+ -[SysDropService invalidate]
+ -[SysDropService peerEventHandler]
+ -[SysDropService serviceStartedFromSetup]
+ -[SysDropService setDispatchQueue:]
+ -[SysDropService setPeerEventHandler:]
+ -[SysDropService setServiceStartedFromSetup:]
+ -[SysDropService setSfService:]
+ -[SysDropService setSfSession:]
+ -[SysDropService sfService]
+ -[SysDropService sfSession]
+ -[SysDropService signpostID]
+ -[SysDropSession .cxx_destruct]
+ -[SysDropSession _activate]
+ -[SysDropSession _cleanupSession]
+ -[SysDropSession _cleanup]
+ -[SysDropSession _getAirDropDiscoverableMode]
+ -[SysDropSession _getAirDropID]
+ -[SysDropSession _invalidate]
+ -[SysDropSession _reportError:label:]
+ -[SysDropSession _runAirDrop]
+ -[SysDropSession _runPreCheckRequest]
+ -[SysDropSession _runPreCheckResponse:error:]
+ -[SysDropSession _runPreCheck]
+ -[SysDropSession _runSFSessionStart]
+ -[SysDropSession _runSysdiagnose]
+ -[SysDropSession _run]
+ -[SysDropSession activate]
+ -[SysDropSession createSysDropAirDropEvent:error:]
+ -[SysDropSession createSysDropSysDiagnoseEvent:]
+ -[SysDropSession dealloc]
+ -[SysDropSession disconnect]
+ -[SysDropSession discoveryControllerLegacyModePropertiesDidChange:]
+ -[SysDropSession discoveryControllerSettingsDidChange:]
+ -[SysDropSession discoveryControllerVisibilityDidChange:]
+ -[SysDropSession dispatchQueue]
+ -[SysDropSession enableAirDropForEveryone]
+ -[SysDropSession handlePeerEvent:flags:]
+ -[SysDropSession init]
+ -[SysDropSession invalidate]
+ -[SysDropSession peerDevice]
+ -[SysDropSession progressHandler]
+ -[SysDropSession setDispatchQueue:]
+ -[SysDropSession setPeerDevice:]
+ -[SysDropSession setProgressHandler:]
+ -[SysDropSession setSetupError:]
+ -[SysDropSession setSfSession:]
+ -[SysDropSession setStartedFromSetup:]
+ -[SysDropSession setupError]
+ -[SysDropSession sfSession]
+ -[SysDropSession signpostID]
+ -[SysDropSession startAirDropSysdiagnose]
+ -[SysDropSession startedFromSetup]
+ -[SysDropSession sysDropActivated]
+ -[SysDropSession sysdiagnoseCompleted]
+ GCC_except_table261
+ _NSErrorF
+ _OBJC_CLASS_$_HDSDefaults
+ _OBJC_CLASS_$_SysDropService
+ _OBJC_CLASS_$_SysDropSession
+ _OBJC_IVAR_$_HDSDefaults._defaults
+ _OBJC_IVAR_$_HDSSetupService._sysDropService
+ _OBJC_IVAR_$_HDSSetupSession._homePodSysDropCapable
+ _OBJC_IVAR_$_HDSSetupSession._isConnectionError
+ _OBJC_IVAR_$_HDSSetupSession._locationServicesEnabled
+ _OBJC_IVAR_$_HDSSetupSession._presentingChildViewController
+ _OBJC_IVAR_$_HDSSetupSession._sysDropSession
+ _OBJC_IVAR_$_HDSSetupSession._wifiMaxAttempts
+ _OBJC_IVAR_$_HDSSetupSession._wifiNumRetries
+ _OBJC_IVAR_$_HDSSetupSession._wifiRetryDelay
+ _OBJC_IVAR_$_SysDropService._activateCalled
+ _OBJC_IVAR_$_SysDropService._advertiseFast
+ _OBJC_IVAR_$_SysDropService._dispatchQueue
+ _OBJC_IVAR_$_SysDropService._invalidateCalled
+ _OBJC_IVAR_$_SysDropService._peerEventHandler
+ _OBJC_IVAR_$_SysDropService._preCheckError
+ _OBJC_IVAR_$_SysDropService._serviceStartedFromSetup
+ _OBJC_IVAR_$_SysDropService._sfService
+ _OBJC_IVAR_$_SysDropService._sfSession
+ _OBJC_IVAR_$_SysDropService._sysdiagnosePathURL
+ _OBJC_IVAR_$_SysDropService._sysdiagnoseStatus
+ _OBJC_IVAR_$_SysDropService._sysdropInterface
+ _OBJC_IVAR_$_SysDropSession._activateCalled
+ _OBJC_IVAR_$_SysDropSession._airDropController
+ _OBJC_IVAR_$_SysDropSession._airDropState
+ _OBJC_IVAR_$_SysDropSession._dispatchQueue
+ _OBJC_IVAR_$_SysDropSession._invalidateCalled
+ _OBJC_IVAR_$_SysDropSession._peerDevice
+ _OBJC_IVAR_$_SysDropSession._preCheckState
+ _OBJC_IVAR_$_SysDropSession._progressHandler
+ _OBJC_IVAR_$_SysDropSession._proxSetupActiveToken
+ _OBJC_IVAR_$_SysDropSession._setupError
+ _OBJC_IVAR_$_SysDropSession._sfSession
+ _OBJC_IVAR_$_SysDropSession._sfSessionSecured
+ _OBJC_IVAR_$_SysDropSession._sfSessionState
+ _OBJC_IVAR_$_SysDropSession._startTicks
+ _OBJC_IVAR_$_SysDropSession._startedFromSetup
+ _OBJC_IVAR_$_SysDropSession._sysdiagnoseDone
+ _OBJC_IVAR_$_SysDropSession._sysdiagnoseState
+ _OBJC_IVAR_$_SysDropSession._sysdiagnoseStatus
+ _OBJC_IVAR_$_SysDropSession._totalSecs
+ _OBJC_METACLASS_$_HDSDefaults
+ _OBJC_METACLASS_$_SysDropService
+ _OBJC_METACLASS_$_SysDropSession
+ _SFAirDropDiscoveryControllerFunction
+ _SharingUILibrary.sLib
+ _SharingUILibrary.sOnce
+ __OBJC_$_CLASS_METHODS_HDSDefaults
+ __OBJC_$_CLASS_METHODS_SysDropService
+ __OBJC_$_CLASS_METHODS_SysDropSession
+ __OBJC_$_CLASS_PROP_LIST_SysDropService
+ __OBJC_$_CLASS_PROP_LIST_SysDropSession
+ __OBJC_$_INSTANCE_METHODS_HDSDefaults
+ __OBJC_$_INSTANCE_METHODS_SysDropService
+ __OBJC_$_INSTANCE_METHODS_SysDropSession
+ __OBJC_$_INSTANCE_VARIABLES_HDSDefaults
+ __OBJC_$_INSTANCE_VARIABLES_SysDropService
+ __OBJC_$_INSTANCE_VARIABLES_SysDropSession
+ __OBJC_$_PROP_LIST_HDSDefaults
+ __OBJC_$_PROP_LIST_SysDropService
+ __OBJC_$_PROP_LIST_SysDropSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFAirDropDiscoveryControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFAirDropDiscoveryControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_SFAirDropDiscoveryControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SysDropService
+ __OBJC_CLASS_PROTOCOLS_$_SysDropSession
+ __OBJC_CLASS_RO_$_HDSDefaults
+ __OBJC_CLASS_RO_$_SysDropService
+ __OBJC_CLASS_RO_$_SysDropSession
+ __OBJC_LABEL_PROTOCOL_$_SFAirDropDiscoveryControllerDelegate
+ __OBJC_METACLASS_RO_$_HDSDefaults
+ __OBJC_METACLASS_RO_$_SysDropService
+ __OBJC_METACLASS_RO_$_SysDropSession
+ __OBJC_PROTOCOL_$_SFAirDropDiscoveryControllerDelegate
+ ___26-[SysDropService activate]_block_invoke
+ ___26-[SysDropSession activate]_block_invoke
+ ___28-[SysDropService invalidate]_block_invoke
+ ___28-[SysDropSession disconnect]_block_invoke
+ ___28-[SysDropSession invalidate]_block_invoke
+ ___29+[HDSDefaults sharedInstance]_block_invoke
+ ___29+[SysDropService signpostLog]_block_invoke
+ ___29+[SysDropSession signpostLog]_block_invoke
+ ___29-[SysDropService _invalidate]_block_invoke
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke.1372
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2
+ ___33-[SysDropService _sfServiceStart]_block_invoke
+ ___33-[SysDropService _sfServiceStart]_block_invoke.27
+ ___33-[SysDropService _sfServiceStart]_block_invoke.29
+ ___33-[SysDropService _sfServiceStart]_block_invoke_2
+ ___33-[SysDropService _sfServiceStart]_block_invoke_3
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.294
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.296
+ ___36-[SysDropSession _runSFSessionStart]_block_invoke
+ ___36-[SysDropSession _runSFSessionStart]_block_invoke.31
+ ___36-[SysDropSession _runSFSessionStart]_block_invoke_2
+ ___36-[SysDropSession _runSFSessionStart]_block_invoke_3
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.569
+ ___37-[SysDropSession _runPreCheckRequest]_block_invoke
+ ___38-[SysDropSession sysdiagnoseCompleted]_block_invoke
+ ___40-[SysDropService _handleSessionStarted:]_block_invoke
+ ___40-[SysDropService _handleSessionStarted:]_block_invoke_2
+ ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_11
+ ___41-[SysDropSession startAirDropSysdiagnose]_block_invoke
+ ___41-[SysDropSession startAirDropSysdiagnose]_block_invoke_2
+ ___47-[HDSSetupSession fetchLocationServicesEnabled]_block_invoke
+ ___47-[HDSSetupSession fetchLocationServicesEnabled]_block_invoke_2
+ ___51-[HDSSetupSession _startSysDropSysdiagnoseRequest:]_block_invoke
+ ___55-[HDSSetupService _handleStartSysDrop:responseHandler:]_block_invoke
+ ___56-[HDSDeviceActivation _mae_createSessionWithCompletion:]_block_invoke.178
+ ___64-[HDSDeviceActivation _mae_createActivationWithData:completion:]_block_invoke.200
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.441
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1499
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1500
+ ___SharingUILibrary_block_invoke
+ ___block_descriptor_32_e19_v16?0"SFSession"8l
+ ___block_descriptor_40_e8_32s_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e51_v32?0"NSError"8"NSDictionary"16"NSDictionary"24ls32l8s40l8
+ ___block_literal_global.1228
+ ___block_literal_global.1232
+ ___block_literal_global.1248
+ ___block_literal_global.1252
+ ___block_literal_global.1257
+ ___block_literal_global.1261
+ ___block_literal_global.1273
+ ___block_literal_global.1279
+ ___block_literal_global.1286
+ ___block_literal_global.1290
+ ___block_literal_global.1294
+ ___block_literal_global.1305
+ ___block_literal_global.1374
+ ___block_literal_global.2873
+ ___block_literal_global.2877
+ ___block_literal_global.2881
+ ___block_literal_global.2885
+ ___block_literal_global.2889
+ ___block_literal_global.2905
+ ___block_literal_global.2909
+ ___block_literal_global.2922
+ ___block_literal_global.2926
+ ___block_literal_global.2930
+ ___block_literal_global.2934
+ ___block_literal_global.2959
+ ___block_literal_global.2963
+ ___block_literal_global.2969
+ ___block_literal_global.2974
+ ___block_literal_global.2978
+ ___block_literal_global.2983
+ ___block_literal_global.2996
+ ___block_literal_global.3000
+ ___block_literal_global.3095
+ ___block_literal_global.574
+ ___block_literal_global.672
+ ___block_literal_global.676
+ ___block_literal_global.683
+ ___block_literal_global.692
+ ___block_literal_global.908
+ __unnamed_array_storage.106
+ __unnamed_array_storage.107
+ __unnamed_array_storage.1116
+ __unnamed_array_storage.1138
+ __unnamed_array_storage.1139
+ __unnamed_array_storage.1149
+ __unnamed_array_storage.1150
+ __unnamed_array_storage.1203
+ __unnamed_array_storage.1204
+ __unnamed_array_storage.1877
+ __unnamed_array_storage.1878
+ __unnamed_array_storage.1927
+ __unnamed_array_storage.1928
+ __unnamed_array_storage.292
+ __unnamed_array_storage.330
+ __unnamed_array_storage.331
+ __unnamed_array_storage.390
+ __unnamed_array_storage.391
+ __unnamed_array_storage.41
+ __unnamed_array_storage.436
+ __unnamed_array_storage.484
+ __unnamed_array_storage.485
+ __unnamed_array_storage.588
+ __unnamed_array_storage.589
+ __unnamed_array_storage.706
+ __unnamed_array_storage.707
+ __unnamed_array_storage.822
+ __unnamed_array_storage.823
+ __unnamed_array_storage.844
+ __unnamed_array_storage.845
+ __unnamed_array_storage.877
+ __unnamed_array_storage.878
+ __unnamed_array_storage.988
+ __unnamed_array_storage.989
+ _classSFAirDropDiscoveryController
+ _gLogCategory_SysDropService
+ _gLogCategory_SysDropSession
+ _getSFAirDropDiscoveryControllerClass
+ _initSFAirDropDiscoveryController
+ _isInternalBuild
+ _kDefaultsDomain
+ _kDefaultsKey_SysDrop
+ _kDefaultsKey_SysDropEarlyError
+ _kDefaultsKey_SysDropLateError
+ _objc_msgSend$_getAirDropDiscoverableMode
+ _objc_msgSend$_getAirDropID
+ _objc_msgSend$_handleAirDropRequest:responseHandler:
+ _objc_msgSend$_handlePreCheckRequest:responseHandler:
+ _objc_msgSend$_handleStartSysDrop:responseHandler:
+ _objc_msgSend$_isPreflightError:
+ _objc_msgSend$_logWiFiRetryMetrics:
+ _objc_msgSend$_runAirDrop
+ _objc_msgSend$_runPreCheck
+ _objc_msgSend$_runPreCheckRequest
+ _objc_msgSend$_runPreCheckResponse:error:
+ _objc_msgSend$_runSysdiagnose
+ _objc_msgSend$_startSysDropMode:
+ _objc_msgSend$_startSysDropSysdiagnoseRequest:
+ _objc_msgSend$_sysdiagnoseStart
+ _objc_msgSend$cancelSysdiagnose:
+ _objc_msgSend$createSysDropAirDropEvent:error:
+ _objc_msgSend$createSysDropSysDiagnoseEvent:
+ _objc_msgSend$defaults
+ _objc_msgSend$deregisterRequestID:
+ _objc_msgSend$description
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$enableAirDropForEveryone
+ _objc_msgSend$fetchLocationServicesEnabled
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$getBoolForKey:defaultValue:
+ _objc_msgSend$handlePeerEvent:flags:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setBoolForKey:newValue:
+ _objc_msgSend$setDiscoverableMode:
+ _objc_msgSend$setPeerEventHandler:
+ _objc_msgSend$setServiceStartedFromSetup:
+ _objc_msgSend$setSetupError:
+ _objc_msgSend$setSfService:
+ _objc_msgSend$setStartedFromSetup:
+ _objc_msgSend$setSysDropMode:
+ _objc_msgSend$sharedDefaults
+ _objc_msgSend$startAirDropSysdiagnose
+ _objc_msgSend$sysDropActivated
+ _objc_msgSend$sysDropEnabled
+ _objc_msgSend$sysDropForceErrorEarlyEnabled
+ _objc_msgSend$sysDropForceErrorLateEnabled
+ _objc_msgSend$sysdiagnoseCompleted
+ _objc_msgSend$wiFiRetryMetrics
+ _sharedInstance.instance
+ _sharedInstance.onceToken
+ _signpostLog.log.165
+ _signpostLog.onceToken.166
- GCC_except_table255
- _CDPStateControllerFunction
- _OBJC_IVAR_$_CLISetupInteractor._homePodType
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke.1336
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.270
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.272
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.537
- ___56-[HDSDeviceActivation _mae_createSessionWithCompletion:]_block_invoke.177
- ___64-[HDSDeviceActivation _mae_createActivationWithData:completion:]_block_invoke.199
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.409
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1463
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1464
- ___block_literal_global.1185
- ___block_literal_global.1189
- ___block_literal_global.1193
- ___block_literal_global.1205
- ___block_literal_global.1209
- ___block_literal_global.1214
- ___block_literal_global.1218
- ___block_literal_global.1230
- ___block_literal_global.1243
- ___block_literal_global.1247
- ___block_literal_global.1251
- ___block_literal_global.1262
- ___block_literal_global.1338
- ___block_literal_global.2754
- ___block_literal_global.2758
- ___block_literal_global.2762
- ___block_literal_global.2766
- ___block_literal_global.2770
- ___block_literal_global.2774
- ___block_literal_global.2790
- ___block_literal_global.2803
- ___block_literal_global.2807
- ___block_literal_global.2811
- ___block_literal_global.2816
- ___block_literal_global.2820
- ___block_literal_global.2845
- ___block_literal_global.2849
- ___block_literal_global.2855
- ___block_literal_global.2860
- ___block_literal_global.2864
- ___block_literal_global.2882
- ___block_literal_global.2886
- ___block_literal_global.2976
- ___block_literal_global.542
- ___block_literal_global.669
- ___block_literal_global.673
- ___block_literal_global.680
- ___block_literal_global.689
- ___block_literal_global.873
- __unnamed_array_storage.1080
- __unnamed_array_storage.1081
- __unnamed_array_storage.1103
- __unnamed_array_storage.1104
- __unnamed_array_storage.1114
- __unnamed_array_storage.1168
- __unnamed_array_storage.1169
- __unnamed_array_storage.1838
- __unnamed_array_storage.1839
- __unnamed_array_storage.268
- __unnamed_array_storage.306
- __unnamed_array_storage.307
- __unnamed_array_storage.362
- __unnamed_array_storage.363
- __unnamed_array_storage.404
- __unnamed_array_storage.452
- __unnamed_array_storage.453
- __unnamed_array_storage.556
- __unnamed_array_storage.557
- __unnamed_array_storage.678
- __unnamed_array_storage.679
- __unnamed_array_storage.791
- __unnamed_array_storage.792
- __unnamed_array_storage.813
- __unnamed_array_storage.814
- __unnamed_array_storage.842
- __unnamed_array_storage.843
- __unnamed_array_storage.953
- __unnamed_array_storage.954
- _classCDPStateController
- _getCDPStateControllerClass
- _initCDPStateController
- _objc_msgSend$isManateeAvailable:
- _signpostLog.log.164
- _signpostLog.onceToken.165
CStrings:
+ "\x1143!\x11!23!\x12\x11\x13\x11\x1111\xf0%1Q3A\xe1!!\x81\x81a!sAb\x13\x13/\x0f"
+ "\x13\x14"
+ "\x15d\x11&\x13\x11\x13!\x12!3\x14"
+ "\"B\x11"
+ "-[HDSSetupService _handleSessionStarted:]_block_invoke_11"
+ "-[HDSSetupService _handleStartSysDrop:responseHandler:]"
+ "-[HDSSetupSession _logWiFiRetryMetrics:]"
+ "-[HDSSetupSession _startSysDropSysdiagnoseRequest:]_block_invoke"
+ "-[HDSSetupSession fetchLocationServicesEnabled]_block_invoke"
+ "-[SysDropService _handleAirDropRequest:responseHandler:]"
+ "-[SysDropService _handlePreCheckRequest:responseHandler:]"
+ "-[SysDropService _handleRawRequest:flags:responseHandler:]"
+ "-[SysDropService _handleSessionEnded:]"
+ "-[SysDropService _handleSessionStarted:]"
+ "-[SysDropService _invalidate]"
+ "-[SysDropService _invalidate]_block_invoke"
+ "-[SysDropService _sfServiceStart]"
+ "-[SysDropService _sfServiceStart]_block_invoke"
+ "-[SysDropService activate]_block_invoke"
+ "-[SysDropService init]"
+ "-[SysDropSession _activate]"
+ "-[SysDropSession _getAirDropDiscoverableMode]"
+ "-[SysDropSession _getAirDropID]"
+ "-[SysDropSession _invalidate]"
+ "-[SysDropSession _reportError:label:]"
+ "-[SysDropSession _runAirDrop]"
+ "-[SysDropSession _runPreCheckRequest]"
+ "-[SysDropSession _runPreCheckResponse:error:]"
+ "-[SysDropSession _runPreCheck]"
+ "-[SysDropSession _runSFSessionStart]"
+ "-[SysDropSession _runSFSessionStart]_block_invoke"
+ "-[SysDropSession _runSysdiagnose]"
+ "-[SysDropSession _run]"
+ "-[SysDropSession discoveryControllerLegacyModePropertiesDidChange:]"
+ "-[SysDropSession discoveryControllerSettingsDidChange:]"
+ "-[SysDropSession discoveryControllerVisibilityDidChange:]"
+ "-[SysDropSession enableAirDropForEveryone]"
+ "-[SysDropSession handlePeerEvent:flags:]"
+ "-[SysDropSession startAirDropSysdiagnose]"
+ "-[SysDropSession startAirDropSysdiagnose]_block_invoke_2"
+ "-[SysDropSession sysdiagnoseCompleted]"
+ "/System/Library/Frameworks/SharingUI.framework/SharingUI"
+ "/private/var/mobile/Library/Preferences/com.apple.sharingd.plist"
+ "@\"NSURL\""
+ "@\"NSUserDefaults\""
+ "@\"SBSSysdiagnoseInterface\""
+ "@\"SFAirDropDiscoveryController\""
+ "@\"SysDropService\""
+ "@\"SysDropSession\""
+ "@28@0:8I16@20"
+ "Activate SysDrop\n"
+ "Activate done, calling run\n"
+ "AirDrop ID invalid\n"
+ "AirDropID"
+ "Could not cancel Sysdiagnose %@\n"
+ "Could not get Error Domain from Wifi Metric: %@\n"
+ "Could not get Error Label from Wifi Metric: %@\n"
+ "Could not get Error code from Wifi Metric: %@\n"
+ "Could not get WiFi retry type from Wifi Metric: %@\n"
+ "Could not get WiFi success from Wifi Metric: %@\n"
+ "Could not get duration from Wifi Metric: %@\n"
+ "DataTransferred"
+ "DiscoverableMode"
+ "Everyone"
+ "EveryoneMode is not enabled\n"
+ "HDS SFSession Peer event: %@\n"
+ "HDSDefaults"
+ "HDSMessageRequestIDSysdiagnoseStart\n"
+ "HomePod SysDrop capable: %s | %#m\n"
+ "In Progress"
+ "LocationServicesEnabled %s\n"
+ "Managed & Unknown Account not supported"
+ "Not set"
+ "PreCheck hasn't succeeded yet (%d)\n"
+ "PreCheck response: %##.32@\n"
+ "PreCheck send request: %##.32@\n"
+ "PreCheck start\n"
+ "PreCheck taking a while\n"
+ "PreCheckRequest: %##@\n"
+ "PreCheckResponse error: %{error}\n"
+ "PreCheckResponse: %##@\n"
+ "Retry Metrics found, reporting\n"
+ "SFAirDropDiscoveryController"
+ "SFAirDropDiscoveryControllerDelegate"
+ "SFService activation error %@\n"
+ "SFSession was inherited, SFSession Done\n"
+ "SharingD prefs %@ | error %@\n"
+ "Started Sysdiagnose for SysDrop\n"
+ "Starting Sysdiagnose for SysDrop\n"
+ "SysDrop"
+ "SysDrop AirDrop Event"
+ "SysDrop Cancel Event"
+ "SysDrop Force Fail Late Default Enabled Error"
+ "SysDrop Init\n"
+ "SysDrop SFSession Peer event: %@\n"
+ "SysDrop Starting setup session with %@\n"
+ "SysDrop Sysdiagnose Error"
+ "SysDrop Sysdiagnose Event"
+ "SysDrop Sysdiagnose Status: %s\n"
+ "SysDrop Sysdiagnose: Error Code = %d | Error Domain: %@\n"
+ "SysDropEarlyError"
+ "SysDropLateError"
+ "SysDropService"
+ "SysDropSession"
+ "Sysdiagnose Completed\n"
+ "Sysdiagnose Failed"
+ "Sysdiagnose Finished\n"
+ "Sysdiagnose started for Sysdrop\n"
+ "Sysdiagnose still in progress\n"
+ "T@\"NSError\",C,N,V_setupError"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSUserDefaults\",&,N,V_defaults"
+ "T@\"SFService\",&,N,V_sfService"
+ "T@\"SysDropService\",&,N,V_sysDropService"
+ "T@\"SysDropSession\",&,N,V_sysDropSession"
+ "T@\"UIViewController\",&,N,V_presentingChildViewController"
+ "T@?,C,N,V_peerEventHandler"
+ "TB,N,V_serviceStartedFromSetup"
+ "TB,N,V_startedFromSetup"
+ "TQ,N,V_delayForOdeonStereoPairSeconds"
+ "WiFi Retry Metric sent: %@\n"
+ "WiFiSetup failed, Error = %{error}, remaining attempts = %d\n"
+ "WiFiSetup retrying in %d secs"
+ "_airDropController"
+ "_airDropState"
+ "_defaults"
+ "_getAirDropDiscoverableMode"
+ "_getAirDropID"
+ "_handleAirDropRequest: %##@\n"
+ "_handleAirDropRequest:responseHandler:"
+ "_handlePreCheckRequest:responseHandler:"
+ "_handleRawRequest: %@\n"
+ "_handleStartSysDrop:responseHandler:"
+ "_homePodSysDropCapable"
+ "_isConnectionError"
+ "_isPreflightError:"
+ "_locationServicesEnabled"
+ "_logWiFiRetryMetrics:"
+ "_peerEventHandler"
+ "_preCheckError"
+ "_preCheckState"
+ "_presentingChildViewController"
+ "_runAirDrop"
+ "_runAirDrop in progress\n"
+ "_runPreCheck"
+ "_runPreCheckRequest"
+ "_runPreCheckResponse: Finished\n"
+ "_runPreCheckResponse:error:"
+ "_runPreflightMisc location fetch status\n"
+ "_runSysdiagnose"
+ "_runSysdiagnose start\n"
+ "_serviceStartedFromSetup"
+ "_setupError"
+ "_startSysDropMode:"
+ "_startSysDropSysdiagnoseRequest:"
+ "_startedFromSetup"
+ "_sysDropService"
+ "_sysDropSession"
+ "_sysdiagnoseDone"
+ "_sysdiagnosePathURL"
+ "_sysdiagnoseStart"
+ "_sysdiagnoseState"
+ "_sysdiagnoseStatus"
+ "_sysdropInterface"
+ "_wifiMaxAttempts"
+ "_wifiNumRetries"
+ "_wifiRetryDelay"
+ "airDropID: %@  | err: %d\n"
+ "airdropID %@\n"
+ "cancelSysdiagnose:"
+ "com.apple.SysDrop"
+ "com.apple.sharing.wifiretry"
+ "createSysDropAirDropEvent:error:"
+ "createSysDropSysDiagnoseEvent:"
+ "d32@0:8@16d24"
+ "defaults"
+ "deregisterRequestID:"
+ "dictionaryWithContentsOfURL:error:"
+ "discoverableMode %@\n"
+ "discoveryControllerLegacyModePropertiesDidChange %@\n"
+ "discoveryControllerLegacyModePropertiesDidChange:"
+ "discoveryControllerSettingsDidChange %@\n"
+ "discoveryControllerSettingsDidChange:"
+ "discoveryControllerVisibilityDidChange %@\n"
+ "discoveryControllerVisibilityDidChange:"
+ "doubleForKey:"
+ "duration"
+ "eSimExternal2FAStart"
+ "eSimExternal2FAStop"
+ "enableAirDropForEveryone"
+ "errorCodeString"
+ "failureType"
+ "fetchLocationServicesEnabled"
+ "fileURLWithPath:"
+ "getBoolForKey:defaultValue:"
+ "getDoubleForKey:defaultValue:"
+ "getIntegerForKey:defaultValue:"
+ "handlePeerEvent:flags:"
+ "integerForKey:"
+ "localizedDescription"
+ "peerEventHandler"
+ "presentingChildViewController"
+ "q\x15"
+ "q28@0:8@16B24"
+ "q32@0:8@16q24"
+ "retryAttempt"
+ "retryCount"
+ "saWiFiMaxAttempts"
+ "saWiFiRetryDelay"
+ "sd_ad_e"
+ "sd_ad_ed"
+ "sd_ad_er"
+ "sd_ad_id"
+ "sd_capa"
+ "sd_de"
+ "sd_ed"
+ "sd_er"
+ "sd_status"
+ "sd_sys_ec"
+ "sd_sys_ed"
+ "serviceStartedFromSetup"
+ "setBool:forKey:"
+ "setBoolForKey:newValue:"
+ "setDefaults:"
+ "setDiscoverableMode:"
+ "setPeerEventHandler:"
+ "setPresentingChildViewController:"
+ "setServiceStartedFromSetup:"
+ "setSetupError:"
+ "setSfService:"
+ "setStartedFromSetup:"
+ "setSysDropMode:"
+ "setSysDropService:"
+ "setSysDropSession:"
+ "setupError"
+ "sfService"
+ "sharedDefaults"
+ "startAirDropSysdiagnose"
+ "startAirDropSysdiagnose called with request %@\n"
+ "startAirDropSysdiagnose done: response = %@ | error = %@\n"
+ "startedFromSetup"
+ "sysDropActivated"
+ "sysDropEnabled"
+ "sysDropForceErrorEarlyEnabled"
+ "sysDropForceErrorLateEnabled"
+ "sysDropService"
+ "sysDropSession"
+ "sysdiagnoseCompleted"
+ "sysdrop"
+ "sysdrop_ad"
+ "sysdrop_check"
+ "sysdrop_sys_start"
+ "sysdrop_sys_update"
+ "v16@?0@\"NSDictionary\"8"
+ "v24@0:8@\"SFAirDropDiscoveryController\"16"
+ "wiFiRetryMetrics"
+ "wifiDN"
+ "wifiEC"
+ "wifiED"
+ "wifiEL"
+ "wifiRT"
+ "wifiSUCC"
- "\x1143!\x11!23!\x12\x11\x13\x11\x1111\xf0&Q3A\xe1!!\x81\x81a!sAe\x12/\x0e"
- "\x15d\x11&\x13\x11\x13!\x12!3\x13"
- "\"R\x11"
- "CDPStateController"
- "FtswpMzGQrpRXPQGOUFUUG"
- "No iCloud HSA2"
- "No iCloud manatee"
- "Preflight iCloud check for manatee\n"
- "SFSession Peer event: %@\n"
- "Ti,N,V_delayForOdeonStereoPairSeconds"
- "WiFiSetup failed, Error = %{error}\n"
- "_handleRawRequest: BasicConfig sent %@\n"
- "_homePodType"
- "homePodType"
- "isManateeAvailable:"
- "setSetupUserInputConfig HomePod Type is %d\n"

```
