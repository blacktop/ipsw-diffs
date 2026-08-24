## mdmclient

> `/usr/libexec/mdmclient`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1911.0.1.0.0
-  __TEXT.__text: 0x13c054
-  __TEXT.__auth_stubs: 0x2550
-  __TEXT.__objc_stubs: 0xa4e0
+1911.1.1.0.0
+  __TEXT.__text: 0x136098
+  __TEXT.__auth_stubs: 0x2510
+  __TEXT.__objc_stubs: 0x9e00
   __TEXT.__init_offsets: 0x28
   __TEXT.__objc_methlist: 0x2a68
-  __TEXT.__gcc_except_tab: 0x2ff54
-  __TEXT.__cstring: 0x37ef6
+  __TEXT.__gcc_except_tab: 0x2ef78
+  __TEXT.__cstring: 0x36c05
   __TEXT.__const: 0x231
-  __TEXT.__objc_methname: 0xa22a
+  __TEXT.__objc_methname: 0x9cfc
   __TEXT.__objc_classname: 0x510
   __TEXT.__objc_methtype: 0x13b8
   __TEXT.__oslogstring: 0x148

   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x6b10
-  __DATA_CONST.__const: 0x35b8
-  __DATA_CONST.__cfstring: 0x34180
+  __TEXT.__unwind_info: 0x69e8
+  __DATA_CONST.__const: 0x3518
+  __DATA_CONST.__cfstring: 0x32c20
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd0
-  __DATA_CONST.__objc_arraydata: 0x18e8
-  __DATA_CONST.__objc_dictobj: 0x6b8
+  __DATA_CONST.__objc_arraydata: 0x18b0
+  __DATA_CONST.__objc_dictobj: 0x690
   __DATA_CONST.__objc_arrayobj: 0x798
   __DATA_CONST.__objc_intobj: 0x420
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x12c0
-  __DATA_CONST.__got: 0xe20
+  __DATA_CONST.__auth_got: 0x12a0
+  __DATA_CONST.__got: 0xd48
   __DATA.__objc_const: 0x4548
-  __DATA.__objc_selrefs: 0x2da8
+  __DATA.__objc_selrefs: 0x2bf0
   __DATA.__objc_ivar: 0x2f4
   __DATA.__objc_data: 0xd88
   __DATA.__data: 0xb3a
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xe20
+  __DATA.__bss: 0xdd0
   __DATA.__common: 0xb0
   __RESTRICT.__restrict: 0x0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 3575
-  Symbols:   1064
-  CStrings:  9062
+  Functions: 3542
+  Symbols:   1033
+  CStrings:  8835
 
Symbols:
- _OBJC_CLASS_$_SUOSUMDMController
- _OBJC_CLASS_$_SUOSUMajorProduct
- _SUOSUConfigurationDictionaryAutoUpdatesEnabledKey
- _SUOSUConfigurationDictionaryAutomaticallyCheckForUpdatesEnabledKey
- _SUOSUConfigurationDictionaryBackgroundDownloadsEnabledKey
- _SUOSUConfigurationDictionaryIsDefaultLegacyCatalogKey
- _SUOSUConfigurationDictionaryLegacyCatalogURLKey
- _SUOSUConfigurationDictionaryPreviousScanDateKey
- _SUOSUConfigurationDictionarySecurityUpdatesEnabledKey
- _SUOSUInstallDidFail
- _SUOSUInstallDidSucceed
- _SUOSUInstallOptionsDoItLaterDeferralMaximumKey
- _SUOSUInstallOptionsDownloadAndNotifyKey
- _SUOSUInstallOptionsDownloadOnlyKey
- _SUOSUInstallOptionsForceRestartKey
- _SUOSUInstallOptionsForegroundKey
- _SUOSUInstallOptionsMDMInitiatedKey
- _SUOSUInstallOptionsScheduleUpdateForLaterKey
- _SUOSUInstallScanningForUpdate
- _SUOSUMDMDeferralsLeft
- _SUOSUMDMDoItLaterScheduledDate
- _SUOSUMDMError
- _SUOSUMDMMaxDeferrals
- _SUOSUMDMProductMarketingVersion
- _SUOSUMDMProgress
- _SUOSUMDMState
- _SUOSUMDMUserNotificationTimes
- __LSVersionNumberCopyStringRepresentation
- __LSVersionNumberGetCurrentSystemVersion
- __LSVersionNumberGetMajorComponent
- __LSVersionNumberGetMinorComponent
CStrings:
- "  AutoInstallTimeRemain:   %@"
- "  AvailabilityText:        %@"
- "  AvailabilityTitle:       %@"
- "  DelayHours:              %@"
- "  Major BundleID:          %@"
- "  Major Title:             %@"
- "  Major Version:           %@"
- "  NotifyAfterInstall:      %@"
- "  Optional:                %@"
- "  OutOfBox:                %@"
- "  PostInstallText:         %@"
- "  PostInstallTitle:        %@"
- "  PostInstallURL:          %@"
- "  VersionMax:              %@"
- "  VersionMin:              %@"
- " (INTERNAL)"
- " | "
- "(?)"
- "-OSUpdateSettings"
- "-OSXSoftwareUpdateStatus"
- "-SoftwareUpdateDeviceID"
- "-availableUpdateWithError: completed with error: %@"
- ".pmv contains unexpected gunk: <%@>"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MCXTools/ConfigProfiles/mdmclient/MajorOSUpdateSupport.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MCXTools/ConfigProfiles/mdmclient/OSUpdateSupport.mm"
- "0123456789."
- "999"
- "; %@"
- "<Eventual Restart>"
- "<Restart>"
- "<Shutdown>"
- "=== OS Update Item ==="
- "======================"
- "Allows InstalLater:        %@"
- "AllowsInstallLater"
- "AppIdentifiersToClose"
- "Apps to close:             %@"
- "Async trigger background SU scan"
- "AttemptAutoInstall"
- "AutoCheckEnabled"
- "AutoUpdate"
- "AutoUpdate:                %@"
- "AutomaticAppInstallationEnabled"
- "AutomaticOSInstallationEnabled"
- "AutomaticSecurityUpdatesEnabled"
- "Available updates (install debug profile for more details): %@"
- "AvailableOSUpdates"
- "AvailableUpdates returned error: %@"
- "BackgroundDownloadEnabled"
- "Build"
- "Calling -availableUpdateWithError:"
- "CatalogURL"
- "Checking status of all OS updates..."
- "Cleaned OS version from '%@' to '%@'"
- "ConfigData:                %@"
- "Critical:                  %@"
- "DeferralsRemaining"
- "Deferred:                  %@  (Date: %@)"
- "DeferredUntil"
- "Downgrading OS to: %@ not allowed"
- "Download size:             %@"
- "DownloadOnly"
- "DownloadPercentComplete"
- "DownloadSize"
- "Downloading"
- "Empty list of updates.  Scanning for all available updates"
- "Firmware warning:          %@"
- "FirmwareUpdate:            %@"
- "Force"
- "Found %@ available updates."
- "GatherAllAvailableUpdatesForInstall found: %@"
- "Generating list of available updates"
- "Have update for unknown productKey: %@"
- "High"
- "HumanReadableName"
- "HumanReadableNameLocale"
- "INTERNAL"
- "Ignoring IA-based installer"
- "Ignoring revoked splat update. ProductKey: %@; Title: %@  Version: %@"
- "Ignoring status IA-based updates: %@"
- "Ignoring unsupported InstallAction: %@ (will proceed as 'Default')"
- "Ignoring update"
- "InstallASAP"
- "InstallForceRestart"
- "InstallLater"
- "IsConfigDataUpdate"
- "IsCritical"
- "IsDefaultCatalog"
- "IsDownloaded"
- "IsFirmwareUpdate"
- "IsMacOSUpdate():           %@"
- "IsMajorOSUpdate"
- "IsSecurityResponse"
- "Known productKeys: %@"
- "License text:              %@"
- "Localization:              %@"
- "Long attr desc:            %@"
- "Long desc:                 %@"
- "Low"
- "MDM requested: %@"
- "MSU:                       %@  (Major: %@  Full: %@  DL: %@  label: %@)"
- "MacOSUpdate:               %@"
- "MajorOSUpdate is missing displayVersion: %@"
- "Mandatory:                 %@"
- "Mapped status SU: [%@] to MDM: [%@]"
- "MaxDeferrals"
- "MaxUserDeferrals"
- "MetadataURL"
- "Missing 'ProductKey' or 'ProductVersion'"
- "NextScheduledInstall"
- "No '%@' provided for update: %@"
- "Not supported while waiting for DeviceConfigured"
- "NotifyOnly"
- "OSUpdate"
- "OSUpdateSettings"
- "OSUpdateStatus"
- "OSXSoftwareUpdateStatus"
- "PastNotifications"
- "Post install:              %@"
- "Prefetching Bootstrap Token for SoftwareUpdate"
- "PreviousScanDate"
- "Priority"
- "ProcessAllCommandsAtMacBuddy"
- "Processing status for '%@': %@"
- "Product Key:               %@"
- "ProductKey"
- "ProductVersion"
- "QueryAvailableUpdates (for Gather) error: %@"
- "QueryAvailableUpdates error: %@"
- "Ramped:                    %@"
- "Recommended:               %@"
- "Requesting SU scan."
- "Requesting installUpdates (PMV): %@  InstallAction: %@ options: %@"
- "Requesting installUpdates: %@  InstallAction: %@ options: %@"
- "Requesting updates for: %@"
- "RequiresBootstrapToken"
- "RestartRequired"
- "SU scan was started"
- "SUMacControllerError"
- "SUOSUMDMError contains NSError not NSString: %@"
- "ScanInitiated"
- "ScanInititated"
- "ScheduleForLater"
- "ScheduleOSUpdate"
- "ScheduleOSUpdateScan"
- "ScheduleOSXSoftwareUpdateScan"
- "ScheduleOSXUpdates"
- "ServerMetaDataURL:         %@"
- "SoftwareUpdate admin deferral mismatch. deferred: %@  deferralDate: %@  productKey: %@ (%@)"
- "SoftwareUpdatePrefetch"
- "Splat:                     %@  <%@> (Revoked: %@)"
- "Tags:                      %@"
- "Title:                     %@"
- "Unable to queue update: (Product: %@  PMV: %@) ==> %@"
- "Unexpected type for SUOSUMDMError: %@ (%@) in: %@"
- "Unrecognized update priority ==> %@"
- "Unspecified"
- "UpdateResults"
- "UpdateStatus '%@' ==> %@"
- "Updates"
- "Version:                   %@ <Build: %@> <PMV: %@>"
- "Will execute SU scan request async."
- "allowedToUseInstallLater"
- "applicationIdentifiersToClose"
- "availableUpdatesWithError:"
- "com.apple.commerce"
- "criticalUpdateAutoInstallWithDelayInHours"
- "criticalUpdateAvailabilityNotificationText"
- "criticalUpdateAvailabilityNotificationTitle"
- "criticalUpdatePostInstallNotificationInfoURL"
- "criticalUpdatePostInstallNotificationText"
- "criticalUpdatePostInstallNotificationTitle"
- "criticalUpdateShouldNotifyAfterInstall"
- "currentLocalization"
- "currentSoftwareUpdateServerConfiguration"
- "deferralEnablementDate"
- "download cancelled"
- "download error"
- "downloadSize"
- "downloadable"
- "downloaded"
- "firmwareWarningText"
- "hardwareModelString"
- "initiateBackgroundScan failed: %@"
- "initiateBackgroundScanWithError:"
- "install error"
- "installMacOSUpdateWithProductMarketingVersion:withOptions:withError:"
- "installUpdates:withOptions:withError:"
- "isAdminDeferred"
- "isAutoUpdateEligible"
- "isConfigData"
- "isCritical"
- "isFirmwareUpdate"
- "isFullReplacement"
- "isMSUUpdate"
- "isMacOSUpdate"
- "isMajorUpdate"
- "isMandatoryUpdate"
- "isRamped"
- "isRecommended"
- "isSplat"
- "licenseAgreementText"
- "longAttributedDescription"
- "longDescription"
- "majorOSBundleIdentifier"
- "majorOSDisplayTitle"
- "majorOSDisplayVersion"
- "mandatoryUpdateOptional"
- "mandatoryUpdateRestrictedToOutOfBox"
- "mandatoryUpdateVersionMax"
- "mandatoryUpdateVersionMin"
- "msuUpdateLabel"
- "not running"
- "postInstallAction"
- "productBuildVersion"
- "productKey"
- "productMarketingVersion"
- "productVersionExtra"
- "serverMetadataURL"
- "splatRevoked"
- "tags"
- "timeRemainingBeforeCriticalAutoInstallIfApplicable"
- "updateStatusForKeys:"
- "versionString"
- "waiting to download"
- "waiting to install"
- "{}"
```
