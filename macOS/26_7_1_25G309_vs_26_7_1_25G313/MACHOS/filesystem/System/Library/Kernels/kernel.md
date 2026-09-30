## kernel

> `System/Library/Kernels/kernel`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__got`
- `__KLDDATA.__init`
- `__KLDDATA.__init_entry_set`
- `__KLDDATA.__const`
- `__KLDDATA.__static_ifinit`
- `__LASTDATA_CONST.__mod_init_func`

```diff

-12377.161.15.700.19
-  __TEXT.__text: 0x8cf360
+12377.161.15.701.19
+  __TEXT.__text: 0x8d0250
   __TEXT.__const: 0x44db0
-  __TEXT.__os_log: 0x47d4b
-  __TEXT.__cstring: 0x9f07b
+  __TEXT.__os_log: 0x47f7b
+  __TEXT.__cstring: 0x9f17b
   __TEXT.__eh_frame: 0x118
   __DATA.__lock_grp: 0x15f10
   __DATA.__data: 0x83520
   __DATA.__percpu: 0x3de8
   __DATA.__common: 0x1bcda0
-  __DATA_CONST.__const: 0xa1098
+  __DATA_CONST.__const: 0xa10a8
   __DATA_CONST.__kalloc_type: 0x17140
   __DATA_CONST.__kalloc_var: 0x7c60
   __DATA_CONST.__assert: 0x974
   __DATA_CONST.__kern_brk_desc: 0x60
-  __DATA_CONST.__sdt_cstring: 0x6e50
-  __DATA_CONST.__sdt: 0xeb80
+  __DATA_CONST.__sdt_cstring: 0x6e84
+  __DATA_CONST.__sdt: 0xebc8
   __DATA_CONST.__mod_init_func: 0x2c8
   __DATA_CONST.__got: 0x58
   __KLDDATA.__init: 0x22ac0

   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
   __LINKINFO.__symbolsets: 0x4d6d4
-  __CTF.__ctf: 0xddaa5
-  Functions: 26465
+  __CTF.__ctf: 0xdde34
+  Functions: 26466
   Symbols:   23791
-  CStrings:  25549
+  CStrings:  25568
 
CStrings:
+ "%s: mbuf %p len (%d) < off+len (%u+%u) @%s:%d"
+ "%s: refusing cross-protocol ifa change on route with llinfo"
+ "22111220222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220222121222221111111222211122112222211221122222112211222221122112222211222211122211112111111"
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
- "221112202222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222221111111222211122112222211221122222112211222221122112222211222211122211112111111"
- "222121112211221122111022222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111112121111222221112221222222222222221122222112"
```
