# 18.7.2 (22H124) .vs 18.7.3 (22H217)

## IPSWs

- `iPhone11,2,iPhone11,4,iPhone11,6_18.7.2_22H124_Restore.ipsw`
- `iPhone11,2,iPhone11,4,iPhone11,6_18.7.3_22H217_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.7.2 *(22H124)* | 24.6.0 | 11417.140.69.702.20~1 | Wed, 15Oct2025 21:14:36 PDT |
| 18.7.3 *(22H217)* | 24.6.0 | 11417.140.69.704.2~1 | Wed, 05Nov2025 21:28:58 PST |

### Kexts

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.kernel

>  `com.apple.kernel`

```diff

-11417.140.69.702.20
+11417.140.69.704.2
   __TEXT.__const: 0x349f0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x6e2aa
+  __TEXT.__cstring: 0x6e2b1
   __TEXT.__os_log: 0x2a585
   __TEXT.__thread_starts: 0x0
   __TEXT.__eh_frame: 0x4e0

   __DATA_CONST.__assert: 0x1cc
   __DATA_CONST.__kern_brk_desc: 0x60
   __TEXT_EXEC.__hib_text: 0xc88
-  __TEXT_EXEC.__text: 0x7e40a4
+  __TEXT_EXEC.__text: 0x7e412c
   __KLD.__text: 0x16d4
   __PPLTEXT.__text: 0x1c930
   __PPLTRAMP.__text: 0xc008

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x46722
-  UUID: 81175E06-7DEE-3088-AEB1-C3BD9889A505
+  UUID: 247C3617-025F-3A7D-B380-D4A653CAB7A7
   Functions: 19448
   Symbols:   0
-  CStrings:  17284
+  CStrings:  17285
 
Functions:
~ sub_fffffff007ed63d8 : 448 -> 472
~ _vm_fault_internal : 14008 -> 14128
~ _vm_fault_copy : 2572 -> 2568
~ _vm_map_wire_nested : 4192 -> 4200
~ sub_fffffff007f5f200 -> sub_fffffff007f5f294 : 100 -> 96
~ sub_fffffff007f764bc -> sub_fffffff007f7654c : 3368 -> 3364
~ _vm_object_upl_request : 4736 -> 4724
~ sub_fffffff007fa6794 -> sub_fffffff007fa6814 : 204 -> 196
~ sub_fffffff008060454 -> sub_fffffff0080604cc : 156 -> 176
~ sub_fffffff0082ecfb4 -> sub_fffffff0082ed040 : 564 -> 560
~ _firehose_buffer_tracepoint_reserve_slow.cold.1 : 16264 -> 16128
CStrings:
+ "%s: map %p va 0x%llx obj %p,%llu saved %p,%llu: unexpected CoW @%s:%d"
+ "fd"
- "%s: map %p va 0x%llx obj %p,%u saved %p,%u: unexpected CoW @%s:%d"

```

#### com.apple.security.sandbox

>  `com.apple.security.sandbox`

```diff

 2401.140.15.0.0
   __TEXT.__os_log: 0x2092
-  __TEXT.__const: 0x1bb121
+  __TEXT.__const: 0x1bb191
   __TEXT.__cstring: 0x71cc
   __TEXT_EXEC.__text: 0x31634
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x35f0
   __DATA_CONST.__kalloc_type: 0xb40
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: 591A2AC8-2B7F-3538-B8A4-DAE65D51CA4B
+  UUID: 7345EFEF-271B-3647-AF63-0FEABD59369A
   Functions: 639
   Symbols:   0
   CStrings:  1322

```


</details>

## MachO

### ⬆️ Updated (49)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AMSEngagementViewService.app/AMSEngagementViewService](MACHOS/AMSEngagementViewService.md)
- [/Applications/Jellyfish.app/PlugIns/Animoji.appex/Animoji](MACHOS/Animoji.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/SharedWebCredentialViewService.app/SharedWebCredentialViewService](MACHOS/SharedWebCredentialViewService.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension](MACHOS/StickersUltraExtension.md)
- [/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver](MACHOS/VoiceOver.md)
- [/System/Library/Accounts/DataclassOwners/KeychainDataclassOwner.bundle/KeychainDataclassOwner](MACHOS/KeychainDataclassOwner.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/CoreServices/IntelligentLight.app/IntelligentLight](MACHOS/IntelligentLight.md)
- [/System/Library/DataClassMigrators/PreferencesMigrator.migrator/PreferencesMigrator](MACHOS/PreferencesMigrator.md)
- [/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension](MACHOS/AssistantSettingsControlsExtension.md)
- [/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension](MACHOS/ScreenTimeAppIntentsExtension.md)
- [/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd](MACHOS/fileproviderd.md)
- [/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension](MACHOS/ScreenTimeWebExtension.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/XPCAcmeService.xpc/XPCAcmeService](MACHOS/XPCAcmeService.md)
- [/System/Library/Frameworks/Security.framework/swcagent](MACHOS/swcagent.md)
- [/System/Library/PreferenceManifestsInternal/PreferencesManifests.bundle/PreferencesManifests](MACHOS/PreferencesManifests.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPosterExtension.appex/AvatarPosterExtension](MACHOS/AvatarPosterExtension.md)
- [/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService](MACHOS/com.apple.NeighborhoodActivityConduitService.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent](MACHOS/ScreenTimeAgent.md)
- [/System/Library/PrivateFrameworks/ScreenTimeUI.framework/PlugIns/ScreenTimeNotificationContentExtension.appex/ScreenTimeNotificationContentExtension](MACHOS/ScreenTimeNotificationContentExtension.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService](MACHOS/com.apple.FTLivePhotoService.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/UsageBundles/SoftwareUpdateUsage.bundle/SoftwareUpdateUsage](MACHOS/SoftwareUpdateUsage.md)
- [/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp](MACHOS/AppleVisionProApp.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone](MACHOS/PassbookWidgetsExtension-iPhone.md)
- [/usr/bin/fileproviderctl](MACHOS/fileproviderctl.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/meshnetd](MACHOS/meshnetd.md)
- [/usr/libexec/otpaird](MACHOS/otpaird.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sirireaderd](MACHOS/sirireaderd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/sbin/ckksctl](MACHOS/ckksctl.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

### iBoot

| iOS | Version |
| :-- | :------ |
| 18.7.2 *(22H124)* | iBoot-11881.140.96 |
| 18.7.3 *(22H217)* | iBoot-11881.140.96 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.7.2 *(22H124)* | 621.5.1.10.7 |
| 18.7.3 *(22H217)* | 621.6.1.10.3 |

### Dylibs

#### ⬆️ Updated (34)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification](DYLIBS/KeychainSyncAccountNotification.md)
- [/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs](DYLIBS/AudioCodecs.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/FileProvider.framework/FileProvider](DYLIBS/FileProvider.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/Intents.framework/Intents](DYLIBS/Intents.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL](DYLIBS/AppleJPEGXL.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit](DYLIBS/ConversationKit.md)
- [/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon](DYLIBS/FileProviderDaemon.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/MIME.framework/MIME](DYLIBS/MIME.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI](DYLIBS/SafariSharedUI.md)
- [/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput](DYLIBS/ScreenReaderOutput.md)
- [/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore](DYLIBS/ScreenTimeCore.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib](DYLIBS/libwebrtc.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU](DYLIBS/WebGPU.md)
- [/System/Library/PrivateFrameworks/WebInspector.framework/WebInspector](DYLIBS/WebInspector.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libarchive.2.dylib](DYLIBS/libarchive.2.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (1)

- `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/Errors.loctable`

## EOF
