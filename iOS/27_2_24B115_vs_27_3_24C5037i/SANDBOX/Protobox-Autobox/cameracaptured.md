## cameracaptured

> Group: ⬆️ Updated

```diff

 		CISP_CMD_CH_AE_BIAS_EXPOSURE_SET
 		CISP_CMD_CH_AE_FRAME_RATE_MAX_GET
 		CISP_CMD_CH_AE_FRAME_RATE_MAX_SET
+		CISP_CMD_CH_AE_FRAME_RATE_MIN_GET
 		CISP_CMD_CH_AE_FRAME_RATE_MIN_SET
 		CISP_CMD_CH_AE_GAIN_CAP_GET
 		CISP_CMD_CH_AE_GAIN_CAP_SET

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.appleh13camerad"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
+		(require-not (global-name "com.apple.appledepthd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.ReportMemoryException"))

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
