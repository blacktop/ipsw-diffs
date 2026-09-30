## Silex

> `/System/Library/PrivateFrameworks/Silex.framework/Silex`

```diff

-5762.0.0.0.0
-  __TEXT.__text: 0x114fb8
+5784.0.0.0.0
+  __TEXT.__text: 0x116500
   __TEXT.__auth_stubs: 0xf90
-  __TEXT.__objc_methlist: 0x1e1e4
-  __TEXT.__const: 0x4cc
-  __TEXT.__cstring: 0x9cbe
-  __TEXT.__gcc_except_tab: 0x23b8
+  __TEXT.__objc_methlist: 0x1e424
+  __TEXT.__const: 0x4dc
+  __TEXT.__cstring: 0x9cf7
+  __TEXT.__gcc_except_tab: 0x2524
   __TEXT.__oslogstring: 0x2324
-  __TEXT.__ustring: 0x6c
-  __TEXT.__unwind_info: 0x4e58
-  __TEXT.__objc_classname: 0x773e
-  __TEXT.__objc_methname: 0x3b743
-  __TEXT.__objc_methtype: 0xe770
-  __TEXT.__objc_stubs: 0x23d40
-  __DATA_CONST.__got: 0x2528
-  __DATA_CONST.__const: 0x3c08
-  __DATA_CONST.__objc_classlist: 0x1ca8
+  __TEXT.__ustring: 0x74
+  __TEXT.__unwind_info: 0x4ec0
+  __TEXT.__objc_classname: 0x77c5
+  __TEXT.__objc_methname: 0x3bbc4
+  __TEXT.__objc_methtype: 0xe7c8
+  __TEXT.__objc_stubs: 0x23f60
+  __DATA_CONST.__got: 0x2548
+  __DATA_CONST.__const: 0x3c58
+  __DATA_CONST.__objc_classlist: 0x1cd0
   __DATA_CONST.__objc_catlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0xd28
+  __DATA_CONST.__objc_protolist: 0xd30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb710
-  __DATA_CONST.__objc_protorefs: 0x588
-  __DATA_CONST.__objc_superrefs: 0x1028
+  __DATA_CONST.__objc_selrefs: 0xb7b8
+  __DATA_CONST.__objc_protorefs: 0x590
+  __DATA_CONST.__objc_superrefs: 0x1048
   __DATA_CONST.__objc_arraydata: 0x3cc8
   __AUTH_CONST.__auth_got: 0x7e0
-  __AUTH_CONST.__const: 0x3c80
-  __AUTH_CONST.__cfstring: 0x97e0
-  __AUTH_CONST.__objc_const: 0x512e0
+  __AUTH_CONST.__const: 0x3ca0
+  __AUTH_CONST.__cfstring: 0x9840
+  __AUTH_CONST.__objc_const: 0x51978
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x2aa8
-  __AUTH.__objc_data: 0x3200
-  __DATA.__objc_ivar: 0x1f64
-  __DATA.__data: 0x9ef8
+  __AUTH.__objc_data: 0x3390
+  __DATA.__objc_ivar: 0x1fa0
+  __DATA.__data: 0x9f58
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0xec90
   __DATA_DIRTY.__bss: 0x1e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87DCA2E6-F074-3B9E-BDE2-750FB270390F
-  Functions: 8478
-  Symbols:   34270
-  CStrings:  14597
+  UUID: C9A82B78-8C0C-36D2-8ADC-384E4D7F41A1
+  Functions: 8523
+  Symbols:   34439
+  CStrings:  14644
 
Symbols:
+ +[SXHighlightScrollPosition jsonDictionaryRepresentationIsValid:exactly:]
+ -[SXComponent accessibilityLabelWithValue:withType:]
+ -[SXDataTableComponentView initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:textAttributionProvider:]
+ -[SXDataTableComponentView textAttributionProvider]
+ -[SXDataTableComponentViewFactory initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:textAttributionProvider:]
+ -[SXDataTableComponentViewFactory textAttributionProvider]
+ -[SXHighlightManager .cxx_destruct]
+ -[SXHighlightManager clear]
+ -[SXHighlightManager highlightLayers]
+ -[SXHighlightManager highlightText:]
+ -[SXHighlightManager highlightText:updateScrollPosition:]
+ -[SXHighlightManager icc]
+ -[SXHighlightManager initWithRenderCollector:icc:viewport:]
+ -[SXHighlightManager removeHighlightLayers]
+ -[SXHighlightManager renderCollector]
+ -[SXHighlightManager setText:]
+ -[SXHighlightManager text]
+ -[SXHighlightManager update]
+ -[SXHighlightManager viewport]
+ -[SXHighlightScrollPosition .cxx_destruct]
+ -[SXHighlightScrollPosition description]
+ -[SXHighlightScrollPosition dictionaryRepresentation]
+ -[SXHighlightScrollPosition encodeWithCoder:]
+ -[SXHighlightScrollPosition initWithDictionaryRepresentation:exactly:]
+ -[SXHighlightScrollPosition initWithText:]
+ -[SXHighlightScrollPosition text]
+ -[SXScrollViewController highlightManager]
+ -[SXTangierController initWithViewport:scrollView:componentActionHandler:dragItemProvider:componentController:componentInteractionManager:DOMObjectProvider:adIgnorableViewFactory:config:textAttributionProvider:]
+ -[SXTangierController textAttributionProvider]
+ -[SXTangierTextRenderCollector itemsForICC:]
+ -[SXTextAttributionProvider attribution]
+ -[SXTextHighlight .cxx_destruct]
+ -[SXTextHighlight initWithItem:range:]
+ -[SXTextHighlight item]
+ -[SXTextHighlight range]
+ -[SXTextHighlightLayer .cxx_destruct]
+ -[SXTextHighlightLayer drawInContext:]
+ -[SXTextHighlightLayer initWithRep:range:]
+ -[SXTextHighlightLayer range]
+ -[SXTextHighlightLayer rep]
+ -[SXTextTangierEditingController .cxx_destruct]
+ -[SXTextTangierEditingController initWithStorage:interactiveCanvasController:]
+ -[SXTextTangierEditingController textAttributionProvider]
+ -[SXTextTangierInteractiveCanvasController setTextAttributionProvider:]
+ -[SXTextTangierInteractiveCanvasController textAttributionProvider]
+ _CGContextSetBlendMode
+ _OBJC_CLASS_$_SXHighlightManager
+ _OBJC_CLASS_$_SXHighlightScrollPosition
+ _OBJC_CLASS_$_SXTextAttributionProvider
+ _OBJC_CLASS_$_SXTextHighlight
+ _OBJC_CLASS_$_SXTextHighlightLayer
+ _OBJC_IVAR_$_SXDataTableComponentView._textAttributionProvider
+ _OBJC_IVAR_$_SXDataTableComponentViewFactory._textAttributionProvider
+ _OBJC_IVAR_$_SXHighlightManager._highlightLayers
+ _OBJC_IVAR_$_SXHighlightManager._icc
+ _OBJC_IVAR_$_SXHighlightManager._renderCollector
+ _OBJC_IVAR_$_SXHighlightManager._text
+ _OBJC_IVAR_$_SXHighlightManager._viewport
+ _OBJC_IVAR_$_SXHighlightScrollPosition._text
+ _OBJC_IVAR_$_SXScrollViewController._highlightManager
+ _OBJC_IVAR_$_SXTangierController._textAttributionProvider
+ _OBJC_IVAR_$_SXTextHighlight._item
+ _OBJC_IVAR_$_SXTextHighlight._range
+ _OBJC_IVAR_$_SXTextHighlightLayer._range
+ _OBJC_IVAR_$_SXTextHighlightLayer._rep
+ _OBJC_IVAR_$_SXTextTangierEditingController._textAttributionProvider
+ _OBJC_IVAR_$_SXTextTangierInteractiveCanvasController._textAttributionProvider
+ _OBJC_METACLASS_$_SXHighlightManager
+ _OBJC_METACLASS_$_SXHighlightScrollPosition
+ _OBJC_METACLASS_$_SXTextAttributionProvider
+ _OBJC_METACLASS_$_SXTextHighlight
+ _OBJC_METACLASS_$_SXTextHighlightLayer
+ __OBJC_$_CLASS_METHODS_SXHighlightScrollPosition
+ __OBJC_$_INSTANCE_METHODS_SXHighlightManager
+ __OBJC_$_INSTANCE_METHODS_SXHighlightScrollPosition
+ __OBJC_$_INSTANCE_METHODS_SXTextAttributionProvider
+ __OBJC_$_INSTANCE_METHODS_SXTextHighlight
+ __OBJC_$_INSTANCE_METHODS_SXTextHighlightLayer
+ __OBJC_$_INSTANCE_VARIABLES_SXHighlightManager
+ __OBJC_$_INSTANCE_VARIABLES_SXHighlightScrollPosition
+ __OBJC_$_INSTANCE_VARIABLES_SXTextHighlight
+ __OBJC_$_INSTANCE_VARIABLES_SXTextHighlightLayer
+ __OBJC_$_PROP_LIST_SXHighlightManager
+ __OBJC_$_PROP_LIST_SXHighlightScrollPosition
+ __OBJC_$_PROP_LIST_SXTextAttributionProvider
+ __OBJC_$_PROP_LIST_SXTextAttributionProviding
+ __OBJC_$_PROP_LIST_SXTextHighlight
+ __OBJC_$_PROP_LIST_SXTextHighlightLayer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SXTextAttributionProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SXTextAttributionProviding
+ __OBJC_$_PROTOCOL_REFS_SXTextAttributionProviding
+ __OBJC_CLASS_PROTOCOLS_$_SXTextAttributionProvider
+ __OBJC_CLASS_RO_$_SXHighlightManager
+ __OBJC_CLASS_RO_$_SXHighlightScrollPosition
+ __OBJC_CLASS_RO_$_SXTextAttributionProvider
+ __OBJC_CLASS_RO_$_SXTextHighlight
+ __OBJC_CLASS_RO_$_SXTextHighlightLayer
+ __OBJC_LABEL_PROTOCOL_$_SXTextAttributionProviding
+ __OBJC_METACLASS_RO_$_SXHighlightManager
+ __OBJC_METACLASS_RO_$_SXHighlightScrollPosition
+ __OBJC_METACLASS_RO_$_SXTextAttributionProvider
+ __OBJC_METACLASS_RO_$_SXTextHighlight
+ __OBJC_METACLASS_RO_$_SXTextHighlightLayer
+ __OBJC_PROTOCOL_$_SXTextAttributionProviding
+ __OBJC_PROTOCOL_REFERENCE_$_SXTextAttributionProviding
+ ___36-[SXTangierAssembly loadInRegistry:]_block_invoke_7
+ ___44-[SXTangierTextRenderCollector itemsForICC:]_block_invoke
+ ___57-[SXHighlightManager highlightText:updateScrollPosition:]_block_invoke
+ ___57-[SXHighlightManager highlightText:updateScrollPosition:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40r_e30_v16?0"<TSKSearchReference>"8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e38_v24?0"SXTextTangierFlowStorage"8^B16ls32l8s40l8r48l8
+ ___block_literal_global.143
+ ___block_literal_global.146
+ ___block_literal_global.167
+ ___block_literal_global.181
+ _objc_msgSend$appendAttributedString:
+ _objc_msgSend$attribution
+ _objc_msgSend$clear
+ _objc_msgSend$drawInContext:limitSelection:suppressInvisibles:
+ _objc_msgSend$drawInContext:limitSelection:suppressInvisibles:renderMode:
+ _objc_msgSend$highlightManager
+ _objc_msgSend$highlightText:
+ _objc_msgSend$highlightText:updateScrollPosition:
+ _objc_msgSend$initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:textAttributionProvider:
+ _objc_msgSend$initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:textAttributionProvider:
+ _objc_msgSend$initWithItem:range:
+ _objc_msgSend$initWithRenderCollector:icc:viewport:
+ _objc_msgSend$initWithRep:range:
+ _objc_msgSend$initWithViewport:scrollView:componentActionHandler:dragItemProvider:componentController:componentInteractionManager:DOMObjectProvider:adIgnorableViewFactory:config:textAttributionProvider:
+ _objc_msgSend$insertAttributedString:atIndex:
+ _objc_msgSend$itemsForICC:
+ _objc_msgSend$nsAttributedSubstringWithAttachmentsRemovedFromRange:withLayoutParent:
+ _objc_msgSend$plainTextStringFromRange:convertTextualAttachments:includeChildTextStorages:forExport:withLayoutParent:
+ _objc_msgSend$rectsForSelectionRange:
+ _objc_msgSend$removeHighlightLayers
+ _objc_msgSend$renderCollector
+ _objc_msgSend$setTextAttributionProvider:
+ _objc_msgSend$textAttributionProvider
- -[SXComponent accessibilityLabel]
- -[SXDataTableComponentView initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:]
- -[SXDataTableComponentViewFactory initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:]
- -[SXTangierController initWithViewport:scrollView:componentActionHandler:dragItemProvider:componentController:componentInteractionManager:DOMObjectProvider:adIgnorableViewFactory:config:]
- -[SXTangierTextRenderCollector getAllItemsWithICC:]
- _OBJC_IVAR_$_SXComponent.accessibilityLabel
- __UISolariumFeatureFlagEnabled
- ___51-[SXTangierTextRenderCollector getAllItemsWithICC:]_block_invoke
- ___block_literal_global.142
- ___block_literal_global.148
- ___block_literal_global.163
- ___block_literal_global.192
- _objc_msgSend$applyTopBackgroundForStyle:onView:
- _objc_msgSend$getAllItemsWithICC:
- _objc_msgSend$initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:
- _objc_msgSend$initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:
- _objc_msgSend$initWithViewport:scrollView:componentActionHandler:dragItemProvider:componentController:componentInteractionManager:DOMObjectProvider:adIgnorableViewFactory:config:
- _objc_msgSend$nsAttributedSubstringFromRange:scale:
CStrings:
+ "\x1c "
+ "\x1d "
+ "1\x82"
+ "<%@: %p> Text: %@"
+ "@\"<SXTextAttributionProviding>\""
+ "@\"SXHighlightManager\""
+ "@\"TSWPRep\""
+ "SXHighlightManager"
+ "SXHighlightScrollPosition"
+ "SXTextAttributionProvider"
+ "SXTextAttributionProviding"
+ "SXTextHighlight"
+ "SXTextHighlightLayer"
+ "T@\"<SXTextAttributionProviding>\",&,N,V_textAttributionProvider"
+ "T@\"<SXTextAttributionProviding>\",R,N,V_textAttributionProvider"
+ "T@\"NSMutableArray\",R,N,V_highlightLayers"
+ "T@\"NSString\",C,N,V_text"
+ "T@\"NSString\",R,C,N,V_text"
+ "T@\"SXHighlightManager\",R,N,V_highlightManager"
+ "T@\"SXTangierTextRenderCollector\",R,N,V_renderCollector"
+ "T@\"SXTangierTextRenderCollectorItem\",R,N,V_item"
+ "T@\"TSWPRep\",R,N,V_rep"
+ "_highlightManager"
+ "_renderCollector"
+ "_textAttributionProvider"
+ "accessibilityLabelWithValue:withType:"
+ "appendAttributedString:"
+ "attribution"
+ "clear"
+ "drawInContext:"
+ "drawInContext:limitSelection:suppressInvisibles:"
+ "drawInContext:limitSelection:suppressInvisibles:renderMode:"
+ "highlightManager"
+ "highlightText:"
+ "highlightText:updateScrollPosition:"
+ "initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:textAttributionProvider:"
+ "initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:textAttributionProvider:"
+ "initWithItem:range:"
+ "initWithRenderCollector:icc:viewport:"
+ "initWithRep:range:"
+ "initWithStorage:interactiveCanvasController:"
+ "initWithViewport:scrollView:componentActionHandler:dragItemProvider:componentController:componentInteractionManager:DOMObjectProvider:adIgnorableViewFactory:config:textAttributionProvider:"
+ "insertAttributedString:atIndex:"
+ "itemsForICC:"
+ "nsAttributedSubstringWithAttachmentsRemovedFromRange:withLayoutParent:"
+ "plainTextStringFromRange:convertTextualAttachments:includeChildTextStorages:forExport:withLayoutParent:"
+ "rectsForSelectionRange:"
+ "removeHighlightLayers"
+ "renderCollector"
+ "setTextAttributionProvider:"
+ "textAttributionProvider"
+ "v24@0:8^{CGContext=}16"
+ "v24@?0@\"SXTextTangierFlowStorage\"8^B16"
- "1r"
- "T@\"NSString\",R,N,VaccessibilityLabel"
- "getAllItemsWithICC:"
- "initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:"
- "initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:imageViewFactory:componentActionHandler:textComponentLayoutHosting:componentController:adIgnorableViewFactory:config:"
- "initWithViewport:scrollView:componentActionHandler:dragItemProvider:componentController:componentInteractionManager:DOMObjectProvider:adIgnorableViewFactory:config:"
- "nsAttributedSubstringFromRange:scale:"

```
