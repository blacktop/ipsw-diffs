## kernel.release.t6050

> `System/Library/Kernels/kernel.release.t6050`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__hib_const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__exclaves_bt`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__KLDDATA.__const`
- `__DATA.__data`
- `__BOOTDATA.__init`
- `__BOOTDATA.__init_entry_set`

```diff

-12377.161.15.700.19
+12377.161.15.701.19
   __TEXT.__const: 0x37d60
   __TEXT.__copyio_vectors: 0x340
-  __TEXT.__cstring: 0xae4c4
-  __TEXT.__os_log: 0x3e332
+  __TEXT.__cstring: 0xae5c3
+  __TEXT.__os_log: 0x3e511
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
-  __DATA_CONST.__sdt_cstring: 0x6e9e
-  __DATA_CONST.__sdt: 0xe610
+  __DATA_CONST.__sdt_cstring: 0x6ed2
+  __DATA_CONST.__sdt: 0xe628
   __DATA_CONST.__kalloc_type: 0x17900
-  __DATA_CONST.__const: 0x133b30
+  __DATA_CONST.__const: 0x133b38
   __DATA_CONST.__assert: 0xd20
   __DATA_CONST.__kalloc_var: 0x82f0
   __DATA_CONST.__exclaves_bt: 0x78

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x54000
   __TEXT_EXEC.__hib_text: 0x17c8
-  __TEXT_EXEC.__text: 0x9ac870
+  __TEXT_EXEC.__text: 0x9ad15c
   __TEXT_EXEC.__commpage_text: 0x334
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0xad68

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4fb78
-  __CTF.__ctf: 0xfbbf4
-  Functions: 23232
+  __CTF.__ctf: 0xfbf6e
+  Functions: 23231
   Symbols:   6896
-  CStrings:  26287
+  CStrings:  26306
 
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
