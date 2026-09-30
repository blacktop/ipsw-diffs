## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2600.120.12.0.0
-  __TEXT.__text: 0xfe83c
+2600.140.2.0.0
+  __TEXT.__text: 0xfe848
   __TEXT.__auth_stubs: 0x2df0
   __TEXT.__objc_stubs: 0x1220
   __TEXT.__objc_methlist: 0x334
   __TEXT.__const: 0x1128
-  __TEXT.__cstring: 0x16fb1
+  __TEXT.__cstring: 0x16fb0
   __TEXT.__gcc_except_tab: 0x154
   __TEXT.__oslogstring: 0x1dc06
   __TEXT.__objc_classname: 0x5f9

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 33FC5664-2544-3691-9155-C0C402D9E1CB
+  UUID: ABB96606-A7AF-372B-8FF8-249F29B1EA4E
   Functions: 1739
   Symbols:   4284
   CStrings:  4560
Functions:
~ ___mdns_dns_service_manager_register_doh_uri_block_invoke : 984 -> 996
CStrings:
+ "mDNSResponder-2600.140.2"
- "mDNSResponder-2600.120.12"

```
