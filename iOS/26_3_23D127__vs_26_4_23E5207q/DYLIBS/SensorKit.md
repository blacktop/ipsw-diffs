## SensorKit

> `/System/Library/Frameworks/SensorKit.framework/SensorKit`

```diff

-958.0.13.0.0
-  __TEXT.__text: 0x3ae28
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x51a4
+972.0.17.0.0
+  __TEXT.__text: 0x3bf04
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_methlist: 0x52cc
   __TEXT.__dlopen_cstrs: 0x95
   __TEXT.__const: 0x168
   __TEXT.__constg_swiftt: 0x68

   __TEXT.__swift5_reflstr: 0x46
   __TEXT.__swift5_fieldmd: 0x40
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x4998
-  __TEXT.__cstring: 0x576e
-  __TEXT.__gcc_except_tab: 0x9a0
-  __TEXT.__unwind_info: 0x1138
-  __TEXT.__objc_classname: 0xb56
-  __TEXT.__objc_methname: 0x9777
-  __TEXT.__objc_methtype: 0x1c08
-  __TEXT.__objc_stubs: 0x6ba0
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x11f8
-  __DATA_CONST.__objc_classlist: 0x280
+  __TEXT.__oslogstring: 0x4b85
+  __TEXT.__cstring: 0x5881
+  __TEXT.__gcc_except_tab: 0x9dc
+  __TEXT.__unwind_info: 0x11b8
+  __TEXT.__objc_classname: 0xb65
+  __TEXT.__objc_methname: 0x9aa6
+  __TEXT.__objc_methtype: 0x1c35
+  __TEXT.__objc_stubs: 0x6d80
+  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__const: 0x1210
+  __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2070
+  __DATA_CONST.__objc_selrefs: 0x2100
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x230
+  __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x5e0
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__const: 0x2e8
-  __AUTH_CONST.__cfstring: 0x58c0
-  __AUTH_CONST.__objc_const: 0x9d30
+  __AUTH_CONST.__cfstring: 0x5a20
+  __AUTH_CONST.__objc_const: 0x9f68
   __AUTH_CONST.__objc_arrayobj: 0x5e8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0x5dc
+  __AUTH.__objc_data: 0x15e0
+  __DATA.__objc_ivar: 0x5fc
   __DATA.__data: 0xf20
-  __DATA.__bss: 0x148
+  __DATA.__bss: 0x150
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_ivar: 0xc
   __DATA_DIRTY.__objc_data: 0x370

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 66FBBAE3-BF92-39C7-96E7-49CA11EB7627
-  Functions: 1694
-  Symbols:   6181
-  CStrings:  3762
+  UUID: 2B68DED0-302D-356F-966E-D3A84CA506CC
+  Functions: 1723
+  Symbols:   6277
+  CStrings:  3827
 
Symbols:
+ +[SRSourceDevice initialize]
+ +[SRSourceDevice supportsSecureCoding]
+ -[SRAuthorizationClient initialAuthorizationNeededForBundleId:]
+ -[SRAuthorizationClient resetInitialAuthorizationCompleted]
+ -[SRAuthorizationClient setInitialAuthorizationCompleteForBundleId:]
+ -[SRAuthorizationClient updateInitialAuthorizationStateIfNeededForBundleId:]
+ -[SRAuthorizationClient updatePrerequisites]
+ -[SRFetchResult sourceDevice]
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
+ -[SRSourceDevice initWithSourceDeviceFromDictionary:]
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
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table28
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table49
+ GCC_except_table60
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table79
+ _CCHmac
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
+ __OBJC_$_CLASS_PROP_LIST_SRSourceDevice
+ __OBJC_$_INSTANCE_METHODS_SRSourceDevice
+ __OBJC_$_INSTANCE_VARIABLES_SRSourceDevice
+ __OBJC_$_PROP_LIST_SRSourceDevice
+ __OBJC_CLASS_PROTOCOLS_$_SRSourceDevice
+ __OBJC_CLASS_RO_$_SRSourceDevice
+ __OBJC_METACLASS_RO_$_SRSourceDevice
+ ___32-[SRSensorWriter setMonitoring:]_block_invoke.139
+ ___33-[SRSensorWriter setupConnection]_block_invoke.70
+ ___34-[SRAuthorizationClient syncProxy]_block_invoke.35
+ ___35-[SRSensorWriter requestNewSegment]_block_invoke.80
+ ___35-[SRSensorWriter requestNewSegment]_block_invoke.81
+ ___43-[SRReaderSensorKitBackend setupConnection]_block_invoke.53
+ ___45-[SRSensorWriter startUpdatingAuthorizations]_block_invoke.149
+ ___47-[SRReaderSensorKitBackend fetch:withCallback:]_block_invoke.59
+ ___47-[SRReaderSensorKitBackend fetch:withCallback:]_block_invoke.61
+ ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.150
+ ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.151
+ ___76-[SRAuthorizationClient updateInitialAuthorizationStateIfNeededForBundleId:]_block_invoke
+ ___block_descriptor_48_e8_32o40o_e59_v40?0"NSDictionary"8"NSDictionary"16"NSDictionary"24q32ls32l8s40l8
+ ___block_literal_global.37
+ ___block_literal_global.72
+ _kSRSourceDevice
+ _objc_msgSend$authorizedServicesForBundleId:
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dataWithData:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$encryptedIdentifier
+ _objc_msgSend$ephemeralIdentifier
+ _objc_msgSend$firmwareVersion
+ _objc_msgSend$hardwareVersion
+ _objc_msgSend$initialAuthorizationNeededForBundleId:
+ _objc_msgSend$localIdentifier
+ _objc_msgSend$manufacturer
+ _objc_msgSend$metadata
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$setEncryptedIdentifier:
+ _objc_msgSend$setEphemeralIdentifier:
+ _objc_msgSend$setInitialAuthorizationCompleteForBundleId:
- -[SRAuthorizationClient authorizedServices]
- -[SRAuthorizationClient initialAuthNeeded]
- -[SRAuthorizationClient setInitialAuthNeeded:]
- -[SRAuthorizationClient updateInitialAuthorizationStateIfNeeded]
- GCC_except_table32
- GCC_except_table47
- GCC_except_table58
- GCC_except_table66
- GCC_except_table69
- GCC_except_table77
- _.str.6
- _OBJC_IVAR_$_SRAuthorizationClient._initialAuthNeeded
- ___32-[SRSensorWriter setMonitoring:]_block_invoke.137
- ___33-[SRSensorWriter setupConnection]_block_invoke.69
- ___34-[SRAuthorizationClient syncProxy]_block_invoke.36
- ___35-[SRSensorWriter requestNewSegment]_block_invoke.78
- ___35-[SRSensorWriter requestNewSegment]_block_invoke.79
- ___43-[SRReaderSensorKitBackend setupConnection]_block_invoke.52
- ___45-[SRSensorWriter startUpdatingAuthorizations]_block_invoke.147
- ___47-[SRReaderSensorKitBackend fetch:withCallback:]_block_invoke.58
- ___47-[SRReaderSensorKitBackend fetch:withCallback:]_block_invoke.60
- ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.148
- ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.149
- ___64-[SRAuthorizationClient updateInitialAuthorizationStateIfNeeded]_block_invoke
- ___block_descriptor_40_e8_32o_e59_v40?0"NSDictionary"8"NSDictionary"16"NSDictionary"24q32ls32l8
- ___block_literal_global.38
- ___block_literal_global.71
- _nan
- _objc_msgSend$authorizedServices
- _objc_msgSend$initialAuthNeeded
- _objc_msgSend$setInitialAuthNeeded:
CStrings:
+ "%@ (%p): localIdentifier:%@, manufacturer:%@, model:%@, hardwareVersion:%@, firmwareVersion:%@"
+ "(null)"
+ "Missing dictionary. Unable to construct SRSourceDevice object."
+ "Missing encrypted identifier."
+ "Missing key to secure identifier with."
+ "Requesting local identifier before identifier has been secured."
+ "SRLogSourceDevice"
+ "SRSourceDevice"
+ "SRSourceDevice.m"
+ "Set source to %{private}@"
+ "Source Device identifier not yet encrypted."
+ "Source object should not have both an encrypted identifier and nonencrypted identifier."
+ "SourceHMACKey"
+ "T@\"NSData\",&,N,V_encryptedIdentifier"
+ "T@\"NSString\",&,N,V_ephemeralIdentifier"
+ "T@\"NSString\",R,C,N,V_firmwareVersion"
+ "T@\"NSString\",R,C,N,V_hardwareVersion"
+ "T@\"NSString\",R,C,N,V_manufacturer"
+ "T@\"NSString\",R,C,N,V_model"
+ "Td,N,V_segmentCreationTime"
+ "Unable to secure source identifier because %{public}@. Not calling setMetadata because source is not secure."
+ "[%@] Fetching initial authorization state for %{public}@"
+ "[%{public}@] Authorization status set to %ld for %{public}@ after initial update"
+ "_encryptedIdentifier"
+ "_ephemeralIdentifier"
+ "_firmwareVersion"
+ "_hardwareVersion"
+ "_initialAuthCompleteByBundleId"
+ "_initialAuthLock"
+ "_manufacturer"
+ "_sourceHMACKey"
+ "authorizedServicesForBundleId:"
+ "base64EncodedStringWithOptions:"
+ "com.apple.SensorKit.motion.headphone"
+ "dataUsingEncoding:"
+ "dataWithData:"
+ "dataWithLength:"
+ "encryptedIdentifier"
+ "ephemeralIdentifier"
+ "firmwareVersion"
+ "hardwareVersion"
+ "initWithIdentifier:manufacturer:model:hardwareVersion:firmwareVersion:"
+ "initialAuthorizationNeededForBundleId:"
+ "localIdentifier"
+ "manufacturer"
+ "mutableBytes"
+ "removeAllObjects"
+ "segmentCreationTime"
+ "setEncryptedIdentifier:"
+ "setEphemeralIdentifier:"
+ "setInitialAuthorizationCompleteForBundleId:"
+ "setSegmentCreationTime:"
+ "setSourceDevice:error:"
+ "source"
+ "sourceDevice"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "TB,V_initialAuthNeeded"
- "[%@] Fetching initial authorization state"
- "[%{public}@] Authorization status set to %ld after initial update"
- "_initialAuthNeeded"
- "authorizedServices"
- "initialAuthNeeded"
- "setInitialAuthNeeded:"

```
