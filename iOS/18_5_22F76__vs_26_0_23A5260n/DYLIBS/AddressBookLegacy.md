## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12828.500.41.0.0
-  __TEXT.__text: 0x736cc
-  __TEXT.__auth_stubs: 0x21e0
-  __TEXT.__objc_methlist: 0x2f9c
-  __TEXT.__const: 0x369
-  __TEXT.__cstring: 0x26160
-  __TEXT.__oslogstring: 0x2259
+12846.100.1.0.0
+  __TEXT.__text: 0x74b5c
+  __TEXT.__auth_stubs: 0x21f0
+  __TEXT.__objc_methlist: 0x2fa4
+  __TEXT.__const: 0x331
+  __TEXT.__cstring: 0x265c4
+  __TEXT.__oslogstring: 0x23f5
   __TEXT.__gcc_except_tab: 0x618
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x18c0
+  __TEXT.__unwind_info: 0x1910
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x915f
+  __TEXT.__objc_methname: 0x91aa
   __TEXT.__objc_methtype: 0x1454
   __TEXT.__objc_stubs: 0x7b80
-  __DATA_CONST.__got: 0x5b8
-  __DATA_CONST.__const: 0x26d0
+  __DATA_CONST.__got: 0x5b0
+  __DATA_CONST.__const: 0x27d8
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x24c0
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x1100
-  __AUTH_CONST.__const: 0xe10
-  __AUTH_CONST.__cfstring: 0xd7e0
-  __AUTH_CONST.__objc_const: 0x4b10
+  __AUTH_CONST.__auth_got: 0x1108
+  __AUTH_CONST.__const: 0xe40
+  __AUTH_CONST.__cfstring: 0xd940
+  __AUTH_CONST.__objc_const: 0x4b40
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x3f0
-  __DATA.__data: 0x2c0
+  __AUTH.__objc_data: 0xaa0
+  __DATA.__objc_ivar: 0x3f4
+  __DATA.__data: 0x2c8
   __DATA.__common: 0x4
   __DATA.__bss: 0x338
-  __DATA_DIRTY.__objc_data: 0x550
+  __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0x128
-  __DATA_DIRTY.__bss: 0xf8
-  __DATA_DIRTY.__common: 0x38c
+  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__common: 0x398
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 17F51BFF-6088-3FA2-A1D6-19A9B9440B32
-  Functions: 2482
-  Symbols:   7067
-  CStrings:  5996
+  UUID: 6CDC8FE9-72CF-3E66-A56C-9D3ED246053E
+  Functions: 2512
+  Symbols:   7112
+  CStrings:  6029
 
Symbols:
+ -[ABBufferQuery requestedAvatarRecipeData]
+ GCC_except_table134
+ GCC_except_table55
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table69
+ _ABAddressBookCopyArrayOfInternalUUIDsOfPeopleWithWallpaper
+ _ABAddressBookCopyPersonInternalUUIDForUnifiedIdentifier
+ _ABAddressBookCopyRecordIDsOfPeopleWithAvatarRecipes
+ _ABAddressBookCopyWallpaperMigrationDataForInternalUUID
+ _ABCAvatarRecipeClass
+ _ABCAvatarRecipeDataProperty
+ _ABCAvatarRecipeProperties
+ _ABCAvatarRecipeRecordIDProperty
+ _ABCImageStoreCopyAvatarRecipeDataForRecord
+ _ABCImageStoreRemoveAvatarRecipeDataForRecord
+ _ABCPersonClearAvatarRecipeData
+ _ABCPersonCopyAvatarRecipeData
+ _ABCPersonSetAvatarRecipeData
+ _ABPersonClearAvatarRecipeData
+ _ABPersonCopyAvatarRecipeData
+ _ABPersonCreateSmartDialerLastFourDigitsStringForIndexing
+ _ABPersonCreateSmartDialerLatinStringFromCFString
+ _ABPersonCreateSmartDialerStringFromCFString
+ _ABPersonSetAvatarRecipeData
+ _OBJC_IVAR_$_ABBufferQuery._requestedAvatarRecipeData
+ _TINumberPadGetEncodedString
+ __ABCAvatarRecipeClass
+ __ABCLogMutatedSharedPhotoPreferenceForUpdatedPersonApplier
+ ___ABAddressBookPersonBufferRowHandler_block_invoke.524
+ ___block_literal_global.361
+ ___block_literal_global.404
+ ___block_literal_global.406
+ ___block_literal_global.408
+ __accumulateABRecordIDPtrs
+ __accumulateInternalUUIDs
+ __copyDataRefForStatementColumn
+ __logUpdatesMutatingSharedPhotoPreference
+ __recreateIndexes
+ _avatarRecipeCallbacks
+ _kABCPersonAvatarRecipeDataProperty
+ _objc_msgSend$requestedAvatarRecipeData
+ _saveAvatarRecipeData
- GCC_except_table133
- GCC_except_table52
- GCC_except_table57
- GCC_except_table66
- _ABFavoritesEntryIdentityChangedNotification
- __LetterNumberMap
- ___ABAddressBookPersonBufferRowHandler_block_invoke.520
- ___block_literal_global.346
- ___block_literal_global.391
- ___block_literal_global.393
- ___block_literal_global.395
- _kCFStringTransformStripDiacritics
- _objc_msgSend$initWithInt:
CStrings:
+ "ABAvatarRecipe"
+ "ABCPerson ABCPersonCopyAvatarRecipeData() fetched no instances of avatarRecipeData for contact identifier (%{public}@)"
+ "ABCPerson ABCPersonSetAvatarRecipeData() fetched no instances of avatarRecipeData for contact identifier (%{public}@)"
+ "AvatarRecipeData"
+ "AvatarRecipeData empty or non-array of type %lu (array is %lu)"
+ "CFArrayRef ABAddressBookCopyArrayOfInternalUUIDsOfPeopleWithWallpaper(ABAddressBookRef)"
+ "CFArrayRef ABAddressBookCopyRecordIDsOfPeopleWithAvatarRecipes(ABAddressBookRef)"
+ "CFDataRef ABPersonCopyAvatarRecipeData(ABRecordRef)"
+ "CREATE TABLE ABAvatarRecipe(record_id, data);"
+ "CREATE UNIQUE INDEX IF NOT EXISTS ABAvatarRecipeRecordIDIndex ON ABAvatarRecipe(record_id);"
+ "CREATE VIRTUAL TABLE IF NOT EXISTS ABPersonSmartDialerFullTextSearch USING fts4(tokenize=ab_cf_tokenizer language=\"en\" %@, FirstEncoding, MiddleEncoding, LastEncoding, OrganizationEncoding, NicknameEncoding, PhoneLastFourDigits);"
+ "CopyPosterDataToMetadataStore"
+ "PhoneLastFourDigits"
+ "SELECT ROWID FROM ABAvatarRecipe WHERE record_id = ?;"
+ "SELECT ROWID, record_id, data FROM ABAvatarRecipe WHERE record_id = ?;"
+ "SELECT Wallpaper, WallpaperMetadata, WatchWallpaperImageData, ExternalUUID from ABPerson where guid = ?;"
+ "SELECT abp.guid from ABPerson abp JOIN ABPersonLink abl ON abp.PersonLink = abl.ROWID WHERE (abl.guid = ? AND abl.PreferredImagePersonID = abp.ROWID);"
+ "SELECT abp.guid from ABPerson abp JOIN ABPersonLink abl ON abp.PersonLink = abl.ROWID WHERE (abl.guid = ? AND abl.PreferredNamePersonID = abp.ROWID);"
+ "SELECT guid from ABPerson where Wallpaper NOT NULL;"
+ "SELECT record_id FROM ABAvatarRecipe INDEXED BY ABAvatarRecipeRecordIDIndex WHERE record_id = 1;"
+ "SELECT record_id FROM ABAvatarRecipe WHERE data IS NOT NULL;"
+ "TB,R,N,V_requestedAvatarRecipeData"
+ "[Shared Photo Display Preference] Updating an ABPerson's sharedPhotoDisplayPreference from %#lo to %#lo, id: %d"
+ "_Bool ABPersonClearAvatarRecipeData(ABRecordRef)"
+ "_Bool ABPersonSetAvatarRecipeData(ABRecordRef, CFDataRef)"
+ "_requestedAvatarRecipeData"
+ "requestedAvatarRecipeData"
- "CFStringRef ABPersonCreateSmartDialerStringForIndexingFromCFString(CFStringRef)"
- "CNFavoritesEntryIdentityChangedNotification"
- "CREATE VIRTUAL TABLE IF NOT EXISTS ABPersonSmartDialerFullTextSearch USING fts4(tokenize=ab_cf_tokenizer language=\"en\" %@, FirstEncoding, MiddleEncoding, LastEncoding, OrganizationEncoding, NicknameEncoding);"
- "Smart dialer stripDiacritics transform failure for string: %@"
- "initWithInt:"

```
