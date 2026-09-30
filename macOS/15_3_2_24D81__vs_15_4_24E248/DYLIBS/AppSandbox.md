## AppSandbox

> `/System/Library/PrivateFrameworks/AppSandbox.framework/Versions/A/AppSandbox`

```diff

-738.60.3.0.0
-  __TEXT.__text: 0xa1d8
+738.100.25.0.0
+  __TEXT.__text: 0xa29c
   __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_methlist: 0x524
   __TEXT.__const: 0xe0
   __TEXT.__oslogstring: 0x955
   __TEXT.__cstring: 0x199a
   __TEXT.__gcc_except_tab: 0x20c
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x250
   __TEXT.__objc_classname: 0x9e
   __TEXT.__objc_methname: 0x18a7
   __TEXT.__objc_methtype: 0x228

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 6EB14BFE-DF9D-3A4B-9E01-2AFB2A0EDE69
-  Functions: 191
-  Symbols:   661
+  UUID: F22F4227-DD3D-3FBC-94F1-2B5334F4DB0B
+  Functions: 202
+  Symbols:   672
   CStrings:  714
 
Symbols:
+ +[AppSandboxFolderRedirector redirectedFolders].cold.1
+ +[AppSandboxRequest implicitIosProfilePaths].cold.1
+ +[AppSandboxRequest implicitMacosProfilePaths].cold.1
+ -[AppSandboxEntitlements __requestsInheritanceOfSandbox:].cold.1
+ -[AppSandboxRequest appsandboxContainerSync:].cold.7
+ -[AppSandboxRequest appsandboxContainerSync:].cold.8
+ -[AppSandboxRequest screenSaverRequest].cold.1
+ -[NSBundle(AppSandboxAdditions) sandboxProfilePath].cold.1
+ AppSandboxUtilCollectionScopedBookmarkSecurityPolicyPermitsFD.cold.1
+ AppSandboxUtilRealPathForUTF8StringPath.cold.2
+ codeRequirementMatchingAnyAdHocSignedBinary.cold.1
+ codeRequirementMatchingPlatformOrMAS.cold.1
+ doesACLIncludeRequirementForAdHocSignature.cold.1
+ localize_string.cold.1
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6

```
