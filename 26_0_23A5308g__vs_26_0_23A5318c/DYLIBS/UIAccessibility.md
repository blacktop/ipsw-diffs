## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3189.2.0.0.0
-  __TEXT.__text: 0x65fc4
+3190.5.0.0.0
+  __TEXT.__text: 0x661e0
   __TEXT.__auth_stubs: 0x15a0
-  __TEXT.__objc_methlist: 0x6a14
+  __TEXT.__objc_methlist: 0x6a1c
   __TEXT.__const: 0x2d0
   __TEXT.__cstring: 0x6d01
   __TEXT.__oslogstring: 0x2c1e
   __TEXT.__gcc_except_tab: 0xdd4
   __TEXT.__dlopen_cstrs: 0x266
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1bd0
+  __TEXT.__unwind_info: 0x1bd8
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x16e4a
+  __TEXT.__objc_methname: 0x16e9d
   __TEXT.__objc_methtype: 0x1f0a
-  __TEXT.__objc_stubs: 0x10860
+  __TEXT.__objc_stubs: 0x108e0
   __DATA_CONST.__got: 0xd08
-  __DATA_CONST.__const: 0x15d0
+  __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5560
+  __DATA_CONST.__objc_selrefs: 0x5580
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 567ABADF-01DF-342E-A65F-A0ED6D258B33
-  Functions: 2754
-  Symbols:   9617
-  CStrings:  5332
+  UUID: 26CBD27E-F107-3350-A180-C2AD56733C38
+  Functions: 2756
+  Symbols:   9626
+  CStrings:  5336
 
Symbols:
+ -[NSObject(UIAccessibilityElementTraversal) _accessibilityActiveScenes]
+ GCC_except_table106
+ ___106-[NSObject(UIAccessibilityElementTraversal) _accessibilityEnumerateSiblingsWithParent:options:usingBlock:]_block_invoke.488
+ ___block_descriptor_56_e8_32s40s48s_e15_v32?08Q16^B24ls32l8s40l8s48l8
+ ___block_literal_global.497
+ ___block_literal_global.508
+ ___block_literal_global.546
+ ___block_literal_global.548
+ _objc_msgSend$_accessibilityActiveScenes
+ _objc_msgSend$_isCarInstrumentsScreen
+ _objc_msgSend$_keyWindowScene
+ _objc_msgSend$connectedScenes
- GCC_except_table104
- ___block_literal_global.495
- ___block_literal_global.506
- ___block_literal_global.543
- ___block_literal_global.545
- ___block_literal_global.557
Functions:
~ -[NSObject(UIAccessibilityElementTraversal) _accessibilityEnumerateSiblingsWithParent:options:usingBlock:] : 2068 -> 2416
~ ___106-[NSObject(UIAccessibilityElementTraversal) _accessibilityEnumerateSiblingsWithParent:options:usingBlock:]_block_invoke : 16 -> 120
+ ___106-[NSObject(UIAccessibilityElementTraversal) _accessibilityEnumerateSiblingsWithParent:options:usingBlock:]_block_invoke.488
+ -[NSObject(UIAccessibilityElementTraversal) _accessibilityViewChildrenWithOptions:]
~ -[UIWindowScene(UIAccessibilityElementTraversal) _accessibilityViewChildrenWithOptions:] : 768 -> 812
~ -[NSObject(AXPrivCategory) _accessibilityIsStarkElement] : 200 -> 220
CStrings:
+ "_accessibilityActiveScenes"
+ "_isCarInstrumentsScreen"
+ "_keyWindowScene"
+ "connectedScenes"

```
