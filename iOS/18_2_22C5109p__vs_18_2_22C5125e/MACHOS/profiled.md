## profiled

> `/usr/libexec/profiled`

```diff

-2381.2.4.0.0
-  __TEXT.__text: 0x9da84
+2381.2.7.1.0
+  __TEXT.__text: 0x9d92c
   __TEXT.__auth_stubs: 0x2130
-  __TEXT.__objc_stubs: 0xfa60
-  __TEXT.__objc_methlist: 0x4c8c
+  __TEXT.__objc_stubs: 0xfaa0
+  __TEXT.__objc_methlist: 0x4ca4
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x194c
-  __TEXT.__oslogstring: 0xcb90
-  __TEXT.__cstring: 0x8b5b
-  __TEXT.__objc_methname: 0x1335a
+  __TEXT.__oslogstring: 0xcba3
+  __TEXT.__cstring: 0x8b4c
+  __TEXT.__objc_methname: 0x1338e
   __TEXT.__objc_classname: 0xb36
-  __TEXT.__objc_methtype: 0x1ff1
+  __TEXT.__objc_methtype: 0x2021
   __TEXT.__unwind_info: 0x16a0
   __DATA_CONST.__auth_got: 0x10a8
   __DATA_CONST.__got: 0x1b90

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x7218
-  __DATA.__objc_selrefs: 0x4348
+  __DATA.__objc_const: 0x7238
+  __DATA.__objc_selrefs: 0x4358
   __DATA.__objc_ivar: 0x1c0
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0x4ea

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1921
+  Functions: 1923
   Symbols:   1459
-  CStrings:  4887
+  CStrings:  4889
 
CStrings:
+ "MCProvisioningProfileJanitor failed to set MCFeatureTrustedCodeSigningIdentities with error: %!{(MISSING)public}@"
+ "MCProvisioningProfileJanitor skipping MCFeatureTrustedCodeSigningIdentities update after MIS enumeration failed"
+ "MCProvisioningProfileJanitor updating MIS trust..."
+ "MCProvisioningProfileJanitor._updateMCTrustedCodeSigningIdentities"
+ "TRUSTED_CODE_SIGNING_IDS_CLIENT_TYPE"
+ "_homepodText"
+ "_updateMCTrustedCodeSigningIdentities:outError:"
+ "com.apple.profiled.trustedcodesigningidentities"
+ "provisiongProfileUUIDsForSignerIdentity:completion:"
+ "provisioningProfileUUIDsForSignerIdentity:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"@\"NSError\">24"
- "Failed to set managed code signing identities. Error: %!{(MISSING)public}@"
- "MANAGED_CODE_SIGNING_IDS_CLIENT_TYPE"
- "MCInstaller skipping untrusted identity purge after MIS get all signer identities failed"
- "MCProvisioningProfileJanitor._updateTrustedCodeSigningIdentitiesWithManagedAppSigners"
- "MCProvisioningProfileJanitor.updateMISTrust"
- "Removing trusted identity '%!{(MISSING)public}@' because it is not trusted by MIS"
- "Updating MIS trust..."
- "_updateTrustedCodeSigningIdentitiesWithManagedAppSigners:outError:"
- "removeUntrustedIdentitiesFromSender:"

```
