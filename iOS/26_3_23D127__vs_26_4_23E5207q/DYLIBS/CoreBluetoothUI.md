## CoreBluetoothUI

> `/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI`

```diff

-193.9.0.0.0
-  __TEXT.__text: 0x1d5c
-  __TEXT.__auth_stubs: 0x2f0
+194.22.1.1.1
+  __TEXT.__text: 0x1edc
+  __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_methlist: 0x2a8
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x243
   __TEXT.__gcc_except_tab: 0x1c
   __TEXT.__oslogstring: 0x13a
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__unwind_info: 0x108
   __TEXT.__objc_classname: 0x83
   __TEXT.__objc_methname: 0xa24
   __TEXT.__objc_methtype: 0x1e7

   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x188
+  __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x4d8
   __AUTH.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3A72A621-7944-3287-9D7D-DEDB7E36F82B
-  Functions: 52
-  Symbols:   321
+  UUID: 8BA2436B-6FF5-394C-826E-B419527B7AC7
+  Functions: 51
+  Symbols:   317
   CStrings:  199
 
Symbols:
+ _objc_release_x28
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- _OUTLINED_FUNCTION_1
- _objc_claimAutoreleasedReturnValue
- _objc_release_x25
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x24
- _objc_retain_x3
Functions:
~ -[BTDevicePickerRemoteViewController discoveredDevice:deviceAddress:] : 128 -> 124
~ -[BTDevicePicker initWithTitle:service:discoveryNameFilter:] : 220 -> 216
~ -[BTDevicePicker dealloc] : 372 -> 376
~ -[BTDevicePicker show] : 272 -> 280
~ -[BTDevicePicker createAlertWindowForRootViewController:] : 700 -> 736
~ -[BTDevicePicker dismissAnimated:] : 120 -> 128
~ -[BTDevicePicker setExtension:] : 12 -> 64
~ -[BTDevicePicker setDevicePickerRemoteViewController:] : 12 -> 64
~ _OUTLINED_FUNCTION_0 : 24 -> 32
- _OUTLINED_FUNCTION_1
~ ___59-[NSMutableDictionary(Merge) mergeWith:overwriteConflicts:]_block_invoke : 220 -> 224
~ +[CBAssetHelper sharedAssetHelper] : 84 -> 92
~ +[CBAssetHelper loadAllAssets] : 360 -> 372
~ +[CBAssetHelper loadAssetsFromFile:] : 156 -> 168
~ +[CBAssetHelper resourcePathFromBundle:withResourceNamed:] : 332 -> 348
~ +[CBAssetHelper getAssetPathsFilenames] : 504 -> 524
~ +[CBAssetHelper findLocalizedStringForKey:] : 668 -> 700
~ +[CBAssetHelper findLocalizedStringForKey:default:] : 124 -> 136
~ -[CBAssetHelper init] : 104 -> 108
~ -[CBAssetHelper getCustomInfoForVID:andPID:] : 96 -> 104
~ -[CBAssetHelper getAssetDictForAppleProductID:] : 400 -> 436
~ -[CBAssetHelper getDeviceNameForAppleProductID:] : 84 -> 92
~ -[CBAssetHelper getDeviceDisplayName:] : 84 -> 92
~ -[CBAssetHelper getImageURLForAppleProductID:andColor:] : 524 -> 572
~ -[CBAssetHelper getImageURLFromImageName:] : 196 -> 212
~ ___22-[BTDevicePicker show]_block_invoke.cold.2 : 12 -> 24
~ -[BTDevicePicker dealloc].cold.2 : 36 -> 28

```
