## adc-rheia-d9x.im4p

> `adc-rheia-d9x.im4p`

```diff

 
-  __TEXT.__text: 0x833634
-  __TEXT.__const: 0x9b5960
+  __TEXT.__text: 0x8368d0
+  __TEXT.__const: 0x9b59a8
   __TEXT.text_env: 0x4fda4
   __TEXT._rtk_mtab: 0x2b8
-  __TEXT.__cstring: 0xa33f9
+  __TEXT.__cstring: 0xa370a
   __TEXT.__data_copy: 0x200000
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.__eh_frame: 0x944
-  __DATA.__const: 0x51d68
+  __DATA.__const: 0x51d90
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xe2a30
   __DATA._rtk_power: 0x3a8

   __DATA.__zerofill: 0x5bf620
   Functions: 0
   Symbols:   0
-  CStrings:  17895
+  CStrings:  17906
 
CStrings:
+ "%s: AXIError: W BE2 (0x%x) # %d "
+ "(((size_t) pChInfo->pMSTFRefInScale0->DataPointer(0) + buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE0)]->BufferTileDataRegionOffsetGet(0)) & 0x1ff) == 0"
+ "(((size_t) pChInfo->pMSTFRefInScale1->DataPointer(0) + buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE1)]->BufferTileDataRegionOffsetGet(0)) & 0x1ff) == 0"
+ "(((size_t) pChInfo->pMSTFRefInScale1->DataPointer(1) + buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE1)]->BufferTileDataRegionOffsetGet(1)) & 0x1ff) == 0"
+ "02:46:45"
+ "CISP_CMD_APPLE_CH_MLVNR_NIGHTMODE_CONFIG_SET"
+ "CISP_CMD_APPLE_CH_MLVNR_TIMEWARP_CONFIG_SET"
+ "CRT: CPCEFlowManager.cpp:%d [DSI] Entering suspend mode (power = %d)\n"
+ "CRT: CPCEFlowManager.cpp:%d [DSI] PCE - Entering Secure Mode (power = %d)\n"
+ "CRT: CPCEFlowManager.cpp:%d [DSI] PCE - Exiting Secure Mode (power = %d)\n"
+ "Currently MLVNR is disabled on J714/J716, J700, J427/J527, will be enabled when MLVNR FW/AFPP support ready"
+ "ISP_PROPERTY_ALGOCONTROL_MLVNR_CAPTURE_ENABLE can't work if platfrom doesn't support MLVNR"
+ "ISP_PROPERTY_ALGOCONTROL_MLVNR_CONTROL can't work if platfrom doesn't support MLVNR"
+ "ISP_PROPERTY_ALGOCONTROL_MLVNR_RPC_PROFILING_ENABLE can't work if platfrom doesn't support MLVNR"
+ "LCDRV [DEBUG] CH%d pAF is NULL while resuming\n"
+ "TransitionComplete"
+ "TransitionRequest"
+ "[%s] CH = 0x%zu MLVNR NightMode Config ctrl=%d,Thres Enter:Exit=%d:%d,RampDownFrames=%d\n"
+ "[%s] CH = 0x%zu MLVNR TimeWarp Config ctrl=%d,Thres Enter:Exit=%d:%d,RampDownFrames=%d\n"
+ "[%s] CH = 0x%zu Sif Pixel format %x, packType %x SifDMACompress %d SifDMACompanding %d %s\n"
+ "[DEBUG] %s L%d Ch%zu Current State = %d\n"
+ "[DEBUG] Ch%zu %s L%d State Req = %d -> %d\n"
+ "[DEBUG] Ch%zu %s L%d pAF is NULL\n"
+ "buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE0)]"
+ "buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE1)]"
+ "buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE2TO5)]"
+ "ch %d fc %d AEStatsUpdated == 0"
+ "chEntry->pool[FILTER_STILLFLOW][VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE0] != 0"
+ "chEntry->pool[FILTER_STILLFLOW][VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE1] != 0"
+ "chEntry->pool[FILTER_STILLFLOW][VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE2TO5] != 0"
+ "chEntry->pool[FILTER_VIDEOFLOW][VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE0] != 0"
+ "chEntry->pool[FILTER_VIDEOFLOW][VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE1] != 0"
+ "chEntry->pool[FILTER_VIDEOFLOW][VFLOWH17_BUFFER_POOL_PYROUTPROC1_SCALE2TO5] != 0"
- "(((size_t) pChInfo->pMSTFRefInScale0->DataPointer(0) + buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_TILEPROC_SCALE0)]->BufferTileDataRegionOffsetGet(0)) & 0x1ff) == 0"
- "(((size_t) pChInfo->pMSTFRefInScale1->DataPointer(0) + buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_TILEPROC_SCALE1)]->BufferTileDataRegionOffsetGet(0)) & 0x1ff) == 0"
- "(((size_t) pChInfo->pMSTFRefInScale1->DataPointer(1) + buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_TILEPROC_SCALE1)]->BufferTileDataRegionOffsetGet(1)) & 0x1ff) == 0"
- "23:28:24"
- "CRT: CPCEFlowManager.cpp:%d [DSI] Entering suspend mode\n"
- "CRT: CPCEFlowManager.cpp:%d [DSI] PCE - Entering Secure Mode\n"
- "CRT: CPCEFlowManager.cpp:%d [DSI] PCE - Exiting Secure Mode\n"
- "ISP_PROPERTY_ALGOCONTROL_RAW_MLVNR_CONTROL can't work if platfrom doesn't support RAW MLVNR"
- "LCDRV %s L%d Ch%d pAF is NULL after resume\n"
- "MLVNR is disabled in H17."
- "Resume"
- "[%d] ch=%d frame=%d, No MLAF buffer available"
- "[%s] CH = 0x%zu   Sif Pixel Format%x, type %x DmaCompress %d Companding %d %s\n"
- "buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_TILEPROC_SCALE0)]"
- "buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_TILEPROC_SCALE1)]"
- "buffPool[BufferPoolPin(pChInfo->chId, FLOWBASE_OUTPUT_PORT_0, VFLOWH17_BUFFER_POOL_TILEPROC_SCALE2TO5)]"
- "chEntry->pool[FILTER_STILLFLOW][VFLOWH17_BUFFER_POOL_TILEPROC_SCALE0] != 0"
- "chEntry->pool[FILTER_STILLFLOW][VFLOWH17_BUFFER_POOL_TILEPROC_SCALE1] != 0"
- "chEntry->pool[FILTER_STILLFLOW][VFLOWH17_BUFFER_POOL_TILEPROC_SCALE2TO5] != 0"
- "chEntry->pool[FILTER_VIDEOFLOW][VFLOWH17_BUFFER_POOL_TILEPROC_SCALE0] != 0"
- "chEntry->pool[FILTER_VIDEOFLOW][VFLOWH17_BUFFER_POOL_TILEPROC_SCALE1] != 0"
- "chEntry->pool[FILTER_VIDEOFLOW][VFLOWH17_BUFFER_POOL_TILEPROC_SCALE2TO5] != 0"

```
