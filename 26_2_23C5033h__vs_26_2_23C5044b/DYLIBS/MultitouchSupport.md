## MultitouchSupport

> `/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport`

```diff

-9110.1.0.0.0
-  __TEXT.__text: 0x1e330
+9120.4.0.0.0
+  __TEXT.__text: 0x1e554
   __TEXT.__auth_stubs: 0xe70
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0x2008

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B93155EF-F56D-3B97-A1B8-D828338503F5
+  UUID: DD252348-EC69-373E-829D-E05A77E95859
   Functions: 664
   Symbols:   1422
   CStrings:  617
Functions:
~ _mt_ProcessMultitouchFrame : 3444 -> 3448
~ _mt_Scale8BitBufferTo16BitRange : 52 -> 60
~ _mt_ExpandImageAndForward : 260 -> 268
~ _mtalg_ProcessImageFrame : 204 -> 224
~ __Z32MTParse_CompactBinaryFrameHeaderPhiP28MTParsedMultitouchFrameRep_tP10__MTDevice : 160 -> 164
~ _MTParse_CompactBinaryPath : 584 -> 700
~ _MTParse_CompactV3orV5BinaryPath : 412 -> 428
~ _MTParse_CompactV4BinaryPath : 364 -> 384
~ _MTParse_CompactV7BinaryPath : 380 -> 404
~ _MTParse_CompactV9BinaryPath : 268 -> 284
~ _MTParse_CompactV10BinaryPath : 368 -> 380
~ __Z27MTParse_V3BinaryFrameHeaderPhiP28MTParsedMultitouchFrameRep_tP10__MTDevice : 424 -> 456
~ _MTParse_V3BinaryPathOrImage : 716 -> 752
~ __Z27MTParse_V4BinaryFrameHeaderPhiP28MTParsedMultitouchFrameRep_tP10__MTDevice : 520 -> 540
~ __Z27MTParse_V4BinaryPathPayloadPhiP28MTParsedMultitouchFrameRep_tP10__MTDeviceitt : 636 -> 648
~ __Z29MTParse_GenerateRingCentroidsP28MTParsedMultitouchFrameRep_tP10__MTDevice : 188 -> 180
~ _MTParse_V4PrecisePathAndImage : 488 -> 504
~ _MTParse_HostPathAndImage : 380 -> 388
~ __Z25MTParse_SensorImageHeaderPhiP28MTParsedMultitouchFrameRep_tP10__MTDevice : 460 -> 476
~ __Z25MTParse_BinaryFrameHeaderPhiP28MTParsedMultitouchFrameRep_tP10__MTDevice : 508 -> 520
~ _MTParse_BinaryPathOrImage : 700 -> 708
~ _MTParse_ExternalMessage : 72 -> 92
~ _MTProcess_0xC5_Data : 356 -> 388
~ _MTProcess_0xCC_Data : 852 -> 876
~ _MTParseSensorRegionsReport : 248 -> 272
~ _mt_ForwardSpecificImageRegion : 380 -> 416
~ _mtp_ForwardDeviceImageSubRegions : 212 -> 220
~ _mtp_ForwardDeviceImageBuffer : 236 -> 240

```
