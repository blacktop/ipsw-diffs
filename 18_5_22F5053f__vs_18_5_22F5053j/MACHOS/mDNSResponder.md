## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2600.120.6.0.0
-  __TEXT.__text: 0xfe7c4
+2600.120.11.0.1
+  __TEXT.__text: 0xfe83c
   __TEXT.__auth_stubs: 0x2df0
   __TEXT.__objc_stubs: 0x1220
   __TEXT.__objc_methlist: 0x334
   __TEXT.__const: 0x1128
-  __TEXT.__cstring: 0x16fb0
+  __TEXT.__cstring: 0x16fb5
   __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__oslogstring: 0x1dbad
+  __TEXT.__oslogstring: 0x1dc06
   __TEXT.__objc_classname: 0x5f9
   __TEXT.__objc_methname: 0x106c
   __TEXT.__objc_methtype: 0x52d

   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x4250
-  __DATA.__bss: 0x16d78
+  __DATA.__bss: 0x16d80
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   Functions: 1739
-  Symbols:   4283
+  Symbols:   4284
   CStrings:  4459
 
Symbols:
+ init_log_utility_service.log_utility_listener
CStrings:
+ "SKIPPED unicast assist query - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P %d %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{mdns:rrtype}d qhash %x"
+ "mDNSResponder-2600.120.11.0.1"
+ "unicast assist qhash (%s) keeping presence - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P qhash %x"
+ "unicast assist qhash flushed (%s) - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P qhash %x"
+ "unicast assist qhash flushed (overflow) - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P qhash %x"
+ "unicast assist record %s %s%s - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P %2.2u %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{public}s qhash %x rectype 0x%X%s"
+ "unicast assist record flushed (0 qhashes) - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P %2.2u ifhash %x"
- "SKIPPED unicast assist query - %{sensitive, mask.hash, mdnsresponder:ip_addr}.20P %d %{sensitive, mask.hash, mdnsresponder:domain_name}.*P %{public}s qhash %x"
- "mDNSResponder-2600.120.6"
- "unicast assist qhash (%s) keeping presence - %{public, mdnsresponder:ip_addr}.20P qhash %x"
- "unicast assist qhash flushed (%s) - %{public, mdnsresponder:ip_addr}.20P qhash %x"
- "unicast assist qhash flushed (overflow) - %{public, mdnsresponder:ip_addr}.20P qhash %x"
- "unicast assist record %s %s%s - %{public, mdnsresponder:ip_addr}.20P %2.2u %{public, mdnsresponder:domain_name}.*P %{public}s qhash %x rectype 0x%X%s"
- "unicast assist record flushed (0 qhashes) - %{public, mdnsresponder:ip_addr}.20P %2.2u ifhash %x"

```
