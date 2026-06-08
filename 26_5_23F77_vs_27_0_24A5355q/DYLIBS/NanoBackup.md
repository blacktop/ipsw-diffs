## NanoBackup

> `/System/Library/PrivateFrameworks/NanoBackup.framework/NanoBackup`

```diff

-130.0.0.0.0
-  __TEXT.__text: 0x6aac
-  __TEXT.__auth_stubs: 0x350
+134.0.0.0.0
+  __TEXT.__text: 0x5cf8
   __TEXT.__objc_methlist: 0x67c
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x615
-  __TEXT.__gcc_except_tab: 0x24c
+  __TEXT.__cstring: 0x61d
+  __TEXT.__gcc_except_tab: 0x1ec
   __TEXT.__oslogstring: 0x37d
-  __TEXT.__unwind_info: 0x318
-  __TEXT.__objc_classname: 0x64
-  __TEXT.__objc_methname: 0x1566
-  __TEXT.__objc_methtype: 0x362
-  __TEXT.__objc_stubs: 0x7c0
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x518
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0xb0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_const: 0x9c0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x180

   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 75347986-7884-31CD-8575-37A6FA53F5A5
+  UUID: FF470744-8410-3AFE-B1B5-1FFF03CEB906
   Functions: 169
-  Symbols:   605
-  CStrings:  403
+  Symbols:   609
+  CStrings:  110
 
Symbols:
+ _PDRDevicePropertyKeyPairingID
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _NRDevicePropertyPairingID
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x27
Functions:
~ -[NBManager initWithQueue:] : 200 -> 196
~ -[NBManager listBackupsOfType:timeout:completionHandler:] : 624 -> 572
~ ___57-[NBManager listBackupsOfType:timeout:completionHandler:]_block_invoke.87 : 420 -> 412
~ -[NBManager connection] : 352 -> 344
~ ___23-[NBManager connection]_block_invoke : 280 -> 268
~ ___57-[NBManager listBackupsOfType:timeout:completionHandler:]_block_invoke_2.90 : 520 -> 480
~ -[NBExclusionListManager excludedPerGizmoDomains] : 64 -> 56
~ -[NBExclusionListManager excludedKeysInDomain:] : 96 -> 92
~ -[NBExclusionListManager readConfigurationIfNeeded] : 640 -> 608
~ ___51-[NBExclusionListManager readConfigurationIfNeeded]_block_invoke : 284 -> 280
~ -[NBExclusionListManager setExcludedPerGizmoDomains:] : 64 -> 12
~ -[NBExclusionListManager setExcludedPerGizmoDomainSettings:] : 64 -> 12
~ -[NBBackup description] : 336 -> 324
~ -[NBBackup activeWatchFaceFileURL] : 704 -> 672
~ -[NBBackup setActiveWatchFaceFileURL:] : 60 -> 52
~ -[NBBackup encodeWithCoder:] : 536 -> 528
~ -[NBBackup initWithCoder:] : 1180 -> 1096
~ -[NBBackup setUuid:] : 64 -> 12
~ -[NBBackup setName:] : 64 -> 12
~ -[NBBackup setProductType:] : 64 -> 12
~ -[NBBackup setProductName:] : 64 -> 12
~ -[NBBackup setSystemVersion:] : 64 -> 12
~ -[NBBackup setSystemBuildVersion:] : 64 -> 12
~ -[NBBackup setMarketingVersion:] : 64 -> 12
~ -[NBBackup setDeviceColor:] : 64 -> 12
~ -[NBBackup setDeviceEnclosureColor:] : 64 -> 12
~ -[NBBackup setBottomEnclosureMaterial:] : 64 -> 12
~ -[NBBackup setTopEnclosureMaterial:] : 64 -> 12
~ -[NBBackup setFcmMaterial:] : 64 -> 12
~ -[NBBackup setBcmWindowMaterial:] : 64 -> 12
~ -[NBBackup setCoverGlassColor:] : 64 -> 12
~ -[NBBackup setHousingColor:] : 64 -> 12
~ -[NBBackup setBackingColor:] : 64 -> 12
~ -[NBBackup setWatchFace:] : 64 -> 12
~ -[NBBackup setWatchFaceColor:] : 64 -> 12
~ -[NBBackup setLastModificationDate:] : 64 -> 12
~ -[NBBackup setSizeInBytes:] : 64 -> 12
~ -[NBBackup setDeviceCSN:] : 64 -> 12
~ -[NBBackup setWatchFaceData:] : 64 -> 12
~ ___23-[NBManager connection]_block_invoke.81 : 232 -> 228
~ ___57-[NBManager listBackupsOfType:timeout:completionHandler:]_block_invoke : 252 -> 208
~ ___57-[NBManager listBackupsOfType:timeout:completionHandler:]_block_invoke_2 : 344 -> 296
~ -[NBManager setBackupsEnabled:completionHandler:] : 400 -> 364
~ ___49-[NBManager setBackupsEnabled:completionHandler:]_block_invoke : 412 -> 404
~ ___49-[NBManager setBackupsEnabled:completionHandler:]_block_invoke_2 : 344 -> 296
~ ___49-[NBManager setBackupsEnabled:completionHandler:]_block_invoke_2.94 : 348 -> 300
~ -[NBManager listBackupsOfType:withSynchronousCompletionHandler:] : 584 -> 536
~ ___64-[NBManager listBackupsOfType:withSynchronousCompletionHandler:]_block_invoke : 272 -> 264
~ ___64-[NBManager listBackupsOfType:withSynchronousCompletionHandler:]_block_invoke_2 : 200 -> 156
~ ___64-[NBManager listBackupsOfType:withSynchronousCompletionHandler:]_block_invoke.96 : 276 -> 244
~ -[NBManager restoreFromBackup:forDevice:completionHandler:] : 648 -> 608
~ ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke : 548 -> 536
~ ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke_2 : 352 -> 304
~ ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke_2.104 : 356 -> 308
~ -[NBManager restoreFromBackup:forDevice:] : 820 -> 768
~ ___41-[NBManager restoreFromBackup:forDevice:]_block_invoke : 300 -> 288
~ ___41-[NBManager restoreFromBackup:forDevice:]_block_invoke_2 : 72 -> 16
~ ___41-[NBManager restoreFromBackup:forDevice:]_block_invoke_3 : 72 -> 16
~ -[NBManager restoreFromDevice:forDevice:completionHandler:] : 620 -> 584
~ ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke : 504 -> 496
~ ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke_2 : 352 -> 304
~ ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke_2.114 : 356 -> 308
~ -[NBManager restoreFromDevice:forDevice:] : 792 -> 744
~ ___41-[NBManager restoreFromDevice:forDevice:]_block_invoke : 252 -> 244
~ ___41-[NBManager restoreFromDevice:forDevice:]_block_invoke_2 : 72 -> 16
~ ___41-[NBManager restoreFromDevice:forDevice:]_block_invoke_3 : 72 -> 16
~ -[NBManager createBackupForDevice:completionHandler:] : 328 -> 288
~ -[NBManager createBackupForDevice:synchronousCompletionHandler:] : 328 -> 288
~ -[NBManager createBackupForPairingID:completionHandler:] : 416 -> 384
~ ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke : 504 -> 488
~ ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke_2 : 352 -> 304
~ ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke_2.124 : 452 -> 404
~ -[NBManager createBackupForPairingID:synchronousCompletionHandler:] : 644 -> 600
~ ___67-[NBManager createBackupForPairingID:synchronousCompletionHandler:]_block_invoke : 264 -> 256
~ ___67-[NBManager createBackupForPairingID:synchronousCompletionHandler:]_block_invoke_2 : 200 -> 156
~ ___67-[NBManager createBackupForPairingID:synchronousCompletionHandler:]_block_invoke.128 : 308 -> 268
~ ___46-[NBManager createManualBackupWithCompletion:]_block_invoke : 248 -> 240
~ ___46-[NBManager createManualBackupWithCompletion:]_block_invoke_2 : 200 -> 156
~ ___46-[NBManager createManualBackupWithCompletion:]_block_invoke.129 : 72 -> 16
~ -[NBManager deleteBackup:completionHandler:] : 516 -> 472
~ ___44-[NBManager deleteBackup:completionHandler:]_block_invoke : 536 -> 524
~ ___44-[NBManager deleteBackup:completionHandler:]_block_invoke_2 : 352 -> 304
~ ___44-[NBManager deleteBackup:completionHandler:]_block_invoke_2.134 : 356 -> 308
~ -[NBManager deleteBackup:] : 672 -> 616
~ ___26-[NBManager deleteBackup:]_block_invoke : 300 -> 288
~ ___26-[NBManager deleteBackup:]_block_invoke_2 : 200 -> 156
~ ___26-[NBManager deleteBackup:]_block_invoke.137 : 72 -> 16
~ -[NBManager setInternalQueue:] : 64 -> 12
~ -[NBManager setExternalQueue:] : 64 -> 12
~ -[NBManager setXpcConnection:] : 64 -> 12
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NBBackup"
- "NBExclusionListManager"
- "NBManager"
- "NBServerProtocol"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSData\",&,N,V_watchFaceData"
- "T@\"NSDate\",&,N,V_lastModificationDate"
- "T@\"NSMutableDictionary\",&,N,V_excludedPerGizmoDomainSettings"
- "T@\"NSNumber\",&,N,V_backingColor"
- "T@\"NSNumber\",&,N,V_bcmWindowMaterial"
- "T@\"NSNumber\",&,N,V_bottomEnclosureMaterial"
- "T@\"NSNumber\",&,N,V_coverGlassColor"
- "T@\"NSNumber\",&,N,V_fcmMaterial"
- "T@\"NSNumber\",&,N,V_housingColor"
- "T@\"NSNumber\",&,N,V_sizeInBytes"
- "T@\"NSNumber\",&,N,V_topEnclosureMaterial"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_externalQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalQueue"
- "T@\"NSSet\",&,N,V_excludedPerGizmoDomains"
- "T@\"NSString\",&,N,V_deviceCSN"
- "T@\"NSString\",&,N,V_deviceColor"
- "T@\"NSString\",&,N,V_deviceEnclosureColor"
- "T@\"NSString\",&,N,V_marketingVersion"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_productName"
- "T@\"NSString\",&,N,V_productType"
- "T@\"NSString\",&,N,V_systemBuildVersion"
- "T@\"NSString\",&,N,V_systemVersion"
- "T@\"NSString\",&,N,V_watchFace"
- "T@\"NSString\",&,N,V_watchFaceColor"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSURL\",&,N,V_activeWatchFaceFileURL"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "TB,N,GisDiagnosticsOptInEnabled,V_diagnosticsOptInEnabled"
- "TB,N,GisLocationOptInEnabled,V_locationOptInEnabled"
- "TB,N,V_hasReadConfiguration"
- "TB,N,V_hasResolvedActiveWatchFaceFilePath"
- "TB,R"
- "TQ,N,V_backupType"
- "TQ,R"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activeWatchFaceFileURL"
- "_backingColor"
- "_backupType"
- "_bcmWindowMaterial"
- "_bottomEnclosureMaterial"
- "_coverGlassColor"
- "_deviceCSN"
- "_deviceColor"
- "_deviceEnclosureColor"
- "_diagnosticsOptInEnabled"
- "_excludedPerGizmoDomainSettings"
- "_excludedPerGizmoDomains"
- "_externalQueue"
- "_fcmMaterial"
- "_hasReadConfiguration"
- "_hasResolvedActiveWatchFaceFilePath"
- "_housingColor"
- "_internalQueue"
- "_lastModificationDate"
- "_locationOptInEnabled"
- "_marketingVersion"
- "_name"
- "_productName"
- "_productType"
- "_sizeInBytes"
- "_systemBuildVersion"
- "_systemVersion"
- "_topEnclosureMaterial"
- "_uuid"
- "_watchFace"
- "_watchFaceColor"
- "_watchFaceData"
- "_xpcConnection"
- "activeWatchFaceFileURL"
- "addBarrierBlock:"
- "arrayWithObjects:count:"
- "autorelease"
- "bcmWindowMaterial"
- "bottomEnclosureMaterial"
- "bundleForClass:"
- "bundlePath"
- "class"
- "conformsToProtocol:"
- "connection"
- "contentsOfDirectoryAtPath:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createBackupForDevice:completionHandler:"
- "createBackupForDevice:synchronousCompletionHandler:"
- "createBackupForPairingID:completionHandler:"
- "createBackupForPairingID:synchronousCompletionHandler:"
- "createLocalBackupForPairingID:completionHandler:"
- "createManualBackupWithCompletion:"
- "dataWithContentsOfFile:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultManager"
- "deleteBackup:"
- "deleteBackup:completionHandler:"
- "deleteBackupID:backupType:completionHandler:"
- "description"
- "deviceColor"
- "deviceEnclosureColor"
- "diagnosticsOptInEnabled"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "excludedKeysInDomain:"
- "excludedPerGizmoDomainSettings"
- "excludedPerGizmoDomains"
- "externalQueue"
- "fcmMaterial"
- "fileURLWithPath:isDirectory:"
- "getBackupsStatus"
- "hasReadConfiguration"
- "hasResolvedActiveWatchFaceFilePath"
- "hash"
- "init"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "initWithQueue:"
- "initialize"
- "interfaceWithProtocol:"
- "internalQueue"
- "invalidate"
- "isDiagnosticsOptInEnabled"
- "isEqual:"
- "isKindOfClass:"
- "isLocationOptInEnabled"
- "isMemberOfClass:"
- "isProxy"
- "lastModificationDate"
- "length"
- "listBackupsOfType:timeout:completionHandler:"
- "listBackupsOfType:withSynchronousCompletionHandler:"
- "listBackupsWithCompletionHandler:"
- "listBackupsWithSynchronousCompletionHandler:"
- "listBackupsWithTimeout:completionHandler:"
- "locationOptInEnabled"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "propertyListWithData:options:format:error:"
- "purgeCache"
- "raise:format:"
- "rangeOfString:options:"
- "readConfigurationIfNeeded"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "restoreFromBackup:forDevice:"
- "restoreFromBackup:forDevice:completionHandler:"
- "restoreFromBackupID:backupType:forPairingID:completionHandler:"
- "restoreFromDevice:forDevice:"
- "restoreFromDevice:forDevice:completionHandler:"
- "restoreFromPairingID:forPairingID:completionHandler:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setActiveWatchFaceFileURL:"
- "setBackingColor:"
- "setBackupType:"
- "setBackupsEnabled:completionHandler:"
- "setBcmWindowMaterial:"
- "setBottomEnclosureMaterial:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCoverGlassColor:"
- "setDeviceCSN:"
- "setDeviceColor:"
- "setDeviceEnclosureColor:"
- "setDiagnosticsOptInEnabled:"
- "setExcludedPerGizmoDomainSettings:"
- "setExcludedPerGizmoDomains:"
- "setExternalQueue:"
- "setFcmMaterial:"
- "setHasReadConfiguration:"
- "setHasResolvedActiveWatchFaceFilePath:"
- "setHousingColor:"
- "setInternalQueue:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLastModificationDate:"
- "setLocationOptInEnabled:"
- "setMarketingVersion:"
- "setName:"
- "setObject:forKeyedSubscript:"
- "setProductName:"
- "setProductType:"
- "setRemoteObjectInterface:"
- "setSizeInBytes:"
- "setSystemBuildVersion:"
- "setSystemVersion:"
- "setTopEnclosureMaterial:"
- "setUuid:"
- "setWatchFace:"
- "setWatchFaceColor:"
- "setWatchFaceData:"
- "setWithArray:"
- "setWithObjects:"
- "setXpcConnection:"
- "sizeInBytes"
- "stringByAppendingPathComponent:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "topEnclosureMaterial"
- "unsafe_invalidate"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8Q16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NBBackup\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8q16@?24"
- "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8Q16q24@?32"
- "v40@0:8Q16q24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v48@0:8@\"NSUUID\"16Q24@\"NSUUID\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16Q24@32@?40"
- "valueForProperty:"
- "watchFace"
- "watchFaceColor"
- "xpcConnection"
- "zone"

```
