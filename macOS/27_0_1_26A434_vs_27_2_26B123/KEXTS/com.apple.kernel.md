## com.apple.kernel

> `com.apple.kernel`

```diff

-13432.1.9.0.0
-  __TEXT.__const: 0x37b50
+13432.41.4.0.0
+  __TEXT.__const: 0x37c10
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0xa67cb
-  __TEXT.__os_log: 0x420fe
+  __TEXT.__cstring: 0xa6f0e
+  __TEXT.__os_log: 0x42597
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
-  __DATA_CONST.__sdt_cstring: 0x7254
-  __DATA_CONST.__sdt: 0xeb80
-  __DATA_CONST.__kalloc_type: 0x17b40
-  __DATA_CONST.__const: 0x130350
-  __DATA_CONST.__assert: 0xe88
+  __DATA_CONST.__sdt_cstring: 0x73b8
+  __DATA_CONST.__sdt: 0xed00
+  __DATA_CONST.__kalloc_type: 0x17b80
+  __DATA_CONST.__const: 0x130448
+  __DATA_CONST.__assert: 0xfa0
   __DATA_CONST.__kalloc_var: 0x7ee0
   __DATA_CONST.__kern_brk_desc: 0x60
   __DATA_CONST.__mod_init_func: 0x2d8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x74000
   __TEXT_EXEC.__exc: 0x1000
-  __TEXT_EXEC.__text: 0x9a2a88
+  __TEXT_EXEC.__text: 0x9a50b8
   __TEXT_EXEC.__hib_text: 0x19c8
   __TEXT_EXEC.__commpage_text: 0x334
   __TEXT_BOOT_EXEC.__bootcode: 0x6ae0

   __DATA.__data: 0x20b89
   __DATA.__lock_grp: 0x17248
   __DATA.__percpu: 0x78d0
-  __DATA.__common: 0x8cdc0
-  __DATA.__bss: 0x49028
+  __DATA.__common: 0x8cea0
+  __DATA.__bss: 0x49128
   __HIBDATA.__data: 0x31
   __HIBDATA.__bss: 0x670
   __HIBDATA.__common: 0x108
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__static_if: 0xe80
-  __BOOTDATA.__init: 0x18140
-  __BOOTDATA.__init_entry_set: 0x147a8
+  __BOOTDATA.__static_if: 0xe90
+  __BOOTDATA.__init: 0x18158
+  __BOOTDATA.__init_entry_set: 0x14868
   __BOOTDATA.__static_ifinit: 0x20
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x507dd
+  __LINKINFO.__symbolsets: 0x5089d
   __CTF.__ctf: 0x0
-  Functions: 22953
-  Symbols:   6947
-  CStrings:  26032
+  Functions: 22980
+  Symbols:   6951
+  CStrings:  26095
 
Symbols:
+ _exclaves_indicator_system_state_change
+ _proc_coalitionids
+ _task_coalition_role_for_type
+ _vfs_context_allows_unmunged_atime
CStrings:
+ "%s: <pid %d> Disallow request nexus with flow divert result\n"
+ "%s: d_from detach pending error %d"
+ "%s: d_to detach pending error %d"
+ "%s: mbuf %p len (%u) < off+len (%u+%u) @%s:%d"
+ "%s: mbuf 0x%llx proto %d IPv6 plen %d (%x) [swapped %d (%x)] doesn't match actual packet length; %u is used instead\n"
+ "%s: rejecting AF_LINK gateway on index %u with unusable link address (nlen %u, alen %u, sdl_len %u)\n"
+ "%s: route %s on %s%d link address does not fit (sdl_alen %u, error %d)\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/xnu/bsd/net/iptap.c"
+ "221111212122222211222221112"
+ "22111220222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220222121222221111111222211111112222211111122222111111222221111112222211222211122211112111111111111"
+ "22212111221122112211102222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220222221111112121111222221112221222222222222221122222112"
+ "Attempt to call task_coalition_role_for_type with invalid coalition_type: %d\n @%s:%d"
+ "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{task_token_data}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQQi{?=QQAQQ}BBBBB^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQ{cpc_task=B}ACBBBBb4b4b4b4CCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b4b12}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b1b1b26}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1b2b1b6c[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}IQQ[16C]Q^{_vmobject_list_output_}II^{vm_deferred_reclamation_metadata_s}QC{task_security_config=(?={?=b1b1b1b3b1b1b1b1b1b1C}I)}}8"
+ "FilterDropBadDirection"
+ "Memory error logging started\n"
+ "RETRY SESSION (Signing Identifier Drop)"
+ "SK[%u]: %-30s %s(%d): %d: skip cls_len < l3hlen + l4hlen\n"
+ "SK[%u]: %-30s %s(%d): EINVAL: SYNCF_ALLOC_BUF without buflet alloc ring\n"
+ "SK[%u]: %-30s %s(%d): EINVAL: SYNCF_LARGE_ALLOC with SYNCF_ALLOC/ALLOC_BUF\n"
+ "SK[%u]: %-30s %s(%d): EINVAL: SYNCF_LARGE_ALLOC without large buffer alloc ring\n"
+ "SK[%u]: %-30s %s(%d): EINVAL: unknown flags 0x%x\n"
+ "SK[%u]: %-30s Tx flow port %d != channel port %d, %s\n"
+ "SK[%u]: %-30s dropped packet injected on ring %u whose wrap flag does not match the ring direction: pkt_pflags 0x%llx\n"
+ "SK[%u]: %-30s filter packet is not mbuf-wrapped: pkt_pflags 0x%llx\n"
+ "SK[%u]: %-30s filter packet is not packet-wrapped: pkt_pflags 0x%llx\n"
+ "The lifetime number of pages freed while still on the speculative queue outside of pageout scan"
+ "The lifetime number of pages that already held content and were put on the speculative queue rather than filled speculatively"
+ "The lifetime number of times pageout scan took a page off the speculativequeue as a reclaim candidate and put it on the inactive queue"
+ "VM entry %p lock shared lock overflow <v:%d c:%c%c w:%c%c %c/%d> @%s:%d"
+ "_dtlecnt != 0"
+ "_in6m->in6m_in_dtle == true"
+ "_inm->inm_in_dtle == true"
+ "bad__direction"
+ "bklb-backlight-dc"
+ "bklb-backlight-frequency"
+ "com.apple.private.verified-jit-mode"
+ "com.apple.security.cs.debugger"
+ "entry != ((void*)0)"
+ "entry != NULL"
+ "iBoot reported a total memory size of 0x%llx, below the 0x%llx bytes it handed to XNU @%s:%d"
+ "ifnet_detach failed: %d @%s:%d"
+ "inconsistent DRAM size reported by iBoot: dram-size 0x%llx, memSizeActual 0x%llx @%s:%d"
+ "inm->in6m_dtlecnt != 0"
+ "inm->inm_dtlecnt != 0"
+ "ipc_misc.c"
+ "ipr != ((void*)0)"
+ "iptap != NULL"
+ "mac__call__exc_action_check_exception_send2"
+ "mac__call__proc_notify_sigaction"
+ "mac__call__thread_check_set_state"
+ "mac__call__vnode_notify_begin_rename_swap"
+ "mac__call__vnode_notify_end_rename_swap"
+ "mac__rslt__exc_action_check_exception_send2"
+ "mac__rslt__proc_notify_sigaction"
+ "mac__rslt__thread_check_set_state"
+ "mac__rslt__vnode_notify_begin_rename_swap"
+ "mac__rslt__vnode_notify_end_rename_swap"
+ "memory override is too small to boot; check the maxmem/memsize boot-args @%s:%d"
+ "memsize=%u MB leaves no memory for XNU/SPTM to manage: the iBoot carveouts alone are %llu MB @%s:%d"
+ "necp_set_socket_resolver_signature_from_parameters"
+ "not__mbuf__wrapped"
+ "not__pkt__wrapped"
+ "nx_netif_filter_pkt_to_mbuf"
+ "nx_netif_filter_pkt_to_pkt"
+ "pktap != NULL"
+ "pktap_build_mbuf_header"
+ "prev_entry != ((void*)0)"
+ "process v1 report %s on ifp 0x%llx(%s)\n"
+ "rt_setgate"
+ "site.struct flow_divert_pcb_handle"
+ "size <= sdl->sdl_alen"
+ "speculative_pages_demoted"
+ "speculative_pages_freed"
+ "speculative_pages_requeued_inactive"
+ "table != ((void*)0)"
+ "v12@?0B8"
+ "v28@?0^{vm_page=(?={vm_page_packed_queue_entry=II}^{vm_page}){vm_page_packed_queue_entry=II}{vm_page_packed_queue_entry=II}IIQ(?=SS){?=b4b2b1b1}{?=b1b1b1b1b1b1b1b1}{?=b2b1b1b1b1b1b1}{?=b1b1b1b1b1b1b1b1}{?=b4b4b4b1b1b1b1}[0C]QS(?=(vmp_lock={?=CC}S))(?=II)}8I16@?<v@?B>20"
- "%s: mbuf %p len (%d) < off+len (%d+%d) @%s:%d"
- "%s: mbuf 0x%llx proto %d IPv6 plen %d (%x) [swapped %d (%x)] doesn't match actual packet length; %d is used instead\n"
- "2211112121222222111222221112"
- "221112202222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222221111111222211111112222211111122222111111222221111112222211222211122211112111111111111"
- "222121112211221122111022222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111112121111222221112221222222222222221122222112"
- "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{task_token_data}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQQi{?=QQAQQ}BBBBB^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQ{cpc_task=B}ACBBBBb4b4b4b4CCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b4b12}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b1b1b26}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1b2b1b6[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}IQQ[16C]Q^{_vmobject_list_output_}II^{vm_deferred_reclamation_metadata_s}QC{task_security_config=(?={?=b1b1b1b3b1b1b1b1b1b1C}I)}}8"
- "External objects are not implemented for CoW. %p %i %i %llx %llx @%s:%d"
- "mac__call__vnode_notify_will_rename_swap"
- "mac__rslt__vnode_notify_will_rename_swap"
- "pktap_bpf_tap"
- "protect_privileged_from_untrusted"
- "sdl->sdl_alen == size"
- "utun_flowswitch_attach - ifnet_detach failed: %d @%s:%d"
- "vm_protect_privileged_from_untrusted"
```
