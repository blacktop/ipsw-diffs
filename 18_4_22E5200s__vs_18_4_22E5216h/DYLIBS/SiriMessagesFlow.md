## SiriMessagesFlow

> `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow`

```diff

-3404.42.5.1.1
-  __TEXT.__text: 0x31b450
-  __TEXT.__auth_stubs: 0x7fd0
+3404.50.1.0.0
+  __TEXT.__text: 0x36214c
+  __TEXT.__auth_stubs: 0x8000
   __TEXT.__objc_methlist: 0x324
-  __TEXT.__const: 0xfe34
-  __TEXT.__cstring: 0xde07
-  __TEXT.__constg_swiftt: 0xcf8c
-  __TEXT.__swift5_typeref: 0x6a63
+  __TEXT.__const: 0xff14
+  __TEXT.__cstring: 0xdf37
+  __TEXT.__constg_swiftt: 0xd01c
+  __TEXT.__swift5_typeref: 0x6a81
   __TEXT.__swift5_builtin: 0x348
-  __TEXT.__swift5_reflstr: 0x7fdb
-  __TEXT.__swift5_fieldmd: 0x8f48
+  __TEXT.__swift5_reflstr: 0x800b
+  __TEXT.__swift5_fieldmd: 0x8f74
   __TEXT.__swift5_assocty: 0x1130
-  __TEXT.__swift5_proto: 0xb00
-  __TEXT.__swift5_types: 0x680
-  __TEXT.__swift5_capture: 0x2a14
-  __TEXT.__oslogstring: 0x24edf
+  __TEXT.__swift5_proto: 0xb10
+  __TEXT.__swift5_types: 0x684
+  __TEXT.__swift5_capture: 0x2a24
+  __TEXT.__oslogstring: 0x250df
   __TEXT.__swift5_protos: 0x170
-  __TEXT.__swift_as_entry: 0x104c
-  __TEXT.__swift_as_ret: 0x14fc
+  __TEXT.__swift_as_entry: 0x1054
+  __TEXT.__swift_as_ret: 0x1510
   __TEXT.__swift5_mpenum: 0xa0
-  __TEXT.__unwind_info: 0xc0f0
-  __TEXT.__eh_frame: 0x22ca4
+  __TEXT.__unwind_info: 0xbfc0
+  __TEXT.__eh_frame: 0x24428
   __TEXT.__objc_classname: 0x111
-  __TEXT.__objc_methname: 0x3c03
+  __TEXT.__objc_methname: 0x3c7a
   __TEXT.__objc_methtype: 0x32c
   __DATA_CONST.__got: 0x21b0
   __DATA_CONST.__const: 0x218
-  __DATA_CONST.__objc_classlist: 0x590
+  __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1638
+  __DATA_CONST.__objc_selrefs: 0x1660
   __DATA_CONST.__objc_protorefs: 0x78
-  __AUTH_CONST.__auth_got: 0x3fe8
-  __AUTH_CONST.__auth_ptr: 0x2480
-  __AUTH_CONST.__const: 0x103c0
-  __AUTH_CONST.__objc_const: 0xc4f8
+  __AUTH_CONST.__auth_got: 0x4000
+  __AUTH_CONST.__auth_ptr: 0x22f0
+  __AUTH_CONST.__const: 0x10488
+  __AUTH_CONST.__objc_const: 0xc5b0
   __AUTH.__objc_data: 0x1e38
-  __AUTH.__data: 0x113b8
-  __DATA.__data: 0x6dd0
-  __DATA.__bss: 0x12790
+  __AUTH.__data: 0x11458
+  __DATA.__data: 0x6df0
+  __DATA.__bss: 0x12990
   __DATA.__common: 0xa98
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 15611
-  Symbols:   8450
-  CStrings:  4317
+  Functions: 16159
+  Symbols:   9400
+  CStrings:  4335
 
Symbols:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
- _NSTemporaryDirectory
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initEnumMetadataSinglePayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
- _swift_singlePayloadEnumGeneric_getEnumTag
CStrings:
+ "#AdaptiveImageGlyphUtils failed to produce a description for %s glyph with count: %ld and descriptions %s, %s, %s"
+ "#AudioMessageUtils Cannot copy audio message file at %s. Proceeding without copy. error: %s"
+ "#ContentProcessor.convertContentToTokens appending ContentToken.generic"
+ "#FollowupOfferFlow exitValue from PromptForConfirmationFlow: %s"
+ "#SendMessageConfirmIntentFlow confirm intent flow completed: %s"
+ "#SendMessageConfirmIntentFlow confirm intent flow failed: %s"
+ "#SendMessageRCHFlowStrategy content from Type to Siri, hiding Siri attribution"
+ "#SendMessageRCHFlowStrategy content updated by keyboard, hiding Siri attribution"
+ "#SendMessageShimFlow failed to create temporary file from %@"
+ "#ShareThisFlow Cannot copy image file at %s. error %@"
+ "SearchForMessages#ReadGlyphDescription"
+ "SiriMessages.FetchAppDisallowListTrial"
+ "TTSUtil#localeExistsInDeviceLanaguageMap Checking if languageLocale=%s exists in #language map %s"
+ "TTSUtil#localeExistsInDeviceLanaguageMap: languageLocale=%s not found in #language map %s"
+ "TTSUtil#localeExistsInDeviceLanguageMap: deviceAvailableLanguages is empty"
+ "Trial factors updated. Refreshing."
+ "_TtC16SiriMessagesFlow22DisallowedAppsProvider"
+ "addUpdateHandlerForNamespaceName:usingBlock:"
+ "beginsWithEmojiOrGlyph"
+ "createFileAtPath:contents:attributes:"
+ "filename"
+ "glyphDescriptions"
+ "isPreviousTokenEmojiOrGlyph"
+ "refresh"
+ "temporaryDirectory"
+ "trialFactorProvider"
+ "v16@?0@\"<TRINamespaceUpdateProtocol>\"8"
- "#AudioMessageUtils Cannot copy audio message file at %s to %s. Proceeding without copy. error: %s"
- "#ContentProcessor.convertContentToTokens appending ContentToken.genericSticker"
- "#ContentProcessor.makeTextFromGroupedContentTokens creating dialog for filteredGroupTokens: %s"
- "#FollowupOfferFlow exitValue from PromptForConfirmationFlow: %{public}s"
- "#SendMessageConfirmIntentFlow confirm intent flow completed: %{public}s"
- "#SendMessageConfirmIntentFlow confirm intent flow failed: %{public}s"
- "#URL  copyToTemp Cannot copy message file at %s to %s. error %@"
- "#language map %s"
- "isEmoji"

```
