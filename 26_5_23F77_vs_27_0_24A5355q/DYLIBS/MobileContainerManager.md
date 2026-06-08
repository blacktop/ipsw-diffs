## MobileContainerManager

> `/System/Library/PrivateFrameworks/MobileContainerManager.framework/MobileContainerManager`

```diff

-725.120.2.0.0
-  __TEXT.__text: 0x2d70
-  __TEXT.__auth_stubs: 0x440
+826.0.0.0.1
+  __TEXT.__text: 0x2cdc
   __TEXT.__objc_methlist: 0x39c
   __TEXT.__const: 0x330
-  __TEXT.__cstring: 0xa2
+  __TEXT.__cstring: 0xa4
   __TEXT.__oslogstring: 0x171
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x1a0
-  __TEXT.__objc_methname: 0x67f
-  __TEXT.__objc_methtype: 0x1b9
-  __TEXT.__objc_stubs: 0x460
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__unwind_info: 0xf8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1c0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0xac0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x14
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 192ADAC6-18C7-3420-B911-89984E21C09C
+  UUID: CDD57769-18BE-3563-9EBD-0B7D2FD936B7
   Functions: 64
-  Symbols:   424
-  CStrings:  136
+  Symbols:   431
+  CStrings:  20
 
Symbols:
+ _CONTAINER_POSIX_OWNERSHIP_NULL
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
CStrings:
- ".cxx_destruct"
- "@\"NSString\""
- "@\"NSUUID\""
- "@16@0:8"
- "@24@0:8@?16"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@32@0:8q16^@24"
- "@36@0:8q16B24^@28"
- "@40@0:8@16^B24^@32"
- "@40@0:8q16@24^@32"
- "@44@0:8@16B24^B28^@36"
- "@48@0:8@16B24^B28B36^@40"
- "@48@0:8q16@24^B32^@40"
- "@52@0:8q16@24B32^B36^@44"
- "@68@0:8@16@24@32@40@48I56^@60"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@16@24"
- "B40@0:8@16@24^@32"
- "B48@0:8@16@24^@32@?40"
- "Internal"
- "LowLevel"
- "MCMAppContainer"
- "MCMAppDataContainer"
- "MCMContainer"
- "MCMContainerManager"
- "MCMDataContainer"
- "MCMFrameworkContainer"
- "MCMInternalDaemonDataContainer"
- "MCMPerUserAppContainer"
- "MCMPluginKitPluginContainer"
- "MCMPluginKitPluginDataContainer"
- "MCMSharedDataContainer"
- "MCMSharedSystemDataContainer"
- "MCMSystemDataContainer"
- "MCMTempDirDataContainer"
- "MCMVPNPluginContainer"
- "MCMVPNPluginDataContainer"
- "MCMXPCServiceDataContainer"
- "Q16@0:8"
- "Q24@0:8^@16"
- "T@\"NSDictionary\",R,N"
- "T@\"NSString\",R,N"
- "T@\"NSURL\",R,N"
- "T@\"NSUUID\",R,D,N"
- "TB,R,N,GisTemporary"
- "T^{container_object_s=},R,N"
- "Tq,R,N"
- "UTF8String"
- "^{container_object_s=}"
- "^{container_object_s=}16@0:8"
- "_containerClass"
- "_containersWithClass:temporary:error:"
- "_errorOccurred"
- "_identifier"
- "_obj1:isEqualToObj2:"
- "_personaUniqueString"
- "_thisContainer"
- "_uuid"
- "addObject:"
- "arrayWithObjects:count:"
- "containerClass"
- "containerWithContentClass:identifier:createIfNecessary:existed:error:"
- "containerWithContentClass:identifier:error:"
- "containerWithIdentifier:createIfNecessary:existed:error:"
- "containerWithIdentifier:error:"
- "containersWithClass:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "defaultManager"
- "deleteContainers:withCompletion:"
- "description"
- "destroyContainerWithCompletion:"
- "diskUsageWithError:"
- "errorWithDomain:code:userInfo:"
- "fileSystemRepresentation"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "getLowLevelContainerObject"
- "getUUIDBytes:"
- "hash"
- "identifier"
- "info"
- "infoValueForKey:error:"
- "init"
- "initWithIdentifier:createIfNecessary:existed:temp:error:"
- "initWithIdentifier:path:uniquePathComponent:uuid:personaUniqueString:uid:error:"
- "initWithUUIDBytes:"
- "isEqual:"
- "isEqualToContainer:"
- "isTemporary"
- "markDeleted"
- "objectAtIndex:"
- "personaUniqueString"
- "q"
- "q16@0:8"
- "recreateDefaultStructureWithError:"
- "regenerateDirectoryUUIDWithError:"
- "replaceContainer:withContainer:error:"
- "replaceContainer:withContainer:error:withCompletion:"
- "setInfoValue:forKey:error:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "temporary"
- "temporaryContainerWithContentClass:identifier:existed:error:"
- "temporaryContainerWithIdentifier:existed:error:"
- "temporaryContainersWithClass:error:"
- "thisContainer"
- "typeContainerClass"
- "url"
- "uuid"
- "v16@0:8"
- "wipeAllMyContainerContent:"

```
