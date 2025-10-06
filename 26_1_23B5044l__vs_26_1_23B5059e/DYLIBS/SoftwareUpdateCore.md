## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.40.19.502.1
-  __TEXT.__text: 0xa5450
+2422.40.31.0.4
+  __TEXT.__text: 0xa5c2c
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x79d4
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x15381
-  __TEXT.__oslogstring: 0xc570
+  __TEXT.__objc_methlist: 0x7a8c
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x15428
+  __TEXT.__oslogstring: 0xc64e
   __TEXT.__gcc_except_tab: 0x758
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x1770
-  __TEXT.__objc_classname: 0x71c
-  __TEXT.__objc_methname: 0x15911
-  __TEXT.__objc_methtype: 0xfcc
-  __TEXT.__objc_stubs: 0xe9a0
-  __DATA_CONST.__got: 0x928
-  __DATA_CONST.__const: 0x2310
-  __DATA_CONST.__objc_classlist: 0x1e0
+  __TEXT.__unwind_info: 0x1780
+  __TEXT.__objc_classname: 0x73b
+  __TEXT.__objc_methname: 0x15afa
+  __TEXT.__objc_methtype: 0xff8
+  __TEXT.__objc_stubs: 0xeae0
+  __DATA_CONST.__got: 0x940
+  __DATA_CONST.__const: 0x2318
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4438
-  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_selrefs: 0x44a0
+  __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x12be0
-  __AUTH_CONST.__objc_const: 0xa710
+  __AUTH_CONST.__cfstring: 0x12c60
+  __AUTH_CONST.__objc_const: 0xa8d8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x9a8
+  __AUTH.__objc_data: 0x640
+  __DATA.__objc_ivar: 0x9c0
   __DATA.__data: 0x360
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E6C6C805-A452-3ED6-B175-312A2FC86B7E
-  Functions: 3020
-  Symbols:   10238
-  CStrings:  9007
+  UUID: 1841920C-7116-3BE3-B5F2-CB2CD4BE1F1B
+  Functions: 3036
+  Symbols:   10296
+  CStrings:  9041
 
Symbols:
+ -[SUCoreDescriptor minReserveSpace]
+ -[SUCoreDescriptor minimumReserveFreeSpace]
+ -[SUCoreDescriptor setMinReserveSpace:]
+ -[SUCoreDescriptor setSplatInstallDate:]
+ -[SUCoreDescriptor splatInstallDate]
+ -[SUCoreRollbackDescriptor rollbackDate]
+ -[SUCoreRollbackDescriptor setRollbackDate:]
+ -[SUCoreRollbackDescriptor setSplatRollbackDate:]
+ -[SUCoreRollbackDescriptor splatRollbackDate]
+ -[SUCoreScan _decideReserveSpace:error:]
+ -[SUCoreUpdate preSUStagingFinished:]
+ -[SUCoreUpdatePreSUStagingOutcome .cxx_destruct]
+ -[SUCoreUpdatePreSUStagingOutcome description]
+ -[SUCoreUpdatePreSUStagingOutcome error]
+ -[SUCoreUpdatePreSUStagingOutcome initWithError:]
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_SUCoreUpdatePreSUStagingOutcome
+ _OBJC_IVAR_$_SUCoreDescriptor._minReserveSpace
+ _OBJC_IVAR_$_SUCoreDescriptor._minimumReserveFreeSpace
+ _OBJC_IVAR_$_SUCoreDescriptor._splatInstallDate
+ _OBJC_IVAR_$_SUCoreRollbackDescriptor._rollbackDate
+ _OBJC_IVAR_$_SUCoreRollbackDescriptor._splatRollbackDate
+ _OBJC_IVAR_$_SUCoreUpdatePreSUStagingOutcome._error
+ _OBJC_METACLASS_$_SUCoreUpdatePreSUStagingOutcome
+ __OBJC_$_INSTANCE_METHODS_SUCoreUpdatePreSUStagingOutcome
+ __OBJC_$_INSTANCE_VARIABLES_SUCoreUpdatePreSUStagingOutcome
+ __OBJC_$_PROP_LIST_SUCoreUpdatePreSUStagingOutcome
+ __OBJC_CLASS_RO_$_SUCoreUpdatePreSUStagingOutcome
+ __OBJC_METACLASS_RO_$_SUCoreUpdatePreSUStagingOutcome
+ ___37-[SUCoreUpdate preSUStagingFinished:]_block_invoke
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.566
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.567
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1094
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1098
+ ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1105
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1155
+ ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1156
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.476
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke_4
+ ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.529
+ _kSUAssetSUMinReserveSpace
+ _objc_msgSend$_decideReserveSpace:error:
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$minReserveSpace
+ _objc_msgSend$preSUStagingFinished:
+ _objc_msgSend$rollbackDate
+ _objc_msgSend$setFormatOptions:
+ _objc_msgSend$setRollbackDate:
+ _objc_msgSend$setSplatInstallDate:
+ _objc_msgSend$setSplatRollbackDate:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$splatInstallDate
- -[SUCoreScan _decideReserveSpace:]
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.563
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.564
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1091
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1095
- ___53-[SUCoreMobileAsset alterDownloadOptions:completion:]_block_invoke.1102
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke.1152
- ___54-[SUCoreMobileAsset _registerProgressAndStartDownload]_block_invoke_2.1153
- ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.473
- ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.526
- _objc_msgSend$_decideReserveSpace:
CStrings:
+ "                 promoteAlternateUpdate: %@\n           enableAlternateAssetAudience: %@\n             alternateAssetAudienceUUID: %@\n                      assetAudienceUUID: %@\n                          uniqueBuildID: %@\n                       splatInstallDate:%@\n                              trainName: %@\n                         productVersion: %@\n                    productBuildVersion: %@\n                    productVersionExtra: %@\n                      productSystemName: %@\n                            releaseType: %@\n                              publisher: %@\n                         restoreVersion: %@\n              targetUpdateBridgeVersion: %@\n                 targetUpdateSFRVersion: %@\n                            releaseDate: %@\n                      prerequisiteBuild: %@\n                  prerequisiteOSVersion: %@\n                       supportedDevices: %@\n                        fullReplacement: %@\n                           downloadSize: %llu\n                         unarchivedSize: %llu\n                         msuPrepareSize: %llu\n                 msuSnapshotPrepareSize: %llu\n                        preparationSize: %llu\n                       installationSize: %llu\n             minimumSystemPartitionSize: %llu\n                 totalRequiredFreeSpace: %llu\n                    streamingZipCapable: %@\n                 systemPartitionPadding: %@\n                 psusRequiredAssetsSize: %llu\n                 psusOptionalAssetsSize: %llu\n                    disableReserveSpace: %@\n                         suDownloadSize: %llu\n"
+ "            centeralizedPurgeableFactor: %lu\n                  pluginPurgeableFactor: %lu\n                        minReserveSpace: %llu\n                        maxReserveSpace: %llu\n                unentitledReserveAmount: %llu\n               installationSnapshotSize: %llu\n<<<]"
+ "%{public}@ delegate does not respond to selector(preSUStagingFinished:) so not reporting psusOutcome=%{public}@"
+ "1.0.6"
+ "MinReserveSpace"
+ "SUCoreUpdatePreSUStagingOutcome"
+ "SUMinReserveSpace"
+ "SplatInstallDate"
+ "T@\"NSDate\",&,N,V_rollbackDate"
+ "T@\"NSDate\",&,N,V_splatInstallDate"
+ "T@\"NSDate\",&,N,V_splatRollbackDate"
+ "TQ,N,V_minReserveSpace"
+ "TQ,R,N,V_minimumReserveFreeSpace"
+ "[%@ >>>\n\terror: %@\n<<<]\n"
+ "[POLICY] Select major/minor software update for policy: %{public}@"
+ "[POLICY] constructMADocumentationAssetDownloadOptionsWithUUID for policy: %{public}@"
+ "[POLICY] constructMASoftwareUpdateAssetDownloadOptionsWithUUID for policy: %{public}@"
+ "[POLICY] constructMASoftwareUpdateCatalogDownloadOptionsWithUUID for policy: %{public}@"
+ "[POLICY] constructSoftwareUpdateMAAssetQuery for policy: %{public}@"
+ "[POLICY] selectDocumentationAsset:fromAssetQuery for policy: %{public}@"
+ "[POLICY] selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery for policy: %{public}@"
+ "[POLICY_UPDATE_BRAIN] constructSoftwareUpdateMAAssetQuery for policy: %{public}@"
+ "[POLICY_UPDATE_BRAIN] selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery for policy: %{public}@"
+ "[PURGE] cache delete purge results: %{public}@"
+ "[SPACE] %s: APFS entitled space is %{public}@"
+ "[SPACE] %{public}s: trying to set reserve space while in paused state, %{public}@"
+ "[SPACE] Checking available space from base path %{public}@. Required free space: %lld"
+ "[Space] %s, isReserveSpaceDisabled: %@, anyUpdateIsIncremental: %@, shouldUseReserveSpace: %@"
+ "_decideReserveSpace:error:"
+ "_minReserveSpace"
+ "_minimumReserveFreeSpace"
+ "_rollbackDate"
+ "_splatInstallDate"
+ "_splatRollbackDate"
+ "localTimeZone"
+ "minReserveSpace"
+ "minimumReserveFreeSpace"
+ "preSUStagingFinished:"
+ "restoreVersion:%@ productVersion:%@ producBuildVersion:%@ releaseType:%@ rollbackEligible:%@ rollbackDate:%@"
+ "rollbackDate"
+ "setFormatOptions:"
+ "setMinReserveSpace:"
+ "setRollbackDate:"
+ "setSplatInstallDate:"
+ "setSplatRollbackDate:"
+ "setTimeZone:"
+ "splatInstallDate"
+ "splatRollbackDate"
+ "unable to stat volume: %{public}s : %{public}s"
+ "v24@0:8@\"SUCoreUpdatePreSUStagingOutcome\"16"
- "                 promoteAlternateUpdate: %@\n           enableAlternateAssetAudience: %@\n             alternateAssetAudienceUUID: %@\n                      assetAudienceUUID: %@\n                          uniqueBuildID: %@\n                              trainName: %@\n                         productVersion: %@\n                    productBuildVersion: %@\n                    productVersionExtra: %@\n                      productSystemName: %@\n                            releaseType: %@\n                              publisher: %@\n                         restoreVersion: %@\n              targetUpdateBridgeVersion: %@\n                 targetUpdateSFRVersion: %@\n                            releaseDate: %@\n                      prerequisiteBuild: %@\n                  prerequisiteOSVersion: %@\n                       supportedDevices: %@\n                        fullReplacement: %@\n                           downloadSize: %llu\n                         unarchivedSize: %llu\n                         msuPrepareSize: %llu\n                 msuSnapshotPrepareSize: %llu\n                        preparationSize: %llu\n                       installationSize: %llu\n             minimumSystemPartitionSize: %llu\n                 totalRequiredFreeSpace: %llu\n                    streamingZipCapable: %@\n                 systemPartitionPadding: %@\n                 psusRequiredAssetsSize: %llu\n                 psusOptionalAssetsSize: %llu\n                    disableReserveSpace: %@\n                         suDownloadSize: %llu\n"
- "            centeralizedPurgeableFactor: %lu\n                  pluginPurgeableFactor: %lu\n                        maxReserveSpace: %llu\n                unentitledReserveAmount: %llu\n               installationSnapshotSize: %llu\n<<<]"
- "%@ Security Response %@ %@"
- "1.0.5"
- "[POLICY] Select major/minor software update for policy: %@"
- "[POLICY] constructMADocumentationAssetDownloadOptionsWithUUID for policy: %@"
- "[POLICY] constructMASoftwareUpdateAssetDownloadOptionsWithUUID for policy: %@"
- "[POLICY] constructMASoftwareUpdateCatalogDownloadOptionsWithUUID for policy: %@"
- "[POLICY] constructSoftwareUpdateMAAssetQuery for policy: %@"
- "[POLICY] selectDocumentationAsset:fromAssetQuery for policy: %@"
- "[POLICY] selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery for policy: %@"
- "[POLICY_UPDATE_BRAIN] constructSoftwareUpdateMAAssetQuery for policy: %@"
- "[POLICY_UPDATE_BRAIN] selectSoftwareUpdatePrimaryAsset:secondaryAsset:fromAssetQuery for policy: %@"
- "[PURGE] cache delete purge results: %@"
- "[Prealloc Space] %s, isReserveSpaceDisabled: %@, anyUpdateIsIncremental: %@, shouldUseReserveSpace: %@"
- "[SPACE] %s: APFS entitled space is %@"
- "[SPACE] %s: trying to set reserve space while in paused state, %{public}@"
- "[SPACE] Checking available space from base path %@.  Required free space: %lld"
- "_decideReserveSpace:"
- "restoreVersion:%@ productVersion:%@ producBuildVersion:%@ releaseType:%@ rollbackEligible:%@"
- "unable to stat volume: %s : %s"

```
