## exclave_ExclaveStackshotServer

> `exclave_ExclaveStackshotServer`

```diff

 68.0.0.0.0
-  __TEXT.__text: 0x3433f4
+  __TEXT.__text: 0x3443c0
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__const: 0xd8f90
-  __TEXT.__cstring: 0x2515b
+  __TEXT.__const: 0xd8f30
+  __TEXT.__cstring: 0x256fb
   __TEXT.__swift5_typeref: 0x5fda
   __TEXT.__swift5_fieldmd: 0x5c8c
-  __TEXT.__constg_swiftt: 0xa758
+  __TEXT.__constg_swiftt: 0xa750
   __TEXT.__swift5_reflstr: 0x1ff0
   __TEXT.__swift5_assocty: 0x4980
   __TEXT.__swift5_protos: 0x258

   __DATA.__got: 0x8
   __DATA.__auth_ptr: 0x70
   __DATA.__mod_init_func: 0x48
-  __DATA.__const: 0x1b148
+  __DATA.__const: 0x1b180
   __DATA.__objc_imageinfo: 0x8
   __DATA.__TIGHTBEAM_VT: 0x60
   __DATA.__TIGHTBEAM: 0x20
-  __DATA.__data: 0x47b0
+  __DATA.__data: 0x4a78
   __DATA.__shared_cache: 0x38
   __DATA.__ENDPOINTS: 0x838
   __DATA.__thread_vars: 0x60
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0x45650
-  __DATA.__common: 0x2820
+  __DATA.__bss: 0x455d0
+  __DATA.__common: 0x2610
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: D2B582B0-51F1-35D6-8481-B7046F764B74
-  Functions: 12776
+  UUID: 0654900F-00CC-3631-B29C-40D4718C9D72
+  Functions: 12796
   Symbols:   0
-  CStrings:  4049
+  CStrings:  4088
 
CStrings:
+ "(span->attrs & VAS_SPAN_PINNED) == 0"
+ "/AppleInternal/Library/BuildRoots/4~B5T1ugAX_AKoyjcECsc8EyeIavxbyIZFKnpPHBs/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "Failed to populate VAS heap VA %s (0x%04hx)"
+ "OutlinedInitializeWithTakeNoValueWitness"
+ "PINNED"
+ "String must be contiguous UTF8"
+ "Substring must be contiguous UTF8"
+ "Swift/UTF8Span.swift"
+ "WARNING: failed attempt to destroy a span that is pinned"
+ "WOB"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx][%#zx, %#zx) not in asan span [%#zx, %#zx)\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]asan populate changed cur_off\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]asan populate changed len\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]overfull cur_reserve_slots\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]span %p ends past asan_shadow_end %#zx\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] Couldn't sustain VAS heap slot reserve\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] asan request out of span bounds\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] asan span_populate(%#zx, %#zx) failed %d:%d\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] cap should already exist!\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] pinned span changed?!\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] reserve count 0, but we allocated one\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] span should be pinned\n"
+ "[VAS abort in function %s at line %d] heap slot reserve ran out\n"
+ "[VAS abort in function %s at line %d] unable to populate frame cap %lx in vas %p for address %lx\n"
+ "[VAS abort in function %s at line %d] unable to populate table cap %lx in vas %p for address %lx\n"
+ "_span_asan_usable"
+ "_span_asan_usable_block_invoke"
+ "alloc_heap_cap"
+ "bad slot layout: nodes [%#zx, %#zx) bootinfo [%#zx, %#zx) free [%#zx, %#zx) reserve [%#zx, %#zx)"
+ "boot slot reserve empty"
+ "cannot be called after slot allocator is being set up"
+ "cna %p: expected state %d, was %d: %s"
+ "cnode range [%#zx, %#zx) and bootinfo range [%#zx, %#zx) should start at the same place"
+ "cnode range [%#zx, %#zx) must contain bootinfo range [%#zx, %#zx)"
+ "count != ptr->count"
+ "cowardly refusing to delete key %zu (out of bounds or has values?)"
+ "expected %zd free slots, only %zd passed in node range [%#zx, %#zx) bootinfo range [%#zx, %#zx)"
+ "heap->cur_reserve_slots == 0"
+ "length == 0 || length > span->config.size - offset"
+ "mtx_lock(&mapspan->spanmap_lock)"
+ "mtx_unlock(&mapspan->spanmap_lock)"
+ "must be called before alloc_setup"
+ "must be called only once"
+ "no cnodes found, need %zd slots for reserve"
+ "non-contiguous cnodes found at %#zx, range [%#zx, %#zx)"
+ "offset >= span->config.size"
+ "reserve_slot_alloc"
+ "ret.newly_allocated"
+ "span->spanmap.key != ptr->spanmap.key"
+ "span->spanmap.pointer != ptr->spanmap.pointer"
+ "span->spanmap.spanmap_type != ptr->spanmap.spanmap_type"
+ "span->spanmap.type_metadata != ptr->spanmap.type_metadata"
+ "spanmap could not alloc a cap: %s (0x%04hx)"
+ "state order issue"
+ "v8@?0"
+ "vas_core_heap_init"
+ "vas_is_occupied"
+ "vascommon->backend == NULL || vascommon->backend->cnode_bitmap_alloc == NULL || vascommon->backend->alloc_cnode == NULL || vascommon->backend->reserve_lock == NULL"
+ "vascore__set_asan_span"
+ "vascore__span_holder_get_cap"
- " x "
- "/AppleInternal/Library/BuildRoots/4~B4DqugABUp7_jQL8duzw3VDWAK6xZZmE5K9yf9o/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "Early unsafe CNode allocater ran out of slots\n"
- "Span over the small string form is not supported yet."
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]Reserve is empty\n"
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]Reserve is full\n"
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]reserve_capacity should fit in a uint8_t\n"
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]vas being reinitialised with different reserve capacity\n"
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]vas_slot_alloc() reserve not satified: reserve_slots (%u) < reserve_capacity (%u)\n"
- "[VAS abort in function %s at line %d] [true: (%s)] Couldn't sustain VAS object watermark: allocating frame failed\n"
- "[VAS abort in function %s at line %d] [true: (%s)] Couldn't sustain VAS object watermark: allocating page table\n"
- "[VAS abort in function %s at line %d] [true: (%s)] passed in reserve should be allocated, [%ld] is Nil\n"
- "[VAS abort in function %s at line %d] [true: (%s)] reserve_capacity should be non-zero if we have an array\n"
- "[VAS abort in function %s at line %d] [true: (%s)] reserve_capacity should only be non-zero if we have an array\n"
- "[VAS abort in function %s at line %d] unable to populate frame cap %lx or table cap %lx in vas %p for address %lx\n"
- "cowardly refusing to delete key %u (out of bounds or has values?)"
- "reserve_arr[i] == L4_Nil"
- "reserve_capacity == 0 && reserve_arr != NULL"
- "reserve_capacity > 0 && reserve_arr == NULL"
- "tss constructor could not find a key state in process info linked list"
- "vascommon->backend == NULL || vascommon->backend->cnode_bitmap_alloc == NULL || vascommon->backend->alloc_cnode == NULL"

```
