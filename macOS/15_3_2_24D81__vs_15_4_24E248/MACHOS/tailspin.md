## tailspin

> `/usr/bin/tailspin`

```diff

-200.2.0.0.0
-  __TEXT.__text: 0x54e4
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_stubs: 0x560
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x2909
-  __TEXT.__gcc_except_tab: 0xe4
+218.2.0.0.0
+  __TEXT.__text: 0x7c68
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_stubs: 0x600
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x28c
+  __TEXT.__cstring: 0x2f7f
   __TEXT.__objc_classname: 0x1
-  __TEXT.__oslogstring: 0x1c
-  __TEXT.__objc_methname: 0x350
-  __TEXT.__unwind_info: 0x158
-  __DATA_CONST.__auth_got: 0x3b8
-  __DATA_CONST.__got: 0x118
+  __TEXT.__oslogstring: 0x3f
+  __TEXT.__objc_methname: 0x3e7
+  __TEXT.__unwind_info: 0x2d0
+  __DATA_CONST.__auth_got: 0x3f8
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x6d0
-  __DATA_CONST.__cfstring: 0x360
+  __DATA_CONST.__const: 0x768
+  __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x158
+  __DATA.__objc_selrefs: 0x180
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x410
+  __DATA.__bss: 0x4e8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
   - /System/Library/PrivateFrameworks/SampleAnalysis.framework/Versions/A/SampleAnalysis
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/TailspinSymbolication.framework/Versions/A/TailspinSymbolication
   - /System/Library/PrivateFrameworks/kperfdata.framework/Versions/A/kperfdata
   - /System/Library/PrivateFrameworks/ktrace.framework/Versions/A/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 8B5C0F30-3EDF-3276-AAB9-2E947431C986
-  Functions: 68
-  Symbols:   159
-  CStrings:  269
+  UUID: 000095D4-B942-367B-985F-FA43213BA38F
+  Functions: 123
+  Symbols:   169
+  CStrings:  319
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ _TSPDumpOptions_ShouldCollectCPUTrace
+ __os_log_debug_impl
+ __sl_dlopen
+ _dlsym
+ _tailspin_cputrace_enabled_reset
+ _tailspin_cputrace_enabled_set_with_options
+ _tailspin_cputrace_handle_deinit
+ _tailspin_get_cputrace_handle
+ _tailspin_pause_cputrace
CStrings:
+ "\t\t             cputrace 0|1\n"
+ "\t\t    --cputrace                              Adds active cputrace session data to the tailspin file\n"
+ "\t\ttailspin save [-r <string>] [-d] [-o] [-s] [-p <pid>] [-l <n>] [-n] [-c <n>] [--cputrace] <path to file>\n"
+ "%s"
+ "/usr/lib/libhwtrace_private.dylib"
+ "/usr/local/lib/libhwtrace_private.dylib"
+ "AppleHWTrace_SoftLinking.h"
+ "CoreAnalytics Event %@ payload: %@"
+ "Current CPUTrace session successfully paused\n"
+ "DidClientRequestEndTimestamp"
+ "DidPrevClientSaveOverlapWithEndTimestamp"
+ "PrevExecName"
+ "cputrace"
+ "currentHandler"
+ "didClientRequestEndTimestamp"
+ "didPrevClientSaveOverlapWithEndTimestamp"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "hwtrace_live_recording_deinit"
+ "hwtrace_live_recording_init_from_session"
+ "hwtrace_live_recording_init_with_options"
+ "hwtrace_live_recording_options_add_system"
+ "hwtrace_live_recording_options_deinit"
+ "hwtrace_live_recording_options_init"
+ "hwtrace_live_recording_options_set_background"
+ "hwtrace_live_recording_options_set_session_policy"
+ "hwtrace_live_recording_pause"
+ "hwtrace_live_recording_session_deinit"
+ "hwtrace_live_recording_session_init"
+ "hwtrace_live_recording_session_serialize"
+ "hwtrace_live_recording_session_uuid"
+ "hwtrace_live_recording_start"
+ "hwtrace_live_recording_stop"
+ "hwtrace_live_recording_system_options_set_context_target"
+ "hwtrace_live_recording_system_options_set_driver"
+ "hwtrace_live_recording_system_options_set_exception_level_target"
+ "hwtrace_live_recording_system_options_set_production"
+ "hwtrace_live_recording_system_options_set_trace_mode"
+ "hwtrace_live_system_name"
+ "hwtrace_live_topology"
+ "hwtrace_live_topology_systems"
+ "hwtrace_recording_deinit"
+ "hwtrace_recording_init_from_live_recording"
+ "hwtrace_recording_save_to_ktrace"
+ "pause-cputrace"
+ "prevExecName"
+ "void *libhwtrace_privateLibrary(void)"
- "\t\ttailspin save [-r <string>] [-d] [-o] [-s] [-p <pid>] [-l <n>] [-n] [-c <n>] <path to file>\n"

```
