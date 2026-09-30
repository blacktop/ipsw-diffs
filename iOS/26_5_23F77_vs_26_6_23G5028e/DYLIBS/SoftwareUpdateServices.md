## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.120.3.0.0
-  __TEXT.__text: 0xc39ac
+950.160.4.0.0
+  __TEXT.__text: 0xc3be0
   __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_methlist: 0xb4f4
-  __TEXT.__const: 0x338
-  __TEXT.__cstring: 0x23a97
-  __TEXT.__gcc_except_tab: 0x12c0
+  __TEXT.__objc_methlist: 0xb524
+  __TEXT.__const: 0x330
+  __TEXT.__cstring: 0x23afe
+  __TEXT.__gcc_except_tab: 0x12d4
   __TEXT.__oslogstring: 0x85d
-  __TEXT.__unwind_info: 0x36b0
-  __TEXT.__objc_classname: 0xf79
-  __TEXT.__objc_methname: 0x1a4e5
+  __TEXT.__unwind_info: 0x36c0
+  __TEXT.__objc_classname: 0xf76
+  __TEXT.__objc_methname: 0x1a4f3
   __TEXT.__objc_methtype: 0x3502
-  __TEXT.__objc_stubs: 0x15540
+  __TEXT.__objc_stubs: 0x155c0
   __DATA_CONST.__got: 0xe08
   __DATA_CONST.__const: 0x2ab0
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6180
+  __DATA_CONST.__objc_selrefs: 0x61a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x730
   __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x14dc0
-  __AUTH_CONST.__objc_const: 0x163a8
+  __AUTH_CONST.__cfstring: 0x14e20
+  __AUTH_CONST.__objc_const: 0x163b8
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F81B2595-DE0F-360D-A3E5-2D8595883465
-  Functions: 4698
-  Symbols:   15571
-  CStrings:  10899
+  UUID: D95739BB-EA62-38AD-A073-F0EE031F0AEB
+  Functions: 4703
+  Symbols:   15586
+  CStrings:  10908
 
Symbols:
+ -[SUDescriptor badgingEnabled]
+ -[SUDescriptor setBadgingEnabled:]
+ -[SUPreferences omitBadge]
+ -[SUSHistoryTracker submitAndClearEvents]
+ _OBJC_IVAR_$_SUDescriptor._badgingEnabled
+ ___40-[SUSHistoryTracker recordHistoryEvent:]_block_invoke
+ ___48-[SUSHistoryTracker submitHistoryAnalyticsEvent]_block_invoke
+ _objc_msgSend$badgingEnabled
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$omitBadge
+ _objc_msgSend$setBadgingEnabled:
+ _objc_msgSend$submitAndClearEvents
- -[SUSHistoryEvent historyProtectionQueue]
- _OBJC_IVAR_$_SUSHistoryEvent._historyProtectionQueue
- _objc_msgSend$submitHistoryAnalyticsEvent
CStrings:
+ "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            MinFreeSpacePostStageOptionalAssets: %llu\n            UnentitledReserveAmount: %llu\n            PreSUStagingCacheDeleteLevel: %d\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            badgingEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@\n            splatInstallDate: %@\n            splatRollbackDate: %@\n"
+ "-[SUSHistoryTracker submitAndClearEvents]"
+ "If set to true, follow ups use FLFollowUpItemDisplayStyleOmitBadge instead of their default display style"
+ "SUOmitBadge"
+ "TB,N,V_badgingEnabled"
+ "[Auto download] Beta: Downloading every 1 day"
+ "_badgingEnabled"
+ "badgingEnabled"
+ "containsValueForKey:"
+ "omitBadge"
+ "setBadgingEnabled:"
+ "submitAndClearEvents"
- "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            MinFreeSpacePostStageOptionalAssets: %llu\n            UnentitledReserveAmount: %llu\n            PreSUStagingCacheDeleteLevel: %d\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@\n            splatInstallDate: %@\n            splatRollbackDate: %@\n"
- "-[SUSHistoryTracker submitHistoryAnalyticsEvent]"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_historyProtectionQueue"
- "[Auto download] Customer: Downloading every 5 days"
- "_historyProtectionQueue"
- "com.apple.softwareupdateserivces.SUSHistoryEvent"
- "historyProtectionQueue"

```
