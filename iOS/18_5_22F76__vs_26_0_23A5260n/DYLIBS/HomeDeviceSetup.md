## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-277.50.15.0.0
-  __TEXT.__text: 0x65b14
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x2d84
-  __TEXT.__const: 0x3a2
-  __TEXT.__cstring: 0x18624
-  __TEXT.__oslogstring: 0x57d
-  __TEXT.__gcc_except_tab: 0x154
+345.0.1.0.0
+  __TEXT.__text: 0x6eb88
+  __TEXT.__auth_stubs: 0xfd0
+  __TEXT.__objc_methlist: 0x30c4
+  __TEXT.__const: 0x432
+  __TEXT.__cstring: 0x1a264
+  __TEXT.__oslogstring: 0x5ad
+  __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__constg_swiftt: 0xe0
   __TEXT.__swift5_typeref: 0xcb
   __TEXT.__swift5_reflstr: 0x8b

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x1530
-  __TEXT.__eh_frame: 0x490
-  __TEXT.__objc_classname: 0x2b4
-  __TEXT.__objc_methname: 0xbb36
-  __TEXT.__objc_methtype: 0x111e
-  __TEXT.__objc_stubs: 0x7340
-  __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x14c8
+  __TEXT.__unwind_info: 0x16e8
+  __TEXT.__eh_frame: 0x460
+  __TEXT.__objc_classname: 0x2bc
+  __TEXT.__objc_methname: 0xc9d3
+  __TEXT.__objc_methtype: 0x113e
+  __TEXT.__objc_stubs: 0x7b60
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__const: 0x179c
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2800
+  __DATA_CONST.__objc_selrefs: 0x2ad0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0x230
-  __AUTH_CONST.__auth_got: 0x800
-  __AUTH_CONST.__const: 0x848
-  __AUTH_CONST.__cfstring: 0x4d80
-  __AUTH_CONST.__objc_const: 0x6a40
+  __DATA_CONST.__objc_arraydata: 0x240
+  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH_CONST.__const: 0xad0
+  __AUTH_CONST.__cfstring: 0x52a0
+  __AUTH_CONST.__objc_const: 0x7170
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x3c0
+  __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH.__objc_data: 0x688
-  __AUTH.__data: 0x2d8
-  __DATA.__objc_ivar: 0x94c
-  __DATA.__data: 0xac0
+  __AUTH.__data: 0x2f8
+  __DATA.__objc_ivar: 0xa18
+  __DATA.__data: 0xa40
   __DATA.__common: 0x40
-  __DATA.__bss: 0x690
+  __DATA.__bss: 0x740
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
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
-  UUID: 1D00AE9F-EBE2-314A-87EB-ED31AD40DC76
-  Functions: 2580
-  Symbols:   7646
-  CStrings:  5650
+  UUID: CC148A0D-F37D-31C9-8ABF-1ECE2EF93029
+  Functions: 2831
+  Symbols:   8316
+  CStrings:  6042
 
Symbols:
+ +[HDSDefaults forceFailWiFi]
+ +[HDSDefaults forceHH2Upsell]
+ +[HDSDefaults forceHomeLocationCreationFlow]
+ +[HDSDefaults forceShowWiFiSummary]
+ +[HDSDefaults numberOfWiFiRetries]
+ +[HDSDefaults sysDropForceErrorHalfwayEnabled]
+ -[HDSDeviceOperationHomeKitSetup _runHomeKitAddHomeWithName:]
+ -[HDSDeviceOperationHomeKitSetup _runHomeKitAutoSelectHome:].cold.8
+ -[HDSDeviceOperationHomeKitSetup _run].cold.17
+ -[HDSDeviceOperationHomeKitSetup _run].cold.18
+ -[HDSDeviceOperationHomeKitSetup _run].cold.19
+ -[HDSDeviceOperationHomeKitSetup _run].cold.20
+ -[HDSDeviceOperationHomeKitSetup _run].cold.21
+ -[HDSDeviceOperationHomeKitSetup acceptSelectSameWrongLocation]
+ -[HDSDeviceOperationHomeKitSetup checkIfExistingHome:]
+ -[HDSDeviceOperationHomeKitSetup createHomeInSameLocation]
+ -[HDSDeviceOperationHomeKitSetup createdNewHomeInSetupFlow]
+ -[HDSDeviceOperationHomeKitSetup promptForHomeInSameLocationHandler]
+ -[HDSDeviceOperationHomeKitSetup promptForHomeNameCreationHandler]
+ -[HDSDeviceOperationHomeKitSetup resetHomeSelection]
+ -[HDSDeviceOperationHomeKitSetup resetToHomeSelection]
+ -[HDSDeviceOperationHomeKitSetup selectHomeName:]
+ -[HDSDeviceOperationHomeKitSetup setPromptForHomeInSameLocationHandler:]
+ -[HDSDeviceOperationHomeKitSetup setPromptForHomeNameCreationHandler:]
+ -[HDSDeviceOperationHomeKitSetup startHomeNameCreation:hasNameConflict:]
+ -[HDSSetupService _handleHomeScanRequest:responseHandler:]
+ -[HDSSetupService _handleHomeScanRequest:responseHandler:].cold.1
+ -[HDSSetupService _handlePreAuthRequest:responseHandler:].cold.10
+ -[HDSSetupService _handlePreAuthRequest:responseHandler:].cold.11
+ -[HDSSetupService _handlePreAuthRequest:responseHandler:].cold.12
+ -[HDSSetupService _handlePreAuthRequest:responseHandler:].cold.9
+ -[HDSSetupService createScanParameters]
+ -[HDSSetupService fetchScanResult:]
+ -[HDSSetupService fetchScanResult:].cold.1
+ -[HDSSetupService fetchScanResult]
+ -[HDSSetupService scanResultToDict:]
+ -[HDSSetupService setTime]
+ -[HDSSetupService setTime].cold.1
+ -[HDSSetupService setTime].cold.2
+ -[HDSSetupService setTime].cold.3
+ -[HDSSetupService setTime].cold.4
+ -[HDSSetupSession _reportErrorWithExtaInfo:label:dict:]
+ -[HDSSetupSession _reportErrorWithExtaInfo:label:dict:].cold.1
+ -[HDSSetupSession _reportErrorWithExtaInfo:label:dict:].cold.2
+ -[HDSSetupSession _runHH2Upsell]
+ -[HDSSetupSession _runHH2Upsell].cold.1
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.3
+ -[HDSSetupSession _runHomePodScanFetch]
+ -[HDSSetupSession _runHomePodScanFetch].cold.1
+ -[HDSSetupSession _runPreAuthResponse:error:].cold.10
+ -[HDSSetupSession _runPreAuthResponse:error:].cold.11
+ -[HDSSetupSession _runPreAuthResponse:error:].cold.12
+ -[HDSSetupSession _runPreAuthResponse:error:].cold.13
+ -[HDSSetupSession _runWiFiPassword]
+ -[HDSSetupSession _runWiFiPassword].cold.1
+ -[HDSSetupSession _runWiFiPassword].cold.2
+ -[HDSSetupSession _runWiFiPassword].cold.3
+ -[HDSSetupSession _runWiFiPicker]
+ -[HDSSetupSession _runWiFiPicker].cold.1
+ -[HDSSetupSession _runWiFiPicker].cold.2
+ -[HDSSetupSession _runWiFiPicker].cold.3
+ -[HDSSetupSession _runWiFiPicker].cold.4
+ -[HDSSetupSession _runWiFiSetup].cold.3
+ -[HDSSetupSession _runWiFiSetup].cold.4
+ -[HDSSetupSession _runWiFiSetup].cold.5
+ -[HDSSetupSession _runWiFiSummaryCard]
+ -[HDSSetupSession _runWiFiSummaryCard].cold.1
+ -[HDSSetupSession _runWiFiSummaryCard].cold.2
+ -[HDSSetupSession _runWiFiSummaryCard].cold.3
+ -[HDSSetupSession _runWiFiSummaryCard].cold.4
+ -[HDSSetupSession acceptSelectSameWrongLocation]
+ -[HDSSetupSession createErrorDictionary:ssid:]
+ -[HDSSetupSession createHomeInSameLocation]
+ -[HDSSetupSession createNewHomeWithName:]
+ -[HDSSetupSession dictForNetworkName:]
+ -[HDSSetupSession fetchAltDSIDAccount]
+ -[HDSSetupSession fetchHomePodLoggingProfile:]
+ -[HDSSetupSession fetchHomePodLoggingProfile:].cold.1
+ -[HDSSetupSession fetchTermsInfo]
+ -[HDSSetupSession filterNetworksForHomePod:]
+ -[HDSSetupSession homeKitStartHomeNameCreation:hasNameConflict:]
+ -[HDSSetupSession lastSSIDUsed]
+ -[HDSSetupSession promptForHH2UpsellHandler]
+ -[HDSSetupSession promptForHomeInSameLocationHandler]
+ -[HDSSetupSession promptForHomeNameCreationHandler]
+ -[HDSSetupSession promptForWiFiFailedHandler]
+ -[HDSSetupSession promptForWiFiPasswordHandler]
+ -[HDSSetupSession promptForWiFiPickerHandler]
+ -[HDSSetupSession promptForWiFiSummaryHandler]
+ -[HDSSetupSession promptToShareSettingsV2Handler]
+ -[HDSSetupSession resetToHomeSelection]
+ -[HDSSetupSession resetWiFiPicker:]
+ -[HDSSetupSession setPromptForHH2UpsellHandler:]
+ -[HDSSetupSession setPromptForHomeInSameLocationHandler:]
+ -[HDSSetupSession setPromptForHomeNameCreationHandler:]
+ -[HDSSetupSession setPromptForWiFiFailedHandler:]
+ -[HDSSetupSession setPromptForWiFiPasswordHandler:]
+ -[HDSSetupSession setPromptForWiFiPickerHandler:]
+ -[HDSSetupSession setPromptForWiFiSummaryHandler:]
+ -[HDSSetupSession setPromptToShareSettingsV2Handler:]
+ -[HDSSetupSession userAtHomeLocation:]
+ -[HDSSetupSession validateHomeName:completion:]
+ -[HDSSetupSession validateHomeName:completion:].cold.1
+ -[HDSSetupSession wiFiAcknowledged]
+ -[HDSSetupSession wiFiRetry]
+ -[HDSSetupSession wiFiSelected:]
+ -[HDSSetupSession wifiPasswordSelected:]
+ GCC_except_table10
+ GCC_except_table310
+ GCC_except_table368
+ GCC_except_table419
+ _CWFInterfaceFunction
+ _CWFNetworkSignatureFunction
+ _CWFScanParametersFunction
+ _CoreWifiLibrary.sLib
+ _CoreWifiLibrary.sOnce
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_IVAR_$_HDSDeviceOperationHomeKitSetup._createdNewHomeInSetupFlow
+ _OBJC_IVAR_$_HDSDeviceOperationHomeKitSetup._promptForHomeInSameLocationHandler
+ _OBJC_IVAR_$_HDSDeviceOperationHomeKitSetup._promptForHomeNameCreationHandler
+ _OBJC_IVAR_$_HDSDeviceOperationHomeKitSetup._userCreateHomeInSameLocation
+ _OBJC_IVAR_$_HDSDeviceOperationHomeKitSetup._userCreatedHomeName
+ _OBJC_IVAR_$_HDSDeviceOperationHomeKitSetup._userSelectHomeWrongLocation
+ _OBJC_IVAR_$_HDSSetupService._finishedFinal
+ _OBJC_IVAR_$_HDSSetupService._scanInProgress
+ _OBJC_IVAR_$_HDSSetupService._scanResults
+ _OBJC_IVAR_$_HDSSetupService._scanTimer
+ _OBJC_IVAR_$_HDSSetupService._timeSet
+ _OBJC_IVAR_$_HDSSetupSession._deviceProductName
+ _OBJC_IVAR_$_HDSSetupSession._deviceProductVersion
+ _OBJC_IVAR_$_HDSSetupSession._didDoV3Terms
+ _OBJC_IVAR_$_HDSSetupSession._doHomePodScan
+ _OBJC_IVAR_$_HDSSetupSession._forceFailEarlyState
+ _OBJC_IVAR_$_HDSSetupSession._forceFailHalfwayState
+ _OBJC_IVAR_$_HDSSetupSession._hh2UpsellState
+ _OBJC_IVAR_$_HDSSetupSession._homeAccessoryCategories
+ _OBJC_IVAR_$_HDSSetupSession._homeHubStatusSelectedHome
+ _OBJC_IVAR_$_HDSSetupSession._homeLocationState
+ _OBJC_IVAR_$_HDSSetupSession._homePodScanResults
+ _OBJC_IVAR_$_HDSSetupSession._homePodSupportsWiFiPicker
+ _OBJC_IVAR_$_HDSSetupSession._joinPrimaryNetworkCrossReference
+ _OBJC_IVAR_$_HDSSetupSession._numberOfAppleMediaAccessoriesInHome
+ _OBJC_IVAR_$_HDSSetupSession._phonesWiFiSSID
+ _OBJC_IVAR_$_HDSSetupSession._preferredHomeNetworkNames
+ _OBJC_IVAR_$_HDSSetupSession._preferredNetworkState
+ _OBJC_IVAR_$_HDSSetupSession._primaryResidentNetwork
+ _OBJC_IVAR_$_HDSSetupSession._promptForHH2UpsellHandler
+ _OBJC_IVAR_$_HDSSetupSession._promptForHomeInSameLocationHandler
+ _OBJC_IVAR_$_HDSSetupSession._promptForHomeNameCreationHandler
+ _OBJC_IVAR_$_HDSSetupSession._promptForWiFiFailedHandler
+ _OBJC_IVAR_$_HDSSetupSession._promptForWiFiPasswordHandler
+ _OBJC_IVAR_$_HDSSetupSession._promptForWiFiPickerHandler
+ _OBJC_IVAR_$_HDSSetupSession._promptForWiFiSummaryHandler
+ _OBJC_IVAR_$_HDSSetupSession._promptToShareSettingsV2Handler
+ _OBJC_IVAR_$_HDSSetupSession._reachableHomePodScanResults
+ _OBJC_IVAR_$_HDSSetupSession._retryPickerCount
+ _OBJC_IVAR_$_HDSSetupSession._selectedHomeHasResidentDevice
+ _OBJC_IVAR_$_HDSSetupSession._showWiFiPicker
+ _OBJC_IVAR_$_HDSSetupSession._ssidsToSelectFrom
+ _OBJC_IVAR_$_HDSSetupSession._upsellHH2
+ _OBJC_IVAR_$_HDSSetupSession._wifiInterface
+ _OBJC_IVAR_$_HDSSetupSession._wifiPassword
+ _OBJC_IVAR_$_HDSSetupSession._wifiPasswordSet
+ _OBJC_IVAR_$_HDSSetupSession._wifiPasswordState
+ _OBJC_IVAR_$_HDSSetupSession._wifiPicked
+ _OBJC_IVAR_$_HDSSetupSession._wifiPickerState
+ _OBJC_IVAR_$_HDSSetupSession._wifiSSIDAcknowledged
+ _OBJC_IVAR_$_HDSSetupSession._wifiScanFetchState
+ _OBJC_IVAR_$_HDSSetupSession._wifiSelectedSSID
+ _OBJC_IVAR_$_HDSSetupSession._wifiSummaryState
+ _OUTLINED_FUNCTION_10
+ ___26-[HDSSetupService setTime]_block_invoke
+ ___26-[HDSSetupService setTime]_block_invoke.cold.1
+ ___26-[HDSSetupService setTime]_block_invoke.cold.2
+ ___27-[HDSSetupService activate]_block_invoke_2
+ ___27-[HDSSetupService activate]_block_invoke_3
+ ___28-[HDSSetupSession wiFiRetry]_block_invoke
+ ___28-[HDSSetupSession wiFiRetry]_block_invoke.cold.1
+ ___32-[HDSSetupSession _runHH2Upsell]_block_invoke
+ ___32-[HDSSetupSession _runHH2Upsell]_block_invoke_2
+ ___32-[HDSSetupSession _runHH2Upsell]_block_invoke_2.cold.1
+ ___32-[HDSSetupSession _runHH2Upsell]_block_invoke_2.cold.2
+ ___32-[HDSSetupSession _runHH2Upsell]_block_invoke_2.cold.3
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke.cold.6
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1657
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1657.cold.1
+ ___32-[HDSSetupSession wiFiSelected:]_block_invoke
+ ___32-[HDSSetupSession wiFiSelected:]_block_invoke.cold.1
+ ___33-[HDSSetupSession _runWiFiPicker]_block_invoke
+ ___33-[HDSSetupSession _runWiFiPicker]_block_invoke_2
+ ___33-[HDSSetupSession _runWiFiPicker]_block_invoke_2.cold.1
+ ___33-[HDSSetupSession _runWiFiPicker]_block_invoke_2.cold.2
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.340
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.342
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.342.cold.1
+ ___34-[HDSSetupService fetchScanResult]_block_invoke
+ ___34-[HDSSetupService fetchScanResult]_block_invoke.cold.1
+ ___35-[HDSSetupService fetchScanResult:]_block_invoke
+ ___35-[HDSSetupService fetchScanResult:]_block_invoke.cold.1
+ ___35-[HDSSetupService fetchScanResult:]_block_invoke_2
+ ___35-[HDSSetupService fetchScanResult:]_block_invoke_2.cold.1
+ ___35-[HDSSetupSession resetWiFiPicker:]_block_invoke
+ ___35-[HDSSetupSession resetWiFiPicker:]_block_invoke.cold.1
+ ___35-[HDSSetupSession wiFiAcknowledged]_block_invoke
+ ___35-[HDSSetupSession wiFiAcknowledged]_block_invoke.cold.1
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.654
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.654.cold.1
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.676
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_3
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_3.cold.1
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_3.cold.2
+ ___39-[HDSSetupSession _runHomeKitUserInput]_block_invoke.cold.7
+ ___39-[HDSSetupSession _runHomePodScanFetch]_block_invoke
+ ___39-[HDSSetupSession _runHomePodScanFetch]_block_invoke_2
+ ___39-[HDSSetupSession _runHomePodScanFetch]_block_invoke_2.cold.1
+ ___39-[HDSSetupSession _runHomePodScanFetch]_block_invoke_2.cold.2
+ ___39-[HDSSetupSession resetToHomeSelection]_block_invoke
+ ___39-[HDSSetupSession resetToHomeSelection]_block_invoke.cold.1
+ ___40-[HDSSetupSession wifiPasswordSelected:]_block_invoke
+ ___40-[HDSSetupSession wifiPasswordSelected:]_block_invoke.cold.1
+ ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_12
+ ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_12.cold.1
+ ___41-[HDSSetupSession createNewHomeWithName:]_block_invoke
+ ___41-[HDSSetupSession createNewHomeWithName:]_block_invoke.cold.1
+ ___43-[HDSSetupSession createHomeInSameLocation]_block_invoke
+ ___43-[HDSSetupSession createHomeInSameLocation]_block_invoke.cold.1
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_16
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_16.cold.1
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_17
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_17.cold.1
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_18
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_18.cold.1
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_19
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_19.cold.1
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_20
+ ___44-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_20.cold.1
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.10
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.11
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.12
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.4
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.5
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.6
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.7
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.8
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.9
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_3
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_4
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_4.cold.1
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_5
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_5.cold.1
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_5.cold.2
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_5.cold.3
+ ___46-[HDSSetupSession fetchHomePodLoggingProfile:]_block_invoke
+ ___46-[HDSSetupSession fetchHomePodLoggingProfile:]_block_invoke_2
+ ___46-[HDSSetupSession fetchHomePodLoggingProfile:]_block_invoke_2.cold.1
+ ___46-[HDSSetupSession fetchHomePodLoggingProfile:]_block_invoke_2.cold.2
+ ___46-[HDSSetupSession fetchHomePodLoggingProfile:]_block_invoke_2.cold.3
+ ___46-[HDSSetupSession fetchHomePodLoggingProfile:]_block_invoke_2.cold.4
+ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke
+ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke_2
+ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke_3
+ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke_3.cold.1
+ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke_4
+ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke_4.cold.1
+ ___48-[HDSSetupSession acceptSelectSameWrongLocation]_block_invoke
+ ___48-[HDSSetupSession acceptSelectSameWrongLocation]_block_invoke.cold.1
+ ___49-[HDSDeviceOperationHomeKitSetup selectHomeName:]_block_invoke
+ ___49-[HDSDeviceOperationHomeKitSetup selectHomeName:]_block_invoke.cold.1
+ ___53-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_3.cold.2
+ ___53-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_4
+ ___53-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_5
+ ___53-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_5.cold.1
+ ___54-[HDSDeviceOperationHomeKitSetup resetToHomeSelection]_block_invoke
+ ___54-[HDSDeviceOperationHomeKitSetup resetToHomeSelection]_block_invoke.cold.1
+ ___55-[HDSDeviceOperationHomeKitSetup _runHomeKitSetupRoom:]_block_invoke_2.cold.2
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2.cold.1
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2.cold.10
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2.cold.2
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2.cold.3
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2.cold.4
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2.cold.5
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2.cold.6
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2.cold.7
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2.cold.8
+ ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2.cold.9
+ ___58-[HDSDeviceOperationHomeKitSetup createHomeInSameLocation]_block_invoke
+ ___58-[HDSDeviceOperationHomeKitSetup createHomeInSameLocation]_block_invoke.cold.1
+ ___58-[HDSSetupService _handleHomeScanRequest:responseHandler:]_block_invoke
+ ___58-[HDSSetupService _handleHomeScanRequest:responseHandler:]_block_invoke_2
+ ___58-[HDSSetupService _handleHomeScanRequest:responseHandler:]_block_invoke_2.cold.1
+ ___58-[HDSSetupService _handleHomeScanRequest:responseHandler:]_block_invoke_3
+ ___61-[HDSDeviceOperationHomeKitSetup _runHomeKitAddHomeWithName:]_block_invoke
+ ___61-[HDSDeviceOperationHomeKitSetup _runHomeKitAddHomeWithName:]_block_invoke_2
+ ___61-[HDSDeviceOperationHomeKitSetup _runHomeKitAddHomeWithName:]_block_invoke_2.cold.1
+ ___63-[HDSDeviceOperationHomeKitSetup acceptSelectSameWrongLocation]_block_invoke
+ ___63-[HDSDeviceOperationHomeKitSetup acceptSelectSameWrongLocation]_block_invoke.cold.1
+ ___64-[HDSSetupSession homeKitStartHomeNameCreation:hasNameConflict:]_block_invoke
+ ___64-[HDSSetupSession homeKitStartHomeNameCreation:hasNameConflict:]_block_invoke.cold.1
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.503
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.503.cold.1
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.503.cold.2
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.503.cold.3
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1804
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1805
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1805.cold.1
+ ___CoreWifiLibrary_block_invoke
+ ___block_descriptor_40_e8_32s_e21_v20?0"NSString"8B16ls32l8
+ ___block_descriptor_40_e8_32s_e29_v32?0"NSDictionary"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e31_v24?0"CWFNetworkProfile"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e39_v24?0"HMHomeNetworkInfo"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e58_v40?0"NSString"8"NSString"16"ACAccount"24"NSString"32ls32l8
+ ___block_descriptor_42_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e30_v32?0"CWFScanResult"8Q16^B24ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e28_v24?0"HMRoom"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e18_v16?0"NSString"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e29_v24?0"NSError"8"NSArray"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e33_v28?0B8"NSString"12"NSError"20ls32l8r48l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8r64l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.1009
+ ___block_literal_global.1337
+ ___block_literal_global.1341
+ ___block_literal_global.1353
+ ___block_literal_global.1357
+ ___block_literal_global.1362
+ ___block_literal_global.1366
+ ___block_literal_global.1378
+ ___block_literal_global.1384
+ ___block_literal_global.1391
+ ___block_literal_global.1395
+ ___block_literal_global.1399
+ ___block_literal_global.1409
+ ___block_literal_global.1413
+ ___block_literal_global.1659
+ ___block_literal_global.3543
+ ___block_literal_global.3547
+ ___block_literal_global.3551
+ ___block_literal_global.3554
+ ___block_literal_global.3557
+ ___block_literal_global.3565
+ ___block_literal_global.3569
+ ___block_literal_global.3583
+ ___block_literal_global.3587
+ ___block_literal_global.3600
+ ___block_literal_global.3603
+ ___block_literal_global.3606
+ ___block_literal_global.3610
+ ___block_literal_global.3614
+ ___block_literal_global.3632
+ ___block_literal_global.3644
+ ___block_literal_global.3648
+ ___block_literal_global.3651
+ ___block_literal_global.3654
+ ___block_literal_global.3658
+ ___block_literal_global.3663
+ ___block_literal_global.3667
+ ___block_literal_global.3672
+ ___block_literal_global.3676
+ ___block_literal_global.3679
+ ___block_literal_global.3682
+ ___block_literal_global.3686
+ ___block_literal_global.3689
+ ___block_literal_global.3693
+ ___block_literal_global.3696
+ ___block_literal_global.3699
+ ___block_literal_global.3703
+ ___block_literal_global.3707
+ ___block_literal_global.3808
+ ___block_literal_global.659
+ ___block_literal_global.700
+ ___block_literal_global.772
+ ___block_literal_global.936
+ ___block_literal_global.940
+ ___block_literal_global.947
+ ___block_literal_global.953
+ ___block_literal_global.956
+ ___block_literal_global.960
+ ___block_literal_global.972
+ ___initValAVAudioSessionCategoryAmbient_block_invoke
+ ___initValAVAudioSessionCategoryAmbient_block_invoke.cold.1
+ ___initValAVAudioSessionInterruptionNotification_block_invoke
+ ___initValAVAudioSessionInterruptionNotification_block_invoke.cold.1
+ ___initValAVAudioSessionModeDefault_block_invoke
+ ___initValAVAudioSessionModeDefault_block_invoke.cold.1
+ ___initValHMAccessoryCategoryTypeAppleTV_block_invoke
+ ___initValHMAccessoryCategoryTypeAppleTV_block_invoke.cold.1
+ ___initValHMAccessoryCategoryTypeHomePod_block_invoke
+ ___initValHMAccessoryCategoryTypeHomePod_block_invoke.cold.1
+ ___initValTRActivationOperationErrorKey_block_invoke
+ ___initValTRActivationOperationErrorKey_block_invoke.cold.1
+ ___initValTRActivationOperationIsActivatedKey_block_invoke
+ ___initValTRActivationOperationIsActivatedKey_block_invoke.cold.1
+ ___initValTRAuthenticationOperationErrorKey_block_invoke
+ ___initValTRAuthenticationOperationErrorKey_block_invoke.cold.1
+ ___initValTRAuthenticationOperationUnauthenticatedServicesKey_block_invoke
+ ___initValTRAuthenticationOperationUnauthenticatedServicesKey_block_invoke.cold.1
+ ___initValTROperationErrorDomain_block_invoke
+ ___initValTROperationErrorDomain_block_invoke.cold.1
+ ___initValTRSetupConfigurationOperationNeedsNetworkKey_block_invoke
+ ___initValTRSetupConfigurationOperationNeedsNetworkKey_block_invoke.cold.1
+ ___initValTRSetupConfigurationOperationUnauthenticatedServicesKey_block_invoke
+ ___initValTRSetupConfigurationOperationUnauthenticatedServicesKey_block_invoke.cold.1
+ ___initValTRSetupConfigurationOperationUseAIDAKey_block_invoke
+ ___initValTRSetupConfigurationOperationUseAIDAKey_block_invoke.cold.1
+ ___initValkAccountDataclassHome_block_invoke
+ ___initValkAccountDataclassHome_block_invoke.cold.1
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_HomeDeviceSetup
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HomeDeviceSetup
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HomeDeviceSetup
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HomeDeviceSetup
+ _classCWFInterface
+ _classCWFNetworkSignature
+ _classCWFScanParameters
+ _getCWFInterfaceClass
+ _getCWFNetworkSignatureClass
+ _getCWFScanParametersClass
+ _initCWFInterface
+ _initCWFInterface.cold.1
+ _initCWFNetworkSignature
+ _initCWFNetworkSignature.cold.1
+ _initCWFScanParameters
+ _initCWFScanParameters.cold.1
+ _kDefaultsKey_ForceFailWifi
+ _kDefaultsKey_ForceHH2
+ _kDefaultsKey_ForceHomeLocationFlow
+ _kDefaultsKey_NumberOfWiFIRetries
+ _kDefaultsKey_ShowWiFiSummary
+ _kDefaultsKey_SysDropHalfwayError
+ _objc_msgSend$BSSID
+ _objc_msgSend$RSSI
+ _objc_msgSend$_handleHomeScanRequest:responseHandler:
+ _objc_msgSend$_runHH2Upsell
+ _objc_msgSend$_runHomeKitAddHomeWithName:
+ _objc_msgSend$_runHomePodScanFetch
+ _objc_msgSend$_runWiFiPicker
+ _objc_msgSend$aa_altDSID
+ _objc_msgSend$aa_appleAccountWithAltDSID:
+ _objc_msgSend$acceptSelectSameWrongLocation
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$binaryIPv4NetworkSignature
+ _objc_msgSend$binaryIPv6NetworkSignature
+ _objc_msgSend$channel
+ _objc_msgSend$checkName:inHome:withValidationOptions:completionHandler:
+ _objc_msgSend$createHomeInSameLocation
+ _objc_msgSend$createScanParameters
+ _objc_msgSend$createdNewHomeInSetupFlow
+ _objc_msgSend$dataTaskWithURL:completionHandler:
+ _objc_msgSend$dictForNetworkName:
+ _objc_msgSend$fetchAltDSIDAccount
+ _objc_msgSend$fetchHomePodLoggingProfile:
+ _objc_msgSend$fetchScanResult:
+ _objc_msgSend$fetchTermsInfo
+ _objc_msgSend$filterNetworksForHomePod:
+ _objc_msgSend$forceFailWiFi
+ _objc_msgSend$forceHH2Upsell
+ _objc_msgSend$forceHomeLocationCreationFlow
+ _objc_msgSend$getPrimaryResidentNetworkInfoWithCompletion:
+ _objc_msgSend$homeHubState
+ _objc_msgSend$homeLocationStatus
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithIPv4NetworkSignatureBytes:IPv6NetworkSignatureBytes:
+ _objc_msgSend$isOpen
+ _objc_msgSend$knownNetworkProfilesInSameLanAsNetworkName:
+ _objc_msgSend$knownNetworkProfilesWithNetworkSignature:
+ _objc_msgSend$lastSSIDUsed
+ _objc_msgSend$networkName
+ _objc_msgSend$numberOfWiFiRetries
+ _objc_msgSend$performScanWithParameters:reply:
+ _objc_msgSend$resetHomeSelection
+ _objc_msgSend$resetToHomeSelection
+ _objc_msgSend$scanResultToDict:
+ _objc_msgSend$scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:
+ _objc_msgSend$selectHomeName:
+ _objc_msgSend$setAcceptableCacheAge:
+ _objc_msgSend$setExclude6GChannels:
+ _objc_msgSend$setMergeScanResults:
+ _objc_msgSend$setOperationType:
+ _objc_msgSend$setPromptForHH2UpsellHandler:
+ _objc_msgSend$setPromptForHomeInSameLocationHandler:
+ _objc_msgSend$setPromptForHomeNameCreationHandler:
+ _objc_msgSend$setPromptForWiFiFailedHandler:
+ _objc_msgSend$setPromptForWiFiPickerHandler:
+ _objc_msgSend$setPromptForWiFiSummaryHandler:
+ _objc_msgSend$setPromptToShareSettingsV2Handler:
+ _objc_msgSend$setSortByAutoJoinPreference:
+ _objc_msgSend$setTime
+ _objc_msgSend$shareSettingsAgreed
+ _objc_msgSend$sharedSession
+ _objc_msgSend$startHomeNameCreation:hasNameConflict:
+ _objc_msgSend$sysDropForceErrorHalfwayEnabled
+ _objc_msgSend$wiFiAcknowledged
+ _objc_msgSend$wiFiInfo
+ _objc_msgSend$wiFiRetry
+ _objc_msgSend$wiFiSelected:
+ _softLinkOnceAVAudioSessionCategoryAmbient
+ _softLinkOnceAVAudioSessionInterruptionNotification
+ _softLinkOnceAVAudioSessionModeDefault
+ _softLinkOnceHMAccessoryCategoryTypeAppleTV
+ _softLinkOnceHMAccessoryCategoryTypeHomePod
+ _softLinkOnceTRActivationOperationErrorKey
+ _softLinkOnceTRActivationOperationIsActivatedKey
+ _softLinkOnceTRAuthenticationOperationErrorKey
+ _softLinkOnceTRAuthenticationOperationUnauthenticatedServicesKey
+ _softLinkOnceTROperationErrorDomain
+ _softLinkOnceTRSetupConfigurationOperationNeedsNetworkKey
+ _softLinkOnceTRSetupConfigurationOperationUnauthenticatedServicesKey
+ _softLinkOnceTRSetupConfigurationOperationUseAIDAKey
+ _softLinkOncekAccountDataclassHome
- -[HDSSetupSession fetchHomePodLoggingProfile]
- -[HDSSetupSession fetchHomePodLoggingProfile].cold.1
- -[HDSSetupSession fetchHomePodLoggingProfile].cold.2
- -[HDSSetupSession fetchHomePodLoggingProfile].cold.3
- -[HDSSetupSession sysDropProfileInstalled]
- GCC_except_table274
- GCC_except_table332
- GCC_except_table8
- _OBJC_IVAR_$_HDSSetupSession._psgHelper
- _OBJC_IVAR_$_HDSSetupSession._selectedHomeHasPrimaryResident
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1547
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1547.cold.1
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.334
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.336
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.336.cold.1
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.634
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.634.cold.1
- ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke.cold.1
- ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke.cold.2
- ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.cold.2
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke.cold.1
- ___53-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke.cold.3
- ___53-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke.cold.4
- ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke.cold.1
- ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke.cold.10
- ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke.cold.2
- ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke.cold.3
- ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke.cold.4
- ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke.cold.5
- ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke.cold.6
- ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke.cold.7
- ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke.cold.8
- ___57-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke.cold.9
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.491
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.491.cold.1
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.491.cold.2
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.491.cold.3
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1694
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1695
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1695.cold.1
- ___block_descriptor_41_e8_32s_e28_v24?0"HMRoom"8"NSError"16ls32l8
- ___block_literal_global.1261
- ___block_literal_global.1265
- ___block_literal_global.1277
- ___block_literal_global.1281
- ___block_literal_global.1286
- ___block_literal_global.1290
- ___block_literal_global.1302
- ___block_literal_global.1308
- ___block_literal_global.1315
- ___block_literal_global.1319
- ___block_literal_global.1323
- ___block_literal_global.1333
- ___block_literal_global.1549
- ___block_literal_global.3270
- ___block_literal_global.3274
- ___block_literal_global.3278
- ___block_literal_global.3286
- ___block_literal_global.3290
- ___block_literal_global.3304
- ___block_literal_global.3308
- ___block_literal_global.3321
- ___block_literal_global.3325
- ___block_literal_global.3329
- ___block_literal_global.3333
- ___block_literal_global.3350
- ___block_literal_global.3362
- ___block_literal_global.3366
- ___block_literal_global.3372
- ___block_literal_global.3377
- ___block_literal_global.3381
- ___block_literal_global.3386
- ___block_literal_global.3401
- ___block_literal_global.3405
- ___block_literal_global.3506
- ___block_literal_global.639
- ___block_literal_global.760
- ___block_literal_global.891
- ___block_literal_global.895
- ___block_literal_global.902
- ___block_literal_global.911
- ___block_literal_global.934
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_HomeDeviceSetup
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_HomeDeviceSetup
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_HomeDeviceSetup
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_HomeDeviceSetup
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_HomeDeviceSetup
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_HomeDeviceSetup
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_HomeDeviceSetup
- _objc_msgSend$dataWithContentsOfURL:
- _objc_msgSend$fetchHomePodLoggingProfile
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "### Get product name failed\n"
+ "### Get product version failed\n"
+ "### HomePod Setup Error with extra info: %@, %{error}, %@\n"
+ "### No device product name: %#m\n"
+ "### No device product version: %#m\n"
+ "(1) HomeKitPrimarySSIDFetchV2 Cached result %@ | Network Name: %@\n"
+ "(2) Cached v2 network profiles %@\n"
+ "(3) Finalized Networks %@\n"
+ "(4) Best network %@\n"
+ "(5) Preferred Network found, updating WiFi Config for %@\n"
+ "-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_16"
+ "-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_17"
+ "-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_18"
+ "-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_19"
+ "-[CLISetupInteractor setCLIPromptsForStates]_block_invoke_20"
+ "-[HDSDeviceOperationHomeKitSetup _runHomeKitAddHomeWithName:]_block_invoke_2"
+ "-[HDSDeviceOperationHomeKitSetup acceptSelectSameWrongLocation]_block_invoke"
+ "-[HDSDeviceOperationHomeKitSetup createHomeInSameLocation]_block_invoke"
+ "-[HDSDeviceOperationHomeKitSetup resetToHomeSelection]_block_invoke"
+ "-[HDSDeviceOperationHomeKitSetup selectHomeName:]_block_invoke"
+ "-[HDSSetupService _handleHomeScanRequest:responseHandler:]"
+ "-[HDSSetupService _handleHomeScanRequest:responseHandler:]_block_invoke_2"
+ "-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke_2"
+ "-[HDSSetupService _handleSessionStarted:]_block_invoke_12"
+ "-[HDSSetupService fetchScanResult:]"
+ "-[HDSSetupService fetchScanResult:]_block_invoke"
+ "-[HDSSetupService fetchScanResult:]_block_invoke_2"
+ "-[HDSSetupService fetchScanResult]_block_invoke"
+ "-[HDSSetupService setTime]"
+ "-[HDSSetupService setTime]_block_invoke"
+ "-[HDSSetupSession _reportErrorWithExtaInfo:label:dict:]"
+ "-[HDSSetupSession _runHH2Upsell]"
+ "-[HDSSetupSession _runHH2Upsell]_block_invoke"
+ "-[HDSSetupSession _runHH2Upsell]_block_invoke_2"
+ "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_4"
+ "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_5"
+ "-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_3"
+ "-[HDSSetupSession _runHomePodScanFetch]"
+ "-[HDSSetupSession _runHomePodScanFetch]_block_invoke_2"
+ "-[HDSSetupSession _runWiFiPassword]"
+ "-[HDSSetupSession _runWiFiPicker]"
+ "-[HDSSetupSession _runWiFiPicker]_block_invoke_2"
+ "-[HDSSetupSession _runWiFiSummaryCard]"
+ "-[HDSSetupSession _startSysDropLoggingProfileRequest]_block_invoke_5"
+ "-[HDSSetupSession acceptSelectSameWrongLocation]_block_invoke"
+ "-[HDSSetupSession createHomeInSameLocation]_block_invoke"
+ "-[HDSSetupSession createNewHomeWithName:]_block_invoke"
+ "-[HDSSetupSession fetchHomePodLoggingProfile:]"
+ "-[HDSSetupSession fetchHomePodLoggingProfile:]_block_invoke_2"
+ "-[HDSSetupSession homeKitStartHomeNameCreation:hasNameConflict:]_block_invoke"
+ "-[HDSSetupSession resetToHomeSelection]_block_invoke"
+ "-[HDSSetupSession resetWiFiPicker:]_block_invoke"
+ "-[HDSSetupSession validateHomeName:completion:]"
+ "-[HDSSetupSession validateHomeName:completion:]_block_invoke_3"
+ "-[HDSSetupSession validateHomeName:completion:]_block_invoke_4"
+ "-[HDSSetupSession wiFiAcknowledged]_block_invoke"
+ "-[HDSSetupSession wiFiRetry]_block_invoke"
+ "-[HDSSetupSession wiFiSelected:]_block_invoke"
+ "-[HDSSetupSession wifiPasswordSelected:]_block_invoke"
+ "/System/Library/PrivateFrameworks/CoreWifi.framework/CoreWifi"
+ "<%@> <%@;%@;%@>"
+ "@\"CWFInterface\""
+ "@\"HMHomeNetworkInfo\""
+ "@\"NSTimer\""
+ "Add home with name succeeded\n"
+ "BSSID"
+ "CLI mode detected, skipping to selected state\n"
+ "CLISetupInteractor: promptForHH2UpsellHandler\n"
+ "CLISetupInteractor: promptForWiFiFailedHandler\n"
+ "CLISetupInteractor: promptForWiFiPickerHandler\n"
+ "CLISetupInteractor: promptForWiFiSummaryHandler\n"
+ "CLISetupInteractor: promptToShareSettingsV2Handler\n"
+ "CWFInterface"
+ "CWFNetworkSignature"
+ "CWFScanParameters"
+ "CmdHomeDeviceSetupNoUI promptToShareSettingsV2Handler\n"
+ "Creating Custom Home\n"
+ "DidUsePhonesNetwork %s\n"
+ "Failed to fetch profile %@"
+ "FakeWiFiError"
+ "Force Home flow default %s\n"
+ "ForceFailHalfway"
+ "HDSMessageKeyWiFiPickerScanFetch\n"
+ "HDSMessageKeyWiFiPickerScanFetch response %@\n"
+ "HH1EOL"
+ "HH2 Upsell Start\n"
+ "HH2Upsell"
+ "HPProfileFetch"
+ "HomeKitPrimarySSIDFetchV2 0 network profiles\n"
+ "HomeKitPrimarySSIDFetchV2 Cached skipping since network is null\n"
+ "HomeKitPrimarySSIDFetchV2 IP Network Signature query results %@\n"
+ "HomeKitPrimarySSIDFetchV2 Starting Cached Fetch\n"
+ "HomeKitPrimarySSIDFetchV2 network name query results %@\n"
+ "HomeKitPrimarySSIDFetchV2 skipping Network Name fetch\n"
+ "HomeKitPrimarySSIDFetchV2 wifi interface nil\n"
+ "HomePod Scan send request: %##.32@\n"
+ "HomePod needsHH2: %s | %#m\n"
+ "Match found for %@\n"
+ "My Home"
+ "Network Improvements Scan done, duration %f | results %d"
+ "Network Improvements Scan failed %@"
+ "Network Improvements results:\n %@"
+ "Network Improvements starting scan"
+ "NetworkSelection"
+ "No Data when profile fetch"
+ "No Scan results\n"
+ "No Selected SSID, defaulting to phone's\n"
+ "Password fetch for %@ | success %s\n"
+ "Primary Network Cached fetch failed %@\n"
+ "ProductName"
+ "RSSI"
+ "Reachable Network Match found for %@\n"
+ "Refetched filtered scan results %@\n"
+ "Resetting WiFi picker\n"
+ "Room already exists\n"
+ "SSID selected = %@"
+ "Scan Finished, Response %@\n"
+ "Scan Refetched"
+ "Scan result %@\n"
+ "Scan results exist\n"
+ "ScanFetch"
+ "Scanning for WiFi networks...\n"
+ "Starting Custom Home Creation\n"
+ "SysDropHalfwayError"
+ "T@?,C,N,V_promptForHH2UpsellHandler"
+ "T@?,C,N,V_promptForHomeInSameLocationHandler"
+ "T@?,C,N,V_promptForHomeNameCreationHandler"
+ "T@?,C,N,V_promptForWiFiFailedHandler"
+ "T@?,C,N,V_promptForWiFiPasswordHandler"
+ "T@?,C,N,V_promptForWiFiPickerHandler"
+ "T@?,C,N,V_promptForWiFiSummaryHandler"
+ "T@?,C,N,V_promptToShareSettingsV2Handler"
+ "TB,R,V_createdNewHomeInSetupFlow"
+ "User Agrees to create Home in same location\n"
+ "User Agrees to select Home in wrong location\n"
+ "User acknowledged selected SSID"
+ "User agrees to create Home in same location as another Home\n"
+ "User agrees to selected home in same location as another\n"
+ "User chose to reset to Home selection\n"
+ "User has chosen to retry wifi config"
+ "User selected Home, location status %d\n"
+ "User selected home name %@\n"
+ "User selected reset to Home Selection\n"
+ "Waiting for User to consent to selecting Home in wrong location\n"
+ "Waiting for User to input Home Name\n"
+ "WiFi Password not done yet (%d)\n"
+ "WiFi Password prompting user\n"
+ "WiFi Password skipping check with no prompt handler\n"
+ "WiFi Password user agreed\n"
+ "WiFi Picker not done yet (%d)\n"
+ "WiFi Picker picked\n"
+ "WiFi Picker prompting user\n"
+ "WiFi Picker skipping check with no prompt handler\n"
+ "WiFi Summary acknowledged\n"
+ "WiFi Summary prompting user, show picker %s\n"
+ "WiFi Summary skipping check with no prompt handler\n"
+ "WiFi password selected\n"
+ "WiFi retry picker count %d\n"
+ "WiFi setup using CWS, network %@\n"
+ "WiFi setup using Picker, network %@\n"
+ "WiFi setup using Preferred Home Network %@\n"
+ "WiFiPassword"
+ "WiFiPicker"
+ "WiFiSetup2"
+ "WiFiSummary"
+ "You cannot setup a HomePod while in HH1\n"
+ "_createdNewHomeInSetupFlow"
+ "_deviceProductName"
+ "_deviceProductVersion"
+ "_didDoV3Terms"
+ "_doHomePodScan"
+ "_finishedFinal"
+ "_forceFailEarlyState"
+ "_forceFailHalfwayState"
+ "_handleHomeScanRequest:responseHandler:"
+ "_hasExistingHomePodInAccount = %s _hasExistingHomePodInSelectedRoom = %s\n"
+ "_hh2UpsellState"
+ "_homeAccessoryCategories"
+ "_homeHubStatusSelectedHome"
+ "_homeHubStatusSelectedHome = %d\n"
+ "_homeLocationState"
+ "_homePodScanResults"
+ "_homePodScanResults: %@ | %#m\n"
+ "_homePodSupportsWiFiPicker"
+ "_homePodSupportsWiFiPicker: %s | %#m\n"
+ "_joinPrimaryNetworkCrossReference"
+ "_numberOfAppleMediaAccessoriesInHome"
+ "_phonesWiFiSSID"
+ "_preferredHomeNetworkNames"
+ "_preferredNetworkState"
+ "_primaryResidentNetwork"
+ "_promptForHH2UpsellHandler"
+ "_promptForHomeInSameLocationHandler"
+ "_promptForHomeNameCreationHandler"
+ "_promptForWiFiFailedHandler"
+ "_promptForWiFiPasswordHandler"
+ "_promptForWiFiPickerHandler"
+ "_promptForWiFiSummaryHandler"
+ "_promptToShareSettingsV2Handler"
+ "_reachableHomePodScanResults"
+ "_reportErrorWithExtaInfo:label:dict:"
+ "_retryPickerCount"
+ "_retryPickerCount %d | limit %d\n"
+ "_runHH2Upsell"
+ "_runHH2Upsell: error %@\n"
+ "_runHH2Upsell: isHH1 %s \n"
+ "_runHH2Upsell: prompting upsell, Account is in HH1\n"
+ "_runHH2Upsell: skipping\n"
+ "_runHomeKitAddHomeWithName:"
+ "_runHomePodScanFetch"
+ "_runWiFiPassword"
+ "_runWiFiPicker"
+ "_runWiFiSummaryCard"
+ "_scanInProgress"
+ "_scanResults"
+ "_scanTimer"
+ "_selectedHomeHasResidentDevice"
+ "_selectedHomeHasResidentDevice = %s\n"
+ "_showWiFiPicker"
+ "_ssidsToSelectFrom"
+ "_timeSet"
+ "_upsellHH2"
+ "_userCreateHomeInSameLocation"
+ "_userCreatedHomeName"
+ "_userSelectHomeWrongLocation"
+ "_wifiInterface"
+ "_wifiPassword"
+ "_wifiPasswordSet"
+ "_wifiPasswordState"
+ "_wifiPicked"
+ "_wifiPickerState"
+ "_wifiSSIDAcknowledged"
+ "_wifiScanFetchState"
+ "_wifiSelectedSSID"
+ "_wifiSummaryState"
+ "aa_altDSID"
+ "aa_appleAccountWithAltDSID:"
+ "acceptSelectSameWrongLocation"
+ "accessory:didUpdateHH1EOLEnabled:"
+ "accessoryDidSetHasOnboardedForAdaptiveTemperatureAutomations:"
+ "accessoryDidSetHasOnboardedForCleanEnergyAutomation:"
+ "addObjectsFromArray:"
+ "arrayWithCapacity:"
+ "binaryIPv4NetworkSignature"
+ "binaryIPv6NetworkSignature"
+ "checkIfExistingHome:"
+ "checkName:inHome:withValidationOptions:completionHandler:"
+ "com.apple.homedevicesetup.sysdrop.prod"
+ "createErrorDictionary:ssid:"
+ "createHomeInSameLocation"
+ "createNewHomeWithName:"
+ "createScanParameters"
+ "createdNewHomeInSetupFlow"
+ "dataTaskWithURL:completionHandler:"
+ "dictForNetworkName:"
+ "fetchAltDSIDAccount"
+ "fetchHomePodLoggingProfile:"
+ "fetchScanResult"
+ "fetchScanResult:"
+ "fetchTermsInfo"
+ "filterNetworksForHomePod:"
+ "forceFailWiFi"
+ "forceHH2"
+ "forceHH2Upsell"
+ "forceHomeLocationCreationFlow"
+ "forceHomeLocationFlow"
+ "forceShowWiFiSummary"
+ "getPrimaryResidentNetworkInfoWithCompletion:"
+ "hds_e_t"
+ "hds_hp_scn_bssid"
+ "hds_hp_scn_ch"
+ "hds_hp_scn_io"
+ "hds_hp_scn_nn"
+ "hds_hp_scn_pw"
+ "hds_hp_scn_re"
+ "hds_hp_scn_res"
+ "hds_hp_scn_rssi"
+ "hds_hp_scn_se_n"
+ "hds_hp_scn_ssid"
+ "hds_n_h2"
+ "hds_w_s"
+ "homeCategory"
+ "homeHubState"
+ "homeHubStatusSelectedHome"
+ "homeKitStartHomeNameCreation:hasNameConflict:"
+ "homeLocationState"
+ "homeLocationStatus"
+ "home_selection"
+ "hp_pn"
+ "initWithDictionary:"
+ "initWithIPv4NetworkSignatureBytes:IPv6NetworkSignatureBytes:"
+ "isOpen"
+ "joinPrimaryNetworkCrossReference"
+ "kCUMultiStateWaitSelectHomeWrongLocation"
+ "kCUMultiStateWaitUserCreateHomeName"
+ "knownNetworkProfilesInSameLanAsNetworkName:"
+ "knownNetworkProfilesWithNetworkSignature:"
+ "lastSSIDUsed"
+ "networkName"
+ "numberOfAppleMediaAccessoriesInHome"
+ "numberOfWiFiRetries"
+ "performScanWithParameters:reply:"
+ "preferredNetworkState"
+ "profile data missing"
+ "promptForHH2UpsellHandler"
+ "promptForHomeInSameLocationHandler"
+ "promptForHomeNameCreationHandler"
+ "promptForWiFiFailedHandler"
+ "promptForWiFiPasswordHandler"
+ "promptForWiFiPickerHandler"
+ "promptForWiFiSummaryHandler"
+ "promptToShareSettingsV2Handler"
+ "resetHomeSelection"
+ "resetToHomeSelection"
+ "resetWiFiPicker:"
+ "retryRetryAttempt"
+ "scanResultToDict:"
+ "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
+ "selectHomeName:"
+ "setAcceptableCacheAge:"
+ "setExclude6GChannels:"
+ "setMergeScanResults:"
+ "setOperationType:"
+ "setPromptForHH2UpsellHandler:"
+ "setPromptForHomeInSameLocationHandler:"
+ "setPromptForHomeNameCreationHandler:"
+ "setPromptForWiFiFailedHandler:"
+ "setPromptForWiFiPasswordHandler:"
+ "setPromptForWiFiPickerHandler:"
+ "setPromptForWiFiSummaryHandler:"
+ "setPromptToShareSettingsV2Handler:"
+ "setSortByAutoJoinPreference:"
+ "setTime"
+ "setupEngineTerminate"
+ "setupUnderlyingErrorCode5"
+ "setupUnderlyingErrorDomain5"
+ "sharedSession"
+ "showWiFiSummary"
+ "startHomeNameCreation:hasNameConflict:"
+ "sysDropForceErrorHalfwayEnabled"
+ "sysdrop_carry"
+ "userAtHomeLocation:"
+ "v20@?0@\"NSString\"8B16"
+ "v24@?0@\"CWFNetworkProfile\"8^B16"
+ "v24@?0@\"HMHomeNetworkInfo\"8@\"NSError\"16"
+ "v24@?0@\"NSError\"8@\"NSArray\"16"
+ "v28@?0B8@\"NSString\"12@\"NSError\"20"
+ "v32@?0@\"CWFScanResult\"8Q16^B24"
+ "v32@?0@\"NSDictionary\"8Q16^B24"
+ "v40@?0@\"NSString\"8@\"NSString\"16@\"ACAccount\"24@\"NSString\"32"
+ "validateHomeName error %@ | conflict name %@\n"
+ "validateHomeName start\n"
+ "validateHomeName success\n"
+ "validateHomeName:completion:"
+ "validateHomename success %s, hasNameConflict %s\n"
+ "wiFiAcknowledged"
+ "wiFiInfo"
+ "wiFiRetry"
+ "wiFiSelected:"
+ "wifiPasswordSelected:"
+ "wifiRetry"
+ "wp_hp_s_r"
+ "wp_s_f"
+ "wr_w_p_c"
- "-[HDSSetupService _handlePreAuthRequest:responseHandler:]_block_invoke"
- "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke"
- "-[HDSSetupSession fetchHomePodLoggingProfile]"
- "@\"HDSPSGHelper\""
- "DidUsePhones %s\n"
- "WiFiDisabled"
- "WiFiSetupNoInternet"
- "_hasExistingHomePodInAccount = %s\n"
- "_psgHelper"
- "_selectedHomeHasPrimaryResident"
- "_selectedHomeHasPrimaryResident = %@\n"
- "dataWithContentsOfURL:"
- "fetchHomePodLoggingProfile"
- "hk_browser"
- "passwordForSSID WiFi Info %@\n"
- "sysdrop_external"

```
