## terminusd

> `/usr/libexec/terminusd`

```diff

-670.0.0.0.0
-  __TEXT.__text: 0x1808d8
-  __TEXT.__auth_stubs: 0x2b90
+673.0.0.0.0
+  __TEXT.__text: 0x180aec
+  __TEXT.__auth_stubs: 0x2bd0
   __TEXT.__objc_stubs: 0x8720
   __TEXT.__objc_methlist: 0x53a8
   __TEXT.__const: 0x24c
   __TEXT.__gcc_except_tab: 0x420c
-  __TEXT.__objc_methname: 0x119fe
-  __TEXT.__cstring: 0x40fd3
+  __TEXT.__objc_methname: 0x119f9
+  __TEXT.__cstring: 0x410b1
   __TEXT.__oslogstring: 0x247e
   __TEXT.__objc_classname: 0xe91
   __TEXT.__objc_methtype: 0x382c
-  __TEXT.__unwind_info: 0x2428
-  __DATA_CONST.__auth_got: 0x15d8
+  __TEXT.__unwind_info: 0x2450
+  __DATA_CONST.__auth_got: 0x15f8
   __DATA_CONST.__got: 0xa00
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x33d8
+  __DATA_CONST.__const: 0x3418
   __DATA_CONST.__cfstring: 0xbea0
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x108

   __DATA.__objc_ivar: 0x1a80
   __DATA.__objc_data: 0x29e0
   __DATA.__data: 0xce8
-  __DATA.__bss: 0x6b0
+  __DATA.__bss: 0x6b8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libdns_services.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 595500C6-80A0-3BC2-9205-3A2DEEA0CB74
-  Functions: 3099
-  Symbols:   1032
-  CStrings:  11584
+  UUID: 142EC419-BC9B-36F0-B53C-2AE568BDA64D
+  Functions: 3101
+  Symbols:   1036
+  CStrings:  11589
 
Symbols:
+ _nw_proxy_hop_disable_keepalives
+ _nw_proxy_hop_set_idle_timeout
+ _nw_proxy_hop_set_ignore_path_errors
+ _nw_quic_set_idle_timeout
CStrings:
+ "%s%.30s:%-4d Successfully released power assertion with id: %u"
+ "%s%.30s:%-4d Successfully took power assertion for %@ (id: %u)"
+ "%s%.30s:%-4d not starting link due to pending companion APL toggle"
+ "-[NRDTestServer setupTestServer]_block_invoke_3"
+ "-[NRLink setLinkMTU]"
+ "01:24:59"
+ "673"
+ "CompanionAPLToggle"
+ "Failed to release power assertion with id %u %d"
+ "Failed to remove power assertion"
+ "Failed to take power assertion for %@ (%d)"
+ "Jun 25 2025"
+ "NRPowerAssertionCreate"
+ "NRPowerAssertionDestroy"
+ "_hasPendingCompanionAPLToggle"
+ "setLinkMTU"
- "%@: Failed to release power assertion: %d"
- "%@: Failed to take power assertion: %d"
- "%s%.30s:%-4d not starting link due to pending companion APL enablement"
- "-[NRDTestServer setupTestServer]_block_invoke"
- "-[NRLink setLinkMTU:]"
- "00:38:43"
- "670"
- "Error: %d"
- "Jun 14 2025"
- "_hasPendingCompanionAPLEnablement"
- "setLinkMTU:"

```
