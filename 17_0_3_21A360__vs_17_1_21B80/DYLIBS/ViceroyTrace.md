## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-1965.73.1.6.0
-  __TEXT.__text: 0x70ee0
+2000.8.1.1.1
+  __TEXT.__text: 0x70f9c
   __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x5da0
+  __TEXT.__objc_methlist: 0x5db0
   __TEXT.__const: 0x1938
   __TEXT.__gcc_except_tab: 0x2bc
   __TEXT.__cstring: 0x85e4
   __TEXT.__oslogstring: 0x8358
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0xe00
+  __TEXT.__unwind_info: 0xdfc
   __TEXT.__objc_classname: 0x324
-  __TEXT.__objc_methname: 0x11c01
-  __TEXT.__objc_methtype: 0x1012
-  __TEXT.__objc_stubs: 0x9e80
+  __TEXT.__objc_methname: 0x11ccd
+  __TEXT.__objc_methtype: 0x1001
+  __TEXT.__objc_stubs: 0x9ee0
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0xaa0
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf4e8
-  __DATA_CONST.__objc_selrefs: 0x2c08
+  __DATA_CONST.__objc_const: 0xf518
+  __DATA_CONST.__objc_selrefs: 0x2c20
   __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__cfstring: 0xa120
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x580
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x1a0
+  __DATA.__objc_classrefs: 0x198
   __DATA.__objc_superrefs: 0xe8
-  __DATA.__objc_ivar: 0x1704
+  __DATA.__objc_ivar: 0x1708
   __DATA.__data: 0x548
   __DATA.__bss: 0xe8
   __DATA.__common: 0x21

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2576
-  Symbols:   8536
-  CStrings:  5097
+  Functions: 2578
+  Symbols:   8543
+  CStrings:  5101
 
Symbols:
+ -[StreamGroupStats setTotalVideoFrameIncompleteNextTSRate:]
+ -[StreamGroupStats totalVideoFrameIncompleteNextTSRate]
+ -[VCAggregatorMultiway transferSegmentStateToNewUplinkSegment:fromPreviousUplinkSegment:]
+ -[VCAggregatorMultiway updateRTStatsOnCallAndSession:audioPacketsSent:]
+ GCC_except_table834
+ _OBJC_IVAR_$_StreamGroupStats._totalVideoFrameIncompleteNextTSRate
+ _objc_msgSend$setTotalVideoFrameIncompleteNextTSRate:
+ _objc_msgSend$totalVideoFrameIncompleteNextTSRate
+ _objc_msgSend$transferSegmentStateToNewUplinkSegment:fromPreviousUplinkSegment:
+ _objc_msgSend$updateRTStatsOnCallAndSession:audioPacketsSent:
- +[MultiwaySegment storeToReport:value:key:streamGroup:]
- -[VCAggregatorMultiway updateRTStatsOnCallAndSession:totalReceiveRate:audioPacketsSent:]
- GCC_except_table833
- __OBJC_$_CLASS_METHODS_MultiwaySegment
- _objc_msgSend$updateRTStatsOnCallAndSession:totalReceiveRate:audioPacketsSent:
CStrings:
+ "Td,V_totalVideoFrameIncompleteNextTSRate"
+ "_totalVideoFrameIncompleteNextTSRate"
+ "setTotalVideoFrameIncompleteNextTSRate:"
+ "totalVideoFrameIncompleteNextTSRate"
+ "transferSegmentStateToNewUplinkSegment:fromPreviousUplinkSegment:"
+ "updateRTStatsOnCallAndSession:audioPacketsSent:"
- "updateRTStatsOnCallAndSession:totalReceiveRate:audioPacketsSent:"
- "v32@0:8@16I24I28"

```
