## netstat

> `/usr/sbin/netstat`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-755.0.0.0.0
-  __TEXT.__text: 0x1b210
+757.0.0.0.0
+  __TEXT.__text: 0x1b6b0
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__cstring: 0xf2c1
+  __TEXT.__cstring: 0xf8c1
   __TEXT.__const: 0x3d8
   __TEXT.__unwind_info: 0x268
   __DATA_CONST.__const: 0x14b8

   __DATA.__common: 0x6b0
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 124
-  Symbols:   269
-  CStrings:  2381
+  Functions: 125
+  Symbols:   272
+  CStrings:  2434
 
Symbols:
+ _print_ipsec_fastpath
+ ipsec_stats.pfastpath_in
+ ipsec_stats.pfastpath_out
CStrings:
+ "\t%llu %s packet%s bypassed policy lookup by offload\n"
+ "\t%llu outbound packet%s failed on IP output after encryption\n"
+ "\t%llu outbound packet%s held by IP output flow control\n"
+ "\t%llu outbound packet%s with SA not yet mature\n"
+ "DROP_REASON_IP6_EXTHDR_TOO_LONG"
+ "DROP_REASON_IP6_EXTHDR_TOO_SHORT"
+ "DROP_REASON_IP6_MCAST_NOT_TRANSMITTED"
+ "DROP_REASON_IP6_NA_EHSRC_MISMATCH"
+ "DROP_REASON_IP6_NS_DAD_IN_PROGRESS"
+ "DROP_REASON_IP6_RS_BAD_ND_OPT"
+ "DROP_REASON_IP6_RS_FROM_NON_NEIGHBOR"
+ "DROP_REASON_PF_BAD_OFFSET"
+ "DROP_REASON_PF_BAD_TIMESTAMP"
+ "DROP_REASON_PF_CONGESTION"
+ "DROP_REASON_PF_DUMMYNET"
+ "DROP_REASON_PF_INVALID_PORT"
+ "DROP_REASON_PF_IP_OPTION"
+ "DROP_REASON_PF_NORMALIZE"
+ "DROP_REASON_PF_PROTO_CKSUM"
+ "DROP_REASON_PF_ROUTE_LOOP"
+ "DROP_REASON_PF_ROUTE_OUTPUT"
+ "DROP_REASON_PF_SRC_LIMIT"
+ "DROP_REASON_PF_STATE_INSERT"
+ "DROP_REASON_PF_STATE_LIMIT"
+ "DROP_REASON_PF_STATE_MISMATCH"
+ "DROP_REASON_PF_SYNPROXY"
+ "IPv6 DAD NA L2 source mismatches target lladdr"
+ "IPv6 NS for a target with DAD in progress"
+ "IPv6 RS from non-neighbor"
+ "IPv6 RS with invalid ND opt"
+ "IPv6 multicast delivered locally, not transmitted"
+ "IPv6 non-contiguous header exceeds mbuf"
+ "IPv6 truncated header"
+ "PF IP option not allowed"
+ "PF SYN proxy"
+ "PF bad TCP timestamp"
+ "PF bad fragment"
+ "PF bad offset for pull header"
+ "PF congestion"
+ "PF dropped by normalizer"
+ "PF dummynet"
+ "PF invalid TCP/UDP port"
+ "PF invalid protocol checksum"
+ "PF route loop"
+ "PF route output error"
+ "PF source node/connection limit"
+ "PF state insertion failure"
+ "PF state limit"
+ "PF state mismatch"
+ "inbound"
+ "net.inet.ipsec.offload_fastpath_in"
+ "net.inet.ipsec.offload_fastpath_out"
+ "outbound"
```
