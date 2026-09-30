## xpcproxy

> `/usr/libexec/xpcproxy`

```diff

-2894.122.1.0.0
-  __TEXT.__text: 0x448c
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xd28
+3070.0.0.0.2
+  __TEXT.__text: 0x62dc
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0xd2e
+  __TEXT.__oslogstring: 0x15a5
   __TEXT.__xpcproxy: 0x1
   __TEXT.__dof_launchd: 0x2e5
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__auth_got: 0x578
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0x148
+  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x1c8
   __DATA.__os_assumes_log: 0x8
   __DATA.__data: 0x20
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0x99
   - /usr/lib/libCoreEntitlements.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcryptex_trampoline.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: AC0FB510-8179-3F06-929E-836B409CE368
-  Functions: 74
-  Symbols:   194
-  CStrings:  146
+  UUID: 13D06294-7C58-31C3-85A0-713B5ABF77E2
+  Functions: 123
+  Symbols:   198
+  CStrings:  200
 
Symbols:
+ __os_crash_msg
+ __os_log_default
+ __os_log_send_and_compose_impl
+ _os_log_type_enabled
+ _posix_spawnattr_set_conclavememlimit_ext
- __os_assert_log
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat May 24 04:25:35 PDT 2025; root:libxpc_executables-3070.0.0.0.2~30/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Sat May 24 04:25:35 PDT 2025; root:libxpc_executables-3070.0.0.0.2~30/xpcproxy/RELEASE_ARM64E"
+ "assertion failure: \"(*__error())\" -> %llu"
+ "assertion failure: \"amfi_launch_constraint_set_spawnattr(&ctx->psattr, ctx->spawn_constraint, ctx->spawn_constraint_sz)\" -> %llu"
+ "assertion failure: \"error\" -> %llu"
+ "assertion failure: \"launch_spawnctx_update_spawn_constraint(&ctx, attr, xtra, ((void*)0), 0)\" -> %llu"
+ "assertion failure: \"nbytes\" -> %{errno}d"
+ "assertion failure: \"posix_spawn_file_actions_add_fileportdup2_np( &ctx->filact, _xpc_fd_get_port(xfd), dest)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, 0)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, 1)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, 2)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 0, \"/dev/null\", 0x0000|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 0, stdin_path, 0x00000200|0x0000|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 1, \"/dev/null\", 0x0002|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 1, stdout_path, 0x00000200|0x0002|0x00000008|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 2, \"/dev/null\", 0x0002|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 2, stderr_path, 0x00000200|0x0002|0x00000008|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_init(&ctx->filact)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_init(&filact)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_disable_ptr_auth_a_keys_np(&ctx->psattr, 0)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_getflags(&ctx->psattr, &psflags)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_init(&ctx->psattr)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_init(&psattr)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_conclavememlimit_ext(&ctx->psattr, attr->ps_jetsam_conclave_memlimit)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_crash_behavior_deadline_np(&ctx->psattr, attr->ps_crash_behavior_deadline, 0)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_crash_behavior_np(&ctx->psattr, attr->ps_crash_behavior)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_crash_count_np(&ctx->psattr, attr->ps_crash_count, attr->ps_throttling_timeout)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_darwin_role_np(&ctx->psattr, attr->ps_role)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_filedesclimit_ext(&ctx->psattr, attr->ps_jetsam_softfiledescriptorlimit, attr->ps_jetsam_hardfiledescriptorlimit)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_kqworklooplimit_ext(&ctx->psattr, attr->ps_jetsam_softkqworklooplimit, attr->ps_jetsam_hardkqworklooplimit)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_launch_type_np(&ctx->psattr, attr->ps_launch_type)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_max_addr_np(&ctx->psattr, 18446744073709551615ULL)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_max_addr_np(&ctx->psattr, attr->ps_jetsam_addresslimit)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_portlimits_ext(&ctx->psattr, attr->ps_jetsam_softportlimit, attr->ps_jetsam_hardportlimit)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_qos_class_np(&ctx->psattr, attr->ps_qos_class)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_registered_ports_np(&ctx->psattr, stash, 1)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_set_threadlimit_ext(&ctx->psattr, attr->ps_jetsam_threadlimit)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setarchpref_np(psattr, self->xb_count, self->xb_cpu_types, self->xb_cpu_subtypes, ((void*)0))\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setcpumonitor(&ctx->psattr, attr->cpumon_percent, attr->cpumon_interval)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setcpumonitor_default(&ctx->psattr)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setdataless_iopolicy_np(&ctx->psattr, 1)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setdataless_iopolicy_np(&ctx->psattr, 2)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setflags(&ctx->psattr, psflags)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setflags(&psattr, psflags)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setjetsam_ext(&ctx->psattr, (short)attr->ps_jetsam_flags, attr->ps_jetsam_priority, attr->ps_jetsam_memlimit_active, attr->ps_jetsam_memlimit_inactive)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setmacpolicyinfo_np(&ctx->psattr, \"Sandbox\", &ctx->sbattrs, sizeof(ctx->sbattrs))\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setprocesstype_np(&ctx.psattr, 0x00000700)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setspecialport_np(&ctx->psattr, port2use, dst)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setspecialport_np(&psattr, globals->bootstrap_port, 4)\" -> %llu"
+ "assertion failure: \"revoke(\"/dev/console\")\" -> %{errno}d"
+ "assertion failure: \"sandbox_spawnattrs_setcontainer(&ctx->sbattrs, container_id)\" -> %{errno}d"
+ "assertion failure: \"sandbox_spawnattrs_setprofilename(&ctx->sbattrs, profile)\" -> %{errno}d"
+ "assertion failure: \"setenv(\"PATH\", \"/usr/bin:/bin:/usr/sbin:/sbin\", 1)\" -> %{errno}d"
+ "assertion failure: \"setiopolicy_np(0, 0, 3)\" -> %llu"
+ "assertion failure: \"setiopolicy_np(0, 2, 3)\" -> %llu"
+ "assertion failure: \"setsid()\" -> %{errno}d"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Tue Apr 22 20:35:08 PDT 2025; root:libxpc_executables-2894.122.1~1/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Tue Apr 22 20:35:08 PDT 2025; root:libxpc_executables-2894.122.1~1/xpcproxy/RELEASE_ARM64E"

```
