## com.apple.driver.AppleH16CameraInterface

> `com.apple.driver.AppleH16CameraInterface`

```diff

-4.109.0.0.0
-  __TEXT.__const: 0xa1f8
-  __TEXT.__cstring: 0x18647
-  __TEXT.__os_log: 0x145f2
-  __TEXT_EXEC.__text: 0x9dfa0
+4.207.2.0.0
+  __TEXT.__const: 0xa238
+  __TEXT.__cstring: 0x188c0
+  __TEXT.__os_log: 0x14a00
+  __TEXT_EXEC.__text: 0xa0c0c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a8
-  __DATA.__common: 0x4c8
+  __DATA.__common: 0x4f0
   __DATA.__bss: 0x1f8
   __DATA_CONST.__auth_got: 0x838
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x18560
-  __DATA_CONST.__kalloc_type: 0x11c0
+  __DATA_CONST.__const: 0x18c10
+  __DATA_CONST.__kalloc_type: 0x1200
   __DATA_CONST.__kalloc_var: 0xa50
-  UUID: CB6F3A1A-0203-36A2-A622-DCA0431EF942
-  Functions: 1761
+  UUID: 2B2FE799-C1E9-3F63-8A7C-5CDA48BA293C
+  Functions: 1782
   Symbols:   0
-  CStrings:  3146
+  CStrings:  3173
 
CStrings:
+ "121111121222121211111111111121222112"
+ "AppleDisplayPseudoStandbyFunction"
+ "AppleH16CamIn:%s - %s psuedo-standby, result=0x%08X\n"
+ "AppleH16CamIn:%s - Client %s not found in client lookup, res = 0x%08X\n"
+ "AppleH16CamIn:%s - Could not create client: %s, error = 0x%08x\n"
+ "AppleH16CamIn:%s - Failed to power off ISP, res = 0x%08X\n"
+ "AppleH16CamIn:%s - Failed to power on ISP, res = 0x%08X\n"
+ "AppleH16CamIn:%s - Failed to send CISP_CMD_ALS_SENSOR_POWER_SET command\n"
+ "AppleH16CamIn:%s - Failed to turn off ALS power, res = 0x%08X\n"
+ "AppleH16CamIn:%s - Failed to turn on ALS power, res = 0x%08X\n"
+ "AppleH16CamIn:%s - wired client surface-id:0x%08X, w=%-4u, h=%-4u, fmt=%-3u, poolID=%-4u, dartMapBase=%#llX\n"
+ "AppleH16CamInFrameReceiver:%s - ISP_EnableSensorPower Error: 0x%08X\n"
+ "AppleH16CamInUserClient:%s - Client is appleh16darwincamerad\n"
+ "AppleH16CamInUserClient:%s - Client is dietappleh16camerad\n"
+ "AppleH16PearlCam:%s - Error sending channel diag command - res=0x%08X\n"
+ "AppleH16PearlCam:%s - Error: Did not dispatch message to the correct handler\n"
+ "CamService"
+ "ISP_DisplayPseudoStandby_gated"
+ "ISP_SendALSPowerCommand"
+ "appleh16darwincamerad"
+ "lpdprx_cfg_fuse532"
+ "lpdprx_cfg_fuse549"
+ "lpdprx_cfg_fuse76"
+ "site.AppleDisplayPseudoStandbyFunction"
- "12111112122212121111111111112122222222222222222112"
- "AppleH16CamIn:%s - Failed to reset SBD state on index: 0x%08X\n\n"
- "AppleH16CamIn:%s - wired client surface-id:0x%08X, w=%-4u, h=%-4u, fmt=%-3u, poolID=%-4u, dartMapBase=0x%08X\n"
- "reset"

```
