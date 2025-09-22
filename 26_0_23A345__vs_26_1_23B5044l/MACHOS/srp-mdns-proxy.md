## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2881.0.25.0.0
-  __TEXT.__text: 0x842d4
-  __TEXT.__auth_stubs: 0x1360
+2881.40.10.0.0
+  __TEXT.__text: 0x83154
+  __TEXT.__auth_stubs: 0x1340
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x282
-  __TEXT.__cstring: 0x7685
-  __TEXT.__oslogstring: 0x11f81
+  __TEXT.__cstring: 0x7665
+  __TEXT.__oslogstring: 0x11ef0
   __TEXT.__objc_classname: 0x38
   __TEXT.__objc_methname: 0x4e6
   __TEXT.__objc_methtype: 0x237
   __TEXT.__unwind_info: 0x588
-  __DATA_CONST.__auth_got: 0x9b8
+  __DATA_CONST.__auth_got: 0x9a8
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x8f0

   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A01527A6-774A-35CC-BB2D-A533C104074A
-  Functions: 453
-  Symbols:   1137
-  CStrings:  2466
+  UUID: 336971F4-8AE3-3179-A259-4FD0E3AD8310
+  Functions: 451
+  Symbols:   1133
+  CStrings:  2462
 
Symbols:
+ _srp_mdns_record_disconnect
- _launch_activate_socket
- _nw_listener_create_with_launchd_key
- _retry_callback
- _start_host_update
- _wait_retry
CStrings:
+ "%{public}s: %p  IN    A %{private, mask.hash, network:in_addr}.4P%{private, mask.hash}s"
+ "%{public}s: %p  IN AAAA %{public}s%{private, mask.hash, network:in6_addr}.16P%{private, mask.hash}s"
+ "%{public}s: %p  IN KEY %xu %{public}s"
+ "%{public}s: called with nonexistent host %p."
+ "%{public}s: forgetting record %p rref %p on %{public}s %p %{private, mask.hash}s"
+ "%{public}s: host %p %{private, mask.hash}s key_id %xu stable %llx lease %d key_lease %d expiry %d%{public}s%{public}s"
+ "%{public}s: instance defunct: sdref %p flags %x error %d context %p freed %{public}s."
+ "%{public}s: mismatch between rrtypes mapped and rrtypes thought to be mappable for rrtype %{public}s"
+ "%{public}s: record %p was not seen"
+ "%{public}s: service defunct: sdref %p rref %p flags %x error %d context %p freed %{public}s."
+ "%{public}s: successfully disconnected services: %p"
+ "23:52:25"
+ "Sep 16 2025"
+ "adv_instance"
+ "indeterminate"
+ "srp_mdns_record_disconnect"
- "%{public}s:   IN    A %{private, mask.hash, network:in_addr}.4P%{private, mask.hash}s"
- "%{public}s:   IN AAAA %{public}s%{private, mask.hash, network:in6_addr}.16P%{private, mask.hash}s"
- "%{public}s: [Q%d][QU%d] record type %{public}s not translated"
- "%{public}s: called with nonexistent host."
- "%{public}s: forgetting rref %p on %{public}s %p %{private, mask.hash}s"
- "%{public}s: host %{private, mask.hash}s key_id %xu stable %llx lease %d key_lease %d expiry %d%{public}s%{public}s"
- "%{public}s: host lease has expired, not retrying: lease_expiry = %lld now = %lld difference = %lld"
- "%{public}s: launchd listener create failed, trying to create it without relying on launchd."
- "%{public}s: launchd port mismatch: %u %u"
- "%{public}s: launchd_activate_socket failed for %{public}s: %{public}s"
- "%{public}s: too few sockets returned from launchd_active_socket for %{public}s : %zd"
- "%{public}s: too many sockets returned from launchd_active_socket for %{public}s : %zd"
- "%{public}s: waiting %d seconds..."
- "00:05:06"
- "Aug  3 2025"
- "adv_instance_vec_copy"
- "adv_record_vec_copy"
- "new_vec->vec[i]"
- "update_from_host"
- "wait_retry"

```
