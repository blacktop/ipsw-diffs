## AutomaticAssessmentConfiguration

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/AutomaticAssessmentConfiguration`

```diff

-14.2.9.0.0
-  __TEXT.__text: 0x21d4
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_methlist: 0x414
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x27f
-  __TEXT.__unwind_info: 0x130
+16.0.0.0.0
+  __TEXT.__text: 0x3050
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_methlist: 0x45c
+  __TEXT.__const: 0x370
+  __TEXT.__cstring: 0x303
+  __TEXT.__swift5_typeref: 0xce
+  __TEXT.__constg_swiftt: 0x64
+  __TEXT.__swift5_reflstr: 0x22
+  __TEXT.__swift5_fieldmd: 0x1c
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_proto: 0x24
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0x198
   __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methname: 0xe47
+  __TEXT.__objc_methname: 0xee3
   __TEXT.__objc_methtype: 0x1ee
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x78
+  __TEXT.__objc_stubs: 0xb00
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x338
+  __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x138
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x780
+  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__const: 0x68
+  __AUTH_CONST.__cfstring: 0x1c0
+  __AUTH_CONST.__objc_const: 0x7f0
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x50
-  __DATA.__data: 0xc0
-  __DATA.__bss: 0x10
+  __DATA.__objc_ivar: 0x5c
+  __DATA.__data: 0x138
+  __DATA.__bss: 0x490
   - /System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AACCore.framework/AACCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 89BA5A55-55BF-3C97-99A6-594C8A0B4067
-  Functions: 89
-  Symbols:   401
-  CStrings:  201
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: BD0F04ED-E3AC-3CBE-A8C2-66BBC587279F
+  Functions: 136
+  Symbols:   476
+  CStrings:  216
 
Symbols:
+ -[AEAssessmentConfiguration _allowsContentCapture]
+ -[AEAssessmentConfiguration _allowsNetworkAccess]
+ -[AEAssessmentConfiguration _setAllowsContentCapture:]
+ -[AEAssessmentConfiguration _setAllowsNetworkAccess:]
+ -[AEAssessmentParticipantConfiguration isRequired]
+ -[AEAssessmentParticipantConfiguration setRequired:]
+ -[AEAssessmentSession unwrapAECoreErrorFrom:]
+ _AENotInstalledParticipantsKey
+ _AERestrictedSystemParticipantsKey
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsContentCapture
+ _OBJC_IVAR_$_AEAssessmentConfiguration._allowsNetworkAccess
+ _OBJC_IVAR_$_AEAssessmentParticipantConfiguration._required
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_AutomaticAssessmentConfiguration
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_AutomaticAssessmentConfiguration
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_AutomaticAssessmentConfiguration
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_AutomaticAssessmentConfiguration
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_AutomaticAssessmentConfiguration
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_AutomaticAssessmentConfiguration
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_AutomaticAssessmentConfiguration
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AutomaticAssessmentConfiguration
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AutomaticAssessmentConfiguration
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AutomaticAssessmentConfiguration
+ _associated conformance SC21AEAssessmentErrorCodeLeV10Foundation021_ObjectiveCBridgeableB0SCs0B0
+ _associated conformance SC21AEAssessmentErrorCodeLeV10Foundation13CustomNSErrorSCs0B0
+ _associated conformance SC21AEAssessmentErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0C0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC21AEAssessmentErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0C0AcDP_AC01_bC8Protocol
+ _associated conformance SC21AEAssessmentErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0C0AcDP_SY
+ _associated conformance SC21AEAssessmentErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC021_ObjectiveCBridgeableB0
+ _associated conformance SC21AEAssessmentErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomG0
+ _associated conformance SC21AEAssessmentErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC21AEAssessmentErrorCodeLeVSHSCSQ
+ _associated conformance So21AEAssessmentErrorCodeV10Foundation01_bC8ProtocolSC01_B4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So21AEAssessmentErrorCodeV10Foundation01_bC8ProtocolSCSQ
+ _objc_msgSend$_allowsContentCapture
+ _objc_msgSend$_allowsNetworkAccess
+ _objc_msgSend$_setAllowsContentCapture:
+ _objc_msgSend$_setAllowsNetworkAccess:
+ _objc_msgSend$firstObject
+ _objc_msgSend$isRequired
+ _objc_msgSend$setRequired:
+ _objc_retain_x19
+ _swift_bridgeObjectRelease
+ _swift_dynamicCast
+ _swift_getForeignTypeMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _symbolic $s10Foundation18_ErrorCodeProtocolP
+ _symbolic $s10Foundation21_BridgedStoredNSErrorP
+ _symbolic $sSY
+ _symbolic SaySSG
+ _symbolic Si
+ _symbolic So7NSErrorC
+ _symbolic _____ SC21AEAssessmentErrorCodeLeV
+ _symbolic _____ So21AEAssessmentErrorCodeV
+ _type_layout_string SC21AEAssessmentErrorCodeLeV
CStrings:
+ "<%@: %p { allowsNetworkAccess = %@, required = %@, configurationInfo = %@ }>"
+ "AENotInstalledParticipants"
+ "AERestrictedSystemParticipantsKey"
+ "Required participants are not available on this device."
+ "TB,N,GisRequired,V_required"
+ "_allowsContentCapture"
+ "_required"
+ "_setAllowsContentCapture:"
+ "_setAllowsNetworkAccess:"
+ "firstObject"
+ "isRequired"
+ "required"
+ "setRequired:"
- "<%@: %p { allowsNetworkAccess = %@, configurationInfo = %@ }>"

```
