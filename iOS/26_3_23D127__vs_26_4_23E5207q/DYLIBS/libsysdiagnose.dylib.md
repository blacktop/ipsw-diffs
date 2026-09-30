## libsysdiagnose.dylib

> `/usr/lib/libsysdiagnose.dylib`

```diff

-1527.80.3.0.0
-  __TEXT.__text: 0x2fbc
-  __TEXT.__auth_stubs: 0x4e0
+1527.100.24.0.0
+  __TEXT.__text: 0x3134
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_methlist: 0xe0
   __TEXT.__oslogstring: 0x1f8
   __TEXT.__cstring: 0x58e

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220
-  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x540
   __AUTH_CONST.__objc_const: 0x90

   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5350432A-F2CB-3793-B3AD-5FE4D389EE38
+  UUID: 5B643B6D-6B31-304E-A18B-AC6B41844C71
   Functions: 38
-  Symbols:   288
+  Symbols:   283
   CStrings:  203
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
- _objc_storeStrong
Functions:
~ _appendToCrashlogsDir : 176 -> 188
~ +[Libsysdiagnose setupConnection] : 200 -> 204
~ +[Libsysdiagnose createSysdiagnoseRequest:] : 832 -> 852
~ +[Libsysdiagnose addErrorString:withCode:forError:] : 252 -> 256
~ ___45+[Libsysdiagnose createMetrics:fromResponse:]_block_invoke : 160 -> 172
~ +[Libsysdiagnose verifyReply:withExpectedType:forError:] : 284 -> 288
~ _safeFetchStr : 64 -> 68
~ ___83+[Libsysdiagnose sendSysdiagnoseRequest:withMetrics:withError:withProgressHandler:]_block_invoke : 660 -> 692
~ _safeFetchErrorStr : 180 -> 196
~ ___83+[Libsysdiagnose sendSysdiagnoseRequest:withMetrics:withError:withProgressHandler:]_block_invoke.93 : 624 -> 668
~ +[Libsysdiagnose sysdiagnoseWithMetadata:withMetrics:withError:withProgressCallback:] : 636 -> 620
~ ___85+[Libsysdiagnose sysdiagnoseWithMetadata:withMetrics:withError:withProgressCallback:]_block_invoke : 240 -> 264
~ +[Libsysdiagnose sysdiagnoseWithMetadata:withMetrics:withError:withProgressHandler:] : 636 -> 620
~ ___84+[Libsysdiagnose sysdiagnoseWithMetadata:withMetrics:withError:withProgressHandler:]_block_invoke : 464 -> 496
~ ___84+[Libsysdiagnose sysdiagnoseWithMetadata:withMetrics:withError:withProgressHandler:]_block_invoke_2 : 112 -> 116
~ +[Libsysdiagnose sysdiagnoseWithMetadata:onCompletion:] : 212 -> 204
~ +[Libsysdiagnose isSysdiagnoseInProgressWithError:] : 680 -> 684
~ +[Libsysdiagnose cancelActiveSysdiagnoseWithError:] : 236 -> 240
~ +[Libsysdiagnose fetchDiagnosticIDFromDeviceSource:WithMaxCount:withError:] : 1224 -> 1292
~ ___75+[Libsysdiagnose fetchDiagnosticIDFromDeviceSource:WithMaxCount:withError:]_block_invoke : 184 -> 188
~ _extractDiagnosticID : 556 -> 568
~ +[Libsysdiagnose fetchRemoteDiagnosticIDsWithError:] : 488 -> 504
~ +[Libsysdiagnose getSysdiagnoseCrashLog] : 924 -> 1016
~ ___40+[Libsysdiagnose getSysdiagnoseCrashLog]_block_invoke : 184 -> 188

```
