## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1378.40.7.0.0
-  __TEXT.__text: 0xa0730
-  __TEXT.__auth_stubs: 0x1330
-  __TEXT.__objc_methlist: 0x43f0
+1378.60.20.502.1
+  __TEXT.__text: 0xa12e4
+  __TEXT.__auth_stubs: 0x1370
+  __TEXT.__objc_methlist: 0x4468
   __TEXT.__const: 0xf6c0
-  __TEXT.__gcc_except_tab: 0xa78
-  __TEXT.__cstring: 0x15d06
+  __TEXT.__gcc_except_tab: 0xa90
+  __TEXT.__cstring: 0x15f54
   __TEXT.__dlopen_cstrs: 0x111
   __TEXT.__oslogstring: 0x8b6
-  __TEXT.__unwind_info: 0x13b8
+  __TEXT.__unwind_info: 0x13d0
   __TEXT.__eh_frame: 0xd78
   __TEXT.__objc_classname: 0x567
-  __TEXT.__objc_methname: 0xce61
-  __TEXT.__objc_methtype: 0x17a6
-  __TEXT.__objc_stubs: 0x81e0
-  __DATA_CONST.__got: 0x3f0
+  __TEXT.__objc_methname: 0xd0dc
+  __TEXT.__objc_methtype: 0x17d9
+  __TEXT.__objc_stubs: 0x8280
+  __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0xc48
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2660
+  __DATA_CONST.__objc_selrefs: 0x26b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x978
-  __AUTH_CONST.__auth_got: 0x9a8
+  __AUTH_CONST.__auth_got: 0x9c8
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x54a8
-  __AUTH_CONST.__cfstring: 0xc160
-  __AUTH_CONST.__objc_const: 0x7f40
+  __AUTH_CONST.__cfstring: 0xc240
+  __AUTH_CONST.__objc_const: 0x7fd0
   __AUTH_CONST.__objc_dictobj: 0x11a8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_ivar: 0x4fc
-  __DATA.__data: 0x1150
+  __DATA.__objc_ivar: 0x508
+  __DATA.__data: 0x1160
   __DATA.__bss: 0xf0
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x1180

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1841
-  Symbols:   2235
-  CStrings:  4242
+  Functions: 1852
+  Symbols:   2252
+  CStrings:  4272
 
Symbols:
+ _MIIsApplicableToCurrentDeviceFamilyWithError
+ _MIIsCompatibleWithAtLeastOneDeviceFamily
+ _MIIsCompatibleWithDeviceFamily
+ _OBJC_CLASS_$_MICodeSigningInfo
+ _OBJC_METACLASS_$_MICodeSigningInfo
+ _SecTaskCopySigningIdentifier
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _audit_token_to_pid
CStrings:
+ "\v"
+ "+[MICodeSigningInfo getValue:forEntitlement:fromProcessWithAuditToken:error:]"
+ "+[MICodeSigningInfo signingIdentifierForAuditToken:error:]"
+ "-[MIUserManagement bundleIDsAssociatedWithPersonaUniqueString:error:]_block_invoke"
+ "-[MIUserManagement setBundleIdentifiers:forPersonaUniqueString:error:]"
+ "@56@0:8{?=[8I]}16^@48"
+ "B72@0:8^@16@24{?=[8I]}32^@64"
+ "Failed to associate apps with persona %!@(MISSING) : %!@(MISSING)"
+ "Failed to create SecTask from audit token for pid %!d(MISSING)"
+ "Failed to find persona %!@(MISSING) when checking associated bundleIDs for it"
+ "Failed to get signing identifier from SecTask for pid %!d(MISSING)"
+ "MI_dictionaryByMergingDictionaries:"
+ "RequireEligibilityForInDevelopmentApps"
+ "T@\"NSNumber\",C,N,V_marketplaceItemID"
+ "T@\"NSString\",C,N,V_marketplaceDomain"
+ "TB,R,N,V_requireEligibilityChecksForAppsInDevelopment"
+ "_marketplaceDomain"
+ "_marketplaceItemID"
+ "_requireEligibilityChecksForAppsInDevelopment"
+ "bundleIDsAssociatedWithPersonaUniqueString:error:"
+ "getValue:forEntitlement:fromProcessWithAuditToken:error:"
+ "marketplaceDomain"
+ "marketplaceItemID"
+ "requireEligibilityChecksForAppsInDevelopment"
+ "setBundleIdentifiers:forPersonaUniqueString:error:"
+ "setBundleIdentifiers:forPersonaWithPersonaUniqueString:withError:"
+ "setMarketplaceDomain:"
+ "setMarketplaceItemID:"
+ "signingIdentifierForAuditToken:error:"
- "\t"

```
