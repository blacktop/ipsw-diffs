## DigitalAccess

> `/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess`

```diff

-63.2.1.0.0
-  __TEXT.__text: 0x330fc
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x2514
-  __TEXT.__const: 0x6a8
-  __TEXT.__cstring: 0x6e71
-  __TEXT.__oslogstring: 0x1f02
-  __TEXT.__gcc_except_tab: 0x1180
-  __TEXT.__unwind_info: 0xbf8
-  __TEXT.__objc_classname: 0x4f4
-  __TEXT.__objc_methname: 0x66ad
-  __TEXT.__objc_methtype: 0x1a1a
-  __TEXT.__objc_stubs: 0x29a0
-  __DATA_CONST.__got: 0x218
+64.20.2.0.0
+  __TEXT.__text: 0x36064
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x25f4
+  __TEXT.__const: 0x680
+  __TEXT.__cstring: 0x70b5
+  __TEXT.__oslogstring: 0x20da
+  __TEXT.__gcc_except_tab: 0x1248
+  __TEXT.__unwind_info: 0xcd0
+  __TEXT.__objc_classname: 0x50a
+  __TEXT.__objc_methname: 0x688f
+  __TEXT.__objc_methtype: 0x19fb
+  __TEXT.__objc_stubs: 0x2a40
+  __DATA_CONST.__got: 0x220
   __DATA_CONST.__const: 0xf90
-  __DATA_CONST.__objc_classlist: 0x120
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12d8
+  __DATA_CONST.__objc_selrefs: 0x1328
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x338
-  __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1be0
-  __AUTH_CONST.__objc_const: 0x41a8
+  __AUTH_CONST.__auth_got: 0x2f0
+  __AUTH_CONST.__const: 0x2a0
+  __AUTH_CONST.__cfstring: 0x1f20
+  __AUTH_CONST.__objc_const: 0x43f0
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x2d8
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x2f8
   __DATA.__data: 0x600
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/SESShared.framework/SESShared
   - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /usr/lib/libMobileGestalt.dylib
-  - /usr/lib/libSESShared.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8CE8D907-DCF2-34C0-B0DB-0663D910DB9A
-  Functions: 915
-  Symbols:   3018
-  CStrings:  2171
+  UUID: 0771A01D-5662-3510-9D66-BFE6C5813007
+  Functions: 956
+  Symbols:   3130
+  CStrings:  2258
 
Symbols:
+ +[DAKeyPairingConfig supportsSecureCoding]
+ -[DAKeyPairingConfig .cxx_destruct]
+ -[DAKeyPairingConfig additionalParameters]
+ -[DAKeyPairingConfig bindingAttestation]
+ -[DAKeyPairingConfig btAddress]
+ -[DAKeyPairingConfig btIRK]
+ -[DAKeyPairingConfig copyWithZone:]
+ -[DAKeyPairingConfig description]
+ -[DAKeyPairingConfig displayName]
+ -[DAKeyPairingConfig encodeWithCoder:]
+ -[DAKeyPairingConfig initWithCoder:]
+ -[DAKeyPairingConfig initWithPassword:displayName:transport:bindingAttestation:ppid:btAddress:btIRK:additionalParameters:]
+ -[DAKeyPairingConfig password]
+ -[DAKeyPairingConfig ppid]
+ -[DAKeyPairingConfig transport]
+ -[DAKeyPairingSession startKeyPairingWithConfig:]
+ -[DAKeyPairingSession startKeyPairingWithConfig:].cold.1
+ -[DASharingAnalyticsUpdateConfig description]
+ -[KmlDeviceConfigurationData constructOemSpecificContentTupleForName:ppid:]
+ -[KmlDeviceConfigurationData parseOemSpecificContent:ppidOverride:]
+ -[KmlDeviceConfigurationData updatePPIDWithConfigValue:]
+ -[KmlDeviceConfigurationData updatePPIDWithServerProvidedData:].cold.1
+ -[KmlSettingsManager simulateCrossPlatformSharingInitiator]
+ GCC_except_table103
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table71
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table80
+ GCC_except_table83
+ GCC_except_table86
+ GCC_except_table89
+ GCC_except_table92
+ GCC_except_table95
+ _OBJC_CLASS_$_DAKeyPairingConfig
+ _OBJC_IVAR_$_DAKeyPairingConfig._additionalParameters
+ _OBJC_IVAR_$_DAKeyPairingConfig._bindingAttestation
+ _OBJC_IVAR_$_DAKeyPairingConfig._btAddress
+ _OBJC_IVAR_$_DAKeyPairingConfig._btIRK
+ _OBJC_IVAR_$_DAKeyPairingConfig._displayName
+ _OBJC_IVAR_$_DAKeyPairingConfig._password
+ _OBJC_IVAR_$_DAKeyPairingConfig._ppid
+ _OBJC_IVAR_$_DAKeyPairingConfig._transport
+ _OBJC_IVAR_$_KmlSettingsManager._stockholmUserDefaults
+ _OBJC_METACLASS_$_DAKeyPairingConfig
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ __OBJC_$_CLASS_METHODS_DAKeyPairingConfig
+ __OBJC_$_CLASS_PROP_LIST_DAKeyPairingConfig
+ __OBJC_$_INSTANCE_METHODS_DAKeyPairingConfig
+ __OBJC_$_INSTANCE_VARIABLES_DAKeyPairingConfig
+ __OBJC_$_PROP_LIST_DAKeyPairingConfig
+ __OBJC_CLASS_PROTOCOLS_$_DAKeyPairingConfig
+ __OBJC_CLASS_RO_$_DAKeyPairingConfig
+ __OBJC_METACLASS_RO_$_DAKeyPairingConfig
+ ___35-[DAKeyPairingSession startProbing]_block_invoke.129
+ ___46-[DAKeyPairingSession preWarmForManufacturer:]_block_invoke.126
+ ___49-[DAKeyPairingSession startKeyPairingWithConfig:]_block_invoke
+ ___49-[DAKeyPairingSession startKeyPairingWithConfig:]_block_invoke.127
+ ___78-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.134
+ ___block_literal_global.358
+ ___block_literal_global.426
+ ___kmlUtilIsVirtualDevice_block_invoke
+ _decodeWithData:error:.allowedClasses.356
+ _decodeWithData:error:.allowedClasses.424
+ _decodeWithData:error:.pred.355
+ _decodeWithData:error:.pred.423
+ _kmlUtilIsVirtualDevice
+ _kmlUtilIsVirtualDevice.bVal
+ _kmlUtilIsVirtualDevice.cold.1
+ _kmlUtilIsVirtualDevice.onceToken
+ _objc_msgSend$initWithPassword:displayName:transport:bindingAttestation:ppid:btAddress:btIRK:additionalParameters:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$password
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$startKeyPairingWithConfig:
+ _objc_msgSend$startKeyPairingWithConfig:callback:
+ _objc_msgSend$transport
+ _objc_retainAutoreleasedReturnValue
- -[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:bindingAttestation:].cold.1
- -[DAKeySharingConfiguration setSharingFlow:]
- -[DAKeySharingConfiguration sharingFlow]
- -[DAKeySharingSession acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler:]
- -[KmlDeviceConfigurationData parseOemSpecificContent:]
- GCC_except_table104
- GCC_except_table14
- GCC_except_table20
- GCC_except_table29
- GCC_except_table32
- GCC_except_table51
- GCC_except_table54
- GCC_except_table57
- GCC_except_table60
- GCC_except_table66
- GCC_except_table72
- GCC_except_table75
- GCC_except_table78
- GCC_except_table81
- GCC_except_table84
- GCC_except_table87
- GCC_except_table9
- GCC_except_table90
- GCC_except_table93
- GCC_except_table96
- _OBJC_IVAR_$_DAKeySharingConfiguration._sharingFlow
- ___35-[DAKeyPairingSession startProbing]_block_invoke.16
- ___46-[DAKeyPairingSession preWarmForManufacturer:]_block_invoke.13
- ___78-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke.21
- ___92-[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:bindingAttestation:]_block_invoke
- ___92-[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:bindingAttestation:]_block_invoke.14
- ___block_literal_global.363
- ___block_literal_global.431
- _decodeWithData:error:.allowedClasses.361
- _decodeWithData:error:.allowedClasses.429
- _decodeWithData:error:.pred.360
- _decodeWithData:error:.pred.428
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$acceptInvitationWithIdentifier:passcode:completionHandler:
- _objc_msgSend$startKeyPairingWithPassword:keyName:transport:bindingAttestation:callback:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x8
CStrings:
+ "\t%@"
+ "\tInvitation Identifiers        : %@\n"
+ "\tKey Identifier                : %@\n"
+ "\tRecipient Flow                : %@\n"
+ "%s : %i : Failed to find applicable product plan data"
+ "%s : %i : Finished rebuilding personalization content to be saved"
+ "%s : %i : Missing OP config"
+ "%s : %i : Not updating ppid with nil or empty value"
+ "%s : %i : Overriding Default PPID to %{private}@"
+ "%s : %i : Overriding PPID to %@"
+ "%s : %i : Overriding ppid to %{private}@"
+ "%s : %i : Somehow we have ppid but no personalization tlv. Update with new value"
+ "%s : %i : This API is deprecated, use startKeyPairingWithConfig: instead"
+ "%s : %i : We already have ppid, need to overwrite our value in device config"
+ "%s : %i : We already have ppid. Ignore the server provided value"
+ "%s : %i : We haven't received ppid yet, save it"
+ "(null)"
+ "-[DAKeyPairingSession startKeyPairingWithConfig:]"
+ "-[DAKeyPairingSession startKeyPairingWithConfig:]_block_invoke"
+ "-[KmlDeviceConfigurationData parseOemSpecificContent:ppidOverride:]"
+ "-[KmlDeviceConfigurationData updatePPIDWithConfigValue:]"
+ "@80@0:8@16@24q32@40@48@56@64@72"
+ "Additional Parameters       : %@\n"
+ "BT Address                  : %@\n"
+ "BT IRK Length               : %lu\n"
+ "DAKeyPairingConfig"
+ "DASharingAnalyticsUpdateConfig:\n"
+ "Display Name                : %@\n"
+ "Existing personalization info"
+ "IsVirtualDevice"
+ "NO"
+ "New personalization content"
+ "PKSharingSimulateCrossPlatformShareKey"
+ "PPID Length                 : %lu\n"
+ "Password Length             : %lu\n"
+ "T@\"NSData\",R,N,V_bindingAttestation"
+ "T@\"NSDictionary\",R,N,V_additionalParameters"
+ "T@\"NSString\",R,N,V_btAddress"
+ "T@\"NSString\",R,N,V_btIRK"
+ "T@\"NSString\",R,N,V_displayName"
+ "T@\"NSString\",R,N,V_password"
+ "T@\"NSString\",R,N,V_ppid"
+ "Tq,R,N,V_transport"
+ "Transport                   : %@\n"
+ "Vv32@0:8@\"DAKeyPairingConfig\"16@?<v@?@\"NSError\">24"
+ "YES"
+ "_additionalParameters"
+ "_btAddress"
+ "_btIRK"
+ "_password"
+ "_ppid"
+ "_stockholmUserDefaults"
+ "_transport"
+ "additionalParameters"
+ "btAddress"
+ "btIRK"
+ "com.apple.stockholm"
+ "initWithPassword:displayName:transport:bindingAttestation:ppid:btAddress:btIRK:additionalParameters:"
+ "objectAtIndexedSubscript:"
+ "password"
+ "ppid"
+ "removeObjectAtIndex:"
+ "simulateCrossPlatformSharingInitiator"
+ "startKeyPairingWithConfig:"
+ "startKeyPairingWithConfig:callback:"
+ "transport"
+ "updatePPIDWithConfigValue:"
- "%s : %i : This API is deprecated, use startKeyPairingWithPassword:displayName:transport:bindingAttestation: instead"
- "%s : %i : We already have car provided ppid. Ignore the server provided value"
- "-[DAKeyPairingSession startKeyPairingWithPassword:displayName:transport:bindingAttestation:]_block_invoke"
- "-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler:]"
- "-[KmlDeviceConfigurationData parseOemSpecificContent:]"
- "Tq,N,V_sharingFlow"
- "Vv56@0:8@\"NSString\"16@\"NSString\"24q32@\"NSData\"40@?<v@?@\"NSError\">48"
- "Vv56@0:8@16@24q32@40@?48"
- "acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler:"
- "setSharingFlow:"
- "startKeyPairingWithPassword:keyName:transport:bindingAttestation:callback:"
- "v48@0:8@16@24q32@?40"

```
