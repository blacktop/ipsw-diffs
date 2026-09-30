## DocumentManager

> `/System/Library/PrivateFrameworks/DocumentManager.framework/DocumentManager`

```diff

-337.6.3.0.0
-  __TEXT.__text: 0x32130
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x2c94
-  __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x4563
-  __TEXT.__ustring: 0x644
-  __TEXT.__oslogstring: 0x2f29
-  __TEXT.__gcc_except_tab: 0x97c
-  __TEXT.__unwind_info: 0xd08
-  __TEXT.__objc_classname: 0x77b
-  __TEXT.__objc_methname: 0xa607
-  __TEXT.__objc_methtype: 0x161a
-  __TEXT.__objc_stubs: 0x7880
-  __DATA_CONST.__got: 0x5e0
-  __DATA_CONST.__const: 0x1630
+357.2.0.0.0
+  __TEXT.__text: 0x349b0
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x2d8c
+  __TEXT.__const: 0x170
+  __TEXT.__cstring: 0x4b79
+  __TEXT.__ustring: 0x6a2
+  __TEXT.__oslogstring: 0x2fd8
+  __TEXT.__gcc_except_tab: 0x9b8
+  __TEXT.__unwind_info: 0xd50
+  __TEXT.__objc_classname: 0x789
+  __TEXT.__objc_methname: 0xab27
+  __TEXT.__objc_methtype: 0x16ab
+  __TEXT.__objc_stubs: 0x7be0
+  __DATA_CONST.__got: 0x630
+  __DATA_CONST.__const: 0x1670
   __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_catlist: 0x50
+  __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2840
+  __DATA_CONST.__objc_selrefs: 0x29d0
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x458
-  __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0x36c0
-  __AUTH_CONST.__objc_const: 0x43e0
+  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x40c0
+  __AUTH_CONST.__objc_const: 0x4528
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x284
+  __DATA.__objc_ivar: 0x288
   __DATA.__data: 0x950
-  __DATA.__bss: 0xc9
+  __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv
   - /System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AD97E55B-6224-364A-ABFB-FD879974BE18
-  Functions: 1200
-  Symbols:   4640
-  CStrings:  3037
+  UUID: 10F44223-CBE6-3D5A-9D5D-042DC946AEE5
+  Functions: 1229
+  Symbols:   4747
+  CStrings:  3261
 
Symbols:
+ +[DOCItemBookmark isAnyNodeAFault:]
+ +[DOCKeyboardFocusManager topFirstResponder:]
+ -[DOCConcreteLocation encodeWithCoder:].cold.1
+ -[DOCDownloadSettingsItem(UI_Extensions) isDefaultFolder]
+ -[DOCDownloadSettingsItem(UI_Extensions) isLocalStorageDomain]
+ -[DOCDownloadSettingsItem(UI_Extensions) isiCloudDriveDomain]
+ -[DOCDownloadSettingsItem(UI_Extensions) localizedSubtitle]
+ -[DOCDownloadSettingsItem(UI_Extensions) localizedTitle]
+ -[DOCDownloadSettingsItem(UI_Extensions) providerIcon]
+ -[DOCItemBookmark initWithBookmarkableString:node:]
+ -[DOCItemBookmark initWithCoder:].cold.1
+ -[DOCItemBookmark initWithURL:node:]
+ -[DOCItemBookmark initWithURL:node:].cold.1
+ -[DOCItemBookmark initWithURL:node:].cold.2
+ -[DOCItemBookmark node]
+ -[DOCItemBookmark setNode:]
+ -[DOCKeyCommandController _commandWithTitle:discoverabilityTitle:image:action:alternates:]
+ -[DOCKeyCommandController _keyCommandWithTitle:discoverabilityTitle:image:action:input:modifierFlags:attributes:alternates:]
+ -[DOCKeyCommandController _keyCommandsInMenu:]
+ -[DOCKeyCommandController allKeyCommandsWithAction:attributes:]
+ -[DOCKeyCommandController buildWithBuilder:].cold.2
+ -[DOCKeyCommandController buildWithBuilder:].cold.3
+ -[DOCKeyCommandController buildWithBuilder:].cold.4
+ -[DOCKeyboardFocusManager currentlyFocused].cold.1
+ -[DOCKeyboardFocusManager requestCurrentFocus:].cold.1
+ -[DOCSBFolderManager(UI_Extensions) thumbnailImageForFolder:URL:size:scale:options:]
+ -[NSXPCConnection(DOCAdditions) doc_hasSandboxAccessToFile:readonly:]
+ -[NSXPCConnection(DOCAdditions) doc_hasSandboxAccessToFile:readonly:].cold.1
+ -[UIDocumentBrowserViewController _core_didTriggerDocumentCreationIntent:]
+ -[UIDocumentBrowserViewController _didTriggerDocumentCreationIntent:]
+ -[UIDocumentBrowserViewController _iOS_didTriggerDocumentCreationIntent:]
+ -[UIDocumentBrowserViewController browserHostedCreateDocumentsMenu]
+ -[UIDocumentBrowserViewController setBrowserHostedCreateDocumentsMenu:]
+ GCC_except_table143
+ GCC_except_table155
+ GCC_except_table164
+ GCC_except_table172
+ GCC_except_table173
+ GCC_except_table180
+ GCC_except_table2
+ GCC_except_table205
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table315
+ GCC_except_table34
+ _CGContextFillRect
+ _CGContextSetFillColorWithColor
+ _DOCItemCollectionViewBeginTypeSelect
+ _DOCLogHandle
+ _DOCScaledThumbnailCornerRadius
+ _DOCUIDeferredMenuIdentifierOpenWith
+ _DOCUserDefaultsTimestampOfLastCallToImportToDefaultLocationSPI
+ _OBJC_CLASS_$_DOCDownloadSettingsItem
+ _OBJC_CLASS_$_DOCSBFolderManager
+ _OBJC_CLASS_$_FIDSNode
+ _OBJC_CLASS_$_FINode
+ _OBJC_CLASS_$_UIDeferredMenuElement
+ _OBJC_CLASS_$_UIGraphicsImageRenderer
+ _OBJC_CLASS_$_UIGraphicsImageRendererFormat
+ _OBJC_IVAR_$_DOCItemBookmark._node
+ _OBJC_IVAR_$_UIDocumentBrowserViewController._browserHostedCreateDocumentsMenu
+ _UIDocumentBrowserActionIdentifierAddToDock
+ _UIDocumentBrowserActionIdentifierCopyiCloudLink
+ _UIDocumentBrowserActionIdentifierCreateiCloudLink
+ _UIDocumentBrowserActionIdentifierFolderCustomization
+ _UIDocumentBrowserActionIdentifierRevealInFiles
+ _UIKeyInputDelete
+ _UIMenuApplication
+ _UIMenuClose
+ _UIMenuPreferences
+ _UIMenuToolbar
+ __OBJC_$_CATEGORY_DOCDownloadSettingsItem_$_UI_Extensions
+ __OBJC_$_CATEGORY_DOCSBFolderManager_$_UI_Extensions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_DOCDownloadSettingsItem_$_UI_Extensions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_DOCSBFolderManager_$_UI_Extensions
+ __OBJC_$_PROP_LIST_DOCDownloadSettingsItem_$_UI_Extensions
+ ___36-[DOCItemBookmark initWithURL:node:]_block_invoke
+ ___71-[UIDocumentBrowserViewController setBrowserHostedCreateDocumentsMenu:]_block_invoke
+ ___74-[UIDocumentBrowserViewController _core_didTriggerDocumentCreationIntent:]_block_invoke
+ ___78-[UIDocumentBrowserViewController _iOS_didRequestDocumentCreationWithHandler:]_block_invoke_2
+ ___84-[DOCSBFolderManager(UI_Extensions) thumbnailImageForFolder:URL:size:scale:options:]_block_invoke
+ ___block_descriptor_64_e8_32s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8
+ ___block_literal_global.190
+ ___block_literal_global.756
+ _objc_msgSend$CGContext
+ _objc_msgSend$_beginTypeSelectWithInput:
+ _objc_msgSend$_commandWithTitle:discoverabilityTitle:image:action:alternates:
+ _objc_msgSend$_core_didTriggerDocumentCreationIntent:
+ _objc_msgSend$_iOS_didTriggerDocumentCreationIntent:
+ _objc_msgSend$_keyCommandWithTitle:discoverabilityTitle:image:action:input:modifierFlags:attributes:alternates:
+ _objc_msgSend$_keyCommandsInMenu:
+ _objc_msgSend$_setBrowserHostedCreateDocumentsMenu:
+ _objc_msgSend$allKeyCommandsWithAction:attributes:
+ _objc_msgSend$browserHostedCreateDocumentsMenu
+ _objc_msgSend$characters
+ _objc_msgSend$children
+ _objc_msgSend$commandWithTitle:image:action:propertyList:alternates:
+ _objc_msgSend$drawInRect:
+ _objc_msgSend$elementUsingFocusWithIdentifier:shouldCacheItems:
+ _objc_msgSend$folderType
+ _objc_msgSend$fpItem
+ _objc_msgSend$imageWithActions:
+ _objc_msgSend$initWithCGImage:
+ _objc_msgSend$initWithSize:format:
+ _objc_msgSend$initWithType:
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$menuByReplacingChildren:
+ _objc_msgSend$providerDomain
+ _objc_msgSend$redColor
+ _objc_msgSend$replaceMenuForIdentifier:withMenu:
+ _objc_msgSend$setBrowserHostedCreateDocumentsMenu:
+ _objc_msgSend$setScale:
+ _objc_msgSend$size
- +[DOCItemBookmark isAnyFPItemAFault:]
- -[DOCItemBookmark fileProviderItem]
- -[DOCItemBookmark initWithBookmarkableString:fileProviderItem:]
- -[DOCItemBookmark initWithURL:fileProviderItem:]
- -[DOCItemBookmark initWithURL:fileProviderItem:].cold.1
- -[DOCItemBookmark initWithURL:fileProviderItem:].cold.2
- -[DOCItemBookmark setFileProviderItem:]
- -[DOCKeyCommandController allKeyCommandsWithAction:]
- -[NSXPCConnection(DOCAdditions) doc_hasSandboxAccessToFile:]
- -[NSXPCConnection(DOCAdditions) doc_hasSandboxAccessToFile:].cold.1
- GCC_except_table1
- GCC_except_table153
- GCC_except_table162
- GCC_except_table169
- GCC_except_table170
- GCC_except_table178
- GCC_except_table203
- GCC_except_table212
- GCC_except_table214
- GCC_except_table23
- GCC_except_table27
- GCC_except_table307
- _OBJC_IVAR_$_DOCItemBookmark._fileProviderItem
- ___44-[DOCKeyCommandController buildWithBuilder:]_block_invoke
- ___48-[DOCItemBookmark initWithURL:fileProviderItem:]_block_invoke
- ___block_descriptor_32_e25_B24?08"NSDictionary"16l
- ___block_literal_global.189
- ___block_literal_global.746
- _objc_msgSend$allKeyCommandsWithAction:
- _objc_msgSend$setFileProviderItem:
CStrings:
+ "%@ nosw=%@"
+ "%s decoding DOCItemBookmark node failed with exception: %@"
+ "%s: _currentlyFocused: %@"
+ "%s: accepted and became success: %@"
+ "-[DOCItemBookmark initWithCoder:]"
+ "-[DOCKeyboardFocusManager currentlyFocused]"
+ "-[DOCKeyboardFocusManager requestCurrentFocus:]"
+ "@\"UIMenu\""
+ "@32@0:8:16Q24"
+ "@56@0:8@16@24@32:40@48"
+ "@64@0:8@16@24{CGSize=dd}32d48@56"
+ "@80@0:8@16@24@32:40@48q56Q64@72"
+ "Add to Dock"
+ "Add to Favorites"
+ "B28@0:8@16B24"
+ "Back"
+ "Browse"
+ "CGContext"
+ "Copy as Pathname"
+ "DOCUserDefaultsTimestampOfLastCallToImportToDefaultLocationSPI"
+ "Date"
+ "Date Created"
+ "Date Last Opened"
+ "Date Modified"
+ "Delete All Recently Deleted"
+ "Desktop"
+ "DocumentManager service tried to send a message to a deallocated host proxy: %@"
+ "Documents"
+ "Downloads"
+ "Enclosing Folder"
+ "Enclosing Folder in New Window"
+ "Expecting 1 submenu in Application menu"
+ "Expecting 3 submenus in Edit menu"
+ "Expecting 7 submenus in File menu"
+ "Forward"
+ "Group By"
+ "Kind"
+ "Name"
+ "None"
+ "Open With"
+ "S"
+ "Sandbox check returned error. readonly: %d errno=%d"
+ "Scan Documents"
+ "Shared by"
+ "Show View Options"
+ "Size"
+ "Skipped encoding FINode root node for %@"
+ "Sort By"
+ "Sort by Date Created"
+ "Sort by Date Last Opened"
+ "Sort by Date Modified"
+ "T@\"UIImage\",R"
+ "T@\"UIMenu\",&,N,V_browserHostedCreateDocumentsMenu"
+ "Tags"
+ "UI_Extensions"
+ "View as Columns"
+ "_beginTypeSelectWithInput:"
+ "_browserHostedCreateDocumentsMenu"
+ "_commandWithTitle:discoverabilityTitle:image:action:alternates:"
+ "_core_didTriggerDocumentCreationIntent:"
+ "_didTriggerDocumentCreationIntent:"
+ "_iOS_didTriggerDocumentCreationIntent:"
+ "_keyCommandWithTitle:discoverabilityTitle:image:action:input:modifierFlags:attributes:alternates:"
+ "_keyCommandsInMenu:"
+ "_setBrowserHostedCreateDocumentsMenu:"
+ "allKeyCommandsWithAction:attributes:"
+ "arrow.down.circle"
+ "arrow.forward.folder"
+ "arrow.up.arrow.down"
+ "arrow.up.forward.app"
+ "arrow.uturn.backward"
+ "arrow.uturn.forward"
+ "as Columns"
+ "as Icons"
+ "as List"
+ "browserHostedCreateDocumentsMenu"
+ "character.textbox"
+ "characters"
+ "chevron.backward"
+ "chevron.forward"
+ "children"
+ "clock"
+ "com.apple.DocumentManager.action.addToDock"
+ "com.apple.DocumentManager.action.copyiCloudLink"
+ "com.apple.DocumentManager.action.createiCloudLink"
+ "com.apple.DocumentManager.action.folderCustomization"
+ "com.apple.DocumentManager.action.revealInFiles"
+ "com.apple.DocumentManager.menu.main.file.openwith-deferred"
+ "commandWithTitle:image:action:propertyList:alternates:"
+ "doc.viewfinder"
+ "doc_hasSandboxAccessToFile:readonly:"
+ "dock.arrow.down.rectangle"
+ "document"
+ "document.on.clipboard"
+ "drawInRect:"
+ "eject"
+ "elementUsingFocusWithIdentifier:shouldCacheItems:"
+ "eye"
+ "false"
+ "file-read-data"
+ "folder.badge.person.crop"
+ "folder.badge.plus"
+ "folderType"
+ "fpItem"
+ "gearshape"
+ "h"
+ "iCloud Drive"
+ "icloud"
+ "imageWithActions:"
+ "info.circle"
+ "initWithBookmarkableString:node:"
+ "initWithCGImage:"
+ "initWithSize:format:"
+ "initWithType:"
+ "initWithURL:node:"
+ "isAnyNodeAFault:"
+ "isDefaultFolder"
+ "isLocalStorageDomain"
+ "isiCloudDriveDomain"
+ "j"
+ "list.bullet"
+ "localizedStringWithFormat:"
+ "localizedSubtitle"
+ "magnifyingglass"
+ "menuByReplacingChildren:"
+ "menubar.dock.rectangle"
+ "performAddFolderToDock:"
+ "performCompress:"
+ "performCopyAsPathname:"
+ "performEmptyTrash:"
+ "performEmptyTrashNow:"
+ "performGoToEnclosingFolderInNewWindow:"
+ "performGoToOnMyDevice:"
+ "performGroupByNone:"
+ "performScanDocuments:"
+ "performShare:"
+ "performShowViewOptions:"
+ "performSortByDateCreated:"
+ "performSortByDateLastOpened:"
+ "performSortByDateModified:"
+ "providerDomain"
+ "providerIcon"
+ "rectangle.connected.to.line.below"
+ "rectangle.split.3x1"
+ "redColor"
+ "repeatBehavior"
+ "replaceMenuForIdentifier:withMenu:"
+ "setBrowserHostedCreateDocumentsMenu:"
+ "setRepeatBehavior:"
+ "setScale:"
+ "size"
+ "square.grid.2x2"
+ "square.grid.3x1.below.line.grid.1x2"
+ "star"
+ "thumbnailImageForFolder:URL:size:scale:options:"
+ "topFirstResponder:"
+ "true"
+ "v16@?0@\"UIGraphicsImageRendererContext\"8"
+ "v24@0:8@\"UIMenu\"16"
+ "zipper.page"
- "%@ FPItem=%@"
- "B24@?0@8@\"NSDictionary\"16"
- "DocumentManager service tried to send a message to a deallocated host proxy"
- "Favorite"
- "Sandbox check returned error. errno=%d"
- "Sort by Date"
- "T@\"FPItem\",&,V_fileProviderItem"
- "View as Column"
- "allKeyCommandsWithAction:"
- "doc_hasSandboxAccessToFile:"
- "initWithBookmarkableString:fileProviderItem:"
- "initWithURL:fileProviderItem:"
- "isAnyFPItemAFault:"
- "performSortByDate:"
- "setFileProviderItem:"

```
