## libsystem_trace.dylib

> `/usr/lib/system/libsystem_trace.dylib`

```diff

-  __TEXT.__text: 0x1abb4
+  __TEXT.__text: 0x1ac0c
   __TEXT.__auth_stubs: 0x1140
   __TEXT.__delay_stubs: 0x180
   __TEXT.__delay_helper: 0xa4
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xf4
   __TEXT.__const: 0x2b5
-  __TEXT.__cstring: 0x1bf5
+  __TEXT.__cstring: 0x1c16
   __TEXT.__gcc_except_tab: 0x64
   __TEXT.__oslogstring: 0x137
   __TEXT.__unwind_info: 0x4f8

   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0xe4
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1d8
+  __DATA.__bss: 0x1e0
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x368
   __DATA_DIRTY.__bss: 0x2c8

   - /usr/lib/system/libsystem_symptoms.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 368
-  Symbols:   1085
-  CStrings:  487
+  Functions: 369
+  Symbols:   1087
+  CStrings:  488
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_nlclslist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __os_trace_preferences_cache_path
+ __os_trace_prefscachedir_path
Functions:
~ ____os_trace_paths_init_block_invoke : 84 -> 100
+ __os_trace_prefscachedir_path
CStrings:
+ "/private/var/db/diagnostics/logd"

```
