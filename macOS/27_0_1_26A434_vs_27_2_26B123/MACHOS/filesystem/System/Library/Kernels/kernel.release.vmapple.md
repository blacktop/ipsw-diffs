## kernel.release.vmapple

> `/System/Library/Kernels/kernel.release.vmapple`

### Sections with Same Size but Changed Content

- `__TEXT.__copyio_vectors`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__KLDDATA.__const`
- `__KLDDATA.__mod_init_func`
- `__KLDDATA.__mod_term_func`
- `__DATA.__data`
- `__BOOTDATA.__static_ifinit`

```diff

-13432.1.9.0.0
-  __TEXT.__const: 0x37610
+13432.41.4.0.0
+  __TEXT.__const: 0x376c0
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0x9da62
-  __TEXT.__os_log: 0x41d91
+  __TEXT.__cstring: 0x9e065
+  __TEXT.__os_log: 0x4222a
   __TEXT.__thread_starts: 0x0
   __TEXT.__eh_frame: 0x6b0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x1a2308
-  __DATA_CONST.__sdt_cstring: 0x71f2
-  __DATA_CONST.__sdt: 0xeb50
-  __DATA_CONST.__kalloc_type: 0x178c0
-  __DATA_CONST.__assert: 0xe38
+  __DATA_CONST.__const: 0x1a2400
+  __DATA_CONST.__sdt_cstring: 0x7356
+  __DATA_CONST.__sdt: 0xecd0
+  __DATA_CONST.__kalloc_type: 0x17900
+  __DATA_CONST.__assert: 0xf50
   __DATA_CONST.__kalloc_var: 0x7da0
   __DATA_CONST.__kern_brk_desc: 0x60
   __DATA_CONST.__mod_init_func: 0x2d0
   __DATA_CONST.__auth_ptr: 0x10
   __TEXT_EXEC.__exc: 0x1000
-  __TEXT_EXEC.__text: 0x984f78
+  __TEXT_EXEC.__text: 0x989b34
   __TEXT_EXEC.__hib_text: 0x10b8
   __TEXT_EXEC.__commpage_text: 0x334
   __KLD.__text: 0xb118

   __DATA.__data: 0x20999
   __DATA.__lock_grp: 0x16058
   __DATA.__percpu: 0x39d0
-  __DATA.__common: 0x89e20
-  __DATA.__bss: 0x49ad0
+  __DATA.__common: 0x89f20
+  __DATA.__bss: 0x49cd0
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__static_if: 0xd70
-  __BOOTDATA.__init: 0x17c50
-  __BOOTDATA.__init_entry_set: 0x13fe0
+  __BOOTDATA.__static_if: 0xd80
+  __BOOTDATA.__init: 0x17c68
+  __BOOTDATA.__init_entry_set: 0x140a0
   __BOOTDATA.__static_ifinit: 0x20
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x50330
-  __CTF.__ctf: 0xf910e
-  Functions: 22173
-  Symbols:   6925
-  CStrings:  25195
+  __LINKINFO.__symbolsets: 0x503f0
+  __CTF.__ctf: 0xf9b7e
+  Functions: 22196
+  Symbols:   6929
+  CStrings:  25255
 
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
+ "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{task_token_data}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQC{?=QQAQQ}BBBB^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQACBBBBb4b4b4b4CCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b4b12}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b1b1b26}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1b2b1b6c[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}IQQ[16C]Q^{_vmobject_list_output_}II^{vm_deferred_reclamation_metadata_s}QC{task_security_config=(?={?=b1b1b1b3b1b1b1b1b1b1C}I)}}8"
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
+ "memsize=%u MB leaves no memory for XNU to manage: the iBoot carveouts alone are %llu MB @%s:%d"
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
- "%s: mbuf %p len (%d) < off+len (%d+%d) @%s:%d"
- "%s: mbuf 0x%llx proto %d IPv6 plen %d (%x) [swapped %d (%x)] doesn't match actual packet length; %d is used instead\n"
- "2211112121222222111222221112"
- "221112202222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222221111111222211111112222211111122222111111222221111112222211222211122211112111111111111"
- "222121112211221122111022222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111112121111222221112221222222222222221122222112"
- "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{task_token_data}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQC{?=QQAQQ}BBBB^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQACBBBBb4b4b4b4CCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b4b12}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b1b1b26}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1b2b1b6[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}IQQ[16C]Q^{_vmobject_list_output_}II^{vm_deferred_reclamation_metadata_s}QC{task_security_config=(?={?=b1b1b1b3b1b1b1b1b1b1C}I)}}8"
- "External objects are not implemented for CoW. %p %i %i %llx %llx @%s:%d"
- "mac__call__vnode_notify_will_rename_swap"
- "mac__rslt__vnode_notify_will_rename_swap"
- "pktap_bpf_tap"
- "protect_privileged_from_untrusted"
- "sdl->sdl_alen == size"
- "utun_flowswitch_attach - ifnet_detach failed: %d @%s:%d"
- "vm_protect_privileged_from_untrusted"
```
