## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3089.0.0.0.1
-  __TEXT.__text: 0x8b3bc
+3109.0.0.0.0
+  __TEXT.__text: 0x8b4f4
   __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x22c
-  __TEXT.__const: 0x2d5
+  __TEXT.__const: 0x2e5
   __TEXT.__cstring: 0x8e75
-  __TEXT.__oslogstring: 0x1411d
+  __TEXT.__oslogstring: 0x141ca
   __TEXT.__objc_methname: 0x506
   __TEXT.__objc_classname: 0x35
   __TEXT.__objc_methtype: 0x237

   - /usr/lib/libsqlite3.dylib
   Functions: 489
   Symbols:   1184
-  CStrings:  2698
+  CStrings:  2700
 
Functions:
~ _dso_state_create : 536 -> 556
~ _dns_proxy_input_for_server : 9384 -> 9620
~ _dp_query_send_dns_response : 9004 -> 9036
~ _srp_update_start : 7956 -> 7980
CStrings:
+ "%{public}s: [DSO%u] Fatal: sizeof (*dso)[%zu], outsize[%zu], namespace[%zu]"
+ "%{public}s: dso_message_received: fatal: %s sent %ld byte message, QR=0, xid=%02x%02x"
+ "%{public}s: dso_message_received: fatal: %s: too many additional TLVs: %ld %ld"
+ "02:42:50"
+ "Jul 10 2026"
- "%{public}s: Fatal: sizeof (*dso)[%zu], outsize[%zu], namespace[%zu]"
- "00:32:02"
- "Jun 25 2026"
```
