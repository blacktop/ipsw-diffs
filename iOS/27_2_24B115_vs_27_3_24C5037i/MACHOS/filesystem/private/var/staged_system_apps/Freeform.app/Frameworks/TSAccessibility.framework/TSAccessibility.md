## TSAccessibility

> `/private/var/staged_system_apps/Freeform.app/Frameworks/TSAccessibility.framework/TSAccessibility`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-656.40.9.0.2
-  __TEXT.__text: 0xc624
+656.60.5.0.0
+  __TEXT.__text: 0xc644
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_stubs: 0x2260
-  __TEXT.__objc_methlist: 0x11e4
+  __TEXT.__objc_stubs: 0x22a0
+  __TEXT.__objc_methlist: 0x11ec
   __TEXT.__const: 0x30
+  __TEXT.__cstring: 0x4356
   __TEXT.__objc_classname: 0x863
-  __TEXT.__objc_methname: 0x2a77
+  __TEXT.__objc_methname: 0x2ac7
   __TEXT.__objc_methtype: 0x4b5
-  __TEXT.__cstring: 0x43ab
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__unwind_info: 0x558
-  __DATA_CONST.__const: 0x4b8
-  __DATA_CONST.__cfstring: 0x41c0
+  __DATA_CONST.__const: 0x4c0
+  __DATA_CONST.__cfstring: 0x4180
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x390
-  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__got: 0x178
   __DATA.__objc_const: 0x1e58
-  __DATA.__objc_selrefs: 0xc20
+  __DATA.__objc_selrefs: 0xc38
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x2c8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 407
-  Symbols:   1239
-  CStrings:  1101
+  Functions: 408
+  Symbols:   1244
+  CStrings:  1102
 
Symbols:
+ -[TSAccessibility loadAccessibilitySupportIfAutoLoadDefaultIsSet]
+ _OBJC_CLASS_$_NSUserDefaults
+ _TSAXAutoLoadAccessibilityUserDefault
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$standardUserDefaults
Functions:
~ -[TSAccessibility addSafeCategoryNamesToCollection:] : 3688 -> 3672
+ -[TSAccessibility loadAccessibilitySupportIfAutoLoadDefaultIsSet]
~ -[TSAccessibility(iOS) addExtraSafeCategoryNamesToCollection:] : 1680 -> 1648
CStrings:
+ "TSAXAutoLoadAccessibility"
+ "boolForKey:"
+ "loadAccessibilitySupportIfAutoLoadDefaultIsSet"
+ "standardUserDefaults"
- "TSDSwatchGridViewAccessibility"
- "TSTCellEditingToolbarViewAccessibility"
- "TSTFloatingDisclosureButtonAccessibility"
```
