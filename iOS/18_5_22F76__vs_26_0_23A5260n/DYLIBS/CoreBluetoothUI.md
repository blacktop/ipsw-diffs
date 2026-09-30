## CoreBluetoothUI

> `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI`

```diff

-185.7.0.0.0
-  __TEXT.__text: 0xb58
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_methlist: 0x1a8
+190.40.1.2.0
+  __TEXT.__text: 0x1aa0
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_methlist: 0x290
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xb0
+  __TEXT.__cstring: 0x253
   __TEXT.__gcc_except_tab: 0x1c
   __TEXT.__oslogstring: 0xfd
-  __TEXT.__unwind_info: 0xb8
-  __TEXT.__objc_classname: 0x6f
-  __TEXT.__objc_methname: 0x5cf
-  __TEXT.__objc_methtype: 0x177
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x58
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__objc_classname: 0x7d
+  __TEXT.__objc_methname: 0x9cf
+  __TEXT.__objc_methtype: 0x1d9
+  __TEXT.__objc_stubs: 0x940
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x28
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x178
+  __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x120
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x3e0
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x24
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x178
+  __AUTH_CONST.__cfstring: 0x320
+  __AUTH_CONST.__objc_const: 0x498
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x28
   __DATA.__data: 0xc0
   __DATA.__common: 0x10
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3627731F-EB4F-3157-94B8-65BF2169862B
-  Functions: 30
-  Symbols:   203
-  CStrings:  96
+  UUID: 2C56A37D-AE48-3D78-A825-F7F8B6C512E1
+  Functions: 48
+  Symbols:   304
+  CStrings:  195
 
Symbols:
+ +[CBAssetHelper findLocalizedStringForKey:]
+ +[CBAssetHelper findLocalizedStringForKey:default:]
+ +[CBAssetHelper getAssetPathsFilenames]
+ +[CBAssetHelper loadAllAssets]
+ +[CBAssetHelper loadAssetsFromFile:]
+ +[CBAssetHelper resourcePathFromBundle:withResourceNamed:]
+ +[CBAssetHelper sharedAssetHelper]
+ +[CBAssetHelper strFromColorID:]
+ +[CBAssetHelper strFromProductID:]
+ +[CBAssetHelper strFromVendorID:andProductID:]
+ -[CBAssetHelper .cxx_destruct]
+ -[CBAssetHelper getAssetDictForAppleProductID:]
+ -[CBAssetHelper getCustomInfoForVID:andPID:]
+ -[CBAssetHelper getDeviceDisplayName:]
+ -[CBAssetHelper getDeviceNameForAppleProductID:]
+ -[CBAssetHelper getImageURLForAppleProductID:andColor:]
+ -[CBAssetHelper getImageURLFromImageName:]
+ -[CBAssetHelper init]
+ OBJC_IVAR_$_CBAssetHelper.mDictCache
+ _NSLog
+ _OBJC_CLASS_$_CBAssetHelper
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSURL
+ _OBJC_METACLASS_$_CBAssetHelper
+ __OBJC_$_CLASS_METHODS_CBAssetHelper
+ __OBJC_$_INSTANCE_METHODS_CBAssetHelper
+ __OBJC_$_INSTANCE_VARIABLES_CBAssetHelper
+ __OBJC_CLASS_RO_$_CBAssetHelper
+ __OBJC_METACLASS_RO_$_CBAssetHelper
+ _objc_alloc_init
+ _objc_enumerationMutation
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addObject:
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$bundlePath
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionaryWithContentsOfURL:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$findLocalizedStringForKey:
+ _objc_msgSend$getAssetDictForAppleProductID:
+ _objc_msgSend$getAssetPathsFilenames
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$length
+ _objc_msgSend$loadAllAssets
+ _objc_msgSend$loadAssetsFromFile:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$pathExtension
+ _objc_msgSend$pathForResource:ofType:
+ _objc_msgSend$resourcePath
+ _objc_msgSend$resourcePathFromBundle:withResourceNamed:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$strFromColorID:
+ _objc_msgSend$strFromProductID:
+ _objc_msgSend$strFromVendorID:andProductID:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$valueForKey:
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
+ _objc_retain_x8
+ _sAssetHelper
CStrings:
+ ""
+ ".plist"
+ ".strings"
+ "0x%02X"
+ "0x%04X"
+ "0x%04X/0x%04X"
+ "@\"NSMutableDictionary\""
+ "@20@0:8C16"
+ "@20@0:8S16"
+ "@24@0:8@16"
+ "@24@0:8S16C20"
+ "@24@0:8S16S20"
+ "@32@0:8@16@24"
+ "AssetPaths"
+ "AssetPaths-"
+ "Assets"
+ "Assets-"
+ "Bundle"
+ "CBAssetHelper"
+ "CBAssetHelper: BAD PARAMS - resourcePathFromBundle:%@ withResourceNamed:%@"
+ "CBAssetHelper: INVALID BUNDLE - resourcePathFromBundle:%@ withResourceNamed:%@"
+ "CBAssetHelper: loading assets from %@: %@"
+ "CBAssetHelper: resourcePathFromBundle:%@ withResourceNamed:%@ -> %@"
+ "Clone"
+ "Color"
+ "DisplayName"
+ "ImageName"
+ "Localizable"
+ "Name"
+ "URLForResource:withExtension:"
+ "addEntriesFromDictionary:"
+ "addObject:"
+ "bundleForClass:"
+ "bundlePath"
+ "bundleWithPath:"
+ "contentsOfDirectoryAtPath:error:"
+ "countByEnumeratingWithState:objects:count:"
+ "defaultManager"
+ "dictionaryWithContentsOfURL:"
+ "dictionaryWithDictionary:"
+ "fileURLWithPath:"
+ "findLocalizedStringForKey:"
+ "findLocalizedStringForKey:default:"
+ "getAssetDictForAppleProductID:"
+ "getAssetPathsFilenames"
+ "getCustomInfoForVID:andPID:"
+ "getDeviceDisplayName:"
+ "getDeviceNameForAppleProductID:"
+ "getImageURLForAppleProductID:andColor:"
+ "getImageURLFromImageName:"
+ "hasPrefix:"
+ "hasSuffix:"
+ "isEqualToString:"
+ "isMemberOfClass:"
+ "length"
+ "loadAllAssets"
+ "loadAssetsFromFile:"
+ "localizedStringForKey:value:table:"
+ "mDictCache"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "pathExtension"
+ "pathForResource:ofType:"
+ "plist"
+ "resourcePath"
+ "resourcePathFromBundle:withResourceNamed:"
+ "setObject:forKey:"
+ "sharedAssetHelper"
+ "strFromColorID:"
+ "strFromProductID:"
+ "strFromVendorID:andProductID:"
+ "stringByDeletingLastPathComponent"
+ "stringByDeletingPathExtension"
+ "stringWithFormat:"
+ "strings"
+ "substringToIndex:"
+ "valueForKey:"

```
