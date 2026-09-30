## SpotlightUIInternal

> `/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal`

```diff

-236.0.21.100.0
-  __TEXT.__text: 0x4f1d4
-  __TEXT.__objc_methlist: 0x5d28
+236.0.21.104.0
+  __TEXT.__text: 0x4f43c
+  __TEXT.__objc_methlist: 0x5d50
   __TEXT.__const: 0x13c0
-  __TEXT.__cstring: 0x13c2
-  __TEXT.__oslogstring: 0x132a
+  __TEXT.__cstring: 0x13e2
+  __TEXT.__oslogstring: 0x133a
   __TEXT.__gcc_except_tab: 0x27c
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x54

   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift_as_cont: 0x8c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x1600
+  __TEXT.__unwind_info: 0x1608
   __TEXT.__eh_frame: 0xc70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4320
+  __DATA_CONST.__objc_selrefs: 0x4340
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__got: 0xa90
   __AUTH_CONST.__const: 0xcc8
-  __AUTH_CONST.__cfstring: 0x1900
+  __AUTH_CONST.__cfstring: 0x1920
   __AUTH_CONST.__objc_const: 0x92a0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2058
-  Symbols:   4841
-  CStrings:  367
+  Functions: 2062
+  Symbols:   4849
+  CStrings:  368
 
Symbols:
+ -[SPUISearchHeader updateCompletionVisibility]
+ -[SPUISearchViewController presentationSource]
+ -[SPUIUnifiedFieldViewController topPocketHeight]
+ GCC_except_table94
+ ___70-[SPUISearchViewController searchViewWillPresentFromSource:isOverApp:]_block_invoke_4
+ _objc_msgSend$initWithQueryID:queryLength:topHitIsElevatable:queryFinished:priorityComplete:resultQualityTier:
+ _objc_msgSend$restore
+ _objc_msgSend$safeAreaInsets
+ _objc_msgSend$setPresentationSource:
+ _objc_msgSend$topPocketHeight
+ _objc_msgSend$updateCompletionVisibility
- GCC_except_table92
- _objc_msgSend$initWithQueryID:queryLength:isSiriWorthy:topHitIsElevatable:hasResults:queryFinished:priorityComplete:
- _objc_msgSend$restoreWithDisplayState:
CStrings:
+ "DisplayPolicy signals: query=%{sensitive}@ qid=%lu len=%ld elevatable=%d tier=%ld rawTier=%ld hasTopHitSection=%d firstBundle=%{sensitive}@ firstResultBundle=%{sensitive}@ firstResultCount=%lu priorityComplete=%d complete=%d sectionCount=%lu"
+ "com.apple.spotlight.tophits"
- "DisplayPolicy signals: query=%{sensitive}@ qid=%lu len=%ld elevatable=%d isSiriWorthy=%d firstBundle=%{sensitive}@ firstResultBundle=%{sensitive}@ firstResultCount=%lu hasTopHits=%d hasTopHitResult=%d complete=%d sectionCount=%lu"
```
