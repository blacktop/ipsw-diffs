## HealthUI

> `/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI`

```diff

-4146.1.11.3.0
-  __TEXT.__text: 0x343e9c
-  __TEXT.__auth_stubs: 0x4170
-  __TEXT.__objc_methlist: 0x2e9e0
+4146.2.12.1.3
+  __TEXT.__text: 0x344a44
+  __TEXT.__auth_stubs: 0x4180
+  __TEXT.__objc_methlist: 0x2e818
   __TEXT.__const: 0x45b4
-  __TEXT.__cstring: 0x1f007
-  __TEXT.__oslogstring: 0x46c3
+  __TEXT.__cstring: 0x1f017
+  __TEXT.__oslogstring: 0x46f2
   __TEXT.__ustring: 0x5a
   __TEXT.__gcc_except_tab: 0x1954
   __TEXT.__dlopen_cstrs: 0x411

   __TEXT.__swift5_types: 0x194
   __TEXT.__swift5_capture: 0x568
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__objc_const_ax: 0x3edc
-  __TEXT.__unwind_info: 0xd144
+  __TEXT.__objc_const_ax: 0x4104
+  __TEXT.__unwind_info: 0xd158
   __TEXT.__eh_frame: 0xdf0
   __TEXT.__objc_classname: 0x8718
-  __TEXT.__objc_methname: 0x75f6d
-  __TEXT.__objc_methtype: 0xf73d
-  __TEXT.__objc_stubs: 0x458c0
-  __DATA_CONST.__got: 0x17a8
-  __DATA_CONST.__const: 0x6d18
+  __TEXT.__objc_methname: 0x761f9
+  __TEXT.__objc_methtype: 0xf764
+  __TEXT.__objc_stubs: 0x45980
+  __DATA_CONST.__got: 0x17c8
+  __DATA_CONST.__const: 0x6d68
   __DATA_CONST.__objc_classlist: 0x1d80
   __DATA_CONST.__objc_catlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0x5e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4c188
-  __DATA_CONST.__objc_selrefs: 0x16548
+  __DATA_CONST.__objc_const: 0x4c218
+  __DATA_CONST.__objc_selrefs: 0x16598
   __DATA_CONST.__objc_arraydata: 0x1c38
   __AUTH_CONST.__objc_const: 0x14668
-  __AUTH_CONST.__cfstring: 0x1b0a0
+  __AUTH_CONST.__cfstring: 0x1b0e0
   __AUTH_CONST.__objc_arrayobj: 0xc18
   __AUTH_CONST.__const: 0x45e8
   __AUTH_CONST.__objc_intobj: 0x2760
   __AUTH_CONST.__objc_doubleobj: 0x280
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_ptr: 0x198
-  __AUTH_CONST.__auth_got: 0x20c8
+  __AUTH_CONST.__auth_got: 0x20d0
   __AUTH.__objc_data: 0xd7a0
   __AUTH.__data: 0x11b0
   __DATA.__objc_protorefs: 0x108
   __DATA.__objc_classrefs: 0x2218
   __DATA.__objc_superrefs: 0x1700
-  __DATA.__objc_ivar: 0x3c50
+  __DATA.__objc_ivar: 0x3c5c
   __DATA.__objc_data: 0x48
   __DATA.__objc_const_ax: 0x0
   __DATA.__data: 0x5f88

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21442
-  Symbols:   59886
-  CStrings:  24307
+  Functions: 21452
+  Symbols:   59922
+  CStrings:  24327
 
Symbols:
+ +[_HKQuantityDistributionData(HKCodingSupport) quantityDistributionDataWithCodableQuantityDistributionData:sourceTimeZone:preferredUnit:]
+ -[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]
+ -[HKAppImageManager _queue_cacheAppIcon:forIdentifier:productType:]
+ -[HKAppImageManager _queue_loadAppIconForSource:productType:onCompletion:]
+ -[HKAppImageManager _queue_synchronousLoadIconForSource:productType:]
+ -[HKAppImageManager _queue_synchronousLoadIconForSource:productType:].cold.1
+ -[HKAppImageManager iconCacheByProductType]
+ -[HKAppImageManager iconForSource:productType:]
+ -[HKAppImageManager loadAppImageAtURL:productType:completionHandler:]
+ -[HKAppImageManager loadAppImageAtURL:productType:crop:completionHandler:]
+ -[HKAppImageManager loadIconForSource:productType:completionHandler:]
+ -[HKAppImageManager loadIconForSource:productType:syncHandler:asyncHandler:]
+ -[HKAppImageManager setIconCacheByProductType:]
+ -[HKHealthChartFactory _additionalChartOptionsForDisplayDate:displayDateInterval:timeScope:]
+ -[HKInteractiveChartViewController hasInitialDateRangeAndTimeScope]
+ -[HKInteractiveChartViewController setHasInitialDateRangeAndTimeScope:]
+ -[HKQuantityDistributionDataSource preferredUnit]
+ -[_HKAppImageManagerContainer productType]
+ -[_HKAppImageManagerContainer setProductType:]
+ _AMSMediaTaskPlatformReality
+ _CGColorSpaceCreateWithName
+ _HKProductTypePrefixVisionPro
+ _LogFirstIncompatibleUnitConversionSet
+ _OBJC_IVAR_$_HKAppImageManager._iconCacheByProductType
+ _OBJC_IVAR_$_HKInteractiveChartViewController._hasInitialDateRangeAndTimeScope
+ _OBJC_IVAR_$_HKQuantityDistributionDataSource._preferredUnit
+ _OBJC_IVAR_$__HKAppImageManagerContainer._productType
+ ___137+[_HKQuantityDistributionData(HKCodingSupport) quantityDistributionDataWithCodableQuantityDistributionData:sourceTimeZone:preferredUnit:]_block_invoke
+ ___47-[HKAppImageManager iconForSource:productType:]_block_invoke
+ ___69-[HKAppImageManager loadIconForSource:productType:completionHandler:]_block_invoke
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.313
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.313.cold.1
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.314
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.cold.1
+ ___74-[HKAppImageManager _queue_loadAppIconForSource:productType:onCompletion:]_block_invoke
+ ___74-[HKAppImageManager _queue_loadAppIconForSource:productType:onCompletion:]_block_invoke_2
+ ___74-[HKAppImageManager loadAppImageAtURL:productType:crop:completionHandler:]_block_invoke
+ ___74-[HKAppImageManager loadAppImageAtURL:productType:crop:completionHandler:]_block_invoke_2
+ ___74-[HKAppImageManager loadAppImageAtURL:productType:crop:completionHandler:]_block_invoke_3
+ ___76-[HKAppImageManager loadIconForSource:productType:syncHandler:asyncHandler:]_block_invoke
+ ___76-[HKAppImageManager loadIconForSource:productType:syncHandler:asyncHandler:]_block_invoke_2
+ ___76-[HKAppImageManager loadIconForSource:productType:syncHandler:asyncHandler:]_block_invoke_3
+ ___block_descriptor_48_e8_32s40s_e72_"_HKQuantityDistributionData"16?0"HKCodableQuantityDistributionData"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e35_v32?0"UIImage"8B16B20"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e36_v24?0"AMSMediaResult"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"UIImage"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e35_v32?0"UIImage"8B16B20"NSError"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ ___block_literal_global.263
+ __doubleValueIfCompatibleForQuantity
+ _kCGColorSpaceDisplayP3
+ _kHKComAppleMomentsdBundleId
+ _objc_msgSend$_additionalChartOptionsForDisplayDate:displayDateInterval:timeScope:
+ _objc_msgSend$_enqueueRequestForAppIconForIdentifier:productType:
+ _objc_msgSend$_queue_cacheAppIcon:forIdentifier:productType:
+ _objc_msgSend$_queue_loadAppIconForSource:productType:onCompletion:
+ _objc_msgSend$_queue_synchronousLoadIconForSource:productType:
+ _objc_msgSend$currentDeviceProductType
+ _objc_msgSend$iconCacheByProductType
+ _objc_msgSend$iconForSource:productType:
+ _objc_msgSend$loadAppImageAtURL:productType:completionHandler:
+ _objc_msgSend$loadAppImageAtURL:productType:crop:completionHandler:
+ _objc_msgSend$loadIconForSource:productType:completionHandler:
+ _objc_msgSend$loadIconForSource:productType:syncHandler:asyncHandler:
+ _objc_msgSend$productType
+ _objc_msgSend$quantityDistributionDataWithCodableQuantityDistributionData:sourceTimeZone:preferredUnit:
+ _objc_msgSend$rangeOfUnit:inUnit:forDate:
+ _objc_msgSend$setAdditionalPlatforms:
+ _objc_msgSend$setHasInitialDateRangeAndTimeScope:
+ _objc_msgSend$setProductType:
- +[_HKQuantityDistributionData(HKCodingSupport) quantityDistributionDataWithCodableQuantityDistributionData:sourceTimeZone:]
- -[HKAppImageManager _enqueueRequestForAppIconForIdentifier:]
- -[HKAppImageManager _queue_cacheAppIcon:forIdentifier:]
- -[HKAppImageManager _queue_loadAppIconForSource:onCompletion:]
- -[HKAppImageManager _queue_synchronousLoadIconForSource:]
- -[HKAppImageManager _queue_synchronousLoadIconForSource:].cold.1
- -[HKAppImageManager iconCache]
- -[HKAppImageManager iconForSource:]
- -[HKAppImageManager loadAppImageAtURL:crop:completionHandler:]
- -[HKAppImageManager loadIconForSource:completionHandler:]
- -[HKAppImageManager setIconCache:]
- _OBJC_IVAR_$_HKAppImageManager._iconCache
- ___123+[_HKQuantityDistributionData(HKCodingSupport) quantityDistributionDataWithCodableQuantityDistributionData:sourceTimeZone:]_block_invoke
- ___35-[HKAppImageManager iconForSource:]_block_invoke
- ___57-[HKAppImageManager loadIconForSource:completionHandler:]_block_invoke
- ___60-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:]_block_invoke
- ___60-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:]_block_invoke.304
- ___60-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:]_block_invoke.304.cold.1
- ___60-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:]_block_invoke.cold.1
- ___62-[HKAppImageManager _queue_loadAppIconForSource:onCompletion:]_block_invoke
- ___62-[HKAppImageManager _queue_loadAppIconForSource:onCompletion:]_block_invoke_2
- ___62-[HKAppImageManager loadAppImageAtURL:crop:completionHandler:]_block_invoke
- ___62-[HKAppImageManager loadAppImageAtURL:crop:completionHandler:]_block_invoke_2
- ___62-[HKAppImageManager loadAppImageAtURL:crop:completionHandler:]_block_invoke_3
- ___64-[HKAppImageManager loadIconForSource:syncHandler:asyncHandler:]_block_invoke
- ___64-[HKAppImageManager loadIconForSource:syncHandler:asyncHandler:]_block_invoke_2
- ___64-[HKAppImageManager loadIconForSource:syncHandler:asyncHandler:]_block_invoke_3
- ___block_descriptor_40_e8_32s_e72_"_HKQuantityDistributionData"16?0"HKCodableQuantityDistributionData"8ls32l8
- ___block_descriptor_48_e8_32s40s_e35_v32?0"UIImage"8B16B20"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e36_v24?0"AMSMediaResult"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"UIImage"8ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48bs_e35_v32?0"UIImage"8B16B20"NSError"24ls32l8s40l8s48l8
- ___block_literal_global.255
- _objc_msgSend$_enqueueRequestForAppIconForIdentifier:
- _objc_msgSend$_queue_cacheAppIcon:forIdentifier:
- _objc_msgSend$_queue_loadAppIconForSource:onCompletion:
- _objc_msgSend$_queue_synchronousLoadIconForSource:
- _objc_msgSend$iconCache
- _objc_msgSend$iconForSource:
- _objc_msgSend$loadAppImageAtURL:crop:completionHandler:
- _objc_msgSend$loadIconForSource:completionHandler:
- _objc_msgSend$loadIconForSource:syncHandler:asyncHandler:
- _objc_msgSend$quantityDistributionDataWithCodableQuantityDistributionData:sourceTimeZone:
- _objc_msgSend$setIconCache:
- _objc_msgSend$setOutstandingRequests:
CStrings:
+ "\x021\x14"
+ "%@:%@"
+ "Q40@0:8@16@24q32"
+ "T@\"HKUnit\",R,N,V_preferredUnit"
+ "T@\"NSMutableDictionary\",&,V_iconCacheByProductType"
+ "T@\"NSString\",C,N,V_productType"
+ "TB,N,V_hasInitialDateRangeAndTimeScope"
+ "[%@] Incompatible unit conversion for %@ to %@"
+ "_additionalChartOptionsForDisplayDate:displayDateInterval:timeScope:"
+ "_enqueueRequestForAppIconForIdentifier:productType:"
+ "_hasInitialDateRangeAndTimeScope"
+ "_iconCacheByProductType"
+ "_queue_cacheAppIcon:forIdentifier:productType:"
+ "_queue_loadAppIconForSource:productType:onCompletion:"
+ "_queue_synchronousLoadIconForSource:productType:"
+ "currentDeviceProductType"
+ "hasInitialDateRangeAndTimeScope"
+ "iconCacheByProductType"
+ "iconForSource:productType:"
+ "loadAppImageAtURL:productType:completionHandler:"
+ "loadAppImageAtURL:productType:crop:completionHandler:"
+ "loadIconForSource:productType:completionHandler:"
+ "loadIconForSource:productType:syncHandler:asyncHandler:"
+ "productType"
+ "quantityDistributionDataWithCodableQuantityDistributionData:sourceTimeZone:preferredUnit:"
+ "rangeOfUnit:inUnit:forDate:"
+ "setAdditionalPlatforms:"
+ "setHasInitialDateRangeAndTimeScope:"
+ "setIconCacheByProductType:"
+ "setProductType:"
+ "v48@0:8@16@24@?32@?40"
+ "xros"
- "\x021\x13"
- "T@\"NSCache\",&,V_iconCache"
- "_enqueueRequestForAppIconForIdentifier:"
- "_queue_cacheAppIcon:forIdentifier:"
- "_queue_loadAppIconForSource:onCompletion:"
- "_queue_synchronousLoadIconForSource:"
- "iconCache"
- "iconForSource:"
- "loadAppImageAtURL:crop:completionHandler:"
- "loadIconForSource:completionHandler:"
- "quantityDistributionDataWithCodableQuantityDistributionData:sourceTimeZone:"
- "setIconCache:"

```
