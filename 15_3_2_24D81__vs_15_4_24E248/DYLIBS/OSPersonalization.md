## OSPersonalization

> `/System/Library/PrivateFrameworks/OSPersonalization.framework/Versions/A/OSPersonalization`

```diff

-139.40.2.0.0
-  __TEXT.__text: 0x389a0
-  __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_methlist: 0x157c
-  __TEXT.__const: 0x6ea8
-  __TEXT.__oslogstring: 0x2e1d
-  __TEXT.__cstring: 0x58cc
-  __TEXT.__gcc_except_tab: 0x1f8
-  __TEXT.__unwind_info: 0x680
+149.0.0.0.0
+  __TEXT.__text: 0x350d4
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_methlist: 0x15fc
+  __TEXT.__const: 0x6957
+  __TEXT.__cstring: 0x529c
+  __TEXT.__oslogstring: 0x252f
+  __TEXT.__gcc_except_tab: 0x240
+  __TEXT.__unwind_info: 0x690
   __TEXT.__objc_classname: 0x21c
-  __TEXT.__objc_methname: 0x3dcc
-  __TEXT.__objc_methtype: 0x494
-  __TEXT.__objc_stubs: 0x3600
-  __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0xf48
+  __TEXT.__objc_methname: 0x405a
+  __TEXT.__objc_methtype: 0x4f8
+  __TEXT.__objc_stubs: 0x3860
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__const: 0xfe8
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfb0
-  __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x598
-  __AUTH_CONST.__const: 0x760
-  __AUTH_CONST.__cfstring: 0x3bc0
-  __AUTH_CONST.__objc_const: 0x25a8
+  __DATA_CONST.__objc_selrefs: 0x1048
+  __DATA_CONST.__objc_superrefs: 0x68
+  __AUTH_CONST.__auth_got: 0x588
+  __AUTH_CONST.__const: 0x7a8
+  __AUTH_CONST.__cfstring: 0x3ac0
+  __AUTH_CONST.__objc_const: 0x24e0
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x1d4
-  __DATA.__data: 0x98
+  __DATA.__objc_ivar: 0x1cc
+  __DATA.__data: 0xf0
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
-  - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
   - /System/Library/PrivateFrameworks/IASUtilitiesCore.framework/Versions/A/IASUtilitiesCore
   - /System/Library/PrivateFrameworks/InstallerDiagnostics.framework/Versions/A/InstallerDiagnostics

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: 05FC25A1-378C-3B28-8DFA-96E68473792B
-  Functions: 841
-  Symbols:   2430
-  CStrings:  2141
+  UUID: 97901998-E258-36C2-8707-DD6A35B2D075
+  Functions: 800
+  Symbols:   2440
+  CStrings:  2109
 
Symbols:
+ +[OSPDevice deviceWithBoardID:chipID:hardwareModel:]
+ +[OSPDevice deviceWithVariantDictionary:].cold.1
+ +[OSPNVRAM sharedInstance].cold.1
+ +[OSPSplunkEvent _compressedTSSRequestStringFromBundle:]
+ +[OSPSplunkEvent _compressedTSSRequestStringFromBundle:].cold.1
+ +[OSPSplunkEvent _compressedTSSRequestStringFromBundle:].cold.2
+ +[OSPSplunkEvent tssRequestFromBundle:ticketType:train:build:variant:device:productionMode:securityMode:result:]
+ +[OSPUtilities cpuCoreCount]
+ +[OSPUtilities cpuCoreCount].cold.1
+ +[OSPUtilities ignoreAuthInstallErrorInTestMode:]
+ +[OSPUtilities initializeRestoreLogging].cold.1
+ +[OSPUtilities mergeDirectoryAtPath:toPath:error:]
+ +[OSPUtilities mergeDirectoryAtPath:toPath:error:].cold.1
+ +[OSPersonalizationController sharedController].cold.1
+ -[OSPBuildIdentity _cacheEntryTypes]
+ -[OSPBuildIdentity _isSFRBuildIdentity:]
+ -[OSPBuildIdentity buildIdentityDictionary]
+ -[OSPBuildIdentity cryptex1Entries]
+ -[OSPBuildIdentity initWithDictionary:].cold.1
+ -[OSPBuildIdentity initWithDictionary:].cold.2
+ -[OSPBuildIdentity isSFR]
+ -[OSPBuildIdentity osEntries]
+ -[OSPBuildIdentity setBuildIdentityDictionary:]
+ -[OSPBuildIdentity setCryptex1Entries:]
+ -[OSPBuildIdentity setIsSFR:]
+ -[OSPBuildIdentity setOsEntries:]
+ -[OSPGlobalSigningController _enqueuePersonalizationRequest:shouldOutputManifestRoots:errors:]
+ -[OSPGlobalSigningController _ticketTypesForBuildIdentity:]
+ -[OSPGlobalSigningController queue]
+ -[OSPGlobalSigningController setQueue:]
+ -[OSPInstallSignedManifestsOperation _copyExtraManifestRootsToSandbox]
+ -[OSPInstallSignedManifestsOperation _findOSTicket]
+ -[OSPInstallSignedManifestsOperation _findOSTicket].cold.1
+ -[OSPRequest copyWithZone:]
+ -[OSPRequest enableTestMode]
+ -[OSPRequest extraManifestRoots]
+ -[OSPRequest maxConcurrentRequests]
+ -[OSPRequest setEnableTestMode:]
+ -[OSPRequest setExtraManifestRoots:]
+ -[OSPRequest setMaxConcurrentRequests:]
+ -[OSPRequest setTicketTypes:]
+ -[OSPRequest ticketTypes]
+ -[OSPSecureBootBundle buildIdentities]
+ -[OSPSecureBootBundle setBuildIdentities:]
+ -[OSPSplunkEvent .cxx_destruct]
+ -[OSPSplunkEvent dict]
+ -[OSPSplunkEvent init]
+ -[OSPSplunkEvent send]
+ -[OSPSplunkEvent send].cold.1
+ -[OSPSplunkEvent send].cold.2
+ -[OSPSplunkEvent setDict:]
+ -[OSPSplunkEvent setUuid:]
+ -[OSPSplunkEvent uuid]
+ -[OSPTelemetry _submitToInstallerDiagnostics].cold.1
+ -[OSPThinRestoreBundleOperation .cxx_destruct]
+ -[OSPThinRestoreBundleOperation cleanUp]
+ -[OSPThinRestoreBundleOperation description]
+ -[OSPThinRestoreBundleOperation main]
+ -[OSPThinRestoreBundleOperation main].cold.1
+ -[OSPThinRestoreBundleOperation setThinnedRestoreBundleURL:]
+ -[OSPThinRestoreBundleOperation thinnedRestoreBundleURL]
+ GCC_except_table7
+ OBJC_IVAR_$_OSPBuildIdentity._buildIdentityDictionary
+ OBJC_IVAR_$_OSPBuildIdentity._cryptex1Entries
+ OBJC_IVAR_$_OSPBuildIdentity._isSFR
+ OBJC_IVAR_$_OSPBuildIdentity._osEntries
+ OBJC_IVAR_$_OSPGlobalSigningController._queue
+ OBJC_IVAR_$_OSPRequest._enableTestMode
+ OBJC_IVAR_$_OSPRequest._extraManifestRoots
+ OBJC_IVAR_$_OSPRequest._maxConcurrentRequests
+ OBJC_IVAR_$_OSPRequest._ticketTypes
+ OBJC_IVAR_$_OSPSecureBootBundle._buildIdentities
+ OBJC_IVAR_$_OSPSplunkEvent._dict
+ OBJC_IVAR_$_OSPSplunkEvent._uuid
+ OBJC_IVAR_$_OSPThinRestoreBundleOperation._thinnedRestoreBundleURL
+ OSPLogObject.cold.1
+ OSPLogVersion.cold.1
+ OSPLogVersion.cold.2
+ OSPShouldLogToInstallLog.cold.1
+ OSPShouldLogToStderr.cold.1
+ OSPStderrDateFormatter.cold.1
+ _OBJC_CLASS_$_LPStaticAPFSVolume
+ _OBJC_CLASS_$_LPStaticMedia
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSMutableURLRequest
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_OSPSplunkEvent
+ _OBJC_CLASS_$_OSPThinRestoreBundleOperation
+ _OBJC_METACLASS_$_OSPSplunkEvent
+ _OBJC_METACLASS_$_OSPThinRestoreBundleOperation
+ _OSPSplunkEventTicketTypeMacOS
+ _OSPersonalizationOptionEnableTestMode
+ _OSPersonalizationOptionMaxConcurrentRequests
+ __22-[OSPSplunkEvent send]_block_invoke.cold.1
+ __Img4DecodePayloadPropertyExistsWithValue
+ __OBJC_$_CLASS_METHODS_OSPSplunkEvent
+ __OBJC_$_INSTANCE_METHODS_OSPSplunkEvent
+ __OBJC_$_INSTANCE_METHODS_OSPThinRestoreBundleOperation
+ __OBJC_$_INSTANCE_VARIABLES_OSPSplunkEvent
+ __OBJC_$_INSTANCE_VARIABLES_OSPThinRestoreBundleOperation
+ __OBJC_$_PROP_LIST_OSPSplunkEvent
+ __OBJC_$_PROP_LIST_OSPThinRestoreBundleOperation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$_OSPRequest
+ __OBJC_CLASS_RO_$_OSPSplunkEvent
+ __OBJC_CLASS_RO_$_OSPThinRestoreBundleOperation
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_OSPSplunkEvent
+ __OBJC_METACLASS_RO_$_OSPThinRestoreBundleOperation
+ __OBJC_PROTOCOL_$_NSCopying
+ ___22-[OSPSplunkEvent send]_block_invoke
+ ___94-[OSPGlobalSigningController _enqueuePersonalizationRequest:shouldOutputManifestRoots:errors:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24l
+ ___block_descriptor_49_e8_32s40s_e5_v8?0l
+ __oidQCCompliance
+ __oidQCDisclosures
+ __oidQCEuRetentionPeriod
+ __oidQCLimitValue
+ __oidQCStatements
+ __oidQCSyntaxv1
+ __oidQCSyntaxv2
+ __oidQCType
+ __oidQCTypeEseal
+ __oidQCTypeEsign
+ __oidQCTypeWeb
+ __oidSemanticsIdEidasLegal
+ __oidSemanticsIdEidasNatural
+ __oidSemanticsIdLegal
+ __oidSemanticsIdNatural
+ _dispatch_time
+ _objc_msgSend$_cacheEntryTypes
+ _objc_msgSend$_compressedTSSRequestStringFromBundle:
+ _objc_msgSend$_copyExtraManifestRootsToSandbox
+ _objc_msgSend$_enqueuePersonalizationRequest:shouldOutputManifestRoots:errors:
+ _objc_msgSend$_findOSTicket
+ _objc_msgSend$_isSFRBuildIdentity:
+ _objc_msgSend$_ticketTypesForBuildIdentity:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addOperationWithBlock:
+ _objc_msgSend$allValues
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$buildIdentities
+ _objc_msgSend$buildIdentityDictionary
+ _objc_msgSend$compressedDataUsingAlgorithm:error:
+ _objc_msgSend$cpuCoreCount
+ _objc_msgSend$cryptex1Entries
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$dict
+ _objc_msgSend$enableTestMode
+ _objc_msgSend$extraManifestRoots
+ _objc_msgSend$firstObject
+ _objc_msgSend$ignoreAuthInstallErrorInTestMode:
+ _objc_msgSend$isSFR
+ _objc_msgSend$maxConcurrentOperationCount
+ _objc_msgSend$maxConcurrentRequests
+ _objc_msgSend$mergeDirectoryAtPath:toPath:error:
+ _objc_msgSend$osEntries
+ _objc_msgSend$queue
+ _objc_msgSend$requestWithURL:
+ _objc_msgSend$resume
+ _objc_msgSend$send
+ _objc_msgSend$setBuildIdentities:
+ _objc_msgSend$setCryptex1Entries:
+ _objc_msgSend$setEnableTestMode:
+ _objc_msgSend$setFakePersonalizationErrorCode:
+ _objc_msgSend$setHTTPMethod:
+ _objc_msgSend$setMaxConcurrentOperationCount:
+ _objc_msgSend$setMaxConcurrentRequests:
+ _objc_msgSend$setMergeToOutputDirectory:
+ _objc_msgSend$setOsEntries:
+ _objc_msgSend$setPackageSpecifiers:
+ _objc_msgSend$setTicketTypes:
+ _objc_msgSend$setValue:forHTTPHeaderField:
+ _objc_msgSend$sharedSession
+ _objc_msgSend$thinnedRestoreBundleURL
+ _objc_msgSend$ticketTypes
+ _objc_msgSend$tssRequestFromBundle:ticketType:train:build:variant:device:productionMode:securityMode:result:
+ _objc_msgSend$uploadTaskWithRequest:fromData:completionHandler:
+ _objc_msgSend$waitUntilAllOperationsAreFinished
+ _objc_msgSend$writeToURL:error:
+ _objc_sync_enter
+ _objc_sync_exit
+ _oidQCCompliance
+ _oidQCDisclosures
+ _oidQCEuRetentionPeriod
+ _oidQCLimitValue
+ _oidQCStatements
+ _oidQCSyntaxv1
+ _oidQCSyntaxv2
+ _oidQCType
+ _oidQCTypeEseal
+ _oidQCTypeEsign
+ _oidQCTypeWeb
+ _oidSemanticsIdEidasLegal
+ _oidSemanticsIdEidasNatural
+ _oidSemanticsIdLegal
+ _oidSemanticsIdNatural
- +[OSPDevice deviceWithBoardID:chipID:]
- +[OSPSecureBootVerifier allTags]
- +[OSPSecureBootVerifier bootloaderTags]
- +[OSPSecureBootVerifier kernelCacheTags]
- -[OSPInstallSignedManifestsOperation _findAPTicket]
- -[OSPInstallSignedManifestsOperation _findAPTicket].cold.1
- -[OSPInstallSignedManifestsOperation _installSandbox].cold.9
- -[OSPRequest automaticallyDetectSplat]
- -[OSPRequest requestSplatTicketOnly]
- -[OSPRequest requestSplatTicket]
- -[OSPRequest setAutomaticallyDetectSplat:]
- -[OSPRequest setRequestSplatTicket:]
- -[OSPRequest setRequestSplatTicketOnly:]
- -[OSPRequest setSkipPersonalizationForTesting:]
- -[OSPRequest skipPersonalizationForTesting]
- -[OSPSecureBootBundle _amaiFromDevice:]
- -[OSPSecureBootBundle _amaiFromDevice:].cold.1
- -[OSPSecureBootBundle _amaiFromDevice:].cold.2
- -[OSPSecureBootVerifier .cxx_destruct]
- -[OSPSecureBootVerifier _verifyManifest:withTag:]
- -[OSPSecureBootVerifier _verifyManifest:withTag:].cold.1
- -[OSPSecureBootVerifier _verifyManifest:withTag:].cold.2
- -[OSPSecureBootVerifier _verifyManifest:withTag:].cold.3
- -[OSPSecureBootVerifier _verifyManifest:withTag:].cold.4
- -[OSPSecureBootVerifier _verifyManifest:withTag:].cold.5
- -[OSPSecureBootVerifier _verifyManifest:withTag:].cold.6
- -[OSPSecureBootVerifier _verifyManifest:withTag:].cold.7
- -[OSPSecureBootVerifier device]
- -[OSPSecureBootVerifier initWithBootFileURL:device:]
- -[OSPSecureBootVerifier payloadData]
- -[OSPSecureBootVerifier policy]
- -[OSPSecureBootVerifier setDevice:]
- -[OSPSecureBootVerifier setPayloadData:]
- -[OSPSecureBootVerifier setPolicy:]
- -[OSPSecureBootVerifier setUrl:]
- -[OSPSecureBootVerifier setValidTags:]
- -[OSPSecureBootVerifier url]
- -[OSPSecureBootVerifier validTags]
- -[OSPSecureBootVerifier verify]
- -[OSPSecureBootVerifier verify].cold.1
- -[OSPSecureBootVerifier verify].cold.2
- -[OSPSecureBootVerifier verify].cold.3
- -[OSPSecureBootVolumeVerifier .cxx_destruct]
- -[OSPSecureBootVolumeVerifier device]
- -[OSPSecureBootVolumeVerifier initWithVolume:]
- -[OSPSecureBootVolumeVerifier initWithVolume:].cold.1
- -[OSPSecureBootVolumeVerifier initWithVolume:].cold.2
- -[OSPSecureBootVolumeVerifier initialPopulateCompleteSemaphore]
- -[OSPSecureBootVolumeVerifier policy]
- -[OSPSecureBootVolumeVerifier prebootVolume]
- -[OSPSecureBootVolumeVerifier setDevice:]
- -[OSPSecureBootVolumeVerifier setInitialPopulateCompleteSemaphore:]
- -[OSPSecureBootVolumeVerifier setPolicy:]
- -[OSPSecureBootVolumeVerifier setPrebootVolume:]
- -[OSPSecureBootVolumeVerifier setTargetDisk:]
- -[OSPSecureBootVolumeVerifier setVolumeURL:]
- -[OSPSecureBootVolumeVerifier targetDisk]
- -[OSPSecureBootVolumeVerifier verify]
- -[OSPSecureBootVolumeVerifier verify].cold.1
- -[OSPSecureBootVolumeVerifier verify].cold.2
- -[OSPSecureBootVolumeVerifier verify].cold.3
- -[OSPSecureBootVolumeVerifier volumeURL]
- OBJC_IVAR_$_OSPRequest._automaticallyDetectSplat
- OBJC_IVAR_$_OSPRequest._requestSplatTicket
- OBJC_IVAR_$_OSPRequest._requestSplatTicketOnly
- OBJC_IVAR_$_OSPRequest._skipPersonalizationForTesting
- OBJC_IVAR_$_OSPSecureBootVerifier._device
- OBJC_IVAR_$_OSPSecureBootVerifier._payloadData
- OBJC_IVAR_$_OSPSecureBootVerifier._policy
- OBJC_IVAR_$_OSPSecureBootVerifier._url
- OBJC_IVAR_$_OSPSecureBootVerifier._validTags
- OBJC_IVAR_$_OSPSecureBootVolumeVerifier._device
- OBJC_IVAR_$_OSPSecureBootVolumeVerifier._initialPopulateCompleteSemaphore
- OBJC_IVAR_$_OSPSecureBootVolumeVerifier._policy
- OBJC_IVAR_$_OSPSecureBootVolumeVerifier._prebootVolume
- OBJC_IVAR_$_OSPSecureBootVolumeVerifier._targetDisk
- OBJC_IVAR_$_OSPSecureBootVolumeVerifier._volumeURL
- _AMAuthInstallBundleCopyBuildIdentityForVariant
- _CFDataGetBytePtr
- _CFDataGetLength
- _LOCAL_RSA4K_SHA384_ROOT_CA_CERTIFICATE
- _LOCAL_RSA4K_SHA384_ROOT_CA_CERTIFICATE_SIZE
- _OBJC_CLASS_$_LPAPFSVolume
- _OBJC_CLASS_$_LPMedia
- _OBJC_CLASS_$_NSMutableString
- _OBJC_CLASS_$_OSPSecureBootVerifier
- _OBJC_CLASS_$_OSPSecureBootVolumeVerifier
- _OBJC_METACLASS_$_OSPSecureBootVerifier
- _OBJC_METACLASS_$_OSPSecureBootVolumeVerifier
- _OSPersonalizationOptionSkipPersonalizationForTesting
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_9
- __88-[OSPGlobalSigningController globallySignForAllDevicesAndVariantsWithCompletionHandler:]_block_invoke.cold.5
- __88-[OSPGlobalSigningController globallySignForAllDevicesAndVariantsWithCompletionHandler:]_block_invoke.cold.6
- __OBJC_$_CLASS_METHODS_OSPSecureBootVerifier
- __OBJC_$_INSTANCE_METHODS_OSPSecureBootVerifier
- __OBJC_$_INSTANCE_METHODS_OSPSecureBootVolumeVerifier
- __OBJC_$_INSTANCE_VARIABLES_OSPSecureBootVerifier
- __OBJC_$_INSTANCE_VARIABLES_OSPSecureBootVolumeVerifier
- __OBJC_$_PROP_LIST_OSPSecureBootVerifier
- __OBJC_$_PROP_LIST_OSPSecureBootVolumeVerifier
- __OBJC_CLASS_RO_$_OSPSecureBootVerifier
- __OBJC_CLASS_RO_$_OSPSecureBootVolumeVerifier
- __OBJC_METACLASS_RO_$_OSPSecureBootVerifier
- __OBJC_METACLASS_RO_$_OSPSecureBootVolumeVerifier
- __digest_str
- __tag_str
- _exit
- _image4_client_callbacks
- _image4_context_validate
- _image4_validation_callback
- _implementation
- _objc_msgSend$_amaiFromDevice:
- _objc_msgSend$_findAPTicket
- _objc_msgSend$_verifyManifest:withTag:
- _objc_msgSend$allTags
- _objc_msgSend$appendString:
- _objc_msgSend$automaticallyDetectSplat
- _objc_msgSend$bootloaderTags
- _objc_msgSend$dataWithContentsOfFile:
- _objc_msgSend$fileURLWithPathComponents:
- _objc_msgSend$getSSOServiceTicketAsOnConsoleUserWithUI:error:
- _objc_msgSend$initWithBootFileURL:device:
- _objc_msgSend$kernelCacheTags
- _objc_msgSend$mediaForPath:
- _objc_msgSend$mediaUUID
- _objc_msgSend$mountAtPath:error:
- _objc_msgSend$payloadData
- _objc_msgSend$policy
- _objc_msgSend$requestSplatTicket
- _objc_msgSend$requestSplatTicketOnly
- _objc_msgSend$setAutomaticallyDetectSplat:
- _objc_msgSend$setPayloadData:
- _objc_msgSend$setPolicy:
- _objc_msgSend$setRequestSplatTicket:
- _objc_msgSend$setRequestSplatTicketOnly:
- _objc_msgSend$setSkipPersonalizationForTesting:
- _objc_msgSend$setValidTags:
- _objc_msgSend$skipPersonalizationForTesting
- _objc_msgSend$string
- _objc_msgSend$targetDisk
- _objc_msgSend$url
- _objc_msgSend$validTags
- _objc_msgSend$verify
- _objc_opt_respondsToSelector
- image4_context_validate.cold.1
- image4_context_validate.cold.10
- image4_context_validate.cold.11
- image4_context_validate.cold.12
- image4_context_validate.cold.13
- image4_context_validate.cold.14
- image4_context_validate.cold.15
- image4_context_validate.cold.16
- image4_context_validate.cold.17
- image4_context_validate.cold.18
- image4_context_validate.cold.19
- image4_context_validate.cold.2
- image4_context_validate.cold.20
- image4_context_validate.cold.3
- image4_context_validate.cold.4
- image4_context_validate.cold.5
- image4_context_validate.cold.6
- image4_context_validate.cold.7
- image4_context_validate.cold.8
- image4_context_validate.cold.9
- image4_validation_callback.cold.1
- image4_validation_callback.cold.10
- image4_validation_callback.cold.11
- image4_validation_callback.cold.12
- image4_validation_callback.cold.13
- image4_validation_callback.cold.14
- image4_validation_callback.cold.15
- image4_validation_callback.cold.16
- image4_validation_callback.cold.17
- image4_validation_callback.cold.18
- image4_validation_callback.cold.19
- image4_validation_callback.cold.2
- image4_validation_callback.cold.3
- image4_validation_callback.cold.4
- image4_validation_callback.cold.5
- image4_validation_callback.cold.6
- image4_validation_callback.cold.7
- image4_validation_callback.cold.8
- image4_validation_callback.cold.9
CStrings:
+ "\n       Modes:\n           --help, -h                      Display this message\n           --bundle, -b BUNDLE_PATH        Globally sign the build manifest located in the specified secure boot bundle path\n\n       Options:\n           --document, -D PATH             PR doc to use (options below will override those specified in the file)\n           --output, -o PATH               Write the resulting image4 manifests to the specified directory\n           --variant, -V VARIANT_NAME      Personalize only the given variant name (default is to choose the first\n                                           available variant)\n           --deviceClass DEVICE_CLASS      If specified, only generate manifests for the given device class. Multiple\n                                           device classes may be specified.\n\n       Examples:\n           sudo %s --bundle /usr/standalone/i386/SecureBoot.bundle --output /tmp/personalized\n               Globally sign all variants for all devices supported by the build manifest in SecureBoot.Bundle, and write\n               the output to /tmp/personalized\n"
+ "149"
+ "18:13:34"
+ "@\"LPStaticAPFSVolume\""
+ "@\"NSMutableDictionary\""
+ "@\"NSOperationQueue\""
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8I16I20@24"
+ "@76@0:8@16@24@32@40@48@56B64B68i72"
+ "B24@0:8Q16"
+ "B40@0:8@16@24^@32"
+ "Build identity dictionary missing"
+ "BuildIdentities"
+ "Content-Type"
+ "DFU"
+ "Detected Cryptex1 entries"
+ "Detected OS entries"
+ "Failed to compress tss request for splunk: %@"
+ "Failed to copy %@ -> %@: %@"
+ "Failed to instantiate build identity: build identity isn't a dictionary"
+ "Failed to instantiate build identity: variant (%@) or device (%@) missing"
+ "Failed to read debug tss request for splunk: %s"
+ "Failed to send event %@ to splunk: %@"
+ "Failed to serialize json for splunk: %@"
+ "Global signing failed (variant: %@, device: %@): %@"
+ "Global signing failed (variant: %@, type: %@, device: %@): %@"
+ "GlobalSigningOutputBundle"
+ "Globally signing %ld variants for %ld devices (concurrency = %ld)"
+ "Ignoring error in test mode: %d"
+ "IsSFR"
+ "Mar 15 2025"
+ "Merging %@ -> %@"
+ "Merging request output"
+ "NSCopying"
+ "No ticket types detected, skipping %@ variant '%@' for %@"
+ "OSPMaxConcurrentRequests"
+ "OSPSplunkEvent"
+ "OSPThinRestoreBundleOperation"
+ "OSPThinnedBundle"
+ "POST"
+ "SFR"
+ "Start global signing (variant: %@, device: %@)"
+ "Start global signing (variant: %@, root type: %@, device: %@)"
+ "Successfully sent event %@ to splunk"
+ "T@\"LPStaticAPFSVolume\",&,V_prebootVolume"
+ "T@\"NSArray\",&,V_cryptex1Entries"
+ "T@\"NSArray\",&,V_osEntries"
+ "T@\"NSDictionary\",&,V_buildIdentities"
+ "T@\"NSDictionary\",&,V_buildIdentityDictionary"
+ "T@\"NSMutableArray\",&,V_extraManifestRoots"
+ "T@\"NSMutableDictionary\",&,V_dict"
+ "T@\"NSOperationQueue\",&,V_queue"
+ "T@\"NSString\",&,V_uuid"
+ "T@\"NSURL\",&,V_thinnedRestoreBundleURL"
+ "TB,V_enableTestMode"
+ "TB,V_isSFR"
+ "TQ,V_maxConcurrentRequests"
+ "TQ,V_ticketTypes"
+ "Thinning restore bundle"
+ "Timed out sending event %@ to splunk"
+ "Using secure boot bundle: %@"
+ "VariantContents"
+ "Writing thinned build manifest to %@"
+ "__OSPEnableTestMode"
+ "_buildIdentities"
+ "_buildIdentityDictionary"
+ "_cacheEntryTypes"
+ "_compressedTSSRequestStringFromBundle:"
+ "_copyExtraManifestRootsToSandbox"
+ "_cryptex1Entries"
+ "_dict"
+ "_enableTestMode"
+ "_enqueuePersonalizationRequest:shouldOutputManifestRoots:errors:"
+ "_extraManifestRoots"
+ "_findOSTicket"
+ "_isSFR"
+ "_isSFRBuildIdentity:"
+ "_maxConcurrentRequests"
+ "_osEntries"
+ "_queue"
+ "_thinnedRestoreBundleURL"
+ "_ticketTypes"
+ "_ticketTypesForBuildIdentity:"
+ "addObjectsFromArray:"
+ "addOperationWithBlock:"
+ "allValues"
+ "amai/debug/tss-request.plist"
+ "application/json"
+ "base64EncodedStringWithOptions:"
+ "build"
+ "buildIdentities"
+ "buildIdentityDictionary"
+ "clientId"
+ "compressedDataUsingAlgorithm:error:"
+ "copyWithZone:"
+ "cpuCoreCount"
+ "cryptex1Entries"
+ "dataWithContentsOfURL:"
+ "dataWithJSONObject:options:error:"
+ "deviceWithBoardID:chipID:hardwareModel:"
+ "dict"
+ "enableTestMode"
+ "event"
+ "events"
+ "extraManifestRoots"
+ "firstObject"
+ "globalSigning"
+ "http://localhost"
+ "https://xp.apple.com/report/2/psr_ota"
+ "hw.logicalcpu"
+ "ignoreAuthInstallErrorInTestMode:"
+ "isSFR"
+ "macOS"
+ "maxConcurrentOperationCount"
+ "maxConcurrentRequests"
+ "mergeDirectoryAtPath:toPath:error:"
+ "osEntries"
+ "queue"
+ "requestWithURL:"
+ "result"
+ "resume"
+ "send"
+ "setBuildIdentities:"
+ "setBuildIdentityDictionary:"
+ "setCryptex1Entries:"
+ "setDict:"
+ "setEnableTestMode:"
+ "setExtraManifestRoots:"
+ "setHTTPMethod:"
+ "setIsSFR:"
+ "setMaxConcurrentOperationCount:"
+ "setMaxConcurrentRequests:"
+ "setOsEntries:"
+ "setQueue:"
+ "setThinnedRestoreBundleURL:"
+ "setTicketTypes:"
+ "setValue:forHTTPHeaderField:"
+ "sharedSession"
+ "sysctl hw.logicalcpu failed: %d, using 1"
+ "thinnedRestoreBundleURL"
+ "ticketType"
+ "ticketTypes"
+ "train"
+ "tssRequest"
+ "tssRequestFromBundle:ticketType:train:build:variant:device:productionMode:securityMode:result:"
+ "uploadTaskWithRequest:fromData:completionHandler:"
+ "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "v36@0:8@16B24@28"
+ "waitUntilAllOperationsAreFinished"
+ "writeToURL:error:"
- "\n       Modes:\n           --help, -h                      Display this message\n           --bundle, -b BUNDLE_PATH        Globally sign the build manifest located in the specified secure boot bundle path\n\n       Options:\n           --document, -D PATH             PR doc to use (options below will override those specified in the file)\n           --output, -o PATH               Write the resulting image4 manifests to the specified directory\n           --variant, -V VARIANT_NAME      Personalize only the given variant name (default is to choose the first\n                                           available variant)\n           --deviceClass DEVICE_CLASS      If specified, only generate manifests for the given device class. Multiple\n                                           device classes may be specified.\n           --splat                         Request a splat ticket alongside the AP ticket, overriding auto-detection\n           --noSplat                       Do not request a splat ticket, overriding auto-detection\n           --splatOnly                     Request a splat ticket alone, overriding auto-detection\n\n       Examples:\n           sudo %s --bundle /usr/standalone/i386/SecureBoot.bundle --output /tmp/personalized\n               Globally sign all variants for all devices supported by the build manifest in SecureBoot.Bundle, and write\n               the output to /tmp/personaized\n"
- "%02X "
- "%c%c%c%c"
- "139.40.2"
- "20:36:11"
- "@\"LPAPFSVolume\""
- "@\"LPMedia\""
- "@24@0:8I16I20"
- "B28@0:8@16I24"
- "Booter doesn't exist at path: %@"
- "Computed: %@"
- "Context validation failed for tag %@"
- "Context validation succeeded for tag %@"
- "Couldn't find release or development kernel cache"
- "Detected splat but no OS entries, setting requestSplatTicketOnly"
- "Detected splat, setting requestSplatTicket"
- "Disk is APFS but couldn't find preboot volume"
- "Encountered error during global signing, stopping"
- "Error loading manifest: %@"
- "Error loading payload: %@"
- "Error validating context: ECID mismatch"
- "Error validating context: board ID mismatch"
- "Error validating context: chip ID mismtach"
- "Error validating context: invalid internal use only build flag"
- "Error validating context: invalid manifest xugs value, needs to be 1"
- "Error validating context: manifest ECID required but not found"
- "Error validating context: manifest certificate epoch is too low"
- "Error validating context: manifest production status is too low"
- "Error validating context: manifest security mode is too low"
- "Error validating context: manifest xugs required but not found"
- "Error validating context: payload digest mismatch"
- "Error validating context: payload effective production status is too low"
- "Error validating context: payload effective security mode is too low"
- "Error validating context: security domain mismatch"
- "Error validating context: unexpected internal use only build flag found"
- "Error validating context: unexpected manifest ECID found"
- "Error validating context: unexpected manifest xugs found"
- "Error validating context: unknown manifest type"
- "Failed to compute payload hash: %i"
- "Failed to configure amai with ap parameters"
- "Failed to configure amai with ap software coprocessor parameters"
- "Failed to decode length of manifest: %d"
- "Failed to find disk for path: %@"
- "Failed to get build identity for variant (%@) in bundle (%@): %d"
- "Failed to initialize manifest: %d"
- "Globally signing %ld variants for %ld devices"
- "Globally signing variant '%@' for %@"
- "Globally signing variant '%@' into manifest root '%@' for %@"
- "Jan  7 2025"
- "Loaded secure boot bundle: %@"
- "Manifest length (%zu) doesn't match file length (%zu)"
- "Manifest: %@"
- "No manifest exists at path: %@"
- "No secure boot policy was set to verify against"
- "OSPSecureBootVerifier"
- "OSPSecureBootVolumeVerifier"
- "Payload digest: %@"
- "Picked kernelcache at %@"
- "System/Library/CoreServices/boot.efi"
- "System/Library/PrelinkedKernels/immutablekernel"
- "System/Library/PrelinkedKernels/immutablekernel.development"
- "T@\"LPAPFSVolume\",&,V_prebootVolume"
- "T@\"LPMedia\",&,V_targetDisk"
- "T@\"NSArray\",&,V_validTags"
- "T@\"NSData\",&,V_payloadData"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,V_initialPopulateCompleteSemaphore"
- "T@\"NSURL\",&,V_url"
- "TB,V_automaticallyDetectSplat"
- "TB,V_requestSplatTicket"
- "TB,V_requestSplatTicketOnly"
- "TB,V_skipPersonalizationForTesting"
- "TQ,V_policy"
- "Trust evaluation failed for tag %@: %d"
- "Verifying %@ with tag %@"
- "Warning: skipPersonalizationForTesting is set"
- "^{__AMAuthInstall=}24@0:8@16"
- "__OSPSkipPersonalizationForTesting"
- "_amaiFromDevice:"
- "_automaticallyDetectSplat"
- "_findAPTicket"
- "_initialPopulateCompleteSemaphore"
- "_payloadData"
- "_policy"
- "_requestSplatTicket"
- "_requestSplatTicketOnly"
- "_skipPersonalizationForTesting"
- "_targetDisk"
- "_url"
- "_validTags"
- "_verifyManifest:withTag:"
- "allTags"
- "appendString:"
- "automaticallyDetectSplat"
- "boot/System/Library/KernelCollections/BootKernelExtensions.kc"
- "boot/System/Library/KernelCollections/BootKernelExtensions.kc.development"
- "bootloaderTags"
- "dataWithContentsOfFile:"
- "deviceWithBoardID:chipID:"
- "fileURLWithPathComponents:"
- "getSSOServiceTicketAsOnConsoleUserWithUI:error:"
- "image4_validation_callback: failed on property 0x%08X"
- "image4_validation_callback: invalid DGST property"
- "image4_validation_callback: manifest board_id = 0x%X"
- "image4_validation_callback: manifest certificate_epoch = 0x%X"
- "image4_validation_callback: manifest chip_id = 0x%X"
- "image4_validation_callback: manifest ecid = 0x%llX"
- "image4_validation_callback: manifest internal_use_only_build = 0x%X"
- "image4_validation_callback: manifest mix_n_match = 0x%X"
- "image4_validation_callback: manifest production_status = 0x%X"
- "image4_validation_callback: manifest security_domain = 0x%X"
- "image4_validation_callback: manifest security_mode = 0x%X"
- "image4_validation_callback: manifest use_global_signing = 0x%X"
- "image4_validation_callback: object effective_production_status = 0x%X"
- "image4_validation_callback: object effective_security_mode = 0x%X"
- "image4_validation_callback: object enable_keys = 0x%X"
- "image4_validation_callback: unhandled manifest tag %@"
- "image4_validation_callback: unhandled object tag %@"
- "image4_validation_callback: unknown property type 0x%08X"
- "initWithBootFileURL:device:"
- "initWithVolume:"
- "initialPopulateCompleteSemaphore"
- "kernelCacheTags"
- "mediaForPath:"
- "mediaUUID"
- "mountAtPath:error:"
- "noSplat"
- "payloadData"
- "policy"
- "preboot"
- "requestSplatTicket"
- "requestSplatTicketOnly"
- "setAutomaticallyDetectSplat:"
- "setInitialPopulateCompleteSemaphore:"
- "setPayloadData:"
- "setPolicy:"
- "setRequestSplatTicket:"
- "setRequestSplatTicketOnly:"
- "setSkipPersonalizationForTesting:"
- "setTargetDisk:"
- "setUrl:"
- "setValidTags:"
- "skipPersonalizationForTesting"
- "splat"
- "splatOnly"
- "string"
- "targetDisk"
- "url"
- "validTags"
- "verify"

```
