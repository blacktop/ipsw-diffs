## installd

> `/usr/libexec/installd`

```diff

-1378.40.7.0.0
-  __TEXT.__text: 0x55058
-  __TEXT.__auth_stubs: 0x11a0
-  __TEXT.__objc_stubs: 0x77a0
-  __TEXT.__objc_methlist: 0x284c
+1378.60.20.502.1
+  __TEXT.__text: 0x55dbc
+  __TEXT.__auth_stubs: 0x11c0
+  __TEXT.__objc_stubs: 0x7920
+  __TEXT.__objc_methlist: 0x28ac
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x2b28
-  __TEXT.__objc_methname: 0xac31
-  __TEXT.__cstring: 0x13c83
+  __TEXT.__gcc_except_tab: 0x2b4c
+  __TEXT.__objc_methname: 0xaf67
+  __TEXT.__cstring: 0x1454d
   __TEXT.__objc_classname: 0x591
-  __TEXT.__objc_methtype: 0x1a3f
+  __TEXT.__objc_methtype: 0x1a99
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x11ad
   __TEXT.__ustring: 0x84
-  __TEXT.__unwind_info: 0xf50
-  __DATA_CONST.__auth_got: 0x8e0
-  __DATA_CONST.__got: 0x328
+  __TEXT.__unwind_info: 0xf70
+  __DATA_CONST.__auth_got: 0x8f0
+  __DATA_CONST.__got: 0x330
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xf80
-  __DATA_CONST.__cfstring: 0x8e60
+  __DATA_CONST.__cfstring: 0x9080
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98

   __DATA_CONST.__objc_arraydata: 0x560
   __DATA_CONST.__objc_dictobj: 0xd70
   __DATA.__objc_const: 0x6578
-  __DATA.__objc_selrefs: 0x21d0
+  __DATA.__objc_selrefs: 0x2240
   __DATA.__objc_ivar: 0x2a0
   __DATA.__objc_data: 0xc80
   __DATA.__data: 0x838

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libParallelCompression.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1201
-  Symbols:   396
-  CStrings:  3369
+  Functions: 1208
+  Symbols:   399
+  CStrings:  3409
 
Symbols:
+ _OBJC_CLASS_$_MICodeSigningInfo
+ _audit_token_to_pid
+ _objc_retain_x5
CStrings:
+ "+[MIInstallableBundle _domainForBrowserEligibilityForApp:withSigningInfo:distributorInfo:isWebDistribution:operationType:]"
+ "+[MIInstallableBundle _domainForMarketplaceEligibilityForApp:withSigningInfo:isWebDistribution:distributorInfo:operationType:]"
+ "+[MIInstallableBundle _getEligibilityForDomain:forBundle:isEligible:ineligibilityReason:error:]"
+ "+[MIInstallableBundle _shouldSkipEligibilityChecksForAppWithSigningInfo:]"
+ "+[MIInstallableBundle _shouldSkipEligibilityChecksForAuthorizingAppWithBundleID:persona:]"
+ "+[MIInstallableBundle _shouldSkipEligibilityChecksForInstallRequestorWithAuditToken:persona:authorizingBundleID:]"
+ "-[MIInstallableBundle _checkEligibilityForAppWithSigningInfo:distributorInfo:isWebDistribution:withError:]"
+ "-[MIInstallableBundle _performBrowserAppEntitlementAndArchitectureValidationForSigningInfo:error:]"
+ "-[MIInstallableBundle _performBrowserAppEntitlementAndArchitectureValidationForSigningInfo:error:]_block_invoke"
+ "-[MIUserManagement bundleIDsAssociatedWithPersonaUniqueString:error:]_block_invoke"
+ "-[MIUserManagement setBundleIdentifiers:forPersonaUniqueString:error:]"
+ "App %!@(MISSING) is in development or testing; skipping browser eligibility check for %!s(MISSING)"
+ "App %!@(MISSING) is in development or testing; skipping third party distribution eligibility check for %!s(MISSING)"
+ "B40@0:8^{?=[8I]}16@24^@32"
+ "B44@0:8@16@24B32^@36"
+ "B56@0:8Q16@24^B32^@40^@48"
+ "Checking eligibility for initial install of %!@(MISSING) \"%!@(MISSING)\""
+ "Checking eligibility for restore of %!@(MISSING) \"%!@(MISSING)\""
+ "Checking eligibility for update of %!@(MISSING) \"%!@(MISSING)\""
+ "Default set to require eligibility checks for in-development apps; would have skipped but not skipping for %!@(MISSING)"
+ "Eligibility check for domain %!l(MISSING)lu for bundle ID %!@(MISSING) returned ineligible value %!l(MISSING)lu, source %!l(MISSING)lu, status %!@(MISSING), context %!@(MISSING)"
+ "Failed to associate apps with persona %!@(MISSING) : %!@(MISSING)"
+ "Failed to check if installation requestor process has the \"%!@(MISSING)\" entitlement: %!@(MISSING)"
+ "Failed to find bundle container for app matching bundle ID %!@(MISSING): %!@(MISSING)"
+ "Failed to find persona %!@(MISSING) when checking associated bundleIDs for it"
+ "Failed to get eligibility for domain %!l(MISSING)lu for %!@(MISSING)"
+ "Failed to get signing identifier from development app with pid %!d(MISSING) : %!@(MISSING)"
+ "Failed to get signing info from installed app %!@(MISSING) : %!@(MISSING)"
+ "Found bundle container for %!@(MISSING) but it did not contain a valid bundle"
+ "No installed app matches the bundle ID %!@(MISSING); unable to authorize bypass of eligibility checks"
+ "Q52@0:8@16@24@32B40Q44"
+ "Q52@0:8@16@24B32@36Q44"
+ "Requestor of %!s(MISSING), \"%!@(MISSING)\", is in development or testing: skipping browser eligibility check for %!@(MISSING)"
+ "Requestor of %!s(MISSING), \"%!@(MISSING)\", is in development or testing: skipping third party distribution eligibility check for %!@(MISSING)"
+ "Skipping ARM64e architecture requirement for %!@(MISSING) and all of its contained executables because it is signed for development or testing."
+ "Test mode: forcing skip of eligibility checks because install requestor %!@(MISSING) is considered in development"
+ "Test mode: forcing skip of eligibility checks for %!@(MISSING)"
+ "The installation requestor process with pid %!d(MISSING) does not have the required entitlement \"%!@(MISSING)\" = TRUE; not skipping entitlement checks"
+ "The installation requestor process with pid %!d(MISSING) has the required entitlement \"%!@(MISSING)\" but its value is not a boolean; not skipping entitlement checks"
+ "_checkEligibilityForAppWithSigningInfo:distributorInfo:isWebDistribution:withError:"
+ "_domainForBrowserEligibilityForApp:withSigningInfo:distributorInfo:isWebDistribution:operationType:"
+ "_domainForMarketplaceEligibilityForApp:withSigningInfo:isWebDistribution:distributorInfo:operationType:"
+ "_getEligibilityForDomain:forBundle:isEligible:ineligibilityReason:error:"
+ "_performBrowserAppEntitlementAndArchitectureValidationForSigningInfo:error:"
+ "_shouldSkipEligibilityChecksForAppWithSigningInfo:"
+ "_shouldSkipEligibilityChecksForAuthorizingAppWithBundleID:persona:"
+ "_shouldSkipEligibilityChecksForInstallRequestorWithAuditToken:persona:authorizingBundleID:"
+ "app distributed by marketplace \"%!@(MISSING)\","
+ "bundleIDsAssociatedWithPersonaUniqueString:error:"
+ "codeInfoIdentifier"
+ "com.apple.mi-test-runner"
+ "distributorIsThirdParty"
+ "getValue:forEntitlement:fromProcessWithAuditToken:error:"
+ "installationRequestorAuditToken"
+ "requireEligibilityChecksForAppsInDevelopment"
+ "setBundleIdentifiers:forPersonaUniqueString:error:"
+ "setBundleIdentifiers:forPersonaWithPersonaUniqueString:withError:"
+ "signingIdentifierForAuditToken:error:"
- "-[MIInstallableBundle _checkEligibilityForEntitlements:withError:]"
- "-[MIInstallableBundle _getMarketplaceEligibilityForWebDistribution:isMarketplace:operationType:isEligible:ineligibilityReason:error:]"
- "-[MIInstallableBundle _performBrowserAppValidationForEntitlements:error:]"
- "-[MIInstallableBundle _performBrowserAppValidationForEntitlements:error:]_block_invoke"
- "B56@0:8B16B20Q24^B32^@40^@48"
- "Checking eligibility for initial install of %!s(MISSING) %!@(MISSING)"
- "Checking eligibility for restore of %!s(MISSING) %!@(MISSING)"
- "Checking eligibility for update of %!s(MISSING) %!@(MISSING)"
- "Eligibility check for domain %!l(MISSING)lu returned ineligible value %!l(MISSING)lu, source %!l(MISSING)lu, status %!@(MISSING), context %!@(MISSING)"
- "Failed to get eligibility for %!@(MISSING)"
- "Failed to get eligibility for browser engine app %!@(MISSING)"
- "Unknown validation operation %!l(MISSING)u for %!@(MISSING)"
- "Unknown validation operation for %!@(MISSING)"
- "Validating %!@(MISSING) distributed by %!@(MISSING)"
- "_checkEligibilityForEntitlements:withError:"
- "_getMarketplaceEligibilityForWebDistribution:isMarketplace:operationType:isEligible:ineligibilityReason:error:"
- "_performBrowserAppValidationForEntitlements:error:"
- "marketplace-distributed app"

```
