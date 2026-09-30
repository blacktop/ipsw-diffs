# 18.5 (22F5053j) .vs 18.5 (22F5068a)

## IPSWs

- `iPhone17,1_18.5_22F5053j_Restore.ipsw`
- `iPhone17,1_18.5_22F5068a_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.5 *(22F5053j)* | 24.5.0 | 11417.120.105.502.1~1 | Tue, 15Apr2025 21:27:46 PDT |
| 18.5 *(22F5068a)* | 24.5.0 | 11417.122.4~2 | Tue, 22Apr2025 21:26:13 PDT |

### Kexts

#### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.AGXFirmwareKextG17PRTBuddy`

```diff

-328.2.0.0.0
-  __TEXT.__const: 0x33c
+328.3.0.0.0
+  __TEXT.__const: 0x2f4
   __TEXT.__cstring: 0x67a
-  __TEXT_EXEC.__text: 0x2ea8
+  __TEXT_EXEC.__text: 0x2e90
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x38

```

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.120.11.0.0
+938.120.13.0.0
   __TEXT.__cstring: 0xb0d5
-  __TEXT.__const: 0x1560
+  __TEXT.__const: 0x1580
   __TEXT.__os_log: 0x32d
-  __TEXT_EXEC.__text: 0x26a54
+  __TEXT_EXEC.__text: 0x26a70
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x402
   __DATA.__common: 0xb0
CStrings:
+ "21:06:35"
+ "Apr 22 2025"
- "21:12:19"
- "Apr 15 2025"

```

>  `com.apple.driver.AppleUSBAudio`

```diff

-750.3.0.0.0
+750.4.0.0.0
   __TEXT.__cstring: 0x2dfd
   __TEXT.__const: 0x648
-  __TEXT_EXEC.__text: 0x787ec
+  __TEXT_EXEC.__text: 0x787f4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x628

```

>  `com.apple.kernel`

```diff

-11417.120.105.502.1
-  __TEXT.__const: 0x34550
+11417.122.4.0.0
+  __TEXT.__const: 0x34540
   __TEXT.__copyio_vectors: 0xf0
   __TEXT.__cstring: 0x7685a
   __TEXT.__os_log: 0x2a68a

   __DATA_CONST.__brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xcc8
-  __TEXT_EXEC.__text: 0x828c5c
+  __TEXT_EXEC.__text: 0x828c68
   __TEXT_BOOT_EXEC.__bootcode: 0x514c
   __KLD.__text: 0x1638
   __LASTDATA_CONST.__mod_init_func: 0x8

   __DATA.__data: 0x185c1
   __DATA.__lock_grp: 0x5a68
   __DATA.__percpu: 0x6e90
-  __DATA.__common: 0x5bd10
+  __DATA.__common: 0x5bd30
   __DATA.__bss: 0x96258
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__init_entry_set: 0x111f0

```

>  `com.apple.security.sandbox`

```diff

-2401.120.23.0.0
+2401.122.2.0.0
   __TEXT.__os_log: 0x2092
-  __TEXT.__const: 0x1b9b39
+  __TEXT.__const: 0x1b9a99
   __TEXT.__cstring: 0x71c6
-  __TEXT_EXEC.__text: 0x315a4
+  __TEXT_EXEC.__text: 0x31510
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x15430

   __DATA_CONST.__const: 0x35f0
   __DATA_CONST.__kalloc_type: 0xb40
   __DATA_CONST.__kalloc_var: 0x4b0
-  Functions: 638
+  Functions: 637
   Symbols:   0
   CStrings:  1322
 

```

</details>

## MachO

### ⬆️ Updated (293)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService](MACHOS/AppleIDSetupUIService.md)
- [/Applications/AskPermissionUI.app/AskPermissionUI](MACHOS/AskPermissionUI.md)
- [/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension](MACHOS/AskToMessagesExtension.md)
- [/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business](MACHOS/Business.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/ClockAngel.app/ClockAngel](MACHOS/ClockAngel.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/CoreAuthUI.app/CoreAuthUI](MACHOS/CoreAuthUI.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/EventViewService.app/EventViewService](MACHOS/EventViewService.md)
- [/Applications/FTMInternal-4.app/FTMInternal-4](MACHOS/FTMInternal-4.md)
- [/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS](MACHOS/Feedback_Assistant_iOS.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets](MACHOS/GCWidgets.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/MediaRemoteUI.app/MediaRemoteUI](MACHOS/MediaRemoteUI.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/Applications/MomentsUIService.app/MomentsUIService](MACHOS/MomentsUIService.md)
- [/Applications/MusicRecognition.app/MusicRecognition](MACHOS/MusicRecognition.md)
- [/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService](MACHOS/NewDeviceSetupUIService.md)
- [/Applications/PCViewService.app/PCViewService](MACHOS/PCViewService.md)
- [/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime](MACHOS/PeopleMessagesScreenTime.md)
- [/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension](MACHOS/PeopleWidget_iOSExtension.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/PreviewShell.app/PreviewShell](MACHOS/PreviewShell.md)
- [/Applications/SMS Filter.app/PlugIns/extensionFilter.appex/extensionFilter](MACHOS/extensionFilter.md)
- [/Applications/SOSBuddy.app/SOSBuddy](MACHOS/SOSBuddy.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension](MACHOS/ScreenTimeWidgetExtension.md)
- [/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension](MACHOS/ScreenTimeWidgetIntentsExtension.md)
- [/Applications/ScreenContinuityShell.app/ScreenContinuityShell](MACHOS/ScreenContinuityShell.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/ShazamEventsApp.app/ShazamEventsApp](MACHOS/ShazamEventsApp.md)
- [/Applications/Sidecar.app/PlugIns/ContinuityDisplay.appex/ContinuityDisplay](MACHOS/ContinuityDisplay.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/Applications/TDGSharingViewService.app/TDGSharingViewService](MACHOS/TDGSharingViewService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/Applications/TirePressure.app/TirePressure](MACHOS/TirePressure.md)
- [/Applications/WritingToolsUIService.app/WritingToolsUIService](MACHOS/WritingToolsUIService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/ExclaveKit/usr/lib/dyld](MACHOS/dyld.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AlarmFlowPlugin.bundle/AlarmFlowPlugin](MACHOS/AlarmFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin](MACHOS/AudioFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin](MACHOS/DailyBriefingFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/EmergencyFlowPlugin.bundle/EmergencyFlowPlugin](MACHOS/EmergencyFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/HealthFlowDelegatePlugin.bundle/HealthFlowDelegatePlugin](MACHOS/HealthFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin](MACHOS/IFFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/PhoneCallFlowDelegatePlugin.bundle/PhoneCallFlowDelegatePlugin](MACHOS/PhoneCallFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SiriLinkFlowPlugin.bundle/SiriLinkFlowPlugin](MACHOS/SiriLinkFlowPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/SocialConversationFlowDelegatePlugin](MACHOS/SocialConversationFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/TimerFlowDelegatePlugin.bundle/TimerFlowDelegatePlugin](MACHOS/TimerFlowDelegatePlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/WellnessFlowPlugin.bundle/WellnessFlowPlugin](MACHOS/WellnessFlowPlugin.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningInferencePlugin.bundle/SiriPrivateLearningInferencePlugin](MACHOS/SiriPrivateLearningInferencePlugin.md)
- [/System/Library/Assistant/PrivateLearningPlugins/SiriPrivateLearningTTSMispronunciationPlugin.bundle/SiriPrivateLearningTTSMispronunciationPlugin](MACHOS/SiriPrivateLearningTTSMispronunciationPlugin.md)
- [/System/Library/Assistant/UIPlugins/Maps.siriUIBundle/Maps](MACHOS/Maps.md)
- [/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/LiveTranscriptionUI.app/LiveTranscriptionUI](MACHOS/LiveTranscriptionUI.md)
- [/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension](MACHOS/AccessibilityControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/AppleAccountIntents.appex/AppleAccountIntents](MACHOS/AppleAccountIntents.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents](MACHOS/DocumentAppIntents.md)
- [/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/FamilyIntents](MACHOS/FamilyIntents.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA](MACHOS/FedStatsMLHostPluginClassA.md)
- [/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB](MACHOS/FedStatsMLHostPluginClassB.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/ExtensionKit/Extensions/KeyboardSettingsExtension.appex/KeyboardSettingsExtension](MACHOS/KeyboardSettingsExtension.md)
- [/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension](MACHOS/MercuryPosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin](MACHOS/PrivateEvolutionPlugin.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension](MACHOS/SearchToolExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/Frameworks/AutomatedDeviceEnrollment.framework/PlugIns/AddDevicesToAutomatedDeviceEnrollmentExtension.appex/AddDevicesToAutomatedDeviceEnrollmentExtension](MACHOS/AddDevicesToAutomatedDeviceEnrollmentExtension.md)
- [/System/Library/Frameworks/ContactsUI.framework/PlugIns/MonogramPosterExtension.appex/MonogramPosterExtension](MACHOS/MonogramPosterExtension.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent](MACHOS/FamilyControlsAgent.md)
- [/System/Library/Frameworks/FamilyControls.framework/PlugIns/ActivityPickerExtension.appex/ActivityPickerExtension](MACHOS/ActivityPickerExtension.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPushButton.bundle/MechPushButton](MACHOS/MechPushButton.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.screenpicker.appex/com.apple.UIKit.screenpicker](MACHOS/com.apple.UIKit.screenpicker.md)
- [/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService](MACHOS/DeviceActivityReportService.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/SMS.imservice/SMS](MACHOS/SMS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup](MACHOS/ActivityBridgeSetup.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion](MACHOS/DepthComplicationBundleCompanion.md)
- [/System/Library/PreferenceBundles/AccountSettings/icloudMailSettings.bundle/icloudMailSettings](MACHOS/icloudMailSettings.md)
- [/System/Library/PreferenceBundles/AdAttributionKitDeveloperSettings.bundle/AdAttributionKitDeveloperSettings](MACHOS/AdAttributionKitDeveloperSettings.md)
- [/System/Library/PreferenceBundles/AirDropSettings.bundle/AirDropSettings](MACHOS/AirDropSettings.md)
- [/System/Library/PreferenceBundles/AppClipDeveloperSettings.bundle/AppClipDeveloperSettings](MACHOS/AppClipDeveloperSettings.md)
- [/System/Library/PreferenceBundles/CarKitSettings.bundle/CarKitSettings](MACHOS/CarKitSettings.md)
- [/System/Library/PreferenceBundles/GameControlleriOSSettings.bundle/GameControlleriOSSettings](MACHOS/GameControlleriOSSettings.md)
- [/System/Library/PreferenceBundles/InternationalSettings.bundle/InternationalSettings](MACHOS/InternationalSettings.md)
- [/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings](MACHOS/JournalSettings.md)
- [/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/MultitaskingAndGesturesSettings](MACHOS/MultitaskingAndGesturesSettings.md)
- [/System/Library/PreferenceBundles/PodcastsSettingsPlugin.bundle/PodcastsSettingsPlugin](MACHOS/PodcastsSettingsPlugin.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PreferenceBundles/StorageSettingsUI.bundle/StorageSettingsUI](MACHOS/StorageSettingsUI.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd](MACHOS/appstorecomponentsd.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/PlugIns/AMSFollowUpExtension.appex/AMSFollowUpExtension](MACHOS/AMSFollowUpExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond](MACHOS/askpermissiond.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/PlugIns/ClockPosterExtension.appex/ClockPosterExtension](MACHOS/ClockPosterExtension.md)
- [/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS](MACHOS/SPIHelper-iOS.md)
- [/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.CloudSharing.appex/com.apple.CloudSharingUI.CloudSharing](MACHOS/com.apple.CloudSharingUI.CloudSharing.md)
- [/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService](MACHOS/CloudTelemetryService.md)
- [/System/Library/PrivateFrameworks/ContactsDonation.framework/Versions/A/Support/contactsdonationagent](MACHOS/contactsdonationagent.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd](MACHOS/corespeechd.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover](MACHOS/RecentsAppPopover.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado](MACHOS/RecentsAvocado.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles](MACHOS/SaveToFiles.md)
- [/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service](MACHOS/com.apple.DocumentManager.Service.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient](MACHOS/finhealthclient.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/Resources/UITypographyPanel.bundle/UITypographyPanel](MACHOS/UITypographyPanel.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/PlugIns/HPSUIViewService.appex/HPSUIViewService](MACHOS/HPSUIViewService.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService](MACHOS/IDSBlastDoorService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService](MACHOS/IntelligencePlatformComputeService.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/IntelligencePlatformLighthousePlugin.appex/IntelligencePlatformLighthousePlugin](MACHOS/IntelligencePlatformLighthousePlugin.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd](MACHOS/intelligenceplatformd.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview](MACHOS/com.apple.MLKit.MLModelPreview.md)
- [/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview](MACHOS/com.apple.MLKit.MLPackagePreview.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService](MACHOS/MediaAnalysisBlastDoorService.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MediaServicesBroker.framework/PlugIns/MediaSetupViewService.appex/MediaSetupViewService](MACHOS/MediaSetupViewService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService](MACHOS/MessagesAirlockService.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService](MACHOS/MessagesBlastDoorService.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged](MACHOS/amsondevicestoraged.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd](MACHOS/previewsd.md)
- [/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed](MACHOS/privatecloudcomputed.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Helpers/ProtectedCloudKeySyncing](MACHOS/ProtectedCloudKeySyncing.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension](MACHOS/AppLaunchIntentExtension.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin](MACHOS/SiriUserFeedbackLearningUniversalSuggestionsPlugin.md)
- [/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService](MACHOS/SiriHeadlessService.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd](MACHOS/stickersd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/CarPlayArtwork.bundle/CarPlayArtwork](MACHOS/CarPlayArtwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/TextEffectsCatalog.bundle/TextEffectsCatalog](MACHOS/TextEffectsCatalog.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/SecureControlService.xpc/SecureControlService](MACHOS/SecureControlService.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/com.apple.UIKit.KeyboardManagement.xpc/com.apple.UIKit.KeyboardManagement](MACHOS/com.apple.UIKit.KeyboardManagement.md)
- [/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent](MACHOS/UsageTrackingAgent.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/PlugIns/CollectionsPoster.appex/CollectionsPoster](MACHOS/CollectionsPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/ExtragalacticPoster.appex/ExtragalacticPoster](MACHOS/ExtragalacticPoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/KaleidoscopePoster](MACHOS/KaleidoscopePoster.md)
- [/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster](MACHOS/RhizomePoster.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension](MACHOS/FocusConfigurationExtension.md)
- [/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored](MACHOS/itunesstored.md)
- [/System/Library/Settings/InstalledApps.settings/InstalledApps](MACHOS/InstalledApps.md)
- [/System/Library/Siri/DM/SiriSuggestions/Owners/HomeAutomationSiriSuggestions.bundle/HomeAutomationSiriSuggestions](MACHOS/HomeAutomationSiriSuggestions.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension](MACHOS/AppStoreWidgetsExtension.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp](MACHOS/AppleVisionProApp.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension](MACHOS/BooksWidgetExtension.md)
- [/private/var/staged_system_apps/FaceTime.app/FaceTime](MACHOS/FaceTime.md)
- [/private/var/staged_system_apps/Files.app/Files](MACHOS/Files.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent](MACHOS/FindMyNotificationsContent.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/Fitness.app/Fitness](MACHOS/Fitness.md)
- [/private/var/staged_system_apps/Freeform.app/Extensions/USDRendererExtension.appex/USDRendererExtension](MACHOS/USDRendererExtension.md)
- [/private/var/staged_system_apps/Freeform.app/Freeform](MACHOS/Freeform.md)
- [/private/var/staged_system_apps/Freeform.app/PlugIns/FreeformWidgetKitExtension.appex/FreeformWidgetKitExtension](MACHOS/FreeformWidgetKitExtension.md)
- [/private/var/staged_system_apps/Health.app/Health](MACHOS/Health.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension](MACHOS/HomeEnergyWidgetsExtension.md)
- [/private/var/staged_system_apps/Journal.app/Journal](MACHOS/Journal.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension](MACHOS/JournalShareExtension.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets](MACHOS/JournalWidgets.md)
- [/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure](MACHOS/JournalWidgetsSecure.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget](MACHOS/GeneralMapsWidget.md)
- [/private/var/staged_system_apps/Measure.app/Measure](MACHOS/Measure.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/MobileTimer.app/PlugIns/WorldClockWidget.appex/WorldClockWidget](MACHOS/WorldClockWidget.md)
- [/private/var/staged_system_apps/Music.app/Frameworks/MusicApplication.framework/MusicApplication](MACHOS/MusicApplication.md)
- [/private/var/staged_system_apps/Music.app/Music](MACHOS/Music.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension](MACHOS/RemindersIntentsExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension](MACHOS/RemindersIntentsUIExtension.md)
- [/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension](MACHOS/RemindersWidgetExtension.md)
- [/private/var/staged_system_apps/Reminders.app/Reminders](MACHOS/Reminders.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/TranslationWidgetsExtension.appex/TranslationWidgetsExtension](MACHOS/TranslationWidgetsExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension](MACHOS/ShortcutsWidgetExtension.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/private/var/staged_system_apps/Tips.app/Tips](MACHOS/Tips.md)
- [/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos](MACHOS/VoiceMemos.md)
- [/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget](MACHOS/WeatherWidget.md)
- [/private/var/staged_system_apps/Weather.app/Weather](MACHOS/Weather.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/usr/bin/swift-inspect](MACHOS/swift-inspect.md)
- [/usr/lib/libramrod.dylib](MACHOS/libramrod.dylib.md)
- [/usr/libexec/SidecarRelay](MACHOS/SidecarRelay.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/applekeystored](MACHOS/applekeystored.md)
- [/usr/libexec/assessmentagent](MACHOS/assessmentagent.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/audioanalyticsd](MACHOS/audioanalyticsd.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/carkitd](MACHOS/carkitd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/demod](MACHOS/demod.md)
- [/usr/libexec/dockaccessoryd](MACHOS/dockaccessoryd.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/findmylocated](MACHOS/findmylocated.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/gamepolicyd](MACHOS/gamepolicyd.md)
- [/usr/libexec/icloudmailagent](MACHOS/icloudmailagent.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/modelmanagerd](MACHOS/modelmanagerd.md)
- [/usr/libexec/momentsd](MACHOS/momentsd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/nptocompaniond](MACHOS/nptocompaniond.md)
- [/usr/libexec/proximitycontrold](MACHOS/proximitycontrold.md)
- [/usr/libexec/rapportd](MACHOS/rapportd.md)
- [/usr/libexec/remindd](MACHOS/remindd.md)
- [/usr/libexec/remotepairingdeviced](MACHOS/remotepairingdeviced.md)
- [/usr/libexec/rtcreportingd](MACHOS/rtcreportingd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/security-sysdiagnose](MACHOS/security-sysdiagnose.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seld](MACHOS/seld.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/sportsd](MACHOS/sportsd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/wifip2pd](MACHOS/wifip2pd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (15)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H17.im4p

>  `AppleAVE2FW_H17.im4p`

```diff

 
   __TEXT.__text: 0xf3d48
   __TEXT._rtk_mtab: 0x2d0
-  __TEXT.__const: 0x2284c
+  __TEXT.__const: 0x22844
   __TEXT.__cstring: 0x1417b
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

```

#### SmartIOFirmware_ASCv7.im4p

>  `SmartIOFirmware_ASCv7.im4p`

```diff

 
   __TEXT.__text: 0x1a1ac
   __TEXT.__cstring: 0x1063
-  __TEXT.__const: 0x2e0
+  __TEXT.__const: 0x2d0
   __TEXT._rtk_mtab: 0x290
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

```

#### adc-rheia-d9x.im4p

>  `adc-rheia-d9x.im4p`

```diff

 
-  __TEXT.__text: 0x836938
-  __TEXT.__const: 0x9b59a8
+  __TEXT.__text: 0x836ffc
+  __TEXT.__const: 0x9b59a0
   __TEXT.text_env: 0x4fda4
   __TEXT._rtk_mtab: 0x2b8
-  __TEXT.__cstring: 0xa3743
+  __TEXT.__cstring: 0xa378c
   __TEXT.__data_copy: 0x200000
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __TEXT.__eh_frame: 0x944
-  __DATA.__const: 0x51d90
+  __DATA.__const: 0x51da0
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xe2a30
   __DATA._rtk_power: 0x3a8

   __DATA._rtk_smp_main: 0x8
   __DATA._rtk_boot_l1: 0x80
   __DATA.__gxf_data: 0x10
-  __DATA.__zerofill: 0x5bf620
+  __DATA.__zerofill: 0x5bb620
   Functions: 0
   Symbols:   0
-  CStrings:  17908
+  CStrings:  17909
 
CStrings:
+ "22:55:46"
+ "CRT: CPCEFlowManager.cpp:%d [DSI] Handling enter secure-mode request (%s)\n"
+ "CRT: CPCEFlowManager.cpp:%d [DSI] Handling exit secure-mode request (%s)\n"
+ "[DSI] GMC during FID has timed-out!! Stop waiting for GMC (%s)"
- "00:07:29"
- "CRT: CPCEFlowManager.cpp:%d [DSI] Handling enter secure-mode request\n"
- "CRT: CPCEFlowManager.cpp:%d [DSI] Handling exit secure-mode request\n"

```

#### agx_a000

>  `agx_a000`

```diff

 
   __TEXT.__text: 0x34dc4
   __TEXT.__gxf_shr_code: 0x55c
-  __TEXT.__gxf_code: 0x1230
+  __TEXT.__gxf_code: 0x1270
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b44
+  __TEXT.__const: 0x1b40
   __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
CStrings:
+ "Apr 22 2025 21:08:41"
- "Apr 15 2025 21:14:02"

```

#### agx_a010

>  `agx_a010`

```diff

 
   __TEXT.__text: 0x34d0c
   __TEXT.__gxf_shr_code: 0x55c
-  __TEXT.__gxf_code: 0x1230
+  __TEXT.__gxf_code: 0x1270
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b44
+  __TEXT.__const: 0x1b40
   __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
CStrings:
+ "Apr 22 2025 21:15:04"
- "Apr 15 2025 21:20:38"

```

#### agx_b000

>  `agx_b000`

```diff

 
   __TEXT.__text: 0x34be8
   __TEXT.__gxf_shr_code: 0x55c
-  __TEXT.__gxf_code: 0x1230
+  __TEXT.__gxf_code: 0x1270
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b44
+  __TEXT.__const: 0x1b40
   __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
CStrings:
+ "Apr 22 2025 21:12:31"
- "Apr 15 2025 21:18:10"

```

#### agx_b010

>  `agx_b010`

```diff

 
   __TEXT.__text: 0x34c74
   __TEXT.__gxf_shr_code: 0x55c
-  __TEXT.__gxf_code: 0x1230
+  __TEXT.__gxf_code: 0x1270
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b44
+  __TEXT.__const: 0x1b40
   __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
CStrings:
+ "Apr 22 2025 21:16:19"
- "Apr 15 2025 21:21:52"

```

#### agx_b100

>  `agx_b100`

```diff

 
-  __TEXT.__text: 0x34b50
+  __TEXT.__text: 0x34be8
   __TEXT.__gxf_shr_code: 0x55c
-  __TEXT.__gxf_code: 0x1230
+  __TEXT.__gxf_code: 0x1270
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b44
+  __TEXT.__const: 0x1b40
   __TEXT._rtk_patchbay: 0x228
   __TEXT._rtk_tunables: 0x6a0
   __TEXT.__chain_starts: 0x2c
CStrings:
+ "Apr 22 2025 21:13:48"
- "Apr 15 2025 21:19:25"

```

#### exclave_ExclaveStackshotServer

>  `exclave_ExclaveStackshotServer`

```diff

 64.120.2.0.0
-  __TEXT.__text: 0x32ecc0
+  __TEXT.__text: 0x32ea44
   __TEXT.__lcxx_override: 0x204
   __TEXT.__const: 0xd7d70
-  __TEXT.__cstring: 0x232ab
+  __TEXT.__cstring: 0x2344b
   __TEXT.__swift5_typeref: 0x5d64
   __TEXT.__swift5_fieldmd: 0x57d8
   __TEXT.__constg_swiftt: 0xa394

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
-  __DATA.__bss: 0x451e0
+  __DATA.__bss: 0x45720
   __DATA.__common: 0x2764
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 12479
+  Functions: 12470
   Symbols:   0
-  CStrings:  3967
+  CStrings:  3968
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/211c1991-1d94-11f0-9801-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "libpmm: L4_Ep_Call(%#zx, intag %#zx, op %#x) failed with %s(%zu), outtag %#zx"
+ "libpmm: ep %#zx op %#x failed (intag %#zx, outtag %#zx) with outerr %#zx, but an unexpected cap was returned in %#zx (ncrs %zd)"
+ "libpmm: ep %#zx op %#x failed with label %#zx (intag %#zx, outtag %#zx), but MR0 was L4_Success"
+ "libpmm: ep %#zx op %#x succeeded (intag %#zx, outtag %#zx), but expected cap was not returned to %#zx (ncrs %zd)"
+ "libpmm: ep %#zx op %#x succeeded (intag %#zx, outtag %#zx), expected %zd MRs, got %zd"
+ "libpmm`_alloc(ep %#zx, %d, %#zx) -> %#zx worked, but L4_Untyped_Create(%#zx, %d, 0, %#zx) failed with %s(%zu)"
+ "libpmm`_alloc(ep %#zx, %d, %#zx) -> %#zx; L4_Cap_Delete(%zx) failed with %s(%zu) after L4_Untyped_Create(%#zx, %d, 0, %#zx) succeeded"
+ "local_storage != NULL"
- "/AppleInternal/Library/BuildRoots/9ffc6a43-1932-11f0-bb2f-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libpmm/pmm.c"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(temp_slot)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Ep_Call(endpoint, &tag)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Untyped_Create( temp_slot, type, 0, dest)'"
- "_alloc"
- "_call_endpoint"
- "pmm__check_frame_allocations"

```

#### exclave_pmm_exclave

>  `exclave_pmm_exclave`

```diff

-839.120.28.0.0
-  __TEXT.__text: 0x3963c
+839.120.30.0.0
+  __TEXT.__text: 0x39540
   __TEXT.__const: 0x1c940
-  __TEXT.__cstring: 0xd5ad
+  __TEXT.__cstring: 0xd77b
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x44720
+  __DATA.__bss: 0x44c60
   __DATA.__common: 0x70b0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 1022
+  Functions: 1016
   Symbols:   4
-  CStrings:  1278
+  CStrings:  1281
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/211c1991-1d94-11f0-9801-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "libpmm: L4_Ep_Call(%#zx, intag %#zx, op %#x) failed with %s(%zu), outtag %#zx"
+ "libpmm: ep %#zx op %#x failed (intag %#zx, outtag %#zx) with outerr %#zx, but an unexpected cap was returned in %#zx (ncrs %zd)"
+ "libpmm: ep %#zx op %#x failed with label %#zx (intag %#zx, outtag %#zx), but MR0 was L4_Success"
+ "libpmm: ep %#zx op %#x succeeded (intag %#zx, outtag %#zx), but expected cap was not returned to %#zx (ncrs %zd)"
+ "libpmm: ep %#zx op %#x succeeded (intag %#zx, outtag %#zx), expected %zd MRs, got %zd"
+ "libpmm`_alloc(ep %#zx, %d, %#zx) -> %#zx worked, but L4_Untyped_Create(%#zx, %d, 0, %#zx) failed with %s(%zu)"
+ "libpmm`_alloc(ep %#zx, %d, %#zx) -> %#zx; L4_Cap_Delete(%zx) failed with %s(%zu) after L4_Untyped_Create(%#zx, %d, 0, %#zx) succeeded"
+ "local_storage != NULL"
- "/AppleInternal/Library/BuildRoots/9ffc6a43-1932-11f0-bb2f-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/libpmm/pmm.c"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(temp_slot)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Ep_Call(endpoint, &tag)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Untyped_Create( temp_slot, type, 0, dest)'"
- "_call_endpoint"

```

#### exclave_roottask

>  `exclave_roottask`

```diff

-839.120.28.0.0
-  __TEXT.__text: 0x4a8e7c
+839.120.30.0.0
+  __TEXT.__text: 0x4ac63c
   __TEXT.__lcxx_override: 0x200
-  __TEXT.__const: 0xe4a16
-  __TEXT.__cstring: 0x2feaa
-  __TEXT.__swift5_typeref: 0xa452
+  __TEXT.__const: 0xe4a56
+  __TEXT.__cstring: 0x300ca
+  __TEXT.__swift5_typeref: 0xa462
   __TEXT.__swift5_capture: 0x1824
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0x9135
+  __TEXT.__swift5_reflstr: 0x9155
   __TEXT.__swift5_assocty: 0x62d0
-  __TEXT.__constg_swiftt: 0x11584
-  __TEXT.__swift5_fieldmd: 0xe564
+  __TEXT.__constg_swiftt: 0x115a8
+  __TEXT.__swift5_fieldmd: 0xe598
   __TEXT.__swift5_builtin: 0xcbc
-  __TEXT.__swift5_proto: 0x2328
-  __TEXT.__swift5_types: 0xffc
+  __TEXT.__swift5_proto: 0x2334
+  __TEXT.__swift5_types: 0x1000
   __TEXT.__swift5_protos: 0x32c
   __TEXT.__swift5_mpenum: 0x434
   __TEXT.__swift5_types2: 0x10

   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x24
-  __TEXT.__eh_frame: 0x1a4cc
+  __TEXT.__eh_frame: 0x1a624
   __DATA.__got: 0x198
-  __DATA.__auth_ptr: 0x140
+  __DATA.__auth_ptr: 0x148
   __DATA.__mod_init_func: 0x50
-  __DATA.__const: 0x2d5c8
+  __DATA.__const: 0x2d6b0
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__data: 0x9630
+  __DATA.__data: 0x9640
   __DATA.__shared_cache: 0x70
   __DATA.__DEVICETREE: 0x30
   __DATA.__ENDPOINTS: 0x62a

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x28
   __DATA.__common: 0x22064
-  __DATA.__bss: 0x11910
+  __DATA.__bss: 0x11e50
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 17555
+  Functions: 17575
   Symbols:   23
-  CStrings:  5325
+  CStrings:  5329
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/211c1991-1d94-11f0-9801-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "libpmm: L4_Ep_Call(%#zx, intag %#zx, op %#x) failed with %s(%zu), outtag %#zx"
+ "libpmm: ep %#zx op %#x failed (intag %#zx, outtag %#zx) with outerr %#zx, but an unexpected cap was returned in %#zx (ncrs %zd)"
+ "libpmm: ep %#zx op %#x failed with label %#zx (intag %#zx, outtag %#zx), but MR0 was L4_Success"
+ "libpmm: ep %#zx op %#x succeeded (intag %#zx, outtag %#zx), but expected cap was not returned to %#zx (ncrs %zd)"
+ "libpmm: ep %#zx op %#x succeeded (intag %#zx, outtag %#zx), expected %zd MRs, got %zd"
+ "libpmm`_alloc(ep %#zx, %d, %#zx) -> %#zx worked, but L4_Untyped_Create(%#zx, %d, 0, %#zx) failed with %s(%zu)"
+ "libpmm`_alloc(ep %#zx, %d, %#zx) -> %#zx; L4_Cap_Delete(%zx) failed with %s(%zu) after L4_Untyped_Create(%#zx, %d, 0, %#zx) succeeded"
+ "local_storage != NULL"
+ "order metadata must be integer"
- "/AppleInternal/Library/BuildRoots/9ffc6a43-1932-11f0-bb2f-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/libpmm/pmm.c"
- "Unexpected L4_Error: %s(%zu) err='L4_Ep_Call(endpoint, &tag)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Untyped_Create( temp_slot, type, 0, dest)'"
- "_alloc"
- "_call_endpoint"

```

#### exclave_scheduler

>  `exclave_scheduler`

```diff

-839.120.28.0.0
-  __TEXT.__text: 0x2fb0e0
+839.120.30.0.0
+  __TEXT.__text: 0x2fafd0
   __TEXT.__lcxx_override: 0x200
-  __TEXT.__cstring: 0x20240
+  __TEXT.__cstring: 0x20400
   __TEXT.__const: 0xd7e8e
   __TEXT.__constg_swiftt: 0xa4c8
   __TEXT.__swift5_typeref: 0x5b20

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x38
-  __DATA.__bss: 0x49470
+  __DATA.__bss: 0x499b0
   __DATA.__common: 0x1efc
   __PDATA.__shared_cache: 0x0
   __PDATA.__mod_init_func: 0x0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 11456
+  Functions: 11450
   Symbols:   24
-  CStrings:  3893
+  CStrings:  3895
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/211c1991-1d94-11f0-9801-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "libpmm: L4_Ep_Call(%#zx, intag %#zx, op %#x) failed with %s(%zu), outtag %#zx"
+ "libpmm: ep %#zx op %#x failed (intag %#zx, outtag %#zx) with outerr %#zx, but an unexpected cap was returned in %#zx (ncrs %zd)"
+ "libpmm: ep %#zx op %#x failed with label %#zx (intag %#zx, outtag %#zx), but MR0 was L4_Success"
+ "libpmm: ep %#zx op %#x succeeded (intag %#zx, outtag %#zx), but expected cap was not returned to %#zx (ncrs %zd)"
+ "libpmm: ep %#zx op %#x succeeded (intag %#zx, outtag %#zx), expected %zd MRs, got %zd"
+ "libpmm`_alloc(ep %#zx, %d, %#zx) -> %#zx worked, but L4_Untyped_Create(%#zx, %d, 0, %#zx) failed with %s(%zu)"
+ "libpmm`_alloc(ep %#zx, %d, %#zx) -> %#zx; L4_Cap_Delete(%zx) failed with %s(%zu) after L4_Untyped_Create(%#zx, %d, 0, %#zx) succeeded"
+ "local_storage != NULL"
- "/AppleInternal/Library/BuildRoots/9ffc6a43-1932-11f0-bb2f-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_services_exclavecore/libpmm/pmm.c"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(temp_slot)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Ep_Call(endpoint, &tag)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Untyped_Create( temp_slot, type, 0, dest)'"
- "_alloc"
- "_call_endpoint"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 543.120.34.0.0
-  __TEXT.__text: 0x4f00ac
+  __TEXT.__text: 0x4efcc8
   __TEXT.__lcxx_override: 0x200
-  __TEXT.__cstring: 0x39d8f
+  __TEXT.__cstring: 0x39f3f
   __TEXT.__const: 0xfd1e8
   __TEXT.__swift5_typeref: 0xfa1b
   __TEXT.__swift5_reflstr: 0xa7e8

   __TEXT.__term_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__thread_starts: 0x40
-  __TEXT.__eh_frame: 0x27464
+  __TEXT.__eh_frame: 0x27494
   __DATA.__got: 0x18
   __DATA.__auth_ptr: 0x2a8
   __DATA.__mod_init_func: 0x38

   __PDATA.__mod_init_func: 0x18
   __PDATA.__auth_ptr: 0x38
   __PDATA.__objc_imageinfo: 0x8
-  __PDATA.__bss: 0x47b8
+  __PDATA.__bss: 0x4cf8
   __PDATA.__common: 0x2530
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 19758
+  Functions: 19747
   Symbols:   0
-  CStrings:  5773
+  CStrings:  5774
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/211c1991-1d94-11f0-9801-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/211c1991-1d94-11f0-9801-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "libpmm: L4_Ep_Call(%#zx, intag %#zx, op %#x) failed with %s(%zu), outtag %#zx"
+ "libpmm: ep %#zx op %#x failed (intag %#zx, outtag %#zx) with outerr %#zx, but an unexpected cap was returned in %#zx (ncrs %zd)"
+ "libpmm: ep %#zx op %#x failed with label %#zx (intag %#zx, outtag %#zx), but MR0 was L4_Success"
+ "libpmm: ep %#zx op %#x succeeded (intag %#zx, outtag %#zx), but expected cap was not returned to %#zx (ncrs %zd)"
+ "libpmm: ep %#zx op %#x succeeded (intag %#zx, outtag %#zx), expected %zd MRs, got %zd"
+ "libpmm`_alloc(ep %#zx, %d, %#zx) -> %#zx worked, but L4_Untyped_Create(%#zx, %d, 0, %#zx) failed with %s(%zu)"
+ "libpmm`_alloc(ep %#zx, %d, %#zx) -> %#zx; L4_Cap_Delete(%zx) failed with %s(%zu) after L4_Untyped_Create(%#zx, %d, 0, %#zx) succeeded"
+ "local_storage != NULL"
- "/AppleInternal/Library/BuildRoots/9ffc6a43-1932-11f0-bb2f-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/9ffc6a43-1932-11f0-bb2f-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.5.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "/Library/Caches/com.apple.xbs/Sources/ExclavePlatform_exclavecore/libpmm/pmm.c"
- "Unexpected L4_Error: %s(%zu) err='L4_Cap_Delete(temp_slot)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Ep_Call(endpoint, &tag)'"
- "Unexpected L4_Error: %s(%zu) err='L4_Untyped_Create( temp_slot, type, 0, dest)'"
- "_alloc"
- "_call_endpoint"
- "pmm__check_frame_allocations"

```

#### h17_ane_fw_theia_d9x.im4p

>  `h17_ane_fw_theia_d9x.im4p`

```diff

 
   __TEXT.__text: 0x9ba10
-  __TEXT.__const: 0x41e4
+  __TEXT.__const: 0x41e0
   __TEXT.__cstring: 0x13811
   __TEXT.ce_env: 0x4000
   __TEXT.__constructor: 0x0
CStrings:
+ "22:34:23"
+ "Apr 20 2025"
- "22:03:30"
- "Apr 13 2025"

```

#### t8140pmp.im4p

>  `t8140pmp.im4p`

```diff

 
   __TEXT.__text: 0x3788c
-  __TEXT.__const: 0x235e
+  __TEXT.__const: 0x235a
   __TEXT.__cstring: 0x1540
   __TEXT._rtk_mtab: 0x5e8
   __TEXT.__constructor: 0x0

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 18.5 *(22F5053j)* | iBoot-11881.120.116.502.1 |
| 18.5 *(22F5068a)* | iBoot-11881.122.1 |

#### 🆕 NEW (2)

<details>
  <summary><i>View NEW</i></summary>

##### `AppleSMCFirmware.bin`
  - `AppleSMCFirmware_H17-5204.122.2.d93.REL`
##### `iboot`
  - `A^w=%n}_^)z`
  - ` ApplePMUFirmware-503.120.3~471.release`
  - `gK\[H!hq[h%`
  - `root@q64km.p1l.plx.sd...2025/04/22@21:17:27`
  - `_ǌWʰvJi4`
  - `U!||]glkVqN`
  - `*/m],RRC-4`
  - `n%dnxN5&ȶ`
  - `MCE FW E001- built on Sun Apr 20 08:41:46 UTC 2025 by root`
  - `cH-û÷/ʣV`
  - `BC_ SfOU\2`
  - `2kP}Vv˷m `
  - `ÂzgJ_]wR#`
  - `iBoot-11881.122.1`
  - `e4d4279a51f9f4da9ac112a2b0c1cb1e`
  - `bFhEXf20Z"ª`

</details>

#### ❌ Removed (2)

<details>
  <summary><i>View Removed</i></summary>

##### `iboot`
  - `08945e28a7d6184e482e6d04f6dc4361`
  - `MCE FW E001- built on Fri Mar 21 22:15:45 UTC 2025 by root`
  - `root@bc2pz.p1l.plx.sd...2025/04/15@01:28:15`
  - `6QĢ>rUAŮ;`
  - `UI|/UV*,L%O`
  - `Br_1V✫U#?q`
  - `iBoot-11881.120.116.502.1`
  - ` ApplePMUFirmware-503.120.3~192.release`
##### `AppleSMCFirmware.bin`
  - `AppleSMCFirmware_H17-5204.120.50.0.3.d93.REL`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.5 *(22F5053j)* | 621.2.4.10.2 |
| 18.5 *(22F5068a)* | 621.2.5.10.6 |

### Dylibs

#### ⬆️ Updated (610)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Accounts/Notification/PCSAccountNotificationPlugin.bundle/PCSAccountNotificationPlugin](DYLIBS/PCSAccountNotificationPlugin.md)
- [/System/Library/Assistant/UIPlugins/SiriFindMyUIPlugin.siriUIBundle/Frameworks/SiriFindMyUI.framework/SiriFindMyUI](DYLIBS/SiriFindMyUI.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AppIntents.framework/AppIntents](DYLIBS/AppIntents.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox](DYLIBS/AudioToolbox.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient](DYLIBS/AACClient.md)
- [/System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit](DYLIBS/BrowserEngineKit.md)
- [/System/Library/Frameworks/Charts.framework/Charts](DYLIBS/Charts.md)
- [/System/Library/Frameworks/Combine.framework/Combine](DYLIBS/Combine.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreAudio.framework/CoreAudio](DYLIBS/CoreAudio.md)
- [/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit](DYLIBS/CoreAudioKit.md)
- [/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation](DYLIBS/CoreFoundation.md)
- [/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics](DYLIBS/CoreGraphics.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/CreateML.framework/CreateML](DYLIBS/CreateML.md)
- [/System/Library/Frameworks/CreateMLComponents.framework/CreateMLComponents](DYLIBS/CreateMLComponents.md)
- [/System/Library/Frameworks/CryptoKit.framework/CryptoKit](DYLIBS/CryptoKit.md)
- [/System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport](DYLIBS/DeveloperToolsSupport.md)
- [/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity](DYLIBS/DeviceActivity.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/ImagePlayground.framework/ImagePlayground](DYLIBS/ImagePlayground.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation](DYLIBS/LinkPresentation.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication](DYLIBS/LocalAuthentication.md)
- [/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils](DYLIBS/SharedUtils.md)
- [/System/Library/Frameworks/MapKit.framework/MapKit](DYLIBS/MapKit.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MusicKit.framework/MusicKit](DYLIBS/MusicKit.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/ProximityReader.framework/ProximityReader](DYLIBS/ProximityReader.md)
- [/System/Library/Frameworks/RealityFoundation.framework/RealityFoundation](DYLIBS/RealityFoundation.md)
- [/System/Library/Frameworks/RoomPlan.framework/RoomPlan](DYLIBS/RoomPlan.md)
- [/System/Library/Frameworks/SceneKit.framework/SceneKit](DYLIBS/SceneKit.md)
- [/System/Library/Frameworks/SecureElementCredential.framework/SecureElementCredential](DYLIBS/SecureElementCredential.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/ShazamKit.framework/ShazamKit](DYLIBS/ShazamKit.md)
- [/System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis](DYLIBS/SoundAnalysis.md)
- [/System/Library/Frameworks/Speech.framework/Speech](DYLIBS/Speech.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/StoreKit.framework/StoreKit](DYLIBS/StoreKit.md)
- [/System/Library/Frameworks/SwiftData.framework/SwiftData](DYLIBS/SwiftData.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/SwiftUICore.framework/SwiftUICore](DYLIBS/SwiftUICore.md)
- [/System/Library/Frameworks/TabularData.framework/TabularData](DYLIBS/TabularData.md)
- [/System/Library/Frameworks/TipKit.framework/TipKit](DYLIBS/TipKit.md)
- [/System/Library/Frameworks/UIKit.framework/UIKit](DYLIBS/UIKit.md)
- [/System/Library/Frameworks/Vision.framework/Vision](DYLIBS/Vision.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/WidgetKit.framework/WidgetKit](DYLIBS/WidgetKit.md)
- [/System/Library/Frameworks/WorkoutKit.framework/WorkoutKit](DYLIBS/WorkoutKit.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/Frameworks/_PassKit_SwiftUI.framework/_PassKit_SwiftUI](DYLIBS/_PassKit_SwiftUI.md)
- [/System/Library/Frameworks/_RealityKit_SwiftUI.framework/_RealityKit_SwiftUI](DYLIBS/_RealityKit_SwiftUI.md)
- [/System/Library/Frameworks/_StoreKit_SwiftUI.framework/_StoreKit_SwiftUI](DYLIBS/_StoreKit_SwiftUI.md)
- [/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin](DYLIBS/HearingAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Heart.healthplugin/Heart](DYLIBS/Heart.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPlugin.healthplugin/MedicationsHealthAppPlugin](DYLIBS/MedicationsHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/MentalHealthAppPlugin.healthplugin/MentalHealthAppPlugin](DYLIBS/MentalHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/RespiratoryHealthAppPlugin.healthplugin/RespiratoryHealthAppPlugin](DYLIBS/RespiratoryHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/MediaCapture/H16ISP.mediacapture](DYLIBS/H16ISP.mediacapture.md)
- [/System/Library/NanoTimeKit/ComplicationBundles/WeatherComplications.bundle/WeatherComplications](DYLIBS/WeatherComplications.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKEsterbrookFaceBundleCompanion.bundle/NTKEsterbrookFaceBundleCompanion](DYLIBS/NTKEsterbrookFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKParmesanFaceBundleCompanion.bundle/NTKParmesanFaceBundleCompanion](DYLIBS/NTKParmesanFaceBundleCompanion.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKRhizomeFaceBundleCompanion.bundle/NTKRhizomeFaceBundleCompanion](DYLIBS/NTKRhizomeFaceBundleCompanion.md)
- [/System/Library/Previews/ShellPlugins/WidgetPreviewsShellPlugin.bundle/WidgetPreviewsShellPlugin](DYLIBS/WidgetPreviewsShellPlugin.md)
- [/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams](DYLIBS/AIMLInstrumentationStreams.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySharedUISupport.framework/AccessibilitySharedUISupport](DYLIBS/AccessibilitySharedUISupport.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/ActionButtonConfigurationUI.framework/ActionButtonConfigurationUI](DYLIBS/ActionButtonConfigurationUI.md)
- [/System/Library/PrivateFrameworks/ActionKit.framework/ActionKit](DYLIBS/ActionKit.md)
- [/System/Library/PrivateFrameworks/ActionKitUI.framework/ActionKitUI](DYLIBS/ActionKitUI.md)
- [/System/Library/PrivateFrameworks/ActivitySharingServices.framework/ActivitySharingServices](DYLIBS/ActivitySharingServices.md)
- [/System/Library/PrivateFrameworks/ActivityUIServices.framework/ActivityUIServices](DYLIBS/ActivityUIServices.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AdaptiveMusic.framework/AdaptiveMusic](DYLIBS/AdaptiveMusic.md)
- [/System/Library/PrivateFrameworks/AirPlayKit.framework/AirPlayKit](DYLIBS/AirPlayKit.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/Announce.framework/Announce](DYLIBS/Announce.md)
- [/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon](DYLIBS/AnnounceDaemon.md)
- [/System/Library/PrivateFrameworks/Anvil.framework/Anvil](DYLIBS/Anvil.md)
- [/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics](DYLIBS/AppAnalytics.md)
- [/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal](DYLIBS/AppAttestInternal.md)
- [/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices](DYLIBS/AppIntentsServices.md)
- [/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection](DYLIBS/AppProtection.md)
- [/System/Library/PrivateFrameworks/AppState.framework/AppState](DYLIBS/AppState.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppleCareSupport.framework/AppleCareSupport](DYLIBS/AppleCareSupport.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon](DYLIBS/AppleIDSetupDaemon.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal](DYLIBS/AppleMediaServicesKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic](DYLIBS/AppleMediaServicesUIDynamic.md)
- [/System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal](DYLIBS/ArgumentParserInternal.md)
- [/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission](DYLIBS/AskPermission.md)
- [/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore](DYLIBS/AskToCore.md)
- [/System/Library/PrivateFrameworks/AskToDaemon.framework/AskToDaemon](DYLIBS/AskToDaemon.md)
- [/System/Library/PrivateFrameworks/AssetViewer.framework/AssetViewer](DYLIBS/AssetViewer.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsBase.framework/AudioAnalyticsBase](DYLIBS/AudioAnalyticsBase.md)
- [/System/Library/PrivateFrameworks/AudioAnalyticsExternal.framework/AudioAnalyticsExternal](DYLIBS/AudioAnalyticsExternal.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI](DYLIBS/BatteryCenterUI.md)
- [/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation](DYLIBS/BiomeFoundation.md)
- [/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub](DYLIBS/BiomePubSub.md)
- [/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams](DYLIBS/BiomeStreams.md)
- [/System/Library/PrivateFrameworks/Blackbeard.framework/Blackbeard](DYLIBS/Blackbeard.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/BookDataStore](DYLIBS/BookDataStore.md)
- [/System/Library/PrivateFrameworks/BookFoundation.framework/BookFoundation](DYLIBS/BookFoundation.md)
- [/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices](DYLIBS/BusinessServices.md)
- [/System/Library/PrivateFrameworks/CAFCombine.framework/CAFCombine](DYLIBS/CAFCombine.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CTBlastDoorSupport.framework/CTBlastDoorSupport](DYLIBS/CTBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/Calculate.framework/Calculate](DYLIBS/Calculate.md)
- [/System/Library/PrivateFrameworks/CalendarLink.framework/CalendarLink](DYLIBS/CalendarLink.md)
- [/System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit](DYLIBS/CalendarUIKit.md)
- [/System/Library/PrivateFrameworks/CalendarWidget.framework/CalendarWidget](DYLIBS/CalendarWidget.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit](DYLIBS/CameraEditKit.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation](DYLIBS/CarKitNavigation.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/Chirp.framework/Chirp](DYLIBS/Chirp.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices](DYLIBS/ChronoServices.md)
- [/System/Library/PrivateFrameworks/ChronoUIServices.framework/ChronoUIServices](DYLIBS/ChronoUIServices.md)
- [/System/Library/PrivateFrameworks/ClassroomKit.framework/Frameworks/ClassroomUIKit.framework/ClassroomUIKit](DYLIBS/ClassroomUIKit.md)
- [/System/Library/PrivateFrameworks/ClockPoster.framework/ClockPoster](DYLIBS/ClockPoster.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudRecommendationUI.framework/CloudRecommendationUI](DYLIBS/CloudRecommendationUI.md)
- [/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures](DYLIBS/CloudSubscriptionFeatures.md)
- [/System/Library/PrivateFrameworks/CloudTelemetryTools.framework/CloudTelemetryTools](DYLIBS/CloudTelemetryTools.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CommandAndControlUI.framework/CommandAndControlUI](DYLIBS/CommandAndControlUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/ContactlessReaderUI.framework/ContactlessReaderUI](DYLIBS/ContactlessReaderUI.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI](DYLIBS/ControlCenterUI.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/CookingKit.framework/CookingKit](DYLIBS/CookingKit.md)
- [/System/Library/PrivateFrameworks/CookingSupport.framework/CookingSupport](DYLIBS/CookingSupport.md)
- [/System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore](DYLIBS/CopresenceCore.md)
- [/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI](DYLIBS/CoreCDPUI.md)
- [/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics](DYLIBS/CoreDiagnostics.md)
- [/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp](DYLIBS/CoreFollowUp.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared](DYLIBS/CoreIDVShared.md)
- [/System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI](DYLIBS/CoreIDVUI.md)
- [/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge](DYLIBS/CoreKnowledge.md)
- [/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC](DYLIBS/CoreOC.md)
- [/System/Library/PrivateFrameworks/CoreODIEssentials.framework/CoreODIEssentials](DYLIBS/CoreODIEssentials.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal](DYLIBS/CoreServicesInternal.md)
- [/System/Library/PrivateFrameworks/CoreSpeechExclave.framework/CoreSpeechExclave](DYLIBS/CoreSpeechExclave.md)
- [/System/Library/PrivateFrameworks/CoreSuggestionsInternals.framework/CoreSuggestionsInternals](DYLIBS/CoreSuggestionsInternals.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/CosmeticAssessment.framework/CosmeticAssessment](DYLIBS/CosmeticAssessment.md)
- [/System/Library/PrivateFrameworks/CryptexServer.framework/CryptexServer](DYLIBS/CryptexServer.md)
- [/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate](DYLIBS/CryptoKitPrivate.md)
- [/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps](DYLIBS/DMCApps.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DVTInstrumentsFoundation](DYLIBS/DVTInstrumentsFoundation.md)
- [/System/Library/PrivateFrameworks/DailyBriefingCommon.framework/DailyBriefingCommon](DYLIBS/DailyBriefingCommon.md)
- [/System/Library/PrivateFrameworks/DarwinDirectory.framework/DarwinDirectory](DYLIBS/DarwinDirectory.md)
- [/System/Library/PrivateFrameworks/DarwinDirectoryInternal.framework/DarwinDirectoryInternal](DYLIBS/DarwinDirectoryInternal.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DataFlow.framework/DataFlow](DYLIBS/DataFlow.md)
- [/System/Library/PrivateFrameworks/DeepThought.framework/DeepThought](DYLIBS/DeepThought.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation](DYLIBS/DigitalSeparation.md)
- [/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI](DYLIBS/DigitalSeparationUI.md)
- [/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI](DYLIBS/DisembarkUI.md)
- [/System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore](DYLIBS/DockKitCore.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding](DYLIBS/DocumentUnderstanding.md)
- [/System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient](DYLIBS/DocumentUnderstandingClient.md)
- [/System/Library/PrivateFrameworks/DrawingBoard.framework/DrawingBoard](DYLIBS/DrawingBoard.md)
- [/System/Library/PrivateFrameworks/DropInCore.framework/DropInCore](DYLIBS/DropInCore.md)
- [/System/Library/PrivateFrameworks/DropletUI.framework/DropletUI](DYLIBS/DropletUI.md)
- [/System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation](DYLIBS/EmojiFoundation.md)
- [/System/Library/PrivateFrameworks/FMFCore.framework/FMFCore](DYLIBS/FMFCore.md)
- [/System/Library/PrivateFrameworks/FMFindingUI.framework/FMFindingUI](DYLIBS/FMFindingUI.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking](DYLIBS/FMNetworking.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle](DYLIBS/FamilyCircle.md)
- [/System/Library/PrivateFrameworks/FamilyCircleUI.framework/FamilyCircleUI](DYLIBS/FamilyCircleUI.md)
- [/System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore](DYLIBS/FeatureStore.md)
- [/System/Library/PrivateFrameworks/Feedback.framework/Feedback](DYLIBS/Feedback.md)
- [/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore](DYLIBS/FeedbackCore.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyLocate.framework/FindMyLocate](DYLIBS/FindMyLocate.md)
- [/System/Library/PrivateFrameworks/FindMyMessaging.framework/FindMyMessaging](DYLIBS/FindMyMessaging.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FitnessAsset.framework/FitnessAsset](DYLIBS/FitnessAsset.md)
- [/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards](DYLIBS/FitnessAwards.md)
- [/System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI](DYLIBS/FitnessCanvasUI.md)
- [/System/Library/PrivateFrameworks/FitnessCoaching.framework/FitnessCoaching](DYLIBS/FitnessCoaching.md)
- [/System/Library/PrivateFrameworks/FitnessCoachingServices.framework/FitnessCoachingServices](DYLIBS/FitnessCoachingServices.md)
- [/System/Library/PrivateFrameworks/FitnessCoreUI.framework/FitnessCoreUI](DYLIBS/FitnessCoreUI.md)
- [/System/Library/PrivateFrameworks/FitnessFiltering.framework/FitnessFiltering](DYLIBS/FitnessFiltering.md)
- [/System/Library/PrivateFrameworks/FitnessMarketing.framework/FitnessMarketing](DYLIBS/FitnessMarketing.md)
- [/System/Library/PrivateFrameworks/FitnessProductDetail.framework/FitnessProductDetail](DYLIBS/FitnessProductDetail.md)
- [/System/Library/PrivateFrameworks/FitnessUI.framework/FitnessUI](DYLIBS/FitnessUI.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI](DYLIBS/FocusSettingsUI.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/GameCenterUI](DYLIBS/GameCenterUI.md)
- [/System/Library/PrivateFrameworks/GameServicesCore.framework/GameServicesCore](DYLIBS/GameServicesCore.md)
- [/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/GenerativeAssistantActions](DYLIBS/GenerativeAssistantActions.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesUI.framework/GenerativeExperiencesUI](DYLIBS/GenerativeExperiencesUI.md)
- [/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation](DYLIBS/GenerativeFunctionsFoundation.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation](DYLIBS/GenerativeModelsFoundation.md)
- [/System/Library/PrivateFrameworks/GroupKitCrypto.framework/GroupKitCrypto](DYLIBS/GroupKitCrypto.md)
- [/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation](DYLIBS/HMFoundation.md)
- [/System/Library/PrivateFrameworks/HTTPTypesInternal.framework/HTTPTypesInternal](DYLIBS/HTTPTypesInternal.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures](DYLIBS/HeadGestures.md)
- [/System/Library/PrivateFrameworks/HealthBalance.framework/HealthBalance](DYLIBS/HealthBalance.md)
- [/System/Library/PrivateFrameworks/HealthBalanceDaemon.framework/HealthBalanceDaemon](DYLIBS/HealthBalanceDaemon.md)
- [/System/Library/PrivateFrameworks/HealthBalanceUI.framework/HealthBalanceUI](DYLIBS/HealthBalanceUI.md)
- [/System/Library/PrivateFrameworks/HealthExperienceUI.framework/HealthExperienceUI](DYLIBS/HealthExperienceUI.md)
- [/System/Library/PrivateFrameworks/HealthExposureNotificationUI.framework/HealthExposureNotificationUI](DYLIBS/HealthExposureNotificationUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon](DYLIBS/HealthMenstrualCyclesDaemon.md)
- [/System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore](DYLIBS/HealthPlatformCore.md)
- [/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon](DYLIBS/HealthRecordsDaemon.md)
- [/System/Library/PrivateFrameworks/HealthRecordsExtraction.framework/HealthRecordsExtraction](DYLIBS/HealthRecordsExtraction.md)
- [/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI](DYLIBS/HealthRecordsUI.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest](DYLIBS/HearingTest.md)
- [/System/Library/PrivateFrameworks/Home.framework/Home](DYLIBS/Home.md)
- [/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI](DYLIBS/HomeAccessoryControlUI.md)
- [/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents](DYLIBS/HomeAppIntents.md)
- [/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/HomeAutomationInternal](DYLIBS/HomeAutomationInternal.md)
- [/System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel](DYLIBS/HomeDataModel.md)
- [/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/HomeEnergyDaemon](DYLIBS/HomeEnergyDaemon.md)
- [/System/Library/PrivateFrameworks/HomeEnergyUI.framework/HomeEnergyUI](DYLIBS/HomeEnergyUI.md)
- [/System/Library/PrivateFrameworks/HomeKitCore.framework/HomeKitCore](DYLIBS/HomeKitCore.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonFoundation.framework/HomeKitDaemonFoundation](DYLIBS/HomeKitDaemonFoundation.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemonLegacy](DYLIBS/HomeKitDaemonLegacy.md)
- [/System/Library/PrivateFrameworks/HomeKitEvents.framework/HomeKitEvents](DYLIBS/HomeKitEvents.md)
- [/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter](DYLIBS/HomeKitMatter.md)
- [/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics](DYLIBS/HomeKitMetrics.md)
- [/System/Library/PrivateFrameworks/HomePlatformSettingsUI.framework/HomePlatformSettingsUI](DYLIBS/HomePlatformSettingsUI.md)
- [/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings](DYLIBS/HomePodSettings.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeUI2.framework/HomeUI2](DYLIBS/HomeUI2.md)
- [/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents](DYLIBS/HomeWidgetIntents.md)
- [/System/Library/PrivateFrameworks/HoverTextUI.framework/HoverTextUI](DYLIBS/HoverTextUI.md)
- [/System/Library/PrivateFrameworks/Human.framework/Human](DYLIBS/Human.md)
- [/System/Library/PrivateFrameworks/HumanUI.framework/HumanUI](DYLIBS/HumanUI.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingEvidence.framework/HumanUnderstandingEvidence](DYLIBS/HumanUnderstandingEvidence.md)
- [/System/Library/PrivateFrameworks/HumanUnderstandingFoundation.framework/HumanUnderstandingFoundation](DYLIBS/HumanUnderstandingFoundation.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation](DYLIBS/IMFoundation.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/ImagePlaygroundInternal.framework/ImagePlaygroundInternal](DYLIBS/ImagePlaygroundInternal.md)
- [/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics](DYLIBS/InputAnalytics.md)
- [/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer](DYLIBS/InputAnalyticsServer.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime](DYLIBS/IntelligenceFlowContextRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/IntelligenceFlowPlannerRuntime](DYLIBS/IntelligenceFlowPlannerRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport](DYLIBS/IntelligenceFlowPlannerSupport.md)
- [/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime](DYLIBS/IntelligenceFlowRuntime.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform](DYLIBS/IntelligencePlatform.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary](DYLIBS/IntelligencePlatformLibrary.md)
- [/System/Library/PrivateFrameworks/IntelligentTrackingCore.framework/IntelligentTrackingCore](DYLIBS/IntelligentTrackingCore.md)
- [/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf](DYLIBS/InternalSwiftProtobuf.md)
- [/System/Library/PrivateFrameworks/JetCore.framework/JetCore](DYLIBS/JetCore.md)
- [/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine](DYLIBS/JetEngine.md)
- [/System/Library/PrivateFrameworks/JetUI.framework/JetUI](DYLIBS/JetUI.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor](DYLIBS/KnowledgeMonitor.md)
- [/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling](DYLIBS/LanguageModeling.md)
- [/System/Library/PrivateFrameworks/LegalAndRegulatorySettingsSupport.framework/LegalAndRegulatorySettingsSupport](DYLIBS/LegalAndRegulatorySettingsSupport.md)
- [/System/Library/PrivateFrameworks/Lexicon.framework/Lexicon](DYLIBS/Lexicon.md)
- [/System/Library/PrivateFrameworks/LiftUI.framework/LiftUI](DYLIBS/LiftUI.md)
- [/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore](DYLIBS/LocalAuthenticationCore.md)
- [/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices](DYLIBS/LockedContentServices.md)
- [/System/Library/PrivateFrameworks/MCCKitCategorization.framework/MCCKitCategorization](DYLIBS/MCCKitCategorization.md)
- [/System/Library/PrivateFrameworks/MDM.framework/MDM](DYLIBS/MDM.md)
- [/System/Library/PrivateFrameworks/MLModelSpecification.framework/MLModelSpecification](DYLIBS/MLModelSpecification.md)
- [/System/Library/PrivateFrameworks/MagnifierSupport.framework/MagnifierSupport](DYLIBS/MagnifierSupport.md)
- [/System/Library/PrivateFrameworks/ManagedAppsCore.framework/ManagedAppsCore](DYLIBS/ManagedAppsCore.md)
- [/System/Library/PrivateFrameworks/MapsSync.framework/MapsSync](DYLIBS/MapsSync.md)
- [/System/Library/PrivateFrameworks/MapsUI.framework/MapsUI](DYLIBS/MapsUI.md)
- [/System/Library/PrivateFrameworks/MeasureFoundation.framework/MeasureFoundation](DYLIBS/MeasureFoundation.md)
- [/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls](DYLIBS/MediaControls.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote](DYLIBS/MediaRemote.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI](DYLIBS/MentalHealthUI.md)
- [/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection](DYLIBS/MessageProtection.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex](DYLIBS/MobileSpotlightIndex.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit](DYLIBS/MobileStoreDemoKit.md)
- [/System/Library/PrivateFrameworks/MobileStoreDemoSetupUI.framework/MobileStoreDemoSetupUI](DYLIBS/MobileStoreDemoSetupUI.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/MobileTimerSupport.framework/MobileTimerSupport](DYLIBS/MobileTimerSupport.md)
- [/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog](DYLIBS/ModelCatalog.md)
- [/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime](DYLIBS/ModelCatalogRuntime.md)
- [/System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices](DYLIBS/ModelManagerServices.md)
- [/System/Library/PrivateFrameworks/Morpheus.framework/Morpheus](DYLIBS/Morpheus.md)
- [/System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal](DYLIBS/MusicKitInternal.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NDOAPI.framework/NDOAPI](DYLIBS/NDOAPI.md)
- [/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit](DYLIBS/NPTKit.md)
- [/System/Library/PrivateFrameworks/NanoTimeKitCompanion.framework/NanoTimeKitCompanion](DYLIBS/NanoTimeKitCompanion.md)
- [/System/Library/PrivateFrameworks/NeuralNetworks.framework/NeuralNetworks](DYLIBS/NeuralNetworks.md)
- [/System/Library/PrivateFrameworks/NewsArticles.framework/NewsArticles](DYLIBS/NewsArticles.md)
- [/System/Library/PrivateFrameworks/NewsEngagement.framework/NewsEngagement](DYLIBS/NewsEngagement.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsLiveActivitiesCore.framework/NewsLiveActivitiesCore](DYLIBS/NewsLiveActivitiesCore.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NexusDaemon.framework/NexusDaemon](DYLIBS/NexusDaemon.md)
- [/System/Library/PrivateFrameworks/NightingaleTraining.framework/NightingaleTraining](DYLIBS/NightingaleTraining.md)
- [/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor](DYLIBS/NotesEditor.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI](DYLIBS/NotesUI.md)
- [/System/Library/PrivateFrameworks/ODDIFramework.framework/ODDIFramework](DYLIBS/ODDIFramework.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/OnDeviceStorageCore](DYLIBS/OnDeviceStorageCore.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageInternal.framework/OnDeviceStorageInternal](DYLIBS/OnDeviceStorageInternal.md)
- [/System/Library/PrivateFrameworks/OpenAPIURLSessionInternal.framework/OpenAPIURLSessionInternal](DYLIBS/OpenAPIURLSessionInternal.md)
- [/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry](DYLIBS/PairedDeviceRegistry.md)
- [/System/Library/PrivateFrameworks/PaperKit.framework/PaperKit](DYLIBS/PaperKit.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation](DYLIBS/PassKitUIFoundation.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PeopleSuggesterLighthouse.framework/PeopleSuggesterLighthouse](DYLIBS/PeopleSuggesterLighthouse.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotosGraph.framework/PhotosGraph](DYLIBS/PhotosGraph.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PhotosensitivityProcessing.framework/PhotosensitivityProcessing](DYLIBS/PhotosensitivityProcessing.md)
- [/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework](DYLIBS/PnROnDeviceFramework.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer](DYLIBS/PoirotSchematizer.md)
- [/System/Library/PrivateFrameworks/PoirotUDFs.framework/PoirotUDFs](DYLIBS/PoirotUDFs.md)
- [/System/Library/PrivateFrameworks/PosterBoard.framework/PosterBoard](DYLIBS/PosterBoard.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended](DYLIBS/PreferencesExtended.md)
- [/System/Library/PrivateFrameworks/PreferencesUI.framework/PreferencesUI](DYLIBS/PreferencesUI.md)
- [/System/Library/PrivateFrameworks/PreviewShellKit.framework/PreviewShellKit](DYLIBS/PreviewShellKit.md)
- [/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS](DYLIBS/PreviewsFoundationOS.md)
- [/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection](DYLIBS/PreviewsInjection.md)
- [/System/Library/PrivateFrameworks/PreviewsMessagingOS.framework/PreviewsMessagingOS](DYLIBS/PreviewsMessagingOS.md)
- [/System/Library/PrivateFrameworks/PreviewsServicesUI.framework/PreviewsServicesUI](DYLIBS/PreviewsServicesUI.md)
- [/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization](DYLIBS/ProactiveSummarization.md)
- [/System/Library/PrivateFrameworks/ProductKit.framework/ProductKit](DYLIBS/ProductKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup](DYLIBS/ProximityAppleIDSetup.md)
- [/System/Library/PrivateFrameworks/ProximityReaderCore.framework/ProximityReaderCore](DYLIBS/ProximityReaderCore.md)
- [/System/Library/PrivateFrameworks/ProximityReaderDaemon.framework/ProximityReaderDaemon](DYLIBS/ProximityReaderDaemon.md)
- [/System/Library/PrivateFrameworks/QOSToolkit.framework/QOSToolkit](DYLIBS/QOSToolkit.md)
- [/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities](DYLIBS/RTTUtilities.md)
- [/System/Library/PrivateFrameworks/RemindersIntentsFramework.framework/RemindersIntentsFramework](DYLIBS/RemindersIntentsFramework.md)
- [/System/Library/PrivateFrameworks/RemindersUICore.framework/RemindersUICore](DYLIBS/RemindersUICore.md)
- [/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement](DYLIBS/RemoteManagement.md)
- [/System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice](DYLIBS/RemotePairingDevice.md)
- [/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI](DYLIBS/RemoteUI.md)
- [/System/Library/PrivateFrameworks/ReplicatorCore.framework/ReplicatorCore](DYLIBS/ReplicatorCore.md)
- [/System/Library/PrivateFrameworks/ReplicatorEngine.framework/ReplicatorEngine](DYLIBS/ReplicatorEngine.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/RequestDispatcherBridges.framework/RequestDispatcherBridges](DYLIBS/RequestDispatcherBridges.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/SafariSafeBrowsing](DYLIBS/SafariSafeBrowsing.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/ScreenSharingKit.framework/ScreenSharingKit](DYLIBS/ScreenSharingKit.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI](DYLIBS/ScreenTimeSettingsUI.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUICore.framework/ScreenTimeUICore](DYLIBS/ScreenTimeUICore.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/SensitiveContentAnalysisUI](DYLIBS/SensitiveContentAnalysisUI.md)
- [/System/Library/PrivateFrameworks/SentencePiece.framework/SentencePiece](DYLIBS/SentencePiece.md)
- [/System/Library/PrivateFrameworks/ServiceExtensions.framework/ServiceExtensions](DYLIBS/ServiceExtensions.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SessionSyncEngine.framework/SessionSyncEngine](DYLIBS/SessionSyncEngine.md)
- [/System/Library/PrivateFrameworks/Settings.framework/Settings](DYLIBS/Settings.md)
- [/System/Library/PrivateFrameworks/Settings/SettingsUIKitPrivate.framework/SettingsUIKitPrivate](DYLIBS/SettingsUIKitPrivate.md)
- [/System/Library/PrivateFrameworks/SeymourClient.framework/SeymourClient](DYLIBS/SeymourClient.md)
- [/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia](DYLIBS/SeymourMedia.md)
- [/System/Library/PrivateFrameworks/SeymourServices.framework/SeymourServices](DYLIBS/SeymourServices.md)
- [/System/Library/PrivateFrameworks/SeymourUI.framework/SeymourUI](DYLIBS/SeymourUI.md)
- [/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet](DYLIBS/ShareSheet.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/ShazamEvents.framework/ShazamEvents](DYLIBS/ShazamEvents.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation](DYLIBS/SiriActivation.md)
- [/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics](DYLIBS/SiriAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/SiriAppLaunchIntents](DYLIBS/SiriAppLaunchIntents.md)
- [/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal](DYLIBS/SiriAudioInternal.md)
- [/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport](DYLIBS/SiriAudioSupport.md)
- [/System/Library/PrivateFrameworks/SiriAutoComplete.framework/SiriAutoComplete](DYLIBS/SiriAutoComplete.md)
- [/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/SiriAutoCompleteAPI](DYLIBS/SiriAutoCompleteAPI.md)
- [/System/Library/PrivateFrameworks/SiriCalendarIntents.framework/SiriCalendarIntents](DYLIBS/SiriCalendarIntents.md)
- [/System/Library/PrivateFrameworks/SiriCam.framework/SiriCam](DYLIBS/SiriCam.md)
- [/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents](DYLIBS/SiriContactsIntents.md)
- [/System/Library/PrivateFrameworks/SiriExpanseInternal.framework/SiriExpanseInternal](DYLIBS/SiriExpanseInternal.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriIdentityInternal.framework/SiriIdentityInternal](DYLIBS/SiriIdentityInternal.md)
- [/System/Library/PrivateFrameworks/SiriInference.framework/SiriInference](DYLIBS/SiriInference.md)
- [/System/Library/PrivateFrameworks/SiriInferredHelpfulness.framework/SiriInferredHelpfulness](DYLIBS/SiriInferredHelpfulness.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow](DYLIBS/SiriKitFlow.md)
- [/System/Library/PrivateFrameworks/SiriKitRuntime.framework/SiriKitRuntime](DYLIBS/SiriKitRuntime.md)
- [/System/Library/PrivateFrameworks/SiriMailInternal.framework/SiriMailInternal](DYLIBS/SiriMailInternal.md)
- [/System/Library/PrivateFrameworks/SiriMailUI.framework/SiriMailUI](DYLIBS/SiriMailUI.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SiriMessagesUI.framework/SiriMessagesUI](DYLIBS/SiriMessagesUI.md)
- [/System/Library/PrivateFrameworks/SiriNaturalLanguageGeneration.framework/SiriNaturalLanguageGeneration](DYLIBS/SiriNaturalLanguageGeneration.md)
- [/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork](DYLIBS/SiriNetwork.md)
- [/System/Library/PrivateFrameworks/SiriNotebook.framework/SiriNotebook](DYLIBS/SiriNotebook.md)
- [/System/Library/PrivateFrameworks/SiriNotebookUI.framework/SiriNotebookUI](DYLIBS/SiriNotebookUI.md)
- [/System/Library/PrivateFrameworks/SiriNotificationsIntents.framework/SiriNotificationsIntents](DYLIBS/SiriNotificationsIntents.md)
- [/System/Library/PrivateFrameworks/SiriOntology.framework/SiriOntology](DYLIBS/SiriOntology.md)
- [/System/Library/PrivateFrameworks/SiriOntologyProtobuf.framework/SiriOntologyProtobuf](DYLIBS/SiriOntologyProtobuf.md)
- [/System/Library/PrivateFrameworks/SiriPaymentsIntents.framework/SiriPaymentsIntents](DYLIBS/SiriPaymentsIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents](DYLIBS/SiriPlaybackControlIntents.md)
- [/System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport](DYLIBS/SiriPlaybackControlSupport.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/SiriPrivateLearningAnalytics](DYLIBS/SiriPrivateLearningAnalytics.md)
- [/System/Library/PrivateFrameworks/SiriPrivateLearningInference.framework/SiriPrivateLearningInference](DYLIBS/SiriPrivateLearningInference.md)
- [/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers](DYLIBS/SiriRemembers.md)
- [/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup](DYLIBS/SiriSetup.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals](DYLIBS/SiriSignals.md)
- [/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions](DYLIBS/SiriSuggestions.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI](DYLIBS/SiriSuggestionsAPI.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsIntelligence.framework/SiriSuggestionsIntelligence](DYLIBS/SiriSuggestionsIntelligence.md)
- [/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport](DYLIBS/SiriSuggestionsSupport.md)
- [/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS](DYLIBS/SiriTTS.md)
- [/System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService](DYLIBS/SiriTTSService.md)
- [/System/Library/PrivateFrameworks/SiriTimeTimerInternal.framework/SiriTimeTimerInternal](DYLIBS/SiriTimeTimerInternal.md)
- [/System/Library/PrivateFrameworks/SiriTranslationIntents.framework/SiriTranslationIntents](DYLIBS/SiriTranslationIntents.md)
- [/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation](DYLIBS/SiriUIFoundation.md)
- [/System/Library/PrivateFrameworks/SiriVideoIntents.framework/SiriVideoIntents](DYLIBS/SiriVideoIntents.md)
- [/System/Library/PrivateFrameworks/SiriVirtualDeviceResolution.framework/SiriVirtualDeviceResolution](DYLIBS/SiriVirtualDeviceResolution.md)
- [/System/Library/PrivateFrameworks/SleepHealthUI.framework/SleepHealthUI](DYLIBS/SleepHealthUI.md)
- [/System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI](DYLIBS/SnippetUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/SonicKit](DYLIBS/SonicKit.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/Stickers.framework/Stickers](DYLIBS/Stickers.md)
- [/System/Library/PrivateFrameworks/StickersUI.framework/StickersUI](DYLIBS/StickersUI.md)
- [/System/Library/PrivateFrameworks/StocksPersonalization.framework/StocksPersonalization](DYLIBS/StocksPersonalization.md)
- [/System/Library/PrivateFrameworks/StocksUI.framework/StocksUI](DYLIBS/StocksUI.md)
- [/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices](DYLIBS/StoreServices.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/SyncedModels.framework/SyncedModels](DYLIBS/SyncedModels.md)
- [/System/Library/PrivateFrameworks/SystemUIAnimationKit.framework/SystemUIAnimationKit](DYLIBS/SystemUIAnimationKit.md)
- [/System/Library/PrivateFrameworks/TDGSharing.framework/TDGSharing](DYLIBS/TDGSharing.md)
- [/System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices](DYLIBS/TVAppServices.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TeaBreeze.framework/TeaBreeze](DYLIBS/TeaBreeze.md)
- [/System/Library/PrivateFrameworks/TeaCharts.framework/TeaCharts](DYLIBS/TeaCharts.md)
- [/System/Library/PrivateFrameworks/TeaDB.framework/TeaDB](DYLIBS/TeaDB.md)
- [/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation](DYLIBS/TeaFoundation.md)
- [/System/Library/PrivateFrameworks/TeaSettings.framework/TeaSettings](DYLIBS/TeaSettings.md)
- [/System/Library/PrivateFrameworks/TeaTemplate.framework/TeaTemplate](DYLIBS/TeaTemplate.md)
- [/System/Library/PrivateFrameworks/TeaUI.framework/TeaUI](DYLIBS/TeaUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyKit.framework/TelephonyKit](DYLIBS/TelephonyKit.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingUI.framework/TextToSpeechVoiceBankingUI](DYLIBS/TextToSpeechVoiceBankingUI.md)
- [/System/Library/PrivateFrameworks/ThirdPartyApplicationSettings.framework/ThirdPartyApplicationSettings](DYLIBS/ThirdPartyApplicationSettings.md)
- [/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam](DYLIBS/Tightbeam.md)
- [/System/Library/PrivateFrameworks/TipKitCore.framework/TipKitCore](DYLIBS/TipKitCore.md)
- [/System/Library/PrivateFrameworks/TipsTryIt.framework/TipsTryIt](DYLIBS/TipsTryIt.md)
- [/System/Library/PrivateFrameworks/TipsUI.framework/TipsUI](DYLIBS/TipsUI.md)
- [/System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration](DYLIBS/TokenGeneration.md)
- [/System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore](DYLIBS/TokenGenerationCore.md)
- [/System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference](DYLIBS/TokenGenerationInference.md)
- [/System/Library/PrivateFrameworks/ToolKit.framework/ToolKit](DYLIBS/ToolKit.md)
- [/System/Library/PrivateFrameworks/TranslationUI.framework/TranslationUI](DYLIBS/TranslationUI.md)
- [/System/Library/PrivateFrameworks/TrustKit.framework/TrustKit](DYLIBS/TrustKit.md)
- [/System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport](DYLIBS/UIIntelligenceSupport.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UINavigationKit.framework/UINavigationKit](DYLIBS/UINavigationKit.md)
- [/System/Library/PrivateFrameworks/UIUnderstanding.framework/UIUnderstanding](DYLIBS/UIUnderstanding.md)
- [/System/Library/PrivateFrameworks/UnifiedMessagingKit.framework/UnifiedMessagingKit](DYLIBS/UnifiedMessagingKit.md)
- [/System/Library/PrivateFrameworks/UniversalDrag.framework/UniversalDrag](DYLIBS/UniversalDrag.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit](DYLIBS/UserNotificationsKit.md)
- [/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/PrivateFrameworks/VFX.framework/VFX](DYLIBS/VFX.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit](DYLIBS/VectorKit.md)
- [/System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch](DYLIBS/VectorSearch.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisionCompanion.framework/VisionCompanion](DYLIBS/VisionCompanion.md)
- [/System/Library/PrivateFrameworks/VisionKitInternal.framework/VisionKitInternal](DYLIBS/VisionKitInternal.md)
- [/System/Library/PrivateFrameworks/VisualGeneration.framework/VisualGeneration](DYLIBS/VisualGeneration.md)
- [/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence](DYLIBS/VisualIntelligence.md)
- [/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding](DYLIBS/VisualUnderstanding.md)
- [/System/Library/PrivateFrameworks/VoiceActions.framework/VoiceActions](DYLIBS/VoiceActions.md)
- [/System/Library/PrivateFrameworks/VoiceControlUI.framework/VoiceControlUI](DYLIBS/VoiceControlUI.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI](DYLIBS/VoiceTriggerUI.md)
- [/System/Library/PrivateFrameworks/WallpaperKit.framework/WallpaperKit](DYLIBS/WallpaperKit.md)
- [/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore](DYLIBS/WeatherCore.md)
- [/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon](DYLIBS/WeatherDaemon.md)
- [/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps](DYLIBS/WeatherMaps.md)
- [/System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI](DYLIBS/WeatherUI.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WidgetRenderer.framework/WidgetRenderer](DYLIBS/WidgetRenderer.md)
- [/System/Library/PrivateFrameworks/WorkflowEditor.framework/WorkflowEditor](DYLIBS/WorkflowEditor.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness](DYLIBS/WorkflowResponsiveness.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkflowUICore.framework/WorkflowUICore](DYLIBS/WorkflowUICore.md)
- [/System/Library/PrivateFrameworks/WorkoutAnnouncements.framework/WorkoutAnnouncements](DYLIBS/WorkoutAnnouncements.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/WorkoutUI.framework/WorkoutUI](DYLIBS/WorkoutUI.md)
- [/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/XCTTargetBootstrap](DYLIBS/XCTTargetBootstrap.md)
- [/System/Library/PrivateFrameworks/ZeoliteLanguage.framework/ZeoliteLanguage](DYLIBS/ZeoliteLanguage.md)
- [/System/Library/PrivateFrameworks/_JetEngine_SwiftUI.framework/_JetEngine_SwiftUI](DYLIBS/_JetEngine_SwiftUI.md)
- [/System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI](DYLIBS/_MusicKitInternal_SwiftUI.md)
- [/System/Library/PrivateFrameworks/iCloudMailAccountUI.framework/iCloudMailAccountUI](DYLIBS/iCloudMailAccountUI.md)
- [/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota](DYLIBS/iCloudQuota.md)
- [/System/Library/PrivateFrameworks/iCloudSettings.framework/iCloudSettings](DYLIBS/iCloudSettings.md)
- [/usr/lib/libAppletTranslationLibrary.dylib](DYLIBS/libAppletTranslationLibrary.dylib.md)
- [/usr/lib/libboringssl.dylib](DYLIBS/libboringssl.dylib.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libnetwork.dylib](DYLIBS/libnetwork.dylib.md)
- [/usr/lib/libnfshared.dylib](DYLIBS/libnfshared.dylib.md)
- [/usr/lib/libobjc.A.dylib](DYLIBS/libobjc.A.dylib.md)
- [/usr/lib/libquic.dylib](DYLIBS/libquic.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libusrtcp.dylib](DYLIBS/libusrtcp.dylib.md)
- [/usr/lib/log/liblog_network.dylib](DYLIBS/liblog_network.dylib.md)
- [/usr/lib/swift/libswiftAVFoundation.dylib](DYLIBS/libswiftAVFoundation.dylib.md)
- [/usr/lib/swift/libswiftAccelerate.dylib](DYLIBS/libswiftAccelerate.dylib.md)
- [/usr/lib/swift/libswiftCore.dylib](DYLIBS/libswiftCore.dylib.md)
- [/usr/lib/swift/libswiftCoreMedia.dylib](DYLIBS/libswiftCoreMedia.dylib.md)
- [/usr/lib/swift/libswiftNaturalLanguage.dylib](DYLIBS/libswiftNaturalLanguage.dylib.md)
- [/usr/lib/swift/libswiftNetwork.dylib](DYLIBS/libswiftNetwork.dylib.md)
- [/usr/lib/swift/libswiftSpatial.dylib](DYLIBS/libswiftSpatial.dylib.md)
- [/usr/lib/swift/libswiftSystem.dylib](DYLIBS/libswiftSystem.dylib.md)
- [/usr/lib/swift/libswiftUIKit.dylib](DYLIBS/libswiftUIKit.dylib.md)
- [/usr/lib/swift/libswiftXPC.dylib](DYLIBS/libswiftXPC.dylib.md)
- [/usr/lib/swift/libswift_Concurrency.dylib](DYLIBS/libswift_Concurrency.dylib.md)
- [/usr/lib/system/libcopyfile.dylib](DYLIBS/libcopyfile.dylib.md)
- [/usr/lib/system/libcorecrypto.dylib](DYLIBS/libcorecrypto.dylib.md)
- [/usr/lib/system/libcorecrypto_noasm.dylib](DYLIBS/libcorecrypto_noasm.dylib.md)
- [/usr/lib/system/libcorecrypto_trace.dylib](DYLIBS/libcorecrypto_trace.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (175)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/Templates/dialog/carCommandsSetCarPlayClimateStatus.catfamily/intentHandledResponse.cat/en-ie.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/Templates/dialog/carCommandsSetCarPlayClimateStatus.catfamily/intentHandledResponse.cat/en-sg.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/Templates/dialog/carCommandsSetCarPlayClimateStatus.catfamily/intentHandledResponse.cat/en-za.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/CompanionAIIsOff.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/CompanionAIIsOff.cat/th.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/CompanionNotCapable.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/CompanionNotCapable.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/CompanionNotFound.cat/ar.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/CompanionNotFound.cat/es-cl.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/CompanionNotFound.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/CompanionNotFound.cat/hi.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/ProtocolIncompatible.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/UserLocationUnknown.cat/es-mx.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/UserLocationUnknown.cat/pt.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/Templates/dialog/IFFlow.catfamily/UserLocationUnknown.cat/zh-cn.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/SocialConversationFlowDelegatePlugin.bundle/Templates/dialog/SocialConversation.catfamily/dalFeelingUplift.cat/vi_VN_u_sd_vnct.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionGroup.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/DeviceExpertIntents.framework/Templates/dialog/DeviceExpert.catfamily/AttributionList.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/de-ch.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/en-za.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/es-cl.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/GenerativeAssistantActions.framework/Templates/dialog/GenerativeAssistantTools.catfamily/modelDownloadingErrorResponse.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/HomeAutomationInternal.framework/Templates/dialog/HomeAutomation.catfamily/ConfirmTemperature.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/Lexicon.framework/al-lexicon.dat`
- `/System/Library/PrivateFrameworks/Lexicon.framework/al-lexicon.idx`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Settings_ChangeSettings.cat/es-cl.cat.bin`
- `/private/var/staged_system_apps/Freeform.app/Base.lproj/nlu.appintents`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/4728d85cdbf7b3580e4b3b80b9e30fb2.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/1428c8d75ce1dff809f4142f6fd12dcb.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/d4dca2d8b43ebbcd825f4d2922ce132e.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/22292dd88fca6cabff3b6e0ccc9d55a7.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/9ce6fcbd8cfd38251786828815da4dba.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/bb94fccf0e60c39ba51856f4b69a9d78.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/5d6e06dff7380a780461eae63630b0e2.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/ee1a787a45d3f133aa9a855f2c899236.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/cb9d507db7d0a83d8097a6d012f7259f.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/b26f8fa4c14a268ae08bdd8f39cf6ddc.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/95c39a2e1de44b45a854e154fdb7f3be.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/0b909522c9526e3b97ce21b3a9fb57bd.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/8c7f70c2f5c27c6a9d6b99fe1582fe2d.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/1339b18492eb52e2a772b1227c0208ce.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/3822b4c6c31ddac4541ad7f4500112d1.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/fa3c6d64a734f59f88a60414254b580f.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/ef730f90ae9eac85b35f65da5d5c4b6b.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/9e3fbccabf5abe4668bbd8e580e81aef.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/d953558d47b66922335a5eb91c9a0d97.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/bac95a6a4cee5e312a870b5dd66ee611.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/8c7835573b9aba02456c055bb16fc1f9.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/76d05b8e16319063ca81e673bd97e145.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/a1195f9bea00930f1dbbc4fc0e7092fe.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/ad93749896c30d778647ab6f90b0258e.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/1164e579c8037e75eeb4ae6c5c2140d2.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/32b20c6dbb7ced387a84e57323a0d9f4.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/7f739accf58a800c85b60e2ed46094f0.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/da420b505d5cf2c4a1b66bfe8661ad2b.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/46bdc8d27bae1ff60c1c348195579fa0.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/756a4005e92aa4c75a01498b389ab8d2.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/6e24e2a6c254778765afdbeae8f72d72.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/f18e675a9f2233aa92e4ad264d5a235c.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/a8f22818ef4f694b8fad6cfd58fec12a.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/578867246a385ba8ff8ab406efd420c2.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/55269225074f4723f863342d3db927d2.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/ca535a65ffb0ca7a64f07ad8c81307a6.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/e59f5fbb437590d4c1cb0333c043538c.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/6bb584064225c6d864e819deb93d3c2c.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/d4a04856da463222a60e696ab5f54d01.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/bc570adc7c2b950201879878d23b187c.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/adb24457f08a998b6016beb856555193.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/2f4e7b4a2cf5260302dc6b0754bd90ae.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/a7070117af18c8d82ef48227061b26f0.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/3c7482ac4b289e0f7c773df5d0509fd7.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/c279798735024110de8f170357d3a9bd.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/80f4866224acd710b52e752f5c6868d3.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/16c9f6cb19a891749f5a92999ccfffc8.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/4ae57218da3ad7c832be326eaa670c5a.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/e570ca6f941b3cc4e8366cf1e883d737.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/b25ee90b6213fd22cc67ef6e998ceaca.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/f5852e4f5276460bd2f2e3b12461527b.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/21babc96cd60bc61dfce66ce60b30273.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/6df263de6e0df9cd51884917d9bff7dd.version`

</details>

### ❌ Removed

#### filesystem (63)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/Templates/dialog/carCommandsSetCarPlayClimateStatus.catfamily/intentHandledResponse.cat/es-us.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/Templates/dialog/carCommandsSetCarPlayClimateStatus.catfamily/intentHandledResponse.cat/fr-be.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/Templates/dialog/carCommandsSetCarPlayClimateStatus.catfamily/intentHandledResponse.cat/fr-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/Templates/dialog/carCommandsSetCarPlayClimateStatus.catfamily/intentHandledResponse.cat/it-ch.cat.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/Templates/dialog/carCommandsSetCarPlayClimateStatus.catfamily/intentHandledResponse.cat/vi_VN_u_sd_vnct.cat.bin`
- `/System/Library/PrivateFrameworks/SiriKitFlow.framework/Templates/dialog/HandoffErrors.catfamily/CompanionEOLForProfileSync.cat/fr-ca.cat.bin`
- `/private/var/staged_system_apps/Freeform.app/en.lproj/nlu.appintents`
- `/private/var/staged_system_apps/Home.app/PlugIns/HomeUtilNotification.appex/es_US.lproj`
- `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookQuicklookPreviewExtension.appex/en_IN.lproj`
- `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookQuicklookPreviewExtension.appex/es_US.lproj`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/45887d781d95d44f50df416bf607dab1.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/1c409a39993c1b2e25acd27fe6fef5db.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/3489555b6d89cf0b99017f1f80d589d3.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/8f4861f27bb6961a87a03c68f17575f8.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/cbba452604bca4fcd4295b94c2b9d8fe.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/978d94c1f163082d79d8866050ab8ec7.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/6f87f7836998c0e1270371c8e276734b.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/2c7ad312771243d9353c6d9585a6ce2a.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/060ca9c42d235c55491f0c6d189bdc47.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/519594fed90784b000b86c07ee364e7e.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/a7e35e2a6a32f9ce62f505ab34290c1a.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/59773de56e7a0a5f34b556aef6a976d0.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/ddf4e403d4912a795354cf68624bd9bd.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/662751c378584280dbc1bd121d2410e3.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/83b5ab5d2d7a3b24a83b33cca98553e1.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/dca16e64f7365a92da03ffecc80a2f39.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/a75321032570306b58e5fda9b59649c8.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/2e1ef679c23a257e1c18ee6a3ecf0a2c.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/73b0e81821f2811603f4f14935e0ce0c.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/d6e88577ad1bd76b0d1c0bd3e1924338.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/3330a37719fabe4ddcfefd2a93120a0d.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/eec705357ac49122a032d09594297d2a.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/5d525a3803276339a8d377ee039ebc9a.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/f5e9909cbbaa0fb95f41b0b269ba48ed.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/fa475a0e956faa3a215907d034f82a93.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/3dc4450d67e649c1491bf8c80e2adccc.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/3a65b593ded4841f2002c80472843415.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/e46bbfc87dcd080f98ded278f4fbfa20.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/9df606a9137e8a5351d4101095db8374.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/3e95a3d6ab226f029de86870cbe141b0.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/f999f593da3c49aaa15741edc8bbff3b.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/6c9f61fe6a7b2733d7690987f81615bb.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/cc3050f6b9ee10cbc7fc3431bfa9dd78.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/93030de495058e763ab6fe17fe8f0a99.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/72d469d3440b3ad43d7192ea263c6bdc.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/83dbd431fbf46032325b55a607fc58c0.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/db27ac3b17bee1fc6b13580361424540.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/fbf9c51d0ad5bcd317db8f5709c26289.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/c1bd638ed2c27bc7e25b08a6892b1827.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/fd24c92cb7d1589f037bcb44368cb8fc.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/2322222857d63db59bd2b8b40c46b434.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/b25c8fbb17ed6c616705b4c6fccdda91.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/b75c0d7e49b16ba56b91e40ccd731222.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/e105fd0e0674cccad7500cbbf6885c4e.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/1a52fcaa6556f355abd9786aa7f45de9.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/290fe020673a50f8ce3d5c2d2778f1f8.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/a956b2fb9637c53fb9204c936b2decfa.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/738da16e99d6df0811f67b61a5d9af61.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/2a49f0d2a5bf7f9cb021df03d1715f76.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/ec6b292002c9791ef6c95c1a45e16776.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/a3a90fef3af3db48a8bd438243edd428.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/caa11a3850f90c867d26b1310212943f.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/d342251cbece2986ac4965df662e0206.version`

</details>

## Feature Flags

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### MobileAsset.plist

>  `Domain/MobileAsset.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>LiveStorageExclaveNonce</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
 	<key>com_apple_mobileassetd_conclave</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```


</details>

## EOF
