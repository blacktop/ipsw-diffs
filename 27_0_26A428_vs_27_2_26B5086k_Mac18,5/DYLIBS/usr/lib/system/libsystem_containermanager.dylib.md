## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-833.0.8.0.1
-  __TEXT.__text: 0x2fb54
+833.40.14.0.0
+  __TEXT.__text: 0x307ec
   __TEXT.__const: 0x434
-  __TEXT.__cstring: 0x3af2
-  __TEXT.__oslogstring: 0x5856
-  __TEXT.__unwind_info: 0x9c0
+  __TEXT.__cstring: 0x3c41
+  __TEXT.__oslogstring: 0x5b30
+  __TEXT.__unwind_info: 0x9d8
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xca0
+  __DATA_CONST.__const: 0xcc0
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x15d0
+  __AUTH_CONST.__const: 0x1600
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__data: 0x478
   __DATA.__data: 0x50
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__bss: 0x1a0
   - /usr/lib/system/libcopyfile.dylib
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 625
-  Symbols:   1013
-  CStrings:  890
+  Functions: 631
+  Symbols:   1021
+  CStrings:  911
 
Symbols:
+ ___container_operation_copy_superseded_block_invoke
+ __container_serialize_copy_deserialized_reference
+ _container_frozenset_get_instance_uuid_of_container_at_index
+ _container_get_instance_uuid
+ _container_object_get_instance_uuid
+ _container_object_set_instance_uuid
+ _container_operation_copy_superseded
+ _container_query_set_instance_uuid
+ _mbr_uid_to_uuid
+ _uuid_clear
- __container_serialize_copy_deserialized_reference_v1
- __container_serialize_copy_deserialized_reference_v2
CStrings:
+ "%s: SPI MISUSE: predecessor required but not valid"
+ "%s: SPI MISUSE: successor provided but not valid"
+ "*"
+ ":"
+ "<none: resuming>"
+ "@(#)VERSION:Container Manager: Sep  3 2026 22:18:46; MobileContainerManager_system-833.40.14~47/arm64e"
+ "CmCo:3:%llu:%u:%s:%s:%s:%s:%s:%u:%u:%s:%s"
+ "ContainerMetadataInstanceUUID"
+ "Failed to convert uid to uuid for required instance uuid; uid = %u, errno = %{darwin.errno}d"
+ "IDENTITY_ALREADY_SUPERSEDED"
+ "INSTANCE_UUID_MISMATCH"
+ "InstanceUUID"
+ "MCMMetadataInstanceUUID"
+ "Metadata plist [%{private}s] has a corrupt instance UUID [🔒%{private}s]."
+ "No usable container in reply during %s"
+ "Query; euid = %u, uid = %u, class = %llu%s, identifier = [%s](%zu), gidentifier = [%s](%zu), instance = 🔒%{private}s, uuid = 🔒%{private}s, flags = %llx"
+ "Query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu%s, identifier = [%s](%zu), gidentifier = [%s](%zu), persona = 🔒%{private}s, instance = 🔒%{private}s, uuid = 🔒%{private}s, flags = %llx"
+ "STALE_FS_NODE"
+ "STALE_XATTR"
+ "Set data protection; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, dpclass = %d, container = 🔒%{private}s, flags = %llx"
+ "SuccessorContainer"
+ "Supersede container; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, successor = 🔒%{private}s, predecessor = 🔒%{private}s, flags = %llx"
+ "[%s%s:%s:%u:%s:(%s%s%s):%s%s%s]%s"
+ "container_get_instance_uuid"
+ "container_operation_copy_superseded"
+ "container_operation_copy_superseded_block_invoke"
+ "container_query_set_instance_uuid"
- "@(#)VERSION:Container Manager: Aug  8 2026 13:21:44; MobileContainerManager_system-833.0.8.0.1~201/arm64e"
- "CmCo:2:%llu:%u:%s:%s:%s:%s:%s:%u:%u:%s"
- "Query; euid = %u, uid = %u, class = %llu%s, identifier = [%s](%zu), gidentifier = [%s](%zu), flags = %llx"
- "Query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu%s, identifier = [%s](%zu), gidentifier = [%s](%zu), flags = %llx"
- "Set data protection; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, dpclass = %d, container = %s, flags = %llx"
- "[%s%s:%s:%u:%s:(%s%s%s):%s]%s"
```
