## demod

> `/usr/libexec/demod`

```diff

-1254.42.1.0.0
-  __TEXT.__text: 0xc88a0
+1254.60.17.0.0
+  __TEXT.__text: 0xc98dc
   __TEXT.__auth_stubs: 0x1640
-  __TEXT.__objc_stubs: 0x16c40
-  __TEXT.__objc_methlist: 0xa3dc
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0xce75
-  __TEXT.__objc_methname: 0x1ab2c
-  __TEXT.__oslogstring: 0x158a5
-  __TEXT.__objc_classname: 0x14de
-  __TEXT.__objc_methtype: 0x3411
-  __TEXT.__gcc_except_tab: 0x35f8
-  __TEXT.__unwind_info: 0x2918
+  __TEXT.__objc_stubs: 0x16be0
+  __TEXT.__objc_methlist: 0xa44c
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0xcf4f
+  __TEXT.__objc_methname: 0x1acba
+  __TEXT.__oslogstring: 0x1599d
+  __TEXT.__objc_classname: 0x14e0
+  __TEXT.__objc_methtype: 0x353c
+  __TEXT.__gcc_except_tab: 0x35d8
+  __TEXT.__unwind_info: 0x2950
   __DATA_CONST.__auth_got: 0xb30
   __DATA_CONST.__got: 0x5f8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2570
-  __DATA_CONST.__cfstring: 0xbf80
+  __DATA_CONST.__const: 0x2620
+  __DATA_CONST.__cfstring: 0xc0c0
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x438
+  __DATA_CONST.__objc_intobj: 0x480
   __DATA_CONST.__objc_arraydata: 0x780
   __DATA_CONST.__objc_arrayobj: 0x3a8
-  __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x17968
-  __DATA.__objc_selrefs: 0x6460
+  __DATA_CONST.__objc_dictobj: 0xf0
+  __DATA.__objc_const: 0x179c8
+  __DATA.__objc_selrefs: 0x64a8
   __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0xa90
+  __DATA.__objc_classrefs: 0xaa0
   __DATA.__objc_superrefs: 0x3a8
-  __DATA.__objc_ivar: 0x9b4
+  __DATA.__objc_ivar: 0x9ac
   __DATA.__objc_data: 0x3ca0
   __DATA.__data: 0x2328
   __DATA.__bss: 0x4e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C63B9D2-4386-379D-9F5E-DD37BA238B18
-  Functions: 4951
-  Symbols:   736
-  CStrings:  10498
+  UUID: 89A6529D-7D05-348E-9B92-D1CEC063F153
+  Functions: 4964
+  Symbols:   738
+  CStrings:  10530
 
Symbols:
+ _OBJC_CLASS_$_MSDKPeerDemoAXSettings
+ _OBJC_CLASS_$_MSDKPeerDemoIPDStatus
CStrings:
+ "\x17"
+ "/var/MobileAsset"
+ "AXSettingsArchive"
+ "AssetsV2/com_apple_MobileAsset_SystemEnvironmentAsset"
+ "FinalIPD"
+ "IPDResetStage"
+ "IPDStatusArchive"
+ "MSDDemoPeerCommander: Failed to unarchive AX settings data: %{public}@"
+ "MSDDemoPeerCommander: Failed to unarchive IPD status data: %{public}@"
+ "MSDDemoPeerCommander: No IPD reset stage found."
+ "MSDDemoPeerCommander: No final IPD found."
+ "MSDDemoPeerResponder: Getting AX settings is not supported on iOS!"
+ "MSDDemoPeerResponder: Initiating IPD reset is not supported on iOS!"
+ "MSDDemoPeerResponder: Querying IPD reset stage is not supported on iOS!"
+ "MSDDemoPeerResponder: Setting AX settings is not supported on iOS!"
+ "MSDDemoPeerResponder: Skipping auto IPD adjustment is not supported on iOS!"
+ "MSDDemoPeerResponder:Reading IPD status is not supported on iOS!"
+ "MSDRapportMessageHandler: Unknown options key: %{public}@"
+ "MobileAssetDomain"
+ "TargetIPD"
+ "Timeout"
+ "_extractRapportOptionsFromMessage:"
+ "_handleGetAXSettingsRequestMessage:"
+ "_handleInitiateIPDResetRequestMessage:"
+ "_handleQueryIPDResetStageRequestMessage:"
+ "_handleReadIPDStatusRequestMessage:"
+ "_handleSetAXSettingsRequestMessage:"
+ "_handleSkipAutoIPDAdjustmentRequestMessage:"
+ "com.apple.MobileStoreDemo.GetAXSettings"
+ "com.apple.MobileStoreDemo.InitiateIPDReset"
+ "com.apple.MobileStoreDemo.QueryIPDResetStage"
+ "com.apple.MobileStoreDemo.ReadIPDStatus"
+ "com.apple.MobileStoreDemo.SetAXSettings"
+ "com.apple.MobileStoreDemo.SkipAutoIPDAdjustment"
+ "getAccessibiltiySettingsOnPeer:withCompletion:"
+ "initiateIPDResetOnPeer:targetIPD:withCompletion:"
+ "queryIPDResetStageOnPeer:withCompletion:"
+ "readIPDStatusFromPeer:withCompletion:"
+ "setAccessibiltiySettingsOnPeer:newSettings:withCompletion:"
+ "skipAutoIPDAdjustmentFromPeer:withCompletion:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"MSDKPeerDemoAXSettings\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"MSDKPeerDemoIPDStatus\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"
+ "v32@?0@\"NSString\"8@16^B24"
+ "v40@0:8@\"NSString\"16@\"MSDKPeerDemoAXSettings\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16d24@?<v@?d@\"NSError\">32"
+ "v40@0:8@16d24@?32"
- "%s - Current system auto-brightness setting: %{public}@"
- "%s - Current system brightness value: %{public}1.2f"
- "%s - Set system auto-brightness to %{public}@"
- "%s - Set system brightness to %{public}@"
- "-[MSDSettingsRefresher autoBrightness]"
- "-[MSDSettingsRefresher brightness]"
- "-[MSDSettingsRefresher setAutoBrightness:]"
- "-[MSDSettingsRefresher setBrightness:]"
- "AutoBrightness"
- "Brightness"
- "Commit"
- "DisplayBrightness"
- "DisplayBrightnessAuto"
- "Failed to retrieve device auto brightness setting. The auto brightness will not be refreshed"
- "Failed to retrieve device brightness setting. The brightness will not be refreshed"
- "Not restoring device auto brightness setting"
- "Not restoring device brightness setting"
- "T@\"NSNumber\",&,N,V_brightness"
- "T@\"NSString\",&,N,V_autoBrightness"
- "_autoBrightness"
- "_brightness"
- "autoBrightness"
- "brightness"
- "setAutoBrightness:"
- "setBrightness:"

```
