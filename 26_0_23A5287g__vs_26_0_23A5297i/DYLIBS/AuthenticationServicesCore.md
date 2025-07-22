## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-622.1.18.10.3
-  __TEXT.__text: 0xbadd8
-  __TEXT.__auth_stubs: 0x2550
-  __TEXT.__objc_methlist: 0x36f8
-  __TEXT.__const: 0xbcb8
-  __TEXT.__cstring: 0x4f72
-  __TEXT.__oslogstring: 0x3eb0
+622.1.19.10.4
+  __TEXT.__text: 0xbd330
+  __TEXT.__auth_stubs: 0x2570
+  __TEXT.__objc_methlist: 0x3710
+  __TEXT.__const: 0xbcc8
+  __TEXT.__cstring: 0x50a2
+  __TEXT.__oslogstring: 0x3f30
   __TEXT.__gcc_except_tab: 0x2e0
   __TEXT.__ustring: 0x564
   __TEXT.__dlopen_cstrs: 0x48
   __TEXT.__swift5_typeref: 0x2177
-  __TEXT.__constg_swiftt: 0x2388
-  __TEXT.__swift5_reflstr: 0x1621
-  __TEXT.__swift5_fieldmd: 0x2154
+  __TEXT.__constg_swiftt: 0x23a8
+  __TEXT.__swift5_reflstr: 0x1641
+  __TEXT.__swift5_fieldmd: 0x216c
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x3f0
   __TEXT.__swift5_proto: 0x92c

   __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x31c0
-  __TEXT.__eh_frame: 0x4190
-  __TEXT.__objc_classname: 0x7a8
-  __TEXT.__objc_methname: 0xaafa
-  __TEXT.__objc_methtype: 0x281c
+  __TEXT.__unwind_info: 0x31f0
+  __TEXT.__eh_frame: 0x41e0
+  __TEXT.__objc_classname: 0x7a9
+  __TEXT.__objc_methname: 0xab5c
+  __TEXT.__objc_methtype: 0x2823
   __TEXT.__objc_stubs: 0x44c0
-  __DATA_CONST.__got: 0x8a0
+  __DATA_CONST.__got: 0x8a8
   __DATA_CONST.__const: 0xba0
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cb0
+  __DATA_CONST.__objc_selrefs: 0x1cd0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x12b8
+  __AUTH_CONST.__auth_got: 0x12c8
   __AUTH_CONST.__const: 0x6190
-  __AUTH_CONST.__cfstring: 0x1f20
-  __AUTH_CONST.__objc_const: 0x76c0
+  __AUTH_CONST.__cfstring: 0x1f80
+  __AUTH_CONST.__objc_const: 0x7720
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xbe0
-  __AUTH.__data: 0x2e0
-  __DATA.__objc_ivar: 0x404
-  __DATA.__data: 0x27d0
+  __AUTH.__objc_data: 0xc08
+  __AUTH.__data: 0x2f0
+  __DATA.__objc_ivar: 0x408
+  __DATA.__data: 0x27f0
   __DATA.__bss: 0x11450
   __DATA.__common: 0x1d8
   __DATA_DIRTY.__objc_data: 0x1b70
-  __DATA_DIRTY.__data: 0x1098
+  __DATA_DIRTY.__data: 0x10a8
   __DATA_DIRTY.__bss: 0xf20
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3CF651FD-60AD-331C-A1DB-763AB5F66FBE
-  Functions: 4678
-  Symbols:   5272
-  CStrings:  2765
+  UUID: 466E9D24-89B8-374C-AE0A-1044846CA6B9
+  Functions: 4695
+  Symbols:   5279
+  CStrings:  2782
 
Symbols:
+ -[ASCPlatformPublicKeyCredentialLoginChoice _initAsRegistrationChoice:withName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:externalCredentialProviderName:externalCredentialProviderBundleID:supportedAlgorithms:excludedCredentials:groupID:groupName:]
+ -[ASCPlatformPublicKeyCredentialLoginChoice groupName]
+ -[ASCPlatformPublicKeyCredentialLoginChoice initWithName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:groupID:groupName:]
+ -[ASCPlatformPublicKeyCredentialLoginChoice localizedCredentialProviderName]
+ _OBJC_IVAR_$_ASCPlatformPublicKeyCredentialLoginChoice._groupName
+ _malloc
+ _objc_msgSend$_initAsRegistrationChoice:withName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:externalCredentialProviderName:externalCredentialProviderBundleID:supportedAlgorithms:excludedCredentials:groupID:groupName:
+ _objc_msgSend$initWithName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:groupID:groupName:
+ _swift_coroFrameAlloc
- -[ASCPlatformPublicKeyCredentialLoginChoice _initAsRegistrationChoice:withName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:externalCredentialProviderName:externalCredentialProviderBundleID:supportedAlgorithms:excludedCredentials:groupID:]
- -[ASCPlatformPublicKeyCredentialLoginChoice initWithName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:groupID:]
- _objc_msgSend$_initAsRegistrationChoice:withName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:externalCredentialProviderName:externalCredentialProviderBundleID:supportedAlgorithms:excludedCredentials:groupID:
- _objc_msgSend$initWithName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:groupID:
CStrings:
+ "@124@0:8B16@20@28@36@44@52@60@68@76@84@92@100@108@116"
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "ASAccountCreationLastUsedCPEIdentifier"
+ "ASAccountCreationLastUsedEmail"
+ "ASAccountCreationLastUsedName"
+ "ASAccountCreationLastUsedPhone"
+ "Account Registration requests cannot be used with other types of requests."
+ "Failed to decode data for key %s into type %s: %{private}@"
+ "Failed to encode %s for key %s: %{private}@"
+ "PersonNameComponents"
+ "Rejecting connection from unentitled process %{public}@."
+ "T@\"SFCredentialIdentity\",R,C,N,V_externalCredentialIdentity"
+ "_initAsRegistrationChoice:withName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:externalCredentialProviderName:externalCredentialProviderBundleID:supportedAlgorithms:excludedCredentials:groupID:groupName:"
+ "dataForKey:"
+ "initWithName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:groupID:groupName:"
+ "lastCreatedHideMyEmail"
+ "localizedCredentialProviderName"
+ "setObject:forKey:"
+ "stringForKey:"
- "@116@0:8B16@20@28@36@44@52@60@68@76@84@92@100@108"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "Rejecting connection from unentitled process."
- "T@\"SFCredentialIdentity\",R,N,V_externalCredentialIdentity"
- "_initAsRegistrationChoice:withName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:externalCredentialProviderName:externalCredentialProviderBundleID:supportedAlgorithms:excludedCredentials:groupID:"
- "initWithName:displayName:customTitle:identifier:userHandle:relyingPartyIdentifier:publicKeyCredentialOperationUUID:groupID:"

```
