## ToneKit

> `/System/Library/PrivateFrameworks/ToneKit.framework/ToneKit`

```diff

-639.0.0.0.0
-  __TEXT.__text: 0x23774
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x3254
+651.0.0.0.0
+  __TEXT.__text: 0x26024
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x33dc
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x21c
-  __TEXT.__cstring: 0x163c
+  __TEXT.__cstring: 0x1737
   __TEXT.__oslogstring: 0xa57
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0xb7
-  __TEXT.__unwind_info: 0xad0
-  __TEXT.__objc_classname: 0x6d3
-  __TEXT.__objc_methname: 0xaa04
-  __TEXT.__objc_methtype: 0x1a8c
-  __TEXT.__objc_stubs: 0x7da0
-  __DATA_CONST.__got: 0x458
-  __DATA_CONST.__const: 0x5b0
+  __TEXT.__unwind_info: 0xb10
+  __TEXT.__objc_classname: 0x6d7
+  __TEXT.__objc_methname: 0xb00a
+  __TEXT.__objc_methtype: 0x1b37
+  __TEXT.__objc_stubs: 0x80e0
+  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__const: 0x5b8
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2478
+  __DATA_CONST.__objc_selrefs: 0x2560
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xf0
-  __AUTH_CONST.__auth_got: 0x358
+  __DATA_CONST.__objc_superrefs: 0x100
+  __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1080
-  __AUTH_CONST.__objc_const: 0x5048
+  __AUTH_CONST.__cfstring: 0x1200
+  __AUTH_CONST.__objc_const: 0x5190
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x414
+  __DATA.__objc_ivar: 0x42c
   __DATA.__data: 0x780
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BBA43A14-137B-35EF-8C4A-1A4F31C32C45
-  Functions: 998
-  Symbols:   3974
-  CStrings:  2188
+  UUID: FBBFD12E-4BDB-35D1-8D95-CC9C4E8BAC78
+  Functions: 1028
+  Symbols:   4064
+  CStrings:  2258
 
Symbols:
+ +[TKTonePickerViewController _disclosureAccessoryImageForReflectionRemixHeaderWithStatus:]
+ -[TKPickerItem hash]
+ -[TKPickerItem isEqual:]
+ -[TKPickerRowItem _setWantsIndentedLayout:]
+ -[TKPickerRowItem hash]
+ -[TKPickerRowItem isEqual:]
+ -[TKPickerRowItem wantsIndentedLayout]
+ -[TKPickerSectionItem hash]
+ -[TKPickerSectionItem isEqual:]
+ -[TKPickerSelectableItem hash]
+ -[TKPickerSelectableItem isEqual:]
+ -[TKToneClassicsPickerItem hash]
+ -[TKToneClassicsPickerItem isEqual:]
+ -[TKTonePickerController _identifierOfSelectedRemixRingtone]
+ -[TKTonePickerController _indexPathForReflectionRemixHeader]
+ -[TKTonePickerController _isReflectionHeaderAtIndexPath:]
+ -[TKTonePickerController _remixRingtoneIdentifiers]
+ -[TKTonePickerController _selectedRemixRingtoneIndex]
+ -[TKTonePickerController _setRemixRingtoneIdentifiers:]
+ -[TKTonePickerController _setSelectedRemixRingtoneIndex:]
+ -[TKTonePickerController initWithAlertType:topic:defaultToneIdentifier:selectedToneIdentifier:showsDefault:showsNone:isNoneAtTop:noneString:]
+ -[TKTonePickerController setShowsReflectionRemixesInline:]
+ -[TKTonePickerController showsReflectionRemixesInline]
+ -[TKTonePickerItem hash]
+ -[TKTonePickerItem isEqual:]
+ -[TKTonePickerSectionItem hash]
+ -[TKTonePickerSectionItem isEqual:]
+ -[TKTonePickerTableView _setSectionContentInset:]
+ -[TKTonePickerTableView tk_rawSectionContentInset]
+ -[TKTonePickerViewController tonePickerController:didUpdateDisclosureStatus:ofTonePickerItem:]
+ -[TKTonePickerViewController updateCell:withAccessoryImage:]
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table85
+ GCC_except_table94
+ _OBJC_CLASS_$_UIDevice
+ _OBJC_CLASS_$_UIListContentConfiguration
+ _OBJC_IVAR_$_TKPickerRowItem._wantsIndentedLayout
+ _OBJC_IVAR_$_TKTonePickerController.__remixRingtoneIdentifiers
+ _OBJC_IVAR_$_TKTonePickerController.__selectedRemixRingtoneIndex
+ _OBJC_IVAR_$_TKTonePickerController._showsReflectionRemixesInline
+ _OBJC_IVAR_$_TKTonePickerTableView._tk_rawSectionContentInset
+ _OBJC_IVAR_$_TKTonePickerViewController._tableViewCellLayoutManagerForIndentedRemixRows
+ ___47-[TKTonePickerController deleteTonePickerItem:]_block_invoke.99
+ ___54-[TKTonePickerController toneStoreDownloadsDidFinish:]_block_invoke.164
+ ___56-[TKTonePickerController toneStoreDownloadsDidProgress:]_block_invoke.161
+ _objc_msgSend$_disclosureAccessoryImageForReflectionRemixHeaderWithStatus:
+ _objc_msgSend$_identifierOfSelectedRemixRingtone
+ _objc_msgSend$_indexPathForReflectionRemixHeader
+ _objc_msgSend$_isReflectionHeaderAtIndexPath:
+ _objc_msgSend$_minimumHeightForTraitCollection:
+ _objc_msgSend$_remixRingtoneIdentifiers
+ _objc_msgSend$_selectedRemixRingtoneIndex
+ _objc_msgSend$_setRemixRingtoneIdentifiers:
+ _objc_msgSend$_setSelectedRemixRingtoneIndex:
+ _objc_msgSend$_setWantsIndentedLayout:
+ _objc_msgSend$cellConfiguration
+ _objc_msgSend$currentDevice
+ _objc_msgSend$directionalLayoutMargins
+ _objc_msgSend$imageWithTintColor:renderingMode:
+ _objc_msgSend$initWithIndexesInRange:
+ _objc_msgSend$insertObjects:atIndexes:
+ _objc_msgSend$layoutManager
+ _objc_msgSend$preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:
+ _objc_msgSend$removeObjectsAtIndexes:
+ _objc_msgSend$setShowsReflectionRemixesInline:
+ _objc_msgSend$showsReflectionRemixesInline
+ _objc_msgSend$supportsReflectionRemixes
+ _objc_msgSend$tertiaryLabelColor
+ _objc_msgSend$tk_rawSectionContentInset
+ _objc_msgSend$tonePickerController:didUpdateDisclosureStatus:ofTonePickerItem:
+ _objc_msgSend$updateCell:withAccessoryImage:
+ _objc_msgSend$userInterfaceIdiom
+ _objc_msgSend$wantsIndentedLayout
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x9
- -[TKTonePickerViewController _updateMinimumTextIndentation]
- GCC_except_table104
- GCC_except_table105
- GCC_except_table80
- GCC_except_table84
- _UITableDefaultRowHeight
- ___47-[TKTonePickerController deleteTonePickerItem:]_block_invoke.89
- ___54-[TKTonePickerController toneStoreDownloadsDidFinish:]_block_invoke.149
- ___56-[TKTonePickerController toneStoreDownloadsDidProgress:]_block_invoke.146
- _objc_msgSend$_updateMinimumTextIndentation
- _objc_msgSend$layoutMargins
CStrings:
+ "-EncoreRemix"
+ "<default>"
+ "<remix_ringtone_identifier>"
+ "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
+ "@40@0:8@16@24@32"
+ "@68@0:8q16@24@32@40B48B52B56@60"
+ "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
+ "B40@0:8@16@24@32"
+ "REMIX_DEFAULT_DETAIL_NAME"
+ "REMIX_HEADER_NAME"
+ "T@\"NSArray\",&,N,S_setRemixRingtoneIdentifiers:,V__remixRingtoneIdentifiers"
+ "TB,N,S_setWantsIndentedLayout:,V_wantsIndentedLayout"
+ "TB,N,SsetShowsReflectionRemixesInline:,V_showsReflectionRemixesInline"
+ "TQ,N,S_setSelectedRemixRingtoneIndex:,V__selectedRemixRingtoneIndex"
+ "T{UIEdgeInsets=dddd},R,N,V_tk_rawSectionContentInset"
+ "_DETAIL_NAME"
+ "_TKTonePickerCellWithRotatingDisclosureIndicatorReuseIdentifier"
+ "__remixRingtoneIdentifiers"
+ "__selectedRemixRingtoneIndex"
+ "_disclosureAccessoryImageForReflectionRemixHeaderWithStatus:"
+ "_identifierOfSelectedRemixRingtone"
+ "_indexPathForReflectionRemixHeader"
+ "_isReflectionHeaderAtIndexPath:"
+ "_minimumHeightForTraitCollection:"
+ "_remixRingtoneIdentifiers"
+ "_selectedRemixRingtoneIndex"
+ "_setRemixRingtoneIdentifiers:"
+ "_setSelectedRemixRingtoneIndex:"
+ "_setWantsIndentedLayout:"
+ "_showsReflectionRemixesInline"
+ "_tableViewCellLayoutManagerForIndentedRemixRows"
+ "_tk_rawSectionContentInset"
+ "_wantsIndentedLayout"
+ "cellConfiguration"
+ "chevron.down"
+ "chevron.forward"
+ "currentDevice"
+ "directionalLayoutMargins"
+ "imageWithTintColor:renderingMode:"
+ "initWithAlertType:topic:defaultToneIdentifier:selectedToneIdentifier:showsDefault:showsNone:isNoneAtTop:noneString:"
+ "initWithIndexesInRange:"
+ "insertObjects:atIndexes:"
+ "layoutManager"
+ "preferredFontDescriptorWithTextStyle:addingSymbolicTraits:options:"
+ "reflection remix header"
+ "remix"
+ "removeObjectsAtIndexes:"
+ "setShowsReflectionRemixesInline:"
+ "showsReflectionRemixesInline"
+ "supportsReflectionRemixes"
+ "tertiaryLabelColor"
+ "textField:editMenuForCharactersInRanges:suggestedActions:"
+ "textField:shouldChangeCharactersInRanges:replacementString:"
+ "tk_rawSectionContentInset"
+ "tonePickerController:didUpdateDisclosureStatus:ofTonePickerItem:"
+ "updateCell:withAccessoryImage:"
+ "userInterfaceIdiom"
+ "wantsIndentedLayout"
+ "\xf01"
- "_updateMinimumTextIndentation"
- "layoutMargins"

```
