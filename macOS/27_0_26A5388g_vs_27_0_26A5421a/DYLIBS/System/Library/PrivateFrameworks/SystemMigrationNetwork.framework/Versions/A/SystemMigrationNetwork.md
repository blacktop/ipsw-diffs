## SystemMigrationNetwork

> `/System/Library/PrivateFrameworks/SystemMigrationNetwork.framework/Versions/A/SystemMigrationNetwork`

```diff

-1426.0.0.0.0
-  __TEXT.__text: 0x3d1e4
-  __TEXT.__objc_methlist: 0x4578
+1428.0.3.0.0
+  __TEXT.__text: 0x3dab8
+  __TEXT.__objc_methlist: 0x4598
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x956f
-  __TEXT.__gcc_except_tab: 0xe84
-  __TEXT.__ustring: 0x2c4c
+  __TEXT.__cstring: 0x9863
+  __TEXT.__gcc_except_tab: 0xea4
+  __TEXT.__ustring: 0x2cf8
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xdd0
+  __TEXT.__unwind_info: 0xde0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x308
+  __DATA_CONST.__const: 0x328
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29b8
+  __DATA_CONST.__objc_selrefs: 0x29d0
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xf0
   __DATA_CONST.__got: 0x5b8
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x96a0
+  __AUTH_CONST.__cfstring: 0x9880
   __AUTH_CONST.__objc_const: 0x6878
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libParallelCompression.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1533
-  Symbols:   4057
-  CStrings:  1264
+  Functions: 1538
+  Symbols:   4066
+  CStrings:  1283
 
Symbols:
+ -[SMNWirelessController softAPInterfaceName]
+ -[SMNWirelessController startIPv6LinkLocalOnSoftAP]
+ -[SMNWirelessController waitForSoftAPIPv6LinkLocalReadyWithTimeout:]
+ _objc_msgSend$softAPInterfaceName
+ _objc_msgSend$startIPv6LinkLocalOnSoftAP
+ _objc_msgSend$waitForSoftAPIPv6LinkLocalReadyWithTimeout:
+ _smn_softap_ipv6_linklocal_state
+ _smn_start_ipv6_linklocal
+ _strcmp
CStrings:
+ "[IPv6LL] %@ link-local NOT ready after %.1fs: state=%s addr=%s — falling back to IPv4"
+ "[IPv6LL] %@ link-local is duplicated after %.2fs; using IPv4"
+ "[IPv6LL] %@ link-local ready: %s (after %.2fs)"
+ "[IPv6LL] %@ post-SIOCLL_START: state=%s addr=%s"
+ "[IPv6LL] Bonjour delivered %@ address for %@: %@"
+ "[IPv6LL] Forcing IPv6 link-local on SoftAP %@"
+ "[IPv6LL] No SoftAP interface for IPv6 link-local"
+ "[IPv6LL] SIOCGIFAFLAG_IN6 read failed on %s (errno=%d %s)"
+ "[IPv6LL] SIOCLL_START on %s failed (errno=%d %s)"
+ "[IPv6LL] SIOCPROTOATTACH_IN6 on %s failed (errno=%d %s)"
+ "[IPv6LL] SoftAP has no usable link-local; skipping %@ (using IPv4)"
+ "[IPv6LL] getifaddrs failed on %s (errno=%d %s)"
+ "[IPv6LL] socket(AF_INET6) failed on %s (errno=%d %s)"
+ "[IPv6LL] socket(AF_INET6) failed reading link-local state on %s (errno=%d %s)"
+ "duplicated"
+ "link-local IPv6"
+ "none"
+ "ready"
+ "tentative"
```
