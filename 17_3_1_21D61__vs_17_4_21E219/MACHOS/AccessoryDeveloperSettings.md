## AccessoryDeveloperSettings

> `/System/Library/PreferenceBundles/AccessoryDeveloperSettings.bundle/AccessoryDeveloperSettings`

```diff

-755.3.1.0.0
-  __TEXT.__text: 0x874
-  __TEXT.__auth_stubs: 0xf0
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__objc_methname: 0x2db
-  __TEXT.__cstring: 0x1c4
-  __TEXT.__objc_classname: 0x25
-  __TEXT.__objc_methtype: 0x7e
-  __TEXT.__unwind_info: 0x7c
-  __DATA_CONST.__auth_got: 0x80
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__cfstring: 0x2a0
-  __DATA_CONST.__objc_classlist: 0x8
+760.20.1.0.0
+  __TEXT.__text: 0x1c98
+  __TEXT.__auth_stubs: 0x180
+  __TEXT.__objc_stubs: 0x960
+  __TEXT.__objc_methlist: 0x184
+  __TEXT.__const: 0x18
+  __TEXT.__gcc_except_tab: 0x40
+  __TEXT.__objc_methname: 0xb28
+  __TEXT.__cstring: 0x5df
+  __TEXT.__ustring: 0x26
+  __TEXT.__objc_classname: 0x61
+  __TEXT.__objc_methtype: 0x1ce
+  __TEXT.__unwind_info: 0xec
+  __DATA_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0xd8
-  __DATA.__objc_classrefs: 0x18
-  __DATA.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x500
+  __DATA.__objc_selrefs: 0x2e8
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x50
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11
-  Symbols:   33
-  CStrings:  57
+  Functions: 41
+  Symbols:   67
+  CStrings:  211
 
Symbols:
+ _NSLog
+ _NSURLIsDirectoryKey
+ _NSURLNameKey
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSFileCoordinator
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSTextAttachment
+ _OBJC_CLASS_$_PSSubtitleDisclosureTableCell
+ _OBJC_CLASS_$_PSTableCell
+ _OBJC_CLASS_$_UIActivityViewController
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_UIDocumentPickerViewController
+ _OBJC_CLASS_$_UIImage
+ _OBJC_METACLASS_$_PSTableCell
+ _PSAccessoryKey
+ _PSCellClassKey
+ _PSFooterTextGroupKey
+ _PSTableCellSubtitleTextKey
+ _PSValueKey
+ _UTTypeZIP
+ __Block_object_assign
+ __Block_object_dispose
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ __dispatch_main_q
+ _dispatch_async
+ _dispatch_get_global_queue
+ _objc_alloc
+ _objc_alloc_init
+ _objc_opt_class
CStrings:
+ " "
+ "#16@0:8"
+ ".zip"
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "ADSSymbolAccessorizedCell"
+ "ADSSymbolAccessorizedCell.leading"
+ "ADSSymbolAccessorizedCell.trailing"
+ "Accessory Logs"
+ "Always Update Display Asset"
+ "AlwaysUpdateAsset"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "CarPlay"
+ "CarPlayApp"
+ "Display Assets"
+ "Enable Ferrite"
+ "EnableFerrite"
+ "FERRITE_GROUP"
+ "Logs/com.apple.CarPlay"
+ "NSObject"
+ "OEMCarPlayReceiverLogCategory"
+ "OEMCarPlayReceiverLogLevel"
+ "Q16@0:8"
+ "Remove All Display Assets"
+ "Remove all CarPlay pairings after making any changes to display assets."
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "UIDocumentPickerDelegate"
+ "URLByAppendingPathComponent:isDirectory:"
+ "URLByStandardizingPath"
+ "URLsForDirectory:inDomains:"
+ "VehicleLogs.tar.gz"
+ "Vv16@0:8"
+ "When enabled only a single display asset may be selected. The display asset version will increment on every connection."
+ "^{_NSZone=}16@0:8"
+ "_carPlayLogsFolderURL"
+ "_carplayLibraryURL"
+ "_didSelectLogArchiveSpecifier:"
+ "_enumerateCurrentAccessoryLogsUsingBlock:"
+ "_enumerateCurrentOverrideAssetsUsingBlock:"
+ "_overrideAssetDestinationURLForAssetFolder:"
+ "appendAttributedString:"
+ "arrayWithObjects:count:"
+ "attributedStringWithAttachment:"
+ "autorelease"
+ "canReload"
+ "cancelled theme picker"
+ "cellStyle"
+ "class"
+ "conformsToProtocol:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "coordinateReadingItemAtURL:options:writingItemAtURL:options:error:byAccessor:"
+ "copyItemAtURL:toURL:error:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "debugDescription"
+ "defaultManager"
+ "description"
+ "detailTextLabel"
+ "doc.zipper"
+ "documentPicker:didPickDocumentAtURL:"
+ "documentPicker:didPickDocumentsAtURLs:"
+ "documentPickerWasCancelled:"
+ "dpCarPlayReceiverLogCategory"
+ "dpCarPlayReceiverLogLevel"
+ "enumerateObjectsUsingBlock:"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "failed to create %@: %@"
+ "failed to move theme asset"
+ "failed to read CarPlay logs directory %@: %@"
+ "failed to remove CarPlay library directory: %@"
+ "fileExistsAtPath:isDirectory:"
+ "firstObject"
+ "getAlwaysUpdateAssetForSpecifier:"
+ "getFerriteEnabledForSpecifier:"
+ "getResourceValue:forKey:error:"
+ "groupSpecifierWithID:"
+ "hasSuffix:"
+ "hash"
+ "imageWithTintColor:"
+ "initForOpeningContentTypes:"
+ "initWithActivityItems:applicationActivities:"
+ "initWithString:"
+ "invalid asset filename %@"
+ "invalid asset filename, not a zip file: %@"
+ "isEqual:"
+ "isEqualToString:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "lastPathComponent"
+ "leadingSymbolNamePropertyKey"
+ "moved theme asset"
+ "name"
+ "numberWithInt:"
+ "path"
+ "pathExtension"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "presentThemePickerFromSpecifier:"
+ "presentViewController:animated:completion:"
+ "presented theme asset picker"
+ "propertyForKey:"
+ "q"
+ "q16@0:8"
+ "refreshCellContentsWithSpecifier:"
+ "release"
+ "reloadSpecifiers"
+ "removeAllAssetsForSpecifier:"
+ "removeItemAtURL:error:"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "setAllowsMultipleSelection:"
+ "setAlwaysUpdateAsset:specifier:"
+ "setAttributedText:"
+ "setButtonAction:"
+ "setDelegate:"
+ "setFerriteEnabled:specifier:"
+ "setImage:"
+ "setNeedsLayout"
+ "setText:"
+ "setTextColor:"
+ "setUserInfo:"
+ "square.and.arrow.up.circle"
+ "staged"
+ "startAccessingSecurityScopedResource"
+ "stopAccessingSecurityScopedResource"
+ "superclass"
+ "systemImageNamed:"
+ "tableCellBlueTextColor"
+ "textLabel"
+ "trailingSymbolNamePropertyKey"
+ "userInfo"
+ "v20@?0@\"NSURL\"8B16"
+ "v24@0:8@\"UIDocumentPickerViewController\"16"
+ "v24@0:8@?16"
+ "v24@?0@\"NSString\"8@\"NSURL\"16"
+ "v24@?0@\"NSURL\"8@\"NSURL\"16"
+ "v32@0:8@\"UIDocumentPickerViewController\"16@\"NSArray\"24"
+ "v32@0:8@\"UIDocumentPickerViewController\"16@\"NSURL\"24"
+ "v32@?0@\"NSURL\"8Q16^B24"
+ "v8@?0"
+ "zip"
+ "zone"
- "removeObjectsInArray:"

```
