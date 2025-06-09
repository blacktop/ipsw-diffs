## libchannel.dylib

> `/usr/lib/libchannel.dylib`

```diff

-50.100.3.0.0
-  __TEXT.__text: 0x330c
+56.0.5.0.0
+  __TEXT.__text: 0x327c
   __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x2a0
+  __TEXT.__gcc_except_tab: 0x220
   __TEXT.__oslogstring: 0x1c7
-  __TEXT.__cstring: 0x157
-  __TEXT.__unwind_info: 0x288
+  __TEXT.__cstring: 0xdd
+  __TEXT.__unwind_info: 0x278
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methname: 0x1e
   __TEXT.__objc_methtype: 0x11

   __DATA_CONST.__objc_selrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x218
-  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__const: 0xf0
   __AUTH_CONST.__objc_const: 0x240
   __AUTH.__objc_data: 0x140
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: B6C8922E-FCAA-381D-8A6D-01F481005528
-  Functions: 140
-  Symbols:   390
-  CStrings:  28
+  UUID: 92408925-E2A1-31D8-89E4-7E188223299A
+  Functions: 143
+  Symbols:   392
+  CStrings:  25
 
Symbols:
+ GCC_except_table18
+ __ZN15DispatchChannel16dequeue_messagesEv
+ ____ZN15DispatchChannel17activate_no_checkEv_block_invoke
+ ___block_descriptor_40_ea8_32c50_ZTSKZN15DispatchChannel17activate_no_checkEvE3$_0_e5_v8?0l
+ ___block_descriptor_40_ea8_32c74_ZTSKZN15DispatchChannel19set_message_handlerEU13block_pointerFvPvmjEE3$_0_e5_v8?0l
+ ___copy_helper_block_ea8_32c50_ZTSKZN15DispatchChannel17activate_no_checkEvE3$_0
+ _dispatch_assert_queue$V2
+ _dispatch_async
- GCC_except_table1
- GCC_except_table15
- GCC_except_table16
- ___block_descriptor_48_ea8_32c74_ZTSKZN15DispatchChannel19set_message_handlerEU13block_pointerFvPvmjEE3$_0_e5_v8?0l
- ___destroy_helper_block_ea8_32c74_ZTSKZN15DispatchChannel19set_message_handlerEU13block_pointerFvPvmjEE3$_0
- _realtime_runtime_check_pop_authorization
- _realtime_runtime_check_push_authorization
CStrings:
- "mach_msg with timeout=0 is RT safe"
- "mach_port_mod_refs is RT safe here"
- "os_crash is not realtime_safe, but crashing is okay"

```
