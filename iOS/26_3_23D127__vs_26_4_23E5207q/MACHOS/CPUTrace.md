## CPUTrace

> `/System/Library/Trace/Providers/CPUTrace.bundle/CPUTrace`

```diff

-134.0.0.0.0
-  __TEXT.__text: 0x3f60
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_stubs: 0x5c0
+134.100.19.0.0
+  __TEXT.__text: 0x2b50
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_stubs: 0x640
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x270
-  __TEXT.__const: 0x51
-  __TEXT.__cstring: 0x73e
-  __TEXT.__objc_methname: 0x6d1
-  __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methtype: 0x206
-  __TEXT.__gcc_except_tab: 0x2dc
-  __TEXT.__unwind_info: 0x1f8
-  __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x160
-  __DATA_CONST.__cfstring: 0x740
+  __TEXT.__objc_methlist: 0x284
+  __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x8a6
+  __TEXT.__objc_methname: 0x738
+  __TEXT.__objc_classname: 0x42
+  __TEXT.__objc_methtype: 0x22e
+  __TEXT.__gcc_except_tab: 0x314
+  __TEXT.__unwind_info: 0x178
+  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x570
-  __DATA.__objc_selrefs: 0x1f8
-  __DATA.__objc_ivar: 0x54
+  __DATA_CONST.__objc_arraydata: 0x8
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0x5a8
+  __DATA.__objc_selrefs: 0x218
+  __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xd0
   __DATA.__bss: 0x24

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libhwtrace.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4353A62F-5B55-356C-A858-BF08BCCE4B68
-  Functions: 88
-  Symbols:   179
-  CStrings:  254
+  UUID: 04AB6352-9EE2-3023-833A-A79092A7B2D3
+  Functions: 56
+  Symbols:   162
+  CStrings:  269
 
Symbols:
+ _CPUTraceProviderOptionCPMU
+ _OBJC_CLASS_$_NSArray
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _ats_configure_postprocessing_with_additional_address_range
+ _hwtrace_live_recording_system_options_set_cpmu_capture
+ _hwtrace_live_recording_system_options_set_trace_buffer_size
+ _hwtrace_segment_used_iter
+ _hwtrace_task_segments_iter
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x8
- __Block_object_dispose
- __ZNSt11logic_errorC2EPKc
- __ZNSt12length_errorD1Ev
- __ZNSt20bad_array_new_lengthC1Ev
- __ZNSt20bad_array_new_lengthD1Ev
- __ZNSt3__112__next_primeEm
- __ZNSt3__119piecewise_constructE
- __ZTISt12length_error
- __ZTISt20bad_array_new_length
- __ZTVSt12length_error
- __ZdlPv
- ___cxa_allocate_exception
- ___cxa_end_catch
- ___cxa_free_exception
- ___cxa_rethrow
- ___cxa_throw
- _ats_configure_postprocessing_with_additional_address
- _dispatch_apply
- _hwtrace_cursor_deinit
- _hwtrace_cursor_init_from_thread
- _hwtrace_cursor_next_range
- _hwtrace_cursor_pc
- _hwtrace_cursor_segment
- _hwtrace_task_threads
- _hwtrace_thread_task
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x23
CStrings:
+ "%s not configured."
+ "%s not paused."
+ "%s not started."
+ "%s not stopped."
+ ")"
+ "/AppleInternal/Library/BuildRoots/4~CHpougDu7mHTwVcZzb67Fpcb9mN9T4C0zAoKTMQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "B32@0:8^{ktrace_target_process=i}16^@24"
+ "CPMU counter collection is not supported for system: %@."
+ "CPUTrace"
+ "Could not set trace buffer size."
+ "Driver is not supported for system: %@, falling back to legacy mode."
+ "Invalid %s configuration. %@"
+ "None"
+ "Production trace (prod=1) requires a non-zero process-id"
+ "Saving %s..."
+ "T@\"NSNumber\",R,&,V_prod"
+ "TB,R,V_cpmu"
+ "Unable to save %s."
+ "_cpmu"
+ "arrayWithObjects:count:"
+ "cpmu"
+ "isEqualToString:"
+ "shouldTargetProcess:error:"
- "("
- "AppleProcessorTrace Driver is not supported for system: %@, falling back to AppleHWAccess."
- "CPUTrace not configured."
- "CPUTrace not paused."
- "CPUTrace not started."
- "CPUTrace not stopped."
- "Invalid CPUTrace configuration. %@"
- "Saving CPUTrace..."
- "TB,R,V_prod"
- "Unable to save CPUTrace."
- "decode-compression requires decode to be enabled"
- "v16@?0Q8"
- "vector"

```
