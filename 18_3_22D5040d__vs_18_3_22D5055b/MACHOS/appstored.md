## appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

-11.2.28.0.0
-  __TEXT.__text: 0x423e10
-  __TEXT.__auth_stubs: 0x3c60
+11.2.30.0.0
+  __TEXT.__text: 0x423bd8
+  __TEXT.__auth_stubs: 0x3c70
   __TEXT.__objc_stubs: 0x12ac0
   __TEXT.__objc_methlist: 0xb3ec
-  __TEXT.__cstring: 0x21bed
+  __TEXT.__cstring: 0x21c26
   __TEXT.__objc_methname: 0x1b285
   __TEXT.__const: 0x19d98
   __TEXT.__constg_swiftt: 0x21c0

   __TEXT.__objc_methtype: 0x7a74
   __TEXT.__swift5_capture: 0x175c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__oslogstring: 0x37e4c
+  __TEXT.__oslogstring: 0x37e7d
   __TEXT.__swift5_protos: 0x14
   __TEXT.__gcc_except_tab: 0xaafc
   __TEXT.__dlopen_cstrs: 0x45e
-  __TEXT.__unwind_info: 0x9fb0
+  __TEXT.__unwind_info: 0x9fb8
   __TEXT.__eh_frame: 0x819c
-  __DATA_CONST.__auth_got: 0x1e40
+  __DATA_CONST.__auth_got: 0x1e48
   __DATA_CONST.__got: 0x1718
-  __DATA_CONST.__auth_ptr: 0x820
-  __DATA_CONST.__const: 0x1dd10
-  __DATA_CONST.__cfstring: 0x1b120
+  __DATA_CONST.__auth_ptr: 0x800
+  __DATA_CONST.__const: 0x1dd20
+  __DATA_CONST.__cfstring: 0x1b160
   __DATA_CONST.__objc_classlist: 0x1630
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x518

   __DATA_CONST.__objc_arrayobj: 0x4c8
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x3acb0
+  __DATA.__objc_const: 0x3acd0
   __DATA.__objc_selrefs: 0x5dd0
-  __DATA.__objc_ivar: 0x24d8
+  __DATA.__objc_ivar: 0x24dc
   __DATA.__objc_data: 0xff70
   __DATA.__data: 0x6cd8
   __DATA.__bss: 0x77d0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12141
-  Symbols:   1917
-  CStrings:  15033
+  Functions: 12142
+  Symbols:   1918
+  CStrings:  15036
 
Symbols:
+ _analytics_is_event_used
CStrings:
+ "22:17:31"
+ "CREATE TABLE IF NOT EXISTS app_install (pid INTEGER, account_id INTEGER, apple_id TEXT, arcade INTEGER NOT NULL DEFAULT 0, alt_dsid TEXT, alternate_icon_name TEXT, approved INTEGER NOT NULL DEFAULT 0, artwork_url URL, auto_install_override INTEGER NOT NULL DEFAULT 0, automatic_type INTEGER NOT NULL DEFAULT 0, bundle_id TEXT, bundle_name TEXT, bundle_url URL, bundle_version TEXT, bootstrapped INTEGER NOT NULL DEFAULT 2, cancel_download_url URL, cancel_if_duplicate INTEGER NOT NULL DEFAULT 0, companion_bundle_id TEXT, check_store_queue_reason INTEGER NOT NULL DEFAULT 0, client_id TEXT, client_type INTEGER NOT NULL DEFAULT 0, coordinator_id UUID, coordinator_intent INTEGER NOT NULL DEFAULT 1, default_browser INTEGER NOT NULL DEFAULT 0, device_based_vpp INTEGER, downloader_id INTEGER, download_path TEXT, download_volume TEXT, external_id UUID, external_order INTEGER, evid INTEGER, failure_error BLOB, gizmo_pairing_id UUID, has_background_assets_extension INTEGER NOT NULL DEFAULT 0, has_messages_extension INTEGER NOT NULL DEFAULT 0, install_finished_timestamp DATETIME, install_verification_token TEXT, install_volume TEXT, item_id INTEGER, last_start_date DATETIME, launch_prohibited INTEGER NOT NULL DEFAULT 0, log_code TEXT, messages_artwork_url URL, metrics_fields JSON, optimal_download_start INTEGER, metrics_install_type INTEGER NOT NULL DEFAULT 0, order_index INTEGER, phase INTEGER NOT NULL DEFAULT 10, policy JSON, placeholder_entitlements BLOB, placeholder_path TEXT, post_processing_state INTEGER NOT NULL DEFAULT 0, preorder INTEGER NOT NULL DEFAULT 0, previous_galette_mode INTEGER, priority INTEGER NOT NULL DEFAULT 0, quarantine INTEGER NOT NULL DEFAULT 0, receipt BLOB, recovery_count INTEGER NOT NULL DEFAULT 0, redownload INTEGER NOT NULL DEFAULT 0, remote_install INTEGER NOT NULL DEFAULT 0, requires_rosetta INTEGER NOT NULL DEFAULT 0, restore_state INTEGER NOT NULL DEFAULT 0, restore_retry_count INTEGER NOT NULL DEFAULT 0, restore_type INTEGER NOT NULL DEFAULT 0, runs_on_apple_silicon INTEGER NOT NULL DEFAULT 1, runs_on_intel INTEGER NOT NULL DEFAULT 1,software_platform INTEGER NOT NULL DEFAULT 0, source_type INTEGER NOT NULL DEFAULT 0, storefront TEXT, store_cohort TEXT, store_metadata BLOB, supports_32bit_only INTEGER NOT NULL DEFAULT 0, supress_dialogs INTEGER NOT NULL DEFAULT 0, timestamp DATETIME DEFAULT (timestamp()), transaction_id TEXT, update_type INTEGER NOT NULL DEFAULT 0, vid UUID, vendor_name TEXT, watch_type INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(pid));"
+ "Jan  7 2025"
+ "[%@] Attributing network to clientID: %{public}@"
+ "preorder"
- "16:25:49"
- "CREATE TABLE IF NOT EXISTS app_install (pid INTEGER, account_id INTEGER, apple_id TEXT, arcade INTEGER NOT NULL DEFAULT 0, alt_dsid TEXT, alternate_icon_name TEXT, approved INTEGER NOT NULL DEFAULT 0, artwork_url URL, auto_install_override INTEGER NOT NULL DEFAULT 0, automatic_type INTEGER NOT NULL DEFAULT 0, bundle_id TEXT, bundle_name TEXT, bundle_url URL, bundle_version TEXT, bootstrapped INTEGER NOT NULL DEFAULT 2, cancel_download_url URL, cancel_if_duplicate INTEGER NOT NULL DEFAULT 0, companion_bundle_id TEXT, check_store_queue_reason INTEGER NOT NULL DEFAULT 0, client_id TEXT, client_type INTEGER NOT NULL DEFAULT 0, coordinator_id UUID, coordinator_intent INTEGER NOT NULL DEFAULT 1, default_browser INTEGER NOT NULL DEFAULT 0, device_based_vpp INTEGER, downloader_id INTEGER, download_path TEXT, download_volume TEXT, external_id UUID, external_order INTEGER, evid INTEGER, failure_error BLOB, gizmo_pairing_id UUID, has_background_assets_extension INTEGER NOT NULL DEFAULT 0, has_messages_extension INTEGER NOT NULL DEFAULT 0, install_finished_timestamp DATETIME, install_verification_token TEXT, install_volume TEXT, item_id INTEGER, last_start_date DATETIME, launch_prohibited INTEGER NOT NULL DEFAULT 0, log_code TEXT, messages_artwork_url URL, metrics_fields JSON, optimal_download_start INTEGER, metrics_install_type INTEGER NOT NULL DEFAULT 0, order_index INTEGER, phase INTEGER NOT NULL DEFAULT 10, policy JSON, placeholder_entitlements BLOB, placeholder_path TEXT, post_processing_state INTEGER NOT NULL DEFAULT 0, previous_galette_mode INTEGER, priority INTEGER NOT NULL DEFAULT 0, quarantine INTEGER NOT NULL DEFAULT 0, receipt BLOB, recovery_count INTEGER NOT NULL DEFAULT 0, redownload INTEGER NOT NULL DEFAULT 0, remote_install INTEGER NOT NULL DEFAULT 0, requires_rosetta INTEGER NOT NULL DEFAULT 0, restore_state INTEGER NOT NULL DEFAULT 0, restore_retry_count INTEGER NOT NULL DEFAULT 0, restore_type INTEGER NOT NULL DEFAULT 0, runs_on_apple_silicon INTEGER NOT NULL DEFAULT 1, runs_on_intel INTEGER NOT NULL DEFAULT 1,software_platform INTEGER NOT NULL DEFAULT 0, source_type INTEGER NOT NULL DEFAULT 0, storefront TEXT, store_cohort TEXT, store_metadata BLOB, supports_32bit_only INTEGER NOT NULL DEFAULT 0, supress_dialogs INTEGER NOT NULL DEFAULT 0, timestamp DATETIME DEFAULT (timestamp()), transaction_id TEXT, update_type INTEGER NOT NULL DEFAULT 0, vid UUID, vendor_name TEXT, watch_type INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(pid));"
- "Dec 16 2024"

```
