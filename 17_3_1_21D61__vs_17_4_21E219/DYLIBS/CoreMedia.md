## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`

```diff

-3095.4.2.0.0
-  __TEXT.__text: 0x13aa00
-  __TEXT.__auth_stubs: 0x2fe0
+3100.20.2.1.6
+  __TEXT.__text: 0x13c4f4
+  __TEXT.__auth_stubs: 0x3090
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x1618
-  __TEXT.__cstring: 0x18856
-  __TEXT.__oslogstring: 0x39eb
+  __TEXT.__cstring: 0x18efa
+  __TEXT.__oslogstring: 0x39f1
   __TEXT.__gcc_except_tab: 0xdc
   __TEXT.__dlopen_cstrs: 0x143
-  __TEXT.__unwind_info: 0x39d4
+  __TEXT.__unwind_info: 0x39e8
   __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methname: 0x5ed
   __TEXT.__objc_methtype: 0xc0
   __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x86d0
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__const: 0x88d0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x110
   __DATA_CONST.__objc_selrefs: 0x220
-  __AUTH_CONST.__const: 0x4180
-  __AUTH_CONST.__cfstring: 0x13980
-  __AUTH_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__const: 0x41b0
+  __AUTH_CONST.__cfstring: 0x13ac0
+  __AUTH_CONST.__auth_ptr: 0x40
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x1800
+  __AUTH_CONST.__auth_got: 0x1858
   __AUTH.__data: 0x1d0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x78
-  __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0xe41
+  __DATA.__data: 0xe19
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x2a38
+  __DATA.__bss: 0x2108
   __DATA.__common: 0x1c0
-  __DATA_DIRTY.__data: 0x274
+  __DATA_DIRTY.__data: 0x2a4
   __DATA_DIRTY.__common: 0xa8
-  __DATA_DIRTY.__bss: 0xd08
+  __DATA_DIRTY.__bss: 0x1678
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5083
-  Symbols:   12228
-  CStrings:  4372
+  Functions: 5100
+  Symbols:   12282
+  CStrings:  4436
 
Symbols:
+ _CC_SHA1
+ _CFBundleCopyExecutableURL
+ _CFBundleGetMainBundle
+ _EstablishOutmostContainerURLOfMainBundle
+ _FigCFDictionaryGetArrayValue
+ _FigCFDictionaryGetBooleanValue
+ _FigCFDictionaryGetDataValue
+ _FigCFDictionaryGetDictionaryValue
+ _FigCFDictionaryGetNumberValue
+ _FigCFDictionaryGetStringValue
+ _FigCFDictionaryGetURLValue
+ _FigIsSecTaskGPUExtensionOfBrowserEngine
+ _FigSecCopyOutmostBundleSignedWithSameCertificateAsCodeAtURL
+ _FigSecCopyOutmostBundleSignedWithSameCertificateAsCodeOfMainBundle
+ _SecCertificateCopyData
+ _SecCertificateGetTypeID
+ _SecCodeCopyPath
+ _SecCodeCopySigningInformation
+ _SecRequirementCreateWithStringAndErrors
+ _SecStaticCodeCheckValidityWithErrors
+ _SecStaticCodeCreateWithPath
+ _SecTaskCopyValueForEntitlement
+ ___loadBrowserEngineFramework_block_invoke
+ _hevcBridgeParseColourMappingOctants
+ _hevcbridgeGetSPSChromaFormatAndBitDepthsCallbackFlag
+ _hevcbridgeMoreRBSPData
+ _hevcbridgeParsePictureParameterSetMultilayerExtension
+ _hevcbridgeParsePictureParameterSetSCCExtension
+ _kFigBufferedAirPlayClientRoutingRegistryNotification_RunningClientsChanged
+ _kFigByteStreamProperty_AvoidSerializationWithOtherByteStreams
+ _kFigEndpointPlaybackSessionProxiedProperty_LoadedTimeRanges
+ _kFigEndpointProperty_StartSessionWithHostRequestIdentifier
+ _kFigEndpointRemoteControlSessionCreationOption_ClientTypeUUID
+ _kFigEndpointRemoteControlSessionCreationOption_QualityOfService
+ _kFigEndpointRemoteControlSessionCreationOption_SendMessageAsIs
+ _kFigEndpointRemoteControlSessionCreationOption_SendMessageWithoutReply
+ _kFigEndpointRemoteControlSessionCreationOption_SessionType
+ _kFigEndpointRemoteControlSessionCreationOption_StreamPriority
+ _kFigEndpointSendCommand_CommandType_SetMRInfo
+ _kFigEndpointSendCommand_Param_MRInfo
+ _kFigFormatDescriptionExtension_TransportStreamEncryptionInitData
+ _kSecCodeInfoCertificates
+ _sEstablishOutmostContainerURLOfMainBundleOnce
+ _sLoadBrowserFrameworkOnce
+ _sOutmostContainerURLOfMainBundle
+ _sOutmostContainerURLOfMainBundleEstablishmentResult
+ _s_SEBrowserEngineEntitlementGPU
- _kFigBufferedAirPlayClientRoutingRegistryNotification_CountOfRunningClientsChanged
CStrings:
+ "/System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore"
+ "<<<< FigCustomURLHandling >>>> %s: %{public}s.%p: requestID: %llu, error: %{private}@ (%d)"
+ "FBS_AvoidSerializationWithOtherByteStreams"
+ "RunningClientsChanged"
+ "StartSessionWithHostRequestIdentifier"
+ "TransportStreamEncryptionInitData"
+ "_BEBrowserEngineEntitlementRendering"
+ "certificate leaf = H\"%@\""
+ "chroma_bit_depth_cm_input_minus8"
+ "chroma_bit_depth_cm_output_minus8"
+ "chroma_bit_depth_entry_minus8"
+ "cm_adapt_threshold_u_delta"
+ "cm_adapt_threshold_v_delta"
+ "cm_delta_flc_bits_minus1"
+ "cm_octant_depth"
+ "cm_ref_layer_id"
+ "cm_res_quant_bits"
+ "cm_y_part_num_log2"
+ "coded_res_flag"
+ "colour_mapping_enabled_flag"
+ "inter_layer_pred_layer_idc"
+ "luma_bit_depth_cm_input_minus8"
+ "luma_bit_depth_cm_output_minus8"
+ "luma_bit_depth_entry_minus8"
+ "monochrome_palette_flag"
+ "mrInfo"
+ "num_cm_ref_layers_minus1"
+ "num_ref_loc_offsets"
+ "phase_hor_chroma_plus8"
+ "phase_hor_luma"
+ "phase_ver_chroma_plus8"
+ "phase_ver_luma"
+ "poc_reset_info_present_flag"
+ "pps_act_cb_qp_offset_plus5"
+ "pps_act_cr_qp_offset_plus3"
+ "pps_act_y_qp_offset_plus5"
+ "pps_curr_pic_ref_enabled_flag"
+ "pps_extension_data_flag"
+ "pps_infer_scaling_list_flag"
+ "pps_num_palette_predictor_initializers"
+ "pps_palette_predictor_initializer"
+ "pps_palette_predictor_initializers_present_flag"
+ "pps_scaling_list_ref_layer_id"
+ "pps_slice_act_qp_offsets_present_flag"
+ "qualityOfService"
+ "ref_loc_offset_layer_id"
+ "ref_region_bottom_offset"
+ "ref_region_left_offset"
+ "ref_region_offset_present_flag"
+ "ref_region_right_offset"
+ "ref_region_top_offset"
+ "res_coeff_q"
+ "res_coeff_r"
+ "res_coeff_s"
+ "resample_phase_set_present_flag"
+ "residual_adaptive_colour_transform_enabled_flag"
+ "scaled_ref_layer_bottom_offset"
+ "scaled_ref_layer_left_offset"
+ "scaled_ref_layer_offset_present_flag"
+ "scaled_ref_layer_right_offset"
+ "scaled_ref_layer_top_offset"
+ "sendMessageAsIs"
+ "sendMessageWithoutReply"
+ "setMRInfo"
+ "split_octant_flag"
+ "streamPriority"
- "<<<< FigCustomURLHandling >>>> %s: %{public}s.%p: requestID: %llu, error: %{public}@"
- "CountOfRunningClientsChanged"

```
