## NanoTimeKitCompanion

> `/System/Library/AccessibilityBundles/NanoTimeKitCompanion.axbundle/NanoTimeKitCompanion`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-1035.0.0.0.0
-  __TEXT.__text: 0x11ea8
-  __TEXT.__auth_stubs: 0x640
+1038.0.0.0.0
+  __TEXT.__text: 0x12054
+  __TEXT.__auth_stubs: 0x680
   __TEXT.__objc_stubs: 0x2060
   __TEXT.__objc_methlist: 0x1ebc
-  __TEXT.__const: 0x48
+  __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x48c
   __TEXT.__objc_classname: 0x18a0
   __TEXT.__cstring: 0x37b9
   __TEXT.__objc_methname: 0x2785
   __TEXT.__objc_methtype: 0x220
+  __TEXT.__oslogstring: 0xdf
   __TEXT.__unwind_info: 0x750
   __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__cfstring: 0x4140

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__auth_got: 0x350
   __DATA_CONST.__got: 0x1d0
   __DATA.__objc_const: 0x5198
   __DATA.__objc_selrefs: 0xb30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 639
-  Symbols:   1840
-  CStrings:  968
+  Symbols:   1844
+  CStrings:  970
 
Symbols:
+ _AXAIWhiteGloveLoggingEnabled
+ _AXLogCommon
+ __os_log_impl
+ _os_log_type_enabled
Functions:
~ -[NTKCFaceDetailSectionHeaderViewAccessibility isAccessibilityElement] : 8 -> 288
~ -[NTKCFaceDetailSectionHeaderViewAccessibility accessibilityLabel] : 148 -> 296
CStrings:
+ "rdar://166127771 NTKCFaceDetailSectionHeaderView accessibilityLabel titleLen=%lu subtitleLen=%lu labelLen=%lu"
+ "rdar://166127771 NTKCFaceDetailSectionHeaderView isAccessibilityElement titleLen=%lu subtitleLen=%lu hasLabel=%d"
```
