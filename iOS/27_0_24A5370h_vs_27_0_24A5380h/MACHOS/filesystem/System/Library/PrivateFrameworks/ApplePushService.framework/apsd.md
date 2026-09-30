## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

-  __TEXT.__text: 0x1175bc
-  __TEXT.__auth_stubs: 0x34a0
-  __TEXT.__objc_stubs: 0x10b80
+  __TEXT.__text: 0x1177f0
+  __TEXT.__auth_stubs: 0x34b0
+  __TEXT.__objc_stubs: 0x10ba0
   __TEXT.__init_offsets: 0xc
-  __TEXT.__objc_methlist: 0xb808
+  __TEXT.__objc_methlist: 0xb7f0
   __TEXT.__objc_methname: 0x1b8d5
   __TEXT.__objc_classname: 0x132b
   __TEXT.__objc_methtype: 0x5559
   __TEXT.__cstring: 0xfc14
-  __TEXT.__const: 0xd973
-  __TEXT.__oslogstring: 0x13fd5
-  __TEXT.__gcc_except_tab: 0x2650
+  __TEXT.__const: 0xd983
+  __TEXT.__oslogstring: 0x14125
+  __TEXT.__gcc_except_tab: 0x2680
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__constg_swiftt: 0x1340
   __TEXT.__swift5_typeref: 0x970

   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__unwind_info: 0x4208
+  __TEXT.__unwind_info: 0x4210
   __TEXT.__eh_frame: 0x320
-  __DATA_CONST.__const: 0x9948
-  __DATA_CONST.__cfstring: 0x8480
+  __DATA_CONST.__const: 0x9970
+  __DATA_CONST.__cfstring: 0x8560
   __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x1a68
-  __DATA_CONST.__got: 0x880
+  __DATA_CONST.__auth_got: 0x1a70
+  __DATA_CONST.__got: 0x938
   __DATA_CONST.__auth_ptr: 0x1e0
-  __DATA.__objc_const: 0x1c530
-  __DATA.__objc_selrefs: 0x5660
-  __DATA.__objc_ivar: 0xbac
+  __DATA.__objc_const: 0x1c540
+  __DATA.__objc_selrefs: 0x5668
+  __DATA.__objc_ivar: 0xbb0
   __DATA.__objc_data: 0x3618
   __DATA.__data: 0x4660
   __DATA.__bss: 0x1360

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6775
-  Symbols:   1193
-  CStrings:  9746
+  Functions: 6772
+  Symbols:   1194
+  CStrings:  9762
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methname : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
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
+ "com.apple.icloud-container."
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
