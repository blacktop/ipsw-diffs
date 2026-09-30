## misd

> `/usr/libexec/misd`

```diff

-360.0.0.0.0
-  __TEXT.__text: 0x201b4
-  __TEXT.__auth_stubs: 0x11e0
+366.0.0.0.0
+  __TEXT.__text: 0x208ac
+  __TEXT.__auth_stubs: 0x11f0
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0xaf17
+  __TEXT.__cstring: 0xb0a8
   __TEXT.__oslogstring: 0x1e
   __TEXT.__objc_methname: 0x8f6
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methtype: 0x69e
-  __TEXT.__unwind_info: 0x4c8
-  __DATA_CONST.__auth_got: 0x8f8
+  __TEXT.__unwind_info: 0x4d0
+  __DATA_CONST.__auth_got: 0x900
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__const: 0x9d8
   __DATA_CONST.__cfstring: 0xb40

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC5A431E-79EF-3B6C-84A2-9F7FDD34307A
-  Functions: 429
-  Symbols:   380
-  CStrings:  1790
+  UUID: 68336DAC-8F74-3F93-81DD-E0357553980E
+  Functions: 441
+  Symbols:   381
+  CStrings:  1801
 
Symbols:
+ _inet_addr
+ _sscanf
- _ether_aton
CStrings:
+ "%hhx:%hhx:%hhx:%hhx:%hhx:%hhx"
+ "%s: stopping network %s"
+ "%s: validateSubnetParameters failed"
+ "destroyed service request %s"
+ "end address %s is beyond the allowed range of network mask"
+ "ip address string is NULL"
+ "mask %s is not valid"
+ "mis_network_cleanup_bridge"
+ "mis_set_reclaim_mac_io_ethernet"
+ "missing dhcp parameters: start address %s, end address %s or mask %s"
+ "netrbServiceRequestRemove"
+ "network != NULL"
+ "network->mn_refcnt >= 2"
+ "start address %s and end address %s must beprivate addresses"
+ "start address %s is not in the subnet"
+ "start address %s, end address %s or mask %s is invalid"
- "%s: host addr is not subnet + 1"
- "%s: inet_pton, invalid netrbXPCNetworkMask"
- "%s: inet_pton, invalid netrbXPCStartAddress"
- "%s: missing either start address or mask"
- "bcast_range"

```
