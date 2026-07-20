## Cinematic

> `/System/iOSSupport/System/Library/Frameworks/Cinematic.framework/Versions/A/Cinematic`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-556.0.0.0.1
-  __TEXT.__text: 0x13e20
-  __TEXT.__objc_methlist: 0xe8c
-  __TEXT.__cstring: 0x379
+558.0.0.0.0
+  __TEXT.__text: 0x1420c
+  __TEXT.__objc_methlist: 0xeb4
+  __TEXT.__cstring: 0x369
   __TEXT.__const: 0x9d8
-  __TEXT.__oslogstring: 0x84d
-  __TEXT.__gcc_except_tab: 0x200
+  __TEXT.__oslogstring: 0x927
+  __TEXT.__gcc_except_tab: 0x290
   __TEXT.__constg_swiftt: 0x5b0
   __TEXT.__swift5_typeref: 0x332
   __TEXT.__swift5_reflstr: 0x22d

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x48
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x838
+  __TEXT.__unwind_info: 0x848
   __TEXT.__eh_frame: 0x448
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x710
-  __DATA_CONST.__objc_classlist: 0xd8
+  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb88
+  __DATA_CONST.__objc_selrefs: 0xb78
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__got: 0x2d0
   __AUTH_CONST.__const: 0x850
-  __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x1df0
+  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__objc_const: 0x1ee0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__auth_got: 0x4d8
-  __AUTH.__objc_data: 0x5a0
+  __AUTH.__objc_data: 0x5f0
   __AUTH.__data: 0x840
-  __DATA.__objc_ivar: 0x94
+  __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x2c8
   __DATA.__bss: 0x740
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 747
-  Symbols:   1296
-  CStrings:  79
+  Functions: 753
+  Symbols:   1307
+  CStrings:  83
 
Symbols:
+ +[CNAssetInfo loadFromCinematicVideoTracks:requireDisparity:error:]
+ -[CNAssetInfo initWithTracks:]
+ -[CNAssetInfoTracks .cxx_destruct]
+ -[CNAssetInfoTracks cinematicDisparityTrack]
+ -[CNAssetInfoTracks cinematicMetadataTrack]
+ -[CNAssetInfoTracks cinematicVideoTrack]
+ -[CNAssetInfoTracks initWithVideoTrack:disparityTrack:metadataTrack:]
+ GCC_except_table15
+ GCC_except_table33
+ OBJC_IVAR_$_CNAssetInfo._assetInfoTracks
+ OBJC_IVAR_$_CNAssetInfoTracks._cinematicDisparityTrack
+ OBJC_IVAR_$_CNAssetInfoTracks._cinematicMetadataTrack
+ OBJC_IVAR_$_CNAssetInfoTracks._cinematicVideoTrack
+ _OBJC_CLASS_$_CNAssetInfoTracks
+ _OBJC_METACLASS_$_CNAssetInfoTracks
+ __67+[CNAssetInfo loadFromCinematicVideoTracks:requireDisparity:error:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_CNAssetInfoTracks
+ __OBJC_$_INSTANCE_VARIABLES_CNAssetInfoTracks
+ __OBJC_$_PROP_LIST_CNAssetInfoTracks
+ __OBJC_CLASS_RO_$_CNAssetInfoTracks
+ __OBJC_METACLASS_RO_$_CNAssetInfoTracks
+ ___67+[CNAssetInfo loadFromCinematicVideoTracks:requireDisparity:error:]_block_invoke
+ ___block_descriptor_57_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48r56r_e34_v24?0"AVAssetTrack"8"NSError"16ls32l8r48l8s40l8r56l8
+ ___block_descriptor_73_e8_32s40s48s56r64r_e34_v24?0"AVAssetTrack"8"NSError"16ls32l8r56l8s40l8s48l8r64l8
+ _kPTCinematographyIdentifier
+ _objc_msgSend$initWithTracks:
+ _objc_msgSend$initWithVideoTrack:disparityTrack:metadataTrack:
+ _objc_msgSend$loadFromCinematicVideoTracks:requireDisparity:error:
+ _objc_retain_x26
- +[CNAssetInfo loadFromCinematicVideoTrack:requireDisparity:completionHandler:]
- -[CNAssetInfo _initWithVideoTrack:disparityTrack:metadataTrack:]
- -[CNAssetInfo setCinematicDisparityTrack:]
- -[CNAssetInfo setCinematicMetadataTrack:]
- -[CNAssetInfo setCinematicVideoTrack:]
- GCC_except_table32
- OBJC_IVAR_$_CNAssetInfo._cinematicDisparityTrack
- OBJC_IVAR_$_CNAssetInfo._cinematicMetadataTrack
- OBJC_IVAR_$_CNAssetInfo._cinematicVideoTrack
- __78+[CNAssetInfo loadFromCinematicVideoTrack:requireDisparity:completionHandler:]_block_invoke
- ___65+[CNAssetInfo _loadFromAsset:requireDisparity:completionHandler:]_block_invoke_2
- ___78+[CNAssetInfo loadFromCinematicVideoTrack:requireDisparity:completionHandler:]_block_invoke
- ___block_descriptor_57_e8_32s40bs_e34_v24?0"AVAssetTrack"8"NSError"16ls32l8s40l8
- ___block_descriptor_57_e8_32s40r48r_e33_v24?0"CNAssetInfo"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_65_e8_32s40s48bs_e34_v24?0"AVAssetTrack"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_73_e8_32s40bs48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
- _objc_msgSend$_initWithVideoTrack:disparityTrack:metadataTrack:
- _objc_msgSend$loadFromCinematicVideoTrack:requireDisparity:completionHandler:
- _objc_retain_x27
CStrings:
+ "Error ptr is nil"
+ "Error: Cannot find video track"
+ "Error: Unexpected number of video tracks. Found %lu expected 1."
+ "Ignoring multiple video tracks in asset"
+ "Unsupported asset. requireDisparity %i. Disparity %i. Metadata %i"
- "mdta/"
```
