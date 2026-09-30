## libtailspin.dylib

> `/usr/lib/libtailspin.dylib`

```diff

 218.2.0.0.0
-  __TEXT.__text: 0x1eb44
-  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__text: 0x269d4
+  __TEXT.__auth_stubs: 0x1070
   __TEXT.__objc_methlist: 0x1c4
   __TEXT.__const: 0x189
-  __TEXT.__cstring: 0x1ae6
-  __TEXT.__oslogstring: 0x2433
-  __TEXT.__gcc_except_tab: 0x1274
+  __TEXT.__cstring: 0x2eec
+  __TEXT.__oslogstring: 0x2a59
+  __TEXT.__gcc_except_tab: 0x1b1c
   __TEXT.__ustring: 0x6
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__unwind_info: 0x790
+  __TEXT.__unwind_info: 0xa18
   __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x108d
+  __TEXT.__objc_methname: 0x10f9
   __TEXT.__objc_methtype: 0xfb
-  __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x958
+  __TEXT.__objc_stubs: 0x1180
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0xa40
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c8
+  __DATA_CONST.__objc_selrefs: 0x4f0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x848
+  __AUTH_CONST.__auth_got: 0x850
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1a40
+  __AUTH_CONST.__cfstring: 0x1b40
   __AUTH_CONST.__objc_const: 0x2a0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x10
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x4a8
+  __DATA.__bss: 0x6a8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x21b8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 504
-  Symbols:   519
-  CStrings:  676
+  Functions: 653
+  Symbols:   538
+  CStrings:  794
 
Symbols:
+ _OBJC_CLASS_$_NSData
+ _TSPConfiguration_CPUTraceEnabledKey
+ _TSPConfiguration_CPUTraceEnabledModifierKey
+ _TSPConfiguration_CPUTraceKey
+ _TSPDumpOptions_ShouldCollectCPUTrace
+ _TSPTaskingConfiguration_CPUTraceEnabledKey
+ _cputrace_session_data_from_disk
+ _create_and_start_cputrace_live_recording
+ _dlerror
+ _reinit_cputrace_live_recording_from_existing_session
+ _serialize_cputrace_session
+ _tailspin_cputrace_enabled_get
+ _tailspin_cputrace_enabled_get_default
+ _tailspin_cputrace_enabled_is_default
+ _tailspin_cputrace_enabled_reset
+ _tailspin_cputrace_enabled_set_with_options
+ _tailspin_cputrace_handle_deinit
+ _tailspin_get_cputrace_handle
+ _tailspin_pause_cputrace
CStrings:
+ "\t    CPUTrace                       = %@"
+ "/usr/lib/libhwtrace_private.dylib"
+ "/usr/local/lib/libhwtrace_private.dylib"
+ "/var/db/tailspin_cputrace_session.json"
+ "AppleHWTrace_SoftLinking.h"
+ "CPUTrace"
+ "CPUTraceEnabled"
+ "CPUTraceEnabledModifier"
+ "Failed to create CPUTrace live recording object for pause/stop"
+ "Failed to create CPUTrace live recording object: %d"
+ "Failed to create CPUTrace live recording session: %d"
+ "Failed to create CPUTrace live recording: %d"
+ "Failed to create CPUTrace session UTF-8 string from data"
+ "Failed to create hwtrace recording from live recording: %d"
+ "Failed to create live recording object: %d"
+ "Failed to create live recording session: %d"
+ "Failed to deserialize existing CPUTrace session"
+ "Failed to find %s system for CPUTrace live recording"
+ "Failed to get valid serialized CPUTrace session"
+ "Failed to pause CPUTrace: (hwtrace error code: %d)"
+ "Failed to query device topology for CPUTrace live recording"
+ "Failed to save CPUTrace data to file: %d"
+ "Failed to serialize CPUTrace session. Tearing down"
+ "Failed to start CPUTrace live recording: %d"
+ "Got error when attempting to pause CPUTrace (may not be fatal): %d"
+ "Got error when attempting to stop CPUTrace: %d"
+ "Missing libhwtrace dependency in %s"
+ "Missing libhwtrace in %s"
+ "Missing libhwtrace in %s in CPUTrace pause+stop"
+ "Missing libhwtrace in %s in save to ktrace"
+ "Missing libhwtrace in %s post-processing setup"
+ "No CPUTrace session file found"
+ "PauseCPUTrace"
+ "Received non-dictionary reply when querying CPUTrace handle"
+ "Received unsuccessful reply when querying CPUTrace handle"
+ "Saving out CPUTrace data to file"
+ "Setting up post-processing for CPUTrace collection"
+ "Started new CPUTrace session %{public, uuid_t}.16P"
+ "TailspinTaskedIsCPUTraceEnabled"
+ "Unable to set up CPUTrace post-processing due to failing to create live recording object earlier"
+ "Unable to write CPUTrace session file to '%{public}s'"
+ "XNU"
+ "const char *soft_hwtrace_live_recording_session_serialize(hwtrace_live_recording_session_t)"
+ "const char *soft_hwtrace_live_system_name(hwtrace_live_system_t)"
+ "create_and_start_cputrace_live_recording"
+ "dataUsingEncoding:"
+ "dataWithContentsOfFile:"
+ "hwtrace_error_t soft_hwtrace_live_recording_init_from_session(hwtrace_live_recording_session_t, hwtrace_live_recording_t *)"
+ "hwtrace_error_t soft_hwtrace_live_recording_init_with_options(hwtrace_live_recording_options_t, hwtrace_live_recording_t *)"
+ "hwtrace_error_t soft_hwtrace_live_recording_pause(hwtrace_live_recording_t)"
+ "hwtrace_error_t soft_hwtrace_live_recording_session_init(const char *, hwtrace_live_recording_session_t *)"
+ "hwtrace_error_t soft_hwtrace_live_recording_start(hwtrace_live_recording_t, hwtrace_live_recording_session_t *)"
+ "hwtrace_error_t soft_hwtrace_live_recording_stop(hwtrace_live_recording_t)"
+ "hwtrace_error_t soft_hwtrace_recording_init_from_live_recording(hwtrace_live_recording_t, hwtrace_recording_t *)"
+ "hwtrace_error_t soft_hwtrace_recording_save_to_ktrace(hwtrace_recording_t, ktrace_file_t)"
+ "hwtrace_live_recording_deinit"
+ "hwtrace_live_recording_init_from_session"
+ "hwtrace_live_recording_init_with_options"
+ "hwtrace_live_recording_options_add_system"
+ "hwtrace_live_recording_options_deinit"
+ "hwtrace_live_recording_options_init"
+ "hwtrace_live_recording_options_set_background"
+ "hwtrace_live_recording_options_set_session_policy"
+ "hwtrace_live_recording_options_t soft_hwtrace_live_recording_options_init()"
+ "hwtrace_live_recording_pause"
+ "hwtrace_live_recording_postprocess"
+ "hwtrace_live_recording_postprocess_options_deinit"
+ "hwtrace_live_recording_postprocess_options_init"
+ "hwtrace_live_recording_postprocess_options_set_ktrace_session"
+ "hwtrace_live_recording_postprocess_options_t soft_hwtrace_live_recording_postprocess(hwtrace_live_recording_t, hwtrace_live_recording_postprocess_options_t)"
+ "hwtrace_live_recording_postprocess_options_t soft_hwtrace_live_recording_postprocess_options_deinit(hwtrace_live_recording_postprocess_options_t)"
+ "hwtrace_live_recording_postprocess_options_t soft_hwtrace_live_recording_postprocess_options_init()"
+ "hwtrace_live_recording_postprocess_options_t soft_hwtrace_live_recording_postprocess_options_set_ktrace_session(hwtrace_live_recording_postprocess_options_t, ktrace_session_t)"
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
+ "hwtrace_live_recording_system_options_t soft_hwtrace_live_recording_options_add_system(hwtrace_live_recording_options_t, hwtrace_live_system_t)"
+ "hwtrace_live_system_name"
+ "hwtrace_live_topology"
+ "hwtrace_live_topology_systems"
+ "hwtrace_live_topology_t soft_hwtrace_live_topology()"
+ "hwtrace_recording_deinit"
+ "hwtrace_recording_init_from_live_recording"
+ "hwtrace_recording_save_to_ktrace"
+ "initWithData:encoding:"
+ "post_process_file"
+ "reinit_cputrace_live_recording_from_existing_session"
+ "serialize_cputrace_session"
+ "stringWithFormat:"
+ "tailspin_cputrace_handle_deinit"
+ "tailspin_cputrace_session_data"
+ "tailspin_dump_option_should_collect_cputrace"
+ "tailspin_pause_cputrace"
+ "tailspin_save_trace_with_standard_chunks"
+ "void *libhwtrace_privateLibrary()"
+ "void *libhwtrace_privateLibrary(void)"
+ "void soft_hwtrace_live_recording_deinit(hwtrace_live_recording_t)"
+ "void soft_hwtrace_live_recording_options_deinit(hwtrace_live_recording_options_t)"
+ "void soft_hwtrace_live_recording_options_set_background(hwtrace_live_recording_options_t, bool)"
+ "void soft_hwtrace_live_recording_options_set_session_policy(hwtrace_live_recording_options_t, hwtrace_live_recording_option_session_policy_t)"
+ "void soft_hwtrace_live_recording_session_deinit(hwtrace_live_recording_session_t)"
+ "void soft_hwtrace_live_recording_session_uuid(hwtrace_live_recording_session_t, unsigned char *)"
+ "void soft_hwtrace_live_recording_system_options_set_context_target(hwtrace_live_recording_system_options_t, hwtrace_live_recording_system_option_context_target_t)"
+ "void soft_hwtrace_live_recording_system_options_set_driver(hwtrace_live_recording_system_options_t, bool)"
+ "void soft_hwtrace_live_recording_system_options_set_exception_level_target(hwtrace_live_recording_system_options_t, hwtrace_live_recording_system_option_exception_level_target_t)"
+ "void soft_hwtrace_live_recording_system_options_set_production(hwtrace_live_recording_system_options_t, bool)"
+ "void soft_hwtrace_live_recording_system_options_set_trace_mode(hwtrace_live_recording_system_options_t, hwtrace_live_recording_system_option_trace_mode_t)"
+ "void soft_hwtrace_live_topology_systems(hwtrace_live_topology_t, hwtrace_live_system_t **, size_t *)"
+ "void soft_hwtrace_recording_deinit(hwtrace_recording_t)"
+ "writeToFile:atomically:"

```
