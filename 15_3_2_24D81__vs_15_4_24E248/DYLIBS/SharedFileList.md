## SharedFileList

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/SharedFileList.framework/Versions/A/SharedFileList`

```diff

-294.9.0.0.0
-  __TEXT.__text: 0x1cee4
+302.3.0.0.0
+  __TEXT.__text: 0x1c8ac
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x15bc
+  __TEXT.__objc_methlist: 0x19fc
   __TEXT.__const: 0xb0
   __TEXT.__oslogstring: 0x13b9
-  __TEXT.__cstring: 0x1a38
+  __TEXT.__cstring: 0x1a95
   __TEXT.__gcc_except_tab: 0x578
   __TEXT.__dlopen_cstrs: 0x63
-  __TEXT.__unwind_info: 0x818
+  __TEXT.__unwind_info: 0x890
   __TEXT.__objc_classname: 0x236
   __TEXT.__objc_methname: 0x2b24
   __TEXT.__objc_methtype: 0x9f0
   __TEXT.__objc_stubs: 0x2660
   __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc48
+  __DATA_CONST.__objc_selrefs: 0xce0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0xb50
   __AUTH_CONST.__cfstring: 0x12c0
-  __AUTH_CONST.__objc_const: 0x5e08
+  __AUTH_CONST.__objc_const: 0x5678
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58EF0C88-7857-30AF-8577-A76E86767816
-  Functions: 755
-  Symbols:   1971
-  CStrings:  1138
+  UUID: 60C98700-FAB7-30C9-BFB7-C8D4146BFE84
+  Functions: 788
+  Symbols:   2109
+  CStrings:  1139
 
Symbols:
+ +[NSData(SFLBookmarkAdditions) __sfl_bookmarkDataWithURL:].cold.2
+ +[NSXPCConnection(SFLClient) sflServiceConnection].cold.1
+ +[NSXPCInterface(SFLService) _SFL_serviceInterface].cold.1
+ +[SFLDefaults shared].cold.1
+ +[SFLDefaults standardDefaults].cold.1
+ +[SFLGenericList initializationQueue].cold.1
+ +[SFLList(LSSharedFileListSupport) itemByInsertingAfterItem:name:URL:propertiesToSet:propertiesToClear:list:].cold.1
+ +[SFLList(LSSharedFileListSupport) itemByInsertingAfterItem:name:URL:propertiesToSet:propertiesToClear:list:].cold.2
+ +[SFLList(LSSharedFileListSupport) itemByInsertingAfterItem:name:URL:propertiesToSet:propertiesToClear:list:].cold.3
+ +[SFLList(LSSharedFileListSupport) itemByInsertingAfterItem:name:bookmark:propertiesToSet:propertiesToClear:list:].cold.1
+ +[SFLList(LSSharedFileListSupport) itemByInsertingAfterItem:name:bookmark:propertiesToSet:propertiesToClear:list:].cold.2
+ +[SFLList(LSSharedFileListSupport) itemByInsertingAfterItem:name:bookmark:propertiesToSet:propertiesToClear:list:].cold.3
+ +[SFLList(LSSharedFileListSupport) refreshResolvedPropertiesForItem:].cold.1
+ +[SFLList(LSSharedFileListSupport) resolveItem:resolutionFlags:URL:fsRef:].cold.1
+ +[SFLList(LSSharedFileListSupport) resolveItem:resolutionFlags:error:].cold.2
+ +[SFLList(LSSharedFileListSupport) setProperty:forName:item:].cold.1
+ +[SFLListObserver observersByList].cold.1
+ +[SFLListObserver observersSerialQueue].cold.1
+ +[SFLManager listIdentifiers].cold.1
+ +[SFLManager sharedInstance].cold.1
+ +[SFLResolveResult resultByResolvingBookmarkData:options:relativeToURL:].cold.2
+ +[_SFLItem supportedPropertyClasses].cold.1
+ -[NSURL(SFLAdditions) __sfl__displayName].cold.2
+ -[NSURL(SFLAdditions) __sfl__volumeURL].cold.2
+ -[NSURL(SFLSharePointUtil) __sfl_fileSecurity].cold.1
+ -[NSURL(SFLSharePointUtil) __sfl_isWriteable].cold.1
+ -[NSURL(SFLSharePointUtil) __sfl_supportsPermissions].cold.1
+ -[SFLBookmark resolveWithOptions:relativeToURL:completion:].cold.2
+ -[SFLGenericList _indexForInsertOfItems:afterItem:].cold.2
+ -[SFLGenericList handleListChangeNotification:].cold.1
+ -[SFLListObserver notify].cold.2
+ -[SFLLoginItem setBookmark:].cold.2
+ -[SFLLoginItem setIdentifier:].cold.2
+ -[SFLLoginItem setListIdentifier:].cold.2
+ -[SFLLoginItem setName:].cold.2
+ -[SFLLoginItem setSeed:].cold.2
+ -[SFLLoginItemListV2 _fetchItems].cold.2
+ -[SFLSharePointItem setBookmark:].cold.2
+ -[SFLSharePointItem setIdentifier:].cold.2
+ -[SFLSharePointItem setListIdentifier:].cold.2
+ -[SFLSharePointItem setName:].cold.2
+ -[SFLSharePointItem setProperties:].cold.2
+ -[SFLSharePointItem setSeed:].cold.2
+ BookmarkDataShouldResolveLocally.cold.1
+ BookmarkDataShouldResolveLocally.cold.2
+ IsCurrentProcessSandboxed.cold.1
+ LSSharedFileListAddObserver.cold.2
+ LSSharedFileListAddObserverOnQueue.cold.2
+ LSSharedFileListCopyProperty.cold.2
+ LSSharedFileListGetSeedValue.cold.2
+ LSSharedFileListInsertItemAlias.cold.2
+ LSSharedFileListInsertItemBookmark.cold.2
+ LSSharedFileListInsertItemFSRef.cold.2
+ LSSharedFileListInsertItemURL.cold.2
+ LSSharedFileListItemCopyAliasData.cold.2
+ LSSharedFileListItemCopyBookmarkData.cold.2
+ LSSharedFileListItemCopyDisplayName.cold.2
+ LSSharedFileListItemCopyIconRef.cold.2
+ LSSharedFileListItemCopyResolvedURL.cold.3
+ LSSharedFileListItemCopyResolvedURL.cold.4
+ LSSharedFileListItemGetID.cold.2
+ LSSharedFileListItemMove.cold.2
+ LSSharedFileListItemMove.cold.3
+ LSSharedFileListItemRemove.cold.2
+ LSSharedFileListItemRemove.cold.3
+ LSSharedFileListItemResolve.cold.3
+ LSSharedFileListItemResolve.cold.4
+ LSSharedFileListItemSetProperty.cold.2
+ LSSharedFileListItemUpdate.cold.2
+ LSSharedFileListRemoveAllItems.cold.2
+ LSSharedFileListRemoveObserver.cold.2
+ LSSharedFileListRemoveObserverOnQueue.cold.2
+ LSSharedFileListSetAuthorization.cold.2
+ LSSharedFileListSetProperty.cold.2
+ LSSharedFileListSetProperty.cold.3
+ URLGetBoolResourceValue.cold.1
+ URLGetBoolResourceValue.cold.2
+ _Internal_LSSharedFileListGetTypeID.cold.1
+ _Internal_LSSharedFileListItemGetTypeID.cold.1
+ _LSSharedFileListCopyListType.cold.2
+ _LSSharedFileListIsURLSharePoint.cold.2
+ _LSSharedFileListItemCopyBinding.cold.2
+ _LSSharedFileListItemSetBookmarkData.cold.2
+ _LSSharedFileListItemSetURL.cold.2
+ _LSSharedFileListVolumeIsVisibleInSidebar.cold.2
+ __28-[SFLGenericList _fetchList]_block_invoke.25.cold.2
+ __28-[SFLGenericList _fetchList]_block_invoke.25.cold.3
+ __28-[SFLGenericList _fetchList]_block_invoke.cold.1
+ __28-[SFLGenericList _fetchList]_block_invoke_2.cold.1
+ __33-[SFLGenericList _removeAllItems]_block_invoke.40.cold.2
+ __33-[SFLGenericList _removeAllItems]_block_invoke.40.cold.3
+ __33-[SFLGenericList _removeAllItems]_block_invoke.cold.1
+ __33-[SFLGenericList _removeAllItems]_block_invoke_2.cold.1
+ __36-[SFLGenericList _updateItem:error:]_block_invoke.41.cold.1
+ __36-[SFLGenericList _updateItem:error:]_block_invoke.42.cold.2
+ __36-[SFLGenericList _updateItem:error:]_block_invoke.42.cold.3
+ __36-[SFLGenericList _updateItem:error:]_block_invoke.cold.1
+ __36-[SFLLoginItemList _notifyObservers]_block_invoke.cold.2
+ __37-[SFLSharePointList _notifyObservers]_block_invoke.cold.2
+ __38-[SFLLoginItemListV2 _notifyObservers]_block_invoke.cold.2
+ __42-[SFLGenericList _moveItem:toIndex:error:]_block_invoke.36.cold.2
+ __42-[SFLGenericList _moveItem:toIndex:error:]_block_invoke.36.cold.3
+ __42-[SFLGenericList _moveItem:toIndex:error:]_block_invoke.cold.1
+ __42-[SFLGenericList _moveItem:toIndex:error:]_block_invoke_3.cold.1
+ __44-[SFLGenericList _insertItem:atIndex:error:]_block_invoke.34.cold.2
+ __44-[SFLGenericList _insertItem:atIndex:error:]_block_invoke.34.cold.3
+ __44-[SFLGenericList _insertItem:atIndex:error:]_block_invoke.cold.1
+ __44-[SFLGenericList _insertItem:atIndex:error:]_block_invoke_3.cold.1
+ __44-[SFLGenericList _moveItem:afterItem:error:]_block_invoke.cold.1
+ __46-[SFLGenericList _insertItem:afterItem:error:]_block_invoke.cold.1
+ __47-[SFLGenericList _notifyObserversListDidChange]_block_invoke.cold.2
+ __47-[_SFLItemWrapper initWithItem:listIdentifier:]_block_invoke.7.cold.1
+ __47-[_SFLItemWrapper initWithItem:listIdentifier:]_block_invoke.cold.1
+ __47-[_SFLItemWrapper initWithItem:listIdentifier:]_block_invoke.cold.2
+ __47-[_SFLItemWrapper initWithItem:listIdentifier:]_block_invoke_2.cold.1
+ __47-[_SFLItemWrapper initWithItem:listIdentifier:]_block_invoke_2.cold.2
+ __50+[NSXPCConnection(SFLClient) sflServiceConnection]_block_invoke.3.cold.2
+ __50+[NSXPCConnection(SFLClient) sflServiceConnection]_block_invoke.cold.2
+ __50-[SFLGenericList _removeItemWithIdentifier:error:]_block_invoke.37.cold.2
+ __50-[SFLGenericList _removeItemWithIdentifier:error:]_block_invoke.37.cold.3
+ __50-[SFLGenericList _removeItemWithIdentifier:error:]_block_invoke.cold.1
+ __50-[SFLGenericList _removeItemWithIdentifier:error:]_block_invoke_2.cold.1
+ __64-[SFLGenericList _setPropertyValuesForKeysWithDictionary:error:]_block_invoke.47.cold.1
+ __64-[SFLGenericList _setPropertyValuesForKeysWithDictionary:error:]_block_invoke.48.cold.2
+ __64-[SFLGenericList _setPropertyValuesForKeysWithDictionary:error:]_block_invoke.48.cold.3
+ __64-[SFLGenericList _setPropertyValuesForKeysWithDictionary:error:]_block_invoke.cold.1
+ __66-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:]_block_invoke.59.cold.3
+ __66-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:]_block_invoke.59.cold.4
+ __66-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:]_block_invoke.59.cold.5
+ __66-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:]_block_invoke.59.cold.6
+ __66-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:]_block_invoke.cold.1
+ __66-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:]_block_invoke_2.cold.1
+ __77-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:completion:]_block_invoke.53.cold.3
+ __77-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:completion:]_block_invoke.53.cold.4
+ __77-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:completion:]_block_invoke.53.cold.5
+ __77-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:completion:]_block_invoke.53.cold.6
+ __77-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:completion:]_block_invoke.cold.1
+ __77-[SFLGenericList resolveItemWithIdentifier:options:relativeToURL:completion:]_block_invoke_2.cold.1
CStrings:
+ "/System/AppleInternal/Library/Frameworks/SharePointManagement.framework/SharePointManagement"

```
