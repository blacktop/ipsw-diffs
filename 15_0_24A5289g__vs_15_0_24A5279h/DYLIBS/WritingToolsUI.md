## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/Versions/A/WritingToolsUI`

```diff

-38.0.0.0.0
-  __TEXT.__text: 0x1b074
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x14f8
-  __TEXT.__const: 0x4c4
-  __TEXT.__gcc_except_tab: 0x600
+34.0.0.0.0
+  __TEXT.__text: 0x1ad04
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x1600
+  __TEXT.__const: 0x4f4
+  __TEXT.__gcc_except_tab: 0x5f4
   __TEXT.__oslogstring: 0x3c4
-  __TEXT.__cstring: 0x10ce
+  __TEXT.__cstring: 0x107e
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0x6c
   __TEXT.__swift5_typeref: 0x22
-  __TEXT.__swift5_reflstr: 0xe4
-  __TEXT.__swift5_fieldmd: 0x98
+  __TEXT.__swift5_reflstr: 0xc4
+  __TEXT.__swift5_fieldmd: 0x8c
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x760
-  __TEXT.__objc_classname: 0x3bb
-  __TEXT.__objc_methname: 0x5894
-  __TEXT.__objc_methtype: 0x1740
-  __TEXT.__objc_stubs: 0x49a0
-  __DATA_CONST.__got: 0x388
+  __TEXT.__unwind_info: 0x768
+  __TEXT.__objc_classname: 0x3ba
+  __TEXT.__objc_methname: 0x575f
+  __TEXT.__objc_methtype: 0x1700
+  __TEXT.__objc_stubs: 0x48a0
+  __DATA_CONST.__got: 0x380
   __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14b8
+  __DATA_CONST.__objc_selrefs: 0x1480
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x430
+  __AUTH_CONST.__auth_got: 0x420
   __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__objc_const: 0x4138
+  __AUTH_CONST.__const: 0x790
+  __AUTH_CONST.__cfstring: 0x380
+  __AUTH_CONST.__objc_const: 0x41f8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x870
+  __AUTH.__objc_data: 0x820
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x1c8
+  __DATA.__objc_ivar: 0x1e4
   __DATA.__data: 0x628
   __DATA.__bss: 0x370
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 623
-  Symbols:   2041
-  CStrings:  130
+  Functions: 645
+  Symbols:   2053
+  CStrings:  126
 
Symbols:
+ -[_WTFinaleTextEffect chunk]
+ -[_WTFinaleTextEffect completion]
+ -[_WTFinaleTextEffect effectView]
+ -[_WTFinaleTextEffect hidesOriginal]
+ -[_WTFinaleTextEffect identifier]
+ -[_WTFinaleTextEffect initWithChunk:effectView:]
+ -[_WTFinaleTextEffect invalidate:]
+ -[_WTFinaleTextEffect rootLayer]
+ -[_WTFinaleTextEffect setChunk:]
+ -[_WTFinaleTextEffect setCompletion:]
+ -[_WTFinaleTextEffect setEffectView:]
+ -[_WTFinaleTextEffect setIdentifier:]
+ -[_WTFinaleTextEffect setRootLayer:]
+ -[_WTFinaleTextEffect setTimer:]
+ -[_WTFinaleTextEffect timer]
+ -[_WTFinaleTextEffect updateAnimationForTimeDelta:]
+ -[_WTReplaceDestinationTextEffect hidesOriginal]
+ -[_WTReplaceRemainderTextEffect hidesOriginal]
+ -[_WTReplaceRemainderTextEffect requestedDuration]
+ -[_WTReplaceRemainderTextEffect setRequestedDuration:]
+ -[_WTReplaceSourceTextEffect RBLayer:draw:]
+ -[_WTReplaceSourceTextEffect hidesOriginal]
+ -[_WTReplaceSourceTextEffect invalidate:]
+ -[_WTReplaceSourceTextEffect isDestination]
+ -[_WTReplaceSourceTextEffect setIsDestination:]
+ -[_WTReplaceSourceTextEffect update:]
+ -[_WTReplaceSourceTextEffect updateEffectWith:]
+ -[_WTReplaceTextEffect _applyToFill:colors:center:startRadius:endRadius:]
+ -[_WTReplaceTextEffect _applyToFill:locatedColors:center:startRadius:endRadius:]
+ -[_WTReplaceTextEffect _applyToFill:nonlocatedColors:center:startRadius:endRadius:]
+ -[_WTReplaceTextEffect chunk]
+ -[_WTReplaceTextEffect effectView]
+ -[_WTReplaceTextEffect firstPreviewRect]
+ -[_WTReplaceTextEffect identifier]
+ -[_WTReplaceTextEffect root]
+ -[_WTReplaceTextEffect setChunk:]
+ -[_WTReplaceTextEffect setEffectView:]
+ -[_WTReplaceTextEffect setFirstPreviewRect:]
+ -[_WTReplaceTextEffect setIdentifier:]
+ -[_WTReplaceTextEffect setRoot:]
+ -[_WTReplaceTextEffect setSnapshotPresentationFrames:]
+ -[_WTReplaceTextEffect setSweepDuration:]
+ -[_WTReplaceTextEffect setSweepVelocity:]
+ -[_WTReplaceTextEffect snapshotPresentationFrames]
+ -[_WTReplaceTextEffect sweepDuration]
+ -[_WTReplaceTextEffect sweepVelocity]
+ -[_WTReplaceTextEffect updateAnimationForTimeDelta:]
+ -[_WTSweepTextEffect _applyToFill:colors:center:startRadius:endRadius:]
+ -[_WTSweepTextEffect _applyToFill:locatedColors:center:startRadius:endRadius:]
+ -[_WTSweepTextEffect _applyToFill:nonlocatedColors:center:startRadius:endRadius:]
+ -[_WTSweepTextEffect chunk]
+ -[_WTSweepTextEffect completion]
+ -[_WTSweepTextEffect effectView]
+ -[_WTSweepTextEffect hidesOriginal]
+ -[_WTSweepTextEffect identifier]
+ -[_WTSweepTextEffect preCompletion]
+ -[_WTSweepTextEffect rootLayer]
+ -[_WTSweepTextEffect setChunk:]
+ -[_WTSweepTextEffect setCompletion:]
+ -[_WTSweepTextEffect setEffectView:]
+ -[_WTSweepTextEffect setIdentifier:]
+ -[_WTSweepTextEffect setPreCompletion:]
+ -[_WTSweepTextEffect setRootLayer:]
+ -[_WTSweepTextEffect updateAnimationForTimeDelta:]
+ GCC_except_table72
+ OBJC_IVAR_$__WTFinaleTextEffect._chunk
+ OBJC_IVAR_$__WTFinaleTextEffect._effectView
+ OBJC_IVAR_$__WTFinaleTextEffect._identifier
+ OBJC_IVAR_$__WTFinaleTextEffect._rootLayer
+ OBJC_IVAR_$__WTFinaleTextEffect._timer
+ OBJC_IVAR_$__WTFinaleTextEffect.completion
+ OBJC_IVAR_$__WTReplaceRemainderTextEffect._requestedDuration
+ OBJC_IVAR_$__WTReplaceSourceTextEffect._isDestination
+ OBJC_IVAR_$__WTReplaceTextEffect._chunk
+ OBJC_IVAR_$__WTReplaceTextEffect._effectView
+ OBJC_IVAR_$__WTReplaceTextEffect._firstPreviewRect
+ OBJC_IVAR_$__WTReplaceTextEffect._identifier
+ OBJC_IVAR_$__WTReplaceTextEffect._root
+ OBJC_IVAR_$__WTReplaceTextEffect._snapshotPresentationFrames
+ OBJC_IVAR_$__WTReplaceTextEffect._sweepDuration
+ OBJC_IVAR_$__WTReplaceTextEffect._sweepVelocity
+ OBJC_IVAR_$__WTSweepTextEffect._chunk
+ OBJC_IVAR_$__WTSweepTextEffect._effectView
+ OBJC_IVAR_$__WTSweepTextEffect._identifier
+ OBJC_IVAR_$__WTSweepTextEffect._rootLayer
+ OBJC_IVAR_$__WTSweepTextEffect.completion
+ OBJC_IVAR_$__WTSweepTextEffect.preCompletion
+ _MGGetBoolAnswer
+ _NSLog
+ __39-[_WTSweepTextEffect updateEffectWith:]_block_invoke.13
+ __40-[_WTFinaleTextEffect updateEffectWith:]_block_invoke.9
+ __43-[WTWritingToolsViewController viewDidLoad]_block_invoke.273
+ __83-[WTWritingToolsRemoteViewController willBeginWritingToolsSession:requestContexts:]_block_invoke.83
+ __94-[WTAffordanceUIController scheduleShowAffordanceForSelectionRect:ofView:forDelegate:onClick:]_block_invoke.39
+ __94-[WTAffordanceUIController scheduleShowAffordanceForSelectionRect:ofView:forDelegate:onClick:]_block_invoke.91
+ __94-[WTAffordanceUIController scheduleShowAffordanceForSelectionRect:ofView:forDelegate:onClick:]_block_invoke_2.40
+ __OBJC_$_INSTANCE_METHODS__WTReplaceSourceTextEffect
+ __OBJC_$_INSTANCE_VARIABLES__WTReplaceSourceTextEffect
+ __OBJC_$_PROP_LIST__WTReplaceSourceTextEffect
+ __OBJC_CLASS_PROTOCOLS_$__WTFinaleTextEffect
+ ___34-[_WTFinaleTextEffect invalidate:]_block_invoke
+ ___41-[_WTReplaceSourceTextEffect invalidate:]_block_invoke
+ ___47-[_WTReplaceSourceTextEffect updateEffectWith:]_block_invoke
+ __block_literal_global.110
+ __block_literal_global.120
+ __block_literal_global.153
+ __block_literal_global.275
+ __block_literal_global.280
+ _objc_msgSend$firstPreviewRect
+ _objc_msgSend$requestedDuration
+ _objc_msgSend$root
+ _objc_msgSend$setFirstPreviewRect:
+ _objc_msgSend$setRequestedDuration:
+ _objc_msgSend$setRoot:
+ _objc_msgSend$setSnapshotPresentationFrames:
+ _objc_msgSend$setSweepDuration:
+ _objc_msgSend$setSweepVelocity:
+ _objc_msgSend$snapshotPresentationFrames
+ _objc_msgSend$sweepVelocity
- -[WTWritingToolsRemoteViewController notifyServiceIsReady]
- -[WTWritingToolsRemoteViewController serviceIsReady]
- -[WTWritingToolsRemoteViewController setServiceIsReady:]
- -[_WTReplaceTextEffect RBLayer:draw:]
- -[_WTReplaceTextEffect highlightsCandidateRects]
- -[_WTReplaceTextEffect isDestination]
- -[_WTReplaceTextEffect nonCandidateTextContentMask]
- -[_WTReplaceTextEffect nonCandidateTextContent]
- -[_WTReplaceTextEffect setHighlightsCandidateRects:]
- -[_WTReplaceTextEffect setIsDestination:]
- -[_WTReplaceTextEffect setNonCandidateTextContent:]
- -[_WTReplaceTextEffect setNonCandidateTextContentMask:]
- -[_WTReplaceTextEffect update:]
- -[_WTTextEffect .cxx_destruct]
- -[_WTTextEffect _applyToFill:colors:center:startRadius:endRadius:]
- -[_WTTextEffect _applyToFill:locatedColors:center:startRadius:endRadius:]
- -[_WTTextEffect _applyToFill:nonlocatedColors:center:startRadius:endRadius:]
- -[_WTTextEffect chunk]
- -[_WTTextEffect completion]
- -[_WTTextEffect effectView]
- -[_WTTextEffect effectVisibilityFrame]
- -[_WTTextEffect hidesOriginal]
- -[_WTTextEffect identifier]
- -[_WTTextEffect initWithChunk:effectView:]
- -[_WTTextEffect invalidate:]
- -[_WTTextEffect invalidationAnimationDuration]
- -[_WTTextEffect needsSetup]
- -[_WTTextEffect preCompletion]
- -[_WTTextEffect rootLayer]
- -[_WTTextEffect setChunk:]
- -[_WTTextEffect setCompletion:]
- -[_WTTextEffect setEffectView:]
- -[_WTTextEffect setHidesOriginal:]
- -[_WTTextEffect setIdentifier:]
- -[_WTTextEffect setPreCompletion:]
- -[_WTTextEffect setRootLayer:]
- -[_WTTextEffect setTimer:]
- -[_WTTextEffect sweepDuration]
- -[_WTTextEffect sweepRadius]
- -[_WTTextEffect timer]
- -[_WTTextEffect updateEffectWith:]
- GCC_except_table36
- GCC_except_table75
- OBJC_IVAR_$_WTWritingToolsRemoteViewController._serviceIsReady
- OBJC_IVAR_$__WTReplaceTextEffect._highlightsCandidateRects
- OBJC_IVAR_$__WTReplaceTextEffect._isDestination
- OBJC_IVAR_$__WTReplaceTextEffect._nonCandidateTextContent
- OBJC_IVAR_$__WTReplaceTextEffect._nonCandidateTextContentMask
- OBJC_IVAR_$__WTTextEffect._chunk
- OBJC_IVAR_$__WTTextEffect._completion
- OBJC_IVAR_$__WTTextEffect._effectPresentationRect
- OBJC_IVAR_$__WTTextEffect._effectView
- OBJC_IVAR_$__WTTextEffect._firstSnapshotRect
- OBJC_IVAR_$__WTTextEffect._hidesOriginal
- OBJC_IVAR_$__WTTextEffect._identifier
- OBJC_IVAR_$__WTTextEffect._preCompletion
- OBJC_IVAR_$__WTTextEffect._rootLayer
- OBJC_IVAR_$__WTTextEffect._timer
- _CFPreferencesAppValueIsForced
- _CFPreferencesGetAppBooleanValue
- _NSEqualSizes
- _NSIsEmptyRect
- _OBJC_$_PROP_LIST__WTTextEffect.132
- _OBJC_CLASS_$__WTTextEffect
- _OBJC_METACLASS_$__WTTextEffect
- __130+[WTAffordanceUIController numberOfSelectedLinesOfTextIsAtLeast:client:selectedRange:rectOriginYPrev:exitAfter:completionHandler:]_block_invoke.121
- __39-[_WTSweepTextEffect updateEffectWith:]_block_invoke.15
- __40-[_WTFinaleTextEffect updateEffectWith:]_block_invoke.5
- __41-[_WTReplaceTextEffect updateEffectWith:]_block_invoke.19
- __43-[WTWritingToolsViewController viewDidLoad]_block_invoke.281
- __83-[WTWritingToolsRemoteViewController willBeginWritingToolsSession:requestContexts:]_block_invoke.86
- __94-[WTAffordanceUIController scheduleShowAffordanceForSelectionRect:ofView:forDelegate:onClick:]_block_invoke.41
- __94-[WTAffordanceUIController scheduleShowAffordanceForSelectionRect:ofView:forDelegate:onClick:]_block_invoke.93
- __94-[WTAffordanceUIController scheduleShowAffordanceForSelectionRect:ofView:forDelegate:onClick:]_block_invoke_2.42
- __OBJC_$_INSTANCE_METHODS__WTTextEffect
- __OBJC_$_INSTANCE_VARIABLES__WTTextEffect
- __OBJC_CLASS_PROTOCOLS_$__WTTextEffect
- __OBJC_CLASS_RO_$__WTTextEffect
- __OBJC_METACLASS_RO_$__WTTextEffect
- ___28-[_WTTextEffect invalidate:]_block_invoke
- ___41-[_WTReplaceTextEffect updateEffectWith:]_block_invoke
- ___block_descriptor_40_e8_32bs_e54_v56?0{CGRect={CGPoint=dd}{CGSize=dd}}8{_NSRange=QQ}40l
- ___block_descriptor_40_e8_32s_e31_v32?0"_WTTextPreview"8Q16^B24l
- ___block_descriptor_41_e8_32s_e5_v8?0l
- __block_literal_global.112
- __block_literal_global.125
- __block_literal_global.156
- __block_literal_global.283
- __block_literal_global.288
- _objc_msgSend$candidateRects
- _objc_msgSend$convertRect:fromLayer:
- _objc_msgSend$effectVisibilityFrame
- _objc_msgSend$firstRectForCharacterRange:completionHandler:
- _objc_msgSend$highlightsCandidateRects
- _objc_msgSend$invalidationAnimationDuration
- _objc_msgSend$needsSetup
- _objc_msgSend$nonCandidateTextContent
- _objc_msgSend$nonCandidateTextContentMask
- _objc_msgSend$selectionAnchorRect
- _objc_msgSend$serviceIsReady
- _objc_msgSend$setCompositingFilter:
- _objc_msgSend$setHidesOriginal:
- _objc_msgSend$setHighlightsCandidateRects:
- _objc_msgSend$setNonCandidateTextContent:
- _objc_msgSend$setNonCandidateTextContentMask:
- _objc_msgSend$setServiceIsReady:
- _objc_msgSend$setToolTip:
- _objc_msgSend$sweepRadius
CStrings:
+ "DeviceSupportsGenerativeModelSystems"
+ "implement in a subclass"
- ".GlobalPreferences"
- "AlternateQuestionnaire_iPadOS"
- "Keep original"
- "allowWritingTools"
- "v32@?0@\"_WTTextPreview\"8Q16^B24"
- "xor"

```
