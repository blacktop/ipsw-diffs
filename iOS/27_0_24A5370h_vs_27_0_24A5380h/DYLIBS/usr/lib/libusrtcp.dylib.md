## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-  __TEXT.__text: 0x5aa20
+  __TEXT.__text: 0x5b420
   __TEXT.__const: 0x244
-  __TEXT.__oslogstring: 0xe618
-  __TEXT.__cstring: 0x1a5e
-  __TEXT.__unwind_info: 0x450
+  __TEXT.__oslogstring: 0xe6be
+  __TEXT.__cstring: 0x1a8e
+  __TEXT.__unwind_info: 0x458
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x410
   __DATA_CONST.__got: 0x0

   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 329
-  Symbols:   1013
-  CStrings:  1116
+  Functions: 333
+  Symbols:   1021
+  CStrings:  1120
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _rbbr_sender_utilizing_rwnd
+ _rbbr_update_win
+ _tcp_calc_rcv_window
+ _tcp_clear_recv_bg
+ _tcp_set_recv_bg
- _rbbr_apply_cruise_backoff
CStrings:
+ "%{public}s %{public}s recv_bg: cleared (was %{public}s)"
+ "%{public}s %{public}s recv_bg: reactive teardown (recv_bg_viable=%d algo_mismatch=%d active=%u desired=%d)"
+ "%{public}s %{public}s recv_bg: switching to %{public}s bg=%d recv_cc_algo=%u"
+ "%{public}s new CE count (%llu) can't be less than current CE count (%llu)OR newly ACKed (%llu) can't be less that current ACKed (%llu)"
+ "%{public}s new CE count (%llu) can't be less than current CE count (%llu)OR newly ACKed (%llu) can't be less that current ACKed (%llu), backtrace limit exceeded"
+ "%{public}s new CE count (%llu) can't be less than current CE count (%llu)OR newly ACKed (%llu) can't be less that current ACKed (%llu), dumping backtrace:%{public}s"
+ "%{public}s new CE count (%llu) can't be less than current CE count (%llu)OR newly ACKed (%llu) can't be less that current ACKed (%llu), no backtrace"
+ "tcp_clear_recv_bg"
+ "tcp_rbbr_init"
+ "tcp_rbbr_switch_to"
+ "tcp_set_recv_bg"
- "%{public}s %u packets were newly CE marked"
- "%{public}s already processed AccECN field/options for this ACK"
- "%{public}s new CE count (%u) can't be less than current CE count (%u)OR newly ACKed (%u) can't be less that current ACKed (%u)"
- "%{public}s new CE count (%u) can't be less than current CE count (%u)OR newly ACKed (%u) can't be less that current ACKed (%u), backtrace limit exceeded"
- "%{public}s new CE count (%u) can't be less than current CE count (%u)OR newly ACKed (%u) can't be less that current ACKed (%u), dumping backtrace:%{public}s"
- "%{public}s new CE count (%u) can't be less than current CE count (%u)OR newly ACKed (%u) can't be less that current ACKed (%u), no backtrace"
- "tcp_process_accecn"

```
