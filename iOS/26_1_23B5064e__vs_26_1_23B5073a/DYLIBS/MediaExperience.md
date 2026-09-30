## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-300.9.1.0.0
-  __TEXT.__text: 0x1fd814
+300.10.1.1.0
+  __TEXT.__text: 0x1fdb38
   __TEXT.__auth_stubs: 0x1fe0
   __TEXT.__delay_helper: 0x190
-  __TEXT.__objc_methlist: 0x5e94
-  __TEXT.__cstring: 0x2ed05
+  __TEXT.__objc_methlist: 0x5ed4
+  __TEXT.__cstring: 0x2ee77
   __TEXT.__const: 0x1b98
   __TEXT.__gcc_except_tab: 0x2de8
-  __TEXT.__oslogstring: 0x3d2c5
+  __TEXT.__oslogstring: 0x3d36b
   __TEXT.__dlopen_cstrs: 0x5bd
   __TEXT.__unwind_info: 0x4a40
   __TEXT.__objc_classname: 0x75e
-  __TEXT.__objc_methname: 0x15b4b
-  __TEXT.__objc_methtype: 0x20fc
-  __TEXT.__objc_stubs: 0xd580
+  __TEXT.__objc_methname: 0x15cc5
+  __TEXT.__objc_methtype: 0x2107
+  __TEXT.__objc_stubs: 0xd620
   __DATA_CONST.__got: 0xaa0
-  __DATA_CONST.__const: 0x65c8
+  __DATA_CONST.__const: 0x6610
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ba0
+  __DATA_CONST.__objc_selrefs: 0x3bc8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x1008
   __AUTH_CONST.__const: 0x3e40
-  __AUTH_CONST.__cfstring: 0x18ca0
-  __AUTH_CONST.__objc_const: 0x8b30
+  __AUTH_CONST.__cfstring: 0x18d80
+  __AUTH_CONST.__objc_const: 0x8b60
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa00
   __AUTH.__data: 0x570
-  __DATA.__objc_ivar: 0x870
+  __DATA.__objc_ivar: 0x874
   __DATA.__data: 0xfe8
   __DATA.__bss: 0x1819
-  __DATA.__common: 0x4b8
+  __DATA.__common: 0x4a8
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__bss: 0x4d0
   __DATA_DIRTY.__common: 0x60

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7FD82BD5-55EE-36FC-BBA3-A2B37A614772
-  Functions: 6771
-  Symbols:   21542
-  CStrings:  14520
+  UUID: CFFF534A-0BA9-3BD6-A438-3077600303BE
+  Functions: 6776
+  Symbols:   21567
+  CStrings:  14543
 
Symbols:
+ -[MXAudioStatistics sendSingleClearUserPreferredInputMessage:audioRouteName:isInputOverride:]
+ -[MXAudioStatistics sendSingleSetUserPreferredInputMessage:clientInitiator:audioRouteName:]
+ -[MXAudioStatistics sendSingleUserPreferredInputMessage:hostApplicationDisplayID:clientInitiator:audioRouteName:isInputOverride:]
+ -[MXSessionManager currentAllowedPortTypes]
+ -[MXSessionManager setCurrentAllowedPortTypes:]
+ _OBJC_IVAR_$_MXSessionManager._currentAllowedPortTypes
+ ___block_literal_global.118
+ ___block_literal_global.126
+ ___block_literal_global.135
+ ___block_literal_global.138
+ _kMXUserPreferredInputSelectionLog_AudioRouteName
+ _kMXUserPreferredInputSelectionLog_ClearUserPreferredInputEventName
+ _kMXUserPreferredInputSelectionLog_ClientInitiator
+ _kMXUserPreferredInputSelectionLog_HostApplicationDisplayID
+ _kMXUserPreferredInputSelectionLog_IsInputOverride
+ _kMXUserPreferredInputSelectionLog_SelectionType
+ _kMXUserPreferredInputSelectionLog_SelectionType_App
+ _kMXUserPreferredInputSelectionLog_SelectionType_Default
+ _kMXUserPreferredInputSelectionLog_SetUserPreferredInputEventName
+ _objc_msgSend$currentAllowedPortTypes
+ _objc_msgSend$sendSingleClearUserPreferredInputMessage:audioRouteName:isInputOverride:
+ _objc_msgSend$sendSingleSetUserPreferredInputMessage:clientInitiator:audioRouteName:
+ _objc_msgSend$sendSingleUserPreferredInputMessage:hostApplicationDisplayID:clientInitiator:audioRouteName:isInputOverride:
+ _objc_msgSend$setCurrentAllowedPortTypes:
- ___block_literal_global.139
CStrings:
+ "-FigRouteDiscoverer- %s: client: %{public}@ type: %{public}@ userSelectionAvailable: %{BOOL}u isFastDiscoveryEnabled: %{BOOL}u"
+ "-MXAudioStatistics- %s: Sending user preferred input event to audio statistics: %{public}@"
+ "-MXSystemSounds- %s: SSID = %d with systemSoundCategory = %{public}@ supressesAudio = %{BOOL}u suppressesVibe = %{BOOL}u playing to output VAD: %{public}@ returning OutVolume = %f, Audio = %d, Vibration = %d, Synchronized = %d, Interrupt = %d, NeedsDidFinishCall = %d, NeedsUnduckCall = %d, BudgetNotAvailable = %d, PrefersToPlayToHeadphonesOnly = %{BOOL}u"
+ "-[MXAudioStatistics sendSingleUserPreferredInputMessage:hostApplicationDisplayID:clientInitiator:audioRouteName:isInputOverride:]"
+ "08:15:25"
+ "ClientInitiator"
+ "IsInputOverride"
+ "Oct 11 2025"
+ "SelectionType"
+ "SelectionType_App"
+ "SelectionType_Default"
+ "T@\"NSArray\",&,V_currentAllowedPortTypes"
+ "_currentAllowedPortTypes"
+ "com.apple.MediaExperience.UserPreferredInputSelection.ClearUserPreferredInput"
+ "com.apple.MediaExperience.UserPreferredInputSelection.SetUserPreferredInput"
+ "currentAllowedPortTypes"
+ "sendSingleClearUserPreferredInputMessage:audioRouteName:isInputOverride:"
+ "sendSingleSetUserPreferredInputMessage:clientInitiator:audioRouteName:"
+ "sendSingleUserPreferredInputMessage:hostApplicationDisplayID:clientInitiator:audioRouteName:isInputOverride:"
+ "service:account:inviteDroppedForSessionID:fromID:context:error:"
+ "setCurrentAllowedPortTypes:"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "-FigRouteDiscoverer- %s: client: %{public}@ type: %{public}@ userSelectionAvailable: %{BOOL}u"
- "-MXSystemSounds- %s: SSID = %d with systemSoundCategory = %{public}@ supressesAudio = %{BOOL}u suppressesVibe = %{BOOL}u playing to output VAD: %{public}@ returning OutVolume = %f, Audio = %d, Vibration = %d, Synchronized = %d, Interrupt = %d, NeedsDidFinishCall = %d, NeedsUnduckCall = %d, BudgetNotAvailable = %d"
- "22:37:18"
- "Oct  5 2025"
- "service:account:inviteDroppedForSessionID:fromID:error:"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"

```
