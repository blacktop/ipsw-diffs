## bless

> `/usr/sbin/bless`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA.__data`

```diff

-335.0.1.0.0
-  __TEXT.__text: 0x21050
-  __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__objc_stubs: 0x560
-  __TEXT.__const: 0x3c8
-  __TEXT.__cstring: 0x9cdc
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__oslogstring: 0x4e2
-  __TEXT.__objc_methname: 0x409
-  __TEXT.__unwind_info: 0x378
+335.0.2.0.0
+  __TEXT.__text: 0x1fee0
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_stubs: 0x3c0
+  __TEXT.__const: 0x3b0
+  __TEXT.__cstring: 0x9aec
+  __TEXT.__oslogstring: 0x43c
+  __TEXT.__objc_methname: 0x257
+  __TEXT.__unwind_info: 0x348
   __TEXT.__eh_frame: 0x7c
-  __DATA_CONST.__const: 0x128
-  __DATA_CONST.__cfstring: 0x12c0
+  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__cfstring: 0x1280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x8f0
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__auth_ptr: 0x90
-  __DATA.__objc_selrefs: 0x158
-  __DATA.__objc_classrefs: 0x48
+  __DATA_CONST.__auth_got: 0x880
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__auth_ptr: 0x88
+  __DATA.__objc_selrefs: 0xf0
+  __DATA.__objc_classrefs: 0x28
   __DATA.__data: 0x710
   __DATA.__common: 0x1a144
   __DATA.__bss: 0x48

   - /System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom
   - /System/Library/PrivateFrameworks/Bootability.framework/Versions/A/Bootability
   - /System/Library/PrivateFrameworks/MediaKit.framework/Versions/A/MediaKit
-  - /System/Library/PrivateFrameworks/OSPersonalization.framework/Versions/A/OSPersonalization
   - /System/Library/PrivateFrameworks/apfs_boot_mount.framework/Versions/A/apfs_boot_mount
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib

   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libimg4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 295
-  Symbols:   337
-  CStrings:  1257
+  Functions: 277
+  Symbols:   311
+  CStrings:  1230
 
Symbols:
- _BOMCopierCopy
- _BOMCopierFree
- _BOMCopierNew
- _OBJC_CLASS_$_NSAutoreleasePool
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_OSPersonalizationController
- _OSPErrorDomain
- _OSPErrorIsNetworkingRelated
- _OSPersonalizationOptionPreferBuildManifest
- _OSPersonalizationOptionShowUI
- _OSPersonalizationOptionUseRunningDeviceIdentity
- _OSPersonalizedManifestRootTypeBoot
- _OSPersonalizedManifestRootTypePreboot
- _OSPersonalizedManifestRootTypeRecoveryBoot
- __Block_object_assign
- __Block_object_dispose
- __NSConcreteStackBlock
- __Unwind_Resume
- ___objc_personality_v0
- _chflags
- _dispatch_release
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _strlcat
CStrings:
+ "The 'allowUI' option is deprecated\n"
+ "The 'personalize' option is deprecated\n"
+ "contentsOfDirectoryAtPath:error:"
+ "disk is vitual ?: %d\n"
+ "hasSuffix:"
- "%s: could not get path for preboot volume\n"
- "Couldn't personalize volume %s\n"
- "Invalid file descriptor value %d for argument %s\n"
- "Malformed manifest name \"%s\" for file \"%s\"\n"
- "Missing argument: a policy volume is required"
- "Missing argument: a policy volume is required\n"
- "Missing argument: a preboot volume is required"
- "Missing argument: a preboot volume is required\n"
- "OSP reports volume is already personalized\n"
- "PATH_KEY_POLICY_PATH"
- "PATH_KEY_PREBOOT_FD"
- "Personalization not required for volume at %s\n"
- "Personalization required for volume at %s\n"
- "RestoreOptions"
- "URLByAppendingPathComponent:"
- "addEntriesFromDictionary:"
- "class"
- "dictionaryWithContentsOfFile:"
- "domain"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "isEqualToString:"
- "networkAvailableForPersonalizationWithOptions:"
- "objectForKey:"
- "personalizationRequiredForVolumeAtMountPoint:"
- "personalizeVolumeAtMountPointForInstall:outputDirectory:options:completionHandler:"
- "preboot_fd"
- "requiredManifestPathsForBootFile:"
- "roots"
- "setObject:forKey:"
- "sharedController"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "volumeHasBeenPersonalized:prebootFolder:"
```
