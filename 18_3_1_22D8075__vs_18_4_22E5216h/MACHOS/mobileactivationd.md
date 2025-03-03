## mobileactivationd

> `/usr/libexec/mobileactivationd`

```diff

-1015.60.1.0.0
-  __TEXT.__text: 0x1fdb78
+1017.100.15.0.0
+  __TEXT.__text: 0x1fd7cc
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x2ec0
-  __TEXT.__objc_methlist: 0xa80
+  __TEXT.__objc_stubs: 0x2f20
+  __TEXT.__objc_methlist: 0x1084
   __TEXT.__const: 0x46351
-  __TEXT.__cstring: 0xd7fb
-  __TEXT.__objc_methname: 0x3ce7
+  __TEXT.__cstring: 0xd882
+  __TEXT.__objc_methname: 0x3d4e
   __TEXT.__oslogstring: 0xe5a
   __TEXT.__objc_classname: 0x1b4
   __TEXT.__objc_methtype: 0x102a
-  __TEXT.__gcc_except_tab: 0x198c
+  __TEXT.__gcc_except_tab: 0x1998
   __TEXT.__dlopen_cstrs: 0x24c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1118
-  __TEXT.__eh_frame: 0x1108
+  __TEXT.__unwind_info: 0x1168
+  __TEXT.__eh_frame: 0x1100
   __DATA_CONST.__auth_got: 0x860
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0xdf30
-  __DATA_CONST.__cfstring: 0xc020
+  __DATA_CONST.__got: 0x468
+  __DATA_CONST.__auth_ptr: 0x68
+  __DATA_CONST.__const: 0xdf00
+  __DATA_CONST.__cfstring: 0xc0e0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x258
-  __DATA_CONST.__objc_arraydata: 0x450
+  __DATA_CONST.__objc_arraydata: 0x460
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0x23c8
-  __DATA.__objc_selrefs: 0xd50
+  __DATA.__objc_const: 0x1850
+  __DATA.__objc_selrefs: 0xfe0
   __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x320
-  __DATA.__data: 0x11f8
+  __DATA.__data: 0x11f0
   __DATA.__bss: 0x510
-  __DATA.__common: 0xa10
+  __DATA.__common: 0xa08
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1297
-  Symbols:   9161
-  CStrings:  2804
+  Functions: 1385
+  Symbols:   9613
+  CStrings:  2814
 
Symbols:
+ +[DeviceType sharedInstance].cold.1
+ +[GestaltHlpr getSharedInstance].cold.1
+ +[MALog getSharedInstance].cold.1
+ -[MACollectionInterface copyIngestData:].cold.1
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ GCC_except_table109
+ GCC_except_table133
+ GCC_except_table145
+ GCC_except_table67
+ GCC_except_table98
+ _OBJC_CLASS_$_NSRegularExpression
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___block_descriptor_111_e8_32s40s48s56s64s72s80bs88r96r_e5_v8?0l
+ __block_literal_global.335
+ __block_literal_global.362
+ __block_literal_global.394
+ __block_literal_global.402
+ __block_literal_global.520
+ __block_literal_global.523
+ __block_literal_global.531
+ __block_literal_global.534
+ __block_literal_global.537
+ __block_literal_global.540
+ __block_literal_global.545
+ __collection_activity_handler_block_invoke.521
+ __collection_activity_handler_block_invoke.524
+ __collection_activity_handler_block_invoke.527
+ __collection_activity_handler_block_invoke_2.525
+ __dcrt_oob_activity_handler_block_invoke.511
+ __dcrt_oob_activity_handler_block_invoke.512
+ __dcrt_oob_activity_handler_block_invoke.515
+ __dcrt_oob_activity_handler_block_invoke_2.513
+ __dcrt_oob_load_spreading_activity_handler_block_invoke.503
+ __issueClientCertificateWithReferenceKey_block_invoke.192
+ __register_xpc_activities_block_invoke.762
+ __register_xpc_activities_block_invoke.762.cold.1
+ __register_xpc_activities_block_invoke.763
+ __register_xpc_activities_block_invoke.763.cold.1
+ __ucrt_oob_activity_handler_block_invoke.532
+ __ucrt_oob_activity_handler_block_invoke.535
+ __ucrt_oob_activity_handler_block_invoke.538
+ __ucrt_oob_activity_handler_block_invoke.543
+ __ucrt_oob_activity_handler_block_invoke_2.542
+ _clientNameSuffixIsValid
+ _createBAAClientName
+ _createUserAgentValue
+ _is_factory_activated
+ _kMAOptionsBAAClientNameSuffix
+ _merge_dict_cb.cold.1
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$stringByAppendingFormat:
+ copyLoggingHandle.cold.1
+ copyMobileActivationSerialQueue.cold.1
+ copyRTCResetSerialQueue.cold.1
+ copySignpostLoggingHandle.cold.1
+ copySplunkQueue.cold.1
+ copySplunkUUIDQueue.cold.1
+ copy_activation_records_directory_path.cold.1
+ copy_data_ark_directory_path.cold.1
+ copy_dcrt_path.cold.1
+ copy_legacy_dcrt_path.cold.1
+ copy_log_directory_path.cold.1
+ copy_regulatory_images_directory_path.cold.1
+ copy_software_update_log_directory_path.cold.1
+ copy_software_update_splunk_directory_path.cold.1
+ copy_software_update_ucrt_directory_path.cold.1
+ copy_splunk_directory_path.cold.1
+ copy_suinfo_directory_path.cold.1
+ copy_system_container_path.cold.1
+ copy_ucrt_path.cold.1
+ copy_uik_path.cold.1
+ create_cert_request.cold.1
+ data_migration_supported.cold.1
+ der_key_validate.cold.1
+ der_key_validate.cold.2
+ get_aks_client_connection.cold.1
+ isRunningInDiagnosticsMode.cold.1
+ isSupportedActivationLockClient.cold.2
+ isSupportedDeviceIdentityClient.cold.2
+ isSupportedRecoveryLogClient.cold.1
+ is_erase_installed_build.cold.1
+ is_upgrade_installed_build.cold.1
+ lockcrypto_query_certificate_properties.cold.1
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/00dbf134-ba8e-11ef-af9a-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- GCC_except_table110
- GCC_except_table134
- GCC_except_table146
- GCC_except_table68
- GCC_except_table81
- GCC_except_table99
- ___block_descriptor_103_e8_32s40s48s56s64s72bs80r88r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72b80r88r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80r88r
- __block_literal_global.333
- __block_literal_global.359
- __block_literal_global.391
- __block_literal_global.399
- __block_literal_global.518
- __block_literal_global.521
- __block_literal_global.527
- __block_literal_global.532
- __block_literal_global.535
- __block_literal_global.538
- __block_literal_global.543
- __collection_activity_handler_block_invoke.519
- __collection_activity_handler_block_invoke.522
- __collection_activity_handler_block_invoke.525
- __collection_activity_handler_block_invoke_2.523
- __dcrt_oob_activity_handler_block_invoke.504
- __dcrt_oob_activity_handler_block_invoke.507
- __dcrt_oob_activity_handler_block_invoke.513
- __dcrt_oob_activity_handler_block_invoke_2.511
- __dcrt_oob_load_spreading_activity_handler_block_invoke.501
- __issueClientCertificateWithReferenceKey_block_invoke.189
- __register_xpc_activities_block_invoke.753
- __register_xpc_activities_block_invoke.753.cold.1
- __register_xpc_activities_block_invoke.754
- __register_xpc_activities_block_invoke.754.cold.1
- __ucrt_oob_activity_handler_block_invoke.530
- __ucrt_oob_activity_handler_block_invoke.533
- __ucrt_oob_activity_handler_block_invoke.536
- __ucrt_oob_activity_handler_block_invoke.539
- __ucrt_oob_activity_handler_block_invoke_2.540
CStrings:
+ "#%@"
+ "1017.100.15"
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-1017.100.15 built on Feb 25 2025 at 21:28:01)"
+ "BAAClientNameSuffix"
+ "Failed to create regex."
+ "Invalid type for option %@"
+ "^[A-Za-z0-9_-]{0,64}$"
+ "clientNameSuffixIsValid"
+ "firstMatchInString:options:range:"
+ "iOS Device Activator (MobileActivation-1017.100.15)"
+ "imagent"
+ "regularExpressionWithPattern:options:error:"
+ "stringByAppendingFormat:"
- "1015.60.1"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-1015.60.1 built on Dec 14 2024 at 21:38:24)"
- "iOS Device Activator (MobileActivation-1015.60.1)"

```
