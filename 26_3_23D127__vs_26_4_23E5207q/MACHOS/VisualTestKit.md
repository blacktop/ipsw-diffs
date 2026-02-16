## VisualTestKit

> `/System/Library/PrivateFrameworks/VisualTestKit.framework/VisualTestKit`

```diff

 5.0.0.0.0
-  __TEXT.__text: 0x5950
-  __TEXT.__auth_stubs: 0x560
+  __TEXT.__text: 0x5d54
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_methlist: 0xbc4
   __TEXT.__const: 0x1f8
   __TEXT.__cstring: 0x2e8
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__unwind_info: 0x2d0
   __TEXT.__objc_classname: 0x292
   __TEXT.__objc_methname: 0x1827
   __TEXT.__objc_methtype: 0x6d3

   __DATA_CONST.__objc_selrefs: 0x658
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0x40e0
   __AUTH.__objc_data: 0x6e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - @rpath/XCTest.framework/XCTest
-  UUID: 47E7123F-F619-3AF8-B444-C216B43652A9
+  UUID: 671A4959-A44C-3011-9D0D-9933BE5F1F41
   Functions: 208
-  Symbols:   864
+  Symbols:   858
   CStrings:  498
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x8
Functions:
~ ___55-[VTKAttachmentStoreManager saveItems:withID:testCase:]_block_invoke : 284 -> 292
~ ___55-[VTKAttachmentStoreManager saveItems:withID:testCase:]_block_invoke_2 : 128 -> 140
~ -[VTKAttachmentStoreManager setItemsDirectory:] : 96 -> 100
~ -[VTKAttachmentStoreManager itemsDirectory] : 76 -> 84
~ _VTKPixelSizeOfImage : 124 -> 128
~ _VTKImageWithDrawItems : 456 -> 460
~ __NSStringFromVTKAssertID : 212 -> 224
~ __StringExtensionForMask : 644 -> 676
~ ___VTKSetReferenceImagesDirectory : 96 -> 100
~ ___VTKAddVerticalGuideAt : 112 -> 116
~ ___VTKAddHorizontalGuideAt : 112 -> 116
~ ___VTKAddSqureGuideAt : 144 -> 148
~ ___VTKAddExclusionAreaAt : 112 -> 116
~ ___VTKExclusionAreaStatusBar : 116 -> 124
~ -[VTKFileReferenceItemsSource setItemsDirectory:] : 228 -> 248
~ -[VTKFileReferenceItemsSource referenceImageWithID:testCase:error:] : 252 -> 276
~ +[VTKStoreManagerImageItem itemWithImage:itemType:] : 132 -> 136
~ -[VTKStoreManagerImageItem fileNameWithTestID:] : 256 -> 284
~ -[VTKStoreManagerImageItem attachWithThestID:] : 184 -> 200
~ +[VTKStoreManagerItem itemWithView:] : 152 -> 160
~ -[VTKStoreManagerItem fileNameWithTestID:] : 144 -> 156
~ -[VTKStoreManagerItem attachWithThestID:] : 176 -> 192
~ -[VTKAntiAliasDetector initWithLeftContext:rightContext:strategy:] : 188 -> 172
~ -[VTKAntiAliasDetector isAntiAliasedAtPointHelper:leftContext:rightContext:] : 784 -> 796
~ -[VTKAntiAliasDetector setLeftContext:] : 12 -> 64
~ -[VTKAntiAliasDetector setRightContext:] : 12 -> 64
~ -[VTKAntiAliasDetector setStrategy:] : 12 -> 64
~ ___VTKSetReferenceItemSourceType : 84 -> 88
~ ___VTKSetImageComparatorStrategy : 84 -> 88
~ ___VTKSetImageComparisonOptions : 84 -> 88
~ -[VTKInternalConfiguration initWithReferenceItemsSource:storeManager:imageComparator:] : 232 -> 224
~ -[VTKInternalConfiguration copyWithZone:] : 244 -> 264
~ -[VTKInternalConfiguration referenceItemsSource] : 108 -> 116
~ -[VTKInternalConfiguration storeManager] : 84 -> 92
~ -[VTKInternalConfiguration imageComparator] : 132 -> 140
~ -[VTKInternalConfiguration setReferenceImagesDirectory:] : 172 -> 184
~ -[VTKInternalConfiguration referenceImagesDirectory] : 140 -> 156
~ -[VTKInternalConfiguration setCachedReferenceItemsSource:] : 12 -> 64
~ -[VTKInternalConfiguration setCachedStoreManager:] : 12 -> 64
~ -[VTKInternalConfiguration setCachedImageComparator:] : 12 -> 64
~ -[VTKColorDifferenceComparator compareImage:withImage:] : 856 -> 852
~ ___55-[VTKColorDifferenceComparator compareImage:withImage:]_block_invoke : 408 -> 440
~ -[VTKColorDifferenceComparator description] : 208 -> 220
~ -[VTKColorDifferenceComparator setStrategy:] : 12 -> 64
~ -[VTKBitmapContext image] : 120 -> 124
~ -[VTKBitmapContext colorAt:] : 80 -> 92
~ -[VTKBitmapContext colorForDifferent] : 116 -> 120
~ -[VTKBitmapContext colorForSame] : 96 -> 100
~ -[VTKBitmapContext colorForAntiAliased] : 116 -> 120
~ -[VTKBitmapContext drawColor:at:] : 132 -> 128
~ -[VTKBitmapContext _draw8BitColor:at:] : 116 -> 120
~ -[VTKBitmapContext _draw16BitColor:at:] : 116 -> 120
~ _VTKTransverseContexs : 308 -> 296
~ -[VTKAssetCatalogReferenceItemsSource referenceImageWithID:testCase:error:] : 376 -> 412
~ -[VTKAssertID isEqual:] : 164 -> 176
~ -[VTKCIEDE2000Strategy differenceBetweenColor:andColor:] : 188 -> 184
~ +[VTKCIEDE2000Strategy getLightness:A:B:alpha:fromColor:] : 192 -> 196
~ ___VTKAssertView : 160 -> 156
~ -[VTKLineDrawItem drawAtContext:] : 296 -> 300
~ -[VTKSquareDrawItem initWitColor:frame:] : 228 -> 220
~ -[VTKSquareDrawItem drawAtContext:] : 144 -> 148
~ -[VTKAssert initWithTestCase:configuration:] : 148 -> 144
~ -[VTKAssert referenceImagesDirectory] : 76 -> 84
~ -[VTKAssert drawItems] : 76 -> 84
~ -[VTKAssert assertView:identifier:filePath:lineNumber:] : 1372 -> 1532
~ -[XCTestCase(VisualTestKit) VisualTestKitAssert] : 116 -> 120
~ -[XCTestCase(VisualTestKit) VisualTestKitConfiguration] : 456 -> 468
~ -[VTKFileStoreManager init] : 100 -> 104
~ __saveItemsRootURLWithItemsDirectory : 180 -> 192
~ -[VTKFileStoreManager setItemsDirectory:] : 252 -> 276
~ -[VTKFileStoreManager saveItems:withID:testCase:] : 316 -> 304
~ ___49-[VTKFileStoreManager saveItems:withID:testCase:]_block_invoke : 160 -> 176
~ -[VTKFileStoreManagerResult initWithURL:] : 116 -> 108
~ -[VTKFileStoreManagerResult saveDescription] : 132 -> 144
~ -[UIView(VTKSnapshot) vtk_SnapshotWithScale:] : 252 -> 264

```
