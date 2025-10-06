## replayd

> `/usr/libexec/replayd`

```diff

-680.3.1.0.0
-  __TEXT.__text: 0x61b80
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x8780
-  __TEXT.__objc_methlist: 0x448c
+680.5.1.0.0
+  __TEXT.__text: 0x64f5c
+  __TEXT.__auth_stubs: 0x1120
+  __TEXT.__objc_stubs: 0x8ce0
+  __TEXT.__objc_methlist: 0x4644
   __TEXT.__const: 0x1b4
-  __TEXT.__objc_methname: 0xcab4
-  __TEXT.__cstring: 0xc9d5
-  __TEXT.__oslogstring: 0x963e
-  __TEXT.__objc_classname: 0x69b
-  __TEXT.__objc_methtype: 0x22c1
-  __TEXT.__gcc_except_tab: 0x7c8
-  __TEXT.__unwind_info: 0x12e8
-  __DATA_CONST.__auth_got: 0x860
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0x1928
-  __DATA_CONST.__cfstring: 0x3aa0
-  __DATA_CONST.__objc_classlist: 0x170
+  __TEXT.__oslogstring: 0x9ef9
+  __TEXT.__cstring: 0xd054
+  __TEXT.__objc_methname: 0xd0b8
+  __TEXT.__objc_classname: 0x6d3
+  __TEXT.__objc_methtype: 0x23c3
+  __TEXT.__gcc_except_tab: 0x848
+  __TEXT.__unwind_info: 0x1350
+  __DATA_CONST.__auth_got: 0x8a0
+  __DATA_CONST.__got: 0x7d8
+  __DATA_CONST.__const: 0x1978
+  __DATA_CONST.__cfstring: 0x3c80
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x9650
-  __DATA.__objc_selrefs: 0x2ae0
-  __DATA.__objc_ivar: 0x5bc
-  __DATA.__objc_data: 0xe60
-  __DATA.__data: 0xa98
+  __DATA.__objc_const: 0x9ab0
+  __DATA.__objc_selrefs: 0x2cc8
+  __DATA.__objc_ivar: 0x5c4
+  __DATA.__objc_data: 0xeb0
+  __DATA.__data: 0xaf8
   __DATA.__bss: 0x1d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox

   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
+  - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting
   - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85F219E0-8134-3FCA-AE6D-0848E322E08F
-  Functions: 1980
-  Symbols:   517
-  CStrings:  4542
+  UUID: EC491D20-B680-34DE-98EA-6BD69F50B561
+  Functions: 2023
+  Symbols:   540
+  CStrings:  4705
 
Symbols:
+ _APP_SANDBOX_READ_WRITE
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _CFPreferencesAppSynchronize
+ _CFPreferencesSetAppValue
+ _CFPreferencesSynchronize
+ _CFStringGetTypeID
+ _NSURLLocalizedNameKey
+ _OBJC_CLASS_$_PSListController
+ _OBJC_CLASS_$_PSSpecifier
+ _OBJC_CLASS_$_UIDocumentPickerViewController
+ _OBJC_CLASS_$_UISwitch
+ _OBJC_CLASS_$_UITableViewCell
+ _OBJC_METACLASS_$_PSListController
+ _PSFooterTextGroupKey
+ _PSIDKey
+ _SANDBOX_EXTENSION_DEFAULT
+ _UTTypeFolder
+ _kCFBooleanFalse
+ _kCFPreferencesAnyUser
+ _kCFPreferencesCurrentHost
+ _sandbox_extension_issue_file
CStrings:
+ " [ERROR] %{public}s:%d Failed to consume sandbox extension handle"
+ " [ERROR] %{public}s:%d Failed to create custom save directory: %@"
+ " [ERROR] %{public}s:%d Failed to issue sandbox extension for custom save path: %s"
+ " [ERROR] %{public}s:%d Failed to move recording to custom location: %@"
+ " [ERROR] %{public}s:%d Failed to release sandbox extension handle"
+ " [INFO] %{public}s:%d Added audioOnly specifier"
+ " [INFO] %{public}s:%d Audio only toggle changed: %d"
+ " [INFO] %{public}s:%d Could not show Saved to Custom Location Banner, show screen notification"
+ " [INFO] %{public}s:%d Created Save Location cell - textLabel: %@, detailLabel: %@"
+ " [INFO] %{public}s:%d Created audio only toggle with value: %d"
+ " [INFO] %{public}s:%d Created custom specifiers array with %lu items"
+ " [INFO] %{public}s:%d Created fallback cell for row: %ld"
+ " [INFO] %{public}s:%d Creating cell for row %ld"
+ " [INFO] %{public}s:%d Document picker cancelled"
+ " [INFO] %{public}s:%d Falling back to Downloads save location"
+ " [INFO] %{public}s:%d Found custom save path: %@"
+ " [INFO] %{public}s:%d Getting audio only setting"
+ " [INFO] %{public}s:%d Issued sandbox extension for custom save path: %s"
+ " [INFO] %{public}s:%d No audio only setting found, defaulting to NO"
+ " [INFO] %{public}s:%d No custom save location configured, using default location"
+ " [INFO] %{public}s:%d Presenting document picker"
+ " [INFO] %{public}s:%d Read audio only value: %d"
+ " [INFO] %{public}s:%d Read audio only: %d"
+ " [INFO] %{public}s:%d Received Darwin notification for audio only preference change"
+ " [INFO] %{public}s:%d Removed RPHQLRAudioOnly key from preferences"
+ " [INFO] %{public}s:%d Returning %lu specifiers"
+ " [INFO] %{public}s:%d Row %ld tapped"
+ " [INFO] %{public}s:%d Save Location row tapped, showing document picker"
+ " [INFO] %{public}s:%d Selected folder: %@ at path: %@"
+ " [INFO] %{public}s:%d Set RPHQLRAudioOnly to true"
+ " [INFO] %{public}s:%d Setting audio only to: %d"
+ " [INFO] %{public}s:%d Show Angel Proxy UI for saving to custom location"
+ " [INFO] %{public}s:%d Skipping reload - already handling notification or view not visible"
+ " [INFO] %{public}s:%d Successfully moved recording to custom location: %@"
+ " [INFO] %{public}s:%d Successfully saved HQLR recording to custom location"
+ " [INFO] %{public}s:%d user canceled stop of recording, broadcast, or local capture"
+ " [INFO] %{public}s:%d user stop recording, broadcast, or local capture"
+ "%@ %@"
+ "-[LocalCaptureSettingsController audioOnlyToggleChanged:]"
+ "-[LocalCaptureSettingsController dealloc]"
+ "-[LocalCaptureSettingsController documentPicker:didPickDocumentsAtURLs:]"
+ "-[LocalCaptureSettingsController documentPickerWasCancelled:]"
+ "-[LocalCaptureSettingsController getLocalCaptureAudioOnlyValue]"
+ "-[LocalCaptureSettingsController getSwitchState:]"
+ "-[LocalCaptureSettingsController handleAudioOnlyPreferenceChanged]"
+ "-[LocalCaptureSettingsController numberOfSectionsInTableView:]"
+ "-[LocalCaptureSettingsController setLocalCaptureAudioOnlyValue:]"
+ "-[LocalCaptureSettingsController showDocumentPicker:]"
+ "-[LocalCaptureSettingsController specifiers]"
+ "-[LocalCaptureSettingsController tableView:cellForRowAtIndexPath:]"
+ "-[LocalCaptureSettingsController tableView:didSelectRowAtIndexPath:]"
+ "-[LocalCaptureSettingsController tableView:numberOfRowsInSection:]"
+ "-[LocalCaptureSettingsController viewDidAppear:]"
+ "-[LocalCaptureSettingsController viewDidDisappear:]"
+ "-[LocalCaptureSettingsController viewDidLoad]"
+ "-[LocalCaptureSettingsController viewWillAppear:]"
+ "-[LocalCaptureSettingsController viewWillDisappear:]"
+ "-[RPMovieWriter moveToCustomSaveLocation:handler:]"
+ "-[RPMovieWriter moveToCustomSaveLocation:handler:]_block_invoke"
+ "-[RPMovieWriter showHQLRNotificationForCustomLocation:sessionID:]"
+ "-[RPMovieWriter showHQLRNotificationForCustomLocation:sessionID:]_block_invoke"
+ "@\"PSSpecifier\""
+ "@24@0:8^{__CFString=}16"
+ "Audio Only"
+ "AudioOnlyCell"
+ "CONTROL_CENTER_HQLR_FILES"
+ "DefaultCell"
+ "HQLR_SETTINGS_SAVE_LOCATION"
+ "HQLR_SETTINGS_SAVE_LOCATION_FOOTER"
+ "LOCAL_CAPTURE_GROUP"
+ "LocalCaptureSettingsController"
+ "RPAudioOnlySelection"
+ "RPSaveLocationName"
+ "RPSaveLocationPath"
+ "Save Location"
+ "SaveLocationCell"
+ "T@\"PSSpecifier\",&,N,V_saveLocationSpecifier"
+ "TB,N,V_isHandlingNotification"
+ "UIDocumentPickerDelegate"
+ "URLByAppendingPathComponent:"
+ "URLByDeletingLastPathComponent"
+ "_isHandlingNotification"
+ "_saveLocationSpecifier"
+ "addTarget:action:forControlEvents:"
+ "audioOnlyToggleChanged:"
+ "audio_only"
+ "com.apple.replaykit.audioOnlyPreferenceChanged"
+ "createCustomDirectoryURLFromDestURL:"
+ "deselectRowAtIndexPath:animated:"
+ "detailTextLabel"
+ "displayNameAtPath:"
+ "displayNameForFolderPath:"
+ "documentPicker:didPickDocumentAtURL:"
+ "documentPicker:didPickDocumentsAtURLs:"
+ "documentPickerWasCancelled:"
+ "fileSystemRepresentation"
+ "getCurrentSaveLocationName"
+ "getLocalCaptureAudioOnlyValue"
+ "getPreferenceValue:"
+ "getSwitchState:"
+ "groupSpecifierWithID:"
+ "handleAudioOnlyPreferenceChanged"
+ "initForOpeningContentTypes:asCopy:"
+ "initWithStyle:reuseIdentifier:"
+ "isHandlingNotification"
+ "isOn"
+ "isViewLoaded"
+ "moveToCustomSaveLocation:handler:"
+ "numberOfSectionsInTableView:"
+ "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
+ "presentViewController:animated:completion:"
+ "presentedViewController"
+ "q32@0:8@16q24"
+ "reloadData"
+ "row"
+ "saveLocationSpecifier"
+ "save_location"
+ "setAccessoryType:"
+ "setAccessoryView:"
+ "setIsHandlingNotification:"
+ "setLocalCaptureAudioOnlyValue:"
+ "setModalPresentationStyle:"
+ "setOn:"
+ "setPreferenceValue:forKey:"
+ "setProperty:forKey:"
+ "setSaveLocationSpecifier:"
+ "setSelectionStyle:"
+ "setSpecifiers:"
+ "setSwitchState:value:"
+ "setText:"
+ "showDocumentPicker:"
+ "showHQLRNotificationForCustomLocation:sessionID:"
+ "specifiers"
+ "table"
+ "tableView:cellForRowAtIndexPath:"
+ "tableView:didSelectRowAtIndexPath:"
+ "tableView:numberOfRowsInSection:"
+ "text"
+ "textLabel"
+ "v24@0:8@\"UIDocumentPickerViewController\"16"
+ "v32@0:8@\"UIDocumentPickerViewController\"16@\"NSArray\"24"
+ "v32@0:8@\"UIDocumentPickerViewController\"16@\"NSURL\"24"
+ "v32@0:8@16^{__CFString=}24"
+ "v32@0:8^{__CFString=}16@24"
+ "view"
+ "viewDidAppear:"
+ "viewDidDisappear:"
+ "viewDidLoad"
+ "viewWillAppear:"
+ "viewWillDisappear:"
+ "window"
- " [INFO] %{public}s:%d user canceled stop of recording or broadcast"
- " [INFO] %{public}s:%d user stop recording or broadcast"
- "RPHQLR"

```
