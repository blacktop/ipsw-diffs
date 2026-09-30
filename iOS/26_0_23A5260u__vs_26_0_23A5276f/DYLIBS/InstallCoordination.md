## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-755.0.0.0.0
-  __TEXT.__text: 0x69418
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x4118
+763.0.0.502.1
+  __TEXT.__text: 0x699ec
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_methlist: 0x4140
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xe5fb
-  __TEXT.__oslogstring: 0x78b8
+  __TEXT.__cstring: 0xe800
+  __TEXT.__oslogstring: 0x7926
   __TEXT.__gcc_except_tab: 0x1d80
-  __TEXT.__unwind_info: 0x1778
+  __TEXT.__unwind_info: 0x1788
   __TEXT.__objc_classname: 0x8ae
-  __TEXT.__objc_methname: 0xac33
-  __TEXT.__objc_methtype: 0x2389
-  __TEXT.__objc_stubs: 0x5fe0
-  __DATA_CONST.__got: 0x3e8
+  __TEXT.__objc_methname: 0xad0e
+  __TEXT.__objc_methtype: 0x23eb
+  __TEXT.__objc_stubs: 0x6040
+  __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__const: 0x1b60
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2060
+  __DATA_CONST.__objc_selrefs: 0x2080
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x5b8
+  __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x5980
+  __AUTH_CONST.__cfstring: 0x59e0
   __AUTH_CONST.__objc_const: 0xada0
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C0A74EF-E82C-318D-BCA5-0703789B8C83
-  Functions: 1952
-  Symbols:   6459
-  CStrings:  4132
+  UUID: 36A2B1C7-E9A0-3DA0-AAFE-D0015E1D952D
+  Functions: 1958
+  Symbols:   6480
+  CStrings:  4154
 
Symbols:
+ +[IXAppInstallCoordinator stagingLocationForInstallLocation:withSandboxExtension:error:]
+ +[IXAppInstallCoordinator(IXSimpleInstaller) _temporaryStagingLocationForInstallLocation:withSandboxExtensionHandle:error:]
+ +[IXAppInstallCoordinator(IXSimpleInstaller) _temporaryStagingLocationForInstallLocation:withSandboxExtensionHandle:error:].cold.1
+ -[IXFileManager consumeSandboxExtension:error:]
+ -[IXFileManager issueSandboxExtensionForURL:withExtensionClass:error:]
+ -[IXFileManager releaseSandboxExtensionToken:error:]
+ -[IXOwnedDataPromise consumeSandboxExtensionWithError:].cold.4
+ _SANDBOX_EXTENSION_DEFAULT
+ ___105+[IXAppInstallCoordinator(IXTesting) setTestModeForIdentifierPrefix:testMode:testSpecificValidationData:]_block_invoke.702
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.126
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.126.cold.1
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.126.cold.2
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.126.cold.3
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.126.cold.4
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.126.cold.5
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.126.cold.6
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.126.cold.7
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.127
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.127.cold.1
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.127.cold.2
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.127.cold.3
+ ___47+[IXAppInstallCoordinator(IXTesting) daemonPid]_block_invoke.695
+ ___55-[IXOwnedDataPromise setTargetLastPathComponent:error:]_block_invoke.19
+ ___55-[IXOwnedDataPromise setTargetLastPathComponent:error:]_block_invoke.19.cold.1
+ ___55-[IXOwnedDataPromise targetLastPathComponentWithError:]_block_invoke.20
+ ___55-[IXOwnedDataPromise targetLastPathComponentWithError:]_block_invoke.20.cold.1
+ ___56+[IXAppInstallCoordinator(IXTesting) setTestingEnabled:]_block_invoke.699
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.705
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.686
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.689
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.693
+ ___78+[IXAppInstallCoordinator(IXTesting) postNSCurrentLocaleDidChangeNotification]_block_invoke.696
+ ___80+[IXAppInstallCoordinator(IXTesting) purgeAllCoordinatorsAndPromisesForCreator:]_block_invoke.685
+ ___88+[IXAppInstallCoordinator stagingLocationForInstallLocation:withSandboxExtension:error:]_block_invoke
+ ___88+[IXAppInstallCoordinator stagingLocationForInstallLocation:withSandboxExtension:error:]_block_invoke.276
+ ___block_descriptor_64_e8_32s40r48r56r_e40_v32?0"NSURL"8"NSString"16"NSError"24ls32l8r40l8r48l8r56l8
+ ___block_descriptor_73_e8_32s40s48bs56r64r_e43_v24?0"IXApplicationIdentity"8"NSError"16ls32l8s40l8r56l8r64l8s48l8
+ ___block_literal_global.691
+ ___block_literal_global.698
+ ___block_literal_global.701
+ _objc_msgSend$_temporaryStagingLocationForInstallLocation:withSandboxExtensionHandle:error:
+ _objc_msgSend$consumeSandboxExtension:error:
+ _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
+ _objc_msgSend$releaseSandboxExtensionToken:error:
+ _objc_msgSend$stagingLocationForInstallLocation:withSandboxExtension:error:
+ _sandbox_extension_issue_file
- +[IXAppInstallCoordinator stagingLocationForInstallLocation:error:]
- +[IXAppInstallCoordinator(IXSimpleInstaller) _temporaryStagingLocationForInstallLocation:error:]
- ___105+[IXAppInstallCoordinator(IXTesting) setTestModeForIdentifierPrefix:testMode:testSpecificValidationData:]_block_invoke.701
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.1
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.2
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.3
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.4
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.5
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.6
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.123.cold.7
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.124
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.124.cold.1
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.124.cold.2
- ___47+[IXAppInstallCoordinator(IXTesting) daemonPid]_block_invoke.694
- ___55-[IXOwnedDataPromise setTargetLastPathComponent:error:]_block_invoke.21
- ___55-[IXOwnedDataPromise setTargetLastPathComponent:error:]_block_invoke.21.cold.1
- ___55-[IXOwnedDataPromise targetLastPathComponentWithError:]_block_invoke.22
- ___55-[IXOwnedDataPromise targetLastPathComponentWithError:]_block_invoke.22.cold.1
- ___56+[IXAppInstallCoordinator(IXTesting) setTestingEnabled:]_block_invoke.698
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.702
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.685
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.687
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.691
- ___67+[IXAppInstallCoordinator stagingLocationForInstallLocation:error:]_block_invoke
- ___67+[IXAppInstallCoordinator stagingLocationForInstallLocation:error:]_block_invoke.276
- ___78+[IXAppInstallCoordinator(IXTesting) postNSCurrentLocaleDidChangeNotification]_block_invoke.695
- ___80+[IXAppInstallCoordinator(IXTesting) purgeAllCoordinatorsAndPromisesForCreator:]_block_invoke.684
- ___block_descriptor_56_e8_32s40r48r_e27_v24?0"NSURL"8"NSError"16ls32l8r40l8r48l8
- ___block_descriptor_65_e8_32s40s48bs56r_e43_v24?0"IXApplicationIdentity"8"NSError"16ls32l8s40l8r56l8s48l8
- ___block_literal_global.690
- ___block_literal_global.697
- ___block_literal_global.700
- _objc_msgSend$_temporaryStagingLocationForInstallLocation:error:
- _objc_msgSend$stagingLocationForInstallLocation:error:
CStrings:
+ "%s: Failed to get access to installcoordinationd's staging directory at \"%@\" : %@"
+ "%s: Failed to get access to the temporary staging location at %@ : %@"
+ "%s: Failed to release sandbox extension for %@: %@"
+ "%s: Failed to release sandbox extension: %@"
+ "+[IXAppInstallCoordinator stagingLocationForInstallLocation:withSandboxExtension:error:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXSimpleInstaller) _temporaryStagingLocationForInstallLocation:withSandboxExtensionHandle:error:]"
+ "-[IXFileManager consumeSandboxExtension:error:]"
+ "-[IXFileManager issueSandboxExtensionForURL:withExtensionClass:error:]"
+ "-[IXFileManager releaseSandboxExtensionToken:error:]"
+ "@40@0:8@16^@24^@32"
+ "@40@0:8@16^q24^@32"
+ "@40@0:8@16r*24^@32"
+ "B32@0:8q16^@24"
+ "Failed to get access to installcoordinationd's staging directory at \"%@\""
+ "Failed to get access to the temporary staging location at %@"
+ "_temporaryStagingLocationForInstallLocation:withSandboxExtensionHandle:error:"
+ "consumeSandboxExtension:error:"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "issueSandboxExtensionForURL:withExtensionClass:error:"
+ "q32@0:8@16^@24"
+ "releaseSandboxExtensionToken:error:"
+ "sandbox_extension_issue_file for path %@ failed: %s"
+ "sandbox_extension_release for %lld failed: %s."
+ "stagingLocationForInstallLocation:withSandboxExtension:error:"
+ "v32@0:8@\"<MILocationProtocol>\"16@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">24"
+ "v32@?0@\"NSURL\"8@\"NSString\"16@\"NSError\"24"
- "%s: Could not get access to installcoordinationd's staging directory at \"%@\". : %@"
- "%s: Failed to release sandbox extension %lld: %s (%d)"
- "+[IXAppInstallCoordinator stagingLocationForInstallLocation:error:]_block_invoke"
- "Could not get access to installcoordinationd's staging directory at \"%@\"."
- "_temporaryStagingLocationForInstallLocation:error:"
- "stagingLocationForInstallLocation:error:"
- "v32@0:8@\"<MILocationProtocol>\"16@?<v@?@\"NSURL\"@\"NSError\">24"

```
