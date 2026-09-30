## DAEAS

> `/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DAEAS`

```diff

-2079.0.1.0.0
-  __TEXT.__text: 0x91cc0
-  __TEXT.__objc_methlist: 0xa5c4
-  __TEXT.__const: 0x700
-  __TEXT.__gcc_except_tab: 0xb70
-  __TEXT.__cstring: 0x93c9
-  __TEXT.__oslogstring: 0x5714
+2079.200.31.0.0
+  __TEXT.__text: 0x929a4
+  __TEXT.__objc_methlist: 0xa684
+  __TEXT.__const: 0x708
+  __TEXT.__gcc_except_tab: 0xc34
+  __TEXT.__cstring: 0x9554
+  __TEXT.__oslogstring: 0x5834
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x24d8
+  __TEXT.__unwind_info: 0x2540
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa80
+  __DATA_CONST.__const: 0xaa8
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4890
+  __DATA_CONST.__objc_selrefs: 0x4908
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__got: 0xb68
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x7480
-  __AUTH_CONST.__objc_const: 0x16a78
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0x75e0
+  __AUTH_CONST.__objc_const: 0x16af8
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2ad0
-  __DATA.__objc_ivar: 0xad0
+  __DATA.__objc_ivar: 0xae0
   __DATA.__data: 0x3df8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 3436
-  Symbols:   7986
-  CStrings:  1845
+  Functions: 3455
+  Symbols:   8029
+  CStrings:  1859
 
Symbols:
+ -[ASAccount _resetServerBackoffStateLocked]
+ -[ASAccount _serverBackoffHeaderDelayForError:]
+ -[ASAccount _serverBackoffHeaderDelayFromUserInfo:]
+ -[ASAccount clearServerBackoff]
+ -[ASAccount isInServerBackoff]
+ -[ASAccount noteServerThrottleFromError:]
+ -[ASAccount noteServerThrottleFromThrottleHeaders:]
+ -[ASAccount recordFanOutReadHoldForWindowUntil:]
+ -[ASAccount recordServerThrottleTelemetryForNewWindow:reason:delaySeconds:until:]
+ -[ASAccount resetServerThrottleFallback]
+ -[ASAccount scheduleServerBackoffDrainAfter:]
+ -[ASAccount serverBackoffUserInfo]
+ -[ASClientAccount recordFanOutReadHoldForWindowUntil:]
+ -[ASFolderItemsSyncTask containsOnlyFanOutReadActions]
+ -[ASItemOperationsFetchAttachmentTask containsOnlyFanOutReadActions]
+ -[ASItemOperationsTask containsOnlyFanOutReadActions]
+ -[ASTask containsOnlyFanOutReadActions]
+ GCC_except_table16
+ GCC_except_table3
+ GCC_except_table42
+ GCC_except_table53
+ OBJC_IVAR_$_ASAccount._serverBackoffAccumulator
+ OBJC_IVAR_$_ASAccount._serverBackoffLastDelay
+ OBJC_IVAR_$_ASAccount._serverBackoffUntil
+ _ASHTTPThrottleBackoffDurationKey
+ _ASHTTPThrottleReasonKey
+ _ASHTTPThrottleRetryAfterKey
+ _ASServerBackoffSecondsKey
+ _ASServerBackoffUntilKey
+ _CalCalendarSetIsAffectingAvailability
+ _OBJC_IVAR_$_ASClientAccount._lastLoggedFanOutReadHoldDeadline
+ ___51-[ASAccount _serverBackoffHeaderDelayFromUserInfo:]_block_invoke
+ __serverBackoffHeaderDelayFromUserInfo:.imfFormatter
+ __serverBackoffHeaderDelayFromUserInfo:.onceToken
+ _objc_msgSend$_resetServerBackoffStateLocked
+ _objc_msgSend$_serverBackoffHeaderDelayFromUserInfo:
+ _objc_msgSend$containsOnlyFanOutReadActions
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$noteServerThrottleFromThrottleHeaders:
+ _objc_msgSend$recordFanOutReadHoldForWindowUntil:
+ _objc_msgSend$recordServerThrottleTelemetryForNewWindow:reason:delaySeconds:until:
+ _objc_msgSend$resetServerThrottleFallback
+ _objc_msgSend$scheduleServerBackoffDrainAfter:
+ _objc_msgSend$serverBackoffUserInfo
+ _objc_msgSend$timeIntervalSince1970
- GCC_except_table59
- GCC_except_table88
CStrings:
+ "#EASTraffic #AccountID: %{public}@ Holding mail Sync until %{public}@; this process is in a server-throttle backoff."
+ "503 for an ungated command while already in a server-throttle backoff (until %@); does not extend the window."
+ "ASHTTPThrottleBackoffDurationKey"
+ "ASHTTPThrottleReasonKey"
+ "ASHTTPThrottleRetryAfterKey"
+ "ASServerBackoffSecondsKey"
+ "ASServerBackoffUntilKey"
+ "Clearing server throttle backoff (was until %@)"
+ "EEE, dd MMM yyyy HH:mm:ss 'GMT'"
+ "Holding fan-out read task %@; account is in a server-throttle backoff."
+ "Retry-After"
+ "Server sent a non-empty Retry-After we couldn't parse as seconds or an HTTP-date (%{public}@); using the backoff fallback."
+ "X-MS-ASThrottle"
+ "X-MS-BackOffDuration"
```
