## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

-822.0.8.0.0
-  __TEXT.__text: 0x5d090
-  __TEXT.__auth_stubs: 0x13a0
-  __TEXT.__objc_stubs: 0x8780
-  __TEXT.__objc_methlist: 0x3f2c
-  __TEXT.__cstring: 0xb147
-  __TEXT.__const: 0x670
-  __TEXT.__gcc_except_tab: 0x194c
-  __TEXT.__objc_methname: 0xe2a2
-  __TEXT.__oslogstring: 0xa688
-  __TEXT.__objc_classname: 0x596
-  __TEXT.__objc_methtype: 0x1c01
+849.0.0.0.0
+  __TEXT.__text: 0x5fa40
+  __TEXT.__auth_stubs: 0x14c0
+  __TEXT.__objc_stubs: 0x8aa0
+  __TEXT.__objc_methlist: 0x4054
+  __TEXT.__cstring: 0xb845
+  __TEXT.__const: 0x6c8
+  __TEXT.__gcc_except_tab: 0x1974
+  __TEXT.__objc_methname: 0xe64d
+  __TEXT.__oslogstring: 0xabf1
+  __TEXT.__objc_classname: 0x5ab
+  __TEXT.__objc_methtype: 0x1c60
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x11f0
-  __DATA_CONST.__auth_got: 0x9e0
-  __DATA_CONST.__got: 0x3a8
+  __TEXT.__unwind_info: 0x1270
+  __DATA_CONST.__auth_got: 0xa70
+  __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x1ce8
-  __DATA_CONST.__cfstring: 0x61c0
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__const: 0x1d70
+  __DATA_CONST.__cfstring: 0x6900
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__objc_intobj: 0x498
-  __DATA_CONST.__objc_arraydata: 0xb90
-  __DATA_CONST.__objc_dictobj: 0xbb8
-  __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_const: 0x77a0
-  __DATA.__objc_selrefs: 0x2980
-  __DATA.__objc_ivar: 0x55c
-  __DATA.__objc_data: 0xf50
-  __DATA.__data: 0x608
-  __DATA.__bss: 0x389
+  __DATA_CONST.__objc_superrefs: 0x148
+  __DATA_CONST.__objc_intobj: 0x4b0
+  __DATA_CONST.__objc_arraydata: 0xfe8
+  __DATA_CONST.__objc_dictobj: 0xcd0
+  __DATA_CONST.__objc_arrayobj: 0xa8
+  __DATA.__objc_const: 0x7950
+  __DATA.__objc_selrefs: 0x2a58
+  __DATA.__objc_ivar: 0x574
+  __DATA.__objc_data: 0xfa0
+  __DATA.__data: 0x600
+  __DATA.__bss: 0x3a1
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 906F4055-5D41-343A-B990-314FA8FC2829
-  Functions: 2120
-  Symbols:   444
-  CStrings:  5113
+  UUID: A89A1CA3-48E7-3FD7-8A7B-7BAC54D073FD
+  Functions: 2162
+  Symbols:   466
+  CStrings:  5308
 
Symbols:
+ _CFRetain
+ _CGBitmapContextCreate
+ _CGBitmapContextCreateImage
+ _CGColorSpaceCreateWithName
+ _CGColorSpaceRelease
+ _CGColorSpaceRetain
+ _CGContextClearRect
+ _CGContextDrawImage
+ _CGContextRelease
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithURL
+ _CGImageDestinationFinalize
+ _CGImageGetColorSpace
+ _CGImageGetHeight
+ _CGImageGetWidth
+ _CGImageRelease
+ _MGCopyAnswer
+ _NSLocaleLanguageCode
+ _SBUserNotificationHeaderImagePath
+ _TCCAuthPromptIconString
+ _kCGColorSpaceExtendedSRGB
+ _kUTTypePNG
CStrings:
+ "#tccIcon %@ already exists"
+ "#tccIcon %@ is accessing TCCCopyIconResourcePathForService without %{private}s"
+ "#tccIcon %s: Attempting to write icon to %@"
+ "#tccIcon %s: No icon found for TCC service=%@"
+ "#tccIcon %s: Setting display scale to %lf"
+ "#tccIcon %s: baseImageSize: (%zu, %zu) overlayImageSize: (%zu, %zu) both scale: %f"
+ "#tccIcon %s: icon not found for TCC service=%@"
+ "#tccIcon %s: unable to write icon to URL %@"
+ "#tccIcon CGImageGetColorSpace returned NULL for baseImage. Defaulting to ExtendedSRGB colorspace"
+ "#tccIcon Colorspace is NULL"
+ "#tccIcon Failed to create context"
+ "#tccIcon Failed to create image destination"
+ "#tccIcon Failed to write image to %@"
+ "#tccIcon Image saved to %@"
+ "#tccIcon Language code is %@ isRTLLanguage: %d"
+ "#tccIcon One of cgImageRef is NULL. nullBaseImage: %s; nullOverlayImage: %s"
+ "#tccIcon Service: %@, icon:%@, "
+ "#tccIcon Service: %@, icon:%@, badge icon: %@"
+ "#tccIcon TCCCopyIconResourcePathForService is called with invalid service value(%{public}d)"
+ "#tccIcon TCCCopyIconResourcePathForService: %s(shouldBadge: %d)"
+ "#tccIcon TCCCopyIconResourcePathForService: %s(shouldBadge: %d) service at %@"
+ "#tccIcon overriding cached icon for %@ at %@"
+ "#tccIcon returning cached icon for %@ at %@"
+ "#tccIcon unable to create temporary dir at %@. Error: %@"
+ "%@@%dx.png"
+ "+[TCCDIconGenerator _createCGImageIconWithBadge:forService:withDescriptor:]"
+ "+[TCCDIconGenerator _createCGImageRefByOverlay:ontoImage:]"
+ "@32@0:8^{CGImage=}16@24"
+ "AudioCapture"
+ "BluetoothAlways"
+ "CGImage"
+ "Calendar"
+ "Camera"
+ "ContactlessAccess"
+ "ContactlessAccessPayments"
+ "CredentialSharingService"
+ "D5834418-F4A0-4C74-AA38-8ED5F7765BD1"
+ "DELETE FROM access WHERE service = 'kTCCServiceContactlessAccess' and auth_value = 3"
+ "FaceID"
+ "Failed to issue generic sandbox extension for class: %{public}s"
+ "FinancialData"
+ "FocusStatus"
+ "Home"
+ "Location"
+ "MediaLibrary"
+ "Microphone"
+ "Migrated database does not exist at %s"
+ "MigratedData/com.apple.TCC"
+ "Motion"
+ "Music"
+ "NearbyInteraction"
+ "PKPassLibraryBackgroundAddPasses"
+ "PKPassLibraryBackgroundAddPassesUsageDescription"
+ "Photos"
+ "PhotosAdd"
+ "REQUEST_ACCESS_DONT_ALLOW"
+ "REQUEST_ACCESS_SERVICE_kTCCServiceExternalCameraMedia"
+ "REQUEST_ACCESS_UPGRADE_kTCCServiceExternalCameraMedia"
+ "Reminders"
+ "SensorKitBedSensingWriting"
+ "Solarium"
+ "SpeechRecognition"
+ "Staged prompting request is invalid for %@: currentAuth: %llu desiredAuth: %llu"
+ "SwiftUI"
+ "SystemPolicyAppData"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,V_migratedDBQueue"
+ "TB,N,V_ios_issueBothSandboxExtension"
+ "TB,N,V_migratedDBUnavailable"
+ "TCC Migrated DB is unavailable"
+ "TCC.IconGenerator.OverrideCachedIcons"
+ "TCC.db"
+ "TCCAccessCopyDatabaseInformationForType"
+ "TCCCopyIconResourcePathForService"
+ "TCCDDatabaseMigrated"
+ "T^{sqlite3=},V_migratedDBHandle"
+ "UPDATE access set auth_version = 2 WHERE service = 'kTCCServiceContactlessAccess'"
+ "UserTracking"
+ "Wallet"
+ "WebBrowserPublicKeyCredential"
+ "Willow"
+ "^{CGImage=}32@0:8^{CGImage=}16^{CGImage=}24"
+ "^{CGImage=}40@0:8@16@24@32"
+ "_createCGImageIconWithBadge:forService:withDescriptor:"
+ "_createCGImageRefByOverlay:ontoImage:"
+ "_ios_issueBothSandboxExtension"
+ "_migratedDBHandle"
+ "_migratedDBQueue"
+ "_migratedDBUnavailable"
+ "_writeCGImage:toTempURL:"
+ "badgeWithPrivacyHand"
+ "boolForKey:"
+ "cStringUsingEncoding:"
+ "characterDirectionForLanguage:"
+ "com.apple.graphic-icon.privacy"
+ "com.apple.private.tcc.icons_for_prompts"
+ "com.apple.tcc.migrated_db_queue"
+ "containsString:"
+ "convertAccessUpdateStatustToMainSet:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "createDirectoryIfNeeded:"
+ "currentLocale"
+ "failed to create migrated db queue"
+ "fileURLWithPath:isDirectory:"
+ "floatValue"
+ "generic_extension"
+ "getMigratedDBDir"
+ "getMigratedDBRelativeDirPath"
+ "graphic-icon.app-tracking-transparency"
+ "graphic-icon.bluetooth"
+ "graphic-icon.contactless-and-nfc"
+ "graphic-icon.face-id"
+ "graphic-icon.focus"
+ "graphic-icon.location"
+ "graphic-icon.microphone-access"
+ "graphic-icon.motion-and-fitness"
+ "graphic-icon.nearby-interactions"
+ "graphic-icon.person-passkey"
+ "graphic-icon.research-sensor-and-usage-data"
+ "graphic-icon.screen-recording"
+ "graphic-icon.video-camera"
+ "graphic-icon.wallet"
+ "graphic-icon.waveform"
+ "iconForService"
+ "iconImprovements"
+ "initWithSize:scale:"
+ "ios_issueBothSandboxExtension"
+ "issuing both generic and file extension due to policy"
+ "kTCCServiceContactlessAccessPayments"
+ "kTCCServiceExternalCameraMedia"
+ "kTCCServicePKPassLibraryBackgroundAddPasses"
+ "kTCCServiceSensorKitHearing"
+ "kTCCServiceSensorKitSleep"
+ "main-screen-scale"
+ "migratedDBHandle"
+ "migratedDBQueue"
+ "migratedDBUnavailable"
+ "mobilecal"
+ "mobileslideshow"
+ "opened migrated database: %{public}s"
+ "pathToIconFile"
+ "peerSupportsIndependentAuthforService:"
+ "reminders"
+ "removeItemAtURL:error:"
+ "setDrawBorder:"
+ "setIos_issueBothSandboxExtension:"
+ "setMigratedDBHandle:"
+ "setMigratedDBUnavailable:"
+ "shouldOverrideCachedIcons"
- "%@.png"
- "%s: Attempting to write icon to %@"
- "%s: No icon found for TCC service=%@"
- "%s: unable to write icon to URL %@"
- "/System/Library/Frameworks/ContactsUI.framework/Assets.car"
- "NSFSKitBlockDeviceUsageDescription"
- "PromptHeader"
- "Staged prompting request is invalid: currentAuth: %llu desiredAuth: %llu"
- "dictionaryMessageSyncIDKey"
- "kSYDictionaryObjectSyncIDKey"
- "kTCCServiceFSKitBlockDevice"

```
