## UARPKit

> `/System/Library/PrivateFrameworks/UARPKit.framework/UARPKit`

```diff

-1338.0.21.0.2
-  __TEXT.__text: 0x11768
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0xd38
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x11a0
-  __TEXT.__gcc_except_tab: 0x788
-  __TEXT.__oslogstring: 0x212
-  __TEXT.__unwind_info: 0x4c0
+1338.0.37.0.0
+  __TEXT.__text: 0x14e4c
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0xea8
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x147b
+  __TEXT.__gcc_except_tab: 0x8cc
+  __TEXT.__oslogstring: 0x3db
+  __TEXT.__unwind_info: 0x5c0
   __TEXT.__objc_classname: 0x151
-  __TEXT.__objc_methname: 0x2fff
-  __TEXT.__objc_methtype: 0x6fa
-  __TEXT.__objc_stubs: 0x14a0
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x278
+  __TEXT.__objc_methname: 0x35f7
+  __TEXT.__objc_methtype: 0x8a5
+  __TEXT.__objc_stubs: 0x1960
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x910
+  __DATA_CONST.__objc_selrefs: 0xa88
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x10e8
+  __AUTH_CONST.__objc_const: 0x1150
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x180

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EFF013A1-51C6-33BD-9BCC-6BFF0DCEA1A1
-  Functions: 350
-  Symbols:   1124
-  CStrings:  577
+  UUID: F51C6015-55F3-36EE-9003-03869D0A60FD
+  Functions: 412
+  Symbols:   1305
+  CStrings:  663
 
Symbols:
+ -[UARPDeviceConfiguration ecidData]
+ -[UARPDeviceConfiguration setEcidData:]
+ -[UARPDeviceManager activate].cold.1
+ -[UARPDeviceManager cacheAsset:assetUUID:appendData:]
+ -[UARPDeviceManager cacheAsset:assetUUID:appendData:].cold.1
+ -[UARPDeviceManager cacheAsset:deviceEndpoint:error:]
+ -[UARPDeviceManager cacheAssetFinish:assetUUID:hashData:]
+ -[UARPDeviceManager cacheAssetFinish:assetUUID:hashData:].cold.1
+ -[UARPDeviceManager cacheAssetStart:assetUUID:]
+ -[UARPDeviceManager cacheAssetStart:assetUUID:].cold.1
+ -[UARPDeviceManager checkAssetManager:]
+ -[UARPDeviceManager clearAssetFolders]
+ -[UARPDeviceManager clearAssetFolders].cold.1
+ -[UARPDeviceManager clearEncodedMappingDatabase]
+ -[UARPDeviceManager clearEncodedMappingDatabase].cold.1
+ -[UARPDeviceManager clearPacketCaptures]
+ -[UARPDeviceManager clearPacketCaptures].cold.1
+ -[UARPDeviceManager deactivate]
+ -[UARPDeviceManager ecidData:endpointIndex:]
+ -[UARPDeviceManager ecidData:endpointIndex:componentIndex:]
+ -[UARPDeviceManager ecidData:endpointNumber:componentNumber:].cold.1
+ -[UARPDeviceManager exportSolicitedAsset:deviceEndpoint:dynamicAssetURL:].cold.2
+ -[UARPDeviceManager exportSolicitedAsset:deviceEndpoint:dynamicAssetURL:].cold.3
+ -[UARPDeviceManager exportSolicitedAsset:deviceEndpoint:dynamicAssetURL:].cold.4
+ -[UARPDeviceManager exportSolicitedAsset:deviceEndpoint:dynamicAssetURL:].cold.5
+ -[UARPDeviceManager pauseAssetManagerNotifications:]
+ -[UARPDeviceManager pauseAssetManagerNotifications:].cold.1
+ -[UARPDeviceManager pauseAssetManagerNotifications:].cold.2
+ -[UARPDeviceManager pullDynamicAsset:assetUUID:range:]
+ -[UARPDeviceManager pullDynamicAsset:assetUUID:range:].cold.1
+ -[UARPDeviceManager pullDynamicAssetFinish:assetUUID:hashData:]
+ -[UARPDeviceManager pullDynamicAssetFinish:assetUUID:hashData:].cold.1
+ -[UARPDeviceManager pullDynamicAssetStart:assetUUID:]
+ -[UARPDeviceManager pullDynamicAssetStart:assetUUID:].cold.1
+ -[UARPDeviceManager queryEncodedMappingDatabase]
+ -[UARPDeviceManager queryEncodedMappingDatabase].cold.1
+ -[UARPDeviceManager resumeAssetManagerNotifications:]
+ -[UARPDeviceManager resumeAssetManagerNotifications:].cold.1
+ -[UARPDeviceManager resumeAssetManagerNotifications:].cold.2
+ GCC_except_table104
+ GCC_except_table109
+ GCC_except_table11
+ GCC_except_table114
+ GCC_except_table119
+ GCC_except_table124
+ GCC_except_table129
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table160
+ GCC_except_table163
+ GCC_except_table166
+ GCC_except_table169
+ GCC_except_table172
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table178
+ GCC_except_table181
+ GCC_except_table19
+ GCC_except_table24
+ GCC_except_table29
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table49
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table74
+ GCC_except_table79
+ GCC_except_table84
+ GCC_except_table89
+ GCC_except_table94
+ GCC_except_table99
+ _CC_SHA512_Final
+ _CC_SHA512_Init
+ _CC_SHA512_Update
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_IVAR_$_UARPDeviceConfiguration._ecidData
+ ___29-[UARPDeviceManager activate]_block_invoke.11
+ ___29-[UARPDeviceManager activate]_block_invoke.15
+ ___29-[UARPDeviceManager activate]_block_invoke_2
+ ___29-[UARPDeviceManager activate]_block_invoke_2.cold.1
+ ___29-[UARPDeviceManager activate]_block_invoke_2.cold.2
+ ___38-[UARPDeviceManager clearAssetFolders]_block_invoke
+ ___39-[UARPDeviceManager checkAssetManager:]_block_invoke
+ ___40-[UARPDeviceManager clearPacketCaptures]_block_invoke
+ ___47-[UARPDeviceManager cacheAssetStart:assetUUID:]_block_invoke
+ ___47-[UARPDeviceManager cacheAssetStart:assetUUID:]_block_invoke_2
+ ___48-[UARPDeviceManager clearEncodedMappingDatabase]_block_invoke
+ ___48-[UARPDeviceManager queryEncodedMappingDatabase]_block_invoke
+ ___48-[UARPDeviceManager queryEncodedMappingDatabase]_block_invoke_2
+ ___52-[UARPDeviceManager pauseAssetManagerNotifications:]_block_invoke
+ ___52-[UARPDeviceManager pauseAssetManagerNotifications:]_block_invoke_2
+ ___53-[UARPDeviceManager cacheAsset:assetUUID:appendData:]_block_invoke
+ ___53-[UARPDeviceManager cacheAsset:assetUUID:appendData:]_block_invoke_2
+ ___53-[UARPDeviceManager pullDynamicAssetStart:assetUUID:]_block_invoke
+ ___53-[UARPDeviceManager pullDynamicAssetStart:assetUUID:]_block_invoke_2
+ ___53-[UARPDeviceManager resumeAssetManagerNotifications:]_block_invoke
+ ___53-[UARPDeviceManager resumeAssetManagerNotifications:]_block_invoke_2
+ ___54-[UARPDeviceManager pullDynamicAsset:assetUUID:range:]_block_invoke
+ ___54-[UARPDeviceManager pullDynamicAsset:assetUUID:range:]_block_invoke_2
+ ___57-[UARPDeviceManager cacheAssetFinish:assetUUID:hashData:]_block_invoke
+ ___57-[UARPDeviceManager cacheAssetFinish:assetUUID:hashData:]_block_invoke_2
+ ___61-[UARPDeviceManager ecidData:endpointNumber:componentNumber:]_block_invoke_2
+ ___63-[UARPDeviceManager pullDynamicAssetFinish:assetUUID:hashData:]_block_invoke
+ ___63-[UARPDeviceManager pullDynamicAssetFinish:assetUUID:hashData:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r40r_e11_v20?0B8Q12lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e18_v20?0B8"NSURL"12lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e19_v20?0B8"NSData"12lr32l8r40l8
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bytes
+ _objc_msgSend$cacheAsset:assetUUID:appendData:
+ _objc_msgSend$cacheAsset:deviceEndpoint:error:
+ _objc_msgSend$cacheAssetFinish:assetUUID:hashData:
+ _objc_msgSend$cacheAssetStart:assetUUID:
+ _objc_msgSend$closeAndReturnError:
+ _objc_msgSend$createFileAtPath:contents:attributes:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$ecidData:endpointNumber:componentNumber:
+ _objc_msgSend$endpointControllerCacheAsset:assetUUID:appendData:reply:
+ _objc_msgSend$endpointControllerCacheAssetFinish:assetUUID:hashData:reply:
+ _objc_msgSend$endpointControllerCacheAssetStart:assetUUID:reply:
+ _objc_msgSend$endpointControllerCheckAssetManager:
+ _objc_msgSend$endpointControllerClearAssets
+ _objc_msgSend$endpointControllerClearDatabase
+ _objc_msgSend$endpointControllerClearPacketCaptures
+ _objc_msgSend$endpointControllerPauseAssetManagerNotifications:reply:
+ _objc_msgSend$endpointControllerPullDynamicAsset:assetUUID:range:reply:
+ _objc_msgSend$endpointControllerPullDynamicAssetFinish:assetUUID:hashData:reply:
+ _objc_msgSend$endpointControllerPullDynamicAssetStart:assetUUID:reply:
+ _objc_msgSend$endpointControllerQueryEncodedMappingDatabase:
+ _objc_msgSend$endpointControllerResumeAssetManagerNotifications:reply:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileHandleForReadingFromURL:error:
+ _objc_msgSend$fileHandleForWritingToURL:error:
+ _objc_msgSend$fileSize
+ _objc_msgSend$path
+ _objc_msgSend$pullDynamicAsset:assetUUID:range:
+ _objc_msgSend$pullDynamicAssetFinish:assetUUID:hashData:
+ _objc_msgSend$pullDynamicAssetStart:assetUUID:
+ _objc_msgSend$readDataUpToLength:error:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$setEcidData:
+ _objc_msgSend$uarpDeviceManagerConnectionInterrupted:
+ _objc_msgSend$uarpDeviceManagerConnectionInvalidated:
+ _objc_msgSend$writeData:error:
+ _objc_release_x28
+ _objc_retainAutorelease
- -[UARPDeviceConfiguration ECIDData]
- -[UARPDeviceConfiguration setECIDData:]
- GCC_except_table103
- GCC_except_table108
- GCC_except_table113
- GCC_except_table118
- GCC_except_table123
- GCC_except_table126
- GCC_except_table13
- GCC_except_table140
- GCC_except_table143
- GCC_except_table21
- GCC_except_table26
- GCC_except_table31
- GCC_except_table36
- GCC_except_table41
- GCC_except_table48
- GCC_except_table53
- GCC_except_table58
- GCC_except_table63
- GCC_except_table68
- GCC_except_table73
- GCC_except_table78
- GCC_except_table8
- GCC_except_table83
- GCC_except_table88
- GCC_except_table93
- GCC_except_table98
- _OBJC_IVAR_$_UARPDeviceConfiguration._ECIDData
- ___29-[UARPDeviceManager activate]_block_invoke.10
- ___29-[UARPDeviceManager activate]_block_invoke.10.cold.1
- ___29-[UARPDeviceManager activate]_block_invoke.10.cold.2
- ___73-[UARPDeviceManager exportSolicitedAsset:deviceEndpoint:dynamicAssetURL:]_block_invoke
- ___73-[UARPDeviceManager exportSolicitedAsset:deviceEndpoint:dynamicAssetURL:]_block_invoke_2
- ___block_descriptor_48_e8_32r40r_e16_v16?0"NSData"8lr32l8r40l8
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _objc_msgSend$endpointControllerExportDynamicAsset:endpointUUID:dynamicAssetURL:reply:
- _objc_release_x9
CStrings:
+ "%s: Create not close %@; %@"
+ "%s: Create not verify hash for %@"
+ "%s: could not create %@ for %@"
+ "%s: paised processing asset manager events"
+ "%s: pullDynamicAsset for %@ failed at offset %lu, length %lu"
+ "%s: pullDynamicAssetStart for %@ failed"
+ "%s: resume processing asset manager events"
+ "%s: writeData for %@ failed at offset %lu, length %lu; %@"
+ "-[UARPDeviceManager cacheAsset:assetUUID:appendData:]"
+ "-[UARPDeviceManager cacheAssetFinish:assetUUID:hashData:]"
+ "-[UARPDeviceManager cacheAssetStart:assetUUID:]"
+ "-[UARPDeviceManager clearAssetFolders]"
+ "-[UARPDeviceManager clearEncodedMappingDatabase]"
+ "-[UARPDeviceManager clearPacketCaptures]"
+ "-[UARPDeviceManager ecidData:endpointNumber:componentNumber:]"
+ "-[UARPDeviceManager pauseAssetManagerNotifications:]"
+ "-[UARPDeviceManager pullDynamicAsset:assetUUID:range:]"
+ "-[UARPDeviceManager pullDynamicAssetFinish:assetUUID:hashData:]"
+ "-[UARPDeviceManager pullDynamicAssetStart:assetUUID:]"
+ "-[UARPDeviceManager queryEncodedMappingDatabase]"
+ "-[UARPDeviceManager resumeAssetManagerNotifications:]"
+ "@40@0:8@16@24o^@32"
+ "@48@0:8@16@24{_NSRange=QQ}32"
+ "B32@0:8@16@24"
+ "Cannot connect to listener for UARPDeviceManager"
+ "File exists, remove it; %@"
+ "T@\"NSData\",C,V_ecidData"
+ "Unable to open file for writing at %@ (%@)"
+ "_ecidData"
+ "attributesOfItemAtPath:error:"
+ "boolValue"
+ "bytes"
+ "cacheAsset:assetUUID:appendData:"
+ "cacheAsset:deviceEndpoint:error:"
+ "cacheAssetFinish:assetUUID:hashData:"
+ "cacheAssetStart:assetUUID:"
+ "checkAssetManager:"
+ "clearAssetFolders"
+ "clearEncodedMappingDatabase"
+ "clearPacketCaptures"
+ "closeAndReturnError:"
+ "createFileAtPath:contents:attributes:"
+ "dataWithBytes:length:"
+ "deactivate"
+ "defaultManager"
+ "ecidData"
+ "ecidData:endpointIndex:"
+ "ecidData:endpointIndex:componentIndex:"
+ "endpointControllerCacheAsset:assetUUID:appendData:reply:"
+ "endpointControllerCacheAssetFinish:assetUUID:hashData:reply:"
+ "endpointControllerCacheAssetStart:assetUUID:reply:"
+ "endpointControllerCheckAssetManager:"
+ "endpointControllerClearAssets"
+ "endpointControllerClearDatabase"
+ "endpointControllerClearPacketCaptures"
+ "endpointControllerPauseAssetManagerNotifications:reply:"
+ "endpointControllerPullDynamicAsset:assetUUID:range:reply:"
+ "endpointControllerPullDynamicAssetFinish:assetUUID:hashData:reply:"
+ "endpointControllerPullDynamicAssetStart:assetUUID:reply:"
+ "endpointControllerQueryEncodedMappingDatabase:"
+ "endpointControllerResumeAssetManagerNotifications:reply:"
+ "fileExistsAtPath:"
+ "fileHandleForReadingFromURL:error:"
+ "fileHandleForWritingToURL:error:"
+ "fileSize"
+ "path"
+ "pauseAssetManagerNotifications:"
+ "pullDynamicAsset:assetUUID:range:"
+ "pullDynamicAssetFinish:assetUUID:hashData:"
+ "pullDynamicAssetStart:assetUUID:"
+ "queryEncodedMappingDatabase"
+ "readDataUpToLength:error:"
+ "removeItemAtURL:error:"
+ "resumeAssetManagerNotifications:"
+ "setEcidData:"
+ "uarpDeviceManagerConnectionInterrupted:"
+ "uarpDeviceManagerConnectionInvalidated:"
+ "v20@?0B8@\"NSData\"12"
+ "v20@?0B8@\"NSURL\"12"
+ "v20@?0B8Q12"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSData\">16"
+ "v32@0:8@\"NSUUID\"16@?<v@?B>24"
+ "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?B>32"
+ "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?BQ>32"
+ "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSData\"32@?<v@?B>40"
+ "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSData\"32@?<v@?B@\"NSURL\">40"
+ "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSURL\"32@?<v@?@\"NSNumber\">40"
+ "v56@0:8@\"NSUUID\"16@\"NSUUID\"24{_NSRange=QQ}32@?<v@?B@\"NSData\">48"
+ "v56@0:8@16@24{_NSRange=QQ}32@?48"
+ "writeData:error:"
- "ECIDData"
- "T@\"NSData\",C,V_ECIDData"
- "_ECIDData"
- "setECIDData:"
- "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSURL\"32@?<v@?B>40"

```
