## com.apple.MobileInstallationHelperService

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService`

```diff

-1513.120.7.0.0
-  __TEXT.__text: 0x15a34
-  __TEXT.__auth_stubs: 0xbd0
+1655.0.0.0.0
+  __TEXT.__text: 0x14ce8
+  __TEXT.__auth_stubs: 0xc20
   __TEXT.__objc_stubs: 0x1f20
-  __TEXT.__objc_methlist: 0x8e4
-  __TEXT.__const: 0xb0
-  __TEXT.__objc_classname: 0x17e
-  __TEXT.__objc_methname: 0x2a5d
-  __TEXT.__objc_methtype: 0x8e9
-  __TEXT.__cstring: 0x5de8
-  __TEXT.__gcc_except_tab: 0x7c4
+  __TEXT.__objc_methlist: 0x8cc
+  __TEXT.__const: 0xa8
+  __TEXT.__objc_classname: 0x15e
+  __TEXT.__objc_methname: 0x2aa5
+  __TEXT.__objc_methtype: 0x8c8
+  __TEXT.__cstring: 0x5c24
+  __TEXT.__gcc_except_tab: 0x760
   __TEXT.__oslogstring: 0x277
-  __TEXT.__unwind_info: 0x418
-  __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x5a0
-  __DATA_CONST.__cfstring: 0x3420
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__unwind_info: 0x408
+  __DATA_CONST.__const: 0x550
+  __DATA_CONST.__cfstring: 0x3360
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_const: 0x10a0
+  __DATA_CONST.__auth_got: 0x620
+  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA.__objc_const: 0x1010
   __DATA.__objc_selrefs: 0x960
   __DATA.__objc_ivar: 0x50
-  __DATA.__objc_data: 0x320
+  __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x180
   __DATA.__bss: 0xb8
   __DATA.__common: 0x8

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC9DD4E5-C83F-394F-A1D3-074F14D0A892
-  Functions: 307
-  Symbols:   403
-  CStrings:  1422
+  UUID: 895A18FB-E0E1-3D6C-BDB6-80080C0256A8
+  Functions: 306
+  Symbols:   408
+  CStrings:  1405
 
Symbols:
+ _MICopyPlugInKitPersonaEntitlement
+ _MIHasCriticalAlertsEntitlement
+ _MIHasExtensionKitAnyPersonaEntitlement
+ _MIHasExtensionKitSystemPersonaEntitlement
+ _MIHasWrapperBundleEntitlement
+ _OBJC_CLASS_$_MIGlobalConfiguration
+ _OBJC_CLASS_$_MIPersonaContainerSet
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- _NSFileType
- _NSFileTypeDirectory
- _NSFileTypeRegular
- _NSFileTypeSymbolicLink
- _NSFileTypeUnknown
- _OBJC_CLASS_$_MIHelperBomVerifier
- _OBJC_METACLASS_$_MIHelperBomVerifier
- _TraverseDirectory
CStrings:
+ "-[MIStagingManager _stagingLocationForVolumeUUID:withVolumeMountPoint:inStagingSubsystem:usingUniqueName:error:]"
+ "-[MIStagingManager stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:]"
+ "09:36:26"
+ "May 21 2026"
+ "_stagingLocationForVolumeUUID:withVolumeMountPoint:inStagingSubsystem:usingUniqueName:error:"
+ "allPersonaVolumeDaemonContainersMapWithError:"
+ "com.apple.developer.usernotifications.critical-alerts"
+ "com.apple.developer.wrapper-bundle"
+ "com.apple.private.extensionkit.builtinanypersona"
+ "com.apple.private.extensionkit.builtinsystempersona"
+ "com.apple.private.pluginkit.persona"
+ "containersForIdentifier:groupContainerIdentifier:ofContentClass:forPersona:fetchTransient:createIfNeeded:created:error:"
+ "deviceHasPersonas"
+ "getPersonaVolumeDaemonContainerForUUID:containerURL:error:"
+ "initWithIdentifier:containerQueryResult:"
+ "stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:completion:"
+ "stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:error:"
+ "stagingLocationForURL:withinStagingSubsystem:usingUniqueName:completion:"
+ "stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:"
- "+[MIHelperBomVerifier applyAndVerifyBOMPropertiesForURL:toUID:GID:removeACLs:setProtectionClass:setFileAttributes:excludePathsAtURL:error:]"
- "+[MIHelperBomVerifier applyAndVerifyBOMPropertiesForURL:toUID:GID:removeACLs:setProtectionClass:setFileAttributes:excludePathsAtURL:error:]_block_invoke"
- "-[MIStagingManager _stagingLocationForVolumeUUID:withVolumeMountPoint:inStagingSubsytem:usingUniqueName:error:]"
- "-[MIStagingManager stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:]"
- "._"
- "/private"
- "/private/"
- "18:14:33"
- "Applying BOM to \"%@\""
- "Applying BOM to \"%@\", excluding \"%@\""
- "Apr 18 2026"
- "B24@?0^{?=QqQ*Q*QIIIIIIISBC}8^B16"
- "B64@0:8@16I24I28B32B36@40@48^@56"
- "Failed to locate items in Bom (count: %lu) as paths in app bundle. Missing files: %@"
- "Found item in app that did not exist in Bom: %@"
- "Item type in Bom entry, %@, does not match type on disk, %@, for %@"
- "MIHelperBomVerifier"
- "Preserving compressed bit on %s"
- "_stagingLocationForVolumeUUID:withVolumeMountPoint:inStagingSubsytem:usingUniqueName:error:"
- "allKeys"
- "allPersonaVolumeDaemonContainersMap"
- "applyAndVerifyBOMPropertiesForURL:toUID:GID:removeACLs:setProtectionClass:setFileAttributes:excludePathsAtURL:error:"
- "embedded.mobileprovision"
- "embedded.provisionprofile"
- "personaVolumeDaemonContainerForUUID:"
- "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:completion:"
- "stagingLocationForInstallLocation:withinStagingSubsytem:usingUniqueName:error:"
- "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:completion:"
- "stagingLocationForURL:withinStagingSubsytem:usingUniqueName:error:"
- "unsignedShortValue"

```
