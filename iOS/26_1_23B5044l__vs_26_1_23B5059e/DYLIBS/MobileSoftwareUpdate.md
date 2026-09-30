## MobileSoftwareUpdate

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate`

```diff

-2422.40.19.502.1
-  __TEXT.__text: 0xcc24
+2422.40.31.0.4
+  __TEXT.__text: 0xcc44
   __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x100
   __TEXT.__const: 0x470
   __TEXT.__cstring: 0x1e16
-  __TEXT.__oslogstring: 0x1d6f
+  __TEXT.__oslogstring: 0x1f0f
   __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 595AC8A4-BF55-3D08-9014-A426C71CA9C9
-  Functions: 204
+  UUID: BA3CD253-2E73-3BEE-9FBD-5C080B2BD8D9
+  Functions: 203
   Symbols:   779
   CStrings:  880
 
Functions:
~ _MSUPreflightUpdate : 808 -> 812
~ _MSUPrepareUpdateWithAsset : 664 -> 668
~ _perform_prepare_command : 908 -> 912
~ _MSUPrepareUpdateWithMAAsset : 712 -> 716
~ _MSUPrepareUpdate : 540 -> 544
~ _MSUApplyUpdate : 1160 -> 1164
~ ___MSUApplyUpdate_block_invoke : 440 -> 448
~ ___perform_prepare_command_block_invoke : 440 -> 448
- _OUTLINED_FUNCTION_0
~ _MSUPerformDownlevel.cold.1 : 124 -> 136
CStrings:
+ "[CLIENT_IPC] Error from softwareupdated: %{public}@"
+ "[CLIENT_IPC] Performed se command with progress: %{public}s | FAILURE"
+ "[CLIENT_IPC] Performed se command with progress: %{public}s | SUCCESS"
+ "[CLIENT_IPC] Performed se command: %{public}s | FAILURE"
+ "[CLIENT_IPC] Performed se command: %{public}s | SUCCESS"
+ "[CLIENT_IPC] Performing se command with progress: %{public}s"
+ "[CLIENT_IPC] Performing se command: %{public}s"
+ "[CLIENT_IPC] Unexpected XPC type from softwareupdated | %{public}s"
+ "[CLIENT_IPC] Unhandled event on service connetion | %{public}s"
+ "[CLIENT_IPC] XPC error creating connection to update brain service | %{public}s"
+ "[CLIENT_IPC] XPC error on service connection: %{public}s"
+ "[CLIENT_IPC] softwareupdated connection event handler | %{public}s"
+ "[SPI] %@ | ...PrepareUpdate | FAILURE | error:%{public}@"
+ "[SPI] %@ | ApplyUpdate | PROGRESS (%@) | state:%{public}@"
+ "[SPI] %@ | ApplyUpdate | PROGRESS (no progress handler - %@) | state:%{public}@"
+ "[SPI] %@ | BEGIN | assetAttributes:%{public}@"
+ "[SPI] %@ | BEGIN | assetprops:%{public}@"
+ "[SPI] %@ | BEGIN | options:%{public}@"
+ "[SPI] %@ | BEGIN | phase:%{public}@, options:%{public}@, fncallback:%@, context:%@"
+ "[SPI] %@ | BEGIN | session:%ld, options:%{public}@, fncallback:%@, context:%@"
+ "[SPI] %@ | BEGIN | source_path:%{public}@, options:%{public}@, fncallback:%@, context:%@"
+ "[SPI] %@ | BEGIN | source_path:%{public}@, prepare_options:%{public}@, update_attributes:%{public}@, fncallback:%@, context:%@"
+ "[SPI] %@ | BEGIN | step:%{public}@"
+ "[SPI] %@ | BEGIN | targetUUID:%{public}@, options:%{public}@"
+ "[SPI] %@ | BEGIN | update_asset:%{public}@, options:%{public}@, fncallback:%@, context:%@"
+ "[SPI] %@ | Current LanguageCode: %{public}@ ExpandedLanguageCode: %{public}@"
+ "[SPI] %@ | DONE | toleratedFailures:%{public}@"
+ "[SPI] %@ | FAILURE | Failed to perform getStashedConnectivityData command, error:%{public}@"
+ "[SPI] %@ | FAILURE | Failed to perform kCommandGetUpdateInformation command, error:%{public}@"
+ "[SPI] %@ | FAILURE | Tolerated failure status:%{public}@"
+ "[SPI] %@ | FAILURE | Unable to determine whether brain is loadable, error:%{public}@"
+ "[SPI] %@ | FAILURE | error:%{public}@"
+ "[SPI] %@ | FAILURE | unable to determine previous restore date, error:%{public}@"
+ "[SPI] %@ | FAILURE | unable to determine previous update date, error:%{public}@"
+ "[SPI] %@ | FAILURE | unable to determine whether first boot after update, error:%{public}@"
+ "[SPI] %@ | PrepareUpdate | PROGRESS (%@) | state:%{public}@"
+ "[SPI] %@ | PrepareUpdate | PROGRESS (no progress handler - %@) | state:%{public}@"
+ "[SPI] %@ | SUCCESS | Installed recovery OS version:%{public}@"
+ "[SPI] %@ | SUCCESS | Tolerated failure status:%{public}@"
+ "[SPI] %@ | SUCCESS | accessibilityDict:%{public}@"
+ "[SPI] %@ | SUCCESS | envDict:%{public}@"
+ "[SPI] %@ | SUCCESS | previous restore date:%{public}@"
+ "[SPI] %@ | SUCCESS | previous update date:%{public}@"
+ "[SPI] %@ | SUCCESS | previous update state:%{public}@"
+ "[SPI] %@ | SUCCESS | update info:%{public}@"
- "[CLIENT_IPC] Error from softwareupdated: %@"
- "[CLIENT_IPC] Performed se command with progress: %s | FAILURE"
- "[CLIENT_IPC] Performed se command with progress: %s | SUCCESS"
- "[CLIENT_IPC] Performed se command: %s | FAILURE"
- "[CLIENT_IPC] Performed se command: %s | SUCCESS"
- "[CLIENT_IPC] Performing se command with progress: %s"
- "[CLIENT_IPC] Performing se command: %s"
- "[CLIENT_IPC] Unexpected XPC type from softwareupdated | %s"
- "[CLIENT_IPC] Unhandled event on service connetion | %s"
- "[CLIENT_IPC] XPC error creating connection to update brain service | %s"
- "[CLIENT_IPC] XPC error on service connection: %s"
- "[CLIENT_IPC] softwareupdated connection event handler | %s"
- "[SPI] %@ | ...PrepareUpdate | FAILURE | error:%@"
- "[SPI] %@ | ApplyUpdate | PROGRESS (%@) | state:%@"
- "[SPI] %@ | ApplyUpdate | PROGRESS (no progress handler - %@) | state:%@"
- "[SPI] %@ | BEGIN | assetAttributes:%@"
- "[SPI] %@ | BEGIN | assetprops:%@"
- "[SPI] %@ | BEGIN | options:%@"
- "[SPI] %@ | BEGIN | phase:%@, options:%@, fncallback:%@, context:%@"
- "[SPI] %@ | BEGIN | session:%ld, options:%@, fncallback:%@, context:%@"
- "[SPI] %@ | BEGIN | source_path:%@, options:%@, fncallback:%@, context:%@"
- "[SPI] %@ | BEGIN | source_path:%@, prepare_options:%@, update_attributes:%@, fncallback:%@, context:%@"
- "[SPI] %@ | BEGIN | step:%@"
- "[SPI] %@ | BEGIN | targetUUID:%@, options:%@"
- "[SPI] %@ | BEGIN | update_asset:%@, options:%@, fncallback:%@, context:%@"
- "[SPI] %@ | Current LanguageCode: %@ ExpandedLanguageCode: %@"
- "[SPI] %@ | DONE | toleratedFailures:%@"
- "[SPI] %@ | FAILURE | Failed to perform getStashedConnectivityData command, error:%@"
- "[SPI] %@ | FAILURE | Failed to perform kCommandGetUpdateInformation command, error:%@"
- "[SPI] %@ | FAILURE | Tolerated failure status:%@"
- "[SPI] %@ | FAILURE | Unable to determine whether brain is loadable, error:%@"
- "[SPI] %@ | FAILURE | error:%@"
- "[SPI] %@ | FAILURE | unable to determine previous restore date, error:%@"
- "[SPI] %@ | FAILURE | unable to determine previous update date, error:%@"
- "[SPI] %@ | FAILURE | unable to determine whether first boot after update, error:%@"
- "[SPI] %@ | PrepareUpdate | PROGRESS (%@) | state:%@"
- "[SPI] %@ | PrepareUpdate | PROGRESS (no progress handler - %@) | state:%@"
- "[SPI] %@ | SUCCESS | Installed recovery OS version:%@"
- "[SPI] %@ | SUCCESS | Tolerated failure status:%@"
- "[SPI] %@ | SUCCESS | accessibilityDict:%@"
- "[SPI] %@ | SUCCESS | envDict:%@"
- "[SPI] %@ | SUCCESS | previous restore date:%@"
- "[SPI] %@ | SUCCESS | previous update date:%@"
- "[SPI] %@ | SUCCESS | previous update state:%@"
- "[SPI] %@ | SUCCESS | update info:%@"

```
