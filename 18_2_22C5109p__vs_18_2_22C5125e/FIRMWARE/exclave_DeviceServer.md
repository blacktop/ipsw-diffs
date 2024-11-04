## exclave_DeviceServer

> `exclave_DeviceServer`

```diff

 402.60.12.0.0
-  __TEXT.__text: 0x35a6cc
+  __TEXT.__text: 0x35a444
   __TEXT.__lcxx_override: 0x204
-  __TEXT.__const: 0xd0b80
-  __TEXT.__cstring: 0x1ef26
+  __TEXT.__const: 0xd0b40
+  __TEXT.__cstring: 0x1ee46
   __TEXT.__swift5_typeref: 0x565c
   __TEXT.__swift5_capture: 0x33c
   __TEXT.__swift5_entry: 0x8

   __TEXT.__eh_frame: 0xfe98
   __DATA.__auth_ptr: 0x50
   __DATA.__mod_init_func: 0x48
-  __DATA.__const: 0x18908
+  __DATA.__const: 0x18928
   __DATA.__objc_imageinfo: 0x8
   __DATA.__DARTS: 0x41c
   __DATA.__MMIOREGS: 0x287
   __DATA.__ENDPOINTS: 0x838
-  __DATA.__data: 0x3b70
+  __DATA.__data: 0x3bd0
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x38
   __DATA.__thread_vars: 0x60

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__common: 0x2790
+  __DATA.__common: 0x2768
   __DATA.__bss: 0x4e30
   __PDATA.__shared_cache: 0x0
   __PDATA.__mod_init_func: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 12221
+  Functions: 12231
   Symbols:   103
-  CStrings:  3691
+  CStrings:  3695
 
CStrings:
+ "!va_alloc->uncommitted_alloc"
+ "/AppleInternal/Library/BuildRoots/11914d60-911b-11ef-aa10-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "<="
+ "CNode"
+ "Could not allocate for VAS private %!s(MISSING) range of %!l(MISSING)x bytes (%!s(MISSING))\n"
+ "DART_CNODE"
+ "EASM_CNODE"
+ "Prespecializations library: Disabling, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED = %!d(MISSING)\n"
+ "SHADOW_CNODE"
+ "TB_FATAL: Attempt to retrieve accumulator in environment without large message support (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from getAddressSpaceInfo (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from getIPCStackEntry (%!s(MISSING):%!d(MISSING))\n"
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
- "(address__v_decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: StackshotTypes.Address (aka. UInt64)\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getAddressSpaceInfo\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getIPCStackEntry\""
- "(stackshotdelegate_helperfailure__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: StackshotDelegate.HelperFailure\""
- "(stackshottypes_addressspaceinfo__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: StackshotTypes.AddressSpaceInfo\""
- "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.2.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "Disabling metadata, SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_METADATA is false."
- "Prespecializations library: %!s(MISSING)\n"
- "Prespecializations library: Data at %!p(MISSING) contains both maps. Using %!s(MISSING) keyed map.\n"
- "Prespecializations library: Data at %!p(MISSING) only contains name-keyed map.\n"
- "Prespecializations library: Data at %!p(MISSING) only contains pointer-keyed map.\n"
- "Prespecializations library: Descriptor table lookup of '%!(BADPREC)%!s(MISSING)' returned NULL pointer to descriptor pointer.\n"
- "Prespecializations library: Did not find descriptor for key '%!(BADPREC)%!s(MISSING)'.\n"
- "Prespecializations library: Failed to build demangling for node %!p(MISSING).\n"
- "Prespecializations library: Failed to build demangling for simplified node %!p(MISSING).\n\n"
- "Prespecializations library: Failed to build simplified mangling for node %!p(MISSING).\n"
- "Prespecializations library: Found descriptor %!p(MISSING) for key '%!(BADPREC)%!s(MISSING)'.\n"
- "Prespecializations library: Hash table lookup checked %!u(MISSING) loaded entries, %!u(MISSING) total entries, starting data pointer %!p(MISSING), starting auxiliary pointer %!p(MISSING).\n"
- "Prespecializations library: Looking up descriptor named '%!(BADPREC)%!s(MISSING)'.\n"
- "Prespecializations library: No prespecializations map available from data at %!p(MISSING), disabling.\n"
- "Prespecializations library: Returning data pointer %!p(MISSING)\n"
- "Prespecializations library: Setting descriptorMapEnabled=%!s(MISSING) from SWIFT_DEBUG_ENABLE_LIB_PRESPECIALIZED_DESCRIPTOR_LOOKUP.\n"
- "Prespecializations library: Setting descriptorMapEnabled=%!s(MISSING) from the option flags.\n"
- "VAS_CNODE"
- "[VAS abort in function %!s(MISSING) at line %!d(MISSING)] [true: %!l(MISSING)lx %!s(MISSING) %!l(MISSING)lx]Could not allocate span for VAS private heap (%!s(MISSING))\n\n"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[32c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "_span_alloc"
- "name"
- "nested"
- "pointer"
- "vas span alloc failed on region of size %!z(MISSING)u with error code %!x(MISSING), error name %!s(MISSING), and detail %!d(MISSING)\n"
- "vas_core_heap_reserve_region"

```
