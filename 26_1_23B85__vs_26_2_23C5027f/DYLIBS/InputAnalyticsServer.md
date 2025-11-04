## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-111.2.1.0.0
-  __TEXT.__text: 0x51f08
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_methlist: 0x43ac
-  __TEXT.__const: 0x430
-  __TEXT.__cstring: 0x3fa9
-  __TEXT.__oslogstring: 0x5853
-  __TEXT.__gcc_except_tab: 0x890
+111.3.100.0.0
+  __TEXT.__text: 0x55388
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x4624
+  __TEXT.__const: 0x440
+  __TEXT.__cstring: 0x4199
+  __TEXT.__oslogstring: 0x5a43
+  __TEXT.__gcc_except_tab: 0x98c
   __TEXT.__swift5_typeref: 0x10d
   __TEXT.__swift5_capture: 0x98
   __TEXT.__constg_swiftt: 0x4c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0xf70
+  __TEXT.__unwind_info: 0x1028
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0xa48
-  __TEXT.__objc_methname: 0x9bf7
-  __TEXT.__objc_methtype: 0xe4c
-  __TEXT.__objc_stubs: 0x7d40
-  __DATA_CONST.__got: 0x1000
-  __DATA_CONST.__const: 0x1000
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __TEXT.__objc_classname: 0xa82
+  __TEXT.__objc_methname: 0xa04d
+  __TEXT.__objc_methtype: 0xe5a
+  __TEXT.__objc_stubs: 0x8060
+  __DATA_CONST.__got: 0x1028
+  __DATA_CONST.__const: 0x1070
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2250
+  __DATA_CONST.__objc_selrefs: 0x2318
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1b0
+  __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x188
-  __AUTH_CONST.__auth_got: 0x768
-  __AUTH_CONST.__const: 0xe18
-  __AUTH_CONST.__cfstring: 0x48c0
-  __AUTH_CONST.__objc_const: 0x7728
-  __AUTH_CONST.__objc_intobj: 0xde0
+  __AUTH_CONST.__auth_got: 0x770
+  __AUTH_CONST.__const: 0xef8
+  __AUTH_CONST.__cfstring: 0x49e0
+  __AUTH_CONST.__objc_const: 0x7a48
+  __AUTH_CONST.__objc_intobj: 0xe40
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH.__objc_data: 0xc48
+  __AUTH.__objc_data: 0xce8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x520
+  __DATA.__objc_ivar: 0x548
   __DATA.__data: 0x430
-  __DATA.__bss: 0x188
+  __DATA.__bss: 0x1f8
   __DATA_DIRTY.__objc_data: 0xfc8
   __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0x368

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7AEC0D7F-980A-3CC0-8117-35696547E846
-  Functions: 1860
-  Symbols:   667
-  CStrings:  3508
+  UUID: FC3C13D6-B263-3593-B523-3EDB67B0EF7D
+  Functions: 1933
+  Symbols:   673
+  CStrings:  3583
 
Symbols:
+ _IAChannelCandidateBar
+ _IASignalCandidateBarMixmojiCombineButtonPressed
+ _IASignalCandidateBarMixmojiCombineButtonShown
+ _IASignalCandidateBarReset
+ _IASignalSmartRepliesPollActionShown
+ _objc_release_x2
CStrings:
+ "%@ [%@] state=%@ errors=%@"
+ "Associating UIAppeared session with pending analyzer."
+ "CandidateShown"
+ "Claiming UIAppeared signal."
+ "Created analyzer for action type %{private}@ with session ID %{private}@"
+ "Creating new analyzer on UIAppeared."
+ "ERROR: analyzer pointed to by action type associated with analyzer ID %@ does not match given analyzerSessionId %@"
+ "ERROR: dangling analyzer ID without an action type for session %@"
+ "ERROR: more than 2 analyzers detected"
+ "IASCandidateBar"
+ "IASCandidateBarAnalyzer"
+ "IASCandidateBarSessionManager"
+ "IASCandidateBarSessionManager.m"
+ "Joining pending session. Selectively updating cache from joining signal."
+ "Multiple analyzers (%lu) tried to claim the UIAppeared signal!"
+ "Observed MixmojiCombineButtonPressed. Creating pending analyzer."
+ "T@\"NSDate\",&,N,V_shownTimestamp"
+ "T@\"NSDate\",C,N,V_lastCreationStartedSignalTimestamp"
+ "T@\"NSMutableDictionary\",&,N,V_actionTypeToAnalyzerMap"
+ "T@\"NSMutableDictionary\",&,N,V_analyzerIdToActionTypeMap"
+ "T@\"NSString\",&,N,V_bundleId"
+ "TB,N,V_isEngaged"
+ "TQ,N,V_actionType"
+ "TQ,N,V_numInitialEmojisCombined"
+ "TQ,N,V_shownDuration"
+ "Terminated session for existing analyzer for session %{private}@"
+ "_actionType"
+ "_actionTypeToAnalyzerMap"
+ "_analyzerIdToActionTypeMap"
+ "_isEngaged"
+ "_lastCreationStartedSignalTimestamp"
+ "_numInitialEmojisCombined"
+ "_shownDuration"
+ "_shownTimestamp"
+ "actionType"
+ "actionTypeToAnalyzerMap"
+ "analyzerIdToActionTypeMap"
+ "cacheIngredientCounts:shouldStartNewPrompt:"
+ "com.apple.inputAnalytics.messagesActionEngagement"
+ "com.apple.inputAnalytics.server.IASCandidateBarSessionManager"
+ "com.apple.inputanalytics.server.IASCandidateBarAnalyzer"
+ "getShownDurationMsWithEndTimestamp:"
+ "handleCreationStartedSignal:shouldStartNewPrompt:"
+ "isValidCandidateBarSignal:"
+ "joinPendingSessionWithSignal:"
+ "lastCreationStartedSignalTimestamp"
+ "numInitialEmojisCombined"
+ "processBundleId:"
+ "processSignalAfterShown:withExpectedActionType:"
+ "propagateTestDelegateForAnalyzer:"
+ "resetSignals"
+ "setActionType:"
+ "setActionTypeToAnalyzerMap:"
+ "setAnalyzerIdToActionTypeMap:"
+ "setIsEngaged:"
+ "setLastCreationStartedSignalTimestamp:"
+ "setNumInitialEmojisCombined:"
+ "setShownDuration:"
+ "setShownTimestamp:"
+ "shownDuration"
+ "shownTimestamp"
+ "signalsToActionType"
+ "startSignals"
+ "v32@0:8@16Q24"
- "cacheIngredientCounts:"
- "handleCreationStartedSignal:"

```
