## profiled

> `/usr/libexec/profiled`

```diff

-2400.5.1.0.0
-  __TEXT.__text: 0x9f4b4
+2400.5.2.0.0
+  __TEXT.__text: 0x9f4f0
   __TEXT.__auth_stubs: 0x2230
   __TEXT.__objc_stubs: 0xfbe0
   __TEXT.__objc_methlist: 0x56e4
   __TEXT.__const: 0x1fc
   __TEXT.__gcc_except_tab: 0x1940
-  __TEXT.__oslogstring: 0xcdca
-  __TEXT.__cstring: 0x8cf2
-  __TEXT.__objc_methname: 0x1364b
+  __TEXT.__oslogstring: 0xce1c
+  __TEXT.__cstring: 0x8d0c
+  __TEXT.__objc_methname: 0x13640
   __TEXT.__objc_classname: 0xb36
   __TEXT.__objc_methtype: 0x205a
-  __TEXT.__unwind_info: 0x16b8
+  __TEXT.__unwind_info: 0x16b0
   __DATA_CONST.__auth_got: 0x1128
   __DATA_CONST.__got: 0x1bb8
   __DATA_CONST.__const: 0x1b50
-  __DATA_CONST.__cfstring: 0x8520
+  __DATA_CONST.__cfstring: 0x8540
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68

   - /usr/lib/libobjc.A.dylib
   Functions: 2025
   Symbols:   1480
-  CStrings:  4933
+  CStrings:  4935
 
CStrings:
+ "MCMigrator failed to clear legacy client MCFeatureTrustedCodeSigningIdentities with error: %{public}@"
+ "MCMigrator successfully cleared legacy client MCFeatureTrustedCodeSigningIdentities"
+ "MCMigrator._migrateSettings"
+ "MCProvisioningProfileJanitor._syncMCTrustedCodeSigningIdentities"
+ "_syncMCTrustedCodeSigningIdentities:"
- "MCProvisioningProfileJanitor failed to set MCFeatureTrustedCodeSigningIdentities with error: %{public}@"
- "MCProvisioningProfileJanitor._updateMCTrustedCodeSigningIdentities"
- "_updateMCTrustedCodeSigningIdentities:outError:"

```
