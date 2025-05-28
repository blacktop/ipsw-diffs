## CarPlaySupport

> `/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport`

```diff

-271.5.2.0.0
-  __TEXT.__text: 0xd54bc
+271.7.4.1.0
+  __TEXT.__text: 0xd4644
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x79fc
+  __TEXT.__objc_methlist: 0x796c
   __TEXT.__const: 0x380
-  __TEXT.__cstring: 0x15ad
+  __TEXT.__cstring: 0x158e
   __TEXT.__gcc_except_tab: 0xbb8
-  __TEXT.__oslogstring: 0x1df5
+  __TEXT.__oslogstring: 0x1d7d
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1824
-  __TEXT.__objc_classname: 0x158d
-  __TEXT.__objc_methname: 0x19d0c
-  __TEXT.__objc_methtype: 0x50f7
-  __TEXT.__objc_stubs: 0x111a0
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x1e50
+  __TEXT.__unwind_info: 0x1814
+  __TEXT.__objc_classname: 0x157e
+  __TEXT.__objc_methname: 0x19cfc
+  __TEXT.__objc_methtype: 0x50d6
+  __TEXT.__objc_stubs: 0x11120
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x1e00
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x2c8
+  __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1e450
-  __DATA_CONST.__objc_selrefs: 0x5170
+  __DATA_CONST.__objc_const: 0x1e0e0
+  __DATA_CONST.__objc_selrefs: 0x5138
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__objc_const: 0x2c28
+  __AUTH_CONST.__objc_const: 0x2b50
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__cfstring: 0x13a0

   __AUTH_CONST.__auth_got: 0x400
   __AUTH.__objc_data: 0x2760
   __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x8a0
+  __DATA.__objc_classrefs: 0x898
   __DATA.__objc_superrefs: 0x370
-  __DATA.__objc_ivar: 0x9c0
-  __DATA.__data: 0x21e8
+  __DATA.__objc_ivar: 0x9bc
+  __DATA.__data: 0x2188
   __DATA.__bss: 0x130
   - /System/Library/Frameworks/CarPlay.framework/CarPlay
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2960
-  Symbols:   11765
-  CStrings:  5186
+  Functions: 2948
+  Symbols:   11713
+  CStrings:  5177
 
Symbols:
+ GCC_except_table20
+ _objc_msgSend$setEstimatedRowHeight:
+ _objc_msgSend$setRowHeight:
- +[CPSImageRowCell heightForListItem:]
- +[CPSMessageCell heightForListItem:]
- +[CPSTableCell heightForListItem:]
- -[CPSListTemplateViewController tableView:heightForRowAtIndexPath:]
- -[CPSSectionedDataSource heightForItemAtIndexPath:inEnvironment:]
- -[CPSSectionedDataSource invalidateHeightCache]
- -[CPSSectionedDataSource rebuildHeightCacheWithEnvironment:]
- -[CPSSectionedDataSource sectionHeightCache]
- -[CPSSectionedDataSource setSectionHeightCache:]
- GCC_except_table27
- _OBJC_IVAR_$_CPSSectionedDataSource._sectionHeightCache
- _UIFontTextStyleTitle3
- __OBJC_$_CLASS_METHODS_CPSImageRowCell
- __OBJC_$_CLASS_METHODS_CPSMessageCell
- __OBJC_$_CLASS_METHODS_CPSTableCell
- __OBJC_$_PROP_LIST_CPSAssistantCell
- __OBJC_$_PROP_LIST_CPSImageRowCell
- __OBJC_$_PROP_LIST_CPSMessageCell
- __OBJC_$_PROP_LIST_CPSTableCell
- __OBJC_$_PROTOCOL_CLASS_METHODS_CPSCellSizable
- __OBJC_$_PROTOCOL_METHOD_TYPES_CPSCellSizable
- __OBJC_$_PROTOCOL_REFS_CPSCellSizable
- __OBJC_CLASS_PROTOCOLS_$_CPSAssistantCell
- __OBJC_CLASS_PROTOCOLS_$_CPSImageRowCell
- __OBJC_CLASS_PROTOCOLS_$_CPSMessageCell
- __OBJC_CLASS_PROTOCOLS_$_CPSTableCell
- __OBJC_LABEL_PROTOCOL_$_CPSCellSizable
- __OBJC_PROTOCOL_$_CPSCellSizable
- ___60-[CPSSectionedDataSource rebuildHeightCacheWithEnvironment:]_block_invoke
- ___60-[CPSSectionedDataSource rebuildHeightCacheWithEnvironment:]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e30_v32?0"CPListSection"8Q16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e37_v32?0"<CPListTemplateItem>"8Q16^B24ls32l8s40l8
- _objc_msgSend$heightForItemAtIndexPath:inEnvironment:
- _objc_msgSend$heightForListItem:
- _objc_msgSend$invalidateHeightCache
- _objc_msgSend$minimumHeight
- _objc_msgSend$rebuildHeightCacheWithEnvironment:
- _objc_msgSend$rowHeight
CStrings:
+ "2#"
+ "attributionArtworkForNowPlayingViewController:"
+ "attributionTitleForNowPlayingViewController:"
+ "nowPlayingViewControllerAttributionButtonTapped:"
+ "nowPlayingViewControllerShouldHideBackButton:"
+ "setEstimatedRowHeight:"
+ "setRowHeight:"
- "2$"
- "CPSCellSizable"
- "T@\"NSArray\",&,N,V_sectionHeightCache"
- "Unexpected list item %@ in section %@"
- "Unexpected missing height cache value for item %{public}@ at indexPath %{public}@"
- "_sectionHeightCache"
- "d24@0:8@\"<CPListTemplateItem>\"16"
- "heightForItemAtIndexPath:inEnvironment:"
- "heightForListItem:"
- "invalidateHeightCache"
- "minimumHeight"
- "rebuildHeightCacheWithEnvironment:"
- "rowHeight"
- "sectionHeightCache"
- "setSectionHeightCache:"
- "v32@?0@\"CPListSection\"8Q16^B24"

```
