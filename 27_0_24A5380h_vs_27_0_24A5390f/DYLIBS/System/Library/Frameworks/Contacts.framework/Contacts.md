## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

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
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-3837.100.1.0.0
-  __TEXT.__text: 0x22096c
-  __TEXT.__objc_methlist: 0x1be18
+3839.100.3.2.1
+  __TEXT.__text: 0x221678
+  __TEXT.__objc_methlist: 0x1be70
   __TEXT.__const: 0x4c60
   __TEXT.__gcc_except_tab: 0x3c2c
-  __TEXT.__cstring: 0xcbf9
+  __TEXT.__cstring: 0xcc19
   __TEXT.__dlopen_cstrs: 0x91e
-  __TEXT.__oslogstring: 0xf67a
+  __TEXT.__oslogstring: 0xf75a
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0x16d4
   __TEXT.__swift5_typeref: 0x1b0b

   __TEXT.__swift_as_entry: 0xb8
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift_as_cont: 0x158
-  __TEXT.__unwind_info: 0x9208
+  __TEXT.__unwind_info: 0x9240
   __TEXT.__eh_frame: 0x3ff0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d28
+  __DATA_CONST.__objc_selrefs: 0x9d70
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0xa20
   __DATA_CONST.__objc_arraydata: 0x268
-  __DATA_CONST.__got: 0x1db0
-  __AUTH_CONST.__const: 0x91f1
-  __AUTH_CONST.__cfstring: 0xdfa0
-  __AUTH_CONST.__objc_const: 0x2db70
-  __AUTH_CONST.__objc_intobj: 0x600
+  __DATA_CONST.__got: 0x1db8
+  __AUTH_CONST.__const: 0x9211
+  __AUTH_CONST.__cfstring: 0xdfc0
+  __AUTH_CONST.__objc_const: 0x2dbc0
+  __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x1de8
-  __AUTH.__objc_data: 0x6df8
-  __AUTH.__data: 0x8a8
-  __DATA.__objc_ivar: 0x1328
+  __AUTH.__objc_data: 0x6b50
+  __AUTH.__data: 0x8b0
+  __DATA.__objc_ivar: 0x132c
   __DATA.__data: 0x3ab8
-  __DATA.__bss: 0x65b0
+  __DATA.__bss: 0x6090
   __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_data: 0x5370
+  __DATA_DIRTY.__objc_data: 0x5618
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0xbf8
+  __DATA_DIRTY.__bss: 0x1128
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14213
-  Symbols:   24322
-  CStrings:  3446
+  Functions: 14232
+  Symbols:   24341
+  CStrings:  3452
 
Symbols:
+ +[CNContact(Predicates_Private) predicateForContactsMatchingEmailAddressPrefix:]
+ +[CNContactProviderSupportManager log]
+ -[CNContactProviderSupportManager clientBundleIdentifier]
+ -[CNContactProviderSupportManager hasSPIEntitlement]
+ -[CNContactProviderSupportManager isProviderExtensionEnabled]
+ -[CNEmailAddressContactPredicate initWithEmailAddress:groupIdentifiers:prefixSearch:returnMultipleResults:]
+ -[CNEmailAddressContactPredicate initWithEmailAddress:prefixSearch:returnMultipleResults:]
+ -[CNEmailAddressContactPredicate prefixSearch]
+ _CNEntitlementNameContactsFrameworkSPI
+ _OBJC_IVAR_$_CNContactProviderSupportManager._clientBundleIdentifier
+ _OBJC_IVAR_$_CNContactProviderSupportManager._hasSPIEntitlement
+ _OBJC_IVAR_$_CNEmailAddressContactPredicate._prefixSearch
+ ___38+[CNContactProviderSupportManager log]_block_invoke
+ ___38-[CNEmailAddressContactPredicate hash]_block_invoke_4
+ ___42-[CNEmailAddressContactPredicate isEqual:]_block_invoke_4
+ _objc_msgSend$auditToken:hasBooleanEntitlement:error:
+ _objc_msgSend$audit_token
+ _objc_msgSend$hasSPIEntitlement
+ _objc_msgSend$initWithEmailAddress:groupIdentifiers:prefixSearch:returnMultipleResults:
+ _objc_msgSend$initWithEmailAddress:prefixSearch:returnMultipleResults:
+ _objc_msgSend$isExtensionEnabledWith:
+ _objc_msgSend$isProviderExtensionEnabled
+ _objc_msgSend$predicateForContactsMatchingMultivaluePropertyPrefix:values:groupIdentifiers:containerIdentifiers:limitToOneResult:map:
+ _objc_msgSend$prefixSearch
- -[CNContactProviderSupportManager clientLoggingIdentifier]
- -[CNContactProviderSupportiOSDataMapper defaultContainerIdentifierImpl]
- _OBJC_IVAR_$_CNContactProviderSupportManager._clientLoggingIdentifier
- _OBJC_IVAR_$_CNContactProviderSupportiOSDataMapper._cachedContainerIdentifier
- ___67-[CNContactProviderSupportiOSDataMapper defaultContainerIdentifier]_block_invoke
CStrings:
+ "%@ has no SPI access to CNContactProviderSupportDomainCommand %@"
+ "%@ has no SPI access to set CNContactProviderSupportDomainCommand.bundleIdentifier (%@)"
+ "Failed to check SPI entitlement, error: %@"
+ "No provider access allowed"
+ "_prefixSearch"
+ "support-manager"
```
