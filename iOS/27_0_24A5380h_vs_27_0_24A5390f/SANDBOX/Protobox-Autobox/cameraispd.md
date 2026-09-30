## cameraispd

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
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleCamera")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.daemonv1")
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")

 	)
 )
 
-(deny isp-command-send)
-(allow isp-command-send
+(deny ipc-sysv-shm)
+(allow ipc-sysv-shm
 	(isp-command
 		CISP_CMD_CONFIG_GET
 		CISP_CMD_OSCAR2_CLOCK_SET
 		CISP_CMD_FLICKER_FREQ_SET
-		CISP_CMD_CH_CAMERA_CONFIG_GET
-		CISP_CMD_CH_INFO_GET
-		CISP_CMD_CH_DEVICE_NVM_GET
-		CISP_CMD_CH_PREPARE_START
-		CISP_CMD_CH_SENSOR_NVM_GET
-		CISP_CMD_CH_STATUS_LED_MBRIGHTNESS_SET
-		CISP_CMD_CH_PROJECTOR_SPEC_GET
-		CISP_CMD_CH_PROJECTOR_ALLOW_ON
-		CISP_CMD_CH_LSC_IDEAL_PERCENTAGE_SET
-		CISP_CMD_CH_LTM_STATE_SET
-		CISP_CMD_CH_CURRENT_DISPLAY_BRIGHTNESS_UPDATE
-		CISP_CMD_CH_HI_RES_HITH_THUMBNAIL_MAX_SIZE_GET)
+		CISP_CMD_CH_CAMERA_CONFIG_SELECT
+		CISP_CMD_CH_BUFFER_RECYCLE_MODE_SET
+		CISP_CMD_CH_SYSCFG_KEY_SET
+		CISP_CMD_CH_LOCAL_HUEMAP_BUFFER_ENABLE
+		CISP_CMD_CH_SENSOR_NVM_RELOAD
+		CISP_CMD_CH_STATUS_LED_MBRIGHTNESS_GET
+		CISP_CMD_CH_PROJECTOR_FORCE_OFF
+		CISP_CMD_CH_PROJECTOR_WDT_SET
+		CISP_CMD_CH_DESKVIEW_MODE_SET
+		CISP_CMD_CH_AMBIENT_VIEWING_LEVEL_GET
+		CISP_CMD_CH_HI_RES_HITH_THUMBNAIL_MAX_SIZE_GET
+		CISP_CMD_CH_WSEG_MAP_MAX_SIZE_GET)
 )
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny mach-issue-extension)
+(deny mach-host-special-port-set)
 
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.lsd.mapdb"))

 	)
 )
 
+(deny process-codesigning
+	(require-any
+		(require-not (require-any
+			(literal "/usr/local/bin/espressoc")
+			(literal "/usr/local/bin/zin_ane_dump")
+		))
+		(require-not (system-attribute internal-build))
+	)
+)
+
 (deny process-exec*
 	(require-any
 		(require-not (require-any
```
