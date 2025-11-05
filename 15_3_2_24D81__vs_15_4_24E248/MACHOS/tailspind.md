## tailspind

> `/usr/libexec/tailspind`

```diff

-200.2.0.0.0
-  __TEXT.__text: 0x7c54
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_stubs: 0x460
-  __TEXT.__objc_methlist: 0x14c
+218.2.0.0.0
+  __TEXT.__text: 0xba14
+  __TEXT.__auth_stubs: 0x990
+  __TEXT.__objc_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x1c4
   __TEXT.__const: 0x104
-  __TEXT.__cstring: 0x779
-  __TEXT.__objc_methname: 0x717
-  __TEXT.__oslogstring: 0x1a0a
-  __TEXT.__objc_classname: 0x16
-  __TEXT.__objc_methtype: 0xe5
-  __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x198
-  __DATA_CONST.__auth_got: 0x498
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__cstring: 0xe9d
+  __TEXT.__objc_methname: 0x9a4
+  __TEXT.__oslogstring: 0x1e6f
+  __TEXT.__objc_classname: 0x17
+  __TEXT.__objc_methtype: 0xfb
+  __TEXT.__gcc_except_tab: 0x238
+  __TEXT.__unwind_info: 0x358
+  __DATA_CONST.__auth_got: 0x4d8
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2d8
-  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x210
-  __DATA.__objc_selrefs: 0x188
-  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_const: 0x2a0
+  __DATA.__objc_selrefs: 0x200
+  __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x2168
+  __DATA.__data: 0x2160
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x460
+  __DATA.__bss: 0x56c
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 539AF47E-FA70-35F7-B196-2FAE1CA51C72
-  Functions: 143
-  Symbols:   184
-  CStrings:  293
+  UUID: C0B624B2-91C9-3D91-AD35-7DB09C11227C
+  Functions: 221
+  Symbols:   194
+  CStrings:  392
 
Symbols:
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSAssertionHandler
+ _TSPDumpOptions_EndTimestamp
+ __sl_dlopen
+ _cputrace_session_data_from_disk
+ _create_and_start_cputrace_live_recording
+ _dlerror
+ _dlsym
+ _reinit_cputrace_live_recording_from_existing_session
+ _tailspin_cputrace_enabled_get_default
CStrings:
+ "%{public}s requested to change tailspin CPUTrace enablement to %{bool}d from default %{bool}d"
+ "%{public}s requested to change tailspin CPUTrace enablement to %{bool}d, overriding previous request from %{public}s to change tailspin CPUTrace enablement to %{bool}d"
+ "/usr/lib/libhwtrace_private.dylib"
+ "/usr/local/lib/libhwtrace_private.dylib"
+ "/var/db/tailspin_cputrace_session.json"
+ "11"
+ "<apply_config>"
+ "<apply_config_%s>"
+ "<foreground_tracing>"
+ "<profile_or_tasking>"
+ "@\"NSString\""
+ "AppleHWTrace_SoftLinking.h"
+ "B"
+ "B16@0:8"
+ "Client requested end timestamp that is past time window that tailspin can provide (tailspin start timestamp: %llu, client timestamp: %llu). Not saving tailspin file."
+ "CoreAnalytics Event %@ payload: %@"
+ "DidClientRequestEndTimestamp"
+ "DidPrevClientSaveOverlapWithEndTimestamp"
+ "ERROR"
+ "File descriptor %d is not read-write (flags: 0x%x)"
+ "Got error when attempting to pause CPUTrace (may not be fatal): %d"
+ "Got error when attempting to stop CPUTrace: %d"
+ "Invalid type for TSPDumpOptions_EndTimestamp. Expect %@, found %@."
+ "Missing libhwtrace dependency in %s"
+ "No CPUTrace session found to teardown for disablement"
+ "No existing CPUTrace session found to teardown"
+ "PostProcessing_Libktrace"
+ "PostProcessing_Tailspin"
+ "PrevExecName"
+ "Reverted previous request by %{public}s to change tailspin CPUTrace enablement to %{bool}d to default %{bool}d"
+ "T@\"NSString\",&,N,V_prevExecName"
+ "TB,N,V_didClientRequestEndTimestamp"
+ "TB,N,V_didPrevClientSaveOverlapWithEndTimestamp"
+ "Tearing down CPUTrace session for disablement"
+ "Tearing down existing CPUTrace session"
+ "Unable to save tailspin for %{public}s [%d]: file descriptor %d is not read-write (flags: 0x%x)"
+ "Unable to save tailspin for %{public}s: %@"
+ "Updating trace buffer reset event name: %s (was %s)"
+ "_didClientRequestEndTimestamp"
+ "_didPrevClientSaveOverlapWithEndTimestamp"
+ "_prevExecName"
+ "bytes"
+ "client %s [%d] does not bear entitlement \"%s\"; refusing TAILSPIN_GET_CPUTRACE_SESSION command"
+ "com.apple.tailspin.cputrace"
+ "com.apple.tailspind.post_processing_queue"
+ "currentHandler"
+ "didClientRequestEndTimestamp"
+ "didPrevClientSaveOverlapWithEndTimestamp"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "hwtrace_error_t soft_hwtrace_live_recording_pause(hwtrace_live_recording_t)"
+ "hwtrace_error_t soft_hwtrace_live_recording_stop(hwtrace_live_recording_t)"
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
+ "ktrace buffer starts after client's end timestamp"
+ "length"
+ "numberWithBool:"
+ "prevExecName"
+ "setDidClientRequestEndTimestamp:"
+ "setDidPrevClientSaveOverlapWithEndTimestamp:"
+ "setPrevExecName:"
+ "startRecordingTimeForLibktracePostProcessing"
+ "startRecordingTimeForTailspinPostProcessing"
+ "stopRecordingTimeForLibktracePostProcessing"
+ "stopRecordingTimeForTailspinPostProcessing"
+ "tailspin CPUTrace config requested by client %s [%d]"
+ "tailspin_cputrace_session_data"
+ "teardown_cputrace_live_recording"
+ "v24@?0r*8Q16"
+ "void *libhwtrace_privateLibrary(void)"
+ "void soft_hwtrace_live_recording_deinit(hwtrace_live_recording_t)"
- "!"
- "File descriptor is not read-write %d"
- "KDBG_STATE"
- "Unable to save tailspin for %{public}s [%d]: file descriptor is not read-write %d"
- "Unable to save tailspin for %{public}s: resulting trace would be shorter than desired duration"
- "Updating trace buffer start info: %s at %llu (was %s at %llu)"

```
