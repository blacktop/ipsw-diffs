## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-725.160.3.0.0
-  __TEXT.__text: 0x2db04
+725.160.3.701.2
+  __TEXT.__text: 0x2dad8
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__const: 0x290
-  __TEXT.__cstring: 0x38df
-  __TEXT.__oslogstring: 0x4fe8
+  __TEXT.__const: 0x278
+  __TEXT.__cstring: 0x38e4
+  __TEXT.__oslogstring: 0x4de8
   __TEXT.__unwind_info: 0x6a0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xc98
Functions:
~ ___container_paths_enumerate_containers_at_block_invoke : 2608 -> 2604
~ __container_authorize_execute : 3020 -> 3008
~ __container_add_remove : 2324 -> 2316
~ __container_references_query_execute : 2564 -> 2556
~ __container_query_execute : 3076 -> 3064
~ __container_info_execute : 2304 -> 2296
~ ___container_create_or_lookup_app_group_path_by_app_group_identifier_block_invoke : 2256 -> 2264
CStrings:
+ "%s connection sharing"
+ "%s(container, %s)"
+ "%s(container, %s): %s container extension"
+ "%s(container, %s): no sandbox token in container"
+ "%s: client had ambiguous persona during request"
+ "%s: client had incorrect persona during request"
+ "%s: client is not entitled"
+ "%s: client persona did not propagate to container manager"
+ "%s: client sent invalid parameters"
+ "%s: client uid is not permitted, uid = %{public}u"
+ "%s: enumeration failure opening container dir [%llu]: %s"
+ "%s: enumeration failure processing container [%s][%llu]: %s"
+ "%s: enumeration of path [%s]: success = %d, found container = %d"
+ "%s: error = %s"
+ "%s: error = ((container_error_t)%{public}llu) %s"
+ "%s: failed (errors during enumeration)"
+ "%s: success"
+ "@(#)VERSION:Container Manager: Aug  1 2026 02:05:44; MobileContainerManager_system-725.160.3.701.2~2/arm64e"
+ "Container delete; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, manifest = %{private}s"
+ "Could not decode message into container object: %s"
+ "Could not decode message into error: %s"
+ "Enumerate; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, context<path = [%s], class = %llu, flags = 0x%llx, persona = [%s], uid = %u, transient = %d>"
+ "Failed to issue sandbox extension to [%s] for containermanagerd"
+ "Metadata plist [%{private}s] is has a corrupt UUID [%s]."
+ "Query; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu, identifier = [%s](%zu), flags = %llx"
+ "Query; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, query = %s"
+ "References query; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, query = %s"
+ "Requesting app group container lookup; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], identifier = %{private}s, euid = %u, uid = %u, platform = %u"
+ "Requesting container lookup; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], bundle = [%s], root = [%s], executable = [%s], flags = %llu, euid = %u, uid = %u"
+ "Requesting container lookup; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], class = %llu, identifier = %{private}s, group_identifier = %{private}s, create = %d, temp = %d, euid = %u, uid = %u"
+ "Requesting multiple containers; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], class = %llu, temp = %d, euid = %u, uid = %u"
+ "Unable to get bundle from [%s]"
+ "Unable to get bundle root path from bundle at [%s]: %{public}d"
+ "Unable to get executable path from bundle at [%s]: %{public}d"
+ "Unable to get user (%u) home path, container results may not be reliable; error = %s"
+ "Unable to get user home path, container results may not be reliable; error = %s"
+ "Unable to obtain a task info for pid %i: %s (0x%x)"
+ "Unable to obtain a task name port right for pid %i: %s (0x%x)"
+ "Update info; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu, identifier = %s, key = [%s](%zu), flags = %llx"
+ "Update info; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, message = %s"
+ "Wait for obliteration; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u"
+ "received superfluous connection%s event, ignoring"
+ "sandbox_extension_issue_file failed for class %s at path [%s]: %d"
- "%{public}s connection sharing"
- "%{public}s(container, %{public}s)"
- "%{public}s(container, %{public}s): %{public}s container extension"
- "%{public}s(container, %{public}s): no sandbox token in container"
- "%{public}s: client had ambiguous persona during request"
- "%{public}s: client had incorrect persona during request"
- "%{public}s: client is not entitled"
- "%{public}s: client persona did not propagate to container manager"
- "%{public}s: client sent invalid parameters"
- "%{public}s: client uid is not permitted, uid = %{public}u"
- "%{public}s: enumeration failure opening container dir [%llu]: %s"
- "%{public}s: enumeration failure processing container [%s][%llu]: %s"
- "%{public}s: enumeration of path [%s]: success = %d, found container = %d"
- "%{public}s: error = %{public}s"
- "%{public}s: error = ((container_error_t)%{public}llu) %{public}s"
- "%{public}s: failed (errors during enumeration)"
- "%{public}s: success"
- "@(#)VERSION:Container Manager: Jul 31 2026 18:24:45; MobileContainerManager_system-725.160.3~57/arm64e"
- "Container delete; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, manifest = %{private}s"
- "Could not decode message into container object: %{public}s"
- "Could not decode message into error: %{public}s"
- "Enumerate; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, context<path = [%s], class = %llu, flags = 0x%llx, persona = [%{public}s], uid = %u, transient = %d>"
- "Failed to issue sandbox extension to [%{public}s] for containermanagerd"
- "Metadata plist [%{private}s] is has a corrupt UUID [%{public}s]."
- "Query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu, identifier = [%s](%zu), flags = %llx"
- "Query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, query = %s"
- "References query; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, query = %s"
- "Requesting app group container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], identifier = %{private}s, euid = %u, uid = %u, platform = %u"
- "Requesting container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], bundle = [%{public}s], root = [%{public}s], executable = [%{public}s], flags = %llu, euid = %u, uid = %u"
- "Requesting container lookup; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], class = %llu, identifier = %{private}s, group_identifier = %{private}s, create = %d, temp = %d, euid = %u, uid = %u"
- "Requesting multiple containers; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], class = %llu, temp = %d, euid = %u, uid = %u"
- "Unable to get bundle from [%{public}s]"
- "Unable to get bundle root path from bundle at [%{public}s]: %{public}d"
- "Unable to get executable path from bundle at [%{public}s]: %{public}d"
- "Unable to get user (%u) home path, container results may not be reliable; error = %{public}s"
- "Unable to get user home path, container results may not be reliable; error = %{public}s"
- "Unable to obtain a task info for pid %i: %{public}s (0x%x)"
- "Unable to obtain a task name port right for pid %i: %{public}s (0x%x)"
- "Update info; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, class = %llu, identifier = %s, key = [%s](%zu), flags = %llx"
- "Update info; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, message = %s"
- "Wait for obliteration; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u"
- "received superfluous connection%{public}s event, ignoring"
- "sandbox_extension_issue_file failed for class %{public}s at path [%s]: %d"
```
