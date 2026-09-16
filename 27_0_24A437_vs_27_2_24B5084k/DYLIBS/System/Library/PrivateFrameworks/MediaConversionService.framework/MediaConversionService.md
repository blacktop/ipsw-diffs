## MediaConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService`

```diff

-912.0.235.0.0
-  __TEXT.__text: 0x1d838
-  __TEXT.__objc_methlist: 0x1eec
+916.40.110.0.0
+  __TEXT.__text: 0x1e3e8
+  __TEXT.__objc_methlist: 0x1ff4
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x5a0
-  __TEXT.__cstring: 0x5970
-  __TEXT.__oslogstring: 0x28ca
-  __TEXT.__unwind_info: 0x8c8
+  __TEXT.__gcc_except_tab: 0x5c0
+  __TEXT.__cstring: 0x5ae4
+  __TEXT.__oslogstring: 0x292c
+  __TEXT.__unwind_info: 0x910
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xcd8
+  __DATA_CONST.__const: 0xcf8
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1638
+  __DATA_CONST.__objc_selrefs: 0x16f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x578
-  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__objc_arraydata: 0x5a8
+  __DATA_CONST.__got: 0x3d0
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x3460
-  __AUTH_CONST.__objc_const: 0x2f88
+  __AUTH_CONST.__cfstring: 0x3520
+  __AUTH_CONST.__objc_const: 0x30d8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x250
+  __DATA.__objc_ivar: 0x26c
   __DATA.__data: 0x4a8
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 708
-  Symbols:   2066
-  CStrings:  623
+  Functions: 732
+  Symbols:   2128
+  CStrings:  631
 
Symbols:
+ -[PAMediaConversionServiceContentProvenanceValidationResult certificateChainDERData]
+ -[PAMediaConversionServiceContentProvenanceValidationResult setCertificateChainDERData:]
+ -[PHMediaFormatConversionCompositeRequest requiresStarRatingMetadataChange]
+ -[PHMediaFormatConversionCompositeRequest requiresTitleMetadataChange]
+ -[PHMediaFormatConversionRequest requiresStarRatingMetadataChange]
+ -[PHMediaFormatConversionRequest requiresTitleMetadataChange]
+ -[PHMediaFormatConversionRequest setStarRatingMetadataBehavior:withStarRating:]
+ -[PHMediaFormatConversionRequest setTitleMetadataBehavior:withTitle:]
+ -[PHMediaFormatConversionRequest starRatingMetadataBehavior]
+ -[PHMediaFormatConversionRequest starRating]
+ -[PHMediaFormatConversionRequest titleMetadataBehavior]
+ -[PHMediaFormatConversionRequest title]
+ -[PHMediaFormatConversionSource checkForStarRatingData]
+ -[PHMediaFormatConversionSource checkForTitleData]
+ -[PHMediaFormatConversionSource markStarRatingMetadataAsCheckedWithStatus:]
+ -[PHMediaFormatConversionSource markTitleMetadataAsCheckedWithStatus:]
+ -[PHMediaFormatConversionSource setStarRatingMetadataStatus:]
+ -[PHMediaFormatConversionSource setTitleMetadataStatus:]
+ -[PHMediaFormatConversionSource sourceStarRatingMetadataStatus]
+ -[PHMediaFormatConversionSource sourceTitleMetadataStatus]
+ -[PHMediaFormatConversionSource starRatingMetadataStatus]
+ -[PHMediaFormatConversionSource titleMetadataStatus]
+ GCC_except_table139
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table171
+ GCC_except_table177
+ GCC_except_table424
+ GCC_except_table426
+ GCC_except_table428
+ GCC_except_table430
+ GCC_except_table432
+ GCC_except_table434
+ GCC_except_table436
+ GCC_except_table438
+ GCC_except_table440
+ GCC_except_table442
+ GCC_except_table557
+ GCC_except_table565
+ GCC_except_table595
+ GCC_except_table597
+ GCC_except_table685
+ GCC_except_table687
+ GCC_except_table690
+ GCC_except_table692
+ GCC_except_table705
+ GCC_except_table96
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetKeywords
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetStarRating
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetTitle
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceValidationResult._certificateChainDERData
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._starRating
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._starRatingMetadataBehavior
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._title
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._titleMetadataBehavior
+ _OBJC_IVAR_$_PHMediaFormatConversionSource._starRatingMetadataStatus
+ _OBJC_IVAR_$_PHMediaFormatConversionSource._titleMetadataStatus
+ _PAMediaConversionServiceOptionAVMetadataIncludeRatingKey
+ _PAMediaConversionServiceOptionAVMetadataIncludeTitleKey
+ _PAMediaConversionServiceOptionAVMetadataRatingKey
+ _PAMediaConversionServiceProvenanceCertificateChainDataKey
+ ___70-[PHMediaFormatConversionCompositeRequest requiresTitleMetadataChange]_block_invoke
+ ___75-[PHMediaFormatConversionCompositeRequest requiresStarRatingMetadataChange]_block_invoke
+ _objc_msgSend$checkForKeywordsData
+ _objc_msgSend$checkForStarRatingData
+ _objc_msgSend$checkForTitleData
+ _objc_msgSend$markStarRatingMetadataAsCheckedWithStatus:
+ _objc_msgSend$markTitleMetadataAsCheckedWithStatus:
+ _objc_msgSend$policyWithKeywords:
+ _objc_msgSend$policyWithStarRating:
+ _objc_msgSend$policyWithTitle:
+ _objc_msgSend$requiresStarRatingMetadataChange
+ _objc_msgSend$requiresTitleMetadataChange
+ _objc_msgSend$setCertificateChainDERData:
+ _objc_msgSend$setStarRatingMetadataBehavior:withStarRating:
+ _objc_msgSend$setTitleMetadataBehavior:withTitle:
+ _objc_msgSend$sourceKeywordsMetadataStatus
+ _objc_msgSend$sourceStarRatingMetadataStatus
+ _objc_msgSend$sourceTitleMetadataStatus
+ _objc_msgSend$starRating
+ _objc_msgSend$starRatingMetadataBehavior
+ _objc_msgSend$starRatingMetadataStatus
+ _objc_msgSend$title
+ _objc_msgSend$titleMetadataBehavior
+ _objc_msgSend$titleMetadataStatus
- GCC_except_table137
- GCC_except_table152
- GCC_except_table159
- GCC_except_table169
- GCC_except_table175
- GCC_except_table404
- GCC_except_table406
- GCC_except_table408
- GCC_except_table410
- GCC_except_table412
- GCC_except_table414
- GCC_except_table416
- GCC_except_table418
- GCC_except_table533
- GCC_except_table541
- GCC_except_table571
- GCC_except_table573
- GCC_except_table661
- GCC_except_table663
- GCC_except_table666
- GCC_except_table668
- GCC_except_table681
- GCC_except_table92
CStrings:
+ "#q"
+ "PAMediaConversionServiceOptionAVMetadataIncludeRatingKey"
+ "PAMediaConversionServiceOptionAVMetadataIncludeTitleKey"
+ "PAMediaConversionServiceOptionAVMetadataRatingKey"
+ "PAMediaConversionServiceProvenanceCertificateChainDataKey"
+ "Read star rating metadata status: %ld from file: %@"
+ "Read title metadata status: %ld from file: %@"
+ "starRating must not be nil if behavior is PHMediaFormatMetadataBehaviorApply"
+ "title must not be nil if behavior is PHMediaFormatMetadataBehaviorApply"
- "#Q"
```
