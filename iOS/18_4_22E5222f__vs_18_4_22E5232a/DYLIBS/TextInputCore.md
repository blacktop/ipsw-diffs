## TextInputCore

> `/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore`

```diff

-3479.318.0.0.0
-  __TEXT.__text: 0x2282c0
+3479.319.102.0.0
+  __TEXT.__text: 0x228844
   __TEXT.__auth_stubs: 0x36e0
   __TEXT.__init_offsets: 0xbc
-  __TEXT.__objc_methlist: 0x10548
+  __TEXT.__objc_methlist: 0x105d0
   __TEXT.__dlopen_cstrs: 0x7d7
   __TEXT.__const: 0x2341
-  __TEXT.__cstring: 0x1988e
+  __TEXT.__cstring: 0x199ad
   __TEXT.__oslogstring: 0x4156
   __TEXT.__ustring: 0x3ca
   __TEXT.__unwind_info: 0x6bc0
-  __TEXT.__objc_classname: 0x2233
-  __TEXT.__objc_methname: 0x30119
-  __TEXT.__objc_methtype: 0x708b
-  __TEXT.__objc_stubs: 0x21400
-  __DATA_CONST.__got: 0x1c20
+  __TEXT.__objc_classname: 0x224d
+  __TEXT.__objc_methname: 0x302f2
+  __TEXT.__objc_methtype: 0x7082
+  __TEXT.__objc_stubs: 0x21520
+  __DATA_CONST.__got: 0x1c28
   __DATA_CONST.__const: 0x52b8
-  __DATA_CONST.__objc_classlist: 0x838
+  __DATA_CONST.__objc_classlist: 0x840
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c00
+  __DATA_CONST.__objc_selrefs: 0x9c48
   __DATA_CONST.__objc_superrefs: 0x708
   __DATA_CONST.__objc_arraydata: 0x9c8
   __AUTH_CONST.__auth_got: 0x1b78
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x8980
-  __AUTH_CONST.__cfstring: 0x11c00
-  __AUTH_CONST.__objc_const: 0x1a0d0
+  __AUTH_CONST.__cfstring: 0x11c60
+  __AUTH_CONST.__objc_const: 0x1a280
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH.__objc_data: 0x2170
+  __AUTH.__objc_data: 0x21c0
   __AUTH.__data: 0x18
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0x1270
+  __DATA.__objc_ivar: 0x1288
   __DATA.__data: 0x34a0
   __DATA.__bss: 0x940
   __DATA.__common: 0x1ad8

   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 11082
-  Symbols:   14259
-  CStrings:  11805
+  Functions: 11093
+  Symbols:   14272
+  CStrings:  11827
 
Symbols:
+ _OBJC_CLASS_$_TISecureCandidateAttributes
+ _OBJC_METACLASS_$_TISecureCandidateAttributes
CStrings:
+ "%s Could not cache sticker image; sticker image ref (%p) and/or identifier (%@) were nil."
+ "%s Retrieved meCard regions from cache"
+ "%s Updated the meCard regions cache."
+ "+[TIKeyboardSecureCandidateTextRendering drawSecureHeaders:secureContents:inContexts:traits:truncationSentinel:]"
+ "-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]"
+ "-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke"
+ "-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:]_block_invoke_2"
+ "-[TIKeyboardSecureCandidateRenderer imagesFromSecureCandidates:withRenderTraits:outAccessibilityLabels:]"
+ "-[TIKeyboardSecureCandidateRenderer slotIDsFromSecureCandidates:withRenderTraits:]"
+ "-[TIStickerCandidateGenerator cacheStickerImage:forIdentifier:]"
+ "@56@0:8@16@24^{__CFArray=}32@40@48"
+ "@72@0:8@16@24@32@40^{__CFArray=}48d56@64"
+ "@76@0:8@16@24@32@40^{__CFArray=}48d56@64B72"
+ "T@\"NSArray\",C,N,V_cachedMeCardRegions"
+ "T@\"NSDate\",C,N,V_lastMeCardRegionFetchTime"
+ "TB,N,V_isSecureCandidateDoubleLines"
+ "TISecureCandidateAttributes"
+ "Td,N,V_secureCandidateWidth"
+ "^{__CFArray=}40@0:8@16@24^@32"
+ "_arrayOfAttributes"
+ "_arrayOfSecureCandidateAttributes:"
+ "_cachedMeCardRegions"
+ "_drawLineFromCellAtIndex:ofResponse:atYCoordinate:atXCoordinate:inContext:"
+ "_drawSingleLineSecureHeaders:secureContents:layoutTraits:renderTraits:contexts:availableWidth:truncationSentinel:abortInsteadOfTruncating:"
+ "_drawTwoLineCellsWithSecureHeaders:secureContents:layoutTraits:renderTraits:contexts:availableWidth:truncationSentinel:"
+ "_isSecureCandidateDoubleLines"
+ "_lastMeCardRegionFetchTime"
+ "_secureCandidateWidth"
+ "cachedMeCardRegions"
+ "drawSecureHeaders:secureContents:inContexts:traits:truncationSentinel:"
+ "generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:isSecureCandidateDoubleLines:completionHandler:"
+ "imagesFromSecureCandidates:withRenderTraits:outAccessibilityLabels:"
+ "isInlinePromptUI"
+ "isSecureCandidateDoubleLines"
+ "lastMeCardRegionFetchTime"
+ "secureCandidateWidth"
+ "setCachedMeCardRegions:"
+ "setIsSecureCandidateDoubleLines:"
+ "setLastMeCardRegionFetchTime:"
+ "slotIDsFromSecureCandidates:withRenderTraits:"
+ "v56@0:8Q16@24d32d40^{CGContext=}48"
+ "v72@0:8I16@20@28@36d44Q52B60@?64"
- "\v"
- "+[TIKeyboardSecureCandidateTextRendering drawSecureHeaders:secureContents:inContexts:traits:truncationSentinel:outWidths:]"
- "-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:completionHandler:]"
- "-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:completionHandler:]_block_invoke"
- "-[TIAppAutofillManager generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:completionHandler:]_block_invoke_2"
- "-[TIKeyboardSecureCandidateRenderer imagesFromSecureCandidates:withRenderTraits:outAccessibilityLabels:outWidths:]"
- "-[TIKeyboardSecureCandidateRenderer slotIDsFromSecureCandidates:withRenderTraits:outWidths:]"
- "B84@0:8@16@24@32@40^{__CFArray=}48d56@64B72@76"
- "^{__CFArray=}48@0:8@16@24^@32@40"
- "_drawLineFromCellAtIndex:ofResponse:atYCoordinate:inContext:withAvailableWidth:"
- "_drawSingleLineSecureHeaders:secureContents:layoutTraits:renderTraits:contexts:availableWidth:truncationSentinel:abortInsteadOfTruncating:outWidths:"
- "_drawTwoLineCellsWithSecureHeaders:secureContents:layoutTraits:renderTraits:contexts:availableWidth:truncationSentinel:outWidths:"
- "drawSecureHeaders:secureContents:inContexts:traits:truncationSentinel:outWidths:"
- "generateHideMyEmailCandidateWithSlotID:applicationBundleId:applicationId:keyboardState:secureCandidateWidth:secureCandidateHash:completionHandler:"
- "imagesFromSecureCandidates:withRenderTraits:outAccessibilityLabels:outWidths:"
- "slotIDsFromSecureCandidates:withRenderTraits:outWidths:"
- "v56@0:8Q16@24d32^{CGContext=}40d48"
- "v64@0:8@16@24^{__CFArray=}32@40@48@56"
- "v68@0:8I16@20@28@36d44Q52@?60"
- "v80@0:8@16@24@32@40^{__CFArray=}48d56@64@72"

```
