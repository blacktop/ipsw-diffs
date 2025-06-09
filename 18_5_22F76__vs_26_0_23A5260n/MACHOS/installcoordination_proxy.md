## installcoordination_proxy

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordination_proxy`

```diff

-699.100.10.0.0
-  __TEXT.__text: 0x123cc
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0xce4
-  __TEXT.__const: 0xb0
+755.0.0.0.0
+  __TEXT.__text: 0x122cc
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_stubs: 0x1f40
+  __TEXT.__objc_methlist: 0xcec
+  __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__cstring: 0x210b
+  __TEXT.__cstring: 0x2152
   __TEXT.__objc_classname: 0x18c
-  __TEXT.__objc_methname: 0x2ab6
-  __TEXT.__oslogstring: 0x1ad8
-  __TEXT.__objc_methtype: 0x78a
-  __TEXT.__unwind_info: 0x408
-  __DATA_CONST.__auth_got: 0x4c0
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x498
+  __TEXT.__objc_methname: 0x2bbe
+  __TEXT.__oslogstring: 0x1a5f
+  __TEXT.__objc_methtype: 0x7b1
+  __TEXT.__unwind_info: 0x420
+  __DATA_CONST.__auth_got: 0x4c8
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x4b8
   __DATA_CONST.__cfstring: 0xbe0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x1b28
-  __DATA.__objc_selrefs: 0x9e8
+  __DATA.__objc_selrefs: 0xa18
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x2b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1E0E964C-7D92-3D2D-8BEC-E37EB9A549C4
+  UUID: 11D8B446-AADE-3794-94B1-B124F8A0D26D
   Functions: 401
-  Symbols:   209
-  CStrings:  957
+  Symbols:   212
+  CStrings:  963
 
Symbols:
+ _OBJC_CLASS_$_IXPlaceholderSpecification
+ _OBJC_CLASS_$_MIHelperServiceFrameworkClient
+ _lchown
CStrings:
+ "%s: Could not find an existing app with %@, creating an initiating coordinator"
+ "%s: Found an existing app with %@, creating an updating coordinator"
+ "+[IXSRemoteInstaller _coordinatorWithIdentity:forUpdate:created:error:]"
+ "-[IXFileManager standardizeOwnershipAtURL:toUID:toGID:error:]_block_invoke"
+ "04:44:44"
+ "@40@0:8@16@24^@32"
+ "B40@0:8@16I24I28^@32"
+ "Failed to get promise staging directory for install location %@ with uniqueName %@: %@"
+ "Failed to lchown %s with uid/gid %d/%d : %s"
+ "May 23 2025"
+ "PersonalPersonaPlaceholderString"
+ "_coordinatorWithIdentity:forUpdate:created:error:"
+ "identity"
+ "initWithBundleIdentifier:personaUniqueString:location:"
+ "initWithLocalizedBundleName:bundleID:type:client:location:"
+ "initWithName:client:data:location:"
+ "initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:location:"
+ "initWithName:client:transferPath:diskSpaceNeeded:location:error:"
+ "initWithSpecification:error:"
+ "location"
+ "promiseStagingRootAbortingOnErrorForInstallLocation:usingUniqueName:"
+ "promiseStagingRootForInstallLocation:usingUniqueName:error:"
+ "realPathForURL:"
+ "setInstallType:"
+ "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:"
+ "standardizeOwnershipAtURL:toUID:toGID:error:"
- "%s: Could not find an app record for app with %@, creating an initiating coordinator"
- "%s: Failed to create IXPromisedTransferToPath for entitlements for %@ : %@"
- "%s: Found an app record for app with %@, creating an updating coordinator"
- "+[IXSRemoteInstaller _coordinatorWithBundleID:forUpdate:created:error:]"
- "04:41:37"
- "Apr 19 2025"
- "Failed to create IXPromisedTransferToPath for entitlements for %@"
- "Failed to create staging root at %@ : %@"
- "Failed to get promise staging directory: %@"
- "Failed to get staging root path: %@"
- "PromiseStaging"
- "_coordinatorWithBundleID:forUpdate:created:error:"
- "createTemporaryIconsDirectoryWithError:"
- "initAppPlaceholderWithBundleName:bundleID:installType:client:error:"
- "initWithBundleIdentifier:"
- "initWithName:client:data:"
- "initWithName:client:streamingZipOptions:archiveSize:diskSpaceNeeded:"
- "initWithName:client:transferPath:diskSpaceNeeded:"
- "promiseStagingRootDirectoryAbortingOnError"
- "promiseStagingRootDirectoryWithError:"

```
