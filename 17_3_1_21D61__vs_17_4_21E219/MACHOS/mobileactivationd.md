## mobileactivationd

> `/usr/libexec/mobileactivationd`

```diff

-898.60.6.0.0
-  __TEXT.__text: 0x1e9d50
-  __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_stubs: 0x2dc0
-  __TEXT.__objc_methlist: 0x9f4
-  __TEXT.__const: 0x3dc00
-  __TEXT.__cstring: 0xd631
-  __TEXT.__objc_methname: 0x3b6b
-  __TEXT.__oslogstring: 0xe42
+921.100.31.0.0
+  __TEXT.__text: 0x1f5700
+  __TEXT.__auth_stubs: 0x1050
+  __TEXT.__objc_stubs: 0x2de0
+  __TEXT.__objc_methlist: 0x9fc
+  __TEXT.__const: 0x3f9f1
+  __TEXT.__cstring: 0xd8c4
+  __TEXT.__objc_methname: 0x3be7
+  __TEXT.__oslogstring: 0xd6b
   __TEXT.__objc_classname: 0x1a1
   __TEXT.__objc_methtype: 0x1015
-  __TEXT.__gcc_except_tab: 0x1420
+  __TEXT.__gcc_except_tab: 0x142c
   __TEXT.__dlopen_cstrs: 0x25c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xeb0
-  __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__auth_got: 0x830
+  __TEXT.__unwind_info: 0x1274
+  __TEXT.__eh_frame: 0x11d0
+  __DATA_CONST.__auth_got: 0x838
   __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0xd8a8
-  __DATA_CONST.__cfstring: 0xba80
+  __DATA_CONST.__const: 0xde68
+  __DATA_CONST.__cfstring: 0xbd20
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x1e0
-  __DATA_CONST.__objc_arraydata: 0x338
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_intobj: 0x210
+  __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x2248
-  __DATA.__objc_selrefs: 0xd00
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x178
-  __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0xe4
+  __DATA.__objc_const: 0x2278
+  __DATA.__objc_selrefs: 0xd08
+  __DATA.__objc_ivar: 0xe8
   __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x1138
-  __DATA.__bss: 0x4d0
-  __DATA.__common: 0x9f8
+  __DATA.__data: 0x11b0
+  __DATA.__bss: 0x4e8
+  __DATA.__common: 0xa14
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F58509F7-D0CE-32CE-9F39-B4CB9FCFCF36
-  Functions: 1226
-  Symbols:   8795
-  CStrings:  4208
+  UUID: F996D97A-A6F8-3275-AF0C-0BA1B3258929
+  Functions: 1249
+  Symbols:   8895
+  CStrings:  4253
 
Symbols:
+ -[DeviceType device_supports_mfi_certificates]
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ GCC_except_table23
+ OBJC_IVAR_$_DeviceType._device_supports_mfi_certificates
+ _BASepAppRoot
+ _BASepAppRootPublicKey
+ _BASepAppRootSKID
+ _BASepAppRootSPKI
+ _CTEvaluateBAA
+ _CTEvaluateBAASepApp
+ _CTGetBAARootType
+ _CTGetBAASubCAType
+ _MFi4RootSKID
+ _VLxCLgDpiF
+ _X509ExtensionParseCertifiedChipIntermediate
+ _X509PolicyBAASepApp
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.403
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.403.cold.1
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.403.cold.2
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.403.cold.3
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.403.cold.4
+ __58-[MobileActivationDaemon handleSessionResponse:withError:]_block_invoke.148
+ __61-[MobileActivationDaemon recertifyDeviceWithCompletionBlock:]_block_invoke.331
+ __66-[MobileActivationDaemon createActivationInfoWithCompletionBlock:]_block_invoke.269
+ __70-[MobileActivationDaemon copyLegacyDeviceIdentityWithCompletionBlock:]_block_invoke.470
+ __70-[MobileActivationDaemon createTunnel1SessionInfoWithCompletionBlock:]_block_invoke.235
+ __75-[MobileActivationDaemon issueClientCertificateLegacy:WithCompletionBlock:]_block_invoke.353
+ __82-[MobileActivationDaemon createTunnel1ActivationInfo:options:withCompletionBlock:]_block_invoke.197
+ __90-[MobileActivationDaemon copyAttestationDictionaryWithCompletionBlock:options:completion:]_block_invoke.384
+ __94-[MobileActivationDaemon handleActivationInfoWithSession:activationSignature:completionBlock:]_block_invoke.346
+ ___copy_legacy_dcrt_path_block_invoke
+ ___der_key_keybag_class
+ ___der_key_op_create
+ __baa_sep_app_root_public_key
+ __baa_sep_app_root_skid
+ __baa_sep_app_root_spki
+ __baa_system_root_skid
+ __baa_user_root_skid
+ __block_literal_global.159
+ __block_literal_global.197
+ __block_literal_global.223
+ __block_literal_global.299
+ __block_literal_global.302
+ __block_literal_global.325
+ __block_literal_global.334
+ __block_literal_global.342
+ __block_literal_global.349
+ __block_literal_global.511
+ __block_literal_global.537
+ __block_literal_global.542
+ __block_literal_global.548
+ __block_literal_global.553
+ __block_literal_global.84
+ __collection_activity_handler_block_invoke.512
+ __collection_activity_handler_block_invoke.535
+ __collection_activity_handler_block_invoke_2.513
+ __dcrt_oob_activity_handler_block_invoke.499
+ __dcrt_oob_activity_handler_block_invoke.500
+ __dcrt_oob_activity_handler_block_invoke.501
+ __dcrt_oob_activity_handler_block_invoke.502
+ __dcrt_oob_activity_handler_block_invoke.503
+ __dcrt_oob_activity_handler_block_invoke.506
+ __dcrt_oob_activity_handler_block_invoke_2.504
+ __handle_activate_block_invoke.466
+ __issueClientCertificateWithReferenceKey_block_invoke.180
+ __issueClientCertificateWithReferenceKey_block_invoke.297
+ __mfi4_root_skid
+ __register_xpc_activities_block_invoke.757
+ __register_xpc_activities_block_invoke.757.cold.1
+ __register_xpc_activities_block_invoke.758
+ __register_xpc_activities_block_invoke.758.cold.1
+ __register_xpc_activities_block_invoke.759
+ __register_xpc_activities_block_invoke.759.cold.1
+ __register_xpc_activities_block_invoke.760
+ __register_xpc_activities_block_invoke.760.cold.1
+ __register_xpc_activities_block_invoke.761
+ __register_xpc_activities_block_invoke.761.cold.1
+ __register_xpc_activities_block_invoke.762
+ __register_xpc_activities_block_invoke.762.cold.1
+ __register_xpc_activities_block_invoke.763
+ __register_xpc_activities_block_invoke.763.cold.1
+ __register_xpc_activities_block_invoke.764
+ __register_xpc_activities_block_invoke.764.cold.1
+ __ucrt_oob_activity_handler_block_invoke.546
+ __ucrt_oob_activity_handler_block_invoke.549
+ __ucrt_oob_activity_handler_block_invoke.551
+ __ucrt_oob_activity_handler_block_invoke_2.550
+ _aks_ref_key_create
+ _calloc
+ _copy_legacy_dcrt_path
+ _deleteLegacyUIKIfMismatched
+ _der_key_keybag_class
+ _der_key_op_create
+ _device_supports_mfi_certificates
+ _kMAPreDawnDataMigrationCompleted
+ _libaks_ref_key_create
+ _objc_msgSend$device_supports_mfi_certificates
+ _performDCRTMigrationTasks
+ _unnamed_array_storage.331
+ _unnamed_array_storage.336
+ copy_legacy_dcrt_path.onceToken
+ copy_legacy_dcrt_path.retval
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- GCC_except_table22
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.390
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.390.cold.1
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.390.cold.2
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.390.cold.3
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.390.cold.4
- __58-[MobileActivationDaemon handleSessionResponse:withError:]_block_invoke.147
- __61-[MobileActivationDaemon recertifyDeviceWithCompletionBlock:]_block_invoke.330
- __66-[MobileActivationDaemon createActivationInfoWithCompletionBlock:]_block_invoke.268
- __70-[MobileActivationDaemon copyLegacyDeviceIdentityWithCompletionBlock:]_block_invoke.457
- __70-[MobileActivationDaemon createTunnel1SessionInfoWithCompletionBlock:]_block_invoke.234
- __75-[MobileActivationDaemon issueClientCertificateLegacy:WithCompletionBlock:]_block_invoke.352
- __82-[MobileActivationDaemon createTunnel1ActivationInfo:options:withCompletionBlock:]_block_invoke.196
- __90-[MobileActivationDaemon copyAttestationDictionaryWithCompletionBlock:options:completion:]_block_invoke.371
- __94-[MobileActivationDaemon handleActivationInfoWithSession:activationSignature:completionBlock:]_block_invoke.345
- __block_literal_global.156
- __block_literal_global.193
- __block_literal_global.220
- __block_literal_global.278
- __block_literal_global.290
- __block_literal_global.310
- __block_literal_global.316
- __block_literal_global.318
- __block_literal_global.348
- __block_literal_global.502
- __block_literal_global.528
- __block_literal_global.530
- __block_literal_global.533
- __block_literal_global.536
- __collection_activity_handler_block_invoke.503
- __collection_activity_handler_block_invoke.526
- __collection_activity_handler_block_invoke_2.504
- __dcrt_oob_activity_handler_block_invoke.485
- __dcrt_oob_activity_handler_block_invoke.490
- __dcrt_oob_activity_handler_block_invoke.491
- __dcrt_oob_activity_handler_block_invoke.492
- __dcrt_oob_activity_handler_block_invoke.493
- __dcrt_oob_activity_handler_block_invoke.497
- __dcrt_oob_activity_handler_block_invoke_2.495
- __handle_activate_block_invoke.457
- __issueClientCertificateWithReferenceKey_block_invoke.174
- __issueClientCertificateWithReferenceKey_block_invoke.288
- __register_xpc_activities_block_invoke.734
- __register_xpc_activities_block_invoke.734.cold.1
- __register_xpc_activities_block_invoke.735
- __register_xpc_activities_block_invoke.735.cold.1
- __register_xpc_activities_block_invoke.736
- __register_xpc_activities_block_invoke.736.cold.1
- __register_xpc_activities_block_invoke.737
- __register_xpc_activities_block_invoke.737.cold.1
- __register_xpc_activities_block_invoke.738
- __register_xpc_activities_block_invoke.738.cold.1
- __register_xpc_activities_block_invoke.739
- __register_xpc_activities_block_invoke.739.cold.1
- __register_xpc_activities_block_invoke.740
- __register_xpc_activities_block_invoke.740.cold.1
- __register_xpc_activities_block_invoke.741
- __register_xpc_activities_block_invoke.741.cold.1
- __ucrt_oob_activity_handler_block_invoke.531
- __ucrt_oob_activity_handler_block_invoke.534
- __ucrt_oob_activity_handler_block_invoke.537
- __ucrt_oob_activity_handler_block_invoke_2.541
- __ucrt_oob_activity_handler_block_invoke_3.cold.3
- _deleteLegacyUikIfMismatched
- _unnamed_array_storage.307
- _unnamed_array_storage.312
CStrings:
+ "%@ is missing required OID: %@"
+ "%@ not supported on virtual machines."
+ "/private/var/hardware/MobileActivation"
+ "921.100.31"
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-921.100.31 built on Feb 21 2024 at 20:47:27)"
+ "Failed to alloc dictionary."
+ "Failed to copy %@ to %@."
+ "Failed to create SDCRT file path."
+ "Failed to create ref key: 0x%08x"
+ "Failed to delete invalid legacy UIK."
+ "Failed to delete legacy UIK: %@"
+ "Failed to parse DCRT DER cert chain."
+ "Failed to perform DCRT migration task."
+ "Failed to perform system key (%d / %d) collection (options=%lld): 0x%08x"
+ "Legacy UIK purged."
+ "MapsTransactionInsightsExtension"
+ "MobileAssetLibTests-Runner"
+ "Moving DCRT from legacy path to system location."
+ "Passbook"
+ "PreDawnDataMigrationCompleted"
+ "SPREngineIntegrationTests-Runner"
+ "Successfuly moved DCRT to system location."
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,V_device_supports_mfi_certificates"
+ "UCRT not supported on virtual machines."
+ "_device_supports_mfi_certificates"
+ "asutil"
+ "dcrt"
+ "deleteLegacyUIKIfMismatched"
+ "device_supports_mfi_certificates"
+ "financed"
+ "iOS Device Activator (MobileActivation-921.100.31)"
+ "libaks_ref_key_create"
+ "mapspushd"
+ "mobileassetd"
+ "performDCRTMigrationTasks"
+ "perform_dawn_data_migration_tasks"
- "898.60.6"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-898.60.6 built on Dec 20 2023 at 18:40:54)"
- "Failed to check legacy UIK validity."
- "Failed to check system UIK for mismatch (%@)."
- "Failed to delete legacy UIK if mismatched (%@)."
- "Failed to perform system key (%d / %d) collection (options=%d): 0x%08x"
- "Failed to purge mismatched legacy UIK."
- "Legacy UIK on disk mismatches UCRT. Deleting legacy UIK."
- "Purged invalid legacy UIK ahead of UIK healing."
- "System UIK matches UCRT. UIK healing cancelled."
- "deleteLegacyUikIfMismatched"
- "iOS Device Activator (MobileActivation-898.60.6)"
- "s7nuHoZIYNoOHCqT9iyZkQ"

```
