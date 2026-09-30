## com.apple.dt.instruments.dtsecurity

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity`

```diff

-64566.107.1.0.0
-  __TEXT.__text: 0xc50c
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x400
-  __TEXT.__const: 0x1a0
-  __TEXT.__oslogstring: 0xe53
-  __TEXT.__cstring: 0xf23
+64570.75.1.0.0
+  __TEXT.__text: 0x13d94
+  __TEXT.__auth_stubs: 0x1650
+  __TEXT.__objc_stubs: 0x1200
+  __TEXT.__objc_methlist: 0x540
+  __TEXT.__const: 0x452
+  __TEXT.__oslogstring: 0x132c
+  __TEXT.__cstring: 0x1346
   __TEXT.__objc_classname: 0x112
   __TEXT.__objc_methtype: 0x29d
-  __TEXT.__gcc_except_tab: 0x418
-  __TEXT.__objc_methname: 0x1002
-  __TEXT.__unwind_info: 0x3d0
-  __DATA_CONST.__auth_got: 0x768
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0xa70
+  __TEXT.__gcc_except_tab: 0x42c
+  __TEXT.__objc_methname: 0x110a
+  __TEXT.__constg_swiftt: 0x140
+  __TEXT.__swift5_typeref: 0xa0
+  __TEXT.__swift5_reflstr: 0x2c4
+  __TEXT.__swift5_fieldmd: 0x23c
+  __TEXT.__swift5_proto: 0x20
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__unwind_info: 0x520
+  __TEXT.__eh_frame: 0x160
+  __DATA_CONST.__auth_got: 0xb40
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__auth_ptr: 0xd8
+  __DATA_CONST.__const: 0xe50
   __DATA_CONST.__cfstring: 0x880
-  __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA.__objc_const: 0xbf8
-  __DATA.__objc_selrefs: 0x4f0
+  __DATA.__objc_const: 0xde0
+  __DATA.__objc_selrefs: 0x550
   __DATA.__objc_ivar: 0x70
-  __DATA.__objc_data: 0x320
-  __DATA.__data: 0x198
-  __DATA.__bss: 0xc8
+  __DATA.__objc_data: 0x508
+  __DATA.__data: 0x2d0
+  __DATA.__common: 0x20
+  __DATA.__bss: 0x4d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 224
-  Symbols:   346
-  CStrings:  501
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  - /usr/local/lib/libhwtrace_private.dylib
+  Functions: 380
+  Symbols:   451
+  CStrings:  586
 
Symbols:
+ _OBJC_CLASS_$_DTProcessorTraceRecorder
+ _OBJC_CLASS_$_DVTProcessorTraceRecorderConfiguration
+ _OBJC_METACLASS_$_DTProcessorTraceRecorder
+ _OBJC_METACLASS_$_DVTProcessorTraceRecorderConfiguration
+ ___chkstk_darwin
+ __os_signpost_emit_with_name_impl
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_stdlib_reportUnimplementedInitializer
+ _hwtrace_cursor_init_from_thread
+ _hwtrace_cursor_next_range
+ _hwtrace_cursor_range
+ _hwtrace_live_recording_deinit
+ _hwtrace_live_recording_finalize_postprocessing
+ _hwtrace_live_recording_init_with_options
+ _hwtrace_live_recording_options_add_system
+ _hwtrace_live_recording_options_deinit
+ _hwtrace_live_recording_options_init
+ _hwtrace_live_recording_options_set_session_policy
+ _hwtrace_live_recording_pause
+ _hwtrace_live_recording_postprocess
+ _hwtrace_live_recording_postprocess_options_deinit
+ _hwtrace_live_recording_postprocess_options_init
+ _hwtrace_live_recording_postprocess_options_set_ktrace_session
+ _hwtrace_live_recording_resume
+ _hwtrace_live_recording_resume_wrapper
+ _hwtrace_live_recording_start
+ _hwtrace_live_recording_stop
+ _hwtrace_live_recording_system_options_add_context_target_filtered
+ _hwtrace_live_recording_system_options_set_context_target
+ _hwtrace_live_recording_system_options_set_driver
+ _hwtrace_live_recording_system_options_set_exception_level_target
+ _hwtrace_live_recording_system_options_set_production
+ _hwtrace_live_recording_system_options_set_throttling
+ _hwtrace_live_recording_system_options_set_trace_mode
+ _hwtrace_live_recording_system_options_set_virtual_ringbuffer_size
+ _hwtrace_live_system_has_capability
+ _hwtrace_live_system_name
+ _hwtrace_live_topology
+ _hwtrace_live_topology_systems
+ _hwtrace_load_options_deinit
+ _hwtrace_load_options_init
+ _hwtrace_range_terminator
+ _hwtrace_recording_deinit
+ _hwtrace_recording_init_from_live_recording
+ _hwtrace_recording_save
+ _hwtrace_recording_save_options_deinit
+ _hwtrace_recording_save_options_init
+ _hwtrace_recording_save_options_set_decode_trace
+ _hwtrace_recording_save_options_set_ktrace_file
+ _hwtrace_recording_save_options_set_port_mode
+ _hwtrace_system_tasks
+ _hwtrace_task_threads
+ _hwtrace_topology_systems
+ _hwtrace_trace_deinit
+ _hwtrace_trace_init_from_recording
+ _hwtrace_trace_topology
+ _is_resume_available
+ _ktrace_file_create_fd
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_opt_self
+ _objc_release_x9
+ _objc_retain_x28
+ _processorTraceRecorder
+ _swift_allocError
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
CStrings:
+ "B28@0:8i16^@20"
+ "Can't create ktrace file"
+ "DTProcessorTraceRecorder"
+ "DVTProcessorTraceRecorderConfiguration"
+ "Failed to decode processor trace config"
+ "Failed to init recording from live recording: %d"
+ "Failed to initialize hwtrace_live_topology."
+ "Failed to initialize recording: %d"
+ "Failed to pause processor trace recording: %@"
+ "Failed to pause recording. currentLiveRecording is nil."
+ "Failed to pause recording: %d"
+ "Failed to postprocess recording: %d"
+ "Failed to save recording: %d"
+ "Failed to save the recording"
+ "Failed to start processor trace recording: %@"
+ "Failed to start processor trace recording: previous session is still recording"
+ "Failed to start recording: %d"
+ "Failed to stop processor trace recording: %@"
+ "Failed to stop recording"
+ "Failed to stop recording: %d"
+ "Failed to transfer processor trace recording: %@"
+ "Failed to unpause processor trace recording: %@"
+ "Failed to unpause recording"
+ "Invalid file descriptor %d"
+ "ProcessorTraceService"
+ "Recording is not in configured state or is not initialized."
+ "Successfully saved recording to tracev3 file."
+ "System %s does not support Driver, falling back to AppleHWAccess."
+ "System %s does not support production mode."
+ "System %s does not support streaming mode, falling back to oneshot mode."
+ "TB,N,R"
+ "[Error] Interval already ended"
+ "com_apple_dt_instruments_dtsecurity.ProcessorTraceRecorder"
+ "com_apple_dt_instruments_dtsecurity.ProcessorTraceRecorderConfiguration"
+ "configuration"
+ "copyImagesOnSave"
+ "currentLiveRecording"
+ "dealloc"
+ "decodeObjectForKey:"
+ "decodeOnSave"
+ "fileURLWithPath:"
+ "init()"
+ "initWithConfiguration:"
+ "isDriverEnabled"
+ "isProductionModeEnabled"
+ "isRecording"
+ "isResumeAvailable"
+ "isThrottlingEnabled"
+ "logger"
+ "mainBundle"
+ "pause"
+ "pauseRecordingAndReturnError:"
+ "processIdentifier"
+ "processor_trace_config"
+ "processor_trace_file_fd"
+ "processor_trace_pause"
+ "processor_trace_resume_capability"
+ "processor_trace_start"
+ "processor_trace_stop"
+ "processor_trace_transfer"
+ "processor_trace_unpause"
+ "recordingMode"
+ "recordingModeRingBufferDefault"
+ "recordingModeRingBufferFilesystem"
+ "recordingModeRingBufferMemory"
+ "recordingModeStreaming"
+ "save"
+ "saveRecordingWithFd:error:"
+ "signposter"
+ "start"
+ "startRecordingAndReturnError:"
+ "state"
+ "stop"
+ "stopRecordingAndReturnError:"
+ "systems"
+ "target"
+ "unpause"
+ "unpauseRecordingAndReturnError:"
+ "unsignedLongLongValue"
- "URLWithString:"

```
