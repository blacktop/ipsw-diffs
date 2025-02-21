## exclave_pmm_exclave

> `exclave_pmm_exclave`

```diff

-696.80.4.0.0
-  __TEXT.__text: 0x311e4
-  __TEXT.__const: 0x1c880
-  __TEXT.__cstring: 0xb3fd
+839.100.252.0.1
+  __TEXT.__text: 0x35840
+  __TEXT.__const: 0x1c910
+  __TEXT.__cstring: 0xb8fb
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x18
   __DATA.__auth_ptr: 0x8
   __DATA.__mod_init_func: 0x18
-  __DATA.__const: 0xc30
-  __DATA.__data: 0x1889
+  __DATA.__const: 0xca0
+  __DATA.__data: 0x1a11
   __DATA.__ENDPOINTS: 0x838
   __DATA.__shared_cache: 0x70
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x1042a0
-  __DATA.__common: 0x7348
+  __DATA.__bss: 0x446f0
+  __DATA.__common: 0x6f90
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 887
-  Symbols:   10
-  CStrings:  1122
+  Functions: 953
+  Symbols:   4
+  CStrings:  1151
 
Symbols:
- _xrt__sync_identify
- _xrt__sync_init_thread
- _xrt__sync_wait
- _xrt__sync_wake
- _xrt__sync_yield
- _xrt__sync_yield_to
CStrings:
+ "\t\t\"allocs_size_bytes\": {\"static\": %lld, \"dynamic\": %llu, \"highest_dynamic\": %llu},\n"
+ "\"\n"
+ "(span->attrs & VAS_SPAN_OPTOUT_SPANMAP) != 0"
+ "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.4.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
+ "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
+ "L4_ErrorCode(err) == L4_ErrorCode(L4_Success)"
+ "No commpage was supplied\n"
+ "Unexpected L4_Error: %s(%zu) err='L4_Untyped_Create( untyped_memory.caps[memory_type][L4_Type_Arm64_FrameLevel0], L4_Type_Arm64_FrameLevel0, paddr - xnu_pbase, frame_cap(ret_frame) )'"
+ "Unexpected L4_Error: %s(%zu) err='_sync_thread( _yield_cap, context, args.permit_missing ? &retry : ((void*)0), &args )'"
+ "Unexpected L4_Error: %s(%zu) err='pmm_alloc_temp_with(vcss->pmm, L4_Type_Arm64_FrameLevel0, dest_cap, fault->rwtmpcap)'"
+ "WARNING: destroying a span that still has spanamp contents (type %u). The PMM won't be informed of these slots' deletion.\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]Invalid object type\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]impossible size\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] %llx + %lx overflowed\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] %s (0x%04hx)\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] spanmap cleanup function on a non-spanmap span\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] spanmap merge failed%s (0x%04hx)\n"
+ "[xrt:0x06x] Full panic message:\""
+ "_frame_cap_impl"
+ "_map_this_frame_internal"
+ "_object_free"
+ "_protect_frame"
+ "_span_split"
+ "exception handling can only be initialized once"
+ "memory limit exceeded. Check earlier log messages."
+ "mtx_init(&_vas_core_list_mutex, mtx_plain)"
+ "mtx_init(&unallocated->spanmap_lock, mtx_plain)"
+ "mtx_lock(&read_span->spanmap_lock)"
+ "mtx_lock(&span->spanmap_lock)"
+ "mtx_lock(&span_a->spanmap_lock)"
+ "mtx_lock(&write_span->spanmap_lock)"
+ "mtx_unlock(&read_span->spanmap_lock)"
+ "mtx_unlock(&span->spanmap_lock)"
+ "mtx_unlock(&span_a->spanmap_lock)"
+ "mtx_unlock(&write_span->spanmap_lock)"
+ "raw_frame_create(paddr, cap, type, requestor) == frame_cap(reserved_frame)"
+ "relocate_bootinfo_caps_spanmap"
+ "response == &msg"
+ "spanmap get cap had unexpected internal error"
+ "tb_priv(transport)->static_vtable != NULL"
+ "timebases were not updated after hibernation!"
+ "tp_priv->static_vtable != NULL"
+ "tss constructor could not find a key state in process info linked list"
+ "vas_core_spanmap_shadow_cleanup"
+ "vas_core_vas_init"
+ "vas_return_code(ret.ret) != VAS_SUCCESS"
+ "xrt__sync_identify_default"
+ "xrt__sync_init_thread_default"
- "\t\t\"allocs_size_bytes\": {\"static\": %lld, \"dynamic\": %u, \"highest_dynamic\": %u},\n"
- "%s(%zu): Cap move from %lx to return slot should succeed"
- "%s(%zu): Result cap move from %lx to return slot should succeed"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.3.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/libvas/shadow.c"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/libvas/span.c"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/libvas/vas.c"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/main.c"
- "Unexpected L4_Error: %s(%zu) err='L4_Untyped_Create( untyped_memory.caps[PHYS_MEM_TYPE_NORMAL][L4_Type_Arm64_FrameLevel0], L4_Type_Arm64_FrameLevel0, paddr - xnu_pbase, frame_cap(ret_frame) )'"
- "Unexpected L4_Error: %s(%zu) err='_sync_thread( _yield_cap, context, args.permit_missing ? &retry : ((void *)0), &args )'"
- "Unexpected L4_Error: %s(%zu) err='pmm_alloc_temp(L4_Type_Arm64_FrameLevel0, dest_cap, fault->rwtmpcap)'"
- "[VAS abort in function %s at line %d] [true: %lx %s %lx]Invliad object type\n"
- "_handle_alloc"
- "_server_encode_capabilities"
- "_server_receive_capabilities"
- "failed to get xrt runflags"
- "is_newest"
- "memory limit exceeded"
- "raw_frame_create(paddr, cap, type, is_realtime, is_finaltype) == frame_cap(reserved_frame)"
- "xrt__sync_identify"
- "xrt__sync_init_thread"

```
