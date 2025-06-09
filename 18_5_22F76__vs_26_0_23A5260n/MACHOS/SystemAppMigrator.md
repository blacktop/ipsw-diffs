## SystemAppMigrator

> `/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator`

```diff

-1378.100.35.0.0
-  __TEXT.__text: 0xa1a4
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_stubs: 0x1860
-  __TEXT.__objc_methlist: 0x7c4
-  __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x34c
-  __TEXT.__cstring: 0x3309
-  __TEXT.__objc_methname: 0x2453
-  __TEXT.__objc_classname: 0xbf
-  __TEXT.__objc_methtype: 0x568
+1513.0.8.0.2
+  __TEXT.__text: 0x78d4
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_stubs: 0x1600
+  __TEXT.__objc_methlist: 0x5fc
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x2b08
+  __TEXT.__gcc_except_tab: 0x240
+  __TEXT.__objc_methname: 0x1deb
+  __TEXT.__objc_classname: 0xad
+  __TEXT.__objc_methtype: 0x3cf
   __TEXT.__oslogstring: 0x142
-  __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__auth_got: 0x450
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x378
-  __DATA_CONST.__cfstring: 0x17e0
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__unwind_info: 0x1e8
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x328
+  __DATA_CONST.__cfstring: 0x15a0
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0xa50
-  __DATA.__objc_selrefs: 0x848
-  __DATA.__objc_ivar: 0x68
-  __DATA.__objc_data: 0x140
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x850
+  __DATA.__objc_selrefs: 0x728
+  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
   __DATA.__common: 0x8
   __DATA.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E9574D99-AFB6-3481-8981-C438278BDBC7
-  Functions: 165
-  Symbols:   230
-  CStrings:  833
+  UUID: 2CBD09F4-27D6-39B8-A8C3-2777A7AA2562
+  Functions: 123
+  Symbols:   177
+  CStrings:  705
 
Symbols:
+ _SystemAppMigratorVersionNumber
+ _SystemAppMigratorVersionString
- _NSFilePathErrorKey
- _OBJC_CLASS_$_MITestManager
- _OBJC_CLASS_$_NSData
- _OBJC_METACLASS_$_MIMCMContainer
- __CFXPCCreateCFObjectFromXPCObject
- __CFXPCCreateXPCObjectFromCFObject
- _container_copy_object
- _container_copy_unlocalized_description
- _container_delete_all_container_content
- _container_disk_usage
- _container_error_free
- _container_error_get_path
- _container_error_get_posix_errno
- _container_error_get_type
- _container_free_array_of_containers
- _container_free_object
- _container_get_class
- _container_get_error_description
- _container_get_identifier
- _container_get_info_value_for_key
- _container_get_path
- _container_get_persona_unique_string
- _container_is_equal
- _container_is_new
- _container_is_transient
- _container_operation_delete_array
- _container_operation_delete_reclaim_disk_space
- _container_query_create
- _container_query_create_from_container
- _container_query_free
- _container_query_get_last_error
- _container_query_get_single_result
- _container_query_iterate_results_sync
- _container_query_operation_set_flags
- _container_query_set_class
- _container_query_set_group_identifiers
- _container_query_set_identifiers
- _container_query_set_include_other_owners
- _container_query_set_persona_unique_string
- _container_query_set_transient
- _container_recreate_structure
- _container_regenerate_uuid
- _container_replace
- _container_serialize_copy_deserialized_reference
- _container_serialize_copy_serialized_reference
- _container_set_info_value
- _container_subdirectories_for_class
- _exit
- _malloc_type_calloc
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_retain_x7
- _xpc_array_append_value
- _xpc_array_create
- _xpc_string_create
CStrings:
- "%s"
- "(container_get_error_description returned NULL)"
- "+[MIMCMContainer _containerForIdentifier:contentClass:forPersona:transient:create:error:]"
- "+[MIMCMContainer _enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:]"
- "+[MIMCMContainer _enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:]_block_invoke"
- "+[MIMCMContainer defaultDirectoriesForContainerType:error:]"
- "+[MIMCMContainer deleteContainers:waitForDeletion:error:]"
- "-[MIMCMContainer _doInitWithContainer:error:]"
- "-[MIMCMContainer _refreshContainerMetadataWithError:]"
- "-[MIMCMContainer diskUsage]"
- "-[MIMCMContainer infoValueForKey:error:]"
- "-[MIMCMContainer initWithSerializedContainer:matchingWithOptions:error:]"
- "-[MIMCMContainer purgeContentWithError:]"
- "-[MIMCMContainer reclaimDiskSpaceWithError:]"
- "-[MIMCMContainer recreateDefaultStructureWithError:]"
- "-[MIMCMContainer regenerateDirectoryUUIDWithError:]"
- "-[MIMCMContainer replaceExistingContainer:error:]"
- "-[MIMCMContainer setInfoValue:forKey:error:]"
- "<%@ container=%@ persona=%@ path=%@>"
- "<No container description>"
- "@\"NSURL\""
- "@32@0:8@16^@24"
- "@32@0:8^{container_object_s=}16^@24"
- "@40@0:8@16Q24^@32"
- "@44@0:8Q16@24B32^@36"
- "@48@0:8@16@24B32B36^@40"
- "@52@0:8@16Q24@32B40^@44"
- "@56@0:8@16Q24@32B40B44^@48"
- "@60@0:8Q16@24B32@36@44@?52"
- "@64@0:8@16@24Q32@40B48B52^@56"
- "@64@0:8Q16@24B32@36@44B52@?56"
- "B"
- "B16@?0@\"MIMCMContainer\"8"
- "B16@?0^{container_object_s=}8"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "B32@0:8^{container_object_s=}16^@24"
- "B36@0:8@16B24^@28"
- "Container query for %@ create: %d transient: %d with nil persona"
- "Error getting disk usage for %@ (%ld): %@"
- "Exiting before replacing transient bundle container: %@"
- "Failed to allocate memory for deleting containers"
- "Failed to construct MIMCMContainer instance with container %@ : %@"
- "Failed to create container query for querying containers for identifier %@"
- "Failed to create container query for querying containers for identifier: %@ groupIdentifiers: %@ containerType: %llu"
- "Failed to fetch container URL from %@"
- "Failed to get identifier for the container"
- "Failed to read container error path"
- "Failed to retrieve container subdirectories for class %llu"
- "Failed to retrieve value for key %@ from the underlying xpc object"
- "Failed to wipe container for identifier %@"
- "MIMCMContainer"
- "Q"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_personaUniqueString"
- "T@\"NSURL\",R,N,V_containerURL"
- "TB,N,V_isTransient"
- "TB,R,N,V_isNew"
- "TQ,R,N"
- "TQ,R,N,V_containerClass"
- "T^{container_object_s=},R,N,V_mcmContainer"
- "Underlying errno set by container manager is %s"
- "^{container_object_s=}"
- "^{container_object_s=}16@0:8"
- "_ContainerURL"
- "_allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:error:"
- "_containerClass"
- "_containerForIdentifier:contentClass:forPersona:transient:create:error:"
- "_containerURL"
- "_doInitWithContainer:error:"
- "_enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:"
- "_identifier"
- "_isNew"
- "_isTransient"
- "_mcmContainer"
- "_personaUniqueString"
- "_refreshContainerMetadataWithError:"
- "bytes"
- "containerClass"
- "containerURL"
- "container_operation_delete_array returned NULL but did not set an error"
- "containersForBundleIdentifier:contentClass:forPersona:create:fetchTransient:error:"
- "containersForContentClass:forPersona:fetchTransient:error:"
- "containersForGroupIdentifier:forPersona:create:fetchTransient:error:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dealloc"
- "defaultDirectoriesForContainerType:error:"
- "deleteContainers:waitForDeletion:error:"
- "diskUsage"
- "enumerateContainersWithClass:forPersona:isTransient:identifiers:groupIdentifiers:usingBlock:"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "identifier"
- "initWithContainer:error:"
- "initWithSerializedContainer:matchingWithOptions:error:"
- "isNew"
- "isTransient"
- "length"
- "mcmContainer"
- "personaUniqueString"
- "purgeContentWithError:"
- "reclaimDiskSpaceWithError:"
- "recreateDefaultStructureWithError:"
- "regenerateDirectoryUUIDWithError:"
- "replaceExistingContainer:error:"
- "serializedContainerRepresentation"
- "setInfoValue:forKey:error:"
- "setIsTransient:"
- "testFlagsAreSet:"
- "transientContainerForIdentifier:contentClass:forPersona:create:error:"
- "v20@0:8B16"

```
