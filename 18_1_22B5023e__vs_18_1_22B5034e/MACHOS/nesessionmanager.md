## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2050.0.0.0.0
-  __TEXT.__text: 0x948b4
+2060.0.0.0.0
+  __TEXT.__text: 0x9457c
   __TEXT.__auth_stubs: 0x1a40
   __TEXT.__objc_stubs: 0x7200
   __TEXT.__objc_methlist: 0x282c
   __TEXT.__const: 0x130
   __TEXT.__gcc_except_tab: 0x1bf4
   __TEXT.__objc_classname: 0x8e8
-  __TEXT.__objc_methname: 0x817c
+  __TEXT.__objc_methname: 0x8168
   __TEXT.__objc_methtype: 0x1b8d
-  __TEXT.__oslogstring: 0xb79b
-  __TEXT.__cstring: 0x4048
+  __TEXT.__oslogstring: 0xb74f
+  __TEXT.__cstring: 0x404d
   __TEXT.__unwind_info: 0x12c8
   __DATA_CONST.__auth_got: 0xd30
   __DATA_CONST.__got: 0x690

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7610
+  __DATA.__objc_const: 0x75f0
   __DATA.__objc_selrefs: 0x1dc8
-  __DATA.__objc_ivar: 0x624
+  __DATA.__objc_ivar: 0x620
   __DATA.__objc_data: 0x1270
   __DATA.__data: 0xc18
   __DATA.__bss: 0xf0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1549
+  Functions: 1550
   Symbols:   624
-  CStrings:  3396
+  CStrings:  3392
 
CStrings:
+ "\x11?\a"
+ "Route Enforcement Policy IDs to be removed %!@(MISSING): %!@(MISSING)"
+ "-[NESMVPNSession applyTunnelRouteEnforcementPolicies]"
+ "Route Enforcement Policy IDs added %!@(MISSING): %!@(MISSING)"
+ "-[NESMPolicySession setTunnelRouteEnforecementPoliciesForInterfaceName:outgoingInterfaceName:agentPIDs:includeIPv4Routes:includeIPv6Routes:excludeIPv4Routes:excludeIPv6Routes:hasExcludeLocalNetworks:]_block_invoke"
+ "%!@(MISSING): Ignoring enforceRoutes because includeAllNetworks is set"
+ "%!@(MISSING): Re-setting route enforcement policies due to interface change event for tunnel \"%!@(MISSING)\" primary \"%!@(MISSING)\""
- "_lowTunnelPolicyIDs"
- "Low tunnel data Policy IDs to be removed %!@(MISSING): %!@(MISSING)"
- "route Policy IDs added %!@(MISSING): %!@(MISSING)"
- "-[NESMPolicySession setTunnelRoutePoliciesForInterfaceName:outgoingInterfaceName:agentPIDs:includeIPv4Routes:includeIPv6Routes:excludeIPv4Routes:excludeIPv6Routes:hasExcludeLocalNetworks:hasEnforcedRoutes:]_block_invoke"
- "-[NESMVPNSession applyTunnelRoutePolicies]"
- "Route Policy IDs to be removed %!@(MISSING): %!@(MISSING)"
- "\x11?\b"
- "%!@(MISSING): Re-setting route policies due to interface change event for tunnel \"%!@(MISSING)\" primary \"%!@(MISSING)\""
- "Low tunnel Policy IDs to be removed: %!@(MISSING)"
- "Low route Policy IDs to be removed %!@(MISSING): %!@(MISSING)"
- "Low tunnel Policy IDs to be removed %!@(MISSING): %!@(MISSING)"

```
