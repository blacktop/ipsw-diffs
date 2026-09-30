## PCSAccountNotificationPlugin

> `/System/Library/Accounts/Notification/PCSAccountNotificationPlugin.bundle/PCSAccountNotificationPlugin`

```diff

-1037.0.21.0.0
-  __TEXT.__text: 0x8b0
+1037.0.25.0.0
+  __TEXT.__text: 0x8c4
   __TEXT.__auth_stubs: 0x70
   __TEXT.__objc_methlist: 0x88
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0xb2
-  __TEXT.__oslogstring: 0x337
+  __TEXT.__oslogstring: 0x33f
   __TEXT.__unwind_info: 0x70
   __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methname: 0x3f3
+  __TEXT.__objc_methname: 0x3fd
   __TEXT.__objc_methtype: 0x20f
-  __TEXT.__objc_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x300
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0xd0
   __AUTH_CONST.__auth_got: 0x40
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x528

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 10
   Symbols:   30
-  CStrings:  53
+  CStrings:  7
 
Symbols:
+ _PCSIdentityHaveiCloudIdentityLocally
- _PCSIdentityNeedsSetup
CStrings:
+ "\x1c\xe8X\x01\xc0\xe1j \x1c\xe8X\x01\xc0\xe1j@\x1c\xe8X\x01\xc0\xe1j`\x1c\xe8X\x01\xc0\xe1j\x80\x1c\xe8X\x01\xc0\xe1j\xa0\x1c\xe8X\x01\xc0\xe1j\xc0\x1c\xe8X\x01\xc0\xe1j\xe0\x1c\xe8X\x01\xc0\xe1j"
+ "\x1d\xe8X\x01\xc0\xe1j \x1d\xe8X\x01\xc0\xe1j@\x1d\xe8X\x01\xc0\xe1j`\x1d\xe8X\x01\xc0\xe1j\x80\x1d\xe8X\x01\xc0\xe1j\xa0\x1d\xe8X\x01\xc0\xe1j\xc0\x1d\xe8X\x01\xc0\xe1j\xe0\x1d\xe8X\x01\xc0\xe1j"
+ "\x1e\xe8X\x01\xc0\xe1j \x1e\xe8X\x01\xc0\xe1j@\x1e\xe8X\x01\xc0\xe1j`\x1e\xe8X\x01\xc0\xe1j\x80\x1e\xe8X\x01\xc0\xe1j\xa0\x1e\xe8X\x01\xc0\xe1j\xc0\x1e\xe8X\x01\xc0\xe1j\xe0\x1e\xe8X\x01\xc0\xe1j"
+ "\x1f\xe8X\x01\xc0\xe1j \x1f\xe8X\x01\xc0\xe1j@\x1f\xe8X\x01\xc0\xe1j`\x1f\xe8X\x01\xc0\xe1j\x80\x1f\xe8X\x01\xc0\xe1j\xa0\x1f\xe8X\x01\xc0\xe1j\xc0\x1f\xe8X\x01\xc0\xe1j\xe0\x1f\xe8X\x01\xc0\xe1j"
+ " \xe8X\x01\xc0\xe1j  \xe8X\x01\xc0\xe1j@ \xe8X\x01\xc0\xe1j` \xe8X\x01\xc0\xe1j\x80 \xe8X\x01\xc0\xe1j\xa0 \xe8X\x01\xc0\xe1j\xc0 \xe8X\x01\xc0\xe1j\xe0 \xe8X\x01\xc0\xe1j"
+ "!\xe8X\x01\xc0\xe1j !\xe8X\x01\xc0\xe1j@!\xe8X\x01\xc0\xe1j`!\xe8X\x01\xc0\xe1j\x80!\xe8X\x01\xc0\xe1j\xa0!\xe8X\x01\xc0\xe1j\xc0!\xe8X\x01\xc0\xe1j\xe0!\xe8X\x01\xc0\xe1j"
+ "\xeaX\x01\xc0\xe1j\x90c\xeaX\x01\xc0\xe1j\xb0c\xeaX\x01\xc0\xe1j\xd0c\xeaX\x01\xc0\xe1j\xf0c\xeaX\x01\xc0\xe1j\x10d\xeaX\x01\xc0\xe1j0d\xeaX\x01\xc0\xe1jPd\xeaX\x01\xc0\xe1jpd\xeaX\x01\xc0\xe1j\x90d\xeaX\x01\xc0\xe1j\xf0n\xeaX\x01\xc0\xe1j\xc0n\xeaX\x01\xc0\xe1j\xd8n\xeaX\x01\xc0\xe1j\xa0\x1b\xe8X\x01\xc0\xe1j\xc0\x1b\xe8X\x01\xc0\xe1j\xe0\x1b\xe8X\x01\xc0\xe1j"
- "METACLASS_$_ATXUnifiedComputedAndInferredModeStream"
- "_ATXCandidateRelevanceModelDataStoreTrainingResult"
- "_OBJC_CLASS_$_ATXAnchorModelModePredictionPostProcessor"
- "_OBJC_CLASS_$_ATXAnchorModelPBModeMetadata"
- "_OBJC_CLASS_$_ATXCandidateRelevanceModelCandidateCacheResult"
- "_OBJC_CLASS_$_ATXCandidateRelevanceModelDataStoreCache"
- "_OBJC_CLASS_$_ATXCandidateRelevanceModelDataStoreTrainingResult"
- "_OBJC_CLASS_$_ATXCloudKitClient"
- "_OBJC_CLASS_$_ATXContinuousUsageAccumulator"
- "_OBJC_CLASS_$_ATXFakeAnchorModelPredictionForwarder"
- "_OBJC_CLASS_$_ATXFakeModeEventProvider"
- "_OBJC_CLASS_$_ATXGamePlayKitARC4RandomSource"
- "_OBJC_CLASS_$_ATXGamePlayKitDecisionTree"
- "_OBJC_CLASS_$_ATXGamePlayKitRandomSource"
- "_OBJC_CLASS_$_ATXGamePlayKitSystemArc4RandomSource"
- "_OBJC_CLASS_$_ATXInformationRanker"
- "_OBJC_CLASS_$_ATXMPBAnchorModelEngagementTracker"
- "_OBJC_CLASS_$_ATXMPBCacheAgeAtEngagementTracker"
- "_OBJC_CLASS_$_ATXMissedNotificationRankingEngagementMetric"
- "_OBJC_CLASS_$_ATXMotionStateDuetEvent"
- "_OBJC_CLASS_$_ATXNotificationSuggestionFeedbackHistoryQueryResult"
- "_OBJC_CLASS_$_ATXPBUnifiedInferredActivityTransition"
- "_OBJC_CLASS_$_ATXPredictionJSONScoreLogger"
- "_OBJC_CLASS_$_ATXTimelineRelevancePBTimelineRelevanceSuggestion"
- "_OBJC_CLASS_$_ATXUnifiedComputedAndInferredModeStream"
- "_OBJC_CLASS_$_ATXUnifiedModeEvent"
- "_OBJC_CLASS_$_ATXUsageInsightsServer"
- "_OBJC_METACLASS_$_ATXAnchorModelModePredictionPostProcessor"
- "_OBJC_METACLASS_$_ATXAnchorModelPBModeMetadata"
- "_OBJC_METACLASS_$_ATXCandidateRelevanceModelCandidateCacheResult"
- "_OBJC_METACLASS_$_ATXCandidateRelevanceModelDataStoreCache"
- "_OBJC_METACLASS_$_ATXCloudKitClient"
- "_OBJC_METACLASS_$_ATXContinuousUsageAccumulator"
- "_OBJC_METACLASS_$_ATXFakeAnchorModelPredictionForwarder"
- "_OBJC_METACLASS_$_ATXFakeModeEventProvider"
- "_OBJC_METACLASS_$_ATXGamePlayKitARC4RandomSource"
- "_OBJC_METACLASS_$_ATXGamePlayKitDecisionNode"
- "_OBJC_METACLASS_$_ATXGamePlayKitRandomDistribution"
- "_OBJC_METACLASS_$_ATXGamePlayKitRandomSource"
- "_OBJC_METACLASS_$_ATXGamePlayKitSystemArc4RandomSource"
- "_OBJC_METACLASS_$_ATXInformationRanker"
- "_OBJC_METACLASS_$_ATXMPBAnchorModelEngagementTracker"
- "_OBJC_METACLASS_$_ATXMPBCacheAgeAtEngagementTracker"
- "_OBJC_METACLASS_$_ATXMissedNotificationRankingEngagementMetric"
- "_OBJC_METACLASS_$_ATXMotionStateDuetEvent"
- "_OBJC_METACLASS_$_ATXNotificationSuggestionFeedbackHistoryQueryResult"
- "_OBJC_METACLASS_$_ATXPBUnifiedInferredActivityTransition"
- "_OBJC_METACLASS_$_ATXPredictionJSONScoreLogger"
- "_OBJC_METACLASS_$_ATXTimelineRelevancePBTimelineRelevanceSuggestion"
- "_OBJC_METACLASS_$_ATXUnifiedModeEvent"
- "andomDistribution"
- "ecisionTree"
- "gResult"

```
