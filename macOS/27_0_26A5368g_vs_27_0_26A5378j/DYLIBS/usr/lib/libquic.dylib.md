## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-  __TEXT.__text: 0xcc8a0
+  __TEXT.__text: 0xcdcd4
   __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x395
-  __TEXT.__cstring: 0x86e0
-  __TEXT.__oslogstring: 0x11a0b
-  __TEXT.__unwind_info: 0xcb8
+  __TEXT.__cstring: 0x8700
+  __TEXT.__oslogstring: 0x11c3e
+  __TEXT.__unwind_info: 0xcb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1840
+  __DATA_CONST.__got: 0x90
+  __AUTH_CONST.__const: 0x1860
   __AUTH_CONST.__cfstring: 0x1320
   __AUTH_CONST.__objc_const: 0xf8
-  __AUTH_CONST.__auth_got: 0xd20
+  __AUTH_CONST.__auth_got: 0xd38
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x110
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x6c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x528
+  __DATA.__bss: 0x520
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x678
+  __DATA_DIRTY.__bss: 0x688
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1155
-  Symbols:   2010
-  CStrings:  2732
+  Functions: 1158
+  Symbols:   2016
+  CStrings:  2737
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
Symbols:
+ ___quic_conn_async_if_needed_block_invoke
+ ___quic_conn_async_if_needed_block_invoke_2
+ _nw_protocol_establishment_report_set_quic_stateless_reset_during_path_probe
+ _nw_protocol_establishment_report_set_quic_stateless_reset_received
+ _nw_protocol_instance_is_flushing
+ _quic_path_mark_migration_intent
CStrings:
+ "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Migration supported: %s, Keep-alives sent/acknowledged: %u/%u\n\tMigration events: %u, paths validated: %u\n\tStateless reset: received %s, during path probe %s\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
+ "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Migration supported: %s, Keep-alives sent/acknowledged: %u/%u, ECN state: %s, L4S: %s\n\tRTT: base %llu ms, network %llu ms, latest %llu ms, minimum %llu ms, smoothed %llu ms (variance %llu ms)\n\tPath MTU: %hu, minimum MSS: %hu\n\tMigration events: %u, paths validated: %u\n\tStateless reset: received %s, during path probe %s\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
+ "%{public}s %{public}s [%{public}s-%{public}s] cancelling pulse timer; current path is still usable"
+ "%{public}s %{public}s [%{public}s-%{public}s] cannot find alternate path for pmtud; disarming timer"
+ "%{public}s %{public}s [%{public}s-%{public}s] connection in PTO recovery for >= %u ms, closing connection"
+ "%{public}s %{public}s [%{public}s-%{public}s] no better path, but current path is still usable; not declaring it lost"
+ "%{public}s %{public}s [%{public}s-%{public}s] not arming pulse timer on companion path; expecting connectivity to resume"
+ "%{public}s %{public}s [%{public}s-%{public}s] suspending pulse timer while probing path over %{public}s"
+ "quic_path_mark_migration_intent"
- "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Migration supported: %s, Keep-alives sent/acknowledged: %u/%u\n\tMigration events: %u, paths validated: %u\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
- "%{public}s %{public}s [%{public}s-%{public}s] \n\tConnection attempts: %u, RETRY received: %s, PTOs: %u\n\tEarly data: %s, Migration supported: %s, Keep-alives sent/acknowledged: %u/%u, ECN state: %s, L4S: %s\n\tRTT: base %llu ms, network %llu ms, latest %llu ms, minimum %llu ms, smoothed %llu ms (variance %llu ms)\n\tPath MTU: %hu, minimum MSS: %hu\n\tMigration events: %u, paths validated: %u\n\tInbound unidirectional/bidirectional streams: %u/%u\n\tOutbound unidirectional/bidirectional streams: %u/%u\n\tDATA_BLOCKED frames sent/received: %u/%u\n\tSTREAM_DATA_BLOCKED frames sent/received: %u/%u\n"
- "%{public}s %{public}s [%{public}s-%{public}s] Connection in PTO recovery for >= %u ms, closing connection"
- "%{public}s %{public}s [%{public}s-%{public}s] cannot find alternate path for pmtud"

```
