## UARPKit

> `/System/Library/PrivateFrameworks/UARPKit.framework/Versions/A/UARPKit`

```diff

-1587.1.3.0.0
-  __TEXT.__text: 0x15a1c
-  __TEXT.__objc_methlist: 0x15a0
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x1e26
+1587.40.26.0.0
+  __TEXT.__text: 0x16f70
+  __TEXT.__objc_methlist: 0x1690
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x1eb3
   __TEXT.__gcc_except_tab: 0x3bc
-  __TEXT.__oslogstring: 0x8a3
-  __TEXT.__unwind_info: 0x708
+  __TEXT.__oslogstring: 0x86f
+  __TEXT.__unwind_info: 0x720
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x110
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc0
+  __DATA_CONST.__objc_selrefs: 0xe50
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__got: 0xe8
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0xbc0
-  __AUTH_CONST.__objc_const: 0x1f80
+  __AUTH_CONST.__cfstring: 0xba0
+  __AUTH_CONST.__objc_const: 0x2270
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1a0
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 553
-  Symbols:   1051
-  CStrings:  253
+  Functions: 570
+  Symbols:   1092
+  CStrings:  251
 
Symbols:
+ +[UARPDeviceProperties supportsSecureCoding]
+ -[NSUUID(UARP) isMatchingUUID:]
+ -[UARPDevice hostEndpointDelegateInactivityTimeout:]
+ -[UARPDevice hostEndpointDelegateNoFirmwareUpdateAvailable:]
+ -[UARPDevice initWithUUID:delegate:delegateQueue:deviceProperties:]
+ -[UARPDevice noSleepWhileStaging]
+ -[UARPDevice transportForStagingOnly]
+ -[UARPDevice(Deprecated) configureDeviceInactivityTimeout:error:]
+ -[UARPDevice(Deprecated) configureDevicePacketMaximumRetries:error:]
+ -[UARPDevice(Deprecated) configureDevicePacketRetryTimeout:error:]
+ -[UARPDevice(Deprecated) configureDeviceSupportsCharging:]
+ -[UARPDevice(Deprecated) configureDeviceSupportsSiri:]
+ -[UARPDevice(Deprecated) deviceAvailable:]
+ -[UARPDevice(Deprecated) deviceSupportsChargingChimeDebounce]
+ -[UARPDevice(Deprecated) deviceSupportsHeySiri]
+ -[UARPDevice(Deprecated) deviceSupportsJustSiri]
+ -[UARPDevice(Deprecated) deviceSupportsVoiceAssist]
+ -[UARPDevice(Deprecated) deviceTransportAvailable:]
+ -[UARPDevice(Deprecated) initWithUUID:delegate:delegateQueue:listener:]
+ -[UARPDevice(Deprecated) isMatchingUUID:]
+ -[UARPDevice(Deprecated) setDeviceAppleModelNumber:]
+ -[UARPDevice(Deprecated) setDeviceProductGroup:productNumber:]
+ -[UARPDevice(Deprecated) setDeviceSupportsCharging:]
+ -[UARPDevice(Deprecated) setDeviceSupportsSiri:]
+ -[UARPDevice(Private) releaseXPCConnection]
+ -[UARPDeviceManager endpointControllerDelegateEndpointInactive:]
+ -[UARPDeviceManager endpointControllerDelegateEndpointUnresponsive:]
+ -[UARPDeviceProperties .cxx_destruct]
+ -[UARPDeviceProperties appleModelNumber]
+ -[UARPDeviceProperties areNullableNumbersEqual:thatString:]
+ -[UARPDeviceProperties areNullableStringsEqual:thatString:]
+ -[UARPDeviceProperties assetIdentifier]
+ -[UARPDeviceProperties copyWithZone:]
+ -[UARPDeviceProperties description]
+ -[UARPDeviceProperties encodeWithCoder:]
+ -[UARPDeviceProperties hash]
+ -[UARPDeviceProperties initWithCoder:]
+ -[UARPDeviceProperties init]
+ -[UARPDeviceProperties isEqual:]
+ -[UARPDeviceProperties noSleepWhileStaging]
+ -[UARPDeviceProperties numPacketRetries]
+ -[UARPDeviceProperties productGroup]
+ -[UARPDeviceProperties productNumber]
+ -[UARPDeviceProperties setAppleModelNumber:]
+ -[UARPDeviceProperties setAssetIdentifier:]
+ -[UARPDeviceProperties setNoSleepWhileStaging:]
+ -[UARPDeviceProperties setNumPacketRetries:]
+ -[UARPDeviceProperties setProductGroup:]
+ -[UARPDeviceProperties setProductNumber:]
+ -[UARPDeviceProperties setSupportsCharging:]
+ -[UARPDeviceProperties setSupportsSiri:]
+ -[UARPDeviceProperties setTimeoutActivity:]
+ -[UARPDeviceProperties setTimeoutPacketRetry:]
+ -[UARPDeviceProperties setTransportDomain:]
+ -[UARPDeviceProperties setTransportForStagingOnly:]
+ -[UARPDeviceProperties supportsCharging]
+ -[UARPDeviceProperties supportsSiri]
+ -[UARPDeviceProperties timeoutActivity]
+ -[UARPDeviceProperties timeoutPacketRetry]
+ -[UARPDeviceProperties transportDomain]
+ -[UARPDeviceProperties transportForStagingOnly]
+ -[UARPHostEndpointProperties init]
+ GCC_except_table30
+ GCC_except_table56
+ OBJC_IVAR_$_UARPDevice._noSleepWhileStaging
+ OBJC_IVAR_$_UARPDevice._transportForStagingOnly
+ OBJC_IVAR_$_UARPDeviceProperties._appleModelNumber
+ OBJC_IVAR_$_UARPDeviceProperties._assetIdentifier
+ OBJC_IVAR_$_UARPDeviceProperties._noSleepWhileStaging
+ OBJC_IVAR_$_UARPDeviceProperties._numPacketRetries
+ OBJC_IVAR_$_UARPDeviceProperties._productGroup
+ OBJC_IVAR_$_UARPDeviceProperties._productNumber
+ OBJC_IVAR_$_UARPDeviceProperties._supportsCharging
+ OBJC_IVAR_$_UARPDeviceProperties._supportsSiri
+ OBJC_IVAR_$_UARPDeviceProperties._timeoutActivity
+ OBJC_IVAR_$_UARPDeviceProperties._timeoutPacketRetry
+ OBJC_IVAR_$_UARPDeviceProperties._transportDomain
+ OBJC_IVAR_$_UARPDeviceProperties._transportForStagingOnly
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_UARPDeviceProperties
+ _OBJC_METACLASS_$_UARPDeviceProperties
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUUID_$_UARP
+ __OBJC_$_CATEGORY_NSUUID_$_UARP
+ __OBJC_$_CLASS_METHODS_UARPDeviceProperties
+ __OBJC_$_CLASS_PROP_LIST_UARPDeviceProperties
+ __OBJC_$_INSTANCE_METHODS_UARPDevice(Private|TapToRadar|Deprecated)
+ __OBJC_$_INSTANCE_METHODS_UARPDeviceProperties
+ __OBJC_$_INSTANCE_VARIABLES_UARPDeviceProperties
+ __OBJC_$_PROP_LIST_UARPDeviceProperties
+ __OBJC_CLASS_PROTOCOLS_$_UARPDeviceProperties
+ __OBJC_CLASS_RO_$_UARPDeviceProperties
+ __OBJC_METACLASS_RO_$_UARPDeviceProperties
+ ___64-[UARPDeviceManager endpointControllerDelegateEndpointInactive:]_block_invoke
+ ___68-[UARPDeviceManager endpointControllerDelegateEndpointUnresponsive:]_block_invoke
+ _objc_msgSend$areNullableNumbersEqual:thatString:
+ _objc_msgSend$deviceAvailable
+ _objc_msgSend$deviceInactivityTimeout:
+ _objc_msgSend$deviceNoFirmwareUpdateAvailable:
+ _objc_msgSend$deviceTransportAvailable
+ _objc_msgSend$hostEndpointAvailable:endpointProperties:
+ _objc_msgSend$hostEndpointDelegateTransportNotNeeded:
+ _objc_msgSend$hostEndpointTransportAvailable:
+ _objc_msgSend$initWithUUID:delegate:delegateQueue:deviceProperties:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$noSleepWhileStaging
+ _objc_msgSend$numPacketRetries
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$setNoSleepWhileStaging:
+ _objc_msgSend$setNumPacketRetries:
+ _objc_msgSend$setTimeoutActivity:
+ _objc_msgSend$setTimeoutPacketRetry:
+ _objc_msgSend$setTransportForStagingOnly:
+ _objc_msgSend$timeoutActivity
+ _objc_msgSend$timeoutPacketRetry
+ _objc_msgSend$transportForStagingOnly
+ _objc_msgSend$uarpDeviceManagerEndpointInactive:deviceEndpoint:
+ _objc_msgSend$uarpDeviceManagerEndpointUnresponsive:deviceEndpoint:
+ _objc_msgSend$uarpDeviceManagerUnknownEndpoint:endpointUUID:
+ _objc_msgSend$unsignedLongValue
+ _objc_setProperty_atomic
- +[UARPHostEndpointProperties supportsSecureCoding]
- -[UARPDevice configureDeviceInactivityTimeout:error:]
- -[UARPDevice configureDevicePacketMaximumRetries:error:]
- -[UARPDevice configureDevicePacketRetryTimeout:error:]
- -[UARPDevice configureDeviceSupportsCharging:]
- -[UARPDevice configureDeviceSupportsSiri:]
- -[UARPDevice deviceAvailable:]
- -[UARPDevice deviceTransportAvailable:]
- -[UARPDevice initWithUUID:delegate:delegateQueue:listener:]
- -[UARPDevice isMatchingUUID:]
- -[UARPDevice releaseXPCConnection]
- -[UARPDevice setSupportsChargingChimeDebounce:]
- -[UARPDevice setSupportsHeySiri:]
- -[UARPDevice setSupportsJustSiri:]
- -[UARPDevice setSupportsVoiceAssist:]
- -[UARPDevice supportsChargingChimeDebounce]
- -[UARPDevice supportsHeySiri]
- -[UARPDevice supportsJustSiri]
- -[UARPDevice supportsVoiceAssist]
- -[UARPDevice(FeatureSupport) deviceSupportsChargingChimeDebounce]
- -[UARPDevice(FeatureSupport) deviceSupportsHeySiri]
- -[UARPDevice(FeatureSupport) deviceSupportsJustSiri]
- -[UARPDevice(FeatureSupport) deviceSupportsVoiceAssist]
- -[UARPDevice(FeatureSupport) setDeviceAppleModelNumber:]
- -[UARPDevice(FeatureSupport) setDeviceProductGroup:productNumber:]
- -[UARPDevice(FeatureSupport) setDeviceSupportsCharging:]
- -[UARPDevice(FeatureSupport) setDeviceSupportsSiri:]
- -[UARPDevice(FeatureSupport) setDeviceTransportDomain:]
- -[UARPHostEndpointProperties .cxx_destruct]
- -[UARPHostEndpointProperties appleModelNumber]
- -[UARPHostEndpointProperties areNullableStringsEqual:thatString:]
- -[UARPHostEndpointProperties assetIdentifier]
- -[UARPHostEndpointProperties copyWithZone:]
- -[UARPHostEndpointProperties description]
- -[UARPHostEndpointProperties encodeWithCoder:]
- -[UARPHostEndpointProperties hash]
- -[UARPHostEndpointProperties initWithCoder:]
- -[UARPHostEndpointProperties isEqual:]
- -[UARPHostEndpointProperties productGroup]
- -[UARPHostEndpointProperties productNumber]
- -[UARPHostEndpointProperties setAppleModelNumber:]
- -[UARPHostEndpointProperties setAssetIdentifier:]
- -[UARPHostEndpointProperties setProductGroup:]
- -[UARPHostEndpointProperties setProductNumber:]
- -[UARPHostEndpointProperties setSupportsCharging:]
- -[UARPHostEndpointProperties setSupportsSiri:]
- -[UARPHostEndpointProperties setTransportDomain:]
- -[UARPHostEndpointProperties supportsCharging]
- -[UARPHostEndpointProperties supportsSiri]
- -[UARPHostEndpointProperties transportDomain]
- GCC_except_table37
- GCC_except_table6
- OBJC_IVAR_$_UARPDevice._supportsChargingChimeDebounce
- OBJC_IVAR_$_UARPDevice._supportsHeySiri
- OBJC_IVAR_$_UARPDevice._supportsJustSiri
- OBJC_IVAR_$_UARPDevice._supportsVoiceAssist
- OBJC_IVAR_$_UARPHostEndpointProperties._appleModelNumber
- OBJC_IVAR_$_UARPHostEndpointProperties._assetIdentifier
- OBJC_IVAR_$_UARPHostEndpointProperties._productGroup
- OBJC_IVAR_$_UARPHostEndpointProperties._productNumber
- OBJC_IVAR_$_UARPHostEndpointProperties._supportsCharging
- OBJC_IVAR_$_UARPHostEndpointProperties._supportsSiri
- OBJC_IVAR_$_UARPHostEndpointProperties._transportDomain
- __OBJC_$_CLASS_METHODS_UARPHostEndpointProperties
- __OBJC_$_INSTANCE_METHODS_UARPDevice(Private|FeatureSupport|TapToRadar)
- __OBJC_$_PROP_LIST_UARPDevice
- _objc_msgSend$deviceAvailable:
- _objc_msgSend$deviceTransportAvailable:
- _objc_msgSend$hostEndpointAvailable:releasePolicy:endpointProperties:
- _objc_msgSend$hostEndpointTransportAvailable:releasePolicy:
- _objc_msgSend$inactivityTimer
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$packetRetries
- _objc_msgSend$packetRetryTimeout
- _objc_msgSend$setInactivityTimer:
- _objc_msgSend$setPacketRetries:
- _objc_msgSend$setPacketRetryTimeout:
- _objc_msgSend$setSupportsVoiceAssist:
- _objc_msgSend$supportsVoiceAssist
CStrings:
+ "%@ = %@,"
+ "%@ = YES,"
+ "-[UARPDevice hostEndpointDelegateInactivityTimeout:]"
+ "-[UARPDevice hostEndpointDelegateNoFirmwareUpdateAvailable:]"
+ "-[UARPDevice(Deprecated) deviceAvailable:]"
+ "-[UARPDeviceManager endpointControllerDelegateEndpointInactive:]"
+ "-[UARPDeviceManager endpointControllerDelegateEndpointInactive:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateEndpointUnresponsive:]"
+ "-[UARPDeviceManager endpointControllerDelegateEndpointUnresponsive:]_block_invoke"
+ "Apple Model Number"
+ "Asset Identifier"
+ "No Sleep While Staging"
+ "Num Packet Retries"
+ "Product Group"
+ "Product Number"
+ "Supports Charging"
+ "Supports Siri"
+ "Timeout Activity"
+ "Timeout Packet Retry"
+ "Transport Domain"
+ "Transport For Staging Only"
- "%s: device not available, cannot plumb transport %@"
- ", "
- "-[UARPDevice deviceAvailable:]"
- "-[UARPDevice deviceTransportAvailable:]"
- "-[UARPDevice(FeatureSupport) deviceSupportsChargingChimeDebounce]"
- "-[UARPDevice(FeatureSupport) deviceSupportsHeySiri]"
- "-[UARPDevice(FeatureSupport) deviceSupportsJustSiri]"
- "-[UARPDevice(FeatureSupport) deviceSupportsVoiceAssist]"
- "Inactivity Timer = %lu"
- "Packet Retries  = %lu"
- "Packet Retry Timeout = %lu"
- "Q"
- "appleModelNumber"
- "assetIdentifier"
- "inactivityTimer"
- "packetRetries"
- "packetRetryTimeout"
- "productGroup"
- "productNumber"
- "supportsCharging"
- "supportsSiri"
- "supportsVoiceAssist"
- "transportDomain"
```
