## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-283.101.0.0.0
-  __TEXT.__text: 0x8d6d8
-  __TEXT.__auth_stubs: 0x1cc0
-  __TEXT.__objc_methlist: 0xa314
+286.101.0.0.0
+  __TEXT.__text: 0x8d1dc
+  __TEXT.__auth_stubs: 0x1c30
+  __TEXT.__objc_methlist: 0xa3e4
   __TEXT.__const: 0xab4
-  __TEXT.__oslogstring: 0x3511
-  __TEXT.__cstring: 0x5d02
-  __TEXT.__gcc_except_tab: 0x1524
+  __TEXT.__oslogstring: 0x3471
+  __TEXT.__cstring: 0x5c52
+  __TEXT.__gcc_except_tab: 0x166c
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__swift5_typeref: 0x502
   __TEXT.__constg_swiftt: 0x1d4

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x2640
-  __TEXT.__objc_classname: 0x1728
-  __TEXT.__objc_methname: 0x18365
-  __TEXT.__objc_methtype: 0x3f4e
-  __TEXT.__objc_stubs: 0x10b80
-  __DATA_CONST.__got: 0xe38
-  __DATA_CONST.__const: 0x24e0
+  __TEXT.__unwind_info: 0x2648
+  __TEXT.__objc_classname: 0x174a
+  __TEXT.__objc_methname: 0x18571
+  __TEXT.__objc_methtype: 0x3f66
+  __TEXT.__objc_stubs: 0x10c60
+  __DATA_CONST.__got: 0xe40
+  __DATA_CONST.__const: 0x2558
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5470
+  __DATA_CONST.__objc_selrefs: 0x54f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__auth_got: 0xe70
+  __AUTH_CONST.__auth_got: 0xe28
   __AUTH_CONST.__const: 0xf80
-  __AUTH_CONST.__cfstring: 0x6740
-  __AUTH_CONST.__objc_const: 0x1df50
+  __AUTH_CONST.__cfstring: 0x6620
+  __AUTH_CONST.__objc_const: 0x1dec0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0x318
+  __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0x22d0
+  __AUTH.__objc_data: 0x2320
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0xb74
+  __DATA.__objc_ivar: 0xb64
   __DATA.__data: 0x1720
   __DATA.__bss: 0x7e0
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0xc30
+  __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit
   - /System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation
   - /System/Library/PrivateFrameworks/PosterFuturesKit.framework/PosterFuturesKit
+  - /System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1C60126E-33A7-3227-919E-F8A79AA061D1
-  Functions: 3835
-  Symbols:   13790
-  CStrings:  6667
+  UUID: 0C4F4854-1D4A-3BC4-87AC-FBF18C5C9246
+  Functions: 3846
+  Symbols:   13799
+  CStrings:  6658
 
Symbols:
+ +[PUIPosterSnapshotDestination destinationForSQLiteCacheAtURL:clientAuditToken:error:]
+ +[PUIPosterSnapshotHostConfigurationDescriptor snapshotInProcessHostConfigurationDescriptorWithWorkQueue:]
+ +[PUIPosterSnapshotHostConfigurationDescriptor snapshotOutOfProcessHostConfigurationDescriptor]
+ +[PUIPosterSnapshotHostConfigurationDescriptor supportsBSXPCSecureCoding]
+ +[PUIPosterSnapshotHostConfigurationDescriptor supportsSecureCoding]
+ -[FBSSceneSettingsDiff(PosterUIFoundation) pui_significantEventsCounterDidChange]
+ -[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:].cold.1
+ -[PUIColorStatistics _lock_initializeWithColorBoxes:]
+ -[PUIColorStatistics _notifyObserversDidUpdate]
+ -[PUIColorStatistics addColorStatisticsObserver:]
+ -[PUIColorStatistics averageColorInRect:]
+ -[PUIColorStatistics averageSaturation]
+ -[PUIColorStatistics colorBoxes]
+ -[PUIColorStatistics contrastInRect:]
+ -[PUIColorStatistics initWithColorBoxes:]
+ -[PUIColorStatistics lumaInRect:]
+ -[PUIColorStatistics removeColorStatisticsObserver:]
+ -[PUIColorStatistics saturationInRect:]
+ -[PUIColorStatistics updateWithColorBoxes:].cold.1
+ -[PUIPosterSnapshotDescriptor hostDescriptor]
+ -[PUIPosterSnapshotDescriptor initWithOutputDescriptor:sceneDescriptor:attachments:analysis:host:]
+ -[PUIPosterSnapshotDescriptor initWithOutputDescriptor:sceneDescriptor:attachments:analysis:host:].cold.1
+ -[PUIPosterSnapshotHostConfigurationDescriptor .cxx_destruct]
+ -[PUIPosterSnapshotHostConfigurationDescriptor copyWithHostWorkQueue:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor copyWithHostWorkQueue:].cold.1
+ -[PUIPosterSnapshotHostConfigurationDescriptor copyWithWaitUntilReady:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor copyWithZone:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor description]
+ -[PUIPosterSnapshotHostConfigurationDescriptor encodeWithBSXPCCoder:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor encodeWithCoder:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor hash]
+ -[PUIPosterSnapshotHostConfigurationDescriptor hostWorkQueue]
+ -[PUIPosterSnapshotHostConfigurationDescriptor inProcessSnapshot]
+ -[PUIPosterSnapshotHostConfigurationDescriptor initWithBSXPCCoder:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor initWithCoder:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor initWithHostWorkQueue:waitUntilReady:inProcessSnapshot:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor isEqual:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor isEqualToHostConfigurationDescriptor:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor waitUntilReady]
+ -[UIImage(PosterUIFoundation) pui_imageHasNoContent]
+ -[_PUIPosterSnapshotCapture _attemptSnapshot:].cold.4
+ GCC_except_table27
+ GCC_except_table31
+ GCC_except_table46
+ _OBJC_CLASS_$_PLKColorBoxes
+ _OBJC_CLASS_$_PUIPosterSnapshotHostConfigurationDescriptor
+ _OBJC_IVAR_$_PUIColorStatistics._lock_averageColor
+ _OBJC_IVAR_$_PUIColorStatistics._lock_averageContrast
+ _OBJC_IVAR_$_PUIColorStatistics._lock_averageSaturation
+ _OBJC_IVAR_$_PUIColorStatistics._lock_colorBoxes
+ _OBJC_IVAR_$_PUIColorStatistics._lock_legibilityProvider
+ _OBJC_IVAR_$_PUIColorStatistics._lock_observers
+ _OBJC_IVAR_$_PUIPosterSnapshotDescriptor._hostDescriptor
+ _OBJC_IVAR_$_PUIPosterSnapshotHostConfigurationDescriptor._hostWorkQueue
+ _OBJC_IVAR_$_PUIPosterSnapshotHostConfigurationDescriptor._inProcessSnapshot
+ _OBJC_IVAR_$_PUIPosterSnapshotHostConfigurationDescriptor._waitUntilReady
+ _OBJC_METACLASS_$_PUIPosterSnapshotHostConfigurationDescriptor
+ __OBJC_$_CLASS_METHODS_PUIPosterSnapshotHostConfigurationDescriptor
+ __OBJC_$_CLASS_PROP_LIST_PUIPosterSnapshotHostConfigurationDescriptor
+ __OBJC_$_INSTANCE_METHODS_PUIPosterSnapshotHostConfigurationDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_PUIPosterSnapshotHostConfigurationDescriptor
+ __OBJC_$_PROP_LIST_PUIPosterSnapshotHostConfigurationDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_PUIPosterSnapshotHostConfigurationDescriptor
+ __OBJC_CLASS_RO_$_PUIPosterSnapshotHostConfigurationDescriptor
+ __OBJC_METACLASS_RO_$_PUIPosterSnapshotHostConfigurationDescriptor
+ ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.116
+ ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.116.cold.1
+ ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_10
+ ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_11
+ ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_4
+ ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_5
+ ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_6
+ ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_7
+ ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_8
+ ___82-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:]_block_invoke_9
+ ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke.97
+ ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke_2.103
+ ___block_descriptor_40_e8_32s_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8r40l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8r72l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e5_v8?0lr64l8s32l8s40l8r72l8s48l8r80l8s56l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72r80r_e17_v16?0"NSError"8ls32l8s40l8r72l8s48l8s56l8s64l8r80l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8r72l8s40l8s48l8s56l8s64l8r80l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80s88r_e5_v8?0ls32l8s40l8r88l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.103
+ ___block_literal_global.132
+ ___block_literal_global.42
+ ___block_literal_global.54
+ ___block_literal_global.57
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$addCompletionBlock:
+ _objc_msgSend$addCompletionBlock:scheduler:
+ _objc_msgSend$averageColorInRect:
+ _objc_msgSend$averageSaturation
+ _objc_msgSend$colorBoxesForAverageColor:contrast:
+ _objc_msgSend$contrastInRect:
+ _objc_msgSend$hostDescriptor
+ _objc_msgSend$hostWorkQueue
+ _objc_msgSend$inProcessSnapshot
+ _objc_msgSend$initWithColorBoxes:
+ _objc_msgSend$initWithOutputDescriptor:sceneDescriptor:attachments:analysis:host:
+ _objc_msgSend$isEqualToColorBoxes:
+ _objc_msgSend$isEqualToHostConfigurationDescriptor:
+ _objc_msgSend$lumaInRect:
+ _objc_msgSend$pf_markPurgableInOneHourWithError:
+ _objc_msgSend$pui_averageColor
+ _objc_msgSend$pui_safelySendActions:outError:
+ _objc_msgSend$saturationInRect:
+ _objc_msgSend$setClass:forClassName:
+ _objc_msgSend$snapshotOutOfProcessHostConfigurationDescriptor
+ _objc_msgSend$waitUntilReady
+ _pui_executeSnapshotForDescriptor:outputDestination:.fallbackQueue
+ _pui_executeSnapshotForDescriptor:outputDestination:.onceToken
- +[PUIColorBoxes colorBoxesForImage:]
- +[PUIColorBoxes colorBoxesForImage:].cold.1
- +[PUIColorBoxes colorBoxesForImage:].cold.2
- +[PUIColorBoxes colorBoxesForImage:].cold.3
- +[PUIColorBoxes colorBoxesForImage:].cold.4
- +[PUIColorBoxes colorBoxesForImage:].cold.5
- +[PUIColorBoxes supportsSecureCoding]
- -[FBScene(PosterUIFoundation) pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:]
- -[FBScene(PosterUIFoundation) pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:].cold.1
- -[PUIColorBoxes colorBoxAtRow:col:]
- -[PUIColorBoxes colorBoxesRowMajor]
- -[PUIColorBoxes columnCount]
- -[PUIColorBoxes contrast]
- -[PUIColorBoxes dealloc]
- -[PUIColorBoxes description]
- -[PUIColorBoxes downsampledBoxSize]
- -[PUIColorBoxes effectiveDownsampleFactor]
- -[PUIColorBoxes encodeWithCoder:]
- -[PUIColorBoxes imageSize]
- -[PUIColorBoxes initWithCoder:]
- -[PUIColorBoxes initWithColorBoxes:size:rowCount:columnCount:totalContrast8:imageSize:downsampledBoxSize:effectiveDownsampleFactor:pixelHeight:pixelWidth:]
- -[PUIColorBoxes pixelHeight]
- -[PUIColorBoxes pixelWidth]
- -[PUIColorBoxes rectForColorBoxAtRow:col:]
- -[PUIColorBoxes rowCount]
- -[PUIColorBoxes size]
- -[PUIColorBoxes totalContrast8]
- -[PUIColorStatistics delegate]
- -[PUIColorStatistics initWithDelegate:]
- -[PUIColorStatistics setDelegate:]
- -[PUIColorStatistics updateWithAverageColor:contrast:]
- -[PUIPosterSnapshotDescriptor initWithOutputDescriptor:sceneDescriptor:attachments:analysis:].cold.1
- -[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:]
- GCC_except_table26
- GCC_except_table40
- _CGBitmapContextGetData
- _CGBitmapGetAlignedBytesPerRow
- _CGContextDrawImage
- _CGContextSetInterpolationQuality
- _CGRectGetMinY
- _CGRectIntersectsRect
- _OBJC_CLASS_$_PUIColorBoxes
- _OBJC_IVAR_$_PUIColorBoxes._colorBoxesRowMajor
- _OBJC_IVAR_$_PUIColorBoxes._columnCount
- _OBJC_IVAR_$_PUIColorBoxes._downsampledBoxSize
- _OBJC_IVAR_$_PUIColorBoxes._effectiveDownsampleFactor
- _OBJC_IVAR_$_PUIColorBoxes._imageSize
- _OBJC_IVAR_$_PUIColorBoxes._pixelHeight
- _OBJC_IVAR_$_PUIColorBoxes._pixelWidth
- _OBJC_IVAR_$_PUIColorBoxes._rowCount
- _OBJC_IVAR_$_PUIColorBoxes._size
- _OBJC_IVAR_$_PUIColorBoxes._totalContrast8
- _OBJC_IVAR_$_PUIColorStatistics._averageColor
- _OBJC_IVAR_$_PUIColorStatistics._averageContrast
- _OBJC_IVAR_$_PUIColorStatistics._delegate
- _OBJC_IVAR_$_PUIColorStatistics._legibilityProvider
- _OBJC_METACLASS_$_PUIColorBoxes
- _PUIAverageColorFromColorBoxes
- _PUICalculateContrastFromColorBoxes
- __OBJC_$_CLASS_METHODS_PUIColorBoxes
- __OBJC_$_CLASS_PROP_LIST_PUIColorBoxes
- __OBJC_$_INSTANCE_METHODS_PUIColorBoxes
- __OBJC_$_INSTANCE_VARIABLES_PUIColorBoxes
- __OBJC_$_PROP_LIST_PUIColorBoxes
- __OBJC_CLASS_PROTOCOLS_$_PUIColorBoxes
- __OBJC_CLASS_RO_$_PUIColorBoxes
- __OBJC_METACLASS_RO_$_PUIColorBoxes
- ___107-[FBScene(PosterUIFoundation) pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:]_block_invoke
- ___107-[FBScene(PosterUIFoundation) pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:]_block_invoke_2
- ___107-[FBScene(PosterUIFoundation) pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:]_block_invoke_3
- ___107-[FBScene(PosterUIFoundation) pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:]_block_invoke_4
- ___107-[FBScene(PosterUIFoundation) pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:]_block_invoke_5
- ___107-[FBScene(PosterUIFoundation) pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:]_block_invoke_6
- ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.112
- ___60-[FBScene(PosterUIFoundation) pui_invalidateWithCompletion:]_block_invoke.112.cold.1
- ___86-[PUIPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:options:completion:]_block_invoke.105
- ___block_descriptor_48_e8_32s40bs_e55_v28?0B8"PUIPosterSnapshotBundleBuilder"12"NSError"20ls40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56bs_e17_v16?0"NSError"8ls56l8s32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_97_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.134
- ___block_literal_global.55
- ___block_literal_global.58
- ___block_literal_global.99
- _contrast
- _contrast.cold.1
- _malloc_type_calloc
- _malloc_type_malloc
- _memcpy
- _objc_msgSend$_luminance
- _objc_msgSend$_luminanceWithRed:green:blue:
- _objc_msgSend$accumulateChangesToContentColor:
- _objc_msgSend$appendPointer:withName:
- _objc_msgSend$cacheSnapshotBundle:forRequest:completion:
- _objc_msgSend$decodeBytesForKey:returnedLength:
- _objc_msgSend$decodeIntForKey:
- _objc_msgSend$encodeBytes:length:forKey:
- _objc_msgSend$encodeInt:forKey:
- _objc_msgSend$initWithAverageColor:contrast:
- _objc_msgSend$initWithDelegate:
- _objc_msgSend$latestSnapshotBundleMatchingPredicate:
- _objc_msgSend$predicateMatchingContext:
- _objc_msgSend$resetWithColor:
- _objc_msgSend$updateWithAverageColor:contrast:
- _pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:.fallbackQueue
- _pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:.onceToken
CStrings:
+ "(%p) host descriptor says skip readiness checks... capturing..."
+ "<%@: %p; color: %@; contrast: %.2f; saturation: %.2f>"
+ "@\"PLKColorBoxes\""
+ "@\"PUIPosterSnapshotHostConfigurationDescriptor\""
+ "PUI-SnapshotTemp"
+ "PUIPosterSnapshotHostConfigurationDescriptor"
+ "Snapshot"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_hostWorkQueue"
+ "T@\"PLKColorBoxes\",R,D,N"
+ "T@\"PUIPosterSnapshotHostConfigurationDescriptor\",R,N,V_hostDescriptor"
+ "TB,R,N,V_inProcessSnapshot"
+ "TB,R,N,V_waitUntilReady"
+ "URLByAppendingPathExtension:"
+ "_hostDescriptor"
+ "_hostWorkQueue"
+ "_inProcessSnapshot"
+ "_lock_averageColor"
+ "_lock_averageContrast"
+ "_lock_averageSaturation"
+ "_lock_colorBoxes"
+ "_lock_legibilityProvider"
+ "_lock_observers"
+ "_waitUntilReady"
+ "addColorStatisticsObserver:"
+ "addCompletionBlock:"
+ "addCompletionBlock:scheduler:"
+ "averageColorInRect:"
+ "averageSaturation"
+ "builder could not build snapshot bundle"
+ "colorBoxes"
+ "colorBoxesForAverageColor:contrast:"
+ "contrastInRect:"
+ "copyWithHostWorkQueue:"
+ "copyWithWaitUntilReady:"
+ "d48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "destinationForSQLiteCacheAtURL:clientAuditToken:error:"
+ "hostDescriptor"
+ "hostWorkQueue"
+ "inProcessSnapshot"
+ "initWithColorBoxes:"
+ "initWithOutputDescriptor:sceneDescriptor:attachments:analysis:host:"
+ "isEqualToColorBoxes:"
+ "isEqualToHostConfigurationDescriptor:"
+ "lumaInRect:"
+ "pf_markPurgableInOneHourWithError:"
+ "pui_imageHasNoContent"
+ "pui_significantEventsCounterDidChange"
+ "removeColorStatisticsObserver:"
+ "saturationInRect:"
+ "setClass:forClassName:"
+ "snapshotInProcessHostConfigurationDescriptorWithWorkQueue:"
+ "snapshotOutOfProcessHostConfigurationDescriptor"
+ "v48@0:8@16@24@32@?40"
+ "waitUntilReady"
- "(unknown)"
- "0 <= lx && lx <= 255"
- "<%@: %p; color: %@; contrast: %.2f>"
- "@\"<PUIColorStatisticsDelegate>\""
- "B40@0:8@16@24@?32"
- "B48@0:8@16@24@32@?40"
- "Bad box index '%lu' from row %lu column %lu and column count %lu"
- "Bundle failed to be cached %@"
- "Color boxes"
- "Columns"
- "Contrast"
- "Detected overflow trying to multiply row count %lu with column count %lu"
- "Failed to allocate color box buffer with row count %lu column count %lu"
- "NON-SOOP SNAPSHOTTING %@"
- "PUIColorBoxes.m"
- "Rows"
- "Scene is not ready to snapshot."
- "Size"
- "T@\"<PUIColorStatisticsDelegate>\",W,N,V_delegate"
- "T@\"UIColor\",R,N,V_averageColor"
- "Td,R,N,V_averageContrast"
- "^{?=CCCC}"
- "_averageContrast"
- "_colorBoxesRowMajor"
- "_columnCount"
- "_downsampledBoxSize"
- "_effectiveDownsampleFactor"
- "_imageSize"
- "_legibilityProvider"
- "_luminanceWithRed:green:blue:"
- "_pixelHeight"
- "_pixelWidth"
- "_rowCount"
- "_size"
- "_totalContrast8"
- "accumulateChangesToContentColor:"
- "appendPointer:withName:"
- "cacheSnapshotBundle:forRequest:"
- "colorBoxesRowMajor"
- "columnCount"
- "decodeBytesForKey:returnedLength:"
- "decodeIntForKey:"
- "downsampledBoxSize"
- "effectiveDownsampleFactor"
- "encodeBytes:length:forKey:"
- "encodeInt:forKey:"
- "imageSize"
- "initWithAverageColor:"
- "initWithAverageColor:contrast:"
- "pixelHeight"
- "pixelWidth"
- "pui_executeSnapshotForLevelSets:determineColorStatistics:onQueue:completion:"
- "reason"
- "round_to_uint8"
- "rowCount"
- "totalContrast8"
- "updateWithAverageColor:contrast:"
- "v28@?0B8@\"PUIPosterSnapshotBundleBuilder\"12@\"NSError\"20"
- "v44@0:8@16B24@28@?36"

```
