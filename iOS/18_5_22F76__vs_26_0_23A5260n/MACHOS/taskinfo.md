## taskinfo

> `/usr/bin/taskinfo`

```diff

-10733.120.3.0.0
-  __TEXT.__text: 0x55fc
-  __TEXT.__auth_stubs: 0x4d0
+10765.0.0.0.0
+  __TEXT.__text: 0x5d9c
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x28fb
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x58
+  __TEXT.__cstring: 0x2f48
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1d0
-  __DATA.__bss: 0xd0
+  __DATA_CONST.__const: 0x2e0
+  __DATA_CONST.__cfstring: 0x20
+  __DATA.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 57CDE2C1-E9B3-33C6-9BDB-EE3F9F2DA13A
-  Functions: 30
-  Symbols:   92
-  CStrings:  422
+  UUID: E0DEC252-8D53-3ABD-9F5F-35F6DC187A08
+  Functions: 35
+  Symbols:   99
+  CStrings:  512
 
Symbols:
+ _CFStringCreateWithFormat
+ _CFStringGetCStringPtr
+ ___CFConstantStringClassReference
+ _csops
+ _getuid
+ _kCFTypeArrayCallBacks
+ _memorystatus_control
CStrings:
+ "\t\t [--vouchers(=1|0)] [--coalitions=(all|jetsam|resource)]"
+ "\t\tUnknown (%u): %s\n"
+ "\t\treq turnstiles sync promotion qos: %s, user promotion base pri: %u\n"
+ "\tboosted by: %s\n"
+ "\ttaskinfo [process-name|pid] [-h|--help] [--threads] [--dq] [--boosts] [--verbose] [--all]"
+ "\tthread ID: 0x%llx / %llu\n"
+ "  %-5d %-32s"
+ " %7llu %7llu "
+ " %s "
+ " (%s)"
+ " ()"
+ " (coalition names, bundle ids)"
+ " Role   "
+ " adhoc"
+ " check_expiration"
+ " datavault_controller"
+ " debugged"
+ " dev_code"
+ " dyld_platform"
+ " enforcement"
+ " entitlements_validated"
+ " exec_inherit_sip"
+ " exec_set_enforcement"
+ " exec_set_hard"
+ " exec_set_kill"
+ " forced_lv"
+ " get_task_allow"
+ " group 0x%llx (%s%s%s%s%s%s%s%s%s, 0x%u)"
+ " hard"
+ " installer"
+ " invalid_allowed"
+ " kill"
+ " killed"
+ " linker_signed"
+ " nvram_unrestricted"
+ " platform_binary"
+ " platform_path"
+ " require_lv"
+ " restrict"
+ " runtime"
+ " signed"
+ " valid"
+ "%-5d %-34s"
+ "%s [%d]"
+ "%s%s: %u"
+ ")"
+ ", "
+ "Encountered invalid container while generating boost map (id 0x%llx)\n"
+ "Encountered transitioning task snapshot outside of a container while generating boost map\n"
+ "GPU role: %s\n"
+ "NULL"
+ "NonUIApp"
+ "PRIO_DARWIN_GPU_ALLOW"
+ "PRIO_DARWIN_GPU_BACKGROUND"
+ "PRIO_DARWIN_GPU_DENY"
+ "PRIO_DARWIN_GPU_UI"
+ "PRIO_DARWIN_GPU_UI_FOCAL"
+ "PRIO_DARWIN_GPU_UI_NON_FOCAL"
+ "PRIO_DARWIN_GPU_UNKNOWN"
+ "PRIO_DARWIN_GPU_UTILITY"
+ "Resource  Jetsam "
+ "TASK_APPTYPE_APP_NONUI"
+ "TASK_USER_INIT_APPLICATION (PRIO_DARWIN_ROLE_USER_INIT)"
+ "UserInit"
+ "allow-promote-above"
+ "arg --%s only works on TARGET_OS_OSX"
+ "atalk"
+ "boosts: %u (%u externalized)\n"
+ "bridgeos"
+ "channel"
+ "coalition (type %d RESOURCE) ID: %llu"
+ "count:%u exceeds STATIC_PERFLEVEL_COUNT:%d skipping PROC_PIDTHREADCOUNTS data\n"
+ "cs_flags (0x%x):%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\n"
+ "csops_audittoken"
+ "driverkit"
+ "file descriptors: %u ("
+ "fsevents"
+ "getpriority(PRIO_DARWIN_GPU, pid)"
+ "getpriority(PRIO_DARWIN_RUNAWAY_MITIGATION, pid)"
+ "hw.perflevel%u.name"
+ "ios"
+ "iossimulator"
+ "kqueue"
+ "maccatalyst"
+ "mach ports: %u (%.0f%% occupied)\n"
+ "macos"
+ "memorystatus_control(MEMORYSTATUS_CMD_GET_PROCESS_IS_MANAGED, pid)"
+ "must be run as root, running as uid:%u euid:%u"
+ "netpolicy"
+ "nexus"
+ "num tasks: %u\n\n"
+ "pipe"
+ "platform: %s (%u)\n"
+ "proc_pidinfo(... PROC_PIDPLATFORMINFO ...)"
+ "proc_pidinfo(PROC_PIDLISTFDS)"
+ "proc_pidinfo(PROC_PIDLISTFDS, fds)"
+ "psem"
+ "pshm"
+ "responsibility"
+ "run time: %llu s\n"
+ "runaway daemon mitigation: ACTIVE"
+ "runaway-mitigation "
+ "runningboard managed: %s\n"
+ "skipping pid %d (fill_coalitions)\n"
+ "skipping pid %d (get_audit_token)\n"
+ "skipping pid %d (proc_name)\n"
+ "socket"
+ "task %u pid changed? from %d to %d\n"
+ "threadcounts.ptc_len %d mismatch with level_count %u\n"
+ "tvossimulator"
+ "unique ID/version: %llu / %d, parent: %u / %llu / %d\n"
+ "unknown"
+ "visionos"
+ "visionossimulator"
+ "vnode"
+ "watchos"
+ "watchossimulator"
+ "workqueue threads: %u running: %u blocked: %u"
- "\t\t [--vouchers(=1|0)] [--coalitions=(all|jetsam|resource)] [process-name|pid]"
- "\t\tUnknown (%d): %s\n"
- "\t\treq turnstiles sync promotion qos: %s, user promotion base pri: %d\n"
- "\tboosted by: \"%s\" [%d]\n"
- "\ttaskinfo [-h|--help] [--threads] [--dq] [--boosts] [--verbose] [--all]"
- "\tthread ID: 0x%llx / %lld\n"
- "  %-5u %-32s"
- " %7llu %7llu  %s "
- " (%s, %s; %s, %s)"
- " group 0x%llx (%s%s%s%s%s%s%s%s%s, 0x%d)"
- "%-5u %-34s"
- "(unknwn)"
- "Encountered invalid container while generating boost map\n"
- "Resource  Jetsam  Role   "
- "boosts: %d (%d externalized)\n"
- "coalition (type %d RESOURCE) ID: %llu\n"
- "count:%d exceeds STATIC_PERFLEVEL_COUNT:%d skipping PROC_PIDTHREADCOUNTS data\n"
- "hw.perflevel%d.name"
- "mach ports: %d (%.0f%% occupied)\n"
- "must be run as root"
- "num tasks: %d\n\n"
- "run time: %lld s\n"
- "skipping pid %u (fill_coalitions)\n"
- "skipping pid %u (get_audit_token)\n"
- "skipping pid %u (proc_name)\n"
- "task %d pid changed? from %d to %d\n"
- "threadcounts.ptc_len %d mismatch with level_count %d\n"
- "unique ID/version: %llu / %d\n"
- "workqueue threads: %d running: %d blocked: %d"

```
