## Contacts

> `/System/Library/Frameworks/Contacts.framework/Versions/A/Contacts`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-3837.100.1.0.0
-  __TEXT.__text: 0x1f76d0
-  __TEXT.__objc_methlist: 0x1b798
+3839.100.3.0.0
+  __TEXT.__text: 0x1f8648
+  __TEXT.__objc_methlist: 0x1b830
   __TEXT.__const: 0x49e0
   __TEXT.__gcc_except_tab: 0x327c
-  __TEXT.__cstring: 0xcd09
+  __TEXT.__cstring: 0xcd99
   __TEXT.__dlopen_cstrs: 0x9e4
-  __TEXT.__oslogstring: 0xceca
+  __TEXT.__oslogstring: 0xcf8a
   __TEXT.__ustring: 0xe
   __TEXT.__constg_swiftt: 0x12d4
   __TEXT.__swift5_typeref: 0x1863

   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift_as_cont: 0x98
-  __TEXT.__unwind_info: 0x88b0
+  __TEXT.__unwind_info: 0x88e8
   __TEXT.__eh_frame: 0x30c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2c98
+  __DATA_CONST.__const: 0x2cb8
   __DATA_CONST.__objc_classlist: 0x1158
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa2d0
+  __DATA_CONST.__objc_selrefs: 0xa370
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x980
   __DATA_CONST.__objc_arraydata: 0x348
-  __DATA_CONST.__got: 0x1b58
-  __AUTH_CONST.__const: 0xd0a1
-  __AUTH_CONST.__cfstring: 0xe1e0
-  __AUTH_CONST.__objc_const: 0x2c440
+  __DATA_CONST.__got: 0x1b70
+  __AUTH_CONST.__const: 0xd0e1
+  __AUTH_CONST.__cfstring: 0xe220
+  __AUTH_CONST.__objc_const: 0x2c4b0
   __AUTH_CONST.__objc_intobj: 0x600
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__auth_got: 0x12d0
-  __AUTH.__objc_data: 0x6148
+  __AUTH.__objc_data: 0x5fe0
   __AUTH.__data: 0x818
-  __DATA.__objc_ivar: 0x121c
+  __DATA.__objc_ivar: 0x1224
   __DATA.__data: 0x3930
-  __DATA.__bss: 0x64b0
+  __DATA.__bss: 0x62b0
   __DATA.__common: 0x98
-  __DATA_DIRTY.__objc_data: 0x5780
+  __DATA_DIRTY.__objc_data: 0x58e8
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0xd10
+  __DATA_DIRTY.__bss: 0xf30
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/ClassKit.framework/Versions/A/ClassKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13675
-  Symbols:   23818
-  CStrings:  3348
+  Functions: 13697
+  Symbols:   23858
+  CStrings:  3355
 
Symbols:
+ +[CNContact(Predicates_Private) predicateForContactsMatchingEmailAddressPrefix:]
+ +[CNContactProviderSupportManager log]
+ -[CNCDSaveRequestExecutor _avatarPropagationKeys]
+ -[CNCDSaveRequestExecutor isPrimaryAppleAccountContainer:]
+ -[CNCDSaveRequestExecutor primaryAppleAccount]
+ -[CNCDSaveRequestExecutor syncDefaultMeAvatarToPrimaryAppleAccount]
+ -[CNCDSaveRequestExecutor updateMeCardForAccount:withContact:]
+ -[CNContactProviderSupportManager clientBundleIdentifier]
+ -[CNContactProviderSupportManager hasSPIEntitlement]
+ -[CNContactProviderSupportManager isProviderExtensionEnabled]
+ -[CNEmailAddressContactPredicate initWithEmailAddress:groupIdentifiers:prefixSearch:returnMultipleResults:]
+ -[CNEmailAddressContactPredicate initWithEmailAddress:prefixSearch:returnMultipleResults:]
+ -[CNEmailAddressContactPredicate prefixSearch]
+ OBJC_IVAR_$_CNContactProviderSupportManager._clientBundleIdentifier
+ OBJC_IVAR_$_CNContactProviderSupportManager._hasSPIEntitlement
+ OBJC_IVAR_$_CNEmailAddressContactPredicate._prefixSearch
+ _ACAccountDataclassContacts
+ _CGRectNull
+ _CNEntitlementNameContactsFrameworkSPI
+ ___38+[CNContactProviderSupportManager log]_block_invoke
+ ___38-[CNEmailAddressContactPredicate hash]_block_invoke_3
+ ___46-[CNCDSaveRequestExecutor primaryAppleAccount]_block_invoke
+ ___block_descriptor_32_e19_B16?0"ACAccount"8l
+ _objc_msgSend$_avatarPropagationKeys
+ _objc_msgSend$_cn_appleAccountAppleID
+ _objc_msgSend$_cn_firstName
+ _objc_msgSend$_cn_lastName
+ _objc_msgSend$accountTypeWithAccountTypeIdentifier:
+ _objc_msgSend$accountsWithAccountType:
+ _objc_msgSend$auditToken:hasBooleanEntitlement:error:
+ _objc_msgSend$audit_token
+ _objc_msgSend$clientBundleIdentifier
+ _objc_msgSend$hasSPIEntitlement
+ _objc_msgSend$initWithEmailAddress:groupIdentifiers:prefixSearch:returnMultipleResults:
+ _objc_msgSend$initWithEmailAddress:prefixSearch:returnMultipleResults:
+ _objc_msgSend$isEnabledForDataclass:
+ _objc_msgSend$isExtensionEnabledWith:
+ _objc_msgSend$isPrimaryAppleAccountContainer:
+ _objc_msgSend$predicateForMeContact
+ _objc_msgSend$prefixSearch
+ _objc_msgSend$primaryAppleAccount
+ _objc_msgSend$syncDefaultMeAvatarToPrimaryAppleAccount
+ _objc_msgSend$updateMeCardForAccount:withContact:
- -[CNContactProviderSupportManager clientLoggingIdentifier]
- OBJC_IVAR_$_CNContactProviderSupportManager._clientLoggingIdentifier
- _objc_msgSend$clientLoggingIdentifier
CStrings:
+ "%@ has no SPI access to CNContactProviderSupportDomainCommand %@"
+ "%@ has no SPI access to set CNContactProviderSupportDomainCommand.bundleIdentifier (%@)"
+ "0 != SUBQUERY(emailAddresses, $rmo, $rmo.addressNormalized BEGINSWITH[c] %@).@count"
+ "B16@?0@\"ACAccount\"8"
+ "Failed to check SPI entitlement, error: %@"
+ "_prefixSearch"
+ "support-manager"
```
