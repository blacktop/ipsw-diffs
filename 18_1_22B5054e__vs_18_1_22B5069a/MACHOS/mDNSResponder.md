## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2559.40.31.0.0
-  __TEXT.__text: 0x100948
+2559.40.32.0.0
+  __TEXT.__text: 0x101258
   __TEXT.__auth_stubs: 0x2df0
   __TEXT.__objc_stubs: 0x15a0
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x1128
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__cstring: 0x16e5b
-  __TEXT.__oslogstring: 0x1da2d
+  __TEXT.__cstring: 0x16e2b
+  __TEXT.__oslogstring: 0x1dc56
   __TEXT.__objc_classname: 0x63a
   __TEXT.__objc_methname: 0x13ed
   __TEXT.__objc_methtype: 0x5da

   - /usr/lib/libxml2.2.dylib
   Functions: 1803
   Symbols:   4329
-  CStrings:  4493
+  CStrings:  4495
 
Symbols:
+ __block_descriptor_tmp.246.2968
+ __block_descriptor_tmp.389
+ __block_literal_global.2972
+ __block_literal_global.391
- __block_descriptor_tmp.246.2969
- __block_descriptor_tmp.390
- __block_literal_global.2973
- __block_literal_global.392
CStrings:
+ "[R%!u(MISSING)->Rec%!u(MISSING)] DNSServiceRemoveRecord -- ifindex: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), duration: %!{(MISSING)mdns:time_duration}u, name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: %!{(MISSING)sensitive, mask.hash, mdns:rdata}.*P"
+ "[R%!u(MISSING)->Rec%!u(MISSING)] DNSServiceRemoveRecord -- ifindex: %!d(MISSING), client pid: %!d(MISSING) (%!{(MISSING)public}s), duration: %!{(MISSING)mdns:time_duration}u, name: %!{(MISSING)sensitive, mask.hash, mdnsresponder:domain_name}.*P(%!x(MISSING)), type: %!{(MISSING)mdns:rrtype}d, rdata: <none>"
+ "[R%!u(MISSING)->Rec%!u(MISSING)] DNSServiceRemoveRecord -- name hash: %!x(MISSING), duration: %!{(MISSING)mdns:time_duration}u"
+ "mDNSResponder-2559.40.32"
- "%!d(MISSING): DNSServiceRemoveRecord(%!u(MISSING) %!s(MISSING))  PID[%!d(MISSING)](%!s(MISSING))"
- "mDNSResponder-2559.40.31"

```
