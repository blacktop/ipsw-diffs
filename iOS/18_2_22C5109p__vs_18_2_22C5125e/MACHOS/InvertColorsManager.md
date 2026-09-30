## InvertColorsManager

> `/System/Library/AccessibilityBundles/InvertColorsManager.bundle/InvertColorsManager`

```diff

-3148.6.2.0.0
-  __TEXT.__text: 0x1fae0
+3148.7.3.0.0
+  __TEXT.__text: 0x1fac0
   __TEXT.__auth_stubs: 0x720
   __TEXT.__objc_stubs: 0x26e0
   __TEXT.__objc_methlist: 0x769c
   __TEXT.__const: 0xa8
   __TEXT.__objc_classname: 0xa3d8
-  __TEXT.__cstring: 0x8d9c
+  __TEXT.__cstring: 0x8dc6
   __TEXT.__objc_methname: 0x2b79
   __TEXT.__objc_methtype: 0x306
   __TEXT.__gcc_except_tab: 0x1b4
CStrings:
+ "function removeFilter() { Array.prototype.forEach.call(document.querySelectorAll('img, picture, video'), function (img) { if (img.style.filter == 'invert(100%!)(MISSING)') {img.style.filter = 'invert(0%!)(MISSING)';} }) }removeFilter();"
- "function removeFilter() { Array.prototype.forEach.call(document.querySelectorAll('img, picture, video'), function (img) { img.style.filter = 'invert(0%!)(MISSING)'; }) }removeFilter();"

```
