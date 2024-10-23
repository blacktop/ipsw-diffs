## BasebandTraceHelper

> `/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`

```diff

-1183.0.0.0.0
-  __TEXT.__text: 0x46410
-  __TEXT.__auth_stubs: 0x1220
+1209.0.0.0.0
+  __TEXT.__text: 0x4743c
+  __TEXT.__auth_stubs: 0x1250
   __TEXT.__init_offsets: 0x30
-  __TEXT.__gcc_except_tab: 0x3300
-  __TEXT.__const: 0x260c
-  __TEXT.__cstring: 0x1856
-  __TEXT.__oslogstring: 0x23b3
-  __TEXT.__unwind_info: 0x14b8
+  __TEXT.__gcc_except_tab: 0x3758
+  __TEXT.__const: 0x262c
+  __TEXT.__cstring: 0x197b
+  __TEXT.__oslogstring: 0x23f6
+  __TEXT.__unwind_info: 0x1518
   __TEXT.__objc_methname: 0x119
   __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x7c0
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x7c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x920
-  __AUTH_CONST.__const: 0x20d0
+  __AUTH_CONST.__auth_got: 0x938
+  __AUTH_CONST.__const: 0x20e0
   __AUTH_CONST.__cfstring: 0x20
   __DATA.__data: 0x370
   __DATA.__bss: 0x68

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 963
-  Symbols:   1455
-  CStrings:  535
+  Functions: 964
+  Symbols:   1463
+  CStrings:  545
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZN19TraceSocketStreamer8snapshotEv
+ __ZN3abm23kLogStreamingStatisticsE
+ __ZN3abm27kLogStreamingStatsSentBytesE
+ __ZN3abm30kLogStreamingStatsDroppedBytesE
+ __ZN3abm31kLogStreamingStatsReceivedBytesE
+ _signal
CStrings:
+ "#I Streaming Statistics:\n%!s(MISSING)"
+ "/private/var/wireless/Library/Preferences/com.apple.AppleBasebandManager.Statistics.plist"
+ "Drop Bytes during Streaming Session: "
+ "Passive external AT Only"
+ "Received Bytes during Streaming Session: "
+ "Sent Bytes during Streaming Session: "
+ "Streaming Statistics:\n%!s(MISSING)"
+ "Watchdog timed out"
+ "error: Failed to send, error: %!s(MISSING)"
+ "get empty stats"
- "error: %!s(MISSING)"

```
