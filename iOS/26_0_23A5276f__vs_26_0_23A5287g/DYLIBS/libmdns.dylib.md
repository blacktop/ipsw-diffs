## libmdns.dylib

> `/usr/lib/libmdns.dylib`

```diff

-2874.0.0.0.1
-  __TEXT.__text: 0x32044
-  __TEXT.__auth_stubs: 0x1d00
+2881.0.7.0.0
+  __TEXT.__text: 0x32084
+  __TEXT.__auth_stubs: 0x1d20
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__cstring: 0x21a3
   __TEXT.__const: 0x1ad

   __TEXT.__unwind_info: 0x990
   __TEXT.__eh_frame: 0x74
   __TEXT.__objc_classname: 0x57f
-  __TEXT.__objc_methname: 0xd27
+  __TEXT.__objc_methname: 0xd33
   __TEXT.__objc_methtype: 0x52d
   __TEXT.__objc_stubs: 0xce0
-  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__const: 0x2b20
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x468
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xe90
+  __AUTH_CONST.__auth_got: 0xea0
   __AUTH_CONST.__const: 0x14c0
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_const: 0x3580

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0F8A0C1-E010-351E-BBDB-339D6884F044
+  UUID: EB05C070-77FE-3514-92C6-DDA6479FC0D3
   Functions: 815
-  Symbols:   3031
+  Symbols:   3032
   CStrings:  1178
 
Symbols:
+ _nw_proxy_config_get_agent_domain
+ _nw_proxy_config_get_system_privacy_proxy_agent_type
+ _objc_msgSend$removeNetworkAgentDomain:agentType:
- _ne_privacy_proxy_netagent_id
- _objc_msgSend$removeNetworkAgentUUID:
Functions:
~ ___mdns_dns_service_manager_apply_pending_updates_block_invoke : 1316 -> 1380
CStrings:
+ "removeNetworkAgentDomain:agentType:"
- "removeNetworkAgentUUID:"

```
