# 18.0 (22A3354) .vs 18.0.1 (22A3370)

## IPSWs

- `iPhone16,2_18.0_22A3354_Restore.ipsw`
- `iPhone16,2_18.0.1_22A3370_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.0 *(22A3354)* | 24.0.0 | 11215.2.5~62 | Thu, 08Aug2024 01:17:15 PDT |
| 18.0.1 *(22A3370)* | 24.0.0 | 11215.2.5~62 | Thu, 08Aug2024 01:17:15 PDT |

### Kexts

#### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.AppleH16CameraInterface`

```diff

-3.48.0.0.0
+3.50.0.0.0
   __TEXT.__const: 0xa058
-  __TEXT.__cstring: 0x19384
-  __TEXT.__os_log: 0x15451
-  __TEXT_EXEC.__text: 0x9b894
+  __TEXT.__cstring: 0x194cf
+  __TEXT.__os_log: 0x1551d
+  __TEXT_EXEC.__text: 0x9bba0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a0
   __DATA.__common: 0x4a0

   __DATA_CONST.__const: 0xa0e8
   __DATA_CONST.__kalloc_type: 0x1300
   __DATA_CONST.__kalloc_var: 0xd70
-  Functions: 1907
+  Functions: 1909
   Symbols:   0
-  CStrings:  3276
+  CStrings:  3285
 
CStrings:
+ "\"AppleH16CamIn::%s: Doorbell number exceeds maximum number of supported ISP doorbells\\n\" @%s:%d"
+ "AppleH16CamIn:%s - Forcing ISP shutdown\n"
+ "AppleH16CamIn:%s - ISP is not fully powered ON, can't proceed with a forced shutdown\n"
+ "AppleH16CamIn:%s - Timed out waiting for ISPCPU to be shutdown, gpr6 = 0x%x\n"
+ "ISP_ForceShutdown"
+ "RingDoorbell"

```

>  `com.apple.security.sandbox`

```diff

 2401.0.65.0.0
-  __TEXT.__const: 0x189169
+  __TEXT.__const: 0x189179
   __TEXT.__cstring: 0x6efc
   __TEXT.__os_log: 0x2029
   __TEXT_EXEC.__text: 0x30494

```

</details>

## MachO

### ⬆️ Updated (32)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/FontPickerUIService.app/FontPickerUIService](MACHOS/FontPickerUIService.md)
- [/Applications/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget](MACHOS/PhotosReliveWidget.md)
- [/Applications/Setup.app/Setup](MACHOS/Setup.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib](MACHOS/libsystem_malloc_debug.dylib.md)
- [/System/Library/AccessibilityBundles/AXAVSPluginService.axuiservice/AXAVSPluginService](MACHOS/AXAVSPluginService.md)
- [/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService](MACHOS/LiveSpeechUIService.md)
- [/System/Library/AppRemovalServices/com.apple.Translate.appremoval.xpc/com.apple.Translate.appremoval](MACHOS/com.apple.Translate.appremoval.md)
- [/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator](MACHOS/BuddyMigrator.md)
- [/System/Library/DataClassMigrators/CookieDataMigrator.migrator/CookieDataMigrator](MACHOS/CookieDataMigrator.md)
- [/System/Library/ExtensionKit/Extensions/TranslationAPISupportExtension.appex/TranslationAPISupportExtension](MACHOS/TranslationAPISupportExtension.md)
- [/System/Library/Frameworks/CFNetwork.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension](MACHOS/DiagnosticExtension.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService](MACHOS/TranslationUIService.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/PlugIns/TranslationWidgetsExtension.appex/TranslationWidgetsExtension](MACHOS/TranslationWidgetsExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/usr/libexec/backboardd](MACHOS/backboardd.md)
- [/usr/libexec/nfcd](MACHOS/nfcd.md)
- [/usr/libexec/seld](MACHOS/seld.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### adc-aceso-d8x.im4p

>  `adc-aceso-d8x.im4p`

```diff

   __TEXT.__text: 0x7a88d4
   __TEXT.__data_copy: 0x100000
   __TEXT.__const: 0x7fd9b0
-  __TEXT.__cstring: 0x9c02a
+  __TEXT.__cstring: 0x9c051
   __TEXT._rtk_mtab: 0x2a0
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA.__zerofill: 0x20de60
   Functions: 0
   Symbols:   0
-  CStrings:  17209
+  CStrings:  17211
 
CStrings:
+ "19:49:55"
+ "Dirty shutdown"
+ "Dirty shutdown request\n"
+ "Sep 24 2024"
- "20:33:37"
- "Aug 12 2024"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.0 *(22A3354)* | 619.1.26.30.5 |
| 18.0.1 *(22A3370)* | 619.1.26.30.7 |

### Dylibs

#### ⬆️ Updated (44)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Frameworks/CFNetwork.framework/CFNetwork](DYLIBS/CFNetwork.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI](DYLIBS/_MapKit_SwiftUI.md)
- [/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI](DYLIBS/AccessibilitySettingsUI.md)
- [/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities](DYLIBS/AccessibilityUtilities.md)
- [/System/Library/PrivateFrameworks/AdaptiveVoiceShortcuts.framework/AdaptiveVoiceShortcuts](DYLIBS/AdaptiveVoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore](DYLIBS/AuthenticationServicesCore.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/DeviceDiscoveryUI.framework/DeviceDiscoveryUI](DYLIBS/DeviceDiscoveryUI.md)
- [/System/Library/PrivateFrameworks/IDS.framework/IDS](DYLIBS/IDS.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/KnowledgeGraphKit.framework/KnowledgeGraphKit](DYLIBS/KnowledgeGraphKit.md)
- [/System/Library/PrivateFrameworks/MailUI.framework/MailUI](DYLIBS/MailUI.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync](DYLIBS/MessagesCloudSync.md)
- [/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI](DYLIBS/MessagesSettingsUI.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI](DYLIBS/PasswordManagerUI.md)
- [/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PhotoAnalysis](DYLIBS/PhotoAnalysis.md)
- [/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PhotosIntelligence](DYLIBS/PhotosIntelligence.md)
- [/System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore](DYLIBS/PhotosSwiftUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/PhotosUIFoundation](DYLIBS/PhotosUIFoundation.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI](DYLIBS/SafetyMonitorUI.md)
- [/System/Library/PrivateFrameworks/Sharing.framework/Sharing](DYLIBS/Sharing.md)
- [/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow](DYLIBS/SiriMessagesFlow.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/WebBookmarksSwift.framework/WebBookmarksSwift](DYLIBS/WebBookmarksSwift.md)
- [/usr/lib/libPN548_API.dylib](DYLIBS/libPN548_API.dylib.md)
- [/usr/lib/system/libsystem_malloc.dylib](DYLIBS/libsystem_malloc.dylib.md)

</details>

## EOF
