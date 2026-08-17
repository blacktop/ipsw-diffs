## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/Versions/A/ContainerManagerCommon`

```diff

-725.160.3.0.0
-  __TEXT.__text: 0xee43c
+725.160.3.701.2
+  __TEXT.__text: 0xee3f8
   __TEXT.__auth_stubs: 0x1f70
   __TEXT.__objc_methlist: 0x9fb4
-  __TEXT.__const: 0x11f8
+  __TEXT.__const: 0x11b8
   __TEXT.__swift5_typeref: 0x5bd
-  __TEXT.__oslogstring: 0xc470
-  __TEXT.__cstring: 0x93eb
+  __TEXT.__oslogstring: 0xc138
+  __TEXT.__cstring: 0x93ef
   __TEXT.__constg_swiftt: 0x5a8
   __TEXT.__swift5_reflstr: 0x38a
   __TEXT.__swift5_fieldmd: 0x420
Functions:
~ __containermanagerd_posix_user_has_home_dir : 788 -> 784
~ ____containermanagerd_listener_handler_for_permanent_error_block_invoke : 660 -> 656
~ -[MCMFileManager diskUsageForURL:] : 1008 -> 1004
~ -[MCMMetadataMinimal initByReadingAndValidatingMetadataAtFileURL:containerPath:userIdentity:containerClass:userIdentityCache:error:] : 3040 -> 3036
~ -[MCMMetadata writeMetadataToFileURL:options:error:] : 2244 -> 2236
~ -[MCMCommandOpenPrimordialDataContainer execute] : 1696 -> 1692
~ ___MCMPersonasAreSupported_block_invoke : 708 -> 704
~ -[MCMUserIdentityCache _lock_resync_fromUserPersonaAttributes:] : 4504 -> 4492
~ -[MCMContainerSchema _executeActions:error:] : 948 -> 944
~ -[MCMContainerSchema _actionsFromVersion:toTargetVersion:context:error:] : 2248 -> 2240
~ -[MCMContainerSchema writeSchemaFromVersion:toTargetVersion:error:] : 1852 -> 1840
CStrings:
+ "%@"
+ "%@ (%@)"
+ "%@ primordial container for '%@' with identifier '%@': error = %@"
+ "%s called before createIfNecessaryWithError:, result may not be valid"
+ "Attempt to create a container identity without a user identity when one is required; identifier = [%@], class = %@"
+ "Cannot find user [%@] specified for bundle container owner, continuing without bundle container support"
+ "Cannot find user [%@] specified for system container owner, continuing without system container support"
+ "Client (%@, %d) requests no container with no-container entitlement"
+ "Container delete; personaid = %u, type = %s, name = %s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, message = %{private}s"
+ "Could not create app group symlink for [%@], falling back to realpath: %@"
+ "Could not generate posix user details for user=%@"
+ "Could not read metadata file at [%@]; error = %@"
+ "Created new POSIX user: %@"
+ "Entered sandbox with HOME: [%s], MACH_LISTENER_NAME: [%s], UID: [%s]"
+ "Error de-elevating inactive jetsam priority: %s"
+ "Error elevating inactive jetsam priority: %s"
+ "Error fetching sandbox extension for persona %@, path %@"
+ "Failed creating working directories for %@: %@"
+ "Failed creating working directories: %@"
+ "Failed to check for existence of %s user home directory [%@]: %@"
+ "Failed to connect container cache database: %@"
+ "Failed to create deathrow at %@: %@"
+ "Failed to enter sandbox: %s"
+ "Failed to get dirstats on %s using fallback: (err %d) %s"
+ "Failed to get fsNode for [%@] when checking for file system changes: %@"
+ "Fetching primordial container for '%@' with identifier '%llu:%@' (%s)"
+ "Invalid app group identifier [%@]"
+ "Invalid nil parameter passed to %s; %d"
+ "Invalid size (%lld) from dirstats on %s using fallback: (err %d) %s"
+ "Metadata file at [%@] is corrupt."
+ "MobileContainerManager-725.160.3.701.2~2"
+ "Path [%@] changed: old = %@, new = %@"
+ "Persona of unknown type %lu being treated as Unspecific: %@"
+ "Personas are supported (static): %s (%s%s%s%s%s%s%s) {pid: %d, uid: %u, apid: %d, auid: %u, asid: %d, session: %s}"
+ "Read [%@], length = %{public}lu, options = 0x%{public}lx"
+ "Reference count for [%@] is %lu"
+ "System container lookup failed, class = %@, identifier = %@, error = (%llu)%@, client = %@"
+ "Unable to get user (%u/[%@]/%{public}d); error = %s"
+ "User home directory at [%@] does not exist"
+ "Using app group symlink for [%@]: %@"
+ "Warning: not remapping plugin identifier '%@ to parent identifier [3]"
+ "Wrote [%@], length = %{public}lu, options = 0x%{public}lx, mode = 0%{public}o"
+ "[%@] is a plugin"
+ "[%s] Enabled APFSIOC_DIR_STATS_OP"
+ "[%s] Enabled APFSIOC_MAINTAIN_DIR_STATS"
+ "[%s] Enabling fast disk sizing failed: %@"
+ "[%s] Failed to get dirstats: %{darwin.errno}d"
+ "[%s] Failed to set maintain-dir-stats: %{darwin.errno}d"
+ "[%s] Fast disk sizing failed: %{darwin.errno}d"
+ "[%s] Invalid size (%lld) from dirstats: %{darwin.errno}d"
+ "[%s]: descendants: %llu, total size: %llu [ph%llu; cl%llu; pu%llu]"
+ "[%s]: descendants: %llu, total size: %llu, using fallback"
+ "[%u]%s command=%llu, client=%s(uid: %u, pid: %d), error=%llu (%s)"
+ "[u %@:p %@:c %@(%{public}llu):i%llu] Action [%@] failed; error = %@"
+ "[u %@:p %@:c %@(%{public}llu):i%llu] Could not fetch fsNode for [%@]: %@"
+ "[u %@:p %@:c %@(%{public}llu):i%llu] Could not form action [%@] with args: %@, error = %@"
+ "[u %@:p %@:c %@(%{public}llu):i%llu] Could not update schema from (%@) → (%@), actions count = %{public}lu, error = %@"
+ "[u %@:p %@:c %@(%{public}llu):i%llu] Could not update schema from (%@) → (%@), no actions available"
+ "[u %@:p %@:c %@(%{public}llu):i%llu] Read metadata from [%@]: %@"
+ "[u %@:p %@:c %@(%{public}llu):i%llu] Successfully updated schema from (%@) → (%@), actions count = %{public}lu"
+ "[u %@:p %@:c %@(%{public}llu):i%llu] Trying to target a version [%@] higher than available [%lu], capping to max"
+ "[u %@:p %@:c %@(%{public}llu):i%llu] Wrote metadata to [%@]: %@"
+ "container_realpath([%@]) failed: %{public, darwin.errno}d"
+ "container_realpath([%@]) → [%@]"
+ "containermanagerd (%s) built at %s %s started"
+ "listAllPersonaAttributes (%f s): error = %@, attributes = %@"
- "%{public}@"
- "%{public}@ (%{public}@)"
- "%{public}@ primordial container for '%{public}@' with identifier '%{public}@': error = %@"
- "%{public}s called before createIfNecessaryWithError:, result may not be valid"
- "Attempt to create a container identity without a user identity when one is required; identifier = [%{public}@], class = %{public}@"
- "Cannot find user [%{public}@] specified for bundle container owner, continuing without bundle container support"
- "Cannot find user [%{public}@] specified for system container owner, continuing without system container support"
- "Client (%{public}@, %d) requests no container with no-container entitlement"
- "Container delete; personaid = %u, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %u], proximate [pid = %d, personaid = %u], euid = %u, uid = %u, message = %{private}s"
- "Could not create app group symlink for [%{public}@], falling back to realpath: %{public}@"
- "Could not generate posix user details for user=%{public}@"
- "Could not read metadata file at [%{public}@]; error = %@"
- "Created new POSIX user: %{public}@"
- "Entered sandbox with HOME: [%{public}s], MACH_LISTENER_NAME: [%{public}s], UID: [%{public}s]"
- "Error de-elevating inactive jetsam priority: %{public}s"
- "Error elevating inactive jetsam priority: %{public}s"
- "Error fetching sandbox extension for persona %{public}@, path %{public}@"
- "Failed creating working directories for %@: %{public}@"
- "Failed creating working directories: %{public}@"
- "Failed to check for existence of %s user home directory [%@]: %{public}@"
- "Failed to connect container cache database: %{public}@"
- "Failed to create deathrow at %@: %{public}@"
- "Failed to enter sandbox: %{public}s"
- "Failed to get dirstats on %{public}s using fallback: (err %d) %s"
- "Failed to get fsNode for [%{public}@] when checking for file system changes: %{public}@"
- "Fetching primordial container for '%{public}@' with identifier '%llu:%{public}@' (%{public}s)"
- "Invalid app group identifier [%{public}@]"
- "Invalid nil parameter passed to %{public}s; %d"
- "Invalid size (%lld) from dirstats on %{public}s using fallback: (err %d) %s"
- "Metadata file at [%{public}@] is corrupt."
- "MobileContainerManager-725.160.3~176"
- "Path [%{public}@] changed: old = %{public}@, new = %{public}@"
- "Persona of unknown type %lu being treated as Unspecific: %{public}@"
- "Personas are supported (static): %s (%s%s%s%s%s%s%s) {pid: %d, uid: %u, apid: %d, auid: %u, asid: %d, session: %{public}s}"
- "Read [%{public}@], length = %{public}lu, options = 0x%{public}lx"
- "Reference count for [%{public}@] is %lu"
- "System container lookup failed, class = %@, identifier = %{public}@, error = (%llu)%{public}@, client = %{public}@"
- "Unable to get user (%u/[%@]/%{public}d); error = %{public}s"
- "User home directory at [%{public}@] does not exist"
- "Using app group symlink for [%{public}@]: %{public}@"
- "Warning: not remapping plugin identifier '%{public}@ to parent identifier [3]"
- "Wrote [%{public}@], length = %{public}lu, options = 0x%{public}lx, mode = 0%{public}o"
- "[%u]%{public}s command=%llu, client=%s(uid: %u, pid: %d), error=%llu (%s)"
- "[%{public}@] is a plugin"
- "[%{public}s] Enabled APFSIOC_DIR_STATS_OP"
- "[%{public}s] Enabled APFSIOC_MAINTAIN_DIR_STATS"
- "[%{public}s] Enabling fast disk sizing failed: %@"
- "[%{public}s] Failed to get dirstats: %{darwin.errno}d"
- "[%{public}s] Failed to set maintain-dir-stats: %{darwin.errno}d"
- "[%{public}s] Fast disk sizing failed: %{darwin.errno}d"
- "[%{public}s] Invalid size (%lld) from dirstats: %{darwin.errno}d"
- "[%{public}s]: descendants: %llu, total size: %llu [ph%llu; cl%llu; pu%llu]"
- "[%{public}s]: descendants: %llu, total size: %llu, using fallback"
- "[u %{public}@:p %{public}@:c %@(%{public}llu):i%llu] Action [%@] failed; error = %@"
- "[u %{public}@:p %{public}@:c %@(%{public}llu):i%llu] Could not fetch fsNode for [%@]: %{public}@"
- "[u %{public}@:p %{public}@:c %@(%{public}llu):i%llu] Could not form action [%@] with args: %@, error = %@"
- "[u %{public}@:p %{public}@:c %@(%{public}llu):i%llu] Could not update schema from (%{public}@) → (%{public}@), actions count = %{public}lu, error = %{public}@"
- "[u %{public}@:p %{public}@:c %@(%{public}llu):i%llu] Could not update schema from (%{public}@) → (%{public}@), no actions available"
- "[u %{public}@:p %{public}@:c %@(%{public}llu):i%llu] Read metadata from [%@]: %@"
- "[u %{public}@:p %{public}@:c %@(%{public}llu):i%llu] Successfully updated schema from (%{public}@) → (%{public}@), actions count = %{public}lu"
- "[u %{public}@:p %{public}@:c %@(%{public}llu):i%llu] Trying to target a version [%@] higher than available [%lu], capping to max"
- "[u %{public}@:p %{public}@:c %@(%{public}llu):i%llu] Wrote metadata to [%@]: %@"
- "container_realpath([%{public}@]) failed: %{public, darwin.errno}d"
- "container_realpath([%{public}@]) → [%{public}@]"
- "containermanagerd (%{public}s) built at %{public}s %{public}s started"
- "listAllPersonaAttributes (%f s): error = %{public}@, attributes = %{public}@"
```
