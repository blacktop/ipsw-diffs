## EventKitUI

> `/System/Library/Frameworks/EventKitUI.framework/EventKitUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1568.0.0.0.0
-  __TEXT.__text: 0x1f6f90
-  __TEXT.__objc_methlist: 0x2020c
+1572.0.0.0.0
+  __TEXT.__text: 0x1f9aec
+  __TEXT.__objc_methlist: 0x2038c
   __TEXT.__const: 0x2e94
-  __TEXT.__cstring: 0xd184
-  __TEXT.__gcc_except_tab: 0x3fbc
+  __TEXT.__cstring: 0xd1a4
+  __TEXT.__gcc_except_tab: 0x3f78
   __TEXT.__oslogstring: 0x7b37
   __TEXT.__ustring: 0x862
   __TEXT.__dlopen_cstrs: 0x36b
   __TEXT.__swift5_typeref: 0x160c
-  __TEXT.__swift5_capture: 0x780
-  __TEXT.__constg_swiftt: 0x1c84
-  __TEXT.__swift5_reflstr: 0x16fd
+  __TEXT.__swift5_capture: 0x7b8
+  __TEXT.__constg_swiftt: 0x1c8c
+  __TEXT.__swift5_reflstr: 0x170d
   __TEXT.__swift5_assocty: 0x278
-  __TEXT.__swift5_fieldmd: 0xdc0
+  __TEXT.__swift5_fieldmd: 0xdcc
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_proto: 0xf8
   __TEXT.__swift5_types: 0x108
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0xac
-  __TEXT.__unwind_info: 0x7db8
+  __TEXT.__unwind_info: 0x7e00
   __TEXT.__eh_frame: 0xbec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4878
-  __DATA_CONST.__objc_classlist: 0xc80
+  __DATA_CONST.__const: 0x4898
+  __DATA_CONST.__objc_classlist: 0xc90
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x658
+  __DATA_CONST.__objc_protolist: 0x660
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfb58
+  __DATA_CONST.__objc_selrefs: 0xfbf0
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x8b8
+  __DATA_CONST.__objc_superrefs: 0x8c8
   __DATA_CONST.__objc_arraydata: 0x1c0
-  __DATA_CONST.__got: 0x1bd8
-  __AUTH_CONST.__const: 0x2ee0
+  __DATA_CONST.__got: 0x1c10
+  __AUTH_CONST.__const: 0x2f98
   __AUTH_CONST.__cfstring: 0xb4c0
-  __AUTH_CONST.__objc_const: 0x31630
+  __AUTH_CONST.__objc_const: 0x31838
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1778
-  __AUTH.__objc_data: 0x7d00
+  __AUTH_CONST.__auth_got: 0x17a0
+  __AUTH.__objc_data: 0x7da0
   __AUTH.__data: 0x1048
-  __DATA.__objc_ivar: 0x2584
-  __DATA.__data: 0x5168
+  __DATA.__objc_ivar: 0x2594
+  __DATA.__data: 0x51c8
   __DATA.__bss: 0x19e8
   __DATA.__common: 0x238
   __DATA_DIRTY.__objc_data: 0x1400

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12358
-  Symbols:   25026
+  Functions: 12398
+  Symbols:   25108
   CStrings:  2364
 
Symbols:
+ +[EKAbstractCalendarEditor usesOverCurrentContextPresentationInView:]
+ +[EKDayTimeView _prefersPadTimeMetricsInViewHierarchy:]
+ +[EKDayTimeView timeInsetForSizeClass:aspectRatioType:inViewHierarchy:]
+ -[EKAbstractCalendarEditor _adjustTableContentInsetForKeyboardNotification:]
+ -[EKDayViewWithGutters _leadingAlignOverlayBandIfNeeded]
+ -[EKDayViewWithGutters _shouldLeadingAlignOverlayBand]
+ -[EKDayViewWithGutters _updateTopLabelsContainerHidden]
+ -[EKEventAttendeePicker _filterBlockedRecipients:completion:]
+ -[EKEventAttendeesEditViewController preferredContentSize]
+ -[EKEventDetailTableView adjustedContentInsetDidChange]
+ -[EKEventEditViewControllerModernImpl willMoveToParentViewController:]
+ -[EKEventViewControllerDefaultImpl _shouldRenderReminderDeleteInList]
+ -[EKEventViewControllerDefaultImpl reminderDeleteDetailItem:requestsDeleteWithSourceView:]
+ -[EKExpandedReminderStackCell _applyBackgroundCornerRadiusVisible:]
+ -[EKExpandedReminderStackCell setupCellWithTitle:completed:editable:date:buttonColor:buttonImageName:backgroundColor:recurringString:shouldMatchDefaultTableStyling:delegate:]
+ -[EKExpandedReminderStackViewController _applyBackgroundColorFromDelegate]
+ -[EKExpandedReminderStackViewController expandedReminderStackShouldMatchDefaultTableStyling]
+ -[EKICSPreviewController eventViewControllerShouldHideNavigationDetailsCancelButton:]
+ -[EKReminderDeleteDetailCell .cxx_destruct]
+ -[EKReminderDeleteDetailCell initWithEvent:editable:]
+ -[EKReminderDeleteDetailCell setSeparatorStyle:]
+ -[EKReminderDeleteDetailItem .cxx_destruct]
+ -[EKReminderDeleteDetailItem cellForSubitemAtIndex:]
+ -[EKReminderDeleteDetailItem defaultCellHeightForSubitemAtIndex:forWidth:forceUpdate:]
+ -[EKReminderDeleteDetailItem eventViewController:didSelectReadOnlySubitem:]
+ -[EKReminderDeleteDetailItem initWithDeleteDelegate:]
+ -[EKReminderDeleteDetailItem reset]
+ -[EKReminderDeleteDetailItem section]
+ -[EKUIEventInviteesEditViewController attendees]
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table172
+ GCC_except_table29
+ GCC_except_table34
+ GCC_except_table42
+ _OBJC_CLASS_$_CalBlockListFilter
+ _OBJC_CLASS_$_EKReminderDeleteDetailCell
+ _OBJC_CLASS_$_EKReminderDeleteDetailItem
+ _OBJC_CLASS_$_UICornerConfiguration
+ _OBJC_CLASS_$_UICornerRadius
+ _OBJC_IVAR_$_EKExpandedReminderStackCell._matchesDefaultTableStyling
+ _OBJC_IVAR_$_EKReminderDeleteDetailCell._titleLabel
+ _OBJC_IVAR_$_EKReminderDeleteDetailItem._cell
+ _OBJC_IVAR_$_EKReminderDeleteDetailItem._deleteDelegate
+ _OBJC_METACLASS_$_EKReminderDeleteDetailCell
+ _OBJC_METACLASS_$_EKReminderDeleteDetailItem
+ _UIKeyboardAnimationCurveUserInfoKey
+ _UIKeyboardAnimationDurationUserInfoKey
+ __OBJC_$_INSTANCE_METHODS_EKReminderDeleteDetailCell
+ __OBJC_$_INSTANCE_METHODS_EKReminderDeleteDetailItem
+ __OBJC_$_INSTANCE_VARIABLES_EKReminderDeleteDetailCell
+ __OBJC_$_INSTANCE_VARIABLES_EKReminderDeleteDetailItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EKReminderDeleteDetailItemDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EKReminderDeleteDetailItemDelegate
+ __OBJC_$_PROTOCOL_REFS_EKReminderDeleteDetailItemDelegate
+ __OBJC_CLASS_RO_$_EKReminderDeleteDetailCell
+ __OBJC_CLASS_RO_$_EKReminderDeleteDetailItem
+ __OBJC_LABEL_PROTOCOL_$_EKReminderDeleteDetailItemDelegate
+ __OBJC_METACLASS_RO_$_EKReminderDeleteDetailCell
+ __OBJC_METACLASS_RO_$_EKReminderDeleteDetailItem
+ __OBJC_PROTOCOL_$_EKReminderDeleteDetailItemDelegate
+ __UITableViewDefaultSectionCornerRadiusForTraitCollection
+ ___120-[EKCalendarChooserDefaultImpl _presentEditor:withIndexPath:barButtonItem:permittedArrowDirections:animated:completion:]_block_invoke
+ ___61-[EKEventAttendeePicker _filterBlockedRecipients:completion:]_block_invoke
+ ___61-[EKEventAttendeePicker _filterBlockedRecipients:completion:]_block_invoke_2
+ ___76-[EKAbstractCalendarEditor _adjustTableContentInsetForKeyboardNotification:]_block_invoke
+ ___block_descriptor_32_e38_"NSString"16?0"CNComposeRecipient"8l
+ ___block_descriptor_34_e71_"NSCollectionLayoutSection"24?0q8"<NSCollectionLayoutEnvironment>"16l
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSArray"8lw48l8s32l8s40l8
+ ___swift_closure_destructor.11Tm
+ ___swift_closure_destructor.153Tm
+ ___swift_closure_destructor.38Tm
+ ___swift_closure_destructor.45Tm
+ ___swift_closure_destructor.85Tm
+ _objc_msgSend$_applyBackgroundColorFromDelegate
+ _objc_msgSend$_applyBackgroundCornerRadiusVisible:
+ _objc_msgSend$_filterBlockedRecipients:completion:
+ _objc_msgSend$_leadingAlignOverlayBandIfNeeded
+ _objc_msgSend$_prefersPadTimeMetricsInViewHierarchy:
+ _objc_msgSend$_shouldLeadingAlignOverlayBand
+ _objc_msgSend$_shouldRenderReminderDeleteInList
+ _objc_msgSend$_updateTopLabelsContainerHidden
+ _objc_msgSend$configurationWithRadius:
+ _objc_msgSend$convertRect:fromWindow:
+ _objc_msgSend$effectiveUserInterfaceLayoutDirection
+ _objc_msgSend$expandedReminderStackShouldMatchDefaultTableStyling
+ _objc_msgSend$filterUnblockedResults:usingBlockList:emailForResult:phoneForResult:completionQueue:completion:
+ _objc_msgSend$fixedRadius:
+ _objc_msgSend$hidesPrimaryDate
+ _objc_msgSend$initWithDeleteDelegate:
+ _objc_msgSend$itemIdentifiers
+ _objc_msgSend$occurrenceLayoutTrailingInset
+ _objc_msgSend$overrideBackgroundColor
+ _objc_msgSend$reminderDeleteDetailItem:requestsDeleteWithSourceView:
+ _objc_msgSend$setCornerConfiguration:
+ _objc_msgSend$setupCellWithTitle:completed:editable:date:buttonColor:buttonImageName:backgroundColor:recurringString:shouldMatchDefaultTableStyling:delegate:
+ _objc_msgSend$shouldMatchDefaultTableStyling
+ _objc_msgSend$showOverlayDate
+ _objc_msgSend$timeInsetForSizeClass:aspectRatioType:inViewHierarchy:
+ _objc_msgSend$usesOverCurrentContextPresentationInView:
+ _objc_msgSend$verticalScrollIndicatorInsets
+ _swift_retain_x25
- +[EKDayTimeView timeInsetForSizeClass:aspectRatioType:]
- -[EKEventAttendeePicker predicateForContactWithBlockedAddress]
- -[EKExpandedReminderStackCell setupCellWithTitle:completed:editable:date:buttonColor:buttonImageName:backgroundColor:recurringString:delegate:]
- GCC_except_table124
- GCC_except_table130
- GCC_except_table133
- GCC_except_table171
- GCC_except_table38
- GCC_except_table72
- _OBJC_CLASS_$_UIKeyboard
- ___62-[EKEventAttendeePicker predicateForContactWithBlockedAddress]_block_invoke
- ___block_descriptor_33_e71_"NSCollectionLayoutSection"24?0q8"<NSCollectionLayoutEnvironment>"16l
- ___block_descriptor_40_e8_32s_e25_B24?08"NSDictionary"16ls32l8
- ___swift_closure_destructor.35Tm
- ___swift_closure_destructor.42Tm
- ___swift_closure_destructor.5Tm
- ___swift_closure_destructor.82Tm
- _objc_msgSend$defaultSize
- _objc_msgSend$isBlockedWithEmail:
- _objc_msgSend$isBlockedWithPhoneNumber:
- _objc_msgSend$loadViewIfNeeded
- _objc_msgSend$predicateForContactWithBlockedAddress
- _objc_msgSend$setupCellWithTitle:completed:editable:date:buttonColor:buttonImageName:backgroundColor:recurringString:delegate:
- _objc_msgSend$timeInsetForSizeClass:aspectRatioType:
CStrings:
+ "@\"NSString\"16@?0@\"CNComposeRecipient\"8"
+ "Gesture controller tried to commit with no dragging view but a live event. Cancelling instead."
- "B24@?0@8@\"NSDictionary\"16"
- "Gesture controller tried to commit, but with no view to drag. Cancelling instead."
```
