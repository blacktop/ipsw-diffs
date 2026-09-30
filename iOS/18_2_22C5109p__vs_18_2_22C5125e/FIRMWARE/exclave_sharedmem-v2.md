## exclave_sharedmem-v2

> `exclave_sharedmem-v2`

```diff

-40.60.7.0.0
-  __TEXT.__text: 0x3888f8
+40.60.8.0.0
+  __TEXT.__text: 0x388a80
   __TEXT.__lcxx_override: 0x204
-  __TEXT.__cstring: 0x1fa18
-  __TEXT.__const: 0xd17a0
-  __TEXT.__swift5_typeref: 0x5a96
+  __TEXT.__cstring: 0x1f9d8
+  __TEXT.__const: 0xd1770
+  __TEXT.__swift5_typeref: 0x5aca
+  __TEXT.__swift5_reflstr: 0x1ba1
+  __TEXT.__swift5_assocty: 0x4940
   __TEXT.__swift5_fieldmd: 0x5418
   __TEXT.__constg_swiftt: 0x9dbc
-  __TEXT.__swift5_reflstr: 0x1ba1
+  __TEXT.__swift5_capture: 0x348
+  __TEXT.__swift5_builtin: 0x3ac
   __TEXT.__swift5_protos: 0x23c
   __TEXT.__swift5_proto: 0x1484
   __TEXT.__swift5_types: 0x7cc
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__swift5_assocty: 0x4940
-  __TEXT.__swift5_capture: 0x348
-  __TEXT.__swift5_builtin: 0x3ac
   __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__swift5_acfuncs: 0x0
-  __TEXT.__swift5_replace: 0x0
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0
+  __TEXT.__swift5_acfuncs: 0x0
+  __TEXT.__swift5_replace: 0x0
   __TEXT.__thread_starts: 0x24
-  __TEXT.__eh_frame: 0x13130
+  __TEXT.__eh_frame: 0x131d8
   __DATA.__auth_ptr: 0x68
   __DATA.__mod_init_func: 0x48
-  __DATA.__const: 0x19568
+  __DATA.__const: 0x19588
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x4cc8
+  __DATA.__data: 0x4d38
   __DATA.__TIGHTBEAM: 0x30
+  __DATA.__shared_cache: 0x38
   __DATA.__ENDPOINTS: 0x62a
   __DATA.__thread_vars: 0x60
-  __DATA.__shared_cache: 0x38
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0x4e00
-  __DATA.__common: 0x27a0
-  __PDATA.__shared_cache: 0x0
+  __DATA.__bss: 0x4df0
+  __DATA.__common: 0x2770
   __PDATA.__mod_init_func: 0x0
+  __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 12778
+  Functions: 12788
   Symbols:   0
-  CStrings:  3756
+  CStrings:  3759
 
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
+ "SharedMemoryComponent/SharedMemoryComponent_Swift.swift"
+ "SharedMemoryComponent/SharedMemoryServer.swift"
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
+ "__span_alloc"
+ "_alloc_memory_frame"
+ "_alloc_va"
+ "_commit_alloc_va"
+ "data"
+ "heap->ensure_watermark_active"
+ "heap->heap_va.uncommitted_alloc || heap->cnode_va.uncommitted_alloc"
+ "invalid rawValue for BackingModel: "
+ "invalid rawValue for MappingAttribute: "
+ "invalid rawValue for Perms: "
+ "invalid rawValue for SharedMemoryGroup: "
+ "va_alloc->uncommitted_alloc"
+ "vas_core_heap_alloc_span"
+ "xrt_init failed with %!d(MISSING)"
- "(address__v_decode(message, &opt->value) == TB_ERROR_SUCCESS) && \"failed to decode type: StackshotTypes.Address (aka. UInt64)\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getAddressSpaceInfo\""
- "(result->tag == TB_ERROR_SUCCESS) && \"invalid error returned from getIPCStackEntry\""
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
- "[xrt] liblibc_plat_cl4_init:xrt_init:default"
- "[xrt] liblibc_plat_cl4_init:xrt_init:spawning"
- "_span_alloc"
- "invalid rawValue for BackingModel "
- "invalid rawValue for MappingAttribute "
- "invalid rawValue for Perms "
- "invalid rawValue for SharedMemoryGroup "
- "liblibc_plat_cl4_main.c:main() called, which should never happen"
- "name"
- "nested"
- "pointer"
- "sharedmem_serverv2/SharedMemoryComponent_Swift.swift"
- "sharedmem_serverv2/SharedMemoryServer.swift"
- "vas span alloc failed on region of size %!z(MISSING)u with error code %!x(MISSING), error name %!s(MISSING), and detail %!d(MISSING)\n"
- "vas_core_heap_reserve_region"

```
