## Heimdal

> `/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal`

```diff

-693.60.3.0.0
-  __TEXT.__text: 0x62ca8
+693.100.10.0.0
+  __TEXT.__text: 0x6247c
   __TEXT.__auth_stubs: 0x1970
-  __TEXT.__const: 0x1080
+  __TEXT.__const: 0x1068
   __TEXT.__cstring: 0xf26f
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x1638
+  __TEXT.__unwind_info: 0x1600
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x172
   __TEXT.__objc_stubs: 0x260

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
   __AUTH_CONST.__auth_got: 0xcc8
-  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0x1e70
   __AUTH_CONST.__cfstring: 0xc20
   __DATA.__data: 0x2c50

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 2454
-  Symbols:   1784
+  Functions: 2506
+  Symbols:   1785
   CStrings:  2263
 
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
- ".."
- "ASL"
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
