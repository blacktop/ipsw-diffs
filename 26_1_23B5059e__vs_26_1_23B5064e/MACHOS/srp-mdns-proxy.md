## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2881.40.17.0.0
-  __TEXT.__text: 0x8305c
+2881.40.18.0.0
+  __TEXT.__text: 0x836bc
   __TEXT.__auth_stubs: 0x1340
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x21c
-  __TEXT.__const: 0x282
-  __TEXT.__cstring: 0x7665
-  __TEXT.__oslogstring: 0x11e6a
+  __TEXT.__const: 0x27a
+  __TEXT.__cstring: 0x77ab
+  __TEXT.__oslogstring: 0x11fd8
   __TEXT.__objc_classname: 0x38
   __TEXT.__objc_methname: 0x4e6
   __TEXT.__objc_methtype: 0x237
-  __TEXT.__unwind_info: 0x588
+  __TEXT.__unwind_info: 0x590
   __DATA_CONST.__auth_got: 0x9a8
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x10

   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x970
+  __DATA.__bss: 0x978
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33A8901E-EB62-3AC5-A67F-9145B518F087
-  Functions: 451
-  Symbols:   1133
-  CStrings:  2460
+  UUID: 63775A49-9AC7-3F70-8B0B-2F2AA7012248
+  Functions: 453
+  Symbols:   1135
+  CStrings:  2470
 
Symbols:
+ _DNSServiceRecordValidate
+ __block_descriptor_tmp.1413
+ __block_descriptor_tmp.165
+ __block_descriptor_tmp.17.1503
+ __block_descriptor_tmp.18.1597
+ __block_descriptor_tmp.243
+ __block_descriptor_tmp.2608
+ __block_descriptor_tmp.557
+ __block_descriptor_tmp.8.1460
+ __block_descriptor_tmp.81
+ __block_literal_global.1504
+ __block_literal_global.555
+ _srp_mdns_shared_record_remove_
+ _srp_mdns_stale_record_callback
- __block_descriptor_tmp.112
- __block_descriptor_tmp.1353
- __block_descriptor_tmp.17.1443
- __block_descriptor_tmp.18.1537
- __block_descriptor_tmp.190
- __block_descriptor_tmp.2546
- __block_descriptor_tmp.497
- __block_descriptor_tmp.76
- __block_descriptor_tmp.8.1400
- __block_literal_global.1444
- __block_literal_global.495
- _srp_mdns_shared_record_remove
CStrings:
+ "%{public}s: record %p (%p %p) validates after removal with error %d"
+ "%{public}s: record %p (%p %p) validates when shared_txn != server_state->shared_txn %p"
+ "%{public}s: removing %{public}s %{public}s %p %p"
+ "%{public}s: stale record callback %lf seconds later for sdref %p rref %p error %d (now %d) at %{public}s:%d"
+ "%{public}s: stale record callback for sdref %p rref %p with null context pointer, error %d."
+ "01:27:10"
+ "DNSServiceRecordValidate called with NULL DNSServiceRef"
+ "DNSServiceRecordValidate called with bad DNSServiceRef"
+ "Oct  6 2025"
+ "dnssd_clientstub DNSServiceRecordValidate called with invalid DNSRecordRef %p %08X %08X"
+ "dnssd_clientstub DNSServiceRecordValidate called with invalid DNSServiceRef %p %08X %08X"
+ "srp_mdns_shared_record_remove_"
+ "srp_mdns_stale_record_callback"
+ "valid"
- "%{public}s: removing %{public}s %p %p"
- "07:20:44"
- "Sep 26 2025"
- "srp_mdns_shared_record_remove"

```
