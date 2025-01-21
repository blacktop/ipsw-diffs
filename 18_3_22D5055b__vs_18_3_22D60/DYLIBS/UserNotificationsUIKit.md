## UserNotificationsUIKit

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

```diff

-910.4.109.0.0
-  __TEXT.__text: 0x178098
+910.4.110.0.0
+  __TEXT.__text: 0x177978
   __TEXT.__auth_stubs: 0x2160
-  __TEXT.__objc_methlist: 0x14790
+  __TEXT.__objc_methlist: 0x14758
   __TEXT.__const: 0x28b4
   __TEXT.__gcc_except_tab: 0x2ce0
-  __TEXT.__cstring: 0xb586
-  __TEXT.__oslogstring: 0xb552
+  __TEXT.__cstring: 0xb616
+  __TEXT.__oslogstring: 0xb562
   __TEXT.__ustring: 0x22
   __TEXT.__swift5_typeref: 0x2532
   __TEXT.__swift5_fieldmd: 0xe24

   __TEXT.__swift5_types: 0xf4
   __TEXT.__swift5_capture: 0x9cc
   __TEXT.__swift5_mpenum: 0x7c
-  __TEXT.__unwind_info: 0x6588
+  __TEXT.__unwind_info: 0x6568
   __TEXT.__eh_frame: 0x9b8
-  __TEXT.__objc_classname: 0x366d
-  __TEXT.__objc_methname: 0x43c08
-  __TEXT.__objc_methtype: 0xbdb0
-  __TEXT.__objc_stubs: 0x273c0
-  __DATA_CONST.__got: 0x1590
+  __TEXT.__objc_classname: 0x3670
+  __TEXT.__objc_methname: 0x43af4
+  __TEXT.__objc_methtype: 0xbd62
+  __TEXT.__objc_stubs: 0x27380
+  __DATA_CONST.__got: 0x1588
   __DATA_CONST.__const: 0x3fb8
   __DATA_CONST.__objc_classlist: 0x778
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb948
+  __DATA_CONST.__objc_selrefs: 0xb920
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0x158
   __AUTH_CONST.__auth_got: 0x10c0
-  __AUTH_CONST.__auth_ptr: 0x630
+  __AUTH_CONST.__auth_ptr: 0x628
   __AUTH_CONST.__const: 0x4490
-  __AUTH_CONST.__cfstring: 0x79a0
-  __AUTH_CONST.__objc_const: 0x2b3d0
+  __AUTH_CONST.__cfstring: 0x79c0
+  __AUTH_CONST.__objc_const: 0x2b398
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x2ba0
   __AUTH.__data: 0x9c8
-  __DATA.__objc_ivar: 0x15c8
+  __DATA.__objc_ivar: 0x15c0
   __DATA.__data: 0x4b68
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x1b08

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9613
-  Symbols:   9228
-  CStrings:  12066
+  Functions: 9606
+  Symbols:   9220
+  CStrings:  12062
 
Symbols:
+ _OBJC_CLASS_$_NCNotificationManagementSummaryFeedbackSuggestionContentProvider
+ _OBJC_METACLASS_$_NCNotificationManagementSummaryFeedbackSuggestionContentProvider
- _OBJC_CLASS_$_NCNotificationManagementStackSummarySuggestionContentProvider
- _OBJC_CLASS_$_NCSummarizationChinSuggestionManager
- _OBJC_METACLASS_$_NCNotificationManagementStackSummarySuggestionContentProvider
CStrings:
+ ")"
+ "-[NCSuggestionManager _createSummaryFeedbackSuggestionIfNeededForRequest:sectionSettings:]"
+ "@52@0:8@16@24B32@36@44"
+ "B32@0:8@\"NCSuggestionManager\"16@\"NCNotificationRequest\"24"
+ "Creating summary feedback suggestion for request %{public}@ from section %{public}@"
+ "NCNotificationManagementSummaryFeedbackSuggestionContentProvider"
+ "NOTIFICATION_MANAGEMENT_SUGGESTION_BAD"
+ "NOTIFICATION_MANAGEMENT_SUGGESTION_GOOD"
+ "NOTIFICATION_MANAGEMENT_SUMMARY_FEEDBACK_SUGGESTION"
+ "Removing summary feedback suggestion for request %{public}@ from section %{public}@"
+ "T@\"NSMutableSet\",&,N,V_requestsWithSummaryFeedbackSuggestions"
+ "TB,R,N,V_isStackedSummary"
+ "_createNewSummaryFeedbackSuggestionForNotificationRequest:sectionSettings:"
+ "_createSummaryFeedbackSuggestionIfNeededForRequest:sectionSettings:"
+ "_isStackedSummary"
+ "_requestsWithSummaryFeedbackSuggestions"
+ "handleBadAction:"
+ "handleGoodAction:"
+ "initWithNotificationRequest:bundleDisplayName:isStackedSummary:managementDelegate:suggestionDelegate:"
+ "isStackedSummary"
+ "notification-management-summary-feedback-bad"
+ "notification-management-summary-feedback-good"
+ "requestsWithSummaryFeedbackSuggestions"
+ "setRequestsWithSummaryFeedbackSuggestions:"
+ "suggestionManager:isSummaryVisibleForNotificationRequest:"
+ "suggestionManager:isThreadSummaryVisibleForNotificationRequest:"
- "*"
- "@\"NCSummarizationChinSuggestionManager\""
- "B24@0:8@\"NCNotificationStructuredSectionList\"16"
- "Creating stack summary for request %{public}@ from section %{public}@"
- "NCNotificationManagementStackSummarySuggestionContentProvider"
- "NOTIFICATION_MANAGEMENT_STACK_SUMMARY_SUGGESTION"
- "NOTIFICATION_MANAGEMENT_SUGGESTION_CONTINUE"
- "Removing stack summary suggestion for request %{public}@ from section %{public}@"
- "T@\"NCSummarizationChinSuggestionManager\",&,N,V_summarizationSuggestionManager"
- "T@\"NSMutableSet\",&,N,V_requestsWithStackSummarySuggestions"
- "_createNewStackSummarySuggestionForNotificationRequest:sectionSettings:"
- "_createStackSummarySuggestionIfNeededForRequest:sectionSettings:"
- "_requestsWithStackSummarySuggestions"
- "_summarizationSuggestionManager"
- "handleContinueAction:"
- "initWithIgnore:"
- "initWithNotificationRequest:bundleDisplayName:managementDelegate:suggestionDelegate:summarizationSuggestionManager:"
- "isNotificationStructuredSectionListCollapsable:"
- "notification-stack-summary-continue "
- "notification-stack-summary-turnoff"
- "notificationListComponent:requestsStackSummarySuggestionVisible:forRequest:"
- "recordEvent:bundleId:"
- "requestMatchingRequest:inSet:"
- "requestStackSummarySuggestionVisible:forRequest:"
- "requestsWithStackSummarySuggestions"
- "setRequestsWithStackSummarySuggestions:"
- "setSummarizationSuggestionManager:"
- "shouldShowChinSuggestionAfterStackSummaryShownForBundleId:"
- "summarizationSuggestionManager"
- "v36@0:8@\"<NCNotificationListComponent>\"16B24@\"NCNotificationRequest\"28"

```
