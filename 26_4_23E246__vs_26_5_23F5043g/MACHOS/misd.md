## misd

> `/usr/libexec/misd`

```diff

-381.100.4.0.0
-  __TEXT.__text: 0x20c68
-  __TEXT.__auth_stubs: 0x11f0
+381.120.3.0.0
+  __TEXT.__text: 0x214e8
+  __TEXT.__auth_stubs: 0x1230
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x38c
-  __TEXT.__const: 0x158
-  __TEXT.__cstring: 0xb286
+  __TEXT.__const: 0x168
+  __TEXT.__cstring: 0xb3d4
   __TEXT.__oslogstring: 0x1e
   __TEXT.__objc_methname: 0x8f6
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methtype: 0x69e
-  __TEXT.__unwind_info: 0x4f8
-  __DATA_CONST.__auth_got: 0x900
-  __DATA_CONST.__got: 0x2b0
+  __TEXT.__unwind_info: 0x508
+  __DATA_CONST.__auth_got: 0x920
+  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x9e8
   __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x10

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 82B76A20-44FC-33F2-BFC5-BAB1D32AFD30
-  Functions: 448
-  Symbols:   381
-  CStrings:  1813
+  UUID: 384E0DF1-D1C8-34F4-888C-0C27705CE422
+  Functions: 451
+  Symbols:   388
+  CStrings:  1826
 
Symbols:
+ _DHCPSDHCPLeaseListCreate
+ _PFUserDeleteStates
+ ___chkstk_darwin
+ _kDHCPSPropDHCPHWAddress
+ _kDHCPSPropDHCPIPAddress
+ _malloc_type_calloc
+ _strcasecmp
CStrings:
+ "%s: MAC %s -> IP %s"
+ "%s: PFUserCreate failed"
+ "%s: SIOCGDRVSPEC(BRDGRTS): %s"
+ "%s: bridge name too long"
+ "%s: calloc() failed"
+ "%s: deleting states for %s"
+ "%s: no DHCP leases"
+ "%s: no bridge RT entry for %s on %s: %s"
+ "%s: socket: %s"
+ "dhcp_lease_get_ipv4_for_mac"
+ "mis_bridge_get_member_mac_addresses"
+ "mis_pf_delete_states_v4"
+ "mis_vmnet_flush_pf_states"

```
