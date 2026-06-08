## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

-3860.600.12.0.0
-  __TEXT.__text: 0x8a9d8
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__delay_helper: 0x14c
-  __TEXT.__objc_stubs: 0xa840
-  __TEXT.__objc_methlist: 0x61b4
-  __TEXT.__const: 0x278
-  __TEXT.__gcc_except_tab: 0x10934
-  __TEXT.__cstring: 0x39b3
-  __TEXT.__objc_methname: 0xf154
-  __TEXT.__objc_classname: 0xbef
-  __TEXT.__objc_methtype: 0x2f3a
-  __TEXT.__oslogstring: 0xf58a
-  __TEXT.__unwind_info: 0x3080
-  __DATA_CONST.__auth_got: 0x868
-  __DATA_CONST.__got: 0x730
-  __DATA_CONST.__auth_ptr: 0x8
+3886.100.1.0.0
+  __TEXT.__text: 0x82f1c
+  __TEXT.__auth_stubs: 0x11b0
+  __TEXT.__lazy_helpers: 0xfc
+  __TEXT.__objc_stubs: 0xa940
+  __TEXT.__objc_methlist: 0x61bc
+  __TEXT.__const: 0x270
+  __TEXT.__gcc_except_tab: 0xe5d4
+  __TEXT.__cstring: 0x3a7e
+  __TEXT.__objc_methname: 0xf185
+  __TEXT.__objc_classname: 0xb94
+  __TEXT.__objc_methtype: 0x2f57
+  __TEXT.__oslogstring: 0xf81a
+  __TEXT.__unwind_info: 0x2de0
   __DATA_CONST.__const: 0x15c8
-  __DATA_CONST.__cfstring: 0x1d80
+  __DATA_CONST.__cfstring: 0x1da0
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x130

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x8ea8
-  __DATA.__objc_selrefs: 0x36e8
-  __DATA.__objc_ivar: 0x704
+  __DATA_CONST.__auth_got: 0x8f0
+  __DATA_CONST.__got: 0x720
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x8e78
+  __DATA.__objc_selrefs: 0x3718
+  __DATA.__objc_ivar: 0x700
   __DATA.__objc_data: 0x1630
+  __DATA.__lazy_load_got: 0x18
   __DATA.__data: 0xe4c
   __DATA.__bss: 0x138
-  - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
-  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 33355234-A8DE-30EC-BDB3-35EA03BB05E4
-  Functions: 2069
-  Symbols:   496
-  CStrings:  4137
+  UUID: C99499C3-A2F1-30A8-9F23-CC8122CDDEAC
+  Functions: 2071
+  Symbols:   514
+  CStrings:  4155
 
Symbols:
+ _CONTAINER_PERSONA_CURRENT
+ _OBJC_CLASS_$_NSURLSessionTaskMetrics
+ _SecTaskCopySigningIdentifier
+ __dyld_lazy_load
+ _container_copy_object
+ _container_error_copy_unlocalized_description
+ _container_free_object
+ _container_get_identifier
+ _container_get_path
+ _container_get_user_managed_assets_relative_path
+ _container_query_create
+ _container_query_free
+ _container_query_get_last_error
+ _container_query_get_single_result
+ _container_query_operation_set_flags
+ _container_query_set_class
+ _container_query_set_identifiers
+ _container_query_set_persona_unique_string
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x10
+ _objc_retain_x4
+ _sqlite3_changes
+ _xpc_string_create
- _CPCopyBundleIdentifierAndTeamFromAuditToken
- _OBJC_CLASS_$___CFN_TaskMetrics
- _container_create_or_lookup_path_for_current_user
- _container_user_managed_assets_relative_path
- _dlopen
- _objc_release_x2
CStrings:
+ "%{public}@ deferring resume - parallel task limit reached (%lu/%lu)"
+ "AVAssetDownloadSessionDiscretionaryKey"
+ "Container (identifier=%s) assets path is nil"
+ "Container (identifier=%s) path is nil"
+ "Could not find container from query."
+ "Error executing container query (bundleID = %@): %s"
+ "Failed to bind WHERE bundle_id to the statement"
+ "Failed to bind WHERE identifier to the statement"
+ "Failed to bind WHERE session_id (count) to the statement"
+ "Failed to bind WHERE session_id to the statement"
+ "Failed to bind limit to the select statement"
+ "Failed to bind max tasks limit to the statement"
+ "INSERT OR REPLACE INTO session_tasks(\tidentifier, task_kind, creation_time, state, suspend_count, task_description, original_request, current_request, response, earliest_begin_date,\tresponded_to_will_begin_delayed_request_callback, error, retry_error, file_url, download_file_url, bundle_id, session_id, has_started, should_cancel_on_disconnect,\tbase_priority, base_priority_set_explicitly, discretionary, discretionary_override, unique_identifier, storage_partition_identifier, count_of_bytes_client_expects_to_send,\tcount_of_bytes_client_expects_to_receive, count_of_bytes_received, count_of_bytes_sent, count_of_bytes_expected_to_send, count_of_bytes_expected_to_receive,\tbytes_per_second_limit, persona_unique_string, expected_progress_target, may_be_demoted_to_discretionary, tls_minimum_supported_protocol_version,\ttls_maximum_supported_protocol_version, has_sz_extractor, does_sz_extractor_consume_extracted_data, updated_streaming_zip_modification_date, started_user_initiated,\tadditional_properties, path_to_download_task_file, retry_count, loading_priority, qos, background_trailers, task_metrics,\tav_url, av_destination_url, av_options, av_initialized_with_av_asset, av_temporary_destination_url, av_asset_title, av_asset_artwork_data, av_asset_url, av_asset_download_token,\tav_asset_download_child_download_session_identifier, av_enable_spi_delegate_callbacks, av_download_config, av_asset_options_plist, resumable_upload_data, rowid) \tSELECT ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\t\t\t(SELECT max(rowid) FROM session_tasks)+1 \tWHERE EXISTS (SELECT 1 FROM session_tasks WHERE identifier = ? AND session_id = ?) \t\tOR (SELECT COUNT(*) FROM session_tasks WHERE session_id = ? AND bundle_id = ?) < ?"
+ "NDNWSession <%{public}@> <%zu> will retry data task"
+ "Refused to persist task %lu for session %{public}@ (bundle: %{public}@): task limit (%d) reached"
+ "Resuming pending task %@ (%lu pending, %lu active)"
+ "SELECT * from session_tasks WHERE session_id = ? LIMIT ?"
+ "^{container_object_s=}16@0:8"
+ "_backgroundSchedulingPriority"
+ "_cfnMetricsDaemon"
+ "_fileURL"
+ "_pendingTasksToResume"
+ "_preferredMaxParallelTasks"
+ "_resumeURL"
+ "atsTrustPolicy"
+ "currentTransactionMetrics"
+ "queryAndCopyContainer"
+ "resumeNextPendingTaskIfNeeded"
+ "setCookieOnCurrentRequest:"
+ "set_atsTrustPolicy:"
+ "set_automaticRetry:"
+ "set_backgroundSchedulingDelay:"
+ "set_backgroundSchedulingPriority:"
+ "set_preferredMaxParallelTasks:"
+ "unsignedCharValue"
+ "\xf0\xe1"
- "/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
- "DisallowCellularDueToSystemPolicy"
- "Error getting User managed assets path: %llu"
- "Error getting container path: %llu"
- "INSERT OR REPLACE INTO session_tasks(\tidentifier, task_kind, creation_time, state, suspend_count, task_description, original_request, current_request, response, earliest_begin_date,\tresponded_to_will_begin_delayed_request_callback, error, retry_error, file_url, download_file_url, bundle_id, session_id, has_started, should_cancel_on_disconnect,\tbase_priority, base_priority_set_explicitly, discretionary, discretionary_override, unique_identifier, storage_partition_identifier, count_of_bytes_client_expects_to_send,\tcount_of_bytes_client_expects_to_receive, count_of_bytes_received, count_of_bytes_sent, count_of_bytes_expected_to_send, count_of_bytes_expected_to_receive,\tbytes_per_second_limit, persona_unique_string, expected_progress_target, may_be_demoted_to_discretionary, tls_minimum_supported_protocol_version,\ttls_maximum_supported_protocol_version, has_sz_extractor, does_sz_extractor_consume_extracted_data, updated_streaming_zip_modification_date, started_user_initiated,\tadditional_properties, path_to_download_task_file, retry_count, loading_priority, qos, background_trailers, task_metrics,\tav_url, av_destination_url, av_options, av_initialized_with_av_asset, av_temporary_destination_url, av_asset_title, av_asset_artwork_data, av_asset_url, av_asset_download_token,\tav_asset_download_child_download_session_identifier, av_enable_spi_delegate_callbacks, av_download_config, av_asset_options_plist, resumable_upload_data, rowid) \tvalues (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\t\t\t(SELECT max(rowid) FROM session_tasks)+1)"
- "SELECT * from session_tasks WHERE session_id = ? LIMIT 512"
- "T@\"NSString\",&,N,V_watchExtensionBundleIdentifier"
- "_watchExtensionBundleIdentifier"
- "backgroundSchedulingPriority"
- "resumeURL"
- "setAutomaticRetry:"
- "setBackgroundSchedulingDelay:"
- "setBackgroundSchedulingPriority:"
- "setWatchExtensionBundleIdentifier:"
- "set_disallowCellular:"
- "set_watchExtensionBundleIdentifier:"
- "watchExtensionBundleIdentifier"
- "\xf0\xf1"

```
