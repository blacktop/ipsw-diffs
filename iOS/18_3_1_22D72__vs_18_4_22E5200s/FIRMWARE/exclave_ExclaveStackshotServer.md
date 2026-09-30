## exclave_ExclaveStackshotServer

> `exclave_ExclaveStackshotServer`

```diff

-26.60.20.0.0
-  __TEXT.__text: 0x368410
+63.0.0.0.0
+  __TEXT.__text: 0x32c7a4
   __TEXT.__lcxx_override: 0x204
-  __TEXT.__const: 0xd1840
-  __TEXT.__cstring: 0x215cb
-  __TEXT.__swift5_typeref: 0x5dae
-  __TEXT.__swift5_fieldmd: 0x5718
-  __TEXT.__constg_swiftt: 0xa264
-  __TEXT.__swift5_reflstr: 0x1d40
-  __TEXT.__swift5_assocty: 0x4908
+  __TEXT.__const: 0xd22d0
+  __TEXT.__cstring: 0x2174b
+  __TEXT.__swift5_typeref: 0x5d68
+  __TEXT.__swift5_fieldmd: 0x581c
+  __TEXT.__constg_swiftt: 0xa3f4
+  __TEXT.__swift5_reflstr: 0x1de0
+  __TEXT.__swift5_assocty: 0x4858
   __TEXT.__swift5_protos: 0x248
-  __TEXT.__swift5_proto: 0x144c
-  __TEXT.__swift5_types: 0x844
-  __TEXT.__swift5_capture: 0x7f8
-  __TEXT.__swift5_builtin: 0x578
+  __TEXT.__swift5_proto: 0x145c
+  __TEXT.__swift5_types: 0x85c
+  __TEXT.__swift5_capture: 0x838
+  __TEXT.__swift5_builtin: 0x58c
   __TEXT.__swift5_mpenum: 0xa8
+  __TEXT.__swift_as_entry: 0x210
+  __TEXT.__swift_as_ret: 0x298
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__swift5_acfuncs: 0x0
   __TEXT.__swift5_replace: 0x0
-  __TEXT.__thread_starts: 0x24
-  __TEXT.__eh_frame: 0x10850
-  __DATA.__auth_ptr: 0x60
+  __TEXT.__thread_starts: 0x28
+  __TEXT.__eh_frame: 0x10058
+  __DATA.__auth_ptr: 0x58
   __DATA.__mod_init_func: 0x48
-  __DATA.__const: 0x1abd0
+  __DATA.__const: 0x1adc8
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x49b8
+  __DATA.__TIGHTBEAM_VT: 0x60
   __DATA.__TIGHTBEAM: 0x20
+  __DATA.__data: 0x4ad8
   __DATA.__shared_cache: 0x38
   __DATA.__ENDPOINTS: 0x838
   __DATA.__thread_vars: 0x60
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0x1050a0
-  __DATA.__common: 0x2738
+  __DATA.__bss: 0x451e0
+  __DATA.__common: 0x273c
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 12469
+  Functions: 12427
   Symbols:   0
-  CStrings:  3843
+  CStrings:  3846
 
CStrings:
+ "    Demangled: %s\n"
+ "    Flags.IsDistributed: %d\n"
+ "    Function Ptr: %p\n"
+ " leaked its continuation without resuming it. This may cause tasks waiting on it to remain suspended forever.\n"
+ "\"\n"
+ "$"
+ "$n"
+ "%s%s"
+ "%s(%zu): pmm_alloc_flags_with(pmm, %d, 0x%x, %lx) = %lx"
+ "%s(%zu): xrt__plat_Dart_SetRoot(%lx, %lx)[0x%x] = %lx"
+ "%s:%d: %s"
+ "(span->attrs & VAS_SPAN_OPTOUT_SPANMAP) != 0"
+ "+"
+ "-removed"
+ "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.4.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libvas/Source/shadow.c"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libvas/Source/sharedmem-util.c"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libvas/Source/sharedmemory.c"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libvas/Source/span.c"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libvas/Source/vas.c"
+ "/Library/Caches/com.apple.xbs/Sources/libcxx_exclavecore/libcxxabi/src/private_typeinfo.cpp"
+ "==== Accessible Function Records ====\n"
+ "==== End of Accessible Function Records ====\n"
+ "@in_cxx"
+ "BV"
+ "Builtin.FixedArray<"
+ "BuiltinFixedArray"
+ "Cannot decode an invalid collection difference"
+ "Could not resolve KeyPath"
+ "DependentGenericParamValueMarker"
+ "DroppedArgument"
+ "Failed to look up symbolic reference at %p - offset %d - symbol %s in %s - pointer at %#lx is likely a reference to a missing weak symbol\n"
+ "FixedArray"
+ "I16@?0^v8"
+ "Illegal attempt to set a TaskLocal value, use `withValue(...) { ... }` instead."
+ "ImplCoroutineKind"
+ "Initializing continuation for task %p that was already initialized.\n"
+ "Integer"
+ "IsolatedDeallocator"
+ "L4_ErrorCode(err) == L4_ErrorCode(L4_Success)"
+ "Modify2Accessor"
+ "NegativeInteger"
+ "No commpage was supplied\n"
+ "Prespecializations library validation: validated %u entries, %u failures.\n"
+ "Prespecializations library: Hash table lookup checked %u loaded entries, %u total entries.\n"
+ "RV"
+ "Read2Accessor"
+ "Record count: %d\n"
+ "Record name: %s\n"
+ "Resuming continuation for task %p that is not awaited (may have already been resumed).\n"
+ "SILThunkHopToMainActorIfNeeded"
+ "SILThunkIdentity"
+ "TT"
+ "Unconditional cast failed. Both source and target types were NULL. %s\n"
+ "Unconditional cast failed. Source type was '%s' (%p), target type was NULL. %s\n"
+ "Unconditional cast failed. Source type was NULL, target was '%s' (%p). %s\n"
+ "Unexpected L4_Error: %s(%zu) err='_sync_thread( _yield_cap, context, args.permit_missing ? &retry : ((void*)0), &args )'"
+ "Unexpected L4_Error: %s(%zu) err='pmm_alloc_temp_with(vcss->pmm, L4_Type_Arm64_FrameLevel0, dest_cap, fault->rwtmpcap)'"
+ "Unknown general category"
+ "Unknown numeric type"
+ "WARNING: destroying a span that still has spanamp contents (type %u). The PMM won't be informed of these slots' deletion.\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]Invalid object type\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]impossible size\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] %llx + %lx overflowed\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] %s (0x%04hx)\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] spanmap cleanup function on a non-spanmap span\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] spanmap merge failed%s (0x%04hx)\n"
+ "[xrt:0x06x] Full panic message:\""
+ "__isolated_deallocating_deinit"
+ "_frame_cap_impl"
+ "_map_this_frame_internal"
+ "_object_free"
+ "_protect_frame"
+ "_span_split"
+ "catching a class without an object?"
+ "exception handling can only be initialized once"
+ "fZ"
+ "failed to decode coroutine kind"
+ "failed to decode function results"
+ "failed to decode function yields"
+ "hop to main actor thunk of "
+ "identity thunk of "
+ "insertions"
+ "modify2"
+ "mtx_init(&_vas_core_list_mutex, mtx_plain)"
+ "mtx_init(&unallocated->spanmap_lock, mtx_plain)"
+ "mtx_lock(&_vas_core_list_mutex)"
+ "mtx_lock(&read_span->spanmap_lock)"
+ "mtx_lock(&span->spanmap_lock)"
+ "mtx_lock(&span_a->spanmap_lock)"
+ "mtx_lock(&write_span->spanmap_lock)"
+ "mtx_unlock(&_vas_core_list_mutex)"
+ "mtx_unlock(&read_span->spanmap_lock)"
+ "mtx_unlock(&span->spanmap_lock)"
+ "mtx_unlock(&span_a->spanmap_lock)"
+ "mtx_unlock(&write_span->spanmap_lock)"
+ "operation unsupported: swift_task_donateThreadToGlobalExecutorUntilImpl"
+ "param"
+ "read2"
+ "relocate_bootinfo_caps_spanmap"
+ "response == &msg"
+ "spanmap get cap had unexpected internal error"
+ "subject value %li does not match constraint value %li"
+ "tb_priv(transport)->static_vtable != NULL"
+ "timebases were not updated after hibernation!"
+ "tp_priv->static_vtable != NULL"
+ "tss constructor could not find a key state in process info linked list"
+ "unable to find vas %p on next_vas list starting at %p"
+ "unknown value generic requirement kind %u"
+ "vas_core_spanmap_shadow_cleanup"
+ "vas_core_vas_free"
+ "vas_core_vas_init"
+ "vas_return_code(ret.ret) != VAS_SUCCESS"
+ "withTransportBuffer called with nil buffer"
+ "xrt__sync_identify_default"
+ "xrt__sync_init_thread_default"
+ "yield_many"
+ "yield_once"
+ "yield_once_2"
- " leaked its continuation!\n"
- " value, use `withValue(...) { ... }` instead."
- "$sBi128_WV"
- "$sBi16_WV"
- "$sBi256_WV"
- "$sBi32_WV"
- "$sBi512_WV"
- "$sBi64_WV"
- "$sBi8_WV"
- "%s(%zu): Cap move from %lx to return slot should succeed"
- "%s(%zu): Result cap move from %lx to return slot should succeed"
- "%s(%zu): pmm_alloc_with(pmm, %d, %lx) = %lx"
- "%s(%zu): xrt__plat_Dart_SetRoot(%lx, %lx) = %lx"
- "%s:%u:%s: "
- "%zu fields"
- "(self lifetime dependence: "
- "+0x"
- "+0x0"
- ", startSlot: "
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.3.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libvas/shadow.c"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libvas/sharedmem-util.c"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libvas/sharedmemory.c"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libvas/span.c"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libvas/vas.c"
- "<<nullptr>>"
- "@yield_many"
- "@yield_once"
- "Building %s"
- "Don't know how to initialize enum metadata yet"
- "Don't know how to initialize metadata kind %#x"
- "Enum descriptor has no payload size offset, computed extra data size from generic arguments, extra data size: %zu"
- "Enum descriptor has payload size offset, computed extra data size: %zu"
- "Examining field %u '%s' type '%.*s' (mangled name is %zu bytes)"
- "Extra data size is %zu, allocating %zu bytes total"
- "Failed to look up symbolic reference at %p - offset %d - symbol %s in %s\n"
- "Fatal error: mismatched metadata.\n"
- "GenericMetadataBuilder.cpp"
- "GenericMetadataBuilder.h"
- "Getting extra data size for %s"
- "Illegal attempt to set a "
- "Initializing continuation context %p that was already initialized.\n"
- "Initializing enum"
- "Initializing new VWT from old VWT %#llx - %s (%s + %llu)"
- "Initializing struct"
- "Installing %hu generic arguments at offset %d"
- "Is bitwise takable, setting pod_copy as initializeWithTake"
- "Looked up field type metadata %p"
- "MetatypeParamsRemoved"
- "Not enough generic arguments, %zu provided, %d required"
- "ParamLifetimeDependence"
- "Prespecializations library: Hash table lookup checked %u loaded entries, %u total entries, starting data pointer %p, starting auxiliary pointer %p.\n"
- "Resuming continuation context %p that was not awaited (may have already been resumed).\n"
- "SelfLifetimeDependence"
- "Setting descriptor"
- "Setting initial value witnesses"
- "Setting metadata kind %#x"
- "Struct descriptor has field offset vector, computed extra data size: %zu"
- "Struct descriptor has no field offset vector, computed extra data size from generic arguments, extra data size: %zu"
- "Swift/FixedArray.swift"
- "TB"
- "TG"
- "Tg"
- "Ti"
- "Ts"
- "Type has no completion function, skipping initialization"
- "Unable to compute extra data size of descriptor with kind %u"
- "Uncommon layout case, flags.isInlineStorage=%s"
- "Unexpected L4_Error: %s(%zu) err='_sync_thread( _yield_cap, context, args.permit_missing ? &retry : ((void *)0), &args )'"
- "Unexpected L4_Error: %s(%zu) err='pmm_alloc_temp(L4_Type_Arm64_FrameLevel0, dest_cap, fault->rwtmpcap)'"
- "Unknown general category "
- "Unknown numeric type "
- "Validated generic metadata builder on %.*s"
- "Value type descriptor has extra data pattern, extra data size: %zu"
- "Writing %hu words of extra data from offset %hu"
- "YL"
- "Yl"
- "[VAS abort in function %s at line %d] [true: %lx %s %lx]Invliad object type\n"
- "_server_encode_capabilities"
- "_server_receive_capabilities"
- "_swift_pod_copy"
- "_swift_pod_destroy"
- "_swift_pod_direct_initializeBufferWithCopyOfBuffer"
- "_swift_pod_indirect_initializeBufferWithCopyOfBuffer"
- "buildGenericValueMetadata"
- "case sizeWithAlignmentMask(1, 0, 0)"
- "case sizeWithAlignmentMask(16, 15, 0)"
- "case sizeWithAlignmentMask(2, 1, 0)"
- "case sizeWithAlignmentMask(32, 31, 0)"
- "case sizeWithAlignmentMask(4, 3, 0)"
- "case sizeWithAlignmentMask(64, 63, 0)"
- "case sizeWithAlignmentMask(8, 7, 0)"
- "error allocating metadata: %s"
- "error getting extra data size: %s"
- "extraDataSize"
- "failed to get xrt runflags"
- "getSymbolPointer is not implemented on this platform"
- "inherit "
- "inherit) "
- "initializeEnumMetadata"
- "initializeGenericMetadata"
- "initializeStructMetadata"
- "initializeValueMetadataFromPattern"
- "installCommonValueWitnesses"
- "installGenericArguments"
- "lifetime dependence: "
- "metatypes-removed"
- "operator()"
- "scope "
- "scope) "
- "substitutions.getMetadata(%u, %u).Ptr = %p"
- "substitutions.getWitnessTable(%p, %u) = %p"
- "swift_initializeGenericValueMetadata failed: %s"
- "type isPOD, hasExtraInhabitants=%s layout.size=%zu flags.getAlignmentMask=%zu"
- "xrt__sync_identify"
- "xrt__sync_init_thread"

```
