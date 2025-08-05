## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2191.0.0.0.0
-  __TEXT.__text: 0xaf608
-  __TEXT.__auth_stubs: 0x1ce0
+2204.0.0.0.1
+  __TEXT.__text: 0xb2584
+  __TEXT.__auth_stubs: 0x1d20
   __TEXT.__objc_stubs: 0x7fe0
-  __TEXT.__objc_methlist: 0x3d34
+  __TEXT.__objc_methlist: 0x3d94
   __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x22b0
-  __TEXT.__objc_methname: 0x90fd
-  __TEXT.__oslogstring: 0xee4b
-  __TEXT.__cstring: 0x5161
+  __TEXT.__gcc_except_tab: 0x2368
+  __TEXT.__objc_methname: 0x9168
+  __TEXT.__oslogstring: 0xf38a
+  __TEXT.__cstring: 0x535e
   __TEXT.__objc_classname: 0xbac
-  __TEXT.__objc_methtype: 0x20b5
-  __TEXT.__unwind_info: 0x1610
-  __DATA_CONST.__auth_got: 0xe80
-  __DATA_CONST.__got: 0x778
+  __TEXT.__objc_methtype: 0x210d
+  __TEXT.__unwind_info: 0x1660
+  __DATA_CONST.__auth_got: 0xea0
+  __DATA_CONST.__got: 0x770
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1d08
-  __DATA_CONST.__cfstring: 0x26e0
+  __DATA_CONST.__const: 0x1d80
+  __DATA_CONST.__cfstring: 0x2660
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7ff0
-  __DATA.__objc_selrefs: 0x2398
-  __DATA.__objc_ivar: 0x77c
+  __DATA.__objc_const: 0x8060
+  __DATA.__objc_selrefs: 0x23a0
+  __DATA.__objc_ivar: 0x788
   __DATA.__objc_data: 0x1860
   __DATA.__data: 0xf80
   __DATA.__bss: 0x130

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 091B9A14-CC64-30BF-A4E4-111FBEEA8D33
-  Functions: 1862
-  Symbols:   686
-  CStrings:  4292
+  UUID: 29916AD4-3984-3701-A028-750B5CA4C28C
+  Functions: 1883
+  Symbols:   689
+  CStrings:  4320
 
Symbols:
+ _NECopySigningIdentifierForPIDwithAuditToken
+ ___kCFBooleanFalse
+ _ne_session_applications_have_local_network_entitlements
+ _separateDomainsFromFQDNs
+ _xpc_connection_get_audit_token
- _OBJC_CLASS_$_NEPvDConfiguration
- _OBJC_CLASS_$_NERelayConfiguration
CStrings:
+ "%@ No match rules found in PvD configuration"
+ "%@: %s - Connection time out scheduled <interval %d secs> for %@"
+ "%@: %s - Connection timed out <interval %d secs> for %@"
+ "%@: %s - Connection timeout canceled for %@"
+ "%@: %s - Failed to bringup filter before timeout of %d seconds"
+ "%@: %s - Failed to set <shouldFailClosed=%llu> for the %s notification (status %d)"
+ "%@: %s - Failed to start connection timer"
+ "%@: %s - Failed to startFilter <%@>"
+ "%@: %s - Filter bringup timed out <interval %d secs>"
+ "%@: %s - Filter bringup timeout scheduled <interval %d secs>"
+ "%@: %s - Updating config %@"
+ "%@: %s - enter - err %@"
+ "%@: %s - update configuration %@"
+ "%@: handleNewRequest - Allow ciphermld requests"
+ "%@: handleNewRequest - FINAL RESULT <failClosed> - filter is not up yet"
+ "%@: handleNewRequest - FINAL RESULT <failClosed> - no prefilter setup yet"
+ "%@: handleNewRequest - FINAL RESULT <failClosed> - request timed out"
+ "%@: handleNewRequest - FINAL RESULT <failOpened> - filter is not up yet"
+ "%@: handleNewRequest - FINAL RESULT <failOpened> - no prefilter setup yet"
+ "%@: handleNewRequest - FINAL RESULT <failOpened> - request timed out"
+ "-[NEAgentURLFilterExtension setFilterBringupTimeout]"
+ "-[NEAgentURLFilterExtension setFilterBringupTimeout]_block_invoke"
+ "-[NEAgentURLFilterExtension updateConfiguration:]_block_invoke"
+ "-[NEPIRChecker start:responseQueue:completionHandler:]"
+ "-[NEPIRChecker start:responseQueue:completionHandler:]_block_invoke"
+ "-[NESMPolicySession addRelayPolicySkipRules:masterSession:extraExceptionDomains:captiveNetworkPluginBundleIDs:]"
+ "-[NESMURLFilterSession postFilterFailClosedChange:]"
+ "-[NEURLFilterEngine cancelConnectionTimer:]"
+ "-[NEURLFilterEngine handleNewRequest:connection:filloutReply:completionHandler:]"
+ "-[NEURLFilterEngine handleNewRequest:connection:filloutReply:completionHandler:]_block_invoke"
+ "-[NEURLFilterEngine setConfiguration:completionHandler:]_block_invoke"
+ "-[NEURLFilterEngine setupConnectionTimer:timeoutHandler:]"
+ "-[NEURLFilterEngine setupConnectionTimer:timeoutHandler:]_block_invoke"
+ "-[NEURLFilterEngine startFilterWithCompletionHandler:]_block_invoke"
+ "Added trie %ld for policy exclude rules (offset = %d, fqdn = %d)"
+ "Ignoring PvD configuration, FQDN %@ was not already configured"
+ "Ignoring PvD configuration, domain %@ was not already configured"
+ "Ignoring PvD configuration, prefix %@ was not already configured"
+ "Ignoring PvD update due to empty contents"
+ "Ignoring PvD update due to empty match rules"
+ "Posted to <shouldFailClosed=%llu> to %s"
+ "Unbalanced ordered relay rules: %lu / %lu / %lu"
+ "_filterBringupTimer"
+ "_pendingConnectionTimers"
+ "com.apple.ciphermld"
+ "com.apple.private.restrict-post.nesessionmanager.url-filter-fail-closed"
+ "com.apple.private.restrict-post.nesessionmanager.url-prefilter-ready"
+ "domains"
+ "numberWithUnsignedLong:"
+ "proxy-match"
+ "setConfiguration:completionHandler:"
+ "start:responseQueue:completionHandler:"
+ "startFilterWithCompletionHandler:"
+ "stringByAppendingString:"
+ "subnets"
+ "v40@0:8@\"NEURLFilterConfiguration\"16@\"NSObject<OS_dispatch_queue>\"24@?<v@?@\"NSError\">32"
- "%@: handleNewRequest - no prefilter / filter setup yet"
- "-"
- "-[NEPIRChecker start:responseQueue:]"
- "-[NEPIRChecker start:responseQueue:]_block_invoke"
- "-[NESMPolicySession setPoliciesForRelayWithAgentUUID:dnsAgentUUID:matchDomains:excludedDomains:matchFQDNs:excludedFQDNs:perApp:captiveNetworkPluginBundleIDs:]_block_invoke"
- "-[NEURLFilterEngine handleNewRequest:filloutReply:completionHandler:]"
- "-[NEURLFilterEngine handleNewRequest:filloutReply:completionHandler:]_block_invoke"
- "-[NEURLFilterEngine startFilter]_block_invoke"
- "Added trie %ld for policy exclude rules (labelOffset = %d, fqdn = %d)"
- "Generated relay config from PvD: %@"
- "PvD match domains or ALPNs do not match"
- "alpn"
- "com.apple.nehelper.tracker-info-ready"
- "com.apple.nesessionmanager.prefilter-ready"
- "connect-udp"
- "excludeDomains"
- "excludeSubnets"
- "https-connect"
- "matchSubnets"
- "refreshConfigForced:"
- "separateDomainsFromFQDNs:domains:fqdns:"
- "setExcludedDomains:"
- "setMatchFQDNs:"

```
