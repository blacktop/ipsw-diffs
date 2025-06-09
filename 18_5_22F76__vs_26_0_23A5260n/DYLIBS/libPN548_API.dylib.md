## libPN548_API.dylib

> `/usr/lib/libPN548_API.dylib`

```diff

-355.4.0.0.0
-  __TEXT.__text: 0x40dac
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__const: 0x700
-  __TEXT.__cstring: 0xa64f
-  __TEXT.__oslogstring: 0x73b5
-  __TEXT.__unwind_info: 0x550
+360.33.0.0.0
+  __TEXT.__text: 0x42758
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__const: 0x664
+  __TEXT.__cstring: 0xa3b9
+  __TEXT.__oslogstring: 0x7410
+  __TEXT.__unwind_info: 0x570
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x1438
-  __AUTH_CONST.__auth_got: 0x678
+  __DATA_CONST.__const: 0x1400
+  __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__const: 0x2d0
   __AUTH_CONST.__cfstring: 0x6c0
   __DATA.__data: 0x18

   - /usr/lib/libNFC_HAL.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  UUID: 02BDD36C-693F-3908-8098-95EEC9E48B95
-  Functions: 395
-  Symbols:   334
-  CStrings:  1813
+  UUID: 82EE8FAC-C453-3515-B990-058ED4AF809A
+  Functions: 406
+  Symbols:   341
+  CStrings:  1824
 
Symbols:
+ _NFDataRetain
+ _NFDriverRFSettingsPushSetting
+ _NFDriverRFSettingsReadSetting
+ _NFDriverSendMFGCommand
+ _NFDriverSetFelicaSystemCode
+ _NFDriverTriggerCoreDump
+ _phLibNfc_Mgt_RawCtrlMsgTransceive
+ _phLibNfc_Mgt_TriggerNfccAssertion
+ _phTmlNfc_ParseSpmiDrvErrorStatus
+ _phTmlNfc_RegisterSpmiErrorCallback
- _IOServiceMatching
- _NFDriverEnableReaderModeDynamicBBAControl
- _NFDriverRFSettingsPushSignedSetting
CStrings:
+ "%s:%i ---- Core Dump ----"
+ "%s:%i ---- SPMI ----"
+ "%s:%i ERROR: no value !"
+ "%s:%i Enabling reader mode dynamic BBA control"
+ "%s:%i Error : Allocation failure"
+ "%s:%i Error : unable to write to transition registers"
+ "%s:%i Failed to read registers from NFCC : 0x%4llx"
+ "%s:%i Failed to trigger core dump"
+ "%s:%i Got null callback context"
+ "%s:%i Invalid opcode 0x%x"
+ "%s:%i LPEM flash writes disabled! Headless mode will not be updated on the device."
+ "%s:%i MFW Notification received"
+ "%s:%i No data received."
+ "%s:%i Received Spmi Error Register Info notification"
+ "%s:%i Received Spmi Error Register Info notification: 0x%02x, 0x%02x, 0x%02x , 0x%02x, 0x%02x ,0x%02x"
+ "%s:%i Received empty SPMI Debug Data RAM from NFCC"
+ "%s:%i Received empty core dump debug info from NFCC"
+ "%s:%i Running build from (B&I) Stockholm_Base-360.33"
+ "%s:%i Sending 2F 0x%x to FW"
+ "%s:%i WARNING : Disabling SE reader mode Power save. Temperature will rise much faster !"
+ "%s:%i failed to crash: 0x%04llX"
+ "%s:%i phLibNfc_Mgt_RawCtrlMsgTransceive failed 0x%04llx"
+ "%{public}s:%i ---- Core Dump ----"
+ "%{public}s:%i ---- SPMI ----"
+ "%{public}s:%i ERROR: no value !"
+ "%{public}s:%i Enabling reader mode dynamic BBA control"
+ "%{public}s:%i Error : Allocation failure"
+ "%{public}s:%i Error : unable to write to transition registers"
+ "%{public}s:%i Failed to read registers from NFCC : 0x%4llx"
+ "%{public}s:%i Failed to trigger core dump"
+ "%{public}s:%i Got null callback context"
+ "%{public}s:%i Invalid opcode 0x%x"
+ "%{public}s:%i LPEM flash writes disabled! Headless mode will not be updated on the device."
+ "%{public}s:%i MFW Notification received"
+ "%{public}s:%i No data received."
+ "%{public}s:%i Received Spmi Error Register Info notification"
+ "%{public}s:%i Received Spmi Error Register Info notification: 0x%02x, 0x%02x, 0x%02x , 0x%02x, 0x%02x ,0x%02x"
+ "%{public}s:%i Received empty SPMI Debug Data RAM from NFCC"
+ "%{public}s:%i Received empty core dump debug info from NFCC"
+ "%{public}s:%i Running build from (B&I) Stockholm_Base-360.33"
+ "%{public}s:%i Sending 2F 0x%x to FW"
+ "%{public}s:%i WARNING : Disabling SE reader mode Power save. Temperature will rise much faster !"
+ "%{public}s:%i failed to crash: 0x%04llX"
+ "%{public}s:%i phLibNfc_Mgt_RawCtrlMsgTransceive failed 0x%04llx"
+ "Core Dump"
+ "Error data :"
+ "MFG command reply: "
+ "Measurement Error"
+ "NFDriverRFSettingsPushSetting"
+ "NFDriverRFSettingsReadSetting"
+ "NFDriverSendMFGCommand"
+ "NFDriverSendMFGCommand_block_invoke"
+ "NFDriverSetFelicaSystemCode"
+ "NFDriverTriggerCoreDump"
+ "Reading registers"
+ "SPMI Flash info"
+ "SPMI RAM info"
+ "_Callback_NFDriverSendMFGCommand"
+ "_NFDriverConfigureReaderModeDynamicBBA"
+ "_NFDriverConfigureReaderModeRFForMercurySigned"
+ "_NFDriverQuerySPMIErrors_block_invoke"
+ "_NFDriverRFSettingsWriteSignedCalData"
+ "_NFDriverRemoteDevTransceive"
+ "_NFSpmiErrorCallback"
+ "_getKeySize"
+ "false"
+ "received SPMI debug info from NFCC"
+ "received core dump debug info from NFCC"
- "%s:%i Cal not supported with this HW."
- "%s:%i Failed to get syscfg data"
- "%s:%i Failed to get syscfg service"
- "%s:%i Failed to read RF cal data from syscfg, and no data in Applet, bailing with success."
- "%s:%i Failed to setup CLK timeout config"
- "%s:%i Invalid TLV format for calData = %s"
- "%s:%i Invalid syscfg key : NFCl, expecting jumbo"
- "%s:%i Invalid syscfg length"
- "%s:%i Invalid syscfg magic"
- "%s:%i Invalid syscfg type"
- "%s:%i Invalid syscfg version : 0x%x, expecting 0x%x or 0x%x"
- "%s:%i NFDriverConfigureReaderModeRFForCathaySigned: Unable to apply Default RF settings"
- "%s:%i NFDriverConfigureReaderModeRFForCathaySigned: Unable to apply Dynamic RF settings. Trying to reset back to defaults"
- "%s:%i Restoring RF using FDR Cal data"
- "%s:%i Running build from (B&I) Stockholm_Base-355.4"
- "%s:%i Unintialized NFCl entry!"
- "%s:%i Version 8 lacks signature and isn't supported anymore, returning NULL"
- "%s:%i calData = %s"
- "%s:%i overriding clock setting to 26MHz "
- "%{public}s:%i Cal not supported with this HW."
- "%{public}s:%i Failed to get syscfg data"
- "%{public}s:%i Failed to get syscfg service"
- "%{public}s:%i Failed to read RF cal data from syscfg, and no data in Applet, bailing with success."
- "%{public}s:%i Failed to setup CLK timeout config"
- "%{public}s:%i Invalid TLV format for calData = %s"
- "%{public}s:%i Invalid syscfg key : NFCl, expecting jumbo"
- "%{public}s:%i Invalid syscfg length"
- "%{public}s:%i Invalid syscfg magic"
- "%{public}s:%i Invalid syscfg type"
- "%{public}s:%i Invalid syscfg version : 0x%x, expecting 0x%x or 0x%x"
- "%{public}s:%i NFDriverConfigureReaderModeRFForCathaySigned: Unable to apply Default RF settings"
- "%{public}s:%i NFDriverConfigureReaderModeRFForCathaySigned: Unable to apply Dynamic RF settings. Trying to reset back to defaults"
- "%{public}s:%i Restoring RF using FDR Cal data"
- "%{public}s:%i Running build from (B&I) Stockholm_Base-355.4"
- "%{public}s:%i Unintialized NFCl entry!"
- "%{public}s:%i Version 8 lacks signature and isn't supported anymore, returning NULL"
- "%{public}s:%i calData = %s"
- "%{public}s:%i overriding clock setting to 26MHz "
- "A0030103"
- "A00E28F0003E11E4E4E40000000000A78EFFFF272A2A2A0A00000001001000040000001740FF0713070507A0AF09119CA02A119C002A00A0980462220880A00D03610982A06A080000000000005000A0940A07F40100003100000000A0682A064060031900004000930400801B801B00014001A000000103FA0000004C0014007D00057F0000010003"
- "A00E28F0003E11E4E4E40000000000A78EFFFF2A2A2A2A0A00000001001000040000001740FF0713070507A0AF09119CA02A119C002A00A0980478170C80A00D03610982A06A080000000000008C00A0940A07F40100003100000000A0682A064060031900004000930400801B801B40014001C000C00003FA0000004C0014007D00057F0000010003"
- "A00E28F0003E11E4E4E40000000000A78EFFFF2A2A2A2A0A00000001001000040000001740FF0713070507A0AF09119CA02A119C002A00A09804B5091780A00D03610982A06A080000000000008C00A0940A07F40100003100000000A0682A064060031900004000930400801B801B00016001A000200103FA0000004C0014007D00057F0000010003"
- "AppleDiagnosticDataAccess"
- "AppleDiagnosticDataSysCfg"
- "INVALID HEX STRING"
- "Invalid syscfg "
- "NFDriverConfigureReaderModeRFForCathaySigned"
- "NFDriverConfigureReaderModeRFForMercurySigned"
- "NFDriverEnableReaderModeDynamicBBAControl"
- "NFDriverQuerySPMIErrors_block_invoke"
- "NFDriverRFSettingsPushSignedSetting"
- "NFDriverRemoteDevTransceive"
- "_NFDriverRFSettingsHWSupportsSignedFDRCal"
- "_NFDriverRFSettingsHWSupportsSignedSyscfgCal"
- "_NFDriverRFSettingsReadCalDataFromSyscfg"
- "_NFDriverRFSettingsWriteSignedData"
- "_NFDriverSetupRFClockTimeout"

```
