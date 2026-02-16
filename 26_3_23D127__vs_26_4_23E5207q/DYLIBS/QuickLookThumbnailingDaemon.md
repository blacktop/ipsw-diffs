## QuickLookThumbnailingDaemon

> `/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon`

```diff

-208.4.1.0.0
-  __TEXT.__text: 0x56a94
-  __TEXT.__auth_stubs: 0x1f10
-  __TEXT.__objc_methlist: 0x31c4
-  __TEXT.__const: 0x1074
-  __TEXT.__gcc_except_tab: 0xe58
-  __TEXT.__cstring: 0x47bb
+208.5.4.0.0
+  __TEXT.__text: 0x570bc
+  __TEXT.__auth_stubs: 0x1e80
+  __TEXT.__objc_methlist: 0x31bc
+  __TEXT.__const: 0x1044
+  __TEXT.__gcc_except_tab: 0xdec
+  __TEXT.__cstring: 0x42c1
   __TEXT.__oslogstring: 0x52c6
   __TEXT.__constg_swiftt: 0x400
-  __TEXT.__swift5_typeref: 0xb90
+  __TEXT.__swift5_typeref: 0xb0c
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_reflstr: 0x2d4
   __TEXT.__swift5_fieldmd: 0x264
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_types: 0x40
-  __TEXT.__swift5_capture: 0x128
+  __TEXT.__swift5_capture: 0xf8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x28
   __TEXT.__dof_QuickLook: 0xb22
-  __TEXT.__unwind_info: 0x14d8
-  __TEXT.__eh_frame: 0x720
-  __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x9ce8
-  __TEXT.__objc_methtype: 0x1b0d
-  __TEXT.__objc_stubs: 0x7600
-  __DATA_CONST.__got: 0x750
-  __DATA_CONST.__const: 0x12a0
+  __TEXT.__unwind_info: 0x15b8
+  __TEXT.__eh_frame: 0x760
+  __TEXT.__objc_classname: 0x5db
+  __TEXT.__objc_methname: 0x9f33
+  __TEXT.__objc_methtype: 0x1c81
+  __TEXT.__objc_stubs: 0x79e0
+  __DATA_CONST.__got: 0x740
+  __DATA_CONST.__const: 0x1318
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24a8
+  __DATA_CONST.__objc_selrefs: 0x2490
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xf0
-  __AUTH_CONST.__auth_got: 0xf98
-  __AUTH_CONST.__const: 0x9a0
+  __AUTH_CONST.__auth_got: 0xf50
+  __AUTH_CONST.__const: 0x978
   __AUTH_CONST.__cfstring: 0x1bc0
-  __AUTH_CONST.__objc_const: 0x52b8
+  __AUTH_CONST.__objc_const: 0x52e8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2e0
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x480
-  __DATA.__data: 0x720
+  __DATA.__objc_ivar: 0x484
+  __DATA.__data: 0x628
   __DATA.__bss: 0xe50
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0xc88
-  __DATA_DIRTY.__data: 0x278
+  __DATA_DIRTY.__data: 0x360
   __DATA_DIRTY.__bss: 0x290
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 163539FE-FD8E-3EFB-8921-69ACE2E88847
-  Functions: 2020
-  Symbols:   5829
-  CStrings:  3024
+  UUID: 65AF4C36-6E6B-3B85-86BF-E230DDD0F84D
+  Functions: 2025
+  Symbols:   5933
+  CStrings:  3007
 
Symbols:
+ -[QLServerThread _afterGenerationForGeneratorRequest:withGenerator:bitmapImages:contentRect:shouldUpdateGenstore:completionHandler:]
+ -[QLServerThread _afterGenerationForGeneratorRequest:withGenerator:bitmapImages:contentRect:shouldUpdateGenstore:completionHandler:].cold.1
+ -[QLSqliteDatabase setUniqueStrings:]
+ -[QLSqliteDatabase uniqueStrings]
+ -[QLSqliteDatabase(SqliteHelpers) newStringFromColumn:inStatement:uniquing:]
+ GCC_except_table69
+ GCC_except_table70
+ _OBJC_IVAR_$_QLSqliteDatabase._uniqueStrings
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _QLCacheSuffixMarkerCheck
+ _QLCacheSuffixMarkerCheck.cold.1
+ ___115-[QLServerThread addImage:contentRect:hasIconModeApplied:flavor:extensionBadge:metadata:toCacheAndCompleteRequest:]_block_invoke
+ ___52-[QLThumbnailAdditionIndex openDatabaseAtURL:error:]_block_invoke.26.cold.1
+ ___52-[QLThumbnailAdditionIndex openDatabaseAtURL:error:]_block_invoke.cold.3
+ ___94-[QLServerThread generateThumbnailForThumbnailRequest:shouldUpdateGenstore:completionHandler:]_block_invoke.72
+ ___94-[QLServerThread generateThumbnailForThumbnailRequest:shouldUpdateGenstore:completionHandler:]_block_invoke_2.74
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_84_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.87
+ ___block_literal_global.93
+ _block_copy_helper.35
+ _block_copy_helper.56
+ _block_descriptor.37
+ _block_descriptor.58
+ _block_destroy_helper.36
+ _block_destroy_helper.57
+ _get_witness_table 7SwiftUI6ZStackVyAA19_ConditionalContentVyAA08ModifiedE0VyAGyAGyAA5ImageVAA18_AspectRatioLayoutVGAA06_FrameJ0VGAA11_ClipEffectVyAA9RectangleVGGAGyAGyAA4ViewPAAE12drawingGroup6opaque9colorModeQrSb_AA014ColorRenderingT0OtFQOyAGyACyAEyAGyAA6CanvasVyAA05EmptyO0VGAKGAUGGAA24_BackgroundStyleModifierVyAA0U0VGG_Qo_AQyAA07RoundedN0V6_InsetVGGAA16_OverlayModifierVyAA017StrokeBorderShapeO0VyA17_A12_A4_GSgGGGGAaVHPyHC.4
+ _objc_msgSend$_afterGenerationForGeneratorRequest:withGenerator:bitmapImages:contentRect:shouldUpdateGenstore:completionHandler:
+ _objc_msgSend$_typeWithIdentifier:allowUndeclared:
+ _objc_msgSend$additionalProperties
+ _objc_msgSend$attributes
+ _objc_msgSend$bitmapImages
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$bundleVersion
+ _objc_msgSend$colorSpace
+ _objc_msgSend$containingBundleRecord
+ _objc_msgSend$contentTypeIsIWorkType:
+ _objc_msgSend$contentTypeIsInternallyClaimed:
+ _objc_msgSend$entitlementNamed:ofClass:
+ _objc_msgSend$executeQueries:
+ _objc_msgSend$extensionIdentities
+ _objc_msgSend$extensionPointIdentifier
+ _objc_msgSend$externalGeneratorPreferredForType:
+ _objc_msgSend$externalThumbnailGeneratorData
+ _objc_msgSend$generateThumbnailWithCompletionHandler:
+ _objc_msgSend$initWithAppex:request:completionHandler:
+ _objc_msgSend$initWithExtensionPointIdentifier:
+ _objc_msgSend$initWithImage:contentRect:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithItem:maximumSize:minimumSize:scale:options:generationData:
+ _objc_msgSend$initWithQueries:
+ _objc_msgSend$ioSurface
+ _objc_msgSend$newStringFromColumn:inStatement:uniquing:
+ _objc_msgSend$nsExtensionAttributes
+ _objc_msgSend$queries
+ _objc_msgSend$setName:
+ _objc_msgSend$setParentDirectoryWrapper:
+ _objc_msgSend$shouldUseRestrictedExtension
+ _objc_msgSend$thirdPartyVideoDecodersAllowed
+ _objc_msgSend$uniqueIdentifier
+ _objc_release_x2
- -[QLCacheMMAPBlobDatabase copyBlobWithInfo:].cold.7
- -[QLSqliteDatabase(SqliteHelpers) newCFStringFromColumn:inStatement:uniqueInStringTable:]
- -[QLSqliteDatabase(SqliteHelpers) newCFURLFromColumn:inStatement:]
- -[QLSqliteDatabase(SqliteHelpers) newColumnName:inStatement:uniqueInStringTable:]
- -[QLSqliteDatabase(SqliteHelpers) newPathFromColumn:inStatement:uniqueInStringTable:]
- -[QLSqliteDatabase(SqliteHelpers) newStringFromColumn:inStatement:uniqueInStringTable:]
- GCC_except_table65
- _CFURLCreateFromFileSystemRepresentation
- ___94-[QLServerThread generateThumbnailForThumbnailRequest:shouldUpdateGenstore:completionHandler:]_block_invoke_2.cold.1
- ___block_literal_global.85
- ___block_literal_global.91
- _block_copy_helper.40
- _block_copy_helper.61
- _block_descriptor.42
- _block_descriptor.63
- _block_destroy_helper.41
- _block_destroy_helper.62
- _get_witness_table 7SwiftUI6ZStackVyAA19_ConditionalContentVyAA08ModifiedE0VyAGyAGyAA5ImageVAA18_AspectRatioLayoutVGAA06_FrameJ0VGAA11_ClipEffectVyAA9RectangleVGGAGyAGyAA4ViewPAAE12drawingGroup6opaque9colorModeQrSb_AA014ColorRenderingT0OtFQOyAGyACyAEyAGyAA6CanvasVyAA05EmptyO0VGAKGAUGGAA24_BackgroundStyleModifierVyAA0U0VGG_Qo_AQyAA07RoundedN0V6_InsetVGGAA16_OverlayModifierVyAA017StrokeBorderShapeO0VyA17_A12_A4_GSgGGGGAaVHPyHC.3
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$knownFileProviderIdentifiersSoFar
- _objc_msgSend$newStringFromColumn:inStatement:uniqueInStringTable:
- _objc_msgSend$stringWithFileSystemRepresentation:length:
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _sqlite3_column_name
- _swift_bridgeObjectRetain_n
- _symbolic So20_EXExtensionIdentityCSgSg
- _symbolic _____y_____y_____y_____yAAy_____y_____G_____GAAyAAyAAy_____AGG_____G_____y_____GGGG_____y_____GG_Qo_ 7SwiftUI4ViewPAAE12drawingGroup6opaque9colorModeQrSb_AA014ColorRenderingH0OtFQO AA15ModifiedContentV AA6ZStackV AA012_ConditionalL0V AA6CanvasV AA05EmptyC0V AA18_AspectRatioLayoutV AA5ImageV AA06_FrameS0V AA11_ClipEffectV AA9RectangleV AA24_BackgroundStyleModifierV AA0I0V
CStrings:
+ "T@\"NSMutableSet\",&,N,V_uniqueStrings"
+ "_afterGenerationForGeneratorRequest:withGenerator:bitmapImages:contentRect:shouldUpdateGenstore:completionHandler:"
+ "_uniqueStrings"
+ "newStringFromColumn:inStatement:uniquing:"
+ "setUniqueStrings:"
+ "uniqueStrings"
+ "v84@0:8@16@24@32{CGRect={CGPoint=dd}{CGSize=dd}}40B72@?76"
- "@36@0:8i16^{sqlite3_stmt=}20@28"
- "^{__CFString=}36@0:8i16^{sqlite3_stmt=}20@28"
- "^{__CFURL=}28@0:8i16^{sqlite3_stmt=}20"
- "knownFileProviderIdentifiersSoFar"
- "newCFStringFromColumn:inStatement:uniqueInStringTable:"
- "newCFURLFromColumn:inStatement:"
- "newColumnName:inStatement:uniqueInStringTable:"
- "newPathFromColumn:inStatement:uniqueInStringTable:"
- "newStringFromColumn:inStatement:uniqueInStringTable:"
- "stringWithFileSystemRepresentation:length:"

```
