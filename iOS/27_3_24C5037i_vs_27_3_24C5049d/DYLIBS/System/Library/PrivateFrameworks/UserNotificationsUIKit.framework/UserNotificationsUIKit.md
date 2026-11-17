## UserNotificationsUIKit

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

```diff

-1077.3.6.0.0
-  __TEXT.__text: 0x1b35cc
-  __TEXT.__objc_methlist: 0x1ae3c
+1077.3.10.0.0
+  __TEXT.__text: 0x1b4ec4
+  __TEXT.__objc_methlist: 0x1af14
   __TEXT.__const: 0x43e4
-  __TEXT.__gcc_except_tab: 0x2bf8
-  __TEXT.__cstring: 0xa02d
-  __TEXT.__oslogstring: 0x10199
+  __TEXT.__gcc_except_tab: 0x2d44
+  __TEXT.__cstring: 0x9fdd
+  __TEXT.__oslogstring: 0x101f9
   __TEXT.__ustring: 0x22
   __TEXT.__constg_swiftt: 0x1b80
   __TEXT.__swift5_typeref: 0x3d20

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_cont: 0x4c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x8d60
+  __TEXT.__unwind_info: 0x8dd8
   __TEXT.__eh_frame: 0xcb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x41a8
-  __DATA_CONST.__objc_classlist: 0x7f8
+  __DATA_CONST.__const: 0x41d8
+  __DATA_CONST.__objc_classlist: 0x800
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x5f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcc80
+  __DATA_CONST.__objc_selrefs: 0xcce0
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x570
+  __DATA_CONST.__objc_superrefs: 0x578
   __DATA_CONST.__objc_arraydata: 0x158
   __DATA_CONST.__got: 0x18b0
   __AUTH_CONST.__const: 0x5058
-  __AUTH_CONST.__cfstring: 0x7f80
-  __AUTH_CONST.__objc_const: 0x26b00
+  __AUTH_CONST.__cfstring: 0x7f60
+  __AUTH_CONST.__objc_const: 0x26c30
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x1570
-  __AUTH.__objc_data: 0x23f0
+  __AUTH.__objc_data: 0x2440
   __AUTH.__data: 0x3d8
-  __DATA.__objc_ivar: 0x17bc
+  __DATA.__objc_ivar: 0x17cc
   __DATA.__data: 0x51c0
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10976
-  Symbols:   14472
+  Functions: 10999
+  Symbols:   14510
   CStrings:  2165
 
Symbols:
+ -[NCAppPickerViewController _updateLayoutForCurrentWidthIfNeeded]
+ -[NCDigestOnboardingCollectionView .cxx_destruct]
+ -[NCDigestOnboardingCollectionView layoutSubviews]
+ -[NCDigestOnboardingCollectionView setWidthDidChangeHandler:]
+ -[NCDigestOnboardingCollectionView widthDidChangeHandler]
+ -[NCNotificationEventTracker _endInteractionWithNotificationRequest:]
+ -[NCNotificationEventTracker _interactionLocationForState:]
+ -[NCNotificationEventTracker _interactionUIForNotificationRequest:]
+ -[NCNotificationEventTracker _longLookInteractionUIForNotificationRequest:withState:]
+ -[NCNotificationEventTracker _recordInteractionWithNotificationRequest:withState:]
+ -[NCNotificationEventTracker clearedNotificationRequests:inSectionType:clearAll:]
+ -[NCNotificationEventTracker longLookPresentedForNotificationRequest:withState:]
+ -[NCNotificationEventTracker priorityFeedback:forNotificationRequest:]
+ -[NCNotificationOptionsMenuBuilder _sendPriorityFeedback:withFeedbackManager:]
+ -[NCNotificationOptionsMenuBuilder _sendSummaryFeedback:withFeedbackManager:isShowingStackSummary:]
+ -[NCNotificationOptionsMenuBuilder _summaryFeedbackNegativeWithFeedbackManager:isShowingStackSummary:]
+ -[NCNotificationOptionsMenuBuilder _summaryFeedbackPositiveWithFeedbackManager:isShowingStackSummary:]
+ -[NCNotificationOptionsMenuBuilder _summaryFeedbackReportConcernWithFeedbackManager:isShowingStackSummary:]
+ -[NCNotificationStructuredListViewController _sectionTypeOfNotificationListComponent:]
+ -[NCSchedulerViewController _availableContentWidth]
+ -[NCSchedulerViewController _updateLayoutForCurrentWidthIfNeeded]
+ -[NCSchedulerViewController _updateLayoutSizesForWidth:onLayout:]
+ GCC_except_table112
+ GCC_except_table211
+ GCC_except_table50
+ _NCATXNotificationDeliveryUIForUILocation
+ _NCNotificationListSectionTypeIdentifier
+ _NCUILocationForSectionType
+ _OBJC_CLASS_$_NCDigestOnboardingCollectionView
+ _OBJC_IVAR_$_NCDigestOnboardingCollectionView._lastLayoutWidth
+ _OBJC_IVAR_$_NCDigestOnboardingCollectionView._widthDidChangeHandler
+ _OBJC_IVAR_$_NCNotificationEventTracker._interactionLocations
+ _OBJC_IVAR_$_NCSchedulerViewController._cachedLayoutWidth
+ _OBJC_METACLASS_$_NCDigestOnboardingCollectionView
+ _OBJC_METACLASS_$_UICollectionView
+ __OBJC_$_INSTANCE_METHODS_NCDigestOnboardingCollectionView
+ __OBJC_$_INSTANCE_VARIABLES_NCDigestOnboardingCollectionView
+ __OBJC_$_PROP_LIST_NCDigestOnboardingCollectionView
+ __OBJC_CLASS_RO_$_NCDigestOnboardingCollectionView
+ __OBJC_METACLASS_RO_$_NCDigestOnboardingCollectionView
+ ___102-[NCNotificationOptionsMenuBuilder _summaryFeedbackNegativeWithFeedbackManager:isShowingStackSummary:]_block_invoke
+ ___102-[NCNotificationOptionsMenuBuilder _summaryFeedbackPositiveWithFeedbackManager:isShowingStackSummary:]_block_invoke
+ ___107-[NCNotificationOptionsMenuBuilder _summaryFeedbackReportConcernWithFeedbackManager:isShowingStackSummary:]_block_invoke
+ ___40-[NCAppPickerViewController viewDidLoad]_block_invoke
+ ___40-[NCSchedulerViewController viewDidLoad]_block_invoke
+ ___block_descriptor_49_e8_32s40s_e18_v16?0"UIAction"8ls32l8s40l8
- -[NCNotificationEventTracker longLookPresentedForNotificationRequest:]
- -[NCNotificationOptionsMenuBuilder _summaryFeedbackNegativeWithFeedbackManager:]
- -[NCNotificationOptionsMenuBuilder _summaryFeedbackPositiveWithFeedbackManager:]
- -[NCNotificationOptionsMenuBuilder _summaryFeedbackReportConcernWithFeedbackManager:]
- GCC_except_table42
- ___80-[NCNotificationOptionsMenuBuilder _summaryFeedbackNegativeWithFeedbackManager:]_block_invoke
- ___80-[NCNotificationOptionsMenuBuilder _summaryFeedbackPositiveWithFeedbackManager:]_block_invoke
- ___85-[NCNotificationOptionsMenuBuilder _summaryFeedbackReportConcernWithFeedbackManager:]_block_invoke
CStrings:
+ "Skip content-reveal re-pin: a page scroll is already in flight; scrollState: %{public}s"
+ "listSectionType"
- "NOTIFICATION_DIGEST_ONBOARDING_APP_PICKER_CANCEL"
- "NOTIFICATION_DIGEST_ONBOARDING_SCHEDULER_CANCEL"
```
