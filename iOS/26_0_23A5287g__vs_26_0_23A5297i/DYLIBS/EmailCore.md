## EmailCore

> `/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore`

```diff

-3858.100.10.2.1
-  __TEXT.__text: 0x53978
+3860.100.5.2.1
+  __TEXT.__text: 0x540fc
   __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x4e38
+  __TEXT.__objc_methlist: 0x4ed8
   __TEXT.__const: 0xe70
-  __TEXT.__gcc_except_tab: 0x6dc0
-  __TEXT.__cstring: 0x7c54
+  __TEXT.__gcc_except_tab: 0x6dd8
+  __TEXT.__cstring: 0x7cc4
   __TEXT.__oslogstring: 0xcd8
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x52
   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x2788
-  __TEXT.__objc_classname: 0xcc0
-  __TEXT.__objc_methname: 0xabcb
-  __TEXT.__objc_methtype: 0x16b7
-  __TEXT.__objc_stubs: 0x7460
+  __TEXT.__unwind_info: 0x27c0
+  __TEXT.__objc_classname: 0xce4
+  __TEXT.__objc_methname: 0xad83
+  __TEXT.__objc_methtype: 0x1706
+  __TEXT.__objc_stubs: 0x7600
   __DATA_CONST.__got: 0x6a0
   __DATA_CONST.__const: 0x21e0
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28f0
+  __DATA_CONST.__objc_selrefs: 0x2958
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0x830
   __AUTH_CONST.__const: 0x6f8
-  __AUTH_CONST.__cfstring: 0x51e0
-  __AUTH_CONST.__objc_const: 0x9bb8
+  __AUTH_CONST.__cfstring: 0x5280
+  __AUTH_CONST.__objc_const: 0x9c58
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH.__objc_data: 0x1b0
   __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x49c
+  __DATA.__objc_ivar: 0x4a4
   __DATA.__data: 0xd44
-  __DATA.__bss: 0x380
+  __DATA.__bss: 0x3a0
   __DATA.__common: 0x24
   __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__data: 0xb50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7C55A14E-F2CA-35BC-9AD5-B652ABC868AD
-  Functions: 1895
-  Symbols:   7496
-  CStrings:  4421
+  UUID: F8EC0ADA-4D63-3EDF-BEFB-92F164279366
+  Functions: 1911
+  Symbols:   7547
+  CStrings:  4451
 
Symbols:
+ +[NSRegularExpression(ECMessageBodyParserPriceExpressions) ec_copyCurrencyRegularExpressionForType:]
+ +[NSRegularExpression(ECMessageBodyParserPriceExpressions) ec_copyCurrencyRegularExpressionForType:].cold.1
+ +[NSRegularExpression(ECMessageBodyParserPriceExpressions) ec_priceBeginningExpression]
+ +[NSRegularExpression(ECMessageBodyParserPriceExpressions) ec_priceEndExpression]
+ -[ECMessageBodyParser currencyFormatter]
+ -[ECMessageBodyParser setCurrencyFormatter:]
+ -[ECMessageBodyStringAccumulator appendCurrencyDecimalSeparator]
+ -[ECMessageBodyStringAccumulator currencyFormatter]
+ -[ECMessageBodyStringAccumulator initWithOptions:lengthLimit:currencyFormatter:]
+ -[NSString(ECMessageBodyParser) ec_isPotentialPriceBeginning]
+ -[NSString(ECMessageBodyParser) ec_isPotentialPriceEnd]
+ -[_ECParsedHTMLNode range]
+ -[_ECParsedHTMLTag needsPriceFormatting:tagName:]
+ _OBJC_IVAR_$_ECMessageBodyParser._currencyFormatter
+ _OBJC_IVAR_$_ECMessageBodyStringAccumulator._currencyFormatter
+ __OBJC_$_CLASS_METHODS_NSRegularExpression(ECMessageBodyParser|ECMessageBodyParserPriceExpressions|SubjectParser)
+ __OBJC_$_PROP_LIST_ECMessageBodyElement.249
+ __OBJC_$_PROP_LIST_ECMessageBodyStringAccumulator.182
+ ___81+[NSRegularExpression(ECMessageBodyParserPriceExpressions) ec_priceEndExpression]_block_invoke
+ ___87+[NSRegularExpression(ECMessageBodyParserPriceExpressions) ec_priceBeginningExpression]_block_invoke
+ ___block_literal_global.252
+ ___block_literal_global.279
+ _ec_priceBeginningExpression.onceToken
+ _ec_priceBeginningExpression.regex
+ _ec_priceEndExpression.onceToken
+ _ec_priceEndExpression.regex
+ _objc_msgSend$appendCurrencyDecimalSeparator
+ _objc_msgSend$currencyDecimalSeparator
+ _objc_msgSend$currencyFormatter
+ _objc_msgSend$ec_copyCurrencyRegularExpressionForType:
+ _objc_msgSend$ec_isPotentialPriceBeginning
+ _objc_msgSend$ec_isPotentialPriceEnd
+ _objc_msgSend$ec_priceBeginningExpression
+ _objc_msgSend$ec_priceEndExpression
+ _objc_msgSend$ef_isCurrencySymbolAtStart
+ _objc_msgSend$hasChildNodes
+ _objc_msgSend$initWithOptions:lengthLimit:currencyFormatter:
+ _objc_msgSend$needsPriceFormatting:tagName:
+ _objc_msgSend$range
- __OBJC_$_CLASS_METHODS_NSRegularExpression(ECMessageBodyParser|SubjectParser)
- __OBJC_$_CLASS_PROP_LIST_NSRegularExpression_$_ECMessageBodyParser
- __OBJC_$_PROP_LIST_ECMessageBodyElement.241
- __OBJC_$_PROP_LIST_ECMessageBodyStringAccumulator.173
- ___block_literal_global.244
- ___block_literal_global.250
- ___block_literal_global.271
CStrings:
+ "(?:%@) *(?:\\d{1,3}(?:(?: *\\d{3})*|(?:, *\\d{3})*|(?:\\. *\\d{3})*))?$"
+ "@\"NSNumberFormatter\""
+ "@\"NSNumberFormatter\"16@0:8"
+ "@40@0:8Q16Q24@32"
+ "B32@0:8@16@24"
+ "Currency Symbols"
+ "CurrencyPatterns"
+ "ECMessageBodyParserPriceExpressions"
+ "T@\"NSNumberFormatter\",&,N,V_currencyFormatter"
+ "T@\"NSNumberFormatter\",R,N"
+ "^[0-9]{2}$"
+ "_currencyFormatter"
+ "appendCurrencyDecimalSeparator"
+ "currencyDecimalSeparator"
+ "currencyFormatter"
+ "ec_copyCurrencyRegularExpressionForType:"
+ "ec_isPotentialPriceBeginning"
+ "ec_isPotentialPriceEnd"
+ "ec_priceBeginningExpression"
+ "ec_priceEndExpression"
+ "ef_isCurrencySymbolAtStart"
+ "initWithOptions:lengthLimit:currencyFormatter:"
+ "needsPriceFormatting:tagName:"
+ "range"
+ "setCurrencyFormatter:"

```
