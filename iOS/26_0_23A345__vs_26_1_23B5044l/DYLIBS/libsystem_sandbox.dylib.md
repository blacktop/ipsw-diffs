## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

```diff

-2680.0.50.0.0
-  __TEXT.__text: 0x3598
-  __TEXT.__auth_stubs: 0x340
+2680.40.8.0.0
+  __TEXT.__text: 0x3698
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__const: 0x178
-  __TEXT.__cstring: 0x741
-  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__cstring: 0x747
+  __TEXT.__unwind_info: 0x1c0
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH_CONST.__const: 0x20
   __DATA.__data: 0x13
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__bss: 0x8
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: 76B3EB7B-A1EA-3E62-9325-0B99A3F6A1EB
-  Functions: 129
-  Symbols:   242
-  CStrings:  66
+  UUID: 7DF93BF7-7E8F-32EF-AD21-38C013989FAA
+  Functions: 131
+  Symbols:   251
+  CStrings:  67
 
Symbols:
+ _SANDBOX_STORAGE_CLASS_PROPERTY_ACCEPTS_USER_APPROVAL_block_invoke
+ __Block_copy
+ __Block_release
+ __NSConcreteGlobalBlock
+ ___block_descriptor_tmp
+ ___block_literal_global
+ _registered_state_flag_callback
+ _sandbox_register_erm_initialization_callback
CStrings:
+ "v8@?0"

```
