## UserSafetyUI

> `/System/Library/PrivateFrameworks/UserSafetyUI.framework/UserSafetyUI`

```diff

-75.1.0.0.0
+75.3.0.0.0
   __TEXT.__text: 0x4118
   __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_methlist: 0x3a4

   __TEXT.__objc_methtype: 0x101
   __TEXT.__objc_stubs: 0x7c0
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x188
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 133
-  Symbols:   191
-  CStrings:  0
+  Symbols:   199
+  CStrings:  92
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "JC_CLASS_$_NTPBTodayConfig"
+ "ListRecord"
+ "NTPBExternalAnalyticsConfig"
+ "_OBJC_CLASS_$_COMAPPLEFELDSPARPROTOCOLScoredTagID"
+ "_OBJC_CLASS_$_NTPBArticleHostViewExposure"
+ "_OBJC_CLASS_$_NTPBArticleListRecord"
+ "_OBJC_CLASS_$_NTPBAudioPlaylistItem"
+ "_OBJC_CLASS_$_NTPBChannelData"
+ "_OBJC_CLASS_$_NTPBDeviceInfo"
+ "_OBJC_CLASS_$_NTPBEnvelope"
+ "_OBJC_CLASS_$_NTPBEvent"
+ "_OBJC_CLASS_$_NTPBEventObject"
+ "_OBJC_CLASS_$_NTPBExternalAnalyticsConfig"
+ "_OBJC_CLASS_$_NTPBExternalAnalyticsQueryParameterConfig"
+ "_OBJC_CLASS_$_NTPBFeedItem"
+ "_OBJC_CLASS_$_NTPBFeedItemInventory"
+ "_OBJC_CLASS_$_NTPBForYouTodaySectionSpecificConfig"
+ "_OBJC_CLASS_$_NTPBIssueReadingHistoryItem"
+ "_OBJC_CLASS_$_NTPBLocationRecommendationMapping"
+ "_OBJC_CLASS_$_NTPBLocationRecommendationMappings"
+ "_OBJC_CLASS_$_NTPBNotificationEntity"
+ "_OBJC_CLASS_$_NTPBPersonalizationLocalData"
+ "_OBJC_CLASS_$_NTPBPrivateDataControllerSyncState"
+ "_OBJC_CLASS_$_NTPBPushNotifySubscriptionRequest"
+ "_OBJC_CLASS_$_NTPBPuzzleRecord"
+ "_OBJC_CLASS_$_NTPBPuzzleTypeRecord"
+ "_OBJC_CLASS_$_NTPBScoreProfiles"
+ "_OBJC_CLASS_$_NTPBSportsEventRecord"
+ "_OBJC_CLASS_$_NTPBTodayModuleContentDescriptor"
+ "_OBJC_CLASS_$_NTPBTodayModuleDescriptor"
+ "_OBJC_CLASS_$_NTPBTodayPersonalizationUpdate"
+ "_OBJC_CLASS_$_NTPBTodayQueueConfig"
+ "_OBJC_CLASS_$_NTPBTodaySectionConfig"
+ "_OBJC_CLASS_$_NTPBTodaySectionConfigFont"
+ "_OBJC_CLASS_$_NTPBTodaySectionConfigItem"
+ "_OBJC_CLASS_$_NTPBTodayWidgetConfig"
+ "_OBJC_CLASS_$_NTPBTodayWidgetExposure"
+ "_OBJC_CLASS_$_NTPBTodayWidgetHeadlineExposure"
+ "_OBJC_CLASS_$_NTPBWidgetPersonalizationFeatureCTRPair"
+ "_OBJC_CLASS_$_NTPBWidgetSectionConfigRecord"
+ "_OBJC_CLASS_$_NTPBWidgetSectionsArticleCountPair"
+ "_OBJC_METACLASS_$_COMAPPLEFELDSPARPROTOCOLLIVERPOOLTopicCohortScore"
+ "_OBJC_METACLASS_$_COMAPPLEFELDSPARPROTOCOLScoredTagID"
+ "_OBJC_METACLASS_$_NTPBArticleHostViewExposure"
+ "_OBJC_METACLASS_$_NTPBArticleIDsTodaySectionSpecificConfig"
+ "_OBJC_METACLASS_$_NTPBArticleListRecord"
+ "_OBJC_METACLASS_$_NTPBArticleListTodaySectionSpecificConfig"
+ "_OBJC_METACLASS_$_NTPBAudioPlaylistItem"
+ "_OBJC_METACLASS_$_NTPBChannelData"
+ "_OBJC_METACLASS_$_NTPBDeviceInfo"
+ "_OBJC_METACLASS_$_NTPBEnvelope"
+ "_OBJC_METACLASS_$_NTPBEvent"
+ "_OBJC_METACLASS_$_NTPBEventObject"
+ "_OBJC_METACLASS_$_NTPBExternalAnalyticsQueryParameterConfig"
+ "_OBJC_METACLASS_$_NTPBFeedItem"
+ "_OBJC_METACLASS_$_NTPBFeedItemInventory"
+ "_OBJC_METACLASS_$_NTPBForYouTodaySectionSpecificConfig"
+ "_OBJC_METACLASS_$_NTPBHeadlineAdElement"
+ "_OBJC_METACLASS_$_NTPBHeadlineAnalyticsElement"
+ "_OBJC_METACLASS_$_NTPBHeadlineBackingElement"
+ "_OBJC_METACLASS_$_NTPBIssueReadingHistoryItem"
+ "_OBJC_METACLASS_$_NTPBItemsTodaySectionSpecificConfig"
+ "_OBJC_METACLASS_$_NTPBPersonalizationLocalData"
+ "_OBJC_METACLASS_$_NTPBPersonalizedSectionPresenceConfig"
+ "_OBJC_METACLASS_$_NTPBPersonalizedTodaySectionSpecificConfig"
+ "_OBJC_METACLASS_$_NTPBPuzzleRecord"
+ "_OBJC_METACLASS_$_NTPBPuzzleTypeRecord"
+ "_OBJC_METACLASS_$_NTPBRelativePersonalizedSectionPresenceConfig"
+ "_OBJC_METACLASS_$_NTPBTagTodaySectionSpecificConfig"
+ "_OBJC_METACLASS_$_NTPBTelemetry"
+ "_OBJC_METACLASS_$_NTPBTelemetryNetworkEvent"
+ "_OBJC_METACLASS_$_NTPBTelemetryNetworkEventGroup"
+ "_OBJC_METACLASS_$_NTPBTodayConfig"
+ "_OBJC_METACLASS_$_NTPBTodayModuleContentDescriptor"
+ "_OBJC_METACLASS_$_NTPBTodayModuleDescriptor"
+ "_OBJC_METACLASS_$_NTPBTodayQueueConfig"
+ "_OBJC_METACLASS_$_NTPBTodaySectionConfig"
+ "_OBJC_METACLASS_$_NTPBTodaySectionConfigArticle"
+ "_OBJC_METACLASS_$_NTPBTodaySectionConfigItem"
+ "_OBJC_METACLASS_$_NTPBTodayWidgetConfig"
+ "_OBJC_METACLASS_$_NTPBTodayWidgetExposure"
+ "_OBJC_METACLASS_$_NTPBTodayWidgetHeadlineExposure"
+ "_OBJC_METACLASS_$_NTPBURLMapping"
+ "_OBJC_METACLASS_$_NTPBURLMappingDomain"
+ "_OBJC_METACLASS_$_NTPBURLMappingPath"
+ "_OBJC_METACLASS_$_NTPBVanityURLMapping"
+ "_OBJC_METACLASS_$_NTPBVanityURLPath"
+ "_OBJC_METACLASS_$_NTPBWidgetPersonalizationFeatureCTRPair"
+ "_OBJC_METACLASS_$_NTPBWidgetSectionConfigRecord"
+ "_OBJC_METACLASS_$_NTPBWidgetSectionsArticleCountPair"
+ "dation"
+ "daySectionConfigArticle"

```
