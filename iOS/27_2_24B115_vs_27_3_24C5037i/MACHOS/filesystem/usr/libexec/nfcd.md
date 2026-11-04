## nfcd

> `/usr/libexec/nfcd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-371.8.0.0.0
-  __TEXT.__text: 0x1eb448
-  __TEXT.__auth_stubs: 0x1920
+372.4.1.0.0
+  __TEXT.__text: 0x1eab94
+  __TEXT.__auth_stubs: 0x1930
   __TEXT.__delay_stubs: 0x540
-  __TEXT.__delay_helper: 0x1878
-  __TEXT.__objc_stubs: 0xe3e0
-  __TEXT.__objc_methlist: 0x9fc4
+  __TEXT.__delay_helper: 0x1760
+  __TEXT.__objc_stubs: 0xe3a0
+  __TEXT.__objc_methlist: 0x9fcc
   __TEXT.__const: 0x143c
-  __TEXT.__cstring: 0x2325c
-  __TEXT.__oslogstring: 0x20d64
+  __TEXT.__cstring: 0x230f7
+  __TEXT.__oslogstring: 0x20c6a
   __TEXT.__objc_classname: 0x1d7c
-  __TEXT.__objc_methname: 0x1600b
-  __TEXT.__objc_methtype: 0x4e6c
-  __TEXT.__unwind_info: 0x3a80
-  __DATA_CONST.__const: 0x9b48
-  __DATA_CONST.__cfstring: 0x11900
+  __TEXT.__objc_methname: 0x15fb1
+  __TEXT.__objc_methtype: 0x4e60
+  __TEXT.__unwind_info: 0x3a78
+  __DATA_CONST.__const: 0x9b40
+  __DATA_CONST.__cfstring: 0x11800
   __DATA_CONST.__objc_classlist: 0x658
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x390

   __DATA_CONST.__objc_arraydata: 0x1ea0
   __DATA_CONST.__objc_dictobj: 0x1090
   __DATA_CONST.__objc_arrayobj: 0x378
-  __DATA_CONST.__auth_got: 0xd40
-  __DATA_CONST.__got: 0xa18
+  __DATA_CONST.__auth_got: 0xd48
+  __DATA_CONST.__got: 0x9f8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x152a0
-  __DATA.__objc_selrefs: 0x4d08
-  __DATA.__objc_ivar: 0x118c
+  __DATA.__objc_const: 0x152e0
+  __DATA.__objc_selrefs: 0x4d00
+  __DATA.__objc_ivar: 0x1194
   __DATA.__objc_data: 0x3f70
   __DATA.__data: 0x2ba0
   __DATA.__common: 0x18

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4351
-  Symbols:   686
-  CStrings:  11589
+  Functions: 4349
+  Symbols:   683
+  CStrings:  11575
 
Symbols:
+ _NFProductSupportsBackgroundTagRead
+ _OBJC_CLASS_$_NFAutoBugCapture
- _kSymptomDiagnosticKeyPayloadPath
- _kSymptomDiagnosticReplyRateLimitExpiresIn
- _kSymptomDiagnosticReplyReason
- _kSymptomDiagnosticReplyReasonString
- _kSymptomDiagnosticReplySuccess
CStrings:
+ "%{public}s:%i Touch service 0x%llx ready=%d, anyReady=%d"
+ "%{public}s:%i Touch service 0x%llx stopped, available=%d, ready=%d"
+ "%{public}s:%i Touch service not available"
+ "-[NFTouchSensorMonitor _setRemovalHandlerForService:]_block_invoke"
+ "-[NFTouchSensorMonitor _updateReady:forService:]"
+ "@56@0:8@16@24@32Q40@48"
+ "NFCD built from (B&I) Stockholm_Base-372.4.1"
+ "_serviceReadyStates"
+ "_uiVersion"
+ "initWithRemoteObject:workQueue:whitelist:serviceType:sessionConfig:"
+ "initWithVersion:"
+ "requestSnapshotWithType:subType:subTypeContext:detectedProcess:attachments:preferencesDomain:queue:completion:"
+ "serviceID"
+ "supportsBackgroundTagReading"
+ "\xf0Q\x81"
- "%{public}s:%i ABC Request submitted successfully"
- "%{public}s:%i ABC Request was rejected. Reason Code: %ld"
- "%{public}s:%i ABC is prohibited until %{public}@"
- "%{public}s:%i Ignoring ABC callback with no error subtype context."
- "%{public}s:%i Ignoring ABC callback with no error subtype."
- "%{public}s:%i Ignoring ABC callback with no error type."
- "%{public}s:%i Requesting Auto Bug Capture!"
- "%{public}s:%i Touch service stopped"
- "-[NFBugCapture _checkRateLimitForType:subType:]"
- "-[NFBugCapture _sync_requestAutoBugCapture:subType:subTypeContext:attachments:completion:]"
- "-[NFBugCapture _sync_requestAutoBugCapture:subType:subTypeContext:attachments:completion:]_block_invoke"
- "-[NFBugCapture _sync_requestAutoBugCapture:subType:subTypeContext:attachments:completion:]_block_invoke_3"
- "@80@0:8@16@24@32Q40Q48Q56@64B72B76"
- "Invalid subType"
- "Invalid subTypeContext"
- "Invalid type"
- "NFABCProhibitRequestsUntil"
- "NFC/SE"
- "NFCD built from (B&I) Stockholm_Base-371.8"
- "T:%@_S:%@"
- "Time limited"
- "Unknown reason"
- "_checkRateLimitForType:subType:"
- "initWithQueue:"
- "initWithRemoteObject:workQueue:whitelist:serviceType:showSharingUI:coreNFCSessionType:scanText:delayConnectionHandoverRestart:isCNFCDevTestMode:"
- "setIsDevTestMode:"
- "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
- "snapshotWithSignature:delay:events:payload:actions:reply:"
- "\xf0Qa"
```
