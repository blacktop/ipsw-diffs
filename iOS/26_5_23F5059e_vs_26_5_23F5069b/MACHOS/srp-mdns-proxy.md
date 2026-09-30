## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2881.120.8.0.1
-  __TEXT.__text: 0x83830
+2881.120.11.0.0
+  __TEXT.__text: 0x83880
   __TEXT.__auth_stubs: 0x1350
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x22c
   __TEXT.__const: 0x27a
-  __TEXT.__cstring: 0x7c80
-  __TEXT.__oslogstring: 0x11f5c
+  __TEXT.__cstring: 0x7ccd
+  __TEXT.__oslogstring: 0x11f3f
   __TEXT.__objc_classname: 0x38
   __TEXT.__objc_methname: 0x506
   __TEXT.__objc_methtype: 0x237

   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 407613F7-D945-3D07-8E50-6822031ECBA7
+  UUID: 9523BFE7-2F67-38A0-8E83-5907D3E437F5
   Functions: 454
   Symbols:   1135
-  CStrings:  2473
+  CStrings:  2476
 
Functions:
~ _srp_dns_evaluate : 20016 -> 20096
CStrings:
+ " has no SRV record"
+ " has no TXT record"
+ " is not referenced by a service update"
+ "%{public}s: service instance update for %{private, mask.hash}s%{public}s"
+ "06:54:10"
+ "Apr 18 2026"
- "%{public}s: service instance update for %{private, mask.hash}s is not referenced by a service update."
- "16:20:27"
- "Apr 11 2026"

```
