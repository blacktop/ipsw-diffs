## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2200.62.1.0.0
-  __TEXT.__text: 0x60784
-  __TEXT.__auth_stubs: 0xf30
+2200.80.16.0.0
+  __TEXT.__text: 0x60afc
+  __TEXT.__auth_stubs: 0xf40
   __TEXT.__objc_stubs: 0x100
   __TEXT.__const: 0xb4
-  __TEXT.__cstring: 0x5b2b
-  __TEXT.__oslogstring: 0xbf1f
+  __TEXT.__cstring: 0x5bae
+  __TEXT.__oslogstring: 0xc013
   __TEXT.__objc_methname: 0x7d
   __TEXT.__unwind_info: 0x494
-  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__auth_got: 0x7a8
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x750

   - /usr/lib/libipconfig.dylib
   - /usr/lib/libmdns.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EAB06C23-60FB-3773-872F-32FB1515B7B3
-  Functions: 349
-  Symbols:   861
-  CStrings:  1763
+  UUID: A693B924-9786-39D6-A10E-DC36E45DDD19
+  Functions: 350
+  Symbols:   863
+  CStrings:  1770
 
Symbols:
+ __block_descriptor_tmp.17.1072
+ __block_descriptor_tmp.46
+ __block_descriptor_tmp.49
+ __block_descriptor_tmp.51
+ __block_descriptor_tmp.58
+ __block_descriptor_tmp.60
+ __block_descriptor_tmp.65
+ __block_descriptor_tmp.8.1019
+ _dispatch_set_finalizer_f
+ _ioloop_read_source_finalize
- __block_descriptor_tmp.17.1071
- __block_descriptor_tmp.45
- __block_descriptor_tmp.48
- __block_descriptor_tmp.50
- __block_descriptor_tmp.57
- __block_descriptor_tmp.59
- __block_descriptor_tmp.62
- __block_descriptor_tmp.8.1017
CStrings:
+ " (already canceled)"
+ "%{public}s: %p: %{public}s %{public}s:%d"
+ "%{public}s: %{private, mask.hash}s (%p %p) state is %d; error = %{public}s"
+ "%{public}s: %{private, mask.hash}s (%p %p) state is %{public}s; error = %{public}s"
+ "%{public}s: %{private, mask.hash}s (%p %p) state is canceled; error = %{public}s"
+ "%{public}s: %{private, mask.hash}s (%p %p) state is ready; error = %{public}s"
+ "%{public}s: after update, %d hosts, %d instances, %d a records, %d aaaa records"
+ "%{public}s: cancel on canceled connection %{private, mask.hash}s"
+ "%{public}s: ready but canceled"
+ "%{public}s: updated TXT record for %{private, mask.hash}s . %{private, mask.hash}s."
+ "20:02:37"
+ "Dec 20 2023"
+ "ioloop_read_source_finalize"
+ "local address type doesn't match query type"
+ "local host IPv4 address"
+ "local host IPv6 address"
+ "local host v4-mapped address"
- "%{public}s: %p: %{public}s:%d"
- "%{public}s: %{private, mask.hash}s state is %d; error = %{public}s"
- "%{public}s: %{private, mask.hash}s state is %{public}s; error = %{public}s"
- "%{public}s: %{private, mask.hash}s state is canceled; error = %{public}s"
- "%{public}s: %{private, mask.hash}s state is ready; error = %{public}s"
- "%{public}s: updated TXT record for %{private, mask.hash}s."
- "08:22:40"
- "Nov 12 2023"
- "ioloop_read_cancel"
- "local host address"

```
