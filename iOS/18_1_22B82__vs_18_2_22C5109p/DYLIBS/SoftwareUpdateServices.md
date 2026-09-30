## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-868.40.6.0.0
-  __TEXT.__text: 0xac948
+868.60.3.0.1
+  __TEXT.__text: 0xac924
   __TEXT.__auth_stubs: 0xf20
   __TEXT.__objc_methlist: 0x9338
-  __TEXT.__cstring: 0x1e491
-  __TEXT.__const: 0x2a8
+  __TEXT.__cstring: 0x1e48c
+  __TEXT.__const: 0x2a0
   __TEXT.__gcc_except_tab: 0x1064
   __TEXT.__oslogstring: 0xd48
   __TEXT.__dlopen_cstrs: 0x5a
Symbols:
+ OBJC_IVAR_$_SUState._autoDownloadNeedsOneTimeRetry
+ OBJC_IVAR_$_SUState._scheduledAutoDownloadPolicyChangeTime
+ OBJC_IVAR_$_SUState._scheduledAutoDownloadWifiPeriodEndTime
+ _kSUAutoDownloadWillRetryKey
- OBJC_IVAR_$_SUState._autodownloadNeedsOneTimeRetry
- OBJC_IVAR_$_SUState._scheduledAutodownloadPolicyChangeTime
- OBJC_IVAR_$_SUState._scheduledAutodownloadWifiPeriodEndTime
- _kSUAutodownloadWillRetryKey
CStrings:
+ "-[SUDownloader tryAutoDownload]"
+ "LastDownload: %!@(MISSING)            \npreferredLastScannedCoreDescriptor: %!@(MISSING)            \nalternateLastScannedCoreDescriptor: %!@(MISSING)            \nFailedPatchDescriptors: %!@(MISSING)            \nScheduledManualDownloadWifiPeriodEndTime: %!@(MISSING)            \nScheduledAutoDownloadWifiPeriodEndTime: %!@(MISSING)            \nScheduledAutoDownloadPolicyChangeTime: %!@(MISSING)            \nLastScanDate: %!@(MISSING)            \nLastAutoDownloadDate: %!@(MISSING)            \nNeedsOneTimeAutoDownloadRetry: %!@(MISSING)            \nStashbagIsPersisted: %!@(MISSING)            \nLastProductVersion: %!@(MISSING)            \nLastProductBuild: %!@(MISSING)            \nLastProductType: %!@(MISSING)            \nLastReleaseType: %!@(MISSING)            \nLastSplatRestoreVersion: %!@(MISSING)            \nLastAutoInstallOperationModel: %!@(MISSING)            \nManagedDeviceDelay: %!@(MISSING)            \nInstallPolicy: %!@(MISSING)            \nMandatoryUpdateDict: %!@(MISSING)            \nLastRollbackRecommendedBuildVersion: %!@(MISSING)            \rolledBackBuildVersions: %!@(MISSING)            \nsessionID: %!@(MISSING)            \nlastDeletedAssetID: %!@(MISSING)            \nlastAssetAudience: %!@(MISSING)            \nappliedSate: %!@(MISSING)            \nunderExclusiveControl: %!@(MISSING)            \nLastRecommendedUpdateVersion: %!@(MISSING)            \nLastRecommendedUpdateInterval: %!@(MISSING)            \nLastRecommendedUpdateDiscoveryDate: %!@(MISSING)            \nUpdateDiscoveryDates: %!@(MISSING)"
+ "SUAutoDownloadNeedsOneTimeRetry"
+ "SUAutoDownloadPolicyChangeTime"
+ "SUAutoDownloadWifiPeriodEndTime"
+ "SUAutoDownloadWillRetry"
+ "T@\"NSDate\",&,N,V_scheduledAutoDownloadPolicyChangeTime"
+ "T@\"NSDate\",&,N,V_scheduledAutoDownloadWifiPeriodEndTime"
+ "TB,N,V_autoDownloadNeedsOneTimeRetry"
+ "[Auto scan] Beta: Downloading every 1 day"
+ "_autoDownloadNeedsOneTimeRetry"
+ "_isWithinAutoDownloadWindowForPolicy:descriptor:"
+ "_scheduledAutoDownloadPolicyChangeTime"
+ "_scheduledAutoDownloadWifiPeriodEndTime"
+ "autoDownloadNeedsOneTimeRetry"
+ "cancelAllAutoDownloadTasks"
+ "cancelAutoDownloadTask"
+ "endAutoDownloadTasksAndResetState"
+ "noteAutoDownloadFailedToStart:withError:"
+ "noteAutoDownloadFailedToStartWithError:"
+ "scheduleAutoDownloadIfNecessary"
+ "scheduledAutoDownloadPolicyChangeTime"
+ "scheduledAutoDownloadWifiPeriodEndTime"
+ "setAutoDownloadNeedsOneTimeRetry:"
+ "setScheduledAutoDownloadPolicyChangeTime:"
+ "setScheduledAutoDownloadWifiPeriodEndTime:"
+ "tryAutoDownload"
+ "tryAutoDownload: Error starting autodownload: %!@(MISSING)"
- "-[SUDownloader tryAutodownload]"
- "LastDownload: %!@(MISSING)            \npreferredLastScannedCoreDescriptor: %!@(MISSING)            \nalternateLastScannedCoreDescriptor: %!@(MISSING)            \nFailedPatchDescriptors: %!@(MISSING)            \nScheduledManualDownloadWifiPeriodEndTime: %!@(MISSING)            \nScheduledAutoDownloadWifiPeriodEndTime: %!@(MISSING)            \nScheduledAutoDownloadPolicyChangeTime: %!@(MISSING)            \nLastScanDate: %!@(MISSING)            \nLastAutoDownloadDate: %!@(MISSING)            \nNeedsOneTimeAutodownloadRetry: %!@(MISSING)            \nStashbagIsPersisted: %!@(MISSING)            \nLastProductVersion: %!@(MISSING)            \nLastProductBuild: %!@(MISSING)            \nLastProductType: %!@(MISSING)            \nLastReleaseType: %!@(MISSING)            \nLastSplatRestoreVersion: %!@(MISSING)            \nLastAutoInstallOperationModel: %!@(MISSING)            \nManagedDeviceDelay: %!@(MISSING)            \nInstallPolicy: %!@(MISSING)            \nMandatoryUpdateDict: %!@(MISSING)            \nLastRollbackRecommendedBuildVersion: %!@(MISSING)            \rolledBackBuildVersions: %!@(MISSING)            \nsessionID: %!@(MISSING)            \nlastDeletedAssetID: %!@(MISSING)            \nlastAssetAudience: %!@(MISSING)            \nappliedSate: %!@(MISSING)            \nunderExclusiveControl: %!@(MISSING)            \nLastRecommendedUpdateVersion: %!@(MISSING)            \nLastRecommendedUpdateInterval: %!@(MISSING)            \nLastRecommendedUpdateDiscoveryDate: %!@(MISSING)            \nUpdateDiscoveryDates: %!@(MISSING)"
- "SUAutodownloadNeedsOneTimeRetry"
- "SUAutodownloadPolicyChangeTime"
- "SUAutodownloadWifiPeriodEndTime"
- "SUAutodownloadWillRetry"
- "T@\"NSDate\",&,N,V_scheduledAutodownloadPolicyChangeTime"
- "T@\"NSDate\",&,N,V_scheduledAutodownloadWifiPeriodEndTime"
- "TB,N,V_autodownloadNeedsOneTimeRetry"
- "[Auto scan] Customer: Downloading every 5 days"
- "_autodownloadNeedsOneTimeRetry"
- "_isWithinAutodownloadWindowForPolicy:descriptor:"
- "_scheduledAutodownloadPolicyChangeTime"
- "_scheduledAutodownloadWifiPeriodEndTime"
- "autodownloadNeedsOneTimeRetry"
- "cancelAllAutodownloadTasks"
- "cancelAutodownloadTask"
- "endAutodownloadTasksAndResetState"
- "noteAutodownloadFailedToStart:withError:"
- "noteAutodownloadFailedToStartWithError:"
- "scheduleAutodownloadIfNecessary"
- "scheduledAutodownloadPolicyChangeTime"
- "scheduledAutodownloadWifiPeriodEndTime"
- "setAutodownloadNeedsOneTimeRetry:"
- "setScheduledAutodownloadPolicyChangeTime:"
- "setScheduledAutodownloadWifiPeriodEndTime:"
- "tryAutodownload"
- "tryAutodownload: Error starting autodownload: %!@(MISSING)"

```
