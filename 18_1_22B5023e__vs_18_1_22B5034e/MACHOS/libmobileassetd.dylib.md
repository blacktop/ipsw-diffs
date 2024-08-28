## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1309.40.28.502.1
-  __TEXT.__text: 0x25809c
-  __TEXT.__auth_stubs: 0x23a0
-  __TEXT.__objc_stubs: 0x1f460
-  __TEXT.__objc_methlist: 0xecc0
+1309.40.54.502.1
+  __TEXT.__text: 0x25a884
+  __TEXT.__auth_stubs: 0x2370
+  __TEXT.__objc_stubs: 0x1f6a0
+  __TEXT.__objc_methlist: 0xedc8
   __TEXT.__const: 0x494e
-  __TEXT.__objc_methname: 0x35f0e
-  __TEXT.__cstring: 0x4bc7c
+  __TEXT.__objc_methname: 0x36678
+  __TEXT.__cstring: 0x4c0ec
   __TEXT.__objc_classname: 0xd7b
-  __TEXT.__objc_methtype: 0x3360
-  __TEXT.__oslogstring: 0x2f80c
-  __TEXT.__gcc_except_tab: 0x250c
+  __TEXT.__objc_methtype: 0x33f4
+  __TEXT.__oslogstring: 0x2f8db
+  __TEXT.__gcc_except_tab: 0x251c
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x10c4
   __TEXT.__constg_swiftt: 0x1530

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x46c8
+  __TEXT.__unwind_info: 0x46e8
   __TEXT.__eh_frame: 0x30c4
-  __DATA_CONST.__auth_got: 0x11e0
+  __DATA_CONST.__auth_got: 0x11c8
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x9c8
-  __DATA_CONST.__const: 0x65b0
-  __DATA_CONST.__cfstring: 0x30ea0
+  __DATA_CONST.__const: 0x6660
+  __DATA_CONST.__cfstring: 0x311e0
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x89a8
+  __DATA_CONST.__objc_selrefs: 0x8a38
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x960
   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x14288
+  __DATA.__objc_const: 0x14378
   __DATA.__objc_classrefs: 0x7a0
   __DATA.__objc_superrefs: 0x2e8
-  __DATA.__objc_ivar: 0x1248
+  __DATA.__objc_ivar: 0x125c
   __DATA.__objc_data: 0xd10
   __DATA.__data: 0x2608
   __DATA.__bss: 0x53a0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8198
-  Symbols:   14705
-  CStrings:  15573
+  Functions: 8220
+  Symbols:   14754
+  CStrings:  15628
 
Symbols:
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1063
+ _objc_msgSend$setConfigurationPersist:fromLocation:dueToAlter:
+ __block_literal_global.1454
+ __block_literal_global.915
+ OBJC_IVAR_$_MANAutoAssetSetStatus._haveReceivedLookupResponse
+ _objc_msgSend$reportIfSetPallasResponseReceived:
+ _objc_msgSend$setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:
+ -[MADAutoAssetJob setSetCheckAwaitingDownload:]
+ -[MADAutoAssetControlManager setConfigurationsRefreshStaleIndications]
+ __block_literal_global.2031
+ -[MADAutoAssetControlManager setSecureHealingPersonalizationAttempted:]
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1022
+ -[MADAnalyticsManager recordPushNotification:assetType:cloudChannel:forPopulationType:userInitiated:interestAcrossTerm:lockAcrossReboot:lockAcrossTermination:]
+ __block_literal_global.1537
+ __block_literal_global.962
+ __block_literal_global.1999
+ __block_literal_global.952
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1118
+ _objc_msgSend$setConfigurationsRefreshStaleIndications
+ __block_literal_global.1019
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1038
+ __block_literal_global.931
+ __block_literal_global.1174
+ -[MANAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ ___block_descriptor_72_e8_32s40s48r56r64r_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24ls32l8r48l8r56l8r64l8s40l8
+ __block_literal_global.1170
+ __block_literal_global.2023
+ __block_literal_global.2212
+ __block_literal_global.951
+ __block_literal_global.2047
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1085
+ GCC_except_table537
+ -[MADAutoAssetJob reportIfSetPallasResponseReceived:]
+ _objc_msgSend$setHaveReceivedLookupResponse:
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1053.cold.1
+ __block_literal_global.1991
+ __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.952
+ __block_literal_global.2015
+ __block_literal_global.1179
+ _objc_msgSend$_isSetDescriptorAvailableToClient:forSetDescriptor:
+ ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ -[MADAutoAssetControlManager action_IssueClientReplySetJob:error:].cold.3
+ __block_literal_global.2039
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1009
+ __block_literal_global.4128
+ _objc_msgSend$setCheckAwaitingDownload
+ -[MADAutoSetConfiguration haveReceivedLookupResponse]
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2826
+ GCC_except_table534
+ __block_literal_global.3201
+ _objc_msgSend$autoAssetJobSetLookupResponseReceived:
+ -[MADAutoAssetControlManager action_SetJobLookupResponseRcvd:error:]
+ _objc_msgSend$_maDownloadErrorIndicatesResponseNoContent:
+ -[MADAutoAssetControlManager _haveReceivedLookupResponseForClientDomainName:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager addToTryPersonalize:forDescriptor:]
+ -[MADAutoAssetJob haveReceivedLookupResponse]
+ __block_literal_global.3345
+ __block_literal_global.1123
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2256.cold.1
+ _objc_msgSend$setConfigurationsUpdateLatestToVend:
+ __block_literal_global.1237
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1023
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2255
+ -[MADAutoAssetControlManager setConfigurationRefreshToVend:forSetConfiguration:fromStaged:]
+ __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1070
+ ___block_descriptor_73_e8_32s40s48r56r64r_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24ls32l8r48l8r56l8r64l8s40l8
+ ___block_descriptor_49_e8_32s40r_e5_v8?0lr40l8s32l8
+ __block_literal_global.3404
+ _objc_msgSend$recordPushNotification:assetType:cloudChannel:forPopulationType:userInitiated:interestAcrossTerm:lockAcrossReboot:lockAcrossTermination:
+ _objc_msgSend$securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:
+ __block_literal_global.1147
+ __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1095
+ ___121-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:]_block_invoke
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1053
+ __block_literal_global.3131
+ -[MADAutoAssetControlManager _isSetDescriptorAvailableToClient:forSetDescriptor:].cold.1
+ _objc_msgSend$recordPushNotification:assetType:cloudChannels:forPopulationType:userInitiated:interestAcrossTerm:lockAcrossReboot:lockAcrossTermination:
+ _objc_msgSend$securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:completion:
+ __block_literal_global.1276
+ __block_literal_global.1242
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1024
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2827
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2056
+ _MAPushNotificationPayloadLockAcrossTerminationKey
+ __block_literal_global.954
+ __block_literal_global.2261
+ _objc_msgSend$setSetCheckAwaitingDownload:
+ __block_literal_global.1540
+ _objc_msgSend$secureHealingPersonalizationAttempted
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80s88bs_e42_v24?0"MADAutoSetDescriptor"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1052
+ _objc_msgSend$initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ __block_literal_global.1212
+ __block_literal_global.1076
+ _objc_msgSend$initForSetJobIssueReply:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:withSetJobInformation:withResponseError:
+ _objc_msgSend$_haveReceivedLookupResponseForSetDescriptor:
+ __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1105
+ __block_literal_global.3203
+ __block_literal_global.1570
+ -[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:completion:]
+ OBJC_IVAR_$_MADAutoAssetControlManager._secureHealingPersonalizationAttempted
+ -[MADAutoAssetJob setCheckAwaitingDownload]
+ OBJC_IVAR_$_MADAutoSetConfiguration._haveReceivedLookupResponse
+ -[MADAutoSetConfiguration setHaveReceivedLookupResponse:]
+ __block_literal_global.943
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1118.cold.1
+ -[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:]
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1069
+ _MAPushNotificationPayloadUserInitiatedKey
+ _objc_msgSend$action_SetJobLookupResponseRcvd:error:
+ -[MADAutoAssetJob _maDownloadErrorIndicatesResponseNoContent:]
+ _objc_msgSend$_haveReceivedLookupResponseForClientDomainName:forAssetSetIdentifier:
+ _objc_msgSend$haveReceivedLookupResponse
+ -[MADAutoAssetControlManager setConfigurationPersist:fromLocation:dueToAlter:]
+ -[MADAutoAssetControlManager _isSetDescriptorAvailableToClient:forSetDescriptor:]
+ __block_literal_global.1055
+ _objc_msgSend$setConfigurationRefreshToVend:forSetConfiguration:fromStaged:
+ ___121-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:completion:]_block_invoke_2
+ __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1095.cold.1
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1084
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.993
+ __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1065
+ OBJC_IVAR_$_MADAutoAssetJob._setCheckAwaitingDownload
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1055.cold.1
+ ___block_descriptor_89_e8_32s40s48s56s64s72bs80bs_e8_v12?0B8ls32l8s40l8s48l8s72l8s56l8s80l8s64l8
+ -[MADAutoAssetControlManager setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:]
+ GCC_except_table539
+ __block_literal_global.2007
+ __block_literal_global.1021
+ __block_literal_global.1531
+ ___121-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:completion:]_block_invoke
+ __block_literal_global.941
+ __block_literal_global.1154
+ -[MANAutoAssetSetStatus haveReceivedLookupResponse]
+ __block_literal_global.901
+ -[MADAutoAssetControlManager setConfigurationsUpdateLatestToVend:]
+ __block_literal_global.922
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1074
+ __block_literal_global.1527
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2256
+ __block_literal_global.1181
+ -[MADAutoAssetControlManager action_SetJobLookupResponseRcvd:error:].cold.1
+ __block_literal_global.1532
+ __block_literal_global.938
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.989
+ __block_literal_global.1668
+ -[MADAutoAssetControlManagerParam initForSetJobIssueReply:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:withSetJobInformation:withResponseError:]
+ -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:]
+ __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.932
+ -[MANAutoAssetSetStatus setHaveReceivedLookupResponse:]
+ -[MADAutoAssetJob setHaveReceivedLookupResponse:]
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1022
+ _objc_msgSend$setSecureHealingPersonalizationAttempted:
+ -[MADAnalyticsManager recordPushNotification:assetType:cloudChannels:forPopulationType:userInitiated:interestAcrossTerm:lockAcrossReboot:lockAcrossTermination:]
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1125
+ __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1066
+ __block_literal_global.988
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1039
+ -[MADAutoAssetControlManager secureHealingPersonalizationAttempted]
+ __block_literal_global.2812
+ __block_literal_global.1437
+ __block_literal_global.947
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1055
+ _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:
+ _MAPushNotificationPayloadLockAcrossRebootKey
+ _objc_msgSend$newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ -[MADAutoAssetControlManager _haveReceivedLookupResponseForSetDescriptor:]
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1031
+ __block_literal_global.986
+ +[MADAutoAssetControlManager autoAssetJobSetLookupResponseReceived:]
+ __block_literal_global.1980
+ _objc_msgSend$addToTryPersonalize:forDescriptor:
+ ___121-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:]_block_invoke_2
+ GCC_except_table374
+ -[MADAutoAssetControlManager newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ OBJC_IVAR_$_MADAutoAssetJob._haveReceivedLookupResponse
+ __block_literal_global.957
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1083
- __block_literal_global.1003
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2791
- -[MADAutoAssetControlManager setConfigurationPersist:fromLocation:]
- ___91+[MADAutoAssetSecure ungraftAll:forSetDescriptor:withAutoAssetDescriptors:ungraftingError:]_block_invoke
- __block_literal_global.4062
- __block_literal_global.2016
- ___94-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:]_block_invoke
- __block_literal_global.3107
- __block_literal_global.968
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.971
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1061
- -[MADAutoAssetControlManager _isSetDescriptorAvailableToClient:forSetDescriptor:requiringSecureGrafted:].cold.1
- -[MADAutoAssetControlManager setConfigurationsUpdateLatestToVend]
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1020
- _objc_msgSend$setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:requiringPersonalized:
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1107
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1051
- _objc_msgSend$newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
- __block_literal_global.1136
- -[MADAutoAssetJob action_PersonalizeFailureDecideMore:error:].cold.1
- __block_literal_global.1552
- __block_literal_global.2008
- __block_literal_global.1156
- _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:
- _objc_msgSend$setConfigurationPersist:fromLocation:
- __block_literal_global.1105
- __block_literal_global.1965
- +[MADAutoAssetControlManager autoSetJobIssueReply:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:fromAutoAssetJob:withSetJobInformation:withResponseError:].cold.1
- __block_literal_global.1976
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1060
- -[MADAutoAssetControlManager setConfigurationRefreshToVend:forSetConfiguration:fromStaged:fromMigrated:requiringPersonalized:]
- __block_literal_global.2194
- __block_literal_global.3177
- __block_literal_global.3179
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1004
- ___block_descriptor_88_e8_32s40s48s56s64s72bs80bs_e8_v12?0B8ls32l8s40l8s48l8s72l8s56l8s80l8s64l8
- __block_literal_global.1152
- __block_literal_global.929
- ___block_descriptor_72_e8_32s40s48r56r_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24ls32l8r48l8r56l8s40l8
- __block_literal_global.2776
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.975
- __block_literal_global.936
- __block_literal_global.2000
- __block_literal_global.1258
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1013
- -[MADAutoAssetControlManager newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
- __block_literal_global.1519
- -[MADAutoAssetControlManager setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:requiringPersonalized:]
- ___94-[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:]_block_invoke_2
- __block_literal_global.1058
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1038
- __block_literal_global.1513
- _pthread_self
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2790
- GCC_except_table532
- __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1048
- _objc_msgSend$securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:
- _objc_msgSend$setConfigurationRefreshToVend:forSetConfiguration:fromStaged:fromMigrated:requiringPersonalized:
- __block_literal_global.1161
- __block_literal_global.1650
- -[MADAutoAssetControlManager _isSetDescriptorAvailableToClient:forSetDescriptor:requiringSecureGrafted:]
- __block_literal_global.2024
- __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1047
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.914
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1034
- __block_literal_global.897
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1035.cold.1
- __block_literal_global.1163
- __block_literal_global.920
- _pthread_get_qos_class_np
- __block_literal_global.1514
- __block_literal_global.1001
- -[MADAutoAssetControlManager securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:]
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1006
- __block_literal_global.939
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.991
- __block_literal_global.923
- GCC_except_table368
- _objc_msgSend$initForSetJobIssueReply:forDomainName:forAssetSetIdentifier:withSetAtomicInstance:withAutoAssetUUID:withSetJobInformation:withResponseMessage:withResponseError:
- __block_literal_global.1509
- __block_literal_global.3327
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2041
- __block_literal_global.926
- __63+[MADAutoSetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.934
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1037.cold.1
- __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1081
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1100.cold.1
- __block_literal_global.916
- __block_literal_global.2032
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1021
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2240
- __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1071.cold.1
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1059
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2241.cold.1
- __block_literal_global.883
- __block_literal_global.1219
- ___block_descriptor_73_e8_32s40s48r56r_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24ls32l8r48l8r56l8s40l8
- GCC_except_table530
- __block_literal_global.970
- _objc_msgSend$_isSetDescriptorAvailableToClient:forSetDescriptor:requiringSecureGrafted:
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1045
- __block_literal_global.1419
- __block_literal_global.1037
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2241
- __block_literal_global.907
- __block_literal_global.1194
- -[MADAutoAssetControlManagerParam initForSetJobIssueReply:forDomainName:forAssetSetIdentifier:withSetAtomicInstance:withAutoAssetUUID:withSetJobInformation:withResponseMessage:withResponseError:]
- GCC_except_table527
- __block_literal_global.1522
- __block_literal_global.1992
- -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:]
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1100
- _pthread_set_qos_class_self_np
- __block_literal_global.1436
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1004
- __block_literal_global.1984
- __block_literal_global.895
- __block_literal_global.942
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e42_v24?0"MADAutoSetDescriptor"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1037
- __block_literal_global.1129
- __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1071
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1005
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1035
- __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1052
- __block_literal_global.1224
- __block_literal_global.904
- __block_literal_global.2243
- _objc_msgSend$setConfigurationsUpdateLatestToVend
CStrings:
+ "setConfigurationRefreshToVend:forSetConfiguration:fromStaged:"
+ "PersonalizeSuccessDecideMore[NEED-GRAFTING]"
+ "setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:"
+ "DecideNeedPersonalize[BEFORE-PERSONALIZING]"
+ "LockAcrossReboot"
+ "securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:fallingBackToSetDescriptor:"
+ "JobSetLookupResponseReceived"
+ "setSecureHealingPersonalizationAttempted:"
+ "[%!{(MISSING)public}@] {%!{(MISSING)public}@} lock-atomic found newer and latest | newerDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "setConfigurationsRefreshStaleIndications"
+ "SetJobLookupResponseRcvd"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "_setCheckAwaitingDownload"
+ "initForSetJobIssueReply:forDomainName:forAssetSetIdentifier:withAutoAssetUUID:withSetJobInformation:withResponseError:"
+ "reportIfSetPallasResponseReceived:"
+ "setCheckAwaitingDownload"
+ "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] unable to replace latestAtomicInstanceToVend (unable to fully personalize) | setConfiguration:%!{(MISSING)public}@"
+ "{IssueClientReplySetJob} unable to allocate basis for response message | clientRequest:%!{(MISSING)public}@"
+ "TB,N,V_setCheckAwaitingDownload"
+ "newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "com.apple.mobileassetd.notifications.push"
+ "TB,N,V_haveReceivedLookupResponse"
+ "securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:replyingOnError:completion:"
+ "@64@0:8@16@24@32q40B48B52B56B60"
+ "%!{(MISSING)public}@\n[AUTO-SECURE][AUTO-PERSONALIZATION] {PersonalizeHealFailureDecideMore} will not make any additional personalization attempts | tryPersonalizeFailed:%!@(MISSING)"
+ "{%!@(MISSING)} set-descriptor without latest-to-vend | setDescriptor:%!@(MISSING)"
+ "[(client)Domain:%!@(MISSING),Name:%!@(MISSING)|(set)Identifier:%!@(MISSING),Entries:%!l(MISSING)d|latestToVend:%!@(MISSING)|inhibitScheduling:%!@(MISSING)|lookupRsp:%!@(MISSING)]"
+ "\n[SET-CONFIGURATION]{%!{(MISSING)public}@} unable to load set-configuration | setConfigurationKey:%!{(MISSING)public}@"
+ "encountered set-descriptor being eliminated | setDescriptor:%!@(MISSING)"
+ "Attempting to read AppleConnect SSO token with %!s(MISSING) interactivity level"
+ "_haveReceivedLookupResponseForClientDomainName:forAssetSetIdentifier:"
+ "encountered set-descriptor with auto-asset being eliminated | nextDownloadedDescriptor:%!@(MISSING)"
+ "CloudChannel"
+ "[overall]instance:%!@(MISSING),selector:%!@(MISSING),UUID:%!@(MISSING),logger:%!@(MISSING),tasks:%!l(MISSING)u,requests:%!l(MISSING)d,table:%!@(MISSING),FSM:%!@(MISSING),sched:%!@(MISSING),NWFail:%!@(MISSING)|beingCancled:%!@(MISSING)|[earlier]sched:%!@(MISSING),NWFail:%!@(MISSING)|bonded:%!@(MISSING)|[active]instance:%!@(MISSING),desire:%!@(MISSING)(awaitDownload:%!@(MISSING),checkAwait:%!@(MISSING)),found:%!@(MISSING),end:%!@(MISSING),listen:%!@(MISSING),jobInfo:%!@(MISSING)|[aggregated]policy:%!@(MISSING),clientRequested:%!@(MISSING)|firstClientName:%!@(MISSING),triggeringLayer:%!@(MISSING)|onFilesystemByVersion:%!l(MISSING)d|[check]Base:%!@(MISSING),UUID:%!@(MISSING),lookupGrant:%!@(MISSING),rampFG:%!@(MISSING),rampLatch:%!@(MISSING),options:%!@(MISSING)|[asset]base:%!@(MISSING),patch:%!@(MISSING),full:%!@(MISSING),newer:%!@(MISSING),downloading:%!@(MISSING),scheduler:%!@(MISSING),lookupRsp:%!@(MISSING),user:%!@(MISSING),boosting:%!@(MISSING),checking:%!@(MISSING),determining:%!@(MISSING),locking:%!@(MISSING),patched:%!@(MISSING)|[installed]:version:%!@(MISSING),build:%!@(MISSING)|[status]current:%!@(MISSING),progress:%!@(MISSING),lastPatch:%!@(MISSING)|[results]selector:%!@(MISSING),instance:%!@(MISSING),found:%!@(MISSING),end:%!@(MISSING),listen:%!@(MISSING),[set]aggregatedPolicy:%!@(MISSING),descriptor:%!@(MISSING),next:%!l(MISSING)d,found:%!@(MISSING)"
+ "setConfigurationPersist:fromLocation:dueToAlter:"
+ "set-job without set-configuration"
+ "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] unable to replace latestAtomicInstanceToVend (requires personalization) | setDescriptorToUpdate:%!{(MISSING)public}@"
+ "unable to end access | nextUngraftDescriptor:%!@(MISSING)"
+ "[%!@(MISSING) | instance latestDownloaded:%!@(MISSING)(entries:%!l(MISSING)d)%!@(MISSING), discovered:%!@(MISSING)(entries:%!l(MISSING)d)%!@(MISSING), requestedEntries:%!l(MISSING)d, fullyDownloaded:%!@(MISSING)(notified:%!@(MISSING)) | onFilesystem:%!@(MISSING)(incomplete:%!@(MISSING)), neverBeenLocked:%!@(MISSING) | secureOperation(inProgress:%!@(MISSING)), (elimintating:%!@(MISSING)) | userInitiated:%!@(MISSING), stagedPrior:%!@(MISSING)]"
+ "setConfigurationsUpdateLatestToVend:"
+ "no secureAssetBundle | nextUngraftDescriptor:%!@(MISSING)"
+ "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {%!{(MISSING)public}@} will attempt personalization count:%!l(MISSING)d | secureDescriptor:%!{(MISSING)public}@"
+ "\n[SECURE][%!{(MISSING)public}@][SET-CONTROL][ELIMINATE] {%!{(MISSING)public}@} set-identifier eliminate while performing secure operation(s) | nextDownloadedDescriptor:%!{(MISSING)public}@"
+ "_secureHealingPersonalizationAttempted"
+ "Using value set in asset specific default(%!@(MISSING)) for baseURL(%!@(MISSING))"
+ "[clientName:%!@(MISSING)|setEntries:%!l(MISSING)d|latestToVend:%!@(MISSING)|inhibitScheduling:%!@(MISSING)|lookupRsp:%!@(MISSING)]"
+ "Starting built-in MobileAsset brain built Aug 22 2024 20:07:49"
+ "secureHealingPersonalizationAttempted"
+ "PersonalizeSuccessDecideMore[NO-GRAFTING]"
+ "{%!@(MISSING)} atomic-instance entry no longer on the filesystem | nextAtomicEntry:%!@(MISSING) | setConfiguration:%!@(MISSING)"
+ "TB,N,V_secureHealingPersonalizationAttempted"
+ "_haveReceivedLookupResponse"
+ "2.2.13"
+ "_maDownloadErrorIndicatesResponseNoContent:"
+ "LockAcrossTermination"
+ "%!{(MISSING)public}@\n[AUTO-SECURE][AUTO-PERSONALIZATION] {PersonalizeFailureDecideMore} will not make any additional personalization attempts | tryPersonalizeFailed:%!@(MISSING)"
+ "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Aug 22 2024 20:07:49"
+ "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] replaced latestAtomicInstanceToVend | setConfiguration:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@\n[%!{(MISSING)public}@] {%!{(MISSING)public}@} [STAGING-CLIENT-REPLY] replied earlier to staging-client (once REQUIRED staged)"
+ "@240@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168B176B180@184q192q200@208@216@224@232"
+ "[domain:%!@(MISSING)|setID:%!@(MISSING)|config:%!l(MISSING)d|AIs:%!l(MISSING)d(newer:%!@(MISSING)[%!l(MISSING)d])(latest:%!@(MISSING)[%!l(MISSING)d])|lookupRsp:%!@(MISSING)|user:%!@(MISSING)|locks:%!@(MISSING)]"
+ "Using value set in global default(%!@(MISSING)) for baseURL(%!@(MISSING)) for asset %!@(MISSING)"
+ "recordPushNotification:assetType:cloudChannel:forPopulationType:userInitiated:interestAcrossTerm:lockAcrossReboot:lockAcrossTermination:"
+ "@64@0:8@?16@24@32@40@48@56"
+ "action_SetJobLookupResponseRcvd:error:"
+ "addToTryPersonalize:forDescriptor:"
+ "                      clientDomainName: %!@(MISSING)\n                    assetSetIdentifier: %!@(MISSING)\n                configuredAssetEntries: %!@(MISSING)\n             atomicInstancesDownloaded: %!@(MISSING)\n               catalogCachedAssetSetID: %!@(MISSING)\n             catalogDownloadedFromLive: %!@(MISSING)\n                catalogLastTimeChecked: %!@(MISSING)\n                     catalogPostedDate: %!@(MISSING)\n         newerAtomicInstanceDiscovered: %!@(MISSING)\n          newerDiscoveredAtomicEntries: %!@(MISSING)\n              latestDownloadedInstance: %!@(MISSING)\n        latestDowloadedInstanceEntries: %!@(MISSING)\n     downloadedCatalogCachedAssetSetID: %!@(MISSING)\n   downloadedCatalogDownloadedFromLive: %!@(MISSING)\n      downloadedCatalogLastTimeChecked: %!@(MISSING)\n           downloadedCatalogPostedDate: %!@(MISSING)\n                  currentNotifications: %!@(MISSING)\n                     currentNeedPolicy: %!@(MISSING)\n                currentSchedulerPolicy: %!@(MISSING)\n                   currentStagerPolicy: %!@(MISSING)\n            haveReceivedLookupResponse: %!@(MISSING)\n                 downloadUserInitiated: %!@(MISSING)\n                      downloadProgress:\n%!@(MISSING)\n                downloadedNetworkBytes: %!l(MISSING)d\n             downloadedFilesystemBytes: %!l(MISSING)d\n                      currentLockUsage:\n%!@(MISSING)\n                   selectorsForStaging: %!@(MISSING)\n                  availableForUseError: %!@(MISSING)\n                     newerVersionError: %!@(MISSING)\n"
+ "{[0]%!@(MISSING):%!@(MISSING)}"
+ "%!@(MISSING):addToTryPersonalize"
+ "encountered set-descriptor with already in-progress secure-operation | setDescriptor:%!@(MISSING)"
+ "v52@0:8@16@24@32B40@?44"
+ "reportIfSetPallasResponseReceived"
+ "_isSetDescriptorAvailableToClient:forSetDescriptor:"
+ "@244@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176B184B188@192q200q208B216@220@228@236"
+ "[%!{(MISSING)public}@] {SetJobLookupResponseRcvd} | job indicating lookup response received yet no set-configuation | event:%!{(MISSING)public}@"
+ "autoAssetJobSetLookupResponseReceived:"
+ "UserInitiated"
+ "setHaveReceivedLookupResponse:"
+ "haveReceivedLookupResponse"
+ "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:"
+ "{%!@(MISSING)} unable to locate asset-descriptor for atomic-instance entry | nextAtomicEntry:%!@(MISSING) | setConfiguration:%!@(MISSING)"
+ "PopulationType"
+ "{%!{(MISSING)publci}@}\n[LATEST-TO-VEND] no previous latestAtomicInstanceToVend | setConfiguration:%!{(MISSING)public}@"
+ "setSetCheckAwaitingDownload:"
+ "T\x1f\x0f\x06\x16<*\x13"
+ "_haveReceivedLookupResponseForSetDescriptor:"
+ "recordPushNotification:assetType:cloudChannels:forPopulationType:userInitiated:interestAcrossTerm:lockAcrossReboot:lockAcrossTermination:"
+ "%!@(MISSING):setConfigurationsUpdateLatestToVend"
+ "DecideNeedPersonalize[NOT-PERSONALIZING]"
- "[domain:%!@(MISSING)|setID:%!@(MISSING)|config:%!l(MISSING)d|AIs:%!l(MISSING)d(newer:%!@(MISSING)[%!l(MISSING)d])(latest:%!@(MISSING)[%!l(MISSING)d])|user:%!@(MISSING)|locks:%!@(MISSING)]"
- "Attempting to read AppleConnect SSO token with default interactivity level"
- "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Aug  5 2024 21:26:31"
- "[overall]instance:%!@(MISSING),selector:%!@(MISSING),UUID:%!@(MISSING),logger:%!@(MISSING),tasks:%!l(MISSING)u,requests:%!l(MISSING)d,table:%!@(MISSING),FSM:%!@(MISSING),sched:%!@(MISSING),NWFail:%!@(MISSING)|beingCancled:%!@(MISSING)|[earlier]sched:%!@(MISSING),NWFail:%!@(MISSING)|bonded:%!@(MISSING)|[active]instance:%!@(MISSING),desire:%!@(MISSING)(awaitDownload:%!@(MISSING)),found:%!@(MISSING),end:%!@(MISSING),listen:%!@(MISSING),jobInfo:%!@(MISSING)|[aggregated]policy:%!@(MISSING),clientRequested:%!@(MISSING)|firstClientName:%!@(MISSING),triggeringLayer:%!@(MISSING)|onFilesystemByVersion:%!l(MISSING)d|[check]Base:%!@(MISSING),UUID:%!@(MISSING),lookupGrant:%!@(MISSING),rampFG:%!@(MISSING),rampLatch:%!@(MISSING),options:%!@(MISSING)|[asset]base:%!@(MISSING),patch:%!@(MISSING),full:%!@(MISSING),newer:%!@(MISSING),downloading:%!@(MISSING),scheduler:%!@(MISSING),user:%!@(MISSING),boosting:%!@(MISSING),checking:%!@(MISSING),determining:%!@(MISSING),locking:%!@(MISSING),patched:%!@(MISSING)|[installed]:version:%!@(MISSING),build:%!@(MISSING)|[status]current:%!@(MISSING),progress:%!@(MISSING),lastPatch:%!@(MISSING)|[results]selector:%!@(MISSING),instance:%!@(MISSING),found:%!@(MISSING),end:%!@(MISSING),listen:%!@(MISSING),[set]aggregatedPolicy:%!@(MISSING),descriptor:%!@(MISSING),next:%!l(MISSING)d,found:%!@(MISSING)"
- "Launching at high priority"
- "_isSetDescriptorAvailableToClient:forSetDescriptor:requiringSecureGrafted:"
- "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] unable to replace latestAtomicInstanceToVend (since not fully available) | setConfiguration:%!{(MISSING)public}@"
- "\n[SECURE][%!{(MISSING)public}@][SET-CONTROL][ELIMINATE] {%!{(MISSING)public}@} set-identifier eliminate while performing secure operation(s) | setDescriptor:%!{(MISSING)public}@"
- "{setConfigurationsUpdateLatestToVend}\n[LATEST-TO-VEND] no previous latestAtomicInstanceToVend | setConfiguration:%!{(MISSING)public}@"
- "[(client)Domain:%!@(MISSING),Name:%!@(MISSING)|(set)Identifier:%!@(MISSING),Entries:%!l(MISSING)d|latestToVend:%!@(MISSING)|inhibitScheduling:%!@(MISSING)]"
- "setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:requiringPersonalized:"
- "{autoSetJobIssueReply} | unable to build response message | error:%!{(MISSING)public}@"
- "{setConfigurationsUpdateLatestToVend}\n[LATEST-TO-VEND] unable to replace latestAtomicInstanceToVend (since not fully available) | setDescriptorToUpdate:%!{(MISSING)public}@"
- "2.2.8"
- "[clientName:%!@(MISSING)|setEntries:%!l(MISSING)d|latestToVend:%!@(MISSING)|inhibitScheduling:%!@(MISSING)]"
- "\n[AUTO-SECURE][AUTO-PERSONALIZATION][STARTUP] {%!{(MISSING)public}@} heal operation #%!l(MISSING)d (personalize) | secureDescriptor:%!{(MISSING)public}@"
- "                      clientDomainName: %!@(MISSING)\n                    assetSetIdentifier: %!@(MISSING)\n                configuredAssetEntries: %!@(MISSING)\n             atomicInstancesDownloaded: %!@(MISSING)\n               catalogCachedAssetSetID: %!@(MISSING)\n             catalogDownloadedFromLive: %!@(MISSING)\n                catalogLastTimeChecked: %!@(MISSING)\n                     catalogPostedDate: %!@(MISSING)\n         newerAtomicInstanceDiscovered: %!@(MISSING)\n          newerDiscoveredAtomicEntries: %!@(MISSING)\n              latestDownloadedInstance: %!@(MISSING)\n        latestDowloadedInstanceEntries: %!@(MISSING)\n     downloadedCatalogCachedAssetSetID: %!@(MISSING)\n   downloadedCatalogDownloadedFromLive: %!@(MISSING)\n      downloadedCatalogLastTimeChecked: %!@(MISSING)\n           downloadedCatalogPostedDate: %!@(MISSING)\n                  currentNotifications: %!@(MISSING)\n                     currentNeedPolicy: %!@(MISSING)\n                currentSchedulerPolicy: %!@(MISSING)\n                   currentStagerPolicy: %!@(MISSING)\n                 downloadUserInitiated: %!@(MISSING)\n                      downloadProgress:\n%!@(MISSING)\n                downloadedNetworkBytes: %!l(MISSING)d\n             downloadedFilesystemBytes: %!l(MISSING)d\n                      currentLockUsage:\n%!@(MISSING)\n                   selectorsForStaging: %!@(MISSING)\n                  availableForUseError: %!@(MISSING)\n                     newerVersionError: %!@(MISSING)\n"
- "@240@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176B184@188q196q204B212@216@224@232"
- "Launching at low priority"
- "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_schedulePushNotifications} triggered 1-shot XPC Activity | delay(%!{(MISSING)public}@..%!{(MISSING)public}@), jitter(%!{(MISSING)public}@..%!{(MISSING)public}@), chosenPushDelay:%!{(MISSING)public}@"
- "newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
- "[%!@(MISSING) | instance latestDownloaded:%!@(MISSING)(entries:%!l(MISSING)d), discovered:%!@(MISSING)(entries:%!l(MISSING)d), requestedEntries:%!l(MISSING)d, fullyDownloaded:%!@(MISSING)(notified:%!@(MISSING)) | onFilesystem:%!@(MISSING)(incomplete:%!@(MISSING)), neverBeenLocked:%!@(MISSING) | secureOperation(inProgress:%!@(MISSING)), (elimintating:%!@(MISSING)) | userInitiated:%!@(MISSING), stagedPrior:%!@(MISSING) | catalog(cachedAssetSetID:%!@(MISSING)), (downloadedFromLive:%!@(MISSING)), (lastTimeChecked:%!@(MISSING)), (postedDate:%!@(MISSING)) | downloaded(cachedAssetSetID:%!@(MISSING)), (downloadedFromLive:%!@(MISSING)), (lastTimeChecked:%!@(MISSING)), (postedDate:%!@(MISSING))]"
- "@80@0:8@?16@24@32@40@48@56@64@72"
- "{setConfigurationsUpdateLatestToVend}\n[LATEST-TO-VEND] replaced latestAtomicInstanceToVend | setConfiguration:%!{(MISSING)public}@"
- "Starting built-in MobileAsset brain built Aug  5 2024 21:26:31"
- "D\x1f\x0f\x06\x16<*\x13"
- "setConfigurationRefreshToVend:forSetConfiguration:fromStaged:fromMigrated:requiringPersonalized:"
- "Resetting Priority"
- "\n[SET-CONFIGURATION]{setConfigurationsUpdateLatestToVend} unable to load set-configuration | setConfigurationKey:%!{(MISSING)public}@"
- "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:"
- "initForSetJobIssueReply:forDomainName:forAssetSetIdentifier:withSetAtomicInstance:withAutoAssetUUID:withSetJobInformation:withResponseMessage:withResponseError:"
- "setConfigurationPersist:fromLocation:"
- "%!{(MISSING)public}@\n[AUTO-SECURE][AUTO-PERSONALIZATION] auto-asset personalization attempt failed (not fatal since personalization to be re-attempted upon first lock) | error:%!{(MISSING)public}@ | downloadingAssetDescriptor:%!{(MISSING)public}@"
- "B44@0:8@16@24@32B40"
- "securePersonalizeGraftLockSet:lockingSetDescriptor:forEventInfo:"

```
