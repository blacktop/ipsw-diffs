# 26.0 (23A5330a) .vs 26.0 (23A5336a)

## IPSWs

- `iPhone17,1_26.0_23A5330a_Restore.ipsw`
- `iPhone17,1_26.0_23A5336a_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.0 *(23A5330a)* | 25.0.0 | 12377.2.7~9 | Fri, 15Aug2025 00:02:28 PDT |
| 26.0 *(23A5336a)* | 25.0.0 | 12377.2.8~3 | Wed, 27Aug2025 20:44:56 PDT |

### Kexts

### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.driver.IOPAudioVoiceTriggerDevice

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 500.14.0.0.0
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x2d89
+  __TEXT.__cstring: 0x2d80
   __TEXT.__os_log: 0x1726
   __TEXT_EXEC.__text: 0xb108
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1750
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: 6FB89CDF-02C5-38E4-BD1E-A44C2ED998B6
+  UUID: 6A290BF8-28B3-3AC5-ADC9-774A0B6F79D5
   Functions: 260
   Symbols:   0
-  CStrings:  236
+  CStrings:  235
 
CStrings:
+ "21:48:15"
+ "Aug 27 2025"
- "00:33:05"
- "00:33:06"
- "Aug 15 2025"

```

#### com.apple.filesystems.apfs

>  `com.apple.filesystems.apfs`

```diff

 2632.2.1.0.0
   __TEXT.__const: 0xa18
-  __TEXT.__cstring: 0x4c59f
+  __TEXT.__cstring: 0x4c596
   __TEXT_EXEC.__text: 0x159a78
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x640

   __DATA_CONST.__kalloc_type: 0x4f00
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: 3E2A9BDF-4573-30D8-94D2-F12FDDCC422F
+  UUID: 494A08C1-B505-3770-8218-795A852075A0
   Functions: 2319
   Symbols:   0
-  CStrings:  6590
+  CStrings:  6589
 
CStrings:
+ "19:55:34"
+ "2025/08/27"
+ "Aug 27 2025"
- "2025/08/14"
- "23:44:47"
- "23:44:48"
- "Aug 14 2025"

```

#### com.apple.iokit.IOSurface

>  `com.apple.iokit.IOSurface`

```diff

-392.4.0.0.0
-  __TEXT.__cstring: 0x2e1b
+392.5.0.0.0
+  __TEXT.__cstring: 0x2e23
   __TEXT.__const: 0x40
   __TEXT.__os_log: 0x2f92
-  __TEXT_EXEC.__text: 0x31794
+  __TEXT_EXEC.__text: 0x3181c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x178
   __DATA.__common: 0x410

   __DATA_CONST.__const: 0x42f8
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0x960
-  UUID: A551A978-6B6C-363B-99D7-B8EDEFFFD9F9
-  Functions: 1245
+  UUID: 76A357D5-0013-32B4-9421-A8BDAC320273
+  Functions: 1246
   Symbols:   0
   CStrings:  574
 
CStrings:
+ "1211112112"
+ "121111211211111111"
+ "bool IOSurfaceSharedEventListener::init(thread_call_priority_t, IOWorkLoop *, bool)"
- "121111211"
- "12111121111111111"
- "bool IOSurfaceSharedEventListener::init(thread_call_priority_t, IOWorkLoop *)"

```

#### com.apple.kernel

>  `com.apple.kernel`

```diff

-12377.2.7.0.0
+12377.2.8.0.0
   __TEXT.__const: 0x34bd0
   __TEXT.__copyio_vectors: 0xf0
   __TEXT.__cstring: 0x7d891

   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x891384
+  __TEXT_EXEC.__text: 0x891388
   __TEXT_EXEC.__hib_text: 0xe38
   __TEXT_BOOT_EXEC.__bootcode: 0x523c
   __KLD.__text: 0x1818

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x470ee
-  UUID: FA9DEF6D-C5EA-3B39-A543-D24C3AF2E771
+  UUID: 852769BC-1BAC-3A6E-98F6-DEC7223D4513
   Functions: 20637
   Symbols:   0
   CStrings:  19956
Functions:
~ _namei : 3720 -> 3724
~ sub_fffffff008a592b4 -> sub_fffffff008a592b8 : 236 -> 232

```

#### com.apple.security.AppleImage4

>  `com.apple.security.AppleImage4`

```diff

 349.2.1.0.0
   __TEXT.__const: 0x9daf
-  __TEXT.__cstring: 0x5fbe
+  __TEXT.__cstring: 0x5fc0
   __TEXT_EXEC.__text: 0x23930
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x8b8

   __DATA_CONST.__const: 0xb9b8
   __DATA_CONST.__kalloc_type: 0x200
   __DATA_CONST.__image4_exp: 0x10
-  UUID: 742EAE55-96BF-3F6B-B546-DFD47C2E556A
+  UUID: 1F5CBA91-B0AE-342B-8548-EB1D17F05C12
   Functions: 1120
   Symbols:   0
   CStrings:  825
CStrings:
+ "@(#)VERSION:Darwin Image4 Extension Version 7.0.0: Wed Aug 27 19:59:22 PDT 2025; root:AppleImage4-349.2.1~119/AppleImage4/RELEASE_ARM64E"
+ "Darwin Image4 Extension Version 7.0.0: Wed Aug 27 19:59:22 PDT 2025; root:AppleImage4-349.2.1~119/AppleImage4/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Image4 Extension Version 7.0.0: Thu Aug 14 23:43:10 PDT 2025; root:AppleImage4-349.2.1~86/AppleImage4/RELEASE_ARM64E"
- "Darwin Image4 Extension Version 7.0.0: Thu Aug 14 23:43:10 PDT 2025; root:AppleImage4-349.2.1~86/AppleImage4/RELEASE_ARM64E"

```


</details>

## MachO

### ⬆️ Updated (603)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AMSUIAuthenticationViewService.app/AMSUIAuthenticationViewService](MACHOS/AMSUIAuthenticationViewService.md)
- [/Applications/AVKitRoutingService.app/AVKitRoutingService](MACHOS/AVKitRoutingService.md)
- [/Applications/AccessibilityReader_iOS.app/AccessibilityReader_iOS](MACHOS/AccessibilityReader_iOS.md)
- [/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension](MACHOS/ActivityMessagesExtension.md)
- [/Applications/ActivityProgressUI.app/ActivityProgressUI](MACHOS/ActivityProgressUI.md)
- [/Applications/AdaptiveMusicApp.app/AdaptiveMusicApp](MACHOS/AdaptiveMusicApp.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AirPlay Receiver.app/AirPlay Receiver](MACHOS/AirPlay_Receiver.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService](MACHOS/AppleIDSetupUIService.md)
- [/Applications/CameraOverlayAngel.app/CameraOverlayAngel](MACHOS/CameraOverlayAngel.md)
- [/Applications/CarPlaySettings.app/CarPlaySettings](MACHOS/CarPlaySettings.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/ClarityPhotos.app/ClarityPhotos](MACHOS/ClarityPhotos.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/DKPairingUIService.app/DKPairingUIService](MACHOS/DKPairingUIService.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6009.appex/Diagnostic-6009](MACHOS/Diagnostic-6009.md)
- [/Applications/DockFolderViewService.app/DockFolderViewService](MACHOS/DockFolderViewService.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FTMInternal.app/FTMInternal](MACHOS/FTMInternal.md)
- [/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/Applications/FamilyExtensionHost.app/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension](MACHOS/FamilyOutOfProcessUIExtension.md)
- [/Applications/FamilyExtensionHost.app/FamilyExtensionHost](MACHOS/FamilyExtensionHost.md)
- [/Applications/FinanceUIService.app/FinanceUIService](MACHOS/FinanceUIService.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GuestUserHandoverSetup.app/GuestUserHandoverSetup](MACHOS/GuestUserHandoverSetup.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/HomeUIService.app/HomeUIService](MACHOS/HomeUIService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/LimitedAccessPromptView.app/LimitedAccessPromptView](MACHOS/LimitedAccessPromptView.md)
- [/Applications/LocalAuthenticationUIService.app/LocalAuthenticationUIService](MACHOS/LocalAuthenticationUIService.md)
- [/Applications/MagnifierAngel.app/MagnifierAngel](MACHOS/MagnifierAngel.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/NFCUISceneService.app/NFCUISceneService](MACHOS/NFCUISceneService.md)
- [/Applications/NetworkEndpointPickerUI.app/NetworkEndpointPickerUI](MACHOS/NetworkEndpointPickerUI.md)
- [/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService](MACHOS/NewDeviceSetupUIService.md)
- [/Applications/PASViewService.app/PASViewService](MACHOS/PASViewService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PeopleMessageService.app/Extensions/PeopleLegacyMessageService.appex/PeopleLegacyMessageService](MACHOS/PeopleLegacyMessageService.md)
- [/Applications/PeopleMessageService.app/PeopleMessageService](MACHOS/PeopleMessageService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy](MACHOS/PeopleMessagesAskToBuy.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PeopleViewService](MACHOS/PeopleViewService.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/PosterBoard.app/XPCServices/PosterPlatformSupportBundleService.xpc/PosterPlatformSupportBundleService](MACHOS/PosterPlatformSupportBundleService.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/ProductKitViewer.app/ProductKitViewer](MACHOS/ProductKitViewer.md)
- [/Applications/ProximityReaderSceneUI.app/ProximityReaderSceneUI](MACHOS/ProximityReaderSceneUI.md)
- [/Applications/ReplayKitAngel.app/ReplayKitAngel](MACHOS/ReplayKitAngel.md)
- [/Applications/SESUIServiceApp.app/SESUIServiceApp](MACHOS/SESUIServiceApp.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/ScreenContinuityShell.app/ScreenContinuityShell](MACHOS/ScreenContinuityShell.md)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/SleepLockScreen.app/SleepLockScreen](MACHOS/SleepLockScreen.md)
- [/Applications/StickerPickerService.app/StickerPickerService](MACHOS/StickerPickerService.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/StoreKitUISceneService.app/StoreKitUISceneService](MACHOS/StoreKitUISceneService.md)
- [/Applications/SupportFlow.app/SupportFlow](MACHOS/SupportFlow.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/TVRemoteUIService.app/TVRemoteUIService](MACHOS/TVRemoteUIService.md)
- [/Applications/TVSetupUIService.app/TVSetupUIService](MACHOS/TVSetupUIService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension](MACHOS/InviteMessageBubbleExtension.md)
- [/System/Library/AccessibilityBundles/AXGuestPassServer.axuiservice/AXGuestPassServer](MACHOS/AXGuestPassServer.md)
- [/System/Library/AccessibilityBundles/AXHapticMusicServer.axuiservice/AXHapticMusicServer](MACHOS/AXHapticMusicServer.md)
- [/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer](MACHOS/AXMotionCuesServer.md)
- [/System/Library/AccessibilityBundles/BrailleUI.axuiservice/BrailleUI](MACHOS/BrailleUI.md)
- [/System/Library/AccessibilityBundles/ClarityUIServer.axuiservice/ClarityUIServer](MACHOS/ClarityUIServer.md)
- [/System/Library/AccessibilityBundles/HoverTextUIServer.axuiservice/HoverTextUIServer](MACHOS/HoverTextUIServer.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/SpeakThis.axuiservice/SpeakThis](MACHOS/SpeakThis.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/Accounts/Authentication/GameCenterAccountAuthenticationPlugin.bundle/GameCenterAccountAuthenticationPlugin](MACHOS/GameCenterAccountAuthenticationPlugin.md)
- [/System/Library/Accounts/DataclassOwners/DeviceEnrollmentDataClassPlugIn.bundle/DeviceEnrollmentDataClassPlugIn](MACHOS/DeviceEnrollmentDataClassPlugIn.md)
- [/System/Library/Accounts/DataclassOwners/FreeformDataclassOwner.bundle/FreeformDataclassOwner](MACHOS/FreeformDataclassOwner.md)
- [/System/Library/Accounts/Notification/ASDAccountNotificationPlugin.bundle/ASDAccountNotificationPlugin](MACHOS/ASDAccountNotificationPlugin.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppRemovalServices/com.apple.weather.appremoval.xpc/com.apple.weather.appremoval](MACHOS/com.apple.weather.appremoval.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/CoreDynamicUIPlugin.bundle/CoreDynamicUIPlugin](MACHOS/CoreDynamicUIPlugin.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CAMRootFlowPlugin.bundle/CAMRootFlowPlugin](MACHOS/CAMRootFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/GeoFlowDelegatePlugin.bundle/GeoFlowDelegatePlugin](MACHOS/GeoFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin](MACHOS/HomeCommunicationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin](MACHOS/IFFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/InformationFlowPlugin.bundle/InformationFlowPlugin](MACHOS/InformationFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriSuggestionsFlowPlugin.bundle/SiriSuggestionsFlowPlugin](MACHOS/SiriSuggestionsFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/Applications.assistantBundle/Applications](MACHOS/Applications.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningPatternExtractionPlugin.bundle/SiriPrivateLearningPatternExtractionPlugin](MACHOS/SiriPrivateLearningPatternExtractionPlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/Suggestions/InferenceBridge/SiriSuggestionsInferenceBridge.bundle/SiriSuggestionsInferenceBridge](MACHOS/SiriSuggestionsInferenceBridge.md)
- [/System/Library/Assistant/Suggestions/SKEBridge/SiriSuggestionsSKEBridge.bundle/SiriSuggestionsSKEBridge](MACHOS/SiriSuggestionsSKEBridge.md)
- [/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod](MACHOS/usbaudiod.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/AegirProxyApp.app/PlugIns/AegirPoster.appex/AegirPoster](MACHOS/AegirPoster.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/System/Library/CoreServices/MusicKitUI.app/MusicKitUI](MACHOS/MusicKitUI.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/CoreServices/appplaceholdersyncd](MACHOS/appplaceholdersyncd.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess](MACHOS/RestorePostProcess.md)
- [/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator](MACHOS/SystemAppMigrator.md)
- [/System/Library/DigitalSeparation/SharingSources/ActivityDigitalSeparation.bundle/ActivityDigitalSeparation](MACHOS/ActivityDigitalSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/DSNotesPlugin.bundle/DSNotesPlugin](MACHOS/DSNotesPlugin.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMyItemsDigitalSeparation.bundle/FindMyItemsDigitalSeparation](MACHOS/FindMyItemsDigitalSeparation.md)
- [/System/Library/DigitalSeparation/SharingSources/FindMyPeopleDigitalSeparation.bundle/FindMyPeopleDigitalSeparation](MACHOS/FindMyPeopleDigitalSeparation.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/ASRFullPayloadCorrection.appex/ASRFullPayloadCorrection](MACHOS/ASRFullPayloadCorrection.md)
- [/System/Library/ExtensionKit/Extensions/AdAttributionKitEngagementExtension.appex/AdAttributionKitEngagementExtension](MACHOS/AdAttributionKitEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider](MACHOS/AmbientPhotoFramePosterProvider.md)
- [/System/Library/ExtensionKit/Extensions/AvatarPosterExtension.appex/AvatarPosterExtension](MACHOS/AvatarPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/ChallengesMessageExtension.appex/ChallengesMessageExtension](MACHOS/ChallengesMessageExtension.md)
- [/System/Library/ExtensionKit/Extensions/ClockPosterExtension.appex/ClockPosterExtension](MACHOS/ClockPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/CloudWorker.appex/CloudWorker](MACHOS/CloudWorker.md)
- [/System/Library/ExtensionKit/Extensions/CollectionsPoster.appex/CollectionsPoster](MACHOS/CollectionsPoster.md)
- [/System/Library/ExtensionKit/Extensions/CustomRingtoneAction.appex/CustomRingtoneAction](MACHOS/CustomRingtoneAction.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/DynamicBackgroundPosterExtension.appex/DynamicBackgroundPosterExtension](MACHOS/DynamicBackgroundPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/EmojiPosterExtension.appex/EmojiPosterExtension](MACHOS/EmojiPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension](MACHOS/FamilyOutOfProcessUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension](MACHOS/GPUIExtension.md)
- [/System/Library/ExtensionKit/Extensions/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/ExtensionKit/Extensions/GradientBackgroundPosterExtension.appex/GradientBackgroundPosterExtension](MACHOS/GradientBackgroundPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/HostInferenceProviderService.appex/HostInferenceProviderService](MACHOS/HostInferenceProviderService.md)
- [/System/Library/ExtensionKit/Extensions/IFTelemetrySELFIngestor.appex/IFTelemetrySELFIngestor](MACHOS/IFTelemetrySELFIngestor.md)
- [/System/Library/ExtensionKit/Extensions/InferenceProviderService.appex/InferenceProviderService](MACHOS/InferenceProviderService.md)
- [/System/Library/ExtensionKit/Extensions/MediaMLExtension.appex/MediaMLExtension](MACHOS/MediaMLExtension.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/Space.metallib](MACHOS/Space.metallib.md)
- [/System/Library/ExtensionKit/Extensions/MessagesAnalyticsWorker.appex/MessagesAnalyticsWorker](MACHOS/MessagesAnalyticsWorker.md)
- [/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension](MACHOS/MusicEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/MusicUIEngagementExtension.appex/MusicUIEngagementExtension](MACHOS/MusicUIEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/PhotosEngagementExtension.appex/PhotosEngagementExtension](MACHOS/PhotosEngagementExtension.md)
- [/System/Library/ExtensionKit/Extensions/PhotosPosterProvider.appex/PhotosPosterProvider](MACHOS/PhotosPosterProvider.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/SafariAssistantWorker.appex/SafariAssistantWorker](MACHOS/SafariAssistantWorker.md)
- [/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin](MACHOS/SiriSuggestionsLightHousePlugin.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/ExtensionKit/Extensions/TVAppExtension.appex/TVAppExtension](MACHOS/TVAppExtension.md)
- [/System/Library/ExtensionKit/Extensions/TetsuoDiagnosticExtension.appex/TetsuoDiagnosticExtension](MACHOS/TetsuoDiagnosticExtension.md)
- [/System/Library/ExtensionKit/Extensions/TranslationAPIExtension.appex/TranslationAPIExtension](MACHOS/TranslationAPIExtension.md)
- [/System/Library/ExtensionKit/Extensions/TranslationAPISupportExtension.appex/TranslationAPISupportExtension](MACHOS/TranslationAPISupportExtension.md)
- [/System/Library/ExtensionKit/Extensions/Unity2025Poster.appex/Unity2025Poster](MACHOS/Unity2025Poster.md)
- [/System/Library/ExtensionKit/Extensions/VisualIntelligenceCameraAnalytics.appex/VisualIntelligenceCameraAnalytics](MACHOS/VisualIntelligenceCameraAnalytics.md)
- [/System/Library/ExtensionKit/Extensions/WritingToolsAppIntentsExtension.appex/WritingToolsAppIntentsExtension](MACHOS/WritingToolsAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/ZeoliteEvalExtension](MACHOS/ZeoliteEvalExtension.md)
- [/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd](MACHOS/attributionkitd.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/XPCServices/BrowserEngineKit.Intermediary.xpc/BrowserEngineKit.Intermediary](MACHOS/BrowserEngineKit.Intermediary.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/Contacts.framework/Support/contactsd](MACHOS/contactsd.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/MonogramPosterExtension.appex/MonogramPosterExtension](MACHOS/MonogramPosterExtension.md)
- [/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService](MACHOS/ContactsButtonXPCService.md)
- [/System/Library/Frameworks/CoreImage.framework/photo_style_archive_bin.metallib](MACHOS/photo_style_archive_bin.metallib.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/ImageIO.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/MusicKit.framework/Support/musicd](MACHOS/musicd.md)
- [/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension](MACHOS/ScreenTimeWebExtension.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition](MACHOS/localspeechrecognition.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/SystemConfiguration.framework/get-network-info](MACHOS/get-network-info.md)
- [/System/Library/Frameworks/TelephonyMessagingKit.framework/XPCServices/TelephonyTransferService.xpc/TelephonyTransferService](MACHOS/TelephonyTransferService.md)
- [/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd](MACHOS/wirelessinsightsd.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
- [/System/Library/HIDPlugins/ServiceFilters/HIDSensorTimeFilter.plugin/HIDSensorTimeFilter](MACHOS/HIDSensorTimeFilter.md)
- [/System/Library/Health/DiagnosticExtensionPlugins/HealthAppDiagnosticExtensionPlugin.bundle/HealthAppDiagnosticExtensionPlugin](MACHOS/HealthAppDiagnosticExtensionPlugin.md)
- [/System/Library/Health/DiagnosticExtensionPlugins/HealthTopicsDiagnosticExtensionPlugin.bundle/HealthTopicsDiagnosticExtensionPlugin](MACHOS/HealthTopicsDiagnosticExtensionPlugin.md)
- [/System/Library/Health/FeedItemPlugins/HealthBalanceAppPluginBundle.healthplugin/HealthBalanceAppPluginBundle](MACHOS/HealthBalanceAppPluginBundle.md)
- [/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin](MACHOS/HealthRecordsPlugin.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/PlugIns/iMessageLite.imservice/iMessageLite](MACHOS/iMessageLite.md)
- [/System/Library/Messages/iMessageApps/AskToMessages.bundle/AskToMessages](MACHOS/AskToMessages.md)
- [/System/Library/Messages/iMessageApps/FindMyMessagesApp.bundle/FindMyMessagesApp](MACHOS/FindMyMessagesApp.md)
- [/System/Library/Messages/iMessageApps/MessagesPolls.bundle/MessagesPolls](MACHOS/MessagesPolls.md)
- [/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages](MACHOS/SafetyMonitorMessages.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/Messages/iMessageBalloons/MSMessageExtensionBalloonPlugin.bundle/MSMessageExtensionBalloonPlugin](MACHOS/MSMessageExtensionBalloonPlugin.md)
- [/System/Library/NanoPreferenceBundles/Applications/BridgeAppStoreDaemonSettings.bundle/BridgeAppStoreDaemonSettings](MACHOS/BridgeAppStoreDaemonSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/NanoMenstrualCyclesCompanionSettings.bundle/NanoMenstrualCyclesCompanionSettings](MACHOS/NanoMenstrualCyclesCompanionSettings.md)
- [/System/Library/NanoPreferenceBundles/Applications/UrchinBridgeSettings.bundle/UrchinBridgeSettings](MACHOS/UrchinBridgeSettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/MindComplicationBundleCompanion.bundle/MindComplicationBundleCompanion](MACHOS/MindComplicationBundleCompanion.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.finddevices.complications.bundle/com.apple.finddevices.complications](MACHOS/com.apple.finddevices.complications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.finditems.complications.bundle/com.apple.finditems.complications](MACHOS/com.apple.finditems.complications.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/com.apple.findpeople.complications.bundle/com.apple.findpeople.complications](MACHOS/com.apple.findpeople.complications.md)
- [/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings](MACHOS/AccessibilitySettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/ActionButtonSettings.bundle/ActionButtonSettings](MACHOS/ActionButtonSettings.md)
- [/System/Library/PreferenceBundles/AdAttributionKitDeveloperSettings.bundle/AdAttributionKitDeveloperSettings](MACHOS/AdAttributionKitDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/AirPlayAndHandoffSettings](MACHOS/AirPlayAndHandoffSettings.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/BackgroundAppRefresh.bundle/BackgroundAppRefresh](MACHOS/BackgroundAppRefresh.md)
- [/System/Library/PreferenceBundles/BatteryUsageUI.bundle/BatteryUsageUI](MACHOS/BatteryUsageUI.md)
- [/System/Library/PreferenceBundles/BlocklistSettings.bundle/BlocklistSettings](MACHOS/BlocklistSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/ClarityUIMusicSettings.bundle/ClarityUIMusicSettings](MACHOS/ClarityUIMusicSettings.md)
- [/System/Library/PreferenceBundles/Content Caches.bundle/Content Caches](MACHOS/Content_Caches.md)
- [/System/Library/PreferenceBundles/DeveloperSettings.bundle/DeveloperSettings](MACHOS/DeveloperSettings.md)
- [/System/Library/PreferenceBundles/DeviceEnrollments.bundle/DeviceEnrollments](MACHOS/DeviceEnrollments.md)
- [/System/Library/PreferenceBundles/FontSettings.bundle/FontSettings](MACHOS/FontSettings.md)
- [/System/Library/PreferenceBundles/ICSSettingsBundle.bundle/ICSSettingsBundle](MACHOS/ICSSettingsBundle.md)
- [/System/Library/PreferenceBundles/JournalNotifications.bundle/JournalNotifications](MACHOS/JournalNotifications.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/LegalAndRegulatorySettings.bundle/LegalAndRegulatorySettings](MACHOS/LegalAndRegulatorySettings.md)
- [/System/Library/PreferenceBundles/ManagedConfigurationUI.bundle/ManagedConfigurationUI](MACHOS/ManagedConfigurationUI.md)
- [/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings](MACHOS/MobileStoreSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/NewsSettings.bundle/NewsSettings](MACHOS/NewsSettings.md)
- [/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings](MACHOS/NotificationsSettings.md)
- [/System/Library/PreferenceBundles/PasscodeAndBiometricsSettingsPref.bundle/PasscodeAndBiometricsSettingsPref](MACHOS/PasscodeAndBiometricsSettingsPref.md)
- [/System/Library/PreferenceBundles/PaymentContactlessSettingsUIPlugin.bundle/PaymentContactlessSettingsUIPlugin](MACHOS/PaymentContactlessSettingsUIPlugin.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/RemindersSettings.bundle/RemindersSettings](MACHOS/RemindersSettings.md)
- [/System/Library/PreferenceBundles/SOSSettings.bundle/SOSSettings](MACHOS/SOSSettings.md)
- [/System/Library/PreferenceBundles/ScreenshotServicesSettings.bundle/ScreenshotServicesSettings](MACHOS/ScreenshotServicesSettings.md)
- [/System/Library/PreferenceBundles/SiriMessagesSettings.bundle/SiriMessagesSettings](MACHOS/SiriMessagesSettings.md)
- [/System/Library/PreferenceBundles/SoftwareUpdateUIMobileSettingsPlugin.bundle/SoftwareUpdateUIMobileSettingsPlugin](MACHOS/SoftwareUpdateUIMobileSettingsPlugin.md)
- [/System/Library/PreferenceBundles/StoragePlugins/PodcastsUsagePlugin.bundle/PodcastsUsagePlugin](MACHOS/PodcastsUsagePlugin.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/TetsuoNotifications.bundle/TetsuoNotifications](MACHOS/TetsuoNotifications.md)
- [/System/Library/PreferenceBundles/WISDeveloperSettings.bundle/WISDeveloperSettings](MACHOS/WISDeveloperSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PreferenceBundles/WeatherSettings.bundle/WeatherSettings](MACHOS/WeatherSettings.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/deflicker-binary-applegpu_g17p.metallib](MACHOS/deflicker-binary-applegpu_g17p.metallib.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/deflicker-binary.metallib](MACHOS/deflicker-binary.metallib.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/axassetsd](MACHOS/axassetsd.md)
- [/System/Library/PrivateFrameworks/AccountsUISupport.framework/XPCServices/AccountsUISupportService.xpc/AccountsUISupportService](MACHOS/AccountsUISupportService.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/activityawardsd](MACHOS/activityawardsd.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/activitysharingd](MACHOS/activitysharingd.md)
- [/System/Library/PrivateFrameworks/AnnounceSiriExtensions.framework/PlugIns/AnnounceIntentExtension.appex/AnnounceIntentExtension](MACHOS/AnnounceIntentExtension.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/CustodianInviteMessageExtension.appex/CustodianInviteMessageExtension](MACHOS/CustodianInviteMessageExtension.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/LegacyContactMessageExtention.appex/LegacyContactMessageExtention](MACHOS/LegacyContactMessageExtention.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetThumbnail.appex/ASVAssetThumbnail](MACHOS/ASVAssetThumbnail.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AutomationMode.framework/automationmode-writer](MACHOS/automationmode-writer.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd](MACHOS/businessservicesd.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/BWPreviewStitcherNodeCoreImageArchive_bin.metallib](MACHOS/BWPreviewStitcherNodeCoreImageArchive_bin.metallib.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper](MACHOS/CallHistorySyncHelper.md)
- [/System/Library/PrivateFrameworks/CallIntelligence.framework/callintelligenced](MACHOS/callintelligenced.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/PlugIns/ClockPosterExtension.appex/ClockPosterExtension](MACHOS/ClockPosterExtension.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd](MACHOS/cloudd.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/CreateiCloudLinkExtension.appex/CreateiCloudLinkExtension](MACHOS/CreateiCloudLinkExtension.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants](MACHOS/com.apple.CloudSharingUI.AddParticipants.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/PlugIns/CSFFollowUpExtension.appex/CSFFollowUpExtension](MACHOS/CSFFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent](MACHOS/CMFSyncAgent.md)
- [/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent](MACHOS/analyticsagent.md)
- [/System/Library/PrivateFrameworks/CoreMLOdie.framework/XPCServices/CoreMLSegmenter.xpc/CoreMLSegmenter](MACHOS/CoreMLSegmenter.md)
- [/System/Library/PrivateFrameworks/CoreMLOdie.framework/XPCServices/E5MLCompiler.xpc/E5MLCompiler](MACHOS/E5MLCompiler.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CorePrescription.framework/XPCServices/CorePrescriptionService.xpc/CorePrescriptionService](MACHOS/CorePrescriptionService.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/default-binaryarchive.metallib](MACHOS/default-binaryarchive.metallib.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/mxi-binaryarchive.metallib](MACHOS/mxi-binaryarchive.metallib.md)
- [/System/Library/PrivateFrameworks/CoreRE3DGSFoundation.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity](MACHOS/com.apple.dt.instruments.dtsecurity.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IMDiagnosticExtension.appex/IMDiagnosticExtension](MACHOS/IMDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/PlugIns/DockKitExtension.appex/DockKitExtension](MACHOS/DockKitExtension.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EnergyKitInternal.framework/XPCServices/EnergyKitService.xpc/EnergyKitService](MACHOS/EnergyKitService.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled](MACHOS/familycircled.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/finhealthd](MACHOS/finhealthd.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService](MACHOS/FindMyDeviceSharedConfigurationXPCService.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/fitnesscoachingd](MACHOS/fitnesscoachingd.md)
- [/System/Library/PrivateFrameworks/FitnessIntelligenceDaemonCore.framework/fitnessintelligenced](MACHOS/fitnessintelligenced.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/PlugIns/HealthBalanceDiagnosticExtension.appex/HealthBalanceDiagnosticExtension](MACHOS/HealthBalanceDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/PlugIns/HealthMedicationsNotificationContentExtension.appex/HealthMedicationsNotificationContentExtension](MACHOS/HealthMedicationsNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd](MACHOS/healthappd.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/PlugIns/HomeKitEventsDiagnosticExtension.appex/HomeKitEventsDiagnosticExtension](MACHOS/HomeKitEventsDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/Support/homeeventsd](MACHOS/homeeventsd.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/Support/jetpackassetd](MACHOS/jetpackassetd.md)
- [/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded](MACHOS/lockdownmoded.md)
- [/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Helper Service.xpc/Managed Background Assets Helper Service](MACHOS/Managed_Background_Assets_Helper_Service.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd](MACHOS/destinationd.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd](MACHOS/mapssyncd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService](MACHOS/MediaAnalysisBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisGeneration.framework/XPCServices/mediaanalysisd-generation.xpc/mediaanalysisd-generation](MACHOS/mediaanalysisd-generation.md)
- [/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService](MACHOS/com.apple.photos.ImageConversionService.md)
- [/System/Library/PrivateFrameworks/MediaMLServices.framework/XPCServices/mediamlxpc.xpc/mediamlxpc](MACHOS/mediamlxpc.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/HubbleBlastDoorService.xpc/HubbleBlastDoorService](MACHOS/HubbleBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd](MACHOS/migrationd.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/XPCServices/MIBULoopbackServerHelper.xpc/MIBULoopbackServerHelper](MACHOS/MIBULoopbackServerHelper.md)
- [/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/com.apple.MobileInstallationHelperService](MACHOS/com.apple.MobileInstallationHelperService.md)
- [/System/Library/PrivateFrameworks/MomentsIntelligence.framework/XPCServices/MomentsIntelligenceService.xpc/MomentsIntelligenceService](MACHOS/MomentsIntelligenceService.md)
- [/System/Library/PrivateFrameworks/NanoLeash.framework/companionfindlocallyd](MACHOS/companionfindlocallyd.md)
- [/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd](MACHOS/nanosystemsettingsd.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NUNICalliopeShadersCompanion.metallib](MACHOS/NUNICalliopeShadersCompanion.metallib.md)
- [/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRestoreService.xpc/NFRestoreService](MACHOS/NFRestoreService.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService](MACHOS/com.apple.SharePlay.NearbyInvitationsService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NetworkInfo.framework/PlugIns/NetworkInfoDiagnosticExtension.appex/NetworkInfoDiagnosticExtension](MACHOS/NetworkInfoDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd](MACHOS/newsd.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged](MACHOS/amsondevicestoraged.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/People.framework/peopled](MACHOS/peopled.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd](MACHOS/photoanalysisd.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.printactivityservice.xpc/com.apple.printactivityservice](MACHOS/com.apple.printactivityservice.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/PromotedContentJetSupport.framework/XPCServices/PromotedContentJetService.xpc/PromotedContentJetService](MACHOS/PromotedContentJetService.md)
- [/System/Library/PrivateFrameworks/PrototypeToolsUI.framework/prototyped](MACHOS/prototyped.md)
- [/System/Library/PrivateFrameworks/Recon3D.framework/Reconstruction_Gpu_Archive.metallib](MACHOS/Reconstruction_Gpu_Archive.metallib.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/InteractiveLegacyProfilesSubscriber.xpc/InteractiveLegacyProfilesSubscriber](MACHOS/InteractiveLegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/LegacyProfilesSubscriber.xpc/LegacyProfilesSubscriber](MACHOS/LegacyProfilesSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber](MACHOS/ManagedAppsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedSettingsSubscriber.xpc/ManagedSettingsSubscriber](MACHOS/ManagedSettingsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/PasscodeSettingsSubscriber.xpc/PasscodeSettingsSubscriber](MACHOS/PasscodeSettingsSubscriber.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SecuritySubscriber.xpc/SecuritySubscriber](MACHOS/SecuritySubscriber.md)
- [/System/Library/PrivateFrameworks/RenderBox.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/PlugIns/ScreenTimeDeviceActivityMonitorExtension.appex/ScreenTimeDeviceActivityMonitorExtension](MACHOS/ScreenTimeDeviceActivityMonitorExtension.md)
- [/System/Library/PrivateFrameworks/SensingPredictServices.framework/XPCServices/SensingPredictXPCService.xpc/SensingPredictXPCService](MACHOS/SensingPredictXPCService.md)
- [/System/Library/PrivateFrameworks/ServicesIntelligence.framework/servicesintelligenced](MACHOS/servicesintelligenced.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDrop.appex/AirDrop](MACHOS/AirDrop.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/XPCServices/SAExtensionOrchestrator.xpc/SAExtensionOrchestrator](MACHOS/SAExtensionOrchestrator.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced](MACHOS/siriinferenced.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsBookkeepingService.xpc/SiriSuggestionsBookkeepingService](MACHOS/SiriSuggestionsBookkeepingService.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/PlugIns/SmartRepliesMLRuntimePlugin.appex/SmartRepliesMLRuntimePlugin](MACHOS/SmartRepliesMLRuntimePlugin.md)
- [/System/Library/PrivateFrameworks/SoundScapesUtility.framework/PlugIns/SoundScapesViewServices.appex/SoundScapesViewServices](MACHOS/SoundScapesViewServices.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond](MACHOS/com.apple.SpeechRecognitionCore.speechrecognitiond.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler](MACHOS/PhoneIntentHandler.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd](MACHOS/voicebankingd.md)
- [/System/Library/PrivateFrameworks/ThreatNotificationUI.framework/Extensions/ThreatNotificationCFU.appex/ThreatNotificationCFU](MACHOS/ThreatNotificationCFU.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd](MACHOS/usernotificationsd.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/PlugIns/TVProductPageExtension.appex/TVProductPageExtension](MACHOS/TVProductPageExtension.md)
- [/System/Library/PrivateFrameworks/VoiceMemos.framework/Support/voicememod](MACHOS/voicememod.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/weatherd](MACHOS/weatherd.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner](MACHOS/BackgroundShortcutRunner.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension](MACHOS/SystemActionConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension](MACHOS/WidgetConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/WorkoutKitServices.framework/XPCServices/WorkoutKitXPCService.xpc/WorkoutKitXPCService](MACHOS/WorkoutKitXPCService.md)
- [/System/Library/PrivateFrameworks/iCloudNotification.framework/ind](MACHOS/ind.md)
- [/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/PlugIns/LighthousePlugin.appex/LighthousePlugin](MACHOS/LighthousePlugin.md)
- [/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd](MACHOS/itunescloudd.md)
- [/System/Library/Settings/DefaultApps/AppInstallation.plugin/AppInstallation](MACHOS/AppInstallation.md)
- [/System/Library/Settings/DefaultApps/DefaultCallingAppsSettings.plugin/DefaultCallingAppsSettings](MACHOS/DefaultCallingAppsSettings.md)
- [/System/Library/Settings/DefaultApps/DefaultContactlessAppSettingsUIPlugin.plugin/DefaultContactlessAppSettingsUIPlugin](MACHOS/DefaultContactlessAppSettingsUIPlugin.md)
- [/System/Library/Settings/DefaultApps/DefaultMessagingAppsSettings.plugin/DefaultMessagingAppsSettings](MACHOS/DefaultMessagingAppsSettings.md)
- [/System/Library/Settings/DeviceDiscoveryUISettings.settings/DeviceDiscoveryUISettings](MACHOS/DeviceDiscoveryUISettings.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AppLaunchSuggestionsPlugin.bundle/AppLaunchSuggestionsPlugin](MACHOS/AppLaunchSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/AudioSuggestionsPlugin.bundle/AudioSuggestionsPlugin](MACHOS/AudioSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/PhoneSuggestions.bundle/PhoneSuggestions](MACHOS/PhoneSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/PlaybackControlsSuggestionsPlugin.bundle/PlaybackControlsSuggestionsPlugin](MACHOS/PlaybackControlsSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriGeoSuggestions.bundle/SiriGeoSuggestions](MACHOS/SiriGeoSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriInformationSuggestionsPlugin.bundle/SiriInformationSuggestionsPlugin](MACHOS/SiriInformationSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriLinkSuggestionsPlugin.bundle/SiriLinkSuggestionsPlugin](MACHOS/SiriLinkSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriMessagesSuggestions.bundle/SiriMessagesSuggestions](MACHOS/SiriMessagesSuggestions.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriNotebookSuggestionsPlugin.bundle/SiriNotebookSuggestionsPlugin](MACHOS/SiriNotebookSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriSettingsSuggestionsPlugin.bundle/SiriSettingsSuggestionsPlugin](MACHOS/SiriSettingsSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriSocialConversationSuggestionsPlugin.bundle/SiriSocialConversationSuggestionsPlugin](MACHOS/SiriSocialConversationSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SiriTimeSuggestionsPlugin.bundle/SiriTimeSuggestionsPlugin](MACHOS/SiriTimeSuggestionsPlugin.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/SystemCommandsSuggestionsPlugin.bundle/SystemCommandsSuggestionsPlugin](MACHOS/SystemCommandsSuggestionsPlugin.md)
- [/System/Library/Snippets/UIPlugins/ResponseGenerationUIPlugin.bundle/ResponseGenerationUIPlugin](MACHOS/ResponseGenerationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriInformationUIPlugin.bundle/SiriInformationUIPlugin](MACHOS/SiriInformationUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SiriLinkUIPlugin.bundle/SiriLinkUIPlugin](MACHOS/SiriLinkUIPlugin.md)
- [/System/Library/Snippets/UIPlugins/SystemPlugin.bundle/SystemPlugin](MACHOS/SystemPlugin.md)
- [/System/Library/StreamingExtractorPlugins/Managed Background Assets Processing Pipeline.bundle/Managed Background Assets Processing Pipeline](MACHOS/Managed_Background_Assets_Processing_Pipeline.md)
- [/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder](MACHOS/AppleVideoEncoder.md)
- [/System/Library/VideoProcessors/DepthProcessorV2.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/SmartStyleV1.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g17p](MACHOS/binaryArchive.g17p.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVIntentsExtension.appex/TVIntentsExtension](MACHOS/TVIntentsExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp](MACHOS/AppleVisionProApp.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/AEBookPlugins.framework/AEBookPlugins](MACHOS/AEBookPlugins.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BKLibrary.framework/BKLibrary](MACHOS/BKLibrary.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookAnalytics.framework/BookAnalytics](MACHOS/BookAnalytics.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/EngagementCollector.framework/EngagementCollector](MACHOS/EngagementCollector.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp](MACHOS/JSApp.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/TemplateUI.framework/TemplateUI](MACHOS/TemplateUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksProductPageExtension.appex/BooksProductPageExtension](MACHOS/BooksProductPageExtension.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/Bridge.app/Bridge](MACHOS/Bridge.md)
- [/private/var/staged_system_apps/Calculator.app/Calculator](MACHOS/Calculator.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/Frameworks/FindMyAppCore.framework/FindMyAppCore](MACHOS/FindMyAppCore.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent](MACHOS/FindMyNotificationsContent.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems](MACHOS/FindMyWidgetItems.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformSharingExtension.appex/FreeformSharingExtension](MACHOS/FreeformSharingExtension.md)
- [/private/var/staged_system_apps/Games.app/Games](MACHOS/Games.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/Home](MACHOS/Home.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen](MACHOS/HomeWidgetLockScreen.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetSingleAccessoryIntent.appex/HomeWidgetSingleAccessoryIntent](MACHOS/HomeWidgetSingleAccessoryIntent.md)
- [/private/var/staged_system_apps/Image Playground.app/Image Playground](MACHOS/Image_Playground.md)
- [/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension](MACHOS/GenerativePlaygroundMessagesAppExtension.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets](MACHOS/JournalWidgets.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileCal.app/MobileCal](MACHOS/MobileCal.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.EditorExtension.appex/com.apple.mobilenotes.EditorExtension](MACHOS/com.apple.mobilenotes.EditorExtension.md)
- [/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesPluginNotificationExtension.appex/MessagesPluginNotificationExtension](MACHOS/MessagesPluginNotificationExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/MobileTimer](MACHOS/MobileTimer.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/XPCServices/MusicScriptUpdateService.xpc/MusicScriptUpdateService](MACHOS/MusicScriptUpdateService.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp](MACHOS/MusicMessagesApp.md)
- [/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets](MACHOS/MusicWidgets.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension](MACHOS/NewsNotificationServiceExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2](MACHOS/NewsToday2.md)
- [/private/var/staged_system_apps/Passwords.app/Passwords](MACHOS/Passwords.md)
- [/private/var/staged_system_apps/Photos.app/Photos](MACHOS/Photos.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsActions.framework/PodcastsActions](MACHOS/PodcastsActions.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsPlayback.framework/PodcastsPlayback](MACHOS/PodcastsPlayback.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Preview.app/Preview](MACHOS/Preview.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension](MACHOS/RemindersSharingExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/TranslationWidgetsExtension.appex/TranslationWidgetsExtension](MACHOS/TranslationWidgetsExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget](MACHOS/StocksWidget.md)
- [/private/var/staged_system_apps/Stocks.app/Stocks](MACHOS/Stocks.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/PlugIns/RecordWidgetExtension.appex/RecordWidgetExtension](MACHOS/RecordWidgetExtension.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/Extensions/WeatherPoster.appex/WeatherPoster](MACHOS/WeatherPoster.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherIntents.appex/WeatherIntents](MACHOS/WeatherIntents.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/usr/bin/csfdiagnose](MACHOS/csfdiagnose.md)
- [/usr/bin/fileproviderctl](MACHOS/fileproviderctl.md)
- [/usr/bin/modelcatalogdump](MACHOS/modelcatalogdump.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/lib/libmobileassetd.dylib](MACHOS/libmobileassetd.dylib.md)
- [/usr/lib/libramrod.dylib](MACHOS/libramrod.dylib.md)
- [/usr/lib/swift/libswiftRemoteMirror.dylib](MACHOS/libswiftRemoteMirror.dylib.md)
- [/usr/libexec/AuthenticationServicesAgent](MACHOS/AuthenticationServicesAgent.md)
- [/usr/libexec/ViewHierarchyAgent](MACHOS/ViewHierarchyAgent.md)
- [/usr/libexec/aonsensed](MACHOS/aonsensed.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/appleidsetupd](MACHOS/appleidsetupd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/caraccessoryd](MACHOS/caraccessoryd.md)
- [/usr/libexec/companiond](MACHOS/companiond.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/countryd](MACHOS/countryd.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/devicesharingd](MACHOS/devicesharingd.md)
- [/usr/libexec/diagnosticspushd](MACHOS/diagnosticspushd.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/enhancedloggingd](MACHOS/enhancedloggingd.md)
- [/usr/libexec/feedbackd](MACHOS/feedbackd.md)
- [/usr/libexec/findmybeaconingd](MACHOS/findmybeaconingd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/fmflocatord](MACHOS/fmflocatord.md)
- [/usr/libexec/frauddefensed](MACHOS/frauddefensed.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/gamesaved](MACHOS/gamesaved.md)
- [/usr/libexec/gpsd](MACHOS/gpsd.md)
- [/usr/libexec/heartratecoordinatord](MACHOS/heartratecoordinatord.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/installd](MACHOS/installd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/linkd](MACHOS/linkd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/managedassetsd](MACHOS/managedassetsd.md)
- [/usr/libexec/mediacontinuityd](MACHOS/mediacontinuityd.md)
- [/usr/libexec/mlhostd](MACHOS/mlhostd.md)
- [/usr/libexec/mmaintenanced](MACHOS/mmaintenanced.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/online-auth-agent](MACHOS/online-auth-agent.md)
- [/usr/libexec/pcapd](MACHOS/pcapd.md)
- [/usr/libexec/photosfaced](MACHOS/photosfaced.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityresearchdevice-init](MACHOS/securityresearchdevice-init.md)
- [/usr/libexec/seld](MACHOS/seld.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/softposreaderd](MACHOS/softposreaderd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/textcontextd](MACHOS/textcontextd.md)
- [/usr/libexec/tipsd](MACHOS/tipsd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/visioncompaniond](MACHOS/visioncompaniond.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)

</details>

## Firmware

### ⬆️ Updated (6)

<details>
  <summary><i>View Updated</i></summary>

#### adc-rheia-d9x.im4p

>  `adc-rheia-d9x.im4p`

```diff

 
-  __TEXT.__text: 0xabe21c
-  __TEXT.__const: 0x9b4a78
+  __TEXT.__text: 0xabe110
+  __TEXT.__const: 0x9b4ab0
   __TEXT.text_env: 0x4f1a4
-  __TEXT.__cstring: 0xa6572
+  __TEXT.__cstring: 0xa6566
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__eh_frame: 0xcbc

   __DATA.__mod_init_func: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x5ae400
-  UUID: F0481F2A-8048-3AA5-BA4F-36AFBEC5EAC9
+  UUID: 44B9E448-D57D-36B6-879A-911D942394B8
   Functions: 9175
   Symbols:   0
-  CStrings:  18212
+  CStrings:  18211
 
Functions:
~ sub_3e1198 : 464 -> 468
~ sub_8dbbd8 -> sub_8dbbdc : 3956 -> 3684
~ sub_abe0e0 -> sub_abdfd4 : 324 -> 316
CStrings:
+ "00:15:56"
- "23:51:14"
- "Aug 14 2025"

```

#### ansf.t8140.release.im4p

>  `ansf.t8140.release.im4p`

```diff

   __TEXT.shared: 0xd768
   __TEXT.read: 0x6c9c
   __TEXT.__const: 0x5298
-  __TEXT.__cstring: 0x237c6
+  __TEXT.__cstring: 0x237c8
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA._rtk_boot: 0x8000
CStrings:
+ "2914.0.121~1193"
+ "AppleStorageFirmware-2914.0.121~1193"
- "2914.0.121~876"
- "AppleStorageFirmware-2914.0.121~876"

```

#### exclave_ExclaveStackshotServer

>  `exclave_ExclaveStackshotServer`

```diff

 68.0.0.0.0
-  __TEXT.__text: 0x344c28
+  __TEXT.__text: 0x34471c
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__const: 0xd8f70
   __TEXT.__cstring: 0x2576b
   __TEXT.__swift5_typeref: 0x5fde
-  __TEXT.__swift5_fieldmd: 0x5c88
-  __TEXT.__constg_swiftt: 0xa734
-  __TEXT.__swift5_reflstr: 0x2010
-  __TEXT.__swift5_assocty: 0x4980
+  __TEXT.__swift5_fieldmd: 0x5ca0
+  __TEXT.__constg_swiftt: 0xa710
+  __TEXT.__swift5_reflstr: 0x2000
+  __TEXT.__swift5_assocty: 0x4920
   __TEXT.__swift5_protos: 0x258
-  __TEXT.__swift5_proto: 0x14f0
-  __TEXT.__swift5_types: 0x88c
+  __TEXT.__swift5_proto: 0x14dc
+  __TEXT.__swift5_types: 0x888
   __TEXT.__swift5_capture: 0x3a8
   __TEXT.__swift5_builtin: 0x58c
   __TEXT.__swift5_mpenum: 0xbc
-  __TEXT.__swift5_types2: 0x24
+  __TEXT.__swift5_types2: 0x28
   __TEXT.__swift_as_entry: 0x21c
   __TEXT.__swift_as_ret: 0x2a4
   __TEXT.__constructor: 0x0

   __DATA.__got: 0x8
   __DATA.__auth_ptr: 0x70
   __DATA.__mod_init_func: 0x48
-  __DATA.__const: 0x1b1d8
+  __DATA.__const: 0x1b220
   __DATA.__objc_imageinfo: 0x8
   __DATA.__TIGHTBEAM_VT: 0x60
   __DATA.__TIGHTBEAM: 0x20

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0x455d0
+  __DATA.__bss: 0x45600
   __DATA.__common: 0x2600
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: 5C04669F-DE4A-3816-96C3-F4D42A4FE8EB
-  Functions: 12787
+  UUID: 56B494FF-0D2F-350B-BA38-CC63D04F7DC5
+  Functions: 12775
   Symbols:   0
   CStrings:  4091
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B8hkugCIHJzU2rfZORy6MlCR3N4R3Y5tL5AA0Sw/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~B6x0ugCn2-lGYAkg2MCvvljkJ5FHRzC4qBwmjX4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"

```

#### exclave_roottask

>  `exclave_roottask`

```diff

 1195.0.38.0.0
-  __TEXT.__text: 0x4ca020
+  __TEXT.__text: 0x4c9b6c
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__const: 0xe62d9
   __TEXT.__cstring: 0x32f1a
   __TEXT.__swift5_typeref: 0xad82
   __TEXT.__swift5_capture: 0x17cc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0x974c
-  __TEXT.__swift5_assocty: 0x6490
-  __TEXT.__constg_swiftt: 0x11ffc
-  __TEXT.__swift5_fieldmd: 0xf0e8
+  __TEXT.__swift5_reflstr: 0x973c
+  __TEXT.__swift5_assocty: 0x6430
+  __TEXT.__constg_swiftt: 0x11fd8
+  __TEXT.__swift5_fieldmd: 0xf100
   __TEXT.__swift5_builtin: 0xd34
-  __TEXT.__swift5_proto: 0x2444
-  __TEXT.__swift5_types: 0x1088
+  __TEXT.__swift5_proto: 0x2430
+  __TEXT.__swift5_types: 0x1084
   __TEXT.__swift5_protos: 0x340
   __TEXT.__swift5_mpenum: 0x468
-  __TEXT.__swift5_types2: 0x38
+  __TEXT.__swift5_types2: 0x3c
   __TEXT.__swift_as_entry: 0x21c
   __TEXT.__swift_as_ret: 0x2a4
   __TEXT.__constructor: 0x0

   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x24
-  __TEXT.__eh_frame: 0x1a554
+  __TEXT.__eh_frame: 0x1a54c
   __DATA.__got: 0x198
   __DATA.__auth_ptr: 0x160
   __DATA.__mod_init_func: 0x50
-  __DATA.__const: 0x2f468
+  __DATA.__const: 0x2f510
   __DATA.__objc_imageinfo: 0x8
   __DATA.__data: 0x9a98
   __DATA.__shared_cache: 0x70

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
   __DATA.__common: 0x21fd8
-  __DATA.__bss: 0x128f0
+  __DATA.__bss: 0x12920
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: 8DD15BD5-DB62-309D-B6F2-9750FEE04CFF
-  Functions: 17960
+  UUID: B5DC9130-7AA8-3E61-83B2-C82FD84602A5
+  Functions: 17948
   Symbols:   26
   CStrings:  5442
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B8hkugCIHJzU2rfZORy6MlCR3N4R3Y5tL5AA0Sw/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~B6x0ugCn2-lGYAkg2MCvvljkJ5FHRzC4qBwmjX4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 1116.0.87.0.0
-  __TEXT.__text: 0x550b8c
+  __TEXT.__text: 0x552078
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__cstring: 0x40eef
   __TEXT.__const: 0x1042d7
   __TEXT.__swift5_typeref: 0x10780
-  __TEXT.__swift5_reflstr: 0xbcda
-  __TEXT.__swift5_assocty: 0x70e0
-  __TEXT.__swift5_fieldmd: 0x14178
-  __TEXT.__constg_swiftt: 0x1ed64
+  __TEXT.__swift5_reflstr: 0xbcca
+  __TEXT.__swift5_assocty: 0x7080
+  __TEXT.__swift5_fieldmd: 0x14190
+  __TEXT.__constg_swiftt: 0x1ed40
   __TEXT.__swift5_protos: 0x75c
-  __TEXT.__swift5_proto: 0x2e94
-  __TEXT.__swift5_types: 0x1aec
-  __TEXT.__swift5_types2: 0x48
+  __TEXT.__swift5_proto: 0x2e80
+  __TEXT.__swift5_types: 0x1ae8
+  __TEXT.__swift5_types2: 0x4c
   __TEXT.__swift5_builtin: 0x12c0
   __TEXT.__swift5_mpenum: 0x2f8
   __TEXT.__swift5_capture: 0x638

   __DATA.__got: 0x18
   __DATA.__auth_ptr: 0x368
   __DATA.__mod_init_func: 0x38
-  __DATA.__const: 0x34fe0
+  __DATA.__const: 0x35a28
   __DATA.__objc_imageinfo: 0x8
   __DATA.__data: 0x10c50
   __DATA.__shared_cache: 0x1f8

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x38
   __DATA.__common: 0x959
-  __DATA.__bss: 0xd880
+  __DATA.__bss: 0xd8b0
   __PDATA.__data: 0x2138
-  __PDATA.__const: 0x4850
+  __PDATA.__const: 0x48a8
   __PDATA.__ENDPOINTS: 0x731
   __PDATA.__shared_cache: 0x38
   __PDATA.__mod_init_func: 0x18

   __PDATA.__common: 0x23a0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: CD2D4FCA-8605-37C6-B9D3-CFAC6B9EA2A0
-  Functions: 20879
+  UUID: 89ED38F5-B5F2-35BF-9C80-2ADD2B5BAB95
+  Functions: 20871
   Symbols:   0
   CStrings:  6321
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B8hkugCIHJzU2rfZORy6MlCR3N4R3Y5tL5AA0Sw/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~B8hkugCvwRuJ9GbEoszXT4-Nia8IOUHrUA5wGRs/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~B8hlugCmdBmb4M-he7QUnLdrVomJpord_Snyk5Q/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "/AppleInternal/Library/BuildRoots/4~B6x0ugCn2-lGYAkg2MCvvljkJ5FHRzC4qBwmjX4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~B6x2ugAyOhyHM4nRKOf7Y_EJIOF_9kZEhdtnRrU/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~B6x3ugARxxRcaHFc0jml-dRt5aLJqLeUprjuuxw/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.0.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"

```

#### rans.t8140.release.im4p

>  `rans.t8140.release.im4p`

```diff

   __TEXT.shared: 0xd768
   __TEXT.read: 0x6c9c
   __TEXT.__const: 0x5298
-  __TEXT.__cstring: 0x237c6
+  __TEXT.__cstring: 0x237c8
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA._rtk_boot: 0x8000
CStrings:
+ "2914.0.121~1193"
+ "AppleStorageFirmware-2914.0.121~1193"
- "2914.0.121~876"
- "AppleStorageFirmware-2914.0.121~876"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.0 *(23A5330a)* | iBoot-13822.2.13 |
| 26.0 *(23A5336a)* | iBoot-13822.2.13 |

#### 🆕 NEW (3)

<details>
  <summary><i>View NEW</i></summary>

##### `AppleSMCFirmware.bin`
  - `AppleSMCFirmware_H17-6164.2.12.d93.REL`
##### `iboot`
  - `JFI7EArY2;`
  - ` ApplePMUFirmware-608.0.9~1278.release`
  - `root@dz5qj.p1l.plx.sd...2025/08/29@19:11:37`
  - `MCE FW E001- built on Thu Aug 28 02:50:09 UTC 2025 by root`
  - `2C5rg"IF|p`
  - `dede69bc4cbcd2151785b9dc85d67152`
  - `JPKOKMKLKKKJ`
##### `iboot_blob30.bin`
  - `root@Aug 27 2025@20:17:41~.release`

</details>

#### ❌ Removed (3)

<details>
  <summary><i>View Removed</i></summary>

##### `iboot`
  - `lN3(![40@ov`
  - `root@4jrrf.p1l.plx.sd...2025/08/14@23:52:31`
  - `2fb56e8d4b571585d38c5ce35d0046fb`
  - `MCE FW E001- built on Mon Aug  4 06:34:21 UTC 2025 by root`
  - `4pH,,*rv2j7`
  - ` ApplePMUFirmware-608.0.9~867.release`
##### `iboot_blob30.bin`
  - `root@Aug 04 2025@00:07:09~.release`
##### `AppleSMCFirmware.bin`
  - `AppleSMCFirmware_H17-6164.2.11.d93.REL`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.0 *(23A5330a)* | 622.1.22.10.8 |
| 26.0 *(23A5336a)* | 622.1.22.10.9 |

### Dylibs

#### ⬆️ Updated (1113)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Accounts/Notification/AISAccountNotificationPlugin.bundle/AISAccountNotificationPlugin](DYLIBS/AISAccountNotificationPlugin.md)
- [/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin](DYLIBS/AMSAccountNotificationPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterModule.bundle/HomeControlCenterModule](DYLIBS/HomeControlCenterModule.md)
- [/System/Library/ControlCenter/Bundles/HomeControlCenterSingleTileModule.bundle/HomeControlCenterSingleTileModule](DYLIBS/HomeControlCenterSingleTileModule.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AlarmKit.framework/AlarmKit](DYLIBS/AlarmKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/AutomatedDeviceEnrollment](DYLIBS/AutomatedDeviceEnrollment.md)
- [/System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets](DYLIBS/BackgroundAssets.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/CarKey.framework/CarKey](DYLIBS/CarKey.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/Cinematic.framework/Cinematic](DYLIBS/Cinematic.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/ContactProvider.framework/ContactProvider](DYLIBS/ContactProvider.md)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreData.framework/CoreData](DYLIBS/CoreData.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreNFC.framework/CoreNFC](DYLIBS/CoreNFC.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTransferable.framework/CoreTransferable](DYLIBS/CoreTransferable.md)
- [/System/Library/Frameworks/CoreVideo.framework/CoreVideo](DYLIBS/CoreVideo.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/Frameworks/DockKit.framework/DockKit](DYLIBS/DockKit.md)
- [/System/Library/Frameworks/EnergyKit.framework/EnergyKit](DYLIBS/EnergyKit.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/ExtensionKit.framework/ExtensionKit](DYLIBS/ExtensionKit.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControls](DYLIBS/FamilyControls.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/FoundationModels.framework/FoundationModels](DYLIBS/FoundationModels.md)
- [/System/Library/Frameworks/GameKit.framework/GameKit](DYLIBS/GameKit.md)
- [/System/Library/Frameworks/GameSave.framework/GameSave](DYLIBS/GameSave.md)
- [/System/Library/Frameworks/GroupActivities.framework/GroupActivities](DYLIBS/GroupActivities.md)
- [/System/Library/Frameworks/HealthKit.framework/HealthKit](DYLIBS/HealthKit.md)
- [/System/Library/Frameworks/HomeKit.framework/HomeKit](DYLIBS/HomeKit.md)
- [/System/Library/Frameworks/IdentityDocumentServices.framework/IdentityDocumentServices](DYLIBS/IdentityDocumentServices.md)
- [/System/Library/Frameworks/IdentityDocumentServicesUI.framework/IdentityDocumentServicesUI](DYLIBS/IdentityDocumentServicesUI.md)
- [/System/Library/Frameworks/IdentityLookup.framework/IdentityLookup](DYLIBS/IdentityLookup.md)
- [/System/Library/Frameworks/ImagePlayground.framework/ImagePlayground](DYLIBS/ImagePlayground.md)
- [/System/Library/Frameworks/JournalingSuggestions.framework/JournalingSuggestions](DYLIBS/JournalingSuggestions.md)
- [/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LockedCameraCapture.framework/LockedCameraCapture](DYLIBS/LockedCameraCapture.md)
- [/System/Library/Frameworks/ManagedApp.framework/ManagedApp](DYLIBS/ManagedApp.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/ManagedAppDistribution](DYLIBS/ManagedAppDistribution.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/MatterSupport.framework/MatterSupport](DYLIBS/MatterSupport.md)
- [/System/Library/Frameworks/MediaPlayer.framework/MediaPlayer](DYLIBS/MediaPlayer.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/Messages.framework/Messages](DYLIBS/Messages.md)
- [/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph](DYLIBS/MetalPerformanceShadersGraph.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension](DYLIBS/NetworkExtension.md)
- [/System/Library/Frameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/QuickLook.framework/QuickLook](DYLIBS/QuickLook.md)
- [/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing](DYLIBS/QuickLookThumbnailing.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RealityKit.framework/RealityKit](DYLIBS/RealityKit.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/SecureElementCredential.framework/SecureElementCredential](DYLIBS/SecureElementCredential.md)
- [/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis](DYLIBS/SensitiveContentAnalysis.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/TelephonyMessagingKit.framework/TelephonyMessagingKit](DYLIBS/TelephonyMessagingKit.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/Translation.framework/Translation](DYLIBS/Translation.md)
- [/System/Library/Frameworks/TranslationUIProvider.framework/TranslationUIProvider](DYLIBS/TranslationUIProvider.md)
- [/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount](DYLIBS/VideoSubscriberAccount.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/VisionKit.framework/VisionKit](DYLIBS/VisionKit.md)
- [/System/Library/Frameworks/WeatherKit.framework/WeatherKit](DYLIBS/WeatherKit.md)
- [/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib](DYLIBS/libWebKitSwift.dylib.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WiFiAware.framework/WiFiAware](DYLIBS/WiFiAware.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WirelessInsights.framework/WirelessInsights](DYLIBS/WirelessInsights.md)
- [/System/Library/Frameworks/_AVKit_SwiftUI.framework/_AVKit_SwiftUI](DYLIBS/_AVKit_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI](DYLIBS/_AppIntents_SwiftUI.md)
- [/System/Library/Frameworks/_AppIntents_UIKit.framework/_AppIntents_UIKit](DYLIBS/_AppIntents_UIKit.md)
- [/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI](DYLIBS/_AuthenticationServices_SwiftUI.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/_DeviceActivity_SwiftUI](DYLIBS/_DeviceActivity_SwiftUI.md)
- [/System/Library/Frameworks/_DeviceDiscoveryUI_SwiftUI.framework/_DeviceDiscoveryUI_SwiftUI](DYLIBS/_DeviceDiscoveryUI_SwiftUI.md)
- [/System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit](DYLIBS/_GroupActivities_UIKit.md)
- [/System/Library/Frameworks/_ManagedAppDistribution_SwiftUI.framework/_ManagedAppDistribution_SwiftUI](DYLIBS/_ManagedAppDistribution_SwiftUI.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_MarketplaceKit_UIKit.framework/_MarketplaceKit_UIKit](DYLIBS/_MarketplaceKit_UIKit.md)
- [/System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI](DYLIBS/_MusicKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_PhotosUI_WidgetKit.framework/_PhotosUI_WidgetKit](DYLIBS/_PhotosUI_WidgetKit.md)
- [/System/Library/Frameworks/_QuickLook_SwiftUI.framework/_QuickLook_SwiftUI](DYLIBS/_QuickLook_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_SecureElementCredential_SwiftUI.framework/_SecureElementCredential_SwiftUI](DYLIBS/_SecureElementCredential_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Frameworks/_SwiftData_SwiftUI.framework/_SwiftData_SwiftUI](DYLIBS/_SwiftData_SwiftUI.md)
- [/System/Library/Frameworks/_Translation_SwiftUI.framework/_Translation_SwiftUI](DYLIBS/_Translation_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/HealthCategories.healthplugin/HealthCategories](DYLIBS/HealthCategories.md)
- [/System/Library/Health/FeedItemPlugins/HealthRecords.healthplugin/HealthRecords](DYLIBS/HealthRecords.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/HighlightAlerts.healthplugin/HighlightAlerts](DYLIBS/HighlightAlerts.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/NanoPreferenceBundles/General/AccessibilitySettings.bundle/AccessibilitySettings](DYLIBS/AccessibilitySettings.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/NanoSleepComplication.bundle/NanoSleepComplication](DYLIBS/NanoSleepComplication.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/PreferenceBundles/AVKitSettings.bundle/AVKitSettings](DYLIBS/AVKitSettings.md)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings](DYLIBS/MobilePhoneSettings.md)
- [/System/Library/PrivateFrameworks/AAAFoundationSwift.framework/AAAFoundationSwift](DYLIBS/AAAFoundationSwift.md)
- [/System/Library/PrivateFrameworks/ACSEFoundation.framework/ACSEFoundation](DYLIBS/ACSEFoundation.md)
- [/System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics](DYLIBS/AIMLExperimentationAnalytics.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/ALDataTypes.framework/ALDataTypes.dylib](DYLIBS/ALDataTypes.dylib.md)
- [/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation](DYLIBS/APFoundation.md)
- [/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture](DYLIBS/AVFCapture.md)
- [/System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities](DYLIBS/AXCoreUtilities.md)
- [/System/Library/PrivateFrameworks/AXGuestPassServices.framework/AXGuestPassServices](DYLIBS/AXGuestPassServices.md)
- [/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance](DYLIBS/AXSpringBoardServerInstance.md)
- [/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AccessibilityPhysicalInteraction](DYLIBS/AccessibilityPhysicalInteraction.md)
- [/System/Library/PrivateFrameworks/AccessibilityReaderData.framework/AccessibilityReaderData](DYLIBS/AccessibilityReaderData.md)
- [/System/Library/PrivateFrameworks/AccessibilityReadingUI.framework/AccessibilityReadingUI](DYLIBS/AccessibilityReadingUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport](DYLIBS/AccessibilitySharedSupport.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService](DYLIBS/AccessibilityUIService.md)
- [/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities](DYLIBS/AccessibilityUIUtilities.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings](DYLIBS/AccountsUISettings.md)
- [/System/Library/PrivateFrameworks/AccountsUISupport.framework/AccountsUISupport](DYLIBS/AccountsUISupport.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActivityAchievementsUI.framework/ActivityAchievementsUI](DYLIBS/ActivityAchievementsUI.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsCore.framework/ActivityAwardsCore](DYLIBS/ActivityAwardsCore.md)
- [/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/ActivityAwardsServices](DYLIBS/ActivityAwardsServices.md)
- [/System/Library/PrivateFrameworks/ActivitySharingClient.framework/ActivitySharingClient](DYLIBS/ActivitySharingClient.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivityUI.framework/ActivityUI](DYLIBS/ActivityUI.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AdaptiveMusic.framework/AdaptiveMusic](DYLIBS/AdaptiveMusic.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AeroML.framework/AeroML](DYLIBS/AeroML.md)
- [/System/Library/PrivateFrameworks/AirPlayAndHandoffSettingsSupport.framework/AirPlayAndHandoffSettingsSupport](DYLIBS/AirPlayAndHandoffSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AlarmKitCore.framework/AlarmKitCore](DYLIBS/AlarmKitCore.md)
- [/System/Library/PrivateFrameworks/AlchemistBase.framework/AlchemistBase](DYLIBS/AlchemistBase.md)
- [/System/Library/PrivateFrameworks/AlchemistService.framework/AlchemistService](DYLIBS/AlchemistService.md)
- [/System/Library/PrivateFrameworks/Announce.framework/Announce](DYLIBS/Announce.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal](DYLIBS/AppAttestInternal.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppMigrationKit.framework/AppMigrationKit](DYLIBS/AppMigrationKit.md)
- [/System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync](DYLIBS/AppPlaceholderSync.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppProtectionDaemon.framework/AppProtectionDaemon](DYLIBS/AppProtectionDaemon.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreComponentsDaemonKit.framework/AppStoreComponentsDaemonKit](DYLIBS/AppStoreComponentsDaemonKit.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/AppSystemSettingsUI](DYLIBS/AppSystemSettingsUI.md)
- [/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount](DYLIBS/AppleAccount.md)
- [/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI](DYLIBS/AppleAccountUI.md)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleIntelligenceReporting.framework/AppleIntelligenceReporting](DYLIBS/AppleIntelligenceReporting.md)
- [/System/Library/PrivateFrameworks/AppleIntelligenceReportingProcessing.framework/AppleIntelligenceReportingProcessing](DYLIBS/AppleIntelligenceReportingProcessing.md)
- [/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery](DYLIBS/AppleMediaDiscovery.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal](DYLIBS/AppleMediaServicesKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/Archetype.framework/Archetype](DYLIBS/Archetype.md)
- [/System/Library/PrivateFrameworks/ArchetypeEngine.framework/ArchetypeEngine](DYLIBS/ArchetypeEngine.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission](DYLIBS/AskPermission.md)
- [/System/Library/PrivateFrameworks/AskTo.framework/AskTo](DYLIBS/AskTo.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AskToDaemon.framework/AskToDaemon](DYLIBS/AskToDaemon.md)
- [/System/Library/PrivateFrameworks/AskToUI.framework/AskToUI](DYLIBS/AskToUI.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport](DYLIBS/AssistantSettingsSupport.md)
- [/System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI](DYLIBS/AssistiveTouchUI.md)
- [/System/Library/PrivateFrameworks/AsyncAlgorithmsInternal.framework/AsyncAlgorithmsInternal](DYLIBS/AsyncAlgorithmsInternal.md)
- [/System/Library/PrivateFrameworks/AttributeGraph.framework/AttributeGraph](DYLIBS/AttributeGraph.md)
- [/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics](DYLIBS/AudioAnalytics.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager](DYLIBS/AudioDSPManager.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/BarcodeSupportUI.framework/BarcodeSupportUI](DYLIBS/BarcodeSupportUI.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BrailleSymbology.framework/BrailleSymbology](DYLIBS/BrailleSymbology.md)
- [/System/Library/PrivateFrameworks/BridgeLiveActivity.framework/BridgeLiveActivity](DYLIBS/BridgeLiveActivity.md)
- [/System/Library/PrivateFrameworks/BusinessFoundation.framework/BusinessFoundation](DYLIBS/BusinessFoundation.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/C2.framework/C2](DYLIBS/C2.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture](DYLIBS/CMCapture.md)
- [/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore](DYLIBS/CMCaptureCore.md)
- [/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport](DYLIBS/CTBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI](DYLIBS/CalculateUI.md)
- [/System/Library/PrivateFrameworks/CalendarIntegrationSupport.framework/CalendarIntegrationSupport](DYLIBS/CalendarIntegrationSupport.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarUIKitInternal.framework/CalendarUIKitInternal](DYLIBS/CalendarUIKitInternal.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CallIntelligence.framework/CallIntelligence](DYLIBS/CallIntelligence.md)
- [/System/Library/PrivateFrameworks/CallsAppServices.framework/CallsAppServices](DYLIBS/CallsAppServices.md)
- [/System/Library/PrivateFrameworks/CallsAppUI.framework/CallsAppUI](DYLIBS/CallsAppUI.md)
- [/System/Library/PrivateFrameworks/CallsPersistence.framework/CallsPersistence](DYLIBS/CallsPersistence.md)
- [/System/Library/PrivateFrameworks/CallsSearch.framework/CallsSearch](DYLIBS/CallsSearch.md)
- [/System/Library/PrivateFrameworks/CallsUtilities.framework/CallsUtilities](DYLIBS/CallsUtilities.md)
- [/System/Library/PrivateFrameworks/CallsXPC.framework/CallsXPC](DYLIBS/CallsXPC.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CarAccessoryDaemon.framework/CarAccessoryDaemon](DYLIBS/CarAccessoryDaemon.md)
- [/System/Library/PrivateFrameworks/CarPlayAssetUI.framework/CarPlayAssetUI](DYLIBS/CarPlayAssetUI.md)
- [/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI](DYLIBS/CarPlayUI.md)
- [/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets](DYLIBS/CascadeSets.md)
- [/System/Library/PrivateFrameworks/Catalyst.framework/Catalyst](DYLIBS/Catalyst.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/CipherML.framework/CipherML](DYLIBS/CipherML.md)
- [/System/Library/PrivateFrameworks/ClassKitUI.framework/ClassKitUI](DYLIBS/ClassKitUI.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset](DYLIBS/CloudAsset.md)
- [/System/Library/PrivateFrameworks/CloudAssets.framework/CloudAssets](DYLIBS/CloudAssets.md)
- [/System/Library/PrivateFrameworks/CloudAssetsCommons.framework/CloudAssetsCommons](DYLIBS/CloudAssetsCommons.md)
- [/System/Library/PrivateFrameworks/CloudAssetsDaemon.framework/CloudAssetsDaemon](DYLIBS/CloudAssetsDaemon.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudCoreInternal.framework/CloudCoreInternal](DYLIBS/CloudCoreInternal.md)
- [/System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode](DYLIBS/CloudKitCode.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudRecommendation.framework/CloudRecommendation](DYLIBS/CloudRecommendation.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI](DYLIBS/CloudSharingUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/CloudTelemetry](DYLIBS/CloudTelemetry.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommunicationDetails.framework/CommunicationDetails](DYLIBS/CommunicationDetails.md)
- [/System/Library/PrivateFrameworks/CommunicationTrust.framework/CommunicationTrust](DYLIBS/CommunicationTrust.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUICore.framework/CommunicationsUICore](DYLIBS/CommunicationsUICore.md)
- [/System/Library/PrivateFrameworks/CompanionInferenceCore.framework/CompanionInferenceCore](DYLIBS/CompanionInferenceCore.md)
- [/System/Library/PrivateFrameworks/ComputationalGraph.framework/ComputationalGraph](DYLIBS/ComputationalGraph.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete](DYLIBS/ContactsAutocomplete.md)
- [/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation](DYLIBS/ContactsFoundation.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit](DYLIBS/ContentKit.md)
- [/System/Library/PrivateFrameworks/ContextualSuggestionClient.framework/ContextualSuggestionClient](DYLIBS/ContextualSuggestionClient.md)
- [/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing](DYLIBS/ContinuitySing.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ControlCenterUIServices.framework/ControlCenterUIServices](DYLIBS/ControlCenterUIServices.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CookingKit.framework/CookingKit](DYLIBS/CookingKit.md)
- [/System/Library/PrivateFrameworks/CookingSupport.framework/CookingSupport](DYLIBS/CookingSupport.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration](DYLIBS/CoreAudioOrchestration.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics](DYLIBS/CoreDiagnostics.md)
- [/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition](DYLIBS/CoreEmbeddedSpeechRecognition.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreHID.framework/CoreHID](DYLIBS/CoreHID.md)
- [/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred](DYLIBS/CoreIDCred.md)
- [/System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder](DYLIBS/CoreIDCredBuilder.md)
- [/System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV](DYLIBS/CoreIDV.md)
- [/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD](DYLIBS/CoreIDVPAD.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreMLOdie.framework/CoreMLOdie](DYLIBS/CoreMLOdie.md)
- [/System/Library/PrivateFrameworks/CoreMotionFDNML.framework/CoreMotionFDNML](DYLIBS/CoreMotionFDNML.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI](DYLIBS/CoreODI.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CoreServicesUI.framework/CoreServicesUI](DYLIBS/CoreServicesUI.md)
- [/System/Library/PrivateFrameworks/CoreSpeechDataAnalytics.framework/CoreSpeechDataAnalytics](DYLIBS/CoreSpeechDataAnalytics.md)
- [/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils](DYLIBS/CoreSpeechUtils.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsUI.framework/CoreSuggestionsUI](DYLIBS/CoreSuggestionsUI.md)
- [/System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift](DYLIBS/CoreUtilsSwift.md)
- [/System/Library/PrivateFrameworks/CosmeticAssessment.framework/CosmeticAssessment](DYLIBS/CosmeticAssessment.md)
- [/System/Library/PrivateFrameworks/Cosmo.framework/Cosmo](DYLIBS/Cosmo.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/CoverSheetKit.framework/CoverSheetKit](DYLIBS/CoverSheetKit.md)
- [/System/Library/PrivateFrameworks/CryptexKit.framework/CryptexKit](DYLIBS/CryptexKit.md)
- [/System/Library/PrivateFrameworks/CryptexServer.framework/CryptexServer](DYLIBS/CryptexServer.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps](DYLIBS/DMCApps.md)
- [/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider](DYLIBS/DMCEnrollmentProvider.md)
- [/System/Library/PrivateFrameworks/DSContinuityPairing.framework/DSContinuityPairing](DYLIBS/DSContinuityPairing.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation](DYLIBS/DVTInstrumentsFoundation.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess](DYLIBS/DataAccess.md)
- [/System/Library/PrivateFrameworks/DataCollector.framework/DataCollector](DYLIBS/DataCollector.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DateAndTimeSupport.framework/DateAndTimeSupport](DYLIBS/DateAndTimeSupport.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/DeepThoughtBiomeFoundation](DYLIBS/DeepThoughtBiomeFoundation.md)
- [/System/Library/PrivateFrameworks/DefaultAppsSettingsUI.framework/DefaultAppsSettingsUI](DYLIBS/DefaultAppsSettingsUI.md)
- [/System/Library/PrivateFrameworks/Dendrite.framework/Dendrite](DYLIBS/Dendrite.md)
- [/System/Library/PrivateFrameworks/DepthCore.framework/DepthCore](DYLIBS/DepthCore.md)
- [/System/Library/PrivateFrameworks/DesignLibrary.framework/DesignLibrary](DYLIBS/DesignLibrary.md)
- [/System/Library/PrivateFrameworks/DesktopServicesUI.framework/DesktopServicesUI](DYLIBS/DesktopServicesUI.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore](DYLIBS/DeviceDiscoveryUICore.md)
- [/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/DeviceExpertIntents](DYLIBS/DeviceExpertIntents.md)
- [/System/Library/PrivateFrameworks/DeviceExpertUI.framework/DeviceExpertUI](DYLIBS/DeviceExpertUI.md)
- [/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing](DYLIBS/DeviceSharing.md)
- [/System/Library/PrivateFrameworks/DeviceSharingServices.framework/DeviceSharingServices](DYLIBS/DeviceSharingServices.md)
- [/System/Library/PrivateFrameworks/DeviceSharingServicesCore.framework/DeviceSharingServicesCore](DYLIBS/DeviceSharingServicesCore.md)
- [/System/Library/PrivateFrameworks/DeviceSharingUI.framework/DeviceSharingUI](DYLIBS/DeviceSharingUI.md)
- [/System/Library/PrivateFrameworks/DeviceTreeKit.framework/DeviceTreeKit](DYLIBS/DeviceTreeKit.md)
- [/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices](DYLIBS/DiagnosticsReporterServices.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/DistributedTimers.framework/DistributedTimers](DYLIBS/DistributedTimers.md)
- [/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon](DYLIBS/DistributedTimersDaemon.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables](DYLIBS/DocumentManagerExecutables.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/DocumentManagerUICore](DYLIBS/DocumentManagerUICore.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient](DYLIBS/DocumentUnderstandingClient.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DropIn.framework/DropIn](DYLIBS/DropIn.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/Dyld.framework/Dyld](DYLIBS/Dyld.md)
- [/System/Library/PrivateFrameworks/EcosystemAnalytics.framework/EcosystemAnalytics](DYLIBS/EcosystemAnalytics.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon](DYLIBS/EmailDaemon.md)
- [/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation](DYLIBS/EmailFoundation.md)
- [/System/Library/PrivateFrameworks/EncoreXPCService.framework/EncoreXPCService](DYLIBS/EncoreXPCService.md)
- [/System/Library/PrivateFrameworks/EnergyKitInternal.framework/EnergyKitInternal](DYLIBS/EnergyKitInternal.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking](DYLIBS/FMNetworking.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FaceTimeNotificationCore.framework/FaceTimeNotificationCore](DYLIBS/FaceTimeNotificationCore.md)
- [/System/Library/PrivateFrameworks/FaceTimeNotificationUI.framework/FaceTimeNotificationUI](DYLIBS/FaceTimeNotificationUI.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService](DYLIBS/FeedbackService.md)
- [/System/Library/PrivateFrameworks/FileIndexerDaemon.framework/FileIndexerDaemon](DYLIBS/FileIndexerDaemon.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore](DYLIBS/FinHealthCore.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase](DYLIBS/FindMyBase.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyCloudKit.framework/FindMyCloudKit](DYLIBS/FindMyCloudKit.md)
- [/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon](DYLIBS/FindMyCommon.md)
- [/System/Library/PrivateFrameworks/FindMyCore.framework/FindMyCore](DYLIBS/FindMyCore.md)
- [/System/Library/PrivateFrameworks/FindMyDaemonSupport.framework/FindMyDaemonSupport](DYLIBS/FindMyDaemonSupport.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyLocateObjCWrapper.framework/FindMyLocateObjCWrapper](DYLIBS/FindMyLocateObjCWrapper.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyPairing.framework/FindMyPairing](DYLIBS/FindMyPairing.md)
- [/System/Library/PrivateFrameworks/FindMyServerInteraction.framework/FindMyServerInteraction](DYLIBS/FindMyServerInteraction.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FindMyUnsafeAsyncBridging.framework/FindMyUnsafeAsyncBridging](DYLIBS/FindMyUnsafeAsyncBridging.md)
- [/System/Library/PrivateFrameworks/FitnessActions.framework/FitnessActions](DYLIBS/FitnessActions.md)
- [/System/Library/PrivateFrameworks/FitnessAppRoot.framework/FitnessAppRoot](DYLIBS/FitnessAppRoot.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards](DYLIBS/FitnessAwards.md)
- [/System/Library/PrivateFrameworks/FitnessBrowsing.framework/FitnessBrowsing](DYLIBS/FitnessBrowsing.md)
- [/System/Library/PrivateFrameworks/FitnessCanvas.framework/FitnessCanvas](DYLIBS/FitnessCanvas.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessCoreUI.framework/FitnessCoreUI](DYLIBS/FitnessCoreUI.md)
- [/System/Library/PrivateFrameworks/FitnessDispatch.framework/FitnessDispatch](DYLIBS/FitnessDispatch.md)
- [/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering](DYLIBS/FitnessFiltering.md)
- [/System/Library/PrivateFrameworks/FitnessForYou.framework/FitnessForYou](DYLIBS/FitnessForYou.md)
- [/System/Library/PrivateFrameworks/FitnessIntelligence.framework/FitnessIntelligence](DYLIBS/FitnessIntelligence.md)
- [/System/Library/PrivateFrameworks/FitnessIntelligenceDaemonCore.framework/FitnessIntelligenceDaemonCore](DYLIBS/FitnessIntelligenceDaemonCore.md)
- [/System/Library/PrivateFrameworks/FitnessIntelligenceFeedback.framework/FitnessIntelligenceFeedback](DYLIBS/FitnessIntelligenceFeedback.md)
- [/System/Library/PrivateFrameworks/FitnessIntelligenceInference.framework/FitnessIntelligenceInference](DYLIBS/FitnessIntelligenceInference.md)
- [/System/Library/PrivateFrameworks/FitnessIntelligenceSnapshotting.framework/FitnessIntelligenceSnapshotting](DYLIBS/FitnessIntelligenceSnapshotting.md)
- [/System/Library/PrivateFrameworks/FitnessLibrary.framework/FitnessLibrary](DYLIBS/FitnessLibrary.md)
- [/System/Library/PrivateFrameworks/FitnessMarketing.framework/FitnessMarketing](DYLIBS/FitnessMarketing.md)
- [/System/Library/PrivateFrameworks/FitnessOnboarding.framework/FitnessOnboarding](DYLIBS/FitnessOnboarding.md)
- [/System/Library/PrivateFrameworks/FitnessProductDetail.framework/FitnessProductDetail](DYLIBS/FitnessProductDetail.md)
- [/System/Library/PrivateFrameworks/FitnessRemoteBrowsing.framework/FitnessRemoteBrowsing](DYLIBS/FitnessRemoteBrowsing.md)
- [/System/Library/PrivateFrameworks/FitnessSampleContent.framework/FitnessSampleContent](DYLIBS/FitnessSampleContent.md)
- [/System/Library/PrivateFrameworks/FitnessSearch.framework/FitnessSearch](DYLIBS/FitnessSearch.md)
- [/System/Library/PrivateFrameworks/FitnessSharePlaySession.framework/FitnessSharePlaySession](DYLIBS/FitnessSharePlaySession.md)
- [/System/Library/PrivateFrameworks/FitnessSiriSession.framework/FitnessSiriSession](DYLIBS/FitnessSiriSession.md)
- [/System/Library/PrivateFrameworks/FitnessTrainerTips.framework/FitnessTrainerTips](DYLIBS/FitnessTrainerTips.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FitnessUtilities.framework/FitnessUtilities](DYLIBS/FitnessUtilities.md)
- [/System/Library/PrivateFrameworks/FitnessWorkoutPlan.framework/FitnessWorkoutPlan](DYLIBS/FitnessWorkoutPlan.md)
- [/System/Library/PrivateFrameworks/FlightUtilitiesCore.framework/FlightUtilitiesCore](DYLIBS/FlightUtilitiesCore.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal](DYLIBS/GRDBInternal.md)
- [/System/Library/PrivateFrameworks/GRPCCoreInternal.framework/GRPCCoreInternal](DYLIBS/GRPCCoreInternal.md)
- [/System/Library/PrivateFrameworks/GRPCInProcessTransportInternal.framework/GRPCInProcessTransportInternal](DYLIBS/GRPCInProcessTransportInternal.md)
- [/System/Library/PrivateFrameworks/GRPCURLSessionTransportInternal.framework/GRPCURLSessionTransportInternal](DYLIBS/GRPCURLSessionTransportInternal.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterOverlayService.framework/GameCenterOverlayService](DYLIBS/GameCenterOverlayService.md)
- [/System/Library/PrivateFrameworks/GameCenterServerClient.framework/GameCenterServerClient](DYLIBS/GameCenterServerClient.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameServices.framework/GameServices](DYLIBS/GameServices.md)
- [/System/Library/PrivateFrameworks/GameServicesCore.framework/GameServicesCore](DYLIBS/GameServicesCore.md)
- [/System/Library/PrivateFrameworks/GameStoreKit.framework/GameStoreKit](DYLIBS/GameStoreKit.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/GenerativeAssistantActions](DYLIBS/GenerativeAssistantActions.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantCommon.framework/GenerativeAssistantCommon](DYLIBS/GenerativeAssistantCommon.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantEnablementFlow.framework/GenerativeAssistantEnablementFlow](DYLIBS/GenerativeAssistantEnablementFlow.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings](DYLIBS/GenerativeAssistantSettings.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences](DYLIBS/GenerativeExperiences.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctions.framework/GenerativeFunctions](DYLIBS/GenerativeFunctions.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation](DYLIBS/GenerativeFunctionsInstrumentation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativePartnerService.framework/GenerativePartnerService](DYLIBS/GenerativePartnerService.md)
- [/System/Library/PrivateFrameworks/GenerativePartnerServiceUI.framework/GenerativePartnerServiceUI](DYLIBS/GenerativePartnerServiceUI.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/Geometry.framework/Geometry](DYLIBS/Geometry.md)
- [/System/Library/PrivateFrameworks/Gestures.framework/Gestures](DYLIBS/Gestures.md)
- [/System/Library/PrivateFrameworks/GridZero.framework/GridZero](DYLIBS/GridZero.md)
- [/System/Library/PrivateFrameworks/HIDRMClientKit.framework/HIDRMClientKit](DYLIBS/HIDRMClientKit.md)
- [/System/Library/PrivateFrameworks/HIDRMKit.framework/HIDRMKit](DYLIBS/HIDRMKit.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HeadphoneCommonUIKit.framework/HeadphoneCommonUIKit](DYLIBS/HeadphoneCommonUIKit.md)
- [/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs](DYLIBS/HeadphoneConfigs.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettingsUI.framework/HeadphoneSettingsUI](DYLIBS/HeadphoneSettingsUI.md)
- [/System/Library/PrivateFrameworks/HealthArticlesUI.framework/HealthArticlesUI](DYLIBS/HealthArticlesUI.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceAppPlugin.framework/HealthBalanceAppPlugin](DYLIBS/HealthBalanceAppPlugin.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthCharts.framework/HealthCharts](DYLIBS/HealthCharts.md)
- [/System/Library/PrivateFrameworks/HealthContentDaemonPlugin.framework/HealthContentDaemonPlugin](DYLIBS/HealthContentDaemonPlugin.md)
- [/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon](DYLIBS/HealthDaemon.md)
- [/System/Library/PrivateFrameworks/HealthDomains.framework/HealthDomains](DYLIBS/HealthDomains.md)
- [/System/Library/PrivateFrameworks/HealthExperience.framework/HealthExperience](DYLIBS/HealthExperience.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExpressions.framework/HealthExpressions](DYLIBS/HealthExpressions.md)
- [/System/Library/PrivateFrameworks/HealthHeartRateStream.framework/HealthHeartRateStream](DYLIBS/HealthHeartRateStream.md)
- [/System/Library/PrivateFrameworks/HealthIntents.framework/HealthIntents](DYLIBS/HealthIntents.md)
- [/System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions](DYLIBS/HealthKitAdditions.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsExperience.framework/HealthMedicationsExperience](DYLIBS/HealthMedicationsExperience.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsVisionUI.framework/HealthMedicationsVisionUI](DYLIBS/HealthMedicationsVisionUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthMobilityUI.framework/HealthMobilityUI](DYLIBS/HealthMobilityUI.md)
- [/System/Library/PrivateFrameworks/HealthOntologyKit.framework/HealthOntologyKit](DYLIBS/HealthOntologyKit.md)
- [/System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration](DYLIBS/HealthOrchestration.md)
- [/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform](DYLIBS/HealthPlatform.md)
- [/System/Library/PrivateFrameworks/HealthPluginHost.framework/HealthPluginHost](DYLIBS/HealthPluginHost.md)
- [/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices](DYLIBS/HealthRecordServices.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction](DYLIBS/HealthRecordsExtraction.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthRecordsWalletSupport.framework/HealthRecordsWalletSupport](DYLIBS/HealthRecordsWalletSupport.md)
- [/System/Library/PrivateFrameworks/HealthTopics.framework/HealthTopics](DYLIBS/HealthTopics.md)
- [/System/Library/PrivateFrameworks/HealthTopicsCore.framework/HealthTopicsCore](DYLIBS/HealthTopicsCore.md)
- [/System/Library/PrivateFrameworks/HealthTopicsDaemonPlugin.framework/HealthTopicsDaemonPlugin](DYLIBS/HealthTopicsDaemonPlugin.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingModeSettingsUI.framework/HearingModeSettingsUI](DYLIBS/HearingModeSettingsUI.md)
- [/System/Library/PrivateFrameworks/HearingModeUI.framework/HearingModeUI](DYLIBS/HearingModeUI.md)
- [/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest](DYLIBS/HearingTest.md)
- [/System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI](DYLIBS/HearingTestUI.md)
- [/System/Library/PrivateFrameworks/HeartRateCoordinator.framework/HeartRateCoordinator](DYLIBS/HeartRateCoordinator.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents](DYLIBS/HomeAppIntents.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup](DYLIBS/HomeDeviceSetup.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonFoundation.framework/HomeKitDaemonFoundation](DYLIBS/HomeKitDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeServices.framework/HomeServices](DYLIBS/HomeServices.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices](DYLIBS/HomeUtilityServices.md)
- [/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents](DYLIBS/HomeWidgetIntents.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMRCSTransfer.framework/IMRCSTransfer](DYLIBS/IMRCSTransfer.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IconRendering.framework/IconRendering](DYLIBS/IconRendering.md)
- [/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/ImagePlaygroundInternal](DYLIBS/ImagePlaygroundInternal.md)
- [/System/Library/PrivateFrameworks/InputAccessoriesSettings.framework/InputAccessoriesSettings](DYLIBS/InputAccessoriesSettings.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow](DYLIBS/IntelligenceFlow.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/IntelligenceFlowShared](DYLIBS/IntelligenceFlowShared.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/IntelligencePlatformCompute](DYLIBS/IntelligencePlatformCompute.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformDataActions.framework/IntelligencePlatformDataActions](DYLIBS/IntelligencePlatformDataActions.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformQuery.framework/IntelligencePlatformQuery](DYLIBS/IntelligencePlatformQuery.md)
- [/System/Library/PrivateFrameworks/IntelligenceSimulation.framework/IntelligenceSimulation](DYLIBS/IntelligenceSimulation.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/IntentRecommendRuntime.framework/IntentRecommendRuntime](DYLIBS/IntentRecommendRuntime.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/JetCore](DYLIBS/JetCore.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/JournalShared.framework/JournalShared](DYLIBS/JournalShared.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/LLMCache.framework/LLMCache](DYLIBS/LLMCache.md)
- [/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport](DYLIBS/LegalAndRegulatorySettingsSupport.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LighthouseAV.framework/LighthouseAV](DYLIBS/LighthouseAV.md)
- [/System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground](DYLIBS/LighthouseBackground.md)
- [/System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor](DYLIBS/LighthouseDataProcessor.md)
- [/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices](DYLIBS/LinkServices.md)
- [/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription](DYLIBS/LiveTranscription.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI](DYLIBS/LocalAuthenticationCoreUI.md)
- [/System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit](DYLIBS/LocalStatusKit.md)
- [/System/Library/PrivateFrameworks/MCCFoundation.framework/MCCFoundation](DYLIBS/MCCFoundation.md)
- [/System/Library/PrivateFrameworks/MCCKitCategorization.framework/MCCKitCategorization](DYLIBS/MCCKitCategorization.md)
- [/System/Library/PrivateFrameworks/MDM.framework/MDM](DYLIBS/MDM.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/ManagedAppsCore.framework/ManagedAppsCore](DYLIBS/ManagedAppsCore.md)
- [/System/Library/PrivateFrameworks/ManagedAppsInterface.framework/ManagedAppsInterface](DYLIBS/ManagedAppsInterface.md)
- [/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/ManagedBackgroundAssets](DYLIBS/ManagedBackgroundAssets.md)
- [/System/Library/PrivateFrameworks/ManagedBackgroundAssetsHelper.framework/ManagedBackgroundAssetsHelper](DYLIBS/ManagedBackgroundAssetsHelper.md)
- [/System/Library/PrivateFrameworks/ManagedBackgroundAssetsHelperFetching.framework/ManagedBackgroundAssetsHelperFetching](DYLIBS/ManagedBackgroundAssetsHelperFetching.md)
- [/System/Library/PrivateFrameworks/ManagedBackgroundAssetsXPC.framework/ManagedBackgroundAssetsXPC](DYLIBS/ManagedBackgroundAssetsXPC.md)
- [/System/Library/PrivateFrameworks/MapsIntelligence.framework/MapsIntelligence](DYLIBS/MapsIntelligence.md)
- [/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions](DYLIBS/MapsSuggestions.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaContinuityKit.framework/MediaContinuityKit](DYLIBS/MediaContinuityKit.md)
- [/System/Library/PrivateFrameworks/MediaControl.framework/MediaControl](DYLIBS/MediaControl.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaML.framework/MediaML](DYLIBS/MediaML.md)
- [/System/Library/PrivateFrameworks/MediaMLServices.framework/MediaMLServices](DYLIBS/MediaMLServices.md)
- [/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit](DYLIBS/MediaMiningKit.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaSuggester.framework/MediaSuggester](DYLIBS/MediaSuggester.md)
- [/System/Library/PrivateFrameworks/MediaTokens.framework/MediaTokens](DYLIBS/MediaTokens.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MemoryAccounting.framework/MemoryAccounting](DYLIBS/MemoryAccounting.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/Mercury.framework/Mercury](DYLIBS/Mercury.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity](DYLIBS/MessageSecurity.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon](DYLIBS/MicroLocationDaemon.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileIdentityServiceUI.framework/MobileIdentityServiceUI](DYLIBS/MobileIdentityServiceUI.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer](DYLIBS/MobileTimer.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/MobileTimerUISupport.framework/MobileTimerUISupport](DYLIBS/MobileTimerUISupport.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/MomentsUI.framework/MomentsUI](DYLIBS/MomentsUI.md)
- [/System/Library/PrivateFrameworks/MonogramPoster.framework/MonogramPoster](DYLIBS/MonogramPoster.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NDOAPI.framework/NDOAPI](DYLIBS/NDOAPI.md)
- [/System/Library/PrivateFrameworks/NDOUI.framework/NDOUI](DYLIBS/NDOUI.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit](DYLIBS/NPTKit.md)
- [/System/Library/PrivateFrameworks/NameRecognition.framework/NameRecognition](DYLIBS/NameRecognition.md)
- [/System/Library/PrivateFrameworks/NanoControlCenter.framework/NanoControlCenter](DYLIBS/NanoControlCenter.md)
- [/System/Library/PrivateFrameworks/NanoFaceGallery.framework/NanoFaceGallery](DYLIBS/NanoFaceGallery.md)
- [/System/Library/PrivateFrameworks/NanoHomeIntents.framework/NanoHomeIntents](DYLIBS/NanoHomeIntents.md)
- [/System/Library/PrivateFrameworks/NanoHomeScreenUIServices.framework/NanoHomeScreenUIServices](DYLIBS/NanoHomeScreenUIServices.md)
- [/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit](DYLIBS/NanoPassKit.md)
- [/System/Library/PrivateFrameworks/NanoPhotosCore.framework/NanoPhotosCore](DYLIBS/NanoPhotosCore.md)
- [/System/Library/PrivateFrameworks/NanoSmartStackControlUI.framework/NanoSmartStackControlUI](DYLIBS/NanoSmartStackControlUI.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/NearbySessions.framework/NearbySessions](DYLIBS/NearbySessions.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/NeighborhoodActivityConduit](DYLIBS/NeighborhoodActivityConduit.md)
- [/System/Library/PrivateFrameworks/NetworkInfo.framework/NetworkInfo](DYLIBS/NetworkInfo.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI](DYLIBS/NewDeviceOutreachUI.md)
- [/System/Library/PrivateFrameworks/NewsAnalytics.framework/NewsAnalytics](DYLIBS/NewsAnalytics.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon](DYLIBS/NewsDaemon.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsToday.framework/NewsToday](DYLIBS/NewsToday.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/Nexus.framework/Nexus](DYLIBS/Nexus.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/NotesUIServices.framework/NotesUIServices](DYLIBS/NotesUIServices.md)
- [/System/Library/PrivateFrameworks/ODIE.framework/ODIE](DYLIBS/ODIE.md)
- [/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility](DYLIBS/OSEligibility.md)
- [/System/Library/PrivateFrameworks/OmniSearch.framework/OmniSearch](DYLIBS/OmniSearch.md)
- [/System/Library/PrivateFrameworks/OmniSearchClient.framework/OmniSearchClient](DYLIBS/OmniSearchClient.md)
- [/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit](DYLIBS/OnBoardingKit.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/OnDeviceStorage](DYLIBS/OnDeviceStorage.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/OnDeviceStorageCore](DYLIBS/OnDeviceStorageCore.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageInternal.framework/OnDeviceStorageInternal](DYLIBS/OnDeviceStorageInternal.md)
- [/System/Library/PrivateFrameworks/OpenAPIRuntimeInternal.framework/OpenAPIRuntimeInternal](DYLIBS/OpenAPIRuntimeInternal.md)
- [/System/Library/PrivateFrameworks/OpenAPIURLSessionInternal.framework/OpenAPIURLSessionInternal](DYLIBS/OpenAPIURLSessionInternal.md)
- [/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry](DYLIBS/PairedDeviceRegistry.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/People.framework/People](DYLIBS/People.md)
- [/System/Library/PrivateFrameworks/PersonalSearch.framework/PersonalSearch](DYLIBS/PersonalSearch.md)
- [/System/Library/PrivateFrameworks/PersonalSearchService.framework/PersonalSearchService](DYLIBS/PersonalSearchService.md)
- [/System/Library/PrivateFrameworks/PersonalSearchTypes.framework/PersonalSearchTypes](DYLIBS/PersonalSearchTypes.md)
- [/System/Library/PrivateFrameworks/PersonalizationPortraitInternals.framework/PersonalizationPortraitInternals](DYLIBS/PersonalizationPortraitInternals.md)
- [/System/Library/PrivateFrameworks/PhoneKit.framework/PhoneKit](DYLIBS/PhoneKit.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging](DYLIBS/PhotoImaging.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace](DYLIBS/PhotosFace.md)
- [/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats](DYLIBS/PhotosFormats.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligenceCore.framework/PhotosIntelligenceCore](DYLIBS/PhotosIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/PhotosSpatialMedia.framework/PhotosSpatialMedia](DYLIBS/PhotosSpatialMedia.md)
- [/System/Library/PrivateFrameworks/PhotosSpatialMediaCore.framework/PhotosSpatialMediaCore](DYLIBS/PhotosSpatialMediaCore.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit](DYLIBS/PhotosUIEdit.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PhotosensitivityProcessing.framework/PhotosensitivityProcessing](DYLIBS/PhotosensitivityProcessing.md)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO](DYLIBS/PlatformSSO.md)
- [/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework](DYLIBS/PnROnDeviceFramework.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotSQLite.framework/PoirotSQLite](DYLIBS/PoirotSQLite.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/PostSiriEngagement.framework/PostSiriEngagement](DYLIBS/PostSiriEngagement.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices](DYLIBS/PosterBoardUIServices.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/PredictedContextAlgorithms](DYLIBS/PredictedContextAlgorithms.md)
- [/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended](DYLIBS/PreferencesExtended.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/PreviewsOSSupport](DYLIBS/PreviewsOSSupport.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupportUI.framework/PreviewsOSSupportUI](DYLIBS/PreviewsOSSupportUI.md)
- [/System/Library/PrivateFrameworks/PreviewsServices.framework/PreviewsServices](DYLIBS/PreviewsServices.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/PriMLETL.framework/PriMLETL](DYLIBS/PriMLETL.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute](DYLIBS/PrivateCloudCompute.md)
- [/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning](DYLIBS/PrivateFederatedLearning.md)
- [/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient](DYLIBS/PrivateMLClient.md)
- [/System/Library/PrivateFrameworks/PrivateMLClientInferenceProvider.framework/PrivateMLClientInferenceProvider](DYLIBS/PrivateMLClientInferenceProvider.md)
- [/System/Library/PrivateFrameworks/PrivateSearchCore.framework/PrivateSearchCore](DYLIBS/PrivateSearchCore.md)
- [/System/Library/PrivateFrameworks/ProDisplayLibrary.framework/ProDisplayLibrary](DYLIBS/ProDisplayLibrary.md)
- [/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport](DYLIBS/ProactiveDaemonSupport.md)
- [/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker](DYLIBS/ProactiveEventTracker.md)
- [/System/Library/PrivateFrameworks/ProactivePredictionClient.framework/ProactivePredictionClient](DYLIBS/ProactivePredictionClient.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient](DYLIBS/ProactiveSummarizationClient.md)
- [/System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport](DYLIBS/ProactiveSupport.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentJetClient.framework/PromotedContentJetClient](DYLIBS/PromotedContentJetClient.md)
- [/System/Library/PrivateFrameworks/PromotedContentJetSupport.framework/PromotedContentJetSupport](DYLIBS/PromotedContentJetSupport.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/PromptKit.framework/PromptKit](DYLIBS/PromptKit.md)
- [/System/Library/PrivateFrameworks/ProofReader.framework/ProofReader](DYLIBS/ProofReader.md)
- [/System/Library/PrivateFrameworks/ProtoDataExtractor.framework/ProtoDataExtractor](DYLIBS/ProtoDataExtractor.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetupUI.framework/ProximityAppleIDSetupUI](DYLIBS/ProximityAppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl](DYLIBS/ProximityControl.md)
- [/System/Library/PrivateFrameworks/ProximityReaderCore.framework/ProximityReaderCore](DYLIBS/ProximityReaderCore.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon](DYLIBS/QuickLookThumbnailingDaemon.md)
- [/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting](DYLIBS/RTCReporting.md)
- [/System/Library/PrivateFrameworks/RapidResourceDelivery.framework/RapidResourceDelivery](DYLIBS/RapidResourceDelivery.md)
- [/System/Library/PrivateFrameworks/RealityIO.framework/RealityIO](DYLIBS/RealityIO.md)
- [/System/Library/PrivateFrameworks/Recount.framework/Recount](DYLIBS/Recount.md)
- [/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain](DYLIBS/RegulatoryDomain.md)
- [/System/Library/PrivateFrameworks/ReminderKitInternal.framework/ReminderKitInternal](DYLIBS/ReminderKitInternal.md)
- [/System/Library/PrivateFrameworks/RemindersAppIntents.framework/RemindersAppIntents](DYLIBS/RemindersAppIntents.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore](DYLIBS/RemoteManagementStore.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/Rules.framework/Rules](DYLIBS/Rules.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/SESUIService.framework/SESUIService](DYLIBS/SESUIService.md)
- [/System/Library/PrivateFrameworks/SESUIServiceCore.framework/SESUIServiceCore](DYLIBS/SESUIServiceCore.md)
- [/System/Library/PrivateFrameworks/SEService.framework/SEService](DYLIBS/SEService.md)
- [/System/Library/PrivateFrameworks/SIDFitness.framework/SIDFitness](DYLIBS/SIDFitness.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SOSUI.framework/SOSUI](DYLIBS/SOSUI.md)
- [/System/Library/PrivateFrameworks/SPFinder.framework/SPFinder](DYLIBS/SPFinder.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SPRCore.framework/SPRCore](DYLIBS/SPRCore.md)
- [/System/Library/PrivateFrameworks/SPShared.framework/SPShared](DYLIBS/SPShared.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation](DYLIBS/SafariFoundation.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor](DYLIBS/SafetyMonitor.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/Sage.framework/Sage](DYLIBS/Sage.md)
- [/System/Library/PrivateFrameworks/SampleAnalysis.framework/Frameworks/SAHelper.framework/SAHelper](DYLIBS/SAHelper.md)
- [/System/Library/PrivateFrameworks/SceneIntelligence.framework/SceneIntelligence](DYLIBS/SceneIntelligence.md)
- [/System/Library/PrivateFrameworks/ScreenContinuityServices.framework/ScreenContinuityServices](DYLIBS/ScreenContinuityServices.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenSharingAccessibilityService.framework/ScreenSharingAccessibilityService](DYLIBS/ScreenSharingAccessibilityService.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSwift.framework/ScreenTimeSwift](DYLIBS/ScreenTimeSwift.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchIntrospectionKit.framework/SearchIntrospectionKit](DYLIBS/SearchIntrospectionKit.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SecureCaptureKit.framework/SecureCaptureKit](DYLIBS/SecureCaptureKit.md)
- [/System/Library/PrivateFrameworks/SecureMessaging.framework/SecureMessaging](DYLIBS/SecureMessaging.md)
- [/System/Library/PrivateFrameworks/SecureMessagingAgentCore.framework/SecureMessagingAgentCore](DYLIBS/SecureMessagingAgentCore.md)
- [/System/Library/PrivateFrameworks/SensingAlgsService.framework/SensingAlgsService](DYLIBS/SensingAlgsService.md)
- [/System/Library/PrivateFrameworks/SensingAlgsTouchButtonHost.framework/SensingAlgsTouchButtonHost](DYLIBS/SensingAlgsTouchButtonHost.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML](DYLIBS/SensitiveContentAnalysisML.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/SensorAccess.framework/SensorAccess](DYLIBS/SensorAccess.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/ServicesIntelligence.framework/ServicesIntelligence](DYLIBS/ServicesIntelligence.md)
- [/System/Library/PrivateFrameworks/SessionAlert.framework/SessionAlert](DYLIBS/SessionAlert.md)
- [/System/Library/PrivateFrameworks/SessionAssertion.framework/SessionAssertion](DYLIBS/SessionAssertion.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation](DYLIBS/SessionFoundation.md)
- [/System/Library/PrivateFrameworks/SessionPushNotifications.framework/SessionPushNotifications](DYLIBS/SessionPushNotifications.md)
- [/System/Library/PrivateFrameworks/SessionSQL.framework/SessionSQL](DYLIBS/SessionSQL.md)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI](DYLIBS/PrivacySettingsUI.md)
- [/System/Library/PrivateFrameworks/SettingsHost.framework/SettingsHost](DYLIBS/SettingsHost.md)
- [/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI](DYLIBS/SetupAssistantSupportUI.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourClientServices.framework/SeymourClientServices](DYLIBS/SeymourClientServices.md)
- [/System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore](DYLIBS/SeymourCore.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourServicesCore.framework/SeymourServicesCore](DYLIBS/SeymourServicesCore.md)
- [/System/Library/PrivateFrameworks/SeymourSessionServices.framework/SeymourSessionServices](DYLIBS/SeymourSessionServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShaderGraph.framework/ShaderGraph](DYLIBS/ShaderGraph.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SharingUI.framework/SharingUI](DYLIBS/SharingUI.md)
- [/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore](DYLIBS/ShazamCore.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/ShazamKitUI.framework/ShazamKitUI](DYLIBS/ShazamKitUI.md)
- [/System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit](DYLIBS/ShellSceneKit.md)
- [/System/Library/PrivateFrameworks/ShimGameServices.framework/ShimGameServices](DYLIBS/ShimGameServices.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution](DYLIBS/SiriAppResolution.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/SiriAutoCompleteAPI](DYLIBS/SiriAutoCompleteAPI.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriContactsCommon.framework/SiriContactsCommon](DYLIBS/SiriContactsCommon.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI](DYLIBS/SiriContactsUI.md)
- [/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics](DYLIBS/SiriCoreMetrics.md)
- [/System/Library/PrivateFrameworks/SiriDailyBriefingInternal.framework/SiriDailyBriefingInternal](DYLIBS/SiriDailyBriefingInternal.md)
- [/System/Library/PrivateFrameworks/SiriDialogEngine.framework/SiriDialogEngine](DYLIBS/SiriDialogEngine.md)
- [/System/Library/PrivateFrameworks/SiriEmergencyIntents.framework/SiriEmergencyIntents](DYLIBS/SiriEmergencyIntents.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment](DYLIBS/SiriFlowEnvironment.md)
- [/System/Library/PrivateFrameworks/SiriGeo.framework/SiriGeo](DYLIBS/SiriGeo.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall](DYLIBS/SiriInCall.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferenceFlow.framework/SiriInferenceFlow](DYLIBS/SiriInferenceFlow.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriInteractive.framework/SiriInteractive](DYLIBS/SiriInteractive.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMASPFLTraining.framework/SiriMASPFLTraining](DYLIBS/SiriMASPFLTraining.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessageBus.framework/SiriMessageBus](DYLIBS/SiriMessageBus.md)
- [/System/Library/PrivateFrameworks/SiriMessagesCommon.framework/SiriMessagesCommon](DYLIBS/SiriMessagesCommon.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNLUOverrides.framework/SiriNLUOverrides](DYLIBS/SiriNLUOverrides.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageParsing.framework/SiriNaturalLanguageParsing](DYLIBS/SiriNaturalLanguageParsing.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPhoneIntents.framework/SiriPhoneIntents](DYLIBS/SiriPhoneIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriReaderIntents.framework/SiriReaderIntents](DYLIBS/SiriReaderIntents.md)
- [/System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution](DYLIBS/SiriReferenceResolution.md)
- [/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher](DYLIBS/SiriRequestDispatcher.md)
- [/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/SiriSettingsIntents](DYLIBS/SiriSettingsIntents.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriStates.framework/SiriStates](DYLIBS/SiriStates.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/SiriSuggestionsBaseModel](DYLIBS/SiriSuggestionsBaseModel.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit](DYLIBS/SiriSuggestionsKit.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriSystemCommandsIntents.framework/SiriSystemCommandsIntents](DYLIBS/SiriSystemCommandsIntents.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTimeAlarmInternal.framework/SiriTimeAlarmInternal](DYLIBS/SiriTimeAlarmInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeInternal.framework/SiriTimeInternal](DYLIBS/SiriTimeInternal.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriTurnRestatement.framework/SiriTurnRestatement](DYLIBS/SiriTurnRestatement.md)
- [/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation](DYLIBS/SiriUIActivation.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriUserSegments.framework/SiriUserSegments](DYLIBS/SiriUserSegments.md)
- [/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities](DYLIBS/SiriUtilities.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution](DYLIBS/SiriVirtualDeviceResolution.md)
- [/System/Library/PrivateFrameworks/SiriWellnessIntents.framework/SiriWellnessIntents](DYLIBS/SiriWellnessIntents.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SmartReplies.framework/SmartReplies](DYLIBS/SmartReplies.md)
- [/System/Library/PrivateFrameworks/SmartRepliesServer.framework/SmartRepliesServer](DYLIBS/SmartRepliesServer.md)
- [/System/Library/PrivateFrameworks/SmartStackFoundation.framework/SmartStackFoundation](DYLIBS/SmartStackFoundation.md)
- [/System/Library/PrivateFrameworks/SmartStackSettings.framework/SmartStackSettings](DYLIBS/SmartStackSettings.md)
- [/System/Library/PrivateFrameworks/SmartStackSettingsUI.framework/SmartStackSettingsUI](DYLIBS/SmartStackSettingsUI.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer](DYLIBS/SocialLayer.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI](DYLIBS/SoftwareUpdateSettingsUI.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation](DYLIBS/SoftwareUpdateUIFoundation.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateUIKit.framework/SoftwareUpdateUIKit](DYLIBS/SoftwareUpdateUIKit.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpatialInspectorFoundation.framework/SpatialInspectorFoundation](DYLIBS/SpatialInspectorFoundation.md)
- [/System/Library/PrivateFrameworks/SpeechRecognitionSharedSupport.framework/SpeechRecognitionSharedSupport](DYLIBS/SpeechRecognitionSharedSupport.md)
- [/System/Library/PrivateFrameworks/SpeechTranslation.framework/SpeechTranslation](DYLIBS/SpeechTranslation.md)
- [/System/Library/PrivateFrameworks/SportsKit.framework/SportsKit](DYLIBS/SportsKit.md)
- [/System/Library/PrivateFrameworks/SpotlightUIShared.framework/SpotlightUIShared](DYLIBS/SpotlightUIShared.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/Stateful.framework/Stateful](DYLIBS/Stateful.md)
- [/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore](DYLIBS/StatusKitAgentCore.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/RecencyService.framework/RecencyService](DYLIBS/RecencyService.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/ServiceShared.framework/ServiceShared](DYLIBS/ServiceShared.md)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/PrivateFrameworks/StocksAnalytics.framework/StocksAnalytics](DYLIBS/StocksAnalytics.md)
- [/System/Library/PrivateFrameworks/StocksCore.framework/StocksCore](DYLIBS/StocksCore.md)
- [/System/Library/PrivateFrameworks/StocksKit.framework/StocksKit](DYLIBS/StocksKit.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StorageContainersPrivate.framework/StorageContainersPrivate](DYLIBS/StorageContainersPrivate.md)
- [/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI](DYLIBS/StoreKitUI.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SupportFlowUI.framework/SupportFlowUI](DYLIBS/SupportFlowUI.md)
- [/System/Library/PrivateFrameworks/SupportServices.framework/SupportServices](DYLIBS/SupportServices.md)
- [/System/Library/PrivateFrameworks/SwiftCertificate.framework/SwiftCertificate](DYLIBS/SwiftCertificate.md)
- [/System/Library/PrivateFrameworks/SwiftMLS.framework/SwiftMLS](DYLIBS/SwiftMLS.md)
- [/System/Library/PrivateFrameworks/SwiftUITracingSupport.framework/SwiftUITracingSupport](DYLIBS/SwiftUITracingSupport.md)
- [/System/Library/PrivateFrameworks/SymptomDistribution.framework/SymptomDistribution](DYLIBS/SymptomDistribution.md)
- [/System/Library/PrivateFrameworks/SymptomNetworkDiagnostics.framework/SymptomNetworkDiagnostics](DYLIBS/SymptomNetworkDiagnostics.md)
- [/System/Library/PrivateFrameworks/SymptomNetworkDiagnosticsCore.framework/SymptomNetworkDiagnosticsCore](DYLIBS/SymptomNetworkDiagnosticsCore.md)
- [/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator](DYLIBS/SymptomEvaluator.md)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/Tabi.framework/Tabi](DYLIBS/Tabi.md)
- [/System/Library/PrivateFrameworks/TeaBreeze.framework/TeaBreeze](DYLIBS/TeaBreeze.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyKit.framework/TelephonyKit](DYLIBS/TelephonyKit.md)
- [/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences](DYLIBS/TelephonyPreferences.md)
- [/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC](DYLIBS/TelephonyRPC.md)
- [/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI](DYLIBS/TelephonyUI.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit](DYLIBS/TemplateKit.md)
- [/System/Library/PrivateFrameworks/TerminalToolKit.framework/TerminalToolKit](DYLIBS/TerminalToolKit.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition](DYLIBS/TextRecognition.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechBundleSupport.framework/TextToSpeechBundleSupport](DYLIBS/TextToSpeechBundleSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport](DYLIBS/TextToSpeechVoiceBankingSupport.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/TextUnderstanding.framework/TextUnderstanding](DYLIBS/TextUnderstanding.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingRuntime.framework/TextUnderstandingRuntime](DYLIBS/TextUnderstandingRuntime.md)
- [/System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared](DYLIBS/TextUnderstandingShared.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/ThreatNotificationCore.framework/ThreatNotificationCore](DYLIBS/ThreatNotificationCore.md)
- [/System/Library/PrivateFrameworks/ThreatNotificationUI.framework/ThreatNotificationUI](DYLIBS/ThreatNotificationUI.md)
- [/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam](DYLIBS/Tightbeam.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipKitServices.framework/TipKitServices](DYLIBS/TipKitServices.md)
- [/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore](DYLIBS/TipsCore.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TranslationAPISupport.framework/TranslationAPISupport](DYLIBS/TranslationAPISupport.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/TrustKit.framework/TrustKit](DYLIBS/TrustKit.md)
- [/System/Library/PrivateFrameworks/UIGrounding.framework/UIGrounding](DYLIBS/UIGrounding.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents](DYLIBS/UIIntelligenceIntents.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceInteraction.framework/UIIntelligenceInteraction](DYLIBS/UIIntelligenceInteraction.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent](DYLIBS/UIIntelligenceSupportAgent.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UnifiedMessagingKit.framework/UnifiedMessagingKit](DYLIBS/UnifiedMessagingKit.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UniversalHID.framework/UniversalHID](DYLIBS/UniversalHID.md)
- [/System/Library/PrivateFrameworks/UrchinKit.framework/UrchinKit](DYLIBS/UrchinKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VDAF.framework/VDAF](DYLIBS/VDAF.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideoIntelligence.framework/VideoIntelligence](DYLIBS/VideoIntelligence.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion](DYLIBS/VisionCompanion.md)
- [/System/Library/PrivateFrameworks/VisionCompanionServices.framework/VisionCompanionServices](DYLIBS/VisionCompanionServices.md)
- [/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore](DYLIBS/VisionKitCore.md)
- [/System/Library/PrivateFrameworks/VisualActionPrediction.framework/VisualActionPrediction](DYLIBS/VisualActionPrediction.md)
- [/System/Library/PrivateFrameworks/VisualActionPredictionCore.framework/VisualActionPredictionCore](DYLIBS/VisualActionPredictionCore.md)
- [/System/Library/PrivateFrameworks/VisualActionPredictionSupport.framework/VisualActionPredictionSupport](DYLIBS/VisualActionPredictionSupport.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligenceCore.framework/VisualIntelligenceCore](DYLIBS/VisualIntelligenceCore.md)
- [/System/Library/PrivateFrameworks/VisualIntelligenceUI.framework/VisualIntelligenceUI](DYLIBS/VisualIntelligenceUI.md)
- [/System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization](DYLIBS/VisualLocalization.md)
- [/System/Library/PrivateFrameworks/VisualLookUp.framework/VisualLookUp](DYLIBS/VisualLookUp.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceProcessor.framework/VoiceProcessor](DYLIBS/VoiceProcessor.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/WatchFacesWallpaperSupport](DYLIBS/WatchFacesWallpaperSupport.md)
- [/System/Library/PrivateFrameworks/WeatherAnalytics.framework/WeatherAnalytics](DYLIBS/WeatherAnalytics.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/Welcome.framework/Welcome](DYLIBS/Welcome.md)
- [/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/WiFiSettingsKit](DYLIBS/WiFiSettingsKit.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices](DYLIBS/WorkflowUIServices.md)
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/XOJITExecutor.framework/XOJITExecutor](DYLIBS/XOJITExecutor.md)
- [/System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed](DYLIBS/XPCDistributed.md)
- [/System/Library/PrivateFrameworks/ZeoliteFramework.framework/ZeoliteFramework](DYLIBS/ZeoliteFramework.md)
- [/System/Library/PrivateFrameworks/ZeoliteLanguage.framework/ZeoliteLanguage](DYLIBS/ZeoliteLanguage.md)
- [/System/Library/PrivateFrameworks/_CommunicationsUICore_PosterBoardServices.framework/_CommunicationsUICore_PosterBoardServices](DYLIBS/_CommunicationsUICore_PosterBoardServices.md)
- [/System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI](DYLIBS/_IconServices_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_JetUI_SwiftUI.framework/_JetUI_SwiftUI](DYLIBS/_JetUI_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_OnDeviceStorage_JavaScriptCore.framework/_OnDeviceStorage_JavaScriptCore](DYLIBS/_OnDeviceStorage_JavaScriptCore.md)
- [/System/Library/PrivateFrameworks/_SonicKit_MusicKit.framework/_SonicKit_MusicKit](DYLIBS/_SonicKit_MusicKit.md)
- [/System/Library/PrivateFrameworks/iCloudMailAssistant.framework/iCloudMailAssistant](DYLIBS/iCloudMailAssistant.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI](DYLIBS/iCloudQuotaUI.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/System/Library/PrivateFrameworks/iTunesStoreUI.framework/iTunesStoreUI](DYLIBS/iTunesStoreUI.md)
- [/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSUtility.framework/TSUtility](DYLIBS/TSUtility.md)
- [/System/Library/PrivateFrameworks/icloudMCCKit.framework/icloudMCCKit](DYLIBS/icloudMCCKit.md)
- [/System/Library/PrivateFrameworks/ktrace.framework/ktrace](DYLIBS/ktrace.md)
- [/System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime](DYLIBS/lighthouse_runtime.md)
- [/System/Library/TextInput/TextInput_th.bundle/TextInput_th](DYLIBS/TextInput_th.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libNFC_Comet.dylib](DYLIBS/libNFC_Comet.dylib.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)
- [/usr/lib/libimage4.dylib](DYLIBS/libimage4.dylib.md)
- [/usr/lib/libmis.dylib](DYLIBS/libmis.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftAppleArchive.dylib](DYLIBS/libswiftAppleArchive.dylib.md)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib.md)
- [/usr/lib/swift/libswiftCoreAudio_Private.dylib](DYLIBS/libswiftCoreAudio_Private.dylib.md)
- [/usr/lib/swift/libswiftCoreLocation.dylib](DYLIBS/libswiftCoreLocation.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftDispatch.dylib](DYLIBS/libswiftDispatch.dylib.md)
- [/usr/lib/swift/libswiftDistributed.dylib](DYLIBS/libswiftDistributed.dylib.md)
- [/usr/lib/swift/libswiftModelIO.dylib](DYLIBS/libswiftModelIO.dylib.md)
- [/usr/lib/swift/libswiftPassKit.dylib](DYLIBS/libswiftPassKit.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftSynchronization.dylib](DYLIBS/libswiftSynchronization.dylib.md)
- [/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib](DYLIBS/libswiftUniformTypeIdentifiers.dylib.md)
- [/usr/lib/swift/libswiftVideoToolbox.dylib](DYLIBS/libswiftVideoToolbox.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_Concurrency.dylib](DYLIBS/libswift_Concurrency.dylib.md)
- [/usr/lib/swift/libswiftos.dylib](DYLIBS/libswiftos.dylib.md)
- [/usr/lib/swift/libswiftsimd.dylib](DYLIBS/libswiftsimd.dylib.md)
- [/usr/lib/usd/libusd_ms.dylib](DYLIBS/libusd_ms.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (106)

<details>
  <summary><i>View Files</i></summary>

- `/private/var/staged_system_apps/Freeform.app/ar.lproj/nlu.appintents/47506e0398e585fecf60be4331831599.version`
- `/private/var/staged_system_apps/Freeform.app/bg.lproj/nlu.appintents/7528372123826696b20583638fbd1563.version`
- `/private/var/staged_system_apps/Freeform.app/bn.lproj/nlu.appintents/e6557ba9b5abcdf2ede774941bd1076b.version`
- `/private/var/staged_system_apps/Freeform.app/ca.lproj/nlu.appintents/9cfb32f739f50ee55d5342bb07645c15.version`
- `/private/var/staged_system_apps/Freeform.app/cs.lproj/nlu.appintents/12403e73efe41bc1afd0050991180572.version`
- `/private/var/staged_system_apps/Freeform.app/da.lproj/nlu.appintents/8d3ed31f823db3db95176d15eda5c991.version`
- `/private/var/staged_system_apps/Freeform.app/de.lproj/nlu.appintents/fa2cbcff98c3eb3ad8bd5e84760821fe.version`
- `/private/var/staged_system_apps/Freeform.app/el.lproj/nlu.appintents/3114539561587c2c8baf24f283519202.version`
- `/private/var/staged_system_apps/Freeform.app/en.lproj/nlu.appintents/23a1ad28ed33f1bf35515337f3f365b1.version`
- `/private/var/staged_system_apps/Freeform.app/en_AU.lproj/nlu.appintents/5948f67279f2ebc33cc89b82a0c0ab60.version`
- `/private/var/staged_system_apps/Freeform.app/en_GB.lproj/nlu.appintents/b94e530bfe688727c554ec494f3b9363.version`
- `/private/var/staged_system_apps/Freeform.app/en_IN.lproj/nlu.appintents/fb7da95dadb53682addbc69c4689d075.version`
- `/private/var/staged_system_apps/Freeform.app/es.lproj/nlu.appintents/51005e34f03cc34717e2ac199f7b6f06.version`
- `/private/var/staged_system_apps/Freeform.app/es_419.lproj/nlu.appintents/c0da685edeb177e97bee05a5feda648f.version`
- `/private/var/staged_system_apps/Freeform.app/es_US.lproj/nlu.appintents/1a0335f21a44b345fbc7c0314744ef80.version`
- `/private/var/staged_system_apps/Freeform.app/fi.lproj/nlu.appintents/ef396e223c01bf7a84690a82253f265c.version`
- `/private/var/staged_system_apps/Freeform.app/fr.lproj/nlu.appintents/f1f707022b0ba53cd3f9ee58809db028.version`
- `/private/var/staged_system_apps/Freeform.app/fr_CA.lproj/nlu.appintents/9e69349755e405392ee258118cf94af0.version`
- `/private/var/staged_system_apps/Freeform.app/gu.lproj/nlu.appintents/38b0e7ecbf1cd6fda9fdeef2287e0c32.version`
- `/private/var/staged_system_apps/Freeform.app/he.lproj/nlu.appintents/556eca240d7351bdcc345116695f775a.version`
- `/private/var/staged_system_apps/Freeform.app/hi.lproj/nlu.appintents/cc93160843b4df03486ec435f321a63c.version`
- `/private/var/staged_system_apps/Freeform.app/hr.lproj/nlu.appintents/6478f816acae1216e1eb368d656b199b.version`
- `/private/var/staged_system_apps/Freeform.app/hu.lproj/nlu.appintents/a3177e1d03cf45befdffbffee4af8dc1.version`
- `/private/var/staged_system_apps/Freeform.app/id.lproj/nlu.appintents/ba81d908d6e77bf023667f18b062bb61.version`
- `/private/var/staged_system_apps/Freeform.app/it.lproj/nlu.appintents/7652f332bb94fc965cea187921404a0e.version`
- `/private/var/staged_system_apps/Freeform.app/ja.lproj/nlu.appintents/9584ae65919e0bd91ce0a5528b189c65.version`
- `/private/var/staged_system_apps/Freeform.app/kk.lproj/nlu.appintents/f013a5d388620bba841d8be548101118.version`
- `/private/var/staged_system_apps/Freeform.app/kn.lproj/nlu.appintents/6f7835a98a636d608e83b5fe4f3ff3de.version`
- `/private/var/staged_system_apps/Freeform.app/ko.lproj/nlu.appintents/abd17eb9f97b61e0aac554c9dfb80986.version`
- `/private/var/staged_system_apps/Freeform.app/lt.lproj/nlu.appintents/919cc8d456e101b1169d602948023af3.version`
- `/private/var/staged_system_apps/Freeform.app/ml.lproj/nlu.appintents/dbc889fc5ecc4954af9aa58edb927d0b.version`
- `/private/var/staged_system_apps/Freeform.app/mr.lproj/nlu.appintents/cd6b925c233c49b867612b984565d5e0.version`
- `/private/var/staged_system_apps/Freeform.app/ms.lproj/nlu.appintents/cb0eebca7c1620a9b8bc1240351c1bbf.version`
- `/private/var/staged_system_apps/Freeform.app/nl.lproj/nlu.appintents/db90ed05cb149e0bb72ed5c7b6b5c162.version`
- `/private/var/staged_system_apps/Freeform.app/no.lproj/nlu.appintents/210e448175550651e23b9cbecfdfc935.version`
- `/private/var/staged_system_apps/Freeform.app/or.lproj/nlu.appintents/d677f78915d49ab9b5c1d4c1d54d55c4.version`
- `/private/var/staged_system_apps/Freeform.app/pa.lproj/nlu.appintents/a3f0d55e4045cf312ef8d466258b9ecc.version`
- `/private/var/staged_system_apps/Freeform.app/pl.lproj/nlu.appintents/5b75f6ecaed16385aa210584bec7634e.version`
- `/private/var/staged_system_apps/Freeform.app/pt_BR.lproj/nlu.appintents/6b6655f422954d8970897f195e6d4772.version`
- `/private/var/staged_system_apps/Freeform.app/ro.lproj/nlu.appintents/e619df38ef181890c96796bbb0d3bb46.version`
- `/private/var/staged_system_apps/Freeform.app/ru.lproj/nlu.appintents/3d4e81d8a77ff684b56c6cfe6a440d48.version`
- `/private/var/staged_system_apps/Freeform.app/sk.lproj/nlu.appintents/8c59925f9dc242b318c17305e9a0d8d1.version`
- `/private/var/staged_system_apps/Freeform.app/sl.lproj/nlu.appintents/fbe741cd6b3080bb159182250cda6ee1.version`
- `/private/var/staged_system_apps/Freeform.app/sv.lproj/nlu.appintents/9a6866758ea9750b7a8d8b0af60b87b0.version`
- `/private/var/staged_system_apps/Freeform.app/ta.lproj/nlu.appintents/35e562c00dc861e41fc81d2623dbace0.version`
- `/private/var/staged_system_apps/Freeform.app/th.lproj/nlu.appintents/4cd62eda20a228d28236ec7f98395f43.version`
- `/private/var/staged_system_apps/Freeform.app/tr.lproj/nlu.appintents/7583a351b1305a09d3a436c19ff760ed.version`
- `/private/var/staged_system_apps/Freeform.app/uk.lproj/nlu.appintents/258a1eb3b0f34290755c1ba58a8dbe86.version`
- `/private/var/staged_system_apps/Freeform.app/ur.lproj/nlu.appintents/3295e475b276c20ae1030d7ec75fa245.version`
- `/private/var/staged_system_apps/Freeform.app/vi.lproj/nlu.appintents/527667dc9faa5833743a51d14d60d45d.version`
- `/private/var/staged_system_apps/Freeform.app/zh_CN.lproj/nlu.appintents/9d9f42c608999efeca35395910974702.version`
- `/private/var/staged_system_apps/Freeform.app/zh_HK.lproj/nlu.appintents/ccf0d81417f3845db685df286236aa54.version`
- `/private/var/staged_system_apps/Freeform.app/zh_TW.lproj/nlu.appintents/dbd5915fd27416d18fb2f8efa94674d5.version`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/38bb1ceb051ff583e666f458e7667e8d.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/7e1d2e70c221a11b1b3685d2ae5d5f48.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/d122bf70bd48f411cd46f89503a676cd.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/74cde225dbe688828c42bf975d75d12b.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/309fcfb3acf8e49c06c7942ffe1cded6.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/9e62f4cd93000fd42008ad985e674ba5.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/5be738ec1199e74ec051133931d74c92.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/639b3b75f1f8e6e306991906881204c0.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/ccdff8159499afe914f2cfe27c9fe84c.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/fdeb14b2d18d41837742bd9375cf2f70.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/fee78c6e3eb2875d6bfb311af8b2c486.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/8127bc571ab04722a22e7556ddf64654.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/d0017f7f30b2b6bb01ace2d62106ffe3.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/6d6ba6a361a8c2be82d250ec7c4d15ae.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/c5eed8bc8a075607d8d6a6a354be83fd.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/0960c8534f525ccb207827dd72a63ee6.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/20d9ff8d45337fc54304e631fd10abe7.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/5eb024bd0825142c85de6604a6ecfe55.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/688760864c12764683fc60f42a675834.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/2a1c612010d491c9b17f684ba266fbf0.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/b75ab09a173497a7ce00e026fd3c8bc5.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/6bd314646e2dc18eadaec71364d20a21.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/cc17b22d2eedf4460657d29ac34ed0fc.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/9d116a0ae76042435a0dcafed031abce.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/f20adb694a354baf6a1bfe110d68987f.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/07a38c4417886a139d69f5e8707dad1b.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/f48812c6b40a89b97dad41a2aba4ce04.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/ad4884de48c57ddaf620888eec88f327.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/de54065f21a71458d02bef27d0b075e3.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/cc40521c9ea4c99255e4a95667f48e1e.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/c6714f74db2a469f1a74a95437328d83.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/d9813ac3ad42e9d08ef4bf613f26234f.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/6d5de7a943ebda61c07c0ac2d67292c4.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/6651ff487f5e9ebf9c4c7b545897f1c0.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/df4aa841256bf9622519961732a15e19.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/ac47e6476eeb558581241fa34406144f.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/0ba6e86c9769e4eabf77b2e4c94b8650.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/1af64e85a7c2217f77f9f29f0f54e9a5.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/306d61cedcb289c150e5fd023a129ee0.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/d27f81177a7e5a885262c2bfb1f9e94c.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/7bbbb11b2712d85958eec2822c1fcb74.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/582260375db26897ddcb27f1861f4da5.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/12e736c219052ecd4e7720ee75ddc8bb.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/a574c401a7167dc36ffef16f1602d574.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/89e2f14d466f8a1b7a16e6589e7615da.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/f14a8ec5fbd2e34d44537928f2fa3062.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/9b44c126b47e14b4b1807ea52c579bfd.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/d0e9e0e8de0ccd186ff001c712f4b149.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/29ac0b6d6c5b686a5a80bf6549ddee2c.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/945b2d187cd0c4c5041e5da066e1bbbb.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/215155935fa7c595ebcaf09b06b4454d.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/296b072a19a3ad5ae7c595c641382bee.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/e28bc0a3d74349420ffbd3648f36d945.version`

</details>

### ❌ Removed

#### filesystem (106)

<details>
  <summary><i>View Files</i></summary>

- `/private/var/staged_system_apps/Freeform.app/ar.lproj/nlu.appintents/f1794c5dcd455b34101124b08a02ffca.version`
- `/private/var/staged_system_apps/Freeform.app/bg.lproj/nlu.appintents/20d8c01204bd3a62acadb488c224f11c.version`
- `/private/var/staged_system_apps/Freeform.app/bn.lproj/nlu.appintents/b8d9d9c9ac6e0d820c6aac1f3b84a29d.version`
- `/private/var/staged_system_apps/Freeform.app/ca.lproj/nlu.appintents/fb8b8bab84a7e64b5502193e709e05f0.version`
- `/private/var/staged_system_apps/Freeform.app/cs.lproj/nlu.appintents/3f46b58ec4efe915a4b9bf1bdae26de5.version`
- `/private/var/staged_system_apps/Freeform.app/da.lproj/nlu.appintents/86d688c4992c51861e88b273635a056b.version`
- `/private/var/staged_system_apps/Freeform.app/de.lproj/nlu.appintents/2c02fab707647d80fc48bb7bb4805717.version`
- `/private/var/staged_system_apps/Freeform.app/el.lproj/nlu.appintents/9959e75af3095d31e3b8fa2ab180cf71.version`
- `/private/var/staged_system_apps/Freeform.app/en.lproj/nlu.appintents/f05824709eb35f10271519495f32f4df.version`
- `/private/var/staged_system_apps/Freeform.app/en_AU.lproj/nlu.appintents/9021ee418d9283349723ce3cd8d482bf.version`
- `/private/var/staged_system_apps/Freeform.app/en_GB.lproj/nlu.appintents/919860d42eaac599623589f6facf1f23.version`
- `/private/var/staged_system_apps/Freeform.app/en_IN.lproj/nlu.appintents/6c95c5ba78f46ee39d2da0c6b6ab92bd.version`
- `/private/var/staged_system_apps/Freeform.app/es.lproj/nlu.appintents/5053711a3219f6fc649d092e6f726e54.version`
- `/private/var/staged_system_apps/Freeform.app/es_419.lproj/nlu.appintents/29abe9d23e712829374808fdbe96f57d.version`
- `/private/var/staged_system_apps/Freeform.app/es_US.lproj/nlu.appintents/e94d8feec0df9621f220941a25c0377c.version`
- `/private/var/staged_system_apps/Freeform.app/fi.lproj/nlu.appintents/ced70a6774b0b9fcb03c5f9fe16c41dc.version`
- `/private/var/staged_system_apps/Freeform.app/fr.lproj/nlu.appintents/af11d7053fc5ea1c028074010a29bbeb.version`
- `/private/var/staged_system_apps/Freeform.app/fr_CA.lproj/nlu.appintents/33a71bd2e65614cf182dae7fc3c5cf31.version`
- `/private/var/staged_system_apps/Freeform.app/gu.lproj/nlu.appintents/20f094e53f2e3917b2a77e01022a50b6.version`
- `/private/var/staged_system_apps/Freeform.app/he.lproj/nlu.appintents/81a51cf7f33f3944fe1c9574f3f7a13d.version`
- `/private/var/staged_system_apps/Freeform.app/hi.lproj/nlu.appintents/e1fb3613db347e0ab7d9ff3e0b1c42e2.version`
- `/private/var/staged_system_apps/Freeform.app/hr.lproj/nlu.appintents/4c0b4fe9c6de9c0066f55bc95828416f.version`
- `/private/var/staged_system_apps/Freeform.app/hu.lproj/nlu.appintents/b2f2bd0e8e9b21161b63e4e3ac94dae7.version`
- `/private/var/staged_system_apps/Freeform.app/id.lproj/nlu.appintents/b54476db139e76d3c613cc928c5376d3.version`
- `/private/var/staged_system_apps/Freeform.app/it.lproj/nlu.appintents/516effe66113c938c1c28029763b1317.version`
- `/private/var/staged_system_apps/Freeform.app/ja.lproj/nlu.appintents/df8a9f8b889a030c9d3a9173baa1b05f.version`
- `/private/var/staged_system_apps/Freeform.app/kk.lproj/nlu.appintents/0a7b12a574dce57b086450497f116e04.version`
- `/private/var/staged_system_apps/Freeform.app/kn.lproj/nlu.appintents/d55c59ce75dfd4ddc961ea62a21a2888.version`
- `/private/var/staged_system_apps/Freeform.app/ko.lproj/nlu.appintents/13a81dfed8137e2a9d862d9a66bccfcd.version`
- `/private/var/staged_system_apps/Freeform.app/lt.lproj/nlu.appintents/b2b72b5e038acd6db1b94b29f5fcf72f.version`
- `/private/var/staged_system_apps/Freeform.app/ml.lproj/nlu.appintents/3872f499175db20eb7b28054ea0ea52a.version`
- `/private/var/staged_system_apps/Freeform.app/mr.lproj/nlu.appintents/32a808dd32fbf4747b5f79ee922b5ee9.version`
- `/private/var/staged_system_apps/Freeform.app/ms.lproj/nlu.appintents/97b3d041a397dcc41c8f5babbbaa1738.version`
- `/private/var/staged_system_apps/Freeform.app/nl.lproj/nlu.appintents/2e566a66deb04288a221825a22ba70fc.version`
- `/private/var/staged_system_apps/Freeform.app/no.lproj/nlu.appintents/589257dee54b4b0f8cecaca3219714a3.version`
- `/private/var/staged_system_apps/Freeform.app/or.lproj/nlu.appintents/da6303786dac314c7dda17b58c05dbe1.version`
- `/private/var/staged_system_apps/Freeform.app/pa.lproj/nlu.appintents/2e4f9e4e28093e08be1660fb0879e774.version`
- `/private/var/staged_system_apps/Freeform.app/pl.lproj/nlu.appintents/91484b74ee15dbf5be78ecc7576852ef.version`
- `/private/var/staged_system_apps/Freeform.app/pt_BR.lproj/nlu.appintents/22ec16fbd4172984978eb476f20d7f8f.version`
- `/private/var/staged_system_apps/Freeform.app/ro.lproj/nlu.appintents/7fbcc4813f562ddbd1283f31106e8083.version`
- `/private/var/staged_system_apps/Freeform.app/ru.lproj/nlu.appintents/c7c37b47a8e0dabdd739196e25ade5b9.version`
- `/private/var/staged_system_apps/Freeform.app/sk.lproj/nlu.appintents/5413134bec449f8a9b4203a54691a7e9.version`
- `/private/var/staged_system_apps/Freeform.app/sl.lproj/nlu.appintents/27835a2f91d3cc888b0de4f1a6a8bd35.version`
- `/private/var/staged_system_apps/Freeform.app/sv.lproj/nlu.appintents/0cbf355bd1e15367ef48ad360e573dd6.version`
- `/private/var/staged_system_apps/Freeform.app/ta.lproj/nlu.appintents/15a164932f27a67a0c887f13d9dabcf8.version`
- `/private/var/staged_system_apps/Freeform.app/th.lproj/nlu.appintents/cde25ae8022283b68b73358b6e6a03df.version`
- `/private/var/staged_system_apps/Freeform.app/tr.lproj/nlu.appintents/33fa7bf3bce8319f96ac7033c1b0bfc6.version`
- `/private/var/staged_system_apps/Freeform.app/uk.lproj/nlu.appintents/2ca9dba9d72efe896946d3c0887fd0b1.version`
- `/private/var/staged_system_apps/Freeform.app/ur.lproj/nlu.appintents/dac1a4c34ee5c7019fcdf2a3f2bbac1d.version`
- `/private/var/staged_system_apps/Freeform.app/vi.lproj/nlu.appintents/8a8a5365c6c683f4fb7242203bfa3e30.version`
- `/private/var/staged_system_apps/Freeform.app/zh_CN.lproj/nlu.appintents/0a83309c2d439b519c7f42b74bce2697.version`
- `/private/var/staged_system_apps/Freeform.app/zh_HK.lproj/nlu.appintents/d067591d5edce4434cbe3d2145fdaf19.version`
- `/private/var/staged_system_apps/Freeform.app/zh_TW.lproj/nlu.appintents/ec5bdb4e496d5f01271300b728fce894.version`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/7c4426a648be2f3175a8649127be7dc0.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/89dc96b23a10c31cf7875f692f0f48e5.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/dc056b1381b97969f1e0707eb676d566.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/f9bb3749bdfbf7b3141b4a94e25f7dc2.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/5bb6a2cbdc7ce714c396b5f39f599b29.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/6d61c4215ee6d8cab4d7c5708800c22f.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/412d70ae9591b48739e037e9a61dedde.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/a54d1870b885258277b3c879ff88c244.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/2b92083da3a0a6d38bf5267a50ae600d.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/2f5467962d38c01ebdea640ed66e8a6f.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/72735ce985286f759ff8f2190ea4dc2f.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/bd82a9f3577b9e19f244519e3a774387.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/21932b530499a4961850d5d1faac6014.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/469af67a377afa789e78e116b6613955.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/2b095a6236717ecf76240863c7911cfd.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/67121d51f236a07261c5499c7d467284.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/327c57fd40adad8522e2d6791a62edb7.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/e128093d664b64631362aa601bce28f2.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/eadf96477d5bc063332d3f90826a52de.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/5e540839654393fd8cfe35d77c01f969.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/1340e2ba7b2b79976b7c897e3f323e6b.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/3ed8c8c9c62d581e1afa74d1151356b2.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/1b21c6824df37b931bf0f47bcd2ba072.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/fa4cadd3697845e7ac6d63c5cbc2bdfc.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/a6b1a1451b8d32a2e8d7208dc5a71605.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/a6747ab27560be28fca60b96966808f4.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/b81370862edcb18f7287b64724b15a69.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/b06a8e64f62cfe8f80343c3c3a2addd8.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/f68552d59debe79082748a0e91a2ad6f.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/213118c1aa5d684da7ddad02641c9341.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/c0041e797859a576d9cdb1289693468b.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/c659fe9a555d189c8ee11b8d1e261099.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/1a38f3b6f488113d74e200c9bf88ae6c.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/c18e209e39af46dca74f1bd8fd183f99.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/20446a4524a5ce19b17ec9c69d1e4fcd.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/e3437675b3ebc9dd0dcfcc7d3c1134e9.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/a30c339a73a29b71629f0a1365a5f15b.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/a8d3ad4b329be9ec801fc898ca8f6167.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/06c7121d5254df23135a33fa1dfb9c38.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/bb6bd8378296fe52faa1381b633f0952.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/67a1f9b6a252dca5e2eab5c3432b5ed4.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/c96501450bd74abc641602b020cc1f2e.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/44c30548e97e2536272aef5aaa7795c7.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/0ebe86ee21a8944451496f2f423d8b73.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/0874902dca211afaaec9d19c7c52fcd9.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/e5f90dcd20c6e0b324c8b2078969e1ac.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/9ae7de64f3614095d13c0966b4fddc90.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/ae86e3405115da256837c62758a34001.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/090d278c21ed9125cd829823881ac154.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/87197f7169cf39f53a60395c91af5356.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/9dd25a4bf7ae42711f75a2e928361f6b.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/43428f806f9f990935f490dcb2ab1ab8.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/fa94865b6d2eeebd9e6a94dd869b9731.version`

</details>

## EOF
