## NanoMediaRemote

> `/System/Library/PrivateFrameworks/NanoMediaRemote.framework/NanoMediaRemote`

```diff

-2022.500.7.0.0
-  __TEXT.__text: 0x15dc
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_methlist: 0xe0
-  __TEXT.__cstring: 0x2b6
-  __TEXT.__const: 0x18
-  __TEXT.__oslogstring: 0x221
-  __TEXT.__unwind_info: 0x98
+2023.100.45.0.0
+  __TEXT.__text: 0x990
+  __TEXT.__auth_stubs: 0x180
+  __TEXT.__objc_methlist: 0xd4
+  __TEXT.__cstring: 0x13d
+  __TEXT.__unwind_info: 0x80
   __TEXT.__objc_classname: 0x23
-  __TEXT.__objc_methname: 0x713
-  __TEXT.__objc_methtype: 0x51
-  __TEXT.__objc_stubs: 0x6e0
-  __DATA_CONST.__got: 0x88
+  __TEXT.__objc_methname: 0x51c
+  __TEXT.__objc_methtype: 0x46
+  __TEXT.__objc_stubs: 0x460
+  __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x200
+  __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x140
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x320
+  __AUTH_CONST.__auth_got: 0xc8
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__cfstring: 0x2a0
   __AUTH_CONST.__objc_const: 0x1f8
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 350CB5CA-7C13-3E1E-A55B-9C70C4FD467B
-  Functions: 30
-  Symbols:   203
-  CStrings:  167
+  UUID: 2BD2A3BC-01A1-3D53-9629-BEEF1801A0A3
+  Functions: 16
+  Symbols:   123
+  CStrings:  113
 
Symbols:
- -[NMRAppLaunchInfo _shouldLaunchPlaybackAppForRoute:]
- _NMDeviceIsTinker
- _NMDeviceIsTinker.cold.1
- _NMDeviceIsTinker.isAltAccount
- _NMDeviceIsTinker.onceToken
- _NMLogForCategory
- _NMLogForCategory.cold.1
- _NMLogForCategory.logObjects
- _NMLogForCategory.onceToken
- _NRDevicePropertyIsAltAccount
- _NSSearchPathForDirectoriesInDomains
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_NSKeyedArchiver
- _OBJC_CLASS_$_NSKeyedUnarchiver
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSString
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- __NMCachedActivePairedDeviceValueForProperty
- __NMCachedActivePairedDeviceValueForProperty.cold.1
- __NMCachedActivePairedDeviceValueForProperty.cold.2
- __NMCachedActivePairedDeviceValueForProperty.cold.3
- __NMCachedActivePairedDeviceValueForProperty.cold.4
- ___NMDeviceIsTinker_block_invoke
- ___NMLogForCategory_block_invoke
- ___kCFBooleanFalse
- __os_feature_enabled_impl
- __os_log_error_impl
- __os_log_impl
- _objc_msgSend$_shouldLaunchPlaybackAppForRoute:
- _objc_msgSend$activePairedDeviceSelectorBlock
- _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
- _objc_msgSend$boolValue
- _objc_msgSend$copy
- _objc_msgSend$dataWithContentsOfFile:options:error:
- _objc_msgSend$defaultManager
- _objc_msgSend$dictionary
- _objc_msgSend$fileExistsAtPath:
- _objc_msgSend$firstObject
- _objc_msgSend$getAllDevicesWithArchivedAltAccountDevicesMatching:
- _objc_msgSend$mutableCopy
- _objc_msgSend$removeItemAtPath:error:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$sharedInstance
- _objc_msgSend$stringByAppendingPathComponent:
- _objc_msgSend$stringByDeletingLastPathComponent
- _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
- _objc_msgSend$valueForProperty:
- _objc_msgSend$writeToFile:options:error:
- _objc_opt_class
- _objc_release
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_retain
- _objc_retain_x21
- _objc_retain_x25
- _objc_retain_x8
- _os_log_create
- _os_log_type_enabled
CStrings:
- "B24@0:8@16"
- "NanoAudioControl"
- "NanoMediaAPI"
- "NanoMediaAPI-Oversize"
- "NanoMediaAppActivity"
- "NanoMediaBridgeUI"
- "NanoMediaBridgeUI-Oversize"
- "NanoMediaRemote-Oversize"
- "NanoMediaTool"
- "NanoMediaUI"
- "NanoMediaUI-Oversize"
- "NanoMusicCore"
- "NanoMusicCore-Oversize"
- "NanoMusicSync"
- "NanoMusicSync-Oversize"
- "TinkerWHA"
- "[DeviceInfoCaching] Failed to archive values: %@ error: %@"
- "[DeviceInfoCaching] Failed to fetch %@ since we are missing an active device."
- "[DeviceInfoCaching] Failed to read data contents of file: %@ error: %@"
- "[DeviceInfoCaching] Failed to unarchive data: %@ error: %@"
- "[DeviceInfoCaching] Failed to write data: %@ file path: %@ error: %@"
- "[DeviceInfoCaching] Found cached property: %@ value: %@"
- "[DeviceInfoCaching] Successfully cached property: %@ value: %@ file path: %@"
- "[DeviceInfoCaching] Using fallback default value for property: %@ value: %@"
- "_shouldLaunchPlaybackAppForRoute:"
- "activeDeviceProperties"
- "activePairedDeviceSelectorBlock"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "boolValue"
- "com.apple.nanomusic"
- "copy"
- "dataWithContentsOfFile:options:error:"
- "defaultManager"
- "deviceIdentifier"
- "dictionary"
- "fileExistsAtPath:"
- "firstObject"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "hasHomeButton"
- "isAltAccount"
- "mutableCopy"
- "removeItemAtPath:error:"
- "setWithObjects:"
- "sharedInstance"
- "stringByAppendingPathComponent:"
- "stringByDeletingLastPathComponent"
- "unarchivedObjectOfClasses:fromData:error:"
- "valueForProperty:"
- "writeToFile:options:error:"

```
