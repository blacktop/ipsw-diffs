## PhotosFaceLayout

> `/System/Library/PrivateFrameworks/PhotosFaceLayout.framework/PhotosFaceLayout`

```diff

-95.1.0.0.0
-  __TEXT.__text: 0x7104
-  __TEXT.__auth_stubs: 0x6d0
+96.0.0.0.0
+  __TEXT.__text: 0x6cd8
   __TEXT.__objc_methlist: 0x47c
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x3c4
-  __TEXT.__gcc_except_tab: 0x188
+  __TEXT.__cstring: 0x3d2
+  __TEXT.__gcc_except_tab: 0x118
   __TEXT.__oslogstring: 0xa50
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_classname: 0xee
-  __TEXT.__objc_methname: 0x139b
-  __TEXT.__objc_methtype: 0x4a6
-  __TEXT.__objc_stubs: 0x10a0
-  __DATA_CONST.__got: 0x1f8
+  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_selrefs: 0x560
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x1f8
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0xc80
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x230
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x94
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5B88ACB9-16C9-33D3-9ECD-CA52F6DDE7EB
-  Functions: 134
-  Symbols:   720
-  CStrings:  418
+  UUID: 46EC8FAE-AD99-3966-9688-E63610C11CAA
+  Functions: 132
+  Symbols:   717
+  CStrings:  112
 
Symbols:
+ ___80-[PFLSegmentationCalculator queue_bestSegmentationForAsset:timePositions:error:]_block_invoke.340
+ ___80-[PFLSegmentationCalculator queue_bestSegmentationForAsset:timePositions:error:]_block_invoke.340.cold.1
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x9
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- ___80-[PFLSegmentationCalculator queue_bestSegmentationForAsset:timePositions:error:]_block_invoke.320
- ___80-[PFLSegmentationCalculator queue_bestSegmentationForAsset:timePositions:error:]_block_invoke.320.cold.1
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x10
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSArray\"88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@\"PFParallaxLayoutConfiguration\"48@\"<PFParallaxAssetRegions>\"56@\"CIImage\"64Q72^@80"
- "@\"NSData\""
- "@\"NSLock\""
- "@\"NSMapTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"PFLCLayout\""
- "@\"PFLJetsamInfoFetcher\""
- "@\"PIParallaxColorAnalysis\""
- "@\"PISegmentationData\""
- "@\"UTType\""
- "@100@0:8{CGSize=dd}16{CGRect={CGPoint=dd}{CGSize=dd}}32@64I72@76{CGSize=dd}84"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16Q24@32@40"
- "@64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16d48d56"
- "@88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56@64Q72^@80"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^{jetsam_info=qqq}16"
- "B32@0:8@16^{jetsam_info=qqq}24"
- "I"
- "I16@0:8"
- "NSObject"
- "PFLImageDataScaler"
- "PFLJetsamInfoFetcher"
- "PFLJetsamInfoInterval"
- "PFLLayoutConfiguration"
- "PFLLayoutProvider"
- "PFLSegmentationCalculator"
- "PIPosterLayoutProvider"
- "PhotosFaceLayout"
- "PhotosFaceLayoutProvider"
- "Q16@0:8"
- "T#,R"
- "T@\"NSArray\",R,N,V_faceRects"
- "T@\"NSArray\",R,N,V_petRects"
- "T@\"NSData\",R,N,V_data"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_assetId"
- "T@\"NSString\",R,N,V_label"
- "T@\"PFLCLayout\",R,N,V_watchLayout"
- "T@\"PIParallaxColorAnalysis\",R,N,V_colorAnalysis"
- "T@\"UTType\",R,N,V_type"
- "TB,R,N,V_maskIsInverted"
- "TB,R,N,V_resultsAreValid"
- "TB,R,N,V_usesMask"
- "TI,R,N,V_orientation"
- "TQ,R"
- "TQ,R,N,V_timePosition"
- "T^{__CVBuffer=},R,N,V_foregroundMask"
- "Td,R,N,V_cropScore"
- "Td,R,N,V_layoutScore"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_acceptableCropRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_inputCrop"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_preferredCropRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_timeRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_timeRectInAsset"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_visibleRect"
- "T{CGSize=dd},R,N,V_assetSize"
- "T{CGSize=dd},R,N,V_inputSize"
- "T{CGSize=dd},R,N,V_outputSize"
- "T{jetsam_info=qqq},R,N"
- "T{jetsam_info=qqq},R,N,V_startInfo"
- "URLByAppendingPathComponent:isDirectory:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CVBuffer=}"
- "^{__CVBuffer=}16@0:8"
- "_PFLSharedJetsamInfo"
- "_acceptableCropRect"
- "_assetId"
- "_assetSize"
- "_colorAnalysis"
- "_compressionQuality"
- "_cropScore"
- "_data"
- "_faceRects"
- "_fetcher"
- "_fetchers"
- "_fetchersLock"
- "_foregroundMask"
- "_inputCrop"
- "_inputSize"
- "_label"
- "_layoutScore"
- "_maskIsInverted"
- "_orientation"
- "_outputData"
- "_outputSize"
- "_petRects"
- "_pid"
- "_preferredCropRect"
- "_queue_segmentationForAsset:timePosition:completion:"
- "_resultsAreValid"
- "_segmentationData"
- "_segmentationQueue"
- "_segmentationQueueSema"
- "_startInfo"
- "_timePosition"
- "_timeRect"
- "_timeRectInAsset"
- "_type"
- "_usesMask"
- "_visibleRect"
- "_watchLayout"
- "_workQueue"
- "acceptableCropRect"
- "addFetchPropertySets:"
- "addObject:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assetId"
- "assetSize"
- "autorelease"
- "bestSegmentationForAsset:completion:"
- "bestSegmentationForAsset:timePosition:completion:"
- "boolValue"
- "class"
- "classification"
- "colorAnalysis"
- "conformsToProtocol:"
- "containsObject:"
- "context"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createCGImage:fromRect:"
- "createCGImage:fromRect:format:colorSpace:"
- "createDirectoryIfNeededAtPath:error:"
- "creationDate"
- "cropAndScaleWithCompletion:"
- "cropScore"
- "currentInfo"
- "d"
- "d16@0:8"
- "data"
- "dataWithLength:"
- "dealloc"
- "debugDescription"
- "defaultManager"
- "description"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "distantPast"
- "ensureResources"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "extent"
- "faceRects"
- "faceRegions"
- "fetchAssetsWithUUIDs:options:"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "filterWithName:"
- "firstObject"
- "floatValue"
- "foregroundMask"
- "freeResources"
- "generateOrientedLayoutsForFullExtent:layoutConfiguration:layoutRegions:segmentationMatteImage:segmentationClassification:error:"
- "getInfo:"
- "getInfoFor:into:"
- "hash"
- "identifier"
- "imageWithCVPixelBuffer:"
- "init"
- "initWithAsset:timePosition:segmentationData:coreLayout:"
- "initWithCropScore:layoutScore:foregroundCoverage:visibleRect:usesMask:"
- "initWithLabel:"
- "initWithPhotoAsset:"
- "initWithPortraitConfiguration:landscapeConfiguration:"
- "initWithScreenSize:timeRect:inactiveTimeRect:parallaxPadding:"
- "initWithSize:crop:data:orientation:type:outputSize:"
- "initWithTimePosition:"
- "initWithVisibleRect:cropScore:layoutScore:"
- "initWithVisibleRect:inactiveRect:zoomStrategy:overlapStrategy:parallaxStrategy:inactiveStrategy:headroomStrategy:cropScore:layoutScore:timeBottomOverlap:timeTopOverlap:unsafeAreaOverlap:uninflatedUnsafeAreaOverlap:hasTopEdgeContact:"
- "inputCrop"
- "inputSize"
- "intValue"
- "invalidateResults"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "keyEnumerator"
- "label"
- "layoutScore"
- "length"
- "loadSegmentationDataForAsset:options:completion:"
- "localIdentifier"
- "lock"
- "logCurrentInterval"
- "longLongValue"
- "maskIsInverted"
- "modificationDate"
- "mutableBytes"
- "numberWithDouble:"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "orientation"
- "outputImage"
- "outputSize"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "petRects"
- "petRegions"
- "pfl_creationDate"
- "pfl_modificationDate"
- "pixelHeight"
- "pixelWidth"
- "preferredCropRect"
- "queue_bestSegmentationForAsset:timePositions:error:"
- "rectValue"
- "regions"
- "release"
- "removeObjectForKey:"
- "requestImageDataAndOrientationForAsset:options:resultHandler:"
- "reset"
- "resetInterval"
- "resetIntervalFor:"
- "respondsToSelector:"
- "resultsAreValid"
- "retain"
- "retainCount"
- "scores"
- "screenSize"
- "segmentationBuffer"
- "self"
- "setBackgroundZorder:"
- "setBaseImageName:"
- "setCreationDate:"
- "setDeliveryMode:"
- "setForegroundZorder:"
- "setImageAOTBrightness:"
- "setLayouts:"
- "setLocalIdentifier:"
- "setMaskImageName:"
- "setModificationDate:"
- "setNetworkAccessAllowed:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOriginalCrop:"
- "setParallaxScale:"
- "setPreferredLayout:"
- "setSynchronous:"
- "setTimeElementZorder:"
- "setTimePosition:"
- "setTimeRect:"
- "setUserEdited:"
- "setValue:forKey:"
- "setVersion:"
- "sharedInstance"
- "sharedJetsamInfo"
- "startInfo"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "timePosition"
- "timeRect"
- "timeRectInAsset"
- "type"
- "unlock"
- "unregister:"
- "usesMask"
- "uuidFromLocalIdentifier:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@?24"
- "v40@0:8@16Q24@?32"
- "valueWithBytes:objCType:"
- "visibleRect"
- "watchLayout"
- "weakToStrongObjectsMapTable"
- "writeToURL:options:error:"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{jetsam_info=\"currentKB\"q\"maxLifetimeKB\"q\"maxIntervalKB\"q}"
- "{jetsam_info=qqq}16@0:8"

```
