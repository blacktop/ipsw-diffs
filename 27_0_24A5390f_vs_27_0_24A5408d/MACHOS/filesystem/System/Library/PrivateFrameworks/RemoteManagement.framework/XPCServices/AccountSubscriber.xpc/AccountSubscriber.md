## AccountSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/AccountSubscriber`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-624.0.10.0.0
-  __TEXT.__text: 0x12784
+624.2.3.0.0
+  __TEXT.__text: 0x13a84
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x1f80
-  __TEXT.__objc_methlist: 0x81c
-  __TEXT.__const: 0x78
+  __TEXT.__objc_stubs: 0x2100
+  __TEXT.__objc_methlist: 0x86c
+  __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__cstring: 0x104b
+  __TEXT.__cstring: 0x10e9
   __TEXT.__objc_classname: 0x419
-  __TEXT.__objc_methname: 0x1c97
-  __TEXT.__objc_methtype: 0x2be
-  __TEXT.__oslogstring: 0xb0d
-  __TEXT.__unwind_info: 0x3c8
+  __TEXT.__objc_methname: 0x1e36
+  __TEXT.__objc_methtype: 0x2f1
+  __TEXT.__oslogstring: 0xfd0
+  __TEXT.__unwind_info: 0x3f8
   __DATA_CONST.__const: 0x8d8
-  __DATA_CONST.__cfstring: 0xca0
+  __DATA_CONST.__cfstring: 0xd20
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__auth_got: 0x1d8
   __DATA_CONST.__got: 0x3f8
   __DATA.__objc_const: 0xfd0
-  __DATA.__objc_selrefs: 0x910
+  __DATA.__objc_selrefs: 0x978
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 280
+  Functions: 299
   Symbols:   300
-  CStrings:  519
+  CStrings:  555
 
CStrings:
+ "(nil)"
+ "@32@0:8@16^@24"
+ "@48@0:8@16@24@32^@40"
+ "B32@0:8@16^@24"
+ "Failed to find transfer candidate for %{public}@: %{public}@"
+ "Failed to resolve user identity asset %{public}@ for declaration %{public}@: %{public}@"
+ "Failed to transfer profile-managed account %{public}@ for configuration %{public}@: %{public}@"
+ "Found profile-managed account %{public}@ matching email for transfer"
+ "Incorrect declaration class: %{public}@"
+ "Multiple profile-managed accounts (%lu) of type %@ match the requested email; refusing ambiguous transfer"
+ "No email address provided for profile-managed account lookup"
+ "No profile transfer candidate found among %lu accounts of type %{public}@"
+ "No profile-managed account matches email %{public}@ for declaration %{public}@"
+ "No transfer candidate for declaration %{public}@"
+ "No user identity asset reference in declaration %{public}@; skipping transfer candidate lookup"
+ "Profile account transfer to DDM"
+ "Refusing to transfer: %lu profile-managed candidates match (identifiers: %{public}@)"
+ "Resolved user identity has no email for declaration %{public}@; skipping transfer candidate lookup"
+ "Resolver returned nil userIdentity with no error for asset %{public}@ (declaration %{public}@)"
+ "Searching %lu accounts of type %{public}@ for profile transfer candidate"
+ "Transferred profile-managed account %{public}@ for configuration %{public}@"
+ "_transferProfileAccountForConfiguration:error:"
+ "accountsWithAccountType:"
+ "array"
+ "arrayWithCapacity:"
+ "caseInsensitiveCompare:"
+ "createInternalErrorWithDescription:"
+ "createNotImplementedErrorForFeature:"
+ "findProfileAccountToTransferForEmail:accountTypeIdentifier:store:error:"
+ "firstObject"
+ "length"
+ "mcProfileUUID"
+ "profileAccountToTransferForConfiguration:store:error:"
+ "transferProfileAccount: not implemented on this platform for account %{public}@"
+ "transferProfileAccount:error:"
+ "transferProfileAccountForConfiguration:error:"
```
