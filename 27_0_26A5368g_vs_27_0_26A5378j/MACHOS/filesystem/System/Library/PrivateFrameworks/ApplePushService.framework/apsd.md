## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

-  __TEXT.__text: 0x13d3e0
-  __TEXT.__auth_stubs: 0x3430
-  __TEXT.__objc_stubs: 0x11d80
+  __TEXT.__text: 0x13d52c
+  __TEXT.__auth_stubs: 0x3440
+  __TEXT.__objc_stubs: 0x11da0
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0xc6d8
-  __TEXT.__const: 0x13310
-  __TEXT.__objc_methname: 0x1d015
-  __TEXT.__cstring: 0xefba
-  __TEXT.__oslogstring: 0x16155
+  __TEXT.__objc_methlist: 0xc6c0
+  __TEXT.__const: 0x13330
+  __TEXT.__objc_methname: 0x1d035
+  __TEXT.__cstring: 0xef9a
+  __TEXT.__oslogstring: 0x162a5
   __TEXT.__objc_classname: 0x129b
   __TEXT.__objc_methtype: 0x4fd9
-  __TEXT.__gcc_except_tab: 0x25f4
+  __TEXT.__gcc_except_tab: 0x2624
   __TEXT.__dlopen_cstrs: 0xae
   __TEXT.__ustring: 0x28
   __TEXT.__swift5_typeref: 0x8a6

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4238
+  __TEXT.__unwind_info: 0x4240
   __TEXT.__eh_frame: 0x3e0
-  __DATA_CONST.__const: 0xafa0
-  __DATA_CONST.__cfstring: 0x8f80
+  __DATA_CONST.__const: 0xafd0
+  __DATA_CONST.__cfstring: 0x9040
   __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x290

   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA_CONST.__auth_got: 0x1a30
-  __DATA_CONST.__got: 0x820
+  __DATA_CONST.__auth_got: 0x1a38
+  __DATA_CONST.__got: 0x920
   __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA.__objc_const: 0x1bdb8
-  __DATA.__objc_selrefs: 0x5c98
-  __DATA.__objc_ivar: 0xc58
+  __DATA.__objc_const: 0x1bdc8
+  __DATA.__objc_selrefs: 0x5ca0
+  __DATA.__objc_ivar: 0xc5c
   __DATA.__objc_data: 0x39c0
   __DATA.__data: 0x3bc8
   __DATA.__bss: 0x1bc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7042
-  Symbols:   1171
-  CStrings:  10347
+  Functions: 7039
+  Symbols:   1172
+  CStrings:  10361
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _nw_connection_copy_tcp_info_async
CStrings:
+ "%@ Schedule server update with change %@; isPowerEfficientToSendFilter %@"
+ "%@ tcp_info[%{public}@]: srtt=%ums rtt=%ums rttvar=%ums bw=%llubps cwnd=%u snd_wnd=%u rto=%ums unacked=%u tx=%llu rx=%llu retx=%llu"
+ "%@ tcp_info[%{public}@]: state=%u opts=%x snd_wscale=%u rcv_wscale=%u flags=%x rto=%u snd_mss=%u rcv_mss=%u rttcur=%u srtt=%u rttvar=%u ssthresh=%u cwnd=%u rcv_space=%u snd_wnd=%u snd_nxt=%u rcv_nxt=%u outif=%d sbbytes=%u tx=%llu retx=%llu unacked=%llu rx=%llu rxdup=%llu bw=%llu"
+ "<%@; connectedFor: %.1fs; isConnected: %@; serverIPAddress: %@; serverHostname: %@; linkQuality: %d; srtt: %@ms>"
+ "ContainerID"
+ "ZoneID"
+ "_lastTCPInfoLogTimeMach"
+ "_logTCPInfoAsync"
+ "_scheduleServerUpdateForChange:"
+ "cid"
+ "ck"
+ "logTCPInfoIfNeeded"
+ "met"
+ "n/a"
+ "smoothedRTTMilliseconds"
+ "smoothedRTTMillisecondsForInterface:"
+ "zid"
- " %u %x %u %u %x %u %u %u %u %u %u %u %u %u %u %u %u %d %u %llu %llu %llu %llu %llu %llu"
- "%@ Schedule server update with change %@; withTimer %@; shortInterval %@; isPowerEfficientToSendFilter %@"
- "<%@; connectedFor: %.1fs; isConnected: %@; serverIPAddress: %@; serverHostname: %@; linkQuality: %d>"
- "Failed to get tcp info data"
- "_scheduleServerUpdateWithChange:timer:"
- "_scheduleServerUpdateWithChange:timer:shortInterval:"
- "tcpInfoDescription"
- "tcpInfoDescriptionForInterface:"
- "tcp_info: %@"

```
