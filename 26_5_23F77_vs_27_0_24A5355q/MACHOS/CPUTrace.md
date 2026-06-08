## CPUTrace

> `/System/Library/Trace/Providers/CPUTrace.bundle/CPUTrace`

```diff

-134.120.2.0.0
-  __TEXT.__text: 0x2b34
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_stubs: 0x640
+188.0.0.0.0
+  __TEXT.__text: 0x90ec
+  __TEXT.__auth_stubs: 0xf30
+  __TEXT.__objc_stubs: 0xbc0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x284
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x763
-  __TEXT.__objc_methname: 0x738
-  __TEXT.__objc_classname: 0x42
-  __TEXT.__objc_methtype: 0x22e
-  __TEXT.__gcc_except_tab: 0x314
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x3b0
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x140
-  __DATA_CONST.__cfstring: 0x7c0
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x8
+  __TEXT.__objc_methlist: 0x51c
+  __TEXT.__const: 0x162
+  __TEXT.__cstring: 0xc32
+  __TEXT.__objc_methname: 0xe1b
+  __TEXT.__objc_classname: 0xe1
+  __TEXT.__objc_methtype: 0x3e4
+  __TEXT.__gcc_except_tab: 0x550
+  __TEXT.__swift5_typeref: 0x100
+  __TEXT.__swift5_capture: 0x60
+  __TEXT.__constg_swiftt: 0x138
+  __TEXT.__swift5_reflstr: 0x68
+  __TEXT.__swift5_fieldmd: 0x80
+  __TEXT.__oslogstring: 0x45
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0x14
+  __TEXT.__unwind_info: 0x318
+  __TEXT.__eh_frame: 0x1a8
+  __DATA_CONST.__const: 0x2d8
+  __DATA_CONST.__cfstring: 0xc20
+  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x5a8
-  __DATA.__objc_selrefs: 0x218
-  __DATA.__objc_ivar: 0x58
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xd0
-  __DATA.__bss: 0x24
+  __DATA_CONST.__auth_got: 0x7a8
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_ptr: 0x50
+  __DATA.__objc_const: 0xc48
+  __DATA.__objc_selrefs: 0x420
+  __DATA.__objc_ivar: 0xa0
+  __DATA.__objc_data: 0x248
+  __DATA.__data: 0x2f0
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication
+  - /System/Library/PrivateFrameworks/StreamingAppleTrace.framework/StreamingAppleTrace
   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libhwtrace.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3A7BB09-0704-33BF-83AF-1749753BA213
-  Functions: 56
-  Symbols:   161
-  CStrings:  268
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 565945C6-3728-3B89-A111-E184C8CC6CE1
+  Functions: 161
+  Symbols:   269
+  CStrings:  473
 
Symbols:
+ _CPUTraceProviderOptionEnergy
+ _CPUTraceProviderOptionSAT
+ _CPUTraceProviderOptionSample
+ _CPUTraceProviderOptionSideload
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_CPUTraceSampler
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSOutputStream
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$__TtC8CPUTrace17CPUTraceSATBridge
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$_CPUTraceSampler
+ _OBJC_METACLASS_$__TtC8CPUTrace17CPUTraceSATBridge
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ ___NSArray0__struct
+ ___chkstk_darwin
+ __dispatch_source_type_timer
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_stdlib_reportUnimplementedInitializer
+ _bzero
+ _clock_gettime_nsec_np
+ _dispatch_after
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_resume
+ _dispatch_semaphore_create
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_sync
+ _dispatch_time
+ _hwtrace_cluster_set_raw_trace_path
+ _hwtrace_live_recording_options_set_image_override
+ _hwtrace_live_recording_resume
+ _hwtrace_live_recording_system_options_set_energy_capture
+ _hwtrace_recording_topology
+ _hwtrace_system_clusters
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_self
+ _objc_release_x1
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_storeWeak
+ _os_log_type_enabled
+ _swift_allocObject
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain
+ _swift_retain_n
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
- _objc_retain_x24
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "#16@0:8"
+ "%.1fms"
+ "%.1fs"
+ "%.1fus"
+ "%lluns"
+ ".cxx_construct"
+ "/"
+ "1"
+ "@\"<CPUTraceSamplerDelegate>\""
+ "@\"CPUTraceSampler\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"NSString\"16@0:8"
+ "@\"_TtC8CPUTrace17CPUTraceSATBridge\""
+ "@24@0:8:16"
+ "@24@0:8@16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "@40@0:8Q16Q24@32"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"CPUTraceSampler\"16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "CIO streaming is not supported for system: %@, falling back to oneshot mode."
+ "CPMU capture disabled for system %@."
+ "CPUTrace sampling plan: %@ captured per %@"
+ "CPUTrace.CPUTraceSATBridge"
+ "CPUTraceSampler"
+ "CPUTraceSamplerDelegate"
+ "Empty time duration string"
+ "Energy capture disabled for system: %@."
+ "Error creating directory %@: %@."
+ "Failed to create sampling timer"
+ "Failed to pause during sampling"
+ "Failed to resume during sampling"
+ "Got %ld bytes for %s"
+ "Invalid sample configuration \"%@\": duration must be less than period"
+ "Invalid sample duration in \"%@\": %@"
+ "Invalid sample format \"%@\": expected \"duration/period\" (e.g., \"10ms/1s\")"
+ "Invalid sample period in \"%@\": %@"
+ "Invalid time duration \"%@\": negative value not allowed"
+ "Invalid time duration \"%@\": no numeric value found"
+ "Invalid time duration \"%@\": unknown suffix \"%@\" (expected: ns, us, ms, s)"
+ "Invalid time duration \"%@\": value too large (max: %llu%@)"
+ "NSObject"
+ "No StreamingAppleTrace ProviderSession"
+ "Options 'sample' and 'rate-limit' are mutually exclusive"
+ "Q"
+ "Q16@0:8"
+ "Sampling timer cancelled due to size limit"
+ "Set SAT raw trace path for system %@: %@"
+ "StreamingAppleTrace"
+ "System %@ does not have a local SAT path."
+ "System %@ has %zu clusters. Not adding SAT raw trace."
+ "T#,R"
+ "T@\"NSArray\",R,&,V_sideloadPaths"
+ "T@\"NSNumber\",R,&,V_sampleDuration"
+ "T@\"NSNumber\",R,&,V_samplePeriod"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TB,R,N,V_isRecordingActive"
+ "TB,R,V_energy"
+ "TB,R,V_sat"
+ "TQ,R"
+ "TQ,R,N,V_sampleCount"
+ "URLByAppendingPathComponent:"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_TtC8CPUTrace17CPUTraceSATBridge"
+ "_TtC8CPUTraceP33_8CF6C84CE721173ED40DDA3E9A7AE08620BufferedOutputStream"
+ "_delegate"
+ "_durationNs"
+ "_energy"
+ "_handleTimerFire"
+ "_isRecordingActive"
+ "_lastResumeTimeNs"
+ "_periodNs"
+ "_queue"
+ "_recordingMutex"
+ "_resumeIfNeeded"
+ "_sampleCount"
+ "_sampleDuration"
+ "_samplePeriod"
+ "_sampler"
+ "_sat"
+ "_satBridge"
+ "_sideloadPaths"
+ "_timer"
+ "_totalSamplingTimeNs"
+ "autorelease"
+ "buffer"
+ "class"
+ "close"
+ "com.apple.CPUTraceProvider.sampling"
+ "com.apple.TracingSupport.CPUTrace"
+ "completionSemaphore"
+ "conformsToProtocol:"
+ "countByEnumeratingWithState:objects:count:"
+ "cputrace-sat"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "debugDescription"
+ "defaultManager"
+ "description"
+ "energy"
+ "filePathWithSystemName:"
+ "fileURLWithPath:"
+ "finalizeCurrentSample"
+ "flushThreshold"
+ "hash"
+ "informWithMessage:"
+ "init()"
+ "initWithDuration:period:logger:"
+ "initWithTemporaryDirectory:"
+ "initWithURL:append:"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "isRecordingActive"
+ "length"
+ "localizedFailureReason"
+ "log"
+ "lowercaseString"
+ "ms"
+ "ns"
+ "numberWithUnsignedLongLong:"
+ "objectAtIndexedSubscript:"
+ "open"
+ "outputStreams"
+ "path"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "release"
+ "removeItemAtURL:error:"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "s"
+ "sample"
+ "sampleCount"
+ "sampleDuration"
+ "samplePeriod"
+ "samplerPauseRecording:"
+ "samplerResumeRecording:"
+ "samplerShouldContinue:"
+ "sat"
+ "scanDouble:"
+ "scanLocation"
+ "scannerWithString:"
+ "self"
+ "sideload"
+ "sideloadPaths"
+ "startListening"
+ "startWithDelegate:"
+ "stop"
+ "string"
+ "stringByTrimmingCharactersInSet:"
+ "substringFromIndex:"
+ "superclass"
+ "tempFiles"
+ "temporaryDirectory"
+ "us"
+ "v24@0:8@16"
+ "waitForCompletion"
+ "whitespaceCharacterSet"
+ "write:maxLength:"
+ "zone"
+ "{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
- ")"
- "CPMU counter collection is not supported for system: %@."

```
