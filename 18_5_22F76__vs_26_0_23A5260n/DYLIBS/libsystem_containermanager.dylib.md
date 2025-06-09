## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-689.100.6.0.0
-  __TEXT.__text: 0x27484
+725.0.3.0.1
+  __TEXT.__text: 0x2c97c
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x3614
-  __TEXT.__oslogstring: 0x3b17
-  __TEXT.__unwind_info: 0x5d8
+  __TEXT.__const: 0x290
+  __TEXT.__cstring: 0x39b8
+  __TEXT.__oslogstring: 0x4517
+  __TEXT.__unwind_info: 0x688
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x1a48
+  __DATA_CONST.__const: 0x1bd8
   __AUTH_CONST.__auth_got: 0x5b0
-  __AUTH_CONST.__const: 0x1e0
-  __AUTH.__data: 0x328
-  __DATA.__data: 0x30
-  __DATA.__bss: 0x390
+  __AUTH_CONST.__const: 0x220
+  __AUTH.__data: 0x3e0
+  __DATA.__data: 0x48
+  __DATA.__bss: 0x448
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x198
+  __DATA_DIRTY.__bss: 0x1a0
   - /usr/lib/system/libcopyfile.dylib
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: FBD2151D-2082-3548-BCBC-51612495072D
-  Functions: 514
-  Symbols:   1146
-  CStrings:  786
+  UUID: DE4D7C26-6ADF-3DFA-9652-A6AA59AC79AD
+  Functions: 570
+  Symbols:   1261
+  CStrings:  864
 
Symbols:
+ _CMDISPATCHSEAM_DEFAULT
+ _CMNOTIFYSEAM_DEFAULT
+ _CMSANDBOXSEAM_DEFAULT
+ _CONTAINER_CLASS_NAMES
+ _CONTAINER_NOTIFY_GENERATION_INITIAL
+ _CONTAINER_NOTIFY_GENERATION_INVALID
+ _CONTAINER_NOTIFY_QUEUE_LABEL
+ __CONTAINER_NOTIFY_EVENT_NAMES
+ ____container_notify_begin_block_invoke
+ ____container_notify_begin_block_invoke_2
+ ____container_query_get_next_result_sync_block_invoke
+ ____container_query_get_result_at_index_block_invoke
+ ____container_xpc_process_warnings_in_reply_block_invoke
+ ___block_descriptor_tmp.1.319
+ ___block_descriptor_tmp.1.398
+ ___block_descriptor_tmp.1.462
+ ___block_descriptor_tmp.1.704
+ ___block_descriptor_tmp.1.736
+ ___block_descriptor_tmp.1.943
+ ___block_descriptor_tmp.1.983
+ ___block_descriptor_tmp.10.1037
+ ___block_descriptor_tmp.10.877
+ ___block_descriptor_tmp.1006
+ ___block_descriptor_tmp.11.1038
+ ___block_descriptor_tmp.12.1039
+ ___block_descriptor_tmp.12.870
+ ___block_descriptor_tmp.13.1044
+ ___block_descriptor_tmp.13.463
+ ___block_descriptor_tmp.162
+ ___block_descriptor_tmp.166
+ ___block_descriptor_tmp.17.1048
+ ___block_descriptor_tmp.17.933
+ ___block_descriptor_tmp.191
+ ___block_descriptor_tmp.2.400
+ ___block_descriptor_tmp.2.706
+ ___block_descriptor_tmp.2.741
+ ___block_descriptor_tmp.2.869
+ ___block_descriptor_tmp.2.947
+ ___block_descriptor_tmp.26.1057
+ ___block_descriptor_tmp.28.1060
+ ___block_descriptor_tmp.3.403
+ ___block_descriptor_tmp.3.455
+ ___block_descriptor_tmp.3.707
+ ___block_descriptor_tmp.3.742
+ ___block_descriptor_tmp.3.762
+ ___block_descriptor_tmp.3.879
+ ___block_descriptor_tmp.30.624
+ ___block_descriptor_tmp.317
+ ___block_descriptor_tmp.34.1064
+ ___block_descriptor_tmp.34.625
+ ___block_descriptor_tmp.36.1066
+ ___block_descriptor_tmp.37.1068
+ ___block_descriptor_tmp.387
+ ___block_descriptor_tmp.393
+ ___block_descriptor_tmp.4.1010
+ ___block_descriptor_tmp.4.405
+ ___block_descriptor_tmp.4.882
+ ___block_descriptor_tmp.4.992
+ ___block_descriptor_tmp.441
+ ___block_descriptor_tmp.5.1008
+ ___block_descriptor_tmp.5.428
+ ___block_descriptor_tmp.5.708
+ ___block_descriptor_tmp.5.885
+ ___block_descriptor_tmp.543
+ ___block_descriptor_tmp.552
+ ___block_descriptor_tmp.560
+ ___block_descriptor_tmp.6.1019
+ ___block_descriptor_tmp.6.430
+ ___block_descriptor_tmp.6.710
+ ___block_descriptor_tmp.669
+ ___block_descriptor_tmp.7.1033
+ ___block_descriptor_tmp.7.705
+ ___block_descriptor_tmp.7.764
+ ___block_descriptor_tmp.730
+ ___block_descriptor_tmp.758
+ ___block_descriptor_tmp.8.1036
+ ___block_descriptor_tmp.8.450
+ ___block_descriptor_tmp.8.711
+ ___block_descriptor_tmp.81.1094
+ ___block_descriptor_tmp.858
+ ___block_descriptor_tmp.9.1034
+ ___block_descriptor_tmp.9.765
+ ___block_descriptor_tmp.900
+ ___block_descriptor_tmp.921
+ ___block_descriptor_tmp.954
+ ___block_descriptor_tmp.978
+ ___block_literal_global.10.448
+ ___block_literal_global.1098
+ ___block_literal_global.15
+ ___block_literal_global.32
+ ___block_literal_global.36
+ ___block_literal_global.376
+ ___block_literal_global.453
+ ___block_literal_global.541
+ ___block_literal_global.550
+ ___block_literal_global.558
+ ___block_literal_global.753
+ ___block_literal_global.883
+ ___container_notify_free_block_invoke
+ ___container_notify_free_block_invoke_2
+ ___container_notify_has_changed_block_invoke
+ ___container_notify_start_block_invoke
+ ___container_notify_stop_block_invoke
+ __container_authorize_execute
+ __container_notify_copy_notify_name
+ __container_notify_end
+ __container_notify_generation_register
+ __container_notify_is_valid
+ __container_notify_log_if_error
+ __container_notify_populate_generation
+ __container_notify_set_generation
+ __container_notify_set_usage_error
+ __container_query_free_results
+ __container_query_get_next_result_sync
+ __container_query_get_result_at_index
+ __container_query_needs_to_be_executed
+ __container_query_operation_set_private_flags
+ __container_query_reset_iterator
+ _container_authorize
+ _container_authorize_container
+ _container_authorize_container_for_self
+ _container_authorize_get_result_description
+ _container_error_create_with_message
+ _container_error_get_message
+ _container_notify_create
+ _container_notify_create_with_class
+ _container_notify_create_with_initial_gen_count
+ _container_notify_free
+ _container_notify_get_generation
+ _container_notify_get_last_error
+ _container_notify_has_changed
+ _container_notify_increment_generation
+ _container_notify_post
+ _container_notify_set_class
+ _container_notify_set_event_handler
+ _container_notify_set_flags
+ _container_notify_set_generation
+ _container_notify_set_queue
+ _container_notify_set_uid
+ _container_notify_start
+ _container_notify_stop
+ _container_paths_copy_part_subpath
+ _container_query_operation_set_part
+ _container_query_operation_set_part_domain
+ _container_seam_dispatch_reset
+ _container_seam_dispatch_set_common
+ _container_seam_notify_reset
+ _container_seam_notify_set_common
+ _container_seam_sandbox_reset
+ _container_seam_sandbox_set_common
+ _dispatch_assert_queue_not$V2
+ _dispatch_barrier_sync
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_release
+ _dispatch_retain
+ _gCMDispatchCustomSeamStore
+ _gCMDispatchSeam
+ _gCMNotifyCustomSeamStore
+ _gCMNotifySeam
+ _gCMSandboxCustomSeamStore
+ _gCMSandboxSeam
+ _notify_cancel
+ _notify_check
+ _notify_get_state
+ _notify_post
+ _notify_register_check
+ _notify_set_state
+ _os_retain
+ _sandbox_check_protected_app_container
+ _sandbox_container_path_for_audit_token
+ _sandbox_register_app_container
+ _sandbox_set_container_path_for_audit_token
- __CONTAINER_NAMES
- ___block_descriptor_tmp.1.274
- ___block_descriptor_tmp.1.339
- ___block_descriptor_tmp.1.397
- ___block_descriptor_tmp.1.623
- ___block_descriptor_tmp.1.653
- ___block_descriptor_tmp.1.811
- ___block_descriptor_tmp.1.849
- ___block_descriptor_tmp.10.903
- ___block_descriptor_tmp.11.697
- ___block_descriptor_tmp.11.904
- ___block_descriptor_tmp.12.905
- ___block_descriptor_tmp.13.910
- ___block_descriptor_tmp.156
- ___block_descriptor_tmp.160
- ___block_descriptor_tmp.17.914
- ___block_descriptor_tmp.185
- ___block_descriptor_tmp.2.341
- ___block_descriptor_tmp.2.625
- ___block_descriptor_tmp.2.658
- ___block_descriptor_tmp.2.815
- ___block_descriptor_tmp.26.923
- ___block_descriptor_tmp.272
- ___block_descriptor_tmp.28.926
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.3.344
- ___block_descriptor_tmp.3.390
- ___block_descriptor_tmp.3.626
- ___block_descriptor_tmp.3.659
- ___block_descriptor_tmp.3.693
- ___block_descriptor_tmp.328
- ___block_descriptor_tmp.33
- ___block_descriptor_tmp.334
- ___block_descriptor_tmp.34.930
- ___block_descriptor_tmp.36.932
- ___block_descriptor_tmp.37.934
- ___block_descriptor_tmp.382
- ___block_descriptor_tmp.4.346
- ___block_descriptor_tmp.4.627
- ___block_descriptor_tmp.4.858
- ___block_descriptor_tmp.4.876
- ___block_descriptor_tmp.477
- ___block_descriptor_tmp.486
- ___block_descriptor_tmp.494
- ___block_descriptor_tmp.5.369
- ___block_descriptor_tmp.5.874
- ___block_descriptor_tmp.591
- ___block_descriptor_tmp.6.371
- ___block_descriptor_tmp.6.628
- ___block_descriptor_tmp.6.885
- ___block_descriptor_tmp.647
- ___block_descriptor_tmp.689
- ___block_descriptor_tmp.7.398
- ___block_descriptor_tmp.7.630
- ___block_descriptor_tmp.7.695
- ___block_descriptor_tmp.7.899
- ___block_descriptor_tmp.74.958
- ___block_descriptor_tmp.769
- ___block_descriptor_tmp.790
- ___block_descriptor_tmp.8.902
- ___block_descriptor_tmp.820
- ___block_descriptor_tmp.844
- ___block_descriptor_tmp.872
- ___block_descriptor_tmp.9.696
- ___block_descriptor_tmp.9.900
- ___block_literal_global.31
- ___block_literal_global.317
- ___block_literal_global.35
- ___block_literal_global.388
- ___block_literal_global.475
- ___block_literal_global.484
- ___block_literal_global.492
- ___block_literal_global.684
- ___block_literal_global.9
- ___block_literal_global.964
- ___container_query_get_single_result_block_invoke
CStrings:
+ "%llu→(%llu) %s at path [%s] with errno (%d) %s; %s"
+ "%llu→(%llu) %s; %s"
+ "%s/%s.plist"
+ "%s: SPI MISUSE: A query must not contain a persona for container_authorize*"
+ "%s: SPI MISUSE: Attempt to free container_error_extended_t that is owned by a container_notify_t. Ignoring."
+ "%s: SPI MISUSE: Cannot use CONTAINER_PATHS_PREFIX_TYPE_DATA_VOLUME_MOUNT_POINT with edu mode user %u"
+ "%s: SPI MISUSE: container class is not set or is invalid (%llu)"
+ "%s: SPI MISUSE: container_class parameter is an invalid value (%llu > %llu < %llu)"
+ "%s: SPI MISUSE: domain parameter is NULL"
+ "%s: SPI MISUSE: event parameter is invalid (%llu/%llu)"
+ "%s: SPI MISUSE: generation parameter is invalid"
+ "%s: SPI MISUSE: invalid container part: %llu"
+ "%s: SPI MISUSE: notify parameter is NULL"
+ "%s: SPI MISUSE: notify parameters cannot be changed after container_notify_start() or container_notify_has_changed()"
+ "%s: SPI MISUSE: out_generation parameter is NULL"
+ "(%04u:0x%08llx:0x%08llx:0x%04lx:%02d:%04u:%04u:%04u:O%06o:%03d:%s%s%s:%s:%03d)[%s][%s]"
+ "@(#)VERSION:Container Manager: May 23 2025 00:54:10; MobileContainerManager_system-725.0.3.0.1~32/arm64e"
+ "ATTEMPT_TO_MUTATE_AFTER_EXEC"
+ "C."
+ "Calling out to client; token = %d, event = %llu, container_class = %llu"
+ "Canceled registered event; token = %d, container_class = %llu"
+ "Checked generation event; token = %d, container_class = %llu, check = %d"
+ "Container delete; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, manifest = %{private}s"
+ "Could not append element [%s] of length %zu to path [%s] because it would make the path longer than MAXPATHLEN"
+ "D."
+ "ERROR"
+ "Enumerate; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, context<path = [%s], class = %llu, flags = 0x%llx, persona = [%{public}s], uid = %u, transient = %d>"
+ "ErrorMessage"
+ "Failed to check generation state; container_class = %llu, status = %u"
+ "Failed to get container root path."
+ "Failed to get generation state; container_class = %llu, status = %u"
+ "Failed to post generation change; class = %llu, generation = %llu"
+ "Failed to post generation changed event; container_class = %llu, generation = %llu, status = %u"
+ "Failed to post notification; class = %llu, event = %llu, name = [%s]"
+ "Failed to register for event; event = [%s], container_class = %llu, status = %u"
+ "Failed to register for generation event; event = [%s], container_class = %llu, status = %u"
+ "Failed to register one or more event handlers; container_class = %llu, expected = %zu, registered = %zu"
+ "Failed to set generation state; container_class = %llu, generation = %llu, status = %u"
+ "G."
+ "Got generation state; token = %d, container_class = %llu, generation = %llu"
+ "INVALID_SANDBOX_EXTENSION_TYPE"
+ "NO"
+ "NOTIFY_GET_STATE_FAILED"
+ "NOTIFY_REGISTER_FAILED"
+ "NO_PATH_ONLY"
+ "No event handlers assigned; container_class = %llu"
+ "Notify check failed, assuming that there are changes. THIS CAUSES A PERFORMANCE PENALTY."
+ "OnBehalfOfSelf"
+ "P."
+ "PART_SUBDIR_CREATION_FAILED"
+ "Part"
+ "Posted event; event = %llu, event_name = [%s], container_class = %llu"
+ "Posted generation change event; event_name = [%s], container_class = %llu"
+ "Query; euid = %u, uid = %u, class = %llu, identifier = [%s](%zu), flags = %llx"
+ "Query; euid = %u, uid = %u, query = %s"
+ "Query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu, identifier = [%s](%zu), flags = %llx"
+ "Query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, query = %s"
+ "References query; euid = %u, uid = %u, query = %s"
+ "References query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, query = %s"
+ "Registered for event; token = %d, event = %llu, name = [%s], container_class = %llu"
+ "Registered for generation check; event = [%s], container_class = %llu"
+ "Replacing existing notify handler; class = %llu, event = %llu"
+ "Replacing existing notify queue; class = %llu"
+ "ReplyAuthorized"
+ "ReplyGeneration"
+ "ReplyWarnings"
+ "Requesting app group container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], identifier = %{private}s, euid = %u, uid = %u, platform = %u"
+ "Requesting container lookup; class = %llu, identifier = %{private}s, group_identifier = %{private}s, create = %d, temp = %d, euid = %u, uid = %u"
+ "Requesting container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], bundle = [%{public}s], root = [%{public}s], executable = [%{public}s], flags = %llu, euid = %u, uid = %u"
+ "Requesting container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], class = %llu, identifier = %{private}s, group_identifier = %{private}s, create = %d, temp = %d, euid = %u, uid = %u"
+ "Requesting multiple containers; class = %llu, temp = %d, euid = %u, uid = %u"
+ "Requesting multiple containers; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], class = %llu, temp = %d, euid = %u, uid = %u"
+ "Set state; token = %d, generation = %llu, container_class = %llu"
+ "SystemDataDomain"
+ "Update info; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu, identifier = %s, key = [%s](%zu), flags = %llx"
+ "Update info; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, message = %s"
+ "WARNING"
+ "WARNING: Calling %s with a notify object that has a previous error: %s"
+ "Wait for obliteration; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u"
+ "XPC connection to containermanagerd interrupted. Retry attempt %u of %u"
+ "XPC connection to containermanagerd invalidated. Retry attempt %u of %u"
+ "YES"
+ "_container_authorize_execute"
+ "_container_query_get_next_result_sync"
+ "_container_query_get_result_at_index"
+ "_container_query_operation_set_private_flags"
+ "_container_query_reset_iterator"
+ "com.apple.containermanager.%s%s"
+ "connection <%p/%llu/%llu; %p> canceled after timeout; cnt = %lld"
+ "connection <%p/%llu/%llu; %p> invalidated"
+ "connection <%p/%llu/%llu> created; cnt = %lld"
+ "connection <%p/%llu/%llu> freed; cnt = %lld"
+ "connection <%p/%llu/%llu> released (shared; canceler); cnt = %lld"
+ "connection <%p/%llu/%llu> released (shared; handler); cnt = %lld"
+ "connection <%p/%llu/%llu> released; cnt = %lld"
+ "connection <%p/%llu/%llu> shared; cnt = %lld"
+ "connection <%p/%llu/%llu> will be canceled in %lld seconds; cnt = %lld"
+ "container_class parameter is an invalid value (%llu > %llu < %llu)"
+ "container_notify_get_generation"
+ "container_notify_has_changed"
+ "container_notify_increment_generation"
+ "container_notify_post"
+ "container_notify_set_class"
+ "container_notify_set_event_handler"
+ "container_notify_set_flags"
+ "container_notify_set_generation"
+ "container_notify_set_queue"
+ "container_notify_set_uid"
+ "container_notify_start"
+ "container_notify_t"
+ "container_query_operation_set_part"
+ "container_query_operation_set_part_domain"
+ "containermanagerd state reset, retry requested. Retry attempt %u of %u"
+ "failed to generate connection for sharing of type %llu, purpose %llu: %llu"
+ "getpwuid_r(%{public}u) returned %{public, darwin.errno}d"
+ "getpwuid_r(%{public}u): user not found"
+ "notify"
+ "v20@?0C8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}12"
+ "v28@?0^v8i16^{container_error_extended_s=QQ*i*^{container_query_s}^{container_references_s}^{container_notify_s}}20"
+ "v48@?0I8Q12^v20I28Q32@?<v@?^vi^{container_error_extended_s=QQ*i*^{container_query_s}^{container_references_s}^{container_notify_s}}>40"
- "%llu→(%llu) %s"
- "%llu→(%llu) %s at path [%s] with errno (%d) %s"
- "%s: SPI MISUSE: Cannot use CONTAINER_PATHS_PREFIX_TYPE_DATA_VOLUME_MOUNT_POINT with edu mode user %d"
- "(%04d:0x%08llx:0x%08llx:0x%04lx:%02d:%04d:%04d:%04d:O%06o:%03d:%s%s%s:%s:%03d)[%s][%s]"
- "@(#)VERSION:Container Manager: Apr 18 2025 23:31:34; MobileContainerManager_system-689.100.6~486/arm64e"
- "Container delete; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], euid = %d, uid = %d, manifest = %{private}s"
- "Could not append element [%s] of length %zd to path [%s] because it would make the path longer than MAXPATHLEN"
- "Enumerate; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], euid = %d, uid = %d, context<path = [%s], class = %llu, flags = 0x%llx, persona = [%{public}s], uid = %d, transient = %d>"
- "Query; euid = %d, uid = %d, class = %llu, identifier = [%s](%zd), flags = %llx"
- "Query; euid = %d, uid = %d, query = %s"
- "Query; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], euid = %d, uid = %d, class = %llu, identifier = [%s](%zd), flags = %llx"
- "Query; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], euid = %d, uid = %d, query = %s"
- "References query; euid = %d, uid = %d, query = %s"
- "References query; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], euid = %d, uid = %d, query = %s"
- "Requesting app group container lookup; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], identifier = %{private}s, euid = %d, uid = %d, platform = %d"
- "Requesting container lookup; class = %llu, identifier = %{private}s, group_identifier = %{private}s, create = %d, temp = %d, euid = %d, uid = %d"
- "Requesting container lookup; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], bundle = [%{public}s], root = [%{public}s], executable = [%{public}s], flags = %llu, euid = %d, uid = %d"
- "Requesting container lookup; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], class = %llu, identifier = %{private}s, group_identifier = %{private}s, create = %d, temp = %d, euid = %d, uid = %d"
- "Requesting multiple containers; class = %llu, temp = %d, euid = %d, uid = %d"
- "Requesting multiple containers; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], class = %llu, temp = %d, euid = %d, uid = %d"
- "Update info; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], euid = %d, uid = %d, class = %llu, identifier = %s, key = [%s](%zd), flags = %llx"
- "Update info; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], euid = %d, uid = %d, message = %s"
- "Wait for obliteration; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], euid = %d, uid = %d"
- "XPC connection to containermanagerd interrupted. Retry attempt %d of %d"
- "XPC connection to containermanagerd invalidated. Retry attempt %d of %d"
- "connection <%p/%lld/%lld; %p> canceled after timeout; cnt = %lld"
- "connection <%p/%lld/%lld; %p> invalidated"
- "connection <%p/%lld/%lld> created; cnt = %lld"
- "connection <%p/%lld/%lld> freed; cnt = %lld"
- "connection <%p/%lld/%lld> released (shared; canceler); cnt = %lld"
- "connection <%p/%lld/%lld> released (shared; handler); cnt = %lld"
- "connection <%p/%lld/%lld> released; cnt = %lld"
- "connection <%p/%lld/%lld> shared; cnt = %lld"
- "connection <%p/%lld/%lld> will be canceled in %lld seconds; cnt = %lld"
- "container_query_get_single_result"
- "containermanagerd state reset, retry requested. Retry attempt %d of %d"
- "failed to generate connection for sharing of type %lld, purpose %lld: %lld"
- "getpwuid_r(%u) returned %{public, darwin.errno}d"
- "getpwuid_r(%u): user not found"
- "v20@?0C8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}12"
- "v28@?0^v8i16^{container_error_extended_s=QQ*i^{container_query_s}^{container_references_s}}20"
- "v48@?0I8Q12^v20I28Q32@?<v@?^vi^{container_error_extended_s=QQ*i^{container_query_s}^{container_references_s}}>40"

```
