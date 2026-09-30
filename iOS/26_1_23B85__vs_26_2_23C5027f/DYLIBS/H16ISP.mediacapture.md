## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-4.109.0.0.0
-  __TEXT.__text: 0x1d3338
+4.207.2.0.0
+  __TEXT.__text: 0x1d3d48
   __TEXT.__auth_stubs: 0x3270
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__const: 0x2803f
-  __TEXT.__oslogstring: 0x1d871
-  __TEXT.__cstring: 0x1992c
-  __TEXT.__gcc_except_tab: 0x6ad4
-  __TEXT.__unwind_info: 0x3e90
+  __TEXT.__const: 0x2836f
+  __TEXT.__oslogstring: 0x1d88c
+  __TEXT.__cstring: 0x199e1
+  __TEXT.__gcc_except_tab: 0x6aec
+  __TEXT.__unwind_info: 0x3e98
   __TEXT.__eh_frame: 0xf0
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0x1d7a
   __TEXT.__objc_methtype: 0x10b3
   __TEXT.__objc_stubs: 0x20a0
-  __DATA_CONST.__got: 0x3508
-  __DATA_CONST.__const: 0xb648
+  __DATA_CONST.__got: 0x3510
+  __DATA_CONST.__const: 0xb8f8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x1948
   __AUTH_CONST.__const: 0x29d0
-  __AUTH_CONST.__cfstring: 0xa1e0
+  __AUTH_CONST.__cfstring: 0xa240
   __AUTH_CONST.__objc_const: 0x880
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x36b6e8
+  __DATA.__data: 0x3746e8
   __DATA.__bss: 0x119
   __DATA.__common: 0x64
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x138
+  __DATA_DIRTY.__data: 0x148
   __DATA_DIRTY.__bss: 0xa8c
   __DATA_DIRTY.__common: 0x57b8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D42B594F-40CC-36F3-A20F-97E9415FE811
-  Functions: 5800
-  Symbols:   14796
-  CStrings:  8027
+  UUID: 1D37293E-A878-36F3-8327-D045C7337EE0
+  Functions: 5809
+  Symbols:   14810
+  CStrings:  8043
 
Symbols:
+ GCC_except_table119
+ GCC_except_table127
+ GCC_except_table141
+ GCC_except_table145
+ __ZL32h16ispOutputPreset_VD56G8_Mirage
+ __ZN6H16ISP12H16ISPDevice24ISP_ExclavesSensorStatusEPy
+ __ZN6H16ISP12H16ISPDevice25SetExclaveAEBracketConfigEjP33sCIspExclaveSensorAEBracketConfig
+ __ZN6H16ISP19H16ISPFrameReceiver21isSensorAccessAllowedEv
+ __ZN6H16ISP19H16ISPFrameReceiver21isSensorAccessAllowedEv.cold.1
+ __ZN6H16ISP34H16ISPGraphExclaveAutoExposureNode5runAEEjb
+ __ZN6H16ISP34H16ISPGraphExclaveAutoExposureNode5runAEEjb.cold.1
+ __ZN6H16ISP34H16ISPGraphExclaveAutoExposureNode5runAEEjb.cold.2
+ __ZN6H16ISP34H16ISPMetadataDictCreatorGraphNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE.cold.2
+ __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode17AddFaceIDMetadataEPNS_24H16ISPFilterGraphMessageERK13AttentionInfoRK20UserEngagementStatusjbP9FrameInfo
+ __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode29AddAttentionDetectionMetadataEPNS_24H16ISPFilterGraphMessageERK13AttentionInfoRK20UserEngagementStatusyb
+ __ZN6H16ISPL24IMX923_setfile_8825_01XXE
+ __ZNK6H16ISP12H16ISPDevice17enabledExclaveFIDEv
+ ___block_descriptor_tmp.15
+ _kFigCaptureStreamMetadataOutputKey_FaceIndex
+ _kFigCaptureStreamMetadata_SensorAccess
- GCC_except_table101
- GCC_except_table118
- GCC_except_table126
- GCC_except_table140
- GCC_except_table144
- GCC_except_table158
- __ZL18SetSIFRControlModePKvP19H16ISPCaptureStreamP18H16ISPCaptureGroupP19H16ISPCaptureDevice.cold.3
- __ZN6H16ISP34H16ISPGraphExclaveAutoExposureNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE.cold.1
- __ZN6H16ISP34H16ISPGraphExclaveAutoExposureNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE.cold.2
- __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode17AddFaceIDMetadataEPNS_24H16ISPFilterGraphMessageEP28ISPExclaveCoreChRunKitADRsltb
- __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode29AddAttentionDetectionMetadataEPNS_24H16ISPFilterGraphMessageEP28ISPExclaveCoreChRunKitADRsltyb
- _kCVImageBufferLogTransferFunction_AppleLog2
CStrings:
+ "%s - Failed to attach intrinsic matrices because pMetaDataInput is NULL\n"
+ "%s - Failed to get sensor status return status is %0x\n"
+ "%s - Failed to get sensor status; return =%0x\n"
+ "%s - ISP_EXCLAVEKIT_CMD_CH_ON is failure Err:%d ch:%u\n"
+ "%s - Sensor access was not allowed, so retriggered the timer\n"
+ "%s - Skipping GMC\n"
+ "%s - channel %d meta output:%s exclave FD:%s AD:%s ER:%s FT:%s PreCheck:%s FID:%s PO:%s FDOD:%s MD:%s DPD:%s BaselineStreaming:%s LSE:%s\n"
+ "/usr/local/share/firmware/isp/8825_01XX.dat"
+ "/var/mobile/Media/DCIM/%s-GMC-"
+ "Debug AE results: reqID %llu aeCounter %llu exp %d ET %d Sensor AG %d Sensor DG %d ISP DG %d resultstatus=%d\n"
+ "DumpGmc"
+ "EK AE RunKit CamChan %d, requestID=0x%08X\n"
+ "EK AE RunKit Failed for reqID 0x%08X resultStatus %d\n"
+ "EK RunKit AE skipped for reqID 0x%08X\n"
+ "EnableExclaveFID"
+ "GenerateAndAttachCoreMediaMetaDataDictionary"
+ "In concurrent mode, skip apply AE Settings to FW\n"
+ "SkipGmc"
+ "isSensorAccessAllowed"
+ "runAE"
- "%s - ISP_EXCLAVEKIT_CMD_CH_ON is failure Err: %d\n"
- "%s - channel %d meta output:%s exclave FD:%s AD:%s ER:%s FT:%s PreCheck:%s FDOD:%s PO:%s MD:%s DPD:%s BaselineStreaming:%s LSE:%s\n"
- "[Exclaves]: H16ISPGraphAutoExposureNode::%s Debug AE results: reqID %llu aeCounter %llu exp %d ET %d Sensor AG %d Sensor DG %d ISP DG %d resultstatus=%d\n"
- "[Exclaves]: H16ISPGraphAutoExposureNode::%s In concurrent mode, skip apply AE Settings to FW\n"
- "[Exclaves]: H16ISPGraphExclaveAutoExposureNode::%s EK AE RunKit CamChan %d, requestID=0x%08X\n"
- "[Exclaves]: H16ISPGraphExclaveAutoExposureNode::%s EK AE RunKit Failed for reqID 0x%08X resultStatus %d\n"
- "[Exclaves]: H16ISPGraphExclaveAutoExposureNode::%s EK RunKit AE skipped for reqID 0x%08X\n"

```
