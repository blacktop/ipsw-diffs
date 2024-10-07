## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1309.40.57.522.1
-  __TEXT.__text: 0x25d4bc
+1309.42.3.0.0
+  __TEXT.__text: 0x261b98
   __TEXT.__auth_stubs: 0x2370
-  __TEXT.__objc_stubs: 0x1f7a0
-  __TEXT.__objc_methlist: 0xee58
+  __TEXT.__objc_stubs: 0x1fa00
+  __TEXT.__objc_methlist: 0xef90
   __TEXT.__const: 0x494e
-  __TEXT.__objc_methname: 0x36880
-  __TEXT.__cstring: 0x4c70c
+  __TEXT.__objc_methname: 0x372cd
+  __TEXT.__cstring: 0x4c8ac
   __TEXT.__objc_classname: 0xd7b
-  __TEXT.__objc_methtype: 0x3428
-  __TEXT.__oslogstring: 0x300c0
+  __TEXT.__objc_methtype: 0x3562
+  __TEXT.__oslogstring: 0x311d0
   __TEXT.__gcc_except_tab: 0x2544
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x10c4

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x4718
+  __TEXT.__unwind_info: 0x4740
   __TEXT.__eh_frame: 0x30c4
   __DATA_CONST.__auth_got: 0x11c8
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x9c8
-  __DATA_CONST.__const: 0x6688
-  __DATA_CONST.__cfstring: 0x31580
+  __DATA_CONST.__const: 0x66b8
+  __DATA_CONST.__cfstring: 0x316c0
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8a90
+  __DATA_CONST.__objc_selrefs: 0x8b28
   __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x988
   __DATA_CONST.__objc_arrayobj: 0x1b0
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x143d8
+  __DATA.__objc_const: 0x14528
   __DATA.__objc_classrefs: 0x7a0
   __DATA.__objc_superrefs: 0x2e8
-  __DATA.__objc_ivar: 0x1264
+  __DATA.__objc_ivar: 0x1280
   __DATA.__objc_data: 0xd10
   __DATA.__data: 0x2608
   __DATA.__bss: 0x53a0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8236
-  Symbols:   14783
-  CStrings:  15693
+  Functions: 8278
+  Symbols:   14853
+  CStrings:  15770
 
Symbols:
+ +[MADAutoAssetControlManager autoAssetJobSetLookupResponseReceived:forAssignedSetDescriptor:]
+ +[MADAutoAssetControlManager preferenceStartupSimulateFirstBoot]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:]
+ +[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:]
+ +[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.1
+ +[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.2
+ +[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.3
+ +[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:].cold.4
+ +[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]
+ +[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]
+ -[MADAutoAssetControlManager _clearSetConfigurationLatestToVend:forSetDesriptor:forSetAtomicInstance:fromLocation:]
+ -[MADAutoAssetControlManager _removeDescriptorFromFilesystem:droppingDescriptor:forHistoryOperation:firstClientName:]
+ -[MADAutoAssetControlManager _vendingAtomicInstanceForConfiguredEntriesForClientDomainName:forAssetSetIdentifier:]
+ -[MADAutoAssetControlManager _vendingAtomicInstanceForConfiguredEntriesForSetDescriptor:]
+ -[MADAutoAssetControlManager action_ResumeJobs:error:].cold.1
+ -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend]
+ -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend].cold.1
+ -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend].cold.2
+ -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend].cold.3
+ -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend].cold.4
+ -[MADAutoAssetControlManager considerSetDescriptorsForLatestToVend].cold.5
+ -[MADAutoAssetControlManager decideSetDescriptorAsLatestToVend:currentlyVendingSetDescriptor:withOtherCandidateSetDescriptors:]
+ -[MADAutoAssetControlManager firstDaemonStartupSinceDeviceBoot]
+ -[MADAutoAssetControlManager handleSetClientCheckAtomic:forAutoJob:instance:desire:fromLocation:].cold.1
+ -[MADAutoAssetControlManager handleSetClientLockAtomic:forAutoJob:instance:desire:fromLocation:].cold.1
+ -[MADAutoAssetControlManager locateSetDescriptorForSelector:]
+ -[MADAutoAssetControlManager migratedFromPreinstalled]
+ -[MADAutoAssetControlManager newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MADAutoAssetControlManager preferenceStartupSimulateFirstBoot]
+ -[MADAutoAssetControlManager setConfigurationPersist:fromLocation:dueToAlter:forHistoryOperation:]
+ -[MADAutoAssetControlManager setConfigurationPotentialLatestToVend:forSetDescriptor:forSetConfiguration:]
+ -[MADAutoAssetControlManager setConfigurationsPrePersonalizedJustCommitted:]
+ -[MADAutoAssetControlManager setFirstDaemonStartupSinceDeviceBoot:]
+ -[MADAutoAssetControlManager setMigratedFromPreinstalled:]
+ -[MADAutoAssetControlManager setPreferenceStartupSimulateFirstBoot:]
+ -[MADAutoAssetControlManagerParam initForSetConfiguration:withSetDescriptor:]
+ -[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]
+ -[MADAutoAssetJob setVendingAtomicInstanceForConfiguredEntries:]
+ -[MADAutoAssetJob updateSetDescriptorDownloaded:forAssetDescriptor:justDownloaded:]
+ -[MADAutoAssetJob vendingAtomicInstanceForConfiguredEntries]
+ -[MADAutoAssetScheduler _performTriggeredSetJobForSetConfiguration:usingSetUpdatePolicy:]
+ -[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]
+ -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:]
+ -[MADAutoSetConfiguration setVendingAtomicInstanceForConfiguredEntries:]
+ -[MADAutoSetConfiguration vendingAtomicInstanceForConfiguredEntries]
+ -[MADAutoSetLookupResult initForAssetType:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withRequestedAutoAssetEntries:withDiscoveredAtomicEntries:withCatalogFromPallasResponse:]
+ -[MADAutoSetLookupResult requestedAutoAssetEntries]
+ -[MADAutoSetLookupResult setRequestedAutoAssetEntries:]
+ -[MANAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MANAutoAssetSetStatus setVendingAtomicInstanceForConfiguredEntries:]
+ -[MANAutoAssetSetStatus vendingAtomicInstanceForConfiguredEntries]
+ GCC_except_table377
+ GCC_except_table539
+ GCC_except_table541
+ GCC_except_table544
+ GCC_except_table546
+ GCC_except_table560
+ GCC_except_table57
+ GCC_except_table63
+ GCC_except_table92
+ OBJC_IVAR_$_MADAutoAssetControlManager._firstDaemonStartupSinceDeviceBoot
+ OBJC_IVAR_$_MADAutoAssetControlManager._migratedFromPreinstalled
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStartupSimulateFirstBoot
+ OBJC_IVAR_$_MADAutoAssetJob._vendingAtomicInstanceForConfiguredEntries
+ OBJC_IVAR_$_MADAutoSetConfiguration._vendingAtomicInstanceForConfiguredEntries
+ OBJC_IVAR_$_MADAutoSetLookupResult._requestedAutoAssetEntries
+ OBJC_IVAR_$_MANAutoAssetSetStatus._vendingAtomicInstanceForConfiguredEntries
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1077
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1078
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1082
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1107
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1107.cold.1
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1117
+ __54-[MADAutoAssetControlManager action_ResumeJobs:error:]_block_invoke.cold.1
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2077
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2839
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2840
+ __98+[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:]_block_invoke.cold.1
+ ___128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke
+ ___128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke_2
+ ___152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke
+ ___266+[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]_block_invoke
+ ___276-[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]_block_invoke
+ ___97-[MADAutoAssetControlManager handleSetClientCheckAtomic:forAutoJob:instance:desire:fromLocation:]_block_invoke
+ ___97-[MADAutoAssetControlManager handleSetClientCheckAtomic:forAutoJob:instance:desire:fromLocation:]_block_invoke_2
+ ___98+[MADAutoAssetScheduler triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:]_block_invoke
+ ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_82_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e42_v24?0"MADAutoSetDescriptor"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ __block_literal_global.1169
+ __block_literal_global.1189
+ __block_literal_global.1194
+ __block_literal_global.1196
+ __block_literal_global.3424
+ __block_literal_global.4152
+ _kMobileAssetPreferencesAutoAssetStartupSimulateFirstBoot
+ _objc_msgSend$_clearSetConfigurationLatestToVend:forSetDesriptor:forSetAtomicInstance:fromLocation:
+ _objc_msgSend$_performTriggeredSetJobForSetConfiguration:usingSetUpdatePolicy:
+ _objc_msgSend$_personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:
+ _objc_msgSend$_removeDescriptorFromFilesystem:droppingDescriptor:forHistoryOperation:firstClientName:
+ _objc_msgSend$_vendingAtomicInstanceForConfiguredEntriesForClientDomainName:forAssetSetIdentifier:
+ _objc_msgSend$_vendingAtomicInstanceForConfiguredEntriesForSetDescriptor:
+ _objc_msgSend$autoAssetJobSetLookupResponseReceived:forAssignedSetDescriptor:
+ _objc_msgSend$considerSetDescriptorsForLatestToVend
+ _objc_msgSend$decideSetDescriptorAsLatestToVend:currentlyVendingSetDescriptor:withOtherCandidateSetDescriptors:
+ _objc_msgSend$doesSetDescriptor:coverAllForAutoAssetEntries:
+ _objc_msgSend$doesSetDescriptor:coverRequestedAutoAssetEntries:
+ _objc_msgSend$firstDaemonStartupSinceDeviceBoot
+ _objc_msgSend$initForAssetType:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withRequestedAutoAssetEntries:withDiscoveredAtomicEntries:withCatalogFromPallasResponse:
+ _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:
+ _objc_msgSend$initForSetConfiguration:withSetDescriptor:
+ _objc_msgSend$initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$loadPersistedSetActiveJobDescriptors
+ _objc_msgSend$locateSetDescriptorForSelector:
+ _objc_msgSend$migratedFromPreinstalled
+ _objc_msgSend$newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$personalizeSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:
+ _objc_msgSend$personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:
+ _objc_msgSend$preferenceStartupSimulateFirstBoot
+ _objc_msgSend$recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:
+ _objc_msgSend$recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:
+ _objc_msgSend$setConfigurationPersist:fromLocation:dueToAlter:forHistoryOperation:
+ _objc_msgSend$setConfigurationPotentialLatestToVend:forSetDescriptor:forSetConfiguration:
+ _objc_msgSend$setConfigurationsPrePersonalizedJustCommitted:
+ _objc_msgSend$setFirstDaemonStartupSinceDeviceBoot:
+ _objc_msgSend$setMigratedFromPreinstalled:
+ _objc_msgSend$setVendingAtomicInstanceForConfiguredEntries:
+ _objc_msgSend$triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:
+ _objc_msgSend$updateSetDescriptorDownloaded:forAssetDescriptor:justDownloaded:
+ _objc_msgSend$vendingAtomicInstanceForConfiguredEntries
- +[MADAutoAssetControlManager autoAssetJobSetLookupResponseReceived:]
- +[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]
- -[MADAutoAssetControlManager _removeDescriptorFromFilesystem:forHistoryOperation:firstClientName:]
- -[MADAutoAssetControlManager newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
- -[MADAutoAssetControlManager setConfigurationPersist:fromLocation:dueToAlter:]
- -[MADAutoAssetControlManager setConfigurationRefreshToVend:forSetConfiguration:fromStaged:]
- -[MADAutoAssetControlManager setConfigurationRefreshToVendFromMigrated:forSetConfiguration:]
- -[MADAutoAssetControlManager setConfigurationRefreshToVendFromPromoted:forSetConfiguration:]
- -[MADAutoAssetControlManager setConfigurationsUpdateLatestToVend:]
- -[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]
- -[MADAutoAssetJob updateSetDescriptorDownloaded:justDownloaded:]
- -[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]
- -[MADAutoSetConfiguration initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:]
- -[MADAutoSetLookupResult initForAssetType:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withDiscoveredAtomicEntries:withCatalogFromPallasResponse:]
- GCC_except_table374
- GCC_except_table535
- GCC_except_table537
- GCC_except_table540
- GCC_except_table542
- GCC_except_table556
- GCC_except_table61
- __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1077
- __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1078
- __121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1082
- __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1107
- __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1107.cold.1
- __140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke.1117
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2080
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.2848
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.2849
- ___121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke
- ___121+[MADAutoAssetSecure personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke_2
- ___140-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:]_block_invoke
- ___206+[MADAutoAssetHistory recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]_block_invoke
- ___216-[MADAutoAssetHistoryTracker recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:]_block_invoke
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_81_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- __block_literal_global.1166
- __block_literal_global.1186
- __block_literal_global.1191
- __block_literal_global.1193
- __block_literal_global.3426
- __block_literal_global.4170
- _loadManagedPrefs
- _objc_msgSend$_isSetDescriptorAvailableToClient:forSetDescriptor:
- _objc_msgSend$_personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:
- _objc_msgSend$_removeDescriptorFromFilesystem:forHistoryOperation:firstClientName:
- _objc_msgSend$autoAssetJobSetLookupResponseReceived:
- _objc_msgSend$initForAssetType:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withDiscoveredAtomicEntries:withCatalogFromPallasResponse:
- _objc_msgSend$initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:
- _objc_msgSend$newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
- _objc_msgSend$recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:
- _objc_msgSend$recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:
- _objc_msgSend$secureHealingPersonalizationAttempted
- _objc_msgSend$setConfigurationPersist:fromLocation:dueToAlter:
- _objc_msgSend$setConfigurationRefreshToVend:forSetConfiguration:fromStaged:
- _objc_msgSend$setConfigurationRefreshToVendFromMigrated:forSetConfiguration:
- _objc_msgSend$setConfigurationRefreshToVendFromPromoted:forSetConfiguration:
- _objc_msgSend$setConfigurationsUpdateLatestToVend:
- _objc_msgSend$updateSetDescriptorDownloaded:justDownloaded:
CStrings:
+ "                      clientDomainName: %!@(MISSING)\n                    assetSetIdentifier: %!@(MISSING)\n                configuredAssetEntries: %!@(MISSING)\n             atomicInstancesDownloaded: %!@(MISSING)\n               catalogCachedAssetSetID: %!@(MISSING)\n             catalogDownloadedFromLive: %!@(MISSING)\n                catalogLastTimeChecked: %!@(MISSING)\n                     catalogPostedDate: %!@(MISSING)\n         newerAtomicInstanceDiscovered: %!@(MISSING)\n          newerDiscoveredAtomicEntries: %!@(MISSING)\n              latestDownloadedInstance: %!@(MISSING)\n        latestDowloadedInstanceEntries: %!@(MISSING)\n     downloadedCatalogCachedAssetSetID: %!@(MISSING)\n   downloadedCatalogDownloadedFromLive: %!@(MISSING)\n      downloadedCatalogLastTimeChecked: %!@(MISSING)\n           downloadedCatalogPostedDate: %!@(MISSING)\n                  currentNotifications: %!@(MISSING)\n                     currentNeedPolicy: %!@(MISSING)\n                currentSchedulerPolicy: %!@(MISSING)\n                   currentStagerPolicy: %!@(MISSING)\n            haveReceivedLookupResponse: %!@(MISSING)\n vendingAtomicInstanceForConfigEntries: %!@(MISSING)\n                 downloadUserInitiated: %!@(MISSING)\n                      downloadProgress:\n%!@(MISSING)\n                downloadedNetworkBytes: %!l(MISSING)d\n             downloadedFilesystemBytes: %!l(MISSING)d\n                      currentLockUsage:\n%!@(MISSING)\n                   selectorsForStaging: %!@(MISSING)\n                  availableForUseError: %!@(MISSING)\n                     newerVersionError: %!@(MISSING)\n"
+ "%!@(MISSING):_removeDescriptorFromFilesystem"
+ "%!@(MISSING):_removeDownloadedDescriptorsWithNewerDownloaded"
+ "%!@(MISSING):isSetFoundAlreadyOnFilesystem"
+ "%!@(MISSING):setConfigurationPotentialLatestToVend"
+ "%!@(MISSING):setConfigurationsPrePersonalizedJustCommitted"
+ "%!@(MISSING):updateSetDescriptorDownloaded"
+ "%!{(MISSING)public}@\n[AUTO-SECURE][AUTO-PERSONALIZATION][SET-JOB-TRY] {%!{(MISSING)public}@:} secure auto-asset just immediate-promoted from staged (requires personalization) | justPromotedDescriptor:%!{(MISSING)public}@"
+ "%!{(MISSING)public}@ | {AUTO-SCHEDULER:_performTriggeredSetJobForSetConfiguration} directly triggered selector | NoRetry:%!l(MISSING)d RequiringRetry:%!l(MISSING)d | MA_MILESTONE"
+ "2.2.19"
+ "@244@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168B176B180B184@188q196q204@212@220@228@236"
+ "@248@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176B184B188B192@196q204q212B220@224@232@240"
+ "@68@0:8@16@24@32@40@48B56B60B64"
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "ADD_SD_SAME_VERSION_FOUND  "
+ "AUTO-CONTROL-MANAGER [AutoAssetVersion:%!{(MISSING)public}@] | Initialized | bootedOSVersion:%!{(MISSING)public}@ | bootedOBuildVersion:%!{(MISSING)public}@"
+ "AUTO-CONTROL:{autoControlManager} initializing the shared auto-control-manager [AutoAssetVersion:%!{(MISSING)public}@] | ...init"
+ "AUTO-CONTROL:{autoControlManager} initializing the shared auto-control-manager [AutoAssetVersion:%!{(MISSING)public}@] | init..."
+ "AutoAssetStartupSimulateFirstBoot"
+ "DEL_SD_DROP_CROSSCHECK_TRIM"
+ "O\x0f\x1f\a\x112Rd"
+ "SET_CONFIGURATION|setConfiguration:%!@(MISSING)|setDescriptor:%!@(MISSING)"
+ "SET_CONFIG_ALTER_ENTRIES   "
+ "SET_CONFIG_FORCE_UNLOCKED  "
+ "SET_CONFIG_LOOKUP_RESPONSE "
+ "SET_CONFIG_NEW_SET_CONFIG  "
+ "SET_CONFIG_REFRESH_STALE   "
+ "Starting built-in MobileAsset brain built Sep 30 2024 03:41:12"
+ "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Sep 30 2024 03:41:12"
+ "TB,N,V_firstDaemonStartupSinceDeviceBoot"
+ "TB,N,V_migratedFromPreinstalled"
+ "TB,N,V_preferenceStartupSimulateFirstBoot"
+ "TB,N,V_vendingAtomicInstanceForConfiguredEntries"
+ "[%!{(MISSING)public}@]\n[DEVICE-BOOT] {ResumeJobs} migrated pre-installed assets"
+ "[%!{(MISSING)public}@] {%!{(MISSING)public}@}\n[LATEST-TO-VEND] clearing set-configuration latestAtomicInstanceToVend | setConfiguration:%!{(MISSING)public}@"
+ "[%!{(MISSING)public}@] {%!{(MISSING)public}@} NO_WAIT_NOT_PERSISTED | successful lock | chosenDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "[%!{(MISSING)public}@] {%!{(MISSING)public}@} removed from filesystem | dropDescriptor:%!{(MISSING)public}@ "
+ "[%!{(MISSING)public}@] {%!{(MISSING)public}@} unable to remove from filesystem | dropDescriptor:%!{(MISSING)public}@, error:%!{(MISSING)public}@"
+ "[(client)Domain:%!@(MISSING),Name:%!@(MISSING)|(set)Identifier:%!@(MISSING),Entries:%!l(MISSING)d|latestToVend:%!@(MISSING)|inhibitScheduling:%!@(MISSING)|lookupRsp:%!@(MISSING)|vendingForConfig:%!@(MISSING)]"
+ "[cachedAssetSetID:%!@(MISSING)|downloadedFromLive:%!@(MISSING)|lastTimeChecked:%!@(MISSING)|postedDate:%!@(MISSING)|atomicEntries(requested:%!l(MISSING)d,discovered:%!l(MISSING)d)|assetIDs:%!l(MISSING)d|setCatalogAssets:%!l(MISSING)d]"
+ "[clientName:%!@(MISSING)|setEntries:%!l(MISSING)d|latestToVend:%!@(MISSING)|inhibitScheduling:%!@(MISSING)|lookupRsp:%!@(MISSING)|vendingforConfig:%!@(MISSING)]"
+ "[domain:%!@(MISSING)|setID:%!@(MISSING)|config:%!l(MISSING)d|AIs:%!l(MISSING)d(newer:%!@(MISSING)[%!l(MISSING)d])(latest:%!@(MISSING)[%!l(MISSING)d])|lookupRsp:%!@(MISSING)(forConfig:%!@(MISSING))|user:%!@(MISSING)|locks:%!@(MISSING)]"
+ "[overall]instance:%!@(MISSING),selector:%!@(MISSING),UUID:%!@(MISSING),logger:%!@(MISSING),tasks:%!l(MISSING)u,requests:%!l(MISSING)d,table:%!@(MISSING),FSM:%!@(MISSING),sched:%!@(MISSING),NWFail:%!@(MISSING)|beingCancled:%!@(MISSING)|[earlier]sched:%!@(MISSING),NWFail:%!@(MISSING)|bonded:%!@(MISSING)|[active]instance:%!@(MISSING),desire:%!@(MISSING)(awaitDownload:%!@(MISSING),checkAwait:%!@(MISSING)),found:%!@(MISSING),end:%!@(MISSING),listen:%!@(MISSING),jobInfo:%!@(MISSING)|[aggregated]policy:%!@(MISSING),clientRequested:%!@(MISSING)|firstClientName:%!@(MISSING),triggeringLayer:%!@(MISSING)|onFilesystemByVersion:%!l(MISSING)d|[check]Base:%!@(MISSING),UUID:%!@(MISSING),lookupGrant:%!@(MISSING),rampFG:%!@(MISSING),rampLatch:%!@(MISSING),options:%!@(MISSING)|[asset]base:%!@(MISSING),patch:%!@(MISSING),full:%!@(MISSING),newer:%!@(MISSING),downloading:%!@(MISSING),scheduler:%!@(MISSING),lookupRsp:%!@(MISSING)(forConfig:%!@(MISSING)),user:%!@(MISSING),boosting:%!@(MISSING),checking:%!@(MISSING),determining:%!@(MISSING),locking:%!@(MISSING),patched:%!@(MISSING)|[installed]:version:%!@(MISSING),build:%!@(MISSING)|[status]current:%!@(MISSING),progress:%!@(MISSING),lastPatch:%!@(MISSING)|[results]selector:%!@(MISSING),instance:%!@(MISSING),found:%!@(MISSING),end:%!@(MISSING),listen:%!@(MISSING),[set]aggregatedPolicy:%!@(MISSING),descriptor:%!@(MISSING),next:%!l(MISSING)d,found:%!@(MISSING)"
+ "_clearSetConfigurationLatestToVend:forSetDesriptor:forSetAtomicInstance:fromLocation:"
+ "_firstDaemonStartupSinceDeviceBoot"
+ "_migratedFromPreinstalled"
+ "_performTriggeredSetJobForSetConfiguration:usingSetUpdatePolicy:"
+ "_personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:"
+ "_preferenceStartupSimulateFirstBoot"
+ "_removeDescriptorFromFilesystem:droppingDescriptor:forHistoryOperation:firstClientName:"
+ "_vendingAtomicInstanceForConfiguredEntries"
+ "_vendingAtomicInstanceForConfiguredEntriesForClientDomainName:forAssetSetIdentifier:"
+ "_vendingAtomicInstanceForConfiguredEntriesForSetDescriptor:"
+ "autoAssetJobSetLookupResponseReceived:forAssignedSetDescriptor:"
+ "configured=%!l(MISSING)d requested:%!l(MISSING)d fromPallas:%!l(MISSING)d vending:%!l(MISSING)d"
+ "considerSetDescriptorsForLatestToVend"
+ "count=%!l(MISSING)d"
+ "decideSetDescriptorAsLatestToVend:currentlyVendingSetDescriptor:withOtherCandidateSetDescriptors:"
+ "firstDaemonStartupSinceDeviceBoot"
+ "initForAssetType:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withRequestedAutoAssetEntries:withDiscoveredAtomicEntries:withCatalogFromPallasResponse:"
+ "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:"
+ "initForSetConfiguration:withSetDescriptor:"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "loadPersistedSetDescriptorAsLatestToVend"
+ "locateSetDescriptorForSelector:"
+ "migratedFromPreinstalled"
+ "newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "personalizeSetDownloaded:forSetDescriptor:allowingNetwork:withAutoAssetDescriptors:completion:"
+ "personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:"
+ "preferenceStartupSimulateFirstBoot"
+ "recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:"
+ "recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:"
+ "recordOperation:toHistoryType:fromLayer:configuredCount:requestedCount:fromPallasCount:vendingCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:"
+ "setConfigurationPersist:fromLocation:dueToAlter:forHistoryOperation:"
+ "setConfigurationPotentialLatestToVend:forSetDescriptor:forSetConfiguration:"
+ "setConfigurationsPrePersonalizedJustCommitted:"
+ "setFirstDaemonStartupSinceDeviceBoot:"
+ "setMigratedFromPreinstalled:"
+ "setPreferenceStartupSimulateFirstBoot:"
+ "setVendingAtomicInstanceForConfiguredEntries:"
+ "time=%!@(MISSING) op=%!@(MISSING) %!@(MISSING)=%!@(MISSING) %!@(MISSING) domain=%!@(MISSING)%!@(MISSING)"
+ "time=%!@(MISSING) op=%!@(MISSING) %!@(MISSING)=%!@(MISSING) %!@(MISSING) id-%!@(MISSING) set=%!@(MISSING) domain=%!@(MISSING)%!@(MISSING)"
+ "time=%!@(MISSING) op=%!@(MISSING) %!@(MISSING)=%!@(MISSING) %!@(MISSING) id=%!@(MISSING) domain=%!@(MISSING)%!@(MISSING)"
+ "time=%!@(MISSING) op=%!@(MISSING) %!@(MISSING)=%!@(MISSING) %!@(MISSING) id=%!@(MISSING) set=%!@(MISSING) domain=%!@(MISSING)%!@(MISSING)"
+ "time=%!@(MISSING) op=%!@(MISSING) %!@(MISSING)=%!@(MISSING) %!@(MISSING)%!@(MISSING)"
+ "triggerWithRetrySetDomainName:forAssetSetIdentifier:usingSetUpdatePolicy:"
+ "updateSetDescriptorDownloaded:forAssetDescriptor:justDownloaded:"
+ "v104@0:8q16q24q32q40q48q56q64@72@80@88@96"
+ "v144@0:8q16q24@32q40@48@56q64q72q80q88q96@104@112@120@128@136"
+ "v44@0:8@16@24B32q36"
+ "v48@0:8@16@24q32@40"
+ "v56@0:8@16@24B32B36@40@?48"
+ "v64@0:8@16@24B32@36@44B52@?56"
+ "vendingAtomicInstanceForConfiguredEntries"
+ "{%!@(MISSING)} all entries available yet set-descriptor contains duplicate selectors | setDescriptor:%!@(MISSING)| setConfiguration:%!@(MISSING)"
+ "{%!@(MISSING)} downloaded atomic-entry already tracked (ignoring duplicate) | downloadedAtomicEntry:%!@(MISSING), downloadedAssetDescriptor:%!@(MISSING)"
+ "{%!@(MISSING)} no set-atomic-instance for set-configuration latest-to-vend | setConfiguration:%!@(MISSING)"
+ "{%!@(MISSING)} unable to determine local URL for descriptor:%!@(MISSING)"
+ "{%!{(MISSING)publci}@}\n[LATEST-TO-VEND] just committed all pre-personalized secure | setDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@}\n[SELF-HEAL] deduped setDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@} check-atomic found newer and latest - newer does not satisfy current set-configuration | newerDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@} check-atomic found newer and latest - newer not from PSUS (vending latest) | newerDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@} check-atomic found newer(PSUS) and latest - unable to create from PSUS (vending latest) | newerDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@} check-atomic found newer(PSUS) and latest - vending new from PSUS | chosenDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@} lock-atomic found newer (not awaiting any secure operation) | chosenDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@} lock-atomic found newer and latest - newer does not satisfy current set-configuration | newerDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@} lock-atomic found newer and latest - newer not from PSUS (vending latest) | newerDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@} lock-atomic found newer(PSUS) and latest - unable to create from PSUS (vending latest) | newerDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "{%!{(MISSING)public}@} lock-atomic found newer(PSUS) and latest - vending new from PSUS | chosenDownloadedSetDescriptor:%!{(MISSING)public}@"
+ "{AUTO-SCHEDULER:triggerWithRetrySetDomainName} no scheduling change | nil asset-set-identifier provided"
+ "{AUTO-SCHEDULER:triggerWithRetrySetDomainName} no scheduling change | nil client-domain-name provided"
+ "{AUTO-SCHEDULER:triggerWithRetrySetDomainName} set-configuration not known - not triggering | clientDomainName:%!{(MISSING)public}@ | assetSetIdentifier:%!{(MISSING)public}@"
+ "{AUTO-SCHEDULER:triggerWithRetrySetDomainName} | unable to create set-selector | clientDomainName:%!{(MISSING)public}@ | assetSetIdentifier:%!{(MISSING)public}@"
+ "{AUTO-SCHEDULER:triggerWithRetrySetDomainName} | unable to locate auto-asset-scheduler | clientDomainName:%!{(MISSING)public}@ | assetSetIdentifier:%!{(MISSING)public}@"
+ "{IssueClientReplySetJob}\n[JOB-UUID] same version found already tracked as latest-to-vend | setConfiguration:%!{(MISSING)public}@"
+ "{IssueClientReplySetJob}\n[JOB-UUID] set-job found same content already latest-to-vend | setJobDescriptor:%!{(MISSING)public}@"
+ "{IssueClientReplySetJob}\n[JOB-UUID] set-job with no assigned UUID - using event information | eventInfo:%!{(MISSING)public}@"
+ "{IssueClientReplySetJob}\n[JOB-UUID] set-job with no assigned UUID, no event UUID - using current set status | currentSetStatus:%!{(MISSING)public}@"
+ "{IssueClientReplySetJob}\n[JOB-UUID] set-job with no set-job descriptor yet jobAtomicInstance is already downloaded set-descriptor | setDescriptor:%!{(MISSING)public}@"
+ "{IssueClientReplySetJob}\n[JOB-UUID] set-job with set-job descriptor that is already a downloaded set-descriptor | setDescriptor:%!{(MISSING)public}@"
+ "{IssueClientReplySetJob}\n[JOB-UUID] set-job with set-job descriptor that is different from already downloaded set-descriptor (using already downloaded) | setJobDescriptor:%!{(MISSING)public}@"
+ "{IssueClientReplySetJob}\n[LATEST-TO-VEND] same version found first-tracked as downloaded set-descriptor | setConfiguration:%!{(MISSING)public}@"
+ "{IssueClientReplySetJob}\n[LATEST-TO-VEND] same version found is always latestAtomicInstanceToVend | setConfiguration:%!{(MISSING)public}@"
+ "{ResumeJobs} | Failed to write STARTUP_ACTIVATED cookie file [%!{(MISSING)public}@]| stashError:%!@(MISSING)"
+ "{ResumeJobs} | Writing STARTUP_ACTIVATED cookie file [%!{(MISSING)public}@]"
+ "{SetJobLookupResponseRcvd} set-job did not provide its assigned set-descriptor"
+ "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] pre-SU-staging set-descriptor | setDescriptor:%!{(MISSING)public}@"
+ "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] set-descriptor with no latestDownloadedAtomicInstance | setDescriptor:%!{(MISSING)public}@"
+ "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] set-descriptor without atomic-instance | setDescriptor:%!{(MISSING)public}@"
+ "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] set-descriptor without set-configuration | setDescriptor:%!{(MISSING)public}@"
+ "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] unable to load persisted entry | entryID:%!{(MISSING)public}@"
+ "{considerSetDescriptorsForLatestToVend} [IGNORE-SET-DESCRIPTOR] unable to load set-descriptor | entryID:%!{(MISSING)public}@"
+ "{considerSetDescriptorsForLatestToVend} no entryID"
+ "{considerSetDescriptorsForLatestToVend} set-descriptor being vended does not cover current set-configuration (not first MA daemon exeution) | beingVendedSetDescriptor:%!{(MISSING)public}@ | setConfiguration:%!{(MISSING)public}@"
+ "{considerSetDescriptorsForLatestToVend} set-descriptor being vended does not cover current set-configuration - triggering scheduler job | beingVendedSetDescriptor:%!{(MISSING)public}@ | setConfiguration:%!{(MISSING)public}@"
+ "{loadPersistedCrossCheckTrimSetDescriptors} [KEEP-SET-DESCRIPTOR] set-descriptor from pre-SU-staging | setDescriptor:%!{(MISSING)public}@"
+ "{loadPersistedSetDescriptorAsLatestToVend} adopted when no pre-existing latest-to-vend | adoptedSetDescriptor:%!{(MISSING)public}@"
+ "{loadPersistedSetDescriptorAsLatestToVend} considering covering | mostRecentSetDescriptor:%!{(MISSING)public}@ | setConfiguration:%!{(MISSING)public}@"
+ "{loadPersistedSetDescriptorAsLatestToVend} considering satisfying | mostRecentSetDescriptor:%!{(MISSING)public}@ | setConfiguration:%!{(MISSING)public}@"
+ "{loadPersistedSetDescriptorAsLatestToVend} no latest-to-vend | setConfiguration:%!{(MISSING)public}@"
+ "{loadPersistedSetDescriptorAsLatestToVend} preserved latest-to-vend | setConfiguration:%!{(MISSING)public}@"
+ "{loadPersistedSetDescriptorAsLatestToVend} replaced latest-to-vend | adoptedSetDescriptor:%!{(MISSING)public}@"
+ "{newFoundSetDescriptorsAsNewerDiscovered} (patch) already encountered | nextFoundDescriptor:%!@(MISSING) | alreadyAtomicEntry:%!@(MISSING)"
- "\n[SET-CONFIGURATION]{%!{(MISSING)public}@} unable to load set-configuration | setConfigurationKey:%!{(MISSING)public}@"
- "                      clientDomainName: %!@(MISSING)\n                    assetSetIdentifier: %!@(MISSING)\n                configuredAssetEntries: %!@(MISSING)\n             atomicInstancesDownloaded: %!@(MISSING)\n               catalogCachedAssetSetID: %!@(MISSING)\n             catalogDownloadedFromLive: %!@(MISSING)\n                catalogLastTimeChecked: %!@(MISSING)\n                     catalogPostedDate: %!@(MISSING)\n         newerAtomicInstanceDiscovered: %!@(MISSING)\n          newerDiscoveredAtomicEntries: %!@(MISSING)\n              latestDownloadedInstance: %!@(MISSING)\n        latestDowloadedInstanceEntries: %!@(MISSING)\n     downloadedCatalogCachedAssetSetID: %!@(MISSING)\n   downloadedCatalogDownloadedFromLive: %!@(MISSING)\n      downloadedCatalogLastTimeChecked: %!@(MISSING)\n           downloadedCatalogPostedDate: %!@(MISSING)\n                  currentNotifications: %!@(MISSING)\n                     currentNeedPolicy: %!@(MISSING)\n                currentSchedulerPolicy: %!@(MISSING)\n                   currentStagerPolicy: %!@(MISSING)\n            haveReceivedLookupResponse: %!@(MISSING)\n                 downloadUserInitiated: %!@(MISSING)\n                      downloadProgress:\n%!@(MISSING)\n                downloadedNetworkBytes: %!l(MISSING)d\n             downloadedFilesystemBytes: %!l(MISSING)d\n                      currentLockUsage:\n%!@(MISSING)\n                   selectorsForStaging: %!@(MISSING)\n                  availableForUseError: %!@(MISSING)\n                     newerVersionError: %!@(MISSING)\n"
- "%!@(MISSING):setConfigurationRefreshToVend"
- "%!@(MISSING):setConfigurationRefreshToVendFromMigrated"
- "%!@(MISSING):setConfigurationRefreshToVendFromPromoted"
- "%!@(MISSING):setConfigurationsUpdateLatestToVend"
- "%!{(MISSING)public}@\n[AUTO-SECURE][AUTO-PERSONALIZATION][SET-JOB-TRY] {%!{(MISSING)public}@:isSetFoundAlreadyOnFilesystem} secure auto-asset just immediate-promoted from staged (requires personalization) | justPromotedDescriptor:%!{(MISSING)public}@"
- "2.2.17"
- "?\x0f\x1f\a\x112Rd"
- "@244@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176B184B188@192q200q208B216@220@228@236"
- "AUTO-CONTROL-MANAGER | Initialized | bootedOSVersion:%!{(MISSING)public}@ | bootedOBuildVersion:%!{(MISSING)public}@"
- "AUTO-CONTROL:{autoControlManager} initializing the shared auto-control-manager | ...init"
- "AUTO-CONTROL:{autoControlManager} initializing the shared auto-control-manager | init..."
- "DecideNeedPersonalize[BEFORE-PERSONALIZING]"
- "DecideNeedPersonalize[NOT-PERSONALIZING]"
- "PersonalizeSuccessDecideMore[NEED-GRAFTING]"
- "Starting built-in MobileAsset brain built Sep 17 2024 17:06:24"
- "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Sep 17 2024 17:06:24"
- "[%!{(MISSING)public}@] {%!{(MISSING)public}@}\n[LATEST-TO-VEND] clearing set-configuration latestAtomicInstanceToVend | nextSetConfiguration:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {%!{(MISSING)public}@} NO_WAIT_NOT_PERISTED | successful lock | chosenDownloadedSetDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {%!{(MISSING)public}@} lock-atomic found newer and latest | newerDownloadedSetDescriptor:%!{(MISSING)public}@"
- "[%!{(MISSING)public}@] {_removeDescriptorFromFilesystem} removed from filesystem | dropDescriptor:%!{(MISSING)public}@ "
- "[%!{(MISSING)public}@] {_removeDescriptorFromFilesystem} unable to remove from filesystem | dropDescriptor:%!{(MISSING)public}@, error:%!{(MISSING)public}@"
- "[(client)Domain:%!@(MISSING),Name:%!@(MISSING)|(set)Identifier:%!@(MISSING),Entries:%!l(MISSING)d|latestToVend:%!@(MISSING)|inhibitScheduling:%!@(MISSING)|lookupRsp:%!@(MISSING)]"
- "[cachedAssetSetID:%!@(MISSING)|downloadedFromLive:%!@(MISSING)|lastTimeChecked:%!@(MISSING)|postedDate:%!@(MISSING)|atomicEntries:%!l(MISSING)d|assetIDs:%!l(MISSING)d|setCatalogAssets:%!l(MISSING)d]"
- "[clientName:%!@(MISSING)|setEntries:%!l(MISSING)d|latestToVend:%!@(MISSING)|inhibitScheduling:%!@(MISSING)|lookupRsp:%!@(MISSING)]"
- "[domain:%!@(MISSING)|setID:%!@(MISSING)|config:%!l(MISSING)d|AIs:%!l(MISSING)d(newer:%!@(MISSING)[%!l(MISSING)d])(latest:%!@(MISSING)[%!l(MISSING)d])|lookupRsp:%!@(MISSING)|user:%!@(MISSING)|locks:%!@(MISSING)]"
- "[overall]instance:%!@(MISSING),selector:%!@(MISSING),UUID:%!@(MISSING),logger:%!@(MISSING),tasks:%!l(MISSING)u,requests:%!l(MISSING)d,table:%!@(MISSING),FSM:%!@(MISSING),sched:%!@(MISSING),NWFail:%!@(MISSING)|beingCancled:%!@(MISSING)|[earlier]sched:%!@(MISSING),NWFail:%!@(MISSING)|bonded:%!@(MISSING)|[active]instance:%!@(MISSING),desire:%!@(MISSING)(awaitDownload:%!@(MISSING),checkAwait:%!@(MISSING)),found:%!@(MISSING),end:%!@(MISSING),listen:%!@(MISSING),jobInfo:%!@(MISSING)|[aggregated]policy:%!@(MISSING),clientRequested:%!@(MISSING)|firstClientName:%!@(MISSING),triggeringLayer:%!@(MISSING)|onFilesystemByVersion:%!l(MISSING)d|[check]Base:%!@(MISSING),UUID:%!@(MISSING),lookupGrant:%!@(MISSING),rampFG:%!@(MISSING),rampLatch:%!@(MISSING),options:%!@(MISSING)|[asset]base:%!@(MISSING),patch:%!@(MISSING),full:%!@(MISSING),newer:%!@(MISSING),downloading:%!@(MISSING),scheduler:%!@(MISSING),lookupRsp:%!@(MISSING),user:%!@(MISSING),boosting:%!@(MISSING),checking:%!@(MISSING),determining:%!@(MISSING),locking:%!@(MISSING),patched:%!@(MISSING)|[installed]:version:%!@(MISSING),build:%!@(MISSING)|[status]current:%!@(MISSING),progress:%!@(MISSING),lastPatch:%!@(MISSING)|[results]selector:%!@(MISSING),instance:%!@(MISSING),found:%!@(MISSING),end:%!@(MISSING),listen:%!@(MISSING),[set]aggregatedPolicy:%!@(MISSING),descriptor:%!@(MISSING),next:%!l(MISSING)d,found:%!@(MISSING)"
- "_personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:completion:"
- "_removeDescriptorFromFilesystem"
- "_removeDescriptorFromFilesystem:forHistoryOperation:firstClientName:"
- "autoAssetJobSetLookupResponseReceived:"
- "initForAssetType:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withDiscoveredAtomicEntries:withCatalogFromPallasResponse:"
- "initForClientDomainName:forSetClientName:forAssetSetIdentifier:withAutoAssetEntries:withLatestAtomicInstanceToVend:inhibitingImpliedScheduling:havingReceivedLookupResponse:"
- "loadManagedPrefs"
- "managed prefs: %!@(MISSING)"
- "newAssetSetStatus:forReason:forClientDomain:forAssetSetIdentifier:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:extendingWithCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
- "recordHistoryEntry:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:"
- "recordOperation:toHistoryType:fromClient:fromLayer:forAssetID:withSelector:usageCount:forClientDomainName:forAssetSetIdentifier:forAtomicInstance:withAddendumMessage:failingWithError:"
- "removing all tracking of set-job downloads in-flight [not yet fully implemented]"
- "setConfigurationPersist:fromLocation:dueToAlter:"
- "setConfigurationRefreshToVend:forSetConfiguration:fromStaged:"
- "setConfigurationRefreshToVendFromMigrated:forSetConfiguration:"
- "setConfigurationRefreshToVendFromPromoted:forSetConfiguration:"
- "setConfigurationsUpdateLatestToVend"
- "setConfigurationsUpdateLatestToVend:"
- "time=%!@(MISSING) op=%!@(MISSING) %!@(MISSING)=%!@(MISSING) count=%!l(MISSING)d domain=%!@(MISSING)%!@(MISSING)"
- "time=%!@(MISSING) op=%!@(MISSING) %!@(MISSING)=%!@(MISSING) count=%!l(MISSING)d id-%!@(MISSING) set=%!@(MISSING) domain=%!@(MISSING)%!@(MISSING)"
- "time=%!@(MISSING) op=%!@(MISSING) %!@(MISSING)=%!@(MISSING) count=%!l(MISSING)d id=%!@(MISSING) domain=%!@(MISSING)%!@(MISSING)"
- "time=%!@(MISSING) op=%!@(MISSING) %!@(MISSING)=%!@(MISSING) count=%!l(MISSING)d id=%!@(MISSING) set=%!@(MISSING) domain=%!@(MISSING)%!@(MISSING)"
- "unable to provide downloaded set-descriptor (requires personalization)"
- "updateSetDescriptorDownloaded"
- "updateSetDescriptorDownloaded:justDownloaded:"
- "v112@0:8q16q24@32q40@48@56q64@72@80@88@96@104"
- "v60@0:8@16@24B32@36@44@?52"
- "{%!@(MISSING)} atomic-instance entry no longer on the filesystem | nextAtomicEntry:%!@(MISSING) | setConfiguration:%!@(MISSING)"
- "{%!@(MISSING)} unable to locate asset-descriptor for atomic-instance entry | nextAtomicEntry:%!@(MISSING) | setConfiguration:%!@(MISSING)"
- "{%!{(MISSING)publci}@}\n[LATEST-TO-VEND] no previous latestAtomicInstanceToVend | setConfiguration:%!{(MISSING)public}@"
- "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] replaced latestAtomicInstanceToVend | setConfiguration:%!{(MISSING)public}@"
- "{%!{(MISSING)public}@}\n[LATEST-TO-VEND] unable to replace latestAtomicInstanceToVend (requires personalization) | setDescriptorToUpdate:%!{(MISSING)public}@"
- "{%!{(MISSING)public}@}\n[PROVIDE-DOWNLOADED] unable to provide downloaded set-descriptor (requires personalization) | chosenDownloadedSetDescriptor:%!{(MISSING)public}@"
- "{IssueClientReplySetJob}\n[LATEST-TO-VEND] same version found when no previous latestAtomicInstanceToVend | setConfiguration:%!{(MISSING)public}@"
- "{IssueClientReplySetJob} set-job for lock-atomic indicated same-version-found - considering as a successful lock of the atomic-instance found earlier | setJobInformation:%!{(MISSING)public}@"
- "{ResumeJobs} | Failed to write STARTUP_ACTIVATED cookie file: %!@(MISSING)"
- "{ResumeJobs} | Writing STARTUP_ACTIVATED cookie file"
- "{_removeDescriptorFromFilesystem} unable to determine local URL for descriptor:%!@(MISSING)"
- "{loadPersistedCrossCheckTrimSetDescriptors} [DROP-SET-DESCRIPTOR] set-descriptor not vended when other being vended | nextSetDescriptorToDrop:%!{(MISSING)public}@"
- "{updateSetDescriptorDownloaded} downloaded atomic-entry already tracked (ignoring duplicate) | downloadedAtomicEntry:%!@(MISSING), downloadedAssetDescriptor:%!@(MISSING)"

```
