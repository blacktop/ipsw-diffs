## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA.__common`

```diff

-  __TEXT.__text: 0xa50830
+  __TEXT.__text: 0xa55a2c
   __TEXT.__auth_stubs: 0x6eb0
-  __TEXT.__objc_stubs: 0x492c0
-  __TEXT.__objc_methlist: 0x2b5a4
-  __TEXT.__const: 0x6c6d0
-  __TEXT.__gcc_except_tab: 0x2759c
-  __TEXT.__objc_methname: 0x79845
-  __TEXT.__cstring: 0x57677
-  __TEXT.__oslogstring: 0x814b6
-  __TEXT.__objc_classname: 0x7cbb
-  __TEXT.__objc_methtype: 0x13c8e
-  __TEXT.__ustring: 0x4ca
+  __TEXT.__objc_stubs: 0x496c0
+  __TEXT.__objc_methlist: 0x2b774
+  __TEXT.__const: 0x6c6e0
+  __TEXT.__gcc_except_tab: 0x27a68
+  __TEXT.__objc_methname: 0x79e45
+  __TEXT.__cstring: 0x58097
+  __TEXT.__oslogstring: 0x81c46
+  __TEXT.__objc_classname: 0x7ceb
+  __TEXT.__objc_methtype: 0x13cde
+  __TEXT.__ustring: 0xbbe
   __TEXT.__dlopen_cstrs: 0xea
   __TEXT.__swift5_typeref: 0x8a5c
   __TEXT.__swift5_capture: 0x1fbc

   __TEXT.__swift5_assocty: 0x1388
   __TEXT.__swift5_acfuncs: 0xa0
   __TEXT.__swift5_mpenum: 0x68
-  __TEXT.__unwind_info: 0x16748
+  __TEXT.__unwind_info: 0x16870
   __TEXT.__eh_frame: 0xfc84
   __DATA_CONST.__auth_got: 0x3768
-  __DATA_CONST.__got: 0x4048
+  __DATA_CONST.__got: 0x4060
   __DATA_CONST.__auth_ptr: 0xdc8
-  __DATA_CONST.__const: 0x2f9f8
-  __DATA_CONST.__cfstring: 0x353a0
-  __DATA_CONST.__objc_classlist: 0x1310
+  __DATA_CONST.__const: 0x2fa88
+  __DATA_CONST.__cfstring: 0x360a0
+  __DATA_CONST.__objc_classlist: 0x1318
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x818
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x190
-  __DATA_CONST.__objc_superrefs: 0xbb8
-  __DATA_CONST.__objc_intobj: 0x1ab8
-  __DATA_CONST.__objc_arraydata: 0x5b0
-  __DATA_CONST.__objc_arrayobj: 0x360
+  __DATA_CONST.__objc_superrefs: 0xbc0
+  __DATA_CONST.__objc_intobj: 0x2328
+  __DATA_CONST.__objc_arraydata: 0x870
+  __DATA_CONST.__objc_arrayobj: 0x378
+  __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x4cd60
-  __DATA.__objc_selrefs: 0x16948
-  __DATA.__objc_ivar: 0x33c0
-  __DATA.__objc_data: 0xe170
-  __DATA.__data: 0x130d8
+  __DATA.__objc_const: 0x4cff0
+  __DATA.__objc_selrefs: 0x16a90
+  __DATA.__objc_ivar: 0x33f0
+  __DATA.__objc_data: 0xe1c0
+  __DATA.__data: 0x130e8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1cf88
+  __DATA.__bss: 0x1cfa8
   __DATA.__common: 0xf58
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 29168
-  Symbols:   2848
-  CStrings:  32236
+  Functions: 29213
+  Symbols:   2851
+  CStrings:  32388
 
Symbols:
+ _IDSSilenceIfUnknownKey
+ _OBJC_CLASS_$_IDSSOSLogger
+ _OBJC_CLASS_$_IDSSOSMetric
CStrings:
+ "%@.spam.txt"
+ "23:51:38"
+ "<eja-redacted>"
+ "@\"IDSEnhancedJunkAnalysisController\""
+ "@\"IDSSOSLogger\""
+ "Accept"
+ "Accept (no ship)"
+ "Apple detected a message from a sender who may be trying harm your iPhone or compromise your privacy. The most important step you can take to protect yourself and others from similar attacks is to share the message with Apple.\n\nSender: %@"
+ "Are you sure you don't want to share the message with Apple?"
+ "Cached decision %@ for sender %@"
+ "Captured pending guid %@ (sender=%@, topic=%@, hasPlaintext=%@)"
+ "Don't Report"
+ "Drain complete: %lu guid(s) for sender %@ (decision=%@)"
+ "Drain: cleared %lu pending guid(s) for %@ with decision=%@"
+ "Drain: eja keys       = %@"
+ "Drain: no account for service=%@ toURI=%@ — skipping ship for guid %@"
+ "Drain: nothing pending for sender %@ (decision=%@)"
+ "Drain: remapping adhoc topic %@ -> primary %@ for account lookup"
+ "Drain: shipping %lu top-level key(s) + %lu eja key(s)"
+ "Drain: shipping guid %@ sender=%@ topic=%@ toURI=%@"
+ "Drain: shipping guid %@ sender=%@ topic=%@ toURI=%@ — debug dump at %@"
+ "Drain: top-level keys = %@"
+ "Drain: wireSpam = %@"
+ "Drain: wireSpam.eja = %@"
+ "E7AAB728-60CE-7881-D569-9FF8825F15EA"
+ "EJA"
+ "EJA confirmation alert body"
+ "EJA confirmation alert title"
+ "EJA confirmation-alert destructive button — final dismissal"
+ "EJA first alert body, %@ is the sender URI"
+ "EJA first alert title"
+ "EJA first-alert alternate button — defers the decision"
+ "EJA primary button — shares the message with Apple"
+ "EJADumpSpamToDisk"
+ "EJATestSenders"
+ "Evicting stale sender state for %@ (older than %.0fh)"
+ "Feature disabled by server bag (%@=%@)"
+ "IDS-EJA-KillSwitch"
+ "IDSEnhancedJunkAnalysisController"
+ "IDSEnhancedJunkAnalysisLocalizable"
+ "IMUserNotification creation failed for title=%@"
+ "IMUserNotification response %ld -> result %ld"
+ "Init: seeded deviceLocked=%@ (state is RAM-only, lost on daemon restart)"
+ "Jul  9 2026"
+ "Malicious Message Detected"
+ "Posted SOS eja_alert=YES, eja_alert_count=%lu"
+ "Prompt (confirm): dismissed for %@ — leaving pending; next event will retry"
+ "Prompt (first): dismissed for %@ — leaving pending; next event will retry"
+ "Prompt chain re-armed: %lu fresh sender(s) queued during walk"
+ "Prompt kick skipped — device is locked"
+ "Prompt kick: %lu sender(s) need a decision"
+ "Prompt: already in flight for %@ — skipping"
+ "Report"
+ "Report (ship attempted per record above)"
+ "SOS post succeeded — cleared %lu accumulated alert(s)"
+ "Share with Apple"
+ "Sharing the message will help Apple investigate the attack and protect against future ones."
+ "Skipped capture: at concurrent-sender cap (%lu); dropping guid %@ from sender %@"
+ "Skipped capture: guid %@ already pending for sender %@"
+ "T@\"IDSEnhancedJunkAnalysisController\",R,N,V_enhancedJunkAnalysisController"
+ "T@\"NSMutableDictionary\",&,N,V_senderState"
+ "T@\"NSMutableSet\",&,N,V_inFlightPromptSenders"
+ "TB,N,V_deviceLocked"
+ "TB,N,V_promptChainInFlight"
+ "TQ,N,V_unreportedAlertCount"
+ "Unknown(pending)"
+ "_EJA_forgeSiuIfTestSenderForNiceMessage:topic:"
+ "_EJA_noteIncomingNiceMessage:topLevelPayload:fromURI:service:"
+ "_addPendingForSender:niceMessage:plaintext:"
+ "_cachedDecisionForSender:"
+ "_deviceLocked"
+ "_drainSender:withDecision:"
+ "_enhancedJunkAnalysisController"
+ "_ensureSenderStateLocked_unsafe:"
+ "_evictExpiredEntriesLocked_unsafe"
+ "_hasAnyPendingLocked_unsafe"
+ "_inFlightPromptSenders"
+ "_kickPromptQueueIfNeeded"
+ "_postAlertShownTelemetry"
+ "_promptChainDone"
+ "_promptChainInFlight"
+ "_promptNextWithRemaining:"
+ "_recordDecision:forSender:"
+ "_releasePromptForSender:"
+ "_senderState"
+ "_sendersNeedingPromptLocked_unsafe"
+ "_shipSpamForRecord:sender:"
+ "_sosLogger"
+ "_stateLock"
+ "_tryAcquirePromptForSender:"
+ "_unreportedAlertCount"
+ "arrayForKey:"
+ "conversation-group-size"
+ "conversation-id"
+ "decision"
+ "deviceDidLock"
+ "deviceDidLock — popups suppressed while locked"
+ "deviceDidUnlock"
+ "deviceDidUnlock — hasPending=%@"
+ "deviceLocked"
+ "eja"
+ "eja-spam"
+ "ejaTestSenders"
+ "eja_alert"
+ "eja_alert_count"
+ "enhancedJunkAnalysisController"
+ "firstSeenAt"
+ "forged siu=EnhancedJunkAnalysis for %@ at entry (matched EJATestSenders)"
+ "inFlightPromptSenders"
+ "initWithServiceController:accountController:notificationsCenter:serverBag:sosLogger:initiallyLocked:"
+ "is-informal"
+ "is-payment"
+ "is-self"
+ "isAllowedCommand:"
+ "isFeatureGloballyDisabled"
+ "isFeatureGloballyDisabledForServerBag:"
+ "kill switch engaged (server bag %@) — bypassing siu flow for inbound from %@"
+ "logMetric:completion:"
+ "message-attachment-info"
+ "message-format-version"
+ "message-has-image"
+ "message-length"
+ "message-service"
+ "message-spam-model-detected-spam"
+ "message-text"
+ "message-type"
+ "metricWithDomain:type:error:bagURL:extras:"
+ "niceMessage"
+ "noteIncomingNiceMessage:sender:plaintext:"
+ "originalUUID"
+ "pending"
+ "plaintext"
+ "postAlertWithTitle:body:defaultButton:alternateButton:completion:"
+ "pre-BD decision=%@ for %@"
+ "promptChainInFlight"
+ "q40@0:8@16@24@32"
+ "recipient"
+ "recipient-uri"
+ "reported-from-blackhole"
+ "reported-from-junk"
+ "sender-records-and-keys"
+ "sender-shared-name-and-photo"
+ "senderState"
+ "setDeviceLocked:"
+ "setInFlightPromptSenders:"
+ "setPromptChainInFlight:"
+ "setSenderState:"
+ "setUnreportedAlertCount:"
+ "skipping EJA for %@ — message is from self"
+ "skipping EJA for %@ — service %@ blocks cross-account"
+ "skipping EJA — command %@ not in allowlist"
+ "time-sensitive"
+ "time-sensitive-evaluated"
+ "unreportedAlertCount"
- "00:03:02"
- "Jun 27 2026"
```
