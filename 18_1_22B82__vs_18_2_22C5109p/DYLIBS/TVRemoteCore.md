## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-443.10.21.0.0
-  __TEXT.__text: 0xb6288
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x8624
+496.20.14.0.0
+  __TEXT.__text: 0xb9274
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_methlist: 0x895c
   __TEXT.__const: 0x23c40
-  __TEXT.__gcc_except_tab: 0xf20
-  __TEXT.__cstring: 0x54bf
-  __TEXT.__oslogstring: 0x840e
-  __TEXT.__unwind_info: 0x1c88
+  __TEXT.__gcc_except_tab: 0xf7c
+  __TEXT.__cstring: 0x569b
+  __TEXT.__oslogstring: 0x8579
+  __TEXT.__unwind_info: 0x1d40
   __TEXT.__eh_frame: 0x7f8
-  __TEXT.__objc_classname: 0x10cc
-  __TEXT.__objc_methname: 0x122f6
-  __TEXT.__objc_methtype: 0x3ca2
-  __TEXT.__objc_stubs: 0xb9c0
-  __DATA_CONST.__got: 0x778
-  __DATA_CONST.__const: 0x1a30
-  __DATA_CONST.__objc_classlist: 0x418
+  __TEXT.__objc_classname: 0x10f7
+  __TEXT.__objc_methname: 0x12827
+  __TEXT.__objc_methtype: 0x3d89
+  __TEXT.__objc_stubs: 0xbec0
+  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__const: 0x1af8
+  __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x178
+  __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d10
+  __DATA_CONST.__objc_selrefs: 0x3e98
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x348
+  __DATA_CONST.__objc_superrefs: 0x368
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x670
-  __AUTH_CONST.__const: 0x3b38
-  __AUTH_CONST.__cfstring: 0x74e0
-  __AUTH_CONST.__objc_const: 0x11918
-  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__auth_got: 0x688
+  __AUTH_CONST.__const: 0x3c18
+  __AUTH_CONST.__cfstring: 0x76e0
+  __AUTH_CONST.__objc_const: 0x120c0
+  __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x27b0
-  __DATA.__objc_ivar: 0xa24
-  __DATA.__data: 0x1280
-  __DATA.__bss: 0x130
+  __AUTH.__objc_data: 0x28f0
+  __DATA.__objc_ivar: 0xa70
+  __DATA.__data: 0x1220
+  __DATA.__bss: 0x150
   __DATA.__common: 0x9f8
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x88

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3243
-  Symbols:   3959
-  CStrings:  5478
+  Functions: 3316
+  Symbols:   4051
+  CStrings:  5603
 
Symbols:
+ _CFDictionaryGetInt64Ranged
+ _CFDictionaryGetTypedValue
+ _OBJC_CLASS_$_NSDateComponentsFormatter
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_CLASS_$_RTIInputSystemSourceSession
+ _OBJC_CLASS_$_TVRCFilmography
+ _OBJC_CLASS_$_TVRCFilmographyCategory
+ _OBJC_CLASS_$_TVRCMediaInfoRoleCategory
+ _OBJC_CLASS_$_TVRCPerson
+ _OBJC_CLASS_$_TVRCUTSPersonRequest
+ _OBJC_CLASS_$_WLKAddToUpNextRequest
+ _OBJC_METACLASS_$_TVRCFilmography
+ _OBJC_METACLASS_$_TVRCFilmographyCategory
+ _OBJC_METACLASS_$_TVRCMediaInfoRoleCategory
+ _OBJC_METACLASS_$_TVRCPerson
+ _OBJC_METACLASS_$_TVRCUTSPersonRequest
+ _RPErrorF
+ _RPOptionStatusFlags
+ _TVRCAddToUpNextEvent
CStrings:
+ "\x01\x13"
+ "\x01q"
+ "\b"
+ "\x12\x1f"
+ "\x14\x11!"
+ "### Activate failed: %!@(MISSING)\n"
+ "### RTI send text change failed: %!@(MISSING)\n"
+ "### TextInput change bad data\n"
+ "### TextInputStart failed: %!@(MISSING)\n"
+ "### TextInputStop failed: %!@(MISSING)\n"
+ "%!s(MISSING) impl:%!@(MISSING) %!@(MISSING)"
+ "%!s(MISSING) linkDevice=%!@(MISSING)"
+ "%!s(MISSING) sortedImpls:%!@(MISSING) %!@(MISSING)"
+ "-[TVRCRPCompanionLinkClientWrapper dealloc]"
+ "-[TVRCRapportDeviceImpl dealloc]"
+ "-[TVRCRapportDeviceQuery dealloc]"
+ "-[TVRCRapportDeviceQuery init]"
+ "-[TVRXDevice _reevaluate]"
+ "-[TVRXDevice _setImpl:]"
+ "-[TVRXDevice addDeviceImpl:]"
+ "-[TVRXDevice dealloc]"
+ "-[TVRXDevice preferredImpl]"
+ "-[TVRXDevice removeDeviceImpl:]"
+ "-[_TVRCRapportDeviceManager createOrUpdateDeviceImplForLinkDevice:]"
+ "-[_TVRCRapportDeviceManager removeDeviceImplForLinkDevice:]"
+ "; deviceImplSet=%!@(MISSING)"
+ "<TVRXDeviceQuery %!p(MISSING)> Device existed for removed television."
+ "<TVRXDeviceQuery %!p(MISSING)> Failed to remove device %!@(MISSING) because it doesn't exist."
+ "<TVRXDeviceQuery %!p(MISSING)> Found new device %!{(MISSING)public}@."
+ "<TVRXDeviceQuery %!p(MISSING)> Removed device %!{(MISSING)public}@."
+ "@\"<RPMessageable>\""
+ "@\"<TVRCServiceDeviceQueryDelegate>\""
+ "@\"<_TVRCDeviceImplDelegate>\""
+ "@\"TVRCUTSPersonRequest\""
+ "Activate\n"
+ "AddToUpNextEvent"
+ "After adding - DeviceImplMap: %!@(MISSING)"
+ "After removing - DeviceImplMap: %!@(MISSING)"
+ "Asking tvremoted to add %!@(MISSING) to UpNext for %!{(MISSING)public}@"
+ "Before adding - DeviceImplMap: %!@(MISSING)"
+ "Before removing - DeviceImplMap: %!@(MISSING)"
+ "Creating new device impl with device=%!{(MISSING)public}@, deviceRecords=%!{(MISSING)public}@"
+ "Device changed, device=%!{(MISSING)public}@, wrapper=%!@(MISSING)"
+ "Device impl to be removed = %!@(MISSING) for device id = %!@(MISSING)"
+ "Device will not be shown because isAppleTV=%!d(MISSING), supportsRemote=%!d(MISSING) for device:%!@(MISSING)"
+ "DeviceQuery Retry eventHandler called"
+ "Error adding to upNext %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "Invalidate\n"
+ "No implementation for performDocumentRequest: %!@(MISSING)\n"
+ "No messenger provided"
+ "RTI Change remote: %!d(MISSING) bytes\n"
+ "RTI Started: %!d(MISSING) bytes\n"
+ "RTI Stopped\n"
+ "RTI event: %!d(MISSING) bytes\n"
+ "Starting DeviceQuery retry timer"
+ "T@\"<RPMessageable>\",&,N,V_messenger"
+ "T@\"<TVRCServiceDeviceQueryDelegate>\",W,N,V_delegate"
+ "T@\"<_TVRCDeviceImpl>\",W,N,G_impl,S_setImpl:,V_impl"
+ "T@\"<_TVRCDeviceImplDelegate>\",W,N,V_delegate"
+ "T@\"NSArray\",&,N,V_roleCategories"
+ "T@\"NSArray\",R,N,V_categories"
+ "T@\"NSArray\",R,N,V_items"
+ "T@\"NSArray\",R,N,V_roles"
+ "T@\"NSDate\",R,N,V_birthDate"
+ "T@\"NSDate\",R,N,V_deathDate"
+ "T@\"NSMutableDictionary\",&,N,V_deviceImplMap"
+ "T@\"NSMutableDictionary\",&,N,V_deviceMap"
+ "T@\"NSMutableSet\",&,N,V_deviceImplSet"
+ "T@\"NSString\",R,N,V_bio"
+ "T@\"NSString\",R,N,V_birthplace"
+ "T@\"NSString\",R,N,V_identifier"
+ "T@\"NSString\",R,N,V_imageURLTemplate"
+ "T@\"NSString\",R,N,V_name"
+ "T@\"NSString\",R,N,V_roleDescription"
+ "T@\"NSString\",R,N,V_title"
+ "T@\"RTIInputSystemSourceSession\",R,N,V_rtiSession"
+ "T@\"TVRCUTSPersonRequest\",&,N,V_selfRetained"
+ "T@?,C,N,V_rtiUpdatedHandler"
+ "TB,N,V_receivedSiriSettings"
+ "TB,N,V_receivedVolumeSettings"
+ "TQ,R,N,V_priority"
+ "TVRCFilmography"
+ "TVRCFilmographyCategory"
+ "TVRCMediaInfoRoleCategory"
+ "TVRCPerson"
+ "TVRCServiceDeviceQueryDelegate"
+ "TVRCTextInputSession"
+ "TVRCUTSPersonRequest"
+ "TextInputStarted\n"
+ "TextInputStopped\n"
+ "T{CGSize=dd},R,N,V_imageSize"
+ "Waiting for volume or siri settings before notifying client of updated supproted buttons. receivedSiriSettings:%!d(MISSING), receivedVolumeSettings:%!d(MISSING)"
+ "_TVRCDeviceImplDelegate"
+ "_TVRCRapportMediaEventsManager timed out waiting for volume:%!d(MISSING) or siri:%!d(MISSING) settings, meaning it is unsupported"
+ "_TVRCRapportMediaEventsManager volume control is %!@(MISSING)"
+ "_activateWithCompletion:"
+ "_bio"
+ "_birthDate"
+ "_birthplace"
+ "_categories"
+ "_checkIfDuplicateNameButDifferentIDSIdentifier:linkDevice:"
+ "_dateFromNumber:"
+ "_deathDate"
+ "_deviceImplMap"
+ "_deviceImplSet"
+ "_deviceMap"
+ "_dispatchQueue"
+ "_findDeviceForIdentifier:createIfNeeded:"
+ "_formattedDateWithDate:"
+ "_handleTextInputChange:started:"
+ "_handleTextInputStarted:"
+ "_handleTextInputStopped:"
+ "_imageSize"
+ "_invalidate"
+ "_items"
+ "_messenger"
+ "_orderedItems"
+ "_priority"
+ "_receivedSiriSettings"
+ "_receivedVolumeSettings"
+ "_reevaluate"
+ "_roleCategories"
+ "_rtiSession"
+ "_rtiUpdatedHandler"
+ "_started"
+ "_tiC"
+ "_tiD"
+ "_tiStart"
+ "_tiStarted"
+ "_tiStop"
+ "_tiStopped"
+ "_tiV"
+ "_updateSupportedButtons"
+ "_urlFromString:"
+ "addDeviceImpl:"
+ "addItemForDeviceWithIdentifier:mediaIdentifier:completion:"
+ "addItemWithMediaIdentifier:completion:"
+ "addedDevice:"
+ "bio"
+ "birthDate"
+ "birthplace"
+ "canvas"
+ "canvases/Persons/%!@(MISSING)"
+ "categories"
+ "compare:"
+ "createOrUpdateDeviceImplForLinkDevice:"
+ "deathDate"
+ "device:didDisconnectWithReason:error:"
+ "device:didEncounterAuthenticationChallenge:"
+ "device:didUpdateFindMyRemoteSupported:"
+ "device:didUpdateName:"
+ "device:didUpdateNowPlayingInfo:"
+ "device:didUpdatePairedRemoteInfo:"
+ "device:didUpdateSupportedButtons:"
+ "deviceImplForLinkDevice:"
+ "deviceImplMap"
+ "deviceImplSet"
+ "deviceMap"
+ "didConnectWithDevice:"
+ "didUpdateAttentionStateWithDevice:"
+ "didUpdateSiriRemoteFindingStateWithDevice:"
+ "dispatchQueue"
+ "filmographyCategoryWithDictionary:"
+ "filmographyWithDictionaries:"
+ "formattedAge"
+ "formattedBirthDate"
+ "formattedDeathDate"
+ "headshot"
+ "imageSize"
+ "initWithDictionaries:"
+ "initWithRoleDescription:roles:"
+ "messenger"
+ "now"
+ "orderedItems"
+ "payloadWithData:"
+ "payloadWithData:version:"
+ "person"
+ "personWithDictionary:"
+ "preferredImpl"
+ "priority"
+ "q24@?0@\"TVRCMediaInfo\"8@\"TVRCMediaInfo\"16"
+ "receivedSiriSettings"
+ "receivedVolumeSettings"
+ "removeDeviceImpl:"
+ "removeDeviceImplForLinkDevice:"
+ "removedDevice:"
+ "requestForPersonID:completion:"
+ "roleCategories"
+ "roleCategoryWithRoleDescription:roles:"
+ "rtiUpdatedHandler"
+ "sendEventID:event:destinationID:options:completion:"
+ "setAllowedUnits:"
+ "setBio:"
+ "setBirthDate:"
+ "setBirthplace:"
+ "setDateStyle:"
+ "setDeathDate:"
+ "setDeviceImplMap:"
+ "setDeviceImplSet:"
+ "setDeviceMap:"
+ "setImageSize:"
+ "setPayloadDelegate:"
+ "setReceivedSiriSettings:"
+ "setReceivedVolumeSettings:"
+ "setRoleCategories:"
+ "setTimeStyle:"
+ "setUnitsStyle:"
+ "setUrl:"
+ "shelves"
+ "sortDescriptorWithKey:ascending:"
+ "sortUsingComparator:"
+ "sortedArrayUsingDescriptors:"
+ "stringFromDate:"
+ "stringFromTimeInterval:"
+ "supported"
+ "unsupported"
+ "v24@0:8@\"<_TVRCDeviceImpl>\"16"
+ "v24@0:8@\"<_TVRCDeviceImplDelegate>\"16"
+ "v24@0:8@\"_TVRCDeviceImpl\"16"
+ "v28@0:8@\"_TVRCDeviceImpl\"16B24"
+ "v32@0:8@\"_TVRCDeviceImpl\"16@\"NSSet\"24"
+ "v32@0:8@\"_TVRCDeviceImpl\"16@\"NSString\"24"
+ "v32@0:8@\"_TVRCDeviceImpl\"16@\"TVRCNowPlayingInfo\"24"
+ "v32@0:8@\"_TVRCDeviceImpl\"16@\"TVRCSiriRemoteInfo\"24"
+ "v32@0:8@\"_TVRCDeviceImpl\"16@\"TVRXDeviceAuthenticationChallenge\"24"
+ "v40@0:8@\"_TVRCDeviceImpl\"16q24@\"NSError\"32"
+ "version"
+ "{CGSize=\"width\"d\"height\"d}"
+ "{CGSize=dd}16@0:8"
- "\x12\x1e"
- "\x14\x11\x11"
- "%!s(MISSING) device=%!@(MISSING)"
- "-[_TVRCRapportDeviceManager createOrUpdateRecordForDevice:]"
- "-[_TVRCRapportDeviceManager removeDeviceRecordForDevice:]"
- "-[_TVRCRapportDeviceRecord updateTransportsForStatusFlags:]"
- "<TVRCDeviceQuery %!p(MISSING)> Aggregate existed for removed service."
- "<TVRCDeviceQuery %!p(MISSING)> HomeKit added service %!{(MISSING)public}@."
- "<TVRCDeviceQuery %!p(MISSING)> HomeKit removed service %!{(MISSING)public}@."
- "<TVRXDeviceQuery %!p(MISSING)> Aggregate existed for removed television."
- "<TVRXDeviceQuery %!p(MISSING)> Created %!{(MISSING)public}@"
- "<TVRXDeviceQuery %!p(MISSING)> RMS found new device %!{(MISSING)public}@."
- "<TVRXDeviceQuery %!p(MISSING)> RMS removed device %!{(MISSING)public}@."
- "<TVRXDeviceQuery %!p(MISSING)> Rapport found new device %!{(MISSING)public}@."
- "<TVRXDeviceQuery %!p(MISSING)> Rapport removed device %!{(MISSING)public}@."
- "<TVRXDeviceQuery %!p(MISSING)> Re-evaluating aggregates."
- "<TVRXDeviceQuery %!p(MISSING)> Removing %!l(MISSING)u aggregates."
- "@\"<TVRCRapportDeviceQueryDelegate>\""
- "@\"<_TVRCMatchPointDeviceQueryDelegate>\""
- "@\"<_TVRCRMSDeviceQueryDelegate>\""
- "@\"TVRXDevice\""
- "Adding transports for record=%!@(MISSING), WiFi=%!{(MISSING)bool}d, BLE=%!{(MISSING)bool}d"
- "After adding - DeviceRecords: %!@(MISSING)"
- "After removing - DeviceRecords: %!@(MISSING)"
- "BLE"
- "Before adding - DeviceRecords: %!@(MISSING)"
- "Before removing - DeviceRecords: %!@(MISSING)"
- "Creating new internal record with device=%!{(MISSING)public}@, deviceRecords=%!{(MISSING)public}@"
- "Device changed, device=%!{(MISSING)public}@"
- "Invalid device was told to disconnect,  device=%!{(MISSING)public}@"
- "Record id to be removed = %!@(MISSING) for device id = %!@(MISSING)"
- "Removing transports for record=%!@(MISSING), WiFi=%!{(MISSING)bool}d, BLE=%!{(MISSING)bool}d"
- "Retry eventHandler called"
- "Starting Retry Timer"
- "T@\"<TVRCRapportDeviceQueryDelegate>\",W,N,V_delegate"
- "T@\"<_TVRCDeviceImpl>\",&,N,G_impl,S_setImpl:,V_impl"
- "T@\"<_TVRCMatchPointDeviceQueryDelegate>\",W,N,V_delegate"
- "T@\"<_TVRCRMSDeviceQueryDelegate>\",W,N,V_delegate"
- "T@\"NSMutableDictionary\",&,N,V_aggregateDevices"
- "T@\"NSMutableDictionary\",&,N,V_deviceRecords"
- "T@\"NSMutableDictionary\",&,N,V_wrapperToIdentifierMapping"
- "T@\"RPCompanionLinkDevice\",R,N,V_device"
- "T@\"TVRCHMServiceWrapper\",&,N,V_homeKit"
- "T@\"TVRCRPCompanionLinkClientWrapper\",&,N,V_rapport"
- "T@\"TVRXDevice\",&,N,V_publicDevice"
- "T@\"TVRXDevice\",W,N,V_device"
- "T@\"_TVRCRMSDeviceWrapper\",&,N,V_remoteMediaService"
- "TB,N,V_deviceQueryRetryTimerFired"
- "TQ,R,N,V_transports"
- "TVRCRapportDeviceQueryDelegate"
- "WiFi"
- "_TVRCMatchPointDeviceQueryDelegate"
- "_TVRCRMSDeviceQueryDelegate"
- "_TVRCRapportDeviceRecord"
- "_TVRDeviceAggregate"
- "_aggregateDevices"
- "_checkIfDuplicateNameButDifferentIDSIdentifier:device:"
- "_deviceQueryRetryTimerFired"
- "_deviceRecords"
- "_findAggregateForIdentifier:createIfNeeded:"
- "_homeKit"
- "_publicDevice"
- "_rapport"
- "_reevaluateAggregates"
- "_remoteMediaService"
- "_transportForStatusFlag:"
- "_transports"
- "_wrapperForDevice:"
- "_wrapperToIdentifierMapping"
- "addTransportForStatusFlag:"
- "aggregateDevices"
- "appendUnsignedInteger:withName:"
- "bestImpl"
- "createOrUpdateRecordForDevice:"
- "deviceQueryRetryTimerFired"
- "deviceRecords"
- "hasAvailableTransports"
- "homeKit"
- "keyEnumerator"
- "matchpointDeviceQuery:addedService:"
- "matchpointDeviceQuery:removedService:"
- "publicDevice"
- "rapport"
- "rapportDeviceQuery:addedDevice:"
- "rapportDeviceQuery:removedDevice:"
- "recordForDevice:"
- "remoteMediaService"
- "removeDeviceRecordForDevice:"
- "removeObjectsForKeys:"
- "removeTransportForStatusFlag:"
- "rmsDeviceQuery:addedDevice:"
- "rmsDeviceQuery:removedDevice:"
- "setAggregateDevices:"
- "setDeviceQueryRetryTimerFired:"
- "setDeviceRecords:"
- "setHomeKit:"
- "setPublicDevice:"
- "setRapport:"
- "setRemoteMediaService:"
- "setWrapperToIdentifierMapping:"
- "transports"
- "updateTransportsForStatusFlags:"
- "v24@0:8@\"TVRXDevice\"16"
- "v32@0:8@\"TVRCMatchPointDeviceQuery\"16@\"TVRCHMServiceWrapper\"24"
- "v32@0:8@\"TVRCRapportDeviceQuery\"16@\"TVRCRPCompanionLinkClientWrapper\"24"
- "v32@0:8@\"_TVRCRMSDeviceQuery\"16@\"_TVRCRMSDeviceWrapper\"24"
- "wrapperToIdentifierMapping"

```
