## libquic.dylib

> `/usr/lib/libquic.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`

```diff

-6681.0.498.502.1
-  __TEXT.__text: 0xcd378
+6681.0.514.502.1
+  __TEXT.__text: 0xd0174
   __TEXT.__objc_methlist: 0x244
-  __TEXT.__const: 0x3a5
-  __TEXT.__cstring: 0x8700
-  __TEXT.__oslogstring: 0x11c3e
-  __TEXT.__unwind_info: 0xd10
+  __TEXT.__const: 0x3b5
+  __TEXT.__cstring: 0x87e1
+  __TEXT.__oslogstring: 0x12459
+  __TEXT.__unwind_info: 0xd28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2558
+  __DATA_CONST.__const: 0x2590
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x90
-  __AUTH_CONST.__const: 0xc90
+  __DATA_CONST.__got: 0x98
+  __AUTH_CONST.__const: 0xcd0
   __AUTH_CONST.__cfstring: 0x1320
   __AUTH_CONST.__objc_const: 0xf8
-  __AUTH_CONST.__auth_got: 0xdc0
+  __AUTH_CONST.__auth_got: 0xdd0
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x110
+  __AUTH.__data: 0x118
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x6c
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x520
   __DATA_DIRTY.__data: 0x1c
-  __DATA_DIRTY.__bss: 0x660
+  __DATA_DIRTY.__bss: 0x670
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1146
-  Symbols:   1699
-  CStrings:  2584
+  Functions: 1153
+  Symbols:   1708
+  CStrings:  2604
 
Symbols:
+ ___quic_conn_listen_handler_added_block_invoke
+ ___quic_conn_log_send_state_block_invoke
+ ___quic_stream_allocate_block_invoke
+ __nw_protocol_pending_flow
+ _nw_protocol_definition_set_listen_handler_added
+ _nw_protocol_definition_set_log_send_state
+ _quic_conn_access_stream_state
+ _quic_conn_listen_handler_added
+ _quic_conn_log_send_state
+ _quic_conn_process_pending_inbound_streams
+ _quic_migration_get_last_event_migration_time_ms
+ _quic_path_get_statistics_bytes_in_flight
+ _quic_path_is_primary
+ _quic_pmtud_create
- ____quic_pmtud_create_block_invoke
- ___quic_pmtud_change_path_block_invoke
- __quic_pmtud_create
- _quic_pmtud_change_path
- _quic_pmtud_destroy
CStrings:
+ "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] PENDING_FLOW but no pending stream found"
+ "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] buffering STREAM frame into pending stream"
+ "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] deallocating unadopted pending inbound stream"
+ "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] listen handler denied pending stream; deallocating"
+ "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] no listen handler; deferring inbound stream"
+ "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] promoting pending inbound stream"
+ "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] stream send state: snd_state=%u offset=%llu remote_max_stream=%llu sendq_len=%llu blocked=%d snd_hiwat=%llu"
+ "%{public}s %{public}s [%{public}s-%{public}s] migration state: established=%u probing=%u validated=%u multipath_type=%u last_event_ms=%u"
+ "%{public}s %{public}s [%{public}s-%{public}s] path if=%{public}s scid=%{public}s dcid=%{public}s state=%{public}s datapath=%d probing=%d validated=%d bytes_in_flight=%u srtt_ms=%llu flow_controlled=%d"
+ "%{public}s %{public}s [%{public}s-%{public}s] send state: conn_state=%u conn_offset=%llu remote_max_data=%llu conn_blocked=%d conn_sendq_len=%llu allowed_cwnd=%llu bytes_in_flight=%llu conn_probe_failed=%d write_probe_failed=%d"
+ "%{public}s %{public}s [%{public}s-%{public}s] skipping probe connectivity keep-alive over companion link on non-watch platform"
+ "%{public}s %{public}s [S%llu] stream send state: snd_state=%u offset=%llu remote_max_stream=%llu sendq_len=%llu blocked=%d snd_hiwat=%llu"
+ "%{public}s %{public}s migration state: established=%u probing=%u validated=%u multipath_type=%u last_event_ms=%u"
+ "%{public}s %{public}s path if=%{public}s scid=%{public}s dcid=%{public}s state=%{public}s datapath=%d probing=%d validated=%d bytes_in_flight=%u srtt_ms=%llu flow_controlled=%d"
+ "%{public}s %{public}s send state: conn_state=%u conn_offset=%llu remote_max_data=%llu conn_blocked=%d conn_sendq_len=%llu allowed_cwnd=%llu bytes_in_flight=%llu conn_probe_failed=%d write_probe_failed=%d"
+ "%{public}s [S%llu] PENDING_FLOW but no pending stream found"
+ "%{public}s [S%llu] skipping FC re-init (was pending)"
+ "%{public}s [S%llu] skipping remaining FC setup for pending stream"
+ "?"
+ "B24@?0Q8^{quic_stream=Q^{quic_conn}^{nw_protocol_metadata}QQQQQ{sbuf=QQ}{sbuf=QQ}QQQQQQQQQQQ{nw_frame_array_s=^{nw_frame}^^{nw_frame}}QQQQQQ{?=QQQ}{?=QQQ}SCC[4c]^{quic_reassq}^{quic_reassq}^{quic_reassq}^{quic_reassq}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b8I}16"
+ "PMTUD_%s_%lx"
+ "quic_conn_access_stream_state"
+ "quic_conn_listen_handler_added"
+ "quic_conn_log_send_state"
+ "quic_conn_log_send_state_block_invoke"
+ "quic_conn_process_pending_inbound_streams"
+ "quic_migration_get_last_event_migration_time_ms"
+ "quic_path_get_statistics_bytes_in_flight"
+ "quic_path_is_primary"
+ "quic_pmtud_create"
+ "quic_pmtud_create_block_invoke"
+ "quic_stream_setup_pending_inbound_stream"
- "%{public}s %{public}s [%{public}s-%{public}s] cannot find alternate path for pmtud; disarming timer"
- "%{public}s over released PMTUD"
- "%{public}s using shared PMTUD for path %p"
- "B24@?0Q8^{quic_stream=Q^{quic_conn}^{nw_protocol_metadata}QQQQQ{sbuf=QQ}{sbuf=QQ}QQQQQQQQQQQ{nw_frame_array_s=^{nw_frame}^^{nw_frame}}QQQQQQ{?=QQQ}{?=QQQ}SCC[4c]^{quic_reassq}^{quic_reassq}^{quic_reassq}^{quic_reassq}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}{?=^{quic_stream}^^{quic_stream}}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b9I}16"
- "PMTUD"
- "PMTUD_%s"
- "PMTUD_initial"
- "_quic_pmtud_create"
- "_quic_pmtud_create_block_invoke"
- "quic_pmtud_change_path"
- "quic_pmtud_change_path_block_invoke"
- "quic_pmtud_destroy"
```
