## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-467.3.4.0.0
-  __TEXT.__text: 0x9abbc
-  __TEXT.__objc_methlist: 0x9328
-  __TEXT.__const: 0x184c
-  __TEXT.__cstring: 0x5bf5
+467.3.12.0.0
+  __TEXT.__text: 0x9e9c0
+  __TEXT.__objc_methlist: 0x9618
+  __TEXT.__const: 0x185c
+  __TEXT.__cstring: 0x5d80
   __TEXT.__swift5_typeref: 0xeec
   __TEXT.__constg_swiftt: 0x960
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_types: 0xa4
-  __TEXT.__oslogstring: 0x287a
+  __TEXT.__oslogstring: 0x2dd1
   __TEXT.__swift5_reflstr: 0x605
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_fieldmd: 0x7f8

   __TEXT.__swift5_protos: 0x8
   __TEXT.__gcc_except_tab: 0x1984
   __TEXT.__ustring: 0x9e
-  __TEXT.__unwind_info: 0x3470
+  __TEXT.__unwind_info: 0x3528
   __TEXT.__eh_frame: 0xa30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1310
-  __DATA_CONST.__objc_classlist: 0x328
+  __DATA_CONST.__const: 0x13d8
+  __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48c0
+  __DATA_CONST.__objc_selrefs: 0x4aa0
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x210
+  __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x380
   __DATA_CONST.__got: 0x790
-  __AUTH_CONST.__const: 0x3280
-  __AUTH_CONST.__cfstring: 0x5720
-  __AUTH_CONST.__objc_const: 0xbdd0
+  __AUTH_CONST.__const: 0x32a0
+  __AUTH_CONST.__cfstring: 0x5960
+  __AUTH_CONST.__objc_const: 0xc370
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x10a8
-  __AUTH.__objc_data: 0x360
-  __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x8dc
-  __DATA.__data: 0x1690
+  __AUTH_CONST.__auth_got: 0x10b0
+  __AUTH.__objc_data: 0x4a0
+  __AUTH.__data: 0x88
+  __DATA.__objc_ivar: 0x920
+  __DATA.__data: 0x16a0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1d10
   __DATA_DIRTY.__data: 0xc20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4032
-  Symbols:   5840
-  CStrings:  1080
+  Functions: 4106
+  Symbols:   5962
+  CStrings:  1119
 
Symbols:
+ +[SCROBrailleUIFinderApp _loadTextOfPDFAtURL:section:intoResult:]
+ +[SCROBrailleUIPDFSections _appendPageRangeSectionsFrom:to:documentTitle:pageCount:toSections:]
+ +[SCROBrailleUIPDFSections _chapterSectionsForDocument:documentTitle:pageCount:]
+ +[SCROBrailleUIPDFSections sectionsForPDFAtURL:]
+ +[SCROBrailleUIUtilities textFromPDFAtURL:isTooLarge:]
+ +[SCROBrailleUIUtilities textFromPDFAtURL:pageRange:isTooLarge:]
+ -[SCROBrailleUIFinderApp _cancelLoading]
+ -[SCROBrailleUIFinderApp _closePDFSectionsMenu]
+ -[SCROBrailleUIFinderApp _handleActionInLoadingView:]
+ -[SCROBrailleUIFinderApp _handleActionInPDFSectionsMenu:]
+ -[SCROBrailleUIFinderApp _isLoading]
+ -[SCROBrailleUIFinderApp _isPDFSectionsMenuOpen]
+ -[SCROBrailleUIFinderApp _loadURL:inBackground:completion:]
+ -[SCROBrailleUIFinderApp _openPDFSectionsMenuForURL:sections:]
+ -[SCROBrailleUIFinderApp _openPlainTextOrPDF:]
+ -[SCROBrailleUIFinderApp _openViewerForPlainText:section:content:]
+ -[SCROBrailleUIFinderApp _performOnEventQueue:]
+ -[SCROBrailleUIFinderApp _plainTextPersistenceKey]
+ -[SCROBrailleUIFinderApp _presentViewerForBRFFile:]
+ -[SCROBrailleUIFinderApp _resetLoadingState]
+ -[SCROBrailleUIFinderApp _scheduleLoadingAnimationTickForGeneration:]
+ -[SCROBrailleUIFinderApp currentPDFSection]
+ -[SCROBrailleUIFinderApp loadGeneration]
+ -[SCROBrailleUIFinderApp loadingURL]
+ -[SCROBrailleUIFinderApp loadingView]
+ -[SCROBrailleUIFinderApp pdfSectionsMenuView]
+ -[SCROBrailleUIFinderApp pdfSections]
+ -[SCROBrailleUIFinderApp setCurrentPDFSection:]
+ -[SCROBrailleUIFinderApp setLoadGeneration:]
+ -[SCROBrailleUIFinderApp setLoadingURL:]
+ -[SCROBrailleUIFinderApp setLoadingView:]
+ -[SCROBrailleUIFinderApp setPdfSections:]
+ -[SCROBrailleUIFinderApp setPdfSectionsMenuView:]
+ -[SCROBrailleUIFinderAppLoadResult .cxx_destruct]
+ -[SCROBrailleUIFinderAppLoadResult brfFile]
+ -[SCROBrailleUIFinderAppLoadResult errorMessageKey]
+ -[SCROBrailleUIFinderAppLoadResult pdfSection]
+ -[SCROBrailleUIFinderAppLoadResult pdfSections]
+ -[SCROBrailleUIFinderAppLoadResult plainTextContent]
+ -[SCROBrailleUIFinderAppLoadResult setBrfFile:]
+ -[SCROBrailleUIFinderAppLoadResult setErrorMessageKey:]
+ -[SCROBrailleUIFinderAppLoadResult setPdfSection:]
+ -[SCROBrailleUIFinderAppLoadResult setPdfSections:]
+ -[SCROBrailleUIFinderAppLoadResult setPlainTextContent:]
+ -[SCROBrailleUILoadingView .cxx_destruct]
+ -[SCROBrailleUILoadingView _animatedText]
+ -[SCROBrailleUILoadingView advanceAnimation]
+ -[SCROBrailleUILoadingView contentValue]
+ -[SCROBrailleUILoadingView contentVisualRepresentation]
+ -[SCROBrailleUILoadingView displayContent]
+ -[SCROBrailleUILoadingView dotCount]
+ -[SCROBrailleUILoadingView handleBackButtonNavigationEvent:]
+ -[SCROBrailleUILoadingView handleContentEvent:]
+ -[SCROBrailleUILoadingView initWithIdentifier:text:]
+ -[SCROBrailleUILoadingView setDotCount:]
+ -[SCROBrailleUILoadingView setText:]
+ -[SCROBrailleUILoadingView text]
+ -[SCROBrailleUIPDFSection .cxx_destruct]
+ -[SCROBrailleUIPDFSection bottomTitle]
+ -[SCROBrailleUIPDFSection identifier]
+ -[SCROBrailleUIPDFSection initWholeDocumentWithTitle:pageCount:]
+ -[SCROBrailleUIPDFSection initWithDocumentTitle:chapterTitle:pageRange:pageCount:]
+ -[SCROBrailleUIPDFSection pageRange]
+ -[SCROBrailleUIPDFSection title]
+ -[SCROBrailleUIPDFSection topTitle]
+ -[SCROBrailleUIPlainTextView _captionsForRows:originalBraille:locations:sourceLine:]
+ -[SCROBrailleUIPlainTextView currentRowCaptions]
+ -[SCROBrailleUIPlainTextView setCurrentRowCaptions:]
+ GCC_except_table1069
+ GCC_except_table1133
+ GCC_except_table1135
+ GCC_except_table1137
+ GCC_except_table1139
+ GCC_except_table1206
+ GCC_except_table1234
+ GCC_except_table1239
+ GCC_except_table1243
+ GCC_except_table1246
+ GCC_except_table1248
+ GCC_except_table1279
+ GCC_except_table1286
+ GCC_except_table1418
+ GCC_except_table1631
+ GCC_except_table1755
+ GCC_except_table1894
+ GCC_except_table1896
+ GCC_except_table1904
+ GCC_except_table1914
+ GCC_except_table1998
+ GCC_except_table2043
+ GCC_except_table2047
+ GCC_except_table2159
+ GCC_except_table2180
+ GCC_except_table2185
+ GCC_except_table2191
+ GCC_except_table2290
+ GCC_except_table2476
+ GCC_except_table2494
+ GCC_except_table2610
+ GCC_except_table2611
+ GCC_except_table2612
+ GCC_except_table2616
+ GCC_except_table2621
+ GCC_except_table2622
+ GCC_except_table2623
+ GCC_except_table2624
+ GCC_except_table2625
+ GCC_except_table2627
+ GCC_except_table2628
+ GCC_except_table2629
+ GCC_except_table2633
+ GCC_except_table2638
+ GCC_except_table2640
+ GCC_except_table2643
+ GCC_except_table3019
+ GCC_except_table3035
+ GCC_except_table3054
+ GCC_except_table3056
+ GCC_except_table3122
+ GCC_except_table3124
+ GCC_except_table3126
+ GCC_except_table3127
+ GCC_except_table3129
+ GCC_except_table3131
+ GCC_except_table501
+ GCC_except_table533
+ GCC_except_table534
+ GCC_except_table556
+ GCC_except_table557
+ GCC_except_table567
+ GCC_except_table569
+ GCC_except_table587
+ GCC_except_table588
+ GCC_except_table590
+ GCC_except_table594
+ GCC_except_table597
+ GCC_except_table607
+ GCC_except_table629
+ GCC_except_table630
+ GCC_except_table638
+ GCC_except_table640
+ GCC_except_table646
+ GCC_except_table660
+ GCC_except_table661
+ GCC_except_table662
+ GCC_except_table663
+ GCC_except_table665
+ GCC_except_table669
+ GCC_except_table670
+ GCC_except_table672
+ GCC_except_table676
+ GCC_except_table694
+ GCC_except_table695
+ GCC_except_table698
+ GCC_except_table896
+ GCC_except_table937
+ GCC_except_table939
+ _NSURLFileSizeKey
+ _OBJC_CLASS_$_SCROBrailleUIFinderAppLoadResult
+ _OBJC_CLASS_$_SCROBrailleUILoadingView
+ _OBJC_CLASS_$_SCROBrailleUIPDFSection
+ _OBJC_CLASS_$_SCROBrailleUIPDFSections
+ _OBJC_IVAR_$_SCROBrailleUIFinderApp._currentPDFSection
+ _OBJC_IVAR_$_SCROBrailleUIFinderApp._loadGeneration
+ _OBJC_IVAR_$_SCROBrailleUIFinderApp._loadingURL
+ _OBJC_IVAR_$_SCROBrailleUIFinderApp._loadingView
+ _OBJC_IVAR_$_SCROBrailleUIFinderApp._pdfSections
+ _OBJC_IVAR_$_SCROBrailleUIFinderApp._pdfSectionsMenuView
+ _OBJC_IVAR_$_SCROBrailleUIFinderAppLoadResult._brfFile
+ _OBJC_IVAR_$_SCROBrailleUIFinderAppLoadResult._errorMessageKey
+ _OBJC_IVAR_$_SCROBrailleUIFinderAppLoadResult._pdfSection
+ _OBJC_IVAR_$_SCROBrailleUIFinderAppLoadResult._pdfSections
+ _OBJC_IVAR_$_SCROBrailleUIFinderAppLoadResult._plainTextContent
+ _OBJC_IVAR_$_SCROBrailleUILoadingView._dotCount
+ _OBJC_IVAR_$_SCROBrailleUILoadingView._text
+ _OBJC_IVAR_$_SCROBrailleUIPDFSection._bottomTitle
+ _OBJC_IVAR_$_SCROBrailleUIPDFSection._identifier
+ _OBJC_IVAR_$_SCROBrailleUIPDFSection._pageRange
+ _OBJC_IVAR_$_SCROBrailleUIPDFSection._title
+ _OBJC_IVAR_$_SCROBrailleUIPDFSection._topTitle
+ _OBJC_IVAR_$_SCROBrailleUIPlainTextView._currentRowCaptions
+ _OBJC_METACLASS_$_SCROBrailleUIFinderAppLoadResult
+ _OBJC_METACLASS_$_SCROBrailleUILoadingView
+ _OBJC_METACLASS_$_SCROBrailleUIPDFSection
+ _OBJC_METACLASS_$_SCROBrailleUIPDFSections
+ __OBJC_$_CLASS_METHODS_SCROBrailleUIPDFSections
+ __OBJC_$_INSTANCE_METHODS_SCROBrailleUIFinderAppLoadResult
+ __OBJC_$_INSTANCE_METHODS_SCROBrailleUILoadingView
+ __OBJC_$_INSTANCE_METHODS_SCROBrailleUIPDFSection
+ __OBJC_$_INSTANCE_VARIABLES_SCROBrailleUIFinderAppLoadResult
+ __OBJC_$_INSTANCE_VARIABLES_SCROBrailleUILoadingView
+ __OBJC_$_INSTANCE_VARIABLES_SCROBrailleUIPDFSection
+ __OBJC_$_PROP_LIST_SCROBrailleUIFinderAppLoadResult
+ __OBJC_$_PROP_LIST_SCROBrailleUILoadingView
+ __OBJC_$_PROP_LIST_SCROBrailleUIPDFSection
+ __OBJC_CLASS_RO_$_SCROBrailleUIFinderAppLoadResult
+ __OBJC_CLASS_RO_$_SCROBrailleUILoadingView
+ __OBJC_CLASS_RO_$_SCROBrailleUIPDFSection
+ __OBJC_CLASS_RO_$_SCROBrailleUIPDFSections
+ __OBJC_METACLASS_RO_$_SCROBrailleUIFinderAppLoadResult
+ __OBJC_METACLASS_RO_$_SCROBrailleUILoadingView
+ __OBJC_METACLASS_RO_$_SCROBrailleUIPDFSection
+ __OBJC_METACLASS_RO_$_SCROBrailleUIPDFSections
+ ___44-[SCROBrailleUIFinderApp _openViewerForBRF:]_block_invoke
+ ___44-[SCROBrailleUIFinderApp _openViewerForBRF:]_block_invoke_2
+ ___46-[SCROBrailleUIFinderApp _openPlainTextOrPDF:]_block_invoke
+ ___46-[SCROBrailleUIFinderApp _openPlainTextOrPDF:]_block_invoke_2
+ ___46-[SCROBrailleUIFinderApp _openPlainTextOrPDF:]_block_invoke_3
+ ___46-[SCROBrailleUIFinderApp _openPlainTextOrPDF:]_block_invoke_4
+ ___57-[SCROBrailleUIFinderApp _handleActionInPDFSectionsMenu:]_block_invoke
+ ___57-[SCROBrailleUIFinderApp _handleActionInPDFSectionsMenu:]_block_invoke_2
+ ___59-[SCROBrailleUIFinderApp _loadURL:inBackground:completion:]_block_invoke
+ ___69-[SCROBrailleUIFinderApp _scheduleLoadingAnimationTickForGeneration:]_block_invoke
+ ___69-[SCROBrailleUIFinderApp _scheduleLoadingAnimationTickForGeneration:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e42_v16?0"SCROBrailleUIFinderAppLoadResult"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e42_v16?0"SCROBrailleUIFinderAppLoadResult"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8s32l8w48l8
+ ___block_descriptor_64_e8_32s40bs48bs_e5_v8?0ls40l8s32l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_74_e8_32s40s48s_e42_v16?0"SCROBrailleUIFinderAppLoadResult"8ls32l8s40l8s48l8
+ _kSCROBrailleUIRequestBlockKey
+ _kSCROCaptionAttribute
+ _task_info
- +[SCROBrailleUIUtilities textFromPDFAtURL:]
- -[SCROBrailleDisplayInput currentHIDCommand]
- -[SCROBrailleDisplayInput setCurrentHIDCommand:]
- -[SCROBrailleUIApp lazyLoad]
- -[SCROBrailleUIFinderApp _openViewerForPlainText:]
- -[SCROBrailleUIFinderApp isViewerViewLoading]
- -[SCROBrailleUIFinderApp lazyLoad]
- -[SCROBrailleUIFinderApp setIsViewerViewLoading:]
- GCC_except_table1025
- GCC_except_table1089
- GCC_except_table1091
- GCC_except_table1093
- GCC_except_table1095
- GCC_except_table1162
- GCC_except_table1190
- GCC_except_table1195
- GCC_except_table1199
- GCC_except_table1202
- GCC_except_table1204
- GCC_except_table1235
- GCC_except_table1242
- GCC_except_table1374
- GCC_except_table1587
- GCC_except_table1711
- GCC_except_table1850
- GCC_except_table1852
- GCC_except_table1860
- GCC_except_table1870
- GCC_except_table1954
- GCC_except_table1999
- GCC_except_table2003
- GCC_except_table2115
- GCC_except_table2136
- GCC_except_table2141
- GCC_except_table2147
- GCC_except_table2246
- GCC_except_table2433
- GCC_except_table2451
- GCC_except_table2567
- GCC_except_table2568
- GCC_except_table2569
- GCC_except_table2573
- GCC_except_table2578
- GCC_except_table2579
- GCC_except_table2580
- GCC_except_table2581
- GCC_except_table2582
- GCC_except_table2584
- GCC_except_table2585
- GCC_except_table2586
- GCC_except_table2590
- GCC_except_table2595
- GCC_except_table2597
- GCC_except_table2600
- GCC_except_table2948
- GCC_except_table2964
- GCC_except_table2983
- GCC_except_table2984
- GCC_except_table2985
- GCC_except_table3048
- GCC_except_table3050
- GCC_except_table3052
- GCC_except_table3053
- GCC_except_table3057
- GCC_except_table444
- GCC_except_table456
- GCC_except_table488
- GCC_except_table511
- GCC_except_table512
- GCC_except_table522
- GCC_except_table524
- GCC_except_table542
- GCC_except_table543
- GCC_except_table545
- GCC_except_table548
- GCC_except_table549
- GCC_except_table552
- GCC_except_table562
- GCC_except_table582
- GCC_except_table584
- GCC_except_table585
- GCC_except_table595
- GCC_except_table601
- GCC_except_table615
- GCC_except_table616
- GCC_except_table617
- GCC_except_table618
- GCC_except_table620
- GCC_except_table624
- GCC_except_table625
- GCC_except_table631
- GCC_except_table649
- GCC_except_table650
- GCC_except_table653
- GCC_except_table851
- GCC_except_table892
- GCC_except_table894
- _OBJC_IVAR_$_SCROBrailleDisplayInput._currentHIDCommand
- _OBJC_IVAR_$_SCROBrailleUIFinderApp._isViewerViewLoading
- ___52-[SCROBrailleDisplayManager handleBrailleUIRequest:]_block_invoke_4
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
CStrings:
+ "%@\n%@\n%@"
+ "%@#%@"
+ "%@%lu%lu%lu"
+ "%lu%lu%lu"
+ "/Library/Accessibility/ktoa_u_kwa_v7.dic"
+ "Braille UI Finder: Load %lu: background load finished, error %@"
+ "Braille UI Finder: Load %lu: background load started"
+ "Braille UI Finder: Load %lu: cancelled"
+ "Braille UI Finder: Load %lu: discarding result of cancelled load"
+ "Braille UI Finder: Load %lu: dispatching background load of .%@ file"
+ "Braille UI Finder: Load %lu: presenting result"
+ "Braille UI Finder: Load %lu: requesting completion on event queue"
+ "Braille UI: Failed to reopen PDF at page %lu"
+ "Braille UI: Finished reading PDF: %lu pages, text size %llu bytes, footprint %llu KB, %.3f s"
+ "Braille UI: Ignoring PDF outline because chapter %lu spans %lu pages"
+ "Braille UI: Ignoring PDF outline with %lu usable chapters for %lu pages"
+ "Braille UI: PDF text exceeds %llu bytes after page %lu/%lu"
+ "Braille UI: Plain text locations don't match braille, captioning first row only"
+ "Braille UI: Plain text locations out of order, captioning first row only"
+ "Braille UI: Read PDF page %lu/%lu: text size %llu bytes, footprint %llu KB"
+ "Braille UI: Reading PDF %@: pages %lu to %lu of %lu, file size %llu bytes, footprint %llu KB"
+ "Braille UI: Reflowed row %lu/%lu doesn't match braille at cell %lu, captioning first row only"
+ "Braille UI: Reflowed rows cover %lu of %lu braille cells, captioning first row only"
+ "Braille UI: Split PDF of %lu pages into %lu page ranges"
+ "Braille UI: Split PDF of %lu pages into %lu sections using its outline"
+ "PDFLastSection"
+ "SCROCaptionAttribute"
+ "Title"
+ "\\p{Cf}"
+ "block"
+ "finder.loading"
+ "finder.pdf.section.bottom.format"
+ "finder.pdf.section.chapter.format"
+ "finder.pdf.section.heading.format"
+ "finder.pdf.section.pages.format"
+ "finder.pdf.section.top.format"
+ "finder.pdf.sections.menu"
+ "pages=%lu-%lu"
+ "v16@?0@\"SCROBrailleUIFinderAppLoadResult\"8"
```
