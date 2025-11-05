## SoftwareUpdateMacController

> `/System/Library/PrivateFrameworks/SoftwareUpdateMacController.framework/Versions/A/SoftwareUpdateMacController`

```diff

-219.0.0.0.0
-  __TEXT.__text: 0xa99d0
+223.100.6.0.0
+  __TEXT.__text: 0xaa39c
   __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0x4ca8
+  __TEXT.__objc_methlist: 0x5474
   __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x13989
-  __TEXT.__oslogstring: 0x115db
-  __TEXT.__gcc_except_tab: 0x6b8
-  __TEXT.__unwind_info: 0xe18
-  __TEXT.__objc_classname: 0x56a
-  __TEXT.__objc_methname: 0x12788
+  __TEXT.__cstring: 0x13c72
+  __TEXT.__oslogstring: 0x11779
+  __TEXT.__gcc_except_tab: 0x6c4
+  __TEXT.__unwind_info: 0xe30
+  __TEXT.__objc_classname: 0x56c
+  __TEXT.__objc_methname: 0x12d9c
   __TEXT.__objc_methtype: 0x11a7
-  __TEXT.__objc_stubs: 0xbf40
-  __DATA_CONST.__got: 0x580
+  __TEXT.__objc_stubs: 0xc160
+  __DATA_CONST.__got: 0x588
   __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3670
+  __DATA_CONST.__objc_selrefs: 0x3900
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1b0
-  __AUTH_CONST.__const: 0x11b0
-  __AUTH_CONST.__cfstring: 0xe160
-  __AUTH_CONST.__objc_const: 0x9818
+  __AUTH_CONST.__const: 0x11e0
+  __AUTH_CONST.__cfstring: 0xe360
+  __AUTH_CONST.__objc_const: 0x8c40
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x6fc
+  __DATA.__objc_ivar: 0x720
   __DATA.__data: 0x660
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Versions/A/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED7D2B2D-4560-3878-87C7-B1F2506E5DA9
-  Functions: 2030
-  Symbols:   5468
-  CStrings:  7438
+  UUID: 516EBF0A-51E0-3A9C-90B3-936D7771BCDC
+  Functions: 2042
+  Symbols:   5511
+  CStrings:  7511
 
Symbols:
+ +[SUMacControllerDiag sharedDiag].cold.1
+ +[SUMacControllerPreferences fakeDisableMASuspension]
+ +[SUMacControllerRecoveryOSManager sharedManager].cold.1
+ +[SUMacControllerServer initializeServer].cold.1
+ -[SUMacControllerDescriptor alignediOSMajorVersion]
+ -[SUMacControllerDescriptor disableDeviceCompatibilityNotification]
+ -[SUMacControllerDescriptor disableMASuspension]
+ -[SUMacControllerDescriptor disableSecurityAdvisoryNotification]
+ -[SUMacControllerDescriptor documentationDeviceCompatibilityNotificationBodyString]
+ -[SUMacControllerDescriptor documentationDeviceCompatibilityNotificationTitleString]
+ -[SUMacControllerDescriptor documentationSecurityAdvisoryNotificationBodyString]
+ -[SUMacControllerDescriptor documentationSecurityAdvisoryNotificationTitleString]
+ -[SUMacControllerOverrides maxPreSUStagingOptionalAssetSize]
+ -[SUMacControllerOverrides setMaxPreSUStagingOptionalAssetSize:]
+ GCC_except_table258
+ GCC_except_table301
+ OBJC_IVAR_$_SUMacControllerDescriptor._alignediOSMajorVersion
+ OBJC_IVAR_$_SUMacControllerDescriptor._disableDeviceCompatibilityNotification
+ OBJC_IVAR_$_SUMacControllerDescriptor._disableMASuspension
+ OBJC_IVAR_$_SUMacControllerDescriptor._disableSecurityAdvisoryNotification
+ OBJC_IVAR_$_SUMacControllerDescriptor._documentationDeviceCompatibilityNotificationBodyString
+ OBJC_IVAR_$_SUMacControllerDescriptor._documentationDeviceCompatibilityNotificationTitleString
+ OBJC_IVAR_$_SUMacControllerDescriptor._documentationSecurityAdvisoryNotificationBodyString
+ OBJC_IVAR_$_SUMacControllerDescriptor._documentationSecurityAdvisoryNotificationTitleString
+ OBJC_IVAR_$_SUMacControllerOverrides._maxPreSUStagingOptionalAssetSize
+ _OBJC_CLASS_$_MAAutoAsset
+ __50-[SUMacController actionCancelCurrentState:error:]_block_invoke.562
+ __50-[SUMacController actionCancelCurrentState:error:]_block_invoke.cold.1
+ __52-[SUMacController actionPrepareRosettaUpdate:error:]_block_invoke.896
+ __52-[SUMacController actionPrepareRosettaUpdate:error:]_block_invoke.897
+ __52-[SUMacController actionPrepareRosettaUpdate:error:]_block_invoke.897.cold.1
+ __52-[SUMacController performSemiSplatForClientRequest:]_block_invoke.996
+ __53-[SUMacController actionDownloadRosettaUpdate:error:]_block_invoke.812
+ __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.601
+ __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.603
+ __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.613
+ __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.613.cold.1
+ __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.614
+ __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.614.cold.1
+ __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.cold.1
+ __55-[SUMacController actionReadyToBeginFromStartup:error:]_block_invoke.629
+ __59-[SUMacController queryCurrentStateWithOptions:completion:]_block_invoke.964
+ __59-[SUMacController queryCurrentStateWithOptions:completion:]_block_invoke.964.cold.1
+ __59-[SUMacController queryCurrentStateWithOptions:completion:]_block_invoke.968
+ ___block_descriptor_49_e8_32s40s_e20_v20?0B8"NSError"12l
+ _objc_msgSend$alignediOSMajorVersion
+ _objc_msgSend$deviceCompatibilityNotificationBodyString
+ _objc_msgSend$deviceCompatibilityNotificationTitleString
+ _objc_msgSend$disableDeviceCompatibilityNotification
+ _objc_msgSend$disableMASuspension
+ _objc_msgSend$disableSecurityAdvisoryNotification
+ _objc_msgSend$documentationDeviceCompatibilityNotificationBodyString
+ _objc_msgSend$documentationDeviceCompatibilityNotificationTitleString
+ _objc_msgSend$documentationSecurityAdvisoryNotificationBodyString
+ _objc_msgSend$documentationSecurityAdvisoryNotificationTitleString
+ _objc_msgSend$fakeDisableMASuspension
+ _objc_msgSend$maxPreSUStagingOptionalAssetSize
+ _objc_msgSend$resumeFromSoftwareUpdateWithCompletion:
+ _objc_msgSend$securityAdvisoryNotificationBodyString
+ _objc_msgSend$securityAdvisoryNotificationTitleString
+ _objc_msgSend$setMaxPreSUStagingOptionalAssetSize:
+ _objc_msgSend$setMaxPreSUStagingOptionalSize:
+ nrdSharedLogger.cold.1
- -[SUMacController actionCancelCurrentState:error:].cold.1
- -[SUMacController actionPurgeAllAssetsAtStartup:error:].cold.1
- GCC_except_table256
- GCC_except_table299
- _OUTLINED_FUNCTION_7
- __52-[SUMacController actionPrepareRosettaUpdate:error:]_block_invoke.882
- __52-[SUMacController actionPrepareRosettaUpdate:error:]_block_invoke.883
- __52-[SUMacController actionPrepareRosettaUpdate:error:]_block_invoke.883.cold.1
- __52-[SUMacController performSemiSplatForClientRequest:]_block_invoke.982
- __53-[SUMacController actionDownloadRosettaUpdate:error:]_block_invoke.798
- __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.588
- __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.598
- __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.598.cold.1
- __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.599
- __55-[SUMacController actionPurgeAllAssetsAtStartup:error:]_block_invoke.599.cold.1
- __55-[SUMacController actionReadyToBeginFromStartup:error:]_block_invoke.612
- __59-[SUMacController queryCurrentStateWithOptions:completion:]_block_invoke.950
- __59-[SUMacController queryCurrentStateWithOptions:completion:]_block_invoke.950.cold.1
- __59-[SUMacController queryCurrentStateWithOptions:completion:]_block_invoke.954
CStrings:
+ "    maxPreSUStagingOptionalAssetSize:%@\n"
+ "  alignediOSMajorVersion: %@\n"
+ "  disableDeviceCompatibilityNotification: %@\n"
+ "  disableMASuspension: %@\n"
+ "  disableSecurityAdvisoryNotification: %@\n"
+ "  documentationDeviceCompatibilityNotificationBodyString: %@\n"
+ "  documentationDeviceCompatibilityNotificationTitleString: %@\n"
+ "  documentationSecurityAdvisoryNotificationBodyString: %@\n"
+ "  documentationSecurityAdvisoryNotificationTitleString: %@\n"
+ "FakeDisableMASuspension"
+ "MaxPreSUStagingOptionalAssetSize"
+ "ResumeMA"
+ "SUMacControllerOverridesMaxPreSUStagingOptionalAssetSize"
+ "T@\"NSNumber\",N,V_maxPreSUStagingOptionalAssetSize"
+ "T@\"NSNumber\",R,&,N,V_alignediOSMajorVersion"
+ "T@\"NSString\",R,&,N,V_documentationDeviceCompatibilityNotificationBodyString"
+ "T@\"NSString\",R,&,N,V_documentationDeviceCompatibilityNotificationTitleString"
+ "T@\"NSString\",R,&,N,V_documentationSecurityAdvisoryNotificationBodyString"
+ "T@\"NSString\",R,&,N,V_documentationSecurityAdvisoryNotificationTitleString"
+ "TB,R,N,V_disableDeviceCompatibilityNotification"
+ "TB,R,N,V_disableMASuspension"
+ "TB,R,N,V_disableSecurityAdvisoryNotification"
+ "[>>>\n                                background: %@\n                    requiresPowerPluggedIn: %@\n                     restrictToIncremental: %@\n                            restrictToFull: %@\n                          allowSameVersion: %@\n              allowSameSplatRestoreVersion: %@\n                       checkAvailableSpace: %@\n                                updateType: %@\n                   softwareUpdateAssetType: %@\n                sfrSoftwareUpdateAssetType: %@\n                            splatAssetType: %@\n                      updateBrainAssetType: %@\n                    documentationAssetType: %@\n                    usesSFRSoftwareUpdates: %@\n                        usesRosettaUpdates: %@\n                     usesRecoveryOSUpdates: %@\n                     usesSplatComboUpdates: %@\n                        enablePreSUStaging: %@\n       enablePreSUStagingForOptionalAssets: %@\n          maxPreSUStagingOptionalAssetSize: %@\n       requirePreparePackageRosettaUpdates: %@\n       attemptPreparePackageRosettaUpdates: %@\n                    rosettaVersionOverride: %@\n                catalogDownloadTimeoutSecs: %@\n    softwareUpdateAssetDownloadTimeoutSecs: %@\n sfrSoftwareUpdateAssetDownloadTimeoutSecs: %@\n                       updateMetricContext: %@\n                          targetVolumeUUID: %@\n             personalizedManifestRootsPath: %@\n                 localAuthenticationUserID: %@\n                localAuthenticationContext: %@\n                         mdmBootstrapToken: %@\n                      appleConnectSsoToken: %@\n                      appleConnectDAWToken: %@\n                   authenticationServiceID: %@\n                       authenticationAppID: %@\n                     bridgeOSAllowTestMode: %@\n                 bridgeOSStagedUpdatesOnly: %@\n        bridgeOSAllowAnyCatalogCertificate: %@\n         bridgeOSIgnoreMinimumVersionCheck: %@\n                        bridgeOSCatalogURL: %@\n                   bridgeOSVersionOverride: %@\n                 bridgeOSDownloadDirectory: %@\n                  rosettaDownloadDirectory: %@\n                     enableBridgeOSInstall: %@\n                   enableOSPersonalization: %@\n            performPreflightEncryptedCheck: %@\n             performPreflightSnapshotCheck: %@\n                             userInitiated: %@\n                         skipVolumeSealing: %@\n            cancelUpdateOnClientDisconnect: %@\n                          qualityOfService: %@\n                disableRootVolumeSealCheck: %@\n                                supervised: %@\n                              requestedPMV: %@\n                         MDMUseDelayPeriod: %@\n                           delayPeriodSecs: %ld\n               liveAssetServerAudienceUUID: %@\n                               deviceClass: %@\n                  prerequisiteBuildVersion: %@\n                prerequisiteProductVersion: %@\n                prerequisiteRestoreVersion: %@\n                      targetRestoreVersion: %@\n                  installedSFRBuildVersion: %@\n                installedSFRProductVersion: %@\n                installedSFRRestoreVersion: %@\n                   installedSFRReleaseType: %@\n                installedSplatBuildVersion: %@\n              installedSplatProductVersion: %@\n              installedSplatRestoreVersion: %@\n                 installedSplatReleaseType: %@\n                                hwModelStr: %@\n                               productType: %@\n                               releaseType: %@\n               updateBrainLocationOverride: %@\n     recoveryOSUpdateBrainLocationOverride: %@\n         additionalUpdateMetricEventFields: %@\n             additionalCatalogServerParams: %@\n                additionalMSUUpdateOptions: %@\n                       additionalOverrides: %@\n<<<]"
+ "[CancellingState] Resuming MobileAsset failed."
+ "[CancellingState] Resuming MobileAsset."
+ "[CancellingState] Successfully resumed MobileAsset."
+ "[PurgeAllAssetsAtStartup] Resuming MobileAsset failed."
+ "[PurgeAllAssetsAtStartup] Resuming MobileAsset."
+ "[PurgeAllAssetsAtStartup] Successfully resumed MobileAsset."
+ "[SUMacControllerDescriptor] WARNING: fakeDisableMASuspension is set in preferences, setting fakeDisableMASuspension to YES."
+ "[SUMacControllerPreferences] Found value for MaxPreSUStagingOptionalAssetSize: %{public}@"
+ "_alignediOSMajorVersion"
+ "_disableDeviceCompatibilityNotification"
+ "_disableMASuspension"
+ "_disableSecurityAdvisoryNotification"
+ "_documentationDeviceCompatibilityNotificationBodyString"
+ "_documentationDeviceCompatibilityNotificationTitleString"
+ "_documentationSecurityAdvisoryNotificationBodyString"
+ "_documentationSecurityAdvisoryNotificationTitleString"
+ "_maxPreSUStagingOptionalAssetSize"
+ "alignediOSMajorVersion"
+ "configMaxPreSUStagingOptionalAssetSizeKey"
+ "deviceCompatibilityNotificationBodyString"
+ "deviceCompatibilityNotificationTitleString"
+ "disableDeviceCompatibilityNotification"
+ "disableMASuspension"
+ "disableSecurityAdvisoryNotification"
+ "documentationDeviceCompatibilityNotificationBodyString"
+ "documentationDeviceCompatibilityNotificationTitleString"
+ "documentationSecurityAdvisoryNotificationBodyString"
+ "documentationSecurityAdvisoryNotificationTitleString"
+ "fakeDisableMASuspension"
+ "maxPreSUStagingOptionalAssetSize"
+ "resumeFromSoftwareUpdateWithCompletion:"
+ "securityAdvisoryNotificationBodyString"
+ "securityAdvisoryNotificationTitleString"
+ "setMaxPreSUStagingOptionalAssetSize:"
+ "setMaxPreSUStagingOptionalSize:"
- "[>>>\n                                background: %@\n                    requiresPowerPluggedIn: %@\n                     restrictToIncremental: %@\n                            restrictToFull: %@\n                          allowSameVersion: %@\n              allowSameSplatRestoreVersion: %@\n                       checkAvailableSpace: %@\n                                updateType: %@\n                   softwareUpdateAssetType: %@\n                sfrSoftwareUpdateAssetType: %@\n                            splatAssetType: %@\n                      updateBrainAssetType: %@\n                    documentationAssetType: %@\n                    usesSFRSoftwareUpdates: %@\n                        usesRosettaUpdates: %@\n                     usesRecoveryOSUpdates: %@\n                     usesSplatComboUpdates: %@\n                        enablePreSUStaging: %@\n       enablePreSUStagingForOptionalAssets: %@\n       requirePreparePackageRosettaUpdates: %@\n       attemptPreparePackageRosettaUpdates: %@\n                    rosettaVersionOverride: %@\n                catalogDownloadTimeoutSecs: %@\n    softwareUpdateAssetDownloadTimeoutSecs: %@\n sfrSoftwareUpdateAssetDownloadTimeoutSecs: %@\n                       updateMetricContext: %@\n                          targetVolumeUUID: %@\n             personalizedManifestRootsPath: %@\n                 localAuthenticationUserID: %@\n                localAuthenticationContext: %@\n                         mdmBootstrapToken: %@\n                      appleConnectSsoToken: %@\n                      appleConnectDAWToken: %@\n                   authenticationServiceID: %@\n                       authenticationAppID: %@\n                     bridgeOSAllowTestMode: %@\n                 bridgeOSStagedUpdatesOnly: %@\n        bridgeOSAllowAnyCatalogCertificate: %@\n         bridgeOSIgnoreMinimumVersionCheck: %@\n                        bridgeOSCatalogURL: %@\n                   bridgeOSVersionOverride: %@\n                 bridgeOSDownloadDirectory: %@\n                  rosettaDownloadDirectory: %@\n                     enableBridgeOSInstall: %@\n                   enableOSPersonalization: %@\n            performPreflightEncryptedCheck: %@\n             performPreflightSnapshotCheck: %@\n                             userInitiated: %@\n                         skipVolumeSealing: %@\n            cancelUpdateOnClientDisconnect: %@\n                          qualityOfService: %@\n                disableRootVolumeSealCheck: %@\n                                supervised: %@\n                              requestedPMV: %@\n                         MDMUseDelayPeriod: %@\n                           delayPeriodSecs: %ld\n               liveAssetServerAudienceUUID: %@\n                               deviceClass: %@\n                  prerequisiteBuildVersion: %@\n                prerequisiteProductVersion: %@\n                prerequisiteRestoreVersion: %@\n                      targetRestoreVersion: %@\n                  installedSFRBuildVersion: %@\n                installedSFRProductVersion: %@\n                installedSFRRestoreVersion: %@\n                   installedSFRReleaseType: %@\n                installedSplatBuildVersion: %@\n              installedSplatProductVersion: %@\n              installedSplatRestoreVersion: %@\n                 installedSplatReleaseType: %@\n                                hwModelStr: %@\n                               productType: %@\n                               releaseType: %@\n               updateBrainLocationOverride: %@\n     recoveryOSUpdateBrainLocationOverride: %@\n         additionalUpdateMetricEventFields: %@\n             additionalCatalogServerParams: %@\n                additionalMSUUpdateOptions: %@\n                       additionalOverrides: %@\n<<<]"

```
