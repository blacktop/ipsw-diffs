## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

-2680.120.12.0.0
-  __TEXT.__os_log: 0x2272
-  __TEXT.__const: 0x1cac21
-  __TEXT.__cstring: 0x72d6
-  __TEXT_EXEC.__text: 0x38ab8
+3033.0.0.0.1
+  __TEXT.__os_log: 0x1d00
+  __TEXT.__const: 0x1e8669
+  __TEXT.__cstring: 0x6f48
+  __TEXT_EXEC.__text: 0x38100
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x220
   __DATA.__bss: 0x152f8
-  __DATA_CONST.__auth_got: 0x878
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x3858
+  __DATA_CONST.__const: 0x3938
   __DATA_CONST.__kalloc_type: 0xbc0
-  __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: 58F3BE22-6099-3D96-B22F-DBA3D67DDE65
-  Functions: 652
+  __DATA_CONST.__kalloc_var: 0x550
+  __DATA_CONST.__auth_got: 0x848
+  __DATA_CONST.__got: 0xb0
+  UUID: 1FD57B39-AC3F-386F-9BD5-8A8AC8968F54
+  Functions: 653
   Symbols:   0
-  CStrings:  1344
+  CStrings:  1306
 
CStrings:
+ " flavor:"
+ " isp-command:-1 CISP_CMD_*:%u"
+ " parser-name:%s"
+ " path:%s xattr:%s"
+ "%s[%d] revoked access to %s"
+ "21111121111111111111222222222133331333111111222222222222222"
+ "<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\"><dict><key>Protobox</key><dict><key>Exclude from data collection</key><array><string>/AppleInternal/</string><string>/Applications/</string><string>/Developer/</string><string>/System/Developer/</string><string>/System/Library/Filesystems/</string><string>/bin/</string><string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_RecoveryOSUpdateBrain/</string><string>/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/com_apple_MobileAsset_MobileSoftwareUpdate_UpdateBrain/</string><string>/private/var/containers/Bundle/</string><string>/private/var/db/com.apple.xpc.roleaccountd.staging/</string><string>/private/var/mobile/</string><string>/private/var/personalized_*</string><string>/private/var/root/</string><string>/private/var/run/com.apple.security.cryptexd/</string><string>/private/var/tmp/</string><string>/usr/appleinternal/</string><string>/usr/bin/</string><string>/usr/local/</string></array></dict></dict></plist>"
+ "asr-parser-enter"
+ "coalition-info"
+ "com.apple.private.security.revoke"
+ "fs-info"
+ "i24@?0r^{profile=^vQ^{profile_state}^{profile}QQQQAISSSCCCCBBBB^{variable_info}^^{__matchExpr}****QQQ**^{collection}}8I16S20"
+ "io_service_get_wait_info"
+ "isp-command-send"
+ "mach_memory_entry_region_info"
+ "not supported for devfs fd paths"
+ "qtn-exec"
+ "qtn-exec-no-quarantine"
+ "sandbox_decommit_capacity"
+ "site.typeof(**&devset->list)"
+ "site.typeof(*devset->list)"
+ "virtual_env_create"
+ "virtual_env_get_current"
+ "virtual_env_get_info"
- "\nelapsed time: %llu ticks\n"
- "%s expects container but none provided by containermanagerd"
- "%s: no ustate"
- "%s: vm_allocate failed"
- "%s: vm_map_copyin failed kr = %d"
- "%s: vm_map_unwire failed kr = %d"
- "%s: vm_map_wire failed kr = %d"
- "21111121111111111111222222222133331333111111222222222222"
- "<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\"><dict><key>Protobox</key><dict><key>Exclude from data collection</key><array><string>/AppleInternal/</string><string>/Applications/</string><string>/Developer/</string><string>/System/Cryptexes/</string><string>/System/Developer/</string><string>/System/Library/Filesystems/</string><string>/bin/</string><string>/private/preboot/Cryptexes/</string><string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_RecoveryOSUpdateBrain/</string><string>/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/com_apple_MobileAsset_MobileSoftwareUpdate_UpdateBrain/</string><string>/private/var/containers/Bundle/</string><string>/private/var/db/com.apple.xpc.roleaccountd.staging/</string><string>/private/var/mobile/</string><string>/private/var/personalized_*</string><string>/private/var/root/</string><string>/private/var/run/com.apple.security.cryptexd/</string><string>/private/var/tmp/</string><string>/usr/appleinternal/</string><string>/usr/bin/</string><string>/usr/local/</string></array></dict></dict></plist>"
- "App Group Container (%s) path: %s\n"
- "CM_KERN_REPLY_APP_GROUP_ID"
- "CM_KERN_REPLY_DATA_CONTAINER_PATH: no ustate"
- "CM_KERN_REQUEST_APPLICATION_ID"
- "CM_KERN_REQUEST_APP_GROUP_ID"
- "CM_KERN_REQUEST_CODE_SIGNATURE_ID"
- "CM_KERN_REQUEST_CONTAINER_ID"
- "CM_KERN_REQUEST_CONTAINER_TYPE"
- "CM_KERN_REQUEST_PERSONA_ID"
- "CM_KERN_REQUEST_SYSTEM_CONTAINER_ID"
- "CM_KERN_REQUEST_SYSTEM_GROUP_CONTAINER_ID"
- "CM_KERN_REQUEST_UID"
- "Data container path: %s\n"
- "Failed pack %s: %s -- %d"
- "Failed to create packbuff."
- "Failed to get the HOST_CONTAINERD_PORT port: %d"
- "Failed to pack %s: %s -- %d"
- "Failed to pack %s: %u -- %d"
- "Home directory path: %s\n"
- "Status: %u\n"
- "System Group Container (%s) path: %s\n"
- "System container path: %s\n"
- "TEMP_DIR path: %s\n"
- "_sfree_obj_track_decommit"
- "attempting to use a container without a code signing identity."
- "container list get: %s, %s, %llu"
- "container_manager status: %u"
- "container_manager_get_process_containers() failed: system=%d subsystem=%d, code=%d"
- "failed to upcall to containermanagerd for a platform app"
- "failed: [%u] = sb_packbuff_unpack_key_with_string_value(): %d"
- "failed: [%u] = sb_packbuff_unpack_key_with_string_value(): %d\n"
- "failed: [%u] = sb_packbuff_unpack_key_with_string_value()=%d"
- "failed: to unpack CM_KERN_REPLY_DATA_CONTAINER_PATH %u, error: %d"
- "failed: to unpack CM_KERN_REPLY_DATA_CONTAINER_PATH %u, error: %d\n"
- "failed: to unpack CM_KERN_REPLY_HOME_DIRECTORY_PATH %u, error: %d"
- "failed: to unpack CM_KERN_REPLY_HOME_DIRECTORY_PATH %u, error: %d\n"
- "failed: to unpack CM_KERN_REPLY_STATUS error: %d"
- "failed: to unpack CM_KERN_REPLY_STATUS error: %d\n"
- "failed: to unpack CM_KERN_REPLY_SYSTEM_CONTAINER_PATH %u, error: %d"
- "failed: to unpack CM_KERN_REPLY_SYSTEM_CONTAINER_PATH %u, error: %d\n"
- "failed: to unpack CM_KERN_REPLY_TEMP_CONTAINER_PATH %u, error: %d"
- "failed: to unpack CM_KERN_REPLY_TEMP_CONTAINER_PATH %u, error: %d\n"
- "i24@?0r^{profile=^vQ^{profile_state}^{profile}QQQQAISSSCCCCBBBB^{variable_info}^^{__matchExpr}****QQQ**^{collection}}8i16S20"
- "invalid value type %u for CM_KERN_REPLY_APP_GROUP_CONTAINER_PATH %s"
- "invalid value type for CM_KERN_REPLY_APP_GROUP_CONTAINER_PATH %s: value: %u\n"
- "invalid value type for CM_KERN_REPLY_SYSTEM_GROUP_CONTAINER_PATH %s: value: %u"
- "invalid value type for CM_KERN_REPLY_SYSTEM_GROUP_CONTAINER_PATH %s: value: %u\n"
- "missing user state for uid %u"
- "sb_mach_vmcopyout() returned: %d\n"
- "sb_packbuff_alloc_vm_buffer"
- "sb_packbuff_new() returned NULL\n"
- "unknown type (%u) in reply message"
- "unknown type (%u) in reply message\n"

```
