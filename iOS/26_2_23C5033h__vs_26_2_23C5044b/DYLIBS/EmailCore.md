## EmailCore

> `/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore`

```diff

-3864.300.22.2.1
-  __TEXT.__text: 0x54938
-  __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x4f40
-  __TEXT.__const: 0xe80
-  __TEXT.__gcc_except_tab: 0x6eb0
-  __TEXT.__cstring: 0x7d04
-  __TEXT.__oslogstring: 0xcf9
+3864.300.41.2.1
+  __TEXT.__text: 0x55038
+  __TEXT.__auth_stubs: 0x1070
+  __TEXT.__objc_methlist: 0x5048
+  __TEXT.__const: 0xe90
+  __TEXT.__gcc_except_tab: 0x6f28
+  __TEXT.__cstring: 0x7d24
+  __TEXT.__oslogstring: 0x1010
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x52
   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x2818
-  __TEXT.__objc_classname: 0xcfc
-  __TEXT.__objc_methname: 0xae92
-  __TEXT.__objc_methtype: 0x171b
-  __TEXT.__objc_stubs: 0x7680
+  __TEXT.__unwind_info: 0x2838
+  __TEXT.__objc_classname: 0xd27
+  __TEXT.__objc_methname: 0xb140
+  __TEXT.__objc_methtype: 0x1751
+  __TEXT.__objc_stubs: 0x7800
   __DATA_CONST.__got: 0x6b0
   __DATA_CONST.__const: 0x2208
-  __DATA_CONST.__objc_classlist: 0x328
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2990
+  __DATA_CONST.__objc_selrefs: 0x2a10
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x278
+  __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__auth_got: 0x848
   __AUTH_CONST.__const: 0x738
   __AUTH_CONST.__cfstring: 0x52a0
-  __AUTH_CONST.__objc_const: 0x9d18
+  __AUTH_CONST.__objc_const: 0x9fa8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH.__objc_data: 0x390
+  __AUTH.__objc_data: 0x3e0
   __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x4a4
-  __DATA.__data: 0xd44
-  __DATA.__bss: 0x3c0
+  __DATA.__objc_ivar: 0x4bc
+  __DATA.__data: 0xda4
+  __DATA.__bss: 0x3d0
   __DATA.__common: 0x24
   __DATA_DIRTY.__objc_data: 0x1c20
   __DATA_DIRTY.__data: 0xb50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F0FA4C97-22DC-3853-8AD7-0CFDF6405CD6
-  Functions: 1926
-  Symbols:   7607
-  CStrings:  4465
+  UUID: 2A61CE24-AC20-38DF-895E-790B01E094A0
+  Functions: 1943
+  Symbols:   7683
+  CStrings:  4503
 
Symbols:
+ +[ECMessageBodyHTMLParser signpostLog]
+ +[ECMessageBodyParsingUtils snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:priceFormattingThresholds:]
+ -[ECMessageBodyHTMLParser initWithHTML:withPriceFormattingThresholds:]
+ -[ECMessageBodyHTMLParser signpostID]
+ -[ECPriceFormattingThresholds bodyChildCountThreshold]
+ -[ECPriceFormattingThresholds initWithNodeDepthThreshold:bodyChildCountThreshold:]
+ -[ECPriceFormattingThresholds nodeDepthThreshold]
+ -[ECPriceFormattingThresholds setBodyChildCountThreshold:]
+ -[ECPriceFormattingThresholds setNodeDepthThreshold:]
+ -[_ECParsedHTMLNode collectDescendantsIntoArray:]
+ -[_ECParsedHTMLNode depth]
+ -[_ECParsedHTMLNode priceFormattingThresholds]
+ -[_ECParsedHTMLNode rootNode]
+ -[_ECParsedHTMLNode setDepth:]
+ -[_ECParsedHTMLNode setPriceFormattingThresholds:]
+ -[_ECParsedHTMLNode setRootNode:]
+ -[_ECParsedHTMLTag _bodyElementChildCount]
+ OBJC_IVAR_$__ECParsedHTMLNode._depth
+ OBJC_IVAR_$__ECParsedHTMLNode._priceFormattingThresholds
+ OBJC_IVAR_$__ECParsedHTMLNode._rootNode
+ _OBJC_CLASS_$_ECPriceFormattingThresholds
+ _OBJC_IVAR_$_ECMessageBodyHTMLParser._priceFormattingThresholds
+ _OBJC_IVAR_$_ECPriceFormattingThresholds._bodyChildCountThreshold
+ _OBJC_IVAR_$_ECPriceFormattingThresholds._nodeDepthThreshold
+ _OBJC_METACLASS_$_ECPriceFormattingThresholds
+ __OBJC_$_CLASS_METHODS_ECMessageBodyHTMLParser
+ __OBJC_$_CLASS_PROP_LIST_ECMessageBodyHTMLParser
+ __OBJC_$_CLASS_PROP_LIST_EFSignpostable
+ __OBJC_$_INSTANCE_METHODS_ECPriceFormattingThresholds
+ __OBJC_$_INSTANCE_VARIABLES_ECPriceFormattingThresholds
+ __OBJC_$_PROP_LIST_ECMessageBodyHTMLParser
+ __OBJC_$_PROP_LIST_ECPriceFormattingThresholds
+ __OBJC_$_PROP_LIST_EFSignpostable
+ __OBJC_$_PROTOCOL_CLASS_METHODS_EFSignpostable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EFSignpostable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EFSignpostable
+ __OBJC_$_PROTOCOL_REFS_EFSignpostable
+ __OBJC_CLASS_PROTOCOLS_$_ECMessageBodyHTMLParser
+ __OBJC_CLASS_RO_$_ECPriceFormattingThresholds
+ __OBJC_LABEL_PROTOCOL_$_EFSignpostable
+ __OBJC_METACLASS_RO_$_ECPriceFormattingThresholds
+ __OBJC_PROTOCOL_$_EFSignpostable
+ ___126+[ECMessageBodyParsingUtils snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:priceFormattingThresholds:]_block_invoke
+ ___126+[ECMessageBodyParsingUtils snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:priceFormattingThresholds:]_block_invoke_2
+ ___38+[ECMessageBodyHTMLParser signpostLog]_block_invoke
+ ___block_descriptor_49_ea8_32s40r_e39_v32?0"<ECMessageBodyElement>"8Q16^B24ls32l8r40l8
+ __os_signpost_emit_with_name_impl
+ _objc_msgSend$_bodyElementChildCount
+ _objc_msgSend$bodyChildCountThreshold
+ _objc_msgSend$collectDescendantsIntoArray:
+ _objc_msgSend$depth
+ _objc_msgSend$initWithHTML:withPriceFormattingThresholds:
+ _objc_msgSend$nodeDepthThreshold
+ _objc_msgSend$priceFormattingThresholds
+ _objc_msgSend$rootNode
+ _objc_msgSend$setDepth:
+ _objc_msgSend$setPriceFormattingThresholds:
+ _objc_msgSend$setRootNode:
+ _objc_msgSend$signpostID
+ _objc_msgSend$signpostLog
+ _objc_msgSend$snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:priceFormattingThresholds:
+ _os_signpost_enabled
+ _os_signpost_id_make_with_pointer
+ _signpostLog.log
+ _signpostLog.onceToken
- -[_ECParsedHTMLNode collectDescendanceIntoArray:]
- ___100+[ECMessageBodyParsingUtils snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:]_block_invoke
- ___100+[ECMessageBodyParsingUtils snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:]_block_invoke_2
- ___block_descriptor_41_ea8_32s_e39_v32?0"<ECMessageBodyElement>"8Q16^B24ls32l8
- _objc_msgSend$collectDescendanceIntoArray:
- _objc_msgSend$initWithHTML:
CStrings:
+ "@\"ECPriceFormattingThresholds\""
+ "@52@0:8@16Q24Q32B40@44"
+ "ECMessageBodyParserExtraction"
+ "ECMessageBodyParserNodeDetective"
+ "ECPriceFormattingThresholds"
+ "EFSignpostable"
+ "Failed to parse HTML and generate a snippet. HTML body length | snippet length: %{public,signpost.telemetry.number1}llu. processedNodes=%{public,signpost.telemetry.number2}lu enableTelemetry=YES "
+ "Found a valid node to apply price formatting at depth %{public,signpost.telemetry:number1}lu and body element count %{public,signpost.telemetry:number2}lu enableTelemetry=YES "
+ "Start parsing HTML for snippet generation enableTelemetry=YES "
+ "Start parsing nodes to determine eligibility for price formatting enableTelemetry=YES "
+ "Successfully parsed the HTML and generated a snippet. HTML body length | snippetLength:  %{public,signpost.telemetry.number1}llu. processedNodes=%{public,signpost.telemetry.number2}lu} enableTelemetry=YES "
+ "T@\"ECPriceFormattingThresholds\",N,V_priceFormattingThresholds"
+ "T@\"_ECParsedHTMLNode\",W,N,V_rootNode"
+ "TQ,N,V_bodyChildCountThreshold"
+ "TQ,N,V_depth"
+ "TQ,N,V_nodeDepthThreshold"
+ "_bodyChildCountThreshold"
+ "_bodyElementChildCount"
+ "_depth"
+ "_nodeDepthThreshold"
+ "_priceFormattingThresholds"
+ "_rootNode"
+ "bodyChildCountThreshold"
+ "collectDescendantsIntoArray:"
+ "com.apple.email.signposts"
+ "depth"
+ "initWithHTML:withPriceFormattingThresholds:"
+ "initWithNodeDepthThreshold:bodyChildCountThreshold:"
+ "nodeDepthThreshold"
+ "priceFormattingThresholds"
+ "rootNode"
+ "setBodyChildCountThreshold:"
+ "setDepth:"
+ "setNodeDepthThreshold:"
+ "setPriceFormattingThresholds:"
+ "setRootNode:"
+ "signpostID"
+ "signpostLog"
+ "snippetFromHTMLBody:options:maxLength:preservingQuotedForwardedContent:priceFormattingThresholds:"
- "collectDescendanceIntoArray:"

```
