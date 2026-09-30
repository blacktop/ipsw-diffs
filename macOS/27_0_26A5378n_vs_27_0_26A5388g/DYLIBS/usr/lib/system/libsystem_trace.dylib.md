## libsystem_trace.dylib

> `/usr/lib/system/libsystem_trace.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1965.0.0.0.0
-  __TEXT.__text: 0x1bcf8
+1966.0.6.0.0
+  __TEXT.__text: 0x1bda0
   __TEXT.__delay_stubs: 0x180
   __TEXT.__delay_helper: 0xa4
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xf4
   __TEXT.__const: 0x2c0
-  __TEXT.__cstring: 0x1cd9
+  __TEXT.__cstring: 0x1cfa
   __TEXT.__gcc_except_tab: 0x68
   __TEXT.__oslogstring: 0x137
   __TEXT.__unwind_info: 0x528

   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0xe4
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x230
+  __DATA.__bss: 0x238
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x368
   __DATA_DIRTY.__bss: 0x2d0

   - /usr/lib/system/libsystem_symptoms.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 392
-  Symbols:   915
-  CStrings:  427
+  Functions: 394
+  Symbols:   918
+  CStrings:  428
 
Symbols:
+ __os_trace_preferences_cache_path
+ __os_trace_prefscachedir_path
+ __os_trace_set_prefscachedir_path
Functions:
~ ____os_trace_paths_init_block_invoke : 84 -> 100
+ __os_trace_prefscachedir_path
+ __os_trace_set_prefscachedir_path
CStrings:
+ "/private/var/db/diagnostics/logd"
```
