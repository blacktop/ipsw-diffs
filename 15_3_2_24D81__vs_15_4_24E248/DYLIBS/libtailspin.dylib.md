## libtailspin.dylib

> `/usr/lib/libtailspin.dylib`

```diff

-200.2.0.0.0
-  __TEXT.__text: 0x1f090
-  __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_methlist: 0x14c
-  __TEXT.__const: 0x171
-  __TEXT.__cstring: 0x19a4
-  __TEXT.__oslogstring: 0x226c
-  __TEXT.__gcc_except_tab: 0x12f4
+218.2.0.0.0
+  __TEXT.__text: 0x281bc
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_methlist: 0x1c4
+  __TEXT.__const: 0x199
+  __TEXT.__cstring: 0x2e4d
+  __TEXT.__oslogstring: 0x2a8c
+  __TEXT.__gcc_except_tab: 0x1b08
   __TEXT.__ustring: 0x6
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__unwind_info: 0x6f8
-  __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0xe14
-  __TEXT.__objc_methtype: 0xe5
-  __TEXT.__objc_stubs: 0xfe0
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x528
+  __TEXT.__unwind_info: 0xa38
+  __TEXT.__objc_classname: 0x18
+  __TEXT.__objc_methname: 0x10ac
+  __TEXT.__objc_methtype: 0xfb
+  __TEXT.__objc_stubs: 0x1120
+  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__const: 0x5b8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x460
+  __DATA_CONST.__objc_selrefs: 0x4d8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x750
-  __AUTH_CONST.__const: 0x740
-  __AUTH_CONST.__cfstring: 0x1760
-  __AUTH_CONST.__objc_const: 0x210
+  __AUTH_CONST.__auth_got: 0x7a0
+  __AUTH_CONST.__const: 0x7d0
+  __AUTH_CONST.__cfstring: 0x1900
+  __AUTH_CONST.__objc_const: 0x2a0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x10
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x4d0
+  __DATA.__bss: 0x6d0
   __DATA_DIRTY.__bss: 0x2178
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 97E5155D-FE29-305A-A6CE-B73FFE398EC0
-  Functions: 516
-  Symbols:   482
-  CStrings:  810
+  UUID: 61C2D883-4015-3173-BFEA-31A00190F96F
+  Functions: 688
+  Symbols:   515
+  CStrings:  978
 
Symbols:
+ _OBJC_CLASS_$_NSData
+ _TSPConfiguration_CPUTraceEnabledKey
+ _TSPConfiguration_CPUTraceEnabledModifierKey
+ _TSPConfiguration_CPUTraceKey
+ _TSPDumpOptions_EndTimestamp
+ _TSPDumpOptions_ShouldCollectCPUTrace
+ _TSPMetadata_SharedCacheInfo
+ _TSPMetadata_SharedCacheResidentSize
+ _TSPMetadata_SharedCacheVirtualSize
+ _TSPTaskingConfiguration_CPUTraceEnabledKey
+ _cputrace_session_data_from_disk
+ _create_and_start_cputrace_live_recording
+ _dlerror
+ _dlsym
+ _dyld_process_create_for_current_task
+ _dyld_process_dispose
+ _dyld_process_snapshot_create_for_process
+ _dyld_process_snapshot_dispose
+ _dyld_process_snapshot_get_shared_cache
+ _dyld_shared_cache_for_each_file
+ _mach_error_string
+ _mincore
+ _mmap
+ _munmap
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
+ _vm_page_size
- _dispatch_queue_create_with_target$V2
- _strdup
CStrings:
+ "\t    CPUTrace                       = %@"
+ "%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu numEvents=%{public,name=numEvents}llu requestID=0x%llx enableTelemetry=YES "
+ "/usr/lib/libhwtrace_private.dylib"
+ "/usr/local/lib/libhwtrace_private.dylib"
+ "/var/db/tailspin_cputrace_session.json"
+ "11"
+ "@\"NSString\""
+ "AppleHWTrace_SoftLinking.h"
+ "B"
+ "B16@0:8"
+ "CPUTrace"
+ "CPUTraceEnabled"
+ "CPUTraceEnabledModifier"
+ "Ended read session: %{public}@ [%d], original fd: %d, duped fd: %d"
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
+ "MAX_CHUNK_SIZE 0x%x isn't a page multiple 0x%lx"
+ "Missing libhwtrace dependency in %s"
+ "Missing libhwtrace in %s"
+ "Missing libhwtrace in %s in CPUTrace pause+stop"
+ "Missing libhwtrace in %s in save to ktrace"
+ "Missing libhwtrace in %s post-processing setup"
+ "No CPUTrace session file found"
+ "PauseCPUTrace"
+ "PostProcessing_Libktrace"
+ "PostProcessing_Tailspin"
+ "Received non-dictionary reply when querying CPUTrace handle"
+ "Received unsuccessful reply when querying CPUTrace handle"
+ "Saved %{bytes}lld tailspin on behalf of %{public}@ [%d]"
+ "Saved %{bytes}lld tailspin on behalf of %{public}@ [%d] (augment failed)"
+ "Saving out CPUTrace data to file"
+ "Setting up post-processing for CPUTrace collection"
+ "SharedCacheInfo"
+ "SharedCacheSizeResident"
+ "SharedCacheSizeVirtual"
+ "Started new CPUTrace session %{public, uuid_t}.16P"
+ "Started read session: %{public}@ [%d], original fd: %d, duped fd: %d, size: %{bytes}lld"
+ "T@\"NSString\",&,N,V_prevExecName"
+ "TB,N,V_didClientRequestEndTimestamp"
+ "TB,N,V_didPrevClientSaveOverlapWithEndTimestamp"
+ "TailspinTaskedIsCPUTraceEnabled"
+ "Unable to create read session for original fd %d (duped fd %d) from client %{public}@ [%d].: %{errno}d"
+ "Unable to fstat %{public}@'s saved tailspin file: %{errno}d"
+ "Unable to get ktfile for original fd %d (duped fd %d) from client %{public}@ [%d].: %{errno}d"
+ "Unable to set up CPUTrace post-processing due to failing to create live recording object earlier"
+ "Unable to start read session for original fd %d (duped fd %d) from client %{public}@ [%d].: %{errno}d"
+ "Unable to write CPUTrace session file to '%{public}s'"
+ "XNU"
+ "_didClientRequestEndTimestamp"
+ "_didPrevClientSaveOverlapWithEndTimestamp"
+ "_prevExecName"
+ "const char *soft_hwtrace_live_recording_session_serialize(hwtrace_live_recording_session_t)"
+ "const char *soft_hwtrace_live_system_name(hwtrace_live_system_t)"
+ "create_and_start_cputrace_live_recording"
+ "dataUsingEncoding:"
+ "dataWithContentsOfFile:"
+ "didClientRequestEndTimestamp"
+ "didPrevClientSaveOverlapWithEndTimestamp"
+ "failed to create dyld process:%d (%s)"
+ "failed to create snapshot of the process:%d (%s)"
+ "failed to fstat shared cache file %s: %{errno}d"
+ "failed to get shared cache"
+ "failed to open shared cache file %s: %{errno}d"
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
+ "mincore of 0x%llx,0x%llx of shared cache file %s failed: %{errno}d"
+ "mmap of 0x%llx,0x%llx of shared cache file %s failed: %{errno}d"
+ "munmap of 0x%llx,0x%llx of shared cache file %s failed: %{errno}d"
+ "native shared cache has %llu/%llu pages resident"
+ "post_process_file"
+ "prevExecName"
+ "reinit_cputrace_live_recording_from_existing_session"
+ "serialize_cputrace_session"
+ "setDidClientRequestEndTimestamp:"
+ "setDidPrevClientSaveOverlapWithEndTimestamp:"
+ "setPrevExecName:"
+ "shared cache file %s has %llu/%llu pages resident"
+ "startRecordingTimeForLibktracePostProcessing"
+ "startRecordingTimeForTailspinPostProcessing"
+ "stopRecordingTimeForLibktracePostProcessing"
+ "stopRecordingTimeForTailspinPostProcessing"
+ "stringWithFormat:"
+ "tailspin_cputrace_handle_deinit"
+ "tailspin_cputrace_session_data"
+ "tailspin_dump_option_end_timestamp"
+ "tailspin_dump_option_should_collect_cputrace"
+ "tailspin_pause_cputrace"
+ "tailspin_save_trace_with_standard_chunks"
+ "v16@?0r*8"
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
- "!"
- "%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu numEvents=%{public,name=numEvents}llu enableTelemetry=YES "
- "Ended read session: %{public}s [%d], original fd: %d, duped fd: %d"
- "Ended writing fd: %{public}s [%d], original fd: %d, duped fd: %d"
- "Saved %{bytes}lld tailspin on behalf of %{public}s [%d]"
- "Saved %{bytes}lld tailspin on behalf of %{public}s [%d] (augment failed)"
- "Started read session: %{public}s [%d], original fd: %d, duped fd: %d, size: %{bytes}lld"
- "Unable to create read session for original fd %d (duped fd %d) from client %{public}s [%d].: %{errno}d"
- "Unable to fstat %{public}s's saved tailspin file: %{errno}d"
- "Unable to get ktfile for original fd %d (duped fd %d) from client %{public}s [%d].: %{errno}d"
- "Unable to start read session for original fd %d (duped fd %d) from client %{public}s [%d].: %{errno}d"
- "com.apple.tailspind.post-processing-queue"

```
