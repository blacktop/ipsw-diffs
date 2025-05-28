## mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

-200.8.1.0.0
-  __TEXT.__text: 0xedb74
-  __TEXT.__auth_stubs: 0x1230
-  __TEXT.__objc_stubs: 0xe220
+205.6.1.0.0
+  __TEXT.__text: 0xef47c
+  __TEXT.__auth_stubs: 0x1240
+  __TEXT.__objc_stubs: 0xe380
   __TEXT.__objc_methlist: 0x6448
-  __TEXT.__cstring: 0xaa81
-  __TEXT.__gcc_except_tab: 0x16d44
+  __TEXT.__cstring: 0xaa9a
+  __TEXT.__gcc_except_tab: 0x16efc
   __TEXT.__const: 0x228
-  __TEXT.__oslogstring: 0x13632
+  __TEXT.__oslogstring: 0x136a0
   __TEXT.__objc_classname: 0x159b
-  __TEXT.__objc_methname: 0x12563
+  __TEXT.__objc_methname: 0x12823
   __TEXT.__objc_methtype: 0x2ab2
-  __TEXT.__dlopen_cstrs: 0x49b
-  __TEXT.__unwind_info: 0x424c
+  __TEXT.__dlopen_cstrs: 0x501
+  __TEXT.__unwind_info: 0x4264
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x930
-  __DATA_CONST.__got: 0x6f0
-  __DATA_CONST.__const: 0x4290
+  __DATA_CONST.__auth_got: 0x938
+  __DATA_CONST.__got: 0x7b8
+  __DATA_CONST.__const: 0x42a8
   __DATA_CONST.__cfstring: 0x5cc0
   __DATA_CONST.__objc_classlist: 0x518
   __DATA_CONST.__objc_catlist: 0x48

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0xfa28
-  __DATA.__objc_selrefs: 0x3c40
+  __DATA.__objc_selrefs: 0x3c98
   __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0xa30
+  __DATA.__objc_classrefs: 0xa38
   __DATA.__objc_superrefs: 0x410
   __DATA.__objc_ivar: 0xd0c
   __DATA.__objc_data: 0x32f0
   __DATA.__data: 0x850
-  __DATA.__bss: 0x348
+  __DATA.__bss: 0x360
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2828
-  Symbols:   711
-  CStrings:  5871
+  Functions: 2839
+  Symbols:   738
+  CStrings:  5886
 
Symbols:
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMPerBatchDomainSpecificAssetCounts
+ _kVIDomainAlbum
+ _kVIDomainAnimals
+ _kVIDomainApparel
+ _kVIDomainArt
+ _kVIDomainAutoSymbol
+ _kVIDomainBarcodeDetection
+ _kVIDomainBirds
+ _kVIDomainBook
+ _kVIDomainBrandLogoSymbol
+ _kVIDomainCats
+ _kVIDomainDogs
+ _kVIDomainFood
+ _kVIDomainInsects
+ _kVIDomainLandmark
+ _kVIDomainLaundryCareSymbol
+ _kVIDomainMammals
+ _kVIDomainMedia
+ _kVIDomainNaturalLandmark
+ _kVIDomainNature
+ _kVIDomainObject2D
+ _kVIDomainReptiles
+ _kVIDomainSculpture
+ _kVIDomainSignSymbol
+ _kVIDomainSkyline
+ _kVIDomainStorefront
CStrings:
+ "  Reporting VUGallery metrics for library %@"
+ "%@ Marking asset contains FC face %@"
+ "%@ Marking resource is too small"
+ "MADReportVUGalleryMetric"
+ "Processing"
+ "analyzeAsset:withResource:resourceURL:isBestResource:quickMode:results:"
+ "domainInfo"
+ "domainKey"
+ "imageRegions"
+ "initWithParsedAssetCount:anyDomainAssetCount:artAssetCount:natureAssetCount:animalsAssetCount:birdsAssetCount:insectsAssetCount:reptilesAssetCount:mammalsAssetCount:landmarkAssetCount:naturalLandmarkAssetCount:mediaAssetCount:bookAssetCount:albumAssetCount:catsAssetCount:dogsAssetCount:apparelAssetCount:foodAssetCount:storefrontAssetCount:signSymbolAssetCount:laundryCareSymbolAssetCount:autoSymbolAssetCount:brandLogoSymbolAssetCount:object2DAssetCount:barcodeDetectionAssetCount:sculptureAssetCount:skylineAssetCount:"
+ "isBestResourceForFaceProcessing:fromResources:"
+ "reportMetrics"
+ "sendEvent:"
+ "visualUnderstanding"
- "%@ Forward-compatible face %@"
- "analyzeAsset:withResource:resourceURL:quickMode:results:"

```
