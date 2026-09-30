## PosterLegibilityKit

> `/System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit`

```diff

-304.4.13.102.0
-  __TEXT.__text: 0x1b9ec
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x1bec
-  __TEXT.__const: 0x328
-  __TEXT.__cstring: 0xf52
-  __TEXT.__oslogstring: 0xf60
-  __TEXT.__gcc_except_tab: 0x6e0
-  __TEXT.__unwind_info: 0x8f0
+304.4.14.101.0
+  __TEXT.__text: 0x1be40
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_methlist: 0x1bf4
+  __TEXT.__const: 0x330
+  __TEXT.__cstring: 0xf2a
+  __TEXT.__oslogstring: 0xf13
+  __TEXT.__gcc_except_tab: 0x70c
+  __TEXT.__unwind_info: 0x918
   __TEXT.__objc_classname: 0x4fb
-  __TEXT.__objc_methname: 0x496b
-  __TEXT.__objc_methtype: 0xd74
-  __TEXT.__objc_stubs: 0x38e0
-  __DATA_CONST.__got: 0x380
+  __TEXT.__objc_methname: 0x49ff
+  __TEXT.__objc_methtype: 0xd84
+  __TEXT.__objc_stubs: 0x39a0
+  __DATA_CONST.__got: 0x388
   __DATA_CONST.__const: 0x8a0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e8
+  __DATA_CONST.__objc_selrefs: 0x1210
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x668
-  __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1180
-  __AUTH_CONST.__objc_const: 0x4f78
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x11a0
+  __AUTH_CONST.__objc_const: 0x4f98
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x220
+  __DATA.__objc_ivar: 0x224
   __DATA.__data: 0x540
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0x7d0
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1DC84018-5B79-3EE0-911B-9FA7F6A4B4C0
-  Functions: 680
-  Symbols:   2821
-  CStrings:  1381
+  UUID: B427C366-ACD1-38E7-AE36-A084DFDE649E
+  Functions: 690
+  Symbols:   2864
+  CStrings:  1389
 
Symbols:
+ +[PLKImageRenderer _poolBackedImage:pool:scale:]
+ -[PLKCachedImageGenerator imageFutureForObject:persistenceOptions:context:].cold.1
+ -[PLKCachedImageGenerator prewarmObjects:context:].cold.1
+ -[PLKCachedImageGenerator removeImagesForCacheKeys:].cold.1
+ GCC_except_table24
+ GCC_except_table26
+ GCC_except_table48
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CGDataProviderCopyData
+ _CGDataProviderCreateWithCFData
+ _CGImageGetDataProvider
+ _OBJC_CLASS_$_BSAtomicFlag
+ _OBJC_IVAR_$_PLKCachedImageGenerator._prewarmInProgressFlag
+ ___50-[PLKCachedImageGenerator prewarmObjects:context:]_block_invoke.41
+ ___50-[PLKCachedImageGenerator prewarmObjects:context:]_block_invoke.45
+ ___52-[PLKCachedImageGenerator removeImagesForCacheKeys:]_block_invoke.48
+ ____imageFutureContinuationScheduler_block_invoke
+ ____prewarmContinuationScheduler_block_invoke
+ ____removeContinuationScheduler_block_invoke
+ ___block_descriptor_48_e8_32s40w_e21_"<PFTFuture>"16?08ls32l8w40l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r_e9_16?0^8ls32l8s40l8s48l8s56l8s64l8r72l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72bs80w_e29_"PFTFuture"16?0"NSString"8ls32l8s40l8s48l8s72l8s56l8w80l8s64l8
+ ___block_literal_global.145
+ ___block_literal_global.150
+ __imageFutureContinuationScheduler.onceToken
+ __imageFutureContinuationScheduler.scheduler
+ __prewarmContinuationScheduler
+ __prewarmContinuationScheduler.cold.1
+ __prewarmContinuationScheduler.onceToken
+ __prewarmContinuationScheduler.scheduler
+ __removeContinuationScheduler.onceToken
+ __removeContinuationScheduler.scheduler
+ _objc_msgSend$_poolBackedImage:pool:scale:
+ _objc_msgSend$flatMap:continuationScheduler:
+ _objc_msgSend$initWithFlag:
+ _objc_msgSend$nextSlotWithBytes:length:
+ _objc_msgSend$serialDispatchQueueSchedulerWithName:
+ _objc_msgSend$setDefaultPersistenceOptions:
+ _objc_msgSend$setFlag:
+ _objc_retain_x8
+ _plk_sharedMemoryPoolForDescriptor:.sharedMemoryPools
- +[PLKImageRenderer contextWithFormat:].cold.1
- GCC_except_table23
- GCC_except_table25
- _CGBitmapAllocateData
- ___50-[PLKCachedImageGenerator prewarmObjects:context:]_block_invoke.39
- ___50-[PLKCachedImageGenerator prewarmObjects:context:]_block_invoke.43
- ___52-[PLKCachedImageGenerator removeImagesForCacheKeys:]_block_invoke.46
- ___block_descriptor_40_e8_32s_e21_"<PFTFuture>"16?08ls32l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e9_16?0^8ls32l8s40l8s48l8s56l8s64l8s72l8r80l8
- ___block_descriptor_97_e8_32s40s48s56s64s72s80bs88w_e29_"PFTFuture"16?0"NSString"8ls32l8s40l8s48l8s56l8s80l8s64l8w88l8s72l8
- _objc_msgSend$stringWithUTF8String:
- _plk_sharedMemoryPoolForDescriptor:.sharedMemoryPoolsForDescriptor
CStrings:
+ "-[PLKCachedImageGenerator(%@%p) prewarmObjects: bailing, prewarm already in progress]"
+ "@\"BSAtomicFlag\""
+ "PLKCachedImageGenerator-imageFuture-continuation"
+ "PLKCachedImageGenerator-prewarm-continuation"
+ "PLKCachedImageGenerator-remove-continuation"
+ "_poolBackedImage:pool:scale:"
+ "_prewarmInProgressFlag"
+ "classicDrawShadows: memoryPool incompatible for shadow %{public}@ @%.0fx"
+ "flatMap:continuationScheduler:"
+ "initWithFlag:"
+ "nextSlotWithBytes:length:"
+ "serialDispatchQueueSchedulerWithName:"
+ "setFlag:"
- "+[PLKImageRenderer contextWithFormat:]"
- "PLK alignment-aware shadow rendering: alignmentInsets=%@"
- "PLKImageRenderer.m"
- "[SBH_LEGIBILITY] PLK alignment-aware contentRect: imageSize=%@, alignmentInsets=%@, alignmentSize=%@, bounds=%@, contentRect=%@"
- "failure in %{public}@ (%{public}@:%i) : %{public}@"
- "requested slot length (%zd) larger than maximum slotLength (%zd), not large enough for %@ context with dimensions %@ @%fx"
- "stringWithUTF8String:"

```
