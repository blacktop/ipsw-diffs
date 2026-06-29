## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-960.0.0.0.0
-  __TEXT.__text: 0x151880 sha256:75c79205f04cccd98235c357085047401527656c2d183ec1e99f9986ae08dd13
-  __TEXT.__auth_stubs: 0xe90 sha256:81ab2d26ada983b0aff491a02953be7df2d733706f02cf0a02f1d9c5140359fb
+961.0.0.0.0
+  __TEXT.__text: 0x151f10 sha256:a364e2809e874097448a7f18854eaa21a706352c0252d9567197ddc40e281e58
+  __TEXT.__auth_stubs: 0xe90 sha256:e3bc47b0fb8b1f59dbcb6f4ccb56d4d352b9fe76dd69bc985144ab42fa4da695
   __TEXT.__const: 0xc013 sha256:7b315febeb52d45c4456a84f8a5d3623531d6610d6a1d5d72892573acd5cefe4
   __TEXT.__gcc_except_tab: 0x8b4 sha256:412f1a5ac08b9096684f26d4ac0b95850d6b59fc75180839db59f29b379a6c7a
-  __TEXT.__oslogstring: 0x147e1 sha256:3eca3d774ccab4c75a1c3c94fb5105c3666ce5d1be8ca07fe56748bcc1a48db0
-  __TEXT.__cstring: 0x52af sha256:3f9eac5c42450662fb41c324ae89a74b7cd998c580b9a035f8bc2d57f73c3291
-  __TEXT.__unwind_info: 0x19c0 sha256:7b26d10ee781f027f4b1b7c7daea1d2b3f7b6f64c46c2dc940b385fdf524e810
+  __TEXT.__oslogstring: 0x1482a sha256:959e44bb4f9af34d73da1da060a96979167883755248c3bb7144f0b3aea7652a
+  __TEXT.__cstring: 0x52c5 sha256:0578ed5c6b12cf9650a5e84200aa2800f5c05aac8b7aaf36718a273b5b837a2a
+  __TEXT.__unwind_info: 0x19c8 sha256:3c6b80d147c39e523545e29cb24a84cc3bb188c461138504333a19ddc7dcd182
   __DATA_CONST.__got: 0x340 sha256:e0084b66cb4a03e2aba6cc7342eead6a91610ad915d66f9ae2c734f99b772ac7
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
   __AUTH_CONST.__auth_got: 0x750 sha256:d3d91a89c2a8d48cf45f2035c1e2cc2a6b81e7f4d3b6cd668bf4e8ba50507793
-  __AUTH_CONST.__const: 0x4800 sha256:b70e00b7dc993d26ad8f699437e8fa3eadb738d820d619062e137e6e22df581a
-  __AUTH_CONST.__cfstring: 0x680 sha256:45f62452ea91f68f9f673abf577f55b820a925a7bd31be4e6da06cb2ab7a02cc
+  __AUTH_CONST.__const: 0x4800 sha256:145cadf9ba1cd8382c599f12d9831dc612088c19be07183b35b12bcac721635a
+  __AUTH_CONST.__cfstring: 0x680 sha256:a35c2cd3b10683d20719cc1ab392f027c344924ddd18c335130a5d9fe98e5e2d
   __DATA.__common: 0x30 sha256:17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1
   __DATA_DIRTY.__data: 0x78 sha256:b862cf8029191c4ed0da9f1599eeb6d24e89e5a0e305a45a11b948601de7707e
   __DATA_DIRTY.__bss: 0x50 sha256:5b6fb58e61fa475939767d68a446f97f1bff02c0e5935a3ea8bb51e6515783d8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 15F7333C-7EA7-31E4-9AD0-94187BEF437C
-  Functions: 3776
-  Symbols:   10015
-  CStrings:  2003
+  UUID: 60F8BC52-A25C-3A42-8D56-D7A7C6ED584F
+  Functions: 3778
+  Symbols:   10021
+  CStrings:  2005
 
Symbols:
+ __ZN15CAVDHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP22hevc_slice_info_structP15HevcPictureInfo
+ __ZN15CAVDHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP22hevc_slice_info_structP15HevcPictureInfo.cold.1
+ __ZN15CAVDHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP22hevc_slice_info_structP15HevcPictureInfo.cold.2
+ __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP22hevc_slice_info_structP15HevcPictureInfo
+ __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP22hevc_slice_info_structP15HevcPictureInfo.cold.1
+ __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP22hevc_slice_info_structP15HevcPictureInfo.cold.2
+ __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP22hevc_slice_info_structP15HevcPictureInfo.cold.3
+ __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP22hevc_slice_info_structP15HevcPictureInfo.cold.4
+ __ZN6CAHDec21workUnitOffsetInvalidEjjP22hevc_slice_info_struct
+ __ZN6CAHDec21workUnitOffsetInvalidEjjP22hevc_slice_info_struct.cold.1
- __ZN15CAVDHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo
- __ZN15CAVDHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.1
- __ZN15CAVDHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.2
- __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo
- __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.1
- __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.2
- __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.3
- __ZN17CAVDMvHevcDecoder16createRefPicListEP28hevc_picture_parameter_set_tP15hevc_slice_infoP15HevcPictureInfo.cold.4
CStrings:
+ "22:16:05"
+ "22:16:06"
+ "AppleAVD: ERROR: %{public}s(): workUnits %d exceeded max %d on slice %d\n"
+ "Jun  9 2026"
+ "workUnitOffsetInvalid"
- "20:33:42"
- "20:33:43"
- "Apr 23 2026"

```
