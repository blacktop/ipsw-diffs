## appstoreagent

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstoreagent`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`

```diff

-13.0.43.0.0
-  __TEXT.__text: 0x47071c
-  __TEXT.__auth_stubs: 0x4630
-  __TEXT.__objc_stubs: 0x119a0
-  __TEXT.__objc_methlist: 0xa10c
+13.0.52.1.2
+  __TEXT.__text: 0x476f64
+  __TEXT.__auth_stubs: 0x4600
+  __TEXT.__objc_stubs: 0x11ae0
+  __TEXT.__objc_methlist: 0xa00c
   __TEXT.__dlopen_cstrs: 0x11a
-  __TEXT.__const: 0x2b258
-  __TEXT.__objc_classname: 0x3df8
-  __TEXT.__objc_methname: 0x191c5
-  __TEXT.__objc_methtype: 0x709f
-  __TEXT.__constg_swiftt: 0x2918
+  __TEXT.__const: 0x2b288
+  __TEXT.__objc_classname: 0x3e0c
+  __TEXT.__objc_methname: 0x19185
+  __TEXT.__objc_methtype: 0x70c0
+  __TEXT.__constg_swiftt: 0x2958
   __TEXT.__swift5_typeref: 0x2f88
-  __TEXT.__swift5_reflstr: 0x22ca
-  __TEXT.__swift5_fieldmd: 0x2bbc
+  __TEXT.__swift5_reflstr: 0x237a
+  __TEXT.__swift5_fieldmd: 0x2c1c
   __TEXT.__swift5_builtin: 0x294
   __TEXT.__swift5_assocty: 0x408
-  __TEXT.__cstring: 0x18d7e
+  __TEXT.__cstring: 0x18f4c
   __TEXT.__swift5_capture: 0x21e8
-  __TEXT.__oslogstring: 0x2bb0b
+  __TEXT.__oslogstring: 0x2cfb0
   __TEXT.__swift5_proto: 0x3f4
   __TEXT.__swift5_types: 0x2c8
-  __TEXT.__swift_as_entry: 0x3e0
-  __TEXT.__swift_as_ret: 0x4b8
-  __TEXT.__swift_as_cont: 0x79c
+  __TEXT.__swift_as_entry: 0x3e4
+  __TEXT.__swift_as_ret: 0x4cc
+  __TEXT.__swift_as_cont: 0x7a8
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_mpenum: 0x70
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__gcc_except_tab: 0x5388
+  __TEXT.__gcc_except_tab: 0x5394
   __TEXT.__ustring: 0x98
-  __TEXT.__unwind_info: 0x8aa8
-  __TEXT.__eh_frame: 0xa818
-  __DATA_CONST.__const: 0x20e58
-  __DATA_CONST.__cfstring: 0x14b20
-  __DATA_CONST.__objc_classlist: 0x1058
+  __TEXT.__unwind_info: 0x8b68
+  __TEXT.__eh_frame: 0xa960
+  __DATA_CONST.__const: 0x21018
+  __DATA_CONST.__cfstring: 0x14ce0
+  __DATA_CONST.__objc_classlist: 0x1068
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x420
+  __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x160
-  __DATA_CONST.__objc_superrefs: 0x9d8
-  __DATA_CONST.__objc_intobj: 0x10b0
+  __DATA_CONST.__objc_superrefs: 0x9e8
+  __DATA_CONST.__objc_intobj: 0x10c8
   __DATA_CONST.__objc_arraydata: 0x748
   __DATA_CONST.__objc_dictobj: 0x258
   __DATA_CONST.__objc_arrayobj: 0x2a0
-  __DATA_CONST.__auth_got: 0x2328
-  __DATA_CONST.__got: 0x1a68
+  __DATA_CONST.__auth_got: 0x2310
+  __DATA_CONST.__got: 0x1a80
   __DATA_CONST.__auth_ptr: 0x9e8
-  __DATA.__objc_const: 0x28560
-  __DATA.__objc_selrefs: 0x5918
-  __DATA.__objc_ivar: 0x1bfc
-  __DATA.__objc_data: 0xc1f8
-  __DATA.__data: 0x7238
-  __DATA.__bss: 0x8270
+  __DATA.__objc_const: 0x28838
+  __DATA.__objc_selrefs: 0x5898
+  __DATA.__objc_ivar: 0x1c34
+  __DATA.__objc_data: 0xc2b0
+  __DATA.__data: 0x7228
+  __DATA.__bss: 0x8280
   __DATA.__common: 0xb64
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10681
+  Functions: 10754
   Symbols:   2089
-  CStrings:  11669
+  CStrings:  11751
 
Symbols:
+ _ASDServiceDaemonMachPort
+ _OBJC_CLASS_$_ASDAppQueryConditions
+ _OBJC_CLASS_$_MIStoreMetadataContentDescriptor
- _class_copyPropertyList
- _property_copyAttributeValue
- _property_getName
CStrings:
+ "(StoreItem) Fixed incorectly formatted bundleDirectoryName: %{public}@ -> %{public}@"
+ "03:45:40"
+ "@\"RBSProcessHandle\""
+ "@24@0:8@?16"
+ "App is frontmost"
+ "App was reported as removed and LS is reporting app at an invalid path. Telling MacAppChangeNotifier that app was removed: %{public}@ : %{public}@"
+ "AppInstallQuitAssertionObserver"
+ "Aug 10 2026"
+ "CREATE TABLE IF NOT EXISTS app_install (pid INTEGER, account_id INTEGER, apple_id TEXT, arcade INTEGER NOT NULL DEFAULT 0, alt_dsid TEXT, alternate_icon_name TEXT, artwork_url URL, auto_install_override INTEGER NOT NULL DEFAULT 0, automatic_type INTEGER NOT NULL DEFAULT 0, bundle_directory_name TEXT, bundle_id TEXT, bundle_name TEXT, bundle_url URL, bundle_version TEXT, bootstrapped INTEGER NOT NULL DEFAULT 2, cancel_download_url URL, cancel_if_duplicate INTEGER NOT NULL DEFAULT 0, companion_bundle_id TEXT, check_store_queue_reason INTEGER NOT NULL DEFAULT 0, client_id TEXT, client_type INTEGER NOT NULL DEFAULT 0, coordinator_id UUID, coordinator_intent INTEGER NOT NULL DEFAULT 1, default_browser INTEGER NOT NULL DEFAULT 0, delta_error BLOB, device_based_vpp INTEGER, downloader_id INTEGER, download_path TEXT, external_id UUID, external_order INTEGER, evid INTEGER, extension_placeholder_data BLOB, failure_error BLOB, gizmo_pairing_id UUID, has_background_assets_extension INTEGER NOT NULL DEFAULT 0, has_messages_extension INTEGER NOT NULL DEFAULT 0, install_finished_timestamp DATETIME, install_options INTEGER NOT NULL DEFAULT 0, install_verification_token TEXT, install_volume TEXT, item_id INTEGER, last_start_date DATETIME, launch_prohibited INTEGER NOT NULL DEFAULT 0, log_code TEXT, messages_artwork_url URL, metrics_fields JSON, one_shot_bootstrap INTEGER NOT NULL DEFAULT 0, optimal_download_duration INTEGER, optimal_download_start INTEGER, metrics_install_type INTEGER NOT NULL DEFAULT 0, order_index INTEGER, persona_identifier TEXT, phase INTEGER NOT NULL DEFAULT 10, policy JSON, placeholder_entitlements BLOB, placeholder_path TEXT, post_processing_state INTEGER NOT NULL DEFAULT 0, preorder INTEGER NOT NULL DEFAULT 0, previous_galette_mode INTEGER, priority INTEGER NOT NULL DEFAULT 0, quarantine INTEGER NOT NULL DEFAULT 0, receipt BLOB, recovery_count INTEGER NOT NULL DEFAULT 0, redownload INTEGER NOT NULL DEFAULT 0, remote_install INTEGER NOT NULL DEFAULT 0, requires_rosetta INTEGER NOT NULL DEFAULT 0, restore_state INTEGER NOT NULL DEFAULT 0, restore_retry_count INTEGER NOT NULL DEFAULT 0, restore_type INTEGER NOT NULL DEFAULT 0, runs_on_apple_silicon INTEGER NOT NULL DEFAULT 1, runs_on_intel INTEGER NOT NULL DEFAULT 1,software_platform INTEGER NOT NULL DEFAULT 0, source_type INTEGER NOT NULL DEFAULT 0, storefront TEXT, store_cohort TEXT, store_metadata BLOB, supports_32bit_only INTEGER NOT NULL DEFAULT 0, supress_dialogs INTEGER NOT NULL DEFAULT 0, switch_distributor INTEGER NOT NULL DEFAULT 0, timestamp DATETIME DEFAULT (timestamp()), transaction_id TEXT, tv_provider INTEGER NOT NULL DEFAULT 0, update_type INTEGER NOT NULL DEFAULT 0, vid UUID, vendor_name TEXT, watch_type INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(pid));"
+ "Checking to see if dynamically-scheduled activities need scheduling"
+ "Confirmed app does not exist but LS still has record; unregistering removed app from LS: %{public}@ : %{public}@"
+ "DaemonCheckInCoordinator"
+ "Daily scheduled check"
+ "FTY"
+ "Handling true DSIDless Install of %{public}@"
+ "IXAppInstallCoordinator"
+ "MacAppChangeNotifier"
+ "PackageKit"
+ "SoftwareMap changed app version %{public}@ (wrapped=%{BOOL}d) — informing MacAppChangeNotifier; bundleVersion %{public}@ → %{public}@, shortVer %{public}@ → %{public}@, extVerID %lld → %lld"
+ "SoftwareMap moved app %{public}@ (wrapped=%{BOOL}d) - informing MacAppChangeNotifier; %{public}@ -> %{public}@"
+ "SoftwareMap non-material change to app %{public}@ - ignoring; bundleVersion %{public}@ → %{public}@, shortVer %{public}@ → %{public}@"
+ "TB,GisFactoryInstall"
+ "TDS"
+ "TDU"
+ "Telling MacAppChangeNotifier that app was removed (LS has no record): %{public}@"
+ "Update failed due to busy app"
+ "[%@] App is running; parking non-interactive install to await termination: %{public}@"
+ "[%@] App not running for PackageKit install; proceeding"
+ "[%@] App terminated; resuming PackageKit install"
+ "[%@] Created new %s%s session with identifier: %{public}@ (%{public}@)"
+ "[%@] Failed to acquire app quit assertion for PackageKit install; failing: %{public}@"
+ "[%@] Failed to encode content-cache ATS exception data error: %{public}@"
+ "[%@] Fixed incorectly formatted bundleDirectoryName: %{public}@ -> %{public}@"
+ "[%@] Found %{public}ld eligible DSIDless apps from the app ledger"
+ "[%@] No bundle to terminate for PackageKit install; proceeding"
+ "[%@] Not parking: install is interactive (isMDM=%{BOOL}d, suppressDialogs=%{BOOL}d)"
+ "[%@] Not parking: installer has no pathToAppToUpdate"
+ "[%@] Parking PackageKit install; sending Quit Apple Event to: %{public}@"
+ "[%@] Quit Apple Event for %{public}@ returned %lld; waiting for the app to exit (the assertion may still reap it)"
+ "[%@] Quit Apple Event result for %{public}@: resultCode=%lld"
+ "[%@] Releasing app quit assertion"
+ "[%@] Releasing app-quit death monitor"
+ "[%@] Resume path: %{public}@"
+ "[%@] Running app is likely not safe to auto-quit (%{public}@); not parking: %{public}@"
+ "[%@] Skipping DSID LESS app install due to restrictions disabled: auto-downloads: %{bool,public}d app-install-allowed: %{bool,public}d"
+ "[%@] Update is blocked by a running app"
+ "[%{public}s] Activity is currently running; will request upon task completion (error: %{public}@)"
+ "[%{public}s] Race attempting to update task request that no longer exists; resubmitting now (error: %{public}@)"
+ "[%{public}s] System task was expired for reason(s) %lu"
+ "[%{public}s] Unexpected error occurred attempting to update task request (error: %{public}@)"
+ "[AppChange] ApplicationProxy not found for app %{public}@ at path %{public}@; skipping user-added fanout"
+ "[AppChange] Not notifying app moved (proxy not found at new path): %{public}@ : %{public}@"
+ "[AppChange] Notifying app addition, user-added: %{public}@"
+ "[AppChange] Notifying app moved (re-registering): %{public}@ : %{public}@"
+ "[AppChange] Suppressing notifying app added for device-assigned VPP app %{public}@"
+ "[AppChange] appBecameUnavailableForBundleID: %{public}@ - Volume unmount - Issuing relevant notifications"
+ "[AppChange] handleSpotlightAppAddedForBundleID: %{public}@ - Issuing notifications"
+ "[AppChange] handleSpotlightAppAddedForBundleID: %{public}@ - received expected Spotlight discovery"
+ "[AppChange] handleSpotlightAppChangedForBundleID: %{public}@ - No notifications issued"
+ "[AppChange] handleSpotlightAppChangedForBundleID: %{public}@ — cleared Spotlight discovery marker"
+ "[AppChange] handleSpotlightAppMovedForBundleID: %{public}@ from %{public}@ to %{public}@ - Issuing notifications"
+ "[AppChange] handleSpotlightAppMovedForBundleID: %{public}@ — received spotlight discovery for an app that changed name"
+ "[AppChange] handleSpotlightAppRemovedForBundleID: %{public}@ - Suppressing notifications for self-instigated uninstall"
+ "[AppChange] handleSpotlightAppRemovedForBundleID: %{public}@ at %{public}@ - Issuing notifications"
+ "[AppChange] installAbortForBundleID: %{public}@ not in spotlight-discovery dedup set (already cleared?)"
+ "[AppChange] installAbortForBundleID: %{public}@ removed"
+ "[AppChange] installCompleteAtPath: %{public}@ (registering LS)"
+ "[AppChange] installCompleteAtPath: ApplicationProxy not found: %{public}@"
+ "[AppChange] installRequestForBundleID: %{public}@ is already awaiting discovery"
+ "[AppChange] installRequestForBundleID: %{public}@ now awaiting Spotlight discovery"
+ "[AppChange] notifying app removal (source=%{public}@) for %{public}@"
+ "[AppChange] uninstallAbortForBundleID: %{public}@ not in self-uninstall dedup set (already cleared?)"
+ "[AppChange] uninstallAbortForBundleID: %{public}@ removed"
+ "[AppChange] uninstallBeginForBundleID: %{public}@"
+ "[AppChange] uninstallCompleteForBundleID: %{public}@ - Issuing notifications"
+ "[AppChange] updateAbortForBundleID: %{public}@ not in spotlight-discovery dedup set (already cleared?)"
+ "[AppChange] updateAbortForBundleID: %{public}@ removed"
+ "[AppChange] updateRequestForBundleID: %{public}@ is already awaiting discovery"
+ "[AppChange] updateRequestForBundleID: %{public}@ now awaiting Spotlight discovery"
+ "[DaemonCheckIn] Candidate %{public}@: quittingWillBeNoisyOrLoseData=%{BOOL}d isActive=%{BOOL}d"
+ "[DaemonCheckIn] Could not reach the daemon callback service: %{public}@"
+ "[DaemonCheckIn] Daemon reports %lu parked app(s): %{public}@"
+ "[DaemonCheckIn] Error asking the daemon for parked apps: %{public}@"
+ "[DaemonCheckIn] No matching running candidate for bundleID=%{public}@; app may have already quit"
+ "[DaemonCheckIn] Not quitting %{public}@ — frontmost or would lose data; leaving parked"
+ "[DaemonCheckIn] Notification received (token=%d); checking in"
+ "[DaemonCheckIn] Parked app entry missing a valid bundleID, skipping: %{public}@"
+ "[DaemonCheckIn] Performing startup check-in"
+ "[DaemonCheckIn][%@] Sending Quit Apple Event to parked app: %{public}@"
+ "[Uninstall:%{public}@] Notifying MacAppChangeNotifier of successful self-uninstall: %{public}@"
+ "[Uninstall:%{public}@] Uninstall failed; NOT notifying MacAppChangeNotifier (app presumed still installed): %{public}@"
+ "[Uninstall] Self-uninstall succeeded but no bundleID (proxy not found); not notifying MacAppChangeNotifier — Spotlight will report the removal"
+ "_MacDaemonCallbackServiceEntitlement"
+ "_MacDaemonCallbackServiceProvider"
+ "_allowsContentCacheATSBypass"
+ "_bundleIDsRecentlySelfUninstalled"
+ "_checkInQueue"
+ "_checkInToken"
+ "_contentDescriptorIDs"
+ "_factoryInstall"
+ "_pendingPollReasons"
+ "_pollCycleActive"
+ "_pollExecutor"
+ "_quitAssertionObserver"
+ "_secondaryGenreID"
+ "_sinfLess"
+ "_terminationDeathMonitorHandle"
+ "_usingContentCacheSession"
+ "allowsUpdates"
+ "allowsUpdates:"
+ "appsAwaitingTerminationWithReply:"
+ "arm64"
+ "beginFactoryAppInstallsWithReplyHandler:"
+ "cache-ats"
+ "cacheSession"
+ "com.apple.AppStoreDaemon.MacAppChangeNotifier"
+ "com.apple.AppStoreDaemon.MacAppChangeNotifier.Notify"
+ "com.apple.appmanagedfeaturesd"
+ "com.apple.appstoreagent.daemon-checkin"
+ "com.apple.appstored.daemon-checkin"
+ "content-cache "
+ "contentDescriptors"
+ "descriptionForConditionsData:"
+ "deviceArchitecture"
+ "executeQueryWithConditionsData:onPairedDevice:withReplyHandler:"
+ "executeQueryWithConditionsData:onRemoteDevice:withReplyHandler:"
+ "executeQueryWithConditionsData:withReplyHandler:"
+ "factoryInstall"
+ "getMacDaemonCallbackServiceWithCompletionHandler:"
+ "getMacDaemonCallbackServiceWithReplyHandler:"
+ "initWithHandler:"
+ "install_options"
+ "installedExternalVersionId"
+ "installedVariantId"
+ "isDSIDlessThatUpdates"
+ "isFactoryInstall"
+ "newBrokerForMachServiceName:"
+ "predicateForConditionsData:error:"
+ "requestProperties"
+ "secondaryGenreId"
+ "self-uninstall"
+ "setContentDescriptors:"
+ "setExpirationHandlerWithReasonMask:"
+ "setSecondaryGenreID:"
+ "sinflessFactoryInstall"
+ "spotlight"
+ "trueDSIDlessUpdate"
+ "v16@?0@\"ApplicationProxy\"8"
+ "v24@0:8@?<v@?@\"<ASDMacDaemonCallbackServiceProtocol><NSXPCProxyCreating>\"@\"NSError\">16"
+ "v24@?0@\"<ASDMacDaemonCallbackServiceProtocol><NSXPCProxyCreating>\"8@\"NSError\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"NSUUID\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "x86-64"
- "01:52:12"
- "App was reported as removed and LS is reporting app at an invalid path. Telling library that app was removed: %{public}@ : %{public}@"
- "Attempted to register added app, but ApplicationProxy not found for app at path: %{public}@"
- "Auto-update failed due to busy app"
- "CREATE TABLE IF NOT EXISTS app_install (pid INTEGER, account_id INTEGER, apple_id TEXT, arcade INTEGER NOT NULL DEFAULT 0, alt_dsid TEXT, alternate_icon_name TEXT, artwork_url URL, auto_install_override INTEGER NOT NULL DEFAULT 0, automatic_type INTEGER NOT NULL DEFAULT 0, bundle_directory_name TEXT, bundle_id TEXT, bundle_name TEXT, bundle_url URL, bundle_version TEXT, bootstrapped INTEGER NOT NULL DEFAULT 2, cancel_download_url URL, cancel_if_duplicate INTEGER NOT NULL DEFAULT 0, companion_bundle_id TEXT, check_store_queue_reason INTEGER NOT NULL DEFAULT 0, client_id TEXT, client_type INTEGER NOT NULL DEFAULT 0, coordinator_id UUID, coordinator_intent INTEGER NOT NULL DEFAULT 1, default_browser INTEGER NOT NULL DEFAULT 0, delta_error BLOB, device_based_vpp INTEGER, downloader_id INTEGER, download_path TEXT, external_id UUID, external_order INTEGER, evid INTEGER, extension_placeholder_data BLOB, failure_error BLOB, gizmo_pairing_id UUID, has_background_assets_extension INTEGER NOT NULL DEFAULT 0, has_messages_extension INTEGER NOT NULL DEFAULT 0, install_finished_timestamp DATETIME, install_verification_token TEXT, install_volume TEXT, item_id INTEGER, last_start_date DATETIME, launch_prohibited INTEGER NOT NULL DEFAULT 0, log_code TEXT, messages_artwork_url URL, metrics_fields JSON, one_shot_bootstrap INTEGER NOT NULL DEFAULT 0, optimal_download_duration INTEGER, optimal_download_start INTEGER, metrics_install_type INTEGER NOT NULL DEFAULT 0, order_index INTEGER, persona_identifier TEXT, phase INTEGER NOT NULL DEFAULT 10, policy JSON, placeholder_entitlements BLOB, placeholder_path TEXT, post_processing_state INTEGER NOT NULL DEFAULT 0, preorder INTEGER NOT NULL DEFAULT 0, previous_galette_mode INTEGER, priority INTEGER NOT NULL DEFAULT 0, quarantine INTEGER NOT NULL DEFAULT 0, receipt BLOB, recovery_count INTEGER NOT NULL DEFAULT 0, redownload INTEGER NOT NULL DEFAULT 0, remote_install INTEGER NOT NULL DEFAULT 0, requires_rosetta INTEGER NOT NULL DEFAULT 0, restore_state INTEGER NOT NULL DEFAULT 0, restore_retry_count INTEGER NOT NULL DEFAULT 0, restore_type INTEGER NOT NULL DEFAULT 0, runs_on_apple_silicon INTEGER NOT NULL DEFAULT 1, runs_on_intel INTEGER NOT NULL DEFAULT 1,sinfless_install INTEGER NOT NULL DEFAULT 0, software_platform INTEGER NOT NULL DEFAULT 0, source_type INTEGER NOT NULL DEFAULT 0, storefront TEXT, store_cohort TEXT, store_metadata BLOB, supports_32bit_only INTEGER NOT NULL DEFAULT 0, supress_dialogs INTEGER NOT NULL DEFAULT 0, switch_distributor INTEGER NOT NULL DEFAULT 0, timestamp DATETIME DEFAULT (timestamp()), transaction_id TEXT, tv_provider INTEGER NOT NULL DEFAULT 0, update_type INTEGER NOT NULL DEFAULT 0, vid UUID, vendor_name TEXT, watch_type INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(pid));"
- "Cannot create a bundle reference: %{public}@"
- "Cannot create a wrapped container URL despite being told by Spotlight this is a wrapped app: %{public}@"
- "Checking to see if sbsync needs scheduling"
- "Daily sbsync scheduled check"
- "G"
- "Invalid expression type '%lu' in expression: %@"
- "Invalid key path '%@' in expression: %@"
- "Jul 11 2026"
- "LSApplicationWorkspaceObserverProtocol"
- "MDQuery changed app: %{public}@"
- "PredicateValidator"
- "SFL"
- "Telling library and internal clients that app was user added: %{public}@ : %{public}@"
- "Telling library that app was removed: %{public}@"
- "Unknown validation error"
- "[%@] Auto-update is blocked by a running app"
- "[%@] Created new %s session with identifier: %{public}@ (%{public}@)"
- "[%{public}s] Error occurred attempting to update task request; will request upon task completion (error: %{public}@)"
- "[32B]"
- "_acceptableExpressionTypes"
- "_acceptableKeyPaths"
- "_bundleIDsBeingInstalled"
- "_errors"
- "_host"
- "allowEvaluation"
- "applicationIconDidChange:"
- "applicationInstallsArePrioritized:arePaused:"
- "applicationInstallsDidCancel:"
- "applicationInstallsDidChange:"
- "applicationInstallsDidPause:"
- "applicationInstallsDidPrioritize:"
- "applicationInstallsDidResume:"
- "applicationInstallsDidStart:"
- "applicationInstallsDidUpdateIcon:"
- "applicationStateDidChange:"
- "applicationsDidChangePersonas:"
- "applicationsDidFailToInstall:"
- "applicationsDidFailToUninstall:"
- "applicationsDidInstall:"
- "applicationsDidUninstall:"
- "applicationsDidUpdateMetadata:"
- "applicationsWillInstall:"
- "applicationsWillUninstall:"
- "beginSINFLessAppInstallsWithReplyHandler:"
- "com.apple.appstored.SoftwareMap.Notify"
- "databaseWasRebuilt"
- "deviceManagementPolicyDidChange:"
- "executeQueryWithPredicate:onPairedDevice:withReplyHandler:"
- "executeQueryWithPredicate:onRemoteDevice:withReplyHandler:"
- "executeQueryWithPredicate:withReplyHandler:"
- "helperPlaceholdersInstalled:"
- "helperPlaceholdersUninstalled:"
- "installAbortForBundleID called but bundleID is not being tracked: %{public}@"
- "installCompleteAtPath called but bundleID is not being tracked: %{public}@"
- "installRequestForBundleID called but bundleID is already being tracked: %{public}@"
- "networkUsageChanged:"
- "observeLaunchProhibitedApps"
- "pluginsDidInstall:"
- "pluginsDidUninstall:"
- "pluginsWillUninstall:"
- "predicateFormat"
- "sinfLess"
- "sinfless_install"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@\"NSPredicate\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v40@0:8@\"NSPredicate\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSPredicate\"16@\"NSUUID\"24@?<v@?@\"NSArray\"@\"NSError\">32"
```
