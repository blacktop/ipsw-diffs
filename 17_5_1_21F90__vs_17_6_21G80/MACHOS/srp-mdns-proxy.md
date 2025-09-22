## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2200.120.24.0.0
-  __TEXT.__text: 0x64a38
-  __TEXT.__auth_stubs: 0x1010
+2200.140.11.0.0
+  __TEXT.__text: 0x65494
+  __TEXT.__auth_stubs: 0x1020
   __TEXT.__const: 0xc4
-  __TEXT.__oslogstring: 0xcb0e
-  __TEXT.__cstring: 0x5e34
+  __TEXT.__oslogstring: 0xcd17
+  __TEXT.__cstring: 0x5ed7
   __TEXT.__objc_classname: 0x1
   __TEXT.__unwind_info: 0x498
-  __DATA_CONST.__auth_got: 0x808
+  __DATA_CONST.__auth_got: 0x810
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x780

   - /usr/lib/libipconfig.dylib
   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
-  UUID: 7D1346ED-EAE8-3064-AEBD-256B9C243B9A
-  Functions: 359
-  Symbols:   876
-  CStrings:  1839
+  UUID: 8BD2C2BA-4222-3EDD-9DE2-EB3C8F32E6DD
+  Functions: 361
+  Symbols:   879
+  CStrings:  1855
 
Symbols:
+ _arc4random
+ _srp_host_record_retry_callback
+ _srp_instance_retry_callback
CStrings:
+ " completed with conflict."
+ " with a conflict"
+ "%{public}s: already scheduled attempt to reregister record %p"
+ "%{public}s: no longer updating host %p because host is no longer valid."
+ "%{public}s: no longer updating instance %p because host is no longer valid."
+ "%{public}s: re-registering host record %p."
+ "%{public}s: re-registering updating instance %p."
+ "%{public}s: re-update succeeded for instance %{private, mask.hash}s (%{private, mask.hash}s %{private, mask.hash}s %{private, mask.hash}s)"
+ "%{public}s: registration for service %{private, mask.hash}s.%{private, mask.hash}s.%{private, mask.hash}s -> %{private, mask.hash}s has completed%{public}s."
+ "%{public}s: unable to make wakeup &host->re_register_wakeup"
+ "%{public}s: unable to make wakeup &instance->retry_wakeup"
+ "%{public}s: will attempt to reregister instance %p in %.3lf seconds"
+ "%{public}s: will attempt to reregister record %p in %.3lf seconds"
+ "%{public}s: will not attempt to reregister record %p"
+ "11:57:38"
+ ":"
+ "Jun 30 2024"
+ "srp_host_record_retry_callback"
+ "srp_instance_retry_callback"
+ "srp_schedule_host_record_retry"
+ "srp_schedule_instance_retry"
- "%{public}s: no error, but update is NULL for instance %{private, mask.hash}s (%{private, mask.hash}s %{private, mask.hash}s %{private, mask.hash}s)"
- "%{public}s: registration for service %{private, mask.hash}s.%{private, mask.hash}s.%{private, mask.hash}s -> %{private, mask.hash}s has completed."
- "%{public}s: update is NULL, registration for host record completed with invalid state."
- "22:56:37"
- "Apr 16 2024"

```
