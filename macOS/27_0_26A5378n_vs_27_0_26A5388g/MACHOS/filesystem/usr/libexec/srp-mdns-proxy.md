## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3089.0.0.0.1
-  __TEXT.__text: 0x8e3d4
+3109.0.0.0.0
+  __TEXT.__text: 0x8e550
   __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__const: 0x2e5
+  __TEXT.__const: 0x2f5
   __TEXT.__cstring: 0x9120
-  __TEXT.__oslogstring: 0x1407b
+  __TEXT.__oslogstring: 0x14128
   __TEXT.__unwind_info: 0x610
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x920

   - /usr/lib/libsqlite3.dylib
   Functions: 481
   Symbols:   1120
-  CStrings:  2602
+  CStrings:  2604
 
Functions:
~ _dso_state_create : 528 -> 548
~ _dns_proxy_input_for_server : 8396 -> 8716
~ _dp_query_send_dns_response : 9004 -> 9036
~ _srp_update_start : 8028 -> 8036
CStrings:
+ "%{public}s: [DSO%u] Fatal: sizeof (*dso)[%zu], outsize[%zu], namespace[%zu]"
+ "%{public}s: dso_message_received: fatal: %s sent %ld byte message, QR=0, xid=%02x%02x"
+ "%{public}s: dso_message_received: fatal: %s: too many additional TLVs: %ld %ld"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/adv-ctl-server.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/cti-services.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-client.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-hints.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-proxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/ioloop.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/macos-ioloop.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/netdata-tracker.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/node-type-tracker.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/omr-watcher.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/probe-srp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/service-publisher.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/service-tracker.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/srp-decompress.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/srp-mdns-proxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/srp-parse.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/state-machine.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/thread-device.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/thread-service.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/thread-tracker.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u9nXNt/Sources/mDNSResponderExtras/ServiceRegistration/tls-macos.c"
+ "01:36:22"
+ "Jul 10 2026"
- "%{public}s: Fatal: sizeof (*dso)[%zu], outsize[%zu], namespace[%zu]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/adv-ctl-server.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/cti-services.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-client.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-hints.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-proxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/ioloop.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/macos-ioloop.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/netdata-tracker.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/node-type-tracker.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/omr-watcher.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/probe-srp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/service-publisher.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/service-tracker.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/srp-decompress.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/srp-mdns-proxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/srp-parse.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/state-machine.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/thread-device.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/thread-service.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/thread-tracker.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/tls-macos.c"
- "13:43:10"
- "Jun 25 2026"
```
