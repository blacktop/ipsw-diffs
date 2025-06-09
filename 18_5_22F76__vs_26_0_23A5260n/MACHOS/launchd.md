## launchd

> `/sbin/launchd`

```diff

-2894.122.1.0.0
-  __TEXT.__text: 0x51ab0
-  __TEXT.__auth_stubs: 0x2120
+3070.0.0.0.2
+  __TEXT.__text: 0x54218
+  __TEXT.__auth_stubs: 0x21f0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x2e0
-  __TEXT.__cstring: 0x1505b
+  __TEXT.__objc_methlist: 0x20c
+  __TEXT.__const: 0x350
+  __TEXT.__cstring: 0x158c9
   __TEXT.__launchd: 0x1
   __TEXT.__objc_methname: 0x8
-  __TEXT.__objc_classname: 0x1ba
+  __TEXT.__objc_classname: 0x1d5
   __TEXT.__objc_methtype: 0x8
-  __TEXT.__config: 0x2544
+  __TEXT.__config: 0x296b
   __TEXT.__dof_launchd: 0x67c
-  __TEXT.__unwind_info: 0x11d0
-  __DATA_CONST.__auth_got: 0x1090
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x5340
-  __DATA_CONST.__objc_classlist: 0xa8
+  __TEXT.__unwind_info: 0x1270
+  __DATA_CONST.__auth_got: 0x10f8
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0x5658
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA.__objc_const: 0xbd0
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA.__objc_const: 0xc60
   __DATA.__objc_selrefs: 0x8
-  __DATA.__objc_data: 0x690
-  __DATA.__data: 0x8d8
+  __DATA.__objc_data: 0x6e0
+  __DATA.__data: 0x948
   __DATA.__os_assumes_log: 0x8
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xe78
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0xea1
   __DATA.__common: 0x804
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: FEBB544E-F4DA-3F20-BE33-F8C3B3206218
-  Functions: 1644
-  Symbols:   583
-  CStrings:  2632
+  UUID: 1DF26BE9-A01B-3D53-825F-DDFBE3D3477A
+  Functions: 1712
+  Symbols:   598
+  CStrings:  2706
 
Symbols:
+ __xpc_type_error
+ __xpc_type_mach_send_once
+ _dispatch_mig_server
+ _dispatch_source_set_cancel_handler_f
+ _getattrlist
+ _host_get_io_main
+ _if_nametoindex
+ _mach_port_allocate
+ _mach_port_get_refs
+ _mig_reply_setup
+ _posix_spawnattr_set_conclavememlimit_ext
+ _time
+ _xpc_bundle_create_from_origin_with_string_cache
+ _xpc_bundle_create_with_string_cache
+ _xpc_create_from_plist_with_string_cache
+ _xpc_mach_send_once_extract_right
+ _xpc_pipe_create_reply_from_port
+ _xpc_string_cache_create
- _arc4random_uniform
- _xpc_bundle_create
- _xpc_bundle_create_from_origin
CStrings:
+ "\"%s\" =>"
+ "\"%s\" exited with exit code = %d"
+ "\"%s\" exited with signal = %s"
+ "%hd"
+ "%s coalition = {"
+ "%s coalition ID = %llu"
+ "%s is less than zero. Ignoring."
+ "--recovery-reason"
+ "/System/Library/CoreServices/SystemVersionCompat.plist"
+ "/usr/libexec/devicerecoverytool"
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat May 24 04:24:41 PDT 2025; root:libxpc_executables-3070.0.0.0.2~30/launchd/RELEASE_ARM64E"
+ "AppNonUI"
+ "AppleKeyStore"
+ "B16@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}^{_launch_attribution_node_s}ICIIC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8"
+ "BoundInterface"
+ "ConclaveMemoryLimit"
+ "Could not convert value for OSLogClientType to str: %lld"
+ "Could not convert value for OSLogRateLimit to str: %lld"
+ "Could not get interface index (name = %s, idx = %lu)"
+ "Darwin Bootstrapper Version 7.0.0: Sat May 24 04:24:41 PDT 2025; root:libxpc_executables-3070.0.0.0.2~30/launchd/RELEASE_ARM64E"
+ "Device recovery"
+ "EX Extension Info.plist missing EXExtensionPointIdentifier"
+ "ElideRoleAccountSetupPathPrefixes"
+ "Failed to set hw.mempath"
+ "Feature disabled, device would have rebooted due to %s"
+ "Flushing logs before initialization. Early logs may not be written to file."
+ "Got first unlock unregistering for AKS events"
+ "ID = %llu"
+ "IOGeneralInterest"
+ "Improper type for _RecoverOnCrash key: %s"
+ "JETSAM_REASON_MEMORY_CONCLAVELIMIT"
+ "JETSAM_REASON_MEMORY_VMCOMPRESSOR_SPACE_SHORTAGE"
+ "Large"
+ "Medium"
+ "MobileAssetEarlyBootTask"
+ "NS Extension Info.plist missing NSExtensionPointIdentifier"
+ "NoExcResourceDuringAudio"
+ "OSLogClientType"
+ "OSLogRTBufferConfig"
+ "OSLogRateLimit"
+ "OS_launch_attribution_node"
+ "PerformAfterUserspaceRebootOnly"
+ "Queried %zu attributed services: caller=%s[%d], coalition=%llu"
+ "Queried %zu attributed services: caller=%s[%d], service=%s"
+ "Rebooting to device recovery environment"
+ "RecoverOnCrash"
+ "RecoverOnCrashCount"
+ "RecoverOnCrashDeadline"
+ "Small"
+ "SupplementalJetsamProperties"
+ "SupplementalPaths"
+ "SupplementalUserPaths"
+ "Unsupported value for OSLogRTBufferConfig: %s"
+ "[%zu] => \"%s\""
+ "_RecoverOnCrash"
+ "_RecoverOnCrash key: RecoverOnCrashCount invalid value. Ignoring."
+ "_RecoverOnCrash key: RecoverOnCrashDeadline invalid. Ignoring."
+ "_RecoverOnCrash key: RecoverOnCrashDeadline overflowed converting to ns (%lld)"
+ "__XPC_"
+ "active"
+ "active count = %llu"
+ "app (nonui)"
+ "archpref"
+ "bound interface = %s"
+ "bundle ID = %s"
+ "can not find service for caller pid %d"
+ "client-reply-port"
+ "coalition-id"
+ "com.apple.private.xpc.launchd.allowed-coalition-quiesce"
+ "com.apple.private.xpc.launchd.job-manager-remove-any"
+ "com.apple.xpc.launchd.plist_key_xsc"
+ "critical process crashes: %s"
+ "device recovery on crashes (%zd)"
+ "device-recovery"
+ "devicerecoverytool"
+ "dirs_cleaner-usr"
+ "failed to add interest notification"
+ "failed to create notification port for AKS"
+ "failed to find %s service"
+ "hw.jetsam_properties_product_type"
+ "hw.mempath"
+ "initiated at %ld by %s"
+ "invalid client reply port %d"
+ "jetsam"
+ "jetsam conclave memory limit = %u"
+ "job not found, returning ENOSERVICE to %d with manual pipe reply"
+ "kern.osproductversioncompat"
+ "kern.userspacerebootpurpose"
+ "kern.userspacereboottime"
+ "kernel"
+ "missing token in request from pid %d"
+ "name = %s"
+ "no EXC_RESOURCE during audio"
+ "no client port found"
+ "no elide roleaccount setup path prefixes"
+ "no requestor found for token %llu"
+ "persistent resource coalition = %s"
+ "reaped"
+ "rebooting due to %s"
+ "resource"
+ "returning username for get_uid_for_token: %s"
+ "service-ctl-reply-port"
+ "spawn of %s failed: %s"
+ "sysctl hw.jetsam_properties_product_type was not set"
+ "terminated"
+ "unknown"
+ "v16@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}^{_launch_attribution_node_s}ICIIC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8"
+ "v20@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}^{_launch_attribution_node_s}ICIIC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8i16"
+ "v24@?0r*8^{_launch_service_stats_s=^{?}IIII*[0{_launch_service_stats_record_s=^{?}QQiICQIIISIi}]}16"
+ "v28@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}^{_launch_attribution_node_s}ICIIC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8B16^{_launch_lint_s=@?*B}20"
+ "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}^{_launch_attribution_node_s}ICIIC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8*16^{_launch_lint_s=@?*B}24"
+ "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}^{_launch_attribution_node_s}ICIIC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8^v16^{_launch_lint_s=@?*B}24"
+ "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}^{_launch_attribution_node_s}ICIIC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8q16^{_launch_lint_s=@?*B}24"
- "\"%s\" => \"%s\""
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Tue Apr 22 20:33:03 PDT 2025; root:libxpc_executables-2894.122.1~1/launchd/RELEASE_ARM64E"
- "ActivationRate"
- "Active user switch initiated by: %s[%d]"
- "App Extension Info.plist is missing EXExtentionPointIdentifier"
- "App Extension Info.plist is missing NSExtentionPointIdentifier"
- "B16@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8"
- "Darwin Bootstrapper Version 7.0.0: Tue Apr 22 20:33:03 PDT 2025; root:libxpc_executables-2894.122.1~1/launchd/RELEASE_ARM64E"
- "Enabling Probabilistic Guard Malloc"
- "GlobalPolicy"
- "MallocProbGuard"
- "MallocProbGuardSampleRate"
- "MallocProbGuardViaLaunchd"
- "ProbGuardPolicy"
- "Probabilistic Guard Malloc ActivationRate has the wrong format"
- "Probabilistic Guard Malloc SampleRate has the wrong format"
- "Probabilistic Guard Malloc config absent"
- "Probabilistic Guard Malloc configuration file plist is not a dictionary"
- "Probabilistic Guard Malloc-enabled process exited"
- "Running with Probabilistic Guard Malloc envvar (Sample Rate = %zu)"
- "SampleRate"
- "activation rate = 1/%u"
- "app (throttled)"
- "hw.targettype"
- "launch_prob_guard_sample_rate_self="
- "launch_prob_guard_self="
- "prob guard = true"
- "prob guard sample rate = %zu"
- "probabilistic guard malloc policy = {"
- "sample rate = 1/%u"
- "sysctl hw.targettype was not set"
- "usermanagerd-switch"
- "v20@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8i16"
- "v24@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8^v16"
- "v24@?0r*8^{_launch_service_stats_s=^{?}IIII*[0{_launch_service_stats_record_s=^{?}QQiICQIIIS}]}16"
- "v28@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8B16^{_launch_lint_s=@?*B}20"
- "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8*16^{_launch_lint_s=@?*B}24"
- "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8^v16^{_launch_lint_s=@?*B}24"
- "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8q16^{_launch_lint_s=@?*B}24"

```
