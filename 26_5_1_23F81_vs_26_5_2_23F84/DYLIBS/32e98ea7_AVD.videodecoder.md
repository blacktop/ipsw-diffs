## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-  __TEXT.__text: 0x151880
+  __TEXT.__text: 0x151f10
   __TEXT.__auth_stubs: 0xe90
   __TEXT.__const: 0xc013
   __TEXT.__gcc_except_tab: 0x8b4
-  __TEXT.__oslogstring: 0x147e1
-  __TEXT.__cstring: 0x52af
-  __TEXT.__unwind_info: 0x19c0
+  __TEXT.__oslogstring: 0x1482a
+  __TEXT.__cstring: 0x52c5
+  __TEXT.__unwind_info: 0x19c8
   __DATA_CONST.__got: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x750

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 3776
-  Symbols:   10015
-  CStrings:  2003
+  Functions: 3778
+  Symbols:   10021
+  CStrings:  2005
 
Sections:
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
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
