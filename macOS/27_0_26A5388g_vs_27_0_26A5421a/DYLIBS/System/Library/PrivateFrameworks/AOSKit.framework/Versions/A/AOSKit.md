## AOSKit

> `/System/Library/PrivateFrameworks/AOSKit.framework/Versions/A/AOSKit`

```diff

-303.0.0.0.0
-  __TEXT.__text: 0x19532c
-  __TEXT.__objc_methlist: 0x13cc
+304.0.0.0.0
+  __TEXT.__text: 0x197814
+  __TEXT.__objc_methlist: 0x1574
+  __TEXT.__gcc_except_tab: 0x1a44
   __TEXT.__const: 0x3b990
-  __TEXT.__gcc_except_tab: 0x1a20
-  __TEXT.__oslogstring: 0x16ec
-  __TEXT.__cstring: 0xab68
+  __TEXT.__cstring: 0xad02
+  __TEXT.__oslogstring: 0x1f5a
   __TEXT.__ustring: 0x26
-  __TEXT.__unwind_info: 0xd80
+  __TEXT.__unwind_info: 0xdf8
   __TEXT.__eh_frame: 0xc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xfd0
+  __DATA_CONST.__const: 0xff0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1160
+  __DATA_CONST.__objc_selrefs: 0x12a0
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__got: 0x3c8
   __AUTH_CONST.__const: 0xdb60
-  __AUTH_CONST.__cfstring: 0x9140
+  __AUTH_CONST.__cfstring: 0x9300
   __AUTH_CONST.__objc_const: 0x16b8
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__auth_got: 0x7b8
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0xee8
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xc0
   __DATA.__common: 0xa88
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__data: 0x70

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 838
-  Symbols:   2079
-  CStrings:  1293
+  Functions: 917
+  Symbols:   2175
+  CStrings:  1346
 
Symbols:
+ +[KeychainAccountStorage(Migration) _attemptKeychainLookupWithService:dsid:dsidStr:appleID:clientID:attemptNum:]
+ +[KeychainAccountStorage(Migration) _copyLegacyKeychainItemRefForService:dsid:]
+ +[KeychainAccountStorage(Migration) _createMigratedSecItemForDSID:service:appleID:legacyKeyData:clientID:]
+ +[KeychainAccountStorage(Migration) _deleteLegacyKeychainItemForDSID:service:clientID:]
+ +[KeychainAccountStorage(Migration) _extractLegacyKeychainDataForDSID:service:clientID:]
+ +[KeychainAccountStorage(Migration) _finalizeMigrationForDSID:service:clientID:]
+ +[KeychainAccountStorage(Migration) _findLegacyPasswordForService:dsid:clientID:]
+ +[KeychainAccountStorage(Migration) _handleDuplicateItemForService:dsid:appleID:encodedKeyData:attributes:clientID:]
+ +[KeychainAccountStorage(Migration) _isBundleIdentifierTrusted:]
+ +[KeychainAccountStorage(Migration) _isCurrentProcessTrustedForKeychainAccess]
+ +[KeychainAccountStorage(Migration) _isMigrationCompleteForDSID:service:]
+ +[KeychainAccountStorage(Migration) _isProcessPathTrusted:]
+ +[KeychainAccountStorage(Migration) _isSecItemKeychainAccessible]
+ +[KeychainAccountStorage(Migration) _isValidSecItemWithService:dsid:clientID:]
+ +[KeychainAccountStorage(Migration) _legacyKeychainItemExistsForDSID:service:]
+ +[KeychainAccountStorage(Migration) _markMigrationCompleteForDSID:service:clientID:]
+ +[KeychainAccountStorage(Migration) _needsMigrationForDSID:service:]
+ +[KeychainAccountStorage(Migration) _performMigrationForDSID:service:appleID:clientID:]
+ +[KeychainAccountStorage(Migration) _performPreflightCanaryCheck]
+ +[KeychainAccountStorage(Migration) _performSecItemLookupWithService:dsid:clientID:]
+ +[KeychainAccountStorage(Migration) _processLegacyKeychainData:length:itemRef:findStatus:clientID:]
+ +[KeychainAccountStorage(Migration) _rollbackMigrationForDSID:service:clientID:]
+ +[KeychainAccountStorage(Migration) _secItemExistsForDSID:service:]
+ +[KeychainAccountStorage(Migration) _setTestLegacyData:forDSID:service:]
+ +[KeychainAccountStorage(Migration) _testLegacyDataForDSID:service:]
+ +[KeychainAccountStorage(Migration) _validateKeychainDataIntegrity:dsid:clientID:]
+ +[KeychainAccountStorage(Migration) _verifyAndCleanupPreflightCanary:expectedData:]
+ +[KeychainAccountStorage(Migration) _verifyMigrationForDSID:service:clientID:]
+ +[KeychainAccountStorage(Proxy) _migrateKeyToSecItemForDSID:andAccount:accountInfo:]
+ +[KeychainAccountStorage(Proxy) shouldMigrate]
+ +[KeychainAccountStorage(SecItem) _attemptTemporaryServiceUpdate:service:attributes:clientID:]
+ +[KeychainAccountStorage(SecItem) _buildRecoveredAttributesFromResult:service:]
+ +[KeychainAccountStorage(SecItem) _createTemporaryItemWithService:attributes:clientID:]
+ +[KeychainAccountStorage(SecItem) _deleteOriginalItemForTempUpdate:tempService:clientID:]
+ +[KeychainAccountStorage(SecItem) _newKeychainQueryForService:dsid:]
+ +[KeychainAccountStorage(SecItem) _performKeychainLookupForDSID:appleID:clientID:]
+ +[KeychainAccountStorage(SecItem) _recoverFromRenameFailure:service:clientID:]
+ +[KeychainAccountStorage(SecItem) _renameTemporaryItemToService:tempService:account:clientID:]
+ +[KeychainAccountStorage(SecItem) isUnitTesting]
+ -[AOSContext _scheduleCallbackForTransaction:]
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSUUID
+ _OUTLINED_FUNCTION_8
+ _SecKeychainItemFreeContent
+ __46-[AOSContext _scheduleCallbackForTransaction:]_block_invoke
+ __OBJC_$_CLASS_METHODS_KeychainAccountStorage(Migration|SecKeychain|Proxy|Testing|SecItem)
+ ___46-[AOSContext _scheduleCallbackForTransaction:]_block_invoke
+ ___65+[KeychainAccountStorage(Migration) _isSecItemKeychainAccessible]_block_invoke
+ _isSecItemKeychainAccessible.onceToken
+ _isSecItemKeychainAccessible.sAccessible
+ _kAOSKeychainAccessGroupiCloud
+ _kAOSKeychainServiceMobileMe
+ _kAOSKeychainServiceiCloud
+ _kAOSPrefShouldMigrateKey
+ _kCFBooleanFalse
+ _kSecAttrAccessGroup
+ _kSecAttrAccessible
+ _kSecAttrAccessibleAfterFirstUnlock
+ _kSecAttrComment
+ _kSecReturnAttributes
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_attemptKeychainLookupWithService:dsid:dsidStr:appleID:clientID:attemptNum:
+ _objc_msgSend$_attemptTemporaryServiceUpdate:service:attributes:clientID:
+ _objc_msgSend$_buildRecoveredAttributesFromResult:service:
+ _objc_msgSend$_copyLegacyKeychainItemRefForService:dsid:
+ _objc_msgSend$_createMigratedSecItemForDSID:service:appleID:legacyKeyData:clientID:
+ _objc_msgSend$_createTemporaryItemWithService:attributes:clientID:
+ _objc_msgSend$_deleteLegacyKeychainItemForDSID:service:clientID:
+ _objc_msgSend$_deleteOriginalItemForTempUpdate:tempService:clientID:
+ _objc_msgSend$_extractLegacyKeychainDataForDSID:service:clientID:
+ _objc_msgSend$_finalizeMigrationForDSID:service:clientID:
+ _objc_msgSend$_findLegacyPasswordForService:dsid:clientID:
+ _objc_msgSend$_isBundleIdentifierTrusted:
+ _objc_msgSend$_isCurrentProcessTrustedForKeychainAccess
+ _objc_msgSend$_isMigrationCompleteForDSID:service:
+ _objc_msgSend$_isProcessPathTrusted:
+ _objc_msgSend$_isSecItemKeychainAccessible
+ _objc_msgSend$_isValidSecItemWithService:dsid:clientID:
+ _objc_msgSend$_legacyKeychainItemExistsForDSID:service:
+ _objc_msgSend$_markMigrationCompleteForDSID:service:clientID:
+ _objc_msgSend$_migrateKeyToSecItemForDSID:andAccount:accountInfo:
+ _objc_msgSend$_needsMigrationForDSID:service:
+ _objc_msgSend$_newKeychainQueryForService:dsid:
+ _objc_msgSend$_performKeychainLookupForDSID:appleID:clientID:
+ _objc_msgSend$_performMigrationForDSID:service:appleID:clientID:
+ _objc_msgSend$_performPreflightCanaryCheck
+ _objc_msgSend$_performSecItemLookupWithService:dsid:clientID:
+ _objc_msgSend$_processLegacyKeychainData:length:itemRef:findStatus:clientID:
+ _objc_msgSend$_recoverFromRenameFailure:service:clientID:
+ _objc_msgSend$_renameTemporaryItemToService:tempService:account:clientID:
+ _objc_msgSend$_rollbackMigrationForDSID:service:clientID:
+ _objc_msgSend$_scheduleCallbackForTransaction:
+ _objc_msgSend$_secItemExistsForDSID:service:
+ _objc_msgSend$_testLegacyDataForDSID:service:
+ _objc_msgSend$_validateKeychainDataIntegrity:dsid:clientID:
+ _objc_msgSend$_verifyAndCleanupPreflightCanary:expectedData:
+ _objc_msgSend$_verifyMigrationForDSID:service:clientID:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$executablePath
+ _objc_msgSend$isUnitTesting
+ _objc_msgSend$mainBundle
+ _objc_msgSend$shouldMigrate
+ _objc_opt_new
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sLegacyKeychainLock
+ _sTestLegacyStore
- +[KeychainAccountStorage(SecItem) _attemptKeychainLookupWithService:dsid:dsidStr:clientID:attemptNum:]
- +[KeychainAccountStorage(SecItem) _attemptTemporaryServiceUpdate:service:appleID:encodedKeyData:attributes:clientID:isExistingItemValid:]
- +[KeychainAccountStorage(SecItem) _handleDuplicateItemForService:dsid:appleID:encodedKeyData:attributes:clientID:]
- +[KeychainAccountStorage(SecItem) _handleReAddFailure:tempServiceName:service:appleID:isExistingItemValid:clientID:reAddStatus:]
- +[KeychainAccountStorage(SecItem) _performKeychainLookupForDSID:clientID:]
- __30-[AOSContext scheduleCallback]_block_invoke
- __OBJC_$_CLASS_METHODS_KeychainAccountStorage(SecKeychain|Proxy|Testing|SecItem)
- ___30-[AOSContext scheduleCallback]_block_invoke
- _objc_msgSend$_attemptKeychainLookupWithService:dsid:dsidStr:clientID:attemptNum:
- _objc_msgSend$_attemptTemporaryServiceUpdate:service:appleID:encodedKeyData:attributes:clientID:isExistingItemValid:
- _objc_msgSend$_handleReAddFailure:tempServiceName:service:appleID:isExistingItemValid:clientID:reAddStatus:
- _objc_msgSend$_performKeychainLookupForDSID:clientID:
CStrings:
+ "%@_%@"
+ "%@_temp_%@"
+ "(%@) (%@): Failed to store key, couldn't add kc item, error %d"
+ "(%@) (%@): Failed to store key, data integrity validation failed"
+ "(%@) (%@): Failed to store key, missing required info"
+ "(%@) (%@): No keychain item found, attemptNum=%d"
+ "(%@) (%@): SecItem data present but base64 decode failed (length=%lu)"
+ "(%@) (%@): Validation failed - empty or nil key data"
+ "(%@) (%@): Validation failed - item not found or inaccessible, error %d"
+ "(%@) ACCT LOOKUP: _dsidForAccount: returning nil — could not resolve email user to DSID (isDaemon=%d)"
+ "(%@) Attempting automatic migration for dsid %@"
+ "(%@) Attempting verified migration from SecKeychain to SecItem"
+ "(%@) Direct update failed, error %d"
+ "(%@) Direct update failed, missing required parameters"
+ "(%@) Direct update successful"
+ "(%@) Failed to create SecItem during migration, error %d"
+ "(%@) Failed to create temporary item, error %d"
+ "(%@) Failed to delete legacy keychain item for dsid %@, error %d"
+ "(%@) Failed to delete original item during temp update, error %d"
+ "(%@) Failed to extract legacy keychain data, error %d"
+ "(%@) Failed to rollback migration, error %d"
+ "(%@) Invalid service or dsid for legacy extraction"
+ "(%@) Legacy data is nil or empty, migration aborted"
+ "(%@) Legacy deletion failed for dsid %@ — rolling back migrated SecItem to prevent credential duplication"
+ "(%@) Legacy keychain item failed validation, skipping migration"
+ "(%@) Marked migration as complete for dsid %@"
+ "(%@) Migration already complete for dsid %@, skipping"
+ "(%@) Migration rollback completed"
+ "(%@) Migration successful, data retrieved"
+ "(%@) Migration verification failed - cannot read migrated item, error %d"
+ "(%@) Recovery add failed, error %d"
+ "(%@) Recovery successful after rename failure"
+ "(%@) Rename failed (error %d), attempting recovery"
+ "(%@) Rolling back failed migration for dsid %@"
+ "(%@) Successfully extracted legacy keychain data (%lu bytes)"
+ "(%@) Temporary service update successful"
+ "(%@) Untrusted process attempted SecItem store for dsid %@, rejecting"
+ "(%@) Untrusted process attempted migration write for dsid %@, skipping"
+ "/System/Library/CoreServices/"
+ "/System/Library/Frameworks/Accounts.framework/"
+ "/System/Library/PrivateFrameworks/AOSKit.framework/"
+ "/System/Library/PrivateFrameworks/AuthKit.framework/"
+ "/usr/libexec/"
+ "AOSDisableProcessTrustEnforcement"
+ "AOSKit_Migration_Complete_%@_%@"
+ "AOSKit_Preflight_Canary"
+ "AOSShouldMigrateKeychain"
+ "Legacy keychain item found for dsid %@, migration needed"
+ "Migrated from legacy keychain"
+ "No keychain items found for dsid %@"
+ "Preflight: SecItemAdd failed (%d) — migration will be skipped"
+ "Preflight: SecItemCopyMatching failed (%d) — migration will be skipped"
+ "Preflight: data mismatch — migration will be skipped"
+ "SecItem already exists for dsid %@, no migration needed"
+ "SecItem keychain inaccessible, skipping migration"
+ "Unrecognized process allowed (enforcement disabled): %@ (%@)"
+ "Untrusted process blocked: %@ (%@)"
+ "canary"
+ "com.apple.AuthKitUI"
+ "com.apple.Preferences"
+ "preflight"
+ "shouldMigrate=YES is ignored when useNewAPI=NO — migration only triggers on the SecItem read path"
- "(%@) (%@): Failed to find existing keychain item after duplicate error, error %d <%@>"
- "(%@) (%@): Failed to store key, couldn't modify kc item, move err %d <%@>"
- "(%@) (%@): No kc item found (perhaps because no account has been configured), error %d, attemptNum=%d (userStr=%s) <%@>"
- "(%@) (%@): Re-add of kc item failed (re-add=%d, restore=%d) <%@>"
- "(%@) ACCT LOOKUP: _dsidForAccount: returning nil — could not resolve email user to DSID"
- "NO"
- "Remove Key"
- "Should use New API: %@"
- "YES"
```
