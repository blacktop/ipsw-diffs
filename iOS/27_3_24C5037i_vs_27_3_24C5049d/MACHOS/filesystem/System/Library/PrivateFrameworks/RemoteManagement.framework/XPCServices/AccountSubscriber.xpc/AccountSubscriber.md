## AccountSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/AccountSubscriber`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-624.60.9.0.0
-  __TEXT.__text: 0x14900
+624.60.12.0.0
+  __TEXT.__text: 0x171e8
   __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_stubs: 0x23a0
-  __TEXT.__objc_methlist: 0x8a4
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__cstring: 0x120e
+  __TEXT.__objc_stubs: 0x2520
+  __TEXT.__objc_methlist: 0x95c
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0x2bc
+  __TEXT.__cstring: 0x1221
   __TEXT.__objc_classname: 0x419
-  __TEXT.__objc_methname: 0x1ff1
-  __TEXT.__objc_methtype: 0x303
-  __TEXT.__oslogstring: 0x115b
-  __TEXT.__unwind_info: 0x520
+  __TEXT.__objc_methname: 0x2183
+  __TEXT.__objc_methtype: 0x319
+  __TEXT.__oslogstring: 0x1108
+  __TEXT.__unwind_info: 0x568
   __DATA_CONST.__const: 0x948
-  __DATA_CONST.__cfstring: 0xde0
+  __DATA_CONST.__cfstring: 0xe00
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__auth_got: 0x1e0
-  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__got: 0x488
   __DATA.__objc_const: 0xfd0
-  __DATA.__objc_selrefs: 0xa10
+  __DATA.__objc_selrefs: 0xa70
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 312
-  Symbols:   321
-  CStrings:  586
+  Functions: 333
+  Symbols:   328
+  CStrings:  599
 
Symbols:
+ _ACAccountPropertyDAAccountHost
+ _ACAccountPropertySendingAccountIdentifier
+ _ACAccountTypeIdentifierSMTP
+ _MailAccountHostname
+ _MailAccountPortNumber
+ _OBJC_CLASS_$_MFAccount
+ ___NSArray0__struct
+ _kDAAccountPort
- _kMCAccountProfileUUIDKey
CStrings:
+ "%{public}@ does not implement profile account transfer for %{public}@"
+ "@48@0:8@16@24@32@40"
+ "@56@0:8@16@24@32@40@48"
+ "Best-effort username resolve failed for asset %{public}@: %{public}@"
+ "Credentials asset specified but resolved no username; skipping transfer candidate lookup"
+ "Found profile-managed account %{public}@ for transfer"
+ "Multiple profile-managed accounts match; refusing ambiguous transfer"
+ "No incoming server type in declaration %{public}@; skipping transfer candidate lookup"
+ "Transformer does not implement profile account transfer"
+ "_profileAccountToTransferForConfiguration:error:"
+ "accountWithPersistentAccount:"
+ "accountsMatchingEmail:inAccounts:"
+ "accountsMatchingHostname:port:username:inAccounts:"
+ "accountsMatchingOutgoingHostname:port:username:inAccounts:store:"
+ "deliveryAccount"
+ "emailsForAccount:"
+ "isEqualToNumber:"
+ "lowercaseString"
+ "profileAccountToTransferForConfiguration:error:"
+ "profileAccountsToTransferForConfiguration:store:error:"
+ "profileManagedAccountsOfType:store:"
+ "profileSecondaryAccountsToTransferForAccount:store:"
+ "reloadDeliveryAccounts"
+ "transferProfileAccount:configuration:error:"
+ "usernameForCredentialsAsset:configuration:"
- "@48@0:8@16@24@32^@40"
- "Found profile-managed account %{public}@ matching email for transfer"
- "Multiple profile-managed accounts (%lu) of type %@ match the requested email; refusing ambiguous transfer"
- "No email address provided for profile-managed account lookup"
- "No profile transfer candidate found among %lu accounts of type %{public}@"
- "No profile-managed account matches email %{public}@ for declaration %{public}@"
- "Resolver returned nil userIdentity with no error for asset %{public}@ (declaration %{public}@)"
- "Searching %lu accounts of type %{public}@ for profile transfer candidate"
- "_transferProfileAccountForConfiguration:error:"
- "findProfileAccountToTransferForEmail:accountTypeIdentifier:store:error:"
- "transferProfileAccount:error:"
- "transferProfileAccountForConfiguration:error:"
```
