## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3137.22.0.0.0
-  __TEXT.__text: 0x63a58
+3148.6.2.0.0
+  __TEXT.__text: 0x652f4
   __TEXT.__auth_stubs: 0x1570
-  __TEXT.__objc_methlist: 0x5f94
+  __TEXT.__objc_methlist: 0x5fc4
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x6ac9
-  __TEXT.__oslogstring: 0x2b3b
-  __TEXT.__gcc_except_tab: 0xd90
+  __TEXT.__cstring: 0x6c56
+  __TEXT.__oslogstring: 0x2bbe
+  __TEXT.__gcc_except_tab: 0xda0
   __TEXT.__dlopen_cstrs: 0x266
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1ac0
+  __TEXT.__unwind_info: 0x1b20
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x16644
+  __TEXT.__objc_methname: 0x16a5f
   __TEXT.__objc_methtype: 0x1e56
-  __TEXT.__objc_stubs: 0x10120
-  __DATA_CONST.__got: 0xc70
+  __TEXT.__objc_stubs: 0x105e0
+  __DATA_CONST.__got: 0xcf8
   __DATA_CONST.__const: 0x1588
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f80
+  __DATA_CONST.__objc_selrefs: 0x50b8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0xac8
   __AUTH_CONST.__const: 0x11a8
-  __AUTH_CONST.__cfstring: 0x5e60
+  __AUTH_CONST.__cfstring: 0x6200
   __AUTH_CONST.__objc_const: 0x5998
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_dictobj: 0x78

   __AUTH.__objc_data: 0xe60
   __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x748
-  __DATA.__bss: 0x4c0
+  __DATA.__bss: 0x4d8
   __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x208
   __DATA_DIRTY.__common: 0x234
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
+  - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreText.framework/CoreText

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2687
-  Symbols:   3678
-  CStrings:  4441
+  Functions: 2693
+  Symbols:   3701
+  CStrings:  4513
 
Symbols:
+ _OBJC_CLASS_$_AXMathExpression
+ _OBJC_CLASS_$_AXMathExpressionFenced
+ _OBJC_CLASS_$_AXMathExpressionFraction
+ _OBJC_CLASS_$_AXMathExpressionIdentifier
+ _OBJC_CLASS_$_AXMathExpressionMultiscript
+ _OBJC_CLASS_$_AXMathExpressionNumber
+ _OBJC_CLASS_$_AXMathExpressionOperator
+ _OBJC_CLASS_$_AXMathExpressionRoot
+ _OBJC_CLASS_$_AXMathExpressionRow
+ _OBJC_CLASS_$_AXMathExpressionSubSuperscript
+ _OBJC_CLASS_$_AXMathExpressionTable
+ _OBJC_CLASS_$_AXMathExpressionTableCell
+ _OBJC_CLASS_$_AXMathExpressionTableRow
+ _OBJC_CLASS_$_AXMathExpressionText
+ _OBJC_CLASS_$_AXMathExpressionUnderOver
+ _OBJC_CLASS_$_BEAccessibilityTextMarker
+ _OBJC_CLASS_$_BEAccessibilityTextMarkerRange
+ __beaxRangeToArray
+ __beaxTextMarkerRangeForArray
CStrings:
+ "AXMBaseObject"
+ "AXMChildren"
+ "AXMCloseOperator"
+ "AXMContent"
+ "AXMDenominatorObject"
+ "AXMMultiscriptPostscripts"
+ "AXMMultiscriptPrescripts"
+ "AXMNumeratorObject"
+ "AXMOpenOperator"
+ "AXMOverObject"
+ "AXMRadicandObject"
+ "AXMRootIndexObject"
+ "AXMType"
+ "AXMUnderObject"
+ "AXMUnichar"
+ "Could not deserialize end marker: %!@(MISSING)"
+ "Could not deserialize start marker: %!@(MISSING)"
+ "Fenced"
+ "Fraction"
+ "Identifier"
+ "Multiscript"
+ "Number"
+ "Operator"
+ "RootOperation"
+ "Row"
+ "SubSuperScript"
+ "Table"
+ "TableCell"
+ "TableRow"
+ "UnderOver"
+ "Window has alpha <= 0: %!@(MISSING)"
+ "Window has hidden = true: %!@(MISSING)"
+ "_accessibilityConvertMathExpression:"
+ "_accessibilityProcessMathExpression:"
+ "_processMathChildrenExpressions:"
+ "_processMathMultiscriptExpressions:"
+ "accessibilityBoundsForTextMarkerRange:"
+ "accessibilityContentForTextMarkerRange:"
+ "accessibilityLineEndMarkerForMarker:"
+ "accessibilityLineEndPositionFromCurrentSelection"
+ "accessibilityLineRangeForPosition:"
+ "accessibilityLineStartMarkerForMarker:"
+ "accessibilityLineStartPositionFromCurrentSelection"
+ "accessibilityMarkerForPoint:"
+ "accessibilityMathExpression"
+ "accessibilityNextTextMarker:"
+ "accessibilityPreviousTextMarker:"
+ "accessibilityRangeForTextMarkerRange:"
+ "accessibilityTextMarkerForPosition:"
+ "accessibilityTextMarkerRange"
+ "accessibilityTextMarkerRangeForCurrentSelection"
+ "accessibilityTextMarkerRangeForRange:"
+ "baseExpression"
+ "closeString"
+ "content"
+ "denimonatorExpression"
+ "endMarker"
+ "expressions"
+ "numeratorExpression"
+ "openString"
+ "overExpression"
+ "postscriptExpressions"
+ "prescriptExpressions"
+ "radicandExpressions"
+ "rootIndexExpression"
+ "setEndMarker:"
+ "setStartMarker:"
+ "startMarker"
+ "subscriptExpressions"
+ "superscriptExpressions"
+ "underExpression"

```
