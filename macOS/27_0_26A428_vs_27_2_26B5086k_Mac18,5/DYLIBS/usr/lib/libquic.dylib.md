## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-6681.1.1.0.0
-  __TEXT.__text: 0xcf214
+6681.40.80.0.0
+  __TEXT.__text: 0xcfa90
   __TEXT.__objc_methlist: 0x244
-  __TEXT.__const: 0x395
-  __TEXT.__cstring: 0x8823
-  __TEXT.__oslogstring: 0x12459
+  __TEXT.__const: 0x3a5
+  __TEXT.__cstring: 0x88b5
+  __TEXT.__oslogstring: 0x1260d
   __TEXT.__unwind_info: 0x12d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c00
+  __DATA_CONST.__const: 0x1c30
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8

   __AUTH_CONST.__const: 0x1870
   __AUTH_CONST.__cfstring: 0x1320
   __AUTH_CONST.__objc_const: 0xf8
-  __AUTH_CONST.__auth_got: 0xd50
+  __AUTH_CONST.__auth_got: 0xd40
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x118
   __DATA.__objc_ivar: 0xc

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1168
-  Symbols:   1719
-  CStrings:  2606
+  Functions: 1169
+  Symbols:   1718
+  CStrings:  2618
 
Symbols:
+ ___os_log_helper_1_2_16_8_34_4_0_8_34_4_0_4_0_4_0_4_0_4_0_8_34_8_34_4_0_4_0_4_0_4_0_4_0_4_0
+ __quic_timer_remove
+ _quic_migration_is_ignoring_events
+ _quic_migration_record_event
- ___os_log_helper_1_2_14_8_34_4_0_4_0_4_0_4_0_4_0_8_34_8_34_4_0_4_0_4_0_4_0_4_0_4_0
- _nw_protocol_establishment_report_set_quic_stateless_reset_during_path_probe
- _nw_protocol_establishment_report_set_quic_stateless_reset_received
- _quic_migration_report_event
- _quic_timer_remove
CStrings:
+ "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Migration supported: %s, Keep-alives sent/acknowledged: %u/%u\n\tMigrations: %u succeeded, %u failed, paths validated: %u\n\tStateless reset: received %s, during path probe %s\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
+ "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Migration supported: %s, Keep-alives sent/acknowledged: %u/%u, ECN state: %s, L4S: %s\n\tRTT: base %llu ms, network %llu ms, latest %llu ms, minimum %llu ms, smoothed %llu ms (variance %llu ms)\n\tPath MTU: %hu, minimum MSS: %hu\n\tMigrations: %u succeeded, %u failed, paths validated: %u\n\tStateless reset: received %s, during path probe %s\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
+ "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] early data verdict pending, holding application data"
+ "%{public}s %{public}s [%{public}s-%{public}s] no longer in fallback mode over %{public}s"
+ "%{public}s acked packet <%{public}s %llu> (length %u bytes, sent %llu)"
+ "%{public}s connection closing; deferring destroy of unprocessed acked packet <%{public}s %llu>"
+ "%{public}s handshake not confirmed, not retransmitting application data"
+ "%{public}s initialized loss recovery timer"
+ "%{public}s inner_state is null or 0"
+ "%{public}s loss_recovery->recovery_timer is null or 0"
+ "%{public}s migration event %u: result '%{public}s' (repeat %u), time %u ms, migration time %u ms, RTT %u ms -> %u ms, type '%{public}s' -> '%{public}s', LQM %d -> %d, fallback? %d primary? %d priority? %d loss? %d"
+ "%{public}s reset loss recovery timer to %llu"
+ "%{public}s timer entry is not on this timer"
+ "_quic_timer_remove"
+ "invalid path state"
+ "no connection ID"
+ "no viable path"
+ "path lost"
+ "path validation failed"
+ "quic_migration_is_ignoring_events"
+ "quic_migration_record_event"
+ "success"
+ "v24@?0^{quic_timer=}8^{quic_timer_entry=}16"
- "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Migration supported: %s, Keep-alives sent/acknowledged: %u/%u\n\tMigration events: %u, paths validated: %u\n\tStateless reset: received %s, during path probe %s\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
- "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Migration supported: %s, Keep-alives sent/acknowledged: %u/%u, ECN state: %s, L4S: %s\n\tRTT: base %llu ms, network %llu ms, latest %llu ms, minimum %llu ms, smoothed %llu ms (variance %llu ms)\n\tPath MTU: %hu, minimum MSS: %hu\n\tMigration events: %u, paths validated: %u\n\tStateless reset: received %s, during path probe %s\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
- "%{public}s initialized loss recovery timer (id %u)"
- "%{public}s loss_recovery->timer_id is null or 0"
- "%{public}s migration event %u: time %u ms, migration time %u ms, RTT %u ms -> %u ms, type '%{public}s' -> '%{public}s', LQM %d -> %d, fallback? %d primary? %d priority? %d loss? %d"
- "%{public}s new_path is null or 0"
- "%{public}s removed packet <%{public}s %llu> (length %u bytes, sent %llu) from outstanding packets"
- "%{public}s reset loss recovery timer (id %u) to %llu"
- "quic_migration_report_event"
- "quic_timer_remove"
- "v20@?0^{quic_timer=}8C16"
```
