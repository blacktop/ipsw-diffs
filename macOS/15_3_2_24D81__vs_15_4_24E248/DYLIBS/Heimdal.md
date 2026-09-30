## Heimdal

> `/System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal`

```diff

-693.60.3.0.0
-  __TEXT.__text: 0xbdcf4
+693.100.10.0.0
+  __TEXT.__text: 0xaca8c
   __TEXT.__auth_stubs: 0x19e0
-  __TEXT.__const: 0xe80
-  __TEXT.__cstring: 0xfbb6
+  __TEXT.__const: 0xe88
+  __TEXT.__cstring: 0xfbbd
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0xba8
+  __TEXT.__unwind_info: 0xb20
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x172
   __TEXT.__objc_stubs: 0x260

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: D7424264-0BE6-3FED-9C6F-427B03D1E905
-  Functions: 2776
-  Symbols:   4616
-  CStrings:  2470
+  UUID: B0E9B130-1585-3CDE-967D-C5CF49CE3921
+  Functions: 2755
+  Symbols:   4617
+  CStrings:  2472
 
Symbols:
+ _DNSServiceQueryRecordWithAttribute
+ _kDNSServiceAttrAllowFailover
- _DNSServiceQueryRecord
CStrings:
+ "%d %s%s%s"
+ "%lu"
+ "%s-%u.%s."
+ "%u"
+ "IPv4 prefix too large (%lu)"
+ "IPv6 prefix too large (%lu)"
+ "KDC sent %u patypes"
+ "KDC sent PA-DATA type: %u (%s)"
+ "derive_key() called with unknown keytype (%d)"
+ "dropping dup KDC host: %s:%d (proto %u)"
+ "fallback lookup %u for realm %s (service %s)"
+ "krb5_get_creds: %s: opt: %u"
+ "mcc_close_internal: %s, %u\n"
+ "salt type %u not supported"
+ "salttype %u not supported"
+ "unknown binding type (%u) in free_binding"
+ "unknown directory type: %u"
- "%s-%d.%s."
- "%u %s%s%s"
- "IPv4 prefix too large (%ld)"
- "IPv6 prefix too large (%ld)"
- "KDC sent %d patypes"
- "KDC sent PA-DATA type: %d (%s)"
- "derive_key() called with unknown keytype (%u)"
- "dropping dup KDC host: %s:%d (proto %d)"
- "fallback lookup %d for realm %s (service %s)"
- "krb5_get_creds: %s: opt: %d"
- "mcc_close_internal: %s, %d\n"
- "salt type %d not supported"
- "salttype %d not supported"
- "unknown binding type (%d) in free_binding"
- "unknown directory type: %d"

```
