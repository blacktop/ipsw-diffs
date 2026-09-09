## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

 360.75.1.2.0
-  __TEXT.__text: 0x252aec
+  __TEXT.__text: 0x254540
   __TEXT.__delay_helper: 0x304
   __TEXT.__lazy_helpers: 0xfc
-  __TEXT.__objc_methlist: 0x8818
-  __TEXT.__cstring: 0x38bac
+  __TEXT.__objc_methlist: 0x88c8
+  __TEXT.__cstring: 0x38f4b
   __TEXT.__const: 0x1d08
   __TEXT.__gcc_except_tab: 0x4eb4
-  __TEXT.__oslogstring: 0x4fced
+  __TEXT.__oslogstring: 0x501a3
   __TEXT.__dlopen_cstrs: 0x613
-  __TEXT.__unwind_info: 0x5f58
+  __TEXT.__unwind_info: 0x5f90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5448
+  __DATA_CONST.__objc_selrefs: 0x54c0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0xf8
-  __DATA_CONST.__got: 0xd08
-  __AUTH_CONST.__const: 0x4968
-  __AUTH_CONST.__cfstring: 0x1bfe0
-  __AUTH_CONST.__objc_const: 0xcec0
+  __DATA_CONST.__got: 0xd10
+  __AUTH_CONST.__const: 0x4988
+  __AUTH_CONST.__cfstring: 0x1c080
+  __AUTH_CONST.__objc_const: 0xcf28
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1d10
   __AUTH.__data: 0x5f0
-  __DATA.__objc_ivar: 0xc70
+  __DATA.__objc_ivar: 0xc78
   __DATA.__data: 0x1410
   __DATA.__common: 0x5d0
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10075
-  Symbols:   15916
-  CStrings:  9867
+  Functions: 10094
+  Symbols:   15951
+  CStrings:  9896
 
Symbols:
+ -[MXCoreSession isAllowedToInterruptSecurePairing]
+ -[MXCoreSessionBase isAllowedToInterruptSecurePairing]
+ -[MXCoreSessionSecure isIsolatedAudioUseCaseIDSecurePairing]
+ -[MXSessionManager(Utilities) copyLocalizedApplicationNameForActiveSessionControllingRouting:]
+ -[MXSessionManager(Utilities) isAnySessionWhichInterruptsSecurePairingActive]
+ -[MXSessionManager(Utilities) showAudioRouteMovedToReceiverBannerForActiveSessionControllingRouting]
+ -[MXSessionManager(Utilities) showAudioRouteMovedToSpeakerBannerForActiveSessionControllingRouting]
+ -[MXSessionManagerSecure handleSecurePairingSessionPreActivation]
+ -[MXSessionManagerSecure interruptSecureSession:interruptorBundleID:interruptorName:fadeDuration:waitingToResume:]
+ -[MXSessionManagerSecure isSecurePairingInProgress]
+ -[MXSessionManagerSecure postInterruptionCommandNotification:interruptionCommand:interruptorName:interruptorBundleID:status:volumeChangeDuration:]
+ -[MXSessionManagerSecure postStopCommandToSecurePairingSession:waitingToResume:]
+ -[MXSessionManagerSecure setIsSecurePairingInProgress:]
+ -[MX_BannerManager showAudioMovedToReceiverBanner:]
+ -[MX_BannerManager showAudioMovedToSpeakerBanner:]
+ GCC_except_table142
+ _MX_FeatureFlags_IsSecurePairingEnabled
+ _MX_FeatureFlags_IsSecurePairingEnabled.onceToken
+ _MX_FeatureFlags_IsSecurePairingEnabled.sIsSecurePairingEnabled
+ _OBJC_IVAR_$_MXCoreSessionBase._isAllowedToInterruptSecurePairing
+ _OBJC_IVAR_$_MXSessionManagerSecure._isSecurePairingInProgress
+ __OBJC_$_PROP_LIST_MXSessionManagerSecure
+ ___146-[MXSessionManagerSecure postInterruptionCommandNotification:interruptionCommand:interruptorName:interruptorBundleID:status:volumeChangeDuration:]_block_invoke
+ ___MX_FeatureFlags_IsSecurePairingEnabled_block_invoke
+ _objc_msgSend$copyLocalizedApplicationNameForActiveSessionControllingRouting:
+ _objc_msgSend$handleSecurePairingSessionPreActivation
+ _objc_msgSend$interruptSecureSession:interruptorBundleID:interruptorName:fadeDuration:waitingToResume:
+ _objc_msgSend$isAllowedToInterruptSecurePairing
+ _objc_msgSend$isAnySessionWhichInterruptsSecurePairingActive
+ _objc_msgSend$isIsolatedAudioUseCaseIDSecurePairing
+ _objc_msgSend$isSecurePairingInProgress
+ _objc_msgSend$postStopCommandToSecurePairingSession:waitingToResume:
+ _objc_msgSend$promptForReceiverEnabledBanner:
+ _objc_msgSend$promptForSpeakerEnabledBanner:
+ _objc_msgSend$setIsSecurePairingInProgress:
+ _objc_msgSend$showAudioMovedToReceiverBanner:
+ _objc_msgSend$showAudioMovedToSpeakerBanner:
+ _objc_msgSend$showAudioRouteMovedToReceiverBannerForActiveSessionControllingRouting
+ _objc_msgSend$showAudioRouteMovedToSpeakerBannerForActiveSessionControllingRouting
- GCC_except_table138
- _OUTLINED_FUNCTION_163
- _OUTLINED_FUNCTION_164
- _OUTLINED_FUNCTION_165
CStrings:
+ "-CMSessionMgr- %s: Skipping  begin interruption for %{public}@ because it is trying to go active during secure airpod pairing"
+ "-MXSessionManagerSecure- %s: INTERRUPTING session '%{public}@' for secure airpod pairing"
+ "-MXSessionManagerSecure- %s: Interrupting secure pairing session for session %{public}@"
+ "-MXSessionManagerSecure- %s: MXSessionManagerSecure with interrupting session %{public}@ INTERRUPTING victim: %{public}@ with audioCategory %{public}@"
+ "-MXSessionManagerSecure- %s: No interruptor session provided!"
+ "-MXSessionManagerSecure- %s: Secure Pairing cannot go active while phone calls/emergency alerts are active"
+ "-MXSessionManagerSecure- %s: Unable to post interruption command for secure audio session"
+ "-MXSessionManagerSecure- %s: isSecurePairingInProgress has changed to %{public}@"
+ "-MXSessionManagerUtilities- %s: Firing moved to receiver banner"
+ "-MXSessionManagerUtilities- %s: Firing moved to speaker banner"
+ "-MXSessionManagerUtilities- %s: Going to show banner for session %{public}@"
+ "-MXSessionManagerUtilities- %s: Nil output param"
+ "-MXSessionManagerUtilities- %s: No active session to show banner for, skipping"
+ "-MX_FeatureFlags- %s: MediaExperience/SecurePairingEnabled feature is %{public}@"
+ "-[MXSessionManager(Utilities) copyLocalizedApplicationNameForActiveSessionControllingRouting:]"
+ "-[MXSessionManager(Utilities) showAudioRouteMovedToReceiverBannerForActiveSessionControllingRouting]"
+ "-[MXSessionManager(Utilities) showAudioRouteMovedToSpeakerBannerForActiveSessionControllingRouting]"
+ "-[MXSessionManagerSecure handleSecurePairingSessionPreActivation]"
+ "-[MXSessionManagerSecure interruptSecureSession:interruptorBundleID:interruptorName:fadeDuration:waitingToResume:]"
+ "-[MXSessionManagerSecure postInterruptionCommandNotification:interruptionCommand:interruptorName:interruptorBundleID:status:volumeChangeDuration:]"
+ "-[MXSessionManagerSecure postStopCommandToSecurePairingSession:waitingToResume:]"
+ "-[MXSessionManagerSecure setIsSecurePairingInProgress:]"
+ "DeviceStateChange"
+ "MXSessionManagerSecure.m"
+ "MX_FeatureFlags_IsSecurePairingEnabled_block_invoke"
+ "SecurePairing"
+ "SecurePairingInput"
+ "SpeakerDriverOutput"
+ "SpeakerValidation"
```
