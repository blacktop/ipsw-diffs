## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/Versions/A/NewsCore`

```diff

-5934.0.2.0.0
-  __TEXT.__text: 0x42460c
-  __TEXT.__objc_methlist: 0x34eb8
-  __TEXT.__const: 0xd578
-  __TEXT.__swift5_typeref: 0x409c
+5971.0.0.0.0
+  __TEXT.__text: 0x423834
+  __TEXT.__objc_methlist: 0x34ee8
+  __TEXT.__const: 0xd668
+  __TEXT.__swift5_typeref: 0x40c8
   __TEXT.__swift5_capture: 0xe28
-  __TEXT.__oslogstring: 0x18269
-  __TEXT.__swift5_fieldmd: 0x2c8c
-  __TEXT.__constg_swiftt: 0x2d90
-  __TEXT.__swift5_reflstr: 0x20c0
-  __TEXT.__swift5_protos: 0x5c
-  __TEXT.__swift5_proto: 0x964
-  __TEXT.__swift5_types: 0x3ec
+  __TEXT.__oslogstring: 0x18309
+  __TEXT.__swift5_fieldmd: 0x2cc4
+  __TEXT.__constg_swiftt: 0x2e18
+  __TEXT.__swift5_reflstr: 0x20e0
+  __TEXT.__swift5_protos: 0x60
+  __TEXT.__swift5_proto: 0x968
+  __TEXT.__swift5_types: 0x3f0
   __TEXT.__swift_as_entry: 0x2cc
   __TEXT.__swift_as_ret: 0x308
   __TEXT.__swift_as_cont: 0x4e4
-  __TEXT.__cstring: 0x58068
+  __TEXT.__cstring: 0x58048
   __TEXT.__swift5_assocty: 0x300
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__gcc_except_tab: 0x49dc
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x280
-  __TEXT.__unwind_info: 0xe4a8
-  __TEXT.__eh_frame: 0x8a64
+  __TEXT.__unwind_info: 0xe4d0
+  __TEXT.__eh_frame: 0x8ab4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6da0
-  __DATA_CONST.__objc_classlist: 0x1ca0
+  __DATA_CONST.__const: 0x6d90
+  __DATA_CONST.__objc_classlist: 0x1cb0
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x920
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14a18
+  __DATA_CONST.__objc_selrefs: 0x14a78
   __DATA_CONST.__objc_protorefs: 0x270
-  __DATA_CONST.__objc_superrefs: 0x15a0
+  __DATA_CONST.__objc_superrefs: 0x15a8
   __DATA_CONST.__objc_arraydata: 0x2a90
   __DATA_CONST.__got: 0x2a70
-  __AUTH_CONST.__const: 0x18620
+  __AUTH_CONST.__const: 0x18628
   __AUTH_CONST.__cfstring: 0x31c40
-  __AUTH_CONST.__objc_const: 0x79110
+  __AUTH_CONST.__objc_const: 0x79390
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x6c0
   __AUTH_CONST.__objc_intobj: 0x13f8
   __AUTH_CONST.__objc_dictobj: 0xc30
   __AUTH_CONST.__objc_doubleobj: 0x120
-  __AUTH_CONST.__auth_got: 0x1c10
+  __AUTH_CONST.__auth_got: 0x1c28
   __AUTH_CONST.__auth_ptr: 0xc00
-  __AUTH.__objc_data: 0x6a0
-  __AUTH.__data: 0x910
-  __DATA.__objc_ivar: 0x4530
-  __DATA.__data: 0x6f78
-  __DATA.__bss: 0x10a98
-  __DATA.__common: 0x178
-  __DATA_DIRTY.__objc_ivar: 0xfb4
-  __DATA_DIRTY.__objc_data: 0x11b20
-  __DATA_DIRTY.__data: 0x2480
-  __DATA_DIRTY.__common: 0x320
-  __DATA_DIRTY.__bss: 0x3ff0
+  __AUTH.__objc_data: 0x570
+  __AUTH.__data: 0x360
+  __DATA.__objc_ivar: 0x4540
+  __DATA.__data: 0x6c58
+  __DATA.__bss: 0xe888
+  __DATA.__common: 0x130
+  __DATA_DIRTY.__objc_ivar: 0xfa4
+  __DATA_DIRTY.__objc_data: 0x11ca0
+  __DATA_DIRTY.__data: 0x2de8
+  __DATA_DIRTY.__common: 0x368
+  __DATA_DIRTY.__bss: 0x61d0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24470
-  Symbols:   44423
-  CStrings:  10468
+  Functions: 24475
+  Symbols:   44462
+  CStrings:  10470
 
Symbols:
+ +[FCPrivateDataController requiresHighPrioritySync]
+ +[FCPublisherGroupEngagement supportsSecureCoding]
+ +[FCPuzzleHistory requiresHighPrioritySync]
+ -[CKRecord(FCCKEncryption) fc_allAndChangedKeys]
+ -[FCMutableTodayPrivateData setPublisherGroupEngagement:]
+ -[FCNewsAppConfig todayWidgetComputationalGraphBestOfEnabled]
+ -[FCPrivateDataController _qualityOfServiceForNextSync]
+ -[FCPublisherGroupEngagement curatedClicks]
+ -[FCPublisherGroupEngagement curatedImpressions]
+ -[FCPublisherGroupEngagement encodeWithCoder:]
+ -[FCPublisherGroupEngagement initWithCoder:]
+ -[FCPublisherGroupEngagement initWithCuratedClicks:curatedImpressions:personalizedClicks:personalizedImpressions:]
+ -[FCPublisherGroupEngagement init]
+ -[FCPublisherGroupEngagement personalizedClicks]
+ -[FCPublisherGroupEngagement personalizedImpressions]
+ -[FCPublisherGroupEngagement setCuratedClicks:]
+ -[FCPublisherGroupEngagement setCuratedImpressions:]
+ -[FCPublisherGroupEngagement setPersonalizedClicks:]
+ -[FCPublisherGroupEngagement setPersonalizedImpressions:]
+ -[FCReadingHistory dislikeDatesByArticleID]
+ -[FCTodayPrivateData publisherGroupEngagement]
+ -[NTPBReadingHistoryItem(FCReadingHistory) dislikedAt]
+ -[NTPBReadingHistoryItem(FCReadingHistory) setDislikedAt:]
+ GCC_except_table131
+ GCC_except_table81
+ GCC_except_table87
+ GCC_except_table95
+ OBJC_IVAR_$_FCPublisherGroupEngagement._curatedClicks
+ OBJC_IVAR_$_FCPublisherGroupEngagement._curatedImpressions
+ OBJC_IVAR_$_FCPublisherGroupEngagement._personalizedClicks
+ OBJC_IVAR_$_FCPublisherGroupEngagement._personalizedImpressions
+ _FCWidgetComputationalGraphBestOfEnabledSharedPreferenceKey
+ _OBJC_CLASS_$_FCPublisherGroupEngagement
+ _OBJC_METACLASS_$_FCPublisherGroupEngagement
+ __DATA__TtC8NewsCore31DropboxPublisherGroupEngagement
+ __IVARS__TtC8NewsCore31DropboxPublisherGroupEngagement
+ __METACLASS_DATA__TtC8NewsCore31DropboxPublisherGroupEngagement
+ __OBJC_$_CLASS_METHODS_FCPublisherGroupEngagement
+ __OBJC_$_CLASS_PROP_LIST_FCPublisherGroupEngagement
+ __OBJC_$_INSTANCE_METHODS_CKRecord(FCAdditions|FCCKEncryption)
+ __OBJC_$_INSTANCE_METHODS_FCPublisherGroupEngagement
+ __OBJC_$_INSTANCE_METHODS_NSMutableArray(FCAdditions|FCAdditions_NSString)
+ __OBJC_$_INSTANCE_VARIABLES_FCPublisherGroupEngagement
+ __OBJC_$_PROP_LIST_FCPublisherGroupEngagement
+ __OBJC_CATEGORY_PROTOCOLS_$_NSMutableArray_$_FCAdditions
+ __OBJC_CLASS_PROTOCOLS_$_FCPublisherGroupEngagement
+ __OBJC_CLASS_RO_$_FCPublisherGroupEngagement
+ __OBJC_METACLASS_RO_$_FCPublisherGroupEngagement
+ ___43-[FCReadingHistory dislikeDatesByArticleID]_block_invoke
+ _objc_msgSend$dislikedAt
+ _objc_msgSend$dislikedDate
+ _objc_msgSend$fc_allAndChangedKeys
+ _objc_msgSend$initWithCuratedClicks:curatedImpressions:personalizedClicks:personalizedImpressions:
+ _objc_msgSend$publisherGroupEngagement
+ _objc_msgSend$requiresHighPrioritySync
+ _objc_msgSend$setDislikedAt:
+ _objc_msgSend$setDislikedDate:
+ _swift_getOpaqueTypeConformance2
+ _symbolic $s8NewsCore33PublisherGroupEngagementProvidingP
+ _symbolic SDySSSo26FCPublisherGroupEngagementCGSg
+ _symbolic So12FCRecipeItemC
+ _symbolic _____ 8NewsCore31DropboxPublisherGroupEngagementC
+ _symbolic _____ So13FCAssetHandleC8NewsCoreE6ErrorsO
+ _symbolic _____y_Qo_ 8NewsCore18RecipeItemDatabaseC03allC5Items5order6filter5limitQrAA0cD5OrderO_AA0cD6FilterOSiSgtKFQO
+ get_witness_table s15LazyMapSequenceVys0a6FilterC0VyABy5TeaDB6CursorCy8NewsCore16RecipeItemEntityVGSo08FCRecipeK0CSgGGAMGSTHPyHC
- -[FCArticleRecordSource setArticleTagMetadataRecordKeys:]
- -[FCArticleRecordSource setTopicFlagsRecordKeys:]
- -[FCNewsAppConfig userSegmentationInWidgetAllowed]
- -[FCNewsTabiFeedPersonalizationConfiguration nonMtBundleOutputConfiguration]
- -[FCNewsTabiFeedPersonalizationConfiguration nonMtNonBundleOutputConfiguration]
- -[FCNewsTabiFeedPersonalizationConfiguration setNonMtBundleOutputConfiguration:]
- -[FCNewsTabiFeedPersonalizationConfiguration setNonMtNonBundleOutputConfiguration:]
- GCC_except_table129
- GCC_except_table77
- GCC_except_table91
- _FCUserSegmentationEnableWidgetConfigSharedPreferenceKey
- __OBJC_$_CATEGORY_INSTANCE_METHODS_CKRecord_$_FCAdditions
- __OBJC_$_INSTANCE_METHODS_NSMutableArray(FCAdditions|FCAdditions_NSString|FCAdditions|FCAdditions_NSString)
- __OBJC_CLASS_PROTOCOLS_$_NSMutableArray(FCAdditions|FCAdditions_NSString|FCAdditions|FCAdditions_NSString)
- ___45-[FCArticleRecordSource topicFlagsRecordKeys]_block_invoke_2
- ___53-[FCArticleRecordSource articleTagMetadataRecordKeys]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48s_e14_"NSArray"8?0l
- _kFCNewsTabiFeedPersonalizationConfigurationNonMTBundleOutputConfigurationKey
- _kFCNewsTabiFeedPersonalizationConfigurationNonMTNonBundleOutputConfigurationKey
- _objc_msgSend$nonMtBundleOutputConfiguration
- _objc_msgSend$nonMtNonBundleOutputConfiguration
- _symbolic SDyS2S_So13FCFeedContextCtG
- _symbolic _____ So13FCAssetHandleC8NewsCoreE6Errors33_DDF6DEB4B5B520D606B58B79E5284D7BLLO
- _symbolic _____yS2S_So13FCFeedContextCtG s18_DictionaryStorageC
- _symbolic _____y_____G 5TeaDB6CursorC 8NewsCore16RecipeItemEntityV
- _symbolic _____y______G 5TeaDB6CursorC8IteratorC 8NewsCore16RecipeItemEntityV
CStrings:
+ "FCTodayWidgetDropboxDataPublisherGroupEngagementDataDictionaryKey"
+ "curatedClicks"
+ "curatedImpressions"
+ "failed to decode persisted content archive, archivePath=%{public}@, error=%{public}@"
+ "persisted content archive is missing or unreadable, archivePath=%{public}@"
+ "personalizedClicks"
+ "personalizedImpressions"
+ "todayWidgetComputationalGraphBestOfEnabled"
+ "widget_computational_graph_best_of_enabled"
- "\n\tnonMtBundleOutputConfiguration: %@"
- "\n\tnonMtNonBundleOutputConfiguration: %@"
- "articleLinkBehaviorImprovementsEnabledLevel"
- "enable_widget_config_user_segmentation"
- "nonMtBundleOutputConfiguration"
- "nonMtNonBundleOutputConfiguration"
- "userSegmentationInWidgetAllowed"
```
