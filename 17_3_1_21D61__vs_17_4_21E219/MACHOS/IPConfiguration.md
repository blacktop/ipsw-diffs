## IPConfiguration

> `/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration`

```diff

-455.60.2.0.0
-  __TEXT.__text: 0x59174
-  __TEXT.__auth_stubs: 0x1120
+455.100.4.0.0
+  __TEXT.__text: 0x5a110
+  __TEXT.__auth_stubs: 0x1130
   __TEXT.__objc_stubs: 0x640
   __TEXT.__objc_methlist: 0x6bc
   __TEXT.__const: 0x210
-  __TEXT.__oslogstring: 0x5dfb
-  __TEXT.__cstring: 0x3ad3
+  __TEXT.__oslogstring: 0x5de7
+  __TEXT.__cstring: 0x3b14
   __TEXT.__objc_methname: 0x15b5
   __TEXT.__objc_classname: 0x27
   __TEXT.__objc_methtype: 0x3ec
   __TEXT.__unwind_info: 0xb54
-  __DATA_CONST.__auth_got: 0x898
+  __DATA_CONST.__auth_got: 0x8a0
   __DATA_CONST.__got: 0x318
   __DATA_CONST.__auth_ptr: 0xe8
   __DATA_CONST.__const: 0x1b20

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x940
   __DATA.__objc_selrefs: 0x4e8
-  __DATA.__objc_classrefs: 0x28
-  __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x88
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x170

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9DC6E136-0782-3EAE-880D-76D55A509A1B
-  Functions: 1095
-  Symbols:   529
-  CStrings:  2177
+  UUID: 1902C659-CF3E-36A5-B35C-CDD203965113
+  Functions: 1097
+  Symbols:   528
+  CStrings:  2183
 
Symbols:
+ __SCNetworkInterfaceIsTetheredHotspot
+ ___assert_rtn
- _DHCPLeaseListRemoveAllButLastLease
- _ServiceUnpublishCLAT46
- __SCNetworkInterfaceIsTethered
CStrings:
+ "%s: IPv6OnlyPreferred is %spossible"
+ "%s: couldn't add client identifier, %s"
+ "%s: couldn't add dhcp message tag %d, %s"
+ "%s: couldn't add max message size, %s"
+ "%s: couldn't add parameter request list, %s"
+ "%s: discarding lease for %@, MAC mismatch"
+ "%s: malloc failed, %s (%d)"
+ "%s: using lease for %@"
+ "add_parameter_request_list"
+ "dhcp.c"
+ "make_dhcp_request"
+ "n_params > 0"
- "Removing lease #%d for IP address %d.%d.%d.%d"
- "make_dhcp_request: couldn't add client identifier, %s"
- "make_dhcp_request: couldn't add dhcp message tag %d, %s"
- "make_dhcp_request: couldn't add max message size, %s"
- "make_dhcp_request: couldn't add parameter request list, %s"
- "make_dhcp_request: malloc failed, %s (%d)"

```
