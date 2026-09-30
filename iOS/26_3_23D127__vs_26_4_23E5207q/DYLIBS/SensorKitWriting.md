## SensorKitWriting

> `/System/Library/PrivateFrameworks/SensorKitWriting.framework/SensorKitWriting`

```diff

-958.0.13.0.0
-  __TEXT.__text: 0xec68
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0xfa4
-  __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x126e
-  __TEXT.__gcc_except_tab: 0x608
-  __TEXT.__oslogstring: 0x2092
-  __TEXT.__unwind_info: 0x4e0
-  __TEXT.__objc_classname: 0x323
-  __TEXT.__objc_methname: 0x301d
-  __TEXT.__objc_methtype: 0x8b6
-  __TEXT.__objc_stubs: 0x1ec0
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x528
-  __DATA_CONST.__objc_classlist: 0x80
+972.0.17.0.0
+  __TEXT.__text: 0xfb30
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x110c
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x1377
+  __TEXT.__gcc_except_tab: 0x644
+  __TEXT.__oslogstring: 0x2222
+  __TEXT.__unwind_info: 0x558
+  __TEXT.__objc_classname: 0x354
+  __TEXT.__objc_methname: 0x33e9
+  __TEXT.__objc_methtype: 0x93a
+  __TEXT.__objc_stubs: 0x2160
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__const: 0x540
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa60
+  __DATA_CONST.__objc_selrefs: 0xb30
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x1060
-  __AUTH_CONST.__objc_const: 0x2168
+  __AUTH_CONST.__cfstring: 0x11c0
+  __AUTH_CONST.__objc_const: 0x23f0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x1ec
-  __DATA.__data: 0x5a8
-  __DATA.__bss: 0x90
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x20c
+  __DATA.__data: 0x6c8
+  __DATA.__bss: 0x98
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 545C2DE1-C6E5-378C-8023-30F01CCDFCB1
-  Functions: 326
-  Symbols:   1494
-  CStrings:  1078
+  UUID: 95497A82-031C-3E2E-9ABE-0AB77F224C5E
+  Functions: 353
+  Symbols:   1612
+  CStrings:  1159
 
Symbols:
+ +[SRSourceDevice initialize]
+ +[SRSourceDevice supportsSecureCoding]
+ -[SRAuthorizationClient initialAuthorizationNeededForBundleId:]
+ -[SRAuthorizationClient resetInitialAuthorizationCompleted]
+ -[SRAuthorizationClient setInitialAuthorizationCompleteForBundleId:]
+ -[SRAuthorizationClient updateInitialAuthorizationStateIfNeededForBundleId:]
+ -[SRAuthorizationClient updatePrerequisites]
+ -[SRSensorWriter setSourceDevice:error:]
+ -[SRSourceDevice copyWithZone:]
+ -[SRSourceDevice dealloc]
+ -[SRSourceDevice description]
+ -[SRSourceDevice dictionaryRepresentation]
+ -[SRSourceDevice encodeWithCoder:]
+ -[SRSourceDevice encryptedIdentifier]
+ -[SRSourceDevice ephemeralIdentifier]
+ -[SRSourceDevice firmwareVersion]
+ -[SRSourceDevice hardwareVersion]
+ -[SRSourceDevice hash]
+ -[SRSourceDevice initWithCoder:]
+ -[SRSourceDevice initWithEncryptedIdentifier:ephemeralIdentifier:manufacturer:model:hardwareVersion:firmwareVersion:]
+ -[SRSourceDevice initWithIdentifier:manufacturer:model:hardwareVersion:firmwareVersion:]
+ -[SRSourceDevice isEqual:]
+ -[SRSourceDevice localIdentifier]
+ -[SRSourceDevice manufacturer]
+ -[SRSourceDevice model]
+ -[SRSourceDevice secureWithKey:error:]
+ -[SRSourceDevice setEncryptedIdentifier:]
+ -[SRSourceDevice setEphemeralIdentifier:]
+ -[SRSourceDevice sr_dictionaryRepresentation]
+ -[SRWritingStats setSegmentCreationTime:]
+ GCC_except_table10
+ GCC_except_table11
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table28
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table49
+ GCC_except_table60
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table79
+ _CCHmac
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_SRSourceDevice
+ _OBJC_IVAR_$_SRAuthorizationClient._initialAuthCompleteByBundleId
+ _OBJC_IVAR_$_SRAuthorizationClient._initialAuthLock
+ _OBJC_IVAR_$_SRDefaults._sourceHMACKey
+ _OBJC_IVAR_$_SRSourceDevice._encryptedIdentifier
+ _OBJC_IVAR_$_SRSourceDevice._ephemeralIdentifier
+ _OBJC_IVAR_$_SRSourceDevice._firmwareVersion
+ _OBJC_IVAR_$_SRSourceDevice._hardwareVersion
+ _OBJC_IVAR_$_SRSourceDevice._manufacturer
+ _OBJC_IVAR_$_SRSourceDevice._model
+ _OBJC_METACLASS_$_SRSourceDevice
+ _SRLogSourceDevice
+ _SRSensorHeadphoneMotion
+ _SensorInfoKeySourceHMACKey
+ __OBJC_$_CLASS_METHODS_SRSourceDevice
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_CLASS_PROP_LIST_SRSourceDevice
+ __OBJC_$_INSTANCE_METHODS_SRSourceDevice
+ __OBJC_$_INSTANCE_VARIABLES_SRSourceDevice
+ __OBJC_$_PROP_LIST_SRSourceDevice
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_SRSourceDevice
+ __OBJC_CLASS_RO_$_SRSourceDevice
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_SRSourceDevice
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ ___32-[SRSensorWriter setMonitoring:]_block_invoke.132
+ ___33-[SRSensorWriter setupConnection]_block_invoke.63
+ ___34-[SRAuthorizationClient syncProxy]_block_invoke.35
+ ___35-[SRSensorWriter requestNewSegment]_block_invoke.73
+ ___35-[SRSensorWriter requestNewSegment]_block_invoke.74
+ ___45-[SRSensorWriter startUpdatingAuthorizations]_block_invoke.142
+ ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.143
+ ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.144
+ ___76-[SRAuthorizationClient updateInitialAuthorizationStateIfNeededForBundleId:]_block_invoke
+ ___block_descriptor_48_e8_32o40o_e59_v40?0"NSDictionary"8"NSDictionary"16"NSDictionary"24q32ls32l8s40l8
+ ___block_literal_global.37
+ ___block_literal_global.65
+ _kSRSourceDevice
+ _objc_msgSend$authorizedServicesForBundleId:
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dataWithData:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$encryptedIdentifier
+ _objc_msgSend$ephemeralIdentifier
+ _objc_msgSend$firmwareVersion
+ _objc_msgSend$hardwareVersion
+ _objc_msgSend$hash
+ _objc_msgSend$initialAuthorizationNeededForBundleId:
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$localIdentifier
+ _objc_msgSend$manufacturer
+ _objc_msgSend$model
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$setEncryptedIdentifier:
+ _objc_msgSend$setEphemeralIdentifier:
+ _objc_msgSend$setInitialAuthorizationCompleteForBundleId:
+ _objc_msgSend$setMetadata:
+ _objc_opt_isKindOfClass
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- -[SRAuthorizationClient authorizedServices]
- -[SRAuthorizationClient initialAuthNeeded]
- -[SRAuthorizationClient setInitialAuthNeeded:]
- -[SRAuthorizationClient updateInitialAuthorizationStateIfNeeded]
- GCC_except_table25
- GCC_except_table27
- GCC_except_table31
- GCC_except_table32
- GCC_except_table35
- GCC_except_table47
- GCC_except_table58
- GCC_except_table66
- GCC_except_table69
- GCC_except_table77
- _OBJC_IVAR_$_SRAuthorizationClient._initialAuthNeeded
- ___32-[SRSensorWriter setMonitoring:]_block_invoke.130
- ___33-[SRSensorWriter setupConnection]_block_invoke.62
- ___34-[SRAuthorizationClient syncProxy]_block_invoke.36
- ___35-[SRSensorWriter requestNewSegment]_block_invoke.71
- ___35-[SRSensorWriter requestNewSegment]_block_invoke.72
- ___45-[SRSensorWriter startUpdatingAuthorizations]_block_invoke.140
- ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.141
- ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.142
- ___64-[SRAuthorizationClient updateInitialAuthorizationStateIfNeeded]_block_invoke
- ___block_descriptor_40_e8_32o_e59_v40?0"NSDictionary"8"NSDictionary"16"NSDictionary"24q32ls32l8
- ___block_literal_global.38
- ___block_literal_global.64
- _objc_msgSend$initialAuthNeeded
- _objc_msgSend$setInitialAuthNeeded:
CStrings:
+ "%@ (%p): localIdentifier:%@, manufacturer:%@, model:%@, hardwareVersion:%@, firmwareVersion:%@"
+ "(null)"
+ "@\"NSData\""
+ "@\"NSMutableSet\""
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8^{_NSZone=}16"
+ "Missing encrypted identifier."
+ "Missing key to secure identifier with."
+ "NSCoding"
+ "NSCopying"
+ "NSSecureCoding"
+ "Requesting local identifier before identifier has been secured."
+ "SRLogSourceDevice"
+ "SRSourceDevice"
+ "Set source to %{private}@"
+ "Source Device identifier not yet encrypted."
+ "Source object should not have both an encrypted identifier and nonencrypted identifier."
+ "SourceHMACKey"
+ "T@\"NSData\",&,N,V_encryptedIdentifier"
+ "T@\"NSString\",&,N,V_ephemeralIdentifier"
+ "T@\"NSString\",R,C,N"
+ "T@\"NSString\",R,C,N,V_firmwareVersion"
+ "T@\"NSString\",R,C,N,V_hardwareVersion"
+ "T@\"NSString\",R,C,N,V_manufacturer"
+ "T@\"NSString\",R,C,N,V_model"
+ "Td,N,V_segmentCreationTime"
+ "Unable to secure source identifier because %{public}@. Not calling setMetadata because source is not secure."
+ "_encryptedIdentifier"
+ "_ephemeralIdentifier"
+ "_firmwareVersion"
+ "_hardwareVersion"
+ "_initialAuthCompleteByBundleId"
+ "_initialAuthLock"
+ "_manufacturer"
+ "_model"
+ "_sourceHMACKey"
+ "authorizedServicesForBundleId:"
+ "base64EncodedStringWithOptions:"
+ "com.apple.SensorKit.motion.headphone"
+ "copyWithZone:"
+ "dataUsingEncoding:"
+ "dataWithData:"
+ "dataWithLength:"
+ "decodeObjectOfClass:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "encryptedIdentifier"
+ "ephemeralIdentifier"
+ "firmwareVersion"
+ "hardwareVersion"
+ "initWithCoder:"
+ "initWithIdentifier:manufacturer:model:hardwareVersion:firmwareVersion:"
+ "initialAuthorizationNeededForBundleId:"
+ "isEqualToData:"
+ "localIdentifier"
+ "manufacturer"
+ "model"
+ "mutableBytes"
+ "removeAllObjects"
+ "segmentCreationTime"
+ "setEncryptedIdentifier:"
+ "setEphemeralIdentifier:"
+ "setInitialAuthorizationCompleteForBundleId:"
+ "setSegmentCreationTime:"
+ "setSourceDevice:error:"
+ "source"
+ "sr_dictionaryRepresentation"
+ "supportsSecureCoding"
+ "v24@0:8@\"NSCoder\"16"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "T@\"NSDictionary\",R,C"
- "TB,V_initialAuthNeeded"
- "_initialAuthNeeded"
- "authorizedServices"
- "initialAuthNeeded"
- "setInitialAuthNeeded:"

```
