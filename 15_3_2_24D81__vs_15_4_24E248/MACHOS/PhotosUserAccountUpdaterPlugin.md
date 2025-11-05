## PhotosUserAccountUpdaterPlugin

> `/System/Library/CoreServices/UAUPlugins/PhotosUserAccountUpdaterPlugin.bundle/Contents/MacOS/PhotosUserAccountUpdaterPlugin`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x1ab4
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x1c0
-  __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__cstring: 0x3cd
-  __TEXT.__objc_methname: 0xa63
-  __TEXT.__oslogstring: 0x3fc
-  __TEXT.__objc_classname: 0xc0
-  __TEXT.__objc_methtype: 0x346
-  __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__auth_got: 0xb8
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__cfstring: 0x2c0
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x20
+751.0.104.0.0
+  __TEXT.__text: 0x70c
+  __TEXT.__auth_stubs: 0xb0
+  __TEXT.__objc_stubs: 0x220
+  __TEXT.__objc_methlist: 0x1b4
+  __TEXT.__const: 0x20
+  __TEXT.__oslogstring: 0x299
+  __TEXT.__cstring: 0x89
+  __TEXT.__objc_classname: 0x45
+  __TEXT.__objc_methname: 0x3c9
+  __TEXT.__objc_methtype: 0x112
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__auth_got: 0x60
+  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__const: 0x30
+  __DATA_CONST.__cfstring: 0x80
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x90
-  __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_const: 0xb48
-  __DATA.__objc_selrefs: 0x1c0
-  __DATA.__objc_ivar: 0x24
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x180
+  __DATA.__objc_const: 0x258
+  __DATA.__objc_selrefs: 0x170
+  __DATA.__objc_ivar: 0x4
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Photos.framework/Versions/A/Photos
+  - /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
   - /System/Library/PrivateFrameworks/UAUPlugin.framework/Versions/A/UAUPlugin
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F8EE553-C63E-3F0D-82E5-324300454B8E
-  Functions: 47
-  Symbols:   46
-  CStrings:  223
+  UUID: D1C9EAC7-9D6E-362B-9803-5C074A874063
+  Functions: 9
+  Symbols:   28
+  CStrings:  90
 
Symbols:
+ _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSString
- _OBJC_CLASS_$_PhotosFileSystemCleanupTask
- _OBJC_CLASS_$_PhotosUserAccountUpdaterTaskCollection
- _OBJC_METACLASS_$_PhotosFileSystemCleanupTask
- _OBJC_METACLASS_$_PhotosUserAccountUpdaterTaskCollection
- __Block_object_assign
- __Block_object_dispose
- __Unwind_Resume
- ___objc_personality_v0
- _objc_alloc
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_autoreleaseReturnValue
- _objc_enumerationMutation
- _objc_msgSendSuper2
- _objc_opt_new
CStrings:
+ "[PhotosUAUPlugin] Launching Photos user account update helper tool %{public}@ for update %{public}@, home directory: %@, FLO is enabled: %{public}@"
+ "[PhotosUAUPlugin] Photos user account update helper tool finished execution %{public}@ successfully"
+ "[PhotosUAUPlugin] Photos user account update helper tool finished execution %{public}@ with non-zero status %d"
+ "[PhotosUAUPlugin] Skipping Photos user account update because the current OS version is lower than expected: %{public}@"
+ "[PhotosUAUPlugin] Unable to launch Photos user account update helper tool: %{public}@"
+ "[PhotosUAUPlugin] Unexpected nil updater parameters"
+ "[PhotosUAU] Photos user account update not required"
+ "[PhotosUAU] Photos user account update required"
+ "numberWithBool:"
+ "stringValue"
+ "updateIsFLO"
- "<%@: %p '%@'>"
- "@\"NSArray\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSURL\""
- "@24@0:8@16"
- "@40@0:8@16@24@32"
- "Account updater task %{public}@ returned non-zero status %d"
- "Account updater task %{public}@ shouldRun: %d"
- "B32@0:8@\"NSFileManager\"16@\"NSString\"24"
- "B32@0:8@\"NSFileManager\"16@\"NSURL\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"NSFileManager\"16@\"NSError\"24@\"NSString\"32"
- "B40@0:8@\"NSFileManager\"16@\"NSError\"24@\"NSURL\"32"
- "B40@0:8@\"NSFileManager\"16@\"NSString\"24@\"NSString\"32"
- "B40@0:8@\"NSFileManager\"16@\"NSURL\"24@\"NSURL\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@\"NSFileManager\"16@\"NSError\"24@\"NSString\"32@\"NSString\"40"
- "B48@0:8@\"NSFileManager\"16@\"NSError\"24@\"NSURL\"32@\"NSURL\"40"
- "B48@0:8@16@24@32@40"
- "Encountered error while deleting subpath %@ in %{public}@: %{public}@ %zd %@ (task %{public}@)"
- "Failed to remove photos file system location to clean up '%{public}@': %{public}@ %zd %@ (task %@)"
- "Invalid parameter not satisfying: %@"
- "Launching Photos user account update helper tool %{public}@ for update %{public}@"
- "Legacy photo stream caches"
- "Library/Application Support/iLifeAssetManagement"
- "Library/Containers/com.apple.MediaLibraryService/Data/Library/Caches/com.apple.iLifeMediaBrowser.ILPhotosTranscodeCache"
- "Library/Containers/com.apple.Photos/Data/Library/Caches/Photos/Mondrian"
- "Library/Containers/com.apple.ScreenSaver.iLife-Slideshow-Extension/Data/Library/Caches/com.apple.iLifeMediaBrowser.ILPhotosTranscodeCache"
- "Library/Containers/com.apple.cloudphotosd"
- "Library/MediaStream"
- "Mondrian cache"
- "NSFileManagerDelegate"
- "Photos file system location to clean up '%{public}@' exists: %d/%d (task %{public}@)"
- "Photos user account update helper tool finished execution %{public}@ successfully"
- "Photos user account update helper tool finished execution %{public}@ with non-zero status %d"
- "Photos user account update not required"
- "Photos user account update required"
- "PhotosFileSystemCleanupTask"
- "PhotosFileSystemCleanupTask.m"
- "PhotosUserAccountUpdaterTask"
- "PhotosUserAccountUpdaterTaskCollection"
- "PhotosUserAccountUpdaterTaskCollection.m"
- "Removed photos file system location to clean up '%{public}@' with %lu items (task %@)"
- "Skipping Photos user account update because the current OS version is lower than expected: %{public}@"
- "Subpath '%{public}@' does not exist (task %@)"
- "T@\"NSArray\",&,V_subpathsToRemove"
- "T@\"NSMutableArray\",&,V_tasks"
- "T@\"NSString\",&,V_currentlyProcessingSubpath"
- "T@\"NSString\",&,V_label"
- "T@\"NSString\",R"
- "T@\"NSString\",R,Vlabel"
- "T@\"NSURL\",&,V_homeDirectoryURL"
- "TB,R"
- "Tq,V_removedFileCount"
- "URLByAppendingPathComponent:"
- "Unable to launch Photos user account update helper tool: %{public}@"
- "Unexpected nil currently processing subpath"
- "Unexpected nil updater parameters"
- "Unexpected non-nil currently processing subpath %@ (task %@)"
- "[subpaths count]"
- "_currentlyProcessingSubpath"
- "_homeDirectoryURL"
- "_label"
- "_removedFileCount"
- "_subpathsToRemove"
- "_tasks"
- "addObject:"
- "anySubPathToRemoveExists"
- "array"
- "code"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentlyProcessingSubpath"
- "defaultManager"
- "domain"
- "enumerateObjectsUsingBlock:"
- "enumerateURLsToRemove:"
- "fileExistsAtPath:isDirectory:"
- "fileManager:shouldCopyItemAtPath:toPath:"
- "fileManager:shouldCopyItemAtURL:toURL:"
- "fileManager:shouldLinkItemAtPath:toPath:"
- "fileManager:shouldLinkItemAtURL:toURL:"
- "fileManager:shouldMoveItemAtPath:toPath:"
- "fileManager:shouldMoveItemAtURL:toURL:"
- "fileManager:shouldProceedAfterError:copyingItemAtPath:toPath:"
- "fileManager:shouldProceedAfterError:copyingItemAtURL:toURL:"
- "fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:"
- "fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:"
- "fileManager:shouldProceedAfterError:movingItemAtPath:toPath:"
- "fileManager:shouldProceedAfterError:movingItemAtURL:toURL:"
- "fileManager:shouldProceedAfterError:removingItemAtPath:"
- "fileManager:shouldProceedAfterError:removingItemAtURL:"
- "fileManager:shouldRemoveItemAtPath:"
- "fileManager:shouldRemoveItemAtURL:"
- "homeDirectoryURL"
- "i16@0:8"
- "iLMB transcode cache"
- "iLMB transcode cache for iLSS"
- "init"
- "initWithHomeDirectoryURL:"
- "initWithLabel:homeDirectoryURL:subpathsToRemove:"
- "label"
- "objectAtIndexedSubscript:"
- "q"
- "q16@0:8"
- "removeItemAtURL:error:"
- "removedFileCount"
- "run"
- "setCurrentlyProcessingSubpath:"
- "setDelegate:"
- "setHomeDirectoryURL:"
- "setLabel:"
- "setRemovedFileCount:"
- "setSubpathsToRemove:"
- "setTasks:"
- "setupDefaultTasks"
- "shouldRun"
- "stringWithFormat:"
- "subpathsToRemove"
- "tasks"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v32@?0@\"NSString\"8Q16^B24"
- "v32@?0@\"NSURL\"8@\"NSString\"16^B24"

```
