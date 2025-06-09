## GKSPerformance

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/GKSPerformance.framework/GKSPerformance`

```diff

-2115.6.1.0.0
-  __TEXT.__text: 0xade8
+2145.45.1.11.2
+  __TEXT.__text: 0xae7c
   __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x89c
+  __TEXT.__objc_methlist: 0x8a4
   __TEXT.__const: 0x380
-  __TEXT.__cstring: 0x2e48
+  __TEXT.__cstring: 0x2e4a
   __TEXT.__oslogstring: 0x3ff
   __TEXT.__unwind_info: 0x260
   __TEXT.__objc_classname: 0x60
-  __TEXT.__objc_methname: 0x239e
+  __TEXT.__objc_methname: 0x23d5
   __TEXT.__objc_methtype: 0x2fe
-  __TEXT.__objc_stubs: 0x20c0
-  __DATA_CONST.__got: 0x90
+  __TEXT.__objc_stubs: 0x20e0
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8f0
+  __DATA_CONST.__objc_selrefs: 0x900
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0xfe0
   __AUTH_CONST.__auth_got: 0x190

   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x2a0
-  __AUTH.__objc_data: 0x190
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x244
   __DATA.__data: 0x320
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA.__bss: 0x18
+  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: E8AA529B-82F9-3D9F-8C7E-6FC6ACA6007E
-  Functions: 204
-  Symbols:   963
-  CStrings:  1498
+  UUID: 34A80D73-F468-3D2A-9F19-F7706E5FF509
+  Functions: 205
+  Symbols:   965
+  CStrings:  1500
 
Symbols:
+ -[AWDAdaptor sendMessageWithMethodPrivate:respCode:dict:]
+ _objc_msgSend$copy
+ _objc_msgSend$dictionary
- _OBJC_CLASS_$_NSNull
- _objc_msgSend$null
Functions:
~ -[AWDStats generateAggregatedCallStats:] : 2552 -> 2576
~ -[AWDAdaptor dealloc] : 436 -> 484
~ -[AWDAdaptor sendMessageWithMethod:respCode:dict:] : 1668 -> 4
+ -[AWDAdaptor sendMessageWithMethodPrivate:respCode:dict:]
~ -[AWDAdaptor wifiCallingAddSamples:] : 988 -> 1064
~ -[AWDAdaptor sendAnalyticsDetailedVoiceCallEvent] : 1640 -> 1548
~ -[AWDAdaptor wifiCallingAddSamplesGenerateAndSendCallEndReport:] : 1376 -> 1380
~ -[AWDAdaptor sendAnalyticsAudioFrameCountStatisticsEvent:] : 1144 -> 1228
CStrings:
+ "StreamConnectionTime"
+ "copy"
+ "dictionary"
+ "sendMessageWithMethodPrivate:respCode:dict:"
- "CallConnectionTime"
- "null"

```
