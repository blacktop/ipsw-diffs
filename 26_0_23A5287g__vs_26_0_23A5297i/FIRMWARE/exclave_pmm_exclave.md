## exclave_pmm_exclave

> `exclave_pmm_exclave`

```diff

-1195.0.24.0.0
-  __TEXT.__text: 0x3e9dc
-  __TEXT.__const: 0x1cb90
-  __TEXT.__cstring: 0xe942
+1195.0.35.0.0
+  __TEXT.__text: 0x4179c
+  __TEXT.__const: 0x1cb92
+  __TEXT.__cstring: 0xf6b3
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0
-  __TEXT.__thread_starts: 0x18
+  __TEXT.__thread_starts: 0x20
   __DATA.__auth_ptr: 0x10
   __DATA.__mod_init_func: 0x18
-  __DATA.__const: 0xe90
-  __DATA.__data: 0x1bf1
+  __DATA.__const: 0x11e0
+  __DATA.__data: 0x1f61
   __DATA.__ENDPOINTS: 0x838
   __DATA.__shared_cache: 0x70
+  __DATA.__TIGHTBEAM_VT: 0x30
+  __DATA.__TIGHTBEAM: 0x10
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x45e70
-  __DATA.__common: 0x75a0
+  __DATA.__bss: 0x45e10
+  __DATA.__common: 0x74a0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  UUID: F7B60FB1-764C-3BE0-A8D8-52AFF33A2F77
-  Functions: 1059
+  UUID: 561BDF69-87A8-36DF-99FA-C5A4D8AFD9FF
+  Functions: 1119
   Symbols:   4
-  CStrings:  1318
+  CStrings:  1360
 
CStrings:
+ "$JgPMMStatsDelegate.PMMStatsDelegate"
+ "$JgStatsDelegate.StatsDelegate.init()"
+ "/AppleInternal/Library/BuildRoots/4~B5T1ugAX_AKoyjcECsc8EyeIavxbyIZFKnpPHBs/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/Library/Caches/com.apple.xbs/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/pmm-server.build/pmm-server.build/DerivedSources/StatsDelegate_C.c"
+ "Failed to populate VAS heap VA %s (0x%04hx)"
+ "I112@?0{pmmstatsdelegate_pmmstatsdelegate_describe__result_s=C(?=C{pmmstatsdelegate_statdescription_s={pmmstatsdelegate_stattype_s=Q(?={?={pmmstatsdelegate_singlestatinfo_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}{?={pmmstatsdelegate_clientstatinfo_s=Ci{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}{?=C})}{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}8"
+ "I12@?0I8"
+ "I24@?0^{statsdelegate_statsdelegate__context_s=^^v^^v}8@?<I@?I>16"
+ "I28@?0^{statsdelegate_statsdelegate__context_s=^^v^^v}8I16@?<I@?{pmmstatsdelegate_pmmstatsdelegate_describe__result_s=C(?=C{pmmstatsdelegate_statdescription_s={pmmstatsdelegate_stattype_s=Q(?={?={pmmstatsdelegate_singlestatinfo_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}{?={pmmstatsdelegate_clientstatinfo_s=Ci{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}{?=C})}{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}>20"
+ "I32@?0^{statsdelegate_statsdelegate__context_s=^^v^^v}8I16I20@?<I@?{pmmstatsdelegate_pmmstatsdelegate_read__result_s=C(?=C{pmmstatsdelegate_statvalue_v_s=C(?={?=^{pmmstatsdelegate_statvalue_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}>24"
+ "I56@?0{pmmstatsdelegate_pmmstatsdelegate_read__result_s=C(?=C{pmmstatsdelegate_statvalue_v_s=C(?={?=^{pmmstatsdelegate_statvalue_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}8"
+ "PINNED"
+ "StatsDelegate"
+ "StatsDelegate.StatsDelegate"
+ "StatsDelegate_C.c"
+ "TB_FATAL: disallowed selector: %llu (%s:%d)\n"
+ "TB_FATAL: invalid error returned from describe (%s:%d)\n"
+ "TB_FATAL: invalid error returned from read (%s:%d)\n"
+ "TB_FATAL: unrecognized selector: %llu (%s:%d)\n"
+ "Total Memory Usage"
+ "WARNING: failed attempt to destroy a span that is pinned"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx][%#zx, %#zx) not in asan span [%#zx, %#zx)\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]asan populate changed cur_off\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]asan populate changed len\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]overfull cur_reserve_slots\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] Couldn't sustain VAS heap slot reserve\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] asan request out of span bounds\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] asan span_populate(%#zx, %#zx) failed %d:%d\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] reserve count 0, but we allocated one\n"
+ "[VAS abort in function %s at line %d] heap slot reserve ran out\n"
+ "[VAS abort in function %s at line %d] unable to populate frame cap %lx in vas %p for address %lx\n"
+ "[VAS abort in function %s at line %d] unable to populate table cap %lx in vas %p for address %lx\n"
+ "^^v16@?0^^v8"
+ "_span_asan_usable"
+ "_span_asan_usable_block_invoke"
+ "alloc_heap_cap"
+ "bad slot layout: nodes [%#zx, %#zx) bootinfo [%#zx, %#zx) free [%#zx, %#zx) reserve [%#zx, %#zx)"
+ "boot slot reserve empty"
+ "cannot be called after slot allocator is being set up"
+ "cna %p: expected state %d, was %d: %s"
+ "cnode range [%#zx, %#zx) and bootinfo range [%#zx, %#zx) should start at the same place"
+ "cnode range [%#zx, %#zx) must contain bootinfo range [%#zx, %#zx)"
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
+ "spanmap could not alloc a cap: %s (0x%04hx)"
+ "state order issue"
+ "v16@?0^^v8"
+ "v20@?0Q8C16"
+ "v24@?0Q8r^{pmmstatsdelegate_statvalue_s=Q(?={?=Q}{?=QQ})}16"
+ "v24@?0^^v8^^v16"
+ "v8@?0"
+ "vas_core_heap_init"
+ "vas_is_occupied"
+ "vascommon->backend == NULL || vascommon->backend->cnode_bitmap_alloc == NULL || vascommon->backend->alloc_cnode == NULL || vascommon->backend->reserve_lock == NULL"
- "/AppleInternal/Library/BuildRoots/4~B4DqugABUp7_jQL8duzw3VDWAK6xZZmE5K9yf9o/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "Early unsafe CNode allocater ran out of slots\n"
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
- "[VAS abort in function %s at line %d] [true: (%s)] vas__setSelf() has not been called\n"
- "[VAS abort in function %s at line %d] unable to populate frame cap %lx or table cap %lx in vas %p for address %lx\n"
- "_slot_reserve_check"
- "_vascommon() == NULL"
- "reserve_arr[i] == L4_Nil"
- "reserve_capacity == 0 && reserve_arr != NULL"
- "reserve_capacity > 0 && reserve_arr == NULL"
- "tss constructor could not find a key state in process info linked list"
- "vascommon->backend == NULL || vascommon->backend->cnode_bitmap_alloc == NULL || vascommon->backend->alloc_cnode == NULL"

```
