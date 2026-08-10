## ClassroomKit

> `/System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-142.0.0.0.0
-  __TEXT.__text: 0xb1218
-  __TEXT.__objc_methlist: 0x12c8c
-  __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x8a75
-  __TEXT.__oslogstring: 0x42cb
-  __TEXT.__gcc_except_tab: 0x6b8
+143.2.1.0.0
+  __TEXT.__text: 0xb4cd0
+  __TEXT.__objc_methlist: 0x130f4
+  __TEXT.__const: 0x190
+  __TEXT.__cstring: 0x8c09
+  __TEXT.__oslogstring: 0x4ab1
+  __TEXT.__gcc_except_tab: 0x720
   __TEXT.__ustring: 0x37e
-  __TEXT.__unwind_info: 0x3a30
+  __TEXT.__unwind_info: 0x3b20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2998
-  __DATA_CONST.__objc_classlist: 0xf00
+  __DATA_CONST.__const: 0x2a38
+  __DATA_CONST.__objc_classlist: 0xf28
   __DATA_CONST.__objc_catlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x450
+  __DATA_CONST.__objc_protolist: 0x458
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6eb0
-  __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0xbf0
+  __DATA_CONST.__objc_selrefs: 0x7038
+  __DATA_CONST.__objc_protorefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0xc10
   __DATA_CONST.__objc_arraydata: 0x288
-  __DATA_CONST.__got: 0x12c0
-  __AUTH_CONST.__const: 0x1860
-  __AUTH_CONST.__cfstring: 0x8ec0
-  __AUTH_CONST.__objc_const: 0x26978
+  __DATA_CONST.__got: 0x12f0
+  __AUTH_CONST.__const: 0x18e0
+  __AUTH_CONST.__cfstring: 0x9040
+  __AUTH_CONST.__objc_const: 0x26fd8
   __AUTH_CONST.__objc_dictobj: 0x370
-  __AUTH_CONST.__objc_intobj: 0x300
+  __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x6fe0
-  __DATA.__objc_ivar: 0x1250
-  __DATA.__data: 0x33c8
+  __AUTH.__objc_data: 0x7170
+  __DATA.__objc_ivar: 0x1270
+  __DATA.__data: 0x3428
   __DATA.__bss: 0x190
   __DATA_DIRTY.__objc_data: 0x2620
-  __DATA_DIRTY.__bss: 0x620
+  __DATA_DIRTY.__bss: 0x630
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6365
-  Symbols:   15072
-  CStrings:  1624
+  Functions: 6469
+  Symbols:   15265
+  CStrings:  1669
 
Symbols:
+ +[CRKASMCredentialStoreFactory instructorCredentialStoreUsingLoginKeychain]
+ +[CRKASMCredentialStoreFactory instructorCredentialStoreUsingModernKeychain]
+ +[CRKASMCredentialStoreFactory instructorManifestServiceNames]
+ +[CRKASMCredentialStoreFactory makeCredentialStoreWithRole:keychainOverride:accessGroupOverride:]
+ +[CRKASMCredentialStoreFactory makeInstructorCredentialStoreWithKeychainOverride:accessGroupOverride:]
+ +[CRKASMRosterProviderConfiguration instructorRosterUsingLoginKeychainConfiguration]
+ +[CRKASMRosterProviderConfiguration instructorRosterUsingModernKeychainConfiguration]
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
+ _OBJC_IVAR_$_CRKDevice._lastStudentError
+ _OBJC_IVAR_$_CRKIdentityConfiguration._createsDataProtectionKey
+ _OBJC_IVAR_$_CRKKeychainMigrationServiceProxy._connectionProvider
+ _OBJC_IVAR_$_CRKMigrateKeychainItemsToModernKeychainRequest._certificatePersistentIDs
+ _OBJC_IVAR_$_CRKMigrateKeychainItemsToModernKeychainRequest._identityPersistentIDs
+ _OBJC_IVAR_$_CRKMigrateKeychainItemsToModernKeychainRequest._migratesInstructorASMCredentialStore
+ _OBJC_IVAR_$_CRKMigrateKeychainItemsToModernKeychainResultObject._modernPersistentIDsByLegacyPersistentID
+ _OBJC_IVAR_$_CRKRemovePersistentIDsFromLoginKeychainRequest._persistentIDs
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
+ ___50-[CRKConcreteKeychain removeItemWithPersistentID:]_block_invoke
+ ___69-[CRKKeychainMigrationServiceProxy performRemovalRequest:completion:]_block_invoke
+ ___70-[CRKKeychainMigrationServiceProxy _performRemovalRequest:completion:]_block_invoke
+ ___70-[CRKKeychainMigrationServiceProxy _performRemovalRequest:completion:]_block_invoke_2
+ ___70-[CRKKeychainMigrationServiceProxy _performRemovalRequest:completion:]_block_invoke_3
+ ___70-[CRKKeychainMigrationServiceProxy _performRemovalRequest:completion:]_block_invoke_4
+ ___71-[CRKKeychainMigrationServiceProxy performMigrationRequest:completion:]_block_invoke
+ ___72-[CRKKeychainMigrationServiceProxy _performMigrationRequest:completion:]_block_invoke
+ ___72-[CRKKeychainMigrationServiceProxy _performMigrationRequest:completion:]_block_invoke_2
+ ___72-[CRKKeychainMigrationServiceProxy _performMigrationRequest:completion:]_block_invoke_3
+ ___72-[CRKKeychainMigrationServiceProxy _performMigrationRequest:completion:]_block_invoke_4
+ ___block_descriptor_32_e18_B16?0"NSNumber"8l
+ ___block_descriptor_32_e25_v32?0"NSNumber"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e73_v24?0"CRKMigrateKeychainItemsToModernKeychainResultObject"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e73_v24?0"CRKMigrateKeychainItemsToModernKeychainResultObject"8"NSError"16ls32l8s40l8
+ _kSecAttrApplicationLabel
+ _kSecAttrKeyClassPublic
+ _kSecAttrPublicKeyHash
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
- _objc_msgSend$makeCredentialStoreWithRole:keychainOverride:
CStrings:
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
