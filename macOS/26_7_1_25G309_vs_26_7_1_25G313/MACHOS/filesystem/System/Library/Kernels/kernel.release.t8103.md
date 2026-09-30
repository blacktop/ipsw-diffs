## kernel.release.t8103

> `System/Library/Kernels/kernel.release.t8103`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__hib_const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__KLDDATA.__const`
- `__DATA.__data`
- `__BOOTDATA.__init`
- `__BOOTDATA.__init_entry_set`
- `__BOOTDATA.__static_ifinit`

```diff

-12377.161.15.700.19
+12377.161.15.701.19
   __TEXT.__const: 0x37110
   __TEXT.__copyio_vectors: 0x150
-  __TEXT.__cstring: 0xa64f1
-  __TEXT.__os_log: 0x3e118
+  __TEXT.__cstring: 0xa65f0
+  __TEXT.__os_log: 0x3e2f7
   __TEXT.__thread_starts: 0x0
   __TEXT.__eh_frame: 0x6b0
   __DATA_CONST.__hib_const: 0x6f0
-  __DATA_CONST.__const: 0x180960
-  __DATA_CONST.__sdt_cstring: 0x6e72
-  __DATA_CONST.__sdt: 0xe4d8
+  __DATA_CONST.__const: 0x180968
+  __DATA_CONST.__sdt_cstring: 0x6ea6
+  __DATA_CONST.__sdt: 0xe4f0
   __DATA_CONST.__kalloc_type: 0x17240
   __DATA_CONST.__assert: 0x960
   __DATA_CONST.__kalloc_var: 0x7d00

   __DATA_CONST.__mod_init_func: 0x2d8
   __DATA_CONST.__auth_ptr: 0x10
   __TEXT_EXEC.__hib_text: 0x3fb0
-  __TEXT_EXEC.__text: 0x96c758
+  __TEXT_EXEC.__text: 0x96d0f8
   __TEXT_EXEC.__commpage_text: 0x334
   __KLD.__text: 0xb020
   __PPLTEXT.__text: 0x2d1e8

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0xe7820
-  Functions: 22682
+  __CTF.__ctf: 0xe7980
+  Functions: 22681
   Symbols:   6896
-  CStrings:  25793
+  CStrings:  25812
 
CStrings:
+ "%s: mbuf %p len (%d) < off+len (%u+%u) @%s:%d"
+ "%s: refusing cross-protocol ifa change on route with llinfo"
+ "22111220222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220222121222221111111222211111112222211111122222111111222221111112222211222211122211112111111"
+ "22212111221122112211102222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220222221111112121111222221112221222222222222221122222112"
+ "FilterDropBadDirection"
+ "SK[%u]: %-30s %s(%d): %d: skip cls_len < l3hlen + l4hlen\n"
+ "SK[%u]: %-30s Tx flow port %d != channel port %d, %s\n"
+ "SK[%u]: %-30s dropped packet injected on ring %u whose wrap flag does not match the ring direction: pkt_pflags 0x%llx\n"
+ "SK[%u]: %-30s filter packet is not mbuf-wrapped: pkt_pflags 0x%llx\n"
+ "SK[%u]: %-30s filter packet is not packet-wrapped: pkt_pflags 0x%llx\n"
+ "_dtlecnt != 0"
+ "_in6m->in6m_in_dtle == true"
+ "_inm->inm_in_dtle == true"
+ "bad__direction"
+ "inm->in6m_dtlecnt != 0"
+ "inm->inm_dtlecnt != 0"
+ "necp_set_socket_resolver_signature_from_parameters"
+ "not__mbuf__wrapped"
+ "not__pkt__wrapped"
+ "nx_netif_filter_pkt_to_mbuf"
+ "nx_netif_filter_pkt_to_pkt"
+ "rt_setif"
- "%s: mbuf %p len (%d) < off+len (%d+%d) @%s:%d"
- "221112202222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222221111111222211111112222211111122222111111222221111112222211222211122211112111111"
- "222121112211221122111022222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111112121111222221112221222222222222221122222112"
```
