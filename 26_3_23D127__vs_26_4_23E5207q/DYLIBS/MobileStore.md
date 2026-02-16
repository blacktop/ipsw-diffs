## MobileStore

> `/System/Library/AccessibilityBundles/MobileStore.axbundle/MobileStore`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x10f4
-  __TEXT.__auth_stubs: 0x1a0
+3005.16.0.0.0
+  __TEXT.__text: 0x11a8
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0x28c
   __TEXT.__cstring: 0x4c4
   __TEXT.__unwind_info: 0xd0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1b8
-  __AUTH_CONST.__auth_got: 0xd8
+  __AUTH_CONST.__auth_got: 0xc8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x740
   __AUTH_CONST.__objc_const: 0xa60

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CD5607B8-ABD6-37A7-8EC7-FE31C6B794D2
+  UUID: 2ED15EF9-FEDB-3E88-B4B6-7BB426FFFB9B
   Functions: 45
-  Symbols:   280
+  Symbols:   278
   CStrings:  209
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x20
Functions:
~ +[AXMobileStoreGlue accessibilityInitializeBundle] : 148 -> 152
~ ___50+[AXMobileStoreGlue accessibilityInitializeBundle]_block_invoke : 708 -> 712
~ ___50+[AXMobileStoreGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___50+[AXMobileStoreGlue accessibilityInitializeBundle]_block_invoke_3 : 172 -> 180
~ -[MSAlbumPropertiesViewAccessibility accessibilityLabel] : 280 -> 316
~ -[MSTrackCellContentsAccessibility accessibilityLabel] : 308 -> 340
~ -[MSTrackAccessibilityElement accessibilityFrame] : 96 -> 100
~ -[MSTrackListHeaderViewAccessibility accessibilityLabel] : 312 -> 340
~ -[MSTrackListHeaderViewAccessibility _accessibilityChildren] : 308 -> 320
~ -[MSTrackListHeaderViewAccessibility _accessibilityHitTest:withEvent:] : 376 -> 388
~ -[MSTrackListHeaderViewAccessibility accessibilityElementCount] : 56 -> 60
~ -[MSTrackListHeaderViewAccessibility accessibilityElementAtIndex:] : 84 -> 92
~ -[MSTrackListHeaderViewAccessibility indexOfAccessibilityElement:] : 88 -> 92
~ _accessibilityLocalizedString : 156 -> 164
~ _starStringForStarCount : 208 -> 220

```
