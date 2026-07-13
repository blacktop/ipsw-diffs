## AssetsLibrary

> `/System/Library/Frameworks/AssetsLibrary.framework/AssetsLibrary`

```diff

-  __TEXT.__text: 0x9e6c
-  __TEXT.__auth_stubs: 0x510
+  __TEXT.__text: 0xa098
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_methlist: 0xae4
   __TEXT.__dlopen_cstrs: 0x43
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x4cc
-  __TEXT.__cstring: 0x850
+  __TEXT.__gcc_except_tab: 0x4ec
+  __TEXT.__cstring: 0x867
   __TEXT.__oslogstring: 0xab
-  __TEXT.__unwind_info: 0x578
+  __TEXT.__unwind_info: 0x590
   __TEXT.__objc_classname: 0x119
-  __TEXT.__objc_methname: 0x235e
+  __TEXT.__objc_methname: 0x23a0
   __TEXT.__objc_methtype: 0x440
-  __TEXT.__objc_stubs: 0x1f60
+  __TEXT.__objc_stubs: 0x1fc0
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x848
+  __DATA_CONST.__const: 0x8c0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa60
+  __DATA_CONST.__objc_selrefs: 0xa80
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x298
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x6a0
+  __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0xe78
-  __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x120
   __DATA.__bss: 0x78

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
+  - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices
   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 295
-  Symbols:   1244
-  CStrings:  597
+  Functions: 297
+  Symbols:   1256
+  CStrings:  605
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ GCC_except_table150
+ GCC_except_table159
+ GCC_except_table165
+ GCC_except_table197
+ GCC_except_table204
+ GCC_except_table225
+ GCC_except_table232
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table250
+ GCC_except_table255
+ GCC_except_table278
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table291
+ _DCIM_newPLImageWithCGImage
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_PHAssetChangeRequest
+ _OBJC_CLASS_$_PHAssetCreationRequest
+ _OBJC_CLASS_$_PHPhotoLibrary
+ ___56-[ALAssetsLibrary assetForURL:resultBlock:failureBlock:]_block_invoke_3
+ ___90-[ALAssetsLibrary _writeVideoAtPathToSavedPhotosAlbum:internalProperties:completionBlock:]_block_invoke_5
+ ___block_descriptor_48_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_64_e8_32o40o48o56b_e8_v16?0q8ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_65_e8_32o40o48o56b_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32o40o48b56r_e20_v20?0B8"NSError"12lr56l8s32l8s48l8s40l8
+ ___block_descriptor_72_e8_32o40o48o56b64r_e20_v20?0B8"NSError"12lr64l8s32l8s40l8s56l8s48l8
+ ___block_descriptor_80_e8_32o40o48o56b_e8_v16?0q8ls32l8s56l8s40l8s48l8
+ ___block_descriptor_81_e8_32o40o48o56b_e5_v8?0ls56l8s32l8s40l8s48l8
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$addResourceWithType:data:options:
+ _objc_msgSend$creationRequestForAsset
+ _objc_msgSend$creationRequestForAssetFromImage:
+ _objc_msgSend$creationRequestForAssetFromVideoAtFileURL:
+ _objc_msgSend$placeholderForCreatedAsset
+ _objc_msgSend$uppercaseString
- GCC_except_table161
- GCC_except_table191
- GCC_except_table202
- GCC_except_table223
- GCC_except_table228
- GCC_except_table237
- GCC_except_table238
- GCC_except_table248
- GCC_except_table253
- GCC_except_table276
- GCC_except_table284
- GCC_except_table285
- GCC_except_table289
- _OBJC_CLASS_$_NSConstantIntegerNumber
- ___115-[ALAssetsLibrary _writeImageToSavedPhotosAlbum:orientation:imageData:metadata:internalProperties:completionBlock:]_block_invoke_4
- ___block_descriptor_56_e8_32o40o48b_e27_v24?0"NSURL"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_72_e8_32o40o48o56o64b_e8_v16?0q8ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32o40o48o56o64b_e5_v8?0ls64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_96_e8_32o40o48o56o64o72b_e8_v16?0q8ls32l8s72l8s40l8s48l8s56l8s64l8
- ___block_descriptor_97_e8_32o40o48o56o64o72b_e5_v8?0ls72l8s32l8s40l8s48l8s56l8s64l8
- ___kCFBooleanTrue
- _kPLAssetsSaverMetadata
- _kPLImageWriterImportedBy
- _kPLRequiresSaveOnlyAuthorization
- _objc_msgSend$_setBundlePropertiesOnPropertiesDictionary:
- _objc_msgSend$initWithDictionary:
- _objc_msgSend$saveImageRef:orientation:imageData:properties:completionBlock:
- _objc_msgSend$saveVideoAtPath:properties:completionBlock:
CStrings:
+ "JPG"
+ "MOV"
+ "URLWithString:"
+ "addResourceWithType:data:options:"
+ "assets-library://asset/asset.%@?id=%@&ext=%@"
+ "creationRequestForAsset"
+ "creationRequestForAssetFromImage:"
+ "creationRequestForAssetFromVideoAtFileURL:"
+ "placeholderForCreatedAsset"
+ "uppercaseString"
- "initWithDictionary:"
- "s"
- "saveImageRef:orientation:imageData:properties:completionBlock:"
- "saveVideoAtPath:properties:completionBlock:"
- "v24@?0@\"NSURL\"8@\"NSError\"16"

```
