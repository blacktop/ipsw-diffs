## exclave_xnuproxy

> `exclave_xnuproxy`

```diff

-696.60.269.0.1
-  __TEXT.__text: 0x41310
-  __TEXT.__cstring: 0xda42
-  __TEXT.__const: 0x27500
+696.60.281.0.0
+  __TEXT.__text: 0x41b24
+  __TEXT.__cstring: 0xe05a
+  __TEXT.__const: 0x274c0
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __TEXT.__eh_frame: 0x48
   __DATA.__auth_ptr: 0x10
   __DATA.__mod_init_func: 0x18
-  __DATA.__const: 0x1c60
+  __DATA.__const: 0x1ca0
   __DATA.__ENDPOINTS: 0x9705
-  __DATA.__data: 0x2218
+  __DATA.__data: 0x2278
   __DATA.__shared_cache: 0x38
   __DATA.__thread_vars: 0x0
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__common: 0x1a60
-  __DATA.__bss: 0x4038
+  __DATA.__common: 0x1a50
+  __DATA.__bss: 0x4028
   __PDATA.__shared_cache: 0x0
   __PDATA.__mod_init_func: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 1121
+  Functions: 1136
   Symbols:   12
-  CStrings:  1187
+  CStrings:  1213
 
CStrings:
+ "!va_alloc->uncommitted_alloc"
+ "/AppleInternal/Library/BuildRoots/11914d60-911b-11ef-aa10-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/Library/Caches/com.apple.xbs/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/xnu-proxy.build/xnu-proxy.build/DerivedSources/ExclaveIndicatorController_C.c"
+ "<="
+ "CNode"
+ "Could not allocate for VAS private %!s(MISSING) range of %!l(MISSING)x bytes (%!s(MISSING))\n"
+ "DART_CNODE"
+ "EASM_CNODE"
+ "SHADOW_CNODE"
+ "TB_FATAL: Attempt to retrieve accumulator in environment without large message support (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from audioBufferCopyOut (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from audioBufferDelete (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from audioBufferLayout (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from audioBufferMap (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from getAddressSpaceInfo (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from getIPCStackEntry (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from namedBufferDelete (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from namedBufferLayout (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from namedBufferMap (%!s(MISSING):%!d(MISSING))\n"
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
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[40c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
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
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from audioBufferCopyOut\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from audioBufferDelete\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from audioBufferLayout\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from audioBufferMap\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getAddressSpaceInfo\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getIPCStackEntry\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from namedBufferDelete\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from namedBufferLayout\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from namedBufferMap\""
- "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "VAS_CNODE"
- "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]Could not allocate span for VAS private heap (%!s(MISSING))\n\n"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[32c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "_span_alloc"
- "nested"
- "vas span alloc failed on region of size %!z(MISSING)u with error code %!x(MISSING), error name %!s(MISSING), and detail %!d(MISSING)\n"
- "vas_core_heap_reserve_region"

```
