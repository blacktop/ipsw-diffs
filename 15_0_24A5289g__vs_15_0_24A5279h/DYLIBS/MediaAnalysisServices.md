## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/Versions/A/MediaAnalysisServices`

```diff

-255.67.2.0.0
-  __TEXT.__text: 0x33c98
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x3b58
+255.62.1.15.1
+  __TEXT.__text: 0x33084
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x39d0
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x2de4
-  __TEXT.__oslogstring: 0x16e7
-  __TEXT.__gcc_except_tab: 0x3848
+  __TEXT.__cstring: 0x2dce
+  __TEXT.__oslogstring: 0x1684
+  __TEXT.__gcc_except_tab: 0x3770
   __TEXT.__dlopen_cstrs: 0x297
-  __TEXT.__unwind_info: 0x15d8
-  __TEXT.__objc_classname: 0xca9
-  __TEXT.__objc_methname: 0x6c52
-  __TEXT.__objc_methtype: 0x1c83
-  __TEXT.__objc_stubs: 0x1fe0
-  __DATA_CONST.__got: 0x3f0
+  __TEXT.__unwind_info: 0x1548
+  __TEXT.__objc_classname: 0xc37
+  __TEXT.__objc_methname: 0x6aeb
+  __TEXT.__objc_methtype: 0x1c57
+  __TEXT.__objc_stubs: 0x1fc0
+  __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x1b8
-  __DATA_CONST.__objc_classlist: 0x388
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1278
+  __DATA_CONST.__objc_selrefs: 0x1238
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x358
-  __AUTH_CONST.__auth_got: 0x310
+  __DATA_CONST.__objc_superrefs: 0x330
+  __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x958
-  __AUTH_CONST.__cfstring: 0x3de0
-  __AUTH_CONST.__objc_const: 0x8f40
+  __AUTH_CONST.__cfstring: 0x3d60
+  __AUTH_CONST.__objc_const: 0x8af0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x2350
-  __DATA.__objc_ivar: 0x45c
+  __AUTH.__objc_data: 0x21c0
+  __DATA.__objc_ivar: 0x444
   __DATA.__data: 0x360
   __DATA.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1363
-  Symbols:   3465
-  CStrings:  540
+  Functions: 1335
+  Symbols:   3387
+  CStrings:  538
 
Symbols:
+ +[MADMovieCurationEntry entryWithTimeRange:highlightScore:highlight:]
+ +[MADMovieCurationEntry supportsSecureCoding]
+ +[MADMovieCurationResult resultWithMovieCurationEntries:]
+ -[MADMovieCurationEntry .cxx_destruct]
+ -[MADMovieCurationEntry description]
+ -[MADMovieCurationEntry encodeWithCoder:]
+ -[MADMovieCurationEntry highlightScore]
+ -[MADMovieCurationEntry highlight]
+ -[MADMovieCurationEntry initWithCoder:]
+ -[MADMovieCurationEntry initWithTimeRange:highlightScore:highlight:]
+ -[MADMovieCurationEntry timeRange]
+ -[MADMovieCurationResult curationEntries]
+ -[MADMovieCurationResult initWithMovieCurationEntries:]
+ OBJC_IVAR_$_MADMovieCurationEntry._highlight
+ OBJC_IVAR_$_MADMovieCurationEntry._highlightScore
+ OBJC_IVAR_$_MADMovieCurationEntry._timeRange
+ OBJC_IVAR_$_MADMovieCurationResult._curationEntries
+ _OBJC_CLASS_$_MADMovieCurationEntry
+ _OBJC_METACLASS_$_MADMovieCurationEntry
+ __OBJC_$_CLASS_METHODS_MADMovieCurationEntry
+ __OBJC_$_CLASS_PROP_LIST_MADMovieCurationEntry
+ __OBJC_$_INSTANCE_METHODS_MADMovieCurationEntry
+ __OBJC_$_INSTANCE_VARIABLES_MADMovieCurationEntry
+ __OBJC_$_PROP_LIST_MADMovieCurationEntry
+ __OBJC_CLASS_PROTOCOLS_$_MADMovieCurationEntry
+ __OBJC_CLASS_RO_$_MADMovieCurationEntry
+ __OBJC_METACLASS_RO_$_MADMovieCurationEntry
+ __os_feature_enabled_impl
+ _objc_msgSend$highlight
+ _objc_msgSend$highlightScore
+ _objc_msgSend$initWithMovieCurationEntries:
+ _objc_msgSend$initWithTimeRange:highlightScore:highlight:
- +[MADExposureImageRequest allocWithZone:]
- +[MADExposureImageRequest allocWithZone:].cold.1
- +[MADExposureResult resultWithExposureScore:]
- +[MADExposureResult supportsSecureCoding]
- +[MADMovieCurationResult resultWithSummaryEntries:highlightEntries:curationScoreEntries:]
- +[MADMovieCurationScoreEntry entryWithTimeRange:score:]
- +[MADMovieCurationScoreEntry supportsSecureCoding]
- +[MADMovieHighlightEntry entryWithTimeRange:score:attributes:]
- +[MADMovieHighlightEntry supportsSecureCoding]
- +[MADSharpnessImageRequest allocWithZone:]
- +[MADSharpnessImageRequest allocWithZone:].cold.1
- +[MADSharpnessResult resultWithSharpnessScore:]
- +[MADSharpnessResult supportsSecureCoding]
- -[MADExposureResult description]
- -[MADExposureResult encodeWithCoder:]
- -[MADExposureResult exposureScore]
- -[MADExposureResult initWithCoder:]
- -[MADExposureResult initWithExposureScore:]
- -[MADMovieCurationResult curationScoreEntries]
- -[MADMovieCurationResult highlightEntries]
- -[MADMovieCurationResult initWithSummaryEntries:highlightEntries:curationScoreEntries:]
- -[MADMovieCurationResult summaryEntries]
- -[MADMovieCurationScoreEntry description]
- -[MADMovieCurationScoreEntry encodeWithCoder:]
- -[MADMovieCurationScoreEntry initWithCoder:]
- -[MADMovieCurationScoreEntry initWithTimeRange:score:]
- -[MADMovieCurationScoreEntry score]
- -[MADMovieCurationScoreEntry timeRange]
- -[MADMovieHighlightEntry .cxx_destruct]
- -[MADMovieHighlightEntry attributes]
- -[MADMovieHighlightEntry description]
- -[MADMovieHighlightEntry encodeWithCoder:]
- -[MADMovieHighlightEntry initWithCoder:]
- -[MADMovieHighlightEntry initWithTimeRange:score:attributes:]
- -[MADMovieHighlightEntry score]
- -[MADMovieHighlightEntry timeRange]
- -[MADSharpnessResult description]
- -[MADSharpnessResult encodeWithCoder:]
- -[MADSharpnessResult initWithCoder:]
- -[MADSharpnessResult initWithSharpnessScore:]
- -[MADSharpnessResult sharpnessScore]
- GCC_except_table19
- GCC_except_table20
- GCC_except_table21
- OBJC_IVAR_$_MADExposureResult._exposureScore
- OBJC_IVAR_$_MADMovieCurationResult._curationScoreEntries
- OBJC_IVAR_$_MADMovieCurationResult._highlightEntries
- OBJC_IVAR_$_MADMovieCurationResult._summaryEntries
- OBJC_IVAR_$_MADMovieCurationScoreEntry._score
- OBJC_IVAR_$_MADMovieCurationScoreEntry._timeRange
- OBJC_IVAR_$_MADMovieHighlightEntry._attributes
- OBJC_IVAR_$_MADMovieHighlightEntry._score
- OBJC_IVAR_$_MADMovieHighlightEntry._timeRange
- OBJC_IVAR_$_MADSharpnessResult._sharpnessScore
- _OBJC_CLASS_$_MADExposureImageRequest
- _OBJC_CLASS_$_MADExposureResult
- _OBJC_CLASS_$_MADMovieCurationScoreEntry
- _OBJC_CLASS_$_MADMovieHighlightEntry
- _OBJC_CLASS_$_MADSharpnessImageRequest
- _OBJC_CLASS_$_MADSharpnessResult
- _OBJC_METACLASS_$_MADExposureImageRequest
- _OBJC_METACLASS_$_MADExposureResult
- _OBJC_METACLASS_$_MADMovieCurationScoreEntry
- _OBJC_METACLASS_$_MADMovieHighlightEntry
- _OBJC_METACLASS_$_MADSharpnessImageRequest
- _OBJC_METACLASS_$_MADSharpnessResult
- __OBJC_$_CLASS_METHODS_MADExposureImageRequest
- __OBJC_$_CLASS_METHODS_MADExposureResult
- __OBJC_$_CLASS_METHODS_MADMovieCurationScoreEntry
- __OBJC_$_CLASS_METHODS_MADMovieHighlightEntry
- __OBJC_$_CLASS_METHODS_MADSharpnessImageRequest
- __OBJC_$_CLASS_METHODS_MADSharpnessResult
- __OBJC_$_CLASS_PROP_LIST_MADMovieCurationScoreEntry
- __OBJC_$_CLASS_PROP_LIST_MADMovieHighlightEntry
- __OBJC_$_INSTANCE_METHODS_MADExposureResult
- __OBJC_$_INSTANCE_METHODS_MADMovieCurationScoreEntry
- __OBJC_$_INSTANCE_METHODS_MADMovieHighlightEntry
- __OBJC_$_INSTANCE_METHODS_MADSharpnessResult
- __OBJC_$_INSTANCE_VARIABLES_MADExposureResult
- __OBJC_$_INSTANCE_VARIABLES_MADMovieCurationScoreEntry
- __OBJC_$_INSTANCE_VARIABLES_MADMovieHighlightEntry
- __OBJC_$_INSTANCE_VARIABLES_MADSharpnessResult
- __OBJC_$_PROP_LIST_MADExposureResult
- __OBJC_$_PROP_LIST_MADMovieCurationScoreEntry
- __OBJC_$_PROP_LIST_MADMovieHighlightEntry
- __OBJC_$_PROP_LIST_MADSharpnessResult
- __OBJC_CLASS_PROTOCOLS_$_MADMovieCurationScoreEntry
- __OBJC_CLASS_PROTOCOLS_$_MADMovieHighlightEntry
- __OBJC_CLASS_RO_$_MADExposureImageRequest
- __OBJC_CLASS_RO_$_MADExposureResult
- __OBJC_CLASS_RO_$_MADMovieCurationScoreEntry
- __OBJC_CLASS_RO_$_MADMovieHighlightEntry
- __OBJC_CLASS_RO_$_MADSharpnessImageRequest
- __OBJC_CLASS_RO_$_MADSharpnessResult
- __OBJC_METACLASS_RO_$_MADExposureImageRequest
- __OBJC_METACLASS_RO_$_MADExposureResult
- __OBJC_METACLASS_RO_$_MADMovieCurationScoreEntry
- __OBJC_METACLASS_RO_$_MADMovieHighlightEntry
- __OBJC_METACLASS_RO_$_MADSharpnessImageRequest
- __OBJC_METACLASS_RO_$_MADSharpnessResult
- _objc_msgSend$initWithExposureScore:
- _objc_msgSend$initWithSharpnessScore:
- _objc_msgSend$initWithSummaryEntries:highlightEntries:curationScoreEntries:
- _objc_msgSend$initWithTimeRange:score:
- _objc_msgSend$initWithTimeRange:score:attributes:
CStrings:
+ "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysisServices/ComputeService/MADCoreMLResult.mm"
+ "Highlight"
+ "HighlightScore"
+ "MediaAnalysis"
+ "MovieCurationEntries"
+ "SearchUnifiedEmbeddingMD4"
- "%!@(MISSING): %!f(MISSING)>"
- "%!@(MISSING): %!l(MISSING)u count, "
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysisServices/ComputeService/MADCoreMLResult.mm"
- "CurationScoreEntries"
- "ExposureScore"
- "HighlightEntries"
- "SharpnessScore"
- "SummaryEntries"

```
