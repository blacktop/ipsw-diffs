## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-622.1.22.10.9
-  __TEXT.__text: 0x119c7c
-  __TEXT.__auth_stubs: 0x2e00
-  __TEXT.__objc_methlist: 0xb584
-  __TEXT.__const: 0x29a4
-  __TEXT.__gcc_except_tab: 0x6574
-  __TEXT.__cstring: 0x11b75
+622.2.5.10.3
+  __TEXT.__text: 0x11b178
+  __TEXT.__auth_stubs: 0x2ea0
+  __TEXT.__objc_methlist: 0xb62c
+  __TEXT.__const: 0x2a14
+  __TEXT.__gcc_except_tab: 0x66d0
+  __TEXT.__cstring: 0x11c35
   __TEXT.__ustring: 0x2810
-  __TEXT.__oslogstring: 0xa0ed
+  __TEXT.__oslogstring: 0x9edd
   __TEXT.__dlopen_cstrs: 0x19b
-  __TEXT.__swift5_typeref: 0xd38
+  __TEXT.__swift5_typeref: 0xd42
   __TEXT.__swift5_fieldmd: 0x804
   __TEXT.__constg_swiftt: 0x854
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_reflstr: 0x619
   __TEXT.__swift5_assocty: 0x1e0
   __TEXT.__swift5_capture: 0x578
-  __TEXT.__swift5_proto: 0x1e0
+  __TEXT.__swift5_proto: 0x1e8
   __TEXT.__swift5_types: 0xb8
   __TEXT.__swift_as_entry: 0xd0
   __TEXT.__swift_as_ret: 0xbc
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5fa0
-  __TEXT.__eh_frame: 0x2d28
-  __TEXT.__objc_classname: 0x19b3
-  __TEXT.__objc_methname: 0x23aa6
-  __TEXT.__objc_methtype: 0x3d7e
-  __TEXT.__objc_stubs: 0x114a0
-  __DATA_CONST.__got: 0xdf0
-  __DATA_CONST.__const: 0x4dd0
-  __DATA_CONST.__objc_classlist: 0x5c8
+  __TEXT.__unwind_info: 0x6008
+  __TEXT.__eh_frame: 0x2d30
+  __TEXT.__objc_classname: 0x19d8
+  __TEXT.__objc_methname: 0x23d1d
+  __TEXT.__objc_methtype: 0x3db9
+  __TEXT.__objc_stubs: 0x11600
+  __DATA_CONST.__got: 0xdf8
+  __DATA_CONST.__const: 0x4e40
+  __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x168
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68f0
+  __DATA_CONST.__objc_selrefs: 0x6958
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x478
+  __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__objc_arraydata: 0x2790
-  __AUTH_CONST.__auth_got: 0x1718
-  __AUTH_CONST.__const: 0x4bc8
-  __AUTH_CONST.__cfstring: 0x18540
-  __AUTH_CONST.__objc_const: 0x12a48
+  __AUTH_CONST.__auth_got: 0x1768
+  __AUTH_CONST.__const: 0x4c38
+  __AUTH_CONST.__cfstring: 0x185a0
+  __AUTH_CONST.__objc_const: 0x12b90
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x23e8
+  __AUTH.__objc_data: 0x2438
   __AUTH.__data: 0x480
-  __DATA.__objc_ivar: 0xbbc
-  __DATA.__data: 0x1670
-  __DATA.__bss: 0x3ea0
+  __DATA.__objc_ivar: 0xbc4
+  __DATA.__data: 0x1678
+  __DATA.__bss: 0x3fb0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1730
   __DATA_DIRTY.__data: 0x1c8

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 431B4093-C041-38BA-93DD-64FB63F9F025
-  Functions: 6753
-  Symbols:   18515
-  CStrings:  12466
+  UUID: 0E3A8BC5-BAD3-3E63-A6C8-BA45AF0F6651
+  Functions: 6767
+  Symbols:   18562
+  CStrings:  12489
 
Symbols:
+ -[NSFileManager(SafariNSFileManagerExtras) safari_getFileExists:atSubpath:relativeToFileHandle:error:]
+ -[NSFileManager(SafariNSFileManagerExtras) safari_getFileSystemSupportsExclusiveRename:atFileHandle:error:]
+ -[NSString(SafariCoreExtras) safari_displayableTabBarTitleString]
+ -[NSString(SafariCoreExtras) safari_stringByReplacingCharacterSetsInContainer:]
+ -[NSURL(SafariCoreExtras) safari_URLByNormalizingBlobURL]
+ -[NSURL(SafariCoreExtras) safari_isBlobURL]
+ -[NSUserDefaults(SafariCoreExtras) safari_integerForKey:defaultValue:]
+ -[WBSCharacterSetReplacementsContainer .cxx_destruct]
+ -[WBSCharacterSetReplacementsContainer allCharacters]
+ -[WBSCharacterSetReplacementsContainer copyWithZone:]
+ -[WBSCharacterSetReplacementsContainer enumerateCharacterSetReplacementStringPairsUsingBlock:]
+ -[WBSCharacterSetReplacementsContainer hash]
+ -[WBSCharacterSetReplacementsContainer initWithReplacementStringsToCharacterSets:]
+ -[WBSCharacterSetReplacementsContainer isEqual:]
+ -[WBSCharacterSetReplacementsContainer replacementStringsToCharacterSets]
+ GCC_except_table156
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table163
+ GCC_except_table41
+ GCC_except_table53
+ GCC_except_table66
+ GCC_except_table73
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table98
+ _OBJC_CLASS_$_WBSCharacterSetReplacementsContainer
+ _OBJC_IVAR_$_WBSCharacterSetReplacementsContainer._allCharacters
+ _OBJC_IVAR_$_WBSCharacterSetReplacementsContainer._replacementStringsToCharacterSets
+ _OBJC_IVAR_$_WBSPasswordManagerWebsiteMetadataStore._metadataEntryLock
+ _OBJC_METACLASS_$_WBSCharacterSetReplacementsContainer
+ __OBJC_$_INSTANCE_METHODS_WBSCharacterSetReplacementsContainer
+ __OBJC_$_INSTANCE_VARIABLES_WBSCharacterSetReplacementsContainer
+ __OBJC_$_PROP_LIST_WBSCharacterSetReplacementsContainer
+ __OBJC_CLASS_PROTOCOLS_$_WBSCharacterSetReplacementsContainer
+ __OBJC_CLASS_RO_$_WBSCharacterSetReplacementsContainer
+ __OBJC_METACLASS_RO_$_WBSCharacterSetReplacementsContainer
+ __ZGVZ65-[NSString(SafariCoreExtras) safari_displayableTabBarTitleString]E12replacements
+ __ZZ65-[NSString(SafariCoreExtras) safari_displayableTabBarTitleString]E12replacements
+ ___102-[NSURLCredentialStorage(SafariCoreExtras) _safari_migrateKeychainItemsWithInvalidAuthenticationTypes]_block_invoke.94
+ ___102-[NSURLCredentialStorage(SafariCoreExtras) _safari_migrateKeychainItemsWithInvalidAuthenticationTypes]_block_invoke.94.cold.1
+ ___38-[WBSOngoingSharingGroupProvider init]_block_invoke.18
+ ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke.32
+ ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke.40
+ ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke_2.37
+ ___79-[NSString(SafariCoreExtras) safari_stringByReplacingCharacterSetsInContainer:]_block_invoke
+ ___79-[WBSOngoingSharingGroupProvider _fetchCurrentUserParticipantIDWithCompletion:]_block_invoke.25
+ ___79-[WBSOngoingSharingGroupProvider _fetchCurrentUserParticipantIDWithCompletion:]_block_invoke.25.cold.1
+ ___82-[WBSCharacterSetReplacementsContainer initWithReplacementStringsToCharacterSets:]_block_invoke
+ ___94-[WBSCharacterSetReplacementsContainer enumerateCharacterSetReplacementStringPairsUsingBlock:]_block_invoke
+ ___Block_byref_object_copy_.69
+ ___Block_byref_object_dispose_.70
+ ___block_descriptor_40_e8_32bs_e41_v32?0"NSString"8"NSCharacterSet"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e41_v32?0"NSString"8"NSCharacterSet"16^B24ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e58_v16?0"<WBSPasswordManagerWebsiteMetadataEntryProtocol>"8ls32l8r48l8s40l8
+ ___block_descriptor_72_ea8_32s40r48r_e41_v32?0"NSCharacterSet"8"NSString"16^B24ls32l8r40l8r48l8
+ ___block_literal_global.139
+ ___block_literal_global.3154
+ ___block_literal_global.36
+ ___block_literal_global.39
+ ___block_literal_global.42
+ ___block_literal_global.6
+ ___block_literal_global.63
+ ___block_literal_global.68
+ _block_copy_helper.153
+ _block_copy_helper.162
+ _block_copy_helper.165
+ _block_copy_helper.168
+ _block_copy_helper.172
+ _block_copy_helper.77
+ _block_copy_helper.99
+ _block_descriptor.101
+ _block_descriptor.155
+ _block_descriptor.164
+ _block_descriptor.167
+ _block_descriptor.170
+ _block_descriptor.174
+ _block_descriptor.79
+ _block_destroy_helper.100
+ _block_destroy_helper.154
+ _block_destroy_helper.163
+ _block_destroy_helper.166
+ _block_destroy_helper.169
+ _block_destroy_helper.173
+ _block_destroy_helper.78
+ _fgetattrlist
+ _fstatat
+ _objc_msgSend$URLWithDataRepresentation:relativeToURL:
+ _objc_msgSend$allCharacters
+ _objc_msgSend$dataRepresentation
+ _objc_msgSend$enumerateCharacterSetReplacementStringPairsUsingBlock:
+ _objc_msgSend$formUnionWithCharacterSet:
+ _objc_msgSend$initWithReplacementStringsToCharacterSets:
+ _objc_msgSend$safari_getFileExists:atSubpath:relativeToFileHandle:error:
+ _objc_msgSend$safari_getFileSystemSupportsExclusiveRename:atFileHandle:error:
+ _objc_msgSend$safari_isBlobURL
+ _objc_msgSend$safari_lockRelatedEmojiCharacterSet
+ _objc_msgSend$safari_stringByReplacingCharacterSetsInContainer:
+ _objc_msgSend$sourceIdentifier
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:options:range:
+ _objectdestroy.119Tm
+ _objectdestroy.23Tm
+ _objectdestroy.32Tm
+ _objectdestroy.65Tm
+ _symbolic _____ySJG s11_SetStorageC
- -[NSURLCredentialStorage(SafariCoreExtras) _safari_setSidecarDictionary:type:credential:htmlFormProtectionSpace:groupID:fromRecentlyDeleted:].cold.5
- -[NSURLCredentialStorage(SafariCoreExtras) safari_deleteCredentialWithEmptyServerHostForUser:forHTMLFormProtectionSpace:forGroupID:fromRecentlyDeleted:].cold.3
- -[NSURLCredentialStorage(SafariCoreExtras) safari_deletePasskeyFromSavedAccount:groupID:].cold.4
- -[NSURLCredentialStorage(SafariCoreExtras) safari_deletePasswordCredentialForUser:forHTMLFormProtectionSpace:forGroupID:fromRecentlyDeleted:].cold.4
- -[NSURLCredentialStorage(SafariCoreExtras) safari_deleteSidecarOfType:forUser:htmlFormProtectionSpace:forGroupID:fromRecentlyDeleted:].cold.4
- -[NSURLCredentialStorage(SafariCoreExtras) safari_setCredential:forHTMLFormProtectionSpace:forGroupID:].cold.3
- -[NSURLCredentialStorage(SafariCoreExtras) safari_setSidecar:credential:htmlFormProtectionSpace:forGroupID:fromRecentlyDeleted:].cold.1
- -[WBSOngoingSharingGroupProvider _updateCachedPermissionLevelsForCurrentUser]
- -[WBSOngoingSharingGroupProvider canCurrentUserEditSavedAccountsInGroupWithID:]
- GCC_except_table167
- GCC_except_table169
- GCC_except_table74
- GCC_except_table78
- GCC_except_table90
- GCC_except_table91
- GCC_except_table92
- GCC_except_table93
- _OBJC_IVAR_$_WBSOngoingSharingGroupProvider._groupIDToPermissionLevelForCurrentUser
- _OUTLINED_FUNCTION_22
- ___102-[NSURLCredentialStorage(SafariCoreExtras) _safari_migrateKeychainItemsWithInvalidAuthenticationTypes]_block_invoke.92
- ___102-[NSURLCredentialStorage(SafariCoreExtras) _safari_migrateKeychainItemsWithInvalidAuthenticationTypes]_block_invoke.92.cold.1
- ___38-[WBSOngoingSharingGroupProvider init]_block_invoke.19
- ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke.34
- ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke.41
- ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke_2.38
- ___77-[WBSOngoingSharingGroupProvider _updateCachedPermissionLevelsForCurrentUser]_block_invoke
- ___79-[WBSOngoingSharingGroupProvider _fetchCurrentUserParticipantIDWithCompletion:]_block_invoke.26.cold.1
- ___79-[WBSOngoingSharingGroupProvider _fetchCurrentUserParticipantIDWithCompletion:]_block_invoke.27
- ___79-[WBSOngoingSharingGroupProvider canCurrentUserEditSavedAccountsInGroupWithID:]_block_invoke
- ___79-[WBSOngoingSharingGroupProvider canCurrentUserEditSavedAccountsInGroupWithID:]_block_invoke.cold.1
- ___block_descriptor_48_e8_32s40r_e58_v16?0"<WBSPasswordManagerWebsiteMetadataEntryProtocol>"8lr40l8s32l8
- ___block_literal_global.3150
- ___block_literal_global.47
- ___block_literal_global.57
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_SafariCore
- _block_copy_helper.152
- _block_copy_helper.161
- _block_copy_helper.164
- _block_copy_helper.167
- _block_copy_helper.171
- _block_copy_helper.76
- _block_copy_helper.98
- _block_descriptor.100
- _block_descriptor.154
- _block_descriptor.163
- _block_descriptor.166
- _block_descriptor.169
- _block_descriptor.173
- _block_descriptor.78
- _block_destroy_helper.153
- _block_destroy_helper.162
- _block_destroy_helper.165
- _block_destroy_helper.168
- _block_destroy_helper.172
- _block_destroy_helper.77
- _block_destroy_helper.99
- _objc_msgSend$_updateCachedPermissionLevelsForCurrentUser
- _objc_msgSend$canCurrentUserEditSavedAccountsInGroupWithID:
- _objectdestroy.118Tm
- _objectdestroy.22Tm
- _objectdestroy.31Tm
- _objectdestroy.64Tm
CStrings:
+ "%@ - %@"
+ "%@ - %@ (%lu)"
+ "@\"NSCharacterSet\""
+ "B40@0:8^B16@24^@32"
+ "B48@0:8^B16@24@32^@40"
+ "Deleting FileVault recovery key from Passwords access group."
+ "Failed to delete FileVault recovery key from FileVault access group: %s, status code: %d"
+ "Failed to delete FileVault recovery key from Passwords access group."
+ "Saved FileVault recovery key in FileVault access group."
+ "Saved FileVault recovery key in Passwords access group."
+ "T@\"NSCharacterSet\",R,C,N,V_allCharacters"
+ "T@\"NSDictionary\",R,C,N,V_replacementStringsToCharacterSets"
+ "URLWithDataRepresentation:relativeToURL:"
+ "WBSCharacterSetReplacementsContainer"
+ "_allCharacters"
+ "_metadataEntryLock"
+ "_replacementStringsToCharacterSets"
+ "_setPrivacyProxyStrictFailClosed:"
+ "allCharacters"
+ "associatedSiteName"
+ "com.apple.passwords.filevault.testing"
+ "enumerateCharacterSetReplacementStringPairsUsingBlock:"
+ "formUnionWithCharacterSet:"
+ "initWithReplacementStringsToCharacterSets:"
+ "replacementStringsToCharacterSets"
+ "safari_URLByNormalizingBlobURL"
+ "safari_displayableTabBarTitleString"
+ "safari_getFileExists:atSubpath:relativeToFileHandle:error:"
+ "safari_getFileSystemSupportsExclusiveRename:atFileHandle:error:"
+ "safari_integerForKey:defaultValue:"
+ "safari_isBlobURL"
+ "safari_stringByReplacingCharacterSetsInContainer:"
+ "sourceIdentifier"
+ "stringByReplacingOccurrencesOfString:withString:options:range:"
+ "v32@?0@\"NSCharacterSet\"8@\"NSString\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSCharacterSet\"16^B24"
- "Could not find permission level for current user in shared group."
- "Deleting in Passwords as well…"
- "Failed to delete keychain item: %s, status code: %d"
- "Saved FileVault recovery key item for Passwords."
- "Saved FileVault recovery key item to Keychain."
- "The user tried to change the username for a passkey in a group they have read only permission in."
- "The user tried to delete a credential in a group they have read only permission in."
- "The user tried to delete a passkey in a group they have read only permission in."
- "The user tried to delete a sidecar in a group they have read only permission in."
- "The user tried to delete credential in a group they have read only permission in."
- "The user tried to update a sidecar in a group they have read only permission in."
- "The user tried to update credential in a group they have read only permission in."
- "_groupIDToPermissionLevelForCurrentUser"
- "_setPrivacyProxyFailClosed:"
- "_updateCachedPermissionLevelsForCurrentUser"
- "canCurrentUserEditSavedAccountsInGroupWithID:"

```
