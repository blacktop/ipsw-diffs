## com.apple.dt.instruments.dtsecurity

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity`

```diff

-64570.80.2.1.0
-  __TEXT.__text: 0x13d94
-  __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_stubs: 0x1200
+64572.171.1.0.0
+  __TEXT.__text: 0x118c4
+  __TEXT.__auth_stubs: 0x1690
+  __TEXT.__objc_stubs: 0x1100
   __TEXT.__objc_methlist: 0x540
-  __TEXT.__const: 0x452
-  __TEXT.__oslogstring: 0x132c
-  __TEXT.__cstring: 0x1346
+  __TEXT.__const: 0x472
+  __TEXT.__oslogstring: 0x125c
+  __TEXT.__cstring: 0x1306
   __TEXT.__objc_classname: 0x112
   __TEXT.__objc_methtype: 0x29d
   __TEXT.__gcc_except_tab: 0x42c
-  __TEXT.__objc_methname: 0x110a
+  __TEXT.__objc_methname: 0x110f
   __TEXT.__constg_swiftt: 0x140
   __TEXT.__swift5_typeref: 0xa0
   __TEXT.__swift5_reflstr: 0x2c4

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__unwind_info: 0x520
   __TEXT.__eh_frame: 0x160
-  __DATA_CONST.__auth_got: 0xb40
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__auth_ptr: 0xd8
-  __DATA_CONST.__const: 0xe50
-  __DATA_CONST.__cfstring: 0x880
+  __DATA_CONST.__auth_got: 0xb60
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_ptr: 0xd0
+  __DATA_CONST.__const: 0xeb8
+  __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA.__objc_const: 0xde0
+  __DATA.__objc_const: 0xdf8
   __DATA.__objc_selrefs: 0x550
   __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0x508
-  __DATA.__data: 0x2d0
-  __DATA.__common: 0x20
+  __DATA.__data: 0x280
   __DATA.__bss: 0x4d0
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
+  - /usr/lib/libhwtrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  - /usr/local/lib/libhwtrace_private.dylib
-  UUID: 1ADE1BF7-C6B0-3B6E-AC42-F3AFE7D9DA3F
-  Functions: 380
+  UUID: 68373A46-7004-359F-A2E7-ACD96FA32AA5
+  Functions: 369
   Symbols:   451
-  CStrings:  650
+  CStrings:  648
 
Symbols:
+ _DTProcessControlServiceOption_PreferredCPUSubType
+ _DTProcessControlServiceOption_PreferredCPUType
+ _DTProcessControlServiceOption_SkipSetPath
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _dlclose
+ _dlopen
+ _dlsym
+ _hwtrace_recording_save_options_set_decode_compression
+ _hwtrace_version_info
+ _xpc_service_instance_set_archpref_shim
+ _xpc_service_instance_set_binpref
- _DTProcessControlServiceOption_CaptureOutputKey
- __Znwm
- ___NSDictionary0__struct
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _hwtrace_live_recording_resume_wrapper
- _is_resume_available
- _processorTraceRecorder
- _swift_bridgeObjectRelease_n
CStrings:
+ "/usr/lib/system/libxpc.dylib"
+ "CPUSubType"
+ "CPUType"
+ "DTXPCServiceController: daemon launch instance path = %@"
+ "DTXPCServiceController: daemon launch instance path unchanged"
+ "Failed to append provider '%{public}@', to a session"
+ "LZ4"
+ "Provider failed: %{public}@"
+ "Provider warning: %{public}@"
+ "SkipSetPath"
+ "T@\"NSString\",N,R"
+ "recordingVersionString"
+ "xpc_service_instance_set_archpref"
- "Failed to append provider '%@', to a session"
- "Failed to decode processor trace config"
- "Failed to pause processor trace recording: %@"
- "Failed to start processor trace recording: %@"
- "Failed to start processor trace recording: previous session is still recording"
- "Failed to stop processor trace recording: %@"
- "Failed to transfer processor trace recording: %@"
- "Failed to unpause processor trace recording: %@"
- "Provider failed: %@"
- "Provider warning: %@"
- "isResumeAvailable"
- "processor_trace_config"
- "processor_trace_file_fd"
- "processor_trace_pause"
- "processor_trace_resume_capability"
- "processor_trace_start"
- "processor_trace_stop"
- "processor_trace_transfer"
- "processor_trace_unpause"

```
