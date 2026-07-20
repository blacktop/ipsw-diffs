## AddressBook

> `/System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__data`
- `__DATA.__objc_ivar`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2759.100.1.0.0
-  __TEXT.__text: 0x1022f8
-  __TEXT.__objc_methlist: 0x17d94
-  __TEXT.__const: 0x330
+2761.100.1.0.0
+  __TEXT.__text: 0x103994
+  __TEXT.__objc_methlist: 0x17e34
+  __TEXT.__const: 0x340
   __TEXT.__gcc_except_tab: 0x1718
-  __TEXT.__cstring: 0x9b96
-  __TEXT.__ustring: 0x39c
+  __TEXT.__cstring: 0x9bc0
+  __TEXT.__ustring: 0x466
   __TEXT.__dlopen_cstrs: 0xdbe
-  __TEXT.__oslogstring: 0xa4b
-  __TEXT.__unwind_info: 0x5498
+  __TEXT.__oslogstring: 0xae8
+  __TEXT.__unwind_info: 0x54a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10a0
-  __DATA_CONST.__objc_classlist: 0xf00
+  __DATA_CONST.__const: 0x10c0
+  __DATA_CONST.__objc_classlist: 0xf10
   __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x300
+  __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbe58
+  __DATA_CONST.__objc_selrefs: 0xbec0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x990
-  __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0x1bf8
-  __AUTH_CONST.__const: 0x43e0
-  __AUTH_CONST.__cfstring: 0x8e60
-  __AUTH_CONST.__objc_const: 0x25208
+  __DATA_CONST.__objc_superrefs: 0x9a0
+  __DATA_CONST.__objc_arraydata: 0x150
+  __DATA_CONST.__got: 0x1c18
+  __AUTH_CONST.__const: 0x43f0
+  __AUTH_CONST.__cfstring: 0x8e80
+  __AUTH_CONST.__objc_const: 0x25438
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x580
-  __AUTH.__objc_data: 0x7a80
+  __AUTH.__objc_data: 0x7b20
   __AUTH.__data: 0x120
   __DATA.__objc_ivar: 0x144c
-  __DATA.__data: 0x2538
-  __DATA.__bss: 0x1268
+  __DATA.__data: 0x2598
+  __DATA.__bss: 0x1278
   __DATA_DIRTY.__objc_data: 0x1b80
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x280

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SecurityFoundation.framework/Versions/A/SecurityFoundation
   - /System/Library/Frameworks/SecurityInterface.framework/Versions/A/SecurityInterface
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AddressBookCore.framework/Versions/A/AddressBookCore
   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/Versions/A/ContactsFoundation
   - /System/Library/PrivateFrameworks/ContactsPersistence.framework/Versions/A/ContactsPersistence

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8137
-  Symbols:   19243
-  CStrings:  1651
+  Functions: 8148
+  Symbols:   19283
+  CStrings:  1657
 
Symbols:
+ +[ABPersonListDragExportHelper log]
+ -[ABContactDragProvider .cxx_destruct]
+ -[ABContactDragProvider auxiliaryPasteboardData]
+ -[ABContactDragProvider pasteboardPropertyListForType:]
+ -[ABContactDragProvider setAuxiliaryPasteboardData:]
+ -[ABContactDragProvider writableTypesForPasteboard:]
+ -[ABContactDragProvider writingOptionsForType:pasteboard:]
+ -[ABGroupListController currentDragIsOptionDrag]
+ -[ABGroupListController outlineView:draggingSession:willBeginAtPoint:forItems:]
+ -[ABGroupListController outlineView:pasteboardWriterForItem:]
+ -[ABGroupListController setCurrentDragIsOptionDrag:]
+ -[ABGroupListView beginDraggingSessionWithItems:event:source:]
+ -[ABGroupOptionDragExpansion .cxx_destruct]
+ -[ABGroupOptionDragExpansion filePromiseProvider:fileNameForType:]
+ -[ABGroupOptionDragExpansion filePromiseProvider:writePromiseToURL:completionHandler:]
+ -[ABGroupOptionDragExpansion providers]
+ -[ABGroupOptionDragExpansion setProviders:]
+ -[ABMainListOutlineView beginDraggingSessionWithItems:event:source:]
+ -[ABPersonListController _auxiliaryDragPasteboardDataForEntries:]
+ -[ABPersonListController outlineView:draggingSession:willBeginAtPoint:forItems:]
+ -[ABPersonListController outlineView:pasteboardWriterForItem:]
+ -[ABPersonListDragExportHelper filePromiseProvider:fileNameForType:]
+ -[ABPersonListDragExportHelper filePromiseProvider:writePromiseToURL:completionHandler:]
+ -[ABPersonListDragExportHelper initWithPersonIdentifiers:names:shouldUnify:]
+ -[ABPersonListDragExportHelper operationQueueForFilePromiseProvider:]
+ -[ABPersonListDragExportHelper suggestedFilename]
+ -[ABPersonListDragExportHelper writeToURL:completionHandler:]
+ -[ABPersonListRowView setFloating:]
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table52
+ OBJC_IVAR_$_ABContactDragProvider._auxiliaryPasteboardData
+ OBJC_IVAR_$_ABGroupListController._currentDragIsOptionDrag
+ OBJC_IVAR_$_ABGroupOptionDragExpansion._providers
+ OBJC_IVAR_$_ABPersonListDragExportHelper._operationQueue
+ OBJC_IVAR_$_ABPersonListDragExportHelper._shouldUnify
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_ABContactDragProvider
+ _OBJC_CLASS_$_ABGroupOptionDragExpansion
+ _OBJC_CLASS_$_NSDraggingItem
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSFilePromiseProvider
+ _OBJC_METACLASS_$_ABContactDragProvider
+ _OBJC_METACLASS_$_ABGroupOptionDragExpansion
+ _OBJC_METACLASS_$_NSFilePromiseProvider
+ _UTTypeVCard
+ __OBJC_$_CLASS_METHODS_ABPersonListDragExportHelper
+ __OBJC_$_INSTANCE_METHODS_ABContactDragProvider
+ __OBJC_$_INSTANCE_METHODS_ABGroupOptionDragExpansion
+ __OBJC_$_INSTANCE_METHODS_ABPersonListRowView
+ __OBJC_$_INSTANCE_VARIABLES_ABContactDragProvider
+ __OBJC_$_INSTANCE_VARIABLES_ABGroupOptionDragExpansion
+ __OBJC_$_PROP_LIST_ABContactDragProvider
+ __OBJC_$_PROP_LIST_ABGroupOptionDragExpansion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSFilePromiseProviderDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSFilePromiseProviderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSFilePromiseProviderDelegate
+ __OBJC_$_PROTOCOL_REFS_NSFilePromiseProviderDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ABGroupOptionDragExpansion
+ __OBJC_CLASS_PROTOCOLS_$_ABPersonListDragExportHelper
+ __OBJC_CLASS_RO_$_ABContactDragProvider
+ __OBJC_CLASS_RO_$_ABGroupOptionDragExpansion
+ __OBJC_LABEL_PROTOCOL_$_NSFilePromiseProviderDelegate
+ __OBJC_METACLASS_RO_$_ABContactDragProvider
+ __OBJC_METACLASS_RO_$_ABGroupOptionDragExpansion
+ __OBJC_PROTOCOL_$_NSFilePromiseProviderDelegate
+ ___35+[ABPersonListDragExportHelper log]_block_invoke
+ ___62-[ABGroupListView beginDraggingSessionWithItems:event:source:]_block_invoke
+ ___68-[ABMainListOutlineView beginDraggingSessionWithItems:event:source:]_block_invoke
+ ___block_descriptor_32_e14_"NSArray"8?0l
+ _objc_msgSend$_auxiliaryDragPasteboardDataForEntries:
+ _objc_msgSend$auxiliaryPasteboardData
+ _objc_msgSend$currentDragIsOptionDrag
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$initWithFileType:delegate:
+ _objc_msgSend$initWithPasteboardWriter:
+ _objc_msgSend$initWithPersonIdentifiers:names:shouldUnify:
+ _objc_msgSend$item
+ _objc_msgSend$numberOfSelectedRows
+ _objc_msgSend$providers
+ _objc_msgSend$setAuxiliaryPasteboardData:
+ _objc_msgSend$setCurrentDragIsOptionDrag:
+ _objc_msgSend$setDraggingFormation:
+ _objc_msgSend$setDraggingFrame:contents:
+ _objc_msgSend$setFloating:
+ _objc_msgSend$setImageComponentsProvider:
+ _objc_msgSend$setProviders:
+ _objc_msgSend$setQualityOfService:
+ _objc_msgSend$setUserInfo:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$stringByReplacingUnsafePathCharactersInString:
+ _objc_msgSend$suggestedFilename
+ _objc_msgSend$uniqueIdForDrag
+ _objc_msgSend$vCardDataForContacts:error:
+ _objc_msgSend$writeToURL:completionHandler:
+ _objc_msgSend$writeToURL:options:error:
- -[ABGroupListController canDragEntries:]
- -[ABGroupListController dragHelper]
- -[ABGroupListController outlineView:namesOfPromisedFilesDroppedAtDestination:forDraggedItems:]
- -[ABGroupListController outlineView:writeItems:toPasteboard:]
- -[ABGroupListController pasteboard:provideDataForType:]
- -[ABGroupListController pasteboardChangedOwner:]
- -[ABGroupListController setDragHelper:]
- -[ABGroupListView dragImageForRowsWithIndexes:tableColumns:event:offset:]
- -[ABMainListOutlineView dragImageForRowsWithIndexes:tableColumns:event:offset:]
- -[ABPersonListController outlineView:draggingSession:endedAtPoint:operation:]
- -[ABPersonListController outlineView:namesOfPromisedFilesDroppedAtDestination:forDraggedItems:]
- -[ABPersonListController outlineView:writeItems:toPasteboard:]
- -[ABPersonListDragExportHelper destinationFolder]
- -[ABPersonListDragExportHelper filenameFromNames:]
- -[ABPersonListDragExportHelper initWithPersonIdentifiers:names:options:]
- -[ABPersonListDragExportHelper nameOfSingleFile]
- -[ABPersonListDragExportHelper namesOfIndividualFiles]
- -[ABPersonListDragExportHelper namesOfPendingFiles]
- -[ABPersonListDragExportHelper people]
- -[ABPersonListDragExportHelper serializePeople]
- -[ABPersonListDragExportHelper setDestinationFolder:]
- -[ABPersonListDragExportHelper shouldUnify]
- -[ABPersonListDragExportHelper singleCard]
- GCC_except_table137
- GCC_except_table139
- GCC_except_table55
- OBJC_IVAR_$_ABGroupListController._dragHelper
- OBJC_IVAR_$_ABPersonListController._dragExportHelper
- OBJC_IVAR_$_ABPersonListDragExportHelper._destinationFolder
- OBJC_IVAR_$_ABPersonListDragExportHelper._options
- OBJC_IVAR_$_ABPersonListDragExportHelper._people
- _OBJC_CLASS_$_CNArchiver
- ___54-[ABPersonListDragExportHelper namesOfIndividualFiles]_block_invoke
- ___62-[ABPersonListController outlineView:writeItems:toPasteboard:]_block_invoke
- ___block_descriptor_40_e8_32s_e18_16?0"NSString"8l
- _kUTTypeVCard
- _objc_msgSend$destinationFolder
- _objc_msgSend$dragHelper
- _objc_msgSend$encodeObject:error:
- _objc_msgSend$filenameFromNames:
- _objc_msgSend$initWithListViewController:entries:pasteboard:
- _objc_msgSend$initWithPersonIdentifiers:names:options:
- _objc_msgSend$isFileURL
- _objc_msgSend$lastPathComponent
- _objc_msgSend$makeDragHelper:
- _objc_msgSend$nameOfSingleFile
- _objc_msgSend$namesOfIndividualFiles
- _objc_msgSend$namesOfPendingFiles
- _objc_msgSend$namesOfPromisedFilesDroppedAtDestination:
- _objc_msgSend$pathWithNames:inDirectory:
- _objc_msgSend$serializePeople
- _objc_msgSend$setDestinationFolder:
- _objc_msgSend$setDragHelper:
- _objc_msgSend$shouldUnify
- _objc_msgSend$singleCard
- _objc_msgSend$writeItems
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBook/ABUserActivityRestoration.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBookUI/ABAllSmartGroup.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBookUI/ABBindingsValueTransformers.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.f1GUfM/Sources/AddressBook/Framework/AddressBookUI/ABLastImportGroup.m"
+ "ABGroupListView.m"
+ "ABGroupOptionDragExpansion sentinel should never be written — it must be expanded by ABGroupListView"
+ "Failed to fetch contacts for vCard export: %{public}@"
+ "Failed to get vCard data for %lu contacts: %{public}@"
+ "Failed to write vCard to %{private}@: %{public}@"
+ "com.apple.contacts.addressbook"
+ "drag-export"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBook/ABUserActivityRestoration.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBookUI/ABAllSmartGroup.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBookUI/ABBindingsValueTransformers.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbS6dV/Sources/AddressBook/Framework/AddressBookUI/ABLastImportGroup.m"
- "_blendedRowIndexes"
```
