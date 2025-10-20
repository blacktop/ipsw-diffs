## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

```diff

-355.2.0.0.0
-  __TEXT.__text: 0x4ea4c
+355.4.0.0.0
+  __TEXT.__text: 0x4fc28
   __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x52c8
-  __TEXT.__const: 0x94c
-  __TEXT.__cstring: 0x2f4e
-  __TEXT.__oslogstring: 0x4936
-  __TEXT.__gcc_except_tab: 0xb10
-  __TEXT.__ustring: 0x26
+  __TEXT.__objc_methlist: 0x53d8
+  __TEXT.__const: 0xa78
+  __TEXT.__cstring: 0x2f9e
+  __TEXT.__oslogstring: 0x4aa6
+  __TEXT.__gcc_except_tab: 0xb50
+  __TEXT.__ustring: 0x90
   __TEXT.__constg_swiftt: 0x26c
   __TEXT.__swift5_typeref: 0x3f9
   __TEXT.__swift5_reflstr: 0x242

   __TEXT.__swift5_capture: 0x174
   __TEXT.__swift_as_entry: 0x44
   __TEXT.__swift_as_ret: 0x48
-  __TEXT.__unwind_info: 0x1898
+  __TEXT.__unwind_info: 0x18e8
   __TEXT.__eh_frame: 0x7a8
-  __TEXT.__objc_classname: 0xafe
-  __TEXT.__objc_methname: 0xaefa
-  __TEXT.__objc_methtype: 0x1c1a
-  __TEXT.__objc_stubs: 0x6380
+  __TEXT.__objc_classname: 0xb36
+  __TEXT.__objc_methname: 0xb2a6
+  __TEXT.__objc_methtype: 0x1c3a
+  __TEXT.__objc_stubs: 0x6560
   __DATA_CONST.__got: 0x500
-  __DATA_CONST.__const: 0x1c38
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__const: 0x1cb8
+  __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2438
+  __DATA_CONST.__objc_selrefs: 0x24c8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_arraydata: 0x78
+  __DATA_CONST.__objc_superrefs: 0x268
+  __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x870
   __AUTH_CONST.__const: 0xce8
-  __AUTH_CONST.__cfstring: 0x32c0
-  __AUTH_CONST.__objc_const: 0xa730
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__cfstring: 0x34c0
+  __AUTH_CONST.__objc_const: 0xaa40
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1150
+  __AUTH.__objc_data: 0x11f0
   __AUTH.__data: 0x480
-  __DATA.__objc_ivar: 0x7b8
+  __DATA.__objc_ivar: 0x7e0
   __DATA.__data: 0xa30
   __DATA.__bss: 0xa00
   __DATA.__common: 0x48

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/Frameworks/Speech.framework/Speech
+  - /System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F80654C5-A53F-3F70-8A09-65D997994785
-  Functions: 2474
-  Symbols:   7136
-  CStrings:  3431
+  UUID: BC2C6C30-4729-3BA0-811B-8A7CB79B58B4
+  Functions: 2502
+  Symbols:   7242
+  CStrings:  3491
 
Symbols:
+ +[_LTCombinedTranslationResult _translatedTextWithAttributesForResult:].cold.3
+ +[_LTGenmojiReplacementManager rareEmojiPlaceholderCandidates]
+ -[NSAttributedString(TranslationAdditions) lt_containsSubstringWithAttribute:]
+ -[_LTGenmojiReplacementInfo .cxx_destruct]
+ -[_LTGenmojiReplacementInfo initWithOriginalRange:replacementRange:requestID:originalSubstring:placeholderString:]
+ -[_LTGenmojiReplacementInfo originalRange]
+ -[_LTGenmojiReplacementInfo originalSubstring]
+ -[_LTGenmojiReplacementInfo placeholderString]
+ -[_LTGenmojiReplacementInfo replacementRange]
+ -[_LTGenmojiReplacementInfo requestUniqueID]
+ -[_LTGenmojiReplacementInfo setSourceAttributes:]
+ -[_LTGenmojiReplacementInfo sourceAttributes]
+ -[_LTGenmojiReplacementManager .cxx_destruct]
+ -[_LTGenmojiReplacementManager addReplacementInfo:]
+ -[_LTGenmojiReplacementManager init]
+ -[_LTGenmojiReplacementManager replacementInfoForRequestID:]
+ -[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]
+ -[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:].cold.1
+ -[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:].cold.2
+ -[_LTTextTranslationRequest preserveGenmoji]
+ -[_LTTextTranslationRequest setPreserveGenmoji:]
+ -[_LTTranslationResult replacementInfos]
+ -[_LTTranslationResult setReplacementInfos:]
+ GCC_except_table127
+ GCC_except_table59
+ GCC_except_table66
+ GCC_except_table69
+ _OBJC_CLASS_$__LTGenmojiReplacementInfo
+ _OBJC_CLASS_$__LTGenmojiReplacementManager
+ _OBJC_IVAR_$__LTGenmojiReplacementInfo._originalRange
+ _OBJC_IVAR_$__LTGenmojiReplacementInfo._originalSubstring
+ _OBJC_IVAR_$__LTGenmojiReplacementInfo._placeholderString
+ _OBJC_IVAR_$__LTGenmojiReplacementInfo._replacementRange
+ _OBJC_IVAR_$__LTGenmojiReplacementInfo._requestUniqueID
+ _OBJC_IVAR_$__LTGenmojiReplacementInfo._sourceAttributes
+ _OBJC_IVAR_$__LTGenmojiReplacementManager._infoMap
+ _OBJC_IVAR_$__LTTextTranslationRequest._genmojiReplacementManager
+ _OBJC_IVAR_$__LTTextTranslationRequest._preserveGenmoji
+ _OBJC_IVAR_$__LTTranslationResult._replacementInfos
+ _OBJC_METACLASS_$__LTGenmojiReplacementInfo
+ _OBJC_METACLASS_$__LTGenmojiReplacementManager
+ __LTTranslationAdaptiveImageAttributeKey
+ __OBJC_$_CLASS_METHODS__LTGenmojiReplacementManager
+ __OBJC_$_CLASS_PROP_LIST__LTGenmojiReplacementManager
+ __OBJC_$_INSTANCE_METHODS__LTGenmojiReplacementInfo
+ __OBJC_$_INSTANCE_METHODS__LTGenmojiReplacementManager
+ __OBJC_$_INSTANCE_VARIABLES__LTGenmojiReplacementInfo
+ __OBJC_$_INSTANCE_VARIABLES__LTGenmojiReplacementManager
+ __OBJC_$_PROP_LIST__LTGenmojiReplacementInfo
+ __OBJC_CLASS_RO_$__LTGenmojiReplacementInfo
+ __OBJC_CLASS_RO_$__LTGenmojiReplacementManager
+ __OBJC_METACLASS_RO_$__LTGenmojiReplacementInfo
+ __OBJC_METACLASS_RO_$__LTGenmojiReplacementManager
+ ___78-[NSAttributedString(TranslationAdditions) lt_containsSubstringWithAttribute:]_block_invoke
+ ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke
+ ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke.231
+ ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke.231.cold.1
+ ___block_descriptor_40_e8_32r_e27_v40?08{_NSRange=QQ}16^B32lr32l8
+ ___block_descriptor_40_e8_32s_e42_v40?0"EMFEmojiToken"8{_NSRange=QQ}16^B32ls32l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e27_v40?08{_NSRange=QQ}16^B32ls32l8r64l8s40l8s48l8s56l8
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ _objc_msgSend$_enumerateEmojiTokensInRange:block:
+ _objc_msgSend$_replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:
+ _objc_msgSend$addReplacementInfo:
+ _objc_msgSend$attributesAtIndex:effectiveRange:
+ _objc_msgSend$enumerateAttribute:inRange:options:usingBlock:
+ _objc_msgSend$initWithOriginalRange:replacementRange:requestID:originalSubstring:placeholderString:
+ _objc_msgSend$lt_containsSubstringWithAttribute:
+ _objc_msgSend$originalSubstring
+ _objc_msgSend$placeholderString
+ _objc_msgSend$preserveGenmoji
+ _objc_msgSend$rareEmojiPlaceholderCandidates
+ _objc_msgSend$replacementInfoForRequestID:
+ _objc_msgSend$replacementInfos
+ _objc_msgSend$requestUniqueID
+ _objc_msgSend$setReplacementInfos:
- GCC_except_table122
- GCC_except_table58
- GCC_except_table65
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
CStrings:
+ "\b&"
+ "<\xd8\x01\xde"
+ "<ؾ\xdc"
+ "<\xd8\xe6\xdd<\xd8\xf6\xdd"
+ "<\xd8\xec\xdd<\xd8\xf5\xdd"
+ "<\xd8\xee\xdd<\xd8\xf4\xdd"
+ "<\xd8\xf3\xdd<\xd8\xf7\xdd"
+ "=\xd8\x0f\xdd"
+ "=\xd8_\xdd"
+ "=ز\xdd\x0f\xfe"
+ "=\xd8\xc2\xde"
+ "=\xd8\xdf\xdc"
+ "=\xd8\xf7\xde"
+ ">ؖ\xde"
+ ">\xd8\xee\xdd"
+ "@\"_LTGenmojiReplacementManager\""
+ "All rare emoji exist in string, can't find any placeholders for translating genmoji; Genmoji will be lost in translation"
+ "CTAdaptiveImageProvider"
+ "Can't find placeholder emoji for putting back genmoji"
+ "Not attempting to replace Genmoji since client didn't request this"
+ "Removing placeholder emoji for genmoji text in %zu places"
+ "T@\"NSArray\",C,N,V_replacementInfos"
+ "T@\"NSString\",R,C,N,V_originalSubstring"
+ "T@\"NSString\",R,C,N,V_placeholderString"
+ "T@\"NSString\",R,C,N,V_requestUniqueID"
+ "TB,N,V_preserveGenmoji"
+ "T{_NSRange=QQ},R,N,V_originalRange"
+ "T{_NSRange=QQ},R,N,V_replacementRange"
+ "Warning: Not enough unique emoji placeholders for how many Genmoji are in the source string; reusing emoji placeholder which could cause issues with translated Genmoji"
+ "_LTGenmojiReplacementInfo"
+ "_LTGenmojiReplacementManager"
+ "_enumerateEmojiTokensInRange:block:"
+ "_genmojiReplacementManager"
+ "_infoMap"
+ "_originalRange"
+ "_originalSubstring"
+ "_placeholderString"
+ "_preserveGenmoji"
+ "_replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:"
+ "_replacementInfos"
+ "_replacementRange"
+ "_requestUniqueID"
+ "addReplacementInfo:"
+ "attributesAtIndex:effectiveRange:"
+ "enumerateAttribute:inRange:options:usingBlock:"
+ "initWithOriginalRange:replacementRange:requestID:originalSubstring:placeholderString:"
+ "lt_containsSubstringWithAttribute:"
+ "originalRange"
+ "originalSubstring"
+ "placeholderString"
+ "preserveGenmoji"
+ "rareEmojiPlaceholderCandidates"
+ "replacementInfoForRequestID:"
+ "replacementInfos"
+ "replacementRange"
+ "requestUniqueID"
+ "setPreserveGenmoji:"
+ "setReplacementInfos:"
+ "v40@?0@\"EMFEmojiToken\"8{_NSRange=QQ}16^B32"
+ "v40@?0@8{_NSRange=QQ}16^B32"
- "Skipping alignment information in translation result since there's nothing to re-align"

```
