## StackshotDelegateComponent

> `/System/ExclaveKit/System/Library/Frameworks/StackshotDelegateComponent.framework/StackshotDelegateComponent`

```diff

-22.0.2.0.0
-  __TEXT.__text: 0x4ea4
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x1145
-  __TEXT.__unwind_info: 0x190
-  __DATA.__auth_got: 0x148
-  __DATA.__got: 0x18
+26.60.20.0.0
+  __TEXT.__text: 0x4b34
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0xfdc
+  __TEXT.__unwind_info: 0x170
+  __DATA.__auth_got: 0x130
+  __DATA.__got: 0x10
   __DATA.__auth_ptr: 0x8
   __DATA.__const: 0x5e0
   __DATA.__data: 0xe0

   __DATA.__common: 0x150
   - /System/ExclaveKit/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/ExclaveKit/usr/lib/libSystem.dylib
-  Functions: 124
-  Symbols:   238
-  CStrings:  49
+  Functions: 117
+  Symbols:   228
+  CStrings:  43
 
Symbols:
+ __Block_release
+ __asid__v_encode_block_invoke.97
+ __block_descriptor_tmp.12
+ __block_descriptor_tmp.93
+ __block_descriptor_tmp.96
+ __block_descriptor_tmp.98
+ __decodeStackshotDelegateComponent2_block_invoke.78.cold.1
+ _tb_message_configure_received
+ _xrt__thread_frame
+ _xrt__thread_state
- __ZL8snprintfPcU25pass_dynamic_object_size1mPKcz
- ___vsnprintf_chk
- __asid__v_encode_block_invoke.101
- __block_descriptor_tmp.10
- __block_descriptor_tmp.100
- __block_descriptor_tmp.102
- __block_descriptor_tmp.97
- __decodeStackshotDelegateComponent2_block_invoke.cold.1
- _cl4_error_name
- _fprintf
- _fputc
- _stderr
- _tb_message_configure_recieved
- _vfprintf
- _xrt__log_format
- _xrt__panic
- _xrt__thread_cap
- _xrt_process_panicv
- get_thread_info.cold.1
- get_thread_info.cold.2
CStrings:
- "%!s(MISSING)(%!z(MISSING)u): "
- "L4_ErrorCode#%!z(MISSING)u"
- "Unexpected L4_Error: %!s(MISSING)(%!z(MISSING)u) err='L4_Ec_GetState( xrt__thread_cap(thread), L4_Arm64_Context_PC, (((L4_StateMask_t) 1) << ((L4_Arm64_Context_PC) - (L4_Arm64_Context_PC))) )'"
- "Unexpected L4_Error: %!s(MISSING)(%!z(MISSING)u) err='L4_Ec_QueryState( xrt__thread_cap(thread), &state, &next_ecid, ((void *)0), ((void *)0), &next_asid )'"
- "[%!s(MISSING)] (%!s(MISSING)[%!d(MISSING)]: %!s(MISSING)): "
- "xrt"

```
