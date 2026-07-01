## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-  __TEXT.__text: 0xbd648
+  __TEXT.__text: 0xbdac4
   __TEXT.__auth_stubs: 0x2040
   __TEXT.__objc_methlist: 0x4714
-  __TEXT.__const: 0x3b0
+  __TEXT.__const: 0x3c8
   __TEXT.__cstring: 0x8ca3
-  __TEXT.__gcc_except_tab: 0x465c
-  __TEXT.__oslogstring: 0xb4c8
+  __TEXT.__gcc_except_tab: 0x4680
+  __TEXT.__oslogstring: 0xb5ed
   __TEXT.__dlopen_cstrs: 0x4a
   __TEXT.__unwind_info: 0x27a8
   __TEXT.__objc_classname: 0x5b0
-  __TEXT.__objc_methname: 0xfe97
+  __TEXT.__objc_methname: 0xfea3
   __TEXT.__objc_methtype: 0x27df
   __TEXT.__objc_stubs: 0xc960
   __DATA_CONST.__got: 0xbc0

   - /usr/lib/libutil.dylib
   Functions: 3117
   Symbols:   10544
-  CStrings:  6195
+  CStrings:  6204
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ ___block_descriptor_113_e8_32s40s48s56s64bs72r80r88r96r_e69_v44?0"SPQueryJob"8i16Q20^{__MDStoreOIDArray=}28^{__MDPlistBytes=}36ls32l8s40l8s48l8r72l8r80l8r88l8s56l8s64l8r96l8
+ _objc_msgSend$filterForDisabledBundles:logForQuery:
- ___block_descriptor_97_e8_32s40s48s56s64bs72r80r_e69_v44?0"SPQueryJob"8i16Q20^{__MDStoreOIDArray=}28^{__MDPlistBytes=}36ls32l8s40l8s64l8r72l8s48l8r80l8s56l8
- _objc_msgSend$filterForDisabledBundles:
Functions:
~ -[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:] : 2892 -> 2904
~ -[SPCoreSpotlightTask _makeDisabledBundlesQueryStringForQueryContext:] : 1148 -> 1184
~ -[SPCoreSpotlightTask addJob:] : 144 -> 408
~ -[SPCoreSpotlightTask finishWithError:] : 304 -> 488
~ -[SPCoreSpotlightTask removeJob:] : 220 -> 464
~ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.2649 : 828 -> 1236
CStrings:
+ "error=%{public}@ jobs=%lu"
+ "filterForDisabledBundles:logForQuery:"
+ "indexerCount=%lu finished=%lu notStarted=%lu"
+ "siJob=%p dataclass=%{public}@ jobs=%lu"
+ "status=%d dataclass=%{public}@ bundle=%{public}@ count=%lu started=%lu finished=%lu gatherEnded=%lu"
+ "task addJob"
+ "task finishWithError"
+ "task gather ended all"
+ "task removeJob"
+ "task results"
- "filterForDisabledBundles:"

```
