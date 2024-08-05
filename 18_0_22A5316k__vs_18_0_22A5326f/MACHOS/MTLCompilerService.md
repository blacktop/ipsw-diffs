## MTLCompilerService

> `/System/Library/Frameworks/Metal.framework/XPCServices/MTLCompilerService.xpc/MTLCompilerService`

```diff

-366.14.0.0.0
-  __TEXT.__text: 0x1870
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__const: 0x18
+366.20.0.0.0
+  __TEXT.__text: 0x1b04
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__cstring: 0x35b
-  __TEXT.__oslogstring: 0x71
+  __TEXT.__cstring: 0x37c
+  __TEXT.__oslogstring: 0xfe
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x150
-  __DATA_CONST.__auth_got: 0x248
+  __TEXT.__unwind_info: 0x160
+  __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x38
   __DATA.__common: 0x8
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 43
-  Symbols:   359
-  CStrings:  43
+  Functions: 47
+  Symbols:   391
+  CStrings:  47
 
Symbols:
+ GCC_except_table12
+ GCC_except_table16
+ GCC_except_table20
+ GCC_except_table22
+ GCC_except_table27
+ GCC_except_table31
+ GCC_except_table36
+ GCC_except_table40
+ GCC_except_table41
+ _ZL15idle_timer_initv.cold.1
+ _ZL15idle_timer_initv.cold.1
+ __Exit
+ __ZL12g_idle_timer
+ __ZL12g_idle_timer
+ __ZL15idle_timer_exitPv
+ __ZL15idle_timer_exitPv
+ __ZL15idle_timer_initv
+ __ZL15idle_timer_initv
+ __ZL16idle_timer_resetv
+ __ZL16idle_timer_resetv
+ __ZL19g_idle_timer_reason
+ __ZL19g_idle_timer_reason
+ __ZL20g_idle_timer_seconds
+ __ZL20g_idle_timer_seconds
+ __block_literal_global.31
+ __block_literal_global.31
+ __block_literal_global.7
+ __block_literal_global.7
+ __os_log_impl
+ _atoll
+ _dispatch_resume
+ _dispatch_source_set_event_handler_f
+ _dispatch_suspend
- GCC_except_table13
- GCC_except_table17
- GCC_except_table19
- GCC_except_table21
- GCC_except_table28
- GCC_except_table33
- GCC_except_table37
- GCC_except_table38
- GCC_except_table9
- __block_literal_global.29
- __block_literal_global.29
- __block_literal_global.5
- __block_literal_global.5
CStrings:
+ "EV"
+ "Idle exit MTLCompilerService after %!{(MISSING)public}lld seconds (reason: %!{(MISSING)public}s)."
+ "MTL_IDLE_EXIT_TIMEOUT_SECONDS"
+ "Unable to create idle timer, idle exit %!{(MISSING)public}s is disabled."

```
