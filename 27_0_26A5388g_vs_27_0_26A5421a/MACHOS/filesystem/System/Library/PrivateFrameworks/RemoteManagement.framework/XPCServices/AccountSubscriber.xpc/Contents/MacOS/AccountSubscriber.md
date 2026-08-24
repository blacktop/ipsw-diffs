## AccountSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/Contents/MacOS/AccountSubscriber`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-624.0.10.0.0
-  __TEXT.__text: 0x11394
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_stubs: 0x1a20
-  __TEXT.__objc_methlist: 0x7cc
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x1e8
-  __TEXT.__cstring: 0xfdf
+624.1.3.0.0
+  __TEXT.__text: 0x12dd8
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__objc_stubs: 0x1bc0
+  __TEXT.__objc_methlist: 0x81c
+  __TEXT.__const: 0x88
+  __TEXT.__gcc_except_tab: 0x23c
+  __TEXT.__cstring: 0x10e1
   __TEXT.__objc_classname: 0x419
-  __TEXT.__objc_methname: 0x18a0
-  __TEXT.__objc_methtype: 0x2be
-  __TEXT.__oslogstring: 0xc2f
-  __TEXT.__unwind_info: 0x3b8
-  __DATA_CONST.__const: 0x9c8
-  __DATA_CONST.__cfstring: 0xcc0
+  __TEXT.__objc_methname: 0x1a31
+  __TEXT.__objc_methtype: 0x2f1
+  __TEXT.__oslogstring: 0x112b
+  __TEXT.__unwind_info: 0x3e8
+  __DATA_CONST.__const: 0xa10
+  __DATA_CONST.__cfstring: 0xd60
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x368
   __DATA.__objc_const: 0xfd0
-  __DATA.__objc_selrefs: 0x7b8
+  __DATA.__objc_selrefs: 0x820
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x120

   - /System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/Versions/A/DMCUtilities
   - /System/Library/PrivateFrameworks/DataAccess.framework/Versions/A/DataAccess
   - /System/Library/PrivateFrameworks/ExchangeWebServices.framework/Versions/A/ExchangeWebServices

   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/Versions/A/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 297
-  Symbols:   244
-  CStrings:  482
+  Functions: 322
+  Symbols:   251
+  CStrings:  520
 
Symbols:
+ _ACAccountPropertyConfigurationProfileIdentifier
+ _AccountPropertyRemoteManagementProfileTransferDate
+ _AccountPropertyRemoteManagementTransferredFromProfileIdentifier
+ _CP_RemoteManagementTransferProfileAccount
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_RMFeatureFlags
+ _RemoteManagementManagingOwnerIdentifier
CStrings:
+ "(nil)"
+ "@32@0:8@16^@24"
+ "@48@0:8@16@24@32^@40"
+ "B32@0:8@16^@24"
+ "Exchange protocol upgrade (EWS to Graph) on same mailbox; mutating in place"
+ "Failed to find transfer candidate for %{public}@: %{public}@"
+ "Failed to record failure for %{public}@: %{public}@"
+ "Failed to resolve user identity asset %{public}@ for declaration %{public}@: %{public}@"
+ "Failed to transfer profile-managed account %{public}@ for configuration %{public}@: %{public}@"
+ "Found profile-managed account %{public}@ matching email for transfer"
+ "Incorrect declaration class: %{public}@"
+ "Multiple profile-managed accounts (%lu) of type %@ match the requested email; refusing ambiguous transfer"
+ "No email address provided for profile-managed account lookup"
+ "No existing DDM-managed account for key %{public}@, checking for profile transfer candidate"
+ "No profile transfer candidate found among %lu accounts of type %{public}@"
+ "No profile-managed account matches email %{public}@ for declaration %{public}@"
+ "No transfer candidate for declaration %{public}@"
+ "No user identity asset reference in declaration %{public}@; skipping transfer candidate lookup"
+ "Refusing Graph-to-EWS protocol downgrade on existing account"
+ "Refusing Graph-to-EWS protocol downgrade on existing account %{public}@"
+ "Refusing to transfer: %lu profile-managed candidates match (identifiers: %{public}@)"
+ "RemoteManagementProfileTransferDate"
+ "RemoteManagementTransferredFromProfileIdentifier"
+ "Resolved user identity has no email for declaration %{public}@; skipping transfer candidate lookup"
+ "Resolver returned nil userIdentity with no error for asset %{public}@ (declaration %{public}@)"
+ "Searching %lu accounts of type %{public}@ for profile transfer candidate"
+ "Skipping configuration %{public}@ after failed profile transfer: %{public}@"
+ "Transferred profile-managed account %{public}@ for configuration %{public}@"
+ "_transferProfileAccountForConfiguration:error:"
+ "accountsWithAccountType:"
+ "array"
+ "arrayWithCapacity:"
+ "caseInsensitiveCompare:"
+ "createInternalErrorWithDescription:"
+ "date"
+ "findProfileAccountToTransferForEmail:accountTypeIdentifier:store:error:"
+ "firstObject"
+ "isAccountTakeoverEnabled"
+ "profileAccountToTransferForConfiguration:store:error:"
+ "transferProfileAccount:error:"
+ "transferProfileAccountForConfiguration:error:"
- "Configuration removal of EWS External URL requires account to be recreated"
- "Configuration removal of EWS Internal URL requires account to be recreated"
- "Configuration removal of Graph API Endpoint URI requires account to be recreated"
```
