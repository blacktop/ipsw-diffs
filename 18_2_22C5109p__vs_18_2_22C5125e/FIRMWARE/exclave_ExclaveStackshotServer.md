## exclave_ExclaveStackshotServer

> `exclave_ExclaveStackshotServer`

```diff

 26.60.20.0.0
-  __TEXT.__text: 0x3673ec
+  __TEXT.__text: 0x3673c4
   __TEXT.__lcxx_override: 0x204
-  __TEXT.__const: 0xd1910
-  __TEXT.__cstring: 0x214cb
-  __TEXT.__swift5_typeref: 0x5dbc
-  __TEXT.__swift5_fieldmd: 0x5740
-  __TEXT.__constg_swiftt: 0xa280
-  __TEXT.__swift5_reflstr: 0x1d60
-  __TEXT.__swift5_assocty: 0x4920
+  __TEXT.__const: 0xd1840
+  __TEXT.__cstring: 0x210bb
+  __TEXT.__swift5_typeref: 0x5dae
+  __TEXT.__swift5_fieldmd: 0x5718
+  __TEXT.__constg_swiftt: 0xa264
+  __TEXT.__swift5_reflstr: 0x1d40
+  __TEXT.__swift5_assocty: 0x4908
   __TEXT.__swift5_protos: 0x248
-  __TEXT.__swift5_proto: 0x145c
-  __TEXT.__swift5_types: 0x848
+  __TEXT.__swift5_proto: 0x144c
+  __TEXT.__swift5_types: 0x844
   __TEXT.__swift5_capture: 0x7f8
   __TEXT.__swift5_builtin: 0x578
   __TEXT.__swift5_mpenum: 0xa8

   __TEXT.__swift5_acfuncs: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__thread_starts: 0x24
-  __TEXT.__eh_frame: 0x105c0
+  __TEXT.__eh_frame: 0x10698
   __DATA.__auth_ptr: 0x58
   __DATA.__mod_init_func: 0x48
-  __DATA.__const: 0x1ac40
+  __DATA.__const: 0x1abd0
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x4960
+  __DATA.__data: 0x49b8
   __DATA.__TIGHTBEAM: 0x20
   __DATA.__shared_cache: 0x38
   __DATA.__ENDPOINTS: 0x838

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0x1050e0
-  __DATA.__common: 0x2740
+  __DATA.__bss: 0x1050b0
+  __DATA.__common: 0x2718
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 12426
+  Functions: 12432
   Symbols:   0
-  CStrings:  3826
+  CStrings:  3825
 
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
+ "TB_FATAL: invalid error returned from backRange (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from createMapping (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingDestroy (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingGetFrame (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingGetInfo (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingGetPhysicalAddress (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingGetPhysicalAddresses (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingMap (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingSetMapped (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from mappingUnmap (%!s(MISSING):%!d(MISSING))\n"
+ "TB_FATAL: invalid error returned from unbackRange (%!s(MISSING):%!d(MISSING))\n"
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
+ "invalid rawValue for HelperFailure: "
+ "invalid rawValue for StackshotServerFailure: "
+ "invalid rawValue for StackshotServerVariant: "
+ "va_alloc->uncommitted_alloc"
+ "vas_core_heap_alloc_span"
+ "xrt_init failed with %!d(MISSING)"
- "(decode_error == TB_ERROR_SUCCESS) && \"tb_message_decode_capability failed\""
- "(physicaladdress__v_decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.PhysicalAddress (aka. UInt64)\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from backRange\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from createMapping\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingDestroy\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingGetFrame\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingGetInfo\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingGetPhysicalAddress\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingGetPhysicalAddresses\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingMap\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingSetMapped\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from mappingUnmap\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from unbackRange\""
- "(sharedmemory_backingerror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemory.BackingError\""
- "(sharedmemorybase_accesserror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.AccessError\""
- "(sharedmemorybase_mappinginfo__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.MappingInfo\""
- "(sharedmemorybase_mappingresult__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.MappingResult\""
- "(sharedmemorybase_perms__decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.Perms\""
- "(sharedmemorybase_perms__decode(msg, &perm) == TB_ERROR_SUCCESS) && \"failed to decode type: SharedMemoryBase.Perms\""
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
- "invalid rawValue for HelperFailure "
- "invalid rawValue for StackshotServerFailure "
- "invalid rawValue for StackshotServerVariant "
- "name"
- "nested"
- "pointer"
- "vas span alloc failed on region of size %!z(MISSING)u with error code %!x(MISSING), error name %!s(MISSING), and detail %!d(MISSING)\n"
- "vas_core_heap_reserve_region"

```
