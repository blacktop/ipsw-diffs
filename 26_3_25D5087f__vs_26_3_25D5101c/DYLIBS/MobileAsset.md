## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset`

```diff

-1837.80.19.0.0
-  __TEXT.__text: 0x92470
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x68ec
+1837.80.25.0.0
+  __TEXT.__text: 0x94530
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_methlist: 0x6abc
   __TEXT.__const: 0x298
-  __TEXT.__cstring: 0x118a1
-  __TEXT.__oslogstring: 0xa59a
+  __TEXT.__cstring: 0x11ebc
+  __TEXT.__oslogstring: 0xaa2a
   __TEXT.__gcc_except_tab: 0x13d0
-  __TEXT.__unwind_info: 0x1bf0
-  __TEXT.__objc_classname: 0x8ad
-  __TEXT.__objc_methname: 0x1702a
-  __TEXT.__objc_methtype: 0x17b2
-  __TEXT.__objc_stubs: 0x88a0
-  __DATA_CONST.__got: 0x408
+  __TEXT.__unwind_info: 0x1c30
+  __TEXT.__objc_classname: 0x8ef
+  __TEXT.__objc_methname: 0x17a4f
+  __TEXT.__objc_methtype: 0x1867
+  __TEXT.__objc_stubs: 0x8aa0
+  __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0xcd0
-  __DATA_CONST.__objc_classlist: 0x258
+  __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3470
+  __DATA_CONST.__objc_selrefs: 0x3540
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x228
+  __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x2f8
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x3f0
   __AUTH_CONST.__const: 0x1d90
-  __AUTH_CONST.__cfstring: 0xe500
-  __AUTH_CONST.__objc_const: 0xa3e0
+  __AUTH_CONST.__cfstring: 0xe900
+  __AUTH_CONST.__objc_const: 0xa700
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x8d4
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x8fc
   __DATA.__data: 0x358
   __DATA.__bss: 0x138
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D38872B4-D821-3E1A-A6D7-4EC9DB35A74D
-  Functions: 2945
-  Symbols:   5966
-  CStrings:  7308
+  UUID: E8872035-42EF-3237-8843-88139CFED745
+  Functions: 2983
+  Symbols:   6046
+  CStrings:  7427
 
Symbols:
+ +[MAAutoAssetSetAssetOriginEntry basicOriginType:]
+ +[MAAutoAssetSetAssetOriginEntry nameOfBasicOriginType:]
+ +[MAAutoAssetSetAssetOriginEntry nameOfOriginType:]
+ -[MAAutoAssetSet _getXattrString:forAtomicEntry:forKey:fromPath:]
+ -[MAAutoAssetSet _getXattrUint32:forAtomicEntry:forKey:fromPath:]
+ -[MAAutoAssetSet _lockedAtomicEntriesOriginReport:forLockedAtomicInstance:oflockedAtomicEntries:error:]
+ -[MAAutoAssetSet lockedAtomicEntriesOriginReport:forLockedAtomicInstance:oflockedAtomicEntries:completion:]
+ -[MAAutoAssetSet lockedAtomicEntriesOriginReportSync:forLockedAtomicInstance:oflockedAtomicEntries:error:]
+ -[MAAutoAssetSetAssetOriginEntry .cxx_destruct]
+ -[MAAutoAssetSetAssetOriginEntry assetAvailableOSBuild]
+ -[MAAutoAssetSetAssetOriginEntry assetDownloadedOSBuild]
+ -[MAAutoAssetSetAssetOriginEntry assetOriginType]
+ -[MAAutoAssetSetAssetOriginEntry description]
+ -[MAAutoAssetSetAssetOriginEntry fullAssetSelector]
+ -[MAAutoAssetSetAssetOriginEntry initWithFullAssetSelector:withAssetOriginType:withAssetDownloadedOSBuild:withAssetAvailableOSBuild:]
+ -[MAAutoAssetSetAssetOriginEntry setAssetAvailableOSBuild:]
+ -[MAAutoAssetSetAssetOriginEntry setAssetDownloadedOSBuild:]
+ -[MAAutoAssetSetAssetOriginEntry setAssetOriginType:]
+ -[MAAutoAssetSetAssetOriginEntry setFullAssetSelector:]
+ -[MAAutoAssetSetAssetOriginEntry summary]
+ -[MAAutoAssetSetAssetOriginReport .cxx_destruct]
+ -[MAAutoAssetSetAssetOriginReport assetOriginEntries]
+ -[MAAutoAssetSetAssetOriginReport assetSetIdentifier]
+ -[MAAutoAssetSetAssetOriginReport clientDomainName]
+ -[MAAutoAssetSetAssetOriginReport description]
+ -[MAAutoAssetSetAssetOriginReport initWithClientDomainName:withAssetSetIdentifier:withOriginAtomicInstance:withAssetOriginEntries:]
+ -[MAAutoAssetSetAssetOriginReport originAtomicInstance]
+ -[MAAutoAssetSetAssetOriginReport setAssetOriginEntries:]
+ -[MAAutoAssetSetAssetOriginReport setAssetSetIdentifier:]
+ -[MAAutoAssetSetAssetOriginReport setClientDomainName:]
+ -[MAAutoAssetSetAssetOriginReport setOriginAtomicInstance:]
+ -[MAAutoAssetSetAssetOriginReport summary]
+ -[MAAutoAssetSetStatus initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDownloadedAtomicInstanceFromFactoryPreinstalled:withLatestDownloadedAtomicInstanceStagedFromOSBuild:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:]
+ -[MAAutoAssetSetStatus latestDownloadedAtomicInstanceFromFactoryPreinstalled]
+ -[MAAutoAssetSetStatus latestDownloadedAtomicInstanceStagedFromOSBuild]
+ -[MAAutoAssetSetStatus setLatestDownloadedAtomicInstanceFromFactoryPreinstalled:]
+ -[MAAutoAssetSetStatus setLatestDownloadedAtomicInstanceStagedFromOSBuild:]
+ GCC_except_table210
+ GCC_except_table220
+ GCC_except_table235
+ GCC_except_table239
+ OBJC_IVAR_$_MAAutoAssetSetAssetOriginEntry._assetAvailableOSBuild
+ OBJC_IVAR_$_MAAutoAssetSetAssetOriginEntry._assetDownloadedOSBuild
+ OBJC_IVAR_$_MAAutoAssetSetAssetOriginEntry._assetOriginType
+ OBJC_IVAR_$_MAAutoAssetSetAssetOriginEntry._fullAssetSelector
+ OBJC_IVAR_$_MAAutoAssetSetAssetOriginReport._assetOriginEntries
+ OBJC_IVAR_$_MAAutoAssetSetAssetOriginReport._assetSetIdentifier
+ OBJC_IVAR_$_MAAutoAssetSetAssetOriginReport._clientDomainName
+ OBJC_IVAR_$_MAAutoAssetSetAssetOriginReport._originAtomicInstance
+ OBJC_IVAR_$_MAAutoAssetSetStatus._latestDownloadedAtomicInstanceFromFactoryPreinstalled
+ OBJC_IVAR_$_MAAutoAssetSetStatus._latestDownloadedAtomicInstanceStagedFromOSBuild
+ _OBJC_CLASS_$_MAAutoAssetSetAssetOriginEntry
+ _OBJC_CLASS_$_MAAutoAssetSetAssetOriginReport
+ _OBJC_METACLASS_$_MAAutoAssetSetAssetOriginEntry
+ _OBJC_METACLASS_$_MAAutoAssetSetAssetOriginReport
+ __120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.628
+ __133+[MAAutoAssetSet endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:]_block_invoke.752
+ __69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.667
+ __84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.660
+ __Block_byref_object_copy_.850
+ __Block_byref_object_dispose_.851
+ __OBJC_$_CLASS_METHODS_MAAutoAssetSetAssetOriginEntry
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSetAssetOriginEntry
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSetAssetOriginReport
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetSetAssetOriginEntry
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetSetAssetOriginReport
+ __OBJC_$_PROP_LIST_MAAutoAssetSetAssetOriginEntry
+ __OBJC_$_PROP_LIST_MAAutoAssetSetAssetOriginReport
+ __OBJC_CLASS_RO_$_MAAutoAssetSetAssetOriginEntry
+ __OBJC_CLASS_RO_$_MAAutoAssetSetAssetOriginReport
+ __OBJC_METACLASS_RO_$_MAAutoAssetSetAssetOriginEntry
+ __OBJC_METACLASS_RO_$_MAAutoAssetSetAssetOriginReport
+ ___107-[MAAutoAssetSet lockedAtomicEntriesOriginReport:forLockedAtomicInstance:oflockedAtomicEntries:completion:]_block_invoke
+ __block_literal_global.718
+ __block_literal_global.870
+ __block_literal_global.875
+ __block_literal_global.877
+ __block_literal_global.879
+ _getxattr
+ _objc_msgSend$_getXattrString:forAtomicEntry:forKey:fromPath:
+ _objc_msgSend$_getXattrUint32:forAtomicEntry:forKey:fromPath:
+ _objc_msgSend$_lockedAtomicEntriesOriginReport:forLockedAtomicInstance:oflockedAtomicEntries:error:
+ _objc_msgSend$assetAvailableOSBuild
+ _objc_msgSend$assetDownloadedOSBuild
+ _objc_msgSend$assetOriginEntries
+ _objc_msgSend$assetOriginType
+ _objc_msgSend$basicOriginType:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDownloadedAtomicInstanceFromFactoryPreinstalled:withLatestDownloadedAtomicInstanceStagedFromOSBuild:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
+ _objc_msgSend$initWithClientDomainName:withAssetSetIdentifier:withOriginAtomicInstance:withAssetOriginEntries:
+ _objc_msgSend$initWithFullAssetSelector:withAssetOriginType:withAssetDownloadedOSBuild:withAssetAvailableOSBuild:
+ _objc_msgSend$latestDownloadedAtomicInstanceFromFactoryPreinstalled
+ _objc_msgSend$latestDownloadedAtomicInstanceStagedFromOSBuild
+ _objc_msgSend$nameOfBasicOriginType:
+ _objc_msgSend$nameOfOriginType:
+ _objc_msgSend$originAtomicInstance
- GCC_except_table204
- GCC_except_table214
- GCC_except_table229
- __120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.595
- __133+[MAAutoAssetSet endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:]_block_invoke.720
- __69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.634
- __84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.627
- __Block_byref_object_copy_.821
- __Block_byref_object_dispose_.822
- __block_literal_global.686
- __block_literal_global.841
- __block_literal_global.846
- __block_literal_global.848
- __block_literal_global.850
- _objc_msgSend$initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:
CStrings:
+ "                                       clientDomainName: %@\n                                     assetSetIdentifier: %@\n                                 configuredAssetEntries: %@\n                              atomicInstancesDownloaded: %@\n                                catalogCachedAssetSetID: %@\n                              catalogDownloadedFromLive: %@\n                                 catalogLastTimeChecked: %@\n                                      catalogPostedDate: %@\n                          newerAtomicInstanceDiscovered: %@\n                           newerDiscoveredAtomicEntries: %@\n                               latestDownloadedInstance: %@\n         latestDownloadedAtomicInstanceFromPreSUStaging: %@\n  latestDownloadedAtomicInstanceFromFactoryPreinstalled: %@\n        latestDownloadedAtomicInstanceStagedFromOSBuild: %@\n                         latestDowloadedInstanceEntries: %@\n                      downloadedCatalogCachedAssetSetID: %@\n                    downloadedCatalogDownloadedFromLive: %@\n                       downloadedCatalogLastTimeChecked: %@\n                            downloadedCatalogPostedDate: %@\n                                   currentNotifications: %@\n                                      currentNeedPolicy: %@\n                                        schedulerPolicy: %@\n                                           stagerPolicy: %@\n                             haveReceivedLookupResponse: %@\n                  vendingAtomicInstanceForConfigEntries: %@\n                                  downloadUserInitiated: %@\n                                       downloadProgress: %@\n                                 downloadedNetworkBytes: %ld\n                              downloadedFilesystemBytes: %ld\n                                       currentLockUsage: %@\n                                    selectorsForStaging: %@\n                                   availableForUseError: %@\n                                      newerVersionError: %@\n"
+ "%@\n"
+ "@260@0:8@16@24@32@40@48@56@64@72@80@88@96B104B108@112@120@128@136@144@152@160@168@176@184B192B196B200@204q212q220@228@236@244@252"
+ "@48@0:8@16q24@32@40"
+ "ALREADY_KNOWN"
+ "BACKOFF_RETRY"
+ "CLIENT_CHECK_DISCRETIONARY"
+ "CLIENT_CHECK_USER_INITIATED"
+ "CLIENT_LOCK_DISCRETIONARY"
+ "CLIENT_LOCK_USER_INITIATED"
+ "I48@0:8@16@24@32@40"
+ "MA-auto-set{%{public}@} | larger than expected size (xattr) | keyName:%{public}@ | atomicEntry:%{public}@ | dataSize:%ld"
+ "MA-auto-set{%{public}@} | larger than expected size (xattr) | keyName:%{public}@ | atomicEntry:%{public}@ | pathName:%{public}@ | dataSize:%ld"
+ "MA-auto-set{%{public}@} | larger than expected size for string (xattr) | keyName:%{public}@ | atomicEntry:%{public}@ | dataSize:%ld"
+ "MA-auto-set{%{public}@} | unable to determine size (xattr) | keyName:%{public}@ | atomicEntry:%{public}@ | errno:%d"
+ "MA-auto-set{%{public}@} | unable to determine size (xattr) | keyName:%{public}@ | atomicEntry:%{public}@ | pathName:%{public}@ | errno:%d"
+ "MA-auto-set{%{public}@} | unable to get string (xattr) | keyName:%{public}@ | atomicEntry:%{public}@ | errno:%d"
+ "MA-auto-set{%{public}@} | unable to get value (xattr) | keyName:%{public}@ | atomicEntry:%{public}@ | pathName:%{public}@ | errno:%d"
+ "MA-auto-set{_lockedAtomicEntriesOriginReport} | FAILURE (xattr) | originAtomicInstance:%{public}@ | originError:%{public}@"
+ "MA-auto-set{_lockedAtomicEntriesOriginReport} | SUCCESS (xattr) | originAtomicInstance:%{public}@ | assetOriginEntries:%ld | originReport:\n%{public}@"
+ "MAAutoAssetSetAssetOriginEntry"
+ "MAAutoAssetSetAssetOriginReport"
+ "NEED"
+ "NOT_YET_DETERMINED"
+ "PRE_INSTALLED"
+ "PSUS"
+ "PSUS_IMMEDIATE_PROMOTED"
+ "PSUS_NEW_OS_PROMOTED"
+ "PSUS_STAGED"
+ "PUSH_NOTIFICATION"
+ "RESUMED_IN_FLIGHT"
+ "SCHEDULER_TRIGGERED"
+ "STANDARD"
+ "T@\"NSArray\",&,N,V_assetOriginEntries"
+ "T@\"NSString\",&,N,V_assetAvailableOSBuild"
+ "T@\"NSString\",&,N,V_assetDownloadedOSBuild"
+ "T@\"NSString\",&,N,V_latestDownloadedAtomicInstanceStagedFromOSBuild"
+ "T@\"NSString\",&,N,V_originAtomicInstance"
+ "TB,N,V_latestDownloadedAtomicInstanceFromFactoryPreinstalled"
+ "TEST_PRE_INSTALLED"
+ "Tq,N,V_assetOriginType"
+ "[domain:%@|setID:%@|config:%ld|AIs:%ld(newer:%@[%ld])(latest:%@[fromPSUS:%@][fromPreinstalled:%@][stagedFrom:%@][entries:%ld])|lookupRsp:%@(forConfig:%@)|user:%@|locks:%@|availErr:%@]"
+ "_assetAvailableOSBuild"
+ "_assetDownloadedOSBuild"
+ "_assetOriginEntries"
+ "_assetOriginType"
+ "_getXattrString:forAtomicEntry:forKey:fromPath:"
+ "_getXattrUint32:forAtomicEntry:forKey:fromPath:"
+ "_latestDownloadedAtomicInstanceFromFactoryPreinstalled"
+ "_latestDownloadedAtomicInstanceStagedFromOSBuild"
+ "_lockedAtomicEntriesOriginReport"
+ "_lockedAtomicEntriesOriginReport:forLockedAtomicInstance:oflockedAtomicEntries:error:"
+ "_originAtomicInstance"
+ "assetAvailableOSBuild"
+ "assetDownloadedOSBuild"
+ "assetOriginEntries"
+ "assetOriginType"
+ "auto-set(_lockedAtomicEntriesOriginReport)"
+ "basicOriginType:"
+ "clientDomainName:%@|assetSetIdentifier:%@|originAtomicInstance:%@|assetOriginEntries:%ld"
+ "com.apple.MobileAsset.AutoAssetXattr.AssetAvailableOSBuild"
+ "com.apple.MobileAsset.AutoAssetXattr.AssetDownloadedOSBuild"
+ "com.apple.MobileAsset.AutoAssetXattr.AssetOriginType"
+ "fullAssetSelector:%@|assetOriginType:%@[%@]|assetDownloadedOSBuild:%@|assetAvailableOSBuild:%@"
+ "hasSuffix:"
+ "initStatusForClientDomain:forAssetSetIdentifier:withConfiguredAssetEntries:withAtomicInstancesDownloaded:withCatalogCachedAssetSetID:withCatalogDownloadedFromLive:withCatalogLastTimeChecked:withCatalogPostedDate:withNewerAtomicInstanceDiscovered:withNewerDiscoveredAtomicEntries:withLatestDownloadedAtomicInstance:withLatestDownloadedAtomicInstanceFromPreSUStaging:withLatestDownloadedAtomicInstanceFromFactoryPreinstalled:withLatestDownloadedAtomicInstanceStagedFromOSBuild:withLatestDowloadedAtomicInstanceEntries:withDownloadedCatalogCachedAssetSetID:withDownloadedCatalogDownloadedFromLive:withDownloadedCatalogLastTimeChecked:withDownloadedCatalogPostedDate:withCurrentNotifications:withCurrentNeedPolicy:withSchedulerPolicy:withStagerPolicy:havingReceivedLookupResponse:vendingAtomicInstanceForConfiguredEntries:withDownloadUserInitiated:withDownloadProgress:withDownloadedNetworkBytes:withDownloadedFilesystemBytes:withCurrentLockUsage:withSelectorsForStaging:withAvailableForUseError:withNewerVersionError:"
+ "initWithClientDomainName:withAssetSetIdentifier:withOriginAtomicInstance:withAssetOriginEntries:"
+ "initWithFullAssetSelector:withAssetOriginType:withAssetDownloadedOSBuild:withAssetAvailableOSBuild:"
+ "latestDownloadedAtomicInstanceFromFactoryPreinstalled"
+ "latestDownloadedAtomicInstanceStagedFromOSBuild"
+ "localContentURL is nil | nextAtomicEntry:%@"
+ "localContentURL is not a directory | nextAtomicEntry:%@ | pathToDirectoryWithXattrInformation:%@"
+ "localContentURL repository location does not exist | nextAtomicEntry:%@ | pathToDirectoryWithXattrInformation:%@"
+ "lockedAtomicEntriesOriginReport:forLockedAtomicInstance:oflockedAtomicEntries:completion:"
+ "lockedAtomicEntriesOriginReportSync:forLockedAtomicInstance:oflockedAtomicEntries:error:"
+ "nameOfBasicOriginType:"
+ "nameOfOriginType:"
+ "originAtomicInstance"
+ "q24@0:8q16"
+ "setAssetAvailableOSBuild:"
+ "setAssetDownloadedOSBuild:"
+ "setAssetOriginEntries:"
+ "setAssetOriginType:"
+ "setLatestDownloadedAtomicInstanceFromFactoryPreinstalled:"
+ "setLatestDownloadedAtomicInstanceStagedFromOSBuild:"
+ "setOriginAtomicInstance:"
+ "unable to allocate assetOriginEntry | nextAtomicEntry:%@"
- "                                clientDomainName: %@\n                              assetSetIdentifier: %@\n                          configuredAssetEntries: %@\n                       atomicInstancesDownloaded: %@\n                         catalogCachedAssetSetID: %@\n                       catalogDownloadedFromLive: %@\n                          catalogLastTimeChecked: %@\n                               catalogPostedDate: %@\n                   newerAtomicInstanceDiscovered: %@\n                    newerDiscoveredAtomicEntries: %@\n                        latestDownloadedInstance: %@\n                  latestDowloadedInstanceEntries: %@\n  latestDownloadedAtomicInstanceFromPreSUStaging: %@\n               downloadedCatalogCachedAssetSetID: %@\n             downloadedCatalogDownloadedFromLive: %@\n                downloadedCatalogLastTimeChecked: %@\n                     downloadedCatalogPostedDate: %@\n                            currentNotifications: %@\n                               currentNeedPolicy: %@\n                                 schedulerPolicy: %@\n                                    stagerPolicy: %@\n                      haveReceivedLookupResponse: %@\n           vendingAtomicInstanceForConfigEntries: %@\n                           downloadUserInitiated: %@\n                                downloadProgress: %@\n                          downloadedNetworkBytes: %ld\n                       downloadedFilesystemBytes: %ld\n                                currentLockUsage: %@\n                             selectorsForStaging: %@\n                            availableForUseError: %@\n                               newerVersionError: %@\n"
- "[domain:%@|setID:%@|config:%ld|AIs:%ld(newer:%@[%ld])(latest:%@[%ld])|lookupRsp:%@(forConfig:%@)|user:%@|locks:%@|availErr:%@]"

```
