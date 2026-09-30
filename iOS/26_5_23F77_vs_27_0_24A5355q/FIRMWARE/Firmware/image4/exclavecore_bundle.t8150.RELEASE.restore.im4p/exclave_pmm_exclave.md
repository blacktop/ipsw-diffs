## exclave_pmm_exclave

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.restore.im4p/exclave_pmm_exclave`

```diff

-1195.120.4.0.1
-  __TEXT.__text: 0x48340 sha256:69de933abda9ccc2b86e140edd63cd4f0f2c9f218c33f701432b72ddb712f202
-  __TEXT.__const: 0x1cbd2 sha256:d9a943fd35e27d70f167e24a8a7e4d57f1df66bd4cb79f5833016cb3da992033
-  __TEXT.__cstring: 0x10d54 sha256:87be74373c7cb404b1015e3ce47737dc762a1732b471db66b2f03b9e98c36844
+1460.0.0.502.2
+  __TEXT.__text: 0x4c440 sha256:00199c323d874dab4e60885919ae0c38e603dd54e947065edb64f6bd0933e9b0
+  __TEXT.__const: 0x1d160 sha256:beb254a8d77e20abab2470688a4e48b17b27a637434e7bcbec38425b6adb1caa
+  __TEXT.__cstring: 0x11c84 sha256:b9cd3c8c557699cbc51601e697b7d7daf0106f754378b60db3a1bfd79daf00c6
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
-  __TEXT.__chain_fixups: 0x58 sha256:5ec2f5ddbf095420132fa25037e67af4e2b27756c3330a8a6bcb6156ce6f4de8
-  __TEXT.__eh_frame: 0x48 sha256:017102a6aa3d3222d8fb06b27dc88fdb69561a05fc1639fde61331b47cb8bf8f
-  __DATA.__const: 0x12a0 sha256:63db4afc14f4d3d4ae3b5d7ac706163badbfd9447320dffb280e6fe1f80f76dd
-  __DATA.__data: 0x2071 sha256:06a8c24e8c29f461033411c1e03fc45a45993b137b54d391051d1372e8082bbc
-  __DATA.__ENDPOINTS: 0x838 sha256:bc42dd2206ef9f400d446c2d6729f3ddb082193c68dd0d26d0d4d18ff2c4c92a
-  __DATA.__shared_cache: 0x70 sha256:ece26b372237028f639b4881d4d4f94d032bf768968146483e92d40fe7c3526a
-  __DATA.__TIGHTBEAM_VT: 0x30 sha256:39ea246ef9aea1f83554e22047c28fff06e216e4637701f6631aad73076731c5
-  __DATA.__TIGHTBEAM: 0x10 sha256:94fe0f974c3f2180d0a076cf67e72a17803c3d531d9e13efcc4b0f3b48229b42
-  __DATA.__mod_init_func: 0x18 sha256:5ea5780dcd21ecba63e6ba127346c3d29bcd39484c7e3b4ee015a9b25fe545f4
-  __DATA.__auth_ptr: 0x10 sha256:2018c39077e1f3a103e9eb0d128868fdb60137e544896776de9d58e28ed665e8
+  __TEXT.__chain_fixups: 0x60 sha256:ba7d43c2ef2a32de0b421f6288562cbdaba1fda3de38d987ba1d2bca89dbf904
+  __TEXT.__eh_frame: 0x48 sha256:2e6fe798b2905b8adf8e06d2a9f8d1ebd4925f8b141e2817a58919c4422923d5
+  __DATA.__const: 0x1348 sha256:73d6a11958fc882fbdbe630e5494b4ea447d95254e963dd4169f13fa7262180a
+  __DATA.__data: 0x2421 sha256:a1d667ceba22106d88f09208f7a036376107dbc8e41f580e062c82c526a9d090
+  __DATA.__auth_ptr: 0x30 sha256:cdf7d6a7240a9848950d7fc0185dd6824e353fa99a6bb71a950a40bc886d6660
+  __DATA.__ENDPOINTS: 0x93f sha256:669cf548297b0dd9d033e49059bbfbdee7920e3b64da83fe54fe0e669526c13a
+  __DATA.__shared_cache: 0x70 sha256:d799c02aa198601af8d3d2da5f13f27f1fb6572e1d91eb5055b9b84a169a19bb
+  __DATA.__mod_init_func: 0x18 sha256:829772991d29bc20a7f4f1eb7716a35b4a4062ef31814cf93d044a47e3d1d956
   __DATA.__mod_term_func: 0x0
   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x47e18 sha256:cc353a3ce4464c2e6326606832ed34db16ad9c34dec0ed82427d4a828713e0b5
-  __DATA.__common: 0x9108
+  __DATA.__bss: 0x4f238 sha256:d7c33595707560948203f0a1d87eaac76a92f2570b19e683ad37d60ec41eaac2
+  __DATA.__common: 0x91b0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  UUID: 94070A4B-A5E5-351F-8C76-8ADDF530CE89
-  Functions: 1133
+  UUID: 1DE2A2F6-E321-36B2-B236-0327A06DB7E9
+  Functions: 1203
   Symbols:   4
-  CStrings:  1442
+  CStrings:  1501
 
CStrings:
+ "!(cnode->bitmap[word] & mask)"
+ "!(old & mask)"
+ "!marked"
+ "!vas_reserve_held(vascommon->backend->reserve_lock)"
+ "!vascommon->setup_structsize"
+ "!vascore_init_initialized"
+ "!xrt__curthread_no_faults()"
+ "%s%s"
+ "(cnode->bitmap[word] & mask) == 0"
+ "(curinuse & mask)"
+ "(old & mask)"
+ "(oldinuse & mask)"
+ "/AppleInternal/Library/BuildRoots/4~CQ9SugDGM67-dzN__132t-DvWWAUQYUthO4FKKg/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS27.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "B16@?0^{vas_core_span={?=CQQCCCCC^vQ}iC[3C]{?=^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}B{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
+ "Conclave ASID mapping"
+ "DELEGATED"
+ "Exclaves Freezer disabled for asid %#04hx\n"
+ "Failed to create stats endpoint\n"
+ "Failed to start pmm stats delegate: %d\n"
+ "I16@?0@?<I@?I>8"
+ "I16@?0@?<I@?{statsdelegate_statsdelegateid_s=[32C]}>8"
+ "I20@?0I8@?<I@?{statsdelegate_statsdelegate_describe__result_s=C(?=C{statsdelegate_statdescription_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}>12"
+ "I24@?0I8I12@?<I@?{statsdelegate_statsdelegate_read__result_s=C(?=C{statsdelegate_statvalue_v_s=C(?={?=^{statsdelegate_statvalue_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}>16"
+ "I40@?0{statsdelegate_statsdelegateid_s=[32C]}8"
+ "I56@?0{statsdelegate_statsdelegate_describe__result_s=C(?=C{statsdelegate_statdescription_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}8"
+ "I56@?0{statsdelegate_statsdelegate_read__result_s=C(?=C{statsdelegate_statvalue_v_s=C(?={?=^{statsdelegate_statvalue_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}8"
+ "Input validation failed"
+ "L4_Type_Ev"
+ "Page was opted out of freezer"
+ "TB_ASSERT: !TB_CHECK_FLAG(query_flags, TB_TRANSPORT_FLAG_ERROR), Server attempted to reply to an error (%s:%d)\n"
+ "TB_ASSERT: context != NULL, Attempting to invalidate a NULL connection (%s:%d)\n"
+ "TB_ASSERT: disp == TB_MESSAGE_DISPOSITION_QUERY || disp == TB_MESSAGE_DISPOSITION_ERROR, %hhu (%s:%d)\n"
+ "TB_ASSERT: query->disposition == TB_MESSAGE_DISPOSITION_QUERY || query->disposition == TB_MESSAGE_DISPOSITION_ERROR, %hhu (%s:%d)\n"
+ "TB_ASSERT: tb_message_get_state(message) == TB_MESSAGE_STATE_RECEIVED, %u (%s:%d)\n"
+ "TB_FATAL: Attempt to retrieve reply list in environment without large message support (%s:%d)\n"
+ "TB_FATAL: invalid error returned from %s (%s:%d)\n"
+ "TB_FATAL: invalid tag in `[StatsDelegate.StatValue]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: tb_message_decode_f64_v2: %d (%s:%d)\n"
+ "TB_FATAL: tb_message_encode_f64_v2: %d (%s:%d)\n"
+ "Unexpected L4_Error: %s(%zu) err='pmm_alloc_temp_flags_with(vcss->pmm, L4_Type_Arm64_FrameLevel0, dest_frame_cap, fault->rwtmpcap, pmm_flags)'"
+ "[PMM DEBUG] stats_describe_handler: returning success for statId=%u\n"
+ "[PMM DEBUG] stats_describe_handler: statId=%u, total_count=%u\n"
+ "[PMM DEBUG] stats_describe_handler: validation failed - returning INVALIDIDX"
+ "[PMM] Stats Delegate EP not initialized (was L4_Nil)"
+ "[PMM] Stats Delegate Init'd"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]Cannot free initially allocated structures\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]EP_ek and dyld_ek have incompatible vascommon sizes\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]delegated vas children do not support non-leaf page tables\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]index out of range\n"
+ "[VAS abort in function %s at line %d] [true: %llx %s %llx]moving cap from delegated page table get cbarg %p offset %#zx (addr %#zx) %#zx -> %#zx failed\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] attempt to insert 0 or non-page-aligned cnode %#lx bitmap %p\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] cached slot %#lx doesn't have an associated cnode_bitmap\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] child delegated VASes only have leaf page tables\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] cn %p (%#lx): slot %#lx (idx %#lx) is already marked free\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] cn %p (%#lx): was on freelist, but allocated count is %#x >= %#x (slots per cnode)\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] delegated page table get cbarg %p offset %#zx (addr %#zx) failed %d:%#hx\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] drain cannot be entered recursively\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] perthread cache %p has crazy nCacheCaps %u > %u\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] perthread cache %p slot %u is L4_Nil\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] perthread cache %p still full after drain\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] slot %#lx (idx %#lx) in cnode_bitmap %p is already marked inuse (oldmask %#llx)\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] slot %#lx (idx %#lx) in cnode_bitmap %p is inuse not clear (inusemask %#llx)\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] slot %#lx (idx %#lx) in cnode_bitmap %p is not allocated\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] slot %#lx (idx %#lx) in cnode_bitmap %p is not marked inuse (oldmask %#llx)\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] slot %#lx in cnode_bitmap %p failed to be allocated\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] slot %#lx in cnode_bitmap %p is already marked inuse (oldmask %#llx)\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] slot %#lx in cnode_bitmap %p is was free, but is already marked inuse (oldinuse %#llx)\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] spanmap_lock acquired without nofault set\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] unable to allocate per-thread VAS structure\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] unable to find cnode_bitmap for slot %#lx\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] vascommon->backend->reserve_lock (%p) not held\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] vascore should be initialized by now\n"
+ "[VAS abort in function %s at line %d] attempt to insert cnode %#lx bitmap %p but bitmap %p is in table\n"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
+ "_cnode_bitmap_getfreelist"
+ "_mark_slot_allocated_and_inuse"
+ "_mark_slot_free"
+ "_object_tree_range_free"
+ "_span_map_return"
+ "addrspace_memory_kib.curr."
+ "addrspace_memory_kib.highest."
+ "backend == NULL || backend->cnode_bitmap_alloc == NULL || backend->alloc_cnode == NULL || backend->alloc_perthread == NULL || backend->free_perthread == NULL"
+ "base == 0 || base != ((base >> L4_FrameSizeBits) << L4_FrameSizeBits)"
+ "cnode == NULL"
+ "cnode->allocated_count >= CNODE_SLOT_COUNT"
+ "count <= _object_tree_level_entries(height) - offset"
+ "describe"
+ "fault while XRT__THREAD_NO_FAULTS set (could deadlock)"
+ "level > 1 && vcss->extOver != NULL"
+ "offset < _object_tree_level_entries(height)"
+ "perthread == NULL"
+ "perthread->nCacheCaps > VAS_PERTHREAD_SLOT_CACHE_SIZE"
+ "perthread->nCacheCaps >= VAS_PERTHREAD_SLOT_CACHE_SIZE"
+ "pmmserver"
+ "read"
+ "shmem_memory_kib.curr."
+ "shmem_memory_kib.highest."
+ "tb_connection_control.c"
+ "total_memory_usage_bytes"
+ "unable to allocate slot during thread exit"
+ "v24@?0Q8r^{statsdelegate_statvalue_s=Q(?={?=q}{?=Q}{?=d})}16"
+ "vas__check_common"
+ "vas__perthread_constructor"
+ "vas__perthread_destructor"
+ "vas_core_span_spanmap_lock"
+ "vas_core_span_spanmap_unlock"
+ "vas_perthread_drain"
+ "vas_perthread_fill"
+ "vas_slot_clear_inuse"
+ "vas_slot_free_empty"
+ "vas_slot_mark_inuse"
+ "vascommon->setup_structsize != 0"
+ "vascore_init_constructor"
- "!vascommon->setup"
- "$JgPMMStatsDelegate.PMMStatsDelegate"
- "$JgStatsDelegate.StatsDelegate.init()"
- "/AppleInternal/Library/BuildRoots/4~CNpgugDt6TcCZQtcm_yHFmMdDEvaL-W1C6QCUb0/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "B16@?0^{vas_core_span={?=CQQCCCCC}iC[3C]{?=^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
- "I112@?0{pmmstatsdelegate_pmmstatsdelegate_describe__result_s=C(?=C{pmmstatsdelegate_statdescription_s={pmmstatsdelegate_stattype_s=Q(?={?={pmmstatsdelegate_singlestatinfo_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}{?={pmmstatsdelegate_clientstatinfo_s=Ci{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}{?=C})}{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}8"
- "I24@?0^{statsdelegate_statsdelegate__context_s=^^v^^v}8@?<I@?I>16"
- "I28@?0^{statsdelegate_statsdelegate__context_s=^^v^^v}8I16@?<I@?{pmmstatsdelegate_pmmstatsdelegate_describe__result_s=C(?=C{pmmstatsdelegate_statdescription_s={pmmstatsdelegate_stattype_s=Q(?={?={pmmstatsdelegate_singlestatinfo_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}{?={pmmstatsdelegate_clientstatinfo_s=Ci{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}}{?=C})}{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}>20"
- "I32@?0^{statsdelegate_statsdelegate__context_s=^^v^^v}8I16I20@?<I@?{pmmstatsdelegate_pmmstatsdelegate_read__result_s=C(?=C{pmmstatsdelegate_statvalue_v_s=C(?={?=^{pmmstatsdelegate_statvalue_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}>24"
- "I56@?0{pmmstatsdelegate_pmmstatsdelegate_read__result_s=C(?=C{pmmstatsdelegate_statvalue_v_s=C(?={?=^{pmmstatsdelegate_statvalue_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}8"
- "StatsDelegate"
- "StatsDelegate.StatsDelegate"
- "TB_ASSERT: query->disposition == TB_MESSAGE_DISPOSITION_QUERY, %hhu (%s:%d)\n"
- "TB_FATAL: TB: size 0 buffer during decoding (%s:%d)\n"
- "TB_FATAL: disallowed selector: %llu (%s:%d)\n"
- "TB_FATAL: invalid error returned from describe (%s:%d)\n"
- "TB_FATAL: invalid error returned from read (%s:%d)\n"
- "TB_FATAL: invalid tag in `[PMMStatsDelegate.StatValue]` metadata: 0x%x (%s:%d)\n"
- "Total Memory Usage"
- "Unexpected L4_Error: %s(%zu) err='pmm_alloc_temp_with(vcss->pmm, L4_Type_Arm64_FrameLevel0, dest_frame_cap, fault->rwtmpcap)'"
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]cn %p (%#lx): slot %#lx (idx %#lx) is already marked free\n"
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]cn %p (%#lx): slot %#lx's idx %#lx too big\n"
- "[VAS abort in function %s at line %d] [true: %llx %s %llx]inserting %p @ %lx, but %p is already %lx\n"
- "[VAS abort in function %s at line %d] [true: (%s)] recursion should have been caught above\n"
- "[VAS abort in function %s at line %d] [true: (%s)] split of %p at %#zx succeeded but at least one NULL span %p %p\n"
- "^^v16@?0^^v8"
- "_alloc_frames"
- "_frame_cap_impl"
- "_map_this_frame_internal"
- "_protect_frame"
- "_span_map_frame"
- "backend == NULL || backend->cnode_bitmap_alloc == NULL || backend->alloc_cnode == NULL"
- "first_span == NULL || second_span == NULL"
- "mtx_lock(&mapspan->spanmap_lock)"
- "mtx_lock(&read_span->spanmap_lock)"
- "mtx_lock(&result->spanmap_lock)"
- "mtx_lock(&second_span->spanmap_lock)"
- "mtx_lock(&span_a->spanmap_lock)"
- "mtx_lock(&span_b->spanmap_lock)"
- "mtx_lock(&write_span->spanmap_lock)"
- "mtx_unlock(&mapspan->spanmap_lock)"
- "mtx_unlock(&read_span->spanmap_lock)"
- "mtx_unlock(&result->spanmap_lock)"
- "mtx_unlock(&second_span->spanmap_lock)"
- "mtx_unlock(&span_a->spanmap_lock)"
- "mtx_unlock(&span_b->spanmap_lock)"
- "mtx_unlock(&write_span->spanmap_lock)"
- "v16@?0^^v8"
- "v24@?0Q8r^{pmmstatsdelegate_statvalue_s=Q(?={?=Q}{?=QQ})}16"
- "v24@?0^^v8^^v16"
- "vas_slot_alloc(): created %#x/%#x slots, allocating cnode failed\n"
- "vas_slot_alloc(): created %#x/%#x slots, allocating cnode metadata failed\n"
- "vas_slot_free"
- "vascommon->setup"

```
