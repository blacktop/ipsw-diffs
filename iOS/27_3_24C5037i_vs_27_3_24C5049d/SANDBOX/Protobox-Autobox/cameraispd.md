## cameraispd

> Group: ⬆️ Updated

```diff

 		CISP_CMD_CH_STATUS_LED_MBRIGHTNESS_SET
 		CISP_CMD_CH_PROJECTOR_SPEC_GET
 		CISP_CMD_CH_PROJECTOR_ALLOW_ON
+		CISP_CMD_UPDATE_DEVICE_IMPACT
 		CISP_CMD_CH_LSC_IDEAL_PERCENTAGE_SET
 		CISP_CMD_CH_LTM_STATE_SET
 		CISP_CMD_CH_CURRENT_DISPLAY_BRIGHTNESS_UPDATE

 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (xpc-service-name "com.apple.CoreRepairCoreXPCService"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
```
