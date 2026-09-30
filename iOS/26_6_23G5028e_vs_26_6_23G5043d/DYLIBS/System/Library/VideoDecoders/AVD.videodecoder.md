## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-960.0.0.0.0
-  __TEXT.__text: 0x1513c8 sha256:8345820e52db8e0377da6690679a1102fdece14d69d8c619404f51c9e57570fd
-  __TEXT.__auth_stubs: 0xe90 sha256:68765c983918f7f2f7ba759dcfe20f501d5490250ab6a134902539aa40dbddd4
+961.0.0.0.0
+  __TEXT.__text: 0x151a58 sha256:89c822ef899ef801d93b8128fb921fa013eeb9663e61a886e19ee70416c51735
+  __TEXT.__auth_stubs: 0xe90 sha256:25fa1b350cdef40324fbb502251ccf46250146970710cbfc9f245f4915f23b6c
   __TEXT.__const: 0xc013 sha256:7b315febeb52d45c4456a84f8a5d3623531d6610d6a1d5d72892573acd5cefe4
   __TEXT.__gcc_except_tab: 0x8b4 sha256:412f1a5ac08b9096684f26d4ac0b95850d6b59fc75180839db59f29b379a6c7a
-  __TEXT.__oslogstring: 0x145d3 sha256:f0b738917da2589445e173259c09eac91d9c660e5ff74322e9d51461bdc28cf9
-  __TEXT.__cstring: 0x529f sha256:36bad09943e72329e550409ed60e61f3989d633e2f3c3eab3d3c908b523c2d0c
-  __TEXT.__unwind_info: 0x19c0 sha256:30278161131ad3b478d513b3b6c3e58bb79ede4deb9b2c6ffa60a49d5fb878ff
+  __TEXT.__oslogstring: 0x1461c sha256:dae3735c074987f306c66e21458ff43839ba3d2d68735110bf349672429639e6
+  __TEXT.__cstring: 0x52ac sha256:7c0c689409255e69bba77a9581d534a949768294aa716b4548104ffe0b16addd
+  __TEXT.__unwind_info: 0x19c8 sha256:0546d88174b6314249532eac77512feefd1adcdfa15cefff4bdb6ebd9e4bc230
   __DATA_CONST.__got: 0x340 sha256:e0084b66cb4a03e2aba6cc7342eead6a91610ad915d66f9ae2c734f99b772ac7
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
   __AUTH_CONST.__auth_got: 0x750 sha256:d3d91a89c2a8d48cf45f2035c1e2cc2a6b81e7f4d3b6cd668bf4e8ba50507793
-  __AUTH_CONST.__const: 0x4800 sha256:afa6684726db14940b4ad23ffca90abd23a1bf37e3a8ba75deceb048167e024d
-  __AUTH_CONST.__cfstring: 0x660 sha256:7559926782894eab32142028d2759bf4c90fcfb68e58c5aae509732e745ddd67
+  __AUTH_CONST.__const: 0x4800 sha256:b2e393ded64bdb4bcc5bf6c57a9ea14188103a402e1fe5aaa6a85e313d279d5f
+  __AUTH_CONST.__cfstring: 0x660 sha256:af282a732783776c5fe47c767ce8616d0f79d1ca4ee580aa1a352f9fe9b4652f
   __DATA.__common: 0x30 sha256:17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1
   __DATA_DIRTY.__data: 0x78 sha256:b862cf8029191c4ed0da9f1599eeb6d24e89e5a0e305a45a11b948601de7707e
   __DATA_DIRTY.__bss: 0x50 sha256:5b6fb58e61fa475939767d68a446f97f1bff02c0e5935a3ea8bb51e6515783d8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 88954DB7-4C19-39D4-8E60-FC89C5ADFE8E
-  Functions: 3771
-  Symbols:   10005
-  CStrings:  1997
+  UUID: 2CC286F8-07AE-39EC-8FD6-481E50C14C85
+  Functions: 3773
+  Symbols:   10011
+  CStrings:  1998
 
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
+ "22:49:42"
+ "22:49:43"
+ "AppleAVD: ERROR: %{public}s(): workUnits %d exceeded max %d on slice %d\n"
+ "Jun  9 2026"
+ "workUnitOffsetInvalid"
- "23:09:23"
- "23:09:24"
- "23:09:25"
- "May 15 2026"

```
