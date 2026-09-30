## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2063.80.10.0.0
-  __TEXT.__text: 0x96e7c
+2063.100.25.0.0
+  __TEXT.__text: 0x96b0c
   __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_stubs: 0x73c0
-  __TEXT.__objc_methlist: 0x28cc
-  __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x1c9c
-  __TEXT.__oslogstring: 0xbd2d
-  __TEXT.__objc_methname: 0x83f9
-  __TEXT.__cstring: 0x41ae
+  __TEXT.__objc_stubs: 0x7420
+  __TEXT.__objc_methlist: 0x320c
+  __TEXT.__const: 0x168
+  __TEXT.__gcc_except_tab: 0x1c98
+  __TEXT.__oslogstring: 0xbd24
+  __TEXT.__objc_methname: 0x8421
+  __TEXT.__cstring: 0x41c7
   __TEXT.__objc_classname: 0x909
   __TEXT.__objc_methtype: 0x1d49
-  __TEXT.__unwind_info: 0x1300
+  __TEXT.__unwind_info: 0x12b0
   __DATA_CONST.__auth_got: 0xd80
-  __DATA_CONST.__got: 0x6b8
-  __DATA_CONST.__const: 0x1a10
+  __DATA_CONST.__got: 0x6c0
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x1a40
   __DATA_CONST.__cfstring: 0x2240
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x100

   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7858
-  __DATA.__objc_selrefs: 0x1e48
+  __DATA.__objc_const: 0x67b0
+  __DATA.__objc_selrefs: 0x2098
   __DATA.__objc_ivar: 0x644
   __DATA.__objc_data: 0x1310
   __DATA.__data: 0xc18

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1566
+  Functions: 1550
   Symbols:   639
-  CStrings:  3468
+  CStrings:  3472
 
CStrings:
+ "%@: Registered fallback relay network agent %{public}@"
+ "%@: Registration failed for fallback relay network agent %{public}@"
+ "%@: Update failed for fallback relay network agent %{public}@"
+ "%@: Updated fallback relay network agent %{public}@"
+ "-[NESMPolicySession setPoliciesForRelayWithAgentUUID:dnsAgentUUID:matchDomains:excludedDomains:matchFQDNs:excludedFQDNs:perApp:captiveNetworkPluginBundleIDs:]_block_invoke"
+ "Excluding FQDNs from relay: %@"
+ "excludedFQDNs"
+ "matchFQDNs"
+ "setExactMatch:"
- "%@: Registered fallback relay network agent %{public,uuid_t}.16P"
- "%@: Registration failed for fallback relay network agent %{public,uuid_t}.16P"
- "%@: Update failed for fallback relay network agent %{public,uuid_t}.16P"
- "%@: Updated fallback relay network agent %{public,uuid_t}.16P"
- "-[NESMPolicySession setPoliciesForRelayWithAgentUUID:dnsAgentUUID:matchDomains:excludedDomains:perApp:captiveNetworkPluginBundleIDs:]_block_invoke"

```
