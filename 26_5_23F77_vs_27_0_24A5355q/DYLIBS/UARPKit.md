## UARPKit

> `/System/Library/PrivateFrameworks/UARPKit.framework/UARPKit`

```diff

-1345.120.5.0.0
-  __TEXT.__text: 0x1e234
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x1210
+1576.0.0.0.0
+  __TEXT.__text: 0x14480
+  __TEXT.__objc_methlist: 0x1470
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x2106
-  __TEXT.__gcc_except_tab: 0x132c
-  __TEXT.__oslogstring: 0x88e
-  __TEXT.__unwind_info: 0x608
-  __TEXT.__objc_classname: 0x1a8
-  __TEXT.__objc_methname: 0x42d0
-  __TEXT.__objc_methtype: 0x9b2
-  __TEXT.__objc_stubs: 0x1e40
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x368
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__cstring: 0x1e75
+  __TEXT.__gcc_except_tab: 0x340
+  __TEXT.__oslogstring: 0x7b1
+  __TEXT.__unwind_info: 0x420
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x430
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcd8
+  __DATA_CONST.__objc_selrefs: 0xd58
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1e0
-  __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x14e8
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x120
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__got: 0xd8
+  __AUTH_CONST.__cfstring: 0xb40
+  __AUTH_CONST.__objc_const: 0x1e80
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x190
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 197B4173-157F-3062-BE8A-D4FF53D147C4
-  Functions: 505
-  Symbols:   1580
-  CStrings:  839
+  UUID: 08B483BB-C35B-3A17-81DF-DF4F8222A4C3
+  Functions: 508
+  Symbols:   1663
+  CStrings:  332
 
Symbols:
+ +[UARPDeviceComponentConfiguration supportsSecureCoding]
+ +[UARPDeviceConfiguration supportsSecureCoding]
+ +[UARPDeviceEndpointConfiguration supportsSecureCoding]
+ +[UARPHostEndpointProperties supportsSecureCoding]
+ -[UARPDevice activeFirmwareVersion].cold.1
+ -[UARPDevice appleModelNumber]
+ -[UARPDevice availableFirmwareVersion]
+ -[UARPDevice availableFirmwareVersion].cold.1
+ -[UARPDevice configureDeviceInactivityTimeout:error:]
+ -[UARPDevice configureDevicePacketMaximumRetries:error:]
+ -[UARPDevice configureDevicePacketRetryTimeout:error:]
+ -[UARPDevice configureDeviceSupportsCharging:]
+ -[UARPDevice configureDeviceSupportsSiri:]
+ -[UARPDevice deactivate]
+ -[UARPDevice deviceReceiveUarpMessageFromTransport:].cold.2
+ -[UARPDevice deviceTransportAvailable:].cold.1
+ -[UARPDevice deviceTransportAvailable].cold.1
+ -[UARPDevice deviceTransportUnavailable].cold.2
+ -[UARPDevice deviceUnavailable].cold.1
+ -[UARPDevice directConfiguration]
+ -[UARPDevice hostEndpointDelegatePropertiesUpdated:endpointConfig:]
+ -[UARPDevice hostEndpointDelegatePropertiesUpdated:endpointConfig:].cold.1
+ -[UARPDevice inactivityTimer]
+ -[UARPDevice packetRetries]
+ -[UARPDevice packetRetryTimeout]
+ -[UARPDevice productGroup]
+ -[UARPDevice productNumber]
+ -[UARPDevice queryEndpointConfiguration]
+ -[UARPDevice queryEndpointConfiguration].cold.1
+ -[UARPDevice stagedFirmwareVersion].cold.1
+ -[UARPDevice supportsCharging]
+ -[UARPDevice supportsSiri]
+ -[UARPDevice(FeatureSupport) setDeviceAppleModelNumber:]
+ -[UARPDevice(FeatureSupport) setDeviceProductGroup:productNumber:]
+ -[UARPDevice(FeatureSupport) setDeviceSupportsCharging:]
+ -[UARPDevice(FeatureSupport) setDeviceSupportsSiri:]
+ -[UARPDeviceComponentConfiguration copyWithZone:]
+ -[UARPDeviceComponentConfiguration encodeWithCoder:]
+ -[UARPDeviceComponentConfiguration hash]
+ -[UARPDeviceComponentConfiguration initWithCoder:]
+ -[UARPDeviceComponentConfiguration isEqual:]
+ -[UARPDeviceComponentConfiguration setConfig:]
+ -[UARPDeviceConfiguration chipEpoch]
+ -[UARPDeviceConfiguration copyWithZone:]
+ -[UARPDeviceConfiguration enableFutureFWVersion]
+ -[UARPDeviceConfiguration enableMixMatch]
+ -[UARPDeviceConfiguration encodeWithCoder:]
+ -[UARPDeviceConfiguration hash]
+ -[UARPDeviceConfiguration initWithCoder:]
+ -[UARPDeviceConfiguration isEqual:]
+ -[UARPDeviceConfiguration life]
+ -[UARPDeviceConfiguration liveNonce]
+ -[UARPDeviceConfiguration manifestEpoch]
+ -[UARPDeviceConfiguration provisioning]
+ -[UARPDeviceConfiguration setChipEpoch:]
+ -[UARPDeviceConfiguration setEnableFutureFWVersion:]
+ -[UARPDeviceConfiguration setEnableMixMatch:]
+ -[UARPDeviceConfiguration setLife:]
+ -[UARPDeviceConfiguration setLiveNonce:]
+ -[UARPDeviceConfiguration setManifestEpoch:]
+ -[UARPDeviceConfiguration setProvisioning:]
+ -[UARPDeviceEndpoint endpointConfigAtIndex:]
+ -[UARPDeviceEndpointConfiguration componentAtIndex:]
+ -[UARPDeviceEndpointConfiguration copyWithZone:]
+ -[UARPDeviceEndpointConfiguration encodeWithCoder:]
+ -[UARPDeviceEndpointConfiguration hash]
+ -[UARPDeviceEndpointConfiguration initWithCoder:]
+ -[UARPDeviceEndpointConfiguration isDirectEndpont]
+ -[UARPDeviceEndpointConfiguration isEqual:]
+ -[UARPDeviceEndpointConfiguration setConfig:]
+ -[UARPDeviceManager endpointControllerDelegatePersonalizationStatus:assetUUID:status:].cold.1
+ -[UARPDeviceManager offerDynamicAsset:deviceEndpoint:assetTag:]
+ -[UARPDeviceManager queryEndpointConfiguration:]
+ -[UARPDeviceManager queryEndpointConfiguration:].cold.1
+ -[UARPHostEndpointProperties .cxx_destruct]
+ -[UARPHostEndpointProperties appleModelNumber]
+ -[UARPHostEndpointProperties areNullableStringsEqual:thatString:]
+ -[UARPHostEndpointProperties copyWithZone:]
+ -[UARPHostEndpointProperties description]
+ -[UARPHostEndpointProperties encodeWithCoder:]
+ -[UARPHostEndpointProperties hash]
+ -[UARPHostEndpointProperties inactivityTimer]
+ -[UARPHostEndpointProperties initWithCoder:]
+ -[UARPHostEndpointProperties isEqual:]
+ -[UARPHostEndpointProperties packetRetries]
+ -[UARPHostEndpointProperties packetRetryTimeout]
+ -[UARPHostEndpointProperties productGroup]
+ -[UARPHostEndpointProperties productNumber]
+ -[UARPHostEndpointProperties setAppleModelNumber:]
+ -[UARPHostEndpointProperties setInactivityTimer:]
+ -[UARPHostEndpointProperties setPacketRetries:]
+ -[UARPHostEndpointProperties setPacketRetryTimeout:]
+ -[UARPHostEndpointProperties setProductGroup:]
+ -[UARPHostEndpointProperties setProductNumber:]
+ -[UARPHostEndpointProperties setSupportsCharging:]
+ -[UARPHostEndpointProperties setSupportsSiri:]
+ -[UARPHostEndpointProperties setSupportsVoiceAssist:]
+ -[UARPHostEndpointProperties supportsCharging]
+ -[UARPHostEndpointProperties supportsSiri]
+ -[UARPHostEndpointProperties supportsVoiceAssist]
+ -[UARPManagedDevice deviceConsentToApplyFirmwareDenied:error:]
+ -[UARPManagedDevice deviceConsentToApplyFirmwareGranted:error:]
+ -[UARPManagedDevice deviceConsentToStageFirmwareDenied:error:]
+ -[UARPManagedDevice deviceConsentToStageFirmwareGranted:error:]
+ -[UARPManagedDevice initWithUUID:delegate:delegateQueue:]
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table123
+ GCC_except_table126
+ GCC_except_table36
+ GCC_except_table65
+ GCC_except_table81
+ GCC_except_table86
+ GCC_except_table92
+ GCC_except_table95
+ GCC_except_table98
+ OBJC_IVAR_$_UARPDevice._delegateQueue
+ OBJC_IVAR_$_UARPDevice._endpointConfiguration
+ OBJC_IVAR_$_UARPDevice._firmwareVersion
+ OBJC_IVAR_$_UARPDevice._log
+ OBJC_IVAR_$_UARPDevice._stagedFirmwareVersion
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_UARPHostEndpointProperties
+ _OBJC_CLASS_$_UARPManagedDevice
+ _OBJC_IVAR_$_UARPDevice._appleModelNumber
+ _OBJC_IVAR_$_UARPDevice._deactivated
+ _OBJC_IVAR_$_UARPDevice._deviceAvailable
+ _OBJC_IVAR_$_UARPDevice._inactivityTimer
+ _OBJC_IVAR_$_UARPDevice._packetRetries
+ _OBJC_IVAR_$_UARPDevice._packetRetryTimeout
+ _OBJC_IVAR_$_UARPDevice._productGroup
+ _OBJC_IVAR_$_UARPDevice._productNumber
+ _OBJC_IVAR_$_UARPDevice._supportsCharging
+ _OBJC_IVAR_$_UARPDevice._supportsSiri
+ _OBJC_IVAR_$_UARPDevice._transportAvailable
+ _OBJC_IVAR_$_UARPDeviceConfiguration._chipEpoch
+ _OBJC_IVAR_$_UARPDeviceConfiguration._enableFutureFWVersion
+ _OBJC_IVAR_$_UARPDeviceConfiguration._enableMixMatch
+ _OBJC_IVAR_$_UARPDeviceConfiguration._life
+ _OBJC_IVAR_$_UARPDeviceConfiguration._liveNonce
+ _OBJC_IVAR_$_UARPDeviceConfiguration._manifestEpoch
+ _OBJC_IVAR_$_UARPDeviceConfiguration._provisioning
+ _OBJC_IVAR_$_UARPDeviceManager._managerListener
+ _OBJC_IVAR_$_UARPHostEndpointProperties._appleModelNumber
+ _OBJC_IVAR_$_UARPHostEndpointProperties._inactivityTimer
+ _OBJC_IVAR_$_UARPHostEndpointProperties._packetRetries
+ _OBJC_IVAR_$_UARPHostEndpointProperties._packetRetryTimeout
+ _OBJC_IVAR_$_UARPHostEndpointProperties._productGroup
+ _OBJC_IVAR_$_UARPHostEndpointProperties._productNumber
+ _OBJC_IVAR_$_UARPHostEndpointProperties._supportsCharging
+ _OBJC_IVAR_$_UARPHostEndpointProperties._supportsSiri
+ _OBJC_IVAR_$_UARPHostEndpointProperties._supportsVoiceAssist
+ _OBJC_METACLASS_$_UARPHostEndpointProperties
+ _OBJC_METACLASS_$_UARPManagedDevice
+ _UARPManagedDeviceFirmwareApplyStatusToString
+ _UARPManagedDeviceFirmwareStagingStatusToString
+ __OBJC_$_CLASS_METHODS_UARPDeviceComponentConfiguration
+ __OBJC_$_CLASS_METHODS_UARPDeviceConfiguration
+ __OBJC_$_CLASS_METHODS_UARPDeviceEndpointConfiguration
+ __OBJC_$_CLASS_METHODS_UARPHostEndpointProperties
+ __OBJC_$_CLASS_PROP_LIST_UARPDeviceComponentConfiguration
+ __OBJC_$_CLASS_PROP_LIST_UARPDeviceConfiguration
+ __OBJC_$_CLASS_PROP_LIST_UARPDeviceEndpointConfiguration
+ __OBJC_$_CLASS_PROP_LIST_UARPHostEndpointProperties
+ __OBJC_$_INSTANCE_METHODS_UARPHostEndpointProperties
+ __OBJC_$_INSTANCE_METHODS_UARPManagedDevice
+ __OBJC_$_INSTANCE_VARIABLES_UARPHostEndpointProperties
+ __OBJC_$_PROP_LIST_UARPHostEndpointProperties
+ __OBJC_CLASS_PROTOCOLS_$_UARPDeviceComponentConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_UARPDeviceConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_UARPDeviceEndpointConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_UARPHostEndpointProperties
+ __OBJC_CLASS_RO_$_UARPHostEndpointProperties
+ __OBJC_CLASS_RO_$_UARPManagedDevice
+ __OBJC_METACLASS_RO_$_UARPHostEndpointProperties
+ __OBJC_METACLASS_RO_$_UARPManagedDevice
+ ___38-[UARPDeviceManager clearAssetFolders]_block_invoke_2
+ ___40-[UARPDevice queryEndpointConfiguration]_block_invoke
+ ___40-[UARPDevice queryEndpointConfiguration]_block_invoke.62
+ ___40-[UARPDevice queryEndpointConfiguration]_block_invoke.cold.1
+ ___40-[UARPDeviceManager clearPacketCaptures]_block_invoke_2
+ ___48-[UARPDevice(TapToRadar) tapToRadarStart:error:]_block_invoke.201
+ ___48-[UARPDeviceManager clearEncodedMappingDatabase]_block_invoke_2
+ ___48-[UARPDeviceManager queryEndpointConfiguration:]_block_invoke
+ ___48-[UARPDeviceManager queryEndpointConfiguration:]_block_invoke_2
+ ___63-[UARPDeviceManager offerDynamicAsset:deviceEndpoint:assetTag:]_block_invoke
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
+ _kUarpHostEndpointTransportXpcServiceName
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$ECID
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$appleModelNumber
+ _objc_msgSend$areNullableStringsEqual:thatString:
+ _objc_msgSend$assetIdentifier
+ _objc_msgSend$boardID
+ _objc_msgSend$chipID
+ _objc_msgSend$chipRevision
+ _objc_msgSend$componentAtIndex:
+ _objc_msgSend$componentTag
+ _objc_msgSend$deactivate
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$description
+ _objc_msgSend$directConfiguration
+ _objc_msgSend$ecidData
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$endpointConfigAtIndex:
+ _objc_msgSend$endpointControllerClearAssets:
+ _objc_msgSend$endpointControllerClearDatabase:
+ _objc_msgSend$endpointControllerClearPacketCaptures:
+ _objc_msgSend$endpointControllerOfferDynamicAsset:endpointUUID:assetUUID:assetTag:
+ _objc_msgSend$endpointControllerQueryEndpointConfig:reply:
+ _objc_msgSend$firmwareVersion
+ _objc_msgSend$friendlyName
+ _objc_msgSend$ftabGeneration
+ _objc_msgSend$hardwareVersion
+ _objc_msgSend$hostEndpointAvailable:releasePolicy:endpointProperties:
+ _objc_msgSend$hostEndpointQueryEndpointConfig:reply:
+ _objc_msgSend$hwFusingType
+ _objc_msgSend$inactivityTimer
+ _objc_msgSend$init
+ _objc_msgSend$isDirectEndpont
+ _objc_msgSend$isEqual:
+ _objc_msgSend$manufacturerName
+ _objc_msgSend$modelName
+ _objc_msgSend$nonce
+ _objc_msgSend$nonceSeed
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$packetRetries
+ _objc_msgSend$packetRetryTimeout
+ _objc_msgSend$productGroup
+ _objc_msgSend$productNumber
+ _objc_msgSend$productionMode
+ _objc_msgSend$queryEndpointConfiguration
+ _objc_msgSend$queryEndpointConfiguration:
+ _objc_msgSend$realHdcpKeyPresent
+ _objc_msgSend$securityDomain
+ _objc_msgSend$securityMode
+ _objc_msgSend$serialNumber
+ _objc_msgSend$setChipEpoch:
+ _objc_msgSend$setConfig:
+ _objc_msgSend$setEnableFutureFWVersion:
+ _objc_msgSend$setEnableMixMatch:
+ _objc_msgSend$setInactivityTimer:
+ _objc_msgSend$setLife:
+ _objc_msgSend$setLiveNonce:
+ _objc_msgSend$setManifestEpoch:
+ _objc_msgSend$setPacketRetries:
+ _objc_msgSend$setPacketRetryTimeout:
+ _objc_msgSend$setProductGroup:
+ _objc_msgSend$setProductNumber:
+ _objc_msgSend$setProvisioning:
+ _objc_msgSend$setSupportsCharging:
+ _objc_msgSend$setSupportsSiri:
+ _objc_msgSend$setSupportsVoiceAssist:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$supportsCharging
+ _objc_msgSend$supportsSiri
+ _objc_msgSend$supportsVoiceAssist
+ _objc_opt_isKindOfClass
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x8
- -[UARPDevice hostEndpointDelegatePropertiesUpdated:]
- -[UARPDevice hostEndpointDelegatePropertiesUpdated:].cold.1
- -[UARPDevice queryActiveFirmwareVersion]
- -[UARPDevice queryActiveFirmwareVersion].cold.1
- -[UARPDevice queryStagedFirmwareVersion]
- -[UARPDevice queryStagedFirmwareVersion].cold.1
- -[UARPDeviceManager appleModelNumber:endpointNumber:componentNumber:]
- -[UARPDeviceManager appleModelNumber:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager assetIdentifier:endpointNumber:componentNumber:]
- -[UARPDeviceManager assetIdentifier:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager boardID:endpointNumber:componentNumber:]
- -[UARPDeviceManager boardID:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager chipID:endpointNumber:componentNumber:]
- -[UARPDeviceManager chipID:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager chipRevision:endpointNumber:componentNumber:]
- -[UARPDeviceManager chipRevision:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager componentTag:endpointIndex:componentIndex:].cold.1
- -[UARPDeviceManager ecid:endpointNumber:componentNumber:]
- -[UARPDeviceManager ecid:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager ecidData:endpointNumber:componentNumber:]
- -[UARPDeviceManager ecidData:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager firmwareVersion:endpointNumber:componentNumber:]
- -[UARPDeviceManager firmwareVersion:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager friendlyName:endpointNumber:componentNumber:]
- -[UARPDeviceManager friendlyName:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager ftabGeneration:endpointNumber:componentNumber:]
- -[UARPDeviceManager ftabGeneration:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager hardwareVersion:endpointNumber:componentNumber:]
- -[UARPDeviceManager hardwareVersion:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager hwFusingType:endpointNumber:componentNumber:]
- -[UARPDeviceManager hwFusingType:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager manufacturerName:endpointNumber:componentNumber:]
- -[UARPDeviceManager manufacturerName:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager modelName:endpointNumber:componentNumber:]
- -[UARPDeviceManager modelName:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager nonce:endpointNumber:componentNumber:]
- -[UARPDeviceManager nonce:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager nonceSeed:endpointNumber:componentNumber:]
- -[UARPDeviceManager nonceSeed:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager numberOfComponents:endpointIndex:].cold.1
- -[UARPDeviceManager numberOfEndpoints:].cold.1
- -[UARPDeviceManager productionMode:endpointNumber:componentNumber:]
- -[UARPDeviceManager productionMode:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager realHdcpKeyPresent:endpointNumber:componentNumber:]
- -[UARPDeviceManager realHdcpKeyPresent:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager securityDomain:endpointNumber:componentNumber:]
- -[UARPDeviceManager securityDomain:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager securityMode:endpointNumber:componentNumber:]
- -[UARPDeviceManager securityMode:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager serialNumber:endpointNumber:componentNumber:]
- -[UARPDeviceManager serialNumber:endpointNumber:componentNumber:].cold.1
- -[UARPDeviceManager stageFirmwareAsset:deviceEndpoint:]
- -[UARPDeviceManager stagedFirmwareVersion:endpointNumber:componentNumber:]
- -[UARPDeviceManager stagedFirmwareVersion:endpointNumber:componentNumber:].cold.1
- GCC_except_table104
- GCC_except_table109
- GCC_except_table119
- GCC_except_table124
- GCC_except_table129
- GCC_except_table134
- GCC_except_table150
- GCC_except_table155
- GCC_except_table158
- GCC_except_table16
- GCC_except_table161
- GCC_except_table164
- GCC_except_table167
- GCC_except_table171
- GCC_except_table174
- GCC_except_table177
- GCC_except_table180
- GCC_except_table183
- GCC_except_table185
- GCC_except_table187
- GCC_except_table189
- GCC_except_table19
- GCC_except_table192
- GCC_except_table24
- GCC_except_table29
- GCC_except_table34
- GCC_except_table39
- GCC_except_table44
- GCC_except_table49
- GCC_except_table52
- GCC_except_table54
- GCC_except_table59
- GCC_except_table64
- GCC_except_table74
- GCC_except_table79
- GCC_except_table84
- GCC_except_table94
- GCC_except_table99
- _OBJC_IVAR_$_UARPDevice._delegateQueue
- _OBJC_IVAR_$_UARPDevice._firmwareVersion
- _OBJC_IVAR_$_UARPDevice._log
- _OBJC_IVAR_$_UARPDevice._stagedFirmwareVersion
- _OBJC_IVAR_$_UARPDeviceManager._xpcListener
- ___39-[UARPDeviceManager numberOfEndpoints:]_block_invoke
- ___39-[UARPDeviceManager numberOfEndpoints:]_block_invoke_2
- ___40-[UARPDevice queryActiveFirmwareVersion]_block_invoke
- ___40-[UARPDevice queryActiveFirmwareVersion]_block_invoke.56
- ___40-[UARPDevice queryActiveFirmwareVersion]_block_invoke.cold.1
- ___40-[UARPDevice queryStagedFirmwareVersion]_block_invoke
- ___40-[UARPDevice queryStagedFirmwareVersion]_block_invoke.58
- ___40-[UARPDevice queryStagedFirmwareVersion]_block_invoke.cold.1
- ___48-[UARPDevice(TapToRadar) tapToRadarStart:error:]_block_invoke.145
- ___54-[UARPDeviceManager numberOfComponents:endpointIndex:]_block_invoke
- ___54-[UARPDeviceManager numberOfComponents:endpointIndex:]_block_invoke_2
- ___57-[UARPDeviceManager ecid:endpointNumber:componentNumber:]_block_invoke
- ___57-[UARPDeviceManager ecid:endpointNumber:componentNumber:]_block_invoke_2
- ___58-[UARPDeviceManager nonce:endpointNumber:componentNumber:]_block_invoke
- ___58-[UARPDeviceManager nonce:endpointNumber:componentNumber:]_block_invoke_2
- ___59-[UARPDeviceManager chipID:endpointNumber:componentNumber:]_block_invoke
- ___59-[UARPDeviceManager chipID:endpointNumber:componentNumber:]_block_invoke_2
- ___60-[UARPDeviceManager boardID:endpointNumber:componentNumber:]_block_invoke
- ___60-[UARPDeviceManager boardID:endpointNumber:componentNumber:]_block_invoke_2
- ___61-[UARPDeviceManager ecidData:endpointNumber:componentNumber:]_block_invoke
- ___61-[UARPDeviceManager ecidData:endpointNumber:componentNumber:]_block_invoke_2
- ___62-[UARPDeviceManager modelName:endpointNumber:componentNumber:]_block_invoke
- ___62-[UARPDeviceManager modelName:endpointNumber:componentNumber:]_block_invoke_2
- ___62-[UARPDeviceManager nonceSeed:endpointNumber:componentNumber:]_block_invoke
- ___62-[UARPDeviceManager nonceSeed:endpointNumber:componentNumber:]_block_invoke_2
- ___63-[UARPDeviceManager componentTag:endpointIndex:componentIndex:]_block_invoke
- ___63-[UARPDeviceManager componentTag:endpointIndex:componentIndex:]_block_invoke_2
- ___65-[UARPDeviceManager chipRevision:endpointNumber:componentNumber:]_block_invoke
- ___65-[UARPDeviceManager chipRevision:endpointNumber:componentNumber:]_block_invoke_2
- ___65-[UARPDeviceManager endpointControllerDelegateEndpointAvailable:]_block_invoke.cold.1
- ___65-[UARPDeviceManager endpointControllerDelegateEndpointAvailable:]_block_invoke.cold.2
- ___65-[UARPDeviceManager friendlyName:endpointNumber:componentNumber:]_block_invoke
- ___65-[UARPDeviceManager friendlyName:endpointNumber:componentNumber:]_block_invoke_2
- ___65-[UARPDeviceManager hwFusingType:endpointNumber:componentNumber:]_block_invoke
- ___65-[UARPDeviceManager hwFusingType:endpointNumber:componentNumber:]_block_invoke_2
- ___65-[UARPDeviceManager securityMode:endpointNumber:componentNumber:]_block_invoke
- ___65-[UARPDeviceManager securityMode:endpointNumber:componentNumber:]_block_invoke_2
- ___65-[UARPDeviceManager serialNumber:endpointNumber:componentNumber:]_block_invoke
- ___65-[UARPDeviceManager serialNumber:endpointNumber:componentNumber:]_block_invoke_2
- ___67-[UARPDeviceManager ftabGeneration:endpointNumber:componentNumber:]_block_invoke
- ___67-[UARPDeviceManager ftabGeneration:endpointNumber:componentNumber:]_block_invoke_2
- ___67-[UARPDeviceManager productionMode:endpointNumber:componentNumber:]_block_invoke
- ___67-[UARPDeviceManager productionMode:endpointNumber:componentNumber:]_block_invoke_2
- ___67-[UARPDeviceManager securityDomain:endpointNumber:componentNumber:]_block_invoke
- ___67-[UARPDeviceManager securityDomain:endpointNumber:componentNumber:]_block_invoke_2
- ___68-[UARPDeviceManager assetIdentifier:endpointNumber:componentNumber:]_block_invoke
- ___68-[UARPDeviceManager assetIdentifier:endpointNumber:componentNumber:]_block_invoke_2
- ___68-[UARPDeviceManager firmwareVersion:endpointNumber:componentNumber:]_block_invoke
- ___68-[UARPDeviceManager firmwareVersion:endpointNumber:componentNumber:]_block_invoke_2
- ___68-[UARPDeviceManager hardwareVersion:endpointNumber:componentNumber:]_block_invoke
- ___68-[UARPDeviceManager hardwareVersion:endpointNumber:componentNumber:]_block_invoke_2
- ___69-[UARPDeviceManager appleModelNumber:endpointNumber:componentNumber:]_block_invoke
- ___69-[UARPDeviceManager appleModelNumber:endpointNumber:componentNumber:]_block_invoke_2
- ___69-[UARPDeviceManager manufacturerName:endpointNumber:componentNumber:]_block_invoke
- ___69-[UARPDeviceManager manufacturerName:endpointNumber:componentNumber:]_block_invoke_2
- ___71-[UARPDeviceManager realHdcpKeyPresent:endpointNumber:componentNumber:]_block_invoke
- ___71-[UARPDeviceManager realHdcpKeyPresent:endpointNumber:componentNumber:]_block_invoke_2
- ___74-[UARPDeviceManager stagedFirmwareVersion:endpointNumber:componentNumber:]_block_invoke
- ___74-[UARPDeviceManager stagedFirmwareVersion:endpointNumber:componentNumber:]_block_invoke_2
- _objc_msgSend$appleModelNumber:endpointNumber:componentNumber:
- _objc_msgSend$assetIdentifier:endpointNumber:componentNumber:
- _objc_msgSend$boardID:endpointNumber:componentNumber:
- _objc_msgSend$chipID:endpointNumber:componentNumber:
- _objc_msgSend$chipRevision:endpointNumber:componentNumber:
- _objc_msgSend$componentTag:endpointIndex:componentIndex:
- _objc_msgSend$ecid:endpointNumber:componentNumber:
- _objc_msgSend$ecidData:endpointNumber:componentNumber:
- _objc_msgSend$endpointControllerClearAssets
- _objc_msgSend$endpointControllerClearDatabase
- _objc_msgSend$endpointControllerClearPacketCaptures
- _objc_msgSend$endpointControllerQueryAppleModelNumber:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryAssetIdentifier:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryBoardID:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryChipID:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryComponentTag:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryECID:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryECIDData:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryFTABGeneration:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryFirmwareVersion:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryFriendlyName:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryHardwareFusingType:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryHardwareVersion:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryManufacturerName:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryModelName:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryNonce:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryNonceSeed:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryNumberOfComponents:endpointNumber:reply:
- _objc_msgSend$endpointControllerQueryNumberOfEndpoints:reply:
- _objc_msgSend$endpointControllerQueryProductionMode:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryRealHdcpKeyPresent:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQuerySecurityDomain:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQuerySecurityMode:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQuerySerialNumber:endpointNumber:componentNumber:reply:
- _objc_msgSend$endpointControllerQueryStagedFirmwareVersion:endpointNumber:componentNumber:reply:
- _objc_msgSend$firmwareVersion:endpointNumber:componentNumber:
- _objc_msgSend$friendlyName:endpointNumber:componentNumber:
- _objc_msgSend$ftabGeneration:endpointNumber:componentNumber:
- _objc_msgSend$hardwareVersion:endpointNumber:componentNumber:
- _objc_msgSend$hostEndpointAvailable:releasePolicy:
- _objc_msgSend$hostEndpointQueryFirmwareVersion:reply:
- _objc_msgSend$hostEndpointQueryStagedFirmwareVersion:reply:
- _objc_msgSend$hostEndpointSupportsChargingChimeDebounce:
- _objc_msgSend$hostEndpointSupportsHeySiri:
- _objc_msgSend$hostEndpointSupportsJustSiri:
- _objc_msgSend$hostEndpointSupportsVoiceAssist:
- _objc_msgSend$manufacturerName:endpointNumber:componentNumber:
- _objc_msgSend$modelName:endpointNumber:componentNumber:
- _objc_msgSend$nonce:endpointNumber:componentNumber:
- _objc_msgSend$nonceSeed:endpointNumber:componentNumber:
- _objc_msgSend$numberOfComponents:endpointIndex:
- _objc_msgSend$numberOfEndpoints:
- _objc_msgSend$numberWithUnsignedInteger:
- _objc_msgSend$productionMode:endpointNumber:componentNumber:
- _objc_msgSend$queryActiveFirmwareVersion
- _objc_msgSend$queryStagedFirmwareVersion
- _objc_msgSend$realHdcpKeyPresent:endpointNumber:componentNumber:
- _objc_msgSend$securityDomain:endpointNumber:componentNumber:
- _objc_msgSend$securityMode:endpointNumber:componentNumber:
- _objc_msgSend$serialNumber:endpointNumber:componentNumber:
- _objc_msgSend$stageFirmwareAsset:deviceEndpoint:tssServerURL:
- _objc_msgSend$stagedFirmwareVersion:endpointNumber:componentNumber:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _objc_setProperty_atomic
CStrings:
+ "%@-%lu"
+ "%lu-%lu"
+ "%s: DEACTIVATED %@"
+ "%s: Database Entries %lu"
+ "%s: Host Endpoint is %@, Asset is %@"
+ "%s: endpoint configuration is %@"
+ "%s: endpointUUID <%@> is not equal to our UUID <%@>"
+ "%s: hostEndpointQueryEndpointConfig failed with %@"
+ ", "
+ "-[UARPDevice activeFirmwareVersion]"
+ "-[UARPDevice availableFirmwareVersion]"
+ "-[UARPDevice hostEndpointDelegatePropertiesUpdated:endpointConfig:]"
+ "-[UARPDevice queryEndpointConfiguration]"
+ "-[UARPDevice queryEndpointConfiguration]_block_invoke"
+ "-[UARPDevice stagedFirmwareVersion]"
+ "-[UARPDeviceManager queryEndpointConfiguration:]"
+ "<"
+ ">"
+ "AppleModelNumber"
+ "Asset Corrupt"
+ "AssetIdentifier"
+ "Battery Power"
+ "BoardID"
+ "ChipEpoch"
+ "ChipID"
+ "ChipRevision"
+ "EcidData"
+ "EnableFutureFWVersion"
+ "EnableMixMatch"
+ "Failure In Use"
+ "Failure Mid-Upload"
+ "Failure Nothing Staged"
+ "Failure Unknown"
+ "FirmwareFusingType"
+ "FirmwareVersion"
+ "FriendlyName"
+ "FtabGeneration"
+ "HardwareVersion"
+ "Has hMismatch"
+ "In Progress"
+ "Inactivity Timer = %lu"
+ "Life"
+ "LiveNonce"
+ "Low Battery"
+ "ManifestEpoch"
+ "ManufacturerName"
+ "ModelName"
+ "Nonce"
+ "NonceSeed"
+ "Packet Retries  = %lu"
+ "Packet Retry Timeout = %lu"
+ "Personalization Failure"
+ "ProductionMode"
+ "Provisioning"
+ "RealHdcpKeyPresent"
+ "SecurityDomain"
+ "SecurityMode"
+ "SerialNumber"
+ "StagedFirmwareVersion"
+ "Success"
+ "Success - Needs Reboot"
+ "Success - Needs Restart"
+ "Unknown"
+ "Unknown Failure"
+ "Unknown Status"
+ "inactivityTimer"
+ "packetRetries"
+ "packetRetryTimeout"
+ "productGroup"
+ "productNumber"
+ "supportsCharging"
+ "supportsSiri"
+ "v16@?0@\"NSArray\"8"
- "%s: Out of band component index %@ on endpoint index %@ for device %@, which has %lu components"
- "%s: Out of band endpoint index %@ for device %@, which has %lu endpoints"
- "%s: active firmware version is %@"
- "%s: deviceUUID <%@> is not equal to our UUID <%@>"
- "%s: failed to create component config"
- "%s: failed to create endpoint config"
- "%s: hostEndpointQueryFirmwareVersion failed with %@"
- "%s: hostEndpointQueryStagedFirmwareVersion failed with %@"
- "-[UARPDevice hostEndpointDelegatePropertiesUpdated:]"
- "-[UARPDevice queryActiveFirmwareVersion]"
- "-[UARPDevice queryActiveFirmwareVersion]_block_invoke"
- "-[UARPDevice queryStagedFirmwareVersion]"
- "-[UARPDevice queryStagedFirmwareVersion]_block_invoke"
- "-[UARPDeviceManager appleModelNumber:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager assetIdentifier:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager boardID:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager chipID:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager chipRevision:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager componentTag:endpointIndex:componentIndex:]"
- "-[UARPDeviceManager ecid:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager ecidData:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager endpointControllerDelegateEndpointAvailable:]_block_invoke"
- "-[UARPDeviceManager firmwareVersion:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager friendlyName:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager ftabGeneration:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager hardwareVersion:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager hwFusingType:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager manufacturerName:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager modelName:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager nonce:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager nonceSeed:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager numberOfComponents:endpointIndex:]"
- "-[UARPDeviceManager numberOfEndpoints:]"
- "-[UARPDeviceManager productionMode:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager realHdcpKeyPresent:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager securityDomain:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager securityMode:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager serialNumber:endpointNumber:componentNumber:]"
- "-[UARPDeviceManager stagedFirmwareVersion:endpointNumber:componentNumber:]"
- ".cxx_destruct"
- "@\"<UARPDeviceDelegateProtocol>\""
- "@\"<UARPDeviceManagerDelegateProtocol>\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"NSXPCInterface\""
- "@\"NSXPCListener\""
- "@\"UARPDeviceConfiguration\""
- "@\"UARPDeviceManager\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24o^@32"
- "@40@0:8@16Q24Q32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24{_NSRange=QQ}32"
- "@48@0:8Q16Q24Q32Q40"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8o^@16"
- "B32@0:8@16@24"
- "B32@0:8@16@?24"
- "B32@0:8@16o^@24"
- "B40@0:8@16@24@32"
- "FeatureSupport"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Private"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q32@0:8@16Q24"
- "T@\"NSData\",C,V_ecidData"
- "T@\"NSData\",C,V_nonce"
- "T@\"NSData\",C,V_nonceSeed"
- "T@\"NSDictionary\",&,V_tssResponse"
- "T@\"NSDictionary\",R,V_tssRequest"
- "T@\"NSNumber\",C,V_ECID"
- "T@\"NSNumber\",C,V_boardID"
- "T@\"NSNumber\",C,V_chipID"
- "T@\"NSNumber\",C,V_chipRevision"
- "T@\"NSNumber\",C,V_ftabGeneration"
- "T@\"NSNumber\",C,V_productionMode"
- "T@\"NSNumber\",C,V_realHdcpKeyPresent"
- "T@\"NSNumber\",C,V_securityDomain"
- "T@\"NSNumber\",C,V_securityMode"
- "T@\"NSString\",&,V_appleModelNumber"
- "T@\"NSString\",&,V_assetIdentifier"
- "T@\"NSString\",&,V_firmwareVersion"
- "T@\"NSString\",&,V_friendlyName"
- "T@\"NSString\",&,V_hardwareVersion"
- "T@\"NSString\",&,V_hwFusingType"
- "T@\"NSString\",&,V_manufacturerName"
- "T@\"NSString\",&,V_modelName"
- "T@\"NSString\",&,V_serialNumber"
- "T@\"NSString\",&,V_stagedFirmwareVersion"
- "T@\"NSString\",R"
- "T@\"NSString\",R,V_componentTag"
- "T@\"NSURL\",R,V_url"
- "T@\"NSUUID\",R,V_uuid"
- "T@\"UARPDeviceConfiguration\",R,V_config"
- "TB,R"
- "TB,R,V_isObservedOnly"
- "TB,V_supportsChargingChimeDebounce"
- "TB,V_supportsHeySiri"
- "TB,V_supportsJustSiri"
- "TB,V_supportsVoiceAssist"
- "TQ,R,V_buildVersion"
- "TQ,R,V_endpointID"
- "TQ,R,V_majorVersion"
- "TQ,R,V_minorVersion"
- "TQ,R,V_releaseVersion"
- "TapToRadar"
- "UARPDevice"
- "UARPDeviceAsset"
- "UARPDeviceComponentConfiguration"
- "UARPDeviceConfiguration"
- "UARPDeviceEndpoint"
- "UARPDeviceEndpointConfiguration"
- "UARPDeviceFirmwareVersion"
- "UARPDeviceManager"
- "UARPDeviceTatsuTicket"
- "UARPEndpointControllerDelegateProtocol"
- "UARPEndpointControllerProtocol"
- "UARPHostEndpointDelegateProtocol"
- "UARPHostEndpointProtocol"
- "URLByAppendingPathComponent:isDirectory:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "_ECID"
- "_appleModelNumber"
- "_assetIdentifier"
- "_assetsCollectionURL"
- "_boardID"
- "_buildVersion"
- "_chipID"
- "_chipRevision"
- "_componentTag"
- "_components"
- "_config"
- "_debug"
- "_debugDownstream"
- "_debugTransfer"
- "_debugTransport"
- "_delegate"
- "_delegateQueue"
- "_deviceAssets"
- "_deviceEndpoints"
- "_deviceManager"
- "_ecidData"
- "_endpointID"
- "_endpoints"
- "_firmwareVersion"
- "_friendlyName"
- "_ftabGeneration"
- "_hardwareVersion"
- "_hwFusingType"
- "_internalQueue"
- "_isObservedOnly"
- "_log"
- "_majorVersion"
- "_manufacturerName"
- "_minorVersion"
- "_modelName"
- "_mustSuspend"
- "_nonce"
- "_nonceSeed"
- "_productionMode"
- "_realHdcpKeyPresent"
- "_releaseVersion"
- "_securityDomain"
- "_securityMode"
- "_serialNumber"
- "_setQueue:"
- "_stagedFirmwareVersion"
- "_supportsChargingChimeDebounce"
- "_supportsHeySiri"
- "_supportsJustSiri"
- "_supportsVoiceAssist"
- "_tssRequest"
- "_tssResponse"
- "_url"
- "_uuid"
- "_xpcConnection"
- "_xpcInterface"
- "_xpcListener"
- "activate"
- "activeFirmwareVersion"
- "addEndpointConfiguration:"
- "addObject:"
- "appleModelNumber:endpointIndex:"
- "appleModelNumber:endpointIndex:componentIndex:"
- "appleModelNumber:endpointNumber:componentNumber:"
- "applyStagedAssets:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "assetIdentifier"
- "assetIdentifier:endpointIndex:"
- "assetIdentifier:endpointIndex:componentIndex:"
- "assetIdentifier:endpointNumber:componentNumber:"
- "assetPersonalizationComplete:endpointUUID:personalizationTicket:"
- "assetPersonalizationComplete:endpointUUID:tssOptions:"
- "attributesOfItemAtPath:error:"
- "boardID"
- "boardID:endpointIndex:"
- "boardID:endpointIndex:componentIndex:"
- "boardID:endpointNumber:componentNumber:"
- "boolValue"
- "buildVersion"
- "bytes"
- "cacheAsset:assetUUID:appendData:"
- "cacheAsset:deviceEndpoint:error:"
- "cacheAssetFinish:assetUUID:hashData:"
- "cacheAssetStart:assetUUID:"
- "checkAssetManager:"
- "chipID"
- "chipID:endpointIndex:"
- "chipID:endpointIndex:componentIndex:"
- "chipID:endpointNumber:componentNumber:"
- "chipRevision"
- "chipRevision:endpointIndex:"
- "chipRevision:endpointIndex:componentIndex:"
- "chipRevision:endpointNumber:componentNumber:"
- "clearAssetFolders"
- "clearEncodedMappingDatabase"
- "clearPacketCaptures"
- "closeAndReturnError:"
- "compare:"
- "componentTag:endpointIndex:componentIndex:"
- "componentsSeparatedByString:"
- "copy"
- "copyItemAtURL:toURL:error:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createFileAtPath:contents:attributes:"
- "dataWithBytes:length:"
- "deactivate"
- "dealloc"
- "decodeObjectOfClass:forKey:"
- "defaultManager"
- "description"
- "deviceAssetForUUID:"
- "deviceAvailable"
- "deviceAvailable:"
- "deviceEndpointForUUID:"
- "deviceReceiveUarpMessageFromTransport:"
- "deviceSendUarpMessageToTransport:uarpMessage:"
- "deviceSupportsChargingChimeDebounce"
- "deviceSupportsHeySiri"
- "deviceSupportsJustSiri"
- "deviceSupportsVoiceAssist"
- "deviceTransportAvailable"
- "deviceTransportAvailable:"
- "deviceTransportNotNeeded:"
- "deviceTransportSetupRequested:"
- "deviceTransportTeardown:"
- "deviceTransportUnavailable"
- "deviceUnavailable"
- "deviceUnresponsive:"
- "doesNotRecognizeSelector:"
- "ecid:endpointIndex:"
- "ecid:endpointIndex:componentIndex:"
- "ecid:endpointNumber:componentNumber:"
- "ecidData"
- "ecidData:endpointIndex:"
- "ecidData:endpointIndex:componentIndex:"
- "ecidData:endpointNumber:componentNumber:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endpoint"
- "endpointControllerApplyStagedAssets:"
- "endpointControllerCacheAsset:assetUUID:appendData:reply:"
- "endpointControllerCacheAssetFinish:assetUUID:hashData:reply:"
- "endpointControllerCacheAssetStart:assetUUID:reply:"
- "endpointControllerCheckAssetManager:"
- "endpointControllerClearAssets"
- "endpointControllerClearDatabase"
- "endpointControllerClearPacketCaptures"
- "endpointControllerDelegateAppliedStagedAssets:layer3Flags:"
- "endpointControllerDelegateAssetMetaDataComplete:assetUUID:assetTag:"
- "endpointControllerDelegateAssetOffered:assetUUID:assetTag:"
- "endpointControllerDelegateAssetPayloadData:assetUUID:payloadTag:payloadIndex:payloadOffset:dataLength:"
- "endpointControllerDelegateAssetPayloadDataComplete:assetUUID:payloadTag:payloadIndex:"
- "endpointControllerDelegateAssetPayloadMetaDataComplete:assetUUID:payloadTag:payloadIndex:"
- "endpointControllerDelegateAssetPayloadReady:assetUUID:payloadTag:payloadIndex:"
- "endpointControllerDelegateAssetTransferProgress:assetUUID:bytesTransferred:totalBytes:"
- "endpointControllerDelegateAssetTransferStatus:assetUUID:transferStatus:"
- "endpointControllerDelegateEndpointAvailable:"
- "endpointControllerDelegateEndpointPropertiesUpdated:"
- "endpointControllerDelegateEndpointUnavailable:"
- "endpointControllerDelegatePersonalizationStatus:assetUUID:status:"
- "endpointControllerDelegateRescindedAssets:"
- "endpointControllerDelegateRxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:"
- "endpointControllerDelegateRxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:"
- "endpointControllerDelegateTxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:"
- "endpointControllerDelegateTxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:"
- "endpointControllerExportDynamicAsset:endpointUUID:dynamicAssetURL:reply:"
- "endpointControllerExportPersonalizedAsset:endpointUUID:personalizedAssetURL:reply:"
- "endpointControllerMonitorForDevices"
- "endpointControllerOfferFirmwareAsset:endpointUUID:assetUUID:"
- "endpointControllerOfferFirmwareAsset:endpointUUID:assetUUID:tssServerURL:"
- "endpointControllerPauseAssetManagerNotifications:reply:"
- "endpointControllerPersonalizeFirmwareAsset:endpointUUID:assetUUID:tatsuRequest:tssServerURL:"
- "endpointControllerPersonalizeFirmwareAsset:endpointUUID:assetUUID:tssServerURL:"
- "endpointControllerPullDynamicAsset:assetUUID:range:reply:"
- "endpointControllerPullDynamicAssetFinish:assetUUID:hashData:reply:"
- "endpointControllerPullDynamicAssetStart:assetUUID:reply:"
- "endpointControllerQueryAppleModelNumber:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryAssetIdentifier:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryBoardID:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryChipID:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryChipRevision:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryComponentTag:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryECID:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryECIDData:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryEncodedMappingDatabase:"
- "endpointControllerQueryFTABGeneration:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryFirmwareVersion:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryFriendlyName:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryHardwareFusingType:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryHardwareVersion:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryManufacturerName:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryModelName:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryNonce:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryNonceSeed:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryNumberOfComponents:endpointNumber:reply:"
- "endpointControllerQueryNumberOfEndpoints:reply:"
- "endpointControllerQueryProductionMode:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryRealHdcpKeyPresent:endpointNumber:componentNumber:reply:"
- "endpointControllerQuerySecurityDomain:endpointNumber:componentNumber:reply:"
- "endpointControllerQuerySecurityMode:endpointNumber:componentNumber:reply:"
- "endpointControllerQuerySerialNumber:endpointNumber:componentNumber:reply:"
- "endpointControllerQueryStagedFirmwareVersion:endpointNumber:componentNumber:reply:"
- "endpointControllerRescindStagedAssets:"
- "endpointControllerResumeAssetManagerNotifications:reply:"
- "endpointControllerSolicitAsset:assetTag:assetURL:assetUUID:"
- "endpointControllerStageAndApplyFirmwareAsset:endpointUUID:assetUUID:tssServerURL:"
- "endpointControllerStageFirmwareAsset:endpointUUID:assetUUID:tssServerURL:"
- "endpointControllerTapToRadarStart:reply:"
- "endpointControllerTapToRadarStop:"
- "endpointControllerTssRequestForPersonalizedAsset:endpointUUID:reply:"
- "endpointControllerTssRequestsForPersonalizedAsset:endpointUUID:reply:"
- "endpointControllerTssResponseForPersonalizedAsset:endpointUUID:reply:"
- "endpointControllerTssResponsesForPersonalizedAsset:endpointUUID:reply:"
- "endpoints"
- "enumeratorAtPath:"
- "exportPersonalizeFirmware:deviceEndpoint:personalizedAssetURL:"
- "exportSolicitedAsset:deviceEndpoint:dynamicAssetURL:"
- "exportedInterface"
- "fileExistsAtPath:"
- "fileHandleForReadingFromURL:error:"
- "fileHandleForWritingToURL:error:"
- "fileSize"
- "fileURLWithPathComponents:"
- "firmwareVersion"
- "firmwareVersion:endpointIndex:"
- "firmwareVersion:endpointIndex:componentIndex:"
- "firmwareVersion:endpointNumber:componentNumber:"
- "friendlyName"
- "friendlyName:endpointIndex:"
- "friendlyName:endpointIndex:componentIndex:"
- "friendlyName:endpointNumber:componentNumber:"
- "ftabGeneration"
- "ftabGeneration:endpointIndex:"
- "ftabGeneration:endpointIndex:componentIndex:"
- "ftabGeneration:endpointNumber:componentNumber:"
- "getIsObservedOnly"
- "hardwareVersion"
- "hardwareVersion:endpointIndex:"
- "hardwareVersion:endpointIndex:componentIndex:"
- "hardwareVersion:endpointNumber:componentNumber:"
- "hash"
- "hostEndpointAvailable:mfiPG:mfiPN:"
- "hostEndpointAvailable:releasePolicy:"
- "hostEndpointAvailableAndTransportAvailable:mfiPG:mfiPN:uarpMessage:"
- "hostEndpointAvailableAndTransportAvailable:uarpMessage:"
- "hostEndpointCopySourceURL:destinationURL:"
- "hostEndpointDelegateAssetTransferProgress:assetUUID:bytesTransferred:totalBytes:"
- "hostEndpointDelegateAssetTransferStatus:assetUUID:transferStatus:"
- "hostEndpointDelegatePropertiesUpdated:"
- "hostEndpointDelegateProvideSandBoxExtension:token:assetURL:appleModelNumber:serialNumber:"
- "hostEndpointDelegateTransportNotNeeded:"
- "hostEndpointDelegateTransportSetup:"
- "hostEndpointDelegateTransportTeardown:"
- "hostEndpointDelegateUARPMessageSend:uarpMessage:"
- "hostEndpointDelegateUnresponsive:"
- "hostEndpointQueryFirmwareVersion:reply:"
- "hostEndpointQueryStagedFirmwareVersion:reply:"
- "hostEndpointSupportsChargingChimeDebounce:"
- "hostEndpointSupportsHeySiri:"
- "hostEndpointSupportsJustSiri:"
- "hostEndpointSupportsVoiceAssist:"
- "hostEndpointTapToRadarStart:reply:"
- "hostEndpointTapToRadarStop:"
- "hostEndpointTransportAvailable:releasePolicy:"
- "hostEndpointTransportUnavailable:"
- "hostEndpointUARPMessageReceived:uarpMessage:"
- "hostEndpointUnavailable:"
- "hwFusingType"
- "hwFusingType:endpointIndex:"
- "hwFusingType:endpointIndex:componentIndex:"
- "hwFusingType:endpointNumber:componentNumber:"
- "init"
- "initWithCoder:"
- "initWithComponentTag:"
- "initWithComponentTag:tssRequest:"
- "initWithDelegate:delegateQueue:listener:"
- "initWithDeviceManager:uuid:"
- "initWithEndpointID:"
- "initWithListenerEndpoint:"
- "initWithMachServiceName:options:"
- "initWithMajorVersion:minorVersion:releaseVersion:buildVersion:"
- "initWithURL:"
- "initWithUUID:"
- "initWithUUID:delegate:delegateQueue:"
- "initWithUUID:delegate:delegateQueue:listener:"
- "initWithVersionString:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqualToString:"
- "isMatchingUUID:"
- "isObservedOnly"
- "isValid"
- "lastPathComponent"
- "length"
- "majorVersion"
- "manufacturerName"
- "manufacturerName:endpointIndex:"
- "manufacturerName:endpointIndex:componentIndex:"
- "manufacturerName:endpointNumber:componentNumber:"
- "minorVersion"
- "modelName"
- "modelName:endpointIndex:"
- "modelName:endpointIndex:componentIndex:"
- "modelName:endpointNumber:componentNumber:"
- "nextObject"
- "nonce"
- "nonce:endpointIndex:"
- "nonce:endpointIndex:componentIndex:"
- "nonce:endpointNumber:componentNumber:"
- "nonceSeed"
- "nonceSeed:endpointIndex:"
- "nonceSeed:endpointIndex:componentIndex:"
- "nonceSeed:endpointNumber:componentNumber:"
- "numberOfComponents:endpointIndex:"
- "numberOfEndpoints:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "offerFirmwareAsset:deviceEndpoint:"
- "path"
- "pauseAssetManagerNotifications:"
- "personalizeFirmware:deviceEndpoint:tssServerURL:"
- "productionMode"
- "productionMode:endpointIndex:"
- "productionMode:endpointIndex:componentIndex:"
- "productionMode:endpointNumber:componentNumber:"
- "pullDynamicAsset:assetUUID:range:"
- "pullDynamicAssetFinish:assetUUID:hashData:"
- "pullDynamicAssetStart:assetUUID:"
- "queryActiveFirmwareVersion"
- "queryEncodedMappingDatabase"
- "queryStagedFirmwareVersion"
- "readDataUpToLength:error:"
- "realHdcpKeyPresent"
- "realHdcpKeyPresent:endpointIndex:"
- "realHdcpKeyPresent:endpointIndex:componentIndex:"
- "realHdcpKeyPresent:endpointNumber:componentNumber:"
- "releaseVersion"
- "releaseXPCConnection"
- "remoteObjectInterface"
- "remoteObjectProxy"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeObject:"
- "rescindAssets:"
- "resumeAssetManagerNotifications:"
- "securityDomain"
- "securityDomain:endpointIndex:"
- "securityDomain:endpointIndex:componentIndex:"
- "securityDomain:endpointNumber:componentNumber:"
- "securityMode"
- "securityMode:endpointIndex:"
- "securityMode:endpointIndex:componentIndex:"
- "securityMode:endpointNumber:componentNumber:"
- "serialNumber"
- "serialNumber:endpointIndex:"
- "serialNumber:endpointIndex:componentIndex:"
- "serialNumber:endpointNumber:componentNumber:"
- "setAnonymousListener:"
- "setAppleModelNumber:"
- "setAssetIdentifier:"
- "setBoardID:"
- "setChipID:"
- "setChipRevision:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setECID:"
- "setEcidData:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFirmwareVersion:"
- "setFriendlyName:"
- "setFtabGeneration:"
- "setHardwareVersion:"
- "setHwFusingType:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setManufacturerName:"
- "setModelName:"
- "setNonce:"
- "setNonceSeed:"
- "setProductionMode:"
- "setRealHdcpKeyPresent:"
- "setRemoteObjectInterface:"
- "setSecurityDomain:"
- "setSecurityMode:"
- "setSerialNumber:"
- "setStagedFirmwareVersion:"
- "setSupportsChargingChimeDebounce:"
- "setSupportsHeySiri:"
- "setSupportsJustSiri:"
- "setSupportsVoiceAssist:"
- "setTssResponse:"
- "setWithArray:"
- "setWithObjects:"
- "solicitDynamicAsset:deviceEndpoint:assetTag:"
- "stageAndApplyFirmwareAsset:deviceEndpoint:tssServerURL:"
- "stageFirmwareAsset:deviceEndpoint:"
- "stageFirmwareAsset:deviceEndpoint:tssServerURL:"
- "stagedFirmwareVersion"
- "stagedFirmwareVersion:endpointIndex:"
- "stagedFirmwareVersion:endpointIndex:componentIndex:"
- "stagedFirmwareVersion:endpointNumber:componentNumber:"
- "stringByAppendingPathComponent:"
- "stringByDeletingLastPathComponent"
- "stringWithFormat:"
- "supportsChargingChimeDebounce"
- "supportsHeySiri"
- "supportsJustSiri"
- "supportsSecureCoding"
- "suspend"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "tagString"
- "tapToRadarAssetsURL"
- "tapToRadarClearBaseURL:"
- "tapToRadarStart:"
- "tapToRadarStart:error:"
- "tapToRadarStart:reply:"
- "tapToRadarStop:"
- "tssRequestForPersonalizeFirmware:deviceEndpoint:"
- "tssRequestsForPersonalizeFirmware:deviceEndpoint:"
- "tssResponseForPersonalizeFirmware:deviceEndpoint:"
- "tssResponsesForPersonalizeFirmware:deviceEndpoint:"
- "uarpDeviceManagerAppliedStagedAssets:deviceEndpoint:layer3Flags:"
- "uarpDeviceManagerAssetMetaDataComplete:deviceEndpoint:deviceAsset:assetTag:"
- "uarpDeviceManagerAssetOffered:deviceEndpoint:deviceAsset:assetTag:"
- "uarpDeviceManagerAssetPayloadReady:deviceEndpoint:deviceAsset:payloadTag:payloadIndex:"
- "uarpDeviceManagerAssetTransferProgress:deviceEndpoint:deviceAsset:bytesTransferred:totalBytes:"
- "uarpDeviceManagerAssetTransferStatus:deviceEndpoint:deviceAsset:transferStatus:"
- "uarpDeviceManagerConnectionInterrupted:"
- "uarpDeviceManagerConnectionInvalidated:"
- "uarpDeviceManagerEndpointReachable:deviceEndpoint:"
- "uarpDeviceManagerEndpointUnreachable:deviceEndpoint:"
- "uarpDeviceManagerPayloadData:deviceEndpoint:deviceAsset:payloadTag:payloadIndex:payloadOffset:dataLength:"
- "uarpDeviceManagerPayloadDataComplete:deviceEndpoint:deviceAsset:payloadTag:payloadIndex:"
- "uarpDeviceManagerPayloadMetaDataComplete:deviceEndpoint:deviceAsset:payloadTag:payloadIndex:"
- "uarpDeviceManagerPersonalizationStatus:deviceEndpoint:deviceAsset:status:"
- "uarpDeviceManagerRescindedAssets:deviceEndpoint:"
- "uarpDeviceManagerRxDynamicAssetTransferProgress:deviceEndpoint:deviceAsset:deviceAssetTag:bytesTransferred:totalBytes:"
- "uarpDeviceManagerRxDynamicAssetTransferStatus:deviceEndpoint:deviceAsset:deviceAssetTag:transferStatus:"
- "uarpDeviceManagerTxDynamicAssetTransferProgress:deviceEndpoint:deviceAsset:deviceAssetTag:bytesTransferred:totalBytes:"
- "uarpDeviceManagerTxDynamicAssetTransferStatus:deviceEndpoint:deviceAsset:deviceAssetTag:transferStatus:"
- "unarchivedObjectOfClasses:fromData:error:"
- "unsignedIntegerValue"
- "url"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSUUID\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSData\">16"
- "v24@0:8q16"
- "v32@0:8@\"NSUUID\"16@\"NSData\"24"
- "v32@0:8@\"NSUUID\"16@\"NSNumber\"24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSNumber\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?B>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSURL\"16@\"NSUUID\"24@\"NSUUID\"32"
- "v40@0:8@\"NSUUID\"16@\"NSNumber\"24@?<v@?@\"NSNumber\">32"
- "v40@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSNumber\"32"
- "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSString\"32"
- "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?B>32"
- "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?BQ>32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSURL\"16@\"NSUUID\"24@\"NSUUID\"32@\"NSURL\"40"
- "v48@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?@\"NSData\">40"
- "v48@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?@\"NSNumber\">40"
- "v48@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?@\"NSString\">40"
- "v48@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40"
- "v48@0:8@\"NSUUID\"16@\"NSString\"24@\"NSURL\"32@\"NSUUID\"40"
- "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSData\"32@?<v@?B>40"
- "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSData\"32@?<v@?B@\"NSURL\">40"
- "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSNumber\"32@\"NSNumber\"40"
- "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSString\"32@\"NSNumber\"40"
- "v48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSURL\"32@?<v@?@\"NSNumber\">40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@\"NSURL\"16@\"NSUUID\"24@\"NSUUID\"32@\"NSDictionary\"40@\"NSURL\"48"
- "v56@0:8@\"NSUUID\"16@\"NSString\"24@\"NSURL\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSString\"32@\"NSNumber\"40@\"NSNumber\"48"
- "v56@0:8@\"NSUUID\"16@\"NSUUID\"24{_NSRange=QQ}32@?<v@?B@\"NSData\">48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24{_NSRange=QQ}32@?48"
- "v64@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSString\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56"
- "v64@0:8@16@24@32@40@48@56"
- "versionString"
- "writeData:error:"

```
