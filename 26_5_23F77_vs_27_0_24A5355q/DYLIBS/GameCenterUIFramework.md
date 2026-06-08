## GameCenterUIFramework

> `/System/Library/AccessibilityBundles/GameCenterUIFramework.axbundle/GameCenterUIFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x4560
-  __TEXT.__auth_stubs: 0x300
+3036.2.0.0.0
+  __TEXT.__text: 0x4bf8
   __TEXT.__objc_methlist: 0xb8c
-  __TEXT.__cstring: 0x114d
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x2b8
-  __TEXT.__objc_classname: 0x9e6
-  __TEXT.__objc_methname: 0xb00
-  __TEXT.__objc_methtype: 0xe6
-  __TEXT.__objc_stubs: 0x9a0
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__cstring: 0x114d
+  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x338
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__cfstring: 0x1400
   __AUTH_CONST.__objc_const: 0x2290
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x19
   __DATA_DIRTY.__objc_data: 0x1310
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0EC12D72-1AF5-3036-9591-A29A7F8612BA
-  Functions: 227
+  UUID: BCB16EB1-9270-3D47-8B8B-DD39735CE6E2
+  Functions: 225
   Symbols:   963
-  CStrings:  517
+  CStrings:  336
 
Symbols:
+ GCC_except_table145
+ ___block_literal_global.115
+ ___block_literal_global.175
+ ___block_literal_global.352
+ ___block_literal_global.361
+ ___block_literal_global.370
+ ___block_literal_global.378
+ ___block_literal_global.395
+ ___block_literal_global.401
+ ___block_literal_global.403
+ ___block_literal_global.405
+ ___block_literal_global.407
+ ___block_literal_global.431
+ ___block_literal_global.433
+ ___block_literal_global.585
+ ___block_literal_global.742
+ ___block_literal_global.818
+ ___block_literal_global.903
+ ___block_literal_global.946
+ ___block_literal_global.981
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x8
- +[AXGameCenterUIFrameworkGlue accessibilityInitializeBundle].cold.1
- GCC_except_table5
- _AXGameCenterUIFrameworkLocString.cold.1
- ___block_literal_global.331
- ___block_literal_global.340
- ___block_literal_global.349
- ___block_literal_global.357
- ___block_literal_global.363
- ___block_literal_global.365
- ___block_literal_global.374
- ___block_literal_global.380
- ___block_literal_global.382
- ___block_literal_global.410
- ___block_literal_global.412
- _objc_retain_x25
- _objc_retain_x28
Functions:
~ +[AchievementHighlightCollectionViewCellAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ +[PlayerProfileInfoBarViewAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[PlayerProfileInfoBarViewAccessibility accessibilityElements] : 384 -> 368
~ ___62-[PlayerProfileInfoBarViewAccessibility accessibilityElements]_block_invoke : 364 -> 356
~ ___62-[PlayerProfileInfoBarViewAccessibility accessibilityElements]_block_invoke_2 : 148 -> 136
~ +[BaseSmallFriendLockupViewAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ +[GKLeaderboardScoreCellAccessibility _accessibilityPerformValidations:] : 168 -> 156
~ +[GKDashboardMultiplayerPickerViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 116
~ -[GKDashboardMultiplayerPickerViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 108
~ ___101-[GKDashboardMultiplayerPickerViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 12 -> 168
~ +[UILabelAccessibility__GameCenterUI__UIKit _accessibilityPerformValidations:] : 132 -> 120
~ -[UILabelAccessibility__GameCenterUI__UIKit isAccessibilityElement] : 128 -> 124
~ _AXGameCenterUIFrameworkLocString : 140 -> 152
~ ___AXGameCenterUIFrameworkLocString_block_invoke : 144 -> 132
~ +[AchievementCardAccessibility _accessibilityPerformValidations:] : 336 -> 324
~ -[AchievementCardAccessibility accessibilityLabel] : 768 -> 992
~ -[CloseButtonAccessibility accessibilityLabel] : 12 -> 168
~ +[GKLeaderboardMetadataViewAccessibility _accessibilityPerformValidations:] : 168 -> 156
~ -[GKLeaderboardMetadataViewAccessibility accessibilityLabel] : 224 -> 212
~ -[GKDashboardPlayerPhotoViewAccessibility accessibilityLabel] : 12 -> 168
~ +[SmallLockupViewAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ +[GKLeaderboardCellAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ +[SmallPlayerCardViewAccessibility _accessibilityPerformValidations:] : 196 -> 184
~ -[SmallPlayerCardViewAccessibility _accessibilitySupplementaryFooterViews] : 320 -> 392
~ -[GKGameCenterViewController(AXGameCenter) __axValueForKey:] : 80 -> 76
~ +[GKDashboardPlayerCellAccessibility _accessibilityPerformValidations:] : 248 -> 236
~ -[GKDashboardPlayerCellAccessibility accessibilityLabel] : 152 -> 148
~ -[GKUILabelAccessibility isAccessibilityElement] : 224 -> 208
~ +[DetailCollectionViewCellAccessibility _accessibilityPerformValidations:] : 168 -> 156
~ -[DetailCollectionViewCellAccessibility _axSwitch] : 104 -> 88
~ -[DetailCollectionViewCellAccessibility accessibilityValue] : 148 -> 132
~ -[DetailCollectionViewCellAccessibility accessibilityActivationPoint] : 156 -> 148
~ -[DetailCollectionViewCellAccessibility accessibilityTraits] : 156 -> 148
~ +[AXGameCenterUIFrameworkGlue accessibilityInitializeBundle] : 44 -> 40
~ ___60+[AXGameCenterUIFrameworkGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___60+[AXGameCenterUIFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___60+[AXGameCenterUIFrameworkGlue accessibilityInitializeBundle]_block_invoke_4 : 660 -> 652
~ +[SectionFooterViewAccessibility _accessibilityPerformValidations:] : 208 -> 196
~ -[SectionFooterViewAccessibility accessibilityLabel] : 84 -> 76
~ -[SectionFooterViewAccessibility _accessibilityInternalTextLinks] : 464 -> 456
~ ___65-[SectionFooterViewAccessibility _accessibilityInternalTextLinks]_block_invoke : 220 -> 212
~ +[GKMultiplayerParticipantCollectionViewCellAccessibility _accessibilityPerformValidations:] : 184 -> 172
~ -[GKMultiplayerParticipantCollectionViewCellAccessibility accessibilityCustomActions] : 428 -> 508
~ +[GKChallengeDetailViewControllerAccessibility _accessibilityPerformValidations:] : 540 -> 532
~ -[GKChallengeDetailViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 816 -> 1104
~ ___90-[GKChallengeDetailViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 56 -> 8
~ ___90-[GKChallengeDetailViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_4 : 80 -> 76
~ -[GKChallengeDetailViewControllerAccessibility _axElementsOfView] : 892 -> 856
~ ___65-[GKChallengeDetailViewControllerAccessibility _axElementsOfView]_block_invoke : 176 -> 160
~ ___65-[GKChallengeDetailViewControllerAccessibility _axElementsOfView]_block_invoke_3 : 108 -> 100
~ +[NicknameFieldCollectionViewCellAccessibility _accessibilityPerformValidations:] : 176 -> 164
~ -[NicknameFieldCollectionViewCellAccessibility accessibilityLabel] : 84 -> 76
~ -[NicknameFieldCollectionViewCellAccessibility accessibilityValue] : 84 -> 76
~ -[NicknameFieldCollectionViewCellAccessibility _accessibilityLineNumberAndColumnForPoint:] : 108 -> 100
~ -[NicknameFieldCollectionViewCellAccessibility _accessibilityRangeForLineNumberAndColumn:] : 100 -> 96
~ -[NicknameFieldCollectionViewCellAccessibility _accessibilitySetSelectedTextRange:] : 92 -> 88
~ -[NicknameFieldCollectionViewCellAccessibility accessibilityTraits] : 124 -> 120
~ -[NicknameFieldCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 260 -> 244
~ +[ProfileAvatarViewAccessibility _accessibilityPerformValidations:] : 292 -> 284
~ -[ProfileAvatarViewAccessibility accessibilityLabel] : 232 -> 312
~ -[ProfileAvatarViewAccessibility accessibilityHint] : 124 -> 224
~ -[ProfileAvatarViewAccessibility automationElements] : 392 -> 368
~ ___52-[ProfileAvatarViewAccessibility automationElements]_block_invoke_2 : 12 -> 168
~ ___52-[ProfileAvatarViewAccessibility automationElements]_block_invoke_5 : 12 -> 168
~ +[GKMultiplayerStepperViewAccessibility _accessibilityPerformValidations:] : 212 -> 204
~ -[GKMultiplayerStepperViewAccessibility _accessibilityLoadAccessibilityInformation] : 188 -> 180
~ ___83-[GKMultiplayerStepperViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 12 -> 168
~ ___83-[GKMultiplayerStepperViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 12 -> 168
~ -[GKMultiplayerStepperViewAccessibility accessibilityUpdateStepperWithValue:] : 276 -> 368
~ -[GKMultiplayerStepperViewAccessibility accessibilityLabel] : 12 -> 168
~ +[GKDashboardSectionHeaderViewAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[GKDashboardSectionHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 108
~ +[PlayerProfileHeaderViewAccessibility _accessibilityPerformValidations:] : 148 -> 140
~ -[PlayerProfileHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 108
~ ___82-[PlayerProfileHeaderViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 12 -> 168
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8{CGPoint=dd}16"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "AXGameCenter"
- "AXGameCenterUIFrameworkGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__AchievementCardAccessibility_super"
- "__AchievementHighlightCollectionViewCellAccessibility_super"
- "__AchievementsLinkViewAccessibility_super"
- "__BaseSmallFriendLockupViewAccessibility_super"
- "__CloseButtonAccessibility_super"
- "__DetailCollectionViewCellAccessibility_super"
- "__GKButtonAccessibility_super"
- "__GKChallengeDetailViewControllerAccessibility_super"
- "__GKChallengeListViewSectionHeaderAccessibility_super"
- "__GKDashboardMultiplayerPickerViewControllerAccessibility_super"
- "__GKDashboardPlayerCellAccessibility_super"
- "__GKDashboardPlayerPhotoViewAccessibility_super"
- "__GKDashboardSectionHeaderViewAccessibility_super"
- "__GKGameCenterViewControllerAccessibility_super"
- "__GKLeaderboardCellAccessibility_super"
- "__GKLeaderboardMetadataViewAccessibility_super"
- "__GKLeaderboardScoreCellAccessibility_super"
- "__GKMultiplayerParticipantCollectionViewCellAccessibility_super"
- "__GKMultiplayerStatusViewAccessibility_super"
- "__GKMultiplayerStepperViewAccessibility_super"
- "__GKUILabelAccessibility_super"
- "__NicknameFieldCollectionViewCellAccessibility_super"
- "__PlayerProfileHeaderViewAccessibility_super"
- "__PlayerProfileInfoBarViewAccessibility_super"
- "__ProfileAvatarViewAccessibility_super"
- "__SectionFooterViewAccessibility_super"
- "__SectionHeaderViewAccessibility_super"
- "__SmallLockupViewAccessibility_super"
- "__SmallPlayerCardViewAccessibility_super"
- "__UILabelAccessibility__GameCenterUI__UIKit_super"
- "__axValueForKey:"
- "_accessibilityAncestorIsKindOf:"
- "_accessibilityAutomationType"
- "_accessibilityChallengeDetailElements"
- "_accessibilityCirclePathBasedOnBoundsWidth"
- "_accessibilityDescendantOfType:"
- "_accessibilityInfoViewElements"
- "_accessibilityInternalTextLinkCustomRotors"
- "_accessibilityInternalTextLinks"
- "_accessibilityLineNumberAndColumnForPoint:"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityRangeForLineNumberAndColumn:"
- "_accessibilitySetRetainedValue:forKey:"
- "_accessibilitySetSelectedTextRange:"
- "_accessibilityStringForLabelKeyValues:"
- "_accessibilitySupplementaryFooterViews"
- "_accessibilitySupportsHandwriting"
- "_accessibilityTextViewTextOperationResponder"
- "_accessibilityValueForKey:"
- "_accessibilityViewIsVisible"
- "_axAccessoryView"
- "_axElementsOfView"
- "_axFooterLabel"
- "_axIsEditable"
- "_axSwitch"
- "_setAccessibilityAdditionalTraitsBlock:"
- "_setAccessibilityChallengeDetailElements:"
- "_setAccessibilityElementsBlock:"
- "_setAccessibilityInfoViewElements:"
- "_setAccessibilityLabelBlock:"
- "_setAccessibilityPathBlock:"
- "_setAccessibilityTraitsBlock:"
- "_setIsAccessibilityElementBlock:"
- "accessibilityActivationPoint"
- "accessibilityContainerType"
- "accessibilityCustomActions"
- "accessibilityCustomRotors"
- "accessibilityElements"
- "accessibilityHint"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityPath"
- "accessibilityRespondsToUserInteraction"
- "accessibilityRowRange"
- "accessibilityTraits"
- "accessibilityValue"
- "array"
- "arrayWithObjects:count:"
- "automationElements"
- "axArrayByIgnoringNilElementsWithCount:"
- "axAttributedStringWithString:"
- "axSafelyAddObject:"
- "axSafelyAddObjectsFromArray:"
- "bundleWithPath:"
- "count"
- "enumerateAttributesInRange:options:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "initWithAccessibilityContainer:"
- "initWithAccessibilityContainer:representedElements:"
- "initWithName:actionHandler:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isEqualToString:"
- "length"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "mutableCopy"
- "objectAtIndexedSubscript:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "safeArrayForKey:"
- "safeBoolForKey:"
- "safeCGFloatForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "sendActionsForControlEvents:"
- "setAccessibilityLabel:"
- "setAccessibilityRespondsToUserInteraction:"
- "setAccessibilityValue:"
- "setAttribute:forKey:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setRange:"
- "setValidationTargetName:"
- "sharedInstance"
- "string"
- "stringByAppendingPathComponent:"
- "stringByTrimmingCharactersInSet:"
- "stringWithFormat:"
- "substringWithRange:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8q16"
- "v32@0:8{_NSRange=QQ}16"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:isKindOfClass:"
- "valueForKey:"
- "viewDidLoad"
- "whitespaceAndNewlineCharacterSet"
- "{CGPoint=dd}16@0:8"
- "{_NSRange=QQ}16@0:8"
- "{_NSRange=QQ}24@0:8@16"

```
