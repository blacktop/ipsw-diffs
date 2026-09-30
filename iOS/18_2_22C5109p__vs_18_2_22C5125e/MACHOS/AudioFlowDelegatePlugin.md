## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin`

```diff

-3402.51.1.1.2
-  __TEXT.__text: 0x288c48
-  __TEXT.__auth_stubs: 0x6c80
+3402.60.1.1.1
+  __TEXT.__text: 0x289e18
+  __TEXT.__auth_stubs: 0x6cd0
   __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0x82d2
+  __TEXT.__const: 0x8302
   __TEXT.__cstring: 0x7b8c
-  __TEXT.__swift5_typeref: 0x3fec
-  __TEXT.__oslogstring: 0x22e77
-  __TEXT.__constg_swiftt: 0x5428
+  __TEXT.__swift5_typeref: 0x4038
+  __TEXT.__oslogstring: 0x233d7
+  __TEXT.__constg_swiftt: 0x5458
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x3d1b
+  __TEXT.__swift5_reflstr: 0x3d6b
   __TEXT.__swift5_assocty: 0xa28
   __TEXT.__swift5_proto: 0x454
-  __TEXT.__swift5_types: 0x30c
+  __TEXT.__swift5_types: 0x310
   __TEXT.__objc_classname: 0xce
   __TEXT.__objc_methname: 0x2a1a
   __TEXT.__objc_methtype: 0x3ef
-  __TEXT.__swift5_fieldmd: 0x2ea0
-  __TEXT.__swift5_capture: 0x3954
+  __TEXT.__swift5_fieldmd: 0x2ed4
+  __TEXT.__swift5_capture: 0x382c
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3778
-  __TEXT.__eh_frame: 0x3444
-  __DATA_CONST.__auth_got: 0x3640
-  __DATA_CONST.__got: 0x1d60
-  __DATA_CONST.__auth_ptr: 0x1f90
-  __DATA_CONST.__const: 0xa7e8
+  __TEXT.__unwind_info: 0x3748
+  __TEXT.__eh_frame: 0x33c4
+  __DATA_CONST.__auth_got: 0x3668
+  __DATA_CONST.__got: 0x1d78
+  __DATA_CONST.__auth_ptr: 0x1f20
+  __DATA_CONST.__const: 0xa630
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0xa818
   __DATA.__objc_selrefs: 0xce8
   __DATA.__objc_data: 0x12f8
-  __DATA.__data: 0xb7f8
+  __DATA.__data: 0xb868
   __DATA.__bss: 0x7a10
   __DATA.__common: 0x488
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/Frameworks/ShazamKit.framework/ShazamKit
+  - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5209
-  Symbols:   372
-  CStrings:  2969
+  Functions: 5196
+  Symbols:   373
+  CStrings:  2979
 
Symbols:
+ _OBJC_CLASS_$_INPlayMediaMediaItemResolutionResult
CStrings:
+ "AddMedia+HandleIntentStrategy#handleFailure with error: %!s(MISSING) %!{(MISSING)public}s"
+ "AddMedia+HandleIntentStrategy#makeIntentHandledResponseUsingDialogProvider for app: %!s(MISSING)"
+ "PlayMedia+HandleIntentStategy#handledIntentOutputWithRF completed successfully. Insights:%!{(MISSING)public}s"
+ "PlayMedia+HandleIntentStategy#handledIntentOutputWithRF created output: %!s(MISSING). Insights:%!{(MISSING)public}s"
+ "PlayMedia+HandleIntentStategy#handledIntentOutputWithRF failed with error: %!{(MISSING)public}s, Insights:%!{(MISSING)public}s"
+ "PlayMedia+HandleIntentStategy#handledIntentOutputWithRF response is being handled using Response Framework2.0. for app: %!s(MISSING) Insights:%!{(MISSING)public}s"
+ "PlayMediaRCHFlowWrapper#dialogForError unhandled PFSQ terminal error, will continue to process the error"
+ "PlayMediaRCHFlowWrapper#sharedErrorDialogHandlingForPFSQTerminalErrors code: %!{(MISSING)public}s"
+ "PlayMediaRCHFlowWrapper#sharedErrorDialogHandlingForPFSQTerminalErrors should NOT be here, PFSQ terminal errors and tracking have gotten out of sync, this needs to be fixed! The unhandled playbackCode: %!{(MISSING)public}s"
+ "PlayMediaRCHFlowWrapper#sharedErrorDialogHandlingForPFSQTerminalErrors using special dialog (musicCellularDataOff) for unsupportMediaItemsCellularDataSettings code"
+ "PlayMediaRCHFlowWrapper#sharedErrorDialogHandlingForPFSQTerminalErrors using special dialog for appNotInstalled code"
+ "PlayMediaRCHFlowWrapper#sharedErrorDialogHandlingForPFSQTerminalErrors using special dialog for gdprNeededInGroup code"
+ "PlayMediaRCHFlowWrapper#sharedErrorDialogHandlingForPFSQTerminalErrors using special dialog for homepod account error code"
+ "PlayMediaRCHFlowWrapper#sharedErrorDialogHandlingForPFSQTerminalErrors using special dialog for noNetwork code"
+ "PlayMediaRCHFlowWrapper#sharedErrorDialogHandlingForPFSQTerminalErrors using special dialog for operationApplicationRequiresPreflight code"
+ "PlayMediaRCHFlowWrapper#sharedErrorDialogHandlingForPFSQTerminalErrors using special dialog for signIntoMusicAccount error code"
+ "PlayMediaRCHFlowWrapper#sharedErrorDialogHandlingForPFSQTerminalErrors using special dialog for unsupportMediaItemsCellularDataSettings code"
+ "PlayeMediaDialogProvider#chooseUnsupportedReason intentResolutionResult type not being handled (yet) today: %!s(MISSING)"
+ "PlayeMediaDialogProvider#chooseUnsupportedReason result is not PFSQ terminating..."
+ "PlayeMediaDialogProvider#chooseUnsupportedReason unhandled PFSQ terminal error, will fall back to unsupported media items"
+ "ResponseFactory+Utilities#makeResponseOutput error: %!s(MISSING)"
+ "ResponseFactory+Utilities#makeResponseOutput..."
+ "ResponseFactory+Utilities#responseOutput creating an empty response"
+ "ResponseFactory+Utilities#responseOutput creating response with a dialog and a snippet on the conversation space"
+ "ResponseFactory+Utilities#responseOutput creating response with a dialog and a snippet on the result space"
+ "ResponseFactory+Utilities#responseOutput creating response with a dialog and no snippets"
+ "ResponseFactory+Utilities#responseOutput creating response with a snippet on the conversation space and no dialog."
+ "ResponseFactory+Utilities#responseOutput creating response with a snippet on the result space and no dialog"
+ "ResponseFactory+Utilities#responseOutput creating response with dialog and snippets on the result and conversation space"
+ "ResponseFactory+Utilities#responseOutput..."
+ "UpdateMediaAffinity+HandleIntentStrategy#makeIntentHandledResponse returning completionViewOutput with a dialog."
- "HandleIntentStrategy#handleFailure with error: %!s(MISSING) %!{(MISSING)public}s"
- "HandleIntentStrategy#handledIntentOutputWithRF completed successfully. Insights:%!{(MISSING)public}s"
- "HandleIntentStrategy#handledIntentOutputWithRF created output: %!s(MISSING). Insights:%!{(MISSING)public}s"
- "HandleIntentStrategy#handledIntentOutputWithRF failed with error: %!{(MISSING)public}s, Insights:%!{(MISSING)public}s"
- "HandleIntentStrategy#handledIntentOutputWithRF response is being handled using Response Framework2.0. for app: %!s(MISSING) Insights:%!{(MISSING)public}s"
- "HandleIntentStrategy#makeIntentHandledResponse returning a completionViewOutput"
- "HandleIntentStrategy#makeIntentHandledResponseUsingDialogProvider for app: %!s(MISSING)"
- "PlayMediaRCHFlowWrapper#dialogForError using special dialog (musicCellularDataOff) for unsupportMediaItemsCellularDataSettings code"
- "PlayMediaRCHFlowWrapper#dialogForError using special dialog for gdprNeededInGroup code"
- "PlayMediaRCHFlowWrapper#dialogForError using special dialog for homepod account error code"
- "PlayMediaRCHFlowWrapper#dialogForError using special dialog for noNetwork code"
- "PlayMediaRCHFlowWrapper#dialogForError using special dialog for operationApplicationRequiresPreflight code"
- "PlayMediaRCHFlowWrapper#dialogForError using special dialog for signIntoMusicAccount error code"
- "PlayMediaRCHFlowWrapper#dialogForError using special dialog for unsupportMediaItemsCellularDataSettings code"
- "ResponseFactory+Utilities#makeResponseOutput creating an empty response"
- "ResponseFactory+Utilities#makeResponseOutput creating response with a dialog and a snippet on the conversation space"
- "ResponseFactory+Utilities#makeResponseOutput creating response with a dialog and a snippet on the result space"
- "ResponseFactory+Utilities#makeResponseOutput creating response with a dialog and no snippets"
- "ResponseFactory+Utilities#makeResponseOutput creating response with a snippet on the conversation space and no dialog."
- "ResponseFactory+Utilities#makeResponseOutput creating response with a snippet on the result space and no dialog"
- "ResponseFactory+Utilities#makeResponseOutput creating response with dialog and snippets on the result and conversation space"

```
