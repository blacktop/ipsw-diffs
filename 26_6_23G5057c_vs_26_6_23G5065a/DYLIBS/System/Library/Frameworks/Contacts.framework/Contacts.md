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
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-  __TEXT.__text: 0x1ee0cc
+  __TEXT.__text: 0x1eecf8
   __TEXT.__auth_stubs: 0x3470
-  __TEXT.__objc_methlist: 0x1b818
+  __TEXT.__objc_methlist: 0x1b840
   __TEXT.__const: 0x4748
   __TEXT.__gcc_except_tab: 0x3d28
-  __TEXT.__cstring: 0xc339
+  __TEXT.__cstring: 0xc349
   __TEXT.__dlopen_cstrs: 0x8ba
-  __TEXT.__oslogstring: 0xcf9a
+  __TEXT.__oslogstring: 0xd07a
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0x116c
   __TEXT.__swift5_typeref: 0x151f

   __TEXT.__swift5_capture: 0x5f4
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x8e58
+  __TEXT.__unwind_info: 0x8e88
   __TEXT.__eh_frame: 0x2e28
   __TEXT.__objc_classname: 0x484b
-  __TEXT.__objc_methname: 0x2cdf9
+  __TEXT.__objc_methname: 0x2ce69
   __TEXT.__objc_methtype: 0x5923
-  __TEXT.__objc_stubs: 0x200c0
-  __DATA_CONST.__got: 0x1bd8
+  __TEXT.__objc_stubs: 0x20160
+  __DATA_CONST.__got: 0x1be0
   __DATA_CONST.__const: 0x64d0
   __DATA_CONST.__objc_classlist: 0x1140
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9ac0
+  __DATA_CONST.__objc_selrefs: 0x9ae0
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x9e0
   __DATA_CONST.__objc_arraydata: 0x268
   __AUTH_CONST.__auth_got: 0x1a48
-  __AUTH_CONST.__const: 0x81d9
+  __AUTH_CONST.__const: 0x81f9
   __AUTH_CONST.__cfstring: 0xdd40
-  __AUTH_CONST.__objc_const: 0x2ca20
-  __AUTH_CONST.__objc_intobj: 0x600
+  __AUTH_CONST.__objc_const: 0x2ca40
+  __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x5988

   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x5eb0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x10b0
+  __DATA_DIRTY.__bss: 0x10c0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13532
-  Symbols:   23822
-  CStrings:  10702
+  Functions: 13545
+  Symbols:   23830
+  CStrings:  10713
 
Symbols:
+ +[CNContactProviderSupportManager log]
+ -[CNContactProviderSupportManager clientBundleIdentifier]
+ -[CNContactProviderSupportManager hasSPIEntitlement]
+ -[CNContactProviderSupportManager isProviderExtensionEnabled]
+ _CNEntitlementNameContactsFrameworkSPI
+ _OBJC_IVAR_$_CNContactProviderSupportManager._clientBundleIdentifier
+ _OBJC_IVAR_$_CNContactProviderSupportManager._hasSPIEntitlement
+ ___38+[CNContactProviderSupportManager log]_block_invoke
+ _objc_msgSend$auditToken:hasBooleanEntitlement:error:
+ _objc_msgSend$audit_token
+ _objc_msgSend$hasSPIEntitlement
+ _objc_msgSend$isExtensionEnabledWith:
+ _objc_msgSend$isProviderExtensionEnabled
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
+ "T@\"NSString\",R,N,V_clientBundleIdentifier"
+ "TB,R,N,V_hasSPIEntitlement"
+ "_clientBundleIdentifier"
+ "_hasSPIEntitlement"
+ "auditToken:hasBooleanEntitlement:error:"
+ "audit_token"
+ "hasSPIEntitlement"
+ "isProviderExtensionEnabled"
+ "support-manager"
- "T@\"NSString\",R,N,V_clientLoggingIdentifier"
- "_cachedContainerIdentifier"
```
