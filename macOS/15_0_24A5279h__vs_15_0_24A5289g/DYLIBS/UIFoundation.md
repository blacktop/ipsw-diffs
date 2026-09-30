## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/Versions/A/UIFoundation`

```diff

-959.0.0.0.0
-  __TEXT.__text: 0x135db8
-  __TEXT.__auth_stubs: 0x2790
-  __TEXT.__objc_methlist: 0xbb44
-  __TEXT.__const: 0x11cc
-  __TEXT.__cstring: 0x1698e
+961.0.0.0.0
+  __TEXT.__text: 0x137ad4
+  __TEXT.__auth_stubs: 0x2780
+  __TEXT.__objc_methlist: 0xbcf4
+  __TEXT.__const: 0x11dc
+  __TEXT.__cstring: 0x169e6
   __TEXT.__ustring: 0x31a
-  __TEXT.__gcc_except_tab: 0x319c
+  __TEXT.__gcc_except_tab: 0x3370
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__dof_UIFoundat: 0x2bd
-  __TEXT.__unwind_info: 0x40c8
-  __TEXT.__objc_classname: 0x1200
-  __TEXT.__objc_methname: 0x20bc8
-  __TEXT.__objc_methtype: 0x8d6f
-  __TEXT.__objc_stubs: 0x16b60
+  __TEXT.__unwind_info: 0x41a8
+  __TEXT.__objc_classname: 0x121d
+  __TEXT.__objc_methname: 0x21243
+  __TEXT.__objc_methtype: 0x8ef5
+  __TEXT.__objc_stubs: 0x16e00
   __DATA_CONST.__got: 0xaf0
   __DATA_CONST.__const: 0x7038
-  __DATA_CONST.__objc_classlist: 0x488
+  __DATA_CONST.__objc_classlist: 0x490
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7040
+  __DATA_CONST.__objc_selrefs: 0x7158
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x13d8
+  __AUTH_CONST.__auth_got: 0x13d0
   __AUTH_CONST.__auth_ptr: 0x50
-  __AUTH_CONST.__const: 0x3e58
-  __AUTH_CONST.__cfstring: 0x10140
-  __AUTH_CONST.__objc_const: 0x146f8
+  __AUTH_CONST.__const: 0x3f88
+  __AUTH_CONST.__cfstring: 0x10180
+  __AUTH_CONST.__objc_const: 0x14a58
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x910
+  __AUTH.__objc_data: 0x960
   __AUTH.__data: 0x48
-  __DATA.__objc_ivar: 0x149c
-  __DATA.__data: 0x1298
-  __DATA.__bss: 0x1050
+  __DATA.__objc_ivar: 0x14dc
+  __DATA.__data: 0x12a0
+  __DATA.__bss: 0x1048
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2440
-  __DATA_DIRTY.__data: 0x5e0
-  __DATA_DIRTY.__bss: 0x5e0
+  __DATA_DIRTY.__data: 0x678
+  __DATA_DIRTY.__bss: 0x5d8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 5446
-  Symbols:   13427
-  CStrings:  3864
+  Functions: 5493
+  Symbols:   13534
+  CStrings:  3868
 
Symbols:
+ +[NSTextLineFragment _hiddenContentRenderingAttributes]
+ -[NSTextAnimationContext .cxx_destruct]
+ -[NSTextAnimationContext _contentsReplaced]
+ -[NSTextAnimationContext _effectiveComponents]
+ -[NSTextAnimationContext _effectiveExclusiveComponents]
+ -[NSTextAnimationContext _endAnimationContext:]
+ -[NSTextAnimationContext _hasRenderableComponentsForRange:]
+ -[NSTextAnimationContext _invalidated]
+ -[NSTextAnimationContext _overridden]
+ -[NSTextAnimationContext _shiftLocationForDelta:]
+ -[NSTextAnimationContext _unionTextRange]
+ -[NSTextAnimationContext _updateEnclosingLocation:endLocation:]
+ -[NSTextAnimationContext completionHandler]
+ -[NSTextAnimationContext componentsForExclusiveRange]
+ -[NSTextAnimationContext components]
+ -[NSTextAnimationContext enclosingTextRange]
+ -[NSTextAnimationContext finalizeAnimation]
+ -[NSTextAnimationContext initWithTextLayoutManager:textRanges:]
+ -[NSTextAnimationContext presentationLayoutFragmentFrameForTextLayoutFragment:proposedOrigin:]
+ -[NSTextAnimationContext presentationSizeProvider]
+ -[NSTextAnimationContext setCompletionHandler:]
+ -[NSTextAnimationContext setComponents:]
+ -[NSTextAnimationContext setComponentsForExclusiveRange:]
+ -[NSTextAnimationContext setPresentationSizeProvider:]
+ -[NSTextAnimationContext setSnapshotAttributeOverrides:]
+ -[NSTextAnimationContext snapshotAttributeOverrides]
+ -[NSTextAnimationContext snapshotWithComponents:exclusiveComponents:usingBlock:]
+ -[NSTextAnimationContext textLayoutManager]
+ -[NSTextAnimationContext textRanges]
+ -[NSTextLayoutFragment _renderingAttributesForTextAnimationContextComponent:range:attributes:effectiveRange:]
+ -[NSTextLayoutManager _addTextAnimationContext:]
+ -[NSTextLayoutManager _adjustedTextLayoutFragmentBoundaryTextRangeForTextRange:location:endLocation:]
+ -[NSTextLayoutManager _invalidateTextAnimationContextForTextRange:reason:]
+ -[NSTextLayoutManager _removeTextAnimationContext:]
+ -[NSTextLayoutManager _textAnimationContextForLocation:]
+ GCC_except_table113
+ GCC_except_table154
+ GCC_except_table287
+ GCC_except_table293
+ GCC_except_table294
+ GCC_except_table295
+ GCC_except_table31
+ GCC_except_table79
+ OBJC_IVAR_$_NSParagraphArbitrator._breakerLanguage
+ OBJC_IVAR_$_NSTextAnimationContext._completionHandler
+ OBJC_IVAR_$_NSTextAnimationContext._components
+ OBJC_IVAR_$_NSTextAnimationContext._componentsForExclusiveRange
+ OBJC_IVAR_$_NSTextAnimationContext._enclosingEndLocation
+ OBJC_IVAR_$_NSTextAnimationContext._enclosingLocation
+ OBJC_IVAR_$_NSTextAnimationContext._enclosingTextRange
+ OBJC_IVAR_$_NSTextAnimationContext._inSnapshot
+ OBJC_IVAR_$_NSTextAnimationContext._presentationSizeProvider
+ OBJC_IVAR_$_NSTextAnimationContext._snapshotAttributeOverrides
+ OBJC_IVAR_$_NSTextAnimationContext._snapshotComponents
+ OBJC_IVAR_$_NSTextAnimationContext._snapshotExclusiveComponents
+ OBJC_IVAR_$_NSTextAnimationContext._textLayoutManager
+ OBJC_IVAR_$_NSTextAnimationContext._textRanges
+ OBJC_IVAR_$_NSTextAnimationContext._unionTextRange
+ OBJC_IVAR_$_NSTextLayoutFragment._textAnimationContextState
+ OBJC_IVAR_$_NSTextLayoutManager._textAnimationContextStorage
+ _NSPOSIXLanguageIdentifier
+ _OBJC_CLASS_$_NSTextAnimationContext
+ _OBJC_METACLASS_$_NSTextAnimationContext
+ __101-[NSTextLineFragment _getCaretPositionsForCharactersInRange:positionsCache:positionsCacheSize:block:]_block_invoke.39
+ __45-[NSTextLineFragment boundsWithType:options:]_block_invoke.20
+ __45-[NSTextLineFragment boundsWithType:options:]_block_invoke.30
+ __74-[NSTextLayoutManager _invalidateTextAnimationContextForTextRange:reason:]_block_invoke.290
+ __OBJC_$_INSTANCE_METHODS_NSTextAnimationContext
+ __OBJC_$_INSTANCE_VARIABLES_NSTextAnimationContext
+ __OBJC_$_PROP_LIST_NSTextAnimationContext
+ __OBJC_CLASS_RO_$_NSTextAnimationContext
+ __OBJC_METACLASS_RO_$_NSTextAnimationContext
+ ___101-[NSTextLayoutManager _adjustedTextLayoutFragmentBoundaryTextRangeForTextRange:location:endLocation:]_block_invoke
+ ___101-[NSTextLayoutManager _adjustedTextLayoutFragmentBoundaryTextRangeForTextRange:location:endLocation:]_block_invoke_2
+ ___109-[NSTextLayoutFragment _renderingAttributesForTextAnimationContextComponent:range:attributes:effectiveRange:]_block_invoke
+ ___55+[NSTextLineFragment _hiddenContentRenderingAttributes]_block_invoke
+ ___56-[NSTextLayoutManager _textAnimationContextForLocation:]_block_invoke
+ ___74-[NSTextLayoutManager _invalidateTextAnimationContextForTextRange:reason:]_block_invoke
+ ___80-[NSTextAnimationContext snapshotWithComponents:exclusiveComponents:usingBlock:]_block_invoke
+ ___NSTextLayoutFragmentConfigureForTextAnimationContext
+ ____NSTextLayoutManagerFillSoftInvalidationToLocation_block_invoke.643
+ ____NSTextLayoutManagerRemoveTextLayoutFragmentsInTextRange_block_invoke.646
+ _____NSTextLayoutFragmentConfigureForTextAnimationContext_block_invoke
+ ___block_descriptor_128_e8_32o40o48o56r64r72r80r88r_e37_v24?0"<NSTextViewportElement>"8^B16l
+ ___block_descriptor_40_e8_32o_e25_v32?0"NSString"816^B24l
+ ___block_descriptor_40_e8_32o_e39_v32?0"NSTextAnimationContext"8Q16^B24l
+ ___block_descriptor_48_e8_32o40o_e28_v32?08"NSTextRange"16^B24l
+ ___block_descriptor_48_e8_32o40r_e28_v32?08"NSTextRange"16^B24l
+ ___block_descriptor_80_e8_32o40o48o56o64r_e28_v32?0"NSTextRange"8Q16^B24l
+ ___copy_helper_block_e8_32o40o48o56o64r
+ ___copy_helper_block_e8_32o40o48o56r64r72r80r88r
+ ___defaultBreakLanguage_block_invoke
+ ___destroy_helper_block_e8_32o40o48o56o64r
+ ___destroy_helper_block_e8_32o40o48o56r64r72r80r88r
+ __block_literal_global.360
+ __block_literal_global.366
+ __block_literal_global.648
+ __block_literal_global.691
+ __block_literal_global.697
+ __block_literal_global.738
+ __block_literal_global.744
+ __block_literal_global.753
+ _defaultBreakLanguage
+ _hiddenContentRenderingAttributes.onceToken
+ _hiddenContentRenderingAttributes.renderingAttributes
+ _objc_msgSend$_addTextAnimationContext:
+ _objc_msgSend$_adjustedTextLayoutFragmentBoundaryTextRangeForTextRange:location:endLocation:
+ _objc_msgSend$_effectiveComponents
+ _objc_msgSend$_effectiveExclusiveComponents
+ _objc_msgSend$_endAnimationContext:
+ _objc_msgSend$_hasRenderableComponentsForRange:
+ _objc_msgSend$_hiddenContentRenderingAttributes
+ _objc_msgSend$_invalidateTextAnimationContextForTextRange:reason:
+ _objc_msgSend$_overridden
+ _objc_msgSend$_removeTextAnimationContext:
+ _objc_msgSend$_renderingAttributesForTextAnimationContextComponent:range:attributes:effectiveRange:
+ _objc_msgSend$_textAnimationContextForLocation:
+ _objc_msgSend$_unionTextRange
+ _objc_msgSend$_updateEnclosingLocation:endLocation:
+ _objc_msgSend$canonicalLanguageIdentifierFromString:
+ _objc_msgSend$completionHandler
+ _objc_msgSend$enclosingTextRange
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$languageIdentifier
+ _objc_msgSend$presentationLayoutFragmentFrameForTextLayoutFragment:proposedOrigin:
+ _objc_msgSend$proofreadingController:replaceCharactersInRange:state:replacementAttributedString:
+ _objc_msgSend$snapshotAttributeOverrides
+ defaultBreakLanguage.onceToken
+ defaultBreakLanguage.result
- GCC_except_table117
- GCC_except_table151
- GCC_except_table152
- GCC_except_table35
- OBJC_IVAR_$_NSParagraphArbitrator._breakerLocale
- _CFLocaleGetIdentifier
- __101-[NSTextLineFragment _getCaretPositionsForCharactersInRange:positionsCache:positionsCacheSize:block:]_block_invoke.36
- __45-[NSTextLineFragment boundsWithType:options:]_block_invoke.17
- __45-[NSTextLineFragment boundsWithType:options:]_block_invoke.27
- ___33+[NSFont systemFontOfSize:width:]_block_invoke
- ___37+[NSFont boldSystemFontOfSize:width:]_block_invoke
- ___NSAppearanceSizeBoldSystemFont
- ___NSAppearanceSizeSystemFont
- ____NSTextLayoutManagerFillSoftInvalidationToLocation_block_invoke.624
- ____NSTextLayoutManagerRemoveTextLayoutFragmentsInTextRange_block_invoke.627
- ___block_descriptor_120_e8_32o40o48o56r64r72r80r_e37_v24?0"<NSTextViewportElement>"8^B16l
- ___defaultBreakLocale_block_invoke
- __block_literal_global.362
- __block_literal_global.368
- __block_literal_global.629
- __block_literal_global.695
- __block_literal_global.699
- __block_literal_global.740
- __block_literal_global.746
- __block_literal_global.755
- _defaultBreakLocale
- _objc_msgSend$localeIdentifier
- boldSystemFontOfSize:width:.onceToken
- defaultBreakLocale.onceToken
- defaultBreakLocale.result
- systemFontOfSize:width:.onceToken
CStrings:
+ "Exception in snapshot handler"
+ "en-US"
+ "en-US-POSIX"
+ "v32@?0@\"NSTextAnimationContext\"8Q16^B24"

```
