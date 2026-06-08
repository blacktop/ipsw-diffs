## CoreBluetoothUI

> `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI`

```diff

-195.7.1.2.0
-  __TEXT.__text: 0x1edc
-  __TEXT.__auth_stubs: 0x2d0
+2700.37.0.0.0
+  __TEXT.__text: 0x1d34
   __TEXT.__objc_methlist: 0x2a8
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x243
+  __TEXT.__cstring: 0x249
   __TEXT.__gcc_except_tab: 0x1c
   __TEXT.__oslogstring: 0x13a
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x83
-  __TEXT.__objc_methname: 0xa24
-  __TEXT.__objc_methtype: 0x1e7
-  __TEXT.__objc_stubs: 0x980
-  __DATA_CONST.__got: 0x98
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x4d8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0BB0F96-3837-3622-A189-DEF0BF2B040D
+  UUID: 3E7AABFA-B235-3674-9C5D-F59BFEF1BC55
   Functions: 51
-  Symbols:   317
-  CStrings:  199
+  Symbols:   319
+  CStrings:  57
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x25
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x24
+ _objc_retain_x3
- _objc_release_x28
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
Functions:
~ -[BTDevicePickerRemoteViewController discoveredDevice:deviceAddress:] : 124 -> 128
~ -[BTDevicePicker initWithTitle:service:discoveryNameFilter:] : 216 -> 220
~ -[BTDevicePicker dealloc] : 376 -> 372
~ -[BTDevicePicker show] : 280 -> 272
~ ___22-[BTDevicePicker show]_block_invoke : 464 -> 420
~ -[BTDevicePicker createAlertWindowForRootViewController:] : 736 -> 704
~ -[BTDevicePicker dismissAnimated:] : 128 -> 120
~ -[BTDevicePicker setExtension:] : 64 -> 12
~ -[BTDevicePicker setDevicePickerRemoteViewController:] : 64 -> 12
~ ___59-[NSMutableDictionary(Merge) mergeWith:overwriteConflicts:]_block_invoke : 224 -> 220
~ +[CBAssetHelper sharedAssetHelper] : 92 -> 84
~ +[CBAssetHelper loadAllAssets] : 372 -> 364
~ +[CBAssetHelper loadAssetsFromFile:] : 168 -> 156
~ +[CBAssetHelper resourcePathFromBundle:withResourceNamed:] : 348 -> 332
~ +[CBAssetHelper getAssetPathsFilenames] : 524 -> 508
~ +[CBAssetHelper findLocalizedStringForKey:] : 700 -> 672
~ +[CBAssetHelper findLocalizedStringForKey:default:] : 136 -> 124
~ -[CBAssetHelper init] : 108 -> 104
~ -[CBAssetHelper getCustomInfoForVID:andPID:] : 104 -> 96
~ -[CBAssetHelper getAssetDictForAppleProductID:] : 436 -> 400
~ -[CBAssetHelper getDeviceNameForAppleProductID:] : 92 -> 84
~ -[CBAssetHelper getDeviceDisplayName:] : 92 -> 84
~ -[CBAssetHelper getImageURLForAppleProductID:andColor:] : 572 -> 524
~ -[CBAssetHelper getImageURLFromImageName:] : 212 -> 196
CStrings:
- ".cxx_destruct"
- "@\"<BTDevicePickerDelegate>\""
- "@\"<BTDevicePickerRemoteViewControllerHost>\""
- "@\"<NSCopying>\""
- "@\"BTDevicePickerRemoteViewController\""
- "@\"NSExtension\""
- "@\"NSMutableDictionary\""
- "@\"NSPredicate\""
- "@\"NSString\""
- "@\"UIWindow_Custom\""
- "@16@0:8"
- "@20@0:8C16"
- "@20@0:8S16"
- "@24@0:8@16"
- "@24@0:8S16C20"
- "@24@0:8S16S20"
- "@32@0:8@16@24"
- "@36@0:8@16I24@28"
- "B16@0:8"
- "BTDevicePicker"
- "BTDevicePickerRemoteViewController"
- "BTDevicePickerRemoteViewControllerHost"
- "CBAssetHelper"
- "I"
- "Merge"
- "T@\"<BTDevicePickerDelegate>\",N,V_delegate"
- "T@\"<BTDevicePickerRemoteViewControllerHost>\",W,N,V_delegate"
- "T@\"<NSCopying>\",C,N,V_extensionRequestIdentifier"
- "T@\"BTDevicePickerRemoteViewController\",&,N,V_devicePickerRemoteViewController"
- "T@\"NSExtension\",&,N,V_extension"
- "UIWindow_Custom"
- "URLForResource:withExtension:"
- "_alertWindow"
- "_delegate"
- "_devicePickerRemoteViewController"
- "_extension"
- "_extensionRequestIdentifier"
- "_predicate"
- "_service"
- "_title"
- "activationState"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObserver:selector:name:object:"
- "allWindowsIncludingInternalWindows:onlyVisibleWindows:"
- "applicationWillResignActive:"
- "bundleForClass:"
- "bundlePath"
- "bundleWithPath:"
- "cancelExtensionRequestWithIdentifier:"
- "connectedScenes"
- "contentsOfDirectoryAtPath:error:"
- "countByEnumeratingWithState:objects:count:"
- "createAlertWindowForRootViewController:"
- "dealloc"
- "defaultCenter"
- "defaultManager"
- "delegate"
- "devicePicker:didDismissWithResult:deviceAddress:"
- "devicePickerRemoteViewController"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithDictionary:"
- "didDismissWithResult:deviceAddress:"
- "discoveredDevice:deviceAddress:"
- "dismissAnimated:"
- "dismissViewControllerAnimated:completion:"
- "displayDevice:deviceAddress:"
- "enumerateKeysAndObjectsUsingBlock:"
- "evaluateWithObject:"
- "exportedInterface"
- "extension"
- "extensionRequestIdentifier"
- "extensionWithIdentifier:error:"
- "fileURLWithPath:"
- "findLocalizedStringForKey:"
- "findLocalizedStringForKey:default:"
- "firstObject"
- "getAssetDictForAppleProductID:"
- "getAssetPathsFilenames"
- "getCustomInfoForVID:andPID:"
- "getDeviceDisplayName:"
- "getDeviceNameForAppleProductID:"
- "getImageURLForAppleProductID:andColor:"
- "getImageURLFromImageName:"
- "hasPrefix:"
- "hasSuffix:"
- "init"
- "initWithTitle:service:discoveryNameFilter:"
- "initWithWindowScene:"
- "instantiateViewControllerWithInputItems:connectionHandler:"
- "interfaceWithProtocol:"
- "isEqualToString:"
- "isInternalWindow"
- "isMemberOfClass:"
- "length"
- "loadAllAssets"
- "loadAssetsFromFile:"
- "localizedStringForKey:value:table:"
- "mDictCache"
- "makeKeyAndVisible"
- "mergeWith:overwriteConflicts:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "pathExtension"
- "pathForResource:ofType:"
- "removeObserver:"
- "resourcePath"
- "resourcePathFromBundle:withResourceNamed:"
- "rootViewController"
- "serviceViewControllerInterface"
- "serviceViewControllerProxy"
- "setDelegate:"
- "setDevicePickerRemoteViewController:"
- "setExtension:"
- "setExtensionRequestIdentifier:"
- "setObject:forKey:"
- "setRootViewController:"
- "setWindowLevel:"
- "set_delegate:"
- "sharedApplication"
- "sharedAssetHelper"
- "show"
- "showBTDevicePickerWithTitle:Service:"
- "strFromColorID:"
- "strFromProductID:"
- "strFromVendorID:andProductID:"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringWithFormat:"
- "substringToIndex:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v28@0:8@\"NSString\"16I24"
- "v28@0:8@16B24"
- "v28@0:8@16I24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8q16@\"NSString\"24"
- "v32@0:8q16@24"
- "valueForKey:"
- "window"

```
