## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-900.0.0.0.0
-  __TEXT.__text: 0x129484
+901.0.0.0.0
+  __TEXT.__text: 0x1296a0
   __TEXT.__auth_stubs: 0xe90
   __TEXT.__const: 0xbe5f
   __TEXT.__gcc_except_tab: 0x7a4
-  __TEXT.__oslogstring: 0xff4c
-  __TEXT.__cstring: 0x5a6f
+  __TEXT.__oslogstring: 0x1003e
+  __TEXT.__cstring: 0x5a83
   __TEXT.__unwind_info: 0x16f0
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: D4723156-5C5D-3471-8C47-D04ED09EF05F
+  UUID: 47E81B63-84C7-3BF6-A343-FA7F7380434A
   Functions: 1982
   Symbols:   4876
-  CStrings:  1978
+  CStrings:  1983
 
Symbols:
+ __ZN10CPBManager22waitForCPBsOutstandingEj
- __ZN10CPBManager22waitForCPBsOutstandingEjy
Functions:
~ _CreateAVDHEVCInstance : 2936 -> 2940
~ _AppleAVDInitializeDecoder : 1120 -> 1128
~ __ZN10CPBManager11allocOneCPBEjmRjPhPbPS1_ : 1772 -> 1844
~ _AppleAVDDecodeFrame : 5408 -> 5404
~ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut : 4556 -> 4548
~ __ZN10CPBManagerC2EP22_sAppleAVDVideoContext : 108 -> 424
~ _CreateAVDFghrnInstance : 2168 -> 2172
~ __ZN22AppleAVDCommandBuilder15waitNumInFlightEj : 16 -> 12
~ _AppleAVDTerminateDecoder : 504 -> 500
~ __ZN10CPBManagerD2Ev : 540 -> 676
~ __ZN10CPBManager22waitForCPBsOutstandingEjy -> __ZN10CPBManager22waitForCPBsOutstandingEj : 636 -> 656
CStrings:
+ "23:39:59"
+ "23:40:00"
+ "AppleAVD: ERROR: %s(): Timed out, waited at least %llums! m_num_CPBs_on_the_fly=%u timeoutMS=%llu"
+ "AppleAVD: INFO: %s(): %s - CPBManager created! cacheSize: %d - timeLimit: %llums\n"
+ "AppleAVD: INFO: %s(): longest wait: %llums (100ms intervals)\n"
+ "CPBManager"
+ "Jul 14 2025"
+ "internal"
- "22:34:56"
- "22:34:57"
- "Jun 30 2025"

```
