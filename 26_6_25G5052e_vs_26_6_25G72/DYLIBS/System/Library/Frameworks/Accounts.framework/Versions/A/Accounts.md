## Accounts

> `/System/Library/Frameworks/Accounts.framework/Versions/A/Accounts`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1037.0.0.0.0
-  __TEXT.__text: 0x648c0
+1038.0.0.0.0
+  __TEXT.__text: 0x612b4
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x42d4
+  __TEXT.__objc_methlist: 0x40cc
   __TEXT.__const: 0x190
-  __TEXT.__gcc_except_tab: 0x3f94
-  __TEXT.__cstring: 0x3db0
-  __TEXT.__oslogstring: 0x536c
-  __TEXT.__unwind_info: 0x1cd0
-  __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x89d3
-  __TEXT.__objc_methtype: 0x1523
-  __TEXT.__objc_stubs: 0x65c0
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0xf08
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__gcc_except_tab: 0x3d34
+  __TEXT.__cstring: 0x3d6c
+  __TEXT.__oslogstring: 0x4fc1
+  __TEXT.__unwind_info: 0x1c18
+  __TEXT.__objc_classname: 0x580
+  __TEXT.__objc_methname: 0x87f9
+  __TEXT.__objc_methtype: 0x1447
+  __TEXT.__objc_stubs: 0x64c0
+  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__const: 0xf10
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2288
+  __DATA_CONST.__objc_selrefs: 0x2228
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x5b0
-  __AUTH_CONST.__const: 0x1c80
-  __AUTH_CONST.__cfstring: 0x49a0
-  __AUTH_CONST.__objc_const: 0x5e40
+  __AUTH_CONST.__const: 0x1c20
+  __AUTH_CONST.__cfstring: 0x4960
+  __AUTH_CONST.__objc_const: 0x5bb8
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x3e0
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x3c4
   __DATA.__data: 0x4d0
   __DATA.__bss: 0x139
   __DATA_DIRTY.__objc_data: 0x730

   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2024
-  Symbols:   4409
-  CStrings:  2787
+  Functions: 1967
+  Symbols:   4330
+  CStrings:  2740
 
Symbols:
+ -[ACAccountStore setCredentialItemCleanupVolatilityDuration:withCompletion:]
+ -[ACAccountStore triggerCredentialItemCleanupWithCompletion:]
+ GCC_except_table274
+ GCC_except_table286
+ GCC_except_table291
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table301
+ GCC_except_table304
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table317
+ GCC_except_table322
+ GCC_except_table331
+ GCC_except_table334
+ GCC_except_table346
+ GCC_except_table350
+ GCC_except_table356
+ GCC_except_table361
+ GCC_except_table368
+ GCC_except_table374
+ GCC_except_table378
+ GCC_except_table385
+ GCC_except_table392
+ GCC_except_table404
+ GCC_except_table414
+ GCC_except_table437
+ GCC_except_table443
+ __76-[ACAccountStore setCredentialItemCleanupVolatilityDuration:withCompletion:]_block_invoke
+ ___61-[ACAccountStore triggerCredentialItemCleanupWithCompletion:]_block_invoke
+ ___61-[ACAccountStore triggerCredentialItemCleanupWithCompletion:]_block_invoke_2
+ ___61-[ACAccountStore triggerCredentialItemCleanupWithCompletion:]_block_invoke_3
+ ___76-[ACAccountStore setCredentialItemCleanupVolatilityDuration:withCompletion:]_block_invoke
+ ___76-[ACAccountStore setCredentialItemCleanupVolatilityDuration:withCompletion:]_block_invoke_2
+ ___block_descriptor_48_e8_32bs_e40_v16?0"<ACRemoteAccountStoreProtocol>"8l
+ _kACDAccountsTestingEntitlement
+ _objc_msgSend$setCredentialItemCleanupVolatilityDuration:withCompletion:
+ _objc_msgSend$triggerCredentialItemCleanupWithCompletion:
- +[ACProtobufCredentialItem dirtyPropertiesType]
- -[ACAccountStore allCredentialItems]
- -[ACAccountStore credentialItemForAccount:serviceName:]
- -[ACAccountStore insertCredentialItem:withCompletionHandler:]
- -[ACAccountStore removeCredentialItem:withCompletionHandler:]
- -[ACAccountStore saveCredentialItem:withCompletionHandler:]
- -[ACCredentialItem _encodeProtobufData]
- -[ACCredentialItem _encodeProtobuf]
- -[ACCredentialItem _initWithProtobuf:]
- -[ACCredentialItem _initWithProtobufData:]
- -[ACProtobufCredentialItem .cxx_destruct]
- -[ACProtobufCredentialItem accountIdentifier]
- -[ACProtobufCredentialItem addDirtyProperties:]
- -[ACProtobufCredentialItem clearDirtyProperties]
- -[ACProtobufCredentialItem copyTo:]
- -[ACProtobufCredentialItem copyWithZone:]
- -[ACProtobufCredentialItem description]
- -[ACProtobufCredentialItem dictionaryRepresentation]
- -[ACProtobufCredentialItem dirtyPropertiesAtIndex:]
- -[ACProtobufCredentialItem dirtyPropertiesCount]
- -[ACProtobufCredentialItem dirtyProperties]
- -[ACProtobufCredentialItem expirationDate]
- -[ACProtobufCredentialItem hasExpirationDate]
- -[ACProtobufCredentialItem hasIsPersistent]
- -[ACProtobufCredentialItem hasObjectID]
- -[ACProtobufCredentialItem hash]
- -[ACProtobufCredentialItem isEqual:]
- -[ACProtobufCredentialItem isPersistent]
- -[ACProtobufCredentialItem mergeFrom:]
- -[ACProtobufCredentialItem objectID]
- -[ACProtobufCredentialItem readFrom:]
- -[ACProtobufCredentialItem serviceName]
- -[ACProtobufCredentialItem setAccountIdentifier:]
- -[ACProtobufCredentialItem setDirtyProperties:]
- -[ACProtobufCredentialItem setExpirationDate:]
- -[ACProtobufCredentialItem setHasIsPersistent:]
- -[ACProtobufCredentialItem setIsPersistent:]
- -[ACProtobufCredentialItem setObjectID:]
- -[ACProtobufCredentialItem setServiceName:]
- -[ACProtobufCredentialItem writeTo:]
- GCC_except_table273
- GCC_except_table276
- GCC_except_table285
- GCC_except_table289
- GCC_except_table294
- GCC_except_table299
- GCC_except_table306
- GCC_except_table311
- GCC_except_table315
- GCC_except_table318
- GCC_except_table321
- GCC_except_table324
- GCC_except_table330
- GCC_except_table347
- GCC_except_table351
- GCC_except_table354
- GCC_except_table357
- GCC_except_table362
- GCC_except_table366
- GCC_except_table370
- GCC_except_table376
- GCC_except_table381
- GCC_except_table388
- GCC_except_table394
- GCC_except_table405
- GCC_except_table412
- GCC_except_table434
- GCC_except_table438
- GCC_except_table444
- GCC_except_table449
- GCC_except_table455
- OBJC_IVAR_$_ACProtobufCredentialItem._accountIdentifier
- OBJC_IVAR_$_ACProtobufCredentialItem._dirtyProperties
- OBJC_IVAR_$_ACProtobufCredentialItem._expirationDate
- OBJC_IVAR_$_ACProtobufCredentialItem._has
- OBJC_IVAR_$_ACProtobufCredentialItem._isPersistent
- OBJC_IVAR_$_ACProtobufCredentialItem._objectID
- OBJC_IVAR_$_ACProtobufCredentialItem._serviceName
- _ACProtobufCredentialItemReadFrom
- _OBJC_CLASS_$_ACProtobufCredentialItem
- _OBJC_METACLASS_$_ACProtobufCredentialItem
- __36-[ACAccountStore allCredentialItems]_block_invoke_2
- __55-[ACAccountStore credentialItemForAccount:serviceName:]_block_invoke_2
- __59-[ACAccountStore saveCredentialItem:withCompletionHandler:]_block_invoke
- __61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke
- __61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke_2
- __61-[ACAccountStore removeCredentialItem:withCompletionHandler:]_block_invoke
- __OBJC_$_CLASS_METHODS_ACProtobufCredentialItem
- __OBJC_$_INSTANCE_METHODS_ACProtobufCredentialItem
- __OBJC_$_INSTANCE_VARIABLES_ACProtobufCredentialItem
- __OBJC_$_PROP_LIST_ACProtobufCredentialItem
- __OBJC_CLASS_PROTOCOLS_$_ACProtobufCredentialItem
- __OBJC_CLASS_RO_$_ACProtobufCredentialItem
- __OBJC_METACLASS_RO_$_ACProtobufCredentialItem
- ___36-[ACAccountStore allCredentialItems]_block_invoke
- ___36-[ACAccountStore allCredentialItems]_block_invoke_2
- ___55-[ACAccountStore credentialItemForAccount:serviceName:]_block_invoke
- ___55-[ACAccountStore credentialItemForAccount:serviceName:]_block_invoke_2
- ___59-[ACAccountStore saveCredentialItem:withCompletionHandler:]_block_invoke
- ___59-[ACAccountStore saveCredentialItem:withCompletionHandler:]_block_invoke_2
- ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke
- ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke_2
- ___61-[ACAccountStore removeCredentialItem:withCompletionHandler:]_block_invoke
- ___61-[ACAccountStore removeCredentialItem:withCompletionHandler:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e38_v24?0"ACCredentialItem"8"NSError"16l
- ___block_descriptor_48_e8_32s40r_e38_v24?0"ACCredentialItem"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16l
- _objc_msgSend$credentialItemForAccount:serviceName:completion:
- _objc_msgSend$credentialItemsWithCompletion:
- _objc_msgSend$hasExpirationDate
- _objc_msgSend$insertCredentialItem:completion:
- _objc_msgSend$removeCredentialItem:completion:
- _objc_msgSend$saveCredentialItem:completion:
- _objc_msgSend$setAccountIdentifier:
- _objc_msgSend$setExpirationDate:
- _objc_msgSend$setIsPersistent:
- _objc_msgSend$setServiceName:
CStrings:
+ "com.apple.private.accounts.testing"
+ "setCredentialItemCleanupVolatilityDuration:withCompletion:"
+ "triggerCredentialItemCleanupWithCompletion:"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?B@\"NSError\">24"
- "\"Calling daemon to save a credential item\""
- "\"Credential item %@ associated with store %@, inserting credential item on store %@\""
- "ACCredentialItem.m"
- "ACProtobufCredentialItem"
- "AllCredentialItems"
- "BEGIN [%lld]: AllCredentialItems "
- "BEGIN [%lld]: CredentialItemsForAccountWithServiceName %@ : %@"
- "BEGIN [%lld]: InsertCredentialItem %@"
- "BEGIN [%lld]: RemoveCredentialItem %@"
- "BEGIN [%lld]: SaveCredentialItem %@"
- "Credential item must be non-nil"
- "CredentialItemsForAccountWithServiceName"
- "END [%lld] %fs: AllCredentialItems %@%@"
- "END [%lld] %fs: CredentialItemsForAccountWithServiceName %@%@"
- "END [%lld] %fs: InsertCredentialItem %@%@"
- "END [%lld] %fs: RemoveCredentialItem %@%@"
- "END [%lld] %fs: RemoveCredentialItem %{public}@"
- "END [%lld] %fs: SaveCredentialItem %@%@"
- "END [%lld] %fs: SaveCredentialItem %{public}@"
- "InsertCredentialItem"
- "RemoveCredentialItem"
- "SaveCredentialItem"
- "T@\"ACProtobufDate\",&,N,V_expirationDate"
- "T@\"NSString\",&,N,V_accountIdentifier"
- "T@\"NSString\",&,N,V_serviceName"
- "TB,N,V_isPersistent"
- "_isPersistent"
- "accounts/all-credential-items"
- "accounts/credential-item-for-account"
- "accounts/insert-credential-item"
- "accounts/remove-credential-item"
- "accounts/save-credential-item"
- "allCredentialItems"
- "credentialItemForAccount:serviceName:"
- "credentialItemForAccount:serviceName:completion:"
- "credentialItemsWithCompletion:"
- "hasExpirationDate"
- "hasIsPersistent"
- "insertCredentialItem:completion:"
- "insertCredentialItem:withCompletionHandler:"
- "removeCredentialItem:completion:"
- "removeCredentialItem:withCompletionHandler:"
- "saveCredentialItem:completion:"
- "saveCredentialItem:withCompletionHandler:"
- "setHasIsPersistent:"
- "setIsPersistent:"
- "v24@?0@\"ACCredentialItem\"8@\"NSError\"16"
- "v32@0:8@\"ACCredentialItem\"16@?<v@?@\"ACCredentialItem\"@\"NSError\">24"
- "v32@0:8@\"ACCredentialItem\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v32@0:8@\"ACCredentialItem\"16@?<v@?B@\"NSError\">24"
- "v40@0:8@\"ACAccount\"16@\"NSString\"24@?<v@?@\"ACCredentialItem\"@\"NSError\">32"
- "{?=\"isPersistent\"b1}"
```
