## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2167.0.0.0.2
-  __TEXT.__text: 0xaf0bc
-  __TEXT.__auth_stubs: 0x1c90
+2185.0.0.0.0
+  __TEXT.__text: 0xaf5cc
+  __TEXT.__auth_stubs: 0x1cd0
   __TEXT.__objc_stubs: 0x7fa0
   __TEXT.__objc_methlist: 0x3cfc
-  __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x2238
-  __TEXT.__objc_methname: 0x90ec
-  __TEXT.__oslogstring: 0xeb71
-  __TEXT.__cstring: 0x5121
-  __TEXT.__objc_classname: 0xba9
-  __TEXT.__objc_methtype: 0x207b
-  __TEXT.__unwind_info: 0x1618
-  __DATA_CONST.__auth_got: 0xe58
-  __DATA_CONST.__got: 0x788
+  __TEXT.__const: 0x178
+  __TEXT.__gcc_except_tab: 0x21a4
+  __TEXT.__objc_methname: 0x9119
+  __TEXT.__oslogstring: 0xee0e
+  __TEXT.__cstring: 0x5150
+  __TEXT.__objc_classname: 0xbac
+  __TEXT.__objc_methtype: 0x20b5
+  __TEXT.__unwind_info: 0x1608
+  __DATA_CONST.__auth_got: 0xe78
+  __DATA_CONST.__got: 0x778
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1d58
-  __DATA_CONST.__cfstring: 0x2700
+  __DATA_CONST.__cfstring: 0x26e0
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7fe8
+  __DATA.__objc_const: 0x8008
   __DATA.__objc_selrefs: 0x2388
-  __DATA.__objc_ivar: 0x77c
+  __DATA.__objc_ivar: 0x780
   __DATA.__objc_data: 0x1860
   __DATA.__data: 0xf80
   __DATA.__bss: 0x130

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 67B2CBA3-C776-3FED-A2A2-F7BA422B3EBD
-  Functions: 1863
-  Symbols:   683
-  CStrings:  4274
+  UUID: D97FC6FE-3E00-3ACC-BFF8-1D917829F683
+  Functions: 1861
+  Symbols:   685
+  CStrings:  4290
 
Symbols:
+ _nw_proxy_config_get_agent_domain
+ _nw_proxy_config_get_system_privacy_proxy_agent_type
+ _nw_resolver_config_get_system_private_dns_agent_type
+ _objc_autorelease
- _ne_privacy_dns_netagent_id
- _ne_privacy_proxy_netagent_id
CStrings:
+ "%@ configuration is enabled"
+ "%@ current Wi-Fi network [%@]"
+ "%@ currentMCCs don't match with newMCCs"
+ "%@ currentMNCs don't match with newMNCs"
+ "%@ currentTACs don't match with newTACs"
+ "%@ private LTE network configuration changed"
+ "%@ private LTE networks are no longer configured, stopping the monitor"
+ "-[NESMPolicySession getDomainTrie:exactMatch:matchSigningIdentifier:appRules:masterSession:]"
+ "@\"NEPrivateLTENetwork\""
+ "Added trie %ld for policy exclude rules (labelOffset = %d, fqdn = %d)"
+ "Added trie %ld for policy match rules (labelOffset = %d, fqdn = %d)"
+ "PvD contents: %@"
+ "PvD match domains or ALPNs do not match"
+ "Relay %@ last recorded error changing from %d to %d"
+ "Relay session ignoring unmapped error %d"
+ "Removing all trie entries for session %@"
+ "_currentMatchedPrivateLTENetwork"
+ "_trieEntries"
+ "didReceiveStatusChangeWithInterface:matchedPrivateLTENetwork:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "extension started successfully with %lu number of process identities"
+ "failed to start the extension"
+ "initWithLong:"
+ "networkName"
+ "removeNetworkAgentDomain:agentType:"
+ "v32@0:8q16@\"NEPrivateLTENetwork\"24"
+ "v32@?0@\"NSNumber\"8@\"NSMutableArray\"16^B24"
- "%@ Wi-Fi SSID match status changed from '%@' to '%@'"
- "-[NESMPolicySession getDomainTrie:matchSigningIdentifier:appRules:masterSession:]"
- "_currentSSIDMatchStaus"
- "_ssidMatchMonitor"
- "didReceiveStatusChangeWithInterface:"
- "initWithString:"
- "proxy"
- "registerServiceUUID:"
- "removeObjectsInArray:"
- "unregisterServiceUUID:"

```
