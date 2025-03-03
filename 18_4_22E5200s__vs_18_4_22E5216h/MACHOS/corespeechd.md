## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3404.71.4.1.1
-  __TEXT.__text: 0x1736a8
-  __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_stubs: 0x1ef20
-  __TEXT.__objc_methlist: 0x19444
+3404.79.2.0.0
+  __TEXT.__text: 0x173cb8
+  __TEXT.__auth_stubs: 0x17a0
+  __TEXT.__objc_stubs: 0x1ef80
+  __TEXT.__objc_methlist: 0x194bc
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__const: 0x380
-  __TEXT.__gcc_except_tab: 0x4250
-  __TEXT.__cstring: 0x2a429
-  __TEXT.__objc_methname: 0x3f076
-  __TEXT.__oslogstring: 0x21b93
-  __TEXT.__objc_classname: 0x3520
-  __TEXT.__objc_methtype: 0x8745
-  __TEXT.__unwind_info: 0x5878
-  __DATA_CONST.__auth_got: 0xbc8
-  __DATA_CONST.__got: 0x13f8
+  __TEXT.__const: 0x390
+  __TEXT.__gcc_except_tab: 0x41d0
+  __TEXT.__objc_methname: 0x3f1d8
+  __TEXT.__cstring: 0x2a5df
+  __TEXT.__oslogstring: 0x21b2e
+  __TEXT.__objc_classname: 0x3521
+  __TEXT.__objc_methtype: 0x8762
+  __TEXT.__unwind_info: 0x58a0
+  __DATA_CONST.__auth_got: 0xbe8
+  __DATA_CONST.__got: 0x13d8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5d18
-  __DATA_CONST.__cfstring: 0x84a0
+  __DATA_CONST.__const: 0x5df8
+  __DATA_CONST.__cfstring: 0x8540
   __DATA_CONST.__objc_classlist: 0x980
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4f0

   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x4b0
-  __DATA.__objc_const: 0x28568
-  __DATA.__objc_selrefs: 0xbad8
-  __DATA.__objc_ivar: 0x1f30
+  __DATA.__objc_const: 0x28598
+  __DATA.__objc_selrefs: 0xbb10
+  __DATA.__objc_ivar: 0x1f34
   __DATA.__objc_data: 0x5f00
   __DATA.__data: 0x3b40
   __DATA.__bss: 0x748

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9640
+  Functions: 9657
   Symbols:   1028
-  CStrings:  15814
+  CStrings:  15827
 
Symbols:
+ _AFIsInternalInstall
+ _AVAudioSessionModeSpeechRecognition
+ _CFAbsoluteTimeGetCurrent
+ _loadBookmark
+ _saveBookmark
- _OBJC_CLASS_$_AFMyriadGoodnessScoreOverrideState
- _OBJC_CLASS_$_NSCoder
- _OBJC_CLASS_$_NSKeyedArchiver
- _OBJC_CLASS_$_NSKeyedUnarchiver
- _OBJC_CLASS_$_SCDAGoodnessScoreOverrideState
CStrings:
+ "%s Detected 2nd-pass trigger at %{public}llu, KeywordDetectionBucket : %@, SpeakerDetectionBucket : %@"
+ "%s On-Device ASR: BGST: Done triggering replay record pruning"
+ "%s On-Device ASR: BGST: Triggering replay record pruning for event of age %f with timestamp %f"
+ "%s Rejected 2nd-pass KeywordDetectionBucket : %@, SpeakerDetectionBucket : %@"
+ "%s Unable to access app container group"
+ "%s didReceivePartialResultWithRequestId : %{public}@, %{public}@"
+ "%s xpcDisconnection:%u"
+ "-[CSIntuitiveConvRequestHandler _attendingExitAndDismissalWithXpcDisconnect:]"
+ "-[CSIntuitiveConvRequestHandler testDismissAttendingWithXPDisconnection:]_block_invoke"
+ "-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke_3"
+ "-[CSVoiceIdXPCClient _notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke_2"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke"
+ ".\x11"
+ "ASR"
+ "ContextualReplayRecord"
+ "Detected"
+ "NearMiss"
+ "Rejected"
+ "StrongAccept"
+ "StrongReject"
+ "Vv32@0:8@\"CCSerializedSetEnumerator\"16@?<v@?q>24"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSURL\">24"
+ "WeakAccept"
+ "WeakReject"
+ "_attendingExitAndDismissalWithXpcDisconnect:"
+ "_handleImplicitUtteranceMessage:client:"
+ "_notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
+ "_processSecondPassInExclave:rejectBlock:"
+ "_runReplayRecordPruning"
+ "_runReplayRecordPruning_block_invoke"
+ "_siriLanguageCode"
+ "appContainerName"
+ "beginEvaluationWithSetEnumerator:completion:"
+ "com.apple.siri.bg_system_task.replay-record-pruning"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "convertSecureVoiceTriggerKeywordDetectionResultTypeToString:"
+ "convertSecureVoiceTriggerSpeakerDetectionResultTypeToString:"
+ "fetchCurrentRequestId"
+ "fetchDismissedRequestId"
+ "getBestSupportedSiriLanguageWithFallback:"
+ "notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
+ "replay-record-pruning"
+ "setCategory:mode:options:error:"
+ "testDismissAttendingWithXPDisconnection:"
+ "v60@?0Q8d16I24Q28Q36Q44Q52"
+ "v68@?0Q8Q16d24I32Q36Q44Q52Q60"
- "%s Detected 2nd-pass trigger at %{public}llu"
- "%s Overriding Myriad state as request was made during a ringtone"
- "%s User Edit: cannot find bookmark from path %@, start enumeration from beginning"
- "%s User Edit: failed to deserialize bookmark, error: %@"
- "%s User Edit: failed to save bookmark on disk %@"
- "%s User Edit: failed to serialize bookmark, error: %@"
- "%s User Edit: invalid bookmark path %@, start enumeration from beginning"
- "%s User Edit: invalid file path for bookmark file %@"
- "%s User Edit: loaded bookmark from Biome %@"
- "%s User Edit: saved Biome bookmark on disk %@"
- "-[CSIntuitiveConvRequestHandler _attendingDismissalAndBlockHelper]"
- "-[CSVoiceIdXPCClient _notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]"
- "-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke"
- "-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke_2"
- "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]"
- "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke"
- "/Assistant/DictationUserEdit"
- "Trigger was during a ringtone"
- "Vv32@0:8@\"NSArray\"16@?<v@?q>24"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSURL\">24"
- "_attendingDismissalAndBlockHelper"
- "_notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
- "_processSecondPassInExclave:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "beginEvaluationWithSerializedSets:completion:"
- "bm_allowedClassesForSecureCodingBMBookmark"
- "bookmark"
- "exclave-built-in"
- "initWithOverrideOption:reason:"
- "loadBookmark"
- "saveBookmark"
- "setCategory:withOptions:error:"
- "setOverrideState:"
- "unarchivedObjectOfClasses:fromData:error:"
- "v44@?0Q8d16I24Q28Q36"
- "v52@?0Q8Q16d24I32Q36Q44"

```
