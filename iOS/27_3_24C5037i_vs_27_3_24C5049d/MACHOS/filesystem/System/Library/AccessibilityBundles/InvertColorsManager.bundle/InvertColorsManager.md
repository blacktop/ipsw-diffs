## InvertColorsManager

> `/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-3245.8.14.0.0
-  __TEXT.__text: 0x2140c
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_stubs: 0x2a80
-  __TEXT.__objc_methlist: 0x78ac
-  __TEXT.__const: 0xe0
+3245.8.23.0.0
+  __TEXT.__text: 0x2184c
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_stubs: 0x2b20
+  __TEXT.__objc_methlist: 0x7924
+  __TEXT.__const: 0xe8
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__gcc_except_tab: 0x200
-  __TEXT.__objc_classname: 0xa34e
-  __TEXT.__cstring: 0x8faf
-  __TEXT.__objc_methname: 0x2e98
+  __TEXT.__objc_classname: 0xa3a8
+  __TEXT.__cstring: 0x94cc
+  __TEXT.__objc_methname: 0x2f43
   __TEXT.__objc_methtype: 0x357
-  __TEXT.__oslogstring: 0xfa9
-  __TEXT.__unwind_info: 0x1238
+  __TEXT.__oslogstring: 0x102c
+  __TEXT.__unwind_info: 0x1258
   __DATA_CONST.__const: 0x930
-  __DATA_CONST.__cfstring: 0x9040
-  __DATA_CONST.__objc_classlist: 0x1ae8
+  __DATA_CONST.__cfstring: 0x90c0
+  __DATA_CONST.__objc_classlist: 0x1af8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x618
+  __DATA_CONST.__objc_superrefs: 0x620
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0x1a0
-  __DATA.__objc_const: 0x21948
-  __DATA.__objc_selrefs: 0xeb0
-  __DATA.__objc_data: 0x10d10
+  __DATA.__objc_const: 0x21a68
+  __DATA.__objc_selrefs: 0xee0
+  __DATA.__objc_data: 0x10db0
   __DATA.__data: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1945
-  Symbols:   1915
-  CStrings:  2196
+  Functions: 1954
+  Symbols:   1918
+  CStrings:  2207
 
Symbols:
+ _OBJC_CLASS_$_WKWebViewLegacyInvertColorsAccessibility
+ _OBJC_CLASS_$___WKWebViewLegacyInvertColorsAccessibility_super
+ _OBJC_METACLASS_$_WKWebViewLegacyInvertColorsAccessibility
+ _OBJC_METACLASS_$___WKWebViewLegacyInvertColorsAccessibility_super
- _AXInvertColorsDarkModeDetectionJavascript
CStrings:
+ "WKWebView %p effective page appearance: %ld, inverted: %d"
+ "WKWebViewLegacyInvertColorsAccessibility"
+ "WebKit lacks content inversion SPI, using legacy WKWebView invert colors"
+ "__WKWebViewLegacyInvertColorsAccessibility_super"
+ "_accessibilityPageIsLight"
+ "_effectivePageAppearance"
+ "_setContentInversionForAccessibility:"
+ "_webKitSupportsContentInversion"
+ "didChangeValueForKey:"
+ "function luminance(color) {  if (color.length == 4 && color[3] == 0) { return 1; } for (var k = 0; k < 3; k++) { var adjusted = 0;  var value = color[k] / 255;  if (value < 0.03928) {        value = value / 12.92;    } else {        value = (value + .055) / 1.055;        value = Math.pow(value, 2.4); } color[k] = value;   } return (color[0] * .2126) + (color[1] * .7152) + (color[2] * .0722); }\nfunction dm() { var supportedSchemes = document.head.querySelector(\"meta[name='supported-color-schemes']\");\nvar supportedSchemesDM = (supportedSchemes && supportedSchemes.content && supportedSchemes.content.includes('dark'));\nvar colorSchemes = document.head.querySelector(\"meta[name='color-scheme']\");\nvar colorSchemesDM = (supportedSchemes && supportedSchemes.content && supportedSchemes.content.includes('dark'));\nvar classListDM = document.documentElement.classList.contains('apple-mail-implicit-dark-support');\nvar bgColor = document.body && window.getComputedStyle(document.body).getPropertyValue('background-color');\nbgColor = bgColor.replace(/[^\\d,]/g, '').split(',');\nvar luma = bgColor ? luminance(bgColor) : .99;\nreturn (supportedSchemesDM || colorSchemesDM || classListDM || (luma < .3)) }\ndm();"
+ "instancesRespondToSelector:"
```
