## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.40.43.0.0
-  __TEXT.__text: 0xb690c
+950.60.20.0.1
+  __TEXT.__text: 0xb7ef0
   __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0xb1a4
-  __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x22c21
-  __TEXT.__gcc_except_tab: 0x11f4
+  __TEXT.__objc_methlist: 0xb284
+  __TEXT.__const: 0x310
+  __TEXT.__cstring: 0x22f7b
+  __TEXT.__gcc_except_tab: 0x138c
   __TEXT.__oslogstring: 0x85d
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3308
+  __TEXT.__unwind_info: 0x3378
   __TEXT.__objc_classname: 0xf4b
-  __TEXT.__objc_methname: 0x19d0c
+  __TEXT.__objc_methname: 0x19e84
   __TEXT.__objc_methtype: 0x34fb
-  __TEXT.__objc_stubs: 0x14d60
+  __TEXT.__objc_stubs: 0x14ea0
   __DATA_CONST.__got: 0xdc8
   __DATA_CONST.__const: 0x2a08
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f78
+  __DATA_CONST.__objc_selrefs: 0x5fd8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x330
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x14640
-  __AUTH_CONST.__objc_const: 0x15f90
+  __AUTH_CONST.__cfstring: 0x146e0
+  __AUTH_CONST.__objc_const: 0x160b0
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x1108
-  __DATA.__objc_ivar: 0x9b8
+  __DATA.__objc_ivar: 0x9c4
   __DATA.__data: 0xe98
   __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0x1658

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 35033EA5-2524-3351-B338-8BDA3F0F5552
-  Functions: 4596
-  Symbols:   15288
-  CStrings:  10683
+  UUID: E773BB83-7BF8-3E97-8601-54B56575A659
+  Functions: 4625
+  Symbols:   15363
+  CStrings:  10719
 
Symbols:
+ +[SUSFollowUp splatActions]
+ +[SUSFollowUpAutoUpdate splatActions]
+ +[SUSFollowUpInsufficientDiskSpace _goToBSIPaneAction]
+ +[SUSFollowUpInsufficientDiskSpace splatActions]
+ +[SUSFollowUpUpdateAvailable splatActions]
+ +[SUSFollowUpUpdateAvailable splatNotificationClear]
+ +[SUSFollowUpUpdateAvailable splatNotificationDetails]
+ -[SUDescriptor setSplatInstallDate:]
+ -[SUDescriptor setSplatRollbackDate:]
+ -[SUDescriptor splatInstallDate]
+ -[SUDescriptor splatRollbackDate]
+ -[SUManagerClient autoInstallSecurityForceOff]
+ -[SUManagerClient autoInstallSecurityForceOn]
+ -[SUManagerServer autoInstallSecurityForceOff:]
+ -[SUManagerServer autoInstallSecurityForceOn:]
+ -[SURollbackDescriptor setSplatRollbackDate:]
+ -[SURollbackDescriptor splatRollbackDate]
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table163
+ GCC_except_table213
+ GCC_except_table216
+ GCC_except_table221
+ GCC_except_table224
+ GCC_except_table237
+ GCC_except_table242
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table265
+ GCC_except_table268
+ GCC_except_table299
+ GCC_except_table301
+ GCC_except_table302
+ GCC_except_table303
+ GCC_except_table304
+ GCC_except_table350
+ GCC_except_table454
+ _OBJC_IVAR_$_SUDescriptor._splatInstallDate
+ _OBJC_IVAR_$_SUDescriptor._splatRollbackDate
+ _OBJC_IVAR_$_SURollbackDescriptor._splatRollbackDate
+ ___32-[SUInstaller installCompleted:]_block_invoke_3.397
+ ___32-[SUInstaller installCompleted:]_block_invoke_4.398
+ ___45-[SUManagerClient autoInstallSecurityForceOn]_block_invoke
+ ___45-[SUManagerClient autoInstallSecurityForceOn]_block_invoke_2
+ ___46-[SUManagerClient autoInstallSecurityForceOff]_block_invoke
+ ___46-[SUManagerClient autoInstallSecurityForceOff]_block_invoke_2
+ ___46-[SUManagerServer autoInstallSecurityForceOn:]_block_invoke
+ ___46-[SUManagerServer autoInstallSecurityForceOn:]_block_invoke_2
+ ___46-[SUManagerServer autoInstallSecurityForceOn:]_block_invoke_3
+ ___47-[SUManagerServer autoInstallSecurityForceOff:]_block_invoke
+ ___47-[SUManagerServer autoInstallSecurityForceOff:]_block_invoke_2
+ ___47-[SUManagerServer autoInstallSecurityForceOff:]_block_invoke_3
+ _objc_msgSend$_goToBSIPaneAction
+ _objc_msgSend$autoInstallSecurityForceOff:
+ _objc_msgSend$autoInstallSecurityForceOn:
+ _objc_msgSend$setSplatInstallDate:
+ _objc_msgSend$setSplatRollbackDate:
+ _objc_msgSend$splatActions
+ _objc_msgSend$splatInstallDate
+ _objc_msgSend$splatNotificationClear
+ _objc_msgSend$splatNotificationDetails
+ _objc_msgSend$splatRollbackDate
+ _splatInstallDate
+ _splatRollbackDate
- GCC_except_table157
- GCC_except_table204
- GCC_except_table207
- GCC_except_table215
- GCC_except_table218
- GCC_except_table231
- GCC_except_table236
- GCC_except_table241
- GCC_except_table244
- GCC_except_table259
- GCC_except_table262
- GCC_except_table293
- GCC_except_table295
- GCC_except_table296
- GCC_except_table297
- GCC_except_table298
- GCC_except_table344
- GCC_except_table446
- ___32-[SUInstaller installCompleted:]_block_invoke_3.394
- ___32-[SUInstaller installCompleted:]_block_invoke_4.395
CStrings:
+ "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            MinFreeSpacePostStageOptionalAssets: %llu\n            UnentitledReserveAmount: %llu\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@\n            splatInstallDate: %@\n            splatRollbackDate: %@\n"
+ "-[SUManagerClient autoInstallSecurityForceOff]"
+ "-[SUManagerClient autoInstallSecurityForceOff]_block_invoke"
+ "-[SUManagerClient autoInstallSecurityForceOff]_block_invoke_2"
+ "-[SUManagerClient autoInstallSecurityForceOn]"
+ "-[SUManagerClient autoInstallSecurityForceOn]_block_invoke"
+ "-[SUManagerClient autoInstallSecurityForceOn]_block_invoke_2"
+ "-[SUManagerServer autoInstallSecurityForceOff:]"
+ "-[SUManagerServer autoInstallSecurityForceOff:]_block_invoke"
+ "-[SUManagerServer autoInstallSecurityForceOn:]"
+ "-[SUManagerServer autoInstallSecurityForceOn:]_block_invoke"
+ "Adding %@ to rolledBackDescriptor list"
+ "SURollbackDescriptor:\n              RestoreVersion: %@\n              ProductVersion: %@\n              ProductBuildVersion: %@\n              ReleaseType: %@\n              SplatRollbackDate: %@\n"
+ "Setting splatInstallDate for splat-only update: %@"
+ "T@\"NSDate\",&,N,V_splatInstallDate"
+ "T@\"NSDate\",&,N,V_splatRollbackDate"
+ "[Auto download] Beta: Downloading every 1 day"
+ "_goToBSIPaneAction"
+ "_splatInstallDate"
+ "_splatRollbackDate"
+ "autoInstallSecurityForceOff"
+ "autoInstallSecurityForceOff:"
+ "autoInstallSecurityForceOn"
+ "autoInstallSecurityForceOn:"
+ "com.followup.go_to_bsi_pane"
+ "setSplatInstallDate:"
+ "setSplatRollbackDate:"
+ "settings-navigation://com.apple.Settings.PrivacyAndSecurity/BACKGROUND_SECURITY_IMPROVEMENTS"
+ "splatActions"
+ "splatInstallDate"
+ "splatNotificationClear"
+ "splatNotificationDetails"
+ "splatRollbackDate"
- "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            MinFreeSpacePostStageOptionalAssets: %llu\n            UnentitledReserveAmount: %llu\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@"
- "Adding %@ to rolledBackDescritor list"
- "SURollbackDescriptor:\n              RestoreVersion: %@\n              ProductVersion: %@\n              ProductBuildVersion: %@\n              ReleaseType: %@\n"
- "[Auto download] Customer: Downloading every 5 days"

```
