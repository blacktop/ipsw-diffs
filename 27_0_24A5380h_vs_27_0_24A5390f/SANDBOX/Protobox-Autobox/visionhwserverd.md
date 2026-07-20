## visionhwserverd

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AppleH13CamIn")
 		(iokit-registry-entry-class "AppleH16CamIn")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny isp-command-send)
-(allow isp-command-send
+(deny ipc-sysv-shm)
+(allow ipc-sysv-shm
 	(isp-command
 		CISP_CMD_CONFIG_GET
 		CISP_CMD_OSCAR2_CLOCK_SET
-		CISP_CMD_CH_CAMERA_CONFIG_GET
-		CISP_CMD_CH_INFO_GET
-		CISP_CMD_CH_GENERAL_PROCESS_START
+		CISP_CMD_CH_CAMERA_CONFIG_SELECT
+		CISP_CMD_CH_BUFFER_RECYCLE_MODE_SET
 		CISP_CMD_CH_GENERAL_PROCESS_STOP
-		CISP_CMD_CH_SENSOR_FOCUS_PIXEL_MAPS_GET
-		CISP_CMD_CH_PROJECTOR_ALLOW_ON
-		CISP_CMD_UPDATE_DEVICE_IMPACT
-		CISP_CMD_CH_MS_SWITCHOVER_ZOOM_FACTOR_GET
-		CISP_CMD_CH_FACE_DETECTION_CONFIG_GET
-		CISP_CMD_CH_TOF_CONTROL_MODE_SET
-		CISP_CMD_CH_PDE_CALDATA_GET)
+		CISP_CMD_CH_QUDRA_FULL_RES_CAPTURE_ENABLE
+		CISP_CMD_CH_SENSOR_PERMODULE_LUMA_SHADING_GET
+		CISP_CMD_CH_PROJECTOR_WDT_SET
+		CISP_CMD_CH_MAGNETIC_INTERFERENCE_SET
+		CISP_CMD_CH_SECONDARY_SCALER_SOURCE_SET
+		CISP_CMD_CH_FACE_DETECTION_DISABLE
+		CISP_CMD_MULTICAM_SESSION_CREATE
+		CISP_CMD_CH_PDE_VERSION_GET)
 )
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny mach-issue-extension)
+(deny mach-host-special-port-set)
 
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 
 (deny syscall-unix)
```
