## ClassroomKit

> `/System/Library/PrivateFrameworks/ClassroomKit.framework/Versions/A/ClassroomKit`

```diff

-142.0.0.0.0
-  __TEXT.__text: 0xbe408
-  __TEXT.__objc_methlist: 0x12dac
-  __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x8c9c
-  __TEXT.__oslogstring: 0x45ac
-  __TEXT.__gcc_except_tab: 0x668
+143.1.1.0.0
+  __TEXT.__text: 0xc2404
+  __TEXT.__objc_methlist: 0x13224
+  __TEXT.__const: 0x178
+  __TEXT.__cstring: 0x8e55
+  __TEXT.__oslogstring: 0x4d92
+  __TEXT.__gcc_except_tab: 0x6d0
   __TEXT.__ustring: 0x37e
-  __TEXT.__unwind_info: 0x3a30
+  __TEXT.__unwind_info: 0x3b20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe68
-  __DATA_CONST.__objc_classlist: 0xf10
+  __DATA_CONST.__const: 0xeb8
+  __DATA_CONST.__objc_classlist: 0xf38
   __DATA_CONST.__objc_catlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x458
+  __DATA_CONST.__objc_protolist: 0x460
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f08
-  __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0xbf8
+  __DATA_CONST.__objc_selrefs: 0x7090
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0xc18
   __DATA_CONST.__objc_arraydata: 0x2a0
-  __DATA_CONST.__got: 0x1248
-  __AUTH_CONST.__const: 0x3730
-  __AUTH_CONST.__cfstring: 0x9160
-  __AUTH_CONST.__objc_const: 0x26aa0
+  __DATA_CONST.__got: 0x1280
+  __AUTH_CONST.__const: 0x3830
+  __AUTH_CONST.__cfstring: 0x9300
+  __AUTH_CONST.__objc_const: 0x27100
   __AUTH_CONST.__objc_dictobj: 0x398
-  __AUTH_CONST.__objc_intobj: 0x300
+  __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x6f8
-  __AUTH.__objc_data: 0x69f0
-  __DATA.__objc_ivar: 0x1250
-  __DATA.__data: 0x3440
+  __AUTH_CONST.__auth_got: 0x720
+  __AUTH.__objc_data: 0x6b80
+  __DATA.__objc_ivar: 0x1270
+  __DATA.__data: 0x34a0
   __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x2cb0
-  __DATA_DIRTY.__bss: 0x650
+  __DATA_DIRTY.__bss: 0x660
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6444
-  Symbols:   15153
-  CStrings:  1656
+  Functions: 6550
+  Symbols:   15349
+  CStrings:  1702
 
Symbols:
+ +[CRKASMCredentialStoreFactory instructorCredentialStoreUsingLoginKeychain]
+ +[CRKASMCredentialStoreFactory instructorCredentialStoreUsingModernKeychain]
+ +[CRKASMCredentialStoreFactory instructorManifestServiceNames]
+ +[CRKASMCredentialStoreFactory makeCredentialStoreWithRole:keychainOverride:accessGroupOverride:]
+ +[CRKASMCredentialStoreFactory makeInstructorCredentialStoreWithKeychainOverride:accessGroupOverride:]
+ +[CRKASMRosterProviderConfiguration instructorRosterUsingLoginKeychainConfiguration]
+ +[CRKASMRosterProviderConfiguration instructorRosterUsingModernKeychainConfiguration]
+ +[CRKConcreteKeychain macOSLegacyLoginKeychain]
+ +[CRKConcreteKeychain modernKeychain]
+ +[CRKIdentityConfiguration defaultCreatesDataProtectionKey]
+ +[CRKMigrateKeychainItemsToModernKeychainRequest allowlistedClassForResultObject]
+ +[CRKMigrateKeychainItemsToModernKeychainRequest supportsSecureCoding]
+ +[CRKMigrateKeychainItemsToModernKeychainResultObject supportsSecureCoding]
+ +[CRKPropertyListConverter propertyListSafeValue:]
+ +[CRKRemovePersistentIDsFromLoginKeychainRequest supportsSecureCoding]
+ +[NSXPCConnection(CRKAdditions) crk_keychainMigrationServiceConnection]
+ -[CRKASMCredentialStore ingestMigratedCredentialsFromStore:modernPersistentIDsByLegacyID:]
+ -[CRKASMCredentialStore removeStoredManifests]
+ -[CRKASMRosterProviderFactory makeInstructorRosterProviderUsingLoginKeychain]
+ -[CRKASMRosterProviderFactory makeInstructorRosterProviderUsingModernKeychain]
+ -[CRKAnnotatedCredentialStore deleteStoredManifestReturningError:]
+ -[CRKAnnotatedCredentialStore ingestMigratedManifestFromStore:modernPersistentIDsByLegacyID:]
+ -[CRKConcreteCertificate publicKeyHash]
+ -[CRKConcreteKeychain addItem:ofClass:toAccessGroup:]
+ -[CRKConcreteKeychain alwaysAccessibleAttribute]
+ -[CRKConcreteKeychain isUsingLegacyKeychain]
+ -[CRKConcreteKeychain isUsingModernKeychain]
+ -[CRKConcreteKeychain removeCertificate:error:]
+ -[CRKConcreteKeychain removeKeyWithApplicationLabel:keyClass:error:]
+ -[CRKConcreteKeychain removePasswordForService:error:]
+ -[CRKConcreteKeychain removePrivateKeyWithApplicationLabel:error:]
+ -[CRKConcreteKeychain removePublicKeyWithApplicationLabel:error:]
+ -[CRKConcretePrivateKey algorithmID]
+ -[CRKConcretePrivateKey applicationLabel]
+ -[CRKConcretePrivateKey publicKey]
+ -[CRKDevice lastStudentError]
+ -[CRKDevice setLastStudentError:]
+ -[CRKIdentityConfiguration createsDataProtectionKey]
+ -[CRKIdentityConfiguration setCreatesDataProtectionKey:]
+ -[CRKInMemoryCertificate publicKeyHash]
+ -[CRKInMemoryKeychain removeCertificate:error:]
+ -[CRKInMemoryKeychain removePasswordForService:error:]
+ -[CRKInMemoryKeychain removePrivateKeyWithApplicationLabel:error:]
+ -[CRKInMemoryKeychain removePublicKeyWithApplicationLabel:error:]
+ -[CRKInMemoryPrivateKey algorithmID]
+ -[CRKInMemoryPrivateKey applicationLabel]
+ -[CRKInMemoryPrivateKey publicKey]
+ -[CRKKeychainMigrationServiceProxy .cxx_destruct]
+ -[CRKKeychainMigrationServiceProxy _performMigrationRequest:completion:]
+ -[CRKKeychainMigrationServiceProxy _performRemovalRequest:completion:]
+ -[CRKKeychainMigrationServiceProxy connectionProvider]
+ -[CRKKeychainMigrationServiceProxy init]
+ -[CRKKeychainMigrationServiceProxy performMigrationRequest:completion:]
+ -[CRKKeychainMigrationServiceProxy performRemovalRequest:completion:]
+ -[CRKMigrateKeychainItemsToModernKeychainRequest .cxx_destruct]
+ -[CRKMigrateKeychainItemsToModernKeychainRequest certificatePersistentIDs]
+ -[CRKMigrateKeychainItemsToModernKeychainRequest encodeWithCoder:]
+ -[CRKMigrateKeychainItemsToModernKeychainRequest identityPersistentIDs]
+ -[CRKMigrateKeychainItemsToModernKeychainRequest initWithCoder:]
+ -[CRKMigrateKeychainItemsToModernKeychainRequest migratesInstructorASMCredentialStore]
+ -[CRKMigrateKeychainItemsToModernKeychainRequest setCertificatePersistentIDs:]
+ -[CRKMigrateKeychainItemsToModernKeychainRequest setIdentityPersistentIDs:]
+ -[CRKMigrateKeychainItemsToModernKeychainRequest setMigratesInstructorASMCredentialStore:]
+ -[CRKMigrateKeychainItemsToModernKeychainResultObject .cxx_destruct]
+ -[CRKMigrateKeychainItemsToModernKeychainResultObject encodeWithCoder:]
+ -[CRKMigrateKeychainItemsToModernKeychainResultObject initWithCoder:]
+ -[CRKMigrateKeychainItemsToModernKeychainResultObject modernPersistentIDsByLegacyPersistentID]
+ -[CRKMigrateKeychainItemsToModernKeychainResultObject setModernPersistentIDsByLegacyPersistentID:]
+ -[CRKNoOpKeychain removeCertificate:error:]
+ -[CRKNoOpKeychain removePasswordForService:error:]
+ -[CRKNoOpKeychain removePrivateKeyWithApplicationLabel:error:]
+ -[CRKNoOpKeychain removePublicKeyWithApplicationLabel:error:]
+ -[CRKRemovePersistentIDsFromLoginKeychainRequest .cxx_destruct]
+ -[CRKRemovePersistentIDsFromLoginKeychainRequest encodeWithCoder:]
+ -[CRKRemovePersistentIDsFromLoginKeychainRequest initWithCoder:]
+ -[CRKRemovePersistentIDsFromLoginKeychainRequest persistentIDs]
+ -[CRKRemovePersistentIDsFromLoginKeychainRequest setPersistentIDs:]
+ -[NSError(CRKAdditions) dictionaryValue]
+ -[NSError(CRKAdditions) initWithDictionary:]
+ GCC_except_table22
+ OBJC_IVAR_$_CRKDevice._lastStudentError
+ OBJC_IVAR_$_CRKIdentityConfiguration._createsDataProtectionKey
+ OBJC_IVAR_$_CRKKeychainMigrationServiceProxy._connectionProvider
+ OBJC_IVAR_$_CRKMigrateKeychainItemsToModernKeychainRequest._certificatePersistentIDs
+ OBJC_IVAR_$_CRKMigrateKeychainItemsToModernKeychainRequest._identityPersistentIDs
+ OBJC_IVAR_$_CRKMigrateKeychainItemsToModernKeychainRequest._migratesInstructorASMCredentialStore
+ OBJC_IVAR_$_CRKMigrateKeychainItemsToModernKeychainResultObject._modernPersistentIDsByLegacyPersistentID
+ OBJC_IVAR_$_CRKRemovePersistentIDsFromLoginKeychainRequest._persistentIDs
+ _CRKClassroomModernKeychainAccessGroup
+ _CRKConfigureInterfaceForKeychainMigrationService
+ _CRKDeviceLastStudentErrorKey
+ _CRKItemNotFoundError
+ _CRKKeychainMigrationServiceXPCInterface
+ _OBJC_CLASS_$_CRKKeychainMigrationServiceProxy
+ _OBJC_CLASS_$_CRKMigrateKeychainItemsToModernKeychainRequest
+ _OBJC_CLASS_$_CRKMigrateKeychainItemsToModernKeychainResultObject
+ _OBJC_CLASS_$_CRKPropertyListConverter
+ _OBJC_CLASS_$_CRKRemovePersistentIDsFromLoginKeychainRequest
+ _OBJC_METACLASS_$_CRKKeychainMigrationServiceProxy
+ _OBJC_METACLASS_$_CRKMigrateKeychainItemsToModernKeychainRequest
+ _OBJC_METACLASS_$_CRKMigrateKeychainItemsToModernKeychainResultObject
+ _OBJC_METACLASS_$_CRKPropertyListConverter
+ _OBJC_METACLASS_$_CRKRemovePersistentIDsFromLoginKeychainRequest
+ _SecCertificateCopyAttributeDictionary
+ _SecKeyCopyAttributes
+ _SecKeyCopyPublicKey
+ _SecKeyCreateRandomKey
+ _SecKeyGetAlgorithmId
+ __50-[CRKConcreteKeychain removeItemWithPersistentID:]_block_invoke
+ __72-[CRKKeychainMigrationServiceProxy _performMigrationRequest:completion:]_block_invoke
+ __72-[CRKKeychainMigrationServiceProxy _performMigrationRequest:completion:]_block_invoke_2
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSError_$_CRKAdditions
+ __OBJC_$_CLASS_METHODS_CRKMigrateKeychainItemsToModernKeychainRequest
+ __OBJC_$_CLASS_METHODS_CRKMigrateKeychainItemsToModernKeychainResultObject
+ __OBJC_$_CLASS_METHODS_CRKPropertyListConverter
+ __OBJC_$_CLASS_METHODS_CRKRemovePersistentIDsFromLoginKeychainRequest
+ __OBJC_$_INSTANCE_METHODS_CRKKeychainMigrationServiceProxy
+ __OBJC_$_INSTANCE_METHODS_CRKMigrateKeychainItemsToModernKeychainRequest
+ __OBJC_$_INSTANCE_METHODS_CRKMigrateKeychainItemsToModernKeychainResultObject
+ __OBJC_$_INSTANCE_METHODS_CRKRemovePersistentIDsFromLoginKeychainRequest
+ __OBJC_$_INSTANCE_VARIABLES_CRKKeychainMigrationServiceProxy
+ __OBJC_$_INSTANCE_VARIABLES_CRKMigrateKeychainItemsToModernKeychainRequest
+ __OBJC_$_INSTANCE_VARIABLES_CRKMigrateKeychainItemsToModernKeychainResultObject
+ __OBJC_$_INSTANCE_VARIABLES_CRKRemovePersistentIDsFromLoginKeychainRequest
+ __OBJC_$_PROP_LIST_CRKKeychainMigrationServiceProxy
+ __OBJC_$_PROP_LIST_CRKMigrateKeychainItemsToModernKeychainRequest
+ __OBJC_$_PROP_LIST_CRKMigrateKeychainItemsToModernKeychainResultObject
+ __OBJC_$_PROP_LIST_CRKRemovePersistentIDsFromLoginKeychainRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRKKeychainMigrationServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRKKeychainMigrationServiceInterface
+ __OBJC_CATEGORY_PROTOCOLS_$_NSError_$_CRKAdditions
+ __OBJC_CLASS_PROTOCOLS_$_CRKKeychainMigrationServiceProxy
+ __OBJC_CLASS_RO_$_CRKKeychainMigrationServiceProxy
+ __OBJC_CLASS_RO_$_CRKMigrateKeychainItemsToModernKeychainRequest
+ __OBJC_CLASS_RO_$_CRKMigrateKeychainItemsToModernKeychainResultObject
+ __OBJC_CLASS_RO_$_CRKPropertyListConverter
+ __OBJC_CLASS_RO_$_CRKRemovePersistentIDsFromLoginKeychainRequest
+ __OBJC_LABEL_PROTOCOL_$_CRKKeychainMigrationServiceInterface
+ __OBJC_METACLASS_RO_$_CRKKeychainMigrationServiceProxy
+ __OBJC_METACLASS_RO_$_CRKMigrateKeychainItemsToModernKeychainRequest
+ __OBJC_METACLASS_RO_$_CRKMigrateKeychainItemsToModernKeychainResultObject
+ __OBJC_METACLASS_RO_$_CRKPropertyListConverter
+ __OBJC_METACLASS_RO_$_CRKRemovePersistentIDsFromLoginKeychainRequest
+ __OBJC_PROTOCOL_$_CRKKeychainMigrationServiceInterface
+ __OBJC_PROTOCOL_REFERENCE_$_CRKKeychainMigrationServiceInterface
+ ___40-[CRKKeychainMigrationServiceProxy init]_block_invoke
+ ___50+[CRKPropertyListConverter propertyListSafeValue:]_block_invoke
+ ___50-[CRKConcreteKeychain privateKeyWithPersistentID:]_block_invoke
+ ___50-[CRKConcreteKeychain removeItemWithPersistentID:]_block_invoke
+ ___69-[CRKKeychainMigrationServiceProxy performRemovalRequest:completion:]_block_invoke
+ ___70-[CRKKeychainMigrationServiceProxy _performRemovalRequest:completion:]_block_invoke
+ ___70-[CRKKeychainMigrationServiceProxy _performRemovalRequest:completion:]_block_invoke_2
+ ___70-[CRKKeychainMigrationServiceProxy _performRemovalRequest:completion:]_block_invoke_3
+ ___70-[CRKKeychainMigrationServiceProxy _performRemovalRequest:completion:]_block_invoke_4
+ ___71-[CRKKeychainMigrationServiceProxy performMigrationRequest:completion:]_block_invoke
+ ___72-[CRKKeychainMigrationServiceProxy _performMigrationRequest:completion:]_block_invoke
+ ___72-[CRKKeychainMigrationServiceProxy _performMigrationRequest:completion:]_block_invoke_2
+ ___block_descriptor_32_e18_B16?0"NSNumber"8l
+ ___block_descriptor_32_e25_v32?0"NSNumber"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e73_v24?0"CRKMigrateKeychainItemsToModernKeychainResultObject"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e73_v24?0"CRKMigrateKeychainItemsToModernKeychainResultObject"8"NSError"16l
+ _kSecAttrApplicationLabel
+ _kSecAttrKeyClassPublic
+ _kSecAttrPublicKeyHash
+ _kSecClassKey
+ _kSecUseDataProtectionKeychain
+ _objc_msgSend$_performMigrationRequest:completion:
+ _objc_msgSend$_performRemovalRequest:completion:
+ _objc_msgSend$addItem:ofClass:toAccessGroup:
+ _objc_msgSend$alwaysAccessibleAttribute
+ _objc_msgSend$array
+ _objc_msgSend$certificatePersistentIDs
+ _objc_msgSend$createsDataProtectionKey
+ _objc_msgSend$crk_keychainMigrationServiceConnection
+ _objc_msgSend$defaultCreatesDataProtectionKey
+ _objc_msgSend$deleteStoredManifestReturningError:
+ _objc_msgSend$identityPersistentIDs
+ _objc_msgSend$ingestMigratedManifestFromStore:modernPersistentIDsByLegacyID:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$instructorCredentialStoreUsingLoginKeychain
+ _objc_msgSend$instructorCredentialStoreUsingModernKeychain
+ _objc_msgSend$instructorRosterUsingLoginKeychainConfiguration
+ _objc_msgSend$instructorRosterUsingModernKeychainConfiguration
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isUsingLegacyKeychain
+ _objc_msgSend$isUsingModernKeychain
+ _objc_msgSend$lastStudentError
+ _objc_msgSend$macOSLegacyLoginKeychain
+ _objc_msgSend$makeCredentialStoreWithRole:keychainOverride:accessGroupOverride:
+ _objc_msgSend$makeInstructorCredentialStoreWithKeychainOverride:accessGroupOverride:
+ _objc_msgSend$migratesInstructorASMCredentialStore
+ _objc_msgSend$modernKeychain
+ _objc_msgSend$modernPersistentIDsByLegacyPersistentID
+ _objc_msgSend$performMigrationRequest:completion:
+ _objc_msgSend$performRemovalRequest:completion:
+ _objc_msgSend$propertyListSafeValue:
+ _objc_msgSend$publicKeyHash
+ _objc_msgSend$removeKeyWithApplicationLabel:keyClass:error:
+ _objc_msgSend$setCreatesDataProtectionKey:
+ _objc_msgSend$setLastStudentError:
- +[CRKASMCredentialStoreFactory makeCredentialStoreWithRole:keychainOverride:]
- -[CRKConcreteKeychain addItem:toAccessGroup:]
- GCC_except_table18
- _objc_msgSend$makeCredentialStoreWithRole:keychainOverride:
CStrings:
+ "4WXS7A4F54.com.apple.macos.classroom"
+ "B16@?0@\"NSNumber\"8"
+ "Encountered multiple errors when removing keychain item with persistent ID %@"
+ "Failed to add identity to keychain."
+ "KEYCHAIN: Added certificate \"%{private, mask.hash}@\" (pubKeyHash %{private, mask.hash}@) -> persistent ID %{public}@"
+ "KEYCHAIN: Added identity \"%{private, mask.hash}@\" (pubKeyHash %{private, mask.hash}@) -> persistent ID %{public}@"
+ "KEYCHAIN: Adding certificate %{private, mask.hash}@ to access group %{public}@"
+ "KEYCHAIN: Adding identity %{private, mask.hash}@ to access group %{public}@"
+ "KEYCHAIN: Adding private key to access group %{public}@"
+ "KEYCHAIN: Calling SecItemAdd with query: %{public}@"
+ "KEYCHAIN: Calling SecItemCopyMatching with query: %{public}@"
+ "KEYCHAIN: Calling SecItemDelete with query %{public}@"
+ "KEYCHAIN: Creating certificate with data: %{public}@"
+ "KEYCHAIN: Creating data protection key"
+ "KEYCHAIN: Creating identity with certificate %{private, mask.hash}@ and private key %{private, mask.hash}@"
+ "KEYCHAIN: Creating identity with configuration"
+ "KEYCHAIN: Creating legacy key"
+ "KEYCHAIN: Creating private key (%lu bytes)"
+ "KEYCHAIN: Removing item with persistent ID %{public}@"
+ "KEYCHAIN: Removing key with application label %{public}@, key class %{public}@"
+ "KEYCHAIN: Retieving certificate with persistent ID %{public}@"
+ "KEYCHAIN: Retieving identity with persistent ID %{public}@"
+ "KEYCHAIN: Retieving private key with persistent ID %{public}@"
+ "KEYCHAIN: Retrieved certificate \"%{private, mask.hash}@\" (pubKeyHash %{private, mask.hash}@) for persistent ID %{public}@"
+ "KEYCHAIN: Retrieved identity \"%{private, mask.hash}@\" (pubKeyHash %{private, mask.hash}@) for persistent ID %{public}@"
+ "KEYCHAIN: SecIdentityCopyCertificate failed with status %{public}@"
+ "KEYCHAIN: SecIdentityCopyCertificate succeeded"
+ "KEYCHAIN: SecIdentityCopyPrivateKey failed with status %{public}@"
+ "KEYCHAIN: SecIdentityCopyPrivateKey succeeded"
+ "KEYCHAIN: SecItemDelete (certificate) failed: %{public}@"
+ "KEYCHAIN: SecItemDelete (key, class %{public}@) failed: %{public}@"
+ "KEYCHAIN: SecItemDelete (password, service %{public}@) status: %d"
+ "Keychain removal error %ld: %{public}@."
+ "No modern persistent ID found for a migrated credential; dropping its manifest entry"
+ "certificatePersistentIDs"
+ "code"
+ "com.apple.ClassroomKit.KeychainMigrationService"
+ "createsDataProtectionKey"
+ "domain"
+ "identityPersistentIDs"
+ "itemName"
+ "lastStudentError"
+ "migratesInstructorASMCredentialStore"
+ "modernPersistentIDsByLegacyPersistentID"
+ "persistentIDs"
+ "v24@?0@\"CRKMigrateKeychainItemsToModernKeychainResultObject\"8@\"NSError\"16"
+ "v32@?0@\"NSNumber\"8Q16^B24"
- "Could not remove keychain item with persistentID %@. Error (ignored): %{public}@."
```
