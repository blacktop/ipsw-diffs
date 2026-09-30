## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-1837.80.19.0.0
-  __TEXT.__text: 0x84d34
-  __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_methlist: 0x68ec
+1837.80.25.0.0
+  __TEXT.__text: 0x86b1c
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x6abc
   __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x11933
-  __TEXT.__oslogstring: 0xa67c
+  __TEXT.__cstring: 0x11f4e
+  __TEXT.__oslogstring: 0xab0c
   __TEXT.__gcc_except_tab: 0x13bc
-  __TEXT.__unwind_info: 0x1bc8
-  __TEXT.__objc_classname: 0x8ad
-  __TEXT.__objc_methname: 0x1702a
-  __TEXT.__objc_methtype: 0x17b2
-  __TEXT.__objc_stubs: 0x8880
-  __DATA_CONST.__got: 0x410
+  __TEXT.__unwind_info: 0x1c00
+  __TEXT.__objc_classname: 0x8ef
+  __TEXT.__objc_methname: 0x17a4f
+  __TEXT.__objc_methtype: 0x1867
+  __TEXT.__objc_stubs: 0x8a80
+  __DATA_CONST.__got: 0x420
   __DATA_CONST.__const: 0x20f8
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
-  __AUTH_CONST.__auth_got: 0x508
+  __AUTH_CONST.__auth_got: 0x510
   __AUTH_CONST.__const: 0x700
-  __AUTH_CONST.__cfstring: 0xe5c0
-  __AUTH_CONST.__objc_const: 0xa3e0
+  __AUTH_CONST.__cfstring: 0xe9c0
+  __AUTH_CONST.__objc_const: 0xa700
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x270
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x8d4
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x8fc
   __DATA.__data: 0x358
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 57693344-1F54-3A36-AF1B-998B30E509F1
-  Functions: 2894
-  Symbols:   8742
-  CStrings:  7324
+  UUID: 32F3D50E-D876-356C-8B33-7C7D4BB8A02C
+  Functions: 2932
+  Symbols:   8860
+  CStrings:  7443
 
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
+ GCC_except_table182
+ GCC_except_table190
+ GCC_except_table203
+ GCC_except_table205
+ GCC_except_table207
+ _OBJC_CLASS_$_MAAutoAssetSetAssetOriginEntry
+ _OBJC_CLASS_$_MAAutoAssetSetAssetOriginReport
+ _OBJC_IVAR_$_MAAutoAssetSetAssetOriginEntry._assetAvailableOSBuild
+ _OBJC_IVAR_$_MAAutoAssetSetAssetOriginEntry._assetDownloadedOSBuild
+ _OBJC_IVAR_$_MAAutoAssetSetAssetOriginEntry._assetOriginType
+ _OBJC_IVAR_$_MAAutoAssetSetAssetOriginEntry._fullAssetSelector
+ _OBJC_IVAR_$_MAAutoAssetSetAssetOriginReport._assetOriginEntries
+ _OBJC_IVAR_$_MAAutoAssetSetAssetOriginReport._assetSetIdentifier
+ _OBJC_IVAR_$_MAAutoAssetSetAssetOriginReport._clientDomainName
+ _OBJC_IVAR_$_MAAutoAssetSetAssetOriginReport._originAtomicInstance
+ _OBJC_IVAR_$_MAAutoAssetSetStatus._latestDownloadedAtomicInstanceFromFactoryPreinstalled
+ _OBJC_IVAR_$_MAAutoAssetSetStatus._latestDownloadedAtomicInstanceStagedFromOSBuild
+ _OBJC_METACLASS_$_MAAutoAssetSetAssetOriginEntry
+ _OBJC_METACLASS_$_MAAutoAssetSetAssetOriginReport
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
+ ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.596
+ ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.635
+ ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.628
+ ___Block_byref_object_copy_.811
+ ___Block_byref_object_dispose_.812
+ ___block_literal_global.686
+ ___block_literal_global.829
+ ___block_literal_global.834
+ ___block_literal_global.836
+ ___block_literal_global.838
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
- GCC_except_table176
- GCC_except_table184
- GCC_except_table191
- GCC_except_table201
- ___120-[MAAutoAssetSet _shortTermLockAtomicHelper:forAtomicInstance:performContentValidation:isSynchronous:completionHandler:]_block_invoke.563
- ___69-[MAAutoAssetSet _shortTermCurrentSetStatusIsSynchronous:completion:]_block_invoke.602
- ___84-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:isSynchronous:completion:]_block_invoke.595
- ___Block_byref_object_copy_.782
- ___Block_byref_object_dispose_.783
- ___block_literal_global.654
- ___block_literal_global.800
- ___block_literal_global.805
- ___block_literal_global.807
- ___block_literal_global.809
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
