## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2349.0.31.0.2
-  __TEXT.__text: 0x122e8
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_stubs: 0x2060
-  __TEXT.__objc_methlist: 0x7a0
-  __TEXT.__const: 0x410
+2349.40.6.0.9
+  __TEXT.__text: 0x144b8
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_stubs: 0x2480
+  __TEXT.__objc_methlist: 0xa48
+  __TEXT.__const: 0x420
+  __TEXT.__cstring: 0x3935
+  __TEXT.__objc_methname: 0x2cb9
+  __TEXT.__objc_classname: 0xf2
+  __TEXT.__objc_methtype: 0x597
+  __TEXT.__oslogstring: 0x25d0
   __TEXT.__gcc_except_tab: 0x384
-  __TEXT.__objc_methname: 0x26e3
-  __TEXT.__cstring: 0x3725
-  __TEXT.__oslogstring: 0x2599
-  __TEXT.__objc_classname: 0xad
-  __TEXT.__objc_methtype: 0x569
   __TEXT.__constg_swiftt: 0x18c
   __TEXT.__swift5_typeref: 0xe4
   __TEXT.__swift5_reflstr: 0x8c

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x470
   __TEXT.__eh_frame: 0x158
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x128
-  __DATA_CONST.__const: 0x650
-  __DATA_CONST.__cfstring: 0xb40
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__cfstring: 0xe40
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x10f8
-  __DATA.__objc_selrefs: 0x9f0
-  __DATA.__objc_ivar: 0x64
-  __DATA.__objc_data: 0x330
-  __DATA.__data: 0x300
-  __DATA.__bss: 0x550
+  __DATA.__objc_const: 0x1618
+  __DATA.__objc_selrefs: 0xb88
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_data: 0x4c0
+  __DATA.__data: 0x360
+  __DATA.__bss: 0x5f0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 298
-  Symbols:   275
-  CStrings:  1025
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 364
+  Symbols:   296
+  CStrings:  1118
 
Symbols:
+ OBJC_IVAR_$_MBContainer._plist
+ _OBJC_CLASS_$_MBAppGroup
+ _OBJC_CLASS_$_MBAppPlugin
+ _OBJC_CLASS_$_MBContainer
+ _OBJC_CLASS_$_MBSystemContainer
+ _OBJC_METACLASS_$_MBApp
+ _OBJC_METACLASS_$_MBAppGroup
+ _OBJC_METACLASS_$_MBAppPlugin
+ _OBJC_METACLASS_$_MBContainer
+ _OBJC_METACLASS_$_MBSystemContainer
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _kMBSafeHarborInfoDirName
+ _kMBSafeHarborInfoPlistFilename
+ _objc_release_x1
CStrings:
+ ".com.apple.mobile_container_manager.metadata.plist"
+ "@24@0:8^{_NSZone=}16"
+ "@36@0:8@16@24B32"
+ "Data/Application"
+ "Data/PluginKitPlugin"
+ "Documents"
+ "Found empty app group container identifier for %!@(MISSING) (%!@(MISSING))"
+ "Found empty app group container identifier for %!@(MISSING) (%!@(MISSING))"
+ "GeoJSON"
+ "Internal"
+ "Library"
+ "Library/Caches"
+ "Library/Caches/NeverRestore"
+ "Library/Saved Application State"
+ "Library/SplashBoard"
+ "Library/SyncedPreferences"
+ "MBApp"
+ "MBApp.m"
+ "MBAppGroup"
+ "MBAppPlugin"
+ "MBContainer"
+ "MBSystemContainer"
+ "NSCopying"
+ "NewsstandArtwork"
+ "Not a safe harbor"
+ "PlaceholderEntitlements.plist"
+ "PluginOwnerBundleID"
+ "SafeHarborDockingDate"
+ "Shared/AppGroup"
+ "System"
+ "System/Data"
+ "System/Shared"
+ "SystemData/com.apple.AuthenticationServices"
+ "SystemData/com.apple.chrono"
+ "T@\"NSDate\",&,N"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSString\",&,N"
+ "T@\"NSString\",R,N,V_volumeMountPoint"
+ "TB,R,N,GisSafeHarbor"
+ "Ti,R,N"
+ "_plist"
+ "_volumeMountPoint"
+ "allAppGroupContainers"
+ "allocWithZone:"
+ "appDomainWithIdentifier:volumeMountPoint:rootPath:"
+ "appGroupDomainWithIdentifier:volumeMountPoint:rootPath:"
+ "appPluginDomainWithIdentifier:volumeMountPoint:rootPath:"
+ "appWithBundleID:"
+ "appWithPropertyList:"
+ "bundleDir"
+ "containerDir"
+ "containerTypeString"
+ "containerTypeWithName:"
+ "containerWithPropertyList:volumeMountPoint:"
+ "containers"
+ "copyWithVolumeMountPoint:"
+ "copyWithZone:"
+ "datePlacedInSafeHarbor"
+ "dictionaryWithCapacity:"
+ "dictionaryWithContentsOfFile:"
+ "doesNotRecognizeSelector:"
+ "entitlementsRelativePath"
+ "groups"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "i16@0:8"
+ "initWithPropertyList:volumeMountPoint:"
+ "isAppUpdating"
+ "isSafeHarbor"
+ "isSystemApp"
+ "isSystemContainer"
+ "isSystemSharedContainer"
+ "mutableCopy"
+ "mutableCopyWithZone:"
+ "ownerBundleID"
+ "plugins"
+ "propertyListForBackupProperties"
+ "propertyListForSafeHarborInfo"
+ "safeHarbor"
+ "setBundleDir:"
+ "setByAddingObjectsFromSet:"
+ "setContainerDir:"
+ "setDatePlacedInSafeHarbor:"
+ "setRelativePathsNotToBackup:"
+ "setRelativePathsNotToRestore:"
+ "setRelativePathsToBackupAndRestore:"
+ "setShouldDigest:"
+ "setWithObjects:"
+ "stringByDeletingLastPathComponent"
+ "stringByStandardizingPath"
+ "systemContainerDomainWithIdentifier:volumeMountPoint:rootPath:"
+ "systemContainerWithDomainName:containerDir:isShared:"
+ "systemSharedContainerDomainWithIdentifier:volumeMountPoint:rootPath:"
+ "uninstalledContainerWithDomainName:volumeMountPoint:"

```
