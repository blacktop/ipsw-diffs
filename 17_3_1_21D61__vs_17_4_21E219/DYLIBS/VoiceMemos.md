## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1140.0.0.0.0
-  __TEXT.__text: 0x42f08
+1158.0.0.0.0
+  __TEXT.__text: 0x430e8
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_methlist: 0x330c
+  __TEXT.__objc_methlist: 0x333c
   __TEXT.__gcc_except_tab: 0x1704
   __TEXT.__const: 0x178
-  __TEXT.__cstring: 0x5ce7
+  __TEXT.__cstring: 0x5cc6
   __TEXT.__oslogstring: 0x26ec
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x17b0
+  __TEXT.__unwind_info: 0x17c0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x7bf
-  __TEXT.__objc_methname: 0xac50
-  __TEXT.__objc_methtype: 0x1578
-  __TEXT.__objc_stubs: 0x7de0
+  __TEXT.__objc_methname: 0xacd2
+  __TEXT.__objc_methtype: 0x156a
+  __TEXT.__objc_stubs: 0x7e40
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0x1c00
   __DATA_CONST.__objc_classlist: 0x198

   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4f70
-  __DATA_CONST.__objc_selrefs: 0x2848
+  __DATA_CONST.__objc_selrefs: 0x2868
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x3b8
+  __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x100
   __AUTH_CONST.__objc_const: 0x1710
-  __AUTH_CONST.__cfstring: 0x2ea0
+  __AUTH_CONST.__cfstring: 0x2e60
   __AUTH_CONST.__const: 0x680
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_dictobj: 0x118

   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__auth_got: 0x600
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x3b8
-  __DATA.__objc_superrefs: 0x128
   __DATA.__objc_ivar: 0x2a4
   __DATA.__data: 0x8b8
-  __DATA.__bss: 0x130
+  __DATA.__bss: 0x128
   __DATA_DIRTY.__objc_data: 0x690
-  __DATA_DIRTY.__bss: 0x118
+  __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1725
-  Symbols:   5981
-  CStrings:  2772
+  Functions: 1729
+  Symbols:   5992
+  CStrings:  2775
 
Symbols:
+ -[RCCloudRecording _audioFutureIsCurrent]
+ -[RCCloudRecording _composedURLIsCloneOfAudioFuture]
+ -[RCCloudRecording _localAssetIsReachable]
+ -[RCCloudRecording audioFutureIsDownloaded]
+ -[RCSavedRecordingsModel transactionsAndChangesForObjectID:]
+ GCC_except_table61
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke.197
+ ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke_2.198
+ ___114-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]_block_invoke.203
+ ___130-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]_block_invoke.208
+ ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke.193
+ ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke_2.194
+ ___40-[RCSSavedRecordingService serviceProxy]_block_invoke.188
+ ___49-[RCSSavedRecordingService openServiceConnection]_block_invoke.109
+ ___51-[RCSSavedRecordingService __fetchAllAccessTokens:]_block_invoke.165
+ ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke.179
+ ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke_2.181
+ ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingExported:]_block_invoke.161
+ ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingModified:]_block_invoke.163
+ ___64-[RCSSavedRecordingService prepareToTrimCompositionAVURL:error:]_block_invoke.155
+ ___66-[RCSSavedRecordingService openAudioFile:settings:metadata:error:]_block_invoke.139
+ ___67-[RCSSavedRecordingService prepareToPreviewCompositionAVURL:error:]_block_invoke.145
+ ___69-[RCSSavedRecordingService prepareToCaptureToCompositionAVURL:error:]_block_invoke.133
+ ___80-[RCSSavedRecordingService prepareToExportCompositionAVURL:cacheWaveform:error:]_block_invoke.150
+ ___block_literal_global.111
+ ___block_literal_global.116
+ ___block_literal_global.120
+ ___block_literal_global.124
+ ___block_literal_global.127
+ ___block_literal_global.149
+ ___block_literal_global.158
+ ___block_literal_global.160
+ ___block_literal_global.162
+ ___block_literal_global.169
+ ___block_literal_global.180
+ ___block_literal_global.183
+ ___block_literal_global.185
+ ___block_literal_global.187
+ ___block_literal_global.193
+ ___block_literal_global.232
+ ___block_literal_global.241
+ ___block_literal_global.299
+ ___block_literal_global.311
+ _objc_msgSend$_audioFutureIsCurrent
+ _objc_msgSend$_composedURLIsCloneOfAudioFuture
+ _objc_msgSend$_localAssetIsReachable
- -[RCSavedRecordingsModel transactionsAndChangesForObjectID:changeType:]
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke.196
- ___100-[RCSSavedRecordingService _sendServiceMessage:withBasicReplyBlock:withServiceProxy:messagingBlock:]_block_invoke_2.197
- ___114-[RCSavedRecordingsModel _importRecordingWithSourceAudioURL:name:date:uniqueID:preferredFormat:completionHandler:]_block_invoke.201
- ___130-[RCSavedRecordingsModel _importImportableRecordingWithAudioAsset:name:date:uniqueID:presetName:outputFileType:completionHandler:]_block_invoke.206
- ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke.192
- ___132-[RCSSavedRecordingService _sendServiceMessage:connectionFailureReplyInfo:infoAndErrorReplyHandler:withServiceProxy:messagingBlock:]_block_invoke_2.193
- ___40-[RCSSavedRecordingService serviceProxy]_block_invoke.187
- ___49-[RCSSavedRecordingService openServiceConnection]_block_invoke.108
- ___51-[RCSSavedRecordingService __fetchAllAccessTokens:]_block_invoke.164
- ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke.178
- ___56-[RCSSavedRecordingService observeFinalizingRecordings:]_block_invoke_2.180
- ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingExported:]_block_invoke.160
- ___64-[RCSSavedRecordingService fetchCompositionAVURLsBeingModified:]_block_invoke.162
- ___64-[RCSSavedRecordingService prepareToTrimCompositionAVURL:error:]_block_invoke.154
- ___66-[RCSSavedRecordingService openAudioFile:settings:metadata:error:]_block_invoke.138
- ___67-[RCSSavedRecordingService prepareToPreviewCompositionAVURL:error:]_block_invoke.144
- ___69-[RCSSavedRecordingService prepareToCaptureToCompositionAVURL:error:]_block_invoke.132
- ___80-[RCSSavedRecordingService prepareToExportCompositionAVURL:cacheWaveform:error:]_block_invoke.149
- ___block_literal_global.110
- ___block_literal_global.115
- ___block_literal_global.119
- ___block_literal_global.123
- ___block_literal_global.126
- ___block_literal_global.148
- ___block_literal_global.156
- ___block_literal_global.159
- ___block_literal_global.161
- ___block_literal_global.168
- ___block_literal_global.179
- ___block_literal_global.182
- ___block_literal_global.184
- ___block_literal_global.186
- ___block_literal_global.192
- ___block_literal_global.226
- ___block_literal_global.239
- ___block_literal_global.298
- ___block_literal_global.310
CStrings:
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "_audioFutureIsCurrent"
+ "_composedURLIsCloneOfAudioFuture"
+ "_localAssetIsReachable"
+ "audioFutureIsDownloaded"
+ "transactionsAndChangesForObjectID:"
- "%K == %@ && %K == %ld"
- "@32@0:8@16q24"
- "transactionsAndChangesForObjectID:changeType:"

```
