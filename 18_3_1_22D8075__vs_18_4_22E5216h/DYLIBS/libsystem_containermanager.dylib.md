## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-689.0.0.0.0
-  __TEXT.__text: 0x25bb0
-  __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__const: 0x1fc
-  __TEXT.__cstring: 0x3544
-  __TEXT.__oslogstring: 0x373a
-  __TEXT.__unwind_info: 0x5a8
+689.100.5.0.0
+  __TEXT.__text: 0x27484
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__const: 0x220
+  __TEXT.__cstring: 0x3613
+  __TEXT.__oslogstring: 0x3b17
+  __TEXT.__unwind_info: 0x5d0
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x1998
-  __AUTH_CONST.__auth_got: 0x5d8
+  __DATA_CONST.__const: 0x1a48
+  __AUTH_CONST.__auth_got: 0x5b0
   __AUTH_CONST.__const: 0x1e0
-  __AUTH.__data: 0x2d0
-  __DATA.__data: 0x20
-  __DATA.__bss: 0x320
-  __DATA_DIRTY.__data: 0x4
+  __AUTH.__data: 0x328
+  __DATA.__data: 0x30
+  __DATA.__bss: 0x390
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x198
   - /usr/lib/system/libcopyfile.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 504
-  Symbols:   784
-  CStrings:  764
+  Functions: 514
+  Symbols:   805
+  CStrings:  786
 
Symbols:
+ _CMCONTAINERSEAM_DEFAULT
+ _CMPWDSEAM_DEFAULT
+ _container_info_delete
+ _container_info_modify
+ _container_info_put
+ _container_pwd_get_cached_current_user_home_path
+ _container_pwd_get_mobile_user_uid
+ _container_seam_container_reset
+ _container_seam_container_set_common
+ _container_seam_pwd_reset
+ _container_seam_pwd_set_common
+ _gCMContainerSeam
+ _gCMPWDSeam
+ _getgid
+ _xpc_dictionary_apply
CStrings:
+ "%s: SPI MISUSE: container parameter is required"
+ "%s: SPI MISUSE: info_dict parameter is expected to be a dictionary"
+ "%s: SPI MISUSE: info_dict parameter is required"
+ "%s: SPI MISUSE: keys_array parameter is expected to be an array of strings"
+ "%s: SPI MISUSE: keys_array parameter is required"
+ "/private/var/containers"
+ "<multiple>"
+ "@(#)VERSION:Container Manager: Feb 21 2025 12:03:58; MobileContainerManager_system-689.100.5~70/arm64e"
+ "B32@?0*8Q16^^{container_error_extended_s}24"
+ "B40@?0{container_pwd_s=II**}8^^{container_error_extended_s}32"
+ "Data"
+ "PATH_IS_INCOMPLETE_CONTAINER"
+ "USER_NOT_FOUND"
+ "Unable to get user (%u) home path, container results may not be reliable; error = %{public}s"
+ "Unable to get user home path, container results may not be reliable; error = %{public}s"
+ "Update info; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], euid = %d, uid = %d, class = %llu, identifier = %s, key = [%s](%zd), flags = %llx"
+ "Update info; personaid = %d, type = %{public}s, name = %{public}s, origin [pid = %d, personaid = %d], proximate [pid = %d, personaid = %d], euid = %d, uid = %d, message = %s"
+ "container_info_delete"
+ "container_info_modify"
+ "container_info_put"
+ "getpwnam_r(%s): user not found"
+ "getpwuid_r(%u) returned %{public, darwin.errno}d"
+ "getpwuid_r(%u): user not found"
+ "kpersona_getpath(%u) returned %{public, darwin.errno}d"
- "@(#)VERSION:Container Manager: Dec 14 2024 01:20:26; MobileContainerManager_system-689~1630/arm64e"
- "B32@?0*8Q16^Q24"
- "B40@?0{container_pwd_s=II**}8^Q32"
- "getpwuid_r(%d) returned %{public, darwin.errno}d"
- "kpersona_getpath(%d) returned %{public, darwin.errno}d"

```
