## PodcastsFoundation

> `/System/Library/PrivateFrameworks/PodcastsFoundation.framework/Versions/A/PodcastsFoundation`

```diff

-4024.100.72.0.0
-  __TEXT.__text: 0x448ef8
-  __TEXT.__auth_stubs: 0x4860
-  __TEXT.__objc_methlist: 0x9720
-  __TEXT.__const: 0x27340
-  __TEXT.__oslogstring: 0xd94b
-  __TEXT.__cstring: 0x1639e
-  __TEXT.__gcc_except_tab: 0xb6c
+4024.100.78.0.0
+  __TEXT.__text: 0x45e3fc
+  __TEXT.__auth_stubs: 0x48f0
+  __TEXT.__objc_methlist: 0x98f0
+  __TEXT.__const: 0x276e0
+  __TEXT.__oslogstring: 0xdd0b
+  __TEXT.__cstring: 0x1692e
+  __TEXT.__gcc_except_tab: 0xbb8
   __TEXT.__ustring: 0x54
   __TEXT.__dlopen_cstrs: 0xca
-  __TEXT.__swift5_typeref: 0x146a2
-  __TEXT.__constg_swiftt: 0xd110
-  __TEXT.__swift5_reflstr: 0xa816
-  __TEXT.__swift5_fieldmd: 0xc404
+  __TEXT.__swift5_typeref: 0x14f00
+  __TEXT.__constg_swiftt: 0xd2ec
+  __TEXT.__swift5_reflstr: 0xab56
+  __TEXT.__swift5_fieldmd: 0xc614
   __TEXT.__swift5_builtin: 0x53c
-  __TEXT.__swift5_assocty: 0x17f8
-  __TEXT.__swift5_proto: 0x1db0
-  __TEXT.__swift5_types: 0xd00
-  __TEXT.__swift5_capture: 0x6604
-  __TEXT.__swift5_protos: 0x178
+  __TEXT.__swift5_assocty: 0x1840
+  __TEXT.__swift5_proto: 0x1dd0
+  __TEXT.__swift5_types: 0xd1c
+  __TEXT.__swift5_capture: 0x65e4
+  __TEXT.__swift5_protos: 0x180
   __TEXT.__swift5_mpenum: 0x128
-  __TEXT.__unwind_info: 0xfcb0
-  __TEXT.__eh_frame: 0xe334
-  __TEXT.__objc_classname: 0xe8a
-  __TEXT.__objc_methname: 0x18eeb
-  __TEXT.__objc_methtype: 0x2c48
-  __TEXT.__objc_stubs: 0xe180
-  __DATA_CONST.__got: 0x1468
-  __DATA_CONST.__const: 0x2a70
-  __DATA_CONST.__objc_classlist: 0x990
+  __TEXT.__unwind_info: 0x10098
+  __TEXT.__eh_frame: 0xea4c
+  __TEXT.__objc_classname: 0xef1
+  __TEXT.__objc_methname: 0x19162
+  __TEXT.__objc_methtype: 0x2cfc
+  __TEXT.__objc_stubs: 0xe260
+  __DATA_CONST.__got: 0x14a8
+  __DATA_CONST.__const: 0x2aa0
+  __DATA_CONST.__objc_classlist: 0x9a0
   __DATA_CONST.__objc_catlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x358
+  __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6198
-  __DATA_CONST.__objc_protorefs: 0x1c8
-  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_selrefs: 0x6228
+  __DATA_CONST.__objc_protorefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x2440
-  __AUTH_CONST.__auth_ptr: 0x20e0
-  __AUTH_CONST.__const: 0x25ca0
-  __AUTH_CONST.__cfstring: 0x9d80
-  __AUTH_CONST.__objc_const: 0x268f8
+  __AUTH_CONST.__auth_got: 0x2488
+  __AUTH_CONST.__auth_ptr: 0x2370
+  __AUTH_CONST.__const: 0x26040
+  __AUTH_CONST.__cfstring: 0x9ea0
+  __AUTH_CONST.__objc_const: 0x26d88
   __AUTH_CONST.__objc_intobj: 0xaf8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x8a90
-  __AUTH.__data: 0x8800
-  __DATA.__objc_ivar: 0x524
-  __DATA.__data: 0xcc28
-  __DATA.__bss: 0x36140
+  __AUTH.__objc_data: 0x8a30
+  __AUTH.__data: 0x88d0
+  __DATA.__objc_ivar: 0x534
+  __DATA.__data: 0xcfd8
+  __DATA.__bss: 0x36240
   __DATA.__common: 0x120
   __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__data: 0x1a0

   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices
   - /System/Library/PrivateFrameworks/AssertionServices.framework/Versions/A/AssertionServices
   - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices
+  - /System/Library/PrivateFrameworks/CacheDelete.framework/Versions/A/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/Koa.framework/Versions/A/Koa

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24395
-  Symbols:   14411
-  CStrings:  3440
+  Functions: 24655
+  Symbols:   14560
+  CStrings:  3480
 
Symbols:
+ -[CacheDeleteNotificationObserver .cxx_destruct]
+ -[CacheDeleteNotificationObserver _onQueueBeginObserving]
+ -[CacheDeleteNotificationObserver _onQueueConfigurePurgeMarkerForVolume:]
+ -[CacheDeleteNotificationObserver _onQueueProcessNotifications:]
+ -[CacheDeleteNotificationObserver _onQueueSubscribeToNotificationsForVolume:]
+ -[CacheDeleteNotificationObserver beginObserving]
+ -[CacheDeleteNotificationObserver delegate]
+ -[CacheDeleteNotificationObserver initWithDelegate:observedPaths:notificationQueue:]
+ -[CacheDeleteNotificationObserver notificationQueue]
+ -[CacheDeleteNotificationObserver observedPaths]
+ OBJC_IVAR_$_CacheDeleteNotificationObserver._delegate
+ OBJC_IVAR_$_CacheDeleteNotificationObserver._formatter
+ OBJC_IVAR_$_CacheDeleteNotificationObserver._notificationQueue
+ OBJC_IVAR_$_CacheDeleteNotificationObserver._observedPaths
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CacheDeleteEnumerateRemovedFilesInDirectories
+ _CacheDeleteInitPurgeMarker
+ _CacheDeleteRegisterPurgeNotification
+ _MTApplicationSceneDidDisconnectNotification
+ _NSLocalizedFailureReasonErrorKey
+ _NSManagedObjectContextDidSaveNotification
+ _OBJC_CLASS_$_CacheDeleteNotificationObserver
+ _OBJC_CLASS_$__TtC18PodcastsFoundation24CacheDeleteNotifications
+ _OBJC_METACLASS_$_CacheDeleteNotificationObserver
+ _OBJC_METACLASS_$__TtC18PodcastsFoundation24CacheDeleteNotifications
+ _PF_APFSIOC_CLEAR_PURGEABLE
+ _PROTOCOLS__TtC18PodcastsFoundation24CacheDeleteNotifications.2
+ __DATA__TtC18PodcastsFoundation24CacheDeleteNotifications
+ __INSTANCE_METHODS__TtC18PodcastsFoundation24CacheDeleteNotifications
+ __IVARS__TtC18PodcastsFoundation24CacheDeleteNotifications
+ __METACLASS_DATA__TtC18PodcastsFoundation24CacheDeleteNotifications
+ __OBJC_$_CLASS_METHODS_MTEpisode(NSSortDescriptor|MTSyncInfo|Core|Library|DB|NSPredicate|PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2|PodcastsFoundation3|PodcastsFoundation4)
+ __OBJC_$_INSTANCE_METHODS_CacheDeleteNotificationObserver
+ __OBJC_$_INSTANCE_METHODS_MTEpisode(NSSortDescriptor|MTSyncInfo|Core|Library|DB|NSPredicate|PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2|PodcastsFoundation3|PodcastsFoundation4)
+ __OBJC_$_INSTANCE_VARIABLES_CacheDeleteNotificationObserver
+ __OBJC_$_PROP_LIST_CacheDeleteNotificationObserver
+ __OBJC_$_PROP_LIST_NSFetchedResultsSectionInfo
+ __OBJC_$_PROP_LIST_NSFetchedResultsSectionInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CacheDeleteNotificationObserverDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFetchedResultsSectionInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFetchedResultsSectionInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CacheDeleteNotificationObserverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSFetchedResultsSectionInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSFetchedResultsSectionInfo
+ __OBJC_CLASS_PROTOCOLS_$_MTEpisode(NSSortDescriptor|MTSyncInfo|Core|Library|DB|NSPredicate|PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2|PodcastsFoundation3|PodcastsFoundation4)
+ __OBJC_CLASS_RO_$_CacheDeleteNotificationObserver
+ __OBJC_LABEL_PROTOCOL_$_CacheDeleteNotificationObserverDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSFetchedResultsSectionInfo
+ __OBJC_METACLASS_RO_$_CacheDeleteNotificationObserver
+ __OBJC_PROTOCOL_$_CacheDeleteNotificationObserverDelegate
+ __OBJC_PROTOCOL_$_NSFetchedResultsSectionInfo
+ __PROTOCOLS__TtC18PodcastsFoundation24CacheDeleteNotifications
+ ___49-[CacheDeleteNotificationObserver beginObserving]_block_invoke
+ ___57-[CacheDeleteNotificationObserver _onQueueBeginObserving]_block_invoke
+ ___73-[CacheDeleteNotificationObserver _onQueueConfigurePurgeMarkerForVolume:]_block_invoke
+ ___77-[CacheDeleteNotificationObserver _onQueueSubscribeToNotificationsForVolume:]_block_invoke
+ ___77-[CacheDeleteNotificationObserver _onQueueSubscribeToNotificationsForVolume:]_block_invoke_2
+ ___block_descriptor_32_e25_"NSString"16?0"NSURL"8l
+ ___block_descriptor_40_e8_32w_e20_v16?0^{__CFArray=}8l
+ ___block_descriptor_48_e8_32s40w_e5_v8?0l
+ __block_literal_global.330
+ __block_literal_global.408
+ __block_literal_global.462
+ __block_literal_global.488
+ __block_literal_global.505
+ _associated conformance 10Foundation9IndexPathV08PodcastsA0E0B5ErrorOSHADSQ
+ _associated conformance 18PodcastsFoundation24CacheDeleteNotificationsC0cD5EventOSLAASQ
+ _associated conformance 18PodcastsFoundation24CacheDeleteNotificationsCSciAA13AsyncIteratorSci_ScI
+ _associated conformance 18PodcastsFoundation24DatabaseEntityChangeTypeOSHAASQ
+ _associated conformance 18PodcastsFoundation25DatabasePropertyPublisherV7Combine0E0AA7FailureAdEP_s5Error
+ _flat unique So27NSFetchedResultsSectionInfo_p
+ _kEpisodeLastCacheDeletePurge
+ _objc_msgSend$_onQueueBeginObserving
+ _objc_msgSend$_onQueueConfigurePurgeMarkerForVolume:
+ _objc_msgSend$_onQueueProcessNotifications:
+ _objc_msgSend$_onQueueSubscribeToNotificationsForVolume:
+ _objc_msgSend$cacheDeleteObserver:didIdentifyCacheDeletedPath:deletedAtDate:
+ _objc_msgSend$cacheDeleteObserverBecameSynchronizedWithFileSystem:
+ _objc_msgSend$storeCleanURLForAdamID:
+ _swift_asyncLet_begin
+ _swift_asyncLet_finish
+ _swift_asyncLet_get_throwing
+ _symbolic $s18PodcastsFoundation30EpisodeOnlyProcessorDataSourceP
+ _symbolic $s18PodcastsFoundation33PerShowEpisodeProcessorDataSourceP
+ _symbolic $s18PodcastsFoundation41InvertableEpisodeAndShowProcessorDelegateP
+ _symbolic SS4path______9timestampt 10Foundation4DateV
+ _symbolic SS_Say_____Gt 18PodcastsFoundation21EpisodeDownloadReportV0D5StateO
+ _symbolic SS______t 10Foundation3URLV
+ _symbolic SS______tSg 10Foundation3URLV
+ _symbolic SaySS______tG 10Foundation3URLV
+ _symbolic Say_____G 10Foundation9IndexPathV
+ _symbolic Say_____G 18PodcastsFoundation20DatabaseEntityChangeV
+ _symbolic ScSy_____G 18PodcastsFoundation24CacheDeleteNotificationsC0cD5EventO
+ _symbolic ScgyShySSG______pG s5ErrorP
+ _symbolic ShySo17NSManagedObjectIDCGSg
+ _symbolic Shy_____G 18PodcastsFoundation9ContentIDO
+ _symbolic Shy_____G_____yyt______pGIeggo_ 18PodcastsFoundation9ContentIDO 7Combine12AnyPublisherV s5ErrorP
+ _symbolic So14NSFetchRequestCySo17NSManagedObjectIDCG
+ _symbolic So20NSNotificationCenterC
+ _symbolic So22NSManagedObjectContextCSaySSG______pIeggrzo_ s5ErrorP
+ _symbolic So22NSManagedObjectContextCSaySo0aB2IDCG______pIeggrzo_ s5ErrorP
+ _symbolic So31CacheDeleteNotificationObserverCSg
+ _symbolic _____ 10Foundation9IndexPathV
+ _symbolic _____ 10Foundation9IndexPathV08PodcastsA0E0B5ErrorO
+ _symbolic _____ 18PodcastsFoundation20DatabaseEntityChangeV
+ _symbolic _____ 18PodcastsFoundation24CacheDeleteNotificationsC
+ _symbolic _____ 18PodcastsFoundation24CacheDeleteNotificationsC0cD5EventO
+ _symbolic _____ 18PodcastsFoundation24DatabaseEntityChangeTypeO
+ _symbolic _____ 18PodcastsFoundation25DatabasePropertyPublisherV
+ _symbolic _____ 18PodcastsFoundation25MediaCacheDeleteProcessorV
+ _symbolic _____ 18PodcastsFoundation33MediaCacheDeleteProcessorDelegateV
+ _symbolic _____ 18PodcastsFoundation35MediaCacheDeleteProcessorDataSourceV
+ _symbolic _____XMT 18PodcastsFoundation26BatchFeedRequestControllerC
+ _symbolic ______AAt 18PodcastsFoundation24CacheDeleteNotificationsC0cD5EventO
+ _symbolic ______p 18PodcastsFoundation30EpisodeOnlyProcessorDataSourceP
+ _symbolic ______p 18PodcastsFoundation33PerShowEpisodeProcessorDataSourceP
+ _symbolic ______p 18PodcastsFoundation41InvertableEpisodeAndShowProcessorDelegateP
+ _symbolic ______p So27NSFetchedResultsSectionInfoP
+ _symbolic ______pSg 18PodcastsFoundation30EpisodeOnlyProcessorDataSourceP
+ _symbolic ______pSg 18PodcastsFoundation33PerShowEpisodeProcessorDataSourceP
+ _symbolic ______pSg 18PodcastsFoundation41InvertableEpisodeAndShowProcessorDelegateP
+ _symbolic _____ySS______tG s23_ContiguousArrayStorageC 10Foundation3URLV
+ _symbolic _____ySaySo17NSManagedObjectIDCG______pG 7Combine12AnyPublisherV s5ErrorP
+ _symbolic _____ySaySo17NSManagedObjectIDCG______pG 7Combine6FutureC s5ErrorP
+ _symbolic _____ySaySo17NSManagedObjectIDCG______pGIegn_ s6ResultOsRi_zrlE s5ErrorP
+ _symbolic _____ySay_____G_____G 7Combine18PassthroughSubjectC 18PodcastsFoundation20DatabaseEntityChangeV s5NeverO
+ _symbolic _____yShySSG______p_G Scg8IteratorV s5ErrorP
+ _symbolic _____yShy_____GG 2os21OSAllocatedUnfairLockV 10Foundation4UUIDV
+ _symbolic _____yShy_____G_____G s13ManagedBufferCsRi__rlE 10Foundation4UUIDV So16os_unfair_lock_sV
+ _symbolic _____ySo11NSPredicateCG 7Combine4JustV
+ _symbolic _____ySo11NSPredicateC______p_G s6ResultO7CombineE9PublisherV s5ErrorP
+ _symbolic _____ySo15NSManagedObjectCG s11_SetStorageC
+ _symbolic _____ySo15NSManagedObjectC_G Sh5IndexV
+ _symbolic _____y_____G s11_SetStorageC 10Foundation4UUIDV
+ _symbolic _____y_____G s11_SetStorageC 18PodcastsFoundation9ContentIDO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation9IndexPathV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 18PodcastsFoundation20DatabaseEntityChangeV
+ _symbolic _____y______G ScS12ContinuationV 18PodcastsFoundation24CacheDeleteNotificationsC0dE5EventO
+ _symbolic _____y______G ScS8IteratorV 18PodcastsFoundation24CacheDeleteNotificationsC0dE5EventO
+ _symbolic _____y______GSg ScS12ContinuationV 18PodcastsFoundation24CacheDeleteNotificationsC0dE5EventO
+ _symbolic _____y_______G ScS12ContinuationV11YieldResultO 18PodcastsFoundation24CacheDeleteNotificationsC0fG5EventO
+ _symbolic _____y_______G ScS12ContinuationV15BufferingPolicyO 18PodcastsFoundation24CacheDeleteNotificationsC0fG5EventO
+ _symbolic _____y______ySaySSG______pGSo17OS_dispatch_queueCG 7Combine10PublishersO9ReceiveOnV AA6FutureC s5ErrorP
+ _symbolic _____y______ySaySo17NSManagedObjectIDCG______pGG 7Combine10PublishersO6FilterV AA12AnyPublisherV s5ErrorP
+ _symbolic _____y______ySay_____G_____GG 7Combine10PublishersO12HandleEventsV AA18PassthroughSubjectC 18PodcastsFoundation20DatabaseEntityChangeV s5NeverO
+ _symbolic _____y______ySo11NSPredicateC______pGSo17OS_dispatch_queueCG 7Combine10PublishersO9ReceiveOnV AA12AnyPublisherV s5ErrorP
+ _symbolic _____y______y______ySaySSG______pGSo17OS_dispatch_queueCGSay_____GG 7Combine10PublishersO3MapV AC9ReceiveOnV AA6FutureC s5ErrorP 10Foundation3URLV
+ _symbolic _____y______y______ySaySSG______pGSo17OS_dispatch_queueCGytG 7Combine10PublishersO3MapV AC9ReceiveOnV AA6FutureC s5ErrorP
+ _symbolic _____y______y______ySaySo17NSManagedObjectIDCG______pGGSo17OS_dispatch_queueCG 7Combine10PublishersO9ReceiveOnV AC6FilterV AA12AnyPublisherV s5ErrorP
+ _symbolic _____y______y______ySo11NSPredicateC______pGSo17OS_dispatch_queueCGG 7Combine10PublishersO7CollectV AC9ReceiveOnV AA12AnyPublisherV s5ErrorP
+ _symbolic _____y______y______y______ySo11NSPredicateC______pGSo17OS_dispatch_queueCGGSo19NSCompoundPredicateCG 7Combine10PublishersO3MapV AC7CollectV AC9ReceiveOnV AA12AnyPublisherV s5ErrorP
+ _symbolic _____y______y______y______y______y______ySo11NSPredicateC______pGGADy______y_SaySSGAI_pGACy_AFyAmI_pGSo17OS_dispatch_queueCGGGAQGGAHG 7Combine10PublishersO3MapV AC7CollectV AC9ReceiveOnV AC04FlatC0V AC4LastV AA12AnyPublisherV s5ErrorP AC8SequenceV
+ _symbolic _____y______y______y______y_____ySiGShy_____GG_____G______pG_____y______y______ySaySo17NSManagedObjectIDCGAL_pGGSo17OS_dispatch_queueCGG 7Combine10PublishersO7FlatMapV AC14SetFailureTypeV AC8SequenceV s04LazydH0V s13StrideThroughV 18PodcastsFoundation9ContentIDO s5NeverO s5ErrorP AC9ReceiveOnV AC6FilterV AA12AnyPublisherV
+ _symbolic _____y______y______yyt______pGABy______y______y______y_____ySiGShy_____GG_____GAD_pGAAy______y_ACySaySo17NSManagedObjectIDCGAD_pGGSo17OS_dispatch_queueCGGGAXG 7Combine10PublishersO9ReceiveOnV AC7FlatMapV AA12AnyPublisherV s5ErrorP AC14SetFailureTypeV AC8SequenceV s04LazyfM0V s13StrideThroughV 18PodcastsFoundation9ContentIDO s5NeverO AC6FilterV
+ _symbolic _____y______y_____ySiGShy_____GG_____G 7Combine10PublishersO8SequenceV s07LazyMapC0V s13StrideThroughV 18PodcastsFoundation9ContentIDO s5NeverO
+ _symbolic _____y______yyt______pGAAy______y______y______y_____ySiGShy_____GG_____GAC_pG_____y______y_ABySaySo17NSManagedObjectIDCGAC_pGGSo17OS_dispatch_queueCGGG 7Combine10PublishersO7FlatMapV AA12AnyPublisherV s5ErrorP AC14SetFailureTypeV AC8SequenceV s04LazydK0V s13StrideThroughV 18PodcastsFoundation9ContentIDO s5NeverO AC9ReceiveOnV AC6FilterV
+ _symbolic _____y_____ySiGShy_____GG s15LazyMapSequenceV s13StrideThroughV 18PodcastsFoundation9ContentIDO
+ block_copy_helper.122
+ block_copy_helper.304
+ block_descriptor.124
+ block_descriptor.306
+ block_destroy_helper.123
+ block_destroy_helper.305
+ objectdestroy.111Tm
+ objectdestroy.114Tm
+ objectdestroy.120Tm
+ objectdestroy.126Tm
+ objectdestroy.129Tm
+ objectdestroy.225Tm
+ objectdestroy.228Tm
+ objectdestroy.231Tm
+ objectdestroy.28Tm
+ objectdestroy.28Tm
+ objectdestroy.38Tm
+ objectdestroy.51Tm
+ objectdestroy.62Tm
+ objectdestroy.69Tm
+ objectdestroy.80Tm
+ objectdestroy.93Tm
+ objectdestroy.96Tm
- __OBJC_$_CLASS_METHODS_MTEpisode(NSSortDescriptor|MTSyncInfo|Core|Library|DB|NSPredicate|PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2|PodcastsFoundation3)
- __OBJC_$_INSTANCE_METHODS_MTEpisode(NSSortDescriptor|MTSyncInfo|Core|Library|DB|NSPredicate|PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2|PodcastsFoundation3)
- __OBJC_CLASS_PROTOCOLS_$_MTEpisode(NSSortDescriptor|MTSyncInfo|Core|Library|DB|NSPredicate|PodcastsFoundation|PodcastsFoundation1|PodcastsFoundation2|PodcastsFoundation3)
- __block_literal_global.328
- __block_literal_global.406
- __block_literal_global.460
- __block_literal_global.486
- __block_literal_global.503
- _associated conformance 18PodcastsFoundation26EpisodeLimitRecommendationV10CodingKeys33_3E93CD23897049B5D5094F8C0020499FLLOSHAASQ
- _associated conformance 18PodcastsFoundation26EpisodeLimitRecommendationV10CodingKeys33_3E93CD23897049B5D5094F8C0020499FLLOs0F3KeyAAs23CustomStringConvertible
- _associated conformance 18PodcastsFoundation26EpisodeLimitRecommendationV10CodingKeys33_3E93CD23897049B5D5094F8C0020499FLLOs0F3KeyAAs28CustomDebugStringConvertible
- _symbolic $s18PodcastsFoundation37LibraryStorageRecommendationsProviderP
- _symbolic SiIegy_
- _symbolic _____ 18PodcastsFoundation26EpisodeLimitRecommendationV
- _symbolic _____ 18PodcastsFoundation26EpisodeLimitRecommendationV10CodingKeys33_3E93CD23897049B5D5094F8C0020499FLLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 18PodcastsFoundation26EpisodeLimitRecommendationV10CodingKeys33_3E93CD23897049B5D5094F8C0020499FLLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 18PodcastsFoundation26EpisodeLimitRecommendationV10CodingKeys33_3E93CD23897049B5D5094F8C0020499FLLO
- _symbolic _____y______GIegy_ 7Combine11SubscribersO10CompletionO s5NeverO
- _symbolic _____y___________pG s6ResultOsRi_zrlE 18PodcastsFoundation31AutoDownloadProcessorDataSourceC0dE7ContextV s5ErrorP
- _symbolic _____y_______pGIegg_ 7Combine11SubscribersO10CompletionO s5ErrorP
- _symbolic _____y______y______y______y______y______ySo11NSPredicateC______pGGADy______y_SaySSGAI_pGACy_AFyAmI_pGSo17OS_dispatch_queueCGGGAQGGSo19NSCompoundPredicateCG 7Combine10PublishersO3MapV AC7CollectV AC9ReceiveOnV AC04FlatC0V AC4LastV AA12AnyPublisherV s5ErrorP AC8SequenceV
- block_copy_helper.139
- block_copy_helper.206
- block_copy_helper.355
- block_descriptor.141
- block_descriptor.208
- block_descriptor.357
- block_destroy_helper.140
- block_destroy_helper.207
- block_destroy_helper.356
- objectdestroy.107Tm
- objectdestroy.110Tm
- objectdestroy.128Tm
- objectdestroy.131Tm
- objectdestroy.137Tm
- objectdestroy.143Tm
- objectdestroy.146Tm
- objectdestroy.17Tm
- objectdestroy.22Tm
- objectdestroy.268Tm
- objectdestroy.271Tm
- objectdestroy.274Tm
- objectdestroy.45Tm
- objectdestroy.54Tm
- objectdestroy.58Tm
- objectdestroy.73Tm
- objectdestroy.94Tm
CStrings:
+ "%!K(MISSING) == 0 || %!K(MISSING) == %!l(MISSING)d"
+ "%!K(MISSING).%!K(MISSING) != NULL AND %!K(MISSING).%!K(MISSING) > %!@(MISSING)"
+ "%!K(MISSING).%!K(MISSING) == %!l(MISSING)ld && %!l(MISSING)ld == %!l(MISSING)ld"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PodcastsFoundation/PodcastsFoundation/PodcastsFoundation/Extensions/Foundation/NSError+MTAdditions.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PodcastsFoundation/PodcastsFoundation/PodcastsFoundation/Logging/IMLogger.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/PodcastsFoundation/PodcastsFoundation/PodcastsFoundation/Query/MTBaseQueryObserver.m"
+ "/id%!l(MISSING)ld"
+ "@\"NSString\"16@?0@\"NSURL\"8"
+ "@44@0:8@16@24@32B40"
+ "A component of the path prefix is not a directory"
+ "A component of the pathname exceeded the maximum allowed characters, or the path exceeded the total allowable length"
+ "An I/O error occurred while reading or writing to the file system"
+ "An unknown error occurred."
+ "FRP"
+ "FRP.RegenerateResults"
+ "MTApplicationSceneDidDisconnectNotification"
+ "Path or data points to an invalid address"
+ "PodcastsFoundation.CacheDeleteNotifications"
+ "Request or data is invalid."
+ "Search permission is denied for a component of the path prefix"
+ "The named file does not exist"
+ "Too many symbolic links were encountered in translating the pathname."
+ "_TtC18PodcastsFoundation24CacheDeleteNotifications"
+ "autoDownloadExplanation"
+ "autoRemovalExplanation"
+ "cacheDeleteExplanation"
+ "completedCheck"
+ "continuation"
+ "highPriorityPurgeable"
+ "historyDone"
+ "https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewPodcast"
+ "https://podcasts.apple.com/podcast"
+ "inverseBatchSize"
+ "invertedEvaluableCancellable"
+ "lastCacheDeletePurge"
+ "lowPriorityPurgeable"
+ "mediumPriorityPurgeable"
+ "noDownloadBehavior"
+ "path"
+ "paths"
+ "softwareUpdatePurgeable"
+ "timestamp"
+ "v16@?0^{__CFArray=}8"
+ "willBeMarkedPurgeable"
+ "yyyy-MM-dd HH:mm:ss.SSSSSS"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PodcastsFoundation/PodcastsFoundation/PodcastsFoundation/Extensions/Foundation/NSError+MTAdditions.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PodcastsFoundation/PodcastsFoundation/PodcastsFoundation/Logging/IMLogger.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/PodcastsFoundation/PodcastsFoundation/PodcastsFoundation/Query/MTBaseQueryObserver.m"
- "Failed to decode BatchFeedRequestResponse"
- "spaceDistribution"

```
