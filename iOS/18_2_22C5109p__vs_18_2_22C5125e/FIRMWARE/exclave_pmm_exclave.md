## exclave_pmm_exclave

> `exclave_pmm_exclave`

```diff

-696.60.269.0.1
-  __TEXT.__text: 0x30dc0
-  __TEXT.__const: 0x1c8c0
-  __TEXT.__cstring: 0xad12
+696.60.281.0.0
+  __TEXT.__text: 0x311e4
+  __TEXT.__const: 0x1c880
+  __TEXT.__cstring: 0xb3fd
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x18
   __DATA.__auth_ptr: 0x8
   __DATA.__mod_init_func: 0x18
-  __DATA.__const: 0xc20
-  __DATA.__data: 0x1829
+  __DATA.__const: 0xc30
+  __DATA.__data: 0x1889
   __DATA.__ENDPOINTS: 0x838
   __DATA.__shared_cache: 0x70
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x1042b0
-  __DATA.__common: 0x64f0
+  __DATA.__bss: 0x1042a0
+  __DATA.__common: 0x7348
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 877
+  Functions: 887
   Symbols:   10
-  CStrings:  1096
+  CStrings:  1122
 
CStrings:
+ "!va_alloc->uncommitted_alloc"
+ "/AppleInternal/Library/BuildRoots/11914d60-911b-11ef-aa10-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/Library/Caches/com.apple.xbs/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/pmm-server.build/pmm-server.build/DerivedSources/exclaves_upcalls_C.c"
+ "<="
+ "CNode"
+ "Client %!s(MISSING) exceeded memory limit of %!l(MISSING)lu bytes, currently using %!l(MISSING)lu bytes. Memory limits can be disabled with the boot-arg exclaves_xrt_runflags_global=disable_memory_limits\n"
+ "Could not allocate for VAS private %!s(MISSING) range of %!l(MISSING)x bytes (%!s(MISSING))\n"
+ "DART_CNODE"
+ "Decrementing a mem_stat_t by more than its current value\n"
+ "EASM_CNODE"
+ "SHADOW_CNODE"
+ "TB_FATAL: Attempt to retrieve accumulator in environment without large message support (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]Could not reserve VA for VAS private %!s(MISSING) range [%!l(MISSING)x, %!l(MISSING)x) (%!s(MISSING))\n\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]Used up entire initial [%!l(MISSING)x, %!l(MISSING)x) allocation for va_alloc %!p(MISSING)\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]addr not as expected; another alloc happened?\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]allocation point must be inside span\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]allocation point must be part of span\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] Couldn't sustain VAS object watermark: _alloc_va() failed\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] Couldn't sustain VAS object watermark: allocating frame failed\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] Couldn't sustain VAS object watermark: allocating page table\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] _alloc_va() with uncommitted allocation\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] _commit_alloc_va()/_undo_alloc_va() with no uncommitted allocation\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] heap reserve dropped with uncommitted allocation\n"
+ "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: (%!s(MISSING))] returning with uncommitted allocation\n"
+ "__span_alloc"
+ "_alloc_memory_frame"
+ "_alloc_va"
+ "_commit_alloc_va"
+ "data"
+ "heap->ensure_watermark_active"
+ "heap->heap_va.uncommitted_alloc || heap->cnode_va.uncommitted_alloc"
+ "va_alloc->uncommitted_alloc"
+ "vas_core_heap_alloc_span"
+ "xrt_init failed with %!d(MISSING)"
- "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "Client %!s(MISSING) exceeded memory limit of %!s(MISSING). You can disable memory limits  using the boot-arg exclaves_xrt_runflags_global=disable_memory_limits\n"
- "Decrementing a mem_stat_t but the stat is already 0\n"
- "VAS_CNODE"
- "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]Could not allocate span for VAS private heap (%!s(MISSING))\n\n"
- "_span_alloc"
- "nested"
- "vas span alloc failed on region of size %!z(MISSING)u with error code %!x(MISSING), error name %!s(MISSING), and detail %!d(MISSING)\n"
- "vas_core_heap_reserve_region"

```
