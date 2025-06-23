## terminusd

> `/usr/libexec/terminusd`

```diff

-658.0.0.0.2
-  __TEXT.__text: 0x17e728
-  __TEXT.__auth_stubs: 0x2b60
-  __TEXT.__objc_stubs: 0x8680
-  __TEXT.__objc_methlist: 0x5388
+670.0.0.0.0
+  __TEXT.__text: 0x1808d8
+  __TEXT.__auth_stubs: 0x2b90
+  __TEXT.__objc_stubs: 0x8720
+  __TEXT.__objc_methlist: 0x53a8
   __TEXT.__const: 0x24c
-  __TEXT.__gcc_except_tab: 0x4244
-  __TEXT.__objc_methname: 0x118f0
-  __TEXT.__cstring: 0x40af5
+  __TEXT.__gcc_except_tab: 0x420c
+  __TEXT.__objc_methname: 0x119fe
+  __TEXT.__cstring: 0x40fd3
   __TEXT.__oslogstring: 0x247e
-  __TEXT.__objc_classname: 0xe87
+  __TEXT.__objc_classname: 0xe91
   __TEXT.__objc_methtype: 0x382c
-  __TEXT.__unwind_info: 0x23e0
-  __DATA_CONST.__auth_got: 0x15c0
-  __DATA_CONST.__got: 0xa08
+  __TEXT.__unwind_info: 0x2428
+  __DATA_CONST.__auth_got: 0x15d8
+  __DATA_CONST.__got: 0xa00
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3330
-  __DATA_CONST.__cfstring: 0xbd80
-  __DATA_CONST.__objc_classlist: 0x428
+  __DATA_CONST.__const: 0x33d8
+  __DATA_CONST.__cfstring: 0xbea0
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e8

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x15068
-  __DATA.__objc_selrefs: 0x2d30
-  __DATA.__objc_ivar: 0x1a44
-  __DATA.__objc_data: 0x2990
+  __DATA.__objc_const: 0x152e8
+  __DATA.__objc_selrefs: 0x2d50
+  __DATA.__objc_ivar: 0x1a80
+  __DATA.__objc_data: 0x29e0
   __DATA.__data: 0xce8
   __DATA.__bss: 0x6b0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libdns_services.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2DEC5460-2A4A-39EB-878D-1C17CF2455EE
-  Functions: 3079
-  Symbols:   1030
-  CStrings:  11526
+  UUID: 595500C6-80A0-3BC2-9205-3A2DEEA0CB74
+  Functions: 3099
+  Symbols:   1032
+  CStrings:  11584
 
Symbols:
+ _nw_endpoint_get_port
+ _nw_proxy_config_get_agent_domain
+ _nw_proxy_config_get_system_privacy_proxy_agent_type
- _ne_privacy_proxy_netagent_id
CStrings:
+ "\nflows: %@"
+ "%s called with null client"
+ "%s called with null deviceID"
+ "%s%.30s:%-4d Defuncting flows for device %@"
+ "%s%.30s:%-4d Failed to copy endpoint for agent client %@"
+ "%s%.30s:%-4d Ignoring enabled device check since director has pending companion APL update"
+ "%s%.30s:%-4d Ignoring stop BT advertisement request, already restarting"
+ "%s%.30s:%-4d Restarting BT advertisements, due to new advertise request(s)"
+ "%s%.30s:%-4d added policy (%@) for identifier %@ : %@"
+ "%s%.30s:%-4d applied policies"
+ "%s%.30s:%-4d ignoring policy apply due to no changes"
+ "%s%.30s:%-4d removed policy (%@) for identifier %@"
+ "%s%.30s:%-4d switching companion APL %u -> %u"
+ "%s%.30s:%-4d unexpected flow by %@ - local: %@ remote: %@, path: %@"
+ "-[NRApplicationServiceManager cancelAllFlowsForDeviceID:]"
+ "-[NRDPolicySessionManager addPolicyForIdentifier:policy:]"
+ "-[NRDPolicySessionManager applyPolicies]"
+ "-[NRDPolicySessionManager removeAllPoliciesForIdentifier:]"
+ "-[NRLinkDirector startFlowMonitor]_block_invoke"
+ "-[NRLinkDirector updateDropPoliciesIfNeeded:]"
+ "-[NRLinkManagerBluetooth stopBTAdvertisementWithRestart:]"
+ "00:38:43"
+ "670"
+ "ASFlow"
+ "CompanionFlowMonitor"
+ "CompanionFlowMonitorAgent"
+ "Jun 14 2025"
+ "NRASMFlow"
+ "NRLinkDirector-Drop-ASQUIC"
+ "NetworkRelay appsvc flow"
+ "_changed"
+ "_companionLinkFlowAgent"
+ "_companionLinkFlowAgentQueue"
+ "_flows"
+ "_incoming"
+ "_incomingFlowAgent"
+ "_incomingFlowAgentUUID"
+ "_pendingTeardown"
+ "_teardownPolicyID"
+ "_trafficDropPolicyIdentifier"
+ "companion flow monitor agent"
+ "copyDeviceIdentifierForAgentClient"
+ "dropWithFlags:"
+ "flow-monitor-agent"
+ "incoming"
+ "iperf3"
+ "isInbound"
+ "isSystemProxyConnection"
+ "network_test"
+ "removeNetworkAgentDomain:agentType:"
+ "teardown"
+ "terminus_test"
+ "trafficDrop"
+ "unexpected flow received"
- "-[NRASMResolveRequest deviceIdentifier]"
- "-[NRLinkManagerBluetooth stopBTAdvertisementForRateChange:]"
- "04:25:30"
- "658.0.0.0.2"
- "May 23 2025"

```
