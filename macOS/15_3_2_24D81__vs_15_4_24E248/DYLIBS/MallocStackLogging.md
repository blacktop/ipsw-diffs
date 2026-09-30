## MallocStackLogging

> `/System/Library/PrivateFrameworks/MallocStackLogging.framework/Versions/A/MallocStackLogging`

```diff

-64567.3.3.0.0
-  __TEXT.__text: 0x9138
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x1f4c
+64570.58.1.0.0
+  __TEXT.__text: 0x9160
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__const: 0x120
+  __TEXT.__cstring: 0x1f73
   __TEXT.__unwind_info: 0x280
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0x90
   __AUTH.__data: 0x88
   __DATA.__data: 0x8

   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_blocks.dylib
   - /usr/lib/system/libsystem_c.dylib
+  - /usr/lib/system/libsystem_darwin.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
-  UUID: 05EF3C0E-574F-3F1B-8A57-046AF3E4E177
-  Functions: 230
-  Symbols:   401
-  CStrings:  206
+  UUID: B37A893B-F4B8-3900-BB25-2440357E0763
+  Functions: 234
+  Symbols:   408
+  CStrings:  208
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _os_variant_has_internal_diagnostics
+ _sld_allocate_pages_no_footprint
+ sld_allocate_pages_no_footprint.alreadyLoggedOnce
+ sld_allocate_pages_no_footprint.alreadyLoggedOnce.4
+ sld_allocate_pages_no_footprint.alreadyLoggedOnce.6
+ uniquing_table_node_release_internal.cold.2
+ uniquing_table_node_release_internal.cold.3
+ uniquing_table_node_release_internal.cold.4
+ uniquing_table_stack_retain_internal.cold.16
- _sld_allocate_pages_no_footprint.alreadyLoggedOnce
- _sld_allocate_pages_no_footprint.alreadyLoggedOnce.5
- _sld_allocate_pages_no_footprint.alreadyLoggedOnce.7
CStrings:
+ "collisions < 0"
+ "com.apple.Symbolication"

```
