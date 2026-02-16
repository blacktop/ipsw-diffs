## AppleKeyStore

> `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore`

```diff

-2155.80.2.0.0
-  __TEXT.__text: 0x57960
-  __TEXT.__auth_stubs: 0x16b0
-  __TEXT.__const: 0xa698
-  __TEXT.__cstring: 0x2f63
-  __TEXT.__oslogstring: 0xf94
+2155.100.111.0.1
+  __TEXT.__text: 0x58ed8
+  __TEXT.__auth_stubs: 0x1760
+  __TEXT.__const: 0xaea8
+  __TEXT.__cstring: 0x3203
+  __TEXT.__oslogstring: 0x1639
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__constg_swiftt: 0x730
-  __TEXT.__swift5_typeref: 0x6b8
-  __TEXT.__swift5_reflstr: 0x83d
-  __TEXT.__swift5_fieldmd: 0xdb0
-  __TEXT.__swift5_types: 0xa0
+  __TEXT.__constg_swiftt: 0x864
+  __TEXT.__swift5_typeref: 0x76e
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0xaa8
+  __TEXT.__swift5_fieldmd: 0x114c
+  __TEXT.__swift5_types: 0xc4
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x2ec
+  __TEXT.__swift5_proto: 0x334
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__swift5_assocty: 0x3d8
-  __TEXT.__unwind_info: 0x1550
-  __TEXT.__eh_frame: 0x1958
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x5c28
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__swift5_assocty: 0x4b0
+  __TEXT.__unwind_info: 0x1618
+  __TEXT.__eh_frame: 0x1b30
+  __TEXT.__objc_classname: 0xbd
+  __TEXT.__objc_methname: 0x46
+  __TEXT.__objc_methtype: 0x1
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x5c80
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0xb58
-  __AUTH_CONST.__const: 0x1f88
-  __AUTH_CONST.__cfstring: 0x600
-  __AUTH_CONST.__objc_const: 0x268
-  __AUTH.__data: 0x480
-  __DATA.__data: 0x1368
+  __AUTH_CONST.__auth_got: 0xbb0
+  __AUTH_CONST.__const: 0x2428
+  __AUTH_CONST.__cfstring: 0x760
+  __AUTH_CONST.__objc_const: 0x340
+  __AUTH.__data: 0x530
+  __DATA.__data: 0x1280
   __DATA.__common: 0x8a0
-  __DATA.__bss: 0x5b10
+  __DATA.__bss: 0x6410
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B17B52A1-DE11-3A89-A495-D54F13C48D7A
-  Functions: 2535
-  Symbols:   3677
-  CStrings:  728
+  UUID: 6C6F1D09-B35F-319A-A0F5-A16DAD239FF5
+  Functions: 2700
+  Symbols:   3920
+  CStrings:  801
 
Symbols:
+ _AKSIdentityAddNTLMVerifier
+ _AKSIdentityAddSRPVerifier
+ _AKSIdentityCreateKeybag
+ _AKSIdentityCreateKeybagWithHash
+ _AKSIdentityDeleteNTLMVerifier
+ _AKSIdentityDeleteSRPVerifier
+ _AKSIdentityImportNTLMVerifier
+ _AKSIdentityImportSRPVerifier
+ _AKSIdentityNTLMDone
+ _AKSIdentityNTLMInit
+ _AKSIdentityNTLMStart
+ _AKSIdentityNTLMVerify
+ _AKSIdentityProperties
+ _AKSIdentitySRPDone
+ _AKSIdentitySRPInit
+ _AKSIdentitySRPStart
+ _AKSIdentitySRPVerify
+ _APFSVolumeRoleFind
+ _CMSAttributeParseAppleHashAgilityV2
+ _CMSGetCertificateUsingIssuerSerialNumber
+ _CMSParseEncapsulatedContent
+ _CMSParseSignedData
+ _CTConvertAsciiHexToUint64
+ _IOIteratorNext
+ _IORegistryEntryGetChildEntry
+ _IORegistryEntryGetChildIterator
+ __DATA__TtCV13AppleKeyStore16AKSAttestContext20AttestationContainer
+ __IVARS__TtCV13AppleKeyStore16AKSAttestContext20AttestationContainer
+ __METACLASS_DATA__TtCV13AppleKeyStore16AKSAttestContext20AttestationContainer
+ ___block_descriptor_tmp.41
+ ___block_descriptor_tmp.43
+ ___block_descriptor_tmp.48
+ ___der_key_keybag_type
+ ___swift_assignWithCopy_strong
+ ___swift_assignWithTake_strong
+ ___swift_destroy_strong
+ ___swift_initWithCopy_strong
+ ___swift_memcpy86_1
+ __os_log_error_impl
+ _aksNotificationCB.cold.1
+ _aks_apfs_container_disk_for_physical_device
+ _aks_apfs_container_disk_for_physical_device.cold.1
+ _aks_apfs_container_disk_for_physical_device.cold.2
+ _aks_apfs_container_disk_for_physical_device.cold.3
+ _aks_apfs_preboot_disk
+ _aks_apfs_preboot_disk.cold.1
+ _aks_apfs_preboot_disk.cold.2
+ _aks_apfs_preboot_disk.cold.3
+ _aks_apfs_preboot_disk.cold.4
+ _aks_apfs_preboot_disk.cold.5
+ _aks_apfs_preboot_mount_point
+ _aks_apfs_preboot_mount_point.cold.1
+ _aks_apfs_preboot_mount_point.cold.2
+ _aks_apfs_preboot_mount_point.cold.3
+ _aks_apfs_preboot_mount_point.cold.4
+ _aks_apfs_preboot_mount_point.cold.5
+ _aks_apfs_preboot_mount_point.cold.6
+ _aks_apfs_preboot_volume_path
+ _aks_apfs_preboot_volume_path.cold.1
+ _aks_apfs_preboot_volume_path.cold.2
+ _aks_apfs_preboot_volume_path.cold.3
+ _aks_apfs_preboot_volume_path.cold.4
+ _aks_apfs_preboot_volume_path.cold.5
+ _aks_do_mount_apfs
+ _aks_do_spawn
+ _aks_do_umount
+ _akstest_check_class.cold.1
+ _akstest_last_user.cold.1
+ _akstest_new_ek.cold.1
+ _akstest_new_ekwk.cold.1
+ _akstest_new_ekwk.cold.2
+ _akstest_new_ekwk.cold.3
+ _akstest_new_key.cold.1
+ _akstest_new_key.cold.2
+ _akstest_new_key.cold.3
+ _akstest_rewrap_ek.cold.1
+ _akstest_rewrap_ek.cold.2
+ _akstest_unwrap_ek.cold.1
+ _akstest_unwrap_ek.cold.2
+ _akstest_unwrap_key.cold.1
+ _akstest_unwrap_key.cold.2
+ _associated conformance 13AppleKeyStore06AKSRefB12AccessDomainOSHAASQ
+ _associated conformance 13AppleKeyStore06AKSRefB12AccessDomainOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 13AppleKeyStore14AKSAttestParamOSHAASQ
+ _associated conformance 13AppleKeyStore15AKSAttestOSTypeOSHAASQ
+ _associated conformance 13AppleKeyStore16AKSAttestPurposeOSHAASQ
+ _associated conformance 13AppleKeyStore18AKSSealedHashFlagsVs10SetAlgebraAASQ
+ _associated conformance 13AppleKeyStore18AKSSealedHashFlagsVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 13AppleKeyStore18AKSSealedHashFlagsVs9OptionSetAASY
+ _associated conformance 13AppleKeyStore18AKSSealedHashFlagsVs9OptionSetAAs0H7Algebra
+ _der_key_keybag_type
+ _get_bsd_name
+ _get_bsd_name.cold.1
+ _get_bsd_name.cold.2
+ _get_bsd_name.cold.3
+ _kAKSIdentityNTLMAuthType_MSCHAPv2
+ _kAKSIdentityNTLMAuthType_NTLMv2
+ _kAKSIdentityNTLMAuthType_SMBNT
+ _kAKSIdentityProperty_HasKEK
+ _kAKSIdentityProperty_HasKerberosSRP
+ _kAKSIdentityProperty_HasKeybag
+ _kAKSIdentityProperty_HasNTLM
+ _kAKSIdentityProperty_HasOTI
+ _kAKSIdentityProperty_HasScreenSharingSRP
+ _kAKSIdentitySRPType_Kerberos
+ _kAKSIdentitySRPType_ScreenSharing
+ _posix_spawn
+ _report_lock_state
+ _report_lock_state.cold.1
+ _swift_getForeignTypeMetadata
+ _swift_retain
+ _symbolic Say_____G 13AppleKeyStore06AKSRefB12AccessDomainO
+ _symbolic Sry_____G s5UInt8V
+ _symbolic _____ 13AppleKeyStore06AKSRefB12AccessDomainO
+ _symbolic _____ 13AppleKeyStore14AKSAttestParamO
+ _symbolic _____ 13AppleKeyStore15AKSAttestOSTypeO
+ _symbolic _____ 13AppleKeyStore16AKSAttestContextV
+ _symbolic _____ 13AppleKeyStore16AKSAttestContextV20AttestationContainerC
+ _symbolic _____ 13AppleKeyStore16AKSAttestPurposeO
+ _symbolic _____ 13AppleKeyStore18AKSSealedHashFlagsV
+ _symbolic _____ 13AppleKeyStore18AKSSealedHashValueV
+ _symbolic _____ So23aks_sealed_hash_value_ta
+ _symbolic _____Sg_ABt 17SwiftASN1Internal0B4NodeV
+ _symbolic ______A19At s5UInt8V
+ _symbolic ______A47At s5UInt8V
+ _type_layout_string 13AppleKeyStore16AKSAttestContextV
+ _type_layout_string 13AppleKeyStore18AKSSealedHashFlagsV
+ _type_layout_string 13AppleKeyStore18AKSSealedHashValueV
+ _type_layout_string So23aks_sealed_hash_value_ta
+ _waitpid
- _AKSIdentityGetOption
- _AKSIdentityOperation
- _AKSIdentityRegisterUnlockToken
- _AKSIdentityRemoteSession
- _AKSIdentitySetOption
- _AKSIdentityUnlockWithToken
- _OUTLINED_FUNCTION_118
- _OUTLINED_FUNCTION_119
- _OUTLINED_FUNCTION_120
- _OUTLINED_FUNCTION_121
- _OUTLINED_FUNCTION_122
- _OUTLINED_FUNCTION_123
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.8
- _aks_apfs_container_disk_for_path.cold.8
- _aks_apfs_container_disk_for_path.cold.9
- _copy_raw_secret
- _decode_ref_key_with_result.cold.1
- _fv_init_cred_from_secret
CStrings:
+ "%s/%s/%s"
+ "%s/%s/%s/%s"
+ "%s/%s/%s/%s%s"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get C string for name%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get C string%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get bsd name for media object%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Did not get a APFS_SCHEME_OBJECT for %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to find preboot volume for disk %s (%d:%s)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to get child for scheme for %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to get container scheme from disk %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to get mount point for preboot %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to get preboot mount point for %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to get uuid for disk %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to spawn %s (rc=%d)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s IOObject %s is not AppleAPFSVolume%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s IOServiceGetMatchingService failed to find %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Invalid number of matches returned (%ld)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s No matches returned%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Returned Preboot volume is not a string%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Truncated path %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unexpected return value for waitpid (rc=%d)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 1)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 3)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n"
+ "-f"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "/sbin/mount_apfs"
+ "/sbin/umount"
+ "AppleAPFSContainerScheme"
+ "_TtCV13AppleKeyStore16AKSAttestContext20AttestationContainer"
+ "aks_apfs_container_disk_for_physical_device"
+ "aks_apfs_preboot_disk"
+ "aks_apfs_preboot_mount_point"
+ "aks_apfs_preboot_volume_path"
+ "aks_do_spawn"
+ "akstest_check_class"
+ "akstest_last_user"
+ "akstest_new_ek"
+ "akstest_new_ekwk"
+ "akstest_new_key"
+ "akstest_rewrap_ek"
+ "akstest_unwrap_ek"
+ "akstest_unwrap_key"
+ "attestationBuffer"
+ "contextBuffer"
+ "failed to create dictionary for handle %d: error:0x%x"
+ "get_bsd_name"
+ "has_kek"
+ "has_kerberos_srp"
+ "has_keybag"
+ "has_ntlm"
+ "has_oti"
+ "has_screensharing_srp"
+ "kerberos_srp"
+ "mount_apfs"
+ "mschapv2"
+ "ntlmv2"
+ "screensharing_srp"
+ "smbnt"
+ "umount"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Container bsd name: %s%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get C string for container%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get container bsd name%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s IOObject %{public}s is not AppleAPFSVolume%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s IOServiceGetMatchingService failed to find %{public}s%s\n"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"

```
