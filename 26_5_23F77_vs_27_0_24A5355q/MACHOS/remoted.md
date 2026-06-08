## remoted

> `/usr/libexec/remoted`

```diff

-219.120.2.0.0
-  __TEXT.__text: 0x41d10
+243.0.0.0.0
+  __TEXT.__text: 0x3d41c
   __TEXT.__auth_stubs: 0x1810
   __TEXT.__objc_stubs: 0x24a0
   __TEXT.__objc_methlist: 0x1578
   __TEXT.__const: 0x1fa
-  __TEXT.__oslogstring: 0x859c
-  __TEXT.__cstring: 0x2171
-  __TEXT.__objc_methname: 0x2549
-  __TEXT.__objc_classname: 0x2f4
+  __TEXT.__oslogstring: 0x842c
+  __TEXT.__cstring: 0x21a4
+  __TEXT.__objc_methname: 0x2543
+  __TEXT.__objc_classname: 0x2c9
   __TEXT.__objc_methtype: 0x79b
-  __TEXT.__gcc_except_tab: 0x14d4
-  __TEXT.__unwind_info: 0x1000
-  __DATA_CONST.__auth_got: 0xc18
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x1370
-  __DATA_CONST.__cfstring: 0xe80
+  __TEXT.__gcc_except_tab: 0x1120
+  __TEXT.__unwind_info: 0xdb8
+  __DATA_CONST.__const: 0x12c8
+  __DATA_CONST.__cfstring: 0xea0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0xc18
+  __DATA_CONST.__got: 0x230
   __DATA.__objc_const: 0x2840
   __DATA.__objc_selrefs: 0x980
   __DATA.__objc_ivar: 0x220
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x6d4
-  __DATA.__bss: 0x3f0
+  __DATA.__bss: 0x3b0
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B09E317A-B35B-3FE6-8025-A69B367905D6
-  Functions: 1427
-  Symbols:   492
-  CStrings:  1920
+  UUID: B6CC95FD-1F1A-34C9-A685-028702077803
+  Functions: 1370
+  Symbols:   482
+  CStrings:  1905
 
Symbols:
+ _CFArrayGetTypeID
+ _CFDictionaryGetTypeID
+ __CFXPCCreateXPCObjectFromCFObject
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
+ _xpc_copy
- _clock_settime
- _ntp_adjtime
- _os_variant_is_recovery
- _remote_device_get_name
- _remote_device_get_type
- _remote_device_set_connected_callback
- _remote_device_set_disconnected_callback
- _remote_device_start_browsing
- _remote_device_timesync
- _sntp_calc_delay
- _sntp_calc_offset
- _sntp_client_process_response
- _sntp_datestamp_to_nsec
- _sntp_datestamp_to_timespec
- _sntp_header_ntoh
- _sntp_packet_ntoh
- _sntp_shortstamp_ntoh
- _sntp_timestamp_ntoh
- _sntp_timestamp_to_datestamp
CStrings:
+ "%{public}@> %{public}s TLS."
+ "%{public}@> Connect failed for %{public}s"
+ "%{public}@> No listener for \"%{public}s\""
+ "%{public}@> Peer %{public}s TLS."
+ "%{public}@> Unable to create listener for \"%{public}s\""
+ "%{public}@> Unable to listen for \"%{public}s\""
+ "%{public}@> advertised endpoint %@ %{public}s"
+ "%{public}@> listening on %@ (state %u, error %{public}@)"
+ "%{public}@> received error: %{public}@"
+ "Can't find 3rd parent for %{public}s"
+ "Chassis manifest is %{public}srequired for TLS on compute node%{public}s"
+ "Chassis manifest lists cctrl UDID '%{public}@'"
+ "Chassis manifest lists cnode UDID '%{public}@' at carrier %lc index %lc"
+ "CoalescedTargetProperties"
+ "EncryptSocketData"
+ "Identity creation not supported."
+ "InDiagnosticsMode"
+ "Peer's DAK attestation contains HW identity: %{public}@"
+ "Populated property with MG: %{public}s"
+ "QbaRRU+muJGhwQ1SZUpQ1g"
+ "Received a timesync request expecting no reply: %{public}@"
+ "Received a timesync request without payload: %{public}@"
+ "RemoteService '%{public}s': Failed to set expose policy"
+ "TLS is %{public}s for loopback%{public}s"
+ "Unable to fetch MG property: %{public}s"
+ "Unexpected 3rd parent class %{public}@"
+ "Unsupported class %{public}@"
+ "advertised endpoint %@ %{public}s"
+ "assertion failure: \"(strncmp(ifname, \"en\", strlen(\"en\")) == 0) || (strncmp(ifname, \"anpi\", strlen(\"anpi\")) == 0) || (strncmp(ifname, \"anri\", strlen(\"anri\")) == 0)\" -> %llu"
+ "assertion failure: \"response\" -> %llu"
+ "browse_results_changed: %{public}@ -> %{public}@"
+ "create_local_device_identity denied: missing entitlement (client=\"%{public}s\")"
+ "delete_local_device_identity denied: missing entitlement (client=\"%{public}s\")"
+ "heartbeat %{public}s"
+ "legacyTimesync:"
+ "legacy_timesync"
+ "listening on %@ (state %u, error %{public}@)"
+ "nw_browser_state_failed: %{public}@"
+ "nw_browser_state_waiting: %{public}@"
+ "received bonjour browser error: %{public}@"
+ "received error: %{public}@"
+ "t1.seconds"
+ "t1.subsecs"
- "%{public}@> %s TLS."
- "%{public}@> Connect failed for %s"
- "%{public}@> No listener for \"%s\""
- "%{public}@> Peer %s TLS."
- "%{public}@> Received a timesync request expecting no reply"
- "%{public}@> Received a timesync request without payload"
- "%{public}@> Unable to create listener for \"%s\""
- "%{public}@> Unable to listen for \"%s\""
- "%{public}@> advertised endpoint %@ %s"
- "%{public}@> create_sntp_response_payload failed"
- "%{public}@> listening on %@ (state %u, error %@)"
- "%{public}@> received error: %@"
- "%{public}@> sending timesync request"
- "%{public}@> time sync failed: invalid sntp response payload"
- "%{public}@> time sync request failed: error on connection"
- "%{public}@> timesync failed: device not connected"
- "%{public}@> timesync failed: remote device doesn't support timesync"
- "%{public}@> timesync failed: timesync already in progress"
- "%{public}s disconnected, timesync stop"
- "3kmXfug8VcxLI5yEmsqQKw"
- "Can't find 3rd parent for %s"
- "Chassis manifest is %srequired for TLS on compute node%s"
- "Chassis manifest lists cctrl UDID '%@'"
- "Chassis manifest lists cnode UDID '%@' at carrier %lc index %lc"
- "PACING with ntp_adjtime of %lld ns => resulting offset: %ld ns freq: %ld PPM"
- "Peer's DAK attestation contains HW identity: %@"
- "Populated property with MG: %s"
- "RemoteService '%s': Failed to set expose policy"
- "TLS is %s for loopback%s"
- "Unable to fetch MG property: %s"
- "Unexpected 3rd parent class %@"
- "Unsupported class %@"
- "advertised endpoint %@ %s"
- "assertion failure: \"(strncmp(ifname, \"en\", strlen(\"en\")) == 0) || (strncmp(ifname, \"anpi\", strlen(\"anpi\")) == 0)\" -> %llu"
- "assertion failure: \"sntp_request_payload\" -> %llu"
- "assertion failure: \"sntp_response_payload\" -> %llu"
- "clock_settime: %{errno}d"
- "com.apple.remoted.timesync"
- "device_timesync: Client lacks privilege (client=\"%{public}s\")"
- "enabled remoted timesync"
- "fail"
- "invalid sntp response payload"
- "listening on %@ (state %u, error %@)"
- "ntp_adjtime returned error: %d"
- "nw_browser_state_failed: %@"
- "nw_browser_state_waiting: %@"
- "nw_listener_state_failed: %@"
- "received bonjour browser error: %@"
- "received error: %@"
- "rsd_timesync"
- "setting time from %{timespec}.*P to %{timespec}.*P"
- "sntp exchange failed: %d"
- "start timesync with %{public}s"
- "success"
- "timesync"
- "timesync with %{public}s %{public}s"
- "timesyncWithCallback:"
- "v16@?0@\"OS_remote_device\"8"

```
