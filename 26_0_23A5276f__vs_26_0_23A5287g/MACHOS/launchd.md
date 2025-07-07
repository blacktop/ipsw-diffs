## launchd

> `/sbin/launchd`

```diff

-3088.0.0.0.0
-  __TEXT.__text: 0x542d8
-  __TEXT.__auth_stubs: 0x21f0
+3089.0.3.502.1
+  __TEXT.__text: 0x53ee0
+  __TEXT.__auth_stubs: 0x21e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20c
-  __TEXT.__const: 0x340
-  __TEXT.__cstring: 0x157ea
+  __TEXT.__const: 0x350
+  __TEXT.__cstring: 0x14ff8
   __TEXT.__launchd: 0x1
   __TEXT.__objc_methname: 0x8
   __TEXT.__objc_classname: 0x1d5

   __TEXT.__config: 0x296b
   __TEXT.__dof_launchd: 0x67c
   __TEXT.__unwind_info: 0x1270
-  __DATA_CONST.__auth_got: 0x10f8
+  __DATA_CONST.__auth_got: 0x10f0
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x55c8
+  __DATA_CONST.__const: 0x55a0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0

   __DATA.__data: 0x948
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xea1
+  __DATA.__bss: 0xe99
   __DATA.__common: 0x804
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 5903B1CC-6D97-302B-A7BB-CF6D3C79833C
-  Functions: 1714
-  Symbols:   598
-  CStrings:  2700
+  UUID: C74AC86E-70B3-339D-AA45-8272F961544C
+  Functions: 1709
+  Symbols:   597
+  CStrings:  2692
 
Symbols:
- _proc_track_dirty
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Tue Jul  1 21:17:26 PDT 2025; root:libxpc_executables-3089.0.3.502.1~1/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Tue Jul  1 21:17:26 PDT 2025; root:libxpc_executables-3089.0.3.502.1~1/launchd/RELEASE_ARM64E"
- "/System/Library/CoreServices/SystemVersionCompat.plist"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Fri Jun 13 07:15:26 PDT 2025; root:libxpc_executables-3088~40/launchd/RELEASE_ARM64E"
- "B16@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}^{_launch_attribution_node_s}ICIIC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8"
- "Darwin Bootstrapper Version 7.0.0: Fri Jun 13 07:15:26 PDT 2025; root:libxpc_executables-3088~40/launchd/RELEASE_ARM64E"
- "Finding services to set shutdown-on-clean"
- "Running with outdated trial config: %s: curr=\"%s\", new=\"%s\""
- "Set shutdown-on-clean on %zu/%zu running services"
- "Set shutdown-on-clean: service=%s, flags=0x%x, error=%d"
- "kern.osproductversioncompat"
- "trial shutdown-on-clean count = %zu"

```
