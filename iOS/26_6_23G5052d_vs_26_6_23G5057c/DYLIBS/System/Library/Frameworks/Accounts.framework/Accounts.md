## Accounts

> `/System/Library/Frameworks/Accounts.framework/Accounts`

```diff

-  __TEXT.__text: 0x5ee70
+  __TEXT.__text: 0x5bad0
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0x42ec
+  __TEXT.__objc_methlist: 0x40e4
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x3f18
-  __TEXT.__cstring: 0x3d35
-  __TEXT.__oslogstring: 0x52c8
-  __TEXT.__unwind_info: 0x1c88
-  __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x89b3
-  __TEXT.__objc_methtype: 0x1523
-  __TEXT.__objc_stubs: 0x65a0
-  __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x2520
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__gcc_except_tab: 0x3cc0
+  __TEXT.__cstring: 0x3cf1
+  __TEXT.__oslogstring: 0x4f1d
+  __TEXT.__unwind_info: 0x1bc8
+  __TEXT.__objc_classname: 0x580
+  __TEXT.__objc_methname: 0x87d9
+  __TEXT.__objc_methtype: 0x1447
+  __TEXT.__objc_stubs: 0x64a0
+  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__const: 0x24d8
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2288
+  __DATA_CONST.__objc_selrefs: 0x2228
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x4900
-  __AUTH_CONST.__objc_const: 0x5e40
+  __AUTH_CONST.__cfstring: 0x48c0
+  __AUTH_CONST.__objc_const: 0x5bb8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x558
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x3e0
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x3c4
   __DATA.__data: 0x4d0
   __DATA.__bss: 0x109
   __DATA_DIRTY.__objc_data: 0x730

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1976
-  Symbols:   6848
-  CStrings:  3441
+  Functions: 1919
+  Symbols:   6700
+  CStrings:  3391
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[ACAccountStore setCredentialItemCleanupVolatilityDuration:withCompletion:]
+ -[ACAccountStore triggerCredentialItemCleanupWithCompletion:]
+ GCC_except_table239
+ GCC_except_table251
+ GCC_except_table256
+ GCC_except_table260
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table275
+ GCC_except_table282
+ GCC_except_table287
+ GCC_except_table296
+ GCC_except_table299
+ GCC_except_table311
+ GCC_except_table315
+ GCC_except_table321
+ GCC_except_table326
+ GCC_except_table333
+ GCC_except_table339
+ GCC_except_table343
+ GCC_except_table350
+ GCC_except_table357
+ GCC_except_table369
+ GCC_except_table379
+ GCC_except_table402
+ GCC_except_table408
+ ___61-[ACAccountStore triggerCredentialItemCleanupWithCompletion:]_block_invoke
+ ___61-[ACAccountStore triggerCredentialItemCleanupWithCompletion:]_block_invoke_2
+ ___61-[ACAccountStore triggerCredentialItemCleanupWithCompletion:]_block_invoke_3
+ ___76-[ACAccountStore setCredentialItemCleanupVolatilityDuration:withCompletion:]_block_invoke
+ ___76-[ACAccountStore setCredentialItemCleanupVolatilityDuration:withCompletion:]_block_invoke_2
+ ___76-[ACAccountStore setCredentialItemCleanupVolatilityDuration:withCompletion:]_block_invoke_3
+ ___block_descriptor_48_e8_32bs_e40_v16?0"<ACRemoteAccountStoreProtocol>"8ls32l8
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
- GCC_except_table238
- GCC_except_table241
- GCC_except_table250
- GCC_except_table254
- GCC_except_table259
- GCC_except_table264
- GCC_except_table271
- GCC_except_table276
- GCC_except_table280
- GCC_except_table283
- GCC_except_table286
- GCC_except_table289
- GCC_except_table295
- GCC_except_table312
- GCC_except_table316
- GCC_except_table319
- GCC_except_table322
- GCC_except_table327
- GCC_except_table331
- GCC_except_table335
- GCC_except_table341
- GCC_except_table346
- GCC_except_table353
- GCC_except_table359
- GCC_except_table370
- GCC_except_table377
- GCC_except_table399
- GCC_except_table403
- GCC_except_table409
- GCC_except_table414
- GCC_except_table420
- _ACProtobufCredentialItemReadFrom
- _OBJC_CLASS_$_ACProtobufCredentialItem
- _OBJC_IVAR_$_ACProtobufCredentialItem._accountIdentifier
- _OBJC_IVAR_$_ACProtobufCredentialItem._dirtyProperties
- _OBJC_IVAR_$_ACProtobufCredentialItem._expirationDate
- _OBJC_IVAR_$_ACProtobufCredentialItem._has
- _OBJC_IVAR_$_ACProtobufCredentialItem._isPersistent
- _OBJC_IVAR_$_ACProtobufCredentialItem._objectID
- _OBJC_IVAR_$_ACProtobufCredentialItem._serviceName
- _OBJC_METACLASS_$_ACProtobufCredentialItem
- _OUTLINED_FUNCTION_14
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
- ___61-[ACAccountStore insertCredentialItem:withCompletionHandler:]_block_invoke_3
- ___61-[ACAccountStore removeCredentialItem:withCompletionHandler:]_block_invoke
- ___61-[ACAccountStore removeCredentialItem:withCompletionHandler:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e38_v24?0"ACCredentialItem"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40r_e38_v24?0"ACCredentialItem"8"NSError"16lr40l8s32l8
- ___block_descriptor_72_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls32l8s48l8s40l8
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
