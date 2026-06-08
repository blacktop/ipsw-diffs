## HeadphoneSettings

> `/System/Library/PrivateFrameworks/HeadphoneSettings.framework/HeadphoneSettings`

```diff

-455.6.0.0.0
-  __TEXT.__text: 0xd0dc
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0xdbc
-  __TEXT.__const: 0x324
-  __TEXT.__cstring: 0xbc9
-  __TEXT.__oslogstring: 0x884
-  __TEXT.__gcc_except_tab: 0x1a8
+2700.13.0.0.0
+  __TEXT.__text: 0xca50
+  __TEXT.__objc_methlist: 0xdfc
+  __TEXT.__const: 0x334
+  __TEXT.__cstring: 0xbd9
+  __TEXT.__oslogstring: 0x924
+  __TEXT.__gcc_except_tab: 0x1c0
   __TEXT.__constg_swiftt: 0xa4
   __TEXT.__swift5_typeref: 0xc2
   __TEXT.__swift5_reflstr: 0x6

   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x508
-  __TEXT.__eh_frame: 0x200
-  __TEXT.__objc_classname: 0x1c1
-  __TEXT.__objc_methname: 0x1d71
-  __TEXT.__objc_methtype: 0x527
-  __TEXT.__objc_stubs: 0x17a0
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x508
+  __TEXT.__swift_as_cont: 0xc
+  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__eh_frame: 0x1f8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x548
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e8
+  __DATA_CONST.__objc_selrefs: 0x900
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__const: 0x1d8
-  __AUTH_CONST.__cfstring: 0x10c0
+  __AUTH_CONST.__cfstring: 0x10e0
   __AUTH_CONST.__objc_const: 0x16f0
+  __AUTH_CONST.__auth_got: 0x438
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0xac

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
-  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A9F8FC4E-36D8-3340-8086-ED1C6D0040CE
-  Functions: 482
-  Symbols:   1187
-  CStrings:  787
+  UUID: FBC3CC3A-15B5-3346-84FB-770E1683CFF8
+  Functions: 486
+  Symbols:   1207
+  CStrings:  344
 
Symbols:
+ -[BTSDevice setWalletPassUID:]
+ -[BTSDevice walletPassUID]
+ -[BTSDeviceClassic setANCSAuthorization:]
+ -[BTSDeviceClassic walletPassUID]
+ -[BTSDeviceLE walletPassUID]
+ -[HPSThirdPartyHeadphonesDatasource _buildHeadphonesWithDADevices:]
+ -[HPSThirdPartyHeadphonesDatasource cachedHeadphones]
+ -[HPSThirdPartyHeadphonesDatasource refreshAsync]
+ -[HPSThirdPartyHeadphonesDatasource setCachedHeadphones:]
+ _OBJC_IVAR_$_BTSDevice._walletPassUID
+ _OBJC_IVAR_$_HPSThirdPartyHeadphonesDatasource._cachedHeadphones
+ ___49-[HPSThirdPartyHeadphonesDatasource refreshAsync]_block_invoke
+ ___49-[HPSThirdPartyHeadphonesDatasource refreshAsync]_block_invoke.158
+ ___49-[HPSThirdPartyHeadphonesDatasource refreshAsync]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e29_v24?0"NSArray"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.112
+ ___block_literal_global.78
+ ___swift_async_cont_functlets
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_buildHeadphonesWithDADevices:
+ _objc_msgSend$getDevicesWithFlags:completionHandler:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$refreshAsync
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_setProperty_nonatomic_copy
+ _swift_release_x20
+ _swift_release_x8
+ _swift_retain_x20
- -[HPSThirdPartyHeadphonesDatasource avDevices]
- -[HPSThirdPartyHeadphonesDatasource daDevices]
- -[HPSThirdPartyHeadphonesDatasource setAvDevices:]
- -[HPSThirdPartyHeadphonesDatasource setDaDevices:]
- _OBJC_IVAR_$_HPSThirdPartyHeadphonesDatasource._avDevices
- _OBJC_IVAR_$_HPSThirdPartyHeadphonesDatasource._daDevices
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___block_literal_global.39
- ___block_literal_global.71
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_HeadphoneSettings
- __swift_FORCE_LOAD_$_swiftMapKit
- __swift_FORCE_LOAD_$_swiftMapKit_$_HeadphoneSettings
- _objc_msgSend$getDevicesWithFlags:session:error:
- _objc_retain_x21
- _objc_retain_x23
- _swift_retain
CStrings:
+ "BTSDevice supportsANCS %s"
+ "Connected 3rd Party Headphones: BluetoothManager not yet available, deferring refresh until BluetoothAvailabilityChangedNotification"
+ "HeadphoneManager."
+ "PassUniqueID"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HPSThirdPartyHeadphonesDatasourceDelegate>\""
- "@\"AVOutputContext\""
- "@\"AVOutputDevice\""
- "@\"BTSDeviceClassic\""
- "@\"BTSDeviceLE\""
- "@\"BluetoothDevice\""
- "@\"CBCentralManager\""
- "@\"CBL2CAPChannel\""
- "@\"CBPeripheral\""
- "@\"DADevice\""
- "@\"DASession\""
- "@\"HPSThirdPartyHeadphonesDatasource\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"PSListController\""
- "@\"PSSpecifier\""
- "@\"UIImage\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16C24"
- "@28@0:8I16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24@32@40"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^i16"
- "B24@0:8i16I20"
- "B28@0:8i16@20"
- "BTSDevice"
- "BTSDeviceClassic"
- "BTSDeviceLE"
- "CBCentralManagerDelegate"
- "DKMessage"
- "HPMHeadphoneMangerTopLevelEntryUIHandling"
- "HPSConnectedHeadphoneInfo"
- "HPSConnectedHeadphonesController"
- "HPSHeadphoneDeepLinkHandler"
- "HPSProductUtils"
- "HPSThirdPartyHeadphone"
- "HPSThirdPartyHeadphonesDatasource"
- "HPSThirdPartyHeadphonesDatasourceDelegate"
- "HeadphoneManager.HeadphoneReplayDevice"
- "Health"
- "ID"
- "NSObject"
- "NSStreamDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"<HPSThirdPartyHeadphonesDatasourceDelegate>\",W,N,V_delegate"
- "T@\"AVOutputContext\",&,N,V_avOutputContext"
- "T@\"AVOutputDevice\",R,N,V_avDevice"
- "T@\"BTSDeviceClassic\",R,N,V_classicDevice"
- "T@\"BTSDeviceLE\",R,N,V_leDevice"
- "T@\"BluetoothDevice\",R,W,N,V_device"
- "T@\"CBCentralManager\",&,N,V_centralManager"
- "T@\"CBL2CAPChannel\",&,N,V_channelSoundingL2CAP"
- "T@\"DADevice\",&,N,V_underlyingDADevice"
- "T@\"DADevice\",R,N,V_daDevice"
- "T@\"DASession\",&,N,V_daSession"
- "T@\"HPSThirdPartyHeadphonesDatasource\",&,N,V_thirdPartyDatasource"
- "T@\"NSArray\",&,N,V_avDevices"
- "T@\"NSArray\",&,N,V_devices"
- "T@\"NSArray\",R,N"
- "T@\"NSDictionary\",&,N,V_daDevices"
- "T@\"NSMutableArray\",&,N,V_channelSoundingTXQueue"
- "T@\"NSString\",&,N,GlinkedRadioAddress,V_linkedRadioAddress"
- "T@\"NSString\",&,N,GrelatedFutureRadioAddress,V_relatedFutureRadioAddress"
- "T@\"NSString\",&,N,V_accessorySetupKitDisplayName"
- "T@\"NSString\",&,N,V_targetBtAddress"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,&,V_deviceID"
- "T@\"NSString\",R,&,V_deviceName"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"PSListController\",&,N,V_targetController"
- "T@\"PSSpecifier\",R,&,V_deviceSpecifier"
- "T@\"UIImage\",R,&,V_deviceImage"
- "T@\"UIImage\",R,N"
- "TB,N,GdoesSupportBackgroundNI"
- "TB,N,GisCTKDDevice"
- "TB,N,GisChannelSoundingDevice,V_isChannelSoundingDevice"
- "TB,N,GisHealthDevice"
- "TB,N,GisManagedByAliroWallet"
- "TB,N,GisManagedByWallet"
- "TB,N,GshouldDenyIncomingClassicConnection"
- "TB,R,N,GisManagedByDeviceAccess"
- "TB,R,N,GisMyDevice"
- "TQ,R"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_BTMAvailable"
- "_BTMPairedDevices"
- "_TtC17HeadphoneSettingsP33_3C725A656CA2BD5AE40EEE81FC87B25C19ResourceBundleClass"
- "__swift_objectForKeyedSubscript:"
- "_accessorySetupKitDisplayName"
- "_avDevice"
- "_avDevices"
- "_avOutputContext"
- "_centralManager"
- "_channelSoundingL2CAP"
- "_channelSoundingTXQueue"
- "_classicDevice"
- "_daDevice"
- "_daDevices"
- "_daSession"
- "_delegate"
- "_device"
- "_deviceChangeHandler"
- "_deviceID"
- "_deviceImage"
- "_deviceName"
- "_deviceSpecifier"
- "_devices"
- "_isChannelSoundingDevice"
- "_leDevice"
- "_linkedRadioAddress"
- "_peripheral"
- "_relatedFutureRadioAddress"
- "_targetBtAddress"
- "_targetController"
- "_thirdPartyDatasource"
- "_underlyingDADevice"
- "accessorySetupKitDisplayName"
- "activate"
- "addDelegate:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addTopLevelEntryWithHpDevice:"
- "address"
- "allValues"
- "ancsAuthorized"
- "appendBytes:length:"
- "appendData:"
- "array"
- "arrayWithArray:"
- "autorelease"
- "avDevice"
- "avDevices"
- "avOutputContext"
- "available"
- "bluetoothIdentifier"
- "boolFromBluetoothPreferences:"
- "bs_map:"
- "bs_reduce:block:"
- "btAddress"
- "btsDevice"
- "bundleForClass:"
- "bytes"
- "cancelPeripheralConnection:force:"
- "centralManager"
- "centralManager:connectionEventDidOccur:forPeripheral:"
- "centralManager:didConnectPeripheral:"
- "centralManager:didDisconnectPeripheral:error:"
- "centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:"
- "centralManager:didDiscoverPeripheral:advertisementData:RSSI:"
- "centralManager:didFailToConnectPeripheral:error:"
- "centralManager:didUpdateANCSAuthorizationForPeripheral:"
- "centralManager:willRestoreState:"
- "centralManagerDidUpdateState:"
- "channelSoundingL2CAP"
- "channelSoundingTXQueue"
- "class"
- "classicDevice"
- "close"
- "closeChannelSoundingL2CAP"
- "cloudPaired"
- "compare:"
- "compare:options:"
- "conformsToProtocol:"
- "connect"
- "connectPeripheral:options:"
- "connected"
- "connectedHeadphoneInfo"
- "connectedHeadphones"
- "controllerForSpecifier:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "ctkdDevice"
- "currentRunLoop"
- "currentThread"
- "customProperty:"
- "daDevice"
- "daDevices"
- "daSession"
- "data"
- "dataWithLength:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "delegate"
- "denyIncomingClassicConnection"
- "description"
- "device"
- "deviceConnectionHandler:"
- "deviceFromIdentifier:"
- "deviceID"
- "deviceImage"
- "deviceKey"
- "deviceName"
- "deviceSpecifier"
- "deviceSubType"
- "deviceType"
- "deviceWithDevice:"
- "deviceWithPeripheral:manager:"
- "devices"
- "dictionary"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "disconnect"
- "doesNotRecognizeSelector:"
- "doesSupportBackgroundNI"
- "encodeDKMessageRangingProcedureResultsContinue:"
- "encodeDKMessageRangingProcedureResultsStart:"
- "encodeStepData:"
- "encodeStepMode:"
- "enumerateObjectsUsingBlock:"
- "eventType"
- "firstObject"
- "getBehaviorForHIDDevice"
- "getDeviceIcon:"
- "getDeviceIconSymbolString:"
- "getDevicesWithFlags:session:error:"
- "getProductIDString:"
- "getProductSpecificString:descriptionKey:"
- "getSpecificStepFromResults:withIndex:"
- "groupSpecifierWithID:"
- "handleDAEvent:"
- "handleDeeplink:specifier:"
- "hasSpaceAvailable"
- "hasTag:"
- "hash"
- "headphoneDevice"
- "healthDevice"
- "healthDeviceType"
- "hpsDevices"
- "i16@0:8"
- "identifier"
- "image"
- "imageNamed:inBundle:"
- "init"
- "initPrivate"
- "initWithDevice:"
- "initWithDictionary:"
- "initWithHeadphoneDevice:btsDevice:"
- "initWithID:name:image:specifier:"
- "initWithLEDevice:classicDevice:daDevice:avDevice:"
- "initWithPeripheral:manager:"
- "insertObject:atIndex:"
- "isAirPods:"
- "isAppleAudioDevice"
- "isAppleHeadphone:"
- "isApplePencil:"
- "isBeatsNonWx:"
- "isCTKDDevice"
- "isCarPlayDevice"
- "isChannelSoundingDevice"
- "isConnectedToSystem"
- "isEqual:"
- "isEqualToString:"
- "isFeatureSupported:byDevice:"
- "isFeatureSupported:byProductId:"
- "isFirmwareUpdateRequiredDevice"
- "isGenuineAirPods"
- "isHIDDevice"
- "isHealthDevice"
- "isKindOfClass:"
- "isLimitedConnectivityDevice"
- "isManagedByAliroWallet"
- "isManagedByDeviceAccess"
- "isManagedByWallet"
- "isMemberOfClass:"
- "isMyDevice"
- "isPSVR2Controller"
- "isPeerCloudPaired:"
- "isPeerPaired:"
- "isProxy"
- "isRealityDevice"
- "isServiceSupported:"
- "isSpatialController"
- "isTemporaryPaired"
- "isTemporaryPairedDevice"
- "isiPad"
- "leDevice"
- "length"
- "linkedRadioAddress"
- "localizedDescription"
- "localizedStringForKey:value:table:"
- "magicPaired"
- "mainThread"
- "managedByAliroWallet"
- "managedByDeviceAccess"
- "managedByWallet"
- "maximumWriteValueLengthForType:"
- "mutableCopy"
- "myDevice"
- "name"
- "nicknameEnabled"
- "numberWithUnsignedLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "open"
- "openChannelSoundingL2CAP"
- "openL2CAPChannel:"
- "outputDevices"
- "outputStream"
- "paired"
- "pairedDevices"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "productId"
- "productName"
- "properties"
- "pulse"
- "q24@0:8@16"
- "relatedFutureRadioAddress"
- "release"
- "removeFromRunLoop:forMode:"
- "removeObjectAtIndex:"
- "removeObserver:"
- "removeTopLevelEntryWithHpDevice:"
- "replaceBytesInRange:withBytes:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retrievePeripheralWithAddress:"
- "routedThirdPartyHeadphones"
- "scheduleInRunLoop:forMode:"
- "self"
- "sendChannelSoundingResults:"
- "sendEntireProcedure:withMTU:"
- "sendNextChannelSoundingMessage"
- "setANCSAuthorization:"
- "setAccessorySetupKitDisplayName:"
- "setAvDevices:"
- "setAvOutputContext:"
- "setCentralManager:"
- "setChannelSoundingL2CAP:"
- "setChannelSoundingTXQueue:"
- "setCtkdDevice:"
- "setCustomProperty:value:"
- "setDaDevices:"
- "setDaSession:"
- "setDelegate:"
- "setDenyIncomingClassicConnection:"
- "setDeviceChangeHandler:"
- "setDevices:"
- "setEventHandler:"
- "setHealthDevice:"
- "setIsChannelSoundingDevice:"
- "setIsExclusivelyDeeplink:"
- "setLinkedRadioAddress:"
- "setManagedByAliroWallet:"
- "setManagedByWallet:"
- "setName:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setProperties:"
- "setRelatedFutureRadioAddress:"
- "setSpecifier:"
- "setSupportsBackgroundNI:"
- "setTargetBtAddress:"
- "setTargetController:"
- "setThirdPartyDatasource:"
- "setUnderlyingDADevice:"
- "setUserInfo:"
- "setUserName:"
- "setUserSelectedHealthDataSyncConfig:"
- "shared"
- "sharedInstance"
- "sharedPairingAgent"
- "sharedSystemAudioContext"
- "shouldDenyIncomingClassicConnection"
- "sortUsingComparator:"
- "specifierFor:btsDevice:"
- "state"
- "stream:handleEvent:"
- "streamError"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "subdataWithRange:"
- "superclass"
- "supportsANCS"
- "supportsBackgroundNI"
- "supportsCTKD"
- "systemImageNamed:"
- "tag:"
- "targetBtAddress"
- "targetController"
- "thirdPartyDatasource"
- "thirdPartyHeadphonesDatasourceDidUpdate:"
- "topLevelSpecifiers"
- "topLevelSpecifiersLegacey"
- "topLevelSpecifiersRedesign"
- "topLevelSpecifiersThirdParty"
- "underlyingDADevice"
- "unpair"
- "unpairPeer:"
- "unsignedCharValue"
- "unsignedShortValue"
- "untag:"
- "updateTitleBar"
- "updateTopLevelEntryWithHpDevice:"
- "userInfo"
- "userSelectedHealthDataSyncConfig"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"CBCentralManager\"16"
- "v24@0:8@\"HPMHeadphoneDevice\"16"
- "v24@0:8@\"HPSThirdPartyHeadphonesDatasource\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24"
- "v32@0:8@\"CBCentralManager\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSStream\"16Q24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSError\"32"
- "v40@0:8@\"CBCentralManager\"16q24@\"CBPeripheral\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16q24@32"
- "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSNumber\"40"
- "v48@0:8@16@24@32@40"
- "v52@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24d32B40@\"NSError\"44"
- "v52@0:8@16@24d32B40@44"
- "vendorId"
- "vendorIdSrc"
- "write:maxLength:"
- "zone"

```
