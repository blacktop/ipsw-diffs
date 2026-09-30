## AppleDeviceQueryService

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService`

```diff

-396.80.5.0.0
-  __TEXT.__text: 0x89c8
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x658
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x3f94
+408.100.18.0.0
+  __TEXT.__text: 0xbba4
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_stubs: 0x1120
+  __TEXT.__objc_methlist: 0x648
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x52b9
   __TEXT.__objc_classname: 0xfc
-  __TEXT.__objc_methname: 0x111a
-  __TEXT.__objc_methtype: 0x39d
+  __TEXT.__objc_methname: 0x1115
+  __TEXT.__objc_methtype: 0x3b1
   __TEXT.__oslogstring: 0xb
-  __TEXT.__gcc_except_tab: 0x1a4
+  __TEXT.__gcc_except_tab: 0x214
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x400
-  __DATA_CONST.__cfstring: 0x2d80
+  __TEXT.__unwind_info: 0x2d8
+  __DATA_CONST.__auth_got: 0x438
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__cfstring: 0x35e0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA.__objc_const: 0x990
-  __DATA.__objc_selrefs: 0x5a0
+  __DATA.__objc_selrefs: 0x598
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x230
   __DATA.__data: 0xc00

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 39772CDF-79A6-37D5-A9B0-9705E63D6B02
-  Functions: 174
-  Symbols:   167
-  CStrings:  1075
+  UUID: BA43AC26-00CA-3EEA-A00F-F056EC1E31F6
+  Functions: 198
+  Symbols:   224
+  CStrings:  1296
 
Symbols:
+ _CSIsNull
+ _CSRegionGetName
+ _CSRegionGetRange
+ _CSRelease
+ _CSSymbolOwnerForeachSegment
+ _CSSymbolOwnerGetArchitecture
+ _CSSymbolOwnerGetCFUUIDBytes
+ _CSSymbolOwnerGetPath
+ _CSSymbolicatorCreateWithTask
+ _CSSymbolicatorForeachSymbolOwnerAtTime
+ _NDR_record
+ ___chkstk_darwin
+ ___error
+ __dispatch_source_type_mach_recv
+ _backtrace_from_fp
+ _backtrace_image_offsets
+ _backtrace_symbols
+ _basename
+ _catch_mach_exc_subsystem
+ _catch_mach_exception_raise_state_identity
+ _dispatch_async
+ _dispatch_mig_server
+ _dispatch_queue_create
+ _dispatch_resume
+ _dispatch_source_create
+ _dispatch_source_set_cancel_handler
+ _dispatch_source_set_event_handler
+ _dispatch_time
+ _exit
+ _mach_error_string
+ _mach_exc_server
+ _mach_exc_server_routine
+ _mach_port_allocate
+ _mach_port_deallocate
+ _mach_port_destruct
+ _mach_port_insert_right
+ _mach_task_self_
+ _mach_vm_read_overwrite
+ _malloc_type_calloc
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _pid_for_task
+ _proc_pidinfo
+ _proc_pidpath
+ _registerCrashReporter
+ _sigaction
+ _snprintf
+ _strcmp
+ _strerror
+ _strncmp
+ _strncpy
+ _sysctl
+ _sysctlbyname
+ _sysctlnametomib
+ _task_set_exception_ports
+ _task_threads
+ _thread_get_state
+ _uuid_unparse
+ _uuid_unparse_lower
+ _vm_deallocate
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "%-21s%s"
+ "%-21s%s (%s)"
+ "%-21s%s [%d]"
+ "%s (%s)"
+ "%s (UUID: %s __TEXT + 0x%zX) "
+ "%s%6s: 0x%016llx"
+ "/Library/Caches/com.apple.xbs/561B6BE2-910E-4DFD-990B-5836D9F2135B/TemporaryDirectory.gYmg00/Sources/ZhuGe_Service/ZhuGeCommon/NSArray+ZhuGe.m"
+ "/Library/Caches/com.apple.xbs/561B6BE2-910E-4DFD-990B-5836D9F2135B/TemporaryDirectory.gYmg00/Sources/ZhuGe_Service/ZhuGeCommon/NSNumber+ZhuGe.m"
+ "/Library/Caches/com.apple.xbs/561B6BE2-910E-4DFD-990B-5836D9F2135B/TemporaryDirectory.gYmg00/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeCache.m"
+ "/Library/Caches/com.apple.xbs/561B6BE2-910E-4DFD-990B-5836D9F2135B/TemporaryDirectory.gYmg00/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeCrashReporter.m"
+ "/Library/Caches/com.apple.xbs/561B6BE2-910E-4DFD-990B-5836D9F2135B/TemporaryDirectory.gYmg00/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeLog.m"
+ "/Library/Caches/com.apple.xbs/561B6BE2-910E-4DFD-990B-5836D9F2135B/TemporaryDirectory.gYmg00/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeUtils.m"
+ "/Library/Caches/com.apple.xbs/561B6BE2-910E-4DFD-990B-5836D9F2135B/TemporaryDirectory.gYmg00/Sources/ZhuGe_Service/ZhuGeInternalSupport/ZhuGeInternalSupportAssistant.m"
+ "/Library/Caches/com.apple.xbs/561B6BE2-910E-4DFD-990B-5836D9F2135B/TemporaryDirectory.gYmg00/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeService/ZhuGeService.m"
+ "/Library/Caches/com.apple.xbs/561B6BE2-910E-4DFD-990B-5836D9F2135B/TemporaryDirectory.gYmg00/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeSupportAssistant.m"
+ "0x%016llx - 0x%016llx %s %s <%s> %s"
+ "========== ABORT: set signals action failed ========================"
+ "========== ABORT: timed out when creating symbolicator ==============="
+ "========== ABORT: timed out when printing crash information =========="
+ "========== BEGIN: caught a BSD signal %d(%s) =================="
+ "========== BEGIN: caught a mach exception ============================"
+ "========== END: caught a mach exception =============================="
+ "========== End: caught a BSD signal %d(%s) =================="
+ "BSDSignalsCrashHandler"
+ "Binary Images:"
+ "Code Type:"
+ "EXC_ARITHMETIC"
+ "EXC_BAD_ACCESS"
+ "EXC_BAD_INSTRUCTION"
+ "EXC_BREAKPOINT"
+ "EXC_CRASH"
+ "EXC_EMULATION"
+ "EXC_GUARD"
+ "EXC_RESOURCE"
+ "EXC_RPC_ALERT"
+ "EXC_SOFTWARE"
+ "EXC_UNSUPPORTED"
+ "Exception Type:"
+ "Failed to allocate crash report, error %d(%s)!"
+ "Failed to allocate for crash_report_thread, error %d(%s)!"
+ "Failed to allocate mach port, error %d(%s)!"
+ "Failed to create CS symbolicator!"
+ "Failed to create crash thread!"
+ "Failed to create dispatch source for receiving mach msg sent to exception port!"
+ "Failed to create exception port!"
+ "Failed to create non-crash thread!"
+ "Failed to destruct exception port!"
+ "Failed to dispatch MIG mach exception server!"
+ "Failed to dump registers for crash thread!"
+ "Failed to get ARM thread exception state, error %d(%s)!"
+ "Failed to get ARM thread state, error %d(%s)!"
+ "Failed to get a proxy for \"%@\"!"
+ "Failed to get arm thread state, error %d(%s)!"
+ "Failed to get backtrace symbols!"
+ "Failed to get cpu type for pid(%d), error %d(%s)!"
+ "Failed to get os version, error %d(%s)!"
+ "Failed to get proc info, error %d(%s)!"
+ "Failed to get proc path, error %d(%s)!"
+ "Failed to get threads for task, error %d(%s)!"
+ "Failed to insert send right for expcetion port, error %d(%s)!"
+ "Failed to link CoreSymbolication framework, CSSymbolicatorCreateWithTask is unavailable!"
+ "Failed to read frame from addr(0x%016llx), error %d(%s)!"
+ "Failed to register BSD signal handler!"
+ "Failed to register mach exception handler!"
+ "Failed to set action for SIGABRT, error %d(%s)!"
+ "Failed to set action for SIGBUS, error %d(%s)!"
+ "Failed to set action for SIGFPE, error %d(%s)!"
+ "Failed to set action for SIGILL, error %d(%s)!"
+ "Failed to set action for SIGPIPE, error %d(%s)!"
+ "Failed to set action for SIGSEGV, error %d(%s)!"
+ "Failed to set action for SIGTRAP, error %d(%s)!"
+ "Failed to set exception ports for current task, error %d(%s)!"
+ "Failed to sysctlnametomib(sysctl.proc_cputype), error %d(%s)!"
+ "Invalid crash thread in report"
+ "Invalid pid: %d!"
+ "MACH_HEADER"
+ "Native"
+ "No arm thread backtrace frame pointer specified!"
+ "No crash context to report!"
+ "No crash thread from context!"
+ "No crash thread in report"
+ "No thread specified!"
+ "No threads got from task!"
+ "OS Version:"
+ "Path:"
+ "Process:"
+ "SIGABRT"
+ "SIGALRM"
+ "SIGBUS"
+ "SIGCHLD"
+ "SIGCONT"
+ "SIGEMT"
+ "SIGFPE"
+ "SIGHUP"
+ "SIGILL"
+ "SIGINFO"
+ "SIGINT"
+ "SIGIO"
+ "SIGKILL"
+ "SIGPIPE"
+ "SIGPROF"
+ "SIGQUIT"
+ "SIGSEGV"
+ "SIGSTOP"
+ "SIGSYS"
+ "SIGTERM"
+ "SIGTRAP"
+ "SIGTSTP"
+ "SIGTTIN"
+ "SIGTTOU"
+ "SIGURG"
+ "SIGUSR1"
+ "SIGUSR2"
+ "SIGVTALRM"
+ "SIGWINCH"
+ "SIGXCPU"
+ "SIGXFSZ"
+ "Successfully registered BSD signal handler."
+ "Successfully registered mach exception handler."
+ "Thread %d Crashed:"
+ "Thread %d crashed with Thread State:"
+ "Thread %d:"
+ "Translated"
+ "Unnecessary to explicitly register crash reporter in this environment!"
+ "Unsupported ARM state!"
+ "Unsupported ARM thread state!"
+ "ZhuGe exception server does not support catch_mach_exception_raise!"
+ "ZhuGe exception server does not support catch_mach_exception_raise_state!"
+ "__TEXT"
+ "arm"
+ "arm64"
+ "arm64_32"
+ "armThreadBacktrace"
+ "armThreadBacktraceFromFP"
+ "armThreadBacktraceWithUnifiedState"
+ "armThreadSetRegisters"
+ "catch_mach_exception_raise"
+ "catch_mach_exception_raise_state"
+ "catch_mach_exception_raise_state_identity"
+ "com.apple.ZhuGe.ZhuGeCrashReporter.getTaskImageInfo"
+ "com.apple.ZhuGe.ZhuGeCrashReporter.printCrash"
+ "com.apple.ZhuGe.ZhuGeCrashReporter.registerMachExceptionsHandler"
+ "createCrashReport"
+ "createCrashReportThread"
+ "createExceptionPort"
+ "getProcCPUType"
+ "getProcInfo"
+ "getTaskImageInfo"
+ "iPhone OS"
+ "kern.osversion"
+ "printCrash"
+ "printCrash_block_invoke"
+ "printRemoteLog:withReply:"
+ "registerCrashReporter"
+ "registerMachExceptionsHandler"
+ "registerMachExceptionsHandler_block_invoke"
+ "registerMachExceptionsHandler_block_invoke_2"
+ "setActionForSignals"
+ "sysctl.proc_cputype"
+ "sysctl.proc_translated"
+ "v16@?0@\"NSNumber\"8"
+ "v24@?0{_CSTypeRef=QQ}8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24"
+ "x86"
+ "x86_64"
- "/Library/Caches/com.apple.xbs/Sources/ZhuGe_Service/ZhuGeCommon/NSArray+ZhuGe.m"
- "/Library/Caches/com.apple.xbs/Sources/ZhuGe_Service/ZhuGeCommon/NSNumber+ZhuGe.m"
- "/Library/Caches/com.apple.xbs/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeCache.m"
- "/Library/Caches/com.apple.xbs/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeLog.m"
- "/Library/Caches/com.apple.xbs/Sources/ZhuGe_Service/ZhuGeCommon/ZhuGeUtils.m"
- "/Library/Caches/com.apple.xbs/Sources/ZhuGe_Service/ZhuGeInternalSupport/ZhuGeInternalSupportAssistant.m"
- "/Library/Caches/com.apple.xbs/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeService/ZhuGeService.m"
- "/Library/Caches/com.apple.xbs/Sources/ZhuGe_Service/ZhuGeSupport/ZhuGeSupportAssistant.m"
- "printRemoteLog:"
- "serviceXpcName"
- "v24@0:8@\"NSString\"16"

```
