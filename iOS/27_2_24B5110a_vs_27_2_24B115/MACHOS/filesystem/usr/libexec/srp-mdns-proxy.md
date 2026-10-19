## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 3111.40.45.0.0
-  __TEXT.__text: 0x8b3dc
+  __TEXT.__text: 0x8b850
   __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x22c
   __TEXT.__const: 0x2e5
-  __TEXT.__cstring: 0x8f27
-  __TEXT.__oslogstring: 0x1423e
+  __TEXT.__cstring: 0x8fde
+  __TEXT.__oslogstring: 0x144a4
   __TEXT.__objc_methname: 0x506
   __TEXT.__objc_classname: 0x35
   __TEXT.__objc_methtype: 0x237
-  __TEXT.__unwind_info: 0x860
+  __TEXT.__unwind_info: 0x870
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x958
   __DATA_CONST.__cfstring: 0x140

   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 489
-  Symbols:   1184
-  CStrings:  2704
+  Functions: 493
+  Symbols:   1188
+  CStrings:  2711
 
Symbols:
+ _thread_netdata_decode_6lowpan_id_payload
+ _thread_netdata_decode_prefix_payload
+ _thread_netdata_decode_server_payload
+ _thread_netdata_decode_service_payload
CStrings:
+ "%{public}s: TLV length %zu exceeds the %d byte maximum"
+ "%{public}s: dns_concatenate_name_to_wire: called at %{public}s:%d with both prefix and labels_prefix non-NULL (labels_prefix = %p, prefix = %p, suffix = %p)"
+ "%{public}s: dns_concatenate_name_to_wire: called at %{public}s:%d with both suffix and labels_prefix including a terminal label (labels_prefix = %p, prefix = %p, suffix = %p)"
+ "%{public}s: dns_concatenate_name_to_wire: called at %{public}s:%d with no way to terminate the name (labels_prefix = %p, prefix = %p, suffix = %p)"
+ "%{public}s: service TLV value must be at least 6 bytes long (was %u bytes long)"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/mDNSResponderExtras/ServiceRegistration/wireutils.c"
+ "dns_concatenate_name_to_wire_"
```
