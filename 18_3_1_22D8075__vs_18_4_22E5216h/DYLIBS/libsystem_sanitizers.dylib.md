## libsystem_sanitizers.dylib

> `/usr/lib/system/libsystem_sanitizers.dylib`

```diff

-17.1.0.0.0
-  __TEXT.__text: 0x3d04
+18.2.0.0.0
+  __TEXT.__text: 0x3fd0
   __TEXT.__auth_stubs: 0x190
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x8e6
-  __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__got: 0x28
+  __TEXT.__cstring: 0xa42
+  __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x90
   __AUTH_CONST.__auth_got: 0xc8
   __AUTH_CONST.__const: 0xb8
-  __DATA.__bss: 0x528
+  __DATA.__bss: 0x530
   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x30
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  Functions: 178
-  Symbols:   217
-  CStrings:  119
+  Functions: 186
+  Symbols:   227
+  CStrings:  129
 
Symbols:
+ _sanitizers_testonly_diagnose_error
+ _sanitizers_testonly_get_shadow_address
CStrings:
+ "__asan_abi_stack_free_n"
+ "__asan_abi_stack_malloc_always_n"
+ "__asan_abi_stack_malloc_n"
+ "allocationBegin <= access.address && access.address < allocationEnd"
+ "compiler_abi.cpp"
+ "frameDescription != __null"
+ "frame_header.magicConstant != kRetiredStackFrameMagic"
+ "n >= sizeof(__asan_abi_frame_header) + sizeof(uintptr_t)"
+ "size >= sizeof(__asan_abi_frame_header) + sizeof(uintptr_t)"
+ "stack-use-after-return"
+ "stack-use-after-scope"
- "allocation <= access.address && access.address < allocationEnd"

```
