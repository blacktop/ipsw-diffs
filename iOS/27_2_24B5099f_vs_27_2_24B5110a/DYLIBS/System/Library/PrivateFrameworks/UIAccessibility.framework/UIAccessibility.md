## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3245.8.4.2.0
-  __TEXT.__text: 0x6b16c
-  __TEXT.__objc_methlist: 0x6c2c
-  __TEXT.__const: 0x278
+3245.8.9.0.0
+  __TEXT.__text: 0x6b468
+  __TEXT.__objc_methlist: 0x6c54
+  __TEXT.__const: 0x288
   __TEXT.__dlopen_cstrs: 0x266
   __TEXT.__gcc_except_tab: 0xdb8
   __TEXT.__cstring: 0x716a
-  __TEXT.__oslogstring: 0x2d31
+  __TEXT.__oslogstring: 0x2dc5
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x2020
+  __TEXT.__unwind_info: 0x2028
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15a0
+  __DATA_CONST.__const: 0x15c8
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5770
+  __DATA_CONST.__objc_selrefs: 0x5788
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2627
-  Symbols:   4592
-  CStrings:  1189
+  Functions: 2631
+  Symbols:   4597
+  CStrings:  1191
 
Symbols:
+ -[NSObject(AXAutoscrolling) _accessibilityShouldRetryScrollToBottom]
+ -[UIAccessibilityAutoscrollManager _bottomContentOffset]
+ -[UIAccessibilityAutoscrollManager _scrollToBottomWithRetriesRemaining:]
+ GCC_except_table1877
+ GCC_except_table1939
+ GCC_except_table1994
+ GCC_except_table2012
+ GCC_except_table2166
+ GCC_except_table2213
+ GCC_except_table2219
+ GCC_except_table2228
+ GCC_except_table2445
+ GCC_except_table2464
+ GCC_except_table2554
+ GCC_except_table2565
+ ___72-[UIAccessibilityAutoscrollManager _scrollToBottomWithRetriesRemaining:]_block_invoke
+ ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
- GCC_except_table1876
- GCC_except_table1938
- GCC_except_table1993
- GCC_except_table2011
- GCC_except_table2165
- GCC_except_table2212
- GCC_except_table2218
- GCC_except_table2226
- GCC_except_table2441
- GCC_except_table2460
- GCC_except_table2550
- GCC_except_table2561
CStrings:
+ "cannot scroll to bottom, no autoscroll target was set"
+ "scrolling to bottom %{public}@ from %{public}@, content size %{public}@, %ld retries left: %@"
```
