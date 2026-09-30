## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

```diff

-689.0.0.0.0
-  __TEXT.__text: 0x25bfc
-  __TEXT.__auth_stubs: 0xb30
-  __TEXT.__const: 0x200
-  __TEXT.__cstring: 0x339f
-  __TEXT.__oslogstring: 0x3657
-  __TEXT.__unwind_info: 0x5e0
+689.100.6.0.0
+  __TEXT.__text: 0x27548
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__const: 0x230
+  __TEXT.__cstring: 0x3471
+  __TEXT.__oslogstring: 0x3a34
+  __TEXT.__unwind_info: 0x5e8
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0xb58
-  __AUTH_CONST.__auth_got: 0x598
-  __AUTH_CONST.__const: 0x1340
-  __AUTH.__data: 0x2d0
-  __DATA.__data: 0x1c
-  __DATA.__bss: 0x4c0
+  __DATA_CONST.__const: 0xb68
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__const: 0x1400
+  __AUTH.__data: 0x328
+  __DATA.__data: 0x30
+  __DATA.__bss: 0x530
   - /usr/lib/system/libcopyfile.dylib
   - /usr/lib/system/libdispatch.dylib
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: A72C2FD5-969A-342F-B8A4-4216D7C7957E
-  Functions: 519
-  Symbols:   971
-  CStrings:  750
+  UUID: C9C367BC-7754-3445-BB2C-797F4E7BE132
+  Functions: 529
+  Symbols:   1001
+  CStrings:  772
 
Symbols:
+ _CMCONTAINERSEAM_DEFAULT
+ _CMPWDSEAM_DEFAULT
+ ____container_info_execute_block_invoke
+ ___container_info_delete_block_invoke
+ ___container_info_modify_block_invoke
+ ___container_info_put_block_invoke
+ __block_descriptor_tmp.1.274
+ __block_descriptor_tmp.1.345
+ __block_descriptor_tmp.1.415
+ __block_descriptor_tmp.11.409
+ __block_descriptor_tmp.12.636
+ __block_descriptor_tmp.12.713
+ __block_descriptor_tmp.13.927
+ __block_descriptor_tmp.15.714
+ __block_descriptor_tmp.156
+ __block_descriptor_tmp.16.929
+ __block_descriptor_tmp.160
+ __block_descriptor_tmp.187
+ __block_descriptor_tmp.2.347
+ __block_descriptor_tmp.21.827
+ __block_descriptor_tmp.270
+ __block_descriptor_tmp.28.930
+ __block_descriptor_tmp.3.350
+ __block_descriptor_tmp.3.404
+ __block_descriptor_tmp.3.632
+ __block_descriptor_tmp.3.666
+ __block_descriptor_tmp.3.710
+ __block_descriptor_tmp.3.839
+ __block_descriptor_tmp.3.881
+ __block_descriptor_tmp.31.934
+ __block_descriptor_tmp.33.558
+ __block_descriptor_tmp.334
+ __block_descriptor_tmp.340
+ __block_descriptor_tmp.38.936
+ __block_descriptor_tmp.394
+ __block_descriptor_tmp.4.352
+ __block_descriptor_tmp.4.671
+ __block_descriptor_tmp.4.912
+ __block_descriptor_tmp.478
+ __block_descriptor_tmp.487
+ __block_descriptor_tmp.495
+ __block_descriptor_tmp.564
+ __block_descriptor_tmp.598
+ __block_descriptor_tmp.6.634
+ __block_descriptor_tmp.6.843
+ __block_descriptor_tmp.6.890
+ __block_descriptor_tmp.658
+ __block_descriptor_tmp.68
+ __block_descriptor_tmp.7.377
+ __block_descriptor_tmp.7.418
+ __block_descriptor_tmp.7.674
+ __block_descriptor_tmp.7.712
+ __block_descriptor_tmp.7.908
+ __block_descriptor_tmp.706
+ __block_descriptor_tmp.792
+ __block_descriptor_tmp.8.381
+ __block_descriptor_tmp.813
+ __block_descriptor_tmp.848
+ __block_descriptor_tmp.874
+ __block_descriptor_tmp.9.635
+ __block_descriptor_tmp.904
+ __block_literal_global.323
+ __block_literal_global.402
+ __block_literal_global.476
+ __block_literal_global.485
+ __block_literal_global.493
+ __block_literal_global.562
+ __block_literal_global.701
+ __block_literal_global.983
+ __container_info_execute
+ __container_user_prefix_managed_by_containermanager_transient
+ _container_info_delete
+ _container_info_modify
+ _container_info_put
+ _container_pwd_get_cached_current_user_home_path
+ _container_pwd_get_mobile_user_uid
+ _container_seam_container_reset
+ _container_seam_container_set_common
+ _container_seam_pwd_reset
+ _container_seam_pwd_set_common
+ _gCMContainerCustomSeamStore
+ _gCMContainerSeam
+ _gCMPWDCustomSeamStore
+ _gCMPWDSeam
+ _getgid
+ _xpc_dictionary_apply
+ container_pwd_get_cached_current_user_home_path.error
+ container_pwd_get_cached_current_user_home_path.lock
+ container_pwd_get_cached_current_user_home_path.user_home_realpath
- __block_descriptor_tmp.1.269
- __block_descriptor_tmp.1.340
- __block_descriptor_tmp.1.410
- __block_descriptor_tmp.11.404
- __block_descriptor_tmp.12.630
- __block_descriptor_tmp.12.707
- __block_descriptor_tmp.13.878
- __block_descriptor_tmp.15.708
- __block_descriptor_tmp.154
- __block_descriptor_tmp.158.933
- __block_descriptor_tmp.16.879
- __block_descriptor_tmp.185.939
- __block_descriptor_tmp.2.342
- __block_descriptor_tmp.265
- __block_descriptor_tmp.28.880
- __block_descriptor_tmp.3.345
- __block_descriptor_tmp.3.399
- __block_descriptor_tmp.3.626
- __block_descriptor_tmp.3.660
- __block_descriptor_tmp.3.704
- __block_descriptor_tmp.3.840
- __block_descriptor_tmp.31.884
- __block_descriptor_tmp.329
- __block_descriptor_tmp.33.552
- __block_descriptor_tmp.335
- __block_descriptor_tmp.38.886
- __block_descriptor_tmp.389
- __block_descriptor_tmp.4.347
- __block_descriptor_tmp.4.665
- __block_descriptor_tmp.4.863
- __block_descriptor_tmp.472
- __block_descriptor_tmp.481
- __block_descriptor_tmp.489
- __block_descriptor_tmp.5
- __block_descriptor_tmp.558
- __block_descriptor_tmp.592
- __block_descriptor_tmp.6.628
- __block_descriptor_tmp.652
- __block_descriptor_tmp.67
- __block_descriptor_tmp.7.372
- __block_descriptor_tmp.7.413
- __block_descriptor_tmp.7.668
- __block_descriptor_tmp.7.706
- __block_descriptor_tmp.7.859
- __block_descriptor_tmp.700
- __block_descriptor_tmp.786
- __block_descriptor_tmp.8.376
- __block_descriptor_tmp.808
- __block_descriptor_tmp.834
- __block_descriptor_tmp.855
- __block_descriptor_tmp.9.629
- __block_literal_global.318
- __block_literal_global.397
- __block_literal_global.470
- __block_literal_global.479
- __block_literal_global.487
- __block_literal_global.556
- __block_literal_global.695
- __block_literal_global.937
CStrings:
+ "%s: SPI MISUSE: container parameter is required"
+ "%s: SPI MISUSE: info_dict parameter is expected to be a dictionary"
+ "%s: SPI MISUSE: info_dict parameter is required"
+ "%s: SPI MISUSE: keys_array parameter is expected to be an array of strings"
+ "%s: SPI MISUSE: keys_array parameter is required"
+ "/private/var/containers"
+ "<multiple>"
+ "@(#)VERSION:Container Manager: Mar  7 2025 19:20:32; MobileContainerManager_system-689.100.6~103/arm64e"
+ "B32@?0*8Q16^^{container_error_extended_s}24"
+ "B40@?0{container_pwd_s=II**}8^^{container_error_extended_s}32"
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
+ "mobile"
- "@(#)VERSION:Container Manager: Dec 13 2024 18:22:00; MobileContainerManager_system-689~1632/arm64e"
- "B32@?0*8Q16^Q24"
- "B40@?0{container_pwd_s=II**}8^Q32"
- "getpwuid_r(%d) returned %{public, darwin.errno}d"
- "kpersona_getpath(%d) returned %{public, darwin.errno}d"

```
