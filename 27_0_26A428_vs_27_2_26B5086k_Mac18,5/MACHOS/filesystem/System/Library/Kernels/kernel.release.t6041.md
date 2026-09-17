## kernel.release.t6041

> `/System/Library/Kernels/kernel.release.t6041`

### Sections with Same Size but Changed Content

- `__TEXT.__copyio_vectors`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__hib_const`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__LASTDATA_CONST.__mod_init_func`
- `__KLDDATA.__const`
- `__KLDDATA.__mod_init_func`
- `__KLDDATA.__mod_term_func`
- `__DATA.__data`
- `__HIBDATA.__data`
- `__BOOTDATA.__static_ifinit`

```diff

-13432.1.9.0.0
-  __TEXT.__const: 0x37b60
+13432.40.144.0.1
+  __TEXT.__const: 0x37c20
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0xa77f2
-  __TEXT.__os_log: 0x4259c
+  __TEXT.__cstring: 0xa7f06
+  __TEXT.__os_log: 0x42886
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
-  __DATA_CONST.__sdt_cstring: 0x7254
-  __DATA_CONST.__sdt: 0xeb50
-  __DATA_CONST.__kalloc_type: 0x17b40
-  __DATA_CONST.__const: 0x130aa8
-  __DATA_CONST.__assert: 0xe9c
+  __DATA_CONST.__sdt_cstring: 0x7384
+  __DATA_CONST.__sdt: 0xecb8
+  __DATA_CONST.__kalloc_type: 0x17b80
+  __DATA_CONST.__const: 0x130bc8
+  __DATA_CONST.__assert: 0xfb4
   __DATA_CONST.__kalloc_var: 0x7f80
-  __DATA_CONST.__kern_brk_desc: 0x60
+  __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_CONST.__mod_init_func: 0x2d8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x74000
   __TEXT_EXEC.__exc: 0x1000
-  __TEXT_EXEC.__text: 0x9ab9d0
+  __TEXT_EXEC.__text: 0x9acee8
   __TEXT_EXEC.__hib_text: 0x19cc
   __TEXT_EXEC.__commpage_text: 0x334
   __TEXT_BOOT_EXEC.__bootcode: 0x6b04

   __DATA.__data: 0x20b89
   __DATA.__lock_grp: 0x17390
   __DATA.__percpu: 0x6730
-  __DATA.__common: 0x91920
+  __DATA.__common: 0x91a00
   __HIBDATA.__data: 0x31
   __HIBDATA.__bss: 0x670
   __HIBDATA.__common: 0x108
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__static_if: 0x10e0
-  __BOOTDATA.__init: 0x221b8
-  __BOOTDATA.__init_entry_set: 0x14928
+  __BOOTDATA.__static_if: 0x10f0
+  __BOOTDATA.__init: 0x221d0
+  __BOOTDATA.__init_entry_set: 0x14a00
   __BOOTDATA.__static_ifinit: 0x20
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x507dd
-  __CTF.__ctf: 0x10a75d
-  Functions: 23005
-  Symbols:   6947
-  CStrings:  26170
+  __LINKINFO.__symbolsets: 0x50830
+  __CTF.__ctf: 0x10b326
+  Functions: 23027
+  Symbols:   6949
+  CStrings:  26221
 
Symbols:
+ _proc_coalitionids
+ _task_coalition_role_for_type
CStrings:
+ "%s: d_from detach pending error %d"
+ "%s: d_to detach pending error %d"
+ "%s: mbuf %p len (%u) < off+len (%u+%u) @%s:%d"
+ "%s: mbuf 0x%llx proto %d IPv6 plen %d (%x) [swapped %d (%x)] doesn't match actual packet length; %u is used instead\n"
+ "%s: rejecting AF_LINK gateway on index %u with unusable link address (nlen %u, alen %u, sdl_len %u)\n"
+ "%s: route %s on %s%d link address does not fit (sdl_alen %u, error %d)\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/xnu/bsd/net/iptap.c"
+ "221111212122222211222221112"
+ "Attempt to call task_coalition_role_for_type with invalid coalition_type: %d\n @%s:%d"
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
+ "bklb-backlight-dc"
+ "bklb-backlight-frequency"
+ "com.apple.private.enable-coredump-on-panic-seed-privacy-approved"
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
+ "v28@?0^{vm_page=(?={vm_page_packed_queue_entry=II}^{vm_page}){vm_page_packed_queue_entry=II}{vm_page_packed_queue_entry=II}IIQ(?=SS){?=b4b2b1b1}{?=b1b1b1b1b1b1b1b1}{?=b2b1b1b1b1b1b1}{?=b1b1b1b1b1b1b1b1}{?=b4b4b4b1b1b1b1}[0C]QS(?=(vmp_lock={?=CC}S){vm_page_ecc=b1b7})(?=II)}8I16@?<v@?B>20"
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
