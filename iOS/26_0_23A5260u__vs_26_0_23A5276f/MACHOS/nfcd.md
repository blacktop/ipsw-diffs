## nfcd

> `/usr/libexec/nfcd`

```diff

-360.33.0.0.0
-  __TEXT.__text: 0x27157c
-  __TEXT.__auth_stubs: 0x1820
+360.35.0.0.0
+  __TEXT.__text: 0x2756a0
+  __TEXT.__auth_stubs: 0x1840
   __TEXT.__delay_stubs: 0x370
-  __TEXT.__delay_helper: 0x117c
-  __TEXT.__objc_stubs: 0xd3c0
-  __TEXT.__objc_methlist: 0x9c20
+  __TEXT.__delay_helper: 0x120c
+  __TEXT.__objc_stubs: 0xd400
+  __TEXT.__objc_methlist: 0x9c48
   __TEXT.__const: 0x1390
-  __TEXT.__objc_methname: 0x17aff
-  __TEXT.__cstring: 0x2ecbf
-  __TEXT.__objc_classname: 0x1d61
-  __TEXT.__objc_methtype: 0x5603
-  __TEXT.__oslogstring: 0x262c8
-  __TEXT.__unwind_info: 0x2b98
-  __DATA_CONST.__auth_got: 0xcb8
-  __DATA_CONST.__got: 0x5b8
+  __TEXT.__objc_methname: 0x17c03
+  __TEXT.__cstring: 0x2f3e2
+  __TEXT.__objc_classname: 0x1d5f
+  __TEXT.__objc_methtype: 0x563a
+  __TEXT.__oslogstring: 0x2677b
+  __TEXT.__unwind_info: 0x2bb8
+  __DATA_CONST.__auth_got: 0xcc8
+  __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x80c8
-  __DATA_CONST.__cfstring: 0x10d60
+  __DATA_CONST.__const: 0x83e0
+  __DATA_CONST.__cfstring: 0x11020
   __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x468
-  __DATA_CONST.__objc_intobj: 0x7758
-  __DATA_CONST.__objc_arraydata: 0x1d28
+  __DATA_CONST.__objc_intobj: 0x77a0
+  __DATA_CONST.__objc_arraydata: 0x1d88
   __DATA_CONST.__objc_arrayobj: 0x2b8
-  __DATA_CONST.__objc_dictobj: 0xeb0
-  __DATA.__objc_const: 0x14888
-  __DATA.__objc_selrefs: 0x5558
-  __DATA.__objc_ivar: 0x109c
+  __DATA_CONST.__objc_dictobj: 0xfa0
+  __DATA.__objc_const: 0x14870
+  __DATA.__objc_selrefs: 0x5598
+  __DATA.__objc_ivar: 0x1098
   __DATA.__objc_data: 0x3d90
   __DATA.__data: 0x2b94
   __DATA.__bss: 0x278

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9EE61DF-A3D3-3A59-88CB-2CA6639C158F
-  Functions: 4125
-  Symbols:   586
-  CStrings:  14464
+  UUID: 6BCADCF0-E735-3337-A5AA-EE516D8330A6
+  Functions: 4145
+  Symbols:   592
+  CStrings:  14555
 
Symbols:
+ _dispatch_block_cancel
+ _dispatch_block_wait
+ _kSymptomDiagnosticKeyPayloadPath
+ _kSymptomDiagnosticReplyRateLimitExpiresIn
+ _kSymptomDiagnosticReplyReason
+ _kSymptomDiagnosticReplyReasonString
CStrings:
+ "%c[%{public}s %{public}s]:%i ABC Request was rejected. Reason Code: %ld"
+ "%c[%{public}s %{public}s]:%i Applet authTransientSupport is enabled; aid=%{public}@"
+ "%c[%{public}s %{public}s]:%i Applet does not support key; aid=%{public}@, key=%{public}@"
+ "%c[%{public}s %{public}s]:%i Applet dump failed"
+ "%c[%{public}s %{public}s]:%i Applet not found from SE; applet=%{public}@"
+ "%c[%{public}s %{public}s]:%i Calling before first unlock!!!"
+ "%c[%{public}s %{public}s]:%i Config not yet initialized"
+ "%c[%{public}s %{public}s]:%i Consistency check failure"
+ "%c[%{public}s %{public}s]:%i Defaults disabling MIFARE detection"
+ "%c[%{public}s %{public}s]:%i Empty express config"
+ "%c[%{public}s %{public}s]:%i Failed to resume Continuous Wave - %{public}@"
+ "%c[%{public}s %{public}s]:%i Key not found; aid=%{public}@, key=%{public}@"
+ "%c[%{public}s %{public}s]:%i Mismatch in moduleID; applet=%{public}@"
+ "%c[%{public}s %{public}s]:%i Not yet first unlock"
+ "%c[%{public}s %{public}s]:%i Not yet first unlock; express config failed"
+ "%c[%{public}s %{public}s]:%i Pass config contain invalid entry; aid=%{public}@"
+ "%c[%{public}s %{public}s]:%i Session is not allowed ..."
+ "%c[%{public}s %{public}s]:%i Skipping MIFARE classification due to previous override"
+ "%c[%{public}s %{public}s]:%i firstUnlock=%d, target state=%ld"
+ "%c[%{public}s %{public}s]:%i haveCache %d cacheCtr %{public}@ currentCtr %{public}@ useCache %d forceReadAndSkipUpdate %d"
+ "%s, client=%@,"
+ "ABC submission failure (code=%ld); trigger os state dump"
+ "Access not accepted"
+ "Applet does not contain specified key"
+ "Applet missing from SE"
+ "B32@0:8@\"NSMutableArray\"16^@24"
+ "Express config init before 1st unlock"
+ "Express config invalid"
+ "HomeKitFirmwareVersion"
+ "Invalid subType"
+ "Invalid subTypeContext"
+ "Invalid type"
+ "Missing authorization"
+ "NFCD built from (B&I) Stockholm_Base-360.35"
+ "Not inited"
+ "Not yet first unlock"
+ "Pass config contains invalid entries"
+ "Pass config expressEnabled set but applet authTransientSetting is true"
+ "Time limited"
+ "Unknown reason"
+ "Watchdog"
+ "_expressConfigInit"
+ "_getApplicationsFromSE:filtered:forceReadAndSkipUpdate:"
+ "_validateKeyExistence:applet:contactless:rapdu:"
+ "checkSessionAllowed"
+ "consistencyCheckWithConfig:"
+ "expressAppletsWithExtraError:"
+ "getExpressPassConfig"
+ "initWithQueue:"
+ "loadConfig:outError:"
+ "nfcd.abc"
+ "out, config not yet initialized"
+ "postDailyTagStatistics"
+ "requestAutoBugCapture:subType:subTypeContext:attachments:completion:"
+ "restoreAuthorizationForAllAppletsExcept:uid:expressConfigInitError:"
+ "restoreAuthorizationForKeys:onApplet:expressConfigInitError:"
+ "startContinuousWaveWithCompletion:"
+ "totalNoUrlTagsRead"
+ "totalNotBackgroundTagsRead"
+ "totalNotNdefTagsRead"
+ "totalOtherErrors"
+ "totalProhibitTimerErrors"
+ "totalSuccesfulBackgroundTagsRead"
+ "updateDailyTagStatistic:"
+ "v24@?0@\"NSError\"8d16"
+ "v56@0:8@16@24@32@40@?48"
- "%c[%{public}s %{public}s]:%i ABC Request was rejected. Reason Code: %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to resume Continous Wave - %{public}@"
- "%c[%{public}s %{public}s]:%i disabling mifare detection"
- "%c[%{public}s %{public}s]:%i haveCache %d cacheCtr %{public}@ currentCtr %{public}@ useCache %d"
- "7"
- "FWversion"
- "Last Field OFF time"
- "NFCD built from (B&I) Stockholm_Base-360.33"
- "_getApplicationsFromSE:filtered:"
- "_requestAutoBugCapture:withSubType:withSubTypeContext:"
- "initFromStorageWithDriverWrapper:"
- "productID"
- "reason"
- "requestAutoBugCapture:withSubType:withSubTypeContext:"
- "restoreAuthorizationForKeys:onApplet:"
- "startContinousWaveWithCompletion:"
- "timeIntervalSinceReferenceDate"
- "vendorID"

```
