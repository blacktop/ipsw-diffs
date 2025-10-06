## nfcd

> `/usr/libexec/nfcd`

```diff

-340.36.0.0.0
-  __TEXT.__text: 0x212690
-  __TEXT.__auth_stubs: 0x16c0
-  __TEXT.__objc_stubs: 0xdae0
-  __TEXT.__objc_methlist: 0x7798
-  __TEXT.__const: 0xfa0
-  __TEXT.__oslogstring: 0x1fe54
-  __TEXT.__cstring: 0x2928d
-  __TEXT.__objc_classname: 0x1768
-  __TEXT.__objc_methname: 0x158bc
-  __TEXT.__objc_methtype: 0x4c08
-  __TEXT.__gcc_except_tab: 0x4668
+341.9.0.0.0
+  __TEXT.__text: 0x21867c
+  __TEXT.__auth_stubs: 0x16d0
+  __TEXT.__objc_stubs: 0xddc0
+  __TEXT.__objc_methlist: 0x78f0
+  __TEXT.__const: 0xfc0
+  __TEXT.__oslogstring: 0x20756
+  __TEXT.__cstring: 0x29c51
+  __TEXT.__objc_classname: 0x1782
+  __TEXT.__objc_methname: 0x15e72
+  __TEXT.__objc_methtype: 0x4cc9
+  __TEXT.__gcc_except_tab: 0x4784
   __TEXT.__dlopen_cstrs: 0x5ac
-  __TEXT.__unwind_info: 0x2fd0
-  __DATA_CONST.__auth_got: 0xb70
+  __TEXT.__unwind_info: 0x305c
+  __DATA_CONST.__auth_got: 0xb78
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x6ab8
-  __DATA_CONST.__cfstring: 0xf1e0
-  __DATA_CONST.__objc_classlist: 0x4e8
+  __DATA_CONST.__const: 0x6d10
+  __DATA_CONST.__cfstring: 0xf420
+  __DATA_CONST.__objc_classlist: 0x4f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x310
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x5a60
+  __DATA_CONST.__objc_intobj: 0x5a90
   __DATA_CONST.__objc_arraydata: 0x1d88
   __DATA_CONST.__objc_arrayobj: 0x3c0
   __DATA_CONST.__objc_dictobj: 0xe60
-  __DATA.__objc_const: 0x14610
-  __DATA.__objc_selrefs: 0x4fb0
+  __DATA.__objc_const: 0x14930
+  __DATA.__objc_selrefs: 0x5098
   __DATA.__objc_protorefs: 0x170
-  __DATA.__objc_classrefs: 0x728
+  __DATA.__objc_classrefs: 0x738
   __DATA.__objc_superrefs: 0x368
-  __DATA.__objc_ivar: 0xe08
-  __DATA.__objc_data: 0x3110
+  __DATA.__objc_ivar: 0xe38
+  __DATA.__objc_data: 0x3160
   __DATA.__data: 0x2528
   __DATA.__bss: 0x4c0
   __DATA.__common: 0x28

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 433C75BF-5FEF-3EF1-835B-B0ABE7F578E7
-  Functions: 3934
-  Symbols:   497
-  CStrings:  13078
+  UUID: 520CA98A-2396-3DFB-9EF1-6446BCC1181A
+  Functions: 3984
+  Symbols:   499
+  CStrings:  13246
 
Symbols:
+ _NFDriverEnableReaderModeDynamicBBAControl
+ _OBJC_CLASS_$_NSMapTable
+ _objc_retain_x5
- _objc_release_x13
CStrings:
+ "\x01\x13\x12"
+ "\x11\x121"
+ "%@,PID:%d"
+ "%c[%{public}s %{public}s]:%i %{public}@ (%d) %{public}@, config=%{public}@"
+ "%c[%{public}s %{public}s]:%i Already in suspended state"
+ "%c[%{public}s %{public}s]:%i Already reset within the last: %f"
+ "%c[%{public}s %{public}s]:%i Archive error=%{public}@"
+ "%c[%{public}s %{public}s]:%i Assertion timer (%{public}fs) started"
+ "%c[%{public}s %{public}s]:%i Assertion timer expired; connected=%{public}s"
+ "%c[%{public}s %{public}s]:%i Broadcast field match rules unavailable"
+ "%c[%{public}s %{public}s]:%i Broadcast field matches"
+ "%c[%{public}s %{public}s]:%i CH assertion count overflow!"
+ "%c[%{public}s %{public}s]:%i Camera assertion exists"
+ "%c[%{public}s %{public}s]:%i Contains undefined RFU bits but existing feature definition matches"
+ "%c[%{public}s %{public}s]:%i Cool ! This is the first SE OS reset since our process started. I mean it's not great but as the internets say : 'First!'"
+ "%c[%{public}s %{public}s]:%i Disabling dynamic BBA"
+ "%c[%{public}s %{public}s]:%i ECP broadcast"
+ "%c[%{public}s %{public}s]:%i ECP broadcast enabled"
+ "%c[%{public}s %{public}s]:%i ECP broadcast in HCE enabled"
+ "%c[%{public}s %{public}s]:%i Enabling FD & LPCD assist w/ECP %@"
+ "%c[%{public}s %{public}s]:%i Enabling LPCD assist w/ECP"
+ "%c[%{public}s %{public}s]:%i Enabling dynamic bba for PACE"
+ "%c[%{public}s %{public}s]:%i Force start session found"
+ "%c[%{public}s %{public}s]:%i Found suspend %@ waiting on field %@"
+ "%c[%{public}s %{public}s]:%i HCE+FD enabled"
+ "%c[%{public}s %{public}s]:%i Ignore field due to first unlock not completed"
+ "%c[%{public}s %{public}s]:%i Last OS reset was %f seconds ago"
+ "%c[%{public}s %{public}s]:%i Missing field"
+ "%c[%{public}s %{public}s]:%i Missing reason code"
+ "%c[%{public}s %{public}s]:%i Missing token"
+ "%c[%{public}s %{public}s]:%i PACE support declared by SessionConfig"
+ "%c[%{public}s %{public}s]:%i PACE support enabled by polling compatibility and AID list in app"
+ "%c[%{public}s %{public}s]:%i Polling options are PACE compatible"
+ "%c[%{public}s %{public}s]:%i Release assertion"
+ "%c[%{public}s %{public}s]:%i Renew timer"
+ "%c[%{public}s %{public}s]:%i Request assertion"
+ "%c[%{public}s %{public}s]:%i Session not active"
+ "%c[%{public}s %{public}s]:%i Session resume disabled"
+ "%c[%{public}s %{public}s]:%i Suspend active session %{public}@ on field"
+ "%c[%{public}s %{public}s]:%i Unexpected delegate type, dropping registration"
+ "%c[%{public}s %{public}s]:%i disableECPBroadcastInHCE override=%d"
+ "&\x11\x13\x11\x12Q\x11\x11\x13\x11?\x04\x12"
+ "@\"NFAssertion\""
+ "@\"NFHCEBroadcastECPConfig\""
+ "@\"NSMapTable\""
+ "@32@0:8Q16@24"
+ "@36@0:8@16B24B28I32"
+ "@40@0:8B16Q20I28@32"
+ "@72@0:8i16B20B24i28Q32Q40Q48I56@60B68"
+ "@8@?0"
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "CHAssertionForCamera"
+ "ECPBroadcast"
+ "ECPBroadcastFieldMatch"
+ "ECPBroadcastInterval"
+ "ECPBroadcastPollDuration"
+ "ERROR"
+ "F\x12"
+ "Initiator detected"
+ "Initiator request detected"
+ "NFCD built from (B&I) Stockholm_Base-341.9 at 22:14:25 on Oct  4 2023"
+ "NFHCEBroadcastECPConfig"
+ "ReasonCode"
+ "SESSION_RESUME_FROM_WAITING_ON_FIELD"
+ "SESSION_SUSPEND_STATE_UPDATE"
+ "SUCCESS"
+ "T@\"NFFieldNotification\",&,N,V_sessionResumeField"
+ "T@\"NFHCEBroadcastECPConfig\",&,N,V_ecpBroadcastConfig"
+ "T@\"NSMutableArray\",&,N,V_startOnFieldList"
+ "T@\"NSMutableArray\",&,N,V_suspendOnFieldList"
+ "TB,N,V_disableAutoStartOnField"
+ "Vv32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "_connectionHandoverAssertionForCamera"
+ "_delegatesLock"
+ "_didEnableDynamicBBA"
+ "_disableAutoStartOnField"
+ "_ecpBroadcastConfig"
+ "_ecpFrame"
+ "_initialRoutingConfigWithEmulation:ecp:pollDurationInMS:"
+ "_lastOSReset"
+ "_matchOnFieldResume"
+ "_maxBroadcastIntervalInMS"
+ "_pollDurationInMS"
+ "_registerForCameraNotifications"
+ "_routingConfigWithECPBroadcastInHCE"
+ "_sessionResumeField"
+ "_startOnFieldList"
+ "_suspendAssertionDeadline"
+ "_suspendOnFieldList"
+ "_syncResumeSession:field:"
+ "_syncStartAssertionTimer:"
+ "_sync_setECPPayload:completion:"
+ "_sync_startPollingWithConfig:completion:"
+ "_updateReaderSettingsBasedOnConfig:"
+ "defaultRoutingConfig:ecp:"
+ "disableAutoStartOnField"
+ "disableAutostartOnField"
+ "disableECPBroadcastInHCE"
+ "ecp"
+ "ecpBroadcastConfig"
+ "enableDefaultRoutingWithECP:"
+ "expressWithECP:"
+ "fd"
+ "hostCardEmulationVASBroadcastWithFrame:lpcdEnable:fieldDetect:pollDuration:"
+ "hostCardEmulationWithFieldDetect:"
+ "initPollingType:wantsSEReader:wantsExpress:cardEmulationType:hostMode:embeddedMode:fieldDetect:pollingDuration:lpcdEcpFrame:ecpBroadcast:"
+ "initialECPConfig"
+ "initialRoutingConfigWithField:"
+ "len=%{public,signpost.description:attribute}lu, status=%{public,signpost.description:attribute}s"
+ "lpcd"
+ "lpcdAssistWithECP"
+ "maybeStartNextSessionOnField:"
+ "pollDuration"
+ "readerWithLPCD:fieldDetect:pollDuration:ecp:"
+ "registerStateChangeWithDelegate:client:"
+ "requestConnectionHandoverAssert:"
+ "resumeSessionFromWaitingOnFieldWithCompletion:"
+ "resumeSessionWaitingOnField:forceStartSession:"
+ "routingOffWithFD:ecp:"
+ "session.suspendOnECP"
+ "sessionResumeField"
+ "setDisableAutoStartOnField:"
+ "setEcpBroadcastConfig:"
+ "setSessionResumeField:"
+ "setStartOnFieldList:"
+ "setSuspendOnFieldList:"
+ "skipMifareClassify"
+ "startOnFieldList"
+ "startPollingWithConfig:completion:"
+ "started=%{public,signpost.description:attribute}d"
+ "strongToWeakObjectsMapTable"
+ "suspendOnFieldList"
+ "suspendSession:reason:field:token:startNextSession:"
+ "suspendWithInfo:"
+ "suspensionStateUpdate:triggeredByField:"
+ "tech"
+ "v28@0:8B16@\"NFFieldNotification\"20"
+ "v28@0:8B16@20"
+ "v32@?0@\"NFFieldNotification\"8Q16^B24"
+ "\xf0\xf0Q"
- "\x01\x11\x11"
- "\x131"
- "%c[%{public}s %{public}s]:%i Assertion timer expired"
- "%c[%{public}s %{public}s]:%i Fail to set routing; reset to field detect"
- "%c[%{public}s %{public}s]:%i Found suspended %@ waiting on field %@"
- "%c[%{public}s %{public}s]:%i Ingore field due to first unlock not completed"
- "%c[%{public}s %{public}s]:%i Previous assertion exists"
- "&\x11\x13\x11\x12Q\x11\x11\x13?\x04\x11"
- "@\"<NFCameraStateMonitorDelegate>\""
- "F\x11"
- "NFCD built from (B&I) Stockholm_Base-340.36 at 03:13:34 on Aug  6 2023"
- "OS Reset"
- "T@\"NFFieldNotification\",&,N,V_startOnFieldDetected"
- "_registerForCameradNotifications"
- "_startOnFieldDetected"
- "_suspendAssertion"
- "_sync_startPollingForTechnology:completion:"
- "enableDefaultRouting"
- "readerWithLPCD:andFieldDetect:"
- "resumeSessionWaitingOnField:"
- "setStartOnFieldDetected:"
- "startOnFieldDetected"
- "startPollingForTechnology:completion:"
- "suspendSession:"
- "v28@0:8I16@?20"
- "\xf0\xf0A"

```
