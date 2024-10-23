## vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

-825.0.0.0.0
-  __TEXT.__text: 0x7b678
-  __TEXT.__auth_stubs: 0x1410
-  __TEXT.__objc_stubs: 0xa0a0
+831.0.0.0.0
+  __TEXT.__text: 0x7ec0c
+  __TEXT.__auth_stubs: 0x14a0
+  __TEXT.__objc_stubs: 0xa360
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x4cc0
-  __TEXT.__cstring: 0x3b10
-  __TEXT.__objc_classname: 0xaf6
-  __TEXT.__objc_methname: 0xce9a
-  __TEXT.__objc_methtype: 0x2bbd
+  __TEXT.__objc_methlist: 0x4e70
+  __TEXT.__cstring: 0x3d14
+  __TEXT.__objc_classname: 0xb6f
+  __TEXT.__objc_methname: 0xd184
+  __TEXT.__objc_methtype: 0x2c10
   __TEXT.__const: 0x460
-  __TEXT.__gcc_except_tab: 0x8554
-  __TEXT.__oslogstring: 0xc426
-  __TEXT.__unwind_info: 0x26b8
-  __DATA_CONST.__auth_got: 0xa20
-  __DATA_CONST.__got: 0x6f0
+  __TEXT.__gcc_except_tab: 0x8c70
+  __TEXT.__oslogstring: 0xc9e2
+  __TEXT.__unwind_info: 0x2858
+  __DATA_CONST.__auth_got: 0xa68
+  __DATA_CONST.__got: 0x708
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2258
-  __DATA_CONST.__cfstring: 0x4420
-  __DATA_CONST.__objc_classlist: 0x210
+  __DATA_CONST.__const: 0x2340
+  __DATA_CONST.__cfstring: 0x4820
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_intobj: 0x348
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xe5c0
-  __DATA.__objc_selrefs: 0x31a0
-  __DATA.__objc_ivar: 0x508
-  __DATA.__objc_data: 0x14a0
-  __DATA.__data: 0xed0
-  __DATA.__bss: 0x2a0
+  __DATA.__objc_const: 0xe920
+  __DATA.__objc_selrefs: 0x3268
+  __DATA.__objc_ivar: 0x53c
+  __DATA.__objc_data: 0x1540
+  __DATA.__data: 0xf90
+  __DATA.__bss: 0x308
   __DATA.__common: 0x4
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/Speech.framework/Speech
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter

   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
+  - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/VisualVoicemail.framework/IMAP.framework/IMAP
   - /System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2287
-  Symbols:   578
-  CStrings:  4141
+  Functions: 2340
+  Symbols:   590
+  CStrings:  4244
 
Symbols:
+ _CFBooleanGetValue
+ _OBJC_CLASS_$_TUCall
+ _OBJC_CLASS_$_TUCallCenter
+ _SCError
+ _SCErrorString
+ _SCPreferencesCreate
+ _SCPreferencesGetValue
+ _SCPreferencesSetCallback
+ _SCPreferencesSetDispatchQueue
+ _SCPreferencesSynchronize
+ _TUCallCenterCallStatusChangedNotification
+ _asNSStringBOOL
CStrings:
+ "\x11!"
+ "!%!\(MISSING)x113\"+#"
+ "#I %!s(MISSING)%!s(MISSING)%!@(MISSING) %!p(MISSING) Creating"
+ "#I %!s(MISSING)%!s(MISSING)%!@(MISSING) %!p(MISSING) Deleting"
+ "#I %!s(MISSING)%!s(MISSING)%!@(MISSING) Adding observer"
+ "#I %!s(MISSING)%!s(MISSING)%!@(MISSING) Creating TUCallCenter instance"
+ "#I %!s(MISSING)%!s(MISSING)%!@(MISSING) is handling CallStatus changed to %!d(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)%!@(MISSING) is handling RadioPreferencesChanged with info <%!@(MISSING)>"
+ "#I %!s(MISSING)%!s(MISSING)%!@(MISSING) is notifying delegate CallStatus Disconnected for uuid %!@(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)%!@(MISSING) is suppressing notification for %!@(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)-[IMAPService synchronize:force=%!s(MISSING), syncRequired=%!s(MISSING), reason=%!@(MISSING)]"
+ "#I %!s(MISSING)%!s(MISSING)AirplaneMode changed to: %!@(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)AirplaneMode is %!@(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)AirplaneMode is not boolean"
+ "#I %!s(MISSING)%!s(MISSING)AirplaneMode key not found"
+ "#I %!s(MISSING)%!s(MISSING)AirplaneMode preferences session is null"
+ "#I %!s(MISSING)%!s(MISSING)CallStatus Disconnected for uuid %!@(MISSING), delayed sync scheduled %!@(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)Deferring synchronize because delayed sync is scheduled"
+ "#I %!s(MISSING)%!s(MISSING)Sending AirplaneModeChanged to %!l(MISSING)u delegates"
+ "#I %!s(MISSING)%!s(MISSING)Suppressing synchronize"
+ "#I %!s(MISSING)%!s(MISSING)Suppressing synchronize because (syncInProgress:%!s(MISSING) OR accountState:%!@(MISSING) is not kStateActive OR we're offline:%!s(MISSING) OR we have no account:%!@(MISSING))"
+ "#I %!s(MISSING)%!s(MISSING)Unable to create airplane mode preferences session: %!s(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)[%!c(MISSING)] Attempting delayed sync, next iteration %!d(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)[%!c(MISSING)] Delayed sync cancelled, next iteration %!d(MISSING), reason %!@(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)[%!c(MISSING)] Delayed sync is already scheduled, last iteration %!d(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)[%!c(MISSING)] Resetting delayed sync, last iteration %!d(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)[%!c(MISSING)] Scheduling delayed sync in %!u(MISSING) s, iteration %!d(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)[%!c(MISSING)] Set delayed sync retry mode: %!@(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)[%!c(MISSING)] Set delayed sync retry state: %!@(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)[%!c(MISSING)] Set delayed sync scheduled %!@(MISSING), next iteration %!d(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)[%!c(MISSING)] Set single mode: %!@(MISSING)"
+ "#I %!s(MISSING)%!s(MISSING)[%!c(MISSING)] Too many delayed sync retries, giving up;"
+ "#I %!s(MISSING)%!s(MISSING)handleRadioPreferencesCallback [type %!d(MISSING)] received"
+ "#I %!s(MISSING)%!s(MISSING)handleRadioPreferencesCallback: no preference changed"
+ "#W %!s(MISSING)%!s(MISSING)COMPACTION: Unable to transition %!@(MISSING) activity to state continue"
+ "@\"VVMSharedCallStatusObserver\""
+ "@\"VVMSharedPreferencesObserver\""
+ "AirplaneMode"
+ "AuthenticationFailed"
+ "COMPACTION: Unable to transition %!@(MISSING) activity to state continue"
+ "CallDisconnected"
+ "CallEnded"
+ "CallStatusChanged"
+ "Continuous"
+ "Dealloc"
+ "GREETINGCHANGED"
+ "Immediate"
+ "Kill"
+ "MBOXUPDATE"
+ "MWI action"
+ "Not Scheduled"
+ "NotSubscribed"
+ "Scheduled"
+ "SetOnline"
+ "SetSubscribed"
+ "StateActive"
+ "StewieStateChanged"
+ "Sync"
+ "SyncAttempting"
+ "SyncCompleted"
+ "SyncRetryOverCellular"
+ "SyncServices"
+ "UidValidityChanged"
+ "Updating IMAP Account"
+ "VVMCallStatusObserverDelegate"
+ "VVMPreferencesObserverDelegate"
+ "VVMSharedCallStatusObserver"
+ "VVMSharedPreferencesObserver"
+ "^{__SCPreferences=}"
+ "_retryImmediate"
+ "_retryScheduled"
+ "_singleMode"
+ "addSyncTask"
+ "airplane"
+ "apm"
+ "automatedTrashActivityIdentifier"
+ "cancelDelayedSynchronize:"
+ "checkAirplaneModePreference"
+ "com.apple.radios.plist"
+ "com.apple.voicemail.SyncRetry"
+ "com.apple.voicemail:registerForAirplaneModeNotifications"
+ "continuous"
+ "csd"
+ "delayedRetryActivityIdentifier"
+ "delegates"
+ "fPreferencesObserver"
+ "fStatusCallObserver"
+ "fallbackActivityIdentifier"
+ "handleAirplaneModeChanged:"
+ "handleCallStatusChangedNotification:"
+ "handleCallStatusDisconnected:"
+ "handleRadioPreferencesChanged:"
+ "imap.syn"
+ "immediate"
+ "isAirplaneMode"
+ "isDelayedRetryImmediate"
+ "isDelayedRetryScheduled"
+ "isDelayedRetryScheduledGuarded"
+ "isSingleMode"
+ "isTelephonyProvider"
+ "localSenderIdentityUUID"
+ "notifyAirplaneModeChanged_sync:"
+ "notifyCallStatusDisconnected:"
+ "preferences"
+ "provider"
+ "scheduleSyncTask:reason:"
+ "setAirplaneMode:"
+ "setDelayedRetryImmediate:"
+ "setDelayedRetryScheduled:"
+ "setupAirplaneModeCallback"
+ "sharedCallStatusObserver"
+ "sharedPreferencesObserver"
+ "syncCompleted"
+ "synchronize:reason:"
- "!%!\(MISSING)x111\"+#"
- "#I %!s(MISSING)%!s(MISSING)-[IMAPService synchronize:force=%!s(MISSING), syncRequired=%!s(MISSING)]"
- "#I %!s(MISSING)%!s(MISSING)Attempting delayed sync"
- "#I %!s(MISSING)%!s(MISSING)Delayed sync cancelled"
- "#I %!s(MISSING)%!s(MISSING)Scheduling delayed sync in %!u(MISSING) s"
- "#W %!s(MISSING)%!s(MISSING)Too many delayed sync retries, giving up;"
- "#W %!s(MISSING)%!s(MISSING)Unable to transition %!@(MISSING) activity to state continue"
- "Unable to transition %!@(MISSING) activity to state continue"
- "cancelDelayedSynchronize"
- "schedule_synchronize_sync:"
- "synchronize:"

```
