## PaperBoardUI

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI`

```diff

-283.101.0.0.0
-  __TEXT.__text: 0x7f0dc
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_methlist: 0x9efc
+286.101.0.0.0
+  __TEXT.__text: 0x80ee4
+  __TEXT.__auth_stubs: 0x1070
+  __TEXT.__objc_methlist: 0xa164
   __TEXT.__const: 0x838
-  __TEXT.__cstring: 0x789e
-  __TEXT.__oslogstring: 0x41e7
-  __TEXT.__gcc_except_tab: 0x119c
+  __TEXT.__cstring: 0x7b12
+  __TEXT.__oslogstring: 0x43e3
+  __TEXT.__gcc_except_tab: 0x1218
   __TEXT.__dlopen_cstrs: 0x1a6
-  __TEXT.__unwind_info: 0x2b90
-  __TEXT.__objc_classname: 0x15f0
-  __TEXT.__objc_methname: 0x177d1
-  __TEXT.__objc_methtype: 0x405e
-  __TEXT.__objc_stubs: 0x11c20
-  __DATA_CONST.__got: 0x928
-  __DATA_CONST.__const: 0x28c0
+  __TEXT.__unwind_info: 0x2c18
+  __TEXT.__objc_classname: 0x15f1
+  __TEXT.__objc_methname: 0x17fb5
+  __TEXT.__objc_methtype: 0x4133
+  __TEXT.__objc_stubs: 0x11f40
+  __DATA_CONST.__got: 0x940
+  __DATA_CONST.__const: 0x2898
   __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52c0
+  __DATA_CONST.__objc_selrefs: 0x5418
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __AUTH_CONST.__auth_got: 0x840
+  __AUTH_CONST.__auth_got: 0x848
   __AUTH_CONST.__const: 0xba0
-  __AUTH_CONST.__cfstring: 0x62c0
-  __AUTH_CONST.__objc_const: 0x1c528
+  __AUTH_CONST.__cfstring: 0x6360
+  __AUTH_CONST.__objc_const: 0x1ca80
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH.__objc_data: 0x2210
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0xa18
+  __DATA.__objc_ivar: 0xa60
   __DATA.__data: 0x18e0
-  __DATA.__bss: 0x3f8
+  __DATA.__bss: 0x418
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 61DB4349-AD0E-30DE-86AF-9E97134CCBCA
-  Functions: 3934
-  Symbols:   13623
-  CStrings:  6466
+  UUID: BC9B04E9-93A8-3CF0-9F70-587FAEA6D8FF
+  Functions: 4000
+  Symbols:   13813
+  CStrings:  6565
 
Symbols:
+ -[PBUICachedSnapshotEffectProvider setNeedsSourceUpdate].cold.1
+ -[PBUIPosterHUDController _createAttachmentForImage:]
+ -[PBUIPosterHUDController _createLabelWithAlignment:]
+ -[PBUIPosterHUDController _createThumbnailFromImage:]
+ -[PBUIPosterHUDController _generateColumnContentForVariant:snapshot:snapshotDate:legibilityEnvironment:legibilityDate:]
+ -[PBUIPosterHUDController _generateHUDContents]
+ -[PBUIPosterHUDController _generatePosterStatusContent]
+ -[PBUIPosterHUDController _setupAndShowHUDWindow]
+ -[PBUIPosterHUDController _updateHUDLayout]
+ -[PBUIPosterHUDController homeColumnContent]
+ -[PBUIPosterHUDController homeColumnLabel]
+ -[PBUIPosterHUDController hudContainerView]
+ -[PBUIPosterHUDController lockColumnContent]
+ -[PBUIPosterHUDController lockColumnLabel]
+ -[PBUIPosterHUDController orientationWrapperView]
+ -[PBUIPosterHUDController posterStatusContent]
+ -[PBUIPosterHUDController posterStatusLabel]
+ -[PBUIPosterHUDController setHomeColumnContent:]
+ -[PBUIPosterHUDController setHomeColumnLabel:]
+ -[PBUIPosterHUDController setHudContainerView:]
+ -[PBUIPosterHUDController setLockColumnContent:]
+ -[PBUIPosterHUDController setLockColumnLabel:]
+ -[PBUIPosterHUDController setOrientationWrapperView:]
+ -[PBUIPosterHUDController setPosterStatusContent:]
+ -[PBUIPosterHUDController setPosterStatusLabel:]
+ -[PBUIPosterHUDController updateVariant:lastSnapshotImage:legibilityEnvironmentContext:]
+ -[PBUIPosterVariantViewController _scheduleSnapshotIfNeeded:].cold.1
+ -[PBUIPosterVariantViewController _snapshotNow:].cold.2
+ -[PBUIPosterVariantViewController _updatePosterColorStatistics:desiredLegibilitySettings:]
+ -[PBUIPosterVariantViewController averageColorInRect:]
+ -[PBUIPosterVariantViewController averageSaturation]
+ -[PBUIPosterVariantViewController contrastInRect:]
+ -[PBUIPosterVariantViewController legibilityEnvironmentContext]
+ -[PBUIPosterVariantViewController lumaInRect:]
+ -[PBUIPosterVariantViewController saturationInRect:]
+ -[PBUIPosterVariantViewController snapshotIfNeeded:reason:]
+ -[PBUIPosterVariantViewController snapshotIfNeeded:reason:].cold.1
+ -[PBUIPosterVariantViewController snapshotIfNeeded:reason:].cold.2
+ -[PBUIPosterVariantViewController snapshotIfNeeded:reason:].cold.3
+ -[PBUIPosterViewController averageColorInRect:]
+ -[PBUIPosterViewController averageSaturation]
+ -[PBUIPosterViewController contrastInRect:]
+ -[PBUIPosterViewController contrastInRect:forVariant:]
+ -[PBUIPosterViewController legibilityEnvironmentContextForVariant:]
+ -[PBUIPosterViewController legibilityEnvironmentContext]
+ -[PBUIPosterViewController lumaInRect:]
+ -[PBUIPosterViewController saturationInRect:]
+ -[PBUIPosterViewController saturationInRect:forVariant:]
+ -[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedForVariants:notifyObservers:]
+ -[PBUIPosterWallpaperRemoteViewController legibilityEnvironmentContextForVariant:]
+ -[PBUIPosterWallpaperRemoteViewController saturationInRect:forVariant:]
+ -[PBUIPosterWallpaperViewController averageColorInRect:]
+ -[PBUIPosterWallpaperViewController averageSaturation]
+ -[PBUIPosterWallpaperViewController contrastInRect:]
+ -[PBUIPosterWallpaperViewController contrastInRect:forVariant:]
+ -[PBUIPosterWallpaperViewController legibilityEnvironmentContextForVariant:]
+ -[PBUIPosterWallpaperViewController legibilityEnvironmentContext]
+ -[PBUIPosterWallpaperViewController lumaInRect:]
+ -[PBUIPosterWallpaperViewController saturationInRect:]
+ -[PBUIPosterWallpaperViewController saturationInRect:forVariant:]
+ GCC_except_table113
+ GCC_except_table118
+ GCC_except_table123
+ GCC_except_table125
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table149
+ GCC_except_table152
+ GCC_except_table154
+ GCC_except_table156
+ GCC_except_table158
+ GCC_except_table18
+ GCC_except_table44
+ GCC_except_table52
+ GCC_except_table56
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table97
+ _CFAbsoluteTimeGetCurrent
+ _OBJC_CLASS_$_BSAuditToken
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSTextAttachment
+ _OBJC_IVAR_$_PBUIFakeBlurView._debugView
+ _OBJC_IVAR_$_PBUIPosterHUDController._homeColumnContent
+ _OBJC_IVAR_$_PBUIPosterHUDController._homeColumnLabel
+ _OBJC_IVAR_$_PBUIPosterHUDController._homeLastLegibilityEnvironment
+ _OBJC_IVAR_$_PBUIPosterHUDController._homeLastSnapshot
+ _OBJC_IVAR_$_PBUIPosterHUDController._homeLastSnapshotUpdateDate
+ _OBJC_IVAR_$_PBUIPosterHUDController._homeLegibilityEnvironmentLastUpdateDate
+ _OBJC_IVAR_$_PBUIPosterHUDController._hudContainerView
+ _OBJC_IVAR_$_PBUIPosterHUDController._lockColumnContent
+ _OBJC_IVAR_$_PBUIPosterHUDController._lockColumnLabel
+ _OBJC_IVAR_$_PBUIPosterHUDController._lockLastLegibilityEnvironment
+ _OBJC_IVAR_$_PBUIPosterHUDController._lockLastSnapshot
+ _OBJC_IVAR_$_PBUIPosterHUDController._lockLastSnapshotUpdateDate
+ _OBJC_IVAR_$_PBUIPosterHUDController._lockLegibilityEnvironmentLastUpdateDate
+ _OBJC_IVAR_$_PBUIPosterHUDController._orientationWrapperView
+ _OBJC_IVAR_$_PBUIPosterHUDController._posterStatusContent
+ _OBJC_IVAR_$_PBUIPosterHUDController._posterStatusLabel
+ _OBJC_IVAR_$_PBUIPosterHUDController._posterStatusString
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._isSnapshotting
+ _OBJC_IVAR_$_PBUIPosterVariantViewController._legibilityEnvironmentContext
+ _OUTLINED_FUNCTION_8
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PUIColorStatisticsObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PUIColorStatisticsObserver
+ __OBJC_$_PROTOCOL_REFS_PUIColorStatisticsObserver
+ __OBJC_LABEL_PROTOCOL_$_PUIColorStatisticsObserver
+ __OBJC_PROTOCOL_$_PUIColorStatisticsObserver
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke.96
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_2
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_2.97
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_2.97.cold.1
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_2.97.cold.2
+ ___59-[PBUIPosterVariantViewController snapshotIfNeeded:reason:]_block_invoke_3
+ ___64-[PBUIPosterVariantViewController fetchWallpaperProminentColor:]_block_invoke.53
+ ___64-[PBUIPosterVariantViewController fetchWallpaperProminentColor:]_block_invoke.53.cold.1
+ ___89-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedForVariants:notifyObservers:]_block_invoke
+ ___89-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedForVariants:notifyObservers:]_block_invoke_2
+ ___89-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedForVariants:notifyObservers:]_block_invoke_3
+ ___89-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedForVariants:notifyObservers:]_block_invoke_4
+ ___90-[PBUIPosterVariantViewController _updatePosterColorStatistics:desiredLegibilitySettings:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s_e40_v16?0"PBUISnapshotPreconditionResult"8ls32l8
+ ___block_descriptor_48_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_49_e8_32w_e5_v8?0lw32l8
+ ___block_literal_global.536
+ ___block_literal_global.794
+ ___block_literal_global.92
+ ___block_literal_global.94
+ ___block_literal_global.96
+ ___getPFPosterRoleLockScreenSymbolLoc_block_invoke
+ ___getPLKAverageColorFromColorBoxesSymbolLoc_block_invoke
+ ___getPLKCalculateContrastFromColorBoxesSymbolLoc_block_invoke
+ ___getPLKColorBoxesClass_block_invoke
+ ___getPLKColorBoxesClass_block_invoke.cold.1
+ ___getPLKLegibilityEnvironmentVariantContextClass_block_invoke
+ ___getPLKLegibilityEnvironmentVariantContextClass_block_invoke.cold.1
+ ___getPLKLegibilityStyleForUILegibilityStyleSymbolLoc_block_invoke
+ ___getPUIPosterSnapshotHostConfigurationDescriptorClass_block_invoke
+ ___getPUIPosterSnapshotHostConfigurationDescriptorClass_block_invoke.cold.1
+ _getPFPosterRoleLockScreen
+ _getPFPosterRoleLockScreen.cold.1
+ _getPFPosterRoleLockScreenSymbolLoc
+ _getPFPosterRoleLockScreenSymbolLoc.ptr
+ _getPLKAverageColorFromColorBoxesSymbolLoc
+ _getPLKAverageColorFromColorBoxesSymbolLoc.ptr
+ _getPLKCalculateContrastFromColorBoxesSymbolLoc
+ _getPLKCalculateContrastFromColorBoxesSymbolLoc.ptr
+ _getPLKColorBoxesClass
+ _getPLKColorBoxesClass.softClass
+ _getPLKLegibilityEnvironmentVariantContextClass
+ _getPLKLegibilityEnvironmentVariantContextClass.softClass
+ _getPLKLegibilityStyleForUILegibilityStyleSymbolLoc
+ _getPLKLegibilityStyleForUILegibilityStyleSymbolLoc.ptr
+ _getPUIPosterSnapshotHostConfigurationDescriptorClass
+ _getPUIPosterSnapshotHostConfigurationDescriptorClass.softClass
+ _objc_msgSend$_createThumbnailFromImage:
+ _objc_msgSend$_legibilityUpdatedForVariants:notifyObservers:
+ _objc_msgSend$_updatePosterColorStatistics:desiredLegibilitySettings:
+ _objc_msgSend$addColorStatisticsObserver:
+ _objc_msgSend$addCompletionBlock:scheduler:
+ _objc_msgSend$attributedStringWithAttachment:
+ _objc_msgSend$averageColorInRect:
+ _objc_msgSend$averageSaturation
+ _objc_msgSend$colorBoxesForAverageColor:
+ _objc_msgSend$contrastInRect:forVariant:
+ _objc_msgSend$copyWithWaitUntilReady:
+ _objc_msgSend$destinationWithTemporaryDirectoryWithAuditToken:error:
+ _objc_msgSend$drawInRect:
+ _objc_msgSend$initWithColorBoxes:
+ _objc_msgSend$initWithOutputDescriptor:sceneDescriptor:attachments:analysis:host:
+ _objc_msgSend$initWithVariant:style:averageColor:contrast:saturation:legibilitySettings:
+ _objc_msgSend$initWithVariant:style:colorBoxes:legibilitySettings:
+ _objc_msgSend$isInvalid
+ _objc_msgSend$legibilityEnvironmentContext
+ _objc_msgSend$lumaInRect:
+ _objc_msgSend$orangeColor
+ _objc_msgSend$pui_executeSnapshotForDescriptor:outputDestination:
+ _objc_msgSend$pui_significantEventsCounterDidChange
+ _objc_msgSend$saturationInRect:
+ _objc_msgSend$saturationInRect:forVariant:
+ _objc_msgSend$setAdjustsFontSizeToFitWidth:
+ _objc_msgSend$setTextAlignment:
+ _objc_msgSend$setTextColor:
+ _objc_msgSend$snapshotIfNeeded:reason:
+ _objc_msgSend$snapshotInProcessHostConfigurationDescriptorWithWorkQueue:
+ _objc_msgSend$snapshotOutOfProcessHostConfigurationDescriptor
+ _objc_msgSend$tokenFromAuditToken:
+ _objc_msgSend$updateWithContext:
+ _objc_msgSend$updateWithContext:variants:
+ _objc_msgSend$valueForEntitlement:
+ _soft_PLKAverageColorFromColorBoxes
+ _soft_PLKAverageColorFromColorBoxes.cold.1
+ _soft_PLKCalculateContrastFromColorBoxes
+ _soft_PLKCalculateContrastFromColorBoxes.cold.1
+ _soft_PLKLegibilityStyleForUILegibilityStyle
+ _soft_PLKLegibilityStyleForUILegibilityStyle.cold.1
- -[PBUIPosterHUDController containerView]
- -[PBUIPosterHUDController posterActiveLabel]
- -[PBUIPosterHUDController setContainerView:]
- -[PBUIPosterHUDController setPosterActiveLabel:]
- -[PBUIPosterHUDController setupAndShowHUDWindow]
- -[PBUIPosterVariantViewController _updatePosterAverageColor:desiredLegibilitySettings:]
- -[PBUIPosterVariantViewController noteUserTapOccured]
- -[PBUIPosterVariantViewController snapshotIfNeeded:]
- -[PBUIPosterVariantViewController snapshotIfNeeded:].cold.1
- -[PBUIPosterVariantViewController snapshotIfNeeded:].cold.2
- -[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]
- GCC_except_table107
- GCC_except_table114
- GCC_except_table119
- GCC_except_table124
- GCC_except_table126
- GCC_except_table128
- GCC_except_table130
- GCC_except_table133
- GCC_except_table138
- GCC_except_table139
- GCC_except_table141
- GCC_except_table142
- GCC_except_table144
- GCC_except_table148
- GCC_except_table150
- GCC_except_table41
- GCC_except_table45
- GCC_except_table49
- GCC_except_table51
- GCC_except_table55
- GCC_except_table57
- GCC_except_table63
- GCC_except_table65
- GCC_except_table69
- _OBJC_IVAR_$_PBUIPosterHUDController._containerView
- _OBJC_IVAR_$_PBUIPosterHUDController._posterActiveLabel
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PUIColorStatisticsDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_PUIColorStatisticsDelegate
- __OBJC_$_PROTOCOL_REFS_PUIColorStatisticsDelegate
- __OBJC_LABEL_PROTOCOL_$_PUIColorStatisticsDelegate
- __OBJC_PROTOCOL_$_PUIColorStatisticsDelegate
- ___52-[PBUIPosterVariantViewController snapshotIfNeeded:]_block_invoke
- ___52-[PBUIPosterVariantViewController snapshotIfNeeded:]_block_invoke.90
- ___52-[PBUIPosterVariantViewController snapshotIfNeeded:]_block_invoke_2
- ___52-[PBUIPosterVariantViewController snapshotIfNeeded:]_block_invoke_2.91
- ___52-[PBUIPosterVariantViewController snapshotIfNeeded:]_block_invoke_3
- ___64-[PBUIPosterVariantViewController fetchWallpaperProminentColor:]_block_invoke.56
- ___64-[PBUIPosterVariantViewController fetchWallpaperProminentColor:]_block_invoke.56.cold.1
- ___75-[PBUIPosterVariantViewController performSnapshotOnQueue:scene:completion:]_block_invoke_3
- ___87-[PBUIPosterVariantViewController _updatePosterAverageColor:desiredLegibilitySettings:]_block_invoke
- ___92-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]_block_invoke
- ___92-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]_block_invoke_2
- ___92-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]_block_invoke_3
- ___92-[PBUIPosterWallpaperRemoteViewController _legibilityUpdatedWithDictionary:notifyObservers:]_block_invoke_4
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32bs_e33_v16?0"PUIPosterSnapshotBundle"8ls32l8
- ___block_descriptor_40_e8_32s_e40_v16?0"PBUISnapshotPreconditionResult"8ls32l8
- ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_literal_global.500
- ___block_literal_global.792
- ___block_literal_global.93
- ___block_literal_global.95
- ___block_literal_global.97
- ___getPUIAverageColorFromColorBoxesSymbolLoc_block_invoke
- ___getPUICalculateContrastFromColorBoxesSymbolLoc_block_invoke
- ___getPUIColorBoxesClass_block_invoke
- ___getPUIColorBoxesClass_block_invoke.cold.1
- _getPUIAverageColorFromColorBoxesSymbolLoc
- _getPUIAverageColorFromColorBoxesSymbolLoc.ptr
- _getPUICalculateContrastFromColorBoxesSymbolLoc
- _getPUICalculateContrastFromColorBoxesSymbolLoc.ptr
- _getPUIColorBoxesClass
- _getPUIColorBoxesClass.softClass
- _objc_msgSend$_updatePosterAverageColor:desiredLegibilitySettings:
- _objc_msgSend$addFailureBlock:scheduler:
- _objc_msgSend$addSuccessBlock:scheduler:
- _objc_msgSend$initWithDelegate:
- _objc_msgSend$initWithOutputDescriptor:sceneDescriptor:attachments:analysis:
- _objc_msgSend$noteUserTapOccured
- _objc_msgSend$pr_averageColorDidChange
- _objc_msgSend$pui_executeSnapshotForDescriptor:
- _objc_msgSend$snapshotIfNeeded:
- _objc_msgSend$updateWithAverageColor:contrast:
- _soft_PUIAverageColorFromColorBoxes
- _soft_PUIAverageColorFromColorBoxes.cold.1
- _soft_PUICalculateContrastFromColorBoxes
- _soft_PUICalculateContrastFromColorBoxes.cold.1
CStrings:
+ "(snapshot now) "
+ "@\"<PLKLegibilityEnvironmentContext>\""
+ "@\"<PLKLegibilityEnvironmentContext>\"16@0:8"
+ "@\"<PLKLegibilityEnvironmentContext>\"24@0:8q16"
+ "@\"NSAttributedString\""
+ "@\"PLKColorBoxes\""
+ "@\"UIColor\"48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "A\xf0a"
+ "CGFloat soft_PLKCalculateContrastFromColorBoxes(PLKColorBoxes *__strong, CGRect, CGFloat *, CGFloat *)"
+ "Class getPLKColorBoxesClass(void)_block_invoke"
+ "Class getPLKLegibilityEnvironmentVariantContextClass(void)_block_invoke"
+ "Class getPUIPosterSnapshotHostConfigurationDescriptorClass(void)_block_invoke"
+ "Jul 16 2025 21:39:12"
+ "PFPosterRoleLockScreen"
+ "PLKAverageColorFromColorBoxes"
+ "PLKCalculateContrastFromColorBoxes"
+ "PLKColorBoxes"
+ "PLKLegibilityEnvironmentVariantContext"
+ "PLKLegibilityStyle soft_PLKLegibilityStyleForUILegibilityStyle(_UILegibilityStyle)"
+ "PLKLegibilityStyleForUILegibilityStyle"
+ "PUIColorStatisticsObserver"
+ "PUIPosterSnapshotHostConfigurationDescriptor"
+ "T@\"<PLKLegibilityEnvironmentContext>\",R,N"
+ "T@\"BSUIOrientationTransformWrapperView\",&,N,V_orientationWrapperView"
+ "T@\"NSAttributedString\",&,N,V_homeColumnContent"
+ "T@\"NSAttributedString\",&,N,V_lockColumnContent"
+ "T@\"NSAttributedString\",&,N,V_posterStatusContent"
+ "T@\"PLKColorBoxes\",&,N"
+ "T@\"UILabel\",&,N,V_homeColumnLabel"
+ "T@\"UILabel\",&,N,V_lockColumnLabel"
+ "T@\"UILabel\",&,N,V_posterStatusLabel"
+ "T@\"UIView\",&,N,V_hudContainerView"
+ "UIColor *soft_PLKAverageColorFromColorBoxes(PLKColorBoxes *__strong, CGRect, CGFloat)"
+ "Updating legibility environment; home updated? %{BOOL}u lockUpdated? %{BOOL}u"
+ "[%{public}@] ABORT Snapshot for now; already snapshotting right now."
+ "[%{public}@] Executing immediate snapshot for reason: %{public}@"
+ "[%{public}@] Poster Extact %lu did change content"
+ "[%{public}@] Snapshot already %@, not scheduling for reason: %{public}@"
+ "[%{public}@] Snapshot completed IN FAILURE in %f seconds."
+ "[%{public}@] Snapshot completed SUCCESSFULLY in %f seconds."
+ "[%{public}@] Snapshot inprogress, not scheduling for reason: %{public}@"
+ "[%{public}@] Snapshotting in progress; bailing on snapshot"
+ "_createAttachmentForImage:"
+ "_createLabelWithAlignment:"
+ "_createThumbnailFromImage:"
+ "_generateColumnContentForVariant:snapshot:snapshotDate:legibilityEnvironment:legibilityDate:"
+ "_generateHUDContents"
+ "_generatePosterStatusContent"
+ "_homeColumnContent"
+ "_homeColumnLabel"
+ "_homeLastLegibilityEnvironment"
+ "_homeLastSnapshot"
+ "_homeLastSnapshotUpdateDate"
+ "_homeLegibilityEnvironmentLastUpdateDate"
+ "_hudContainerView"
+ "_isSnapshotting"
+ "_legibilityEnvironmentContext"
+ "_legibilityUpdatedForVariants:notifyObservers:"
+ "_lockColumnContent"
+ "_lockColumnLabel"
+ "_lockLastLegibilityEnvironment"
+ "_lockLastSnapshot"
+ "_lockLastSnapshotUpdateDate"
+ "_lockLegibilityEnvironmentLastUpdateDate"
+ "_orientationWrapperView"
+ "_posterStatusContent"
+ "_posterStatusLabel"
+ "_posterStatusString"
+ "_setupAndShowHUDWindow"
+ "_updateHUDLayout"
+ "_updatePosterColorStatistics:desiredLegibilitySettings:"
+ "addColorStatisticsObserver:"
+ "addCompletionBlock:scheduler:"
+ "attributedStringWithAttachment:"
+ "auth token for sb snapshot is invalid"
+ "averageColorInRect:"
+ "averageSaturation"
+ "colorBoxesForAverageColor:"
+ "com.apple.posterkit.RolesForInprocessSnapshotOnly"
+ "copyWithWaitUntilReady:"
+ "destinationWithTemporaryDirectoryWithAuditToken:error:"
+ "drawInRect:"
+ "homeColumnContent"
+ "homeColumnLabel"
+ "hudContainerView"
+ "in progress"
+ "initWithColorBoxes:"
+ "initWithOutputDescriptor:sceneDescriptor:attachments:analysis:host:"
+ "initWithVariant:style:averageColor:contrast:saturation:legibilitySettings:"
+ "initWithVariant:style:colorBoxes:legibilitySettings:"
+ "isInvalid"
+ "legibilityEnvironmentContext"
+ "lockColumnContent"
+ "lockColumnLabel"
+ "lumaInRect:"
+ "orangeColor"
+ "orientationWrapperView"
+ "output destination for sb snapshot could not be created"
+ "posterStatusContent"
+ "posterStatusLabel"
+ "pui_executeSnapshotForDescriptor:outputDestination:"
+ "pui_significantEventsCounterDidChange"
+ "saturationInRect:"
+ "saturationInRect:forVariant:"
+ "scheduled"
+ "setAdjustsFontSizeToFitWidth:"
+ "setHomeColumnContent:"
+ "setHomeColumnLabel:"
+ "setHudContainerView:"
+ "setLockColumnContent:"
+ "setLockColumnLabel:"
+ "setOrientationWrapperView:"
+ "setPosterStatusContent:"
+ "setPosterStatusLabel:"
+ "setTextAlignment:"
+ "setTextColor:"
+ "snapshotIfNeeded:reason:"
+ "snapshotInProcessHostConfigurationDescriptorWithWorkQueue:"
+ "snapshotOutOfProcessHostConfigurationDescriptor"
+ "tokenFromAuditToken:"
+ "typeof (((typeof (PFPosterRoleLockScreen) (*)(void))0)()) getPFPosterRoleLockScreen(void)"
+ "updateVariant:lastSnapshotImage:legibilityEnvironmentContext:"
+ "updateWithContext:"
+ "updateWithContext:variants:"
+ "v24@?0@\"PUIPosterSnapshotBundle\"8@\"NSError\"16"
+ "v28@0:8B16@20"
+ "valueForEntitlement:"
+ "\x91"
+ "\x94"
- "@\"PUIColorBoxes\""
- "A\xf0A"
- "CGFloat soft_PUICalculateContrastFromColorBoxes(PUIColorBoxes *__strong, CGRect, CGFloat *, CGFloat *)"
- "Class getPUIColorBoxesClass(void)_block_invoke"
- "Jul  3 2025 21:22:12"
- "PUIAverageColorFromColorBoxes"
- "PUICalculateContrastFromColorBoxes"
- "PUIColorBoxes"
- "PUIColorStatisticsDelegate"
- "T@\"BSUIOrientationTransformWrapperView\",&,N,V_containerView"
- "T@\"PUIColorBoxes\",&,N"
- "T@\"UILabel\",&,N,V_posterActiveLabel"
- "UIColor *soft_PUIAverageColorFromColorBoxes(PUIColorBoxes *__strong, CGRect, CGFloat)"
- "[%{public}@] Snapshot scheduled for (now) %{public}@ for reason %{public}@"
- "_posterActiveLabel"
- "_updatePosterAverageColor:desiredLegibilitySettings:"
- "addFailureBlock:scheduler:"
- "addSuccessBlock:scheduler:"
- "containerView"
- "initWithDelegate:"
- "initWithOutputDescriptor:sceneDescriptor:attachments:analysis:"
- "noteUserTapOccured"
- "posterActiveLabel"
- "pr_averageColorDidChange"
- "pui_executeSnapshotForDescriptor:"
- "setContainerView:"
- "setPosterActiveLabel:"
- "setupAndShowHUDWindow"
- "snapshotIfNeeded:"
- "updateWithAverageColor:contrast:"
- "user tap occured"
- "v16@?0@\"NSError\"8"
- "v16@?0@\"PUIPosterSnapshotBundle\"8"
- "\x81"
- "\x84"

```
