## launchd

> `/sbin/launchd`

```diff

-2894.140.11.0.0
-  __TEXT.__text: 0x51a94
-  __TEXT.__auth_stubs: 0x2120
+2894.140.11.0.1
+  __TEXT.__text: 0x5168c
+  __TEXT.__auth_stubs: 0x2110
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x14f6a
+  __TEXT.__cstring: 0x147d9
   __TEXT.__launchd: 0x1
   __TEXT.__objc_methname: 0x8
   __TEXT.__objc_classname: 0x1ba

   __TEXT.__config: 0x2544
   __TEXT.__dof_launchd: 0x67c
   __TEXT.__unwind_info: 0x11d0
-  __DATA_CONST.__auth_got: 0x1090
+  __DATA_CONST.__auth_got: 0x1088
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x52b0
+  __DATA_CONST.__const: 0x5288
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa8

   __DATA.__data: 0x8d8
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xe78
+  __DATA.__bss: 0xe70
   __DATA.__common: 0x804
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 67D87F5C-C555-31F0-8542-4CC18096ED84
-  Functions: 1644
-  Symbols:   583
-  CStrings:  2624
+  UUID: 31EF5B99-264A-369E-AD28-9DAD099EE690
+  Functions: 1639
+  Symbols:   582
+  CStrings:  2618
 
Symbols:
- _proc_track_dirty
Functions (added):
+ sub_100011d90
+ sub_100011df4
+ sub_100012098

Functions (removed):
- sub_10004c66c
- sub_100050dcc
- sub_100051158
- sub_1000511f0
- sub_10005131c
- sub_100051818
- sub_100051988
- sub_100052674
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sun Jul  6 18:43:26 PDT 2025; root:libxpc_executables-2894.140.11.0.1~18/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Sun Jul  6 18:43:26 PDT 2025; root:libxpc_executables-2894.140.11.0.1~18/launchd/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sun Jun 22 21:55:04 PDT 2025; root:libxpc_executables-2894.140.11~34/launchd/RELEASE_ARM64E"
- "B16@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8"
- "Darwin Bootstrapper Version 7.0.0: Sun Jun 22 21:55:04 PDT 2025; root:libxpc_executables-2894.140.11~34/launchd/RELEASE_ARM64E"
- "Finding services to set shutdown-on-clean"
- "Running with outdated trial config: %s: curr=\"%s\", new=\"%s\""
- "Set shutdown-on-clean on %zu/%zu running services"
- "Set shutdown-on-clean: service=%s, flags=0x%x, error=%d"
- "trial shutdown-on-clean count = %zu"

```
