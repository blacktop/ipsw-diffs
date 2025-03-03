## SoftwareUpdateController

> `/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController`

```diff

-163.0.0.0.0
-  __TEXT.__text: 0xd160
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x1180
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x31fe
+166.100.3.0.0
+  __TEXT.__text: 0xd268
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0x14dc
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x3292
   __TEXT.__oslogstring: 0x17
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x330
   __TEXT.__objc_classname: 0x13a
-  __TEXT.__objc_methname: 0x3eaa
+  __TEXT.__objc_methname: 0x3f55
   __TEXT.__objc_methtype: 0xd4a
-  __TEXT.__objc_stubs: 0x2000
+  __TEXT.__objc_stubs: 0x2060
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xba8
+  __DATA_CONST.__objc_selrefs: 0xd20
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x370
+  __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x2300
-  __AUTH_CONST.__objc_const: 0x2a80
+  __AUTH_CONST.__cfstring: 0x2360
+  __AUTH_CONST.__objc_const: 0x24a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x1bc
+  __DATA.__objc_ivar: 0x1c0
   __DATA.__data: 0x348
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 402
-  Symbols:   645
-  CStrings:  1150
+  Functions: 407
+  Symbols:   651
+  CStrings:  1158
 
Symbols:
+ _objc_retain_x26
+ _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "\nuseSUCore: %@\nVPNOnDemandAsInternal: %@\nPerformAutoScan: %@\nPerformAutoDownloadAndPrepare: %@\nPerformAutoInstall: %@\nAutoAcceptTermsAndConditions: %@\nAutoActivityCheckPeriod: %d minutes\nAutoInstallForceMaxWait: %d minutes\nAutoInstallWindowBegin: %02d:%02d\nAutoInstallWindowEnd: %02d:%02d\nDownloadDocAsset: %@\nIgnoreRamping: %@\nSupervisedMDM: %@\nRequestedPMV: %@\nDelayPeriod: %d days\nInstallPhaseOSBackgroundImagePath: %@\nRestrictToFullReplacement: %@\nAllowSameVersionUpdates: %@\nUpdateMetricContext: %@\nPrerequisiteBuildVersion: %@\nPrerequisiteProductVersion: %@\nAsReleaseType: %@\nsimulatorCommandsFile: %@\nuseSpecifiedInstallWindow: %@\nexpiredSpecifiedAsExpired: %@\nHideIndicationMayReboot: %@\nInternalDefaultsAsExternal: %@\nRequirePrepareSize: %@\nInstallWindowAsDeltas: %@\nmaxOptionalPSUSDownloadSize: %ld"
+ "SUMaxOptionalPSUSDownloadSize"
+ "Tq,N,V_maxOptionalPSUSDownloadSize"
+ "_allowedToTurnOffAutoScan"
+ "_loadIntegerFromDefaults:usingDefault:"
+ "_maxOptionalPSUSDownloadSize"
+ "maxOptionalPSUSDownloadSize"
+ "setMaxOptionalPSUSDownloadSize:"
+ "useSUCore:%@,vpnAsInternal:%@,autoScan:%@,autoDownload:%@,autoInstall:%@,autoAccept:%@,activityPeriod:%d,forceMaxWait:%d,windowBegin:%02d:%02d,windowEnd:%02d:%02d,downloadDoc:%@,ignoreRamp:%@,supervisedMDM:%@,requestedPMV:%@,delayPeriod:%d,installPhaseBGImgPath:%@,restrictToFull:%@,allowSame:%@,context:%@,asBuild:%@,asProduct:%@,asRelease:%@,simFile:%@,useInstallWindow:%@,expiredAsExpired:%@,hideMayReboot:%@,asExternal:%@,requirePrepSize:%@,windowDeltas:%@,maxOptionalPSUSDownloadSize:%ld"
+ "|maxOptionalPSUSSize:%ld"
- "\nuseSUCore: %@\nVPNOnDemandAsInternal: %@\nPerformAutoScan: %@\nPerformAutoDownloadAndPrepare: %@\nPerformAutoInstall: %@\nAutoAcceptTermsAndConditions: %@\nAutoActivityCheckPeriod: %d minutes\nAutoInstallForceMaxWait: %d minutes\nAutoInstallWindowBegin: %02d:%02d\nAutoInstallWindowEnd: %02d:%02d\nDownloadDocAsset: %@\nIgnoreRamping: %@\nSupervisedMDM: %@\nRequestedPMV: %@\nDelayPeriod: %d days\nInstallPhaseOSBackgroundImagePath: %@\nRestrictToFullReplacement: %@\nAllowSameVersionUpdates: %@\nUpdateMetricContext: %@\nPrerequisiteBuildVersion: %@\nPrerequisiteProductVersion: %@\nAsReleaseType: %@\nsimulatorCommandsFile: %@\nuseSpecifiedInstallWindow: %@\nexpiredSpecifiedAsExpired: %@\nHideIndicationMayReboot: %@\nInternalDefaultsAsExternal: %@\nRequirePrepareSize: %@\nInstallWindowAsDeltas: %@"
- "_runningOnAppleTV"
- "useSUCore:%@,vpnAsInternal:%@,autoScan:%@,autoDownload:%@,autoInstall:%@,autoAccept:%@,activityPeriod:%d,forceMaxWait:%d,windowBegin:%02d:%02d,windowEnd:%02d:%02d,downloadDoc:%@,ignoreRamp:%@,supervisedMDM:%@,requestedPMV:%@,delayPeriod:%d,installPhaseBGImgPath:%@,restrictToFull:%@,allowSame:%@,context:%@,asBuild:%@,asProduct:%@,asRelease:%@,simFile:%@,useInstallWindow:%@,expiredAsExpired:%@,hideMayReboot:%@,asExternal:%@,requirePrepSize:%@,windowDeltas:%@"

```
