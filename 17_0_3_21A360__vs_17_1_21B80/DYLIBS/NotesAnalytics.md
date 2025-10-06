## NotesAnalytics

> `/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics`

```diff

-2448.3.0.0.0
-  __TEXT.__text: 0x556dc
+2463.0.0.0.0
+  __TEXT.__text: 0x56904
   __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x8ec4
+  __TEXT.__objc_methlist: 0x8f44
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x6511
-  __TEXT.__gcc_except_tab: 0x7bc
-  __TEXT.__oslogstring: 0xc17
+  __TEXT.__cstring: 0x65aa
+  __TEXT.__gcc_except_tab: 0x8b0
+  __TEXT.__oslogstring: 0xc05
   __TEXT.__dlopen_cstrs: 0xcc
-  __TEXT.__unwind_info: 0x1a50
+  __TEXT.__unwind_info: 0x1ab4
   __TEXT.__objc_classname: 0x2492
-  __TEXT.__objc_methname: 0x19bb8
-  __TEXT.__objc_methtype: 0x1a45
-  __TEXT.__objc_stubs: 0xb3a0
+  __TEXT.__objc_methname: 0x19e94
+  __TEXT.__objc_methtype: 0x1a34
+  __TEXT.__objc_stubs: 0xb500
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x1240
+  __DATA_CONST.__const: 0x1298
   __DATA_CONST.__objc_classlist: 0xb30
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x11c90
-  __DATA_CONST.__objc_selrefs: 0x34a8
+  __DATA_CONST.__objc_const: 0x11cf0
+  __DATA_CONST.__objc_selrefs: 0x34f8
   __DATA_CONST.__objc_arraydata: 0x2410
-  __AUTH_CONST.__cfstring: 0x9440
+  __AUTH_CONST.__cfstring: 0x94c0
   __AUTH_CONST.__objc_const: 0xa5f0
   __AUTH_CONST.__objc_intobj: 0x5cd0
   __AUTH_CONST.__objc_arrayobj: 0x318

   __AUTH_CONST.__auth_got: 0x388
   __AUTH.__objc_data: 0x43d0
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xce0
+  __DATA.__objc_classrefs: 0xcf8
   __DATA.__objc_superrefs: 0x758
-  __DATA.__objc_ivar: 0xc84
+  __DATA.__objc_ivar: 0xc8c
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x2c10

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 956D49CE-B343-374A-A177-4146FADE293C
-  Functions: 2692
-  Symbols:   11259
-  CStrings:  6212
+  UUID: F0AB4189-B8BF-3F10-B4D6-50533AEC5EC1
+  Functions: 2715
+  Symbols:   11326
+  CStrings:  6236
 
Symbols:
+ -[ICNAController endSessionBackgroundTaskIdentifiersByWindowSceneIdentifier]
+ -[ICNAController enterGroupWithSubtracker:]
+ -[ICNAController killEndSessionBackgroundTaskIfNecessaryForWindowScene:]
+ -[ICNAController leaveGroupWithSubtracker:]
+ -[ICNAController leaveGroupWithSubtracker:completionHandler:]
+ -[ICNAController setEndSessionBackgroundTaskIdentifiersByWindowSceneIdentifier:]
+ -[ICNAController startWindowSceneSessionWithType:windowScene:successHandler:]
+ -[ICNAEventReporter initWithSubTrackerName:view:].cold.1
+ -[ICNAEventReporter initWithSubTrackerName:window:].cold.1
+ -[ICNAEventReporter initWithSubTrackerName:windowScene:].cold.1
+ -[ICNAEventReporter startOnboardingScreenViewEventDurationTracking]
+ -[ICNAEventReporter submitOnboardingScreenViewEventWithType:]
+ -[ICNAInlineDrawingRecognitionReporter analyticsSessionWillEnd:]
+ -[ICNAInlineDrawingRecognitionReporter submitReportsWithEventReporter:]
+ -[ICNASnapshotReporter beginMiniSnapshotBackgroundTask]
+ -[ICNASnapshotReporter killMiniSnapshotBackgroundTaskIfNecessary]
+ -[ICNASnapshotReporter miniSnapshotBackgroundTaskIdentifier]
+ -[ICNASnapshotReporter setMiniSnapshotBackgroundTaskIdentifier:]
+ GCC_except_table120
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table191
+ GCC_except_table195
+ GCC_except_table210
+ GCC_except_table217
+ GCC_except_table229
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table246
+ GCC_except_table31
+ GCC_except_table32
+ GCC_except_table38
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table57
+ GCC_except_table80
+ GCC_except_table83
+ GCC_except_table97
+ _ICNASessionFlushTimedDataNotification
+ _OBJC_CLASS_$_UIWindowScene
+ _OBJC_IVAR_$_ICNAController._endSessionBackgroundTaskIdentifiersByWindowSceneIdentifier
+ _OBJC_IVAR_$_ICNASnapshotReporter._miniSnapshotBackgroundTaskIdentifier
+ ___39-[ICNAController startSessionWithType:]_block_invoke.99
+ ___42-[ICNASnapshotReporter submitMiniSnapshot]_block_invoke.521
+ ___43-[ICNAController enterGroupWithSubtracker:]_block_invoke
+ ___55-[ICNASnapshotReporter beginMiniSnapshotBackgroundTask]_block_invoke
+ ___55-[ICNASnapshotReporter beginMiniSnapshotBackgroundTask]_block_invoke_2
+ ___55-[ICNASnapshotReporter beginMiniSnapshotBackgroundTask]_block_invoke_2.cold.1
+ ___60-[ICNASearchResultExposureReporter analyticsSessionWillEnd:]_block_invoke.60
+ ___61-[ICNAController leaveGroupWithSubtracker:completionHandler:]_block_invoke
+ ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.106
+ ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.106.cold.1
+ ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.108
+ ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.118
+ ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.119
+ ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.119.cold.1
+ ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.120
+ ___77-[ICNAController startWindowSceneSessionWithType:windowScene:successHandler:]_block_invoke
+ ___77-[ICNAController startWindowSceneSessionWithType:windowScene:successHandler:]_block_invoke.102
+ ___77-[ICNAController startWindowSceneSessionWithType:windowScene:successHandler:]_block_invoke_2
+ ___77-[ICNAController startWindowSceneSessionWithType:windowScene:successHandler:]_block_invoke_3
+ ___90-[ICNAController endWindowSceneSessionSynchronously:forSessionType:endReason:windowScene:]_block_invoke.124
+ ___90-[ICNAController endWindowSceneSessionSynchronously:forSessionType:endReason:windowScene:]_block_invoke.126
+ ___90-[ICNAController endWindowSceneSessionSynchronously:forSessionType:endReason:windowScene:]_block_invoke.127
+ ___90-[ICNAController endWindowSceneSessionSynchronously:forSessionType:endReason:windowScene:]_block_invoke_2.125
+ ___90-[ICNAController endWindowSceneSessionSynchronously:forSessionType:endReason:windowScene:]_block_invoke_3.cold.1
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.182
+ ___block_literal_global.205
+ ___block_literal_global.386
+ ___block_literal_global.79
+ ___block_literal_global.86
+ _objc_msgSend$beginBackgroundTaskWithName:expirationHandler:
+ _objc_msgSend$beginMiniSnapshotBackgroundTask
+ _objc_msgSend$endSessionBackgroundTaskIdentifiersByWindowSceneIdentifier
+ _objc_msgSend$enterGroup
+ _objc_msgSend$enterGroupWithSubtracker:
+ _objc_msgSend$initWithOnboardingScreenType:
+ _objc_msgSend$initWithOnboardingScreenType:onboardingUserAction:
+ _objc_msgSend$initWithOnboardingUserAction:
+ _objc_msgSend$killEndSessionBackgroundTaskIfNecessaryForWindowScene:
+ _objc_msgSend$killMiniSnapshotBackgroundTaskIfNecessary
+ _objc_msgSend$leaveGroup
+ _objc_msgSend$leaveGroupWithSubtracker:
+ _objc_msgSend$leaveGroupWithSubtracker:completionHandler:
+ _objc_msgSend$miniSnapshotBackgroundTaskIdentifier
+ _objc_msgSend$sessionDidStartForWindowScene:
+ _objc_msgSend$setMiniSnapshotBackgroundTaskIdentifier:
+ _objc_msgSend$submitReportsWithEventReporter:
- -[ICNAController pushDataObject:unique:onlyOnce:]
- -[ICNAController pushDataObjects:unique:onlyOnce:]
- -[ICNAController startWindowSceneSessionWithType:windowScene:]
- -[ICNAController trackTimedEventType:]
- -[ICNAInlineDrawingRecognitionReporter createReportForDrawing:drawingID:insideNote:].cold.1
- -[ICNAInlineDrawingRecognitionReporter createReportForDrawing:drawingID:insideNote:].cold.2
- -[ICNAInlineDrawingRecognitionReporter submitReports]
- GCC_except_table118
- GCC_except_table142
- GCC_except_table145
- GCC_except_table189
- GCC_except_table193
- GCC_except_table208
- GCC_except_table216
- GCC_except_table228
- GCC_except_table29
- GCC_except_table30
- GCC_except_table34
- GCC_except_table46
- GCC_except_table55
- GCC_except_table76
- GCC_except_table95
- _OBJC_CLASS_$_NSValue
- ___39-[ICNAController startSessionWithType:]_block_invoke.96
- ___60-[ICNASearchResultExposureReporter analyticsSessionWillEnd:]_block_invoke.59
- ___62-[ICNAController startWindowSceneSessionWithType:windowScene:]_block_invoke
- ___62-[ICNAController startWindowSceneSessionWithType:windowScene:]_block_invoke.100
- ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.101
- ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.101.cold.1
- ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.103
- ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.110
- ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.113
- ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.114
- ___67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.114.cold.1
- ___90-[ICNAController endWindowSceneSessionSynchronously:forSessionType:endReason:windowScene:]_block_invoke.116
- ___90-[ICNAController endWindowSceneSessionSynchronously:forSessionType:endReason:windowScene:]_block_invoke.117
- ___block_literal_global.172
- ___block_literal_global.195
- ___block_literal_global.380
- ___block_literal_global.76
- ___block_literal_global.83
- _objc_msgSend$beginBackgroundTaskWithExpirationHandler:
- _objc_msgSend$pushDataObject:unique:onlyOnce:
- _objc_msgSend$sessionDidStart
- _objc_msgSend$submitEventOfType:pushThenPopDataObjects:
- _objc_msgSend$submitReports
- _objc_msgSend$valueWithNonretainedObject:
CStrings:
+ "\x14"
+ ",\x15"
+ "Analytics mini snapshot"
+ "Background task expired before mini snapshot completed."
+ "Finish end analytics session operation"
+ "Finish end analytics window scene session operation"
+ "ICNASessionFlushTimedDataNotification"
+ "T@\"NSMutableDictionary\",&,N,V_endSessionBackgroundTaskIdentifiersByWindowSceneIdentifier"
+ "T@\"NSNumber\",&,N,V_miniSnapshotBackgroundTaskIdentifier"
+ "Tried to init event reporter for a nil view."
+ "Tried to init event reporter for a nil window scene."
+ "Tried to init event reporter for a nil window."
+ "_endSessionBackgroundTaskIdentifiersByWindowSceneIdentifier"
+ "_miniSnapshotBackgroundTaskIdentifier"
+ "beginBackgroundTaskWithName:expirationHandler:"
+ "beginMiniSnapshotBackgroundTask"
+ "endSessionBackgroundTaskIdentifiersByWindowSceneIdentifier"
+ "endWindowSceneSession Background task expired before endSession completed."
+ "enterGroup"
+ "enterGroupWithSubtracker:"
+ "killEndSessionBackgroundTaskIfNecessaryForWindowScene:"
+ "killMiniSnapshotBackgroundTaskIfNecessary"
+ "leaveGroup"
+ "leaveGroupWithSubtracker:"
+ "leaveGroupWithSubtracker:completionHandler:"
+ "miniSnapshotBackgroundTaskIdentifier"
+ "sessionDidStartForWindowScene:"
+ "setEndSessionBackgroundTaskIdentifiersByWindowSceneIdentifier:"
+ "setMiniSnapshotBackgroundTaskIdentifier:"
+ "startOnboardingScreenViewEventDurationTracking"
+ "startWindowSceneSessionWithType:windowScene:successHandler:"
+ "submitOnboardingScreenViewEventWithType:"
+ "submitReportsWithEventReporter:"
- "\x13"
- ",\x14"
- "Not firing InlineDrawingHandWritingRecognitionEvent as we have only accumulated reports for %lu unique drawings. Expecting more than %lu unique drawings, or when session ends."
- "Submitted a batch of InlineDrawingHandWritingRecognitionEvent. Currently accumulated reports for %lu unique drawings."
- "beginBackgroundTaskWithExpirationHandler:"
- "pushDataObject:unique:onlyOnce:"
- "pushDataObjects:unique:onlyOnce:"
- "sessionDidStart"
- "startWindowSceneSessionWithType:windowScene:"
- "submitReports"
- "trackTimedEventType:"
- "v32@0:8@16B24B28"
- "valueWithNonretainedObject:"

```
