## SoftwareUpdateController

> `/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController`

```diff

-138.0.0.0.0
-  __TEXT.__text: 0xcfa4
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x10dc
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x2feb
+146.0.0.0.1
+  __TEXT.__text: 0xcea8
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x10f4
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x302a
   __TEXT.__oslogstring: 0x17
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x304
+  __TEXT.__unwind_info: 0x310
   __TEXT.__objc_classname: 0x13a
-  __TEXT.__objc_methname: 0x3bd8
+  __TEXT.__objc_methname: 0x3c3a
   __TEXT.__objc_methtype: 0xd4a
-  __TEXT.__objc_stubs: 0x1f60
+  __TEXT.__objc_stubs: 0x1f40
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x358
+  __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2378
-  __DATA_CONST.__objc_selrefs: 0xb40
-  __AUTH_CONST.__cfstring: 0x22a0
+  __DATA_CONST.__objc_const: 0x23a8
+  __DATA_CONST.__objc_selrefs: 0xb50
+  __DATA_CONST.__objc_classrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0x58
+  __AUTH_CONST.__cfstring: 0x2240
   __AUTH_CONST.__objc_const: 0x5e8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__auth_got: 0x370
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0x58
-  __DATA.__objc_ivar: 0x1a4
+  __DATA.__objc_ivar: 0x1a8
   __DATA.__data: 0x348
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 037E4E64-B61E-3804-8B54-AE34F7E189BD
-  Functions: 385
-  Symbols:   1526
-  CStrings:  1395
+  UUID: E3C22AA2-FC05-39E7-A6FD-02CA1602FEF3
+  Functions: 390
+  Symbols:   1538
+  CStrings:  1397
 
Symbols:
+ -[SUControllerManager _daemonLaunched]
+ -[SUControllerManager _forwardConnectionError:]
+ -[SUControllerManager _forwardConnectionRegained]
+ -[SUControllerManager _indicateConnectionRegained]
+ -[SUControllerManager disconnected]
+ -[SUControllerManager initializing]
+ -[SUControllerManager notifyDaemonStartedToken]
+ -[SUControllerManager setDisconnected:]
+ -[SUControllerManager setInitializing:]
+ -[SUControllerManager setNotifyDaemonStartedToken:]
+ GCC_except_table10
+ GCC_except_table15
+ _OBJC_IVAR_$_SUControllerManager._disconnected
+ _OBJC_IVAR_$_SUControllerManager._initializing
+ _OBJC_IVAR_$_SUControllerManager._notifyDaemonStartedToken
+ _SUControllerDaemonLaunchedNotification
+ ___30-[SUControllerManager dealloc]_block_invoke
+ ___46-[SUControllerManager cancelCurrentConnection]_block_invoke
+ ___50-[SUControllerManager _indicateConnectionRegained]_block_invoke
+ ___84-[SUControllerManager initWithExclusiveControl:communalUponDisconnect:withDelegate:]_block_invoke_2
+ _dispatch_assert_queue$V2
+ _objc_msgSend$_daemonLaunched
+ _objc_msgSend$_forwardConnectionError:
+ _objc_msgSend$_forwardConnectionRegained
+ _objc_msgSend$_indicateConnectionRegained
+ _objc_msgSend$disconnected
+ _objc_msgSend$initializing
+ _objc_msgSend$setDisconnected:
+ _objc_msgSend$setInitializing:
+ _objc_msgSend$setServerXPCConnection:
- -[SUControllerManager _attemptReconnect]
- -[SUControllerManager _forwardConnectionError:message:]
- -[SUControllerManager _forwardConnectionRegained:message:]
- -[SUControllerManager _indicateConnectionRegained:]
- -[SUControllerManager reconnectFailed]
- -[SUControllerManager reconnecting]
- -[SUControllerManager setReconnectFailed:]
- -[SUControllerManager setReconnecting:]
- GCC_except_table12
- GCC_except_table7
- _OBJC_IVAR_$_SUControllerManager._reconnectFailed
- _OBJC_IVAR_$_SUControllerManager._reconnecting
- ___51-[SUControllerManager _indicateConnectionRegained:]_block_invoke
- _objc_msgSend$_attemptReconnect
- _objc_msgSend$_forwardConnectionError:message:
- _objc_msgSend$_forwardConnectionRegained:message:
- _objc_msgSend$_indicateConnectionRegained:
- _objc_msgSend$preservePreparedMaxAttempts
- _objc_msgSend$reconnectFailed
- _objc_msgSend$reconnecting
- _objc_msgSend$setPreservePreparedMaxAttempts:
- _objc_msgSend$setReconnectFailed:
- _objc_msgSend$setReconnecting:
CStrings:
+ "\nuseSUCore: %@\nVPNOnDemandAsInternal: %@\nPerformAutoScan: %@\nPerformAutoDownloadAndPrepare: %@\nPerformAutoInstall: %@\nAutoAcceptTermsAndConditions: %@\nAutoActivityCheckPeriod: %d minutes\nAutoInstallForceMaxWait: %d minutes\nAutoInstallWindowBegin: %02d:%02d\nAutoInstallWindowEnd: %02d:%02d\nDownloadDocAsset: %@\nIgnoreRamping: %@\nSupervisedMDM: %@\nRequestedPMV: %@\nDelayPeriod: %d days\nInstallPhaseOSBackgroundImagePath: %@\nRestrictToFullReplacement: %@\nAllowSameVersionUpdates: %@\nUpdateMetricContext: %@\nPrerequisiteBuildVersion: %@\nPrerequisiteProductVersion: %@\nAsReleaseType: %@\nsimulatorCommandsFile: %@\nuseSpecifiedInstallWindow: %@\nexpiredSpecifiedAsExpired: %@\nHideIndicationMayReboot: %@\nInternalDefaultsAsExternal: %@\nRequirePrepareSize: %@\nInstallWindowAsDeltas: %@"
+ "-[SUControllerManager _daemonLaunched]"
+ "-[SUControllerManager _forwardConnectionError:]"
+ "-[SUControllerManager _forwardConnectionRegained]"
+ "-[SUControllerManager _handleStateReport]"
+ "-[SUControllerManager initWithExclusiveControl:communalUponDisconnect:withDelegate:]_block_invoke"
+ "3"
+ "SUCManager - received notification that sucontrollerd is launched"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_disconnected"
+ "TB,N,V_initializing"
+ "Ti,N,V_notifyDaemonStartedToken"
+ "_daemonLaunched"
+ "_disconnected"
+ "_forwardConnectionError:"
+ "_forwardConnectionRegained"
+ "_indicateConnectionRegained"
+ "_initializing"
+ "_notifyDaemonStartedToken"
+ "com.apple.SoftwareUpdateController.Daemon.Launched"
+ "disconnected"
+ "initializing"
+ "notifyDaemonStartedToken"
+ "setDisconnected:"
+ "setInitializing:"
+ "setNotifyDaemonStartedToken:"
+ "sucontrollerd disconnected"
+ "sucontrollerd is launched"
+ "sucontrollerd state changed"
+ "useSUCore:%@,vpnAsInternal:%@,autoScan:%@,autoDownload:%@,autoInstall:%@,autoAccept:%@,activityPeriod:%d,forceMaxWait:%d,windowBegin:%02d:%02d,windowEnd:%02d:%02d,downloadDoc:%@,ignoreRamp:%@,supervisedMDM:%@,requestedPMV:%@,delayPeriod:%d,installPhaseBGImgPath:%@,restrictToFull:%@,allowSame:%@,context:%@,asBuild:%@,asProduct:%@,asRelease:%@,simFile:%@,useInstallWindow:%@,expiredAsExpired:%@,hideMayReboot:%@,asExternal:%@,requirePrepSize:%@,windowDeltas:%@"
- "\nuseSUCore: %@\npreservePreparedMaxAttempts: %d\nVPNOnDemandAsInternal: %@\nPerformAutoScan: %@\nPerformAutoDownloadAndPrepare: %@\nPerformAutoInstall: %@\nAutoAcceptTermsAndConditions: %@\nAutoActivityCheckPeriod: %d minutes\nAutoInstallForceMaxWait: %d minutes\nAutoInstallWindowBegin: %02d:%02d\nAutoInstallWindowEnd: %02d:%02d\nDownloadDocAsset: %@\nIgnoreRamping: %@\nSupervisedMDM: %@\nRequestedPMV: %@\nDelayPeriod: %d days\nInstallPhaseOSBackgroundImagePath: %@\nRestrictToFullReplacement: %@\nAllowSameVersionUpdates: %@\nUpdateMetricContext: %@\nPrerequisiteBuildVersion: %@\nPrerequisiteProductVersion: %@\nAsReleaseType: %@\nsimulatorCommandsFile: %@\nuseSpecifiedInstallWindow: %@\nexpiredSpecifiedAsExpired: %@\nHideIndicationMayReboot: %@\nInternalDefaultsAsExternal: %@\nRequirePrepareSize: %@\nInstallWindowAsDeltas: %@"
- "\x11"
- "#"
- "%@ XPC connection regained"
- "%@ XPC error on server connection (attempting reconnect): %s"
- "%@ XPC error while reconnecting: %s"
- "%@ received XPC message %s"
- "-[SUControllerManager _forwardConnectionError:message:]"
- "-[SUControllerManager _forwardConnectionRegained:message:]"
- "SUCManager[RECONNECTING]"
- "SUPreservePreparedMaxAttempts"
- "TB,N,V_reconnectFailed"
- "TB,N,V_reconnecting"
- "_attemptReconnect"
- "_forwardConnectionError:message:"
- "_forwardConnectionRegained:message:"
- "_indicateConnectionRegained:"
- "_reconnectFailed"
- "_reconnecting"
- "reconnectFailed"
- "reconnecting"
- "setReconnectFailed:"
- "setReconnecting:"
- "useSUCore:%@,preserveMax:%d,vpnAsInternal:%@,autoScan:%@,autoDownload:%@,autoInstall:%@,autoAccept:%@,activityPeriod:%d,forceMaxWait:%d,windowBegin:%02d:%02d,windowEnd:%02d:%02d,downloadDoc:%@,ignoreRamp:%@,supervisedMDM:%@,requestedPMV:%@,delayPeriod:%d,installPhaseBGImgPath:%@,restrictToFull:%@,allowSame:%@,context:%@,asBuild:%@,asProduct:%@,asRelease:%@,simFile:%@,useInstallWindow:%@,expiredAsExpired:%@,hideMayReboot:%@,asExternal:%@,requirePrepSize:%@,windowDeltas:%@"
- "|preserveMax:%d"

```
