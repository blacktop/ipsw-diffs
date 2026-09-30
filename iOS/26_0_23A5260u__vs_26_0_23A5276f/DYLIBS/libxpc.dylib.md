## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-3070.0.0.0.2
-  __TEXT.__text: 0x3bccc
-  __TEXT.__auth_stubs: 0x11e0
-  __TEXT.__objc_methlist: 0x35c
-  __TEXT.__const: 0x620
-  __TEXT.__cstring: 0x7672
+3088.0.0.0.0
+  __TEXT.__text: 0x3c014
+  __TEXT.__auth_stubs: 0x1210
+  __TEXT.__objc_methlist: 0x374
+  __TEXT.__const: 0x610
+  __TEXT.__cstring: 0x7677
   __TEXT.__oslogstring: 0x1668
   __TEXT.__dof_libxpc: 0xa5d
-  __TEXT.__unwind_info: 0x1168
+  __TEXT.__unwind_info: 0x1190
   __TEXT.__objc_classname: 0x243
   __TEXT.__objc_methname: 0x1e2
   __TEXT.__objc_methtype: 0xb5
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x1be0
+  __DATA_CONST.__const: 0x1c40
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_nlclslist: 0xe8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x8f8
+  __AUTH_CONST.__auth_got: 0x910
   __AUTH_CONST.__const: 0x1b18
   __AUTH_CONST.__objc_const: 0x2338
   __AUTH.__objc_data: 0x50

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: D972AD1B-9BF1-33EF-B521-81546D27EB3D
-  Functions: 1781
-  Symbols:   4461
-  CStrings:  1239
+  UUID: 12CCAC98-7B44-3926-8BE3-D019C60E6B93
+  Functions: 1791
+  Symbols:   4487
+  CStrings:  1240
 
Symbols:
+ -[OS_os_transaction _xref_dispose]
+ -[OS_os_transaction release]
+ ____xpc_bootout_wait_for_completion_block_invoke
+ ____xpc_bootout_wait_for_completion_block_invoke_2
+ ____xpc_bootout_wait_for_completion_sync_block_invoke
+ ___block_descriptor_tmp.18
+ __os_transaction_xref_dispose
+ __transaction_snapshot_destroy
+ __transaction_snapshot_new_locked
+ __transaction_snapshot_new_locked.cold.1
+ __xpc_bootout_wait_for_completion_sync
+ __xpc_token_satisfies_lwcr.cold.2
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _launch_bootout_user_service_4coresim_with_flags
+ _os_transaction_log_active
- ___block_descriptor_tmp.46
- __os_transaction_log_active.cold.2
- __xpc_os_transaction_dispose
CStrings:
+ "[%p] Connection returned listener port: 0x%x"
+ "wait"
- "[%p] Channel could not return listener port."

```
