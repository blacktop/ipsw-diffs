## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-737.6.0.0.0
-  __TEXT.__text: 0xd6160
+740.5.0.0.0
+  __TEXT.__text: 0xdc588
   __TEXT.__auth_stubs: 0xe20
-  __TEXT.__gcc_except_tab: 0xa78
-  __TEXT.__const: 0xb926
-  __TEXT.__oslogstring: 0xcd3d
-  __TEXT.__cstring: 0x540b
-  __TEXT.__unwind_info: 0x1850
-  __TEXT.__eh_frame: 0x2a4
+  __TEXT.__gcc_except_tab: 0xab4
+  __TEXT.__oslogstring: 0xd10b
+  __TEXT.__cstring: 0x54d4
+  __TEXT.__const: 0xb956
+  __TEXT.__unwind_info: 0x1904
+  __TEXT.__eh_frame: 0x2b8
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__const: 0x858
+  __AUTH_CONST.__const: 0x710
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__auth_got: 0x718
   __DATA.__bss: 0x11
   __DATA.__common: 0x50
-  __DATA_DIRTY.__const: 0x2098
+  __DATA_DIRTY.__const: 0x23d0
   __DATA_DIRTY.__data: 0x70
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 0232C469-E8DB-3D64-ADA6-6F60B19B61E0
-  Functions: 1844
-  Symbols:   4297
-  CStrings:  1708
+  UUID: 42405E70-10C5-3E99-A71E-1804AF2CBCF7
+  Functions: 1894
+  Symbols:   4400
+  CStrings:  1734
 
Symbols:
+ GCC_except_table9
+ __ZN17CAVDMvHevcDecoder10GetCurrMsbEiiii
+ __ZN17CAVDMvHevcDecoder11flushMV_RLMEv
+ __ZN17CAVDMvHevcDecoder11initPictureEP26hevc_video_parameter_set_tP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP27hevc_slice_segment_header_tP15HevcPictureInfob
+ __ZN17CAVDMvHevcDecoder11insertFrameEP15HevcPictureInfo
+ __ZN17CAVDMvHevcDecoder11printAuListEv
+ __ZN17CAVDMvHevcDecoder11removeFrameEP17hevc_frame_params
+ __ZN17CAVDMvHevcDecoder12VAStopDecodeEv
+ __ZN17CAVDMvHevcDecoder12getHwDecoderEi
+ __ZN17CAVDMvHevcDecoder13DecodePictureEjjb
+ __ZN17CAVDMvHevcDecoder13VADecodeFrameEPhiiiiiP14avd_seq_params
+ __ZN17CAVDMvHevcDecoder13VAStartDecodeEPhi
+ __ZN17CAVDMvHevcDecoder14getFrameParamsEP17hevc_frame_params
+ __ZN17CAVDMvHevcDecoder14printCurrentAuEv
+ __ZN17CAVDMvHevcDecoder15getAuOutputFlagEi
+ __ZN17CAVDMvHevcDecoder15getCollocMVInfoEi
+ __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo
+ __ZN17CAVDMvHevcDecoder16getSliceRefIDmapE20hevc_ref_list_type_ti
+ __ZN17CAVDMvHevcDecoder17isAuBumpingNeededEv
+ __ZN17CAVDMvHevcDecoder18getDispFrameParamsEP17hevc_frame_params
+ __ZN17CAVDMvHevcDecoder18getRefTileHdrsInfoEv
+ __ZN17CAVDMvHevcDecoder19calcSmallestLayerIdEi
+ __ZN17CAVDMvHevcDecoder19mvhevcOutputBumpingEP22hevc_nal_unit_header_tP29hevc_sequence_parameter_set_tP27hevc_slice_segment_header_tP15HevcPictureInfo
+ __ZN17CAVDMvHevcDecoder20InitMultiViewDpbInfoEv
+ __ZN17CAVDMvHevcDecoder20getAuRemainingLayersEi
+ __ZN17CAVDMvHevcDecoder21handlePOCResetPictureEP27hevc_slice_segment_header_t
+ __ZN17CAVDMvHevcDecoder21removeAccessUnitEntryEi
+ __ZN17CAVDMvHevcDecoder22derivePocResetPeriodIdEP27hevc_slice_segment_header_t
+ __ZN17CAVDMvHevcDecoder22insertCurPicIntoAuListEP15HevcPictureInfo
+ __ZN17CAVDMvHevcDecoder22populateSnapshotStructEii
+ __ZN17CAVDMvHevcDecoder24AccessUnitBumpingProcessEv
+ __ZN17CAVDMvHevcDecoder24getNumAusMarkedforOutputEv
+ __ZN17CAVDMvHevcDecoder25checkRefLayersInitializedEi
+ __ZN17CAVDMvHevcDecoder25getInterLayerShortTermPicEii
+ __ZN17CAVDMvHevcDecoder26checkNewPocResettingPeriodEP22hevc_nal_unit_header_tP27hevc_slice_segment_header_t
+ __ZN17CAVDMvHevcDecoder27allocateMultiViewHwDecodersEi
+ __ZN17CAVDMvHevcDecoder27isAuBumpingNeededForNonIRAPEi
+ __ZN17CAVDMvHevcDecoder28deriveSpsParamsFromActiveVpsEP29hevc_sequence_parameter_set_ti
+ __ZN17CAVDMvHevcDecoder28initOutputDecodeLayerSetInfoEv
+ __ZN17CAVDMvHevcDecoder30deriveMvHevcOutputControlFlagsEP22hevc_nal_unit_header_tP27hevc_slice_segment_header_tP15HevcPictureInfob
+ __ZN17CAVDMvHevcDecoder31decrementPocValuesInLayerSubDPBEii
+ __ZN17CAVDMvHevcDecoder32decodeMultiViewPictureOrderCountEP29hevc_sequence_parameter_set_t
+ __ZN17CAVDMvHevcDecoder34releaseUnusedPicturesFromOneSubDpbEi
+ __ZN17CAVDMvHevcDecoder35releaseUnusedPicturesFromAllSubDpbsEv
+ __ZN17CAVDMvHevcDecoder9createDPBEP29hevc_sequence_parameter_set_tP15HevcPictureInfoi
+ __ZN17CAVDMvHevcDecoderC1EPvjb
+ __ZN17CAVDMvHevcDecoderC2EPvjb
+ __ZN17CAVDMvHevcDecoderD0Ev
+ __ZN17CAVDMvHevcDecoderD1Ev
+ __ZN17CAVDMvHevcDecoderD2Ev
+ __ZTI17CAVDMvHevcDecoder
+ __ZTS17CAVDMvHevcDecoder
+ __ZTV17CAVDMvHevcDecoder
CStrings:
+ "20:42:57"
+ "20:42:58"
+ "AppleAVD: %s -- DPB is full auIndex %d"
+ "AppleAVD: %s -- DPB is full numAus %d auIndex %d"
+ "AppleAVD: %s -- emptyLayer out of range"
+ "AppleAVD: %s -- m_numActiveAccessUnits out of range %d"
+ "AppleAVD: %s MultiView client %d"
+ "AppleAVD: %s invalid VPS id!"
+ "AppleAVD: %s layer id not found in vps_layer_id_in_nuh"
+ "AppleAVD: %s layerActive mem alloc fialed"
+ "AppleAVD: %s m_auList mem alloc fialed "
+ "AppleAVD: %s m_curAu layerActive alloc fialed"
+ "AppleAVD: %s nuh_layer_id > max layer ! %d %d"
+ "AppleAVD: %s() tile[%d] width %d, need at least two CTU wide"
+ "AppleAVD: %s(): WARNING, frame insertion is aborted because pic=NULL\n"
+ "AppleAVD: %s(): fail to activate parameter set for slice"
+ "AppleAVD: %s(): insertCurPicIntoAuList fail"
+ "AppleAVD: AVC_Decoder::ParseHeader unsupported naluLengthSize "
+ "AppleAVD: CAVDMvHevcDecoder: Not supported!"
+ "AppleAVD: CAVDMvHevcDecoder: error allocating decodeBuffer or m_pAHwDecoder is NULL!"
+ "AppleAVD: CAVDMvHevcDecoder: error data members!"
+ "AppleAVD: ERROR: %s(): m_highestTid > vps_max_sub_layers_minus1\n"
+ "AppleAVD: ERROR: %s(): slice count for frame is 0"
+ "AppleAVD: ERROR: [CAVDMvHevcDecErr] %s"
+ "AppleAVD: getHwDecoder error in %s"
+ "Feb 21 2024"
+ "InitMultiViewDpbInfo"
+ "createDPB"
+ "handlePOCResetPicture"
+ "insertCurPicIntoAuList"
+ "mvhevcOutputBumping"
+ "virtual int CAVDMvHevcDecoder::VADecodeFrame(unsigned char *, int, int, int, int, int, avd_seq_params *)"
- "18:11:36"
- "18:11:37"
- "AppleAVD: ## fno:%8d isIntra = %d (skip2IDR)"
- "AppleAVD: %s(): Allocating new AppleAVDCommandBuilder\n"
- "AppleAVD: %s(): Allocating new AppleAVDCommandBuilder failed\n"
- "Dec 20 2023"

```
