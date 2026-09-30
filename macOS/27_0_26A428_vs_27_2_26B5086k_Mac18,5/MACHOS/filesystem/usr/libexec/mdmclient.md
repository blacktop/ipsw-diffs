## mdmclient

> `/usr/libexec/mdmclient`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-1911.1.1.0.0
-  __TEXT.__text: 0x1320d4
-  __TEXT.__auth_stubs: 0x2510
-  __TEXT.__objc_stubs: 0x9e00
+1911.40.8.0.0
+  __TEXT.__text: 0x13448c
+  __TEXT.__auth_stubs: 0x2520
+  __TEXT.__objc_stubs: 0x9de0
   __TEXT.__init_offsets: 0x28
   __TEXT.__objc_methlist: 0x2a68
-  __TEXT.__gcc_except_tab: 0x2ef78
-  __TEXT.__cstring: 0x36c05
+  __TEXT.__gcc_except_tab: 0x2f5c4
+  __TEXT.__cstring: 0x371ef
   __TEXT.__const: 0x231
-  __TEXT.__objc_methname: 0x9cfc
+  __TEXT.__objc_methname: 0x9cde
   __TEXT.__objc_classname: 0x510
   __TEXT.__objc_methtype: 0x13b8
   __TEXT.__oslogstring: 0x148

   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x6d68
+  __TEXT.__unwind_info: 0x6de8
   __DATA_CONST.__const: 0x3518
-  __DATA_CONST.__cfstring: 0x32c20
+  __DATA_CONST.__cfstring: 0x32f60
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98

   __DATA_CONST.__objc_arrayobj: 0x798
   __DATA_CONST.__objc_intobj: 0x420
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x12a0
+  __DATA_CONST.__auth_got: 0x12a8
   __DATA_CONST.__got: 0xd48
   __DATA.__objc_const: 0x4548
-  __DATA.__objc_selrefs: 0x2bf0
+  __DATA.__objc_selrefs: 0x2be8
   __DATA.__objc_ivar: 0x2f4
   __DATA.__objc_data: 0xd88
-  __DATA.__data: 0xb3a
+  __DATA.__data: 0xb42
   __DATA.__crash_info: 0x148
   __DATA.__common: 0xb0
   __RESTRICT.__restrict: 0x0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 3534
-  Symbols:   1033
-  CStrings:  8835
+  Functions: 3545
+  Symbols:   1034
+  CStrings:  8860
 
Symbols:
+ _CP_ImportCertificatesForPayload
CStrings:
+ "CPDestinationForUserGUID passed: %@ but that's not the current user GUID: %@"
+ "Error saving account %@: %@"
+ "Failed to delete keychain item for forced re-import"
+ "ForceReimportCertificatePayload"
+ "ForceReimportCertificatePayload: Failed to re-import cert for payload %@: %@"
+ "ForceReimportCertificatePayload: Flushing profile userData"
+ "ForceReimportCertificatePayload: Looking up profile: %@"
+ "ForceReimportCertificatePayload: Missing required parameter(s)"
+ "ForceReimportCertificatePayload: Payload %@ not found in profile: %@"
+ "ForceReimportCertificatePayload: Profile not found: %@"
+ "ForceReimportCertificatePayload: Unable to delete keychain item for payload: %@: %@"
+ "ForceReimportCertificatePayload: Unable to get direct persistent ref for re-imported identity"
+ "ForceReimportCertificatePayload: Unable to locate re-imported identity for payload: %@"
+ "ForceReimportCertificatePayload: Unable to resolve re-imported identity"
+ "ForceReimportCertificatePayload: Unexpected destination for userGUID: %@"
+ "ForceReimportCertificatePayload: Unknown keychainPersistentRef: %@"
+ "Keychain: GetDirectPersistentRefForIdentity Found ref: %@ for: %@"
+ "Keychain: ResolveKeychain for persistent ref: %@"
+ "MCTakeoverErrorDomain"
+ "Missing required parameter: %@"
+ "NewIdentityPersistRef"
+ "ResolveKeychain: Returning '%@' for: %@ ==> %@"
+ "ResolveKeychain: Unable to determine keychain for: %@ ==> %@"
+ "ResolveKeychain: Unable to resolve persistent reference ==> %@"
+ "Transferred Exchange account %@ from profile %@ (payload: %@, new owner: %@)"
+ "Transferred account %@ (type: %@, new owner: %@)"
+ "Unsupported item type in import: %@"
+ "com.apple.private.managedclient.certpayloadrecovery"
+ "postNotificationName:object:userInfo:audience:entitlement:options:error:"
- "Account %@ is not Exchange (type: %@)"
- "Transferred account %@ from profile %@ (payload: %@, new owner: %@)"
- "postNotificationName:object:userInfo:deliverImmediately:"
- "postNotificationName:object:userInfo:options:"
```
