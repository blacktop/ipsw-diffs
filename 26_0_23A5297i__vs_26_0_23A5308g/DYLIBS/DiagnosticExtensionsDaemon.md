## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-201.0.0.0.0
-  __TEXT.__text: 0x6fa90
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x6a2c
-  __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x520b
+204.0.0.0.0
+  __TEXT.__text: 0x71ff0
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x6aac
+  __TEXT.__const: 0x300
+  __TEXT.__cstring: 0x5335
   __TEXT.__gcc_except_tab: 0x1dbc
-  __TEXT.__oslogstring: 0x8558
+  __TEXT.__oslogstring: 0x8729
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1aa8
+  __TEXT.__constg_swiftt: 0x60
+  __TEXT.__swift5_typeref: 0x42
+  __TEXT.__swift5_fieldmd: 0x50
+  __TEXT.__swift5_reflstr: 0x80
+  __TEXT.__swift5_proto: 0x4
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0x1b18
+  __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x892
-  __TEXT.__objc_methname: 0xee9e
-  __TEXT.__objc_methtype: 0x2332
-  __TEXT.__objc_stubs: 0xbd20
-  __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__const: 0x2058
-  __DATA_CONST.__objc_classlist: 0x260
+  __TEXT.__objc_methname: 0xf00c
+  __TEXT.__objc_methtype: 0x23a5
+  __TEXT.__objc_stubs: 0xbe40
+  __DATA_CONST.__got: 0x6d0
+  __DATA_CONST.__const: 0x20b0
+  __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3930
+  __DATA_CONST.__objc_selrefs: 0x3978
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x4b8
-  __AUTH_CONST.__const: 0xc20
-  __AUTH_CONST.__cfstring: 0x4ce0
-  __AUTH_CONST.__objc_const: 0x12898
+  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__const: 0xc40
+  __AUTH_CONST.__cfstring: 0x4d00
+  __AUTH_CONST.__objc_const: 0x12910
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x5ac
-  __DATA.__data: 0xa40
-  __DATA.__bss: 0x198
+  __AUTH.__objc_data: 0xfb0
+  __AUTH.__data: 0xb8
+  __DATA.__objc_ivar: 0x5b0
+  __DATA.__data: 0xa70
+  __DATA.__bss: 0x260
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x228
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/HomeKit.framework/HomeKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 338FBF25-1476-3C10-AF1D-9548F13B70E3
-  Functions: 2721
-  Symbols:   9485
-  CStrings:  5106
+  - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSystem.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: C7466E41-3EAE-3FA0-8B8F-5B39F534F777
+  Functions: 2761
+  Symbols:   9594
+  CStrings:  5140
 
Symbols:
+ +[DEDDevice arrayRepresentationForOperatingSystemVersion:]
+ +[DEDDevice operatingSystemVersionFromArrayRepresentation:]
+ -[DEDDevice operatingSystemVersion]
+ -[DEDDevice setOperatingSystemVersion:]
+ -[DEDSeedingFinisher archiveAndEncryptItemsInDirectory:]
+ -[DEDSeedingFinisher archiveAndEncryptItemsInDirectory:].cold.1
+ -[DEDSeedingFinisher archiveAndEncryptItemsInDirectory:].cold.2
+ -[DEDSeedingFinisher isSecurityResearchDeviceERM]
+ -[DEDSeedingFinisher isSecurityResearchDeviceERM].cold.1
+ _DEDDeviceKeyOperatingSystemVersion
+ _OBJC_CLASS_$__TtC26DiagnosticExtensionsDaemon10AEAHandler
+ _OBJC_IVAR_$_DEDDevice._operatingSystemVersion
+ _OBJC_METACLASS_$__TtC26DiagnosticExtensionsDaemon10AEAHandler
+ __CLASS_METHODS__TtC26DiagnosticExtensionsDaemon10AEAHandler
+ __DATA__TtC26DiagnosticExtensionsDaemon10AEAHandler
+ __INSTANCE_METHODS__TtC26DiagnosticExtensionsDaemon10AEAHandler
+ __METACLASS_DATA__TtC26DiagnosticExtensionsDaemon10AEAHandler
+ ___49-[DEDSeedingFinisher isSecurityResearchDeviceERM]_block_invoke
+ ___block_literal_global.69
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftAppleArchive_$_DiagnosticExtensionsDaemon
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_DiagnosticExtensionsDaemon
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_DiagnosticExtensionsDaemon
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_DiagnosticExtensionsDaemon
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_DiagnosticExtensionsDaemon
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_DiagnosticExtensionsDaemon
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_DiagnosticExtensionsDaemon
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_DiagnosticExtensionsDaemon
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_DiagnosticExtensionsDaemon
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_DiagnosticExtensionsDaemon
+ __swift_stdlib_bridgeErrorToNSError
+ _isSecurityResearchDeviceERM.ermEnabled
+ _isSecurityResearchDeviceERM.onceToken
+ _objc_allocWithZone
+ _objc_copyStruct
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$archiveAndEncryptItemsInDirectory:
+ _objc_msgSend$arrayRepresentationForOperatingSystemVersion:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$encryptWithSourceURL:destinationURL:
+ _objc_msgSend$isSecurityResearchDeviceERM
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$operatingSystemVersionFromArrayRepresentation:
+ _objc_msgSend$setOperatingSystemVersion:
+ _objc_opt_self
+ _swift_allocError
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_once
+ _swift_release
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_willThrow
+ _symbolic Say_____G 12AppleArchive0B5FlagsV
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 10Foundation3URLV
+ _symbolic _____ 26DiagnosticExtensionsDaemon10AEAHandlerC
+ _symbolic _____ 26DiagnosticExtensionsDaemon10AEAHandlerC5ErrorO
+ _symbolic _____Sg 6System8FilePathV
CStrings:
+ "/private/preboot/Cryptexes/System/Library/Diagnostics/DiagnosticsEncryptionPublicKey"
+ "/private/var/RPSupport/System/Library/Diagnostics/DiagnosticsEncryptionPublicKey"
+ "@40@0:8{?=qqq}16"
+ "AEA context public key set"
+ "AEA encryption file stream created"
+ "AEA encryption with %ld threads"
+ "AEA process finished"
+ "AEA source file stream created"
+ "Encryption failed with error: %{public}@"
+ "Failed to find encryption public key in expected paths."
+ "Failed to upload logs with error %{public}@"
+ "T{?=qqq},V_operatingSystemVersion"
+ "URLByAppendingPathExtension:"
+ "_TtC26DiagnosticExtensionsDaemon10AEAHandler"
+ "_operatingSystemVersion"
+ "archiveAndEncryptItemsInDirectory [%{public}@]"
+ "archiveAndEncryptItemsInDirectory:"
+ "arrayRepresentationForOperatingSystemVersion:"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "encryptWithSourceURL:destinationURL:"
+ "failed to aea encrypt [%{public}@] with path name [%{public}@] to [%{public}@]"
+ "isSecurityResearchDeviceERM"
+ "operatingSystemVersion"
+ "operatingSystemVersionFromArrayRepresentation:"
+ "setOperatingSystemVersion:"
+ "v40@0:8{?=qqq}16"
+ "{?=\"majorVersion\"q\"minorVersion\"q\"patchVersion\"q}"
+ "{?=qqq}16@0:8"
+ "{?=qqq}24@0:8@16"

```
