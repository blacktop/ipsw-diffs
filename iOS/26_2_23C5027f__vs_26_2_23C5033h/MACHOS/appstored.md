## appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

-12.2.9.1.0
-  __TEXT.__text: 0x40f228
-  __TEXT.__auth_stubs: 0x4760
-  __TEXT.__objc_stubs: 0x134a0
-  __TEXT.__objc_methlist: 0xe448
+12.2.12.1.0
+  __TEXT.__text: 0x416c90
+  __TEXT.__auth_stubs: 0x4770
+  __TEXT.__objc_stubs: 0x13580
+  __TEXT.__objc_methlist: 0xe510
   __TEXT.__dlopen_cstrs: 0x45e
-  __TEXT.__const: 0x18ad0
-  __TEXT.__cstring: 0x24125
-  __TEXT.__objc_methname: 0x1bd8c
-  __TEXT.__constg_swiftt: 0x2820
-  __TEXT.__swift5_typeref: 0x42f2
-  __TEXT.__swift5_fieldmd: 0x299c
+  __TEXT.__const: 0x18b50
+  __TEXT.__cstring: 0x2441e
+  __TEXT.__objc_methname: 0x1bf85
+  __TEXT.__constg_swiftt: 0x2884
+  __TEXT.__swift5_typeref: 0x4310
+  __TEXT.__swift5_fieldmd: 0x2a28
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_reflstr: 0x1d0e
+  __TEXT.__swift5_reflstr: 0x1d6f
   __TEXT.__swift5_assocty: 0x450
   __TEXT.__swift5_proto: 0x40c
-  __TEXT.__swift5_types: 0x2d0
+  __TEXT.__swift5_types: 0x2d8
   __TEXT.__objc_classname: 0x423e
-  __TEXT.__objc_methtype: 0x7dd4
-  __TEXT.__swift5_capture: 0x283c
-  __TEXT.__oslogstring: 0x3a41d
-  __TEXT.__swift_as_entry: 0x4a8
-  __TEXT.__swift_as_ret: 0x5a4
+  __TEXT.__objc_methtype: 0x7e2c
+  __TEXT.__swift5_capture: 0x28bc
+  __TEXT.__oslogstring: 0x3a975
+  __TEXT.__swift_as_entry: 0x4bc
+  __TEXT.__swift_as_ret: 0x5c4
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0xa764
-  __TEXT.__unwind_info: 0xb7a0
-  __TEXT.__eh_frame: 0xc784
-  __DATA_CONST.__auth_got: 0x23c0
-  __DATA_CONST.__got: 0x19b8
-  __DATA_CONST.__auth_ptr: 0xa10
-  __DATA_CONST.__const: 0x20528
-  __DATA_CONST.__cfstring: 0x1baa0
-  __DATA_CONST.__objc_classlist: 0x1698
+  __TEXT.__gcc_except_tab: 0xa788
+  __TEXT.__unwind_info: 0xb8c8
+  __TEXT.__eh_frame: 0xcbac
+  __DATA_CONST.__auth_got: 0x23c8
+  __DATA_CONST.__got: 0x19d8
+  __DATA_CONST.__auth_ptr: 0xa28
+  __DATA_CONST.__const: 0x207b0
+  __DATA_CONST.__cfstring: 0x1bb20
+  __DATA_CONST.__objc_classlist: 0x16a0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x498
   __DATA_CONST.__objc_dictobj: 0x190
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x35e80
-  __DATA.__objc_selrefs: 0x6720
-  __DATA.__objc_ivar: 0x2460
-  __DATA.__objc_data: 0x10cd0
-  __DATA.__data: 0x7450
+  __DATA.__objc_const: 0x36020
+  __DATA.__objc_selrefs: 0x6770
+  __DATA.__objc_ivar: 0x2464
+  __DATA.__objc_data: 0x10db0
+  __DATA.__data: 0x7510
   __DATA.__bss: 0x8880
-  __DATA.__common: 0xb6c
+  __DATA.__common: 0xb74
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 08990719-8C9D-3F39-9D29-48E34380ADA5
-  Functions: 13726
-  Symbols:   2200
-  CStrings:  18967
+  UUID: 3CCFAB09-455E-37C7-9E5E-A8C604A01256
+  Functions: 13800
+  Symbols:   2205
+  CStrings:  19026
 
Symbols:
+ _$s13OSEligibility0A6DomainO8nitrogenyA2CmFWC
+ _$s13OSEligibility0A7ContextO13countryPolicyyACSaySSGcACmFWC
+ _$s14MarketplaceKit19InstallSheetContextV6SourceO018replaceWithAppFromI5StoreyA2E0ikdE0V_tcAEmFWC
+ _$s14MarketplaceKit19InstallSheetContextV6SourceO08AppStoredE0V14showBiometrics11installType7appName7iconURL16metricsFieldData018currentDistributorN0AGSb_S2S10Foundation0P0VSgAN0S0VSgSSSgtcfC
+ _OBJC_CLASS_$_APAskToAgeRestrictionMetadata
CStrings:
+ "23:05:54"
+ ":/"
+ "Application(s) moved to alternate distribution: %{public}@"
+ "CREATE TABLE IF NOT EXISTS app_install (pid INTEGER, account_id INTEGER, apple_id TEXT, arcade INTEGER NOT NULL DEFAULT 0, alt_dsid TEXT, alternate_icon_name TEXT, artwork_url URL, auto_install_override INTEGER NOT NULL DEFAULT 0, automatic_type INTEGER NOT NULL DEFAULT 0, bundle_id TEXT, bundle_name TEXT, bundle_url URL, bundle_version TEXT, bootstrapped INTEGER NOT NULL DEFAULT 2, cancel_download_url URL, cancel_if_duplicate INTEGER NOT NULL DEFAULT 0, companion_bundle_id TEXT, check_store_queue_reason INTEGER NOT NULL DEFAULT 0, client_id TEXT, client_type INTEGER NOT NULL DEFAULT 0, coordinator_id UUID, coordinator_intent INTEGER NOT NULL DEFAULT 1, default_browser INTEGER NOT NULL DEFAULT 0, device_based_vpp INTEGER, downloader_id INTEGER, download_path TEXT, download_volume TEXT, external_id UUID, external_order INTEGER, evid INTEGER, failure_error BLOB, gizmo_pairing_id UUID, has_background_assets_extension INTEGER NOT NULL DEFAULT 0, has_messages_extension INTEGER NOT NULL DEFAULT 0, install_finished_timestamp DATETIME, install_verification_token TEXT, install_volume TEXT, item_id INTEGER, last_start_date DATETIME, launch_prohibited INTEGER NOT NULL DEFAULT 0, log_code TEXT, messages_artwork_url URL, metrics_fields JSON, optimal_download_duration INTEGER, optimal_download_start INTEGER, metrics_install_type INTEGER NOT NULL DEFAULT 0, order_index INTEGER, phase INTEGER NOT NULL DEFAULT 10, policy JSON, placeholder_entitlements BLOB, placeholder_path TEXT, post_processing_state INTEGER NOT NULL DEFAULT 0, preorder INTEGER NOT NULL DEFAULT 0, previous_galette_mode INTEGER, priority INTEGER NOT NULL DEFAULT 0, quarantine INTEGER NOT NULL DEFAULT 0, receipt BLOB, recovery_count INTEGER NOT NULL DEFAULT 0, redownload INTEGER NOT NULL DEFAULT 0, remote_install INTEGER NOT NULL DEFAULT 0, requires_rosetta INTEGER NOT NULL DEFAULT 0, restore_state INTEGER NOT NULL DEFAULT 0, restore_retry_count INTEGER NOT NULL DEFAULT 0, restore_type INTEGER NOT NULL DEFAULT 0, runs_on_apple_silicon INTEGER NOT NULL DEFAULT 1, runs_on_intel INTEGER NOT NULL DEFAULT 1,software_platform INTEGER NOT NULL DEFAULT 0, source_type INTEGER NOT NULL DEFAULT 0, storefront TEXT, store_cohort TEXT, store_metadata BLOB, supports_32bit_only INTEGER NOT NULL DEFAULT 0, supress_dialogs INTEGER NOT NULL DEFAULT 0, switch_distributor INTEGER NOT NULL DEFAULT 0, timestamp DATETIME DEFAULT (timestamp()), transaction_id TEXT, tv_provider INTEGER NOT NULL DEFAULT 0, update_type INTEGER NOT NULL DEFAULT 0, vid UUID, vendor_name TEXT, watch_type INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(pid));"
+ "ManagedAppDistribution.Common.Cancel"
+ "ManagedAppDistribution.Common.ReplaceApp"
+ "ManagedAppDistribution.SwitchingDistributor.Prompt.FromMarketplaceToAppStore.Body"
+ "ManagedAppDistribution.SwitchingDistributor.Prompt.FromWebToAppStore.Body"
+ "ManagedAppDistribution.SwitchingDistributor.Prompt.Title"
+ "MarketplaceKit"
+ "Nov  4 2025"
+ "SwitchDistributionSource"
+ "[%@] Asking to overwrite an app placeholder from a different distributor"
+ "[%@] Asking to replace app from a different distributor"
+ "[%@] Failed to ask for an exception: %{public}@"
+ "[%@] Failed to convert artwork into URL"
+ "[%@] Failed to create age rating exception but no error was thrown"
+ "[%@] Failed to create age rating exception request: %{public}@"
+ "[%@] Failed to fetch metadata for %{public}s"
+ "[%@] Invalid item ID: %{public}s"
+ "[%@] Missing age rating on Media API response"
+ "[%@] Missing artwork on Media API response"
+ "[%@] Missing item ID on Media API response"
+ "[%@] Missing name on Media API response"
+ "[%@] Preflight finished and will proceed to postamble"
+ "[%@] Successfully created age rating exception request with UUID: %{public}s"
+ "[%@] Switching failed, SINF not available"
+ "[%@] Switching failed, SINF update failed: %{public}@"
+ "[%@] Switching failed, installed application not found"
+ "[%@] Switching failed, installed variant mismatch (%{public}@ != %{public}@)"
+ "[%@] Switching failed, installed version mismatch (%lld != %{public}@)"
+ "[%@] Switching failed, invalid identity"
+ "[%@] Switching failed, metadata not available: %{public}@"
+ "[%@] Switching failed, metadata update failed: %{public}@"
+ "[%@] Switching succeeded, jumping to postamble step"
+ "[%@] System app has a rating of %llu"
+ "[%@] User requested to switch distribution source"
+ "[%{public}@] Application(s) moved to alternate distribution: %{public}@"
+ "_TtC9appstored31AskForExceptionForSystemAppTask"
+ "_installedApp"
+ "addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:metadata:withCompletion:"
+ "ageRating"
+ "applicationsDidUpdateMetadata:"
+ "appstored.AskForExceptionForSystemAppTask"
+ "com.apple.AppDistribution.ADAskForExceptionExtension"
+ "correspondingApplicationRecord"
+ "currentDistributorName"
+ "distributorBundleID"
+ "initWithBundleID:ageRating:logKey:"
+ "isEligibleToSwapDefaultBrowserApplicationIconsInProminentPositionsWithLogKey:"
+ "isReplacement"
+ "requestedAppIconURL"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "setCurrentDistributorName:"
+ "setSwitchDistributor:"
+ "showDialogToReplaceAlreadyInstalledApp:presenter:completionHandler:"
+ "switchDistributor"
+ "switch_distributor"
+ "v40@0:8@\"ApplicationProxy\"16@\"<RequestPresenter>\"24@?<v@?B>32"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"
- "01:46:00"
- "CREATE TABLE IF NOT EXISTS app_install (pid INTEGER, account_id INTEGER, apple_id TEXT, arcade INTEGER NOT NULL DEFAULT 0, alt_dsid TEXT, alternate_icon_name TEXT, artwork_url URL, auto_install_override INTEGER NOT NULL DEFAULT 0, automatic_type INTEGER NOT NULL DEFAULT 0, bundle_id TEXT, bundle_name TEXT, bundle_url URL, bundle_version TEXT, bootstrapped INTEGER NOT NULL DEFAULT 2, cancel_download_url URL, cancel_if_duplicate INTEGER NOT NULL DEFAULT 0, companion_bundle_id TEXT, check_store_queue_reason INTEGER NOT NULL DEFAULT 0, client_id TEXT, client_type INTEGER NOT NULL DEFAULT 0, coordinator_id UUID, coordinator_intent INTEGER NOT NULL DEFAULT 1, default_browser INTEGER NOT NULL DEFAULT 0, device_based_vpp INTEGER, downloader_id INTEGER, download_path TEXT, download_volume TEXT, external_id UUID, external_order INTEGER, evid INTEGER, failure_error BLOB, gizmo_pairing_id UUID, has_background_assets_extension INTEGER NOT NULL DEFAULT 0, has_messages_extension INTEGER NOT NULL DEFAULT 0, install_finished_timestamp DATETIME, install_verification_token TEXT, install_volume TEXT, item_id INTEGER, last_start_date DATETIME, launch_prohibited INTEGER NOT NULL DEFAULT 0, log_code TEXT, messages_artwork_url URL, metrics_fields JSON, optimal_download_duration INTEGER, optimal_download_start INTEGER, metrics_install_type INTEGER NOT NULL DEFAULT 0, order_index INTEGER, phase INTEGER NOT NULL DEFAULT 10, policy JSON, placeholder_entitlements BLOB, placeholder_path TEXT, post_processing_state INTEGER NOT NULL DEFAULT 0, preorder INTEGER NOT NULL DEFAULT 0, previous_galette_mode INTEGER, priority INTEGER NOT NULL DEFAULT 0, quarantine INTEGER NOT NULL DEFAULT 0, receipt BLOB, recovery_count INTEGER NOT NULL DEFAULT 0, redownload INTEGER NOT NULL DEFAULT 0, remote_install INTEGER NOT NULL DEFAULT 0, requires_rosetta INTEGER NOT NULL DEFAULT 0, restore_state INTEGER NOT NULL DEFAULT 0, restore_retry_count INTEGER NOT NULL DEFAULT 0, restore_type INTEGER NOT NULL DEFAULT 0, runs_on_apple_silicon INTEGER NOT NULL DEFAULT 1, runs_on_intel INTEGER NOT NULL DEFAULT 1,software_platform INTEGER NOT NULL DEFAULT 0, source_type INTEGER NOT NULL DEFAULT 0, storefront TEXT, store_cohort TEXT, store_metadata BLOB, supports_32bit_only INTEGER NOT NULL DEFAULT 0, supress_dialogs INTEGER NOT NULL DEFAULT 0, timestamp DATETIME DEFAULT (timestamp()), transaction_id TEXT, tv_provider INTEGER NOT NULL DEFAULT 0, update_type INTEGER NOT NULL DEFAULT 0, vid UUID, vendor_name TEXT, watch_type INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(pid));"
- "Oct 25 2025"
- "[%@] Failed to create age rating exception request with error: %{public}@"
- "[%@] Successfully created age rating exception request with UUID: %{public}@"
- "addExceptionRequestWithUUID:type:bundleIdentifier:adamID:distributorID:ageRatingValue:withCompletion:"
- "pause_resume_offer_button_label_2024E"
- "v28@?0B8@\"NSUUID\"12@\"NSError\"20"

```
