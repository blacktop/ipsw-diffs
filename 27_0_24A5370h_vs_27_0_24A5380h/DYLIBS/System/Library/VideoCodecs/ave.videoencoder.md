## ave.videoencoder

> `/System/Library/VideoCodecs/ave.videoencoder`

```diff

-  __TEXT.__text: 0x16b06c
+  __TEXT.__text: 0x16afb8
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x2535c
   __TEXT.__gcc_except_tab: 0x6e4

   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__auth_got: 0x760
   __DATA.__data: 0x80
-  __DATA.__bss: 0x8
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x1058
+  __DATA_DIRTY.__bss: 0x1060
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ __ZN29H264VideoEncoderFrameReceiver9SendFrameEP16_S_AVE_FrameInfoP6Packet : 28272 -> 28220
~ __Z13AVC_FindLeveli : 64 -> 76
~ __Z15AVC_FindProfilei : 68 -> 76
~ __ZN29H264VideoEncoderFrameReceiver34CopyEncodedFrameIntoExternalBufferEP18_S_AVE_EncDataInfoiPh : 1552 -> 1556
~ __Z29AVE_Prop_HEVC_SetProfileLevelPvS_PK10__CFStringPKv : 1908 -> 1916
~ __Z16HEVC_FindProfilei : 68 -> 76
~ __Z14HEVC_FindLeveli : 68 -> 76
~ __Z22AVE_MCTF_GetGatingTypePK19_S_AVE_ISP_Metadata14_E_AVE_DevType20_E_AVE_MCTF_WorkMode16_E_AVE_MCTF_ModeP22_E_AVE_MCTF_GatingType : 1100 -> 1108
~ __Z24AVE_ISP_RetrieveMetadataPK14__CFDictionaryP19_S_AVE_ISP_Metadata : 1056 -> 1060
~ __Z28AVE_Prop_AVC_SetProfileLevelPvS_PK10__CFStringPKv : 2108 -> 2116
~ __Z34AVE_Session_HEVC_ProcessMultiFrameP19_S_AVE_Session_HEVCP25OpaqueVTVideoEncoderFrameP25OpaqueCMTaggedBufferGroupP11_S_AVE_RectP14_S_AVE_TimeExtS8_PK14__CFDictionary : 2960 -> 2972
~ __ZN13AVE_MultiPass12QuantizeDataENSt3__16vectorINS_16_S_AVE_MPClusterENS0_9allocatorIS2_EEEERS5_ : 908 -> 888
~ __ZNSt3__15dequeIP21_S_AVE_MultiPassStatsNS_9allocatorIS2_EEE19__add_back_capacityEv : 484 -> 472
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyERN13AVE_MultiPass25_S_AVE_MPClusterSortCountEPNS2_16_S_AVE_MPClusterEEEvT1_S7_T0_ : 144 -> 140
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_17_ClassicAlgPolicyEPN13AVE_MultiPass16_S_AVE_MPClusterERNS2_25_S_AVE_MPClusterSortCountEEENS_4pairIT0_bEES8_S8_T1_ : 256 -> 244
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERN13AVE_MultiPass25_S_AVE_MPClusterSortCountEPNS2_16_S_AVE_MPClusterEEEbT1_S7_T0_ : 820 -> 808
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyERN13AVE_MultiPass26_S_AVE_MPClusterSortCenterEPNS2_16_S_AVE_MPClusterEEEvT1_S7_T0_ : 152 -> 148
~ __ZNSt3__132__partition_with_equals_on_rightB9fqe220106INS_17_ClassicAlgPolicyEPN13AVE_MultiPass16_S_AVE_MPClusterERNS2_26_S_AVE_MPClusterSortCenterEEENS_4pairIT0_bEES8_S8_T1_ : 284 -> 276
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERN13AVE_MultiPass26_S_AVE_MPClusterSortCenterEPNS2_16_S_AVE_MPClusterEEEbT1_S7_T0_ : 820 -> 808
~ __ZN12htpc_entropy8get_bitsEi : 116 -> 108
~ __Z27AVE_SEI_WriteAV1MetadataOBUPhi19_E_AV1_MetadataTypePKhiPi : 2236 -> 2216
~ __Z26AVE_MCTF_GetPreFiltAdjTypePK19_S_AVE_ISP_Metadata14_E_AVE_DevType20_E_AVE_MCTF_WorkMode16_E_AVE_MCTF_ModeP26_E_AVE_MCTF_PreFiltAdjType : 1132 -> 1140
~ __Z26AVE_MCTF_DecideEnableFlagsiiiiPK19_S_AVE_ISP_Metadata14_E_AVE_DevType20_E_AVE_MCTF_WorkMode16_E_AVE_MCTF_ModePbS5_ : 1700 -> 1708
~ __Z17AVE_MCTF_RetrievePK9__CFArrayP17_S_AVE_MCTF_Param : 3048 -> 2952
~ __Z13AVE_MCTF_MakeP17_S_AVE_MCTF_ParamP9__CFArray : 1004 -> 988
CStrings:
+ "21:19:06"
+ "Jun 29 2026"
- "19:39:57"
- "Jun 18 2026"

```
