## tailspind

> `/usr/libexec/tailspind`

```diff

 218.2.0.0.0
-  __TEXT.__text: 0xa124
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_stubs: 0x880
+  __TEXT.__text: 0xd40c
+  __TEXT.__auth_stubs: 0xbc0
+  __TEXT.__objc_stubs: 0x900
   __TEXT.__objc_methlist: 0x1c4
-  __TEXT.__const: 0x124
-  __TEXT.__cstring: 0xa20
-  __TEXT.__objc_methname: 0xb81
-  __TEXT.__oslogstring: 0x2262
+  __TEXT.__const: 0x12c
+  __TEXT.__cstring: 0xff6
+  __TEXT.__objc_methname: 0xbd2
+  __TEXT.__oslogstring: 0x256d
   __TEXT.__objc_classname: 0x17
   __TEXT.__objc_methtype: 0xfb
-  __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__auth_got: 0x5b8
-  __DATA_CONST.__got: 0x158
+  __TEXT.__gcc_except_tab: 0x238
+  __TEXT.__unwind_info: 0x390
+  __DATA_CONST.__auth_got: 0x5f0
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__cfstring: 0x540
+  __DATA_CONST.__const: 0x408
+  __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x2a0
-  __DATA.__objc_selrefs: 0x2b0
+  __DATA.__objc_selrefs: 0x2d0
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x2160
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x488
+  __DATA.__bss: 0x580
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 175
-  Symbols:   234
-  CStrings:  378
+  Functions: 240
+  Symbols:   242
+  CStrings:  430
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
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
+ "AppleHWTrace_SoftLinking.h"
+ "Got error when attempting to pause CPUTrace (may not be fatal): %d"
+ "Got error when attempting to stop CPUTrace: %d"
+ "Missing libhwtrace dependency in %s"
+ "No CPUTrace session found to teardown for disablement"
+ "No existing CPUTrace session found to teardown"
+ "Reverted previous request by %{public}s to change tailspin CPUTrace enablement to %{bool}d to default %{bool}d"
+ "Tearing down CPUTrace session for disablement"
+ "Tearing down existing CPUTrace session"
+ "bytes"
+ "client %s [%d] does not bear entitlement \"%s\"; refusing TAILSPIN_GET_CPUTRACE_SESSION command"
+ "com.apple.tailspin.cputrace"
+ "currentHandler"
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
+ "length"
+ "tailspin CPUTrace config requested by client %s [%d]"
+ "tailspin_cputrace_session_data"
+ "teardown_cputrace_live_recording"
+ "void *libhwtrace_privateLibrary(void)"
+ "void soft_hwtrace_live_recording_deinit(hwtrace_live_recording_t)"
- "client %s [%d] requested for tailspin data but was rejected by the allowlist"
- "hangtracerd"

```
