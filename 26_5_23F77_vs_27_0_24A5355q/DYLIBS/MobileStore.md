## MobileStore

> `/System/Library/AccessibilityBundles/MobileStore.axbundle/MobileStore`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x11a8
-  __TEXT.__auth_stubs: 0x180
+3036.2.0.0.0
+  __TEXT.__text: 0x10f0
   __TEXT.__objc_methlist: 0x28c
   __TEXT.__cstring: 0x4c4
   __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0x2d9
-  __TEXT.__objc_methname: 0x555
-  __TEXT.__objc_methtype: 0x86
-  __TEXT.__objc_stubs: 0x5a0
-  __DATA_CONST.__got: 0x78
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1b8
-  __AUTH_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x740
   __AUTH_CONST.__objc_const: 0xa60
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x5a0
   __DATA.__common: 0x8
   __DATA.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D490B037-71FB-3AAE-9936-A9D797B21A13
+  UUID: 1DAAF153-28C8-3EA2-8831-3BD7712711B6
   Functions: 45
-  Symbols:   278
-  CStrings:  209
+  Symbols:   280
+  CStrings:  124
 
Symbols:
+ ___block_literal_global.439
+ ___block_literal_global.448
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x20
- ___block_literal_global.418
- ___block_literal_global.427
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXMobileStoreGlue accessibilityInitializeBundle] : 152 -> 148
~ ___50+[AXMobileStoreGlue accessibilityInitializeBundle]_block_invoke : 712 -> 708
~ ___50+[AXMobileStoreGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___50+[AXMobileStoreGlue accessibilityInitializeBundle]_block_invoke_3 : 180 -> 172
~ -[MSAlbumPropertiesViewAccessibility accessibilityLabel] : 316 -> 280
~ -[MSTrackCellContentsAccessibility accessibilityLabel] : 340 -> 308
~ -[MSTrackListCellConfigurationAccessibility accessibilityLabel] : 552 -> 548
~ -[MSTrackAccessibilityElement accessibilityFrame] : 100 -> 96
~ -[MSTrackListHeaderViewAccessibility accessibilityLabel] : 340 -> 312
~ -[MSTrackListHeaderViewAccessibility _accessibilityChildren] : 320 -> 308
~ -[MSTrackListHeaderViewAccessibility _accessibilityHitTest:withEvent:] : 388 -> 380
~ -[MSTrackListHeaderViewAccessibility accessibilityElementCount] : 60 -> 56
~ -[MSTrackListHeaderViewAccessibility accessibilityElementAtIndex:] : 92 -> 84
~ -[MSTrackListHeaderViewAccessibility indexOfAccessibilityElement:] : 92 -> 88
~ _accessibilityLocalizedString : 164 -> 156
~ _starStringForStarCount : 220 -> 204
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@24@0:8q16"
- "@40@0:8{CGPoint=dd}16@32"
- "AXMobileStoreGlue"
- "AXPrivate"
- "B16@0:8"
- "MSAlbumPropertiesViewAccessibility"
- "MSTrackAccessibilityElement"
- "MSTrackCellContentsAccessibility"
- "Q16@0:8"
- "SafeCategory"
- "__MSAlbumPropertiesViewAccessibility_super"
- "__MSTableCellAccessibility_super"
- "__MSTrackCellContentsAccessibility_super"
- "__MSTrackListCellConfigurationAccessibility_super"
- "__MSTrackListCopyrightFooterViewAccessibility_super"
- "__MSTrackListHeaderViewAccessibility_super"
- "__MSTrackListLinkCellConfigurationAccessibility_super"
- "__UIMobileStoreApplicationAccessibility_super"
- "_accessibilityChildren"
- "_accessibilityHitTest:withEvent:"
- "_accessibilityReloadMediaStrings"
- "_accessibilitySetRetainedValue:forKey:"
- "_accessibilityValueForKey:"
- "_gsEvent"
- "accessibilityContainer"
- "accessibilityElementAtIndex:"
- "accessibilityElementCount"
- "accessibilityFrame"
- "accessibilityHint"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityLanguage"
- "accessibilityTraits"
- "addObject:"
- "allObjects"
- "appendFormat:"
- "axAttributedStringWithString:"
- "boolValue"
- "bundleWithIdentifier:"
- "bytes"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "indexOfAccessibilityElement:"
- "indexOfObject:"
- "init"
- "initWithAccessibilityContainer:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "length"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "mutableCopyWithZone:"
- "objectAtIndex:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "q24@0:8@16"
- "reloadStrings"
- "replaceOccurrencesOfString:withString:options:range:"
- "reverseObjectEnumerator"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setAccessibilityFrame:"
- "setAccessibilityLabel:"
- "setAccessibilityLanguage:"
- "setAttribute:forKey:withRange:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "string"
- "v16@0:8"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
