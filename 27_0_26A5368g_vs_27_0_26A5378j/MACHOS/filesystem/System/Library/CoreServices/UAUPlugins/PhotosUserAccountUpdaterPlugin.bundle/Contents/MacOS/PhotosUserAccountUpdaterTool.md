## PhotosUserAccountUpdaterTool

> `/System/Library/CoreServices/UAUPlugins/PhotosUserAccountUpdaterPlugin.bundle/Contents/MacOS/PhotosUserAccountUpdaterTool`

```diff

-  __TEXT.__text: 0x3884
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x47c
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x11c
-  __TEXT.__cstring: 0x5a6
-  __TEXT.__objc_methname: 0xce6
-  __TEXT.__oslogstring: 0x992
-  __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methtype: 0x39a
-  __TEXT.__unwind_info: 0x138
-  __DATA_CONST.__const: 0x1b0
-  __DATA_CONST.__cfstring: 0x460
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__text: 0x49d4
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x4fc
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x180
+  __TEXT.__cstring: 0x655
+  __TEXT.__objc_methname: 0xe87
+  __TEXT.__oslogstring: 0xcf5
+  __TEXT.__objc_classname: 0x106
+  __TEXT.__objc_methtype: 0x3bf
+  __TEXT.__unwind_info: 0x170
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__cfstring: 0x520
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0xa0
-  __DATA.__objc_const: 0x7c8
-  __DATA.__objc_selrefs: 0x398
-  __DATA.__objc_ivar: 0x2c
-  __DATA.__objc_data: 0x140
+  __DATA_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0xb0
+  __DATA.__objc_const: 0x950
+  __DATA.__objc_selrefs: 0x410
+  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_data: 0x190
   __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /System/Library/Frameworks/Photos.framework/Versions/A/Photos
   - /System/Library/PrivateFrameworks/CloudPhotoServicesConfiguration.framework/Versions/A/CloudPhotoServicesConfiguration
   - /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
+  - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/A/PhotoLibraryServicesCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 67
-  Symbols:   70
-  CStrings:  304
+  Functions: 86
+  Symbols:   88
+  CStrings:  353
 
Sections:
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ _CONTAINER_PERSONA_PRIMARY
+ _NSStringFromClass
+ _OBJC_CLASS_$_PLPhotoLibraryPathManagerCore
+ _container_copy_sandbox_token
+ _container_error_copy_unlocalized_description
+ _container_query_create
+ _container_query_free
+ _container_query_get_last_error
+ _container_query_get_single_result
+ _container_query_operation_set_flags
+ _container_query_set_class
+ _container_query_set_identifiers
+ _container_query_set_persona_unique_string
+ _free
+ _objc_opt_isKindOfClass
+ _sandbox_extension_consume
+ _sandbox_extension_release
+ _xpc_string_create
CStrings:
+ "(null)"
+ "."
+ "@40@0:8@16@24@32"
+ "Error executing query: %s"
+ "Library/Containers/com.apple.photolibraryd/Data/Library/Preferences"
+ "MovePhotolibrarydPrivatePrefsToGroupContainerTask"
+ "PhotosMovePhotolibrarydPrivatePrefsToGroupContainerTask"
+ "[PhotosUAUTool] Initiating PhotosUserAccountUpdaterTool with identifier: %s, directory: %s, flo: %s prevOS: %s"
+ "[PhotosUAUTool] Photos user account update tool execution %{public}@, home directory = %@, updateIsFlo = %{public}@ previousOSVersion = %@"
+ "[UAUMovePrefs] %@ = %@"
+ "[UAUMovePrefs] Error: %@ value is not a string (%@)"
+ "[UAUMovePrefs] Failed to access photolibraryd's container"
+ "[UAUMovePrefs] Failed to read source plist: %@"
+ "[UAUMovePrefs] No value for %@ in source plist"
+ "[UAUMovePrefs] failed to delete source, error %@"
+ "[UAUMovePrefs] failed to provide running queue"
+ "[UAUMovePrefs] source path does not exist"
+ "[UAUMovePrefs] source path is %@"
+ "[UAUMovePrefs] source plist deleted"
+ "[UAUMovePrefs] successfully wrote %@ for key %@"
+ "[UAUMovePrefs] unable to initialize user defaults with suite name %@"
+ "[UAUMovePrefs] unexpected existing value for %@: %@, leaving as-is."
+ "[UAUMovePrefs] validation of written value failed"
+ "[UAUPhotosTaskRegistration] Missing home directory property for PhotosMovePhotolibrarydPrivatePrefsToGroupContainerTask task registration"
+ "_accessSourceContainerWithBlock:"
+ "_onQueue_performAction"
+ "_previousOSVersion"
+ "com.apple.photolibraryd"
+ "dictionaryWithContentsOfURL:error:"
+ "fileExistsAtPath:"
+ "fileURLWithPath:"
+ "firstObject"
+ "i16@0:8"
+ "i24@0:8@?16"
+ "initWithQueue:homeDirectoryURL:previousOSVersion:"
+ "initWithSuiteName:"
+ "intValue"
+ "photolibrarydPrivateGroupContainerName"
+ "plist"
+ "previousOSVersion"
+ "registerMigrationTasksWithCollection:options:"
+ "removeItemAtPath:error:"
+ "setObject:forKey:"
+ "stringByAppendingPathComponent:"
+ "stringByAppendingPathExtension:"
+ "systemLibraryPathDefaultsKey"
- "[PhotosUAUTool] Initiating PhotosUserAccountUpdaterTool with identifier: %s, directory: %s, flo: %s"
- "[PhotosUAUTool] Photos user account update tool execution %{public}@, home directory = %@, updateIsFlo = %{public}@"
- "registerMigrationTasksWithCollection:"

```
