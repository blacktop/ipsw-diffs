## VisualTestKit

> `/System/Library/PrivateFrameworks/VisualTestKit.framework/VisualTestKit`

```diff

 5.0.0.0.0
-  __TEXT.__text: 0x5d54
-  __TEXT.__auth_stubs: 0x500
+  __TEXT.__text: 0x5950
   __TEXT.__objc_methlist: 0xbc4
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x2e8
+  __TEXT.__cstring: 0x2f9
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__unwind_info: 0x2d0
-  __TEXT.__objc_classname: 0x292
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__objc_stubs: 0x1520
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_classname: 0x282
   __TEXT.__objc_methname: 0x1827
   __TEXT.__objc_methtype: 0x6d3
-  __TEXT.__objc_stubs: 0x1520
-  __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_selrefs: 0x658
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0xd0
   __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0x40e0
+  __AUTH_CONST.__auth_got: 0x2c0
   __AUTH.__objc_data: 0x6e0
   __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x488

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - @rpath/XCTest.framework/XCTest
-  UUID: BFF650DC-E70A-3265-BED1-C2FE289F2C1A
+  UUID: 89BB2538-0F4C-399B-AB2E-696EB714938C
   Functions: 208
-  Symbols:   858
+  Symbols:   864
   CStrings:  498
 
Symbols:
+ _OBJC_$_PROP_LIST_VTKAssertID.58
+ _OBJC_$_PROP_LIST_VTKStoreManagerItem.110
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x8
- _OBJC_$_PROP_LIST_VTKAssertID.59
- _OBJC_$_PROP_LIST_VTKStoreManagerItem.111
- _objc_retainAutoreleasedReturnValue
Functions:
~ ___55-[VTKAttachmentStoreManager saveItems:withID:testCase:]_block_invoke : 292 -> 284
~ ___55-[VTKAttachmentStoreManager saveItems:withID:testCase:]_block_invoke_2 : 140 -> 128
~ -[VTKAttachmentStoreManager setItemsDirectory:] : 100 -> 96
~ -[VTKAttachmentStoreManager itemsDirectory] : 84 -> 76
~ _VTKPixelSizeOfImage : 128 -> 124
~ _VTKImageWithDrawItems : 460 -> 456
~ __NSStringFromVTKAssertID : 224 -> 212
~ __StringExtensionForMask : 676 -> 644
~ ___VTKSetReferenceImagesDirectory : 100 -> 96
~ ___VTKAddVerticalGuideAt : 116 -> 112
~ ___VTKAddHorizontalGuideAt : 116 -> 112
~ ___VTKAddSqureGuideAt : 148 -> 144
~ ___VTKAddExclusionAreaAt : 116 -> 112
~ ___VTKExclusionAreaStatusBar : 124 -> 116
~ -[VTKFileReferenceItemsSource setItemsDirectory:] : 248 -> 228
~ -[VTKFileReferenceItemsSource referenceImageWithID:testCase:error:] : 276 -> 252
~ +[VTKStoreManagerImageItem itemWithImage:itemType:] : 136 -> 132
~ -[VTKStoreManagerImageItem fileNameWithTestID:] : 284 -> 256
~ -[VTKStoreManagerImageItem attachWithThestID:] : 200 -> 184
~ +[VTKStoreManagerItem itemWithView:] : 160 -> 152
~ -[VTKStoreManagerItem fileNameWithTestID:] : 156 -> 144
~ -[VTKStoreManagerItem attachWithThestID:] : 192 -> 176
~ -[VTKAntiAliasDetector initWithLeftContext:rightContext:strategy:] : 172 -> 188
~ -[VTKAntiAliasDetector isAntiAliasedAtPointHelper:leftContext:rightContext:] : 796 -> 784
~ -[VTKAntiAliasDetector setLeftContext:] : 64 -> 12
~ -[VTKAntiAliasDetector setRightContext:] : 64 -> 12
~ -[VTKAntiAliasDetector setStrategy:] : 64 -> 12
~ ___VTKSetReferenceItemSourceType : 88 -> 84
~ ___VTKSetImageComparatorStrategy : 88 -> 84
~ ___VTKSetImageComparisonOptions : 88 -> 84
~ -[VTKInternalConfiguration initWithReferenceItemsSource:storeManager:imageComparator:] : 224 -> 232
~ -[VTKInternalConfiguration copyWithZone:] : 264 -> 244
~ -[VTKInternalConfiguration referenceItemsSource] : 116 -> 108
~ -[VTKInternalConfiguration storeManager] : 92 -> 84
~ -[VTKInternalConfiguration imageComparator] : 140 -> 132
~ -[VTKInternalConfiguration setReferenceImagesDirectory:] : 184 -> 172
~ -[VTKInternalConfiguration referenceImagesDirectory] : 156 -> 140
~ -[VTKInternalConfiguration setCachedReferenceItemsSource:] : 64 -> 12
~ -[VTKInternalConfiguration setCachedStoreManager:] : 64 -> 12
~ -[VTKInternalConfiguration setCachedImageComparator:] : 64 -> 12
~ -[VTKColorDifferenceComparator compareImage:withImage:] : 852 -> 856
~ ___55-[VTKColorDifferenceComparator compareImage:withImage:]_block_invoke : 440 -> 408
~ -[VTKColorDifferenceComparator description] : 220 -> 208
~ -[VTKColorDifferenceComparator setStrategy:] : 64 -> 12
~ -[VTKBitmapContext image] : 124 -> 120
~ -[VTKBitmapContext colorAt:] : 92 -> 80
~ -[VTKBitmapContext colorForDifferent] : 120 -> 116
~ -[VTKBitmapContext colorForSame] : 100 -> 96
~ -[VTKBitmapContext colorForAntiAliased] : 120 -> 116
~ -[VTKBitmapContext drawColor:at:] : 128 -> 132
~ -[VTKBitmapContext _draw8BitColor:at:] : 120 -> 116
~ -[VTKBitmapContext _draw16BitColor:at:] : 120 -> 116
~ _VTKTransverseContexs : 296 -> 308
~ -[VTKAssetCatalogReferenceItemsSource referenceImageWithID:testCase:error:] : 412 -> 376
~ -[VTKAssertID isEqual:] : 176 -> 164
~ -[VTKCIEDE2000Strategy differenceBetweenColor:andColor:] : 184 -> 188
~ +[VTKCIEDE2000Strategy getLightness:A:B:alpha:fromColor:] : 196 -> 192
~ ___VTKAssertView : 156 -> 160
~ -[VTKLineDrawItem drawAtContext:] : 300 -> 296
~ -[VTKSquareDrawItem initWitColor:frame:] : 220 -> 228
~ -[VTKSquareDrawItem drawAtContext:] : 148 -> 144
~ -[VTKAssert initWithTestCase:configuration:] : 144 -> 148
~ -[VTKAssert referenceImagesDirectory] : 84 -> 76
~ -[VTKAssert drawItems] : 84 -> 76
~ -[VTKAssert assertView:identifier:filePath:lineNumber:] : 1532 -> 1372
~ -[XCTestCase(VisualTestKit) VisualTestKitAssert] : 120 -> 116
~ -[XCTestCase(VisualTestKit) VisualTestKitConfiguration] : 468 -> 456
~ -[VTKFileStoreManager init] : 104 -> 100
~ __saveItemsRootURLWithItemsDirectory : 192 -> 180
~ -[VTKFileStoreManager setItemsDirectory:] : 276 -> 252
~ -[VTKFileStoreManager saveItems:withID:testCase:] : 304 -> 316
~ ___49-[VTKFileStoreManager saveItems:withID:testCase:]_block_invoke : 176 -> 160
~ -[VTKFileStoreManagerResult initWithURL:] : 108 -> 116
~ -[VTKFileStoreManagerResult saveDescription] : 144 -> 132
~ -[UIView(VTKSnapshot) vtk_SnapshotWithScale:] : 264 -> 252
CStrings:
+ "HasExtendedColorDisplay"
- "Aixt/MEN2O2B7f+8m4TxUA"

```
