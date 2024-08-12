## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-61.0.0.0.0
-  __TEXT.__text: 0x12114
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__objc_methlist: 0xdc4
-  __TEXT.__const: 0x132
-  __TEXT.__oslogstring: 0x1ec0
-  __TEXT.__cstring: 0x1042
-  __TEXT.__gcc_except_tab: 0x2bc
-  __TEXT.__swift5_typeref: 0x86
-  __TEXT.__swift5_capture: 0x60
+64.101.0.0.0
+  __TEXT.__text: 0x136cc
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0xf64
+  __TEXT.__const: 0x142
+  __TEXT.__oslogstring: 0x1fb0
+  __TEXT.__cstring: 0x10f2
+  __TEXT.__gcc_except_tab: 0x358
+  __TEXT.__swift5_typeref: 0x84
+  __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x500
-  __TEXT.__eh_frame: 0x2c8
-  __TEXT.__objc_classname: 0x23c
-  __TEXT.__objc_methname: 0x2467
-  __TEXT.__objc_methtype: 0x4db
-  __TEXT.__objc_stubs: 0x1a60
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x3d0
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__unwind_info: 0x570
+  __TEXT.__eh_frame: 0x2f8
+  __TEXT.__objc_classname: 0x264
+  __TEXT.__objc_methname: 0x264b
+  __TEXT.__objc_methtype: 0x4e5
+  __TEXT.__objc_stubs: 0x1bc0
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0x440
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x858
+  __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x3d8
+  __AUTH_CONST.__auth_got: 0x3e0
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x368
-  __AUTH_CONST.__cfstring: 0xc20
-  __AUTH_CONST.__objc_const: 0x20f0
+  __AUTH_CONST.__const: 0x3d8
+  __AUTH_CONST.__cfstring: 0xce0
+  __AUTH_CONST.__objc_const: 0x23f8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x570
+  __AUTH.__objc_data: 0x200
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x148
-  __DATA.__data: 0x2a0
-  __DATA.__bss: 0x118
+  __DATA.__objc_ivar: 0x168
+  __DATA.__data: 0x2b0
+  __DATA.__bss: 0x78
+  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 489
-  Symbols:   170
-  CStrings:  779
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 529
+  Symbols:   184
+  CStrings:  813
 
Symbols:
+ _IAChannelWritingTools
+ _IAPayloadKeyWritingToolsFeature
+ _IAPayloadKeyWritingToolsFeatureDetails
+ _IAPayloadKeyWritingToolsUI
+ _OBJC_CLASS_$_IAUtility
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retain_x24
+ _objc_unsafeClaimAutoreleasedReturnValue
- _swift_retain
CStrings:
+ "\x01\x11c\x14"
+ "\x02\x18\x13"
+ "@\"NSDate\""
+ "G"
+ "Handling channel %!{(MISSING)private}@ signal %!{(MISSING)private}@"
+ "IAGeneric"
+ "IASGenericAnalyzer"
+ "IASGenericAnalyzer.m"
+ "IASStatelessSessionManager"
+ "IASTextInputActionsAnalyzer"
+ "IASTextInputActionsAnalyzer.m"
+ "IASTextInputActionsAnalyzerEntry"
+ "Initialized"
+ "Perform garbage collection on all session managers..."
+ "Stateless session manager initialized with generic analyzer of UUID %!@(MISSING)"
+ "T@\"NSDate\",C,N,V_dateOfLastAction"
+ "T@\"NSDictionary\",&,N,V_channelBasedPayloadKeyAllowList"
+ "T@\"NSUUID\",&,N,V_genericAnalyzerId"
+ "TextInputActionsAnalyzer"
+ "[%!{(MISSING)private}@][IASTextInputActionsAnalyzer] Initial deletion %!l(MISSING)u, %!l(MISSING)u"
+ "[%!{(MISSING)private}@][IASTextInputActionsAnalyzer] New input mode key found - initializing new entry for source:%!l(MISSING)u actionType:%!l(MISSING)u flagOptions%!l(MISSING)u inputMode:\"%!{(MISSING)private}@\""
+ "[%!{(MISSING)private}@][IASTextInputActionsAnalyzer] Updated entry for source:%!l(MISSING)u actionType:%!l(MISSING)u flagOptions%!l(MISSING)u inputMode:\"%!{(MISSING)private}@\" by netChars:%!l(MISSING)d userRemovedChars:%!l(MISSING)d netEmojiChars:%!l(MISSING)d userRemovedEmojiChars:%!l(MISSING)d actions:%!l(MISSING)d"
+ "[%!{(MISSING)private}@][IASTextInputActionsAnalyzer] consumeAction(): %!{(MISSING)private}@ netCharactersDelta:%!l(MISSING)d userRemovedCharactersDelta:%!l(MISSING)d netEmojiCharactersDelta:%!l(MISSING)d sysRemovedObjectsDelta:%!l(MISSING)d inputActionsDelta:%!l(MISSING)d for source:%!l(MISSING)u type:%!l(MISSING)u inputMode:%!{(MISSING)private}@"
+ "[%!{(MISSING)private}@][IASTextInputActionsAnalyzer] emoji search - override insertion %!l(MISSING)u, deletion %!l(MISSING)u, net %!l(MISSING)d"
+ "[%!{(MISSING)private}@][IASTextInputActionsAnalyzer] largestSessionDeletionLength %!l(MISSING)u -> %!l(MISSING)u"
+ "[%!{(MISSING)private}@][IASTextInputActionsAnalyzer] largestSessionInsertionLength %!l(MISSING)u -> %!l(MISSING)u"
+ "[%!{(MISSING)private}@]nil inputMode passed to [IASTextInputActionsAnalyzer consumeAction:] in action '%!{(MISSING)private}@'"
+ "[IASTextInputActionsAnalyzer] Cached keyboardTrialParameters"
+ "[IASTextInputActionsAnalyzer] Enumerating TextInputActions..."
+ "[IASTextInputActionsAnalyzer] Initial deletion latch"
+ "[IASTextInputActionsAnalyzer] Initialized analyzer"
+ "[IASTextInputActionsAnalyzer] New key found - initializing new array for key \"%!{(MISSING)private}@\" with capacity %!l(MISSING)u"
+ "[IASTextInputActionsAnalyzer] New key found - initializing new array for key %!l(MISSING)u with capacity %!l(MISSING)u"
+ "[IASTextInputActionsAnalyzer] New key found - initializing new dictionary for key %!l(MISSING)u with capacity %!l(MISSING)u"
+ "[IASTextInputActionsAnalyzer] Received nil input mode unique key"
+ "[IASTextInputActionsAnalyzer] Reset analyzer"
+ "[IASTextInputActionsAnalyzer] eventHandler nil"
+ "_appendAllowListedPayloadKeyAndValueTo:forSignalAnalyticsObject:"
+ "_channelBasedPayloadKeyAllowList"
+ "_dateOfLastAction"
+ "_genericAnalyzerId"
+ "analyzerWithName:"
+ "broadcasting action to generic analyzer %!{(MISSING)private}@"
+ "channelBasedPayloadKeyAllowList"
+ "com.apple.inputAnalytics.server.IASGenericAnalyzer"
+ "com.apple.inputAnalytics.server.IASStatelessSessionManager"
+ "com.apple.inputAnalytics.signalAnalytics."
+ "compare:"
+ "date"
+ "dateOfLastAction"
+ "dateWithTimeInterval:sinceDate:"
+ "error with broadcast, analyzer list does not exist for analyzerId %!{(MISSING)private}@"
+ "feature"
+ "featureDetails"
+ "generateAnalyzerEntryFromAction:"
+ "genericAnalyzerId"
+ "increaseCountForAppBundleId:forSource:forActionType:forFlagOptions:forInputModeKey:byAnalyzerEntry:"
+ "lookupAppBundle:"
+ "nil raw action passed to [IASTextInputActionsAnalyzer consumeAction:]"
+ "periodic24HourEvents called"
+ "periodic24HourEvents was unable to convert weak reference to strong within block"
+ "setChannelBasedPayloadKeyAllowList:"
+ "setDateOfLastAction:"
+ "setGenericAnalyzerId:"
+ "shouldBeGarbageCollected"
+ "signal"
+ "ui"
+ "v32@?0@\"NSString\"8@\"IASTextInputActionsAnalyzerEntry\"16^B24"
- "\x01\x11c\x13"
- "\x02\x18\x12"
- "IASTextInputActionsAccumulator"
- "IASTextInputActionsAccumulator.m"
- "IASTextInputActionsAccumulatorEntry"
- "TextInputActionsAccumulator"
- "[%!{(MISSING)private}@] generated content is nil"
- "[%!{(MISSING)private}@] original content is nil"
- "[%!{(MISSING)private}@][IASTextInputActionsAccumulator] Initial deletion %!l(MISSING)u, %!l(MISSING)u"
- "[%!{(MISSING)private}@][IASTextInputActionsAccumulator] New input mode key found - initializing new entry for source:%!l(MISSING)u actionType:%!l(MISSING)u flagOptions%!l(MISSING)u inputMode:\"%!{(MISSING)private}@\""
- "[%!{(MISSING)private}@][IASTextInputActionsAccumulator] Updated entry for source:%!l(MISSING)u actionType:%!l(MISSING)u flagOptions%!l(MISSING)u inputMode:\"%!{(MISSING)private}@\" by netChars:%!l(MISSING)d userRemovedChars:%!l(MISSING)d netEmojiChars:%!l(MISSING)d userRemovedEmojiChars:%!l(MISSING)d actions:%!l(MISSING)d"
- "[%!{(MISSING)private}@][IASTextInputActionsAccumulator] consumeAction(): %!{(MISSING)private}@ netCharactersDelta:%!l(MISSING)d userRemovedCharactersDelta:%!l(MISSING)d netEmojiCharactersDelta:%!l(MISSING)d sysRemovedObjectsDelta:%!l(MISSING)d inputActionsDelta:%!l(MISSING)d for source:%!l(MISSING)u type:%!l(MISSING)u inputMode:%!{(MISSING)private}@"
- "[%!{(MISSING)private}@][IASTextInputActionsAccumulator] emoji search - override insertion %!l(MISSING)u, deletion %!l(MISSING)u, net %!l(MISSING)d"
- "[%!{(MISSING)private}@][IASTextInputActionsAccumulator] largestSessionDeletionLength %!l(MISSING)u -> %!l(MISSING)u"
- "[%!{(MISSING)private}@][IASTextInputActionsAccumulator] largestSessionInsertionLength %!l(MISSING)u -> %!l(MISSING)u"
- "[%!{(MISSING)private}@]nil inputMode passed to [IASTextInputActionsAccumulator consumeAction:] in action '%!{(MISSING)private}@'"
- "[IASTextInputActionsAccumulator] Cached keyboardTrialParameters"
- "[IASTextInputActionsAccumulator] Enumerating TextInputActions..."
- "[IASTextInputActionsAccumulator] Initial deletion latch"
- "[IASTextInputActionsAccumulator] Initialized accumulator"
- "[IASTextInputActionsAccumulator] New key found - initializing new array for key \"%!{(MISSING)private}@\" with capacity %!l(MISSING)u"
- "[IASTextInputActionsAccumulator] New key found - initializing new array for key %!l(MISSING)u with capacity %!l(MISSING)u"
- "[IASTextInputActionsAccumulator] New key found - initializing new dictionary for key %!l(MISSING)u with capacity %!l(MISSING)u"
- "[IASTextInputActionsAccumulator] Received nil input mode unique key"
- "[IASTextInputActionsAccumulator] Reset accumulator"
- "[IASTextInputActionsAccumulator] eventHandler nil"
- "accumulatorWithName:"
- "garbage collection triggered"
- "garbageCollect not implemented"
- "generateAccumulatorEntryFromAction:"
- "increaseCountForAppBundleId:forSource:forActionType:forFlagOptions:forInputModeKey:byAccumulatorEntry:"
- "nil raw action passed to [IASTextInputActionsAccumulator consumeAction:]"
- "publishDailyEvents"
- "v32@?0@\"NSString\"8@\"IASTextInputActionsAccumulatorEntry\"16^B24"

```
