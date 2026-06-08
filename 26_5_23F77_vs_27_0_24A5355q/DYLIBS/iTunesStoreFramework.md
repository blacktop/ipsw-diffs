## iTunesStoreFramework

> `/System/Library/AccessibilityBundles/iTunesStoreFramework.axbundle/iTunesStoreFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x318
-  __TEXT.__auth_stubs: 0xa0
+3036.2.0.0.0
+  __TEXT.__text: 0x300
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x1db
   __TEXT.__unwind_info: 0x60
-  __TEXT.__objc_classname: 0x12
-  __TEXT.__objc_methname: 0xf2
-  __TEXT.__objc_methtype: 0x13
-  __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x58
+  __DATA_CONST.__got: 0x28
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B98D5645-EE9A-3988-A454-CC1C6616FF64
+  UUID: B5F56360-15CD-3C24-BE4D-D4F3FA244A25
   Functions: 4
   Symbols:   44
-  CStrings:  40
+  CStrings:  26
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ _accessibilityLocalizedString : 164 -> 156
~ +[AXiTunesStoreGlue accessibilityInitializeBundle] : 148 -> 144
~ -[AXiTunesStoreGlue _libraryWeakLoaded:] : 324 -> 316
~ ___40-[AXiTunesStoreGlue _libraryWeakLoaded:]_block_invoke : 156 -> 152
CStrings:
- "AXiTunesStoreGlue"
- "_libraryWeakLoaded:"
- "accessibilityInitializeBundle"
- "addObserver:selector:name:object:"
- "bundleWithIdentifier:"
- "defaultCenter"
- "init"
- "intValue"
- "loadAccessibilityBundleForBundle:didLoadCallback:"
- "localizedStringForKey:value:table:"
- "objectForKey:"
- "userInfo"
- "v16@0:8"
- "v24@0:8@16"

```
