## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-685.1.8.200.0
-  __TEXT.__text: 0xef8d8
+685.1.10.0.0
+  __TEXT.__text: 0xf00f4
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0x12530
-  __TEXT.__const: 0x3ac4
+  __TEXT.__objc_methlist: 0x12580
+  __TEXT.__const: 0x3ad4
   __TEXT.__cstring: 0x3b59
   __TEXT.__oslogstring: 0x2975
   __TEXT.__gcc_except_tab: 0xad4

   __TEXT.__swift_as_cont: 0x1c8
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5690
+  __TEXT.__unwind_info: 0x56d0
   __TEXT.__eh_frame: 0x2334
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x410
   __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa318
+  __DATA_CONST.__objc_selrefs: 0xa340
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x6f8
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x2570
+  __DATA_CONST.__got: 0x25a8
   __AUTH_CONST.__const: 0x2ae8
   __AUTH_CONST.__cfstring: 0x33e0
-  __AUTH_CONST.__objc_const: 0x1e148
+  __AUTH_CONST.__objc_const: 0x1e178
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH_CONST.__auth_got: 0x1920
   __AUTH.__objc_data: 0x36b0
   __AUTH.__data: 0x4c0
-  __DATA.__objc_ivar: 0xd08
-  __DATA.__data: 0x2fec
+  __DATA.__objc_ivar: 0xd0c
+  __DATA.__data: 0x305c
   __DATA.__common: 0xe0
   __DATA_DIRTY.__objc_data: 0x4358
   __DATA_DIRTY.__data: 0xb50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7033
-  Symbols:   11527
-  CStrings:  832
+  Functions: 7053
+  Symbols:   11537
+  CStrings:  833
 
Symbols:
+ +[SearchUIAppIconCardSectionView contentLayoutMarginsFittingWidth:shouldFillAvailableSpace:]
+ -[SFAppIconCardSection(SearchUIGridSectionModel) searchUIGridSectionModel_groupInsetFor:backgroundStyle:]
+ -[SFAppIconCardSection(SearchUIGridSectionModel) searchUIGridSectionModel_maximumNumberOfVisibleCardSectionsForWidth:]
+ -[SFCardSection(SearchUIGridSectionModel) searchUIGridSectionModel_groupInsetFor:backgroundStyle:]
+ -[SFCardSection(SearchUIGridSectionModel) searchUIGridSectionModel_maximumNumberOfVisibleCardSectionsForWidth:]
+ -[SFLinkPresentationCardSection(SearchUIGridSectionModel) searchUIGridSectionModel_groupInsetFor:backgroundStyle:]
+ -[SearchUICollectionViewDataSource truncatedVisibleCardSectionsAsyncSectionModel:]
+ -[SearchUICollectionViewDataSource updatePositionalStylingForCell:atIndexPath:]
+ -[SearchUIGridSectionModel maximumNumberOfVisibleCardSectionsForWidth:]
+ -[SearchUIResultsCollectionViewController isApplyingTableModel]
+ -[SearchUIResultsCollectionViewController setIsApplyingTableModel:]
+ -[SearchUISectionModel maximumNumberOfVisibleCardSectionsForWidth:]
+ GCC_except_table30
+ _OBJC_IVAR_$_SearchUIResultsCollectionViewController._isApplyingTableModel
+ _SearchUINoMaximumVisibleCardSections
+ _swift_retain_x28
- +[SearchUIAppIconUtilities gridSectionLayoutMarginsFittingSize:shouldFillAvailableSpace:]
- +[SearchUIAppIconUtilities idealHorizontalSpacingBetweenAppIcons]
- -[SFAppIconCardSection(SearchUIGridSectionModel) searchUIGridSectionModel_groupInsetFor:]
- -[SFCardSection(SearchUIGridSectionModel) searchUIGridSectionModel_groupInsetFor:]
- -[SFLinkPresentationCardSection(SearchUIGridSectionModel) searchUIGridSectionModel_groupInsetFor:]
- _swift_retain_x27
CStrings:
+ "$"
```
