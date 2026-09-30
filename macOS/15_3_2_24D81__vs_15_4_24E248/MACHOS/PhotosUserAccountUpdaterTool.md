## PhotosUserAccountUpdaterTool

> `/System/Library/CoreServices/UAUPlugins/PhotosUserAccountUpdaterPlugin.bundle/Contents/MacOS/PhotosUserAccountUpdaterTool`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x17ec
-  __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_stubs: 0x420
-  __TEXT.__objc_methlist: 0x170
-  __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__cstring: 0x38a
-  __TEXT.__objc_methname: 0x8fe
-  __TEXT.__oslogstring: 0x2eb
-  __TEXT.__objc_classname: 0x84
-  __TEXT.__objc_methtype: 0x2f4
-  __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__cfstring: 0x240
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x18
+751.0.104.0.0
+  __TEXT.__text: 0x3bc4
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_stubs: 0x900
+  __TEXT.__objc_methlist: 0x47c
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0x11c
+  __TEXT.__cstring: 0x59f
+  __TEXT.__objc_methname: 0xd16
+  __TEXT.__oslogstring: 0x95f
+  __TEXT.__objc_classname: 0xd5
+  __TEXT.__objc_methtype: 0x39a
+  __TEXT.__unwind_info: 0x138
+  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x1b0
+  __DATA_CONST.__cfstring: 0x460
+  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_const: 0x938
-  __DATA.__objc_selrefs: 0x170
-  __DATA.__objc_ivar: 0x20
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x120
+  __DATA.__objc_const: 0x7c8
+  __DATA.__objc_selrefs: 0x3a0
+  __DATA.__objc_ivar: 0x2c
+  __DATA.__objc_data: 0x140
+  __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Photos.framework/Versions/A/Photos
   - /System/Library/PrivateFrameworks/CloudPhotoServicesConfiguration.framework/Versions/A/CloudPhotoServicesConfiguration
+  - /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84DB9CF6-1EFB-3D05-91F5-BA98976B8D4F
-  Functions: 42
-  Symbols:   46
-  CStrings:  191
+  UUID: 81A010F0-762E-39C5-897B-E0D89B902BFA
+  Functions: 67
+  Symbols:   71
+  CStrings:  305
 
Symbols:
+ _CFRelease
+ _DADiskMount
+ _DASessionCreate
+ _DASessionSetDispatchQueue
+ _NSLocalizedDescriptionKey
+ _NSURLVolumeNameKey
+ _OBJC_CLASS_$_DMManager
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_PHPhotoLibrary
+ _PHPhotosErrorDomain
+ _dispatch_block_create
+ _dispatch_block_wait
+ _dispatch_get_global_queue
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _dispatch_time
+ _kCFAllocatorDefault
+ _objc_retainAutorelease
+ _objc_retainBlock
CStrings:
+ "/"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@24@0:8^@16"
+ "@48@0:8@16@24@32@40"
+ "B24@0:8^@16"
+ "B32@0:8@16^@24"
+ "B40@0:8@16@24^@32"
+ "Disk mount of volume %@ timed out"
+ "Failed to locate System Photos Library"
+ "Failed to locate System Photos Library on mounted volume"
+ "Invalid number of path components in URL"
+ "Missing \"/Volumes\" in URL"
+ "Missing Volumes name in URL"
+ "NO"
+ "PUAUPhotosMigrationPluginIsEnabled"
+ "PhotosSystemPhotoLibraryMigrationTask"
+ "PhotosUserAccountUpdaterTaskRegistration"
+ "SystemPhotosLibraryMigrationTask"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSURL\",&,V_upgradeLibraryURL"
+ "UTF8String"
+ "Unable to create DASession"
+ "Unable to get shared DMManager instance"
+ "Volume %@ not found"
+ "Volumes"
+ "YES"
+ "[PhotosUAUTool] Initiating PhotosUserAccountUpdaterTool with identifier: %s, directory: %s, flo: %s"
+ "[PhotosUAUTool] Photos user account update tool execution %{public}@ finished after %.2fs with status %d"
+ "[PhotosUAUTool] Photos user account update tool execution %{public}@, home directory = %@, updateIsFlo = %{public}@"
+ "[UAUCleanup] Encountered error while deleting subpath %@ in %{public}@: %{public}@ %zd %@ (task %{public}@)"
+ "[UAUCleanup] Failed to remove photos file system location to clean up '%{public}@': %{public}@ %zd %@ (task %@)"
+ "[UAUCleanup] Photos file system location to clean up '%{public}@' exists: %d/%d (task %{public}@)"
+ "[UAUCleanup] Removed photos file system location to clean up '%{public}@' with %lu items (task %@)"
+ "[UAUCleanup] Subpath '%{public}@' does not exist (task %@)"
+ "[UAUCleanup] failed to provide running queue"
+ "[UAUMigration] %{public}@"
+ "[UAUMigration] Completed migration. Success: %{public}@ Error: %@"
+ "[UAUMigration] Exiting PhotosSystemPhotoLibraryMigrationTask, shouldRun: %{public}@"
+ "[UAUMigration] Failed to mount volume for URL: %@. Error: %@"
+ "[UAUMigration] Mount of volume [%@] is done."
+ "[UAUMigration] SPL URL does not contain Volumes"
+ "[UAUMigration] Should run: %{public}@"
+ "[UAUMigration] Starting migration for SPL %@"
+ "[UAUMigration] System Photo Library not found"
+ "[UAUMigration] System Photo Library not found on mounted volume"
+ "[UAUMigration] Unable to create DASession"
+ "[UAUMigration] Unable to get shared DMManager instance"
+ "[UAUMigration] Unexpected empty volume name"
+ "[UAUMigration] Volume %s is already mounted."
+ "[UAUMigration] error while looking for library to upgrade %@"
+ "[UAUMigration] failed to determine if there is a system library: %@"
+ "[UAUMigration] failed to provide running queue"
+ "[UAUMigration] failed to run UAU Migration %@"
+ "[UAUMigration] findURLToUpgrade %@ Error: %@"
+ "[UAUMigration] found System Photo Library: %s"
+ "[UAUMigration] looking for a system photo library"
+ "[UAUPhotosTaskRegistration] Adding task: %{public}@"
+ "[UAUPhotosTaskRegistration] Missing home directory property for cleanup task registration"
+ "[UAUPhotosTaskRegistration] Skipping migration task due to FLO update"
+ "[UAUTaskCollection] Skipping user account updater task %{public}@"
+ "[UAUTaskCollection] User account updater task %{public}@"
+ "[UAUTaskCollection] User account updater task %{public}@ completed with result: %d"
+ "_mountVolumeForVolumeName:dmManager:error:"
+ "_queue"
+ "_upgradeLibraryURL"
+ "addTask:"
+ "arrayWithObjects:count:"
+ "attemptMountVolumeForSystemLibraryURL:error:"
+ "boolValue"
+ "checkResourceIsReachableAndReturnError:"
+ "com.apple.Photos.PhotosUserAccountUpdaterTool.cleanup"
+ "com.apple.Photos.PhotosUserAccountUpdaterTool.migration"
+ "componentsSeparatedByString:"
+ "dictionaryWithObjects:forKeys:count:"
+ "errorWithDomain:code:userInfo:"
+ "initWithLabel:homeDirectoryURL:subpathsToRemove:queue:"
+ "initWithPhotoLibraryURL:"
+ "initWithQueue:"
+ "isEqualToString:"
+ "length"
+ "libraryURLToUpgradeWithError:"
+ "mountedVolumeURLsIncludingResourceValuesForKeys:options:"
+ "numberWithBool:"
+ "objectAtIndex:"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "openAndWaitWithUpgrade:error:"
+ "partitionChildrenForDisk:error:"
+ "partitionMapSchemeForDisk:error:"
+ "queue"
+ "registerCleanupTasksWithCollection:options:"
+ "registerMigrationTasksWithCollection:"
+ "registerTasksWithCollection:options:"
+ "resourceValuesForKeys:error:"
+ "runWithCompletionHandler:"
+ "runWithError:"
+ "setDefaultDASession:"
+ "setQueue:"
+ "setUpgradeLibraryURL:"
+ "sharedManager"
+ "standardUserDefaults"
+ "systemPhotoLibraryURL"
+ "systemPhotoLibraryURLWithError:"
+ "task"
+ "topLevelDisks"
+ "updateIsFLO"
+ "upgradeLibraryURL"
+ "v12@?0i8"
+ "v24@0:8@\"NSObject<PhotosUserAccountUpdaterTask>\"16"
+ "v24@0:8@?<v@?i>16"
+ "v32@0:8@16@24"
+ "volumeNameForDisk:error:"
- "@40@0:8@16@24@32"
- "Account updater task %{public}@ returned non-zero status %d"
- "Account updater task %{public}@ shouldRun: %d"
- "Encountered error while deleting subpath %@ in %{public}@: %{public}@ %zd %@ (task %{public}@)"
- "Failed to remove photos file system location to clean up '%{public}@': %{public}@ %zd %@ (task %@)"
- "Photos file system location to clean up '%{public}@' exists: %d/%d (task %{public}@)"
- "Photos user account update tool execution %{public}@ finished after %.2fs with status %d"
- "Photos user account update tool execution %{public}@, home directory = %@"
- "Removed photos file system location to clean up '%{public}@' with %lu items (task %@)"
- "Subpath '%{public}@' does not exist (task %@)"
- "i16@0:8"
- "initWithHomeDirectoryURL:"
- "initWithLabel:homeDirectoryURL:subpathsToRemove:"
- "run"
- "setupDefaultTasks"

```
