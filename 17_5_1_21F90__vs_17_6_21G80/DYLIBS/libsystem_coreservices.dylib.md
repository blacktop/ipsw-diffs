## libsystem_coreservices.dylib

> `/usr/lib/system/libsystem_coreservices.dylib`

```diff

-152.5.1.0.0
-  __TEXT.__text: 0x1840
-  __TEXT.__auth_stubs: 0x280
+152.5.2.0.0
+  __TEXT.__text: 0x1af0
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x2eb
-  __TEXT.__oslogstring: 0x140
-  __TEXT.__unwind_info: 0xb0
+  __TEXT.__cstring: 0x315
+  __TEXT.__oslogstring: 0x214
+  __TEXT.__unwind_info: 0xac
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x908
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__auth_got: 0x140
-  __DATA.__bss: 0x818
+  __DATA_CONST.__const: 0x928
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__auth_got: 0x148
+  __DATA.__bss: 0x820
   __DATA_DIRTY.__bss: 0x20
   __DATA_DIRTY.__common: 0x88
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 66704D42-86C0-35B8-8CCA-1683E397FC93
-  Functions: 29
-  Symbols:   139
-  CStrings:  55
+  UUID: DA0E1F74-2B70-3877-BAAD-08329CE7017E
+  Functions: 34
+  Symbols:   153
+  CStrings:  59
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ ____dirhelper_relative_internal_block_invoke.22
+ ___block_descriptor_tmp.18
+ ___block_descriptor_tmp.23
+ ___block_descriptor_tmp.8
+ ___block_literal_global.10
+ ___block_literal_global.20
+ ___block_literal_global.25
+ ___makeDirectory.cold.2
+ __dirhelper_relative_internal.cold.2
+ __dirhelper_relative_internal.onceToken.21
+ __os_log_debug_impl
- ___block_descriptor_tmp.12
- ___block_literal_global.14
CStrings:
+ "%s: error for relativepath %s: %{errno}d"
+ "%s: no result for relativepath %s, err=%{errno}d"
+ "%s: this process is sandboxed so will never return /var/tmp/ or /var/mobile/tmp. This message is only logged once per process."
+ "__makeDirectory: created %s"
+ "_dirhelper_relative_internal_block_invoke"
- "%s: error for path %s: %{errno}d"

```
