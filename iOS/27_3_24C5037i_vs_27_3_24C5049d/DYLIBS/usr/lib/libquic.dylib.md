## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-6681.60.32.0.0
-  __TEXT.__text: 0xcfc24
+6681.60.37.0.0
+  __TEXT.__text: 0xd0a38
   __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x3b5
-  __TEXT.__cstring: 0x8907
-  __TEXT.__oslogstring: 0x1271c
-  __TEXT.__unwind_info: 0x12b8
+  __TEXT.__cstring: 0x899c
+  __TEXT.__oslogstring: 0x12961
+  __TEXT.__unwind_info: 0x12c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1161
-  Symbols:   1665
-  CStrings:  2625
+  Functions: 1164
+  Symbols:   1668
+  CStrings:  2633
 
Symbols:
+ _quic_conn_reset_streams_after_early_data_rejection
+ _quic_packet_builder_get_pending_stream_frame_count
+ _quic_packet_builder_remove_stream_frames
CStrings:
+ "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] received STREAM_DATA_BLOCKED (max=%llu), app read %llu bytes and has yet to read %llu bytes, stream receive window is %llu bytes, local stream max data is %llu bytes and the last received offset is %llu; reassq dequeue offset %llu, available %llu, buffered %llu, first buffered offset %lld, dequeue scheduled %d"
+ "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] stream send state: snd_state=%u offset=%llu remote_max_stream=%llu sendq_len=%llu blocked=%d snd_hiwat=%llu queued_frames=%u lowest_queued_offset=%lld"
+ "%{public}s %{public}s [%{public}s-%{public}s] dropped %u queued STREAM frames"
+ "%{public}s %{public}s [%{public}s-%{public}s] failed to process %{public}s frame in packet %llu; dropping the rest of an acknowledged packet"
+ "%{public}s %{public}s [S%llu] stream send state: snd_state=%u offset=%llu remote_max_stream=%llu sendq_len=%llu blocked=%d snd_hiwat=%llu queued_frames=%u lowest_queued_offset=%lld"
+ "%{public}s dropping stream data [%llu, %llu) (%llu bytes): frame no longer valid"
+ "%{public}s early data verdict pending, holding application data in the packet builder"
+ "count"
+ "quic_conn_reset_streams_after_early_data_rejection"
+ "quic_packet_builder_get_pending_stream_frame_count"
+ "quic_packet_builder_remove_stream_frames"
- "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] received STREAM_DATA_BLOCKED (max=%llu), app read %llu bytes and has yet to read %llu bytes, stream receive window is %llu bytes, local stream max data is %llu bytes and the last received offset is %llu"
- "%{public}s %{public}s [%{public}s-%{public}s] [S%llu] stream send state: snd_state=%u offset=%llu remote_max_stream=%llu sendq_len=%llu blocked=%d snd_hiwat=%llu"
- "%{public}s %{public}s [S%llu] stream send state: snd_state=%u offset=%llu remote_max_stream=%llu sendq_len=%llu blocked=%d snd_hiwat=%llu"
```
