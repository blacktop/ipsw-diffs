## AppleEmbeddedAccessoryUpdaterService

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleEmbeddedAccessoryUpdaterService.xpc/AppleEmbeddedAccessoryUpdaterService`

```diff

-2899.60.5.0.0
-  __TEXT.__text: 0x59950
-  __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_stubs: 0x1b80
-  __TEXT.__objc_methlist: 0xd44
-  __TEXT.__const: 0x9f10
-  __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__cstring: 0x15487
-  __TEXT.__objc_methname: 0x2002
-  __TEXT.__objc_classname: 0x2af
-  __TEXT.__objc_methtype: 0x890
-  __TEXT.__oslogstring: 0x267
-  __TEXT.__unwind_info: 0xe00
-  __DATA_CONST.__auth_got: 0xb40
-  __DATA_CONST.__got: 0x180
+2899.100.77.0.0
+  __TEXT.__text: 0x6dce8
+  __TEXT.__auth_stubs: 0x1720
+  __TEXT.__objc_stubs: 0x2c00
+  __TEXT.__objc_methlist: 0x2ae4
+  __TEXT.__const: 0xa150
+  __TEXT.__gcc_except_tab: 0x1d4
+  __TEXT.__cstring: 0x15cc5
+  __TEXT.__objc_methname: 0x35c7
+  __TEXT.__objc_classname: 0xb08
+  __TEXT.__objc_methtype: 0xd99
+  __TEXT.__oslogstring: 0x752
+  __TEXT.__unwind_info: 0x15f0
+  __DATA_CONST.__auth_got: 0xba0
+  __DATA_CONST.__got: 0x190
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x1c68
-  __DATA_CONST.__cfstring: 0xe700
-  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__const: 0x1f58
+  __DATA_CONST.__cfstring: 0xf0c0
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x260
+  __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2810
-  __DATA.__objc_selrefs: 0x918
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x108
-  __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0x1a8
-  __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0xa10
-  __DATA.__bss: 0x918
-  __DATA.__common: 0x10
+  __DATA_CONST.__objc_intobj: 0x78
+  __DATA.__objc_const: 0x5a68
+  __DATA.__objc_selrefs: 0xe78
+  __DATA.__objc_ivar: 0x36c
+  __DATA.__objc_data: 0x14f0
+  __DATA.__data: 0xa70
+  __DATA.__bss: 0x948
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libc++.1.dylib
+  - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1342
-  Symbols:   1567
-  CStrings:  3827
+  Functions: 1951
+  Symbols:   1719
+  CStrings:  4347
 
Symbols:
+ _IONotificationPortSetDispatchQueue
+ _IOServiceAddInterestNotification
+ _OBJC_CLASS_$_UARPAssetTagBackDeploy
+ _OBJC_CLASS_$_UARPAssetVersionBackDeploy
+ _OBJC_CLASS_$_UARPMetaDataTLV16BackDeploy
+ _OBJC_CLASS_$_UARPMetaDataTLV32BackDeploy
+ _OBJC_CLASS_$_UARPMetaDataTLV64BackDeploy
+ _OBJC_CLASS_$_UARPMetaDataTLV8BackDeploy
+ _OBJC_CLASS_$_UARPMetaDataTLVBackDeploy
+ _OBJC_CLASS_$_UARPMetaDataTLVDataBackDeploy
+ _OBJC_CLASS_$_UARPMetaDataTLVStringBackDeploy
+ _OBJC_CLASS_$_UARPSuperBinaryBackDeploy
+ _OBJC_CLASS_$_UARPSuperBinaryPayloadBackDeploy
+ _OBJC_CLASS_$_UARPTLVHostPersonalizationRequiredBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationBoardIDBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationChipEpochBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationChipIDBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationChipRevisionBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationECIDBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationECIDDataBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationEnableMixMatchBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationFTABPayloadBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationFTABSubfileDigestBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationFTABSubfileDigestFilenameBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationFTABSubfileEPROBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationFTABSubfileESECBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationFTABSubfileHashAlgorithmBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationFTABSubfileLongnameBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationFTABSubfileTagBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationFTABSubfileTrustedBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationLifeBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationLogicalUnitNumberBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationManifestEpochBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationManifestPrefixBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationManifestSuffixBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationNonceBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationNonceHashBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationPayloadTagBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationPrefixNeedsLogicalUnitNumberBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationProductionModeBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationProvisioningBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationRequiredBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationSecurityDomainBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationSecurityModeBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationSoCLiveNonceBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationSuffixNeedsLogicalUnitNumberBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationSuperBinaryAssetIDBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationSuperBinaryPayloadIndexBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizationTicketNeedsLogicalUnitNumberBackDeploy
+ _OBJC_CLASS_$_UARPTLVPersonalizedManifestBackDeploy
+ _OBJC_CLASS_$_UARPTLVRequiredPersonalizationOptionBackDeploy
+ _OBJC_METACLASS_$_UARPAssetTagBackDeploy
+ _OBJC_METACLASS_$_UARPAssetVersionBackDeploy
+ _OBJC_METACLASS_$_UARPMetaDataTLV16BackDeploy
+ _OBJC_METACLASS_$_UARPMetaDataTLV32BackDeploy
+ _OBJC_METACLASS_$_UARPMetaDataTLV64BackDeploy
+ _OBJC_METACLASS_$_UARPMetaDataTLV8BackDeploy
+ _OBJC_METACLASS_$_UARPMetaDataTLVBackDeploy
+ _OBJC_METACLASS_$_UARPMetaDataTLVDataBackDeploy
+ _OBJC_METACLASS_$_UARPMetaDataTLVStringBackDeploy
+ _OBJC_METACLASS_$_UARPSuperBinaryBackDeploy
+ _OBJC_METACLASS_$_UARPSuperBinaryPayloadBackDeploy
+ _OBJC_METACLASS_$_UARPTLVHostPersonalizationRequiredBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationBoardIDBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationChipEpochBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationChipIDBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationChipRevisionBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationECIDBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationECIDDataBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationEnableMixMatchBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationFTABPayloadBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationFTABSubfileDigestBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationFTABSubfileDigestFilenameBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationFTABSubfileEPROBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationFTABSubfileESECBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationFTABSubfileHashAlgorithmBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationFTABSubfileLongnameBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationFTABSubfileTagBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationFTABSubfileTrustedBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationLifeBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationLogicalUnitNumberBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationManifestEpochBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationManifestPrefixBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationManifestSuffixBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationNonceBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationNonceHashBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationPayloadTagBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationPrefixNeedsLogicalUnitNumberBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationProductionModeBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationProvisioningBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationRequiredBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationSecurityDomainBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationSecurityModeBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationSoCLiveNonceBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationSuffixNeedsLogicalUnitNumberBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationSuperBinaryAssetIDBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationSuperBinaryPayloadIndexBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizationTicketNeedsLogicalUnitNumberBackDeploy
+ _OBJC_METACLASS_$_UARPTLVPersonalizedManifestBackDeploy
+ _OBJC_METACLASS_$_UARPTLVRequiredPersonalizationOptionBackDeploy
+ _UARPPersonalizationTSSRequestWithSigningServer
+ _UARPPersonalizationTSSRequestWithSigningServerSSO
+ __closeNotificationPort
+ __notificationPort
+ __notificationQueue
+ __os_log_default
+ _calloc
+ _dispatch_async
+ _dispatch_get_global_queue
+ _dispatch_queue_create
+ _dispatch_sync_f
+ _kAMAuthInstallTagApOSReleaseType
+ _kAMAuthInstallTagApTarget
+ _kATCRTSuperBinaryTagRTKitOSString
+ _kATCRTSuperBinaryTagRestoreRTKitOSString
+ _kIOMainPortDefault
+ _kUARPDefaultPersonalizationServer
+ _kUARPStringMetadataRootAppleName
+ _kUARPStringMetadataRootAppleValue
+ _kUARPStringPersonalizationOptionBoardID
+ _kUARPStringPersonalizationOptionChipID
+ _kUARPStringPersonalizationOptionDigest
+ _kUARPStringPersonalizationOptionECID
+ _kUARPStringPersonalizationOptionEPRO
+ _kUARPStringPersonalizationOptionESEC
+ _kUARPStringPersonalizationOptionLife
+ _kUARPStringPersonalizationOptionManifestEpoch
+ _kUARPStringPersonalizationOptionNonce
+ _kUARPStringPersonalizationOptionProductionMode
+ _kUARPStringPersonalizationOptionProvisioning
+ _kUARPStringPersonalizationOptionSecurityDomain
+ _kUARPStringPersonalizationOptionSecurityMode
+ _kUARPStringPersonalizationOptionTrusted
+ _lz4_decode_asm
+ _lz4_encode_2gb
+ _lzfse_decode_literals
+ _lzfse_decode_lmd
+ _lzvn_decode_buffer
+ _malloc
+ _objc_destroyWeak
+ _objc_loadWeakRetained
+ _objc_storeWeak
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _realloc
+ _uarpHtonl
+ _uarpHtonll
+ _uarpHtons
+ _uarpNtohl
+ _uarpNtohll
+ _uarpNtohs
+ _uarpPayloadHeaderEndianSwap
+ _uarpPayloadTagPack
+ _uarpSuperBinaryHeaderEndianSwap
- ___strncpy_chk
- _malloc_type_realloc
- _sleep
CStrings:
+ "\x01"
+ "\x01\x14\x11\x13$\x11"
+ "\tFirmware bundle path: %@\n"
+ "\tFirmware path suffix: %@\n"
+ "\x11"
+ "\x11\x11\x19\x12\x112"
+ "        <%@>\r"
+ "    >"
+ " <AppleConnect>"
+ "%@.plist"
+ "%c%c%c%c"
+ "%lu.%lu.%lu.%lu"
+ "%s: _AMAuthInstallSsoSUSSOCopyToken failed"
+ "%s: _AMAuthInstallSsoSUSSOCopyToken is NULL"
+ "%s: _AMAuthInstallSsoSUSSOCopyToken returned without ssodata"
+ "**Unknown**"
+ ",%@"
+ ",%lu"
+ ",Ticket"
+ "/usr/lib/libSoftwareUpdateSSO.dylib"
+ "<%@: \r"
+ "<%@: %@>"
+ "<%@: %u>"
+ "<%@: 0x%016llx>"
+ "<%@: 0x%02x>"
+ "<%@: 0x%08x>"
+ "<Type = 0x%08x, Length = 0x%08x>"
+ "@\"<UARPSuperBinaryDelegate>\""
+ "@\"NSMutableString\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"UARPAssetTagBackDeploy\""
+ "@\"UARPAssetVersionBackDeploy\""
+ "@20@0:8C16"
+ "@20@0:8S16"
+ "@24@0:8@?16"
+ "@24@0:8@?<v@?@\"NSError\">16"
+ "@24@0:8I16C20"
+ "@24@0:8I16I20"
+ "@24@0:8I16S20"
+ "@24@0:8Q16"
+ "@28@0:8I16@20"
+ "@28@0:8I16Q20"
+ "@28@0:8Q16B24"
+ "@32@0:8@16Q24"
+ "@32@0:8I16I20^v24"
+ "@32@0:8Q16Q24"
+ "@32@0:8Q16^v24"
+ "@32@0:8c16c20c24c28"
+ "@36@0:8Q16@24B32"
+ "@40@0:8@16@24@32"
+ "@48@0:8Q16Q24Q32Q40"
+ "Ap,OSReleaseType"
+ "Ap,Target"
+ "B24@0:8^{UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}16"
+ "B24@0:8^{UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}16"
+ "B32@0:8Q16@24"
+ "B36@0:8@16B24^@28"
+ "C16@0:8"
+ "Data was : %.*s"
+ "FIRM"
+ "FPGAValidateFirmwareTimeout"
+ "FPGAValidateFirmwareTimeout expects an integer!"
+ "FPGAValidateRamdiskTimeout"
+ "FPGAValidateRamdiskTimeout expects an integer!"
+ "Failed to locate FTAB in super binary"
+ "Failed to locate rkos file in super binary ftab"
+ "Failed to locate rrko file in super binary"
+ "Failed to parse FTAB in super binary"
+ "Failed to parse firmware data"
+ "Host Personalization Required"
+ "Host Personalization not required for payload %@"
+ "IOGeneralInterest"
+ "Life"
+ "ManifestEpoch"
+ "NSXPCProxyCreating"
+ "Name"
+ "No cphy data found"
+ "Payload - 4cc <%@> - Version <%@> - TLVs - %@"
+ "Personalization Board ID"
+ "Personalization Chip Epoch"
+ "Personalization Chip ID"
+ "Personalization Chip Revision"
+ "Personalization ECID"
+ "Personalization ECID Data"
+ "Personalization Enable Mix Match"
+ "Personalization FTAB Payload"
+ "Personalization FTAB Payload Longname"
+ "Personalization FTAB Payload Production Mode"
+ "Personalization FTAB Payload Security Mode"
+ "Personalization FTAB Payload Tag"
+ "Personalization FTAB Payload Trusted"
+ "Personalization Life"
+ "Personalization Manifest Epoch"
+ "Personalization Manifest Prefix"
+ "Personalization Manifest Suffix"
+ "Personalization Nonce"
+ "Personalization Nonce Hash"
+ "Personalization Payload Tag"
+ "Personalization Prefix Needs Logical Unit Number"
+ "Personalization Production Mode"
+ "Personalization Provisioning"
+ "Personalization Required"
+ "Personalization Security Domain"
+ "Personalization Security Mode"
+ "Personalization SoC Live Nonce"
+ "Personalization Suffix Needs Logical Unit Number"
+ "Personalization SuperBinary AssetID"
+ "Personalization SuperBinary Payload Index"
+ "Personalization Ticket Needs Logical Unit Number"
+ "Personalized Manifest"
+ "Personalizing %@"
+ "ProductionMode"
+ "Provisioning"
+ "RRKO"
+ "RTKit"
+ "Required Personalization Option"
+ "S16@0:8"
+ "Sending commands by pipe with timeouts isn't supported! If a timeout was supplied, it'll be ignored."
+ "SoftwareUpdateSSO dylib found"
+ "SoftwareUpdateSSO dylib not found"
+ "T@\"NSArray\",R,V_measurements"
+ "T@\"NSArray\",R,V_payloads"
+ "T@\"NSArray\",R,V_tlvs"
+ "T@\"NSData\",&,V_ecidData"
+ "T@\"NSData\",&,V_manifest"
+ "T@\"NSData\",&,V_nonce"
+ "T@\"NSData\",R"
+ "T@\"NSData\",R,V_digest"
+ "T@\"NSData\",R,V_ecID"
+ "T@\"NSData\",R,V_metaData"
+ "T@\"NSData\",R,V_nonceHash"
+ "T@\"NSData\",R,V_payloadData"
+ "T@\"NSDictionary\",R,V_tssRequest"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,V_filename"
+ "T@\"NSString\",R,V_longname"
+ "T@\"NSString\",R,V_manifestSuffix"
+ "T@\"NSString\",R,V_ticketPrefix"
+ "T@\"UARPAssetTagBackDeploy\",R,V_tag"
+ "T@\"UARPAssetVersionBackDeploy\",R,V_version"
+ "TB,R,V_needsHostPersonalization"
+ "TB,V_provisioning"
+ "TC,R,V_enableMixMatch"
+ "TC,R,V_isRequired"
+ "TC,R,V_life"
+ "TC,R,V_liveNonce"
+ "TC,R,V_manifestEpoch"
+ "TC,R,V_prefixNeedsLogicalUnitNumber"
+ "TC,R,V_provisioning"
+ "TC,R,V_suffixNeedsLogicalUnitNumber"
+ "TC,R,V_ticketNeedsLogicalUnitNumber"
+ "TC,V_life"
+ "TC,V_manifestEpoch"
+ "TC,V_productionMode"
+ "TC,V_securityDomain"
+ "TC,V_securityMode"
+ "TI,R,V_chipEpoch"
+ "TI,R,V_chipRevision"
+ "TI,R,V_isRequired"
+ "TI,R,V_logicalUnitNumber"
+ "TI,R,V_payloadIndex"
+ "TI,R,V_productionMode"
+ "TI,R,V_securityMode"
+ "TI,R,V_tag"
+ "TI,R,V_tlvLength"
+ "TI,R,V_tlvType"
+ "TI,R,V_tssOption"
+ "TI,V_boardID"
+ "TI,V_chipID"
+ "TQ,R,V_buildVersion"
+ "TQ,R,V_ecID"
+ "TQ,R,V_majorVersion"
+ "TQ,R,V_minorVersion"
+ "TQ,R,V_releaseVersion"
+ "TQ,R,V_totalBytesRequested"
+ "TQ,R,V_totalLength"
+ "TQ,V_ecID"
+ "TS,R,V_assetID"
+ "TS,R,V_epro"
+ "TS,R,V_esec"
+ "TS,R,V_hashAlgorithm"
+ "TS,R,V_trusted"
+ "TSS Request Options for payload %@"
+ "T^v,V_layer2Context"
+ "Tc,R,V_char1"
+ "Tc,R,V_char2"
+ "Tc,R,V_char3"
+ "Tc,R,V_char4"
+ "Timer,AppleTypeCPhyFirmware,%u"
+ "UARP: %@"
+ "UARP: Failed personalization response, error = %u"
+ "UARP: Failed to create authinstall reference"
+ "UARP: Failed to set signing server"
+ "UARP: Personalization Message >> %s"
+ "UARP: TSS Request %@%@ is "
+ "UARP: TSS Request failed customer path / auth listed"
+ "UARP: TSS Request failed sso modes"
+ "UARP: TSS Request to server %@ with SSO and options %@"
+ "UARP: TSS Request to server %@ with options %@"
+ "UARP: TSS Response %@%@ is "
+ "UARP: TSS request to signing server %@"
+ "UARPAssetTagBackDeploy"
+ "UARPAssetVersionBackDeploy"
+ "UARPMetaDataTLV16BackDeploy"
+ "UARPMetaDataTLV32BackDeploy"
+ "UARPMetaDataTLV64BackDeploy"
+ "UARPMetaDataTLV8BackDeploy"
+ "UARPMetaDataTLVBackDeploy"
+ "UARPMetaDataTLVDataBackDeploy"
+ "UARPMetaDataTLVStringBackDeploy"
+ "UARPSuperBinaryBackDeploy"
+ "UARPSuperBinaryPayloadBackDeploy"
+ "UARPTLVHostPersonalizationRequiredBackDeploy"
+ "UARPTLVPersonalizationBoardIDBackDeploy"
+ "UARPTLVPersonalizationChipEpochBackDeploy"
+ "UARPTLVPersonalizationChipIDBackDeploy"
+ "UARPTLVPersonalizationChipRevisionBackDeploy"
+ "UARPTLVPersonalizationECIDBackDeploy"
+ "UARPTLVPersonalizationECIDDataBackDeploy"
+ "UARPTLVPersonalizationEnableMixMatchBackDeploy"
+ "UARPTLVPersonalizationFTABPayloadBackDeploy"
+ "UARPTLVPersonalizationFTABSubfileDigestBackDeploy"
+ "UARPTLVPersonalizationFTABSubfileDigestFilenameBackDeploy"
+ "UARPTLVPersonalizationFTABSubfileEPROBackDeploy"
+ "UARPTLVPersonalizationFTABSubfileESECBackDeploy"
+ "UARPTLVPersonalizationFTABSubfileHashAlgorithmBackDeploy"
+ "UARPTLVPersonalizationFTABSubfileLongnameBackDeploy"
+ "UARPTLVPersonalizationFTABSubfileTagBackDeploy"
+ "UARPTLVPersonalizationFTABSubfileTrustedBackDeploy"
+ "UARPTLVPersonalizationLifeBackDeploy"
+ "UARPTLVPersonalizationLogicalUnitNumberBackDeploy"
+ "UARPTLVPersonalizationManifestEpochBackDeploy"
+ "UARPTLVPersonalizationManifestPrefixBackDeploy"
+ "UARPTLVPersonalizationManifestSuffixBackDeploy"
+ "UARPTLVPersonalizationNonceBackDeploy"
+ "UARPTLVPersonalizationNonceHashBackDeploy"
+ "UARPTLVPersonalizationPayloadTagBackDeploy"
+ "UARPTLVPersonalizationPrefixNeedsLogicalUnitNumberBackDeploy"
+ "UARPTLVPersonalizationProductionModeBackDeploy"
+ "UARPTLVPersonalizationProvisioningBackDeploy"
+ "UARPTLVPersonalizationRequiredBackDeploy"
+ "UARPTLVPersonalizationSecurityDomainBackDeploy"
+ "UARPTLVPersonalizationSecurityModeBackDeploy"
+ "UARPTLVPersonalizationSoCLiveNonceBackDeploy"
+ "UARPTLVPersonalizationSuffixNeedsLogicalUnitNumberBackDeploy"
+ "UARPTLVPersonalizationSuperBinaryAssetIDBackDeploy"
+ "UARPTLVPersonalizationSuperBinaryPayloadIndexBackDeploy"
+ "UARPTLVPersonalizationTicketNeedsLogicalUnitNumberBackDeploy"
+ "UARPTLVPersonalizedManifestBackDeploy"
+ "UARPTLVRequiredPersonalizationOptionBackDeploy"
+ "URLWithString:"
+ "UsbExclusiveOwner"
+ "Value"
+ "^v16@0:8"
+ "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}I{uarpAssetCoreObj=SS{UARP4ccTag=CCCC}{UARPVersion=IIII}IIS}CC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI{UARPPayloadHeader=II{UARPVersion=IIII}IIII}C{UARP4ccTag=CCCC}[4C]S}^{uarpProcessedPayloadObj}*IC*IC*II^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}CCIIIS}"
+ "_AMAuthInstallSsoCopyTicketUsingSUSSO"
+ "_AMAuthInstallSsoCopyTicketUsingSUSSO successfully acquired ssoData"
+ "_AMAuthInstallSsoSUSSOInit"
+ "_asset"
+ "_assetID"
+ "_buildVersion"
+ "_char1"
+ "_char2"
+ "_char3"
+ "_char4"
+ "_chipEpoch"
+ "_chipRevision"
+ "_cphyData"
+ "_delegateQueue"
+ "_digest"
+ "_ecID"
+ "_ecidData"
+ "_enableMixMatch"
+ "_epro"
+ "_esec"
+ "_filename"
+ "_formatVersion"
+ "_hashAlgorithm"
+ "_isRequired"
+ "_keyManifest"
+ "_layer2Context"
+ "_life"
+ "_liveNonce"
+ "_logicalUnitNumber"
+ "_longname"
+ "_majorVersion"
+ "_manifestEpoch"
+ "_manifestSuffix"
+ "_measurements"
+ "_metaData"
+ "_minorVersion"
+ "_needsHostPersonalization"
+ "_nonceHash"
+ "_payloadData"
+ "_payloadIndex"
+ "_payloads"
+ "_prefixNeedsLogicalUnitNumber"
+ "_prefixNeedsUnitNumber"
+ "_productionMode"
+ "_provisioning"
+ "_releaseVersion"
+ "_rkosData"
+ "_rrkoData"
+ "_subfiles"
+ "_suffixNeedsLogicalUnitNumber"
+ "_suffixNeedsUnitNumber"
+ "_tatsuMeasurements"
+ "_ticketNeedsLogicalUnitNumber"
+ "_ticketNeedsUnitNumber"
+ "_ticketPrefix"
+ "_ticketSuffix"
+ "_tlvLength"
+ "_tlvType"
+ "_tlvValue"
+ "_tlvs"
+ "_totalBytesRequested"
+ "_totalLength"
+ "_trimmedTlvs"
+ "_trusted"
+ "_tssOption"
+ "_tssRequest"
+ "_uinitNumber"
+ "_version"
+ "addSubfile:tag:"
+ "appendData:"
+ "assetID"
+ "buildVersion"
+ "c"
+ "c16@0:8"
+ "caseInsensitiveCompare:"
+ "char1"
+ "char2"
+ "char3"
+ "char4"
+ "chipEpoch"
+ "chipRevision"
+ "com.apple.MobileDevice.USBCloseNotification.queue"
+ "com.apple.accessoryupdater.uarp"
+ "componentsSeparatedByString:"
+ "composeTSSRequest:"
+ "composeTSSRequest:asMeasurement:"
+ "copyPersonalizationSSOToken"
+ "copyPersonalizationSSOToken symbol not found"
+ "cphy"
+ "dataWithContentsOfFile:"
+ "dataWithContentsOfURL:"
+ "decodeBytesForKey:returnedLength:"
+ "decodeCharForKey:key:"
+ "decodeObjectOfClass:forKey:"
+ "deviceOpenResult"
+ "digest"
+ "doesNotRecognizeSelector:"
+ "ecID"
+ "ecidData"
+ "enableMixMatch"
+ "encodeBytes:length:forKey:"
+ "epro"
+ "error opening USB device failed with kIOReturnExclusiveAccess. Current owner: %@"
+ "error opening USB device in the background: 0x%x"
+ "error opening USB device: 0x%x"
+ "error scheduling USB device notification: 0x%x"
+ "esec"
+ "expandMetaData:"
+ "expandSuperBinary"
+ "expandTLVs"
+ "failed to get a ticket using SUSSO, status:%d, error:%@"
+ "fileURLWithPath:isDirectory:relativeToURL:"
+ "filename"
+ "freeDeviceNotifications"
+ "generateHashForData:"
+ "generatePersonalizedSuperBinary"
+ "generatePersonalizedSuperBinaryInternal:"
+ "generatePersonalizedSuperBinaryWithoutRRKO"
+ "generateTLV"
+ "generateTLV:tlvValue:"
+ "generateTatsuMeasurements:"
+ "generateTatsuMeasurements:relativeURL:"
+ "generateTatsuMeasurementsPerPayload:"
+ "getBytes:range:"
+ "getDataBlock:offset:"
+ "getManifest"
+ "getMeasurements"
+ "getNeedsHostPersonalization"
+ "getPayloads"
+ "getTlvs"
+ "getTssRequest"
+ "handleUSBDeviceGeneralInterestNotification:"
+ "hashAlgorithm"
+ "https://gs.apple.com:443"
+ "initWithBVERString:"
+ "initWithChar1:char2:char3:char4:"
+ "initWithData:delegate:delegateQueue:"
+ "initWithData:metaData:tag:version:"
+ "initWithFilePath:delegate:delegateQueue:"
+ "initWithMajorVersion:minorVersion:releaseVersion:buildVersion:"
+ "initWithString:"
+ "initWithType:length:value:"
+ "initWithURL:delegate:delegateQueue:"
+ "initWithVersionString:"
+ "integerValue"
+ "isRequired"
+ "isValid"
+ "lastPathComponent"
+ "layer2Context"
+ "libauthinstall_device-973.100.10"
+ "life"
+ "liveNonce"
+ "logicalUnitNumber"
+ "longLongValue"
+ "longname"
+ "majorVersion"
+ "manifestEpoch"
+ "manifestSuffix"
+ "measurements"
+ "metaData"
+ "metaDataTable"
+ "metaDataTableEntry"
+ "minorVersion"
+ "needsHostPersonalization"
+ "nonceHash"
+ "numberWithUnsignedInteger:"
+ "numberWithUnsignedLong:"
+ "objectAtIndex:"
+ "objectAtIndexedSubscript:"
+ "payloadData"
+ "payloadIndex"
+ "payloadWith4ccTag:"
+ "payloads"
+ "payloadsWithout4ccTag:"
+ "personalization"
+ "personalizeSuperBinary:signingServer:ssoOnly:"
+ "personalizedData"
+ "personalizedMetaData"
+ "prefixNeedsLogicalUnitNumber"
+ "preparePayload:"
+ "printDeviceWithExclusiveAccess"
+ "processMeasurementsForTSSOptions:unitNumber:asMeasurement:"
+ "processTLVsForPersonalization"
+ "productionMode"
+ "provisioning"
+ "queryTatsuSigningServer:ssoOnly:error:"
+ "r*32@0:8@16@24"
+ "releaseVersion"
+ "remoteObjectProxy"
+ "remoteObjectProxyWithErrorHandler:"
+ "removeAllObjects"
+ "removeSubfile:tag:"
+ "requiredTSSOptions"
+ "setAssetID:"
+ "setBootNonce:"
+ "setChipEpoch:"
+ "setChipRevision:"
+ "setDigest:"
+ "setEcID:"
+ "setEcidData:"
+ "setEnableMixMatch:"
+ "setEpro:"
+ "setEsec:"
+ "setFilename:"
+ "setHashAlgorithm:"
+ "setIsRequired:"
+ "setLayer2Context:"
+ "setLife:"
+ "setLiveNonce:"
+ "setLogicalUnitNumber:"
+ "setLongname:"
+ "setManifestEpoch:"
+ "setManifestSuffix:"
+ "setNonce:"
+ "setNonceHash:"
+ "setPayloadIndex:"
+ "setPrefixNeedsLogicalUnitNumber:"
+ "setProductionMode:"
+ "setProvisioning:"
+ "setSecurityDomain:"
+ "setSecurityMode:"
+ "setSuffixNeedsLogicalUnitNumber:"
+ "setTLVs:"
+ "setTag:"
+ "setTicketNeedsLogicalUnitNumber:"
+ "setTicketPrefix:"
+ "setTrusted:"
+ "setTssOption:"
+ "ssodata"
+ "stealthMode"
+ "stringByExpandingTildeInPath"
+ "subdataWithRange:"
+ "suffixNeedsLogicalUnitNumber"
+ "superbinary:logString:"
+ "tatsuMeasurements:"
+ "ticketNeedsLogicalUnitNumber"
+ "ticketPrefix"
+ "tlvFromKey:value:"
+ "tlvFromPropertyListValue:"
+ "tlvFromType:length:value:"
+ "tlvLength"
+ "tlvType"
+ "tlvTypeName:"
+ "tlvValue"
+ "tlvValue:"
+ "tlvWithLength:value:"
+ "tlvs"
+ "totalBytesRequested"
+ "totalLength"
+ "trusted"
+ "tssKeyName:unitNumber:"
+ "tssOption"
+ "tssRequest"
+ "tssRequestAsString"
+ "unsignedIntegerValue"
+ "unsignedLongValue"
+ "usbDeviceNotification"
+ "usbService"
+ "v20@0:8B16"
+ "v24@0:8Q16"
+ "v24@0:8^v16"
+ "v36@0:8@16Q24B32"
+ "version"
+ "versionString"
+ "waitForOpenSemaphore"
+ "writeToURL:error:"
- "\tFTAB bundle path: %@\n"
- "\tFTAB path suffix: %@\n"
- "@\"AMRLocalUSBInterface\""
- "Data was : %s"
- "_ftabBundleURL"
- "_ftabPathSuffix"
- "error opening USB device (after retrying): 0x%x - giving up"
- "error opening USB device: 0x%x - will try again"
- "isRemote:"
- "libauthinstall_device-973.60.2"
- "v12@?0B8"
- "v24@0:8@?<v@?B>16"

```
