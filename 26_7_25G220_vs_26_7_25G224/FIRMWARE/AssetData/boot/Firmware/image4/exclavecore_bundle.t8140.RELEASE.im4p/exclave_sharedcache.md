## exclave_sharedcache

> `AssetData/boot/Firmware/image4/exclavecore_bundle.t8140.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__PDATA.__data`
- `__PDATA.__const`
- `__PDATA.__shared_cache`
- `__PDATA.__auth_ptr`

```diff

 1148.120.6.0.0
-  __TEXT.__text: 0xceca90
+  __TEXT.__text: 0xce7258
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__cstring: 0x940d1
-  __TEXT.__const: 0x18ec24
-  __TEXT.__swift5_typeref: 0x25b84
-  __TEXT.__swift5_reflstr: 0x3dcc8
-  __TEXT.__swift5_assocty: 0xced0
-  __TEXT.__swift5_fieldmd: 0x630cc
-  __TEXT.__constg_swiftt: 0x584d8
-  __TEXT.__swift5_protos: 0xf78
-  __TEXT.__swift5_proto: 0x93fc
-  __TEXT.__swift5_types: 0x5b84
+  __TEXT.__cstring: 0x928a1
+  __TEXT.__const: 0x189c14
+  __TEXT.__swift5_typeref: 0x25a52
+  __TEXT.__swift5_reflstr: 0x3d8b8
+  __TEXT.__swift5_assocty: 0xce70
+  __TEXT.__swift5_fieldmd: 0x62d00
+  __TEXT.__constg_swiftt: 0x580f8
+  __TEXT.__swift5_protos: 0xf68
+  __TEXT.__swift5_proto: 0x9384
+  __TEXT.__swift5_types: 0x5b48
   __TEXT.__swift5_types2: 0x80
   __TEXT.__swift5_builtin: 0x2300
   __TEXT.__objc_methtype: 0x21f
-  __TEXT.__swift5_capture: 0x2848
+  __TEXT.__swift5_capture: 0x2818
   __TEXT.__swift5_mpenum: 0xa94
   __TEXT.__swift_as_entry: 0x14f8
   __TEXT.__swift_as_ret: 0x1620

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x130
-  __TEXT.__eh_frame: 0x6c0b0
+  __TEXT.__eh_frame: 0x6bdf8
   __DATA.__TIGHTBEAM_VT: 0xfc0
   __DATA.__TIGHTBEAM: 0x3f0
-  __DATA.__data: 0x42578
-  __DATA.__const: 0x10a470
+  __DATA.__data: 0x42230
+  __DATA.__const: 0x109e98
   __DATA.__mod_init_func: 0x48
-  __DATA.__ENDPOINTS: 0x18456
-  __DATA.__auth_ptr: 0x5578
+  __DATA.__ENDPOINTS: 0x148c0
+  __DATA.__auth_ptr: 0x5528
   __DATA.__DEVICETREE: 0x30
   __DATA.__shared_cache: 0x2a0
   __DATA.__MMIOREGS: 0x795

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 50164
+  Functions: 50094
   Symbols:   1
-  CStrings:  13723
+  CStrings:  13643
 
CStrings:
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Tue Aug 18 19:38:56 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
+ "Build Date: Tue Aug 18 18:02:44 PDT 2026"
+ "ExclaveOS Image4 Framework Version 7.0.0: Tue Aug 18 19:38:56 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "$JgExclaveIndicatorController.AccessorySensorRequest"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Tue Aug 11 00:28:07 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "Accessory      = "
- "Build Date: Tue Aug 11 00:15:50 PDT 2026"
- "Copy failed: ExclaveBufferArbiter threw unknown exception: "
- "Copy failed: buffer arbiter got out of bounds for size "
- "ExclaveBufferArbiter/ExclaveBufferArbiter_swift.swift"
- "ExclaveBufferArbiter/client.swift"
- "ExclaveOS Image4 Framework Version 7.0.0: Tue Aug 11 00:28:07 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "FaceLivelinessFull"
- "Invalid ArbitratedBuffer "
- "Lbl2D_Anonymized"
- "Missing buffer arbiter for health check enforcement"
- "PatchKeypointTracker"
- "Recon3DBlinkerDecoder"
- "Recon3DBlinkerEncoder"
- "Requested octopus_accessory_indicator_window exceeds maximum "
- "SFDPhoton_320x320"
- "SFDPhoton_320x320.hwx"
- "SFDPhoton_640x640"
- "SFDPhoton_640x640.hwx"
- "SmartFormerImageEncoder"
- "SmartFormerRoomTypeDecoder"
- "SmartFormerSceneSegmentationDecoder"
- "SmartFormerStaticOcclusionDecoder"
- "SmartFormerVisualGroundingDecoder"
- "System/ExclaveKit/System/Library/Frameworks/Vision.framework/facelivelinessfull_ek_fp16.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/SFDPhoton_320x320.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/SFDPhoton_640x640.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/ane_color_cc_forward.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/ane_color_cc_forward_320x320.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/ane_color_cc_postproc.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/ane_color_cc_postproc_320x320.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/ane_color_postproc.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/ane_color_postproc_320x320.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/anisp_srp.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/anisp_srp_320x320.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/swiftawbmodel.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/swiftawbmodel_320x320.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ANSTKit.framework/ANSTEK_320x320.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ANSTKit.framework/ANSTEK_640x640.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/FaceIDCoreLib_exclavekit.framework/models/V6X.bundle/attention_detection_ir.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/FaceIDCoreLib_exclavekit.framework/models/V6X.bundle/attention_detection_rgb.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/FaceIDCoreLib_exclavekit.framework/models/V6X.bundle/face_detection.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/FaceIDCoreLib_exclavekit.framework/models/V6X.bundle/landmark_semantic_face.bundle/*.bundle"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ODTL.framework/PhoneTracking/odtl/0/0/PatchKeypointTracker.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/ODTL.framework/PhoneTracking/odtl/ObjectDetector.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/Recon3D.framework/Models/BlinkerDecoder/model.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/Recon3D.framework/Models/BlinkerEncoder/model.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/SceneIntelligence.framework/ClipImageEncoder.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/SceneIntelligence.framework/ClipRoomTypeDecoder.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/SceneIntelligence.framework/ClipSceneSegmentationDecoder.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/SceneIntelligence.framework/StaticOcclusionDecoder.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/SceneIntelligence.framework/VisualGrounding.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/Visage.framework/VGUnifiedLightingH5Models.bundle/img_to_sg_exclave_model.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/VisualLocalization.framework/espressos/hs.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/VisualLocalization.framework/espressos/lbl2d_anonymized.bundle/*.bundle/main/main_ane"
- "System/ExclaveKit/System/Library/PrivateFrameworks/VisualLocalization.framework/espressos/lbl2d_legacy.bundle/*.bundle/main/main_ane"
- "Unknown buffer type "
- "ane_color_cc_forward"
- "ane_color_cc_forward.hwx"
- "ane_color_cc_forward_320x320"
- "ane_color_cc_forward_320x320.hwx"
- "ane_color_cc_postproc"
- "ane_color_cc_postproc.hwx"
- "ane_color_cc_postproc_320x320"
- "ane_color_cc_postproc_320x320.hwx"
- "ane_color_postproc"
- "ane_color_postproc.hwx"
- "ane_color_postproc_320x320"
- "ane_color_postproc_320x320.hwx"
- "anisp_srp_320x320"
- "anisp_srp_320x320.hwx"
- "invalid rawValue for AccessorySensorType: "
- "invalid rawValue for ArbitratedBuffer: "
- "invalid rawValue for DeviceType: "
- "invalid rawValue for ExclaveBufferArbiter.Selector "
- "ms, clamping to max "
- "octopus_accessory_indicator_window"
- "policy-allow-accessory"
- "swiftawbmodel.hwx"
- "swiftawbmodel_320x320"
- "swiftawbmodel_320x320.hwx"
```
