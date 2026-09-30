## HearingModeService

> `/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService`

```diff

-30.45.3.0.0
-  __TEXT.__text: 0x1327c
+30.48.2.1.2
+  __TEXT.__text: 0x13a7c
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x150c
+  __TEXT.__objc_methlist: 0x161c
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x4359
+  __TEXT.__cstring: 0x44c6
   __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__unwind_info: 0x430
-  __TEXT.__objc_classname: 0x127
-  __TEXT.__objc_methname: 0x4fa3
-  __TEXT.__objc_methtype: 0x8b5
-  __TEXT.__objc_stubs: 0x2040
-  __DATA_CONST.__got: 0x118
+  __TEXT.__unwind_info: 0x450
+  __TEXT.__objc_classname: 0x130
+  __TEXT.__objc_methname: 0x5493
+  __TEXT.__objc_methtype: 0x8bf
+  __TEXT.__objc_stubs: 0x2060
+  __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x5e8
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf40
+  __DATA_CONST.__objc_selrefs: 0xfc0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_const: 0x2988
+  __AUTH_CONST.__cfstring: 0x15a0
+  __AUTH_CONST.__objc_const: 0x2cf8
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x2c8
+  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x300
   __DATA.__data: 0x4d0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1A5F281-BEE4-3CD4-B022-67D9984753C5
-  Functions: 539
-  Symbols:   1786
-  CStrings:  1607
+  UUID: 96913BBF-D4EE-3F75-A005-CA062B8329AF
+  Functions: 563
+  Symbols:   1859
+  CStrings:  1684
 
Symbols:
+ +[HMInfo supportsSecureCoding]
+ -[HMDeviceRecord getSafetyInformation:]
+ -[HMDeviceRecord safetyInformation]
+ -[HMDeviceRecord setVersion:]
+ -[HMDeviceRecord version]
+ -[HMInfo .cxx_destruct]
+ -[HMInfo adaptiveModeDays]
+ -[HMInfo adaptiveModeHours]
+ -[HMInfo adaptiveModeLowerBound]
+ -[HMInfo adaptiveModeUpperBound]
+ -[HMInfo encodeWithCoder:]
+ -[HMInfo initWithCoder:]
+ -[HMInfo noiseCancellationModeDays]
+ -[HMInfo noiseCancellationModeHours]
+ -[HMInfo noiseCancellationModeLowerBound]
+ -[HMInfo noiseCancellationModeUpperBound]
+ -[HMInfo setConstantsWith:]
+ -[HMInfo setConstantsWith:].cold.1
+ -[HMInfo setConstantsWith:].cold.2
+ -[HMInfo setConstantsWith:].cold.3
+ -[HMInfo transparencyModeDays]
+ -[HMInfo transparencyModeHours]
+ -[HMInfo transparencyModeLowerBound]
+ -[HMInfo transparencyModeUpperBound]
+ _OBJC_CLASS_$_HMInfo
+ _OBJC_IVAR_$_HMDeviceRecord._safetyInformation
+ _OBJC_IVAR_$_HMDeviceRecord._version
+ _OBJC_IVAR_$_HMInfo._adaptiveModeDays
+ _OBJC_IVAR_$_HMInfo._adaptiveModeHours
+ _OBJC_IVAR_$_HMInfo._adaptiveModeLowerBound
+ _OBJC_IVAR_$_HMInfo._adaptiveModeUpperBound
+ _OBJC_IVAR_$_HMInfo._noiseCancellationModeDays
+ _OBJC_IVAR_$_HMInfo._noiseCancellationModeHours
+ _OBJC_IVAR_$_HMInfo._noiseCancellationModeLowerBound
+ _OBJC_IVAR_$_HMInfo._noiseCancellationModeUpperBound
+ _OBJC_IVAR_$_HMInfo._transparencyModeDays
+ _OBJC_IVAR_$_HMInfo._transparencyModeHours
+ _OBJC_IVAR_$_HMInfo._transparencyModeLowerBound
+ _OBJC_IVAR_$_HMInfo._transparencyModeUpperBound
+ _OBJC_METACLASS_$_HMInfo
+ __OBJC_$_CLASS_METHODS_HMInfo
+ __OBJC_$_CLASS_PROP_LIST_HMInfo
+ __OBJC_$_INSTANCE_METHODS_HMInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMInfo
+ __OBJC_$_PROP_LIST_HMInfo
+ __OBJC_CLASS_PROTOCOLS_$_HMInfo
+ __OBJC_CLASS_RO_$_HMInfo
+ __OBJC_METACLASS_RO_$_HMInfo
+ ___69+[HMAudiogramUtility frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.452
+ _objc_msgSend$setConstantsWith:
- ___69+[HMAudiogramUtility frequencyToHearingDecibelLevelMapFromAudiogram:]_block_invoke.449
CStrings:
+ "\f"
+ "## Unknown settings data received with identifier: %d. Version updated ? %d (value = %d)"
+ "-[HMInfo setConstantsWith:]"
+ "@\"HMInfo\""
+ "HMInfo"
+ "HMInfo PID check - %d"
+ "HMInfo creating safety information for unknown device, please check PID to see if functionality is supported!"
+ "HMInfo creating safety information values for B698"
+ "T@\"HMInfo\",R,N,V_safetyInformation"
+ "T@\"NSNumber\",R,N,V_adaptiveModeDays"
+ "T@\"NSNumber\",R,N,V_adaptiveModeHours"
+ "T@\"NSNumber\",R,N,V_adaptiveModeLowerBound"
+ "T@\"NSNumber\",R,N,V_adaptiveModeUpperBound"
+ "T@\"NSNumber\",R,N,V_noiseCancellationModeDays"
+ "T@\"NSNumber\",R,N,V_noiseCancellationModeHours"
+ "T@\"NSNumber\",R,N,V_noiseCancellationModeLowerBound"
+ "T@\"NSNumber\",R,N,V_noiseCancellationModeUpperBound"
+ "T@\"NSNumber\",R,N,V_transparencyModeDays"
+ "T@\"NSNumber\",R,N,V_transparencyModeHours"
+ "T@\"NSNumber\",R,N,V_transparencyModeLowerBound"
+ "T@\"NSNumber\",R,N,V_transparencyModeUpperBound"
+ "TC,N,V_version"
+ "_\f"
+ "_adaptiveModeDays"
+ "_adaptiveModeHours"
+ "_adaptiveModeLowerBound"
+ "_adaptiveModeUpperBound"
+ "_noiseCancellationModeDays"
+ "_noiseCancellationModeHours"
+ "_noiseCancellationModeLowerBound"
+ "_noiseCancellationModeUpperBound"
+ "_safetyInformation"
+ "_transparencyModeDays"
+ "_transparencyModeHours"
+ "_transparencyModeLowerBound"
+ "_transparencyModeUpperBound"
+ "aDay"
+ "aHrs"
+ "aLwr"
+ "aUpr"
+ "adaptiveModeDays"
+ "adaptiveModeHours"
+ "adaptiveModeLowerBound"
+ "adaptiveModeUpperBound"
+ "getSafetyInformation:"
+ "nDay"
+ "nHrs"
+ "nLwr"
+ "nUpr"
+ "noiseCancellationModeDays"
+ "noiseCancellationModeHours"
+ "noiseCancellationModeLowerBound"
+ "noiseCancellationModeUpperBound"
+ "sInf"
+ "safetyInformation"
+ "setConstantsWith:"
+ "setVersion:"
+ "tDay"
+ "tHrs"
+ "tLwr"
+ "tUpr"
+ "transparencyModeDays"
+ "transparencyModeHours"
+ "transparencyModeLowerBound"
+ "transparencyModeUpperBound"
- "O\v"

```
