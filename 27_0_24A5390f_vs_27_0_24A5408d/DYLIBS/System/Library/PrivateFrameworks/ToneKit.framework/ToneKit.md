## ToneKit

> `/System/Library/PrivateFrameworks/ToneKit.framework/ToneKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-672.0.0.0.0
-  __TEXT.__text: 0x26858
-  __TEXT.__objc_methlist: 0x33dc
-  __TEXT.__cstring: 0x18c1
-  __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__oslogstring: 0xaa4
+675.0.0.0.0
+  __TEXT.__text: 0x26b50
+  __TEXT.__objc_methlist: 0x33b4
+  __TEXT.__cstring: 0x19ab
+  __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x1ec
+  __TEXT.__oslogstring: 0xae7
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0xb7
-  __TEXT.__unwind_info: 0xb10
+  __TEXT.__unwind_info: 0xb20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5b8
-  __DATA_CONST.__objc_classlist: 0x118
+  __DATA_CONST.__const: 0x630
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2580
+  __DATA_CONST.__objc_selrefs: 0x2588
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__got: 0x470
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1220
-  __AUTH_CONST.__objc_const: 0x5190
+  __AUTH_CONST.__cfstring: 0x1240
+  __AUTH_CONST.__objc_const: 0x50c0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x370
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x42c
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x428
   __DATA.__data: 0x780
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x190

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1028
-  Symbols:   2964
-  CStrings:  240
+  Functions: 1030
+  Symbols:   2963
+  CStrings:  243
 
Symbols:
+ +[TKPickerTableViewCell checkmarkImage]
+ +[TKPickerTableViewCell checkmarkPlaceholderImage]
+ -[TKPickerTableViewCell indentedRowSeparatorLeftInset]
+ -[TKTonePickerItem _setWantsIndentedLayout:]
+ -[TKTonePickerItem wantsIndentedLayout]
+ -[TKTonePickerViewController _isAlarmWakeUp]
+ -[TKTonePickerViewController _shouldShowCheckmarkOnLeadingEdge]
+ GCC_except_table50
+ GCC_except_table60
+ GCC_except_table71
+ GCC_except_table74
+ _OBJC_IVAR_$_TKTonePickerItem._wantsIndentedLayout
+ _OBJC_IVAR_$_TKTonePickerViewController._checkmarkPlaceholderImage
+ _OBJC_IVAR_$_TKVibrationPickerViewController._isAnimatingCommittedRowDeletion
+ _OBJC_IVAR_$_TKVibrationPickerViewController._pendingSwipeToDeleteExitEditingModeAfterRowDeletionAnimation
+ __OBJC_$_CLASS_METHODS_TKPickerTableViewCell
+ ___82-[TKVibrationPickerViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke
+ ___82-[TKVibrationPickerViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke_2
+ ___82-[TKVibrationPickerViewController tableView:commitEditingStyle:forRowAtIndexPath:]_block_invoke_3
+ ___86-[TKVibrationPickerViewController _handleUserGeneratedVibrationsDidChangeNotification]_block_invoke
+ ___86-[TKVibrationPickerViewController _handleUserGeneratedVibrationsDidChangeNotification]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ _objc_msgSend$_isAlarmWakeUp
+ _objc_msgSend$_setSectionContentInsetFollowsLayoutMargins:
+ _objc_msgSend$_shouldShowCheckmarkOnLeadingEdge
+ _objc_msgSend$activateConstraints:
+ _objc_msgSend$centerYAnchor
+ _objc_msgSend$checkmarkImage
+ _objc_msgSend$checkmarkPlaceholderImage
+ _objc_msgSend$constraintEqualToAnchor:
+ _objc_msgSend$convertRect:fromView:
+ _objc_msgSend$effectiveUserInterfaceLayoutDirection
+ _objc_msgSend$indentedRowSeparatorLeftInset
+ _objc_msgSend$layoutMarginsGuide
+ _objc_msgSend$leadingAnchor
+ _objc_msgSend$setIndentationLevel:
+ _objc_msgSend$trailingAnchor
- +[TKTonePickerViewController _checkmarkImage]
- -[TKPickerRowItem _setWantsIndentedLayout:]
- -[TKPickerRowItem wantsIndentedLayout]
- -[TKTonePickerTableViewCellLayoutManager _adjustedTextFrameWithOriginalTextFrame:forCell:]
- -[TKTonePickerTableViewCellLayoutManager minimumTextIndentation]
- -[TKTonePickerTableViewCellLayoutManager setMinimumTextIndentation:]
- -[TKTonePickerTableViewCellLayoutManager textRectForCell:rowWidth:forSizing:]
- -[TKTonePickerViewController _minimumTextIndentationForTableView:withCheckmarkImage:]
- -[TKTonePickerViewController _shouldShowCheckmarkOnTrailingEdge]
- -[TKVibrationPickerTableViewCell _layoutRemovableTextField]
- -[TKVibrationPickerTableViewCell layoutSubviews]
- GCC_except_table61
- GCC_except_table75
- _OBJC_CLASS_$_TKTonePickerTableViewCellLayoutManager
- _OBJC_CLASS_$_UITableViewCellLayoutManagerValue1
- _OBJC_IVAR_$_TKPickerRowItem._wantsIndentedLayout
- _OBJC_IVAR_$_TKTonePickerTableViewCellLayoutManager._minimumTextIndentation
- _OBJC_IVAR_$_TKTonePickerViewController._tableViewCellLayoutManagerForIndentedRemixRows
- _OBJC_IVAR_$_TKTonePickerViewController._tableViewCellLayoutManagerForIndentedRows
- _OBJC_IVAR_$_TKTonePickerViewController._tableViewCellLayoutManagerForUnindentedRows
- _OBJC_METACLASS_$_TKTonePickerTableViewCellLayoutManager
- _OBJC_METACLASS_$_UITableViewCellLayoutManagerValue1
- __OBJC_$_INSTANCE_METHODS_TKTonePickerTableViewCellLayoutManager
- __OBJC_$_INSTANCE_VARIABLES_TKTonePickerTableViewCellLayoutManager
- __OBJC_$_PROP_LIST_TKTonePickerTableViewCellLayoutManager
- __OBJC_CLASS_RO_$_TKTonePickerTableViewCellLayoutManager
- __OBJC_METACLASS_RO_$_TKTonePickerTableViewCellLayoutManager
- _objc_msgSend$_adjustedTextFrameWithOriginalTextFrame:forCell:
- _objc_msgSend$_checkmarkImage
- _objc_msgSend$_layoutRemovableTextField
- _objc_msgSend$_minimumTextIndentationForTableView:withCheckmarkImage:
- _objc_msgSend$_sectionContentInset
- _objc_msgSend$_shouldShowCheckmarkOnTrailingEdge
- _objc_msgSend$descender
- _objc_msgSend$directionalLayoutMargins
- _objc_msgSend$indentationLevel
- _objc_msgSend$layoutManager
- _objc_msgSend$minimumTextIndentation
- _objc_msgSend$setLayoutManager:
- _objc_msgSend$setMinimumTextIndentation:
CStrings:
+ "-[TKTonePickerItem wantsIndentedLayout]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/ToneLibraryUI/Kit/Tones/TKTonePickerItem.m"
+ "A nested row must be able to show a leading checkmark: %{public}@."
+ "_TLVibrationPickerViewTableCellEditableIdentifier"
+ "\xf1B"
- "\xe1B"
- "\xf01"
```
