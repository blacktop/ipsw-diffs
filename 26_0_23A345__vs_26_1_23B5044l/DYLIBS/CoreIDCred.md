## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`

```diff

-8.43.1.0.0
-  __TEXT.__text: 0x48c74
+8.104.2.0.0
+  __TEXT.__text: 0x4a6b8
   __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x206c
-  __TEXT.__const: 0x3768
-  __TEXT.__cstring: 0x2046
-  __TEXT.__oslogstring: 0x3a3c
+  __TEXT.__objc_methlist: 0x211c
+  __TEXT.__const: 0x3788
+  __TEXT.__cstring: 0x2066
+  __TEXT.__oslogstring: 0x3f4c
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__constg_swiftt: 0x900
   __TEXT.__swift5_typeref: 0xe70
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x706
-  __TEXT.__swift5_fieldmd: 0x7d8
+  __TEXT.__swift5_reflstr: 0x746
+  __TEXT.__swift5_fieldmd: 0x7f0
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x2cc
   __TEXT.__swift5_types: 0xf4
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift5_capture: 0x590
+  __TEXT.__swift5_capture: 0x5a0
   __TEXT.__swift_as_entry: 0xd8
   __TEXT.__swift_as_ret: 0xf0
-  __TEXT.__unwind_info: 0x1908
-  __TEXT.__eh_frame: 0x2380
+  __TEXT.__unwind_info: 0x1988
+  __TEXT.__eh_frame: 0x23b8
   __TEXT.__objc_classname: 0x2be
-  __TEXT.__objc_methname: 0x41f0
-  __TEXT.__objc_methtype: 0xf08
-  __TEXT.__objc_stubs: 0x1a20
+  __TEXT.__objc_methname: 0x44fb
+  __TEXT.__objc_methtype: 0xfc0
+  __TEXT.__objc_stubs: 0x1ae0
   __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x9f8
+  __DATA_CONST.__const: 0xa20
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc50
+  __DATA_CONST.__objc_selrefs: 0xca8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xb8
   __AUTH_CONST.__auth_got: 0x720
-  __AUTH_CONST.__const: 0x2400
-  __AUTH_CONST.__cfstring: 0x16e0
-  __AUTH_CONST.__objc_const: 0x3768
+  __AUTH_CONST.__const: 0x2450
+  __AUTH_CONST.__cfstring: 0x1760
+  __AUTH_CONST.__objc_const: 0x3780
   __AUTH.__objc_data: 0x2a8
   __AUTH.__data: 0x1b8
   __DATA.__objc_ivar: 0x244

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 033048FA-DCAD-3936-9998-9D53B358AE3A
-  Functions: 2395
-  Symbols:   3343
-  CStrings:  1459
+  UUID: 482D012B-0114-3ACE-AA5A-98DFE4EFC277
+  Functions: 2449
+  Symbols:   3450
+  CStrings:  1496
 
Symbols:
+ -[DCCredentialStore deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]
+ -[DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]
+ -[DCCredentialStore retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]
+ -[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]
+ -[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]
+ -[DCCredentialStore storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]
+ -[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]
+ -[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]
+ -[DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]
+ -[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]
+ -[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:].cold.1
+ -[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]
+ -[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:].cold.1
+ -[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]
+ -[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:].cold.1
+ -[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]
+ -[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:].cold.1
+ -[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]
+ -[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:].cold.1
+ -[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]
+ -[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:].cold.1
+ -[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]
+ -[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:].cold.1
+ _DCCredentialKeyStoreTypeToString
+ ___100-[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke
+ ___100-[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2
+ ___100-[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2.cold.1
+ ___100-[DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2.cold.2
+ ___100-[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke
+ ___100-[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke_2
+ ___100-[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke_2.cold.1
+ ___100-[DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke_2.cold.2
+ ___101-[DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke
+ ___101-[DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke.43
+ ___101-[DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke.cold.1
+ ___103-[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke
+ ___103-[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke.41
+ ___103-[DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke.cold.1
+ ___107-[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke
+ ___107-[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke_2
+ ___107-[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke_2.cold.1
+ ___107-[DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:]_block_invoke_2.cold.2
+ ___109-[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke
+ ___109-[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke_2
+ ___109-[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke_2.cold.1
+ ___109-[DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke_2.cold.2
+ ___114-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke
+ ___114-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke.40
+ ___114-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke.cold.1
+ ___118-[DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke
+ ___118-[DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke.44
+ ___118-[DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke.cold.1
+ ___124-[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke
+ ___124-[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke_2
+ ___124-[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke_2.cold.1
+ ___124-[DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:]_block_invoke_2.cold.2
+ ___64-[DCCredentialStore(DebugAPIs) eraseLegacySEKeySlot:completion:]_block_invoke.289
+ ___64-[DCCredentialStore(DebugAPIs) keyInfoForCredential:completion:]_block_invoke.291
+ ___64-[DCCredentialStore(DebugAPIs) payloadsOfCredential:completion:]_block_invoke.286
+ ___65-[DCCredentialStore isPIITokenAvailableForIdentifier:completion:]_block_invoke.48
+ ___71-[DCCredentialStore(DebugAPIs) occupiedLegacySEKeySlotsWithCompletion:]_block_invoke.288
+ ___76-[DCCredentialStore deleteDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.39
+ ___76-[DCCredentialStore(DebugAPIs) allElementsOfCredential:authData:completion:]_block_invoke.287
+ ___78-[DCCredentialStore retrieveDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.38
+ ___81-[DCCredentialStore(DebugAPIs) clearPresentmentKeyUsageForCredential:completion:]_block_invoke.290
+ ___82-[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke
+ ___82-[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.42
+ ___82-[DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.cold.1
+ ___88-[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke
+ ___88-[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2
+ ___88-[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2.cold.1
+ ___88-[DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2.cold.2
+ ___92-[DCCredentialStore deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke
+ ___92-[DCCredentialStore deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke.47
+ ___92-[DCCredentialStore deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke.cold.1
+ ___94-[DCCredentialStore retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke
+ ___94-[DCCredentialStore retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke.46
+ ___94-[DCCredentialStore retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke.cold.1
+ ___94-[DCCredentialStore storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke
+ ___94-[DCCredentialStore storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke.45
+ ___94-[DCCredentialStore storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:]_block_invoke.cold.1
+ ___98-[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke
+ ___98-[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2
+ ___98-[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2.cold.1
+ ___98-[DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:]_block_invoke_2.cold.2
+ ___99-[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke
+ ___99-[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke.37
+ ___99-[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:]_block_invoke.cold.1
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
+ _block_copy_helper.66
+ _block_copy_helper.69
+ _block_copy_helper.85
+ _block_descriptor.68
+ _block_descriptor.71
+ _block_descriptor.87
+ _block_destroy_helper.67
+ _block_destroy_helper.70
+ _block_destroy_helper.86
+ _objc_msgSend$deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:
+ _objc_msgSend$deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:
+ _objc_msgSend$localizedCaseInsensitiveContainsString:
+ _objc_msgSend$retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:
+ _objc_msgSend$retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:
+ _objc_msgSend$storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:
+ _objc_msgSend$storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:
+ _objc_msgSend$storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:
- -[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]
- -[DCCredentialStoreClient deleteDataFromSyncableKeyStoreForIdentifier:completion:]
- -[DCCredentialStoreClient deleteDataFromSyncableKeyStoreForIdentifier:completion:].cold.1
- -[DCCredentialStoreClient retrieveDataFromSyncableKeyStoreForIdentifier:completion:]
- -[DCCredentialStoreClient retrieveDataFromSyncableKeyStoreForIdentifier:completion:].cold.1
- -[DCCredentialStoreClient storeDataInSyncableKeyStoreForIdentifier:data:completion:]
- -[DCCredentialStoreClient storeDataInSyncableKeyStoreForIdentifier:data:completion:].cold.1
- -[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]
- -[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:].cold.1
- ___64-[DCCredentialStore(DebugAPIs) eraseLegacySEKeySlot:completion:]_block_invoke.265
- ___64-[DCCredentialStore(DebugAPIs) keyInfoForCredential:completion:]_block_invoke.267
- ___64-[DCCredentialStore(DebugAPIs) payloadsOfCredential:completion:]_block_invoke.262
- ___65-[DCCredentialStore isPIITokenAvailableForIdentifier:completion:]_block_invoke.32
- ___71-[DCCredentialStore(DebugAPIs) occupiedLegacySEKeySlotsWithCompletion:]_block_invoke.264
- ___76-[DCCredentialStore deleteDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.30
- ___76-[DCCredentialStore(DebugAPIs) allElementsOfCredential:authData:completion:]_block_invoke.263
- ___78-[DCCredentialStore retrieveDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke.29
- ___78-[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke
- ___78-[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke.28
- ___78-[DCCredentialStore storeDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke.cold.1
- ___81-[DCCredentialStore(DebugAPIs) clearPresentmentKeyUsageForCredential:completion:]_block_invoke.266
- ___82-[DCCredentialStoreClient deleteDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke
- ___82-[DCCredentialStoreClient deleteDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2
- ___82-[DCCredentialStoreClient deleteDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2.cold.1
- ___82-[DCCredentialStoreClient deleteDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2.cold.2
- ___84-[DCCredentialStoreClient retrieveDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke
- ___84-[DCCredentialStoreClient retrieveDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2
- ___84-[DCCredentialStoreClient retrieveDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2.cold.1
- ___84-[DCCredentialStoreClient retrieveDataFromSyncableKeyStoreForIdentifier:completion:]_block_invoke_2.cold.2
- ___84-[DCCredentialStoreClient storeDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke
- ___84-[DCCredentialStoreClient storeDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke_2
- ___84-[DCCredentialStoreClient storeDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke_2.cold.1
- ___84-[DCCredentialStoreClient storeDataInSyncableKeyStoreForIdentifier:data:completion:]_block_invoke_2.cold.2
- ___93-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke
- ___93-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke.31
- ___93-[DCCredentialStore updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke.cold.1
- ___99-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke
- ___99-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke_2
- ___99-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke_2.cold.1
- ___99-[DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:]_block_invoke_2.cold.2
- _block_copy_helper.57
- _block_copy_helper.79
- _block_descriptor.59
- _block_descriptor.81
- _block_destroy_helper.58
- _block_destroy_helper.80
- _objc_msgSend$deleteDataFromSyncableKeyStoreForIdentifier:completion:
- _objc_msgSend$retrieveDataFromSyncableKeyStoreForIdentifier:completion:
- _objc_msgSend$storeDataInSyncableKeyStoreForIdentifier:data:completion:
- _objc_msgSend$updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:
CStrings:
+ ""
+ "-cross-check"
+ "DCCredentialStore deletePIIHashFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStore deletePIITokenFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStore retrievePIIHashFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStore retrievePIITokenFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStore storePIIHashInSyncableKeyStoreForIdentifier"
+ "DCCredentialStore storePIITokenInSyncableKeyStoreForIdentifier"
+ "DCCredentialStore updatePIITokenInSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient deletePIIHashFromSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient deletePIITokenFromSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient retrievePIIHashFromSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient retrievePIITokenFromSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient storePIIHashInSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient storePIITokenInSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier"
+ "DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier returned successfully"
+ "DCCredentialStoreClient updatePIITokenInSyncableKeyStoreForIdentifier returned with error %{public}@"
+ "Local"
+ "cross-check"
+ "deletePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:"
+ "deletePIITokenFromSyncableKeyStoreForIdentifier:credentialIdentifier:completion:"
+ "localizedCaseInsensitiveContainsString:"
+ "retrievePIIHashFromSyncableKeyStoreForIdentifier:keystoreType:completion:"
+ "retrievePIITokenFromSyncableKeyStoreForIdentifier:completion:"
+ "storeDataInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:"
+ "storePIIHashInSyncableKeyStoreForIdentifier:data:keystoreType:completion:"
+ "storePIITokenInSyncableKeyStoreForIdentifier:data:credentialIdentifier:completion:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:"
+ "updatePIITokenInSyncableKeyStoreForIdentifier:attributesToUpdate:credentialIdentifier:completion:"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v48@0:8@\"NSString\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "DCCredentialStoreClient deleteDataFromSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient deleteDataFromSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient deleteDataFromSyncableKeyStoreForIdentifier returned with error %{public}@"
- "DCCredentialStoreClient retrieveDataFromSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient retrieveDataFromSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient retrieveDataFromSyncableKeyStoreForIdentifier returned with error %{public}@"
- "DCCredentialStoreClient storeDataInSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient storeDataInSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient storeDataInSyncableKeyStoreForIdentifier returned with error %{public}@"
- "DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier"
- "DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier returned successfully"
- "DCCredentialStoreClient updateDataInSyncableKeyStoreForIdentifier returned with error %{public}@"
- "updateDataInSyncableKeyStoreForIdentifier:attributesToUpdate:completion:"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"

```
