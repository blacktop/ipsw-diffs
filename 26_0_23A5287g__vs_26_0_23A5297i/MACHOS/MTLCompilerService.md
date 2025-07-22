## MTLCompilerService

> `/System/Library/Frameworks/Metal.framework/XPCServices/MTLCompilerService.xpc/MTLCompilerService`

```diff

-370.56.0.0.0
-  __TEXT.__text: 0x392c
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__gcc_except_tab: 0x22c
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x427
-  __TEXT.__oslogstring: 0x101
+370.57.0.0.0
+  __TEXT.__text: 0x42cc
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__gcc_except_tab: 0x2c8
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0x556
+  __TEXT.__oslogstring: 0x3d6
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x270
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0x98
+  __TEXT.__unwind_info: 0x298
+  __DATA_CONST.__auth_got: 0x348
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x30
-  __DATA.__bss: 0x530
+  __DATA.__bss: 0x598
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 55E80F27-100E-3E3D-837B-B0BDD5E06136
-  Functions: 104
-  Symbols:   740
-  CStrings:  60
+  UUID: 697D1CB9-0037-3674-99AF-C4D1A99459EE
+  Functions: 113
+  Symbols:   802
+  CStrings:  76
 
Symbols:
+ GCC_except_table10
+ GCC_except_table21
+ GCC_except_table23
+ GCC_except_table29
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table51
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _ZN18MTLCompilerService12errorHandlerEPU24objcproto13OS_xpc_object8NSObject.cold.1
+ _ZN18MTLCompilerService12errorHandlerEPU24objcproto13OS_xpc_object8NSObject.cold.2
+ _ZN18MTLCompilerService12errorHandlerEPU24objcproto13OS_xpc_object8NSObject.cold.3
+ _ZN18MTLCompilerService12errorHandlerEPU24objcproto13OS_xpc_object8NSObject.cold.4
+ __ZN18MTLCompilerService12errorHandlerEPU24objcproto13OS_xpc_object8NSObject
+ __ZN18MTLCompilerService34waitForAllActiveContextsToCompleteERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ ___ZN18MTLCompilerService12eventHandlerEPU24objcproto13OS_xpc_object8NSObject_block_invoke.cold.1
+ __os_log_impl
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ __xpc_error_termination_imminent
+ __xpc_type_dictionary
+ _pthread_cond_broadcast
+ _pthread_cond_destroy
+ _pthread_cond_init
+ _pthread_cond_wait
+ _pthread_mutex_destroy
+ _pthread_mutex_init
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
+ _xpc_copy_description
+ _xpc_type_get_name
- GCC_except_table20
- GCC_except_table27
- GCC_except_table34
- GCC_except_table36
- GCC_except_table41
- GCC_except_table48
- GCC_except_table49
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
CStrings:
+ "' - ensuring clean shutdown"
+ "' is invalid"
+ "' might have exited"
+ "' must terminate"
+ "(unable to get description)"
+ "MTLCompilerService: All active compilations have completed. Reason: %s"
+ "MTLCompilerService: Received unexpected XPC object type in event handler: %{public}s"
+ "MTLCompilerService: Received unknown XPC error type from client '%{public}s': %{public}s"
+ "MTLCompilerService: Waiting for %lld active compilations to complete. Reason: %s"
+ "MTLCompilerService: XPC_ERROR_CONNECTION_INTERRUPTED - Host app '%{public}s' might have exited, connection interrupted but still live"
+ "MTLCompilerService: XPC_ERROR_CONNECTION_INVALID - Connection to host app '%s' is invalid, could not establish XPC connection"
+ "MTLCompilerService: XPC_ERROR_TERMINATION_IMMINENT - Compiler service for client '%{public}s' must terminate, program termination imminent"
+ "Unknown XPC error from client '"
+ "XPC_ERROR_CONNECTION_INTERRUPTED - Host app '"
+ "XPC_ERROR_CONNECTION_INVALID - Connection to host app '"
+ "XPC_ERROR_TERMINATION_IMMINENT - Compiler service for client '"

```
