## UserNotificationsCore

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Versions/A/UserNotificationsCore`

```diff

-563.0.0.0.0
-  __TEXT.__text: 0x1a0a90
-  __TEXT.__auth_stubs: 0x2f70
-  __TEXT.__objc_methlist: 0x6178
-  __TEXT.__const: 0xb4d0
-  __TEXT.__cstring: 0xbee7
-  __TEXT.__oslogstring: 0xbae8
+569.1.0.0.0
+  __TEXT.__text: 0x19dd28
+  __TEXT.__auth_stubs: 0x2f40
+  __TEXT.__objc_methlist: 0x61f0
+  __TEXT.__const: 0xb410
+  __TEXT.__cstring: 0xbff7
+  __TEXT.__oslogstring: 0xbb78
   __TEXT.__gcc_except_tab: 0x6a0
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__constg_swiftt: 0x4fec
-  __TEXT.__swift5_typeref: 0x4ee2
-  __TEXT.__swift5_reflstr: 0x2c37
-  __TEXT.__swift5_fieldmd: 0x36b0
+  __TEXT.__constg_swiftt: 0x4e50
+  __TEXT.__swift5_typeref: 0x4de8
+  __TEXT.__swift5_reflstr: 0x2c67
+  __TEXT.__swift5_fieldmd: 0x3700
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x420
-  __TEXT.__swift5_protos: 0xdc
-  __TEXT.__swift5_proto: 0x940
+  __TEXT.__swift5_protos: 0xe0
+  __TEXT.__swift5_proto: 0x924
   __TEXT.__swift5_types: 0x428
-  __TEXT.__swift5_capture: 0x1544
-  __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x5470
-  __TEXT.__eh_frame: 0x4ff8
-  __TEXT.__objc_classname: 0xdea
-  __TEXT.__objc_methname: 0x14fac
-  __TEXT.__objc_methtype: 0x3000
-  __TEXT.__objc_stubs: 0xc440
-  __DATA_CONST.__got: 0xf50
-  __DATA_CONST.__const: 0x968
+  __TEXT.__swift5_capture: 0x1500
+  __TEXT.__swift5_mpenum: 0x48
+  __TEXT.__unwind_info: 0x5378
+  __TEXT.__eh_frame: 0x4cf0
+  __TEXT.__objc_classname: 0xdeb
+  __TEXT.__objc_methname: 0x1519d
+  __TEXT.__objc_methtype: 0x302e
+  __TEXT.__objc_stubs: 0xc560
+  __DATA_CONST.__got: 0xf58
+  __DATA_CONST.__const: 0x988
   __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e98
+  __DATA_CONST.__objc_selrefs: 0x3ee0
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x1e8
-  __AUTH_CONST.__auth_got: 0x17c8
-  __AUTH_CONST.__auth_ptr: 0xea0
-  __AUTH_CONST.__const: 0xa0d0
-  __AUTH_CONST.__cfstring: 0x53c0
-  __AUTH_CONST.__objc_const: 0x21500
+  __AUTH_CONST.__auth_got: 0x17b0
+  __AUTH_CONST.__auth_ptr: 0xeb8
+  __AUTH_CONST.__const: 0xa260
+  __AUTH_CONST.__cfstring: 0x5440
+  __AUTH_CONST.__objc_const: 0x21710
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0x3390
-  __AUTH.__data: 0x5cd8
-  __DATA.__objc_ivar: 0x830
-  __DATA.__data: 0x4650
-  __DATA.__bss: 0x10740
-  __DATA.__common: 0x338
+  __AUTH.__data: 0x5b40
+  __DATA.__objc_ivar: 0x844
+  __DATA.__data: 0x45a8
+  __DATA.__bss: 0x10340
+  __DATA.__common: 0x360
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8343
-  Symbols:   8852
-  CStrings:  1508
+  Functions: 8284
+  Symbols:   8881
+  CStrings:  1525
 
Symbols:
+ +[UNSNotificationRecordAddUpdate updateWithNotificationRecord:shouldSync:]
+ -[UNCLocalNotificationRepository _queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:shouldSync:forBundleIdentifier:]
+ -[UNCSummaryServiceIndividualSummary contentCreationDate]
+ -[UNCSummaryServiceIndividualSummary initWithSpotlightIdentifier:individualSummary:isHighlight:contentCreationDate:]
+ -[UNCSummaryServiceIndividualSummary setContentCreationDate:]
+ -[UNSNotificationRecord eventBehavior]
+ -[UNSNotificationRecord isHighlight]
+ -[UNSNotificationRecord pipelineState]
+ -[UNSNotificationRecord setEventBehavior:]
+ -[UNSNotificationRecord setIsHighlight:]
+ -[UNSNotificationRecord setPipelineState:]
+ -[UNSNotificationRecord setSummary:]
+ -[UNSNotificationRecord summary]
+ GCC_except_table35
+ OBJC_IVAR_$_UNCSummaryServiceIndividualSummary._contentCreationDate
+ OBJC_IVAR_$_UNSNotificationRecord._eventBehavior
+ OBJC_IVAR_$_UNSNotificationRecord._isHighlight
+ OBJC_IVAR_$_UNSNotificationRecord._pipelineState
+ OBJC_IVAR_$_UNSNotificationRecord._summary
+ _MDItemContentCreationDate
+ _MDItemUrgencyStatus
+ _NSURLIsDirectoryKey
+ _OBJC_CLASS_$_DNDClientEventBehavior
+ __DATA__TtC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774129NotificationPipelineScheduler
+ __DATA__TtCC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774129NotificationPipelineScheduler7Request
+ __IVARS__TtC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774129NotificationPipelineScheduler
+ __IVARS__TtCC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774129NotificationPipelineScheduler7Request
+ __METACLASS_DATA__TtC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774129NotificationPipelineScheduler
+ __METACLASS_DATA__TtCC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774129NotificationPipelineScheduler7Request
+ ___200-[UNCLocalNotificationRepository _queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:shouldSync:forBundleIdentifier:]_block_invoke
+ ___38-[UNCKeyedDataStoreRepository allKeys]_block_invoke
+ ___block_descriptor_32_e27_B24?0"NSURL"8"NSError"16l
+ __block_literal_global.1202
+ __block_literal_global.1205
+ __block_literal_global.1219
+ _associated conformance 21UserNotificationsCore29NotificationPipelineScheduler33_44CB2ECED9549B956A840C1DBFE37741LLC7ChannelVSHAASQ
+ _associated conformance 21UserNotificationsCore29NotificationPipelineScheduler33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC5StateOSHAASQ
+ _kUNNotificationDataRetentionAge
+ _objc_msgSend$_queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:shouldSync:forBundleIdentifier:
+ _objc_msgSend$bs_safeObjectForKey:ofType:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$eventBehavior
+ _objc_msgSend$isHighlight
+ _objc_msgSend$pipelineState
+ _objc_msgSend$setEventBehavior:
+ _objc_msgSend$setIsHighlight:
+ _objc_msgSend$setPipelineState:
+ _objc_msgSend$setSummary:
+ _objc_msgSend$summary
+ _symbolic $s21UserNotificationsCore44NotificationPipelineSchedulerRequestDelegate33_44CB2ECED9549B956A840C1DBFE37741LLP
+ _symbolic SDy_____Say_____GG 21UserNotificationsCore29NotificationPipelineScheduler33_44CB2ECED9549B956A840C1DBFE37741LLC7ChannelV AD7RequestC
+ _symbolic _____ 21UserNotificationsCore23AlertCoordinatorContextV
+ _symbolic _____ 21UserNotificationsCore29NotificationPipelineScheduler33_44CB2ECED9549B956A840C1DBFE37741LLC
+ _symbolic _____ 21UserNotificationsCore29NotificationPipelineScheduler33_44CB2ECED9549B956A840C1DBFE37741LLC7ChannelV
+ _symbolic _____ 21UserNotificationsCore29NotificationPipelineScheduler33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC
+ _symbolic _____ 21UserNotificationsCore29NotificationPipelineScheduler33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC5StateO
+ _symbolic _____ 21UserNotificationsCore33NotificationPipelineRequestLoggerV
+ _symbolic _____ So31UNNotificationInterruptionLevelV
+ _symbolic _____SgXw 21UserNotificationsCore29NotificationPipelineScheduler33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC
+ _symbolic _____SgXwz_Xx 21UserNotificationsCore29NotificationPipelineScheduler33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC
+ _symbolic ______pSgXw 21UserNotificationsCore44NotificationPipelineSchedulerRequestDelegate33_44CB2ECED9549B956A840C1DBFE37741LLP
+ _symbolic _____y_____Say_____GG s18_DictionaryStorageC 21UserNotificationsCore29NotificationPipelineScheduler33_44CB2ECED9549B956A840C1DBFE37741LLC7ChannelV AF7RequestC
+ block_copy_helper.24
+ block_descriptor.26
+ block_destroy_helper.25
+ objectdestroy.7Tm
- +[UNSNotificationRecordAddUpdate updateWithNotificationRecord:]
- -[UNCLocalNotificationRepository _queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:shouldSyncForRemoval:forBundleIdentifier:]
- -[UNCSummaryServiceIndividualSummary initWithSpotlightIdentifier:individualSummary:isHighlight:]
- GCC_except_table38
- __DATA__TtC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774113PipelineQueue
- __DATA__TtCC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774113PipelineQueue7Request
- __IVARS__TtC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774113PipelineQueue
- __IVARS__TtCC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774113PipelineQueue7Request
- __METACLASS_DATA__TtC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774113PipelineQueue
- __METACLASS_DATA__TtCC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774113PipelineQueue7Request
- ___210-[UNCLocalNotificationRepository _queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:shouldSyncForRemoval:forBundleIdentifier:]_block_invoke
- ___swift_memcpy33_8
- __block_literal_global.1168
- __block_literal_global.1171
- __block_literal_global.1185
- _associated conformance 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7ChannelOSHAASQ
- _associated conformance 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC10IdentifierVSHAASQ
- _associated conformance 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestCSHAASQ
- _associated conformance 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestCs12IdentifiableAA2IDsAGP_SH
- _associated conformance 21UserNotificationsCore15SpotlightSearchV10QueryError33_EBB20240FE67DA19FDA0304F6D5E0E46LLOSHAASQ
- _associated conformance 21UserNotificationsCore27NotificationPipelineFactoryC10UsageErrorOSHAASQ
- _objc_msgSend$_queue_notifyObserversNotificationsDidAddNotifications:replaceNotifications:replacementNotifications:removedNotifications:shouldRepost:shouldSyncForRemoval:forBundleIdentifier:
- _objc_msgSend$updateWithNotificationRecord:
- _symbolic SDy_____Say_____GG 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7ChannelO AD7RequestC
- _symbolic SDy__________G 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC10IdentifierV AD7ChannelO
- _symbolic SS8bundleID_t
- _symbolic SS8threadID_SS06bundleB0t
- _symbolic ScCy___________pG 25UserNotificationsServices0A12NotificationV s5ErrorP
- _symbolic So34UNCSummaryServiceIndividualSummaryCSg
- _symbolic So7NSCacheCySo8NSStringCSo34UNCSummaryServiceIndividualSummaryCG
- _symbolic _____ 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC
- _symbolic _____ 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7ChannelO
- _symbolic _____ 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC
- _symbolic _____ 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC10IdentifierV
- _symbolic _____ 21UserNotificationsCore15SpotlightSearchV
- _symbolic _____ 21UserNotificationsCore15SpotlightSearchV10QueryError33_EBB20240FE67DA19FDA0304F6D5E0E46LLO
- _symbolic _____ 21UserNotificationsCore22PipelineWorkItemLoggerV
- _symbolic _____ 21UserNotificationsCore27NotificationPipelineFactoryC10UsageErrorO
- _symbolic _____Sg 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7ChannelO
- _symbolic _____Sg 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC
- _symbolic _____SgXw 21UserNotificationsCore27NotificationPipelineFactoryC
- _symbolic _____SgXwz_Xx 21UserNotificationsCore27NotificationPipelineFactoryC
- _symbolic ______SitSg 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7ChannelO
- _symbolic _______________AA______pIegHnynrzo_ 25UserNotificationsServices0A12NotificationV 0aB4Core0D14PipelineActionO AD0F14WorkItemLoggerV s5ErrorP
- _symbolic ______pSg s5ErrorP
- _symbolic ______pSgz_Xx s5ErrorP
- _symbolic _____y_____Say_____GG s18_DictionaryStorageC 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7ChannelO AF7RequestC
- _symbolic _____y______G ScS8IteratorV 21UserNotificationsCore23SequentialAsyncEntranceC8WorkItem33_180F1A33B120AD5AD22F72381EE6F494LLV
- _symbolic _____y_______G ScS12ContinuationV11YieldResultO 21UserNotificationsCore23SequentialAsyncEntranceC8WorkItem33_180F1A33B120AD5AD22F72381EE6F494LLV
- _symbolic _____y_______G ScS12ContinuationV15BufferingPolicyO 21UserNotificationsCore23SequentialAsyncEntranceC8WorkItem33_180F1A33B120AD5AD22F72381EE6F494LLV
- _symbolic _____y__________G s18_DictionaryStorageC 21UserNotificationsCore13PipelineQueue33_44CB2ECED9549B956A840C1DBFE37741LLC7RequestC10IdentifierV AF7ChannelO
- block_copy_helper.10
- block_copy_helper.97
- block_descriptor.12
- block_descriptor.99
- block_destroy_helper.11
- block_destroy_helper.98
- objectdestroy.46Tm
- objectdestroy.71Tm
CStrings:
+ "(_kMDItemDomainIdentifier = \""
+ "<NotificationPipelineScheduler.Request notificationIdentifier="
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "EventBehavior"
+ "IsHighlight"
+ "PipelineState"
+ "Programmer error: Analytics deallocated without logging to CoreAnalytics"
+ "Programmer error: Attempted to end analytics twice"
+ "Summary"
+ "Usage: Must never call queue_callCompletion() without a result"
+ "_TtC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774129NotificationPipelineScheduler"
+ "_TtCC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774129NotificationPipelineScheduler7Request"
+ "allowiPhoneMirroring"
+ "calledCompletion"
+ "channel"
+ "com.apple.AppStore"
+ "com.apple.ClarityPhotos"
+ "com.apple.MobileAddressBook"
+ "com.apple.Passbook"
+ "com.apple.UserNotifications.NotificationPipelineScheduler"
+ "com.apple.VoiceMemos"
+ "com.apple.findmy"
+ "com.apple.freeform"
+ "com.apple.iBooks"
+ "com.apple.mobilenotes"
+ "com.apple.mobilesafari"
+ "com.apple.mobiletimer"
+ "com.apple.podcasts"
+ "com.apple.stocks"
+ "com.apple.weather"
+ "completionQueue"
+ "deleted"
+ "enableAnalytics"
+ "existingSearchableListItems(inDomain:attributes:)"
+ "initialNotification"
+ "logged"
+ "scheduler"
+ "testing"
- "(Sequential async entrance) - Enter pipeline entrance"
- "(Sequential async entrance) - Exiting pipeline entrance"
- "(Sequential async entrance) Entering pipeline."
- "(Sequential async entrance) Exiting pipeline. Failure. "
- "(Sequential async entrance) Exiting pipeline. Success."
- "(_kMDItemDomainIdentifier = \"com.apple.usernotifications.groups\")"
- "Queue has no record of what channel it is in."
- "_TtC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774113PipelineQueue"
- "_TtCC21UserNotificationsCoreP33_44CB2ECED9549B956A840C1DBFE3774113PipelineQueue7Request"
- "com.apple.UserNotifications.PipelineQueue"
- "com.apple.usernotificationsd.sequentialEntry."
- "create(_:completion:)"
- "delete(_:completion:)"
- "existingSearchableListItems(attributes:)"
- "isolated_create(_:action:logger:)"
- "isolated_delete(_:action:logger:)"
- "isolated_update(_:action:logger:)"
- "pipelineEntrance"
- "queue_individualSummaryItemBySpotlightID"
- "queue_requestIDToChannel"
- "update(_:completion:)"

```
