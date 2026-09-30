## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-889.0.0.0.0
-  __TEXT.__text: 0xb3178
-  __TEXT.__auth_stubs: 0x1890
-  __TEXT.__objc_stubs: 0xbf20
-  __TEXT.__objc_methlist: 0x4d0c
-  __TEXT.__const: 0x349
+896.0.0.0.1
+  __TEXT.__text: 0xb376c
+  __TEXT.__auth_stubs: 0x18c0
+  __TEXT.__objc_stubs: 0xbf40
+  __TEXT.__objc_methlist: 0x4d3c
+  __TEXT.__const: 0x361
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__gcc_except_tab: 0x3de8
-  __TEXT.__oslogstring: 0xf6ae
-  __TEXT.__cstring: 0xcb08
-  __TEXT.__objc_methname: 0xefce
-  __TEXT.__objc_classname: 0xc3c
+  __TEXT.__oslogstring: 0xf831
+  __TEXT.__cstring: 0xcb1a
+  __TEXT.__objc_methname: 0xf02e
+  __TEXT.__objc_classname: 0xc7b
   __TEXT.__objc_methtype: 0x27d9
-  __TEXT.__unwind_info: 0x1820
-  __DATA_CONST.__auth_got: 0xc58
-  __DATA_CONST.__got: 0x6b8
-  __DATA_CONST.__const: 0x1ed0
+  __TEXT.__unwind_info: 0x1830
+  __DATA_CONST.__auth_got: 0xc70
+  __DATA_CONST.__got: 0x6c8
+  __DATA_CONST.__const: 0x1f30
   __DATA_CONST.__cfstring: 0x7e40
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xab00
-  __DATA.__objc_selrefs: 0x3630
-  __DATA.__objc_ivar: 0x998
-  __DATA.__objc_data: 0x1b30
+  __DATA.__objc_const: 0xac60
+  __DATA.__objc_selrefs: 0x3638
+  __DATA.__objc_ivar: 0x9a0
+  __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0xb58
-  __DATA.__bss: 0x1c0
+  __DATA.__bss: 0x1f0
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1AA7D7E7-80F1-36F1-B878-F4DE6054D5AD
-  Functions: 2042
-  Symbols:   624
-  CStrings:  6856
+  UUID: 95FDE48F-B9FD-34FC-9900-C23072D7A500
+  Functions: 2048
+  Symbols:   627
+  CStrings:  6866
 
Symbols:
+ _nw_proxy_config_get_privacy_proxy_agent_type
+ _nw_proxy_config_get_system_privacy_proxy_agent_type
+ _nw_resolver_config_get_private_dns_agent_type
+ _nw_resolver_config_get_system_private_dns_agent_type
- _nw_proxy_config_get_agent_type
CStrings:
+ "%@ performing captive evaluation of Wi-Fi network [%{private}@]"
+ "-[NSPPrivacyProxyNetworkRegistration initWithAgentUUID:name:systemAgentType:agentDescription:delegate:]"
+ "Failed to save preference to disable on Wi-Fi network %{private}@: %@"
+ "IPv4/IPv6 changed for SSID [%{private}@]"
+ "NSPSystemPrivacyProxyConfigAgent"
+ "NSPSystemPrivacyProxyDNSAgent"
+ "PvD fetch for proxied content map to %@ received empty response"
+ "Received %u file handle activity callbacks without progress"
+ "Received %u file handle activity callbacks without progress in %u seconds, exiting"
+ "Received file handle activity callback"
+ "Saving preference to disable on Wi-Fi network: %{private}@"
+ "Scheduled block on internal queue, file handle activity acknowledged"
+ "Wi-Fi SSID changed to [%{private}@]"
+ "Wi-Fi network %{private}@ is active"
+ "Wi-Fi network %{private}@ is blocked"
+ "Wi-Fi network %{private}@ is disabled"
+ "_fileHandleActivityTime"
+ "_unacknowledgedFileHandleActivityCounter"
+ "quarantine"
+ "setFileHandleActivityCallback:"
- "%@ performing captive evaluation of Wi-Fi network [%@]"
- "-[NSPPrivacyProxyNetworkRegistration initWithAgentUUID:name:agentDescription:delegate:]"
- "DNSAgent"
- "Failed to save preference to disable on Wi-Fi network %@: %@"
- "IPv4/IPv6 changed for SSID [%@]"
- "Saving preference to disable on Wi-Fi network: %@"
- "Wi-Fi SSID changed to [%@]"
- "Wi-Fi network %@ is active"
- "Wi-Fi network %@ is blocked"
- "Wi-Fi network %@ is disabled"

```
