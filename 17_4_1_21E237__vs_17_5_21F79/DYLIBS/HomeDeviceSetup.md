## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-217.41.1.0.0
-  __TEXT.__text: 0x51698
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x215c
+217.51.1.0.0
+  __TEXT.__text: 0x53438
+  __TEXT.__auth_stubs: 0xa60
+  __TEXT.__objc_methlist: 0x2294
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x153af
-  __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__oslogstring: 0x3bc
-  __TEXT.__unwind_info: 0xc68
-  __TEXT.__objc_classname: 0x275
-  __TEXT.__objc_methname: 0xa0de
-  __TEXT.__objc_methtype: 0xf2d
-  __TEXT.__objc_stubs: 0x6940
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x1268
-  __DATA_CONST.__objc_classlist: 0x70
+  __TEXT.__cstring: 0x15acf
+  __TEXT.__gcc_except_tab: 0x114
+  __TEXT.__oslogstring: 0x3a7
+  __TEXT.__unwind_info: 0xca8
+  __TEXT.__objc_classname: 0x291
+  __TEXT.__objc_methname: 0xa4ae
+  __TEXT.__objc_methtype: 0xf8c
+  __TEXT.__objc_stubs: 0x6a20
+  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__const: 0x12c0
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6050
-  __DATA_CONST.__objc_selrefs: 0x20b8
+  __DATA_CONST.__objc_const: 0x6368
+  __DATA_CONST.__objc_selrefs: 0x2150
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x238
-  __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x218
-  __AUTH_CONST.__cfstring: 0x3e20
-  __AUTH_CONST.__objc_const: 0x6f0
+  __DATA_CONST.__objc_classrefs: 0x240
+  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_arraydata: 0x210
+  __AUTH_CONST.__cfstring: 0x40a0
+  __AUTH_CONST.__objc_const: 0x780
   __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_dictobj: 0x3c0
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_intobj: 0x1c8
-  __AUTH_CONST.__auth_got: 0x570
-  __AUTH.__objc_data: 0x460
+  __AUTH_CONST.__auth_got: 0x540
+  __AUTH.__objc_data: 0x4b0
   __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0x82c
-  __DATA.__data: 0x960
+  __DATA.__objc_ivar: 0x878
+  __DATA.__data: 0x968
   __DATA.__common: 0x10
-  __DATA.__bss: 0x518
+  __DATA.__bss: 0x510
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1248
-  Symbols:   4706
-  CStrings:  4431
+  Functions: 1278
+  Symbols:   4800
+  CStrings:  4528
 
Symbols:
+ +[HDSDefaults disableNeedsSetup]
+ +[HDSDefaults forceFailiTunesAuth]
+ +[HDSFileTransferService destDirectoryForTargetId:]
+ +[HDSFileTransferService tmpRapportDir]
+ -[HDSDeviceActivationOperation _sendActivationURLRequest:retries:completion:]
+ -[HDSFileTransfer beginSysDropFileTransfer:pathToFile:withCompletion:]
+ -[HDSFileTransferService .cxx_destruct]
+ -[HDSFileTransferService dispatchQueue]
+ -[HDSFileTransferService fileTransferCompletionHandler]
+ -[HDSFileTransferService fileTransferProgressHandler]
+ -[HDSFileTransferService handleSysDropStartFileTransferRequest:responseHandler:]
+ -[HDSFileTransferService init]
+ -[HDSFileTransferService invalidate]
+ -[HDSFileTransferService setDispatchQueue:]
+ -[HDSFileTransferService setFileTransferCompletionHandler:]
+ -[HDSFileTransferService setFileTransferProgressHandler:]
+ -[HDSSetupSession _logiTunesAuthRetryMetrics:durationSeconds:authType:retryAttempt:]
+ -[HDSSetupSession promptForTermsAndConditionsV2Disagree]
+ -[HDSSetupSession setPromptForTermsAndConditionsV2Disagree:]
+ -[SysDropService _runPreflightRPFileTransfer]
+ -[SysDropService _sendSysdiagnosePeerUpdate:inError:]
+ -[SysDropSession _runFileTransferComplete]
+ -[SysDropSession _runReceiveRPFileTransferSysdiagnose]
+ -[SysDropSession _setupHandlers]
+ -[SysDropSession createSysDropRPFileTransferEvent:error:fileTransferProgress:]
+ -[SysDropSession fileTransferCompleted:]
+ -[SysDropSession fileTransferredSysDiagnosePath]
+ -[SysDropSession setSysDropFailed:]
+ -[SysDropSession sysDropFailed]
+ GCC_except_table22
+ GCC_except_table255
+ _CUSetSystemName
+ _HDSErrorDomain
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_HDSFileTransferService
+ _OBJC_IVAR_$_HDSFileTransferService._dispatchQueue
+ _OBJC_IVAR_$_HDSFileTransferService._fileTransferCompletionHandler
+ _OBJC_IVAR_$_HDSFileTransferService._fileTransferProgressHandler
+ _OBJC_IVAR_$_HDSFileTransferService._finished
+ _OBJC_IVAR_$_HDSFileTransferService._rpFileTransferError
+ _OBJC_IVAR_$_HDSFileTransferService._transferItem
+ _OBJC_IVAR_$_HDSSetupSession._canDoV2TermsAndConditions
+ _OBJC_IVAR_$_HDSSetupSession._homePodIsWiFiRetryV2
+ _OBJC_IVAR_$_HDSSetupSession._iTunesAuthRetryAttempt
+ _OBJC_IVAR_$_HDSSetupSession._promptForTermsAndConditionsV2Disagree
+ _OBJC_IVAR_$_SysDropService._companionCanRPFileTransfer
+ _OBJC_IVAR_$_SysDropService._fileTransferSession
+ _OBJC_IVAR_$_SysDropService._targetID
+ _OBJC_IVAR_$_SysDropSession._fileTransferSession
+ _OBJC_IVAR_$_SysDropSession._homePodCanRPFileTransfer
+ _OBJC_IVAR_$_SysDropSession._rpFileCompleteState
+ _OBJC_IVAR_$_SysDropSession._rpFileTransferError
+ _OBJC_IVAR_$_SysDropSession._rpFileTransferState
+ _OBJC_IVAR_$_SysDropSession._setupHandlersState
+ _OBJC_IVAR_$_SysDropSession._sysDropFailed
+ _OBJC_IVAR_$_SysDropSession._transferCompleted
+ _OBJC_IVAR_$_SysDropSession._transferItem
+ _OBJC_METACLASS_$_HDSFileTransferService
+ _TRActivationOperationErrorKeyFunction
+ _TROperationErrorDomainFunction
+ __OBJC_$_CLASS_METHODS_HDSFileTransferService
+ __OBJC_$_CLASS_METHODS_NSData(Hexadecimal|Hexadecimal)
+ __OBJC_$_INSTANCE_METHODS_HDSFileTransferService
+ __OBJC_$_INSTANCE_METHODS_NSData(Hexadecimal|Hexadecimal)
+ __OBJC_$_INSTANCE_VARIABLES_HDSFileTransferService
+ __OBJC_$_PROP_LIST_HDSFileTransferService
+ __OBJC_CLASS_PROTOCOLS_$_HDSFileTransferService
+ __OBJC_CLASS_RO_$_HDSFileTransferService
+ __OBJC_METACLASS_RO_$_HDSFileTransferService
+ ___29-[SysDropService _invalidate]_block_invoke_2
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke.1345
+ ___32-[SysDropSession _setupHandlers]_block_invoke
+ ___32-[SysDropSession _setupHandlers]_block_invoke_2
+ ___32-[SysDropSession _setupHandlers]_block_invoke_3
+ ___32-[SysDropSession _setupHandlers]_block_invoke_4
+ ___33-[SysDropService _sfServiceStart]_block_invoke.42
+ ___33-[SysDropService _sfServiceStart]_block_invoke.44
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.298
+ ___36-[SysDropSession _runSFSessionStart]_block_invoke.42
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.556
+ ___40-[SysDropSession fileTransferCompleted:]_block_invoke
+ ___56-[HDSDeviceActivation _mae_createSessionWithCompletion:]_block_invoke.180
+ ___64-[HDSDeviceActivation _mae_createActivationWithData:completion:]_block_invoke.202
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.427
+ ___70-[HDSFileTransfer beginSysDropFileTransfer:pathToFile:withCompletion:]_block_invoke
+ ___70-[HDSFileTransfer beginSysDropFileTransfer:pathToFile:withCompletion:]_block_invoke_2
+ ___70-[HDSFileTransfer beginSysDropFileTransfer:pathToFile:withCompletion:]_block_invoke_3
+ ___70-[HDSFileTransfer beginSysDropFileTransfer:pathToFile:withCompletion:]_block_invoke_4
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1478
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1479
+ ___77-[HDSDeviceActivationOperation _sendActivationURLRequest:retries:completion:]_block_invoke
+ ___80-[HDSFileTransferService handleSysDropStartFileTransferRequest:responseHandler:]_block_invoke
+ ___80-[HDSFileTransferService handleSysDropStartFileTransferRequest:responseHandler:]_block_invoke_2
+ ___block_descriptor_32_e32_v16?0"RPFileTransferProgress"8l
+ ___block_descriptor_40_e8_32s_e32_v16?0"RPFileTransferProgress"8ls32l8
+ ___block_descriptor_40_e8_32s_e47_v24?0"RPFileTransferItem"8?<v?"NSError">16ls32l8
+ ___block_descriptor_48_e8_32s40s_e40_v24?0"NSError"8"RPFileTransferItem"16ls32l8s40l8
+ ___block_descriptor_76_e8_32s40s48bs56w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8w56l8s40l8s48l8
+ ___block_literal_global.1193
+ ___block_literal_global.1197
+ ___block_literal_global.1209
+ ___block_literal_global.1213
+ ___block_literal_global.1218
+ ___block_literal_global.1222
+ ___block_literal_global.1234
+ ___block_literal_global.1240
+ ___block_literal_global.1247
+ ___block_literal_global.1251
+ ___block_literal_global.1255
+ ___block_literal_global.1265
+ ___block_literal_global.1347
+ ___block_literal_global.2886
+ ___block_literal_global.2890
+ ___block_literal_global.2894
+ ___block_literal_global.2898
+ ___block_literal_global.2902
+ ___block_literal_global.2918
+ ___block_literal_global.2935
+ ___block_literal_global.2939
+ ___block_literal_global.2943
+ ___block_literal_global.2947
+ ___block_literal_global.2964
+ ___block_literal_global.2976
+ ___block_literal_global.2980
+ ___block_literal_global.2986
+ ___block_literal_global.2991
+ ___block_literal_global.2995
+ ___block_literal_global.3015
+ ___block_literal_global.3019
+ ___block_literal_global.3114
+ ___block_literal_global.33
+ ___block_literal_global.561
+ ___block_literal_global.879
+ __unnamed_array_storage.1085
+ __unnamed_array_storage.1086
+ __unnamed_array_storage.1108
+ __unnamed_array_storage.1109
+ __unnamed_array_storage.1119
+ __unnamed_array_storage.1120
+ __unnamed_array_storage.1173
+ __unnamed_array_storage.1174
+ __unnamed_array_storage.1423
+ __unnamed_array_storage.180
+ __unnamed_array_storage.181
+ __unnamed_array_storage.1887
+ __unnamed_array_storage.1888
+ __unnamed_array_storage.1938
+ __unnamed_array_storage.1939
+ __unnamed_array_storage.294
+ __unnamed_array_storage.324
+ __unnamed_array_storage.325
+ __unnamed_array_storage.378
+ __unnamed_array_storage.379
+ __unnamed_array_storage.422
+ __unnamed_array_storage.470
+ __unnamed_array_storage.471
+ __unnamed_array_storage.56
+ __unnamed_array_storage.575
+ __unnamed_array_storage.576
+ __unnamed_array_storage.58
+ __unnamed_array_storage.694
+ __unnamed_array_storage.695
+ __unnamed_array_storage.810
+ __unnamed_array_storage.811
+ __unnamed_array_storage.832
+ __unnamed_array_storage.833
+ __unnamed_array_storage.89
+ __unnamed_array_storage.90
+ _constantValTRActivationOperationErrorKey
+ _constantValTROperationErrorDomain
+ _getTRActivationOperationErrorKey
+ _getTROperationErrorDomain
+ _initValTRActivationOperationErrorKey
+ _initValTROperationErrorDomain
+ _kDefaultsKey_DisableNeedsSetup
+ _kDefaultsKey_FailiTunesRetry
+ _objc_msgSend$_logiTunesAuthRetryMetrics:durationSeconds:authType:retryAttempt:
+ _objc_msgSend$_runFileTransferComplete
+ _objc_msgSend$_runReceiveRPFileTransferSysdiagnose
+ _objc_msgSend$_sendActivationURLRequest:retries:completion:
+ _objc_msgSend$_setupHandlers
+ _objc_msgSend$addItem:
+ _objc_msgSend$authType
+ _objc_msgSend$createSysDropRPFileTransferEvent:error:fileTransferProgress:
+ _objc_msgSend$disableNeedsSetup
+ _objc_msgSend$fileTransferCompleted:
+ _objc_msgSend$handleSysDropStartFileTransferRequest:responseHandler:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$remainingSeconds
+ _objc_msgSend$serialNumber
+ _objc_msgSend$setCanDoTermsAndConditions:
+ _objc_msgSend$setFileTransferCompletionHandler:
+ _objc_msgSend$setFileTransferProgressHandler:
+ _objc_msgSend$setPresentingChildViewController:
+ _objc_msgSend$setProgressHandlerTimeInterval:
+ _objc_msgSend$setSysDropFailed:
+ _objc_msgSend$totalByteCount
+ _objc_msgSend$transferredByteCount
+ _signpostLog.log.167
+ _signpostLog.onceToken.168
- -[HDSDeviceActivationOperation _sendActivationURLRequest:completion:]
- -[HDSSetupService _handleStartFileTransferRequest:responseHandler:]
- -[HDSSetupService _setSystemName:hostname:]
- -[HDSSetupService fetchVoiceProfile:sharedUserId:locale:withCompletion:]
- -[HDSSetupSession _runTransferVoiceProfile]
- -[HDSSetupSession sideloadVoiceProfile:locale:withCompletion:]
- GCC_except_table261
- _OBJC_IVAR_$_HDSSetupService._hdsFileTransferSession
- _OBJC_IVAR_$_HDSSetupSession._hdsFileTransferSession
- _OBJC_IVAR_$_HDSSetupSession._siriVoiceProfileState
- _SCError
- _SCPreferencesApplyChanges
- _SCPreferencesCommitChanges
- _SCPreferencesCreateWithAuthorization
- _SCPreferencesSetComputerName
- _SCPreferencesSetHostName
- _SCPreferencesSetLocalHostName
- __OBJC_$_CLASS_METHODS_NSData(Hexadecimal)
- __OBJC_$_INSTANCE_METHODS_NSData(Hexadecimal)
- ___30-[HDSSetupSession _invalidate]_block_invoke
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke.1372
- ___33-[SysDropService _sfServiceStart]_block_invoke.27
- ___33-[SysDropService _sfServiceStart]_block_invoke.29
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.294
- ___36-[SysDropSession _runSFSessionStart]_block_invoke.31
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.569
- ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_11
- ___43-[HDSSetupSession _runTransferVoiceProfile]_block_invoke
- ___43-[HDSSetupSession _runTransferVoiceProfile]_block_invoke_2
- ___56-[HDSDeviceActivation _mae_createSessionWithCompletion:]_block_invoke.178
- ___62-[HDSSetupSession sideloadVoiceProfile:locale:withCompletion:]_block_invoke
- ___64-[HDSDeviceActivation _mae_createActivationWithData:completion:]_block_invoke.200
- ___67-[HDSSetupService _handleStartFileTransferRequest:responseHandler:]_block_invoke
- ___69-[HDSDeviceActivationOperation _sendActivationURLRequest:completion:]_block_invoke
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.441
- ___72-[HDSSetupService fetchVoiceProfile:sharedUserId:locale:withCompletion:]_block_invoke
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1499
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1500
- ___block_descriptor_56_e8_32s40s48s_e51_v32?0"NSError"8"NSDictionary"16"NSDictionary"24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s48l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1228
- ___block_literal_global.1232
- ___block_literal_global.1236
- ___block_literal_global.1248
- ___block_literal_global.1252
- ___block_literal_global.1257
- ___block_literal_global.1261
- ___block_literal_global.1273
- ___block_literal_global.1279
- ___block_literal_global.1286
- ___block_literal_global.1290
- ___block_literal_global.1294
- ___block_literal_global.1305
- ___block_literal_global.1374
- ___block_literal_global.2869
- ___block_literal_global.2873
- ___block_literal_global.2877
- ___block_literal_global.2881
- ___block_literal_global.2885
- ___block_literal_global.2889
- ___block_literal_global.2905
- ___block_literal_global.2909
- ___block_literal_global.2926
- ___block_literal_global.2930
- ___block_literal_global.2934
- ___block_literal_global.2959
- ___block_literal_global.2963
- ___block_literal_global.2969
- ___block_literal_global.2974
- ___block_literal_global.2978
- ___block_literal_global.2983
- ___block_literal_global.2996
- ___block_literal_global.3095
- ___block_literal_global.574
- ___block_literal_global.908
- __unnamed_array_storage.106
- __unnamed_array_storage.107
- __unnamed_array_storage.1115
- __unnamed_array_storage.1116
- __unnamed_array_storage.1138
- __unnamed_array_storage.1139
- __unnamed_array_storage.1149
- __unnamed_array_storage.1150
- __unnamed_array_storage.1203
- __unnamed_array_storage.1204
- __unnamed_array_storage.1877
- __unnamed_array_storage.1878
- __unnamed_array_storage.1927
- __unnamed_array_storage.1928
- __unnamed_array_storage.292
- __unnamed_array_storage.330
- __unnamed_array_storage.331
- __unnamed_array_storage.390
- __unnamed_array_storage.391
- __unnamed_array_storage.41
- __unnamed_array_storage.436
- __unnamed_array_storage.484
- __unnamed_array_storage.485
- __unnamed_array_storage.588
- __unnamed_array_storage.589
- __unnamed_array_storage.706
- __unnamed_array_storage.707
- __unnamed_array_storage.822
- __unnamed_array_storage.823
- __unnamed_array_storage.844
- __unnamed_array_storage.845
- __unnamed_array_storage.877
- __unnamed_array_storage.878
- __unnamed_array_storage.988
- __unnamed_array_storage.989
- _initAFInterstitialIsDialogIdentifierInterstitial
- _objc_msgSend$SSRSpeakerProfilesBasePath
- _objc_msgSend$UUID
- _objc_msgSend$_handleStartFileTransferRequest:responseHandler:
- _objc_msgSend$_runTransferVoiceProfile
- _objc_msgSend$_sendActivationURLRequest:completion:
- _objc_msgSend$_setSystemName:hostname:
- _objc_msgSend$destDirectoryForTargetId:
- _objc_msgSend$fetchVoiceProfile:sharedUserId:locale:withCompletion:
- _objc_msgSend$importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:
- _objc_msgSend$isSpeakerRecognitionAvailable
- _objc_msgSend$locale
- _objc_msgSend$profileID
- _objc_msgSend$provisionedVoiceProfilesForAppDomain:withLocale:
- _objc_msgSend$sideloadFilesForTargetId:pathToDirectory:withCompletion:
- _objc_msgSend$sideloadVoiceProfile:locale:withCompletion:
- _objc_msgSend$siriProfileId
- _objc_msgSend$waitForFilesWithTargetId:withCompletion:
- _signpostLog.log.165
- _signpostLog.onceToken.166
- _softLinkAFInterstitialIsDialogIdentifierInterstitial
CStrings:
+ "\x02\x13"
+ "\x1143!\x11!232\x11\x13\x11\x1111\xf0%1Q3A\xe1!!\x81\x81a!sAr\x13\x13/\x0f\x01"
+ "\x15\x14"
+ "\x15d\x11%\x13\x11\x13!\x12!3\x14"
+ "### HomePod SysDrop Setup Error: %@, %{error}\n"
+ "-[HDSDeviceActivationOperation _sendActivationURLRequest:retries:completion:]"
+ "-[HDSDeviceActivationOperation _sendActivationURLRequest:retries:completion:]_block_invoke"
+ "-[HDSFileTransfer beginSysDropFileTransfer:pathToFile:withCompletion:]"
+ "-[HDSFileTransfer beginSysDropFileTransfer:pathToFile:withCompletion:]_block_invoke"
+ "-[HDSFileTransfer beginSysDropFileTransfer:pathToFile:withCompletion:]_block_invoke_3"
+ "-[HDSFileTransfer beginSysDropFileTransfer:pathToFile:withCompletion:]_block_invoke_4"
+ "-[HDSFileTransferService handleSysDropStartFileTransferRequest:responseHandler:]"
+ "-[HDSFileTransferService handleSysDropStartFileTransferRequest:responseHandler:]_block_invoke"
+ "-[HDSFileTransferService handleSysDropStartFileTransferRequest:responseHandler:]_block_invoke_2"
+ "-[HDSSetupService _handleSessionStarted:]_block_invoke_10"
+ "-[HDSSetupSession _logiTunesAuthRetryMetrics:durationSeconds:authType:retryAttempt:]"
+ "-[SysDropService _sendSysdiagnosePeerUpdate:inError:]"
+ "-[SysDropSession _runFileTransferComplete]"
+ "-[SysDropSession _runReceiveRPFileTransferSysdiagnose]"
+ "-[SysDropSession _setupHandlers]"
+ "-[SysDropSession _setupHandlers]_block_invoke"
+ "-[SysDropSession _setupHandlers]_block_invoke_3"
+ "-[SysDropSession _setupHandlers]_block_invoke_4"
+ "-[SysDropSession createSysDropRPFileTransferEvent:error:fileTransferProgress:]"
+ "-[SysDropSession fileTransferCompleted:]_block_invoke"
+ "-[SysDropSession fileTransferredSysDiagnosePath]"
+ "@\"RPFileTransferItem\""
+ "@\"RPFileTransferSession\""
+ "@36@0:8I16@20@28"
+ "Checking If Sysdiagnose file exists at %@\n"
+ "Failed To Setup File Transfer receiver"
+ "Failed to get target ID"
+ "Failed to get target ID\n"
+ "Failed to sent peer event: Status %@ | error %@\n"
+ "File Transfer Complete, moving onto finish\n"
+ "File Transfer Did not complete"
+ "File Transfer Disconnected"
+ "File transfer session started for item in path: %@ \n"
+ "ForceFailiTunes"
+ "HDSErrorDomain"
+ "HDSFileTransferService"
+ "HomePod Can do v2 terms: %s | %#m\n"
+ "Incoming HDSMessageRequestStartFileTransferSysDrop request\n"
+ "Item was successfully shared from %@ \n"
+ "No Sysdiagnose To File Transfer"
+ "No Transferred Item last path component\n"
+ "No sysdiagnose at cached path, ending sysdrop \n"
+ "NoDomain"
+ "RPFileTransferSession prepareTemplateAndReturnError: error %@ \n"
+ "Reporting iTunes auth Metric\n"
+ "Retrying iTunes auth\n"
+ "Setting needs setup to NO\n"
+ "Setting up Handlers\n"
+ "Setting up RPFileTransfer Listener Error %@ \n"
+ "Setting up RPFileTransfer Listener Success, responding to HP to start transfer\n"
+ "Setting up listener/reciever for File Xfer\n"
+ "Setup Ending due to SysDrop error, Session identifier %@\n"
+ "Setup Tearing Down\n"
+ "StereoPairUserInput HomePod being setup serial %@\n"
+ "SysDrop File Transfer Event: progress %.2f\n"
+ "SysDrop File Transfer Event: transferred %d | total %d\n"
+ "SysDrop Receiver Progress object: %@\n"
+ "SysDrop Receiver Progress sent to handler\n"
+ "SysDrop Receiver Progress state: %s\n"
+ "SysDrop Receiver Progress transferred byes: %d\n Progress total byes: %d\n"
+ "SysDrop Sender Progress object: %@\n"
+ "SysDrop Sender Progress state: %s\n"
+ "T@?,C,N,V_fileTransferCompletionHandler"
+ "T@?,C,N,V_fileTransferProgressHandler"
+ "T@?,C,N,V_promptForTermsAndConditionsV2Disagree"
+ "TB,N,V_sysDropFailed"
+ "TRActivationOperationErrorKey"
+ "TRAuthentication User declined Terms, exiting\n"
+ "TROperationErrorDomain"
+ "User declined Terms prompt not set\n"
+ "WiFiSetupTimeOut"
+ "_canDoV2TermsAndConditions"
+ "_companionCanRPFileTransfer"
+ "_companionCanRPFileTransfer: %s\n"
+ "_fileTransferCompletionHandler"
+ "_fileTransferProgressHandler"
+ "_fileTransferSession"
+ "_hds_rpft_sysdrop"
+ "_homePodCanRPFileTransfer"
+ "_homePodIsWiFiRetryV2"
+ "_homePodIsWiFiRetryV2: %s | %#m\n"
+ "_iTunesAuthRetryAttempt"
+ "_logiTunesAuthRetryMetrics:durationSeconds:authType:retryAttempt:"
+ "_promptForTermsAndConditionsV2Disagree"
+ "_rpFileCompleteState"
+ "_rpFileTransferError"
+ "_rpFileTransferState"
+ "_runFileTransferComplete"
+ "_runPreflightRPFileTransfer"
+ "_runReceiveRPFileTransferSysdiagnose"
+ "_runReceiveRPFileTransferSysdiagnose Start\n"
+ "_runReceiveRPFileTransferSysdiagnose done\n"
+ "_runReceiveRPFileTransferSysdiagnose in progress\n"
+ "_sendActivationURLRequest:retries:completion:"
+ "_sendSysdiagnosePeerUpdate:inError:"
+ "_setupHandlers"
+ "_setupHandlersState"
+ "_sysDropFailed"
+ "_targetID"
+ "_transferCompleted"
+ "_transferItem"
+ "addItem:"
+ "authType"
+ "beginSysDropFileTransfer:pathToFile:withCompletion:"
+ "com.apple.homedevicesetup.iTunesRetry"
+ "createSysDropRPFileTransferEvent:error:fileTransferProgress:"
+ "disableNeedsSetup"
+ "fileTransferCompleted:"
+ "fileTransferCompletionHandler"
+ "fileTransferCompletionHandler Failed\n"
+ "fileTransferCompletionHandler Successful\n"
+ "fileTransferCompletionHandler completed, Error %@ | transferItem %@\n"
+ "fileTransferProgressHandler"
+ "fileTransferredSysDiagnosePath"
+ "fileTransferredSysDiagnosePath %@\n"
+ "forceFailiTunesAuth"
+ "handleSysDropStartFileTransferRequest:responseHandler:"
+ "hds_tc_v2"
+ "homePodCanDoRPFileTransfer: %s\n"
+ "iTunes Auth Retry Metric sent: %@\n"
+ "iTunesAuthRetry"
+ "initWithArray:"
+ "initWithString:"
+ "lastPathComponent"
+ "promptForTermsAndConditionsV2Disagree"
+ "q\x12!\x15"
+ "remainingSeconds"
+ "retrying request for status code %d (error: %@)"
+ "sd_pt"
+ "sd_rp_e"
+ "sd_rp_ed"
+ "sd_rp_er"
+ "sd_rp_pr"
+ "sd_rp_rs"
+ "sd_rpft_cap"
+ "serialNumber"
+ "setCanDoTermsAndConditions:"
+ "setFileTransferCompletionHandler:"
+ "setFileTransferProgressHandler:"
+ "setProgressHandlerTimeInterval:"
+ "setPromptForTermsAndConditionsV2Disagree:"
+ "setSysDropFailed:"
+ "setupUnderlyingErrorCode3"
+ "setupUnderlyingErrorCode4"
+ "setupUnderlyingErrorDomain3"
+ "setupUnderlyingErrorDomain4"
+ "sysDropFailed"
+ "sysdrop_rp"
+ "termsandconditionsv2"
+ "totalByteCount"
+ "transferredByteCount"
+ "underlyingErrorCode"
+ "underlyingErrorCodeString"
+ "underlyingErrorDomain"
+ "v24@?0@\"NSError\"8@\"RPFileTransferItem\"16"
+ "v28@0:8I16@20"
+ "v36@0:8@16i24@?28"
+ "v40@0:8@16d24i32i36"
+ "wr_v2"
- "\x1143!\x11!23!\x12\x11\x13\x11\x1111\xf0%1Q3A\xe1!!\x81\x81a!sAb\x13\x13/\x0f"
- "\x13\x14"
- "\x15d\x11&\x13\x11\x13!\x12!3\x14"
- "### Apply name changes failed: %#m\n"
- "### Commit name changes failed: %#m\n"
- "### Set computer name %@' failed: %#m\n"
- "### Set hostname %@' failed: %#m\n"
- "### Set local hostname '%@' failed: %#m\n"
- "%@/%@/%@/%@"
- "-[HDSDeviceActivationOperation _sendActivationURLRequest:completion:]"
- "-[HDSDeviceActivationOperation _sendActivationURLRequest:completion:]_block_invoke"
- "-[HDSSetupService _handleSessionStarted:]_block_invoke_11"
- "-[HDSSetupService _handleSessionStarted:]_block_invoke_5"
- "-[HDSSetupService _handleStartFileTransferRequest:responseHandler:]"
- "-[HDSSetupService _handleStartFileTransferRequest:responseHandler:]_block_invoke"
- "-[HDSSetupService _setSystemName:hostname:]"
- "-[HDSSetupService fetchVoiceProfile:sharedUserId:locale:withCompletion:]"
- "-[HDSSetupService fetchVoiceProfile:sharedUserId:locale:withCompletion:]_block_invoke"
- "-[HDSSetupSession _runTransferVoiceProfile]"
- "-[HDSSetupSession _runTransferVoiceProfile]_block_invoke"
- "-[HDSSetupSession _runTransferVoiceProfile]_block_invoke_2"
- "-[HDSSetupSession sideloadVoiceProfile:locale:withCompletion:]"
- "-[HDSSetupSession sideloadVoiceProfile:locale:withCompletion:]_block_invoke"
- "AFInterstitialIsDialogIdentifierInterstitial"
- "Allocated new HDSFileTransfer session %@ \n"
- "An error happened waiting for files transfer: %{error}\n"
- "Create prefs to set name failed: %#m\n"
- "Fetching voice profile files for locale %@ and sharedUserId %@ \n"
- "Incoming HDSMessageRequestStartFileTransfer request\n"
- "Registered handlers for file transfer requests\n"
- "SSRSpeakerProfilesBasePath"
- "Setting systen name '%@', hostname '%@'\n"
- "Speaker recognition is unavailable"
- "StartFileTransferRequest: %##@\n"
- "Starting voice profile files transfer with target sessionId %@ and locale %@ \n"
- "The sideload voice profile failed: %{error}\n"
- "There are no voice profiles available"
- "TransferVoiceProfile"
- "TransferVoiceProfile errored: %{error}\n"
- "TransferVoiceProfile incoming response: %##.32@\n"
- "TransferVoiceProfile send request: %##.32@\n"
- "UUID"
- "Voice profile sideload completed, nullifying HDSFileTransfer session %@ \n"
- "Voice profile sideload succeeded\n"
- "Voice profile sideload succeeded \n"
- "Wait for files completed, nullifying HDSFileTransfer session %@ \n"
- "_handleStartFileTransferRequest:responseHandler:"
- "_hdsFileTransferSession"
- "_hds_ksuid"
- "_hds_kvpl"
- "_hds_rpft"
- "_runTransferVoiceProfile"
- "_sendActivationURLRequest:completion:"
- "_setSystemName:hostname:"
- "_siriVoiceProfileState"
- "com.apple.siri"
- "fetchVoiceProfile:sharedUserId:locale:withCompletion:"
- "importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:"
- "isSpeakerRecognitionAvailable"
- "profileID"
- "provisionedVoiceProfilesForAppDomain:withLocale:"
- "q\x15"
- "sideloadVoiceProfile:locale:withCompletion:"
- "siriProfileId"
- "siri_setup_optimization"
- "v48@0:8@16@24@32@?40"

```
