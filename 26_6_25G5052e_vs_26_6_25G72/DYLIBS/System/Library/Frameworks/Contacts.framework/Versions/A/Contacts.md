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
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3804.700.21.0.0
-  __TEXT.__text: 0x1fede4
+3804.700.52.0.0
+  __TEXT.__text: 0x1ff278
   __TEXT.__auth_stubs: 0x2350
-  __TEXT.__objc_methlist: 0x1b498
+  __TEXT.__objc_methlist: 0x1b4c0
   __TEXT.__const: 0x4788
   __TEXT.__gcc_except_tab: 0x319c
-  __TEXT.__cstring: 0xc9f9
+  __TEXT.__cstring: 0xca09
   __TEXT.__dlopen_cstrs: 0x9e4
-  __TEXT.__oslogstring: 0xc7fa
+  __TEXT.__oslogstring: 0xc8ca
   __TEXT.__ustring: 0xe
   __TEXT.__constg_swiftt: 0x116c
   __TEXT.__swift5_typeref: 0x151f

   __TEXT.__swift5_capture: 0x5f4
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x8bb0
+  __TEXT.__unwind_info: 0x8bc0
   __TEXT.__eh_frame: 0x2e20
   __TEXT.__objc_classname: 0x479b
-  __TEXT.__objc_methname: 0x2d3f9
+  __TEXT.__objc_methname: 0x2d4b9
   __TEXT.__objc_methtype: 0x5513
-  __TEXT.__objc_stubs: 0x21480
-  __DATA_CONST.__got: 0x1a88
+  __TEXT.__objc_stubs: 0x21500
+  __DATA_CONST.__got: 0x1a90
   __DATA_CONST.__const: 0x2c30
   __DATA_CONST.__objc_classlist: 0x1130
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa1d0
+  __DATA_CONST.__objc_selrefs: 0xa1f8
   __DATA_CONST.__objc_protorefs: 0xe8
   __DATA_CONST.__objc_superrefs: 0x978
   __DATA_CONST.__objc_arraydata: 0x340
   __AUTH_CONST.__auth_got: 0x11b8
-  __AUTH_CONST.__const: 0xc9e9
+  __AUTH_CONST.__const: 0xca09
   __AUTH_CONST.__cfstring: 0xe060
-  __AUTH_CONST.__objc_const: 0x2bdb8
+  __AUTH_CONST.__objc_const: 0x2bdf8
   __AUTH_CONST.__objc_intobj: 0x600
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH.__objc_data: 0x5690
   __AUTH.__data: 0x6e8
-  __DATA.__objc_ivar: 0x11f4
+  __DATA.__objc_ivar: 0x11f8
   __DATA.__data: 0x3748
   __DATA.__bss: 0x62f0
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x6108
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0xe70
+  __DATA_DIRTY.__bss: 0xe80
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/ClassKit.framework/Versions/A/ClassKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13477
-  Symbols:   23594
-  CStrings:  10937
+  Functions: 13488
+  Symbols:   23604
+  CStrings:  10949
 
Symbols:
+ +[CNContactProviderSupportManager log]
+ -[CNContactProviderSupportManager clientBundleIdentifier]
+ -[CNContactProviderSupportManager hasSPIEntitlement]
+ -[CNContactProviderSupportManager isProviderExtensionEnabled]
+ OBJC_IVAR_$_CNContactProviderSupportManager._clientBundleIdentifier
+ OBJC_IVAR_$_CNContactProviderSupportManager._hasSPIEntitlement
+ _CNEntitlementNameContactsFrameworkSPI
+ ___38+[CNContactProviderSupportManager log]_block_invoke
+ _objc_msgSend$auditToken:hasBooleanEntitlement:error:
+ _objc_msgSend$audit_token
+ _objc_msgSend$clientBundleIdentifier
+ _objc_msgSend$hasSPIEntitlement
+ _objc_msgSend$isExtensionEnabledWith:
- -[CNContactProviderSupportManager clientLoggingIdentifier]
- OBJC_IVAR_$_CNContactProviderSupportManager._clientLoggingIdentifier
- _objc_msgSend$clientLoggingIdentifier
CStrings:
+ "%@ has no SPI access to CNContactProviderSupportDomainCommand %@"
+ "%@ has no SPI access to set CNContactProviderSupportDomainCommand.bundleIdentifier (%@)"
+ "Failed to check SPI entitlement, error: %@"
+ "T@\"NSString\",R,N,V_clientBundleIdentifier"
+ "TB,R,N,V_hasSPIEntitlement"
+ "_clientBundleIdentifier"
+ "_hasSPIEntitlement"
+ "auditToken:hasBooleanEntitlement:error:"
+ "audit_token"
+ "clientBundleIdentifier"
+ "hasSPIEntitlement"
+ "isProviderExtensionEnabled"
+ "support-manager"
- "T@\"NSString\",R,N,V_clientLoggingIdentifier"
```
