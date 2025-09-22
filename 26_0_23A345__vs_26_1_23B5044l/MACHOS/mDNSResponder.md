## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2881.0.25.0.0
-  __TEXT.__text: 0x10631c
+2881.40.10.0.0
+  __TEXT.__text: 0x1066a4
   __TEXT.__auth_stubs: 0x2f00
   __TEXT.__objc_stubs: 0x1d00
   __TEXT.__objc_methlist: 0x664
-  __TEXT.__const: 0x1168
-  __TEXT.__cstring: 0x175c7
+  __TEXT.__const: 0x1180
+  __TEXT.__cstring: 0x175c8
   __TEXT.__gcc_except_tab: 0x334
-  __TEXT.__oslogstring: 0x1ecde
+  __TEXT.__oslogstring: 0x1edcc
   __TEXT.__objc_classname: 0x649
   __TEXT.__objc_methname: 0x1b39
   __TEXT.__objc_methtype: 0x62a

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: E8A66541-98B4-3F99-890E-751C10EABC8A
+  UUID: 852C127D-4E01-3373-A8FF-9E402C999A2F
   Functions: 1836
   Symbols:   4575
   CStrings:  4852
Functions:
~ _request_callback : 43816 -> 43820
~ _mDNSCoreReceiveResponse : 42844 -> 42936
~ _resolve_result_callback : 14076 -> 14884
CStrings:
+ "[R%u->(Q%u, Q%u)] DNSServiceResolve NoSuchRecord -- instance: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%{sensitive}x)"
+ "[R%u->(Q%u, Q%u)] DNSServiceResolve RESULT -- instance: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%{sensitive}x), ifindex: %u, target host: %{sensitive, mask.hash, mdnsresponder:domain_name}.*P(%{sensitive}x), port: %u, negative txt: %{mdns:yesno}d, txt rdlength: %u"
+ "mDNSResponder-2881.40.10"
- "[R%u->Q%d] DNSServiceResolve(%{sensitive, mask.hash}s(%x)) NoSuchRecord"
- "[R%u->Q%d] DNSServiceResolve(%{sensitive, mask.hash}s(%x)) RESULT   %{sensitive, mask.hash}s(%x):%d"
- "mDNSResponder-2881.0.25"

```
