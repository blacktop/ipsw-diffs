## ImageCaptureCore

> `/System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore`

```diff

-1936.4.3.0.0
-  __TEXT.__text: 0x3a0cc
+2013.0.0.0.0
+  __TEXT.__text: 0x3c10c
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x3794
-  __TEXT.__const: 0x74
-  __TEXT.__cstring: 0x6515
+  __TEXT.__objc_methlist: 0x391c
+  __TEXT.__const: 0x84
+  __TEXT.__gcc_except_tab: 0xe18
+  __TEXT.__cstring: 0x5e35
   __TEXT.__oslogstring: 0x3f
-  __TEXT.__gcc_except_tab: 0xd88
   __TEXT.__ustring: 0x478
-  __TEXT.__unwind_info: 0xc30
-  __TEXT.__objc_classname: 0x2b7
-  __TEXT.__objc_methname: 0x8ccc
-  __TEXT.__objc_methtype: 0xe6b
-  __TEXT.__objc_stubs: 0x5cc0
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0xef0
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__unwind_info: 0xcb0
+  __TEXT.__objc_classname: 0x337
+  __TEXT.__objc_methname: 0x93c6
+  __TEXT.__objc_methtype: 0xee2
+  __TEXT.__objc_stubs: 0x6100
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__const: 0xf28
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2350
+  __DATA_CONST.__objc_selrefs: 0x2488
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x28d8
   __AUTH_CONST.__auth_got: 0x4d0
-  __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x7d20
-  __AUTH_CONST.__objc_const: 0x4870
+  __AUTH_CONST.__const: 0x2a0
+  __AUTH_CONST.__cfstring: 0x78c0
+  __AUTH_CONST.__objc_const: 0x4a18
   __AUTH_CONST.__objc_dictobj: 0x2238
   __AUTH_CONST.__objc_intobj: 0x750
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x430
-  __DATA.__data: 0x328
+  __AUTH.__objc_data: 0x640
+  __DATA.__objc_ivar: 0x418
+  __DATA.__data: 0x4a8
   __DATA.__bss: 0xa8
   __DATA.__common: 0xc
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x60
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 35D436F9-2BFD-3C02-9073-92ED9FBB9695
-  Functions: 1366
-  Symbols:   4425
-  CStrings:  3872
+  UUID: 9D6A1E2C-064B-3046-8C78-21B1907257C6
+  Functions: 1389
+  Symbols:   4550
+  CStrings:  3869
 
Symbols:
+ +[ICCameraItemProxy supportsSecureCoding]
+ -[ICCameraFile initWithProxy:parentFolder:device:]
+ -[ICCameraFolder initWithProxy:parentFolder:device:]
+ -[ICCameraItemProxy .cxx_destruct]
+ -[ICCameraItemProxy captureDate]
+ -[ICCameraItemProxy encodeWithCoder:]
+ -[ICCameraItemProxy hasThumbnail]
+ -[ICCameraItemProxy height]
+ -[ICCameraItemProxy initWithCoder:]
+ -[ICCameraItemProxy init]
+ -[ICCameraItemProxy keywords]
+ -[ICCameraItemProxy modificationDate]
+ -[ICCameraItemProxy name]
+ -[ICCameraItemProxy objectHandle]
+ -[ICCameraItemProxy orientation]
+ -[ICCameraItemProxy parentObjectHandle]
+ -[ICCameraItemProxy readOnly]
+ -[ICCameraItemProxy sequenceNumber]
+ -[ICCameraItemProxy setCaptureDate:]
+ -[ICCameraItemProxy setHasThumbnail:]
+ -[ICCameraItemProxy setHeight:]
+ -[ICCameraItemProxy setKeywords:]
+ -[ICCameraItemProxy setModificationDate:]
+ -[ICCameraItemProxy setName:]
+ -[ICCameraItemProxy setObjectHandle:]
+ -[ICCameraItemProxy setOrientation:]
+ -[ICCameraItemProxy setParentObjectHandle:]
+ -[ICCameraItemProxy setReadOnly:]
+ -[ICCameraItemProxy setSequenceNumber:]
+ -[ICCameraItemProxy setSize:]
+ -[ICCameraItemProxy setStorageID:]
+ -[ICCameraItemProxy setTopLevel:]
+ -[ICCameraItemProxy setType:]
+ -[ICCameraItemProxy setWidth:]
+ -[ICCameraItemProxy size]
+ -[ICCameraItemProxy storageID]
+ -[ICCameraItemProxy topLevel]
+ -[ICCameraItemProxy type]
+ -[ICCameraItemProxy width]
+ -[ICDeviceManager deviceListQueue]
+ -[ICDeviceManager setDeviceListQueue:]
+ -[ICRemoteCameraDevice .cxx_destruct]
+ -[ICRemoteCameraDevice acceptConnection:]
+ -[ICRemoteCameraDevice addInitiatedOperation:]
+ -[ICRemoteCameraDevice addInteractiveOperation:]
+ -[ICRemoteCameraDevice addSelectorToInterface:selectorString:origin:]
+ -[ICRemoteCameraDevice addSelectorToInterface:selectorString:origin:].cold.1
+ -[ICRemoteCameraDevice addedBundles]
+ -[ICRemoteCameraDevice additionalProperties]
+ -[ICRemoteCameraDevice allConnections]
+ -[ICRemoteCameraDevice cameraDictionary]
+ -[ICRemoteCameraDevice closeDevice]
+ -[ICRemoteCameraDevice cpPowerAssertion]
+ -[ICRemoteCameraDevice dealloc]
+ -[ICRemoteCameraDevice delegate]
+ -[ICRemoteCameraDevice deniedBundles]
+ -[ICRemoteCameraDevice deviceOperationQueue]
+ -[ICRemoteCameraDevice deviceOperationUnderlyingQueue]
+ -[ICRemoteCameraDevice endpoint]
+ -[ICRemoteCameraDevice evaulateCommonTCC:]
+ -[ICRemoteCameraDevice holdPowerAssertion]
+ -[ICRemoteCameraDevice initWithDeviceContext:]
+ -[ICRemoteCameraDevice internalUUID]
+ -[ICRemoteCameraDevice listener:shouldAcceptNewConnection:]
+ -[ICRemoteCameraDevice listener]
+ -[ICRemoteCameraDevice registerInterestedEventNotifications:]
+ -[ICRemoteCameraDevice releasePowerAssertion]
+ -[ICRemoteCameraDevice removeAllSessions]
+ -[ICRemoteCameraDevice removeSessionsWithProcessIdentifier:]
+ -[ICRemoteCameraDevice sendAddedItemsNotification:toConnections:]
+ -[ICRemoteCameraDevice sendNotification:toConnections:selector:]
+ -[ICRemoteCameraDevice sendPTPEventNotification:]
+ -[ICRemoteCameraDevice sendRemovedItemsNotification:toConnections:]
+ -[ICRemoteCameraDevice sendStatusNotification:toConnections:]
+ -[ICRemoteCameraDevice sendUpdatedItemsNotification:toConnections:]
+ -[ICRemoteCameraDevice sessionManagerDidCloseAllSessions:]
+ -[ICRemoteCameraDevice sessionManager]
+ -[ICRemoteCameraDevice setAddedBundles:]
+ -[ICRemoteCameraDevice setCameraDictionary:]
+ -[ICRemoteCameraDevice setCpPowerAssertion:]
+ -[ICRemoteCameraDevice setDelegate:]
+ -[ICRemoteCameraDevice setDeniedBundles:]
+ -[ICRemoteCameraDevice setDeviceOperationQueue:]
+ -[ICRemoteCameraDevice setDeviceOperationUnderlyingQueue:]
+ -[ICRemoteCameraDevice setListener:]
+ -[ICRemoteCameraDevice setSessionManager:]
+ -[ICRemoteCameraDevice startListening]
+ -[ICRemoteCameraDevice unregisterInterestedEventNotifications:]
+ -[ICRemoteCameraDeviceManager .cxx_destruct]
+ -[ICRemoteCameraDeviceManager addRemoteCameraDevice:uuidString:deviceName:]
+ -[ICRemoteCameraDeviceManager addRemoteManagerConnection:]
+ -[ICRemoteCameraDeviceManager addSelectorToInterface:selectorString:origin:]
+ -[ICRemoteCameraDeviceManager addSelectorToInterface:selectorString:origin:].cold.1
+ -[ICRemoteCameraDeviceManager closeDevice:]
+ -[ICRemoteCameraDeviceManager dealloc]
+ -[ICRemoteCameraDeviceManager ejectDevice:withReply:]
+ -[ICRemoteCameraDeviceManager initManaging:systemDaemon:]
+ -[ICRemoteCameraDeviceManager listener:shouldAcceptNewConnection:]
+ -[ICRemoteCameraDeviceManager managedObjectName]
+ -[ICRemoteCameraDeviceManager notifyClientDeviceAdded:uuidString:deviceName:]
+ -[ICRemoteCameraDeviceManager notifyClientDeviceRemoved:]
+ -[ICRemoteCameraDeviceManager openDevice:withReply:]
+ -[ICRemoteCameraDeviceManager osTransactions]
+ -[ICRemoteCameraDeviceManager remoteCameraDevicesLock]
+ -[ICRemoteCameraDeviceManager remoteCameraDevices]
+ -[ICRemoteCameraDeviceManager remoteDeviceForPrimaryIdentifier:]
+ -[ICRemoteCameraDeviceManager remoteDeviceForUUID:]
+ -[ICRemoteCameraDeviceManager remoteManagerConnectionWithProcessIdentifierAuthorized:]
+ -[ICRemoteCameraDeviceManager remoteManagerConnectionsLock]
+ -[ICRemoteCameraDeviceManager remoteManagerConnections]
+ -[ICRemoteCameraDeviceManager removeRemoteCameraDevice:]
+ -[ICRemoteCameraDeviceManager removeRemoteManagerConnectionWithProcessIdentifier:]
+ -[ICRemoteCameraDeviceManager requestDeviceListWithOptions:reply:]
+ -[ICRemoteCameraDeviceManager setManagedObjectName:]
+ -[ICRemoteCameraDeviceManager setOsTransactions:]
+ -[ICRemoteCameraDeviceManager setRemoteCameraDevices:]
+ -[ICRemoteCameraDeviceManager setRemoteCameraDevicesLock:]
+ -[ICRemoteCameraDeviceManager setRemoteManagerConnections:]
+ -[ICRemoteCameraDeviceManager setRemoteManagerConnectionsLock:]
+ -[ICRemoteCameraDeviceManager setSystemDaemon:]
+ -[ICRemoteCameraDeviceManager startDeviceNotifications]
+ -[ICRemoteCameraDeviceManager systemDaemon]
+ -[ICRemoteCameraDeviceManager updateRemoteManagerConnectionWithProcessIdentifier:authorized:]
+ -[ICRemoteCameraDeviceProxy .cxx_destruct]
+ -[ICRemoteCameraDeviceProxy camera]
+ -[ICRemoteCameraDeviceProxy dealloc]
+ -[ICRemoteCameraDeviceProxy deviceContext]
+ -[ICRemoteCameraDeviceProxy initWithPrimaryIdentifierString:uuidString:localizedName:]
+ -[ICRemoteCameraDeviceProxy localizedName]
+ -[ICRemoteCameraDeviceProxy primaryIdentifierString]
+ -[ICRemoteCameraDeviceProxy setCamera:]
+ -[ICRemoteCameraDeviceProxy setLocalizedName:]
+ -[ICRemoteCameraDeviceProxy setPrimaryIdentifierString:]
+ -[ICRemoteCameraDeviceProxy setUuidString:]
+ -[ICRemoteCameraDeviceProxy uuidString]
+ GCC_except_table32
+ GCC_except_table77
+ GCC_except_table86
+ OBJC_IVAR_$_ICCameraFileFingerprint._lock
+ OBJC_IVAR_$_ICCameraFileFingerprint._zeroByteFileFingerprintOnce
+ OBJC_IVAR_$_ICDeviceAccessManager._externalMediaAccessDB
+ OBJC_IVAR_$_ICSession._resourceLock
+ OBJC_IVAR_$_ICSessionManager._sessionConnectionAdded
+ OBJC_IVAR_$_ICSessionManager._sessions
+ OBJC_IVAR_$_ICSessionManager._sessionsLock
+ _CPPowerAssertionCreate
+ _ICAccessTypeControlInformed
+ _ICCameraItemProxyTypeFile
+ _ICCameraItemProxyTypeFolder
+ _ICCameraItemProxyTypeStorage
+ _ICEvaluatePrivateEntitlement
+ _NSClassFromString
+ _NSStringFromSelector
+ _OBJC_CLASS_$_ICCameraItemProxy
+ _OBJC_CLASS_$_ICRemoteCameraDevice
+ _OBJC_CLASS_$_ICRemoteCameraDeviceManager
+ _OBJC_CLASS_$_ICRemoteCameraDeviceProxy
+ _OBJC_CLASS_$_NSXPCListener
+ _OBJC_IVAR_$_ICCameraItemProxy._captureDate
+ _OBJC_IVAR_$_ICCameraItemProxy._hasThumbnail
+ _OBJC_IVAR_$_ICCameraItemProxy._height
+ _OBJC_IVAR_$_ICCameraItemProxy._keywords
+ _OBJC_IVAR_$_ICCameraItemProxy._modificationDate
+ _OBJC_IVAR_$_ICCameraItemProxy._name
+ _OBJC_IVAR_$_ICCameraItemProxy._objectHandle
+ _OBJC_IVAR_$_ICCameraItemProxy._orientation
+ _OBJC_IVAR_$_ICCameraItemProxy._parentObjectHandle
+ _OBJC_IVAR_$_ICCameraItemProxy._readOnly
+ _OBJC_IVAR_$_ICCameraItemProxy._sequenceNumber
+ _OBJC_IVAR_$_ICCameraItemProxy._size
+ _OBJC_IVAR_$_ICCameraItemProxy._storageID
+ _OBJC_IVAR_$_ICCameraItemProxy._topLevel
+ _OBJC_IVAR_$_ICCameraItemProxy._type
+ _OBJC_IVAR_$_ICCameraItemProxy._width
+ _OBJC_IVAR_$_ICDeviceManager._deviceListQueue
+ _OBJC_IVAR_$_ICRemoteCameraDevice._addedBundles
+ _OBJC_IVAR_$_ICRemoteCameraDevice._cameraDictionary
+ _OBJC_IVAR_$_ICRemoteCameraDevice._cpPowerAssertion
+ _OBJC_IVAR_$_ICRemoteCameraDevice._delegate
+ _OBJC_IVAR_$_ICRemoteCameraDevice._deniedBundles
+ _OBJC_IVAR_$_ICRemoteCameraDevice._deviceOperationQueue
+ _OBJC_IVAR_$_ICRemoteCameraDevice._deviceOperationUnderlyingQueue
+ _OBJC_IVAR_$_ICRemoteCameraDevice._listener
+ _OBJC_IVAR_$_ICRemoteCameraDevice._sessionManager
+ _OBJC_IVAR_$_ICRemoteCameraDeviceManager._managedObjectName
+ _OBJC_IVAR_$_ICRemoteCameraDeviceManager._osTransactions
+ _OBJC_IVAR_$_ICRemoteCameraDeviceManager._remoteCameraDevices
+ _OBJC_IVAR_$_ICRemoteCameraDeviceManager._remoteCameraDevicesLock
+ _OBJC_IVAR_$_ICRemoteCameraDeviceManager._remoteManagerConnections
+ _OBJC_IVAR_$_ICRemoteCameraDeviceManager._remoteManagerConnectionsLock
+ _OBJC_IVAR_$_ICRemoteCameraDeviceManager._startDeviceNotifications
+ _OBJC_IVAR_$_ICRemoteCameraDeviceManager._systemDaemon
+ _OBJC_IVAR_$_ICRemoteCameraDeviceProxy._camera
+ _OBJC_IVAR_$_ICRemoteCameraDeviceProxy._localizedName
+ _OBJC_IVAR_$_ICRemoteCameraDeviceProxy._primaryIdentifierString
+ _OBJC_IVAR_$_ICRemoteCameraDeviceProxy._uuidString
+ _OBJC_METACLASS_$_ICCameraItemProxy
+ _OBJC_METACLASS_$_ICRemoteCameraDevice
+ _OBJC_METACLASS_$_ICRemoteCameraDeviceManager
+ _OBJC_METACLASS_$_ICRemoteCameraDeviceProxy
+ __OBJC_$_CLASS_METHODS_ICCameraItemProxy
+ __OBJC_$_CLASS_PROP_LIST_ICCameraItemProxy
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_ICCameraItemProxy
+ __OBJC_$_INSTANCE_METHODS_ICRemoteCameraDevice
+ __OBJC_$_INSTANCE_METHODS_ICRemoteCameraDeviceManager
+ __OBJC_$_INSTANCE_METHODS_ICRemoteCameraDeviceProxy
+ __OBJC_$_INSTANCE_VARIABLES_ICCameraItemProxy
+ __OBJC_$_INSTANCE_VARIABLES_ICRemoteCameraDevice
+ __OBJC_$_INSTANCE_VARIABLES_ICRemoteCameraDeviceManager
+ __OBJC_$_INSTANCE_VARIABLES_ICRemoteCameraDeviceProxy
+ __OBJC_$_PROP_LIST_ICCameraItemProxy
+ __OBJC_$_PROP_LIST_ICRemoteCameraDevice
+ __OBJC_$_PROP_LIST_ICRemoteCameraDeviceManager
+ __OBJC_$_PROP_LIST_ICRemoteCameraDeviceProxy
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICSessionManagerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICSessionManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_ICSessionManagerProtocol
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ICCameraItemProxy
+ __OBJC_CLASS_PROTOCOLS_$_ICRemoteCameraDevice
+ __OBJC_CLASS_RO_$_ICCameraItemProxy
+ __OBJC_CLASS_RO_$_ICRemoteCameraDevice
+ __OBJC_CLASS_RO_$_ICRemoteCameraDeviceManager
+ __OBJC_CLASS_RO_$_ICRemoteCameraDeviceProxy
+ __OBJC_LABEL_PROTOCOL_$_ICSessionManagerProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_METACLASS_RO_$_ICCameraItemProxy
+ __OBJC_METACLASS_RO_$_ICRemoteCameraDevice
+ __OBJC_METACLASS_RO_$_ICRemoteCameraDeviceManager
+ __OBJC_METACLASS_RO_$_ICRemoteCameraDeviceProxy
+ __OBJC_PROTOCOL_$_ICSessionManagerProtocol
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ ___36-[ICDeviceManager openDeviceHandle:]_block_invoke.175
+ ___36-[ICDeviceManager openDeviceHandle:]_block_invoke.45
+ ___42-[ICDeviceManager openRemoteDeviceManager]_block_invoke.258
+ ___42-[ICDeviceManager openRemoteDeviceManager]_block_invoke_2
+ ___52-[ICRemoteCameraDeviceManager openDevice:withReply:]_block_invoke
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.245
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.255
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.265
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.280
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.296
+ ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke_2.297
+ ___57-[ICRemoteCameraDeviceManager notifyClientDeviceRemoved:]_block_invoke
+ ___58-[ICCameraFile requestReadDataAtOffset:length:completion:]_block_invoke.317
+ ___58-[ICRemoteCameraDeviceManager addRemoteManagerConnection:]_block_invoke
+ ___59-[ICCameraFile requestThumbnailDataWithOptions:completion:]_block_invoke.169
+ ___59-[ICCameraFile requestThumbnailDataWithOptions:completion:]_block_invoke.193
+ ___61-[ICRemoteCameraDevice registerInterestedEventNotifications:]_block_invoke
+ ___63-[ICRemoteCameraDevice unregisterInterestedEventNotifications:]_block_invoke
+ ___64-[ICCameraFile requestMetadataDictionaryWithOptions:completion:]_block_invoke.202
+ ___64-[ICCameraFile requestMetadataDictionaryWithOptions:completion:]_block_invoke.212
+ ___64-[ICRemoteCameraDevice sendNotification:toConnections:selector:]_block_invoke
+ ___66-[ICRemoteCameraDeviceManager requestDeviceListWithOptions:reply:]_block_invoke
+ ___69-[ICRemoteCameraDevice addSelectorToInterface:selectorString:origin:]_block_invoke
+ ___76-[ICRemoteCameraDeviceManager addSelectorToInterface:selectorString:origin:]_block_invoke
+ ___77-[ICRemoteCameraDeviceManager notifyClientDeviceAdded:uuidString:deviceName:]_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_literal_global.155
+ ___block_literal_global.69
+ ___block_literal_global.99
+ _exit
+ _objc_msgSend$acceptConnection:
+ _objc_msgSend$addNotifications:toSessionWithConnection:
+ _objc_msgSend$addRemoteCameraDevice:uuidString:deviceName:
+ _objc_msgSend$addRemoteManagerConnection:
+ _objc_msgSend$addedBundles
+ _objc_msgSend$additionalProperties
+ _objc_msgSend$anonymousListener
+ _objc_msgSend$auditToken
+ _objc_msgSend$camera
+ _objc_msgSend$cameraDictionary
+ _objc_msgSend$closeDevice
+ _objc_msgSend$closeDevice:
+ _objc_msgSend$connections
+ _objc_msgSend$connectionsMonitoringNotification:
+ _objc_msgSend$createSessionWithConnection:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$deniedBundles
+ _objc_msgSend$deviceContext
+ _objc_msgSend$deviceListQueue
+ _objc_msgSend$deviceOperationQueue
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$endpoint
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$initWithDeviceContext:
+ _objc_msgSend$initWithPrimaryIdentifierString:uuidString:localizedName:
+ _objc_msgSend$initWithProxy:parentFolder:device:
+ _objc_msgSend$listener
+ _objc_msgSend$localizedName
+ _objc_msgSend$managedObjectName
+ _objc_msgSend$osTransactions
+ _objc_msgSend$parentObjectHandle
+ _objc_msgSend$primaryIdentifierString
+ _objc_msgSend$readOnly
+ _objc_msgSend$remNotifications:fromSessionWithConnection:
+ _objc_msgSend$remoteCameraDevices
+ _objc_msgSend$remoteDeviceForPrimaryIdentifier:
+ _objc_msgSend$remoteDeviceForUUID:
+ _objc_msgSend$removeAllSessions
+ _objc_msgSend$removeRemoteCameraDevice:
+ _objc_msgSend$removeRemoteManagerConnectionWithProcessIdentifier:
+ _objc_msgSend$removeSessionsWithProcessIdentifier:
+ _objc_msgSend$sendNotification:toConnections:selector:
+ _objc_msgSend$sessionManager
+ _objc_msgSend$setCamera:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setListener:
+ _objc_msgSend$setLocalizedName:
+ _objc_msgSend$setManagedObjectName:
+ _objc_msgSend$setSystemDaemon:
+ _objc_msgSend$setUnderlyingQueue:
+ _objc_msgSend$setUuidString:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$size
+ _objc_msgSend$startListening
+ _objc_msgSend$topLevel
+ _objc_msgSend$uuidString
+ _objc_msgSend$valueForEntitlement:
+ _objc_opt_new
+ _os_transaction_create
- -[MSCameraDeviceManager updateCameraFile:withInfo:]
- -[MSCameraDeviceManager updateCameraFolder:withInfo:]
- -[MSObjectInfoDataset .cxx_destruct]
- -[MSObjectInfoDataset associationDesc]
- -[MSObjectInfoDataset associationType]
- -[MSObjectInfoDataset captureDate_tvsec]
- -[MSObjectInfoDataset contentLength:bufferLength:]
- -[MSObjectInfoDataset content]
- -[MSObjectInfoDataset filename]
- -[MSObjectInfoDataset imageBitDepth]
- -[MSObjectInfoDataset imageOrientation]
- -[MSObjectInfoDataset imagePixHeight]
- -[MSObjectInfoDataset imagePixWidth]
- -[MSObjectInfoDataset initWithBytes:length:]
- -[MSObjectInfoDataset initWithData:]
- -[MSObjectInfoDataset init]
- -[MSObjectInfoDataset modificationDate_tvsec]
- -[MSObjectInfoDataset objectCompressedSize]
- -[MSObjectInfoDataset objectFormat]
- -[MSObjectInfoDataset objectHandle]
- -[MSObjectInfoDataset parentObject]
- -[MSObjectInfoDataset protectionStatus]
- -[MSObjectInfoDataset sequenceNumber]
- -[MSObjectInfoDataset setAssociationDesc:]
- -[MSObjectInfoDataset setAssociationType:]
- -[MSObjectInfoDataset setCaptureDate_tvsec:]
- -[MSObjectInfoDataset setFilename:]
- -[MSObjectInfoDataset setImageBitDepth:]
- -[MSObjectInfoDataset setImageOrientation:]
- -[MSObjectInfoDataset setImagePixHeight:]
- -[MSObjectInfoDataset setImagePixWidth:]
- -[MSObjectInfoDataset setModificationDate_tvsec:]
- -[MSObjectInfoDataset setObjectCompressedSize:]
- -[MSObjectInfoDataset setObjectFormat:]
- -[MSObjectInfoDataset setObjectHandle:]
- -[MSObjectInfoDataset setParentObject:]
- -[MSObjectInfoDataset setProtectionStatus:]
- -[MSObjectInfoDataset setSequenceNumber:]
- -[MSObjectInfoDataset setStorageID:]
- -[MSObjectInfoDataset setThumbCompressedSize:]
- -[MSObjectInfoDataset setThumbFormat:]
- -[MSObjectInfoDataset setThumbOffset:]
- -[MSObjectInfoDataset setThumbPixHeight:]
- -[MSObjectInfoDataset setThumbPixWidth:]
- -[MSObjectInfoDataset storageID]
- -[MSObjectInfoDataset thumbCompressedSize]
- -[MSObjectInfoDataset thumbFormat]
- -[MSObjectInfoDataset thumbOffset]
- -[MSObjectInfoDataset thumbPixHeight]
- -[MSObjectInfoDataset thumbPixWidth]
- -[PTPCameraDeviceManager updateCameraFile:withInfo:]
- -[PTPCameraDeviceManager updateCameraFile:withKeywords:]
- -[PTPCameraDeviceManager updateCameraFolder:withInfo:]
- -[PTPObjectInfoDataset .cxx_destruct]
- -[PTPObjectInfoDataset addCustomKeyword:withIdentifier:]
- -[PTPObjectInfoDataset addCustomKeyword:withIdentifier:].cold.1
- -[PTPObjectInfoDataset associationDesc]
- -[PTPObjectInfoDataset associationType]
- -[PTPObjectInfoDataset captureDate]
- -[PTPObjectInfoDataset content:]
- -[PTPObjectInfoDataset content:].cold.1
- -[PTPObjectInfoDataset contentLength:bufferLength:contentType:]
- -[PTPObjectInfoDataset contentLengthValid:forContentType:]
- -[PTPObjectInfoDataset content]
- -[PTPObjectInfoDataset description]
- -[PTPObjectInfoDataset filename]
- -[PTPObjectInfoDataset imageBitDepth]
- -[PTPObjectInfoDataset imagePixHeight]
- -[PTPObjectInfoDataset imagePixWidth]
- -[PTPObjectInfoDataset initWithBytes:length:]
- -[PTPObjectInfoDataset initWithBytes:length:contentType:]
- -[PTPObjectInfoDataset initWithData:]
- -[PTPObjectInfoDataset initWithData:contentType:]
- -[PTPObjectInfoDataset init]
- -[PTPObjectInfoDataset intervalSince1970]
- -[PTPObjectInfoDataset keywords]
- -[PTPObjectInfoDataset modificationDate]
- -[PTPObjectInfoDataset objectBufferSizeForContentType:]
- -[PTPObjectInfoDataset objectCompressedSize64]
- -[PTPObjectInfoDataset objectCompressedSize]
- -[PTPObjectInfoDataset objectContentSizeForContentType:]
- -[PTPObjectInfoDataset objectFormat]
- -[PTPObjectInfoDataset objectHandle]
- -[PTPObjectInfoDataset parentObject]
- -[PTPObjectInfoDataset protectionStatus]
- -[PTPObjectInfoDataset relatedUUID]
- -[PTPObjectInfoDataset sequenceNumber]
- -[PTPObjectInfoDataset setAssociationDesc:]
- -[PTPObjectInfoDataset setAssociationType:]
- -[PTPObjectInfoDataset setCaptureDate:]
- -[PTPObjectInfoDataset setFilename:]
- -[PTPObjectInfoDataset setImageBitDepth:]
- -[PTPObjectInfoDataset setImagePixHeight:]
- -[PTPObjectInfoDataset setImagePixWidth:]
- -[PTPObjectInfoDataset setKeywords:]
- -[PTPObjectInfoDataset setModificationDate:]
- -[PTPObjectInfoDataset setObjectCompressedSize:]
- -[PTPObjectInfoDataset setObjectFormat:]
- -[PTPObjectInfoDataset setObjectHandle:]
- -[PTPObjectInfoDataset setParentObject:]
- -[PTPObjectInfoDataset setProtectionStatus:]
- -[PTPObjectInfoDataset setSequenceNumber:]
- -[PTPObjectInfoDataset setStorageID:]
- -[PTPObjectInfoDataset setThumbCompressedSize:]
- -[PTPObjectInfoDataset setThumbFormat:]
- -[PTPObjectInfoDataset setThumbOffset:]
- -[PTPObjectInfoDataset setThumbPixHeight:]
- -[PTPObjectInfoDataset setThumbPixWidth:]
- -[PTPObjectInfoDataset storageID]
- -[PTPObjectInfoDataset thumbCompressedSize]
- -[PTPObjectInfoDataset thumbFormat]
- -[PTPObjectInfoDataset thumbOffset]
- -[PTPObjectInfoDataset thumbPixHeight]
- -[PTPObjectInfoDataset thumbPixWidth]
- GCC_except_table42
- GCC_except_table48
- GCC_except_table76
- GCC_except_table85
- _CFStringConvertEncodingToNSStringEncoding
- _CopyUnicodeStringWithLengthByteFromBuffer
- _CopyUnicodeStringWithLengthByteFromBufferMaxSize
- _ICStandardDateFromPTPString
- _ICTimeIntervalSince1970FromPTPString
- _OBJC_CLASS_$_MSObjectInfoDataset
- _OBJC_CLASS_$_NSUUID
- _OBJC_CLASS_$_PTPObjectInfoDataset
- _OBJC_IVAR_$_ICCameraFileFingerprint._lock
- _OBJC_IVAR_$_ICCameraFileFingerprint._zeroByteFileFingerprintOnce
- _OBJC_IVAR_$_ICDeviceAccessManager._externalMediaAccessDB
- _OBJC_IVAR_$_ICSession._resourceLock
- _OBJC_IVAR_$_ICSessionManager._sessionConnectionAdded
- _OBJC_IVAR_$_ICSessionManager._sessions
- _OBJC_IVAR_$_ICSessionManager._sessionsLock
- _OBJC_IVAR_$_MSObjectInfoDataset._associationDesc
- _OBJC_IVAR_$_MSObjectInfoDataset._associationType
- _OBJC_IVAR_$_MSObjectInfoDataset._captureDate_tvsec
- _OBJC_IVAR_$_MSObjectInfoDataset._filename
- _OBJC_IVAR_$_MSObjectInfoDataset._imageBitDepth
- _OBJC_IVAR_$_MSObjectInfoDataset._imageOrientation
- _OBJC_IVAR_$_MSObjectInfoDataset._imagePixHeight
- _OBJC_IVAR_$_MSObjectInfoDataset._imagePixWidth
- _OBJC_IVAR_$_MSObjectInfoDataset._modificationDate_tvsec
- _OBJC_IVAR_$_MSObjectInfoDataset._objectCompressedSize
- _OBJC_IVAR_$_MSObjectInfoDataset._objectFormat
- _OBJC_IVAR_$_MSObjectInfoDataset._objectHandle
- _OBJC_IVAR_$_MSObjectInfoDataset._parentObject
- _OBJC_IVAR_$_MSObjectInfoDataset._protectionStatus
- _OBJC_IVAR_$_MSObjectInfoDataset._sequenceNumber
- _OBJC_IVAR_$_MSObjectInfoDataset._storageID
- _OBJC_IVAR_$_MSObjectInfoDataset._thumbCompressedSize
- _OBJC_IVAR_$_MSObjectInfoDataset._thumbFormat
- _OBJC_IVAR_$_MSObjectInfoDataset._thumbOffset
- _OBJC_IVAR_$_MSObjectInfoDataset._thumbPixHeight
- _OBJC_IVAR_$_MSObjectInfoDataset._thumbPixWidth
- _OBJC_IVAR_$_PTPObjectInfoDataset._associationDesc
- _OBJC_IVAR_$_PTPObjectInfoDataset._associationType
- _OBJC_IVAR_$_PTPObjectInfoDataset._captureDate
- _OBJC_IVAR_$_PTPObjectInfoDataset._filename
- _OBJC_IVAR_$_PTPObjectInfoDataset._imageBitDepth
- _OBJC_IVAR_$_PTPObjectInfoDataset._imagePixHeight
- _OBJC_IVAR_$_PTPObjectInfoDataset._imagePixWidth
- _OBJC_IVAR_$_PTPObjectInfoDataset._intervalSince1970
- _OBJC_IVAR_$_PTPObjectInfoDataset._keywords
- _OBJC_IVAR_$_PTPObjectInfoDataset._modificationDate
- _OBJC_IVAR_$_PTPObjectInfoDataset._objectCompressedSize
- _OBJC_IVAR_$_PTPObjectInfoDataset._objectFormat
- _OBJC_IVAR_$_PTPObjectInfoDataset._objectHandle
- _OBJC_IVAR_$_PTPObjectInfoDataset._parentObject
- _OBJC_IVAR_$_PTPObjectInfoDataset._protectionStatus
- _OBJC_IVAR_$_PTPObjectInfoDataset._relatedUUID
- _OBJC_IVAR_$_PTPObjectInfoDataset._sequenceNumber
- _OBJC_IVAR_$_PTPObjectInfoDataset._storageID
- _OBJC_IVAR_$_PTPObjectInfoDataset._thumbCompressedSize
- _OBJC_IVAR_$_PTPObjectInfoDataset._thumbFormat
- _OBJC_IVAR_$_PTPObjectInfoDataset._thumbOffset
- _OBJC_IVAR_$_PTPObjectInfoDataset._thumbPixHeight
- _OBJC_IVAR_$_PTPObjectInfoDataset._thumbPixWidth
- _OBJC_METACLASS_$_MSObjectInfoDataset
- _OBJC_METACLASS_$_PTPObjectInfoDataset
- _ReadUInt64
- _WriteUInt64
- _WriteUnicodeStringWithLengthByteToBuffer
- __OBJC_$_INSTANCE_METHODS_MSObjectInfoDataset
- __OBJC_$_INSTANCE_METHODS_PTPObjectInfoDataset
- __OBJC_$_INSTANCE_VARIABLES_MSObjectInfoDataset
- __OBJC_$_INSTANCE_VARIABLES_PTPObjectInfoDataset
- __OBJC_$_PROP_LIST_MSObjectInfoDataset
- __OBJC_$_PROP_LIST_PTPObjectInfoDataset
- __OBJC_CLASS_RO_$_MSObjectInfoDataset
- __OBJC_CLASS_RO_$_PTPObjectInfoDataset
- __OBJC_METACLASS_RO_$_MSObjectInfoDataset
- __OBJC_METACLASS_RO_$_PTPObjectInfoDataset
- ___36-[ICDeviceManager openDeviceHandle:]_block_invoke.173
- ___36-[ICDeviceManager openDeviceHandle:]_block_invoke.43
- ___40-[PTPCameraDeviceManager deleteFileImp:]_block_invoke.166
- ___42-[ICDeviceManager openRemoteDeviceManager]_block_invoke.256
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.224
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.234
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.244
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.256
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke.272
- ___54-[ICCameraFile requestDownloadWithOptions:completion:]_block_invoke_2.273
- ___58-[ICCameraFile requestReadDataAtOffset:length:completion:]_block_invoke.293
- ___59-[ICCameraFile requestThumbnailDataWithOptions:completion:]_block_invoke.148
- ___59-[ICCameraFile requestThumbnailDataWithOptions:completion:]_block_invoke.172
- ___64-[ICCameraFile requestMetadataDictionaryWithOptions:completion:]_block_invoke.181
- ___64-[ICCameraFile requestMetadataDictionaryWithOptions:completion:]_block_invoke.191
- _mktime
- _objc_msgSend$UUID
- _objc_msgSend$associationType
- _objc_msgSend$captureDate_tvsec
- _objc_msgSend$content:
- _objc_msgSend$contentLength:bufferLength:
- _objc_msgSend$contentLength:bufferLength:contentType:
- _objc_msgSend$contentLengthValid:forContentType:
- _objc_msgSend$filename
- _objc_msgSend$getCString:maxLength:encoding:
- _objc_msgSend$imagePixHeight
- _objc_msgSend$imagePixWidth
- _objc_msgSend$initWithBytes:length:contentType:
- _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
- _objc_msgSend$initWithData:
- _objc_msgSend$initWithData:contentType:
- _objc_msgSend$initWithLength:
- _objc_msgSend$initWithName:parentFolder:device:
- _objc_msgSend$initWithUUIDString:
- _objc_msgSend$modificationDate_tvsec
- _objc_msgSend$objectCompressedSize
- _objc_msgSend$objectCompressedSize64
- _objc_msgSend$objectFormat
- _objc_msgSend$parentObject
- _objc_msgSend$protectionStatus
- _objc_msgSend$setKeywords:
- _objc_msgSend$storageID
- _objc_msgSend$thumbCompressedSize
- _objc_msgSend$updateCameraFile:withInfo:
- _objc_msgSend$updateCameraFile:withKeywords:
- _objc_msgSend$updateCameraFolder:withInfo:
- _stringForAssociationType
- _stringForObjectFormatCode
- _stringForProtectionStatus
- _strlen
- _strncpy
- _strptime_l
- _strtok
CStrings:
+ "$"
+ "%05d-%@"
+ "%@-%d"
+ "%@-[D]"
+ "+ %@:[%05lu]"
+ "- %@:[%05lu]"
+ "> Existing Device"
+ "> New Device: %@"
+ "> Not Found: %@"
+ "@\"ICRemoteCameraDevice\""
+ "@\"ICSessionManager\""
+ "@\"NSXPCListener\""
+ "@24@0:8@\"NSCoder\"16"
+ "@28@0:8@16B24"
+ "B20@0:8i16"
+ "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
+ "B40@0:8@16@24@32"
+ "Downloading Failed - Missing File Data"
+ "Exiting %@"
+ "ICAuthorizationBypassEntitlement found"
+ "ICCameraItemProxy"
+ "ICCameraItemProxyArray"
+ "ICDeviceListQueue"
+ "ICDeviceUnderlyingQueue"
+ "ICRemoteCameraDevice"
+ "ICRemoteCameraDeviceManager"
+ "ICRemoteCameraDeviceProxy"
+ "ICRemoteManagerAuthorized"
+ "ICRemoteManagerConnection"
+ "ICSessionManagerProtocol"
+ "MTPOperationCodeGetPartialObject64"
+ "MTPSetObjectPropValue"
+ "NSCoding"
+ "NSSecureCoding"
+ "NSXPCListenerDelegate"
+ "New Connection: %d"
+ "Orientation"
+ "Q1"
+ "T@\"ICRemoteCameraDevice\",&,N,V_camera"
+ "T@\"ICSessionManager\",&,N,V_sessionManager"
+ "T@\"NSMutableArray\",&,N,V_addedBundles"
+ "T@\"NSMutableArray\",&,N,V_deniedBundles"
+ "T@\"NSMutableArray\",&,N,V_remoteCameraDevices"
+ "T@\"NSMutableDictionary\",&,N,V_cameraDictionary"
+ "T@\"NSMutableDictionary\",&,N,V_keywords"
+ "T@\"NSMutableDictionary\",&,N,V_osTransactions"
+ "T@\"NSMutableDictionary\",&,N,V_remoteManagerConnections"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_deviceListQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_deviceOperationUnderlyingQueue"
+ "T@\"NSString\",C,N,V_localizedName"
+ "T@\"NSString\",C,N,V_managedObjectName"
+ "T@\"NSString\",C,N,V_primaryIdentifierString"
+ "T@\"NSString\",C,N,V_uuidString"
+ "T@\"NSXPCListener\",&,N,V_listener"
+ "T@\"NSXPCListenerEndpoint\",R"
+ "T@,W,N,V_delegate"
+ "TB,N,V_hasThumbnail"
+ "TB,N,V_readOnly"
+ "TB,N,V_systemDaemon"
+ "TB,N,V_topLevel"
+ "TB,R,N,V_startDeviceNotifications"
+ "TI,N,V_height"
+ "TI,N,V_orientation"
+ "TI,N,V_parentObjectHandle"
+ "TI,N,V_type"
+ "TI,N,V_width"
+ "TQ,N,V_captureDate"
+ "TQ,N,V_modificationDate"
+ "TQ,N,V_size"
+ "T^v,N,V_cpPowerAssertion"
+ "T{os_unfair_lock_s=I},N,V_remoteCameraDevicesLock"
+ "T{os_unfair_lock_s=I},N,V_remoteManagerConnectionsLock"
+ "[%05d] --> %@"
+ "^v"
+ "_addedBundles"
+ "_camera"
+ "_cameraDictionary"
+ "_cpPowerAssertion"
+ "_deniedBundles"
+ "_deviceListQueue"
+ "_deviceOperationUnderlyingQueue"
+ "_hasThumbnail"
+ "_listener"
+ "_localizedName"
+ "_managedObjectName"
+ "_orientation"
+ "_osTransactions"
+ "_parentObjectHandle"
+ "_primaryIdentifierString"
+ "_readOnly"
+ "_remoteCameraDevices"
+ "_remoteCameraDevicesLock"
+ "_remoteManagerConnections"
+ "_remoteManagerConnectionsLock"
+ "_sessionManager"
+ "_size"
+ "_startDeviceNotifications"
+ "_systemDaemon"
+ "_topLevel"
+ "_uuidString"
+ "acceptConnection:"
+ "addRemoteCameraDevice:uuidString:deviceName:"
+ "addRemoteManagerConnection:"
+ "addedBundles"
+ "additionalProperties"
+ "allConnections"
+ "anonymousListener"
+ "auditToken"
+ "cameraDictionary"
+ "close device"
+ "close: %@"
+ "closeDevice"
+ "closeDevice:"
+ "com.apple.mscamerad-xpc+%@"
+ "control_informed"
+ "cpPowerAssertion"
+ "decodeBoolForKey:"
+ "decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:"
+ "decodeInt32ForKey:"
+ "decodeInt64ForKey:"
+ "decodeObjectOfClass:forKey:"
+ "deniedBundles"
+ "deviceContext"
+ "deviceListQueue"
+ "deviceOperationUnderlyingQueue"
+ "encodeBool:forKey:"
+ "encodeInt32:forKey:"
+ "encodeInt64:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "endpoint"
+ "evaulateCommonTCC:"
+ "holdPowerAssertion"
+ "initManaging:systemDaemon:"
+ "initWithCoder:"
+ "initWithDeviceContext:"
+ "initWithPrimaryIdentifierString:uuidString:localizedName:"
+ "initWithProxy:parentFolder:device:"
+ "listener"
+ "listener:shouldAcceptNewConnection:"
+ "localizedName"
+ "managedObjectName"
+ "notifyClientDeviceAdded:uuidString:deviceName:"
+ "notifyClientDeviceRemoved:"
+ "osTransactions"
+ "parentObjectHandle"
+ "primaryIdentifierString"
+ "privateBypass"
+ "readOnly"
+ "releasePowerAssertion"
+ "remoteCameraDevices"
+ "remoteCameraDevicesLock"
+ "remoteDeviceForPrimaryIdentifier:"
+ "remoteDeviceForUUID:"
+ "remoteManagerConnectionWithProcessIdentifierAuthorized:"
+ "remoteManagerConnections"
+ "remoteManagerConnectionsLock"
+ "removeRemoteCameraDevice:"
+ "removeRemoteManagerConnectionWithProcessIdentifier:"
+ "requestDeviceListWithOptions:reply"
+ "sendAddedItemsNotification:toConnections:"
+ "sendNote"
+ "sendNotification:toConnections:selector:"
+ "sendPTPEventNotification:"
+ "sendRemovedItemsNotification:toConnections:"
+ "sendStatusNotification:toConnections:"
+ "sendUpdatedItemsNotification:toConnections:"
+ "sessionManager"
+ "setAddedBundles:"
+ "setCamera:"
+ "setCameraDictionary:"
+ "setCpPowerAssertion:"
+ "setDeniedBundles:"
+ "setDeviceListQueue:"
+ "setDeviceOperationUnderlyingQueue:"
+ "setListener:"
+ "setLocalizedName:"
+ "setManagedObjectName:"
+ "setOsTransactions:"
+ "setParentObjectHandle:"
+ "setPrimaryIdentifierString:"
+ "setReadOnly:"
+ "setRemoteCameraDevices:"
+ "setRemoteCameraDevicesLock:"
+ "setRemoteManagerConnections:"
+ "setRemoteManagerConnectionsLock:"
+ "setSessionManager:"
+ "setSize:"
+ "setSystemDaemon:"
+ "setTopLevel:"
+ "setUnderlyingQueue:"
+ "setUuidString:"
+ "setWithObjects:"
+ "size"
+ "startDeviceNotifications"
+ "startListening"
+ "supportsSecureCoding"
+ "systemDaemon"
+ "topLevel"
+ "updateRemoteManagerConnectionWithProcessIdentifier:authorized:"
+ "uuidString"
+ "v24@0:8@\"ICSessionManager\"16"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8^v16"
+ "v24@0:8i16B20"
+ "v40@0:8@16@24:32"
+ "valueForEntitlement:"
- "%"
- "%@%@^%@"
- "%Y%m%dT%H%M%S.0"
- "<PTPObjectInfoDataset %p>{\n  _objectHandle:            0x%08lX\n  _storageID:            0x%08lX\n  _objectFormat:         %@\n  _protectionStatus:     %@\n  _objectCompressedSize: %llu\n  _thumbFormat:          %@\n  _thumbCompressedSize:  %lu\n  _thumbPixWidth:        %lu\n  _thumbPixHeight:       %lu\n  _imagePixWidth:        %lu\n  _imagePixHeight:       %lu\n  _imageBitDepth:        %lu\n  _parentObject:         0x%08lX\n  _associationType:      %@\n  _associationDesc:      0x%08lX\n  _sequenceNumber:       %lu\n  _filename:             %@\n  _captureDate:          %@\n  _modificationDate:     %@\n  _keywords:             %@\n}"
- "@\"NSMutableString\""
- "@\"NSUUID\""
- "@20@0:8i16"
- "@28@0:8*16I24"
- "@28@0:8@16i24"
- "@32@0:8*16I24i28"
- "B24@0:8I16i20"
- "BFAV"
- "BPIK"
- "BUUID"
- "CFN"
- "Dropping keyword: %@ identifier: %@ -- Would create string of illegal length: 0x%llx > 0xFF"
- "FPIK"
- "FPRINT"
- "G"
- "GUUID"
- "HFRV"
- "I20@0:8i16"
- "ICMSObjectInfoArray"
- "ICPTPObjectInfoArray"
- "IO"
- "Input Content Length Mismatch: contentLength: %d"
- "Keywords length of: %lu is larger than a uint8 and cannot be written."
- "MSObjectInfoDataset"
- "OAID"
- "ON"
- "Output Content Length Mismatch: contentLength: %d  datasetLength: %d\n"
- "PTPAssociationType2DPanoramic"
- "PTPAssociationTypeAlbum"
- "PTPAssociationTypeAncillaryData"
- "PTPAssociationTypeGenericFolder"
- "PTPAssociationTypeHorizontalPanoramic"
- "PTPAssociationTypeReserved (0x%04X)"
- "PTPAssociationTypeTimeSequence"
- "PTPAssociationTypeUndefined"
- "PTPAssociationTypeVendorDefined (0x%04X)"
- "PTPAssociationTypeVerticalPanoramic"
- "PTPObjInfo"
- "PTPObjectFormatCodeAIFF"
- "PTPObjectFormatCodeASF"
- "PTPObjectFormatCodeAVI"
- "PTPObjectFormatCodeAssociation"
- "PTPObjectFormatCodeBMP"
- "PTPObjectFormatCodeCIFF"
- "PTPObjectFormatCodeDPOF"
- "PTPObjectFormatCodeEXIF_JPEG"
- "PTPObjectFormatCodeExecutable"
- "PTPObjectFormatCodeFlashPix"
- "PTPObjectFormatCodeGIF"
- "PTPObjectFormatCodeHTML"
- "PTPObjectFormatCodeJFIF"
- "PTPObjectFormatCodeJP2"
- "PTPObjectFormatCodeJPX"
- "PTPObjectFormatCodeMOV"
- "PTPObjectFormatCodeMP3"
- "PTPObjectFormatCodeMPEG"
- "PTPObjectFormatCodePCD"
- "PTPObjectFormatCodePICT"
- "PTPObjectFormatCodePNG"
- "PTPObjectFormatCodeReserved1"
- "PTPObjectFormatCodeReserved2"
- "PTPObjectFormatCodeReservedForFuture (0x%04X)"
- "PTPObjectFormatCodeScript"
- "PTPObjectFormatCodeTIFF"
- "PTPObjectFormatCodeTIFF_EP"
- "PTPObjectFormatCodeTIFF_IT"
- "PTPObjectFormatCodeText"
- "PTPObjectFormatCodeUndefinedNonImageObject"
- "PTPObjectFormatCodeUnknownImageObject"
- "PTPObjectFormatCodeVendorDefined (0x%04X)"
- "PTPObjectFormatCodeWAV"
- "PTPObjectFormatCodeXML"
- "PTPObjectInfoDataset"
- "PTPProtectionStatusNoProtection"
- "PTPProtectionStatusReadOnly"
- "PTPProtectionStatusReserved (0x%04X)"
- "RUUID"
- "RUUID^"
- "SOCGID"
- "T@\"NSData\",R,C,N"
- "T@\"NSString\",C,N,V_captureDate"
- "T@\"NSString\",C,N,V_filename"
- "T@\"NSString\",C,N,V_modificationDate"
- "TI,N,V_associationDesc"
- "TI,N,V_imageBitDepth"
- "TI,N,V_imagePixHeight"
- "TI,N,V_imagePixWidth"
- "TI,N,V_parentObject"
- "TI,N,V_thumbCompressedSize"
- "TI,N,V_thumbOffset"
- "TI,N,V_thumbPixHeight"
- "TI,N,V_thumbPixWidth"
- "TLV"
- "TQ,N,V_captureDate_tvsec"
- "TQ,N,V_modificationDate_tvsec"
- "TQ,N,V_objectCompressedSize"
- "TS,N,V_associationType"
- "TS,N,V_imageOrientation"
- "TS,N,V_objectFormat"
- "TS,N,V_protectionStatus"
- "TS,N,V_thumbFormat"
- "UUID"
- "^"
- "_associationDesc"
- "_associationType"
- "_captureDate_tvsec"
- "_filename"
- "_imageBitDepth"
- "_imageOrientation"
- "_imagePixHeight"
- "_imagePixWidth"
- "_intervalSince1970"
- "_modificationDate_tvsec"
- "_objectCompressedSize"
- "_objectFormat"
- "_parentObject"
- "_protectionStatus"
- "_thumbCompressedSize"
- "_thumbFormat"
- "_thumbOffset"
- "_thumbPixHeight"
- "_thumbPixWidth"
- "addCustomKeyword:withIdentifier:"
- "associationDesc"
- "associationType"
- "captureDate_tvsec"
- "content"
- "content:"
- "contentLength:bufferLength:"
- "contentLength:bufferLength:contentType:"
- "contentLengthValid:forContentType:"
- "deleted sidecar: %@"
- "filename"
- "getCString:maxLength:encoding:"
- "imageBitDepth"
- "imageOrientation"
- "imagePixHeight"
- "imagePixWidth"
- "initWithBytes:length:contentType:"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithData:"
- "initWithData:contentType:"
- "initWithLength:"
- "initWithUUIDString:"
- "intervalSince1970"
- "modificationDate_tvsec"
- "objectBufferSizeForContentType:"
- "objectCompressedSize"
- "objectCompressedSize64"
- "objectContentSizeForContentType:"
- "objectFormat"
- "parentObject"
- "protectionStatus"
- "setAssociationDesc:"
- "setAssociationType:"
- "setCaptureDate_tvsec:"
- "setFilename:"
- "setImageBitDepth:"
- "setImageOrientation:"
- "setImagePixHeight:"
- "setImagePixWidth:"
- "setModificationDate_tvsec:"
- "setObjectCompressedSize:"
- "setObjectFormat:"
- "setParentObject:"
- "setProtectionStatus:"
- "setThumbCompressedSize:"
- "setThumbFormat:"
- "setThumbOffset:"
- "setThumbPixHeight:"
- "setThumbPixWidth:"
- "thumbCompressedSize"
- "thumbFormat"
- "thumbOffset"
- "thumbPixHeight"
- "thumbPixWidth"
- "updateCameraFile:withInfo:"
- "updateCameraFile:withKeywords:"
- "updateCameraFolder:withInfo:"
- "v32@0:8^I16^I24"
- "v36@0:8^I16^I24i32"
- "\x91"

```
