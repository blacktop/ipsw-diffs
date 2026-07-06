## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-  __TEXT.__text: 0x8b4f4
-  __TEXT.__auth_stubs: 0x1450
+  __TEXT.__text: 0x8e3d4
+  __TEXT.__auth_stubs: 0x14f0
   __TEXT.__const: 0x2e5
-  __TEXT.__cstring: 0x8b69
-  __TEXT.__oslogstring: 0x132af
-  __TEXT.__unwind_info: 0x608
+  __TEXT.__cstring: 0x9120
+  __TEXT.__oslogstring: 0x1407b
+  __TEXT.__unwind_info: 0x610
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x920
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xa28
-  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__auth_got: 0xa78
+  __DATA_CONST.__got: 0x208
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__data: 0x1e0
   __DATA.__bss: 0xa70

   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 478
-  Symbols:   1141
-  CStrings:  2541
+  Functions: 481
+  Symbols:   1156
+  CStrings:  2612
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__data : content changed
Symbols:
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _CFDataAppendBytes
+ _CFDataCreate
+ _CFDataCreateMutable
+ _CFDictionaryCreate
+ _SecKeyCreateWithData
+ _SecKeyVerifySignature
+ _dnssd_hints_find_host_name_conflict
+ _dnssd_hints_finish_name_conflict_check
+ _kSecAttrKeyClassPublic
+ _kSecKeyAlgorithmECDSASignatureDigestRFC4754
+ _sqlite3_bind_blob
+ _srp_sig0_verify
CStrings:
+ "%{public}s: %{private, mask.hash}s has %d messages in the database, not saving any more."
+ "%{public}s: %{public}s %{private, mask.hash}s with key tag %x conflicts with existing %u second key lease on key tag %x expiring at %{public}s"
+ "%{public}s: %{public}s lease query failed: %d%{public}s"
+ "%{public}s: CFDataCreate failed when creating data_to_verify_cfdata"
+ "%{public}s: CFDataCreate failed when creating sig_to_match_cfdata"
+ "%{public}s: CFDataCreateMutable failed when creating public key CFMutableDataRef"
+ "%{public}s: CFDictionaryCreate failed when creating public key options CFDictionaryRef"
+ "%{public}s: Failed to create public_key"
+ "%{public}s: Failed to data_to_verify_cfdata"
+ "%{public}s: Failed to write canonical name - canonical_signer_name_length: %lu"
+ "%{public}s: Invalid KEY length - KEY len: %d"
+ "%{public}s: Invalid SIG(0) length - SIG(0) length: %d"
+ "%{public}s: Invalid signer name length - signer name length: %zu"
+ "%{public}s: KEY algorithm does not match the SIG(0) algorithm - KEY algorithm: %u, SIG(0) algorithm: %u"
+ "%{public}s: SecKeyCreateWithData failed when creating public key SecKeyRef"
+ "%{public}s: SecKeyVerifySignature failed to validate - Error Description: %s"
+ "%{public}s: Unsupported KEY algorithm - KEY algorithm: %u"
+ "%{public}s: Unsupported SIG(0) algorithm - SIG(0) algorithm: %u"
+ "%{public}s: data already present for %{private, mask.hash}s %x/%x"
+ "%{public}s: failed to consume sandbox token: %s"
+ "%{public}s: insert failed for %{private, mask.hash}s %x/%x with unexpected error %d"
+ "%{public}s: signature is not valid"
+ "%{public}s: successfully consumed sandbox token"
+ "%{public}s: successfully inserted instance for %{private, mask.hash}s %x/%x"
+ "%{public}s: successfully inserted lease for %x/%x"
+ "%{public}s: successfully inserted message for %x/%x"
+ "%{public}s: successfully updated instance for %{private, mask.hash}s %x/%x"
+ "%{public}s: successfully updated lease for %x/%x: %d"
+ "%{public}s: successfully updated message receive_time for %x/%x: %d"
+ "%{public}s: unable to bind instance hint: %d %{public}s"
+ "%{public}s: unable to bind instance instance_name: %d %{public}s"
+ "%{public}s: unable to bind instance key_tag: %d %{public}s"
+ "%{public}s: unable to bind lease update column %d key_tag: %d %{public}s"
+ "%{public}s: unable to bind message blob: %d %{public}s"
+ "%{public}s: unable to bind message hint: %d %{public}s"
+ "%{public}s: unable to bind message hostname: %d %{public}s"
+ "%{public}s: unable to bind message key_tag: %d %{public}s"
+ "%{public}s: unable to bind message prefix: %d %{public}s"
+ "%{public}s: unable to bind message removes_all: %d %{public}s"
+ "%{public}s: unable to bind message update column %d key_tag: %d %{public}s"
+ "%{public}s: unable to fetch message count for %{private, mask.hash}s: %d %{public}s"
+ "%{public}s: unable to insert lease %x/%x: %d %{public}s"
+ "%{public}s: unable to insert message: %d %{public}s"
+ "%{public}s: unable to prepare the instance insert statement: %d%{public}s"
+ "%{public}s: unable to prepare the instance update statement: %d%{public}s"
+ "%{public}s: unable to prepare the leases insert statement: %d: %{public}s"
+ "%{public}s: unable to prepare the leases update statement: %d%{public}s"
+ "%{public}s: unable to prepare the message count statement: %d: %{public}s"
+ "%{public}s: unable to prepare the messages insert statement: %d: %{public}s"
+ "%{public}s: unable to prepare the messages update statement: %d%{public}s"
+ "%{public}s: unable to update lease %x/%x: %d %{public}s"
+ "%{public}s: unable to update message %x/%x: %d %{public}s"
+ "%{public}s: update failed for %{private, mask.hash}s %x/%x with unexpected error %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/adv-ctl-server.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/cti-services.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-client.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-hints.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-proxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/ioloop.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/macos-ioloop.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/netdata-tracker.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/node-type-tracker.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/omr-watcher.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/probe-srp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/service-publisher.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/service-tracker.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/srp-decompress.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/srp-mdns-proxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/srp-parse.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/state-machine.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/thread-device.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/thread-service.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/thread-tracker.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c3mLdQ/Sources/mDNSResponderExtras/ServiceRegistration/tls-macos.c"
+ "13:43:10"
+ "INSERT INTO instances(name, key_tag, hint, prefix) VALUES (?, ?, ?, ?);"
+ "INSERT INTO leases(host_expiry, key_expiry, receive_time, key_tag, hint) VALUES (?, ?, ?, ?, ?);"
+ "INSERT INTO messages(key_tag, hint, message, removes_all, hostname) VALUES (?, ?, ?, ?, ?);"
+ "Jun 25 2026"
+ "SELECT COUNT(hint) from messages WHERE key_tag = ?;"
+ "SELECT leases.key_tag, leases.receive_time, leases.key_expiry FROM leases, messages WHERE leases.key_expiry + leases.receive_time > ?   AND message.hostname = ?   AND key_tag != ?   AND leases.key_tag = message.key_tag AND leases.hint = message.hint ORDER BY leases.key_expiry + leases.receive_time DESC LIMIT 1"
+ "SELECT leases.key_tag, leases.receive_time, leases.key_lease FROM leases, instances WHERE leases.key_expiry + leases.receive_time > ?   AND instances.name = ?   AND key_tag != ?   AND leases.key_tag = instances.key_tag AND leases.hint = instances.hint ORDER BY leases.receive_time + leases.key_lease DESC LIMIT 1"
+ "UPDATE instances SET key_tag = ?, hint = ? WHERE name = ? and prefix = ?;"
+ "UPDATE leases SET host_expiry = ?, key_expiry = ?, receive_time = ? WHERE key_tag = ? AND hint = ?;"
+ "UPDATE messages SET receive_time = ? WHERE key_tag = ? AND hint = ?;"
+ "create_data_to_verify"
+ "create_public_sec_key"
+ "dnssd_hints_find_host_name_conflict"
+ "dnssd_hints_find_instance_name_conflict"
+ "dnssd_hints_finish_name_conflict_check"
+ "dnssd_hints_sqlite_instance_to_message_map_add"
+ "dnssd_hints_sqlite_message_update"
+ "probe_result %d %d %d %d|"
+ "srp_sig0_verify"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/adv-ctl-server.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/cti-services.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-client.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-hints.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-proxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/ioloop.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/macos-ioloop.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/netdata-tracker.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/node-type-tracker.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/omr-watcher.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/probe-srp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/service-publisher.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/service-tracker.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/srp-decompress.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/srp-mdns-proxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/srp-parse.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/state-machine.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/thread-device.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/thread-service.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/thread-tracker.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BJs5M2/Sources/mDNSResponderExtras/ServiceRegistration/tls-macos.c"
- "10:27:09"
- "Jun 14 2026"

```
