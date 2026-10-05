## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-1114.40.9.0.0
-  __TEXT.__text: 0x67374
+1114.40.10.0.0
+  __TEXT.__text: 0x673d4
   __TEXT.__lazy_helpers: 0xa8
   __TEXT.__objc_methlist: 0x708c
   __TEXT.__const: 0x5aa
   __TEXT.__gcc_except_tab: 0xc34
-  __TEXT.__cstring: 0x15531
+  __TEXT.__cstring: 0x154e1
   __TEXT.__oslogstring: 0x93c
   __TEXT.__swift5_typeref: 0x205
   __TEXT.__swift5_capture: 0x124

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x7c8
   __AUTH_CONST.__const: 0x990
-  __AUTH_CONST.__cfstring: 0xdfc0
+  __AUTH_CONST.__cfstring: 0xdfe0
   __AUTH_CONST.__objc_const: 0xdf58
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xe58

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2912
   Symbols:   4802
-  CStrings:  2225
+  CStrings:  2227
 
Functions:
~ __requiredBatteryLevelToAutoDownload : 364 -> 472
~ _SURequiredBatteryLevelForAutoDownloadForDescriptor : 452 -> 444
~ -[SUPreferences overrideAllowAutoDownloadOnBattery] : 16 -> 12
CStrings:
+ "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            MinFreeSpacePostStageOptionalAssets: %llu\n            UnentitledReserveAmount: %llu\n            PreSUStagingCacheDeleteLevel: %d\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            CDCriticalModeDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            badgingEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u day(s)\n            autoDownloadOnBatteryMinBattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@\n            splatInstallDate: %@\n            splatRollbackDate: %@\n"
+ "%s: [PREFERENCES] override allowAutoDownloadOnBattery to %d"
+ "%s: [PREFERENCES] override autoDownloadOnBatteryDelay to %.0lf"
+ "%s: autoDownloadOnBatteryDelay = %.0lf sec (~ %.2lf days)"
+ "%s: fullyUnrampedDate = %@ for %@; timeElapsed = %.0lf sec (~ %.2lf days)"
+ "If set, control if the device allows auto-downloading on battery"
+ "SUHasEnoughBatteryForAutoDownloadForDescriptor"
+ "SUHasEnoughBatteryForDownloadForDescriptor"
+ "SURequiredBatteryLevelForAutoDownloadForDescriptor"
+ "SURequiredBatteryLevelForDownloadForDescriptor"
+ "_requiredBatteryLevelToAutoDownload"
+ "getCurrentBatteryLevel"
- "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            MinFreeSpacePostStageOptionalAssets: %llu\n            UnentitledReserveAmount: %llu\n            PreSUStagingCacheDeleteLevel: %d\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            CDCriticalModeDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            badgingEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@\n            splatInstallDate: %@\n            splatRollbackDate: %@\n"
- "BOOL SUHasEnoughBatteryForAutoDownloadForDescriptor(SUDescriptor *__strong _Nonnull, NSDate *__strong _Nonnull)"
- "BOOL SUHasEnoughBatteryForDownloadForDescriptor(SUDescriptor *__strong _Nonnull)"
- "If set to true, allow auto-downloading on battery"
- "NSNumber * _Nonnull SURequiredBatteryLevelForDownloadForDescriptor(SUDescriptor *__strong _Nonnull)"
- "NSNumber *getCurrentBatteryLevel(void)"
- "autoDownloadOnBatteryDelay = %.0lf sec (~ %.2lf days)"
- "autoDownloadOnBatteryDelay is set to %.0lf sec by default"
- "fullyUnrampedDate = %@ for %@; timeElapsed = %.0lf sec (~ %.2lf days)"
- "unsigned int _requiredBatteryLevelToAutoDownload(SUDescriptor *__strong _Nonnull, BOOL, BOOL)"
```
