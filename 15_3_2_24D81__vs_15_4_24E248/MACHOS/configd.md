## configd

> `/usr/libexec/configd`

```diff

-1351.80.2.0.0
-  __TEXT.__text: 0x68cc0
-  __TEXT.__auth_stubs: 0x2380
+1351.101.1.0.0
+  __TEXT.__text: 0x69fb0
+  __TEXT.__auth_stubs: 0x2390
   __TEXT.__objc_stubs: 0x1580
-  __TEXT.__objc_methlist: 0x904
+  __TEXT.__objc_methlist: 0xb4c
   __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x313e
-  __TEXT.__oslogstring: 0x546f
+  __TEXT.__cstring: 0x31d1
+  __TEXT.__oslogstring: 0x5633
   __TEXT.__objc_methname: 0x1bf7
   __TEXT.__objc_classname: 0x7c
   __TEXT.__objc_methtype: 0x660
-  __TEXT.__gcc_except_tab: 0x8c
-  __TEXT.__unwind_info: 0xa28
-  __DATA_CONST.__auth_got: 0x11d0
-  __DATA_CONST.__got: 0x700
-  __DATA_CONST.__auth_ptr: 0xe8
-  __DATA_CONST.__const: 0x1960
-  __DATA_CONST.__cfstring: 0x2a80
+  __TEXT.__gcc_except_tab: 0x94
+  __TEXT.__unwind_info: 0xa30
+  __DATA_CONST.__auth_got: 0x11d8
+  __DATA_CONST.__got: 0x6e8
+  __DATA_CONST.__auth_ptr: 0x100
+  __DATA_CONST.__const: 0x1998
+  __DATA_CONST.__cfstring: 0x2a60
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA.__objc_const: 0x1230
-  __DATA.__objc_selrefs: 0x718
+  __DATA.__objc_const: 0xde8
+  __DATA.__objc_selrefs: 0x7c0
   __DATA.__objc_ivar: 0xa0
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x160
+  __DATA.__data: 0x168
   __DATA.__common: 0x80
-  __DATA.__bss: 0x680
+  __DATA.__bss: 0x688
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08476525-154F-354B-ADA0-87CC9C5210A7
-  Functions: 934
-  Symbols:   803
-  CStrings:  2069
+  UUID: E0529544-7EEE-39C4-8E9C-21141BB72172
+  Functions: 963
+  Symbols:   804
+  CStrings:  2086
 
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
+ "CategoryManagerServer: server already started"
+ "NAT64PrefixRequestAddToWaiting"
+ "NAT64PrefixRequestCheckStart"
+ "NAT64PrefixRequestRemoveFromWaiting"
+ "monitor_dnsinfo_start"
+ "monitor_dnsinfo_start_block_invoke"
+ "monitor_dnsinfo_stop"
+ "nat64_get_dns_config"
+ "not "
- ".."
- "com.apple.SystemConfiguration.ApplicationFirewall"

```
