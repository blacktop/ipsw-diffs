## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore`

```diff

-866.3.1.0.0
-  __TEXT.__text: 0xaed5c
-  __TEXT.__objc_methlist: 0x8c20
-  __TEXT.__const: 0x2b44
-  __TEXT.__cstring: 0x50b3
+866.3.3.0.0
+  __TEXT.__text: 0xafe1c
+  __TEXT.__objc_methlist: 0x8d30
+  __TEXT.__const: 0x2b34
+  __TEXT.__cstring: 0x5193
   __TEXT.__oslogstring: 0x141e
   __TEXT.__gcc_except_tab: 0xfdc
   __TEXT.__ustring: 0x118
-  __TEXT.__constg_swiftt: 0x18fc
-  __TEXT.__swift5_typeref: 0x1012
-  __TEXT.__swift5_reflstr: 0x12d2
-  __TEXT.__swift5_fieldmd: 0x1118
+  __TEXT.__constg_swiftt: 0x193c
+  __TEXT.__swift5_typeref: 0x1026
+  __TEXT.__swift5_reflstr: 0x1342
+  __TEXT.__swift5_fieldmd: 0x1170
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x270
   __TEXT.__swift5_proto: 0x16c
-  __TEXT.__swift5_types: 0x118
-  __TEXT.__swift5_capture: 0x748
-  __TEXT.__swift_as_entry: 0x70
-  __TEXT.__swift_as_ret: 0x60
-  __TEXT.__swift_as_cont: 0x108
+  __TEXT.__swift5_types: 0x11c
+  __TEXT.__swift5_capture: 0x710
+  __TEXT.__swift_as_entry: 0x6c
+  __TEXT.__swift_as_ret: 0x5c
+  __TEXT.__swift_as_cont: 0xfc
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x41d0
-  __TEXT.__eh_frame: 0x1910
+  __TEXT.__unwind_info: 0x41c8
+  __TEXT.__eh_frame: 0x1828
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2350
+  __DATA_CONST.__const: 0x2380
   __DATA_CONST.__objc_classlist: 0x518
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d78
+  __DATA_CONST.__objc_selrefs: 0x3e28
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x330
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__got: 0x988
-  __AUTH_CONST.__const: 0x40a0
-  __AUTH_CONST.__cfstring: 0x55a0
-  __AUTH_CONST.__objc_const: 0xe910
+  __AUTH_CONST.__const: 0x4058
+  __AUTH_CONST.__cfstring: 0x5780
+  __AUTH_CONST.__objc_const: 0xeae0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x11e8
+  __AUTH_CONST.__auth_got: 0x1200
   __AUTH.__objc_data: 0x710
-  __DATA.__objc_ivar: 0x7d0
-  __DATA.__data: 0x12f0
+  __AUTH.__data: 0x90
+  __DATA.__objc_ivar: 0x7f4
+  __DATA.__data: 0x1330
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x4400
+  __DATA_DIRTY.__objc_data: 0x4408
   __DATA_DIRTY.__data: 0x1250
   __DATA_DIRTY.__bss: 0x488
   __DATA_DIRTY.__common: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5430
-  Symbols:   5825
-  CStrings:  1138
+  Functions: 5456
+  Symbols:   5862
+  CStrings:  1153
 
Symbols:
+ +[TPSAnalyticsEventSearchResultSelected eventWithSearchID:searchTerm:articleID:source:]
+ -[TPSAnalyticsEventSearchPerformed _addIdentifiersToEventRepresentation:]
+ -[TPSAnalyticsEventSearchPerformed deShown]
+ -[TPSAnalyticsEventSearchPerformed identifier]
+ -[TPSAnalyticsEventSearchPerformed numArticles]
+ -[TPSAnalyticsEventSearchPerformed numFlows]
+ -[TPSAnalyticsEventSearchPerformed numTips]
+ -[TPSAnalyticsEventSearchPerformed numTopics]
+ -[TPSAnalyticsEventSearchPerformed resultType]
+ -[TPSAnalyticsEventSearchPerformed secondaryIdentifier]
+ -[TPSAnalyticsEventSearchPerformed setDeShown:]
+ -[TPSAnalyticsEventSearchPerformed setIdentifier:]
+ -[TPSAnalyticsEventSearchPerformed setNumArticles:]
+ -[TPSAnalyticsEventSearchPerformed setNumFlows:]
+ -[TPSAnalyticsEventSearchPerformed setNumTips:]
+ -[TPSAnalyticsEventSearchPerformed setNumTopics:]
+ -[TPSAnalyticsEventSearchPerformed setResultType:]
+ -[TPSAnalyticsEventSearchPerformed setSecondaryIdentifier:]
+ -[TPSAnalyticsEventSearchResultSelected _initWithSearchID:searchTerm:articleID:source:]
+ -[TPSAnalyticsEventSearchResultSelected articleID]
+ -[TPSAnalyticsEventSearchResultSelected resultType]
+ -[TPSAnalyticsEventSearchResultSelected setArticleID:]
+ -[TPSAnalyticsEventSearchResultSelected setResultType:]
+ -[TPSAnalyticsEventSearchResultSelected setSource:]
+ -[TPSAnalyticsEventSearchResultSelected source]
+ -[TPSCommonDefines rolloutBucket]
+ -[TPSCommonDefines setRolloutBucket:]
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchPerformed._deShown
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchPerformed._identifier
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchPerformed._numArticles
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchPerformed._numFlows
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchPerformed._numTips
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchPerformed._numTopics
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchPerformed._resultType
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchPerformed._secondaryIdentifier
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchResultSelected._articleID
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchResultSelected._resultType
+ _OBJC_IVAR_$_TPSAnalyticsEventSearchResultSelected._source
+ _TPSAnalyticsSearchResultSourceDeviceExpertAnswer
+ _TPSAnalyticsSearchResultSourceResultsList
+ _TPSAnalyticsSearchResultTypeArticle
+ _TPSAnalyticsSearchResultTypeSupportFlow
+ _TPSAnalyticsSearchResultTypeTip
+ _TPSAnalyticsSearchResultTypeTopic
+ _symbolic _____ 8TipsCore28LearnMoreAnalyticsControllerC17PendingUsedSearch33_ACA61E624AC8C1EE2DA2ACFA5CDF23E4LLV
+ _symbolic _____ s15ContinuousClockV7InstantV
+ _symbolic _____Sg 8TipsCore28LearnMoreAnalyticsControllerC17PendingUsedSearch33_ACA61E624AC8C1EE2DA2ACFA5CDF23E4LLV
- +[TPSFeatureFlags allowModernTipView]
- -[TPSAnalyticsEventSearchPerformed collectionID]
- -[TPSAnalyticsEventSearchPerformed setCollectionID:]
- -[TPSAnalyticsEventSearchPerformed setTipID:]
- -[TPSAnalyticsEventSearchPerformed tipID]
- _OBJC_IVAR_$_TPSAnalyticsEventSearchPerformed._collectionID
- _OBJC_IVAR_$_TPSAnalyticsEventSearchPerformed._tipID
- ___37+[TPSFeatureFlags allowModernTipView]_block_invoke
- _allowModernTipView.allowFeature
- _allowModernTipView.predicate
CStrings:
+ ", containsChinaPolicy: "
+ "TPSOverrideRolloutBucket"
+ "TPSRolloutBucket"
+ "article"
+ "article_id"
+ "de_shown"
+ "device_expert_answer"
+ "flow"
+ "num_articles"
+ "num_flows"
+ "num_tips"
+ "num_topics"
+ "result_type"
+ "results_list"
+ "secondary_identifier"
+ "source"
+ "topic"
- "\t"
- "modern_tip_view"
```
