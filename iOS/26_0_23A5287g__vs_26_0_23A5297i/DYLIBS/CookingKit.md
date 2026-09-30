## CookingKit

> `/System/Library/PrivateFrameworks/CookingKit.framework/CookingKit`

```diff

-5726.2.0.0.0
-  __TEXT.__text: 0x1a217c
-  __TEXT.__auth_stubs: 0x4bf0
-  __TEXT.__objc_methlist: 0x264
-  __TEXT.__const: 0x19b94
-  __TEXT.__cstring: 0x43bf
+5728.0.0.0.0
+  __TEXT.__text: 0x1a97d8
+  __TEXT.__auth_stubs: 0x4d80
+  __TEXT.__objc_methlist: 0x2cc
+  __TEXT.__const: 0x1a0a4
+  __TEXT.__cstring: 0x467f
   __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__swift5_typeref: 0x1dd06
-  __TEXT.__constg_swiftt: 0x6b58
+  __TEXT.__swift5_typeref: 0x1cdca
+  __TEXT.__constg_swiftt: 0x6ca8
   __TEXT.__swift5_builtin: 0x294
-  __TEXT.__swift5_reflstr: 0x435f
-  __TEXT.__swift5_fieldmd: 0x6250
-  __TEXT.__swift5_assocty: 0x15a8
-  __TEXT.__swift5_proto: 0x10c8
-  __TEXT.__swift5_types: 0x868
-  __TEXT.__swift5_capture: 0x1234
+  __TEXT.__swift5_reflstr: 0x432f
+  __TEXT.__swift5_fieldmd: 0x6348
+  __TEXT.__swift5_assocty: 0x15f0
+  __TEXT.__swift5_proto: 0x10cc
+  __TEXT.__swift5_types: 0x87c
+  __TEXT.__swift5_capture: 0x11dc
   __TEXT.__swift5_protos: 0x8c
   __TEXT.__swift5_mpenum: 0x108
-  __TEXT.__swift_as_entry: 0x198
-  __TEXT.__swift_as_ret: 0x168
-  __TEXT.__oslogstring: 0xc21
-  __TEXT.__unwind_info: 0x6178
-  __TEXT.__eh_frame: 0x63bc
+  __TEXT.__swift_as_entry: 0x16c
+  __TEXT.__swift_as_ret: 0x160
+  __TEXT.__oslogstring: 0xf61
+  __TEXT.__unwind_info: 0x6268
+  __TEXT.__eh_frame: 0x6044
   __TEXT.__objc_classname: 0x38
-  __TEXT.__objc_methname: 0xe04
+  __TEXT.__objc_methname: 0xf36
   __TEXT.__objc_methtype: 0x657
   __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x1578
+  __DATA_CONST.__got: 0x15a0
   __DATA_CONST.__const: 0x240
-  __DATA_CONST.__objc_classlist: 0x248
+  __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x528
+  __DATA_CONST.__objc_selrefs: 0x588
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x2608
-  __AUTH_CONST.__const: 0xbec0
-  __AUTH_CONST.__objc_const: 0x3c50
-  __AUTH.__objc_data: 0x518
-  __AUTH.__data: 0x3290
+  __AUTH_CONST.__auth_got: 0x26d0
+  __AUTH_CONST.__const: 0xbf38
+  __AUTH_CONST.__objc_const: 0x3ec0
+  __AUTH.__objc_data: 0x680
+  __AUTH.__data: 0x3490
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x6a70
-  __DATA.__bss: 0x1e7c8
+  __DATA.__data: 0x6b10
+  __DATA.__bss: 0x1e8d8
   __DATA.__common: 0x228
   __DATA_DIRTY.__objc_data: 0x910
-  __DATA_DIRTY.__data: 0x4e88
+  __DATA_DIRTY.__data: 0x4dc8
   __DATA_DIRTY.__bss: 0x2ea0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/MobileTimerUI.framework/MobileTimerUI
+  - /System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit
   - /System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet
   - /System/Library/PrivateFrameworks/TeaBreeze.framework/TeaBreeze
   - /System/Library/PrivateFrameworks/TeaDB.framework/TeaDB

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5D5AA5B6-B5F0-3619-88C0-1159B7E4A08F
-  Functions: 9100
-  Symbols:   412
-  CStrings:  624
+  UUID: F36FC5E8-7B74-31D2-8141-DFE8ECE7A11B
+  Functions: 9232
+  Symbols:   409
+  CStrings:  664
 
Symbols:
+ _OBJC_CLASS_$_REMReminder
+ _OBJC_CLASS_$_REMStore
+ _OBJC_METACLASS_$_UIViewController
- _OBJC_CLASS_$_UIFontMetrics
- _UIFontTextStyleSubheadline
- _UIFontWeightBold
- _UIFontWeightRegular
- _UIFontWidthStandard
- _objc_release_x1
CStrings:
+ "@32@0:8@16@24"
+ "Error determining if reminders exist for recipeID %s. Error: %{public}@. Returning false."
+ "Error getting details on reminders for recipeID %s: %{public}@. Returning nil"
+ "GroceriesButtonViewModel finished adding recipeID %s to grocery list with result: %s"
+ "GroceriesButtonViewModel tapped add to grocery list for recipeID %s."
+ "GroceriesButtonViewModel tapped open grocery list for recipeID %s."
+ "GroceriesButtonViewModel unable to add ingredients due to recipe ID being nil"
+ "GroceriesButtonViewModel unable to open grocery list due to recipe ID being nil"
+ "GroceriesLabelViewModel finished adding recipeID %s to grocery list with result: %s"
+ "GroceriesLabelViewModel tapped add more ingredients to grocery list for recipeID %s."
+ "No reminders found for recipe. Returning nil"
+ "The text showing when ingredients were last added to the grocery list. %@ will be replaced with the formatted date."
+ "_TtC10CookingKit18GroceryExportState"
+ "_TtC10CookingKitP33_04E1833260F82E278E94C0F09760429C25AdContainerViewController"
+ "_TtC10CookingKitP33_6C32768279A34A304DA1EE2F1863B55F34EndOfRecipeContainerViewController"
+ "_adPlacement"
+ "_isExported"
+ "_recipeCardID"
+ "_recipeCardViewSessionID"
+ "_remindersListDetails"
+ "adViewControllerProvider"
+ "addSubview:"
+ "addToGroceryList(on:ingredients:recipeURL:recipeID:)"
+ "childViewControllers"
+ "com.apple.news.recipeExportToGroceryList"
+ "creationDate"
+ "didMoveToParentViewController:"
+ "dismissed"
+ "endOfRecipeViewController"
+ "endOfRecipeViewControllerProvider"
+ "fail"
+ "fetchIncompleteRemindersCountForNewsRecipeCardWithBatchCreationID:error:"
+ "fetchIncompleteRemindersForNewsRecipeCardWithBatchCreationID:error:"
+ "initWithCoder:"
+ "initWithNibName:bundle:"
+ "integerValue"
+ "isExported"
+ "list"
+ "objectID"
+ "preferredContentSize"
+ "preferredContentSizeDidChangeForChildContentContainer:"
+ "presentingViewController"
+ "setPreferredContentSize:"
+ "stringRepresentation"
+ "success"
+ "x-apple-reminderkit://REMCDList/"
- "_adViewController"
- "_endOfRecipeViewController"
- "_loadingTasks"
- "addToGroceryList(on:ingredients:recipeURL:)"
- "initForTextStyle:"
- "scaledValueForValue:compatibleWithTraitCollection:"
- "systemFontOfSize:weight:width:"

```
