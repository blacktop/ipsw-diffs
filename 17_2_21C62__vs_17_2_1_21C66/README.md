# 17.2 (21C62) .vs 17.2.1 (21C66)

## IPSWs

- `iPhone16,1_17.2_21C62_Restore.ipsw`
- `iPhone16,1_17.2.1_21C66_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.2 *(21C62)* | 23.2.0 | 10002.60.75.0.3~27 | Sun, 12Nov2023 06:35:58 PST |
| 17.2.1 *(21C66)* | 23.2.0 | 10002.60.75.0.3~27 | Sun, 12Nov2023 06:35:58 PST |

### Kexts

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.security.sandbox`

```diff

   __DATA_CONST.__const: 0x3478
   __DATA_CONST.__kalloc_var: 0x550
   __DATA_CONST.__kalloc_type: 0xbc0
-  UUID: 43A8C0B4-CE57-302F-8044-5B8EFDCA37FA
+  UUID: 5A0A0C39-FC51-3CD2-82B2-84FF541C22B4
   Functions: 553
   Symbols:   0
   CStrings:  1227

```

</details>

## MachO

### ⬆️ Updated (28)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/FaceTimeLinkTrampoline.app/FaceTimeLinkTrampoline](MACHOS/FaceTimeLinkTrampoline.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/InCallService.app/PlugIns/FaceTimeShareExtension.appex/FaceTimeShareExtension](MACHOS/FaceTimeShareExtension.md)
- [/Applications/InCallService.app/PlugIns/IntentsUI.appex/IntentsUI](MACHOS/IntentsUI.md)
- [/Applications/InCallService.app/PlugIns/RemotePeoplePicker.appex/RemotePeoplePicker](MACHOS/RemotePeoplePicker.md)
- [/Applications/MobilePhone.app/MobilePhone](MACHOS/MobilePhone.md)
- [/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension](MACHOS/VoicemailMessageNotificationExtension.md)
- [/System/Library/ControlCenter/Bundles/SilenceCallsCCWidget.bundle/SilenceCallsCCWidget](MACHOS/SilenceCallsCCWidget.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService](MACHOS/CoreSpotlightService.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension1_iOS.appex/CoreSpotlightImportExtension1_iOS](MACHOS/CoreSpotlightImportExtension1_iOS.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightImportExtension2_iOS.appex/CoreSpotlightImportExtension2_iOS](MACHOS/CoreSpotlightImportExtension2_iOS.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged](MACHOS/spotlightknowledged.md)
- [/System/Library/PreferenceBundles/BlocklistSettings.bundle/BlocklistSettings](MACHOS/BlocklistSettings.md)
- [/System/Library/PreferenceBundles/CallDirectorySettings.bundle/CallDirectorySettings](MACHOS/CallDirectorySettings.md)
- [/System/Library/PreferenceBundles/CallScreeningSettingsBundle.bundle/CallScreeningSettingsBundle](MACHOS/CallScreeningSettingsBundle.md)
- [/System/Library/PreferenceBundles/ICBSettingsBundle.bundle/ICBSettingsBundle](MACHOS/ICBSettingsBundle.md)
- [/System/Library/PreferenceBundles/ICSSettingsBundle.bundle/ICSSettingsBundle](MACHOS/ICSSettingsBundle.md)
- [/System/Library/PreferenceBundles/NameAndPhotoSettingsBundle.bundle/NameAndPhotoSettingsBundle](MACHOS/NameAndPhotoSettingsBundle.md)
- [/System/Library/PreferenceBundles/PrimaryCloudCallingSettingsBundle.bundle/PrimaryCloudCallingSettingsBundle](MACHOS/PrimaryCloudCallingSettingsBundle.md)
- [/System/Library/PreferenceBundles/ReplyWithMessageSettings.bundle/ReplyWithMessageSettings](MACHOS/ReplyWithMessageSettings.md)
- [/System/Library/PreferenceBundles/SIMSettings.bundle/SIMSettings](MACHOS/SIMSettings.md)
- [/System/Library/PreferenceBundles/SecondaryCloudCallingSettingsBundle.bundle/SecondaryCloudCallingSettingsBundle](MACHOS/SecondaryCloudCallingSettingsBundle.md)
- [/System/Library/PreferenceBundles/SharePlaySettings.bundle/SharePlaySettings](MACHOS/SharePlaySettings.md)
- [/System/Library/PreferenceBundles/SilenceCallsSettingBundle.bundle/SilenceCallsSettingBundle](MACHOS/SilenceCallsSettingBundle.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.2 *(21C62)* | 617.1.17.10.9 |
| 17.2.1 *(21C66)* | 617.1.17.10.9 |

### Dylibs

#### ⬆️ Updated (17)

<details>
  <summary><i>View Updated</i></summary>

#### Phone

>  `/System/Library/Assistant/Plugins/Phone.assistantBundle/Phone`

```diff

-2869.300.81.2.3
+2869.300.81.2.4
   __TEXT.__text: 0x5460
   __TEXT.__auth_stubs: 0x340
   __TEXT.__objc_methlist: 0x26c

   - /System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 68CCCECF-03B6-3F05-8600-E057519174F0
+  UUID: 0FBFF852-4DD0-31E9-85C9-C2C532F3501F
   Functions: 86
   Symbols:   142
   CStrings:  412

```

#### CoreSpotlight

>  `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0x9d6f8
   __TEXT.__auth_stubs: 0x1950
   __TEXT.__objc_methlist: 0x990c

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6C96A9CF-F497-377A-9BA5-FEACF68AC41E
+  UUID: DFCE0D9D-E112-3907-89AC-D5AC4AAA3D16
   Functions: 4294
   Symbols:   13359
   CStrings:  9207

```

#### CarrierSettings

>  `/System/Library/PreferenceBundles/CarrierSettings.bundle/CarrierSettings`

```diff

-2869.300.81.2.3
+2869.300.81.2.4
   __TEXT.__text: 0x87dc
   __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x82c

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 518C7E3E-7473-3FC1-9B91-AB4EF32D754E
+  UUID: 014BB840-984F-35AD-BA07-9CB455DCFC69
   Functions: 194
   Symbols:   872
   CStrings:  529

```

#### MobilePhoneSettings

>  `/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings`

```diff

-2869.300.81.2.3
+2869.300.81.2.4
   __TEXT.__text: 0x5430
   __TEXT.__auth_stubs: 0x3b0
   __TEXT.__objc_methlist: 0x5f0

   - /System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EDA60117-DA80-3334-ABB8-CB7DF048ADE0
+  UUID: 4B5C6015-A451-345B-B3E6-A9E22A88831F
   Functions: 134
   Symbols:   720
   CStrings:  493

```

#### CSExattrCrypto

>  `/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0x8764
   __TEXT.__auth_stubs: 0x9d0
   __TEXT.__objc_methlist: 0x2b8

   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76500631-893A-375F-9657-5FB1F11E4A50
+  UUID: 033B8199-62F0-3F79-BF6E-F6BE297B030D
   Functions: 145
   Symbols:   757
   CStrings:  375

```

#### MetadataUtilities

>  `/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0x36ac0
   __TEXT.__auth_stubs: 0x1610
   __TEXT.__objc_methlist: 0x460

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CD9A26CE-71C0-306C-9EB6-D6662277205D
+  UUID: 2D6B1C1E-5688-3F6D-BE05-1A6FCD18BFC4
   Functions: 929
   Symbols:   2462
   CStrings:  1626

```

#### MobileSpotlightIndex

>  `/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0x313e10
   __TEXT.__auth_stubs: 0x3040
   __TEXT.__objc_methlist: 0x20

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5496C9CE-5941-328E-8FED-4D3241E93CF2
+  UUID: 036F1499-2910-3059-AB97-15C374E2F554
   Functions: 6905
   Symbols:   20367
   CStrings:  6026

```

#### Search

>  `/System/Library/PrivateFrameworks/Search.framework/Search`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0x11520
   __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_methlist: 0xfe8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 89CAB0DB-116A-3581-92DA-4B165EB270F2
+  UUID: 566F7385-23E5-3AA0-A886-5EA71EB93CAF
   Functions: 563
   Symbols:   2126
   CStrings:  1556

```

#### Spotlight

>  `/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0xa0d4
   __TEXT.__auth_stubs: 0x750
   __TEXT.__objc_methlist: 0x734

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0D417F7A-D564-3D2F-B578-AA207E1F37C3
+  UUID: A059003A-0147-388A-9B01-F887509686AA
   Functions: 192
   Symbols:   1056
   CStrings:  626

```

#### SpotlightDaemon

>  `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0x710d4
   __TEXT.__auth_stubs: 0x1770
   __TEXT.__objc_methlist: 0x2ee0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E87A635-5A56-3AAF-8F59-05E0AD99C72D
+  UUID: FDC8BF30-B441-3DDF-9878-11005D6606DC
   Functions: 2036
   Symbols:   6960
   CStrings:  3772

```

#### SpotlightFoundation

>  `/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0x8404
   __TEXT.__auth_stubs: 0x390
   __TEXT.__objc_methlist: 0x460

   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7FBA7223-C199-32A1-B81B-59EDEFDBE33B
+  UUID: 68341032-9B38-37B6-A443-20D3B7114B5D
   Functions: 157
   Symbols:   634
   CStrings:  398

```

#### SpotlightLinguistics

>  `/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0x17b64
   __TEXT.__auth_stubs: 0xc80
   __TEXT.__const: 0x19f

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 29915DA1-3213-39AA-AF76-AF3B55C7FB9A
+  UUID: 5FFD1749-18D3-31A2-A307-1CE9E76CFB80
   Functions: 417
   Symbols:   1236
   CStrings:  380

```

#### SpotlightReceiver

>  `/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0x348c
   __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_methlist: 0x190

   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F8507E4-E200-3614-894F-7B7BB63848BA
+  UUID: 580D6C6A-95B6-3782-BF55-FC73AE8005F0
   Functions: 74
   Symbols:   344
   CStrings:  176

```

#### SpotlightRecommendation

>  `/System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0xf2a0
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_methlist: 0x420

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D66557AD-64BC-39EB-B9BD-AFD2CC13337D
+  UUID: E9247E8B-64F0-339C-A0D7-836483E1C0BE
   Functions: 219
   Symbols:   814
   CStrings:  706

```

#### SpotlightResources

>  `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0x14a90
   __TEXT.__auth_stubs: 0x540
   __TEXT.__objc_methlist: 0xe08

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E53EDFEF-96BD-3CF1-9029-B454AFFD234F
+  UUID: BBCFD4D8-19B9-36E4-AA90-23BA7255E870
   Functions: 425
   Symbols:   1629
   CStrings:  1061

```

#### SpotlightServices

>  `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2274.8.2.0.0
+2274.8.3.0.0
   __TEXT.__text: 0xe5958
   __TEXT.__auth_stubs: 0x1380
   __TEXT.__objc_methlist: 0x951c

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C1A2FB4-F3EE-3C5D-AC85-F01612B27F2D
+  UUID: 649C7A17-A459-3403-A370-F668EFC66D5B
   Functions: 4037
   Symbols:   14722
   CStrings:  15090

```

#### VoiceDial

>  `/System/Library/VoiceServices/PlugIns/VoiceDial.vsplugin/VoiceDial`

```diff

-2869.300.81.2.3
+2869.300.81.2.4
   __TEXT.__text: 0xa8e4
   __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_methlist: 0x760

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1262681F-27C0-3D38-9632-0C64244F4B53
+  UUID: E4D42F09-430E-3B7E-B124-C354AEF6F082
   Functions: 195
   Symbols:   972
   CStrings:  583

```


</details>

## EOF
