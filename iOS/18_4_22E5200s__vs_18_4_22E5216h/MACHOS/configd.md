## configd

> `/usr/libexec/configd`

```diff

-1351.100.11.0.1
-  __TEXT.__text: 0x64888
-  __TEXT.__auth_stubs: 0x23f0
+1351.100.16.0.1
+  __TEXT.__text: 0x65640
+  __TEXT.__auth_stubs: 0x2400
   __TEXT.__objc_stubs: 0x1460
   __TEXT.__objc_methlist: 0xa4c
   __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x2e74
-  __TEXT.__oslogstring: 0x5175
+  __TEXT.__cstring: 0x2f37
+  __TEXT.__oslogstring: 0x530b
   __TEXT.__objc_methname: 0x19d5
   __TEXT.__objc_classname: 0x5d
   __TEXT.__objc_methtype: 0x4ef
   __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__unwind_info: 0x9c0
-  __DATA_CONST.__auth_got: 0x1208
+  __TEXT.__unwind_info: 0x9d8
+  __DATA_CONST.__auth_got: 0x1210
   __DATA_CONST.__got: 0x6a0
   __DATA_CONST.__auth_ptr: 0x108
-  __DATA_CONST.__const: 0x1968
+  __DATA_CONST.__const: 0x19a8
   __DATA_CONST.__cfstring: 0x2580
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8

   __DATA.__objc_selrefs: 0x718
   __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x100
+  __DATA.__data: 0x104
   __DATA.__common: 0x80
   __DATA.__bss: 0x630
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 917
-  Symbols:   801
-  CStrings:  1621
+  Functions: 924
+  Symbols:   802
+  CStrings:  1639
 
Symbols:
+ _notify_cancel
CStrings:
+ "%s %s: no longer waiting for DNS"
+ "%s %s: waiting for DNS"
+ "%s notify_cancel(token %d) failed %d"
+ "%s notify_cancel(token %d) success"
+ "%s notify_register_dispatch failed %d"
+ "%s notify_register_dispatch success (token %d)"
+ "%s token %d != expected token %d, ignoring"
+ "%s: %s: DNS is %savailable (gen %llu)"
+ "%s: %s: waiting for DNS before starting resolver"
+ "%s: dns_configuration_copy() returned NULL"
+ "%s: generation %llu"
+ "NAT64PrefixRequestAddToWaiting"
+ "NAT64PrefixRequestCheckStart"
+ "NAT64PrefixRequestRemoveFromWaiting"
+ "monitor_dnsinfo_start"
+ "monitor_dnsinfo_start_block_invoke"
+ "monitor_dnsinfo_stop"
+ "nat64_get_dns_config"

```
