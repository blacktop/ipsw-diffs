## kernel

> `/System/Library/Kernels/kernel`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__got`
- `__KLDDATA.__const`
- `__KLDDATA.__static_ifinit`
- `__KLDDATA.__mod_init_func`
- `__KLDDATA.__mod_term_func`
- `__LASTDATA_CONST.__mod_init_func`

```diff

-13432.1.9.0.0
-  __TEXT.__text: 0x9055f0
-  __TEXT.__const: 0x45780
-  __TEXT.__os_log: 0x4c2eb
-  __TEXT.__cstring: 0xa356d
+13432.40.144.0.1
+  __TEXT.__text: 0x909520
+  __TEXT.__const: 0x45830
+  __TEXT.__os_log: 0x4c64b
+  __TEXT.__cstring: 0xa3a6d
   __TEXT.__eh_frame: 0x118
   __DATA.__lock_grp: 0x16578
-  __DATA.__data: 0x82bc0
+  __DATA.__data: 0x82c00
   __DATA.__percpu: 0x3e28
-  __DATA.__common: 0x1bddb0
-  __DATA_CONST.__const: 0xa3948
-  __DATA_CONST.__kalloc_type: 0x17b00
+  __DATA.__common: 0x1bde00
+  __DATA_CONST.__const: 0xa3b88
+  __DATA_CONST.__kalloc_type: 0x17b40
   __DATA_CONST.__kalloc_var: 0x7ee0
-  __DATA_CONST.__assert: 0xe4c
+  __DATA_CONST.__assert: 0xf64
   __DATA_CONST.__kern_brk_desc: 0x60
-  __DATA_CONST.__sdt_cstring: 0x7232
-  __DATA_CONST.__sdt: 0xf348
+  __DATA_CONST.__sdt_cstring: 0x7362
+  __DATA_CONST.__sdt: 0xf4c8
   __DATA_CONST.__mod_init_func: 0x2c8
   __DATA_CONST.__got: 0x58
-  __KLDDATA.__init: 0x11d40
-  __KLDDATA.__init_entry_set: 0x14448
+  __KLDDATA.__init: 0x11d58
+  __KLDDATA.__init_entry_set: 0x14520
   __KLDDATA.__const: 0x9470
   __KLDDATA.__static_ifinit: 0x8
   __KLDDATA.__cstring: 0x79c

   __LASTDATA_CONST.__mod_init_func: 0x8
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
-  __LINKINFO.__symbolsets: 0x4e2fa
-  __CTF.__ctf: 0xd3d95
-  Functions: 27124
-  Symbols:   24380
-  CStrings:  26059
+  __LINKINFO.__symbolsets: 0x4e34d
+  __CTF.__ctf: 0xd458a
+  Functions: 27152
+  Symbols:   24399
+  CStrings:  26103
 
Symbols:
+ __ZN9IOService49exclaveRegisterANEUpcallUpdateXnuContentWithFlagsEPNS_19IOExclaveProxyStateEU13block_pointerFyyyyyE
+ ___vm_page_speculative_demoted_early_storage
+ ___vm_page_speculative_freed_early_storage
+ ___vm_page_speculative_requeued_inactive_early_storage
+ _in6_tmpaddr_note_removal
+ _in6_tmpaddr_reuse
+ _in6_tmpaddr_update
+ _mac_proc_notify_sigaction
+ _mac_thread_check_set_state
+ _mac_vnode_notify_begin_rename_swap
+ _mac_vnode_notify_end_rename_swap
+ _rt_gateway_lladdr_copyout
+ _upl_object_range
+ _upl_set_phys_page
+ _vm_object_get_locked_copy
+ _vm_object_release_locked_copy
+ _vm_page_push_to_copy
+ _vm_page_speculative_demoted
+ _vm_page_speculative_freed
+ _vm_page_speculative_requeued_inactive
- _mac_vnode_notify_will_rename_swap
CStrings:
+ "%s: d_from detach pending error %d"
+ "%s: d_to detach pending error %d"
+ "%s: mbuf %p len (%u) < off+len (%u+%u) @%s:%d"
+ "%s: mbuf 0x%llx proto %d IPv6 plen %d (%x) [swapped %d (%x)] doesn't match actual packet length; %u is used instead\n"
+ "%s: rejecting AF_LINK gateway on index %u with unusable link address (nlen %u, alen %u, sdl_len %u)\n"
+ "%s: route %s on %s%d link address does not fit (sdl_alen %u, error %d)\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/xnu/bsd/net/iptap.c"
+ "221111212122222211222221112"
+ "RETRY SESSION (Signing Identifier Drop)"
+ "SK[%u]: %-30s %s(%d): %d: skip cls_len < l3hlen + l4hlen\n"
+ "SK[%u]: %-30s %s(%d): EINVAL: SYNCF_ALLOC_BUF without buflet alloc ring\n"
+ "SK[%u]: %-30s %s(%d): EINVAL: SYNCF_LARGE_ALLOC with SYNCF_ALLOC/ALLOC_BUF\n"
+ "SK[%u]: %-30s %s(%d): EINVAL: SYNCF_LARGE_ALLOC without large buffer alloc ring\n"
+ "SK[%u]: %-30s %s(%d): EINVAL: unknown flags 0x%x\n"
+ "The lifetime number of pages freed while still on the speculative queue outside of pageout scan"
+ "The lifetime number of pages that already held content and were put on the speculative queue rather than filled speculatively"
+ "The lifetime number of times pageout scan took a page off the speculativequeue as a reclaim candidate and put it on the inactive queue"
+ "VM entry %p lock shared lock overflow <v:%d c:%c%c w:%c%c %c/%d> @%s:%d"
+ "_dtlecnt != 0"
+ "_in6m->in6m_in_dtle == true"
+ "_inm->inm_in_dtle == true"
+ "com.apple.private.enable-coredump-on-panic-seed-privacy-approved"
+ "entry != ((void*)0)"
+ "entry != NULL"
+ "ifnet_detach failed: %d @%s:%d"
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
+ "v28@?0^{vm_page=(?={vm_page_packed_queue_entry=II}^{vm_page}){vm_page_packed_queue_entry=II}{vm_page_packed_queue_entry=II}IIQ(?=SS){?=b4b2b1b1}{?=b1b1b1b1b1b1b1b1}{?=b2b1b1b1b1b1b1}{?=b1b1b1b1b1b1b1b1}{?=b4b4b4b1b1b1b1}[0C]I}8I16@?<v@?B>20"
- "%s: mbuf %p len (%d) < off+len (%d+%d) @%s:%d"
- "%s: mbuf 0x%llx proto %d IPv6 plen %d (%x) [swapped %d (%x)] doesn't match actual packet length; %d is used instead\n"
- "2211112121222222111222221112"
- "External objects are not implemented for CoW. %p %i %i %llx %llx @%s:%d"
- "mac__call__vnode_notify_will_rename_swap"
- "mac__rslt__vnode_notify_will_rename_swap"
- "pktap_bpf_tap"
- "sdl->sdl_alen == size"
- "utun_flowswitch_attach - ifnet_detach failed: %d @%s:%d"
```
