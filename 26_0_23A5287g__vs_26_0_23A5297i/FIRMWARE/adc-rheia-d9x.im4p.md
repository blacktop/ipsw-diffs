## adc-rheia-d9x.im4p

> `adc-rheia-d9x.im4p`

```diff

 
-  __TEXT.__text: 0xab58d4
-  __TEXT.__const: 0x9b4820
+  __TEXT.__text: 0xaba4a0
+  __TEXT.__const: 0x9b4a28
   __TEXT.text_env: 0x4f1a4
-  __TEXT.__cstring: 0xa4d7b
+  __TEXT.__cstring: 0xa5b0d
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__eh_frame: 0xcbc
-  __DATA.__const: 0x54ce0
+  __DATA.__const: 0x54b78
   __DATA._rtk_heap: 0x1000
-  __DATA.__data: 0xe2bf8
+  __DATA.__data: 0xe2c00
   __DATA._rtk_power: 0x3f8
   __DATA._rtk_patchbay: 0x241
   __DATA._rtk_init_stack: 0x2000

   __DATA.__chain_starts: 0x2c
   __DATA.__mod_init_func: 0x0
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x5ba400
-  UUID: 57FFB971-7934-3FAF-8286-BD363D304E5C
-  Functions: 9160
+  __DATA.__zerofill: 0x5b2400
+  UUID: A0F9D3F6-4834-3D7A-AD58-5253F54BA310
+  Functions: 9167
   Symbols:   0
-  CStrings:  18082
+  CStrings:  18154
 
CStrings:
+ "                   x: Enable prints \n"
+ "      X:                               %f, %f, %f\n"
+ "      Y:                               %f, %f, %f\n"
+ "    OIS Stroke Based DVC\n"
+ " [%d] [x] [-] [-]: Enable/Disable Debug Prints \n"
+ "%"
+ "%4d (%d,%d)%s"
+ "%s  (too close) useCandidateCh %d \n"
+ "%s  Focus override useCandidateCh %d \n"
+ "%s  SFocus override useCandidateCh %d \n"
+ "%s  SFocus override useCandidateCh %d (dist %.1f vs %.1f)\n"
+ "%s  decide based on single cam %d (ref %d)\n"
+ "%s  useCandidateCh %d (fm %d) \n"
+ "%s  useCandidateCh2 %d (fm %d) \n"
+ "%s F preview %d chRecommended %d\n"
+ "%s HFLCK Lock (densification) [%d,%d,%d] d%.1f vs %.1f\n"
+ "%s Limits %d MFD %.1f FD %.1f %.1f D %.1f %.1f FP %.1f %.1f %.1f dc %.1f\n"
+ "%s N2 chPreviewMaster %d chPreviewStarted? %d (prevValid %d prevCh %d started %d) \n"
+ "%s Schecked %d focus %d pf %d pos%.1f d%.1f, fd%.1f\n"
+ "%s Schecked2 %d focus %d pf %d pos%.1f d%.1f, fd%.1f \n"
+ "%s autoswitch reset\n"
+ "%s autoswitch tear down\n"
+ "%s ch %d SwitchDepthAvg %.2f (%d)\n"
+ "%s ch %d previewNotReady F %d \n"
+ "%s ch %d: Unable to retain APE convergence \n"
+ "%s ch %d: camswitch defocus %.1f um %.1f tgtdac %.1f tgt %d \n"
+ "%s ch %d: defocus(%d): %.1f active:%d targetPos:%d %.1f(dist %.1f, %.1f) hyperfocal %d depth %d %d\n"
+ "%s ch %d: reset depth\n"
+ "%s ch %d: resetting depth:  %f --> %d [%d, %d](conf %.1f)\n"
+ "%s ch %d: sending depth:  %f --> %d [%d, %d](conf %.1f)\n"
+ "%s ch %llu:  enableDepthComputeTiles = %d \n"
+ "%s ch %llu:  invalid selection \n"
+ "%s ch%d focus %d (prevfocus %d) pos %.1f depth %.1f fd %.1f %d chOk[%d] HFLK %d\n"
+ "%s ch%d pos[%.1f, %.1f] dist[%.1f, %.1f] %.1f -> %.1f \n"
+ "%s chSrc %zu chPreviewMaster %d prevRec %d\n"
+ "%s checked %d vs %d focus %d,%d pf %d,%d pos%.1f,%.1f d%.1f,%.1f, fd%.1f,%.1f %d\n"
+ "%s checked2 %d vs %d focus %d,%d pf %d,%d pos%.1f,%.1f d%.1f,%.1f, fd%.1f,%.1f %d\n"
+ "%s invalid channel number \n"
+ "%s preview %d not good, changing chRecommended %d\n"
+ "%s settings final chRecommended %d (prev Valid %d) \n"
+ "%s using previous recommended %d (vs %d) \n"
+ "%s: %s EX depth %.2f, std %.2f, conf %.2f #%d/%d (%d)\n"
+ "%s: %s depth %.2f, std %.2f, conf %.2f #%d/%d (%d)\n"
+ "%s: EP %u out of send buffers\n"
+ "%s: ch%d: timeMsec %.2f, deltaC %d minD %d maxD %d defocR %d \n"
+ "%s: ch%d: timeMsecFloat %.2f, deltaC %d minD %d maxD %d defocR %d \n"
+ "%s: hiResWinID: %d tileInd: %d, PF_Cnt=0!"
+ ".DepthSpots  = %3d\n"
+ ".DepthSpotsX = %3d\n"
+ ".TotSpots    = %3d\n"
+ "22:22:37"
+ "8adf6d2"
+ "AETable_Photo_Digital_Flash_Qsub_Wide"
+ "AETable_Photo_Digital_Flash_Wide"
+ "AFDBG CH[%zu]: validTofSignal=[%d] obstructedProjector=[%d] specularSurface=[%d]\n"
+ "APE(ExStats): ch%d: apeRetentionLostDueToDropFeature: %d \n"
+ "APERetentionCheck"
+ "CH:%zu Setting the Clock Master in AE to %u\n"
+ "CH[%1d]S[%s] F[%1d][%1d]%3d [%2d] D[%5d][%5d] P[%5d]%2d PFPS[%2d] APE[%s] [T %2d] [MFD %3d]%1d %2d"
+ "CRNT[T %2d] [CR %2d] D[%5d] PFL[%3d.%02d] Z[%3d] PFLErr[%4d,%3d.%02d] DFPS[%3d] Lux[%s]"
+ "Crop Update=%d %d, ch=%zu, singlePipelineOnly=%d, InitialZoom=%d, singleppl=%d\n"
+ "Crop Update=%d %d, ch=%zu, singlePipelineOnly=%d, singleppl=%d\n"
+ "DBG2 (%s%s%s%s) [%d%d%d%d  %d%d%d%d%d]   [%d%d%d_ %d%d_%d %d%d%d%d]  (%4d,%4d / %4d) FM:(%2d,%d)"
+ "DEPTH IN TILE: ch %d \n"
+ "DEPTH [%s][%s][%s][%s][%s][%s][%s] [%s][%s][%s] [%s][%s][%s][%s] %d %d %d"
+ "DepthProcSpotDepth2LC"
+ "EBD might be corrupted, ch:%zu fc:%d SFc:%d lSFc:%d %d\n"
+ "Enable prints:  %d \n"
+ "F-TILES:  (%3d,%3d),(%3d,%3d)  #:(%3d,%3d)  (%3d / %3d)  (Med,sig): (%3d,%3d)"
+ "LCDRV Range lin (um): [%.2f, %.2f], dyn (um): [%.2f, %.2f]\n"
+ "LCMOT: ACCEL_VALID flag not set? No acceleration data populated\n"
+ "LCMOT: Detected unexpected acceleration data: %f %f %f\n"
+ "LCMOT: Detected unexpected unfilteredAcceleration data: %f %f %f\n"
+ "LCMOT: UNFILTERED_ACCEL_VALID flag not set? No unfiltered acceleration data populated\n"
+ "LENSC: First real motion data received! #%llu: %llums\n"
+ "MOT[%s][%s][%s][%s] SHFT: %4d  TTC %8d  Dep:(%4d,%4d)  DepX%d:(%4d,%4d) DRng:[%4d]"
+ "No valid RV, skip EBD processing, ch:%zu fc:%d\n"
+ "O"
+ "PRE(ExStats): ch%d: apeRetentionLostDueToDropFeature: %d \n"
+ "RecommendPreviewChannel"
+ "ResetDepthMetaData"
+ "SendMessage"
+ "TM depth %zu replacement scheme %d not supported. change TM depth to 1"
+ "TM: Isp output[%u] change: prevFr w:%u h: %u, currFr w: %u h: %u tag:%u\n"
+ "TearDown"
+ "ch %02d:  blobAgeOK = %d, impactType = %d, event before blob = %d, threshOK = %d, duration OK = %d\n"
+ "ch %02d:  drop stats min = %.2f, max = %.2f\n"
+ "ch %d ROI SHIFT %.2f, ROI SWITCHING SHIFT %.2f, focal %.2f \n"
+ "ch %zu fc %d bSplitSIFRFrame %d != sifrSkipRatio %d"
+ "ch %zu set gA 0x%x skipratio %d curr %d fc %d\n"
+ "ch %zu:  FULL [%d, %d] WH[%d, %d] = %4.2f std %.2f (%d) (%d/%d)\n"
+ "ch %zu:  [%d, %d] WH[%d, %d] = %4.2f std %.2f flag (%d) (%d/%d)\n"
+ "max flood current lowered to %d uA\n"
- "%s ch %d: APE converged recently (delta %llu) %d\n"
- "%s ch %d: Unable to bootstrap APE convergence flags (delta-T %llu >= %d) : curr APSmode=%d\n"
- "%s ch %d: defocus(%d): %.1f active:%d targetPos:%d (dist %.1f, %.1f) hyperfocal %d depth %d\n"
- "%s: %s EX depth %.2f, std %.2f, conf %.2f #%d (%d)\n"
- "%s: %s depth %.2f, std %.2f, conf %.2f #%d (%d)\n"
- "%s: ch%d: timeMsec %d, deltaC %d minD %d maxD %d defocR %d \n"
- ".DepthRange  = %8.3f\n"
- ".Spots       = %d / %d\n"
- "01:53:08"
- "5e9e630"
- "AFDBG CH[%zu]: obstructedProjector=[%d]\n"
- "APEPersistentFlagLoad"
- "CH[%1d]S[%s] F[%1d][%1d]%3d [%2d] D[%5d][%5d] P[%5d]%2d PFPS[%2d] APE[%s] [T %2d] [MFD %3d]%1d"
- "CRNT[T %2d] [CR %2d] D[%5d] PFLsig[%5d] Z[%3d] PFL[%4d] DFPS[%3d] Lux[%s]"
- "DEPTH [%s][%s][%s][%s][%s][%s][%s] [%s][%s][%s] [%s][%s][%s][%s] %d %d"
- "MOT[%s][%s][%s][%s] SHFT: %4d  TTC %8d  [%d%d%d_ %d%d_%d %d%d%d%d]"
- "TM depth %zu replacement scheme %d, not supported combination, change TM depth to 1"
- "[%s] CH = 0x%zu   FD Input Set %s\n"
- "ch %d ROI SHIFT %.2f focal %.2f \n"
- "ch %hhu fc %d Sifr int %d isSifrFrame %d supported %d"
- "ch %zu set gA 0x%x skipratio %d curr %d\n"

```
