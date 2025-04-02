## SiriUI

> `/System/Library/PrivateFrameworks/SiriUI.framework/Versions/A/SiriUI`

```diff

-3404.72.1.14.4
-  __TEXT.__text: 0xe6734
+3405.19.1.0.0
+  __TEXT.__text: 0xe6a5c
   __TEXT.__auth_stubs: 0x20a0
-  __TEXT.__objc_methlist: 0x11aa4
+  __TEXT.__objc_methlist: 0x11b14
   __TEXT.__const: 0x1ee4
-  __TEXT.__cstring: 0xe50b
-  __TEXT.__gcc_except_tab: 0x14c0
-  __TEXT.__oslogstring: 0x65e2
+  __TEXT.__cstring: 0xe53b
+  __TEXT.__gcc_except_tab: 0x1514
+  __TEXT.__oslogstring: 0x66ec
   __TEXT.__ustring: 0x2a
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__swift5_typeref: 0x1684

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x4178
+  __TEXT.__unwind_info: 0x4180
   __TEXT.__eh_frame: 0x58c
   __TEXT.__objc_classname: 0x20c4
-  __TEXT.__objc_methname: 0x2cb41
-  __TEXT.__objc_methtype: 0xa12d
-  __TEXT.__objc_stubs: 0x1d480
+  __TEXT.__objc_methname: 0x2cc09
+  __TEXT.__objc_methtype: 0xa13b
+  __TEXT.__objc_stubs: 0x1d4e0
   __DATA_CONST.__got: 0x1678
   __DATA_CONST.__const: 0x7d0
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x180
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa3a0
+  __DATA_CONST.__objc_selrefs: 0xa3d0
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x1b8
   __AUTH_CONST.__auth_got: 0x1060
   __AUTH_CONST.__auth_ptr: 0x5c0
-  __AUTH_CONST.__const: 0x33e0
+  __AUTH_CONST.__const: 0x33f0
   __AUTH_CONST.__cfstring: 0x5ee0
-  __AUTH_CONST.__objc_const: 0x281c0
+  __AUTH_CONST.__objc_const: 0x28268
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x4838
   __AUTH.__data: 0x908
-  __DATA.__objc_ivar: 0xeec
+  __DATA.__objc_ivar: 0xef0
   __DATA.__data: 0x3560
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x1d68

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6436
-  Symbols:   14271
-  CStrings:  10128
+  Functions: 6441
+  Symbols:   14281
+  CStrings:  10140
 
Symbols:
+ -[AFUISiriSession prewarmForPossibleTextRequest]
+ -[SVSSiriView isFlipped]
+ -[SiriUISystemAssistantExperiencePresentation didPunchOut]
+ -[SiriUISystemAssistantExperienceViewController latencyPillSize]
+ -[SiriUISystemAssistantExperienceViewController setLatencyPillSize:]
+ GCC_except_table119
+ GCC_except_table157
+ GCC_except_table162
+ GCC_except_table190
+ GCC_except_table328
+ GCC_except_table88
+ OBJC_IVAR_$_SiriUISystemAssistantExperienceViewController._latencyPillSize
+ __112-[SiriUISystemAssistantExperienceViewController dropletContentWillUpdateLayout:withUpdatedContentSize:animated:]_block_invoke.59
+ __112-[SiriUISystemAssistantExperienceViewController dropletContentWillUpdateLayout:withUpdatedContentSize:animated:]_block_invoke.64
+ __113-[SiriUISystemAssistantExperienceViewController _setUpConversationContinuerSuggestions:forRequestId:currentMode:]_block_invoke.34
+ __116-[SiriUISystemAssistantExperienceViewController _transitionSuggestionsWithExpansion:animated:withCompletionHandler:]_block_invoke.115
+ __199-[SVSSiriViewController _speakText:audioData:ignoreMuteSwitch:identifier:sessionId:provisionally:eligibleAfterDuration:canUseServerTTS:speakableUtteranceParser:preparation:completion:animationBlock:]_block_invoke.154
+ __43-[SiriUISiriStatusView fadeTextAndMoveDown]_block_invoke.76
+ __48-[SVSSiriViewController initWithNibName:bundle:]_block_invoke.44
+ __48-[SVSSiriViewController initWithNibName:bundle:]_block_invoke.44.cold.1
+ __55-[AFUISiriSession assistantConnectionRequestWillStart:]_block_invoke.79
+ __56-[AFUISiriSession _handlePhotoPickerRequest:completion:]_block_invoke.137
+ __56-[AFUISiriSession _handlePhotoPickerRequest:completion:]_block_invoke.137.cold.1
+ __56-[AFUISiriSession _startRequestWithText:turnIdentifier:]_block_invoke.150
+ __62-[SVSSiriViewController siriSessionDidReceiveRepeatItCommand:]_block_invoke.345
+ __71-[SiriUISystemAssistantExperienceViewController siriViewDidChangeText:]_block_invoke.120
+ __71-[SiriUISystemAssistantExperienceViewController siriViewDidChangeText:]_block_invoke_2.121
+ __73-[SiriUISystemAssistantExperienceViewController _performResultAnimation:]_block_invoke.74
+ __81-[SiriUISystemAssistantExperienceViewController performSinglePillExpandAnimation]_block_invoke.90
+ __81-[SiriUISystemAssistantExperienceViewController performSinglePillExpandAnimation]_block_invoke.93
+ __88-[SiriUISystemAssistantExperienceViewController setupConversationStarterSuggestionViews]_block_invoke.132
+ __90-[SVSSiriViewController _performAppPunchOutCommand:conversationItemIdentifier:completion:]_block_invoke.454
+ __90-[SVSSiriViewController _performAppPunchOutCommand:conversationItemIdentifier:completion:]_block_invoke_2.455
+ __OBJC_$_INSTANCE_METHODS_SVSSiriView
+ ___block_descriptor_56_e8_32w_e5_v8?0l
+ __block_literal_global.102
+ __block_literal_global.114
+ __block_literal_global.116
+ __block_literal_global.127
+ __block_literal_global.128
+ __block_literal_global.129
+ __block_literal_global.134
+ __block_literal_global.143
+ __block_literal_global.154
+ __block_literal_global.161
+ __block_literal_global.162
+ __block_literal_global.168
+ __block_literal_global.177
+ __block_literal_global.453
+ __block_literal_global.52
+ __block_literal_global.58
+ __block_literal_global.66
+ __block_literal_global.73
+ __block_literal_global.77
+ __block_literal_global.81
+ __block_literal_global.90
+ _objc_msgSend$didPunchOut
+ _objc_msgSend$notifySessionThatTypingStarted
+ _objc_msgSend$prewarmForPossibleTextRequest
- GCC_except_table156
- GCC_except_table161
- GCC_except_table327
- __112-[SiriUISystemAssistantExperienceViewController dropletContentWillUpdateLayout:withUpdatedContentSize:animated:]_block_invoke.56
- __112-[SiriUISystemAssistantExperienceViewController dropletContentWillUpdateLayout:withUpdatedContentSize:animated:]_block_invoke.58
- __113-[SiriUISystemAssistantExperienceViewController _setUpConversationContinuerSuggestions:forRequestId:currentMode:]_block_invoke.31
- __116-[SiriUISystemAssistantExperienceViewController _transitionSuggestionsWithExpansion:animated:withCompletionHandler:]_block_invoke.111
- __199-[SVSSiriViewController _speakText:audioData:ignoreMuteSwitch:identifier:sessionId:provisionally:eligibleAfterDuration:canUseServerTTS:speakableUtteranceParser:preparation:completion:animationBlock:]_block_invoke.150
- __43-[SiriUISiriStatusView fadeTextAndMoveDown]_block_invoke.77
- __48-[SVSSiriViewController initWithNibName:bundle:]_block_invoke.40
- __48-[SVSSiriViewController initWithNibName:bundle:]_block_invoke.40.cold.1
- __55-[AFUISiriSession assistantConnectionRequestWillStart:]_block_invoke.76
- __56-[AFUISiriSession _handlePhotoPickerRequest:completion:]_block_invoke.134
- __56-[AFUISiriSession _handlePhotoPickerRequest:completion:]_block_invoke.134.cold.1
- __56-[AFUISiriSession _startRequestWithText:turnIdentifier:]_block_invoke.147
- __62-[SVSSiriViewController siriSessionDidReceiveRepeatItCommand:]_block_invoke.341
- __71-[SiriUISystemAssistantExperienceViewController siriViewDidChangeText:]_block_invoke.116
- __71-[SiriUISystemAssistantExperienceViewController siriViewDidChangeText:]_block_invoke_2.117
- __73-[SiriUISystemAssistantExperienceViewController _performResultAnimation:]_block_invoke.71
- __81-[SiriUISystemAssistantExperienceViewController performSinglePillExpandAnimation]_block_invoke.89
- __88-[SiriUISystemAssistantExperienceViewController setupConversationStarterSuggestionViews]_block_invoke.128
- __90-[SVSSiriViewController _performAppPunchOutCommand:conversationItemIdentifier:completion:]_block_invoke.448
- __90-[SVSSiriViewController _performAppPunchOutCommand:conversationItemIdentifier:completion:]_block_invoke_2.449
- ___81-[SiriUISystemAssistantExperienceViewController performSinglePillExpandAnimation]_block_invoke_4
- __block_literal_global.111
- __block_literal_global.113
- __block_literal_global.123
- __block_literal_global.125
- __block_literal_global.130
- __block_literal_global.139
- __block_literal_global.150
- __block_literal_global.158
- __block_literal_global.165
- __block_literal_global.174
- __block_literal_global.447
- __block_literal_global.49
- __block_literal_global.55
- __block_literal_global.63
- __block_literal_global.69
- __block_literal_global.74
- __block_literal_global.78
- __block_literal_global.80
- __block_literal_global.87
- __block_literal_global.96
CStrings:
+ "%s Skipping didReceiveTextInput because Siri is still animating current result"
+ "%s Skipping siriViewDidReceiveStatusViewTextUpdateAction because Siri is still animating current result"
+ "%s Skipping startRequestWithOptions because Siri is still animating current result"
+ "-[AFUISiriViewController siriView:didReceiveTextInput:]"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AssistantUIX/SiriUI/AppKit+SiriUIAdditions.m"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AssistantUIX/SiriUI/SiriUISetup.m"
+ "T{CGSize=dd},N,V_latencyPillSize"
+ "_latencyPillSize"
+ "didPunchOut"
+ "latencyPillSize"
+ "notifySessionThatTypingStarted"
+ "prewarmForPossibleTextRequest"
+ "setLatencyPillSize:"
+ "speechSynthesisDidFinish:withIdentifier:"
+ "v32@0:8@\"AFSpeechSynthesisRecord\"16@\"NSString\"24"
- "/AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AssistantUIX/SiriUI/AppKit+SiriUIAdditions.m"
- "/AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AssistantUIX/SiriUI/SiriUISetup.m"
- "v24@0:8@\"SRUIFSpeechSynthesizer\"16"

```
