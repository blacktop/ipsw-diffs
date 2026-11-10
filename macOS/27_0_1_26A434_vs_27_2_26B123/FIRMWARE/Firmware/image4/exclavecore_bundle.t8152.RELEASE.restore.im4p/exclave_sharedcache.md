## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8152.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__DATA.__thread_vars`
- `__PDATA.__auth_ptr`
- `__PDATA.__mod_init_func`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.0.27.0.0
-  __TEXT.__text: 0x5391e4
+1777.40.37.0.0
+  __TEXT.__text: 0x543ee4
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0x48be1
-  __TEXT.__const: 0x116454
-  __TEXT.__swift5_typeref: 0x107bc
-  __TEXT.__swift5_reflstr: 0xc6b8
-  __TEXT.__swift5_assocty: 0x71f0
-  __TEXT.__swift5_fieldmd: 0x15160
-  __TEXT.__constg_swiftt: 0x20c20
-  __TEXT.__swift5_protos: 0x764
-  __TEXT.__swift5_proto: 0x31cc
-  __TEXT.__swift5_types: 0x1d04
+  __TEXT.__cstring: 0x499a1
+  __TEXT.__const: 0x1176d4
+  __TEXT.__swift5_typeref: 0x10940
+  __TEXT.__swift5_reflstr: 0xd568
+  __TEXT.__swift5_assocty: 0x7388
+  __TEXT.__swift5_fieldmd: 0x158ec
+  __TEXT.__constg_swiftt: 0x21100
+  __TEXT.__swift5_protos: 0x774
+  __TEXT.__swift5_proto: 0x3274
+  __TEXT.__swift5_types: 0x1d48
   __TEXT.__swift5_types2: 0x5c
   __TEXT.__swift5_builtin: 0x12ac
-  __TEXT.__swift5_capture: 0xd6c
-  __TEXT.__objc_methtype: 0xe1
+  __TEXT.__swift5_capture: 0xdbc
+  __TEXT.__objc_methtype: 0x111
   __TEXT.__swift5_mpenum: 0x2a8
-  __TEXT.__swift_as_entry: 0x990
-  __TEXT.__swift_as_ret: 0xb04
-  __TEXT.__swift_as_cont: 0x11e8
+  __TEXT.__swift_as_entry: 0x9ac
+  __TEXT.__swift_as_ret: 0xb28
+  __TEXT.__swift_as_cont: 0x1214
   __TEXT.__swift5_entry: 0x8
   __TEXT.__oslogstring: 0xeb
   __TEXT.__constructor: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xa8
-  __TEXT.__eh_frame: 0x2e320
+  __TEXT.__eh_frame: 0x2ecd8
   __DATA.__TIGHTBEAM_VT: 0x6f0
   __DATA.__TIGHTBEAM: 0x1c8
-  __DATA.__const: 0x322f0
-  __DATA.__data: 0x127f0
+  __DATA.__const: 0x32d40
+  __DATA.__data: 0x12b68
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1a328
-  __DATA.__auth_ptr: 0x19f8
+  __DATA.__ENDPOINTS: 0x1a84b
+  __DATA.__auth_ptr: 0x1a58
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x380
   __DATA.__DARTS: 0x93f

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__bss: 0xd8e0
+  __DATA.__bss: 0xd8f0
   __DATA.__common: 0x57a
   __PDATA.__auth_ptr: 0x280
-  __PDATA.__const: 0x67b0
+  __PDATA.__const: 0x6810
   __PDATA.__objc_imageinfo: 0x8
   __PDATA.__mod_init_func: 0x18
   __PDATA.__data: 0x2af0
   __PDATA.__ENDPOINTS: 0x838
   __PDATA.__shared_cache: 0x70
-  __PDATA.__bss: 0xba48
+  __PDATA.__bss: 0xbae8
   __PDATA.__common: 0x2578
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   Functions: 652
   Symbols:   1
-  CStrings:  6613
+  CStrings:  6676
 
Functions:
~ sub_7ffe468 : 141632 -> 141224
~ sub_8020db8 -> sub_8020c20 : 14556 -> 14632
~ sub_8024694 -> sub_8024548 : 424404 -> 428048
~ sub_808c068 -> sub_808cd58 : 170752 -> 171232
~ sub_80b5ce0 -> sub_80b6bb0 : 224 -> 208
~ sub_80b9968 -> sub_80ba828 : 140604 -> 140336
~ sub_80e7b84 -> sub_80e8938 : 62956 -> 62296
~ sub_80f7170 -> sub_80f7c90 : 26312 -> 26364
~ sub_80fde48 -> sub_80fe99c : 8624 -> 8788
~ sub_8104e60 -> sub_8105a58 : 21632 -> 21620
~ sub_8110354 -> sub_8110f40 : 47904 -> 48400
~ sub_8127508 -> sub_81282e4 : 1096 -> 1108
~ sub_8127950 -> sub_8128738 : 15212 -> 15228
~ sub_812c788 -> sub_812d580 : 305468 -> 307348
~ sub_818b5b8 -> sub_818cb08 : 324628 -> 336556
~ sub_81dc20c -> sub_81e05f4 : 15956 -> 16116
~ sub_81f5654 -> sub_81f9adc : 582792 -> 599612
~ sub_828b4a4 -> sub_8293ae0 : 33004 -> 33008
~ sub_829bf28 -> sub_82a4568 : 10620 -> 10624
~ sub_829eb50 -> sub_82a7194 : 208 -> 188
~ sub_829ed7c -> sub_82a73ac : 1112 -> 1172
~ sub_829f250 -> sub_82a78bc : 392 -> 408
~ sub_829f3d8 -> sub_82a7a54 : 208 -> 232
~ sub_829f4a8 -> sub_82a7b3c : 608 -> 624
~ sub_829f7e0 -> sub_82a7e84 : 964 -> 988
~ sub_829fba4 -> sub_82a8260 : 1180 -> 1276
~ sub_82a006c -> sub_82a8788 : 644 -> 628
~ sub_82a02f0 -> sub_82a89fc : 2948 -> 2936
~ sub_82a0e74 -> sub_82a9574 : 32688 -> 32720
~ sub_82bf0a0 -> sub_82c77c0 : 6456 -> 6860
~ sub_82c4870 -> sub_82cd124 : 27264 -> 27280
~ sub_82f4340 -> sub_82fcc04 : 11564 -> 11568
~ sub_8334d58 -> sub_833d620 : 42848 -> 42852
~ sub_833f4b8 -> sub_8347d84 : 32196 -> 32200
~ sub_8379b0c -> sub_83823dc : 24400 -> 24412
~ sub_839899c -> sub_83a1278 : 45864 -> 45936
~ sub_83a3cc4 -> sub_83ac5e8 : 31728 -> 31732
~ sub_83af864 -> sub_83b818c : 25344 -> 24516
~ sub_83d525c -> sub_83dd848 : 23204 -> 23148
~ sub_83e9f98 -> sub_83f254c : 7504 -> 7560
~ sub_83ebce8 -> sub_83f42d4 : 8496 -> 8500
~ sub_83ede18 -> sub_83f6408 : 163664 -> 163596
~ sub_842d98c -> sub_8435f38 : 15984 -> 16084
~ sub_844efb4 -> sub_84575c4 : 11644 -> 11668
~ sub_8453868 -> sub_845be90 : 9332 -> 9308
~ sub_845c530 -> sub_8464b40 : 984 -> 964
~ sub_845c908 -> sub_8464f04 : 188 -> 208
~ sub_845d694 -> sub_8465ca4 : 1464 -> 1488
~ sub_845dcc4 -> sub_84662ec : 228 -> 252
~ sub_845e008 -> sub_8466648 : 72 -> 60
~ sub_845e068 -> sub_846669c : 108 -> 132
~ sub_845eda8 -> sub_84673f4 : 900 -> 888
~ sub_845f12c -> sub_846776c : 392 -> 404
~ sub_845f2b4 -> sub_8467900 : 216 -> 240
~ sub_845f43c -> sub_8467aa0 : 120 -> 108
~ sub_845f784 -> sub_8467ddc : 896 -> 884
~ sub_845fb04 -> sub_8468150 : 460 -> 472
~ sub_8460744 -> sub_8468d9c : 884 -> 872
~ sub_8460c18 -> sub_8469264 : 996 -> 1044
~ sub_846114c -> sub_84697c8 : 992 -> 960
~ sub_846152c -> sub_8469b88 : 448 -> 468
~ sub_8461704 -> sub_8469d74 : 356 -> 376
~ sub_8461868 -> sub_8469eec : 1548 -> 1532
~ sub_8462248 -> sub_846a8bc : 152 -> 168
~ sub_84622e0 -> sub_846a964 : 136 -> 100
~ sub_8462368 -> sub_846a9c8 : 368 -> 384
~ sub_8462790 -> sub_846ae00 : 1248 -> 1260
~ sub_8462c70 -> sub_846b2ec : 844 -> 856
~ sub_8462fbc -> sub_846b644 : 520 -> 496
~ sub_84631c4 -> sub_846b834 : 300 -> 312
~ sub_8463504 -> sub_846bb80 : 492 -> 524
~ sub_8463740 -> sub_846bddc : 736 -> 800
~ sub_8463a20 -> sub_846c0fc : 1144 -> 1080
~ sub_8464178 -> sub_846c814 : 320 -> 288
~ sub_8465524 -> sub_846dba0 : 64 -> 52
~ sub_8465564 -> sub_846dbd4 : 148 -> 160
~ sub_84655f8 -> sub_846dc74 : 264 -> 240
~ sub_8465bc8 -> sub_846e22c : 1696 -> 1672
~ sub_84665a8 -> sub_846ebf4 : 1624 -> 1548
~ sub_8466c00 -> sub_846f200 : 536 -> 612
~ sub_8466e18 -> sub_846f464 : 160 -> 104
~ sub_8466ee8 -> sub_846f4fc : 48 -> 72
~ sub_8466f18 -> sub_846f544 : 1608 -> 1660
~ sub_8467664 -> sub_846fcc4 : 548988 -> 549152
~ sub_84efdcc -> sub_84f84d0 : 285236 -> 294960
CStrings:
+ "  Quick start = "
+ " message to SEP. ane_id: "
+ " succeeded for ane_id "
+ " will start once sensor sessions are resumed"
+ "$JgExclaveSEPManager.ExclaveSEPANEControlEndpoint"
+ "%s(%zu): failed to delete delta scratch RO span slot"
+ "%s(%zu): failed to delete delta scratch RO temp cap"
+ "%s(%zu): failed to map frame into delta scratch RO span"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.2.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "ANE power op returned unknown status byte: "
+ "Active pause requests: "
+ "Adding pause request: "
+ "B16@?0^{vas_core_span={?=CQQCCCCC^vQ}iC[3C]{?=^?^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}B{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
+ "BUG IN LIBTRACE: log payload "
+ "Builtin.Borrow is not supported in runtime type lookup"
+ "Failed to get frames from region "
+ "I14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "I28@?0Q8I16@?<I@?{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}>20"
+ "Ignoring duplicate pause request: "
+ "Ignoring pause request due to non-enforcing mode: "
+ "Ignoring pause request since ISP watchdog is disabled: "
+ "Ignoring pause request since health checks are disabled: "
+ "Initialized count must be in 0 ... unsafeUninitializedCapacity."
+ "Invalid key value while decoding result type for hold_ane_power_assertion"
+ "Invalid key value while decoding result type for release_ane_power_assertion"
+ "Invalid key value while decoding result type for unloadMemoryWithFlags"
+ "Invalid key value while decoding result type for updateXnuContentWithFlags"
+ "Log payload exceeds "
+ "Quick start policy resolved @ GLTB "
+ "Quick start policy violated @ GLTB "
+ "Removed pause request: "
+ "Start not allowed: camera disabled by EDT policy"
+ "Starting quick start policy @ GLTB "
+ "Status not allowed: camera disabled by EDT policy"
+ "TB_FATAL: invalid result returned from unmapXnuContentRegionWithFlags (%s:%d)\n"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(scratch->ro_span_slot)'"
+ "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(scratch->ro_temp_slot)'"
+ "Unexpected L4_Error: %s(%zu) err='_map_this_frame_readonly(scratch->ro_span, (uintptr_t)ro_words, scratch->ro_temp_slot)'"
+ "VIOLATION: CIL never came on during quick start policy"
+ "[LogServer] error: "
+ "[VAS abort in function %s at line %d] [%s] could not allocate fixup span for fault handler\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] Could not depopulate temp span (drop): %s (0x%04hx)\n\n"
+ "[VAS abort in function %s at line %d] [true: (%s)] _delta_page_against_original returned unexpected result(%p)\n"
+ "]\n  defaultDisplayChanged: triggered="
+ "])\n  deviceStateDisplayWake: allowance="
+ "])\n  quickStart: allowance="
+ "_delta_page_against_original"
+ "_insecure_random_buf"
+ "_os_log_payload_size(olp), OS_LOG_EXCLAVES_PAYLOAD_MAX"
+ "applyFixups: rebase failed for %#lx (region %zd)"
+ "applyFixups: region %zd has NULL fixup_metadata_pointer"
+ "delta_output != fault->write_buffer"
+ "fpwm-frequency-hz"
+ "hold_ane_power_assertion threw an unexpected error type"
+ "i24@?0^{?=^{thread}}8^{thread={allocation=^{allocation_map}{?=s}{?=AC}^{allocation}}QCQQQ^{?}(?={?=^{thread}^^{thread}}{heap_element=^{?}{?=^{thread}}{?=^{thread}}Q})^{turnstile}{?={?=CQ}Q}QQQ{inherit_set=^{turnstile}}{?={?=s}Q}QQQCS}16"
+ "invalid rawValue for ExclaveSEPANEControlEndpoint.Selector "
+ "invalid rawValue for SensorPauseReason: "
+ "invalid rawValue for XnuContentANEFlags: unexpected bits in value, "
+ "invalid rawValue for XnuContentUnloadFlags: unexpected bits in value, "
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:982)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8903)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8331)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7872)"
+ "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6854)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2216)"
+ "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5356)"
+ "ms\n  displayPower: triggered="
+ "octopus_no_quick_start"
+ "octopus_quick_start"
+ "olp->olp_tpb.tp_size, OS_LOG_EXCLAVES_TRACEPOINT_HDR_SIZE"
+ "policy-sil-disable"
+ "quick-start-allowance"
+ "release_ane_power_assertion threw an unexpected error type"
+ "s[0] || s[1]"
+ "sharedmem_framemap_getPhysicalAddress"
+ "sharedmem_framemap_setMapped_delta"
+ "sil-disable-config"
+ "sil-disable-offset"
+ "total_memory_usage_bytes"
+ "unmapXnuContentRegionWithFlags"
+ "updateXnuContent(refId:ranges:flags:)"
+ "v14@?0{easm_space_unmapxnucontentregionwithflags__result_s=C(?={easm_failure_s=CS})}8"
+ "v24@?0{sharedmem_pagerange=QQ}8"
+ "vas__easm_unmap_xnu_content_region_with_flags"
+ "vas_return_code(drop_depop) != VAS_SUCCESS"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.0.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "B16@?0^{vas_core_span={?=CQQCCCCC^vQ}iC[3C]{?=^?^?}^vQQ^{vas_core_vas}^{vas_core_span}^{vas_core_span}Q^{vas_segment}{spanmap_struct=b2b4b22b36}{_liblibc_mtx=[16C]}B{?=^{vas_core_span}^^{vas_core_span}}{spanmap_struct=b2b4b22b36}}8"
- "BUG IN LIBTRACE: Received a BATCH_ERROR while creating a LogBatch"
- "Initialized count set to greater than specified capacity."
- "[B] Start Siri dark wake policy"
- "[B] Stop Siri dark wake policy"
- "_os_log_payload_size(olp), OS_LOG_PAYLOAD_HARD_MAX_SIZE"
- "i24@?0^{?=^{thread}}8^{thread={allocation=^{allocation_map}{?=s}{?=AC}^{allocation}}QCQQQ^{?}(?={?=^{thread}^^{thread}}{heap_element=^{?}{?=^{thread}}{?=^{thread}}Q})^{turnstile}{?={?=CQ}Q}QQQ{inherit_set=^{turnstile}}{?={?=s}{?=s}}QQQCS}16"
- "localmap_map(%zx): localmap() remap with changed PA (%llx != %llx)\n"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:981)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8865)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8293)"
- "malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7834)"
- "malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6830)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2197)"
- "malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5336)"
- "olp->olp_tpb.tp_size, OS_LOG_PAYLOAD_HDR_SIZE"
- "sharedmem_framemap_getPhysicalAddresses"
- "sharedmem_framemap_setMapped"
- "total_memory_kib"
- "v14@?0{easm_space_unmapxnucontentregion__result_s=C(?={easm_failure_s=CS})}8"
- "vas__easm_unmap_xnu_content_region"
```
