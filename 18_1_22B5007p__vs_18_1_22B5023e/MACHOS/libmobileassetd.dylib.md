## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1309.40.0.502.1
-  __TEXT.__text: 0x258284
-  __TEXT.__auth_stubs: 0x2380
-  __TEXT.__objc_stubs: 0x1efa0
-  __TEXT.__objc_methlist: 0xe9f8
+1309.40.28.502.1
+  __TEXT.__text: 0x25809c
+  __TEXT.__auth_stubs: 0x23a0
+  __TEXT.__objc_stubs: 0x1f460
+  __TEXT.__objc_methlist: 0xecc0
   __TEXT.__const: 0x494e
-  __TEXT.__objc_methname: 0x35604
-  __TEXT.__cstring: 0x4b86c
-  __TEXT.__objc_classname: 0xd50
-  __TEXT.__objc_methtype: 0x32ad
-  __TEXT.__oslogstring: 0x31d88
-  __TEXT.__gcc_except_tab: 0x2518
+  __TEXT.__objc_methname: 0x35f0e
+  __TEXT.__cstring: 0x4bc7c
+  __TEXT.__objc_classname: 0xd7b
+  __TEXT.__objc_methtype: 0x3360
+  __TEXT.__oslogstring: 0x2f80c
+  __TEXT.__gcc_except_tab: 0x250c
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x10c4
   __TEXT.__constg_swiftt: 0x1530

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x4668
+  __TEXT.__unwind_info: 0x46c8
   __TEXT.__eh_frame: 0x30c4
-  __DATA_CONST.__auth_got: 0x11d0
-  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__auth_got: 0x11e0
+  __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x9c8
-  __DATA_CONST.__const: 0x6460
-  __DATA_CONST.__cfstring: 0x30940
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __DATA_CONST.__const: 0x65b0
+  __DATA_CONST.__cfstring: 0x30ea0
+  __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8850
+  __DATA_CONST.__objc_selrefs: 0x89a8
   __DATA_CONST.__objc_intobj: 0x3f0
-  __DATA_CONST.__objc_arraydata: 0x918
+  __DATA_CONST.__objc_arraydata: 0x960
   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x13de8
-  __DATA.__objc_classrefs: 0x790
-  __DATA.__objc_superrefs: 0x2e0
-  __DATA.__objc_ivar: 0x1200
-  __DATA.__objc_data: 0xc70
+  __DATA.__objc_const: 0x14288
+  __DATA.__objc_classrefs: 0x7a0
+  __DATA.__objc_superrefs: 0x2e8
+  __DATA.__objc_ivar: 0x1248
+  __DATA.__objc_data: 0xd10
   __DATA.__data: 0x2608
-  __DATA.__bss: 0x5370
+  __DATA.__bss: 0x53a0
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x1978
   __DATA_DIRTY.__bss: 0x340

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/Seeding.framework/Seeding
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8127
-  Symbols:   14523
-  CStrings:  15527
+  Functions: 8198
+  Symbols:   14705
+  CStrings:  15573
 
Symbols:
+ +[MADAutoAssetControlManager preferencePersistedTableLoggingEnabled]
+ +[MADAutoAssetControlManager preferenceStagerDeterminePallasResponseFewer]
+ +[MADAutoAssetControlManager preferenceStagerDownloadFirstNotInCatalog]
+ +[MADAutoAssetControlManager preferenceStagingLookupFlipRequiredOptional]
+ +[MADAutoAssetLocker setPersistedStateCaching:]
+ +[MADAutoAssetScheduler setPersistedStateCaching:]
+ +[MADAutoAssetStager setPersistedStateCaching:]
+ +[MADPowerLogManager _retrieveSpecificIdentifier:andCategory:]
+ +[MADPowerLogManager _retrieveSpecificIdentifier:andCategory:].cold.1
+ +[MADPowerLogManager _retrieveSpecificIdentifier:andCategory:].cold.2
+ +[MADPowerLogManager sendTelemetry:forCategory:withPayload:]
+ +[MADPowerLogManager sharedManager]
+ +[SecureMobileAssetBundle getSigningServerURL:]
+ -[ControlManager getAssetAttributes:purpose:assetID:]
+ -[DownloadManager _getKeysNotLoggedForAutoResponse]
+ -[DownloadManager _getKeysNotLoggedForV2Response]
+ -[DownloadManager _isAutoAsset:]
+ -[DownloadManager _logResponseBody:nonce:extraServerOptions:]
+ -[DownloadManager _parseForAssetDetailsToLog:]
+ -[DownloadManager _shouldLogAssetDetails:extraServerOptions:]
+ -[MADAutoAssetControlManager action_QueueDownloadManager:error:].cold.1
+ -[MADAutoAssetControlManager alreadyHaveSetDescriptorMatching:]
+ -[MADAutoAssetControlManager alreadyHaveSetDescriptorMatching:].cold.1
+ -[MADAutoAssetControlManager doesSetDescriptor:coverAllForAtomicInstanceEntries:]
+ -[MADAutoAssetControlManager preferencePersistedTableLoggingEnabled]
+ -[MADAutoAssetControlManager preferenceStagerDeterminePallasResponseFewer]
+ -[MADAutoAssetControlManager preferenceStagerDownloadFirstNotInCatalog]
+ -[MADAutoAssetControlManager preferenceStagingLookupFlipRequiredOptional]
+ -[MADAutoAssetControlManager setPreferencePersistedTableLoggingEnabled:]
+ -[MADAutoAssetControlManager setPreferenceStagerDeterminePallasResponseFewer:]
+ -[MADAutoAssetControlManager setPreferenceStagerDownloadFirstNotInCatalog:]
+ -[MADAutoAssetControlManager setPreferenceStagingLookupFlipRequiredOptional:]
+ -[MADAutoAssetJob action_JobSuccessFoundPromoted:error:]
+ -[MADAutoAssetJob action_JobSuccessPersonalized:error:]
+ -[MADAutoAssetJob action_SetJobSuccessFoundPromoted:error:]
+ -[MADAutoAssetJob finishSetJobDownloadedNewer:forJobFinishedReason:]
+ -[MADAutoAssetJob isFoundAlreadyOnFilesystem:]
+ -[MADAutoAssetJob isFoundAlreadyOnFilesystem:].cold.1
+ -[MADAutoAssetPersisted cachingEnabled]
+ -[MADAutoAssetPersisted flushPersistedStateCacheAndSetCachingBehaviour:]
+ -[MADAutoAssetPersisted knownPersistedFiles]
+ -[MADAutoAssetPersisted knownPersistedStates]
+ -[MADAutoAssetPersisted setCachingEnabled:]
+ -[MADAutoAssetPersisted setKnownPersistedFiles:]
+ -[MADAutoAssetPersisted setKnownPersistedStates:]
+ -[MADAutoAssetStager _adjustPallasResponseBasedOnPreferences:]
+ -[MADAutoAssetStager _adjustPallasResponseBasedOnPreferences:].cold.1
+ -[MADAutoAssetStager firstDownloadedAsIfNotInCatalog]
+ -[MADAutoAssetStager setFirstDownloadedAsIfNotInCatalog:]
+ -[MADAutoTargetLookupResults lookupResultsAssetCount]
+ -[MADPowerLogData .cxx_destruct]
+ -[MADPowerLogData assetSpecifier]
+ -[MADPowerLogData assetType]
+ -[MADPowerLogData assetVersion]
+ -[MADPowerLogData clientName]
+ -[MADPowerLogData convertPayloadToDict]
+ -[MADPowerLogData description]
+ -[MADPowerLogData initWithType:withAssetSpecifier:versionNumber:clientName:startingAt:endingAt:withTotalBytes:andResult:]
+ -[MADPowerLogData result]
+ -[MADPowerLogData timeEnd]
+ -[MADPowerLogData timeStart]
+ -[MADPowerLogData totalBytes]
+ -[MADPowerLogManager autoDownloads]
+ -[MADPowerLogManager setAutoDownloads:]
+ -[MADPowerLogManager setV2Downloads:]
+ -[MADPowerLogManager v2Downloads]
+ GCC_except_table128
+ GCC_except_table135
+ GCC_except_table152
+ GCC_except_table162
+ GCC_except_table166
+ GCC_except_table18
+ GCC_except_table222
+ GCC_except_table247
+ GCC_except_table33
+ GCC_except_table368
+ GCC_except_table527
+ GCC_except_table530
+ GCC_except_table532
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table69
+ GCC_except_table89
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferencePersistedTableLoggingEnabled
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagerDeterminePallasResponseFewer
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagerDownloadFirstNotInCatalog
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagingLookupFlipRequiredOptional
+ OBJC_IVAR_$_MADAutoAssetPersisted._cachingEnabled
+ OBJC_IVAR_$_MADAutoAssetPersisted._knownPersistedFiles
+ OBJC_IVAR_$_MADAutoAssetPersisted._knownPersistedStates
+ OBJC_IVAR_$_MADAutoAssetStager._firstDownloadedAsIfNotInCatalog
+ OBJC_IVAR_$_MADPowerLogData._assetSpecifier
+ OBJC_IVAR_$_MADPowerLogData._assetType
+ OBJC_IVAR_$_MADPowerLogData._assetVersion
+ OBJC_IVAR_$_MADPowerLogData._clientName
+ OBJC_IVAR_$_MADPowerLogData._result
+ OBJC_IVAR_$_MADPowerLogData._timeEnd
+ OBJC_IVAR_$_MADPowerLogData._timeStart
+ OBJC_IVAR_$_MADPowerLogData._totalBytes
+ OBJC_IVAR_$_MADPowerLogManager._autoDownloads
+ OBJC_IVAR_$_MADPowerLogManager._v2Downloads
+ _OBJC_CLASS_$_MADPowerLogData
+ _OBJC_CLASS_$_MADPowerLogManager
+ _OBJC_METACLASS_$_MADPowerLogData
+ _OBJC_METACLASS_$_MADPowerLogManager
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1045
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.971
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.975
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.991
+ __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1047
+ __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1048
+ __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1052
+ __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1071
+ __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1071.cold.1
+ __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1081
+ __27-[MABrainUpdater schedule:]_block_invoke_2.405
+ __27-[MABrainUpdater schedule:]_block_invoke_3.406
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1004
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1051
+ __46-[MABAACertManager issueAndCopyCertsInternal:]_block_invoke.347
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1100
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1100.cold.1
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1107
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1059
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1060
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1061
+ __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.914
+ __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.934
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.283
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1038
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1056
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1013
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1020
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1021
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2041
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2240
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2241
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2241.cold.1
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1004
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1005
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1006
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1034
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1035
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1035.cold.1
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1037
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1037.cold.1
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2790
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2791
+ __OBJC_$_CLASS_METHODS_MADPowerLogManager
+ __OBJC_$_INSTANCE_METHODS_MADPowerLogData
+ __OBJC_$_INSTANCE_METHODS_MADPowerLogManager
+ __OBJC_$_INSTANCE_VARIABLES_MADPowerLogData
+ __OBJC_$_INSTANCE_VARIABLES_MADPowerLogManager
+ __OBJC_$_PROP_LIST_MADPowerLogData
+ __OBJC_$_PROP_LIST_MADPowerLogManager
+ __OBJC_CLASS_RO_$_MADPowerLogData
+ __OBJC_CLASS_RO_$_MADPowerLogManager
+ __OBJC_METACLASS_RO_$_MADPowerLogData
+ __OBJC_METACLASS_RO_$_MADPowerLogManager
+ ___121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke_2
+ ___24-[MADAutoSetLocker init]_block_invoke_2
+ ___26-[MADAutoAssetLocker init]_block_invoke_2
+ ___26-[MADAutoAssetStager init]_block_invoke_5
+ ___29-[MADAutoAssetScheduler init]_block_invoke_2
+ ___35+[MADPowerLogManager sharedManager]_block_invoke
+ ___47+[MADAutoAssetLocker setPersistedStateCaching:]_block_invoke
+ ___47+[MADAutoAssetStager setPersistedStateCaching:]_block_invoke
+ ___49-[DownloadManager _getKeysNotLoggedForV2Response]_block_invoke
+ ___50+[MADAutoAssetScheduler setPersistedStateCaching:]_block_invoke
+ ___51-[DownloadManager _getKeysNotLoggedForAutoResponse]_block_invoke
+ ___52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke_2
+ ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152bs160r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lr160l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s152l8s104l8s112l8s120l8s128l8s136l8s144l8
+ ___block_descriptor_187_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8s152l8s160l8s168l8
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ __block_literal_global.1001
+ __block_literal_global.1003
+ __block_literal_global.1058
+ __block_literal_global.1105
+ __block_literal_global.1129
+ __block_literal_global.1136
+ __block_literal_global.1152
+ __block_literal_global.1152
+ __block_literal_global.1156
+ __block_literal_global.1161
+ __block_literal_global.1163
+ __block_literal_global.1194
+ __block_literal_global.1219
+ __block_literal_global.1224
+ __block_literal_global.1258
+ __block_literal_global.1419
+ __block_literal_global.1436
+ __block_literal_global.1509
+ __block_literal_global.1513
+ __block_literal_global.1514
+ __block_literal_global.1519
+ __block_literal_global.1522
+ __block_literal_global.1552
+ __block_literal_global.1650
+ __block_literal_global.1976
+ __block_literal_global.1984
+ __block_literal_global.1992
+ __block_literal_global.2000
+ __block_literal_global.2008
+ __block_literal_global.2016
+ __block_literal_global.2024
+ __block_literal_global.2032
+ __block_literal_global.2194
+ __block_literal_global.2243
+ __block_literal_global.266
+ __block_literal_global.269
+ __block_literal_global.272
+ __block_literal_global.2776
+ __block_literal_global.2794
+ __block_literal_global.3107
+ __block_literal_global.3177
+ __block_literal_global.3179
+ __block_literal_global.323
+ __block_literal_global.3327
+ __block_literal_global.338
+ __block_literal_global.4062
+ __block_literal_global.408
+ __block_literal_global.547
+ __block_literal_global.568
+ __block_literal_global.897
+ __block_literal_global.907
+ __block_literal_global.916
+ __block_literal_global.920
+ __block_literal_global.925
+ __block_literal_global.926
+ __block_literal_global.929
+ __block_literal_global.934
+ __block_literal_global.936
+ __block_literal_global.939
+ __block_literal_global.942
+ __block_literal_global.944
+ __block_literal_global.968
+ __block_literal_global.970
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_CryptoKit_Static
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_MobileAssetKeyManager
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_CryptoKit_Static
+ __swift_FORCE_LOAD_$_swift_errno_$_MobileAssetKeyManager
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_math_$_CryptoKit_Static
+ __swift_FORCE_LOAD_$_swift_math_$_MobileAssetKeyManager
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_signal_$_CryptoKit_Static
+ __swift_FORCE_LOAD_$_swift_signal_$_MobileAssetKeyManager
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_stdio_$_CryptoKit_Static
+ __swift_FORCE_LOAD_$_swift_stdio_$_MobileAssetKeyManager
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_CryptoKit_Static
+ __swift_FORCE_LOAD_$_swift_time_$_MobileAssetKeyManager
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftsys_time_$_CryptoKit_Static
+ __swift_FORCE_LOAD_$_swiftsys_time_$_MobileAssetKeyManager
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_FORCE_LOAD_$_swiftunistd_$_CryptoKit_Static
+ __swift_FORCE_LOAD_$_swiftunistd_$_MobileAssetKeyManager
+ _getKeysNotLoggedForAutoResponse.autoNotLoggedKeys
+ _getKeysNotLoggedForAutoResponse.autoNotLoggedKeysOnce
+ _getKeysNotLoggedForV2Response.v2NotLoggedKeys
+ _getKeysNotLoggedForV2Response.v2NotLoggedKeysOnce
+ _kMobileAssetPreferencesAutoAssetPersistedTableLoggingEnabled
+ _kMobileAssetPreferencesAutoAssetStagerDeterminePallasResponseFewer
+ _kMobileAssetPreferencesAutoAssetStagerDownloadFirstNotInCatalog
+ _kMobileAssetPreferencesAutoAssetStagingLookupFlipRequiredOptional
+ _objc_msgSend$_adjustPallasResponseBasedOnPreferences:
+ _objc_msgSend$_getKeysNotLoggedForAutoResponse
+ _objc_msgSend$_getKeysNotLoggedForV2Response
+ _objc_msgSend$_isAutoAsset:
+ _objc_msgSend$_logResponseBody:nonce:extraServerOptions:
+ _objc_msgSend$_parseForAssetDetailsToLog:
+ _objc_msgSend$_retrieveSpecificIdentifier:andCategory:
+ _objc_msgSend$_shouldLogAssetDetails:extraServerOptions:
+ _objc_msgSend$action_JobSuccessFoundPromoted:error:
+ _objc_msgSend$action_JobSuccessPersonalized:error:
+ _objc_msgSend$action_SetJobSuccessFoundPromoted:error:
+ _objc_msgSend$alreadyHaveSetDescriptorMatching:
+ _objc_msgSend$assetQueue
+ _objc_msgSend$autoDownloads
+ _objc_msgSend$cachingEnabled
+ _objc_msgSend$convertPayloadToDict
+ _objc_msgSend$doesSetDescriptor:coverAllForAtomicInstanceEntries:
+ _objc_msgSend$finishSetJobDownloadedNewer:forJobFinishedReason:
+ _objc_msgSend$firstDownloadedAsIfNotInCatalog
+ _objc_msgSend$flushPersistedStateCacheAndSetCachingBehaviour:
+ _objc_msgSend$getAssetAttributes:purpose:assetID:
+ _objc_msgSend$getSigningServerURL:
+ _objc_msgSend$initWithType:withAssetSpecifier:versionNumber:clientName:startingAt:endingAt:withTotalBytes:andResult:
+ _objc_msgSend$isFoundAlreadyOnFilesystem:
+ _objc_msgSend$knownPersistedFiles
+ _objc_msgSend$knownPersistedStates
+ _objc_msgSend$lookupResultsAssetCount
+ _objc_msgSend$preferencePersistedTableLoggingEnabled
+ _objc_msgSend$preferenceStagerDeterminePallasResponseFewer
+ _objc_msgSend$preferenceStagerDownloadFirstNotInCatalog
+ _objc_msgSend$preferenceStagingLookupFlipRequiredOptional
+ _objc_msgSend$result
+ _objc_msgSend$sendTelemetry:forCategory:withPayload:
+ _objc_msgSend$setAutoDownloads:
+ _objc_msgSend$setCachingEnabled:
+ _objc_msgSend$setFirstDownloadedAsIfNotInCatalog:
+ _objc_msgSend$setPersistedStateCaching:
+ _objc_msgSend$setV2Downloads:
+ _objc_msgSend$timeEnd
+ _objc_msgSend$timeStart
+ _objc_msgSend$totalBytes
+ _objc_msgSend$v2Downloads
+ sharedManager.powerLogManager
+ sharedManager.powerLogManagerOnce
- +[SecureMobileAssetBundle getSigningServerURL]
- -[DownloadManager _logResponseBody:nonce:]
- -[MADAutoAssetJob isFoundAlreadyOnFilesystem]
- -[MADAutoAssetJob isFoundAlreadyOnFilesystem].cold.1
- -[MADAutoAssetStager _countOfEntriesDictionaryOfDictionary:]
- -[MADAutoAssetStager action_NextAwaitingBeginDownload:error:].cold.1
- GCC_except_table10
- GCC_except_table127
- GCC_except_table134
- GCC_except_table151
- GCC_except_table157
- GCC_except_table161
- GCC_except_table19
- GCC_except_table221
- GCC_except_table23
- GCC_except_table239
- GCC_except_table367
- GCC_except_table4
- GCC_except_table526
- GCC_except_table529
- GCC_except_table53
- GCC_except_table531
- GCC_except_table57
- GCC_except_table57
- GCC_except_table59
- GCC_except_table63
- GCC_except_table68
- GCC_except_table86
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1024
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.950
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.954
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.970
- __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1026
- __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1027
- __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1031
- __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1032
- __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1051
- __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1051.cold.1
- __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1061
- __27-[MABrainUpdater schedule:]_block_invoke_2.387
- __27-[MABrainUpdater schedule:]_block_invoke_3.388
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1006
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.959
- __46-[MABAACertManager issueAndCopyCertsInternal:]_block_invoke.329
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1055
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1055.cold.1
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1062
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1039
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1040
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1041
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.893
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.913
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.265
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1017
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1035
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.992
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.999
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1000
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2008
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2201
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2202
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2202.cold.1
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.cold.1
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.983
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.984
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.985
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1013
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1014
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1014.cold.1
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1016
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1016.cold.1
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2751
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2752
- ___block_descriptor_155_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8
- ___block_descriptor_160_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144bs152r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lr152l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s144l8s96l8s104l8s112l8s120l8s128l8s136l8
- __block_literal_global.1016
- __block_literal_global.1084
- __block_literal_global.1103
- __block_literal_global.1107
- __block_literal_global.1108
- __block_literal_global.1123
- __block_literal_global.1128
- __block_literal_global.1130
- __block_literal_global.1131
- __block_literal_global.1173
- __block_literal_global.1198
- __block_literal_global.1203
- __block_literal_global.1237
- __block_literal_global.1398
- __block_literal_global.1415
- __block_literal_global.1488
- __block_literal_global.1492
- __block_literal_global.1493
- __block_literal_global.1498
- __block_literal_global.1501
- __block_literal_global.1531
- __block_literal_global.1629
- __block_literal_global.1938
- __block_literal_global.1949
- __block_literal_global.1957
- __block_literal_global.1973
- __block_literal_global.1981
- __block_literal_global.1989
- __block_literal_global.1997
- __block_literal_global.2005
- __block_literal_global.2161
- __block_literal_global.2210
- __block_literal_global.248
- __block_literal_global.251
- __block_literal_global.254
- __block_literal_global.2745
- __block_literal_global.2763
- __block_literal_global.305
- __block_literal_global.3079
- __block_literal_global.320
- __block_literal_global.3326
- __block_literal_global.390
- __block_literal_global.4017
- __block_literal_global.529
- __block_literal_global.550
- __block_literal_global.862
- __block_literal_global.874
- __block_literal_global.874
- __block_literal_global.876
- __block_literal_global.886
- __block_literal_global.892
- __block_literal_global.892
- __block_literal_global.899
- __block_literal_global.902
- __block_literal_global.902
- __block_literal_global.905
- __block_literal_global.908
- __block_literal_global.915
- __block_literal_global.918
- __block_literal_global.921
- __block_literal_global.947
- __block_literal_global.949
- __block_literal_global.956
- __block_literal_global.958
- _objc_msgSend$_countOfEntriesDictionaryOfDictionary:
- _objc_msgSend$_logResponseBody:nonce:
- _objc_msgSend$getSigningServerURL
- _objc_msgSend$isFoundAlreadyOnFilesystem
CStrings:
+ "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attribute | graftedOrMounted:Y | secureAssetBundle:%!{(MISSING)public}@ | autoAssetDescriptor:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attribute | involvesGrafting:Y | autoAssetDescriptor:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attribute | isSecureAsset:Y | secureAssetBundle:%!{(MISSING)public}@ | autoAssetDescriptor:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attribute | personalizationRequired:Y | secureAssetBundle:%!{(MISSING)public}@ | autoAssetDescriptor:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attribute | prePersonalized:Y | secureAssetBundle:%!{(MISSING)public}@ | autoAssetDescriptor:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} unable to self-heal, clearing latest-to-vend | setConfiguration:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | latest-to-vend includes personalized-not-grafted|mounted (acceptable since not currently locked) | downloadedSelector:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | personalization required after startup secure-healing | downloadedSelector:%!{(MISSING)public}@"
+ "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | unable to re-graft during startup secure-healing | downloadedSelector:%!{(MISSING)public}@"
+ "\x1c"
+ "%!@(MISSING)/%!@(MISSING)/%!@(MISSING)%!@(MISSING).asset"
+ "%!@(MISSING)|status:%!l(MISSING)d(set:%!l(MISSING)d)|jobs:%!l(MISSING)d(set:%!l(MISSING)d)(UUID:%!l(MISSING)d)|grants:%!l(MISSING)d|configs:%!l(MISSING)d|AI:%!l(MISSING)d|FS:%!l(MISSING)d(set:%!l(MISSING)d)|sched:%!l(MISSING)d|timed:%!l(MISSING)d|client:%!l(MISSING)d"
+ "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [%!{(MISSING)public}@OPTIONAL] (unarchivedSize=0) | stagedDescriptor:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [%!{(MISSING)public}@OPTIONAL] | nextAvailableDescirptor:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [%!{(MISSING)public}@OPTIONAL] | stagedDescriptor:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [%!{(MISSING)public}@REQUIRED] (unarchivedSize=0) | stagedDescriptor:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [%!{(MISSING)public}@REQUIRED] | nextAvailableDescirptor:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [%!{(MISSING)public}@REQUIRED] | stagedDescriptor:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@\n[AUTO-STAGER] {_adjustPallasResponseBasedOnPreferences} key value is not an array | setCatalogKey:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@\n[AUTO-STAGER] {_adjustPallasResponseBasedOnPreferences} unable to determine key/value from set-catalog | setCatalogKey:%!{(MISSING)public}@ | setCatalogValue:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@ {flushPersistedStateCacheAndSetCachingBehaviour} | Flushing persisted state in memory cache and %!{(MISSING)public}@ future caching"
+ "%!{(MISSING)public}@ | unable to create persisted-state for file:%!{(MISSING)public}@ | %!{(MISSING)public}@[%!{(MISSING)public}@]"
+ "%!{(MISSING)public}@ | {%!{(MISSING)public}@} no latest-downloaded-atomic-entries so reporting discovered:\n%!{(MISSING)public}@"
+ "+[SecureMobileAssetBundle getSigningServerURL:]"
+ "-[DownloadManager _logResponseBody:nonce:extraServerOptions:]"
+ "2.1.13"
+ "2.2.8"
+ "?\x0f\x1f\a\x112Rd"
+ "?1"
+ "?@"
+ "@76@0:8@16@24@32@40@48@56Q64B72"
+ "AutoAssetDownloads"
+ "AutoAssetPersistedTableLoggingEnabled"
+ "AutoAssetStagerDeterminePallasResponseFewer"
+ "AutoAssetStagerDownloadFirstNotInCatalog"
+ "AutoAssetStagingLookupFlipRequiredOptional"
+ "B24@0:8^B16"
+ "CatalogFoundPromoted"
+ "CatalogFoundPromotedHeal"
+ "DownloadMetrics"
+ "EraseAcceptedRemoveAll"
+ "FLIPPED-TO-"
+ "FoundPromotedHealing"
+ "Indicating that loading of persisted state is done"
+ "Indicating that loading of persisted state is starting"
+ "JobSuccessFoundPromoted"
+ "JobSuccessPersonalized"
+ "MADPowerLogData"
+ "MADPowerLogManager"
+ "Pallas response nonce: %!@(MISSING). Details for asset #%!l(MISSING)d [of %!l(MISSING)d] is: %!@(MISSING)"
+ "Pallas response nonce: %!@(MISSING). Total asset count: %!l(MISSING)d. The response body is: %!@(MISSING)"
+ "SUCCESS(IMMEDIATE_PROMOTED)"
+ "SUCCESS(PERSONALIZED)"
+ "SetCatalogFoundPromoted"
+ "SetCatalogFoundPromotedHeal"
+ "SetJobSuccessFoundPromoted"
+ "Starting built-in MobileAsset brain built Aug  5 2024 21:26:31"
+ "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Aug  5 2024 21:26:31"
+ "SupportedDeviceNames"
+ "T@\"NSDate\",R,&,N,V_timeEnd"
+ "T@\"NSDate\",R,&,N,V_timeStart"
+ "T@\"NSMutableDictionary\",&,N,V_knownPersistedFiles"
+ "T@\"NSMutableDictionary\",&,N,V_knownPersistedStates"
+ "T@\"NSString\",R,&,N,V_clientName"
+ "TB,N,V_cachingEnabled"
+ "TB,N,V_firstDownloadedAsIfNotInCatalog"
+ "TB,N,V_preferencePersistedTableLoggingEnabled"
+ "TB,N,V_preferenceStagerDownloadFirstNotInCatalog"
+ "TB,N,V_preferenceStagingLookupFlipRequiredOptional"
+ "TB,R,N,V_result"
+ "TQ,R,N,V_totalBytes"
+ "T^{PPSTelemetryIdentifier=},N,V_autoDownloads"
+ "T^{PPSTelemetryIdentifier=},N,V_v2Downloads"
+ "Tq,N,V_preferenceStagerDeterminePallasResponseFewer"
+ "UnsupportedDevices"
+ "[%!{(MISSING)public}@] {%!{(MISSING)public}@:atomicInstanceNewSetAtomicInstance}\n[PSUS] not trimming based on overflow | setAtomicInstance:%!{(MISSING)public}@"
+ "[%!{(MISSING)public}@] {LoadPersistedResumeLocker} | Enabling in memory caching for persisted state objects"
+ "[%!{(MISSING)public}@] {LoadPersistedResumeLocker} | Not using in memory caching for persisted state objects"
+ "[%!{(MISSING)public}@] {alreadyHaveSetDescriptorMatching} no entryID"
+ "[%!{(MISSING)public}@] {alreadyHaveSetDescriptorMatching} unable to determine previous status | entryID:%!{(MISSING)public}@"
+ "[%!{(MISSING)public}@] {alreadyHaveSetDescriptorMatching} unable to load set-descriptor | entryID:%!{(MISSING)public}@"
+ "[%!{(MISSING)public}@] {locateSetDescriptorDownloadedPreferringByAtomicInstance} located descriptor not fully downloaded | locatedDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "[CATALOG-LOOKUP-ADJUST] job provided jobInformation dropped | eventInfo:%!{(MISSING)public}@"
+ "[MADPowerLogManager] invalid category"
+ "[MADPowerLogManager] invalid subsystem"
+ "[OSVersion:%!@(MISSING)|Build:%!@(MISSING)|GroupNames:%!@(MISSING)|LookupResults:%!l(MISSING)d|Assets:%!l(MISSING)d]"
+ "[clientInstance:%!@(MISSING)|clientDesire:%!@(MISSING)|setDescriptor:%!@(MISSING)|currentSetStatus:%!@(MISSING)|UUID:%!@(MISSING)]"
+ "[clientInstance:%!@(MISSING)|clientDesire:%!@(MISSING)|setDescriptor:%!@(MISSING)|foundContent:%!@(MISSING)|UUID:%!@(MISSING)]"
+ "[domain:%!@(MISSING)|setID:%!@(MISSING)|config:%!l(MISSING)d|AIs:%!l(MISSING)d(newer:%!@(MISSING)[%!l(MISSING)d])(latest:%!@(MISSING)[%!l(MISSING)d])|user:%!@(MISSING)|locks:%!@(MISSING)]"
+ "^{PPSTelemetryIdentifier=}"
+ "^{PPSTelemetryIdentifier=}16@0:8"
+ "^{PPSTelemetryIdentifier=}32@0:8@16@24"
+ "_MeasurementAlgorithm"
+ "_OSVersionCompatibilities"
+ "_adjustPallasResponseBasedOnPreferences:"
+ "_autoDownloads"
+ "_cachingEnabled"
+ "_firstDownloadedAsIfNotInCatalog"
+ "_getKeysNotLoggedForAutoResponse"
+ "_getKeysNotLoggedForV2Response"
+ "_isAutoAsset:"
+ "_knownPersistedFiles"
+ "_knownPersistedStates"
+ "_logResponseBody:nonce:extraServerOptions:"
+ "_parseForAssetDetailsToLog:"
+ "_preferencePersistedTableLoggingEnabled"
+ "_preferenceStagerDeterminePallasResponseFewer"
+ "_preferenceStagerDownloadFirstNotInCatalog"
+ "_preferenceStagingLookupFlipRequiredOptional"
+ "_result"
+ "_retrieveSpecificIdentifier:andCategory:"
+ "_shouldLogAssetDetails:extraServerOptions:"
+ "_timeEnd"
+ "_timeStart"
+ "_totalBytes"
+ "_v2Downloads"
+ "action JobSuccessFoundPromoted should never execute for set-job"
+ "action JobSuccessPersonalized should never execute for set-job"
+ "action_JobSuccessFoundPromoted:error:"
+ "action_JobSuccessPersonalized:error:"
+ "action_SetJobSuccessFoundPromoted:error:"
+ "alreadyHaveSetDescriptorMatching"
+ "alreadyHaveSetDescriptorMatching:"
+ "assetType:%!@(MISSING) | assetVersion:%!@(MISSING) | assetSpecifier:%!@(MISSING) | clientName:%!@(MISSING) | timeStart:%!@(MISSING) | timeEnd:%!@(MISSING) | totalBytes:%!l(MISSING)ld | result:%!@(MISSING)"
+ "autoDownloads"
+ "bytesDownloaded"
+ "cachingEnabled"
+ "com.apple.MobileAsset.UAF.FM.CodeLM"
+ "com.apple.MobileAsset.UAF.FM.GenerativeModels"
+ "com.apple.MobileAsset.UAF.Handwriting.Synthesis"
+ "com.apple.MobileAsset.UAF.IF.Planner"
+ "com.apple.MobileAsset.UAF.Photos.MagicCleanup"
+ "com.apple.MobileAsset.UAF.Search.ODLA"
+ "com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition"
+ "com.apple.MobileAsset.UAF.VoiceAssistant"
+ "convertPayloadToDict"
+ "disabling"
+ "doesSetDescriptor:coverAllForAtomicInstanceEntries:"
+ "dropping descriptor when no item exists at path:%!@(MISSING)"
+ "enabling"
+ "finishSetJobDownloadedNewer:forJobFinishedReason:"
+ "firstDownloadedAsIfNotInCatalog"
+ "flushPersistedStateCacheAndSetCachingBehaviour:"
+ "getAssetAttributes:purpose:assetID:"
+ "getSigningServerURL:"
+ "https://gs.apple.com"
+ "initWithType:withAssetSpecifier:versionNumber:clientName:startingAt:endingAt:withTotalBytes:andResult:"
+ "isFoundAlreadyOnFilesystem:"
+ "knownPersistedFiles"
+ "knownPersistedStates"
+ "logger:%!@(MISSING)|policy:%!@(MISSING)|server:%!@(MISSING)|table:%!@(MISSING)|FSM:%!@(MISSING)|(persisted)active:%!@(MISSING),known:%!@(MISSING),configs:%!@(MISSING),AI:%!@(MISSING)|(sets)active:%!@(MISSING),desc:%!@(MISSING),targets:%!@(MISSING),lookups:%!@(MISSING),map:%!@(MISSING)"
+ "lookupResultsAssetCount"
+ "persistedStateLoadingInProgress"
+ "preferencePersistedTableLoggingEnabled"
+ "preferenceStagerDeterminePallasResponseFewer"
+ "preferenceStagerDownloadFirstNotInCatalog"
+ "preferenceStagingLookupFlipRequiredOptional"
+ "purpose_%!@(MISSING)/"
+ "resumeJobs"
+ "sendTelemetry:forCategory:withPayload:"
+ "set-job ended with all content downloaded but some secure auto-assets require personalization [intended:%!@(MISSING)]"
+ "setAutoDownloads:"
+ "setCachingEnabled:"
+ "setFirstDownloadedAsIfNotInCatalog:"
+ "setKnownPersistedFiles:"
+ "setKnownPersistedStates:"
+ "setPersistedStateCaching:"
+ "setPreferencePersistedTableLoggingEnabled:"
+ "setPreferenceStagerDeterminePallasResponseFewer:"
+ "setPreferenceStagerDownloadFirstNotInCatalog:"
+ "setPreferenceStagingLookupFlipRequiredOptional:"
+ "setV2Downloads:"
+ "timeEnd"
+ "timeStart"
+ "timestampEnd"
+ "timestampStart"
+ "totalBytes"
+ "unable to determine local repository path for selector:%!@(MISSING)"
+ "unable to locate asset to be downloaded in set-lookup-results - skipping asset"
+ "v24@0:8^{PPSTelemetryIdentifier=}16"
+ "v2AssetDownloads"
+ "v2Downloads"
+ "{IssueClientReplySetJob} set-job for lock-atomic indicated same-version-found - considering as a successful lock of the atomic-instance found earlier | setJobInformation:%!{(MISSING)public}@"
+ "{NextAwaitingBeginDownload} unable to locate entry in set-look-results - skipping asset | stagingDescriptor:%!@(MISSING)"
+ "{_logResponseBody} ANOLMALY: list of assets is not of type NSArray"
+ "{_logResponseBody} ANOLMALY:_parseForAssetDetailsToLog returned nil for detailsToLog for the following asset meta data: %!@(MISSING)"
+ "{_logResponseBody} ANOLMALY:_parseForAssetDetailsToLog: number of asset details to log do not match assets found.  Assets found: %!l(MISSING)d.  Asset details to log: %!l(MISSING)d"
+ "{_removeAllContentForEliminateTracker} unable to determine local repository path for assetDirectory:%!@(MISSING)"
+ "{_removeDescriptorFromFilesystem} unable to determine local URL for descriptor:%!@(MISSING)"
+ "{_removeDescriptorFromFilesystem} unable to determine local filesystem URL from localContentURL:%!@(MISSING)"
+ "{_removeStagedAssetFromFilesystem} unable to determine local URL for stagedDescriptor:%!@(MISSING)"
+ "{handleControlClientForceGlobalPurgeRequest} unable to determine local repository path for selector:%!@(MISSING)"
+ "{persistForJobSelector} unable to determine local repository path for jobDescriptor:%!@(MISSING)"
+ "{persistSetJobDescriptor} unable to determine local repository path for nextDownloadedAtomicEntry:%!@(MISSING)"
- "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attribute | graftedOrMounted:%!{(MISSING)public}@ | secureAssetBundle:%!{(MISSING)public}@ | autoAssetDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attribute | involvesGrafting:%!{(MISSING)public}@ | autoAssetDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attribute | isSecureAsset:%!{(MISSING)public}@ | secureAssetBundle:%!{(MISSING)public}@ | autoAssetDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attribute | personalizationRequired:%!{(MISSING)public}@ | secureAssetBundle:%!{(MISSING)public}@ | autoAssetDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attribute | prePersonalized:%!{(MISSING)public}@ | secureAssetBundle:%!{(MISSING)public}@ | autoAssetDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attributes | involvesPersonalization:%!{(MISSING)public}@ | involvesGrafting:%!{(MISSING)public}@ | autoAssetDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-DETERMINE] {%!{(MISSING)public}@} determined secure attributes | involvesSecureOperations:%!{(MISSING)public}@ | setDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-GRAFT-REMOVE-ALL] {%!{(MISSING)public}@} endAccess SUCCESS | nextUngraftDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-GRAFT-REMOVE-ALL] {%!{(MISSING)public}@} ending access | nextUngraftDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-GRAFT-REMOVE] {ungraftIfNotAccessible} not a secure mobile asset | assetPath:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-PERSONALIZATION-GRAFT-SET] {%!{(MISSING)public}@} personalize+graft set - no secure elements | setDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-PERSONALIZATION-GRAFT-SET] {%!{(MISSING)public}@} personalize+graft set - no secure operations required | setDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | latest-to-vend includes personalized-not-grafted|mounted (acceptable since not currently locked) | setConfiguration:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | personalization required after startup secure-healing - clearing latest-to-vend | setConfiguration:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-VALIDATE][SET-CONTROL][STARTUP] {%!{(MISSING)public}@} | unable to re-graft during startup secure-healing - clearing latest-to-vend | setConfiguration:%!{(MISSING)public}@"
- "\n[SECURE][%!{(MISSING)public}@][SET-CONTROL] {%!{(MISSING)public}@} requiring(Personalization:%!d(MISSING) Grafting:%!d(MISSING)) | allowNetwork:%!{(MISSING)public}@ | setDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][%!{(MISSING)public}@][SET-CONTROL] {%!{(MISSING)public}@} secure operation(s) ERROR | error:%!{(MISSING)public}@ | setDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][%!{(MISSING)public}@][SET-CONTROL] {%!{(MISSING)public}@} secure operation(s) SUCCESS | setDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-GRAFT-REMOVE][SINGLETON-CONTROL] {_removeDescriptorFromFilesystem} | forcing ungraft|unmount | dropDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-GRAFT][SINGLETON-CONTROL] {%!{(MISSING)public}@} | grafting|mounting | chosenDownloadedDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-GRAFT][SINGLETON-CONTROL] {%!{(MISSING)public}@} | graft|mount ERROR| error:%!{(MISSING)public}@ | chosenDownloadedDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-GRAFT][SINGLETON-CONTROL] {%!{(MISSING)public}@} | graft|mount SUCCESS | chosenDownloadedDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-GRAFT][STARTUP] {AttemptNextGraft} | grafting|mounting | nextToGraft:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-MAP] {%!{(MISSING)public}@} | map-to-exclave ERROR | error:%!{(MISSING)public}@ | mapDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-MAP] {%!{(MISSING)public}@} | map-to-exclave SUCCESS | mapDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-MAP] {%!{(MISSING)public}@} | mapping-to-exclave | mapDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-PERSONALIZATION-GRAFT][SINGLETON-CONTROL] {%!{(MISSING)public}@} | performing personalize+graft|mount | chosenDownloadedDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-PERSONALIZATION-GRAFT][SINGLETON-CONTROL] {%!{(MISSING)public}@} | personalize+graft ERROR | error:%!{(MISSING)public}@ | chosenDownloadedDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-PERSONALIZATION-GRAFT][SINGLETON-CONTROL] {%!{(MISSING)public}@} | personalize+graft SUCCESS | chosenDownloadedDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-PERSONALIZATION-GRAFT][SINGLETON-CONTROL] {IssueClientReplyJobResponse} | personalize/graft ERROR | error:%!{(MISSING)public}@ chosenDownloadedDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-PERSONALIZATION-GRAFT][SINGLETON-CONTROL] {IssueClientReplyJobResponse} | personalize/graft SUCCESS | chosenDownloadedDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-PERSONALIZATION-GRAFT][SINGLETON-CONTROL] {IssueClientReplyJobResponse} | triggering personalize+graft | chosenDownloadedDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-PERSONALIZATION-REMOVE][SINGLETON-CONTROL] {_removeDescriptorFromFilesystem} | depersonalizing | dropDescriptor:%!{(MISSING)public}@"
- "\n[SECURE][AUTO-PERSONALIZATION][STARTUP] {AttemptNextPersonalize} attempting to pre-personalize | nextToPersonalize:%!{(MISSING)public}@"
- "\n[SET-STATUS] {%!{(MISSING)public}@:updateAutoAssetSetStatus} final status reported without found information | setIdentifier:%!{(MISSING)public}@ | instance:%!{(MISSING)public}@"
- "\n[SET-STATUS] {%!{(MISSING)public}@:updateAutoAssetSetStatus} no download progress (%!{(MISSING)public}@) | setIdentifier:%!{(MISSING)public}@ | setJobFinalStatus:%!{(MISSING)public}@"
- "\n[SET-STATUS] {%!{(MISSING)public}@:updateAutoAssetSetStatus} no final status determined (%!{(MISSING)public}@) | setIdentifier:%!{(MISSING)public}@"
- "\n{%!{(MISSING)public}@} [SET-DESCRIPTOR] checking whether set descriptor is currently locked | setDescriptorLocked:%!{(MISSING)public}@ | setDescriptor:%!{(MISSING)public}@"
- "\n{chooseNewerSetStatus} left:%!{(MISSING)public}@"
- "\n{chooseNewerSetStatus} right:%!{(MISSING)public}@"
- "%!@(MISSING)|statusBySelector:%!l(MISSING)d(set:%!l(MISSING)d)|jobsByInstance:%!l(MISSING)d(setJobsByID:%!l(MISSING)d)|jobsByUUID:%!l(MISSING)d|lookupGrants:%!l(MISSING)d|setConfigs:%!l(MISSING)d|atomicInstances:%!l(MISSING)d|downloaded:%!l(MISSING)d(set:%!l(MISSING)d)|scheduledSelectors:%!l(MISSING)d|timedOps:%!l(MISSING)d|clientRequests:%!l(MISSING)d|awaitingSync:%!l(MISSING)d|awaitingUnlock:%!l(MISSING)d|awaitingResume:%!l(MISSING)d"
- "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [OPTIONAL] (unarchivedSize=0) | stagedDescriptor:%!{(MISSING)public}@"
- "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [OPTIONAL] | nextAvailableDescirptor:%!{(MISSING)public}@"
- "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [OPTIONAL] | stagedDescriptor:%!{(MISSING)public}@"
- "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [REQUIRED] (unarchivedSize=0) | stagedDescriptor:%!{(MISSING)public}@"
- "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [REQUIRED] | nextAvailableDescirptor:%!{(MISSING)public}@"
- "%!{(MISSING)public}@\n[AUTO-STAGER] {%!{(MISSING)public}@} [REQUIRED] | stagedDescriptor:%!{(MISSING)public}@"
- "%!{(MISSING)public}@\n[AUTO-STAGER] {NextAwaitingBeginDownload} unable to form autoAssetCatalog | stagingDescriptor:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {%!{(MISSING)public}@:doneWithAllJobs} cleared active-jobs"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {%!{(MISSING)public}@:doneWithAllJobs} replied so dropping job:%!{(MISSING)public}@}"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {%!{(MISSING)public}@:replyToJobsWhenCatalogDownloaded} continuing job:%!{(MISSING)public}@}"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {%!{(MISSING)public}@:replyToJobsWhenCatalogDownloaded} continuing non-determine-job:%!{(MISSING)public}@}"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {%!{(MISSING)public}@:replyToJobsWhenCatalogDownloaded} continuing set-job check-atomic - awaiting download | jobParam:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {%!{(MISSING)public}@:replyToJobsWhenCatalogDownloaded} continuing without-client-request-job:%!{(MISSING)public}@}"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {%!{(MISSING)public}@:replyToJobsWhenCatalogDownloaded} dropping determine-job:%!{(MISSING)public}@}"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {%!{(MISSING)public}@:replyToJobsWhenCatalogDownloaded} replied so dropping job:%!{(MISSING)public}@}"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {%!{(MISSING)public}@:replyToJobsWhenLookupFailed} continuing job | jobParam:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {%!{(MISSING)public}@:replyToJobsWhenLookupFailed} continuing without-client-request-job | jobParam:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {_autoAssetJobFinished} cleared"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {addToActiveJobTasks} added job:%!{(MISSING)public}@}"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {removeCurrentJobTask} removed job:%!{(MISSING)public}@}"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {replyToSetCheckAtomicDownloadSuccess} continuing job | jobParam:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {replyToSetCheckAtomicDownloadSuccess} continuing without-client-request-job | jobParam:%!{(MISSING)public}@"
- "%!{(MISSING)public}@ | ACTIVE_JOB_TASKS: {replyToSetCheckAtomicDownloadSuccess} replied so dropping job:%!{(MISSING)public}@}"
- "%!{(MISSING)public}@ | unable to create persisted-state for existing file:%!{(MISSING)public}@ | %!{(MISSING)public}@[%!{(MISSING)public}@]"
- "+[SecureMobileAssetBundle getSigningServerURL]"
- "-[ControlManager handleQueryRequest:clientName:connection:message:]_block_invoke"
- "-[ControlManager handleQueryRequest:clientName:connection:message:]_block_invoke_3"
- "-[DownloadManager _logResponseBody:nonce:]"
- "2.1.12"
- "2.2.4"
- "?\x0f\x1f\a\x11\"Rd"
- "Adding %!@(MISSING) : %!@(MISSING) to analytics payload"
- "Additional AnalyticsInfo for task : %!@(MISSING)"
- "AssetSpecifiers"
- "ErasseAcceptedRemoveAll"
- "Failed to load %!@(MISSING)"
- "Failed to ungraft/unmount %!@(MISSING): %!@(MISSING)"
- "Starting built-in MobileAsset brain built Jul 19 2024 18:02:56"
- "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Jul 19 2024 18:02:56"
- "The asset receipt is null, adding anyway as it is optional 1"
- "[%!{(MISSING)public}@]\n[ASSET_STATUS][%!{(MISSING)public}@] | statusKey:%!{(MISSING)public}@ | currentStatus:%!{(MISSING)public}@ | jobUUID:%!{(MISSING)public}@ | downloading:%!{(MISSING)public}@ | baseForPatch:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[ASSET_STATUS][ASSOCIATED] | statusKey:%!{(MISSING)public}@ | currentStatus:%!{(MISSING)public}@ "
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {%!{(MISSING)public}@e} (%!{(MISSING)public}@) NOT removing by UUID | setAtomicInstanceUUID:%!{(MISSING)public}@ | nextSetAtomicInstance:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {%!{(MISSING)public}@} cannot remove - currently locked | jobDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {%!{(MISSING)public}@} cannot remove - currently locked | nextSetDescriptor:%!{(MISSING)public}@ | entryID:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {%!{(MISSING)public}@} cannot remove - no newer downloaded descriptor | jobDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {%!{(MISSING)public}@} cannot remove - part of latest atomic-instance to vend | downloadedAssetDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {%!{(MISSING)public}@} cannot remove - part of latest atomic-instance to vend | jobDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {%!{(MISSING)public}@} cannot remove - part of latest atomic-instance to vend | setDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {%!{(MISSING)public}@} not considering for removal since currently locked | keepingDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {%!{(MISSING)public}@} not considering for removal since found by lookup with asset-version | keepingDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {%!{(MISSING)public}@} not considering for removal since no newer on filesystem | keepingDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {_removeDownloadedDescriptorsWithNewerDownloaded} no persisted known-descriptors"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {_removeUnlockedForOlderSelectorsWithoutVersion} cannot remove - part of latest atomic-instance to vend | downloadedDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@]\n[CONSIDER-REMOVAL] {loadPersistedCrossCheckTrimAtomicInstances} preserving previously staged | setAtomicInstance:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] %!{(MISSING)public}@ | %!{(MISSING)public}@ | currentSetStatus:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] INITIAL_SET_STATUS | currentSetStatus:%!{(MISSING)public}@ | jobUUID:%!{(MISSING)public}@ | assignedSetDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {%!{(MISSING)public}@:_latestDownloadedDescriptor} first found as potential latest | descriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {%!{(MISSING)public}@:_latestDownloadedDescriptor} later version as potential latest | descriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {%!{(MISSING)public}@:_latestDownloadedDescriptor} not considering older version | descriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {%!{(MISSING)public}@} | NOT eliminating nextSetAtomicInstance:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {QueueClientRequestBefore1st} [CLIENT_REQUESTS_AWAITING_SYNC] | added client-request | eventInfo:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {QueueClientRequest} [CLIENT_REQUESTS_AWAITING_SYNC] | added client-request | eventInfo:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {RouteClientClosed} | client closed connection (allowing any previous client-requests to proceed) | eventInfo:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {loadPersistedDescriptors} content on filesystem validated | entryID:%!{(MISSING)public}@, adoptedDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {loadPersistedSetAtomicInstances} content on filesystem validated | entryID:%!{(MISSING)public}@, adoptedDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {loadPersistedSetConfigurations} content on filesystem validated | entryID:%!{(MISSING)public}@, adopted setConfiguration:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {loadPersistedSetDownloadedDescriptors} content on filesystem validated | entryID:%!{(MISSING)public}@, adoptedSetDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {loadPersistedSetLookupResults} content on filesystem validated | entryID:%!{(MISSING)public}@, adopted setLookupResult:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {loadPersistedSetTargets} content on filesystem validated | entryID:%!{(MISSING)public}@, adopted setTarget:%!{(MISSING)public}@"
- "[CONTROL_MANAGER_ASSET_QUEUE] {dumpClientUsage} ...dumping usage"
- "[CONTROL_MANAGER_ASSET_QUEUE] {dumpClientUsage} dumping usage..."
- "[CONTROL_MANAGER_ASSET_QUEUE] {handleQueryRequest} !getDownloadState | ...determineAssets"
- "[CONTROL_MANAGER_ASSET_QUEUE] {handleQueryRequest} !getDownloadState | determineAssets..."
- "[CONTROL_MANAGER_ASSET_QUEUE] {handleQueryRequest} getDownloadState | ...determineAssets"
- "[CONTROL_MANAGER_ASSET_QUEUE] {handleQueryRequest} getDownloadState | determineAssets..."
- "[CONTROL_MANAGER_ASSET_QUEUE] {handleUpdateClientUsage} ...updating usage"
- "[CONTROL_MANAGER_ASSET_QUEUE] {handleUpdateClientUsage} updating usage..."
- "[OSVersion:%!@(MISSING)|Build:%!@(MISSING)|GroupNames:%!@(MISSING)|LookupResults:%!l(MISSING)d]"
- "[clientDomain:%!@(MISSING)|setID:%!@(MISSING)|configEntries:%!@(MISSING)|instancesDownloaded:%!@(MISSING)|(catalog)CachedAssetSetID:%!@(MISSING),DownloadedFromLive:%!@(MISSING),LastTimeChecked:%!@(MISSING),PostedDate:%!@(MISSING)|newerInstanceDiscovered:%!@(MISSING)|newerDiscoveredAtomicEntries:%!@(MISSING)|latestDownloadedInstance:%!@(MISSING)|latestDownloadedEntries:%!@(MISSING)|(downloaded)CachedAssetSetID:%!@(MISSING),DownloadedFromLive:%!@(MISSING),LastTimeChecked:%!@(MISSING),PostedDate:%!@(MISSING)|notifications:%!@(MISSING)|(policy)need:%!@(MISSING),scheduler:%!@(MISSING),stager:%!@(MISSING)|downloadUserInitiated:%!@(MISSING)|downloadProgress:%!@(MISSING)|downloadedNetworkBytes:%!l(MISSING)d|downloadedFilesystemBytes:%!l(MISSING)d|currentLockUsage:%!@(MISSING)|selectosForStaging:%!@(MISSING)|availableForUseError:%!@(MISSING)|newerVersionError:%!@(MISSING)]"
- "[clientInstance:%!@(MISSING)|clientDesire:%!@(MISSING)|setDescriptor:%!@(MISSING)|currentSetStatus:%!@(MISSING)]"
- "[clientInstance:%!@(MISSING)|clientDesire:%!@(MISSING)|setDescriptor:%!@(MISSING)|foundContent:%!@(MISSING)]"
- "_countOfEntriesDictionaryOfDictionary:"
- "_logResponseBody:nonce:"
- "discovered-atomic-instance"
- "discovered-different-downloaded-atomic-instance"
- "discovered-matching-downloaded-atomic-instance"
- "downloaded-atomic-instance"
- "getSigningServerURL"
- "no-atomic-instance"
- "nonce is: %!@(MISSING) and no response assets were found in the response"
- "nonce is: %!@(MISSING) and the body for asset #%!l(MISSING)d is: %!@(MISSING)"
- "set-job ended with all content downloaded but some secure auto-assets require personalization"
- "the Pallas response nonce is: %!@(MISSING) total asset count is: %!l(MISSING)d and the body is: %!@(MISSING)"
- "unable to locate set-lookup-results"
- "{%!{(MISSING)public}@:_doesSetDescriptorRequirePersonalization} secure asset-descriptor that is not presonalized+grafted/mounted | nextAssetDescriptor:%!{(MISSING)public}@"
- "{%!{(MISSING)public}@:_doesSetDescriptorRequirePersonalization} set-descriptor personalized check | requiresPersonalization:%!{(MISSING)public}@ | downloadedSetDescriptor:%!{(MISSING)public}@"
- "{%!{(MISSING)public}@:_isSetDescriptorAvailableToClient} secure asset-descriptor that is not presonalized | nextAssetDescriptor:%!{(MISSING)public}@"
- "{%!{(MISSING)public}@:_isSetDescriptorAvailableToClient} secure asset-descriptor that is not presonalized+grafted/mounted | nextAssetDescriptor:%!{(MISSING)public}@"
- "{%!{(MISSING)public}@:_isSetDescriptorAvailableToClient} set-descriptor available check | setAvailableToClient:%!{(MISSING)public}@ | downloadedSetDescriptor:%!{(MISSING)public}@"
- "{%!{(MISSING)public}@} [CHECK-SET-DESCRIPTOR] checking set-descriptor | setDescriptor:%!{(MISSING)public}@"
- "{%!{(MISSING)public}@} forcing unlocked of set-configuration | setConfiguration:%!{(MISSING)public}@"
- "{PromoteStagedMigrate} | set-lookup-results when had previous lookup-results"
- "{_autoAssetJobProgressNewValidatedCurrentStatus} | no jobInformation.initialAssetSelector so no client should be receiving progress [probable failed scheduled job]"
- "{_autoAssetSetJobProgressNewValidatedCurrentStatus} | no setJobInformation.currentSetStatus.assetSetIdentifier so no client should be receiving progress [probable failed scheduled job]"
- "{_autoAssetSetJobProgressNewValidatedCurrentStatus} | no setJobInformation.currentSetStatus.clientDomainName so no client should be receiving progress [probable failed scheduled job]"
- "{_autoAssetSetJobProgressNewValidatedCurrentStatus} | no setJobInformation.currentSetStatus.downloadProgress"
- "{autoAssetJobIssueProgress} | no client requests to report progress to"
- "{loadPersistedCrossCheckTrimSetDescriptors} [KEEP-SET-DESCRIPTOR] set-descriptor with atomic-instance | setDescriptor:%!{(MISSING)public}@"
- "{writeDictionaryToFile} notifying download manager move complete | taskDescriptor:%!@(MISSING)"

```
