## HIDRMUI

> `/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`

```diff

-71.80.2.0.0
-  __TEXT.__text: 0x7310
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x88c
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x494
-  __TEXT.__cstring: 0x5c0
-  __TEXT.__ustring: 0x110
-  __TEXT.__oslogstring: 0x75e
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__objc_classname: 0xd1
-  __TEXT.__objc_methname: 0x184e
-  __TEXT.__objc_methtype: 0x24d
-  __TEXT.__objc_stubs: 0x1400
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x270
+85.0.0.0.0
+  __TEXT.__text: 0x82c0
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_methlist: 0x8ec
+  __TEXT.__const: 0x98
+  __TEXT.__gcc_except_tab: 0x480
+  __TEXT.__cstring: 0x901
+  __TEXT.__ustring: 0x1bc
+  __TEXT.__oslogstring: 0x848
+  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__objc_classname: 0xd2
+  __TEXT.__objc_methname: 0x1ad2
+  __TEXT.__objc_methtype: 0x276
+  __TEXT.__objc_stubs: 0x1660
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x2e0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x6f0
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x258
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0xe38
+  __AUTH_CONST.__auth_got: 0x260
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x860
+  __AUTH_CONST.__objc_const: 0xe98
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xb8
+  __DATA.__objc_ivar: 0xc0
   __DATA.__data: 0x120
-  __DATA.__bss: 0x68
+  __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 903C2950-89ED-3374-9C62-0A0462B821A3
-  Functions: 228
-  Symbols:   914
-  CStrings:  470
+  UUID: CD40379D-FE26-3858-96CA-07BFF486C0BE
+  Functions: 247
+  Symbols:   989
+  CStrings:  561
 
Symbols:
+ +[HIDRMUIUserAuthorizationManager launchTTRForNotificationType:andDeviceName:]
+ +[HIDRMUIUserAuthorizationManager shouldShowInternalUI]
+ +[HIDRMUIUserAuthorizationManager shouldShowInternalUI].cold.1
+ +[HIDRMUIUserAuthorizationRequest requestWithDeviceName:requiresPairing:requestedFromSettings:]
+ -[AuthRequestWrapper characterLockoutExpirationTimestamp]
+ -[AuthRequestWrapper setCharacterLockoutExpirationTimestamp:]
+ -[HIDRMUIUserAuthorizationRequest initWithDeviceName:requiresPairing:requestedFromSettings:]
+ -[HIDRMUIUserAuthorizationRequest requestedFromSettings]
+ -[HIDRMUIUserAuthorizationRequest setRequestedFromSettings:]
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table21
+ GCC_except_table32
+ GCC_except_table59
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_IVAR_$_AuthRequestWrapper._characterLockoutExpirationTimestamp
+ _OBJC_IVAR_$_HIDRMUIUserAuthorizationRequest._requestedFromSettings
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___55+[HIDRMUIUserAuthorizationManager shouldShowInternalUI]_block_invoke
+ ___70+[HIDRMUIUserAuthorizationManager userNotificationForType:deviceName:]_block_invoke.67
+ ___70+[HIDRMUIUserAuthorizationManager userNotificationForType:deviceName:]_block_invoke.67.cold.1
+ ___70+[HIDRMUIUserAuthorizationManager userNotificationForType:deviceName:]_block_invoke.67.cold.2
+ ___74-[HIDRMUIUserAuthorizationManager addUserAuthorizationRequest:completion:]_block_invoke.156
+ ___74-[HIDRMUIUserAuthorizationManager addUserAuthorizationRequest:completion:]_block_invoke_2
+ ___78+[HIDRMUIUserAuthorizationManager launchTTRForNotificationType:andDeviceName:]_block_invoke
+ ___78+[HIDRMUIUserAuthorizationManager launchTTRForNotificationType:andDeviceName:]_block_invoke.cold.1
+ ___block_descriptor_32_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_56_e8_32s_e40_v24?0"IOUserNotification"8"NSError"16ls32l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e40_v24?0"IOUserNotification"8"NSError"16lw56l8s32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
+ ___block_literal_global.150
+ _objc_msgSend$URL
+ _objc_msgSend$addButtonWithTitle:andIdentifier:
+ _objc_msgSend$characterLockoutExpirationTimestamp
+ _objc_msgSend$date
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$hasSelectedButtonWithIdentifier:
+ _objc_msgSend$initWithDeviceName:requiresPairing:requestedFromSettings:
+ _objc_msgSend$launchTTRForNotificationType:andDeviceName:
+ _objc_msgSend$openURL:configuration:completionHandler:
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$requestWithDeviceName:requiresPairing:requestedFromSettings:
+ _objc_msgSend$requestedFromSettings
+ _objc_msgSend$setCharacterLockoutExpirationTimestamp:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setHost:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setScheme:
+ _objc_msgSend$shouldShowInternalUI
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_retainAutoreleasedReturnValue
+ _objc_retainBlock
+ _objc_retain_x23
+ _objc_retain_x26
+ _objc_retain_x27
+ _os_variant_has_internal_ui
+ _shouldShowInternalUI.onceToken
+ _shouldShowInternalUI.showInternalUI
- -[HIDRMUIUserAuthorizationManager handleInputCharacter:forUserAuthorizationRequest:error:].cold.3
- GCC_except_table11
- GCC_except_table15
- GCC_except_table26
- GCC_except_table47
- GCC_except_table8
- ___74-[HIDRMUIUserAuthorizationManager addUserAuthorizationRequest:completion:]_block_invoke.67
- ___block_descriptor_40_e40_v24?0"IOUserNotification"8"NSError"16l
- ___block_descriptor_64_e8_32s40s48bs56r_e40_v24?0"IOUserNotification"8"NSError"16ls32l8s40l8r56l8s48l8
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$firstObject
- _objc_msgSend$lastObject
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "\n\n[INTERNAL ONLY]\nNavigate to Settings -> Privacy & Security -> Wired Accessories to allow this accessory."
+ "1"
+ "1684648"
+ "2129480"
+ "@\"NSDate\""
+ "@32@0:8@16B24B28"
+ "Allow"
+ "Allow Accessory in Settings"
+ "Allow “%@” to control your Device?"
+ "AppleHIDRM"
+ "BundleID"
+ "Can’t Enter Code"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Description"
+ "Don’t Allow"
+ "Enter this code on the keyboard to allow it to control your Device."
+ "Error launching radar! (error: %@)"
+ "Error launching settings pane! (error: %@)"
+ "Error presenting user notification! (error: %@"
+ "File Radar"
+ "Guidance"
+ "HID Restricted Mode (HIDRM) Issue Report\nFiled via Tap-to-Radar Button\n\nISSUE DESCRIPTION:\nWhat happened?\n\nEXPECTED BEHAVIOR:\nWhat did you expect to happen?\n\nACTUAL BEHAVIOR:\nWhat actually happened instead?\n\nSTEPS TO REPRODUCE:\n1. \n2. \n3. \n\nADDITIONAL DETAILS:\nAny other relevant information...\n\n\n\n[AUTO-GENERATED HIDRM CONTEXT - DO NOT MODIFY BELOW]\n\n*** HIDRM User Notification Info ***\nnotificationType: %ld [%@]\ndeviceName: %@\n\nTimestamp: %@\n\n\n"
+ "Handling input character 0x%02x... (authorizationRequest: %@)"
+ "If you didn’t connect this accessory, someone may be using it to try to access your data or harm your Device."
+ "IncludeDevicePrefixInTitle"
+ "Input character lockout expired, clearing expiration timestamp..."
+ "Invalid character! (character: 0x%02x)"
+ "Keywords"
+ "Launching TTR... (radarURL: %@)"
+ "Not in pairing flow, ignoring input character! (character: 0x%02x)"
+ "Pairing"
+ "Pairing Failure"
+ "Skip Pairing"
+ "Starting character input lockout for %lums..."
+ "T@\"NSDate\",&,N,V_characterLockoutExpirationTimestamp"
+ "TB,N,V_requestedFromSettings"
+ "TimeOfIssue"
+ "Title"
+ "URL"
+ "Undefined"
+ "You can allow this accessory to control your Device in Settings.\n\nSome accessories may appear as another type of device to try to access your data or harm your Device. Only allow accessories you recognize."
+ "[TTR] [HIDRM] "
+ "_characterLockoutExpirationTimestamp"
+ "_requestedFromSettings"
+ "all"
+ "allow"
+ "characterLockoutExpirationTimestamp"
+ "date"
+ "dateWithTimeIntervalSinceNow:"
+ "don't-allow"
+ "file-radar"
+ "initWithDeviceName:requiresPairing:requestedFromSettings:"
+ "launchTTRForNotificationType:andDeviceName:"
+ "new"
+ "not-a-keyboard"
+ "openURL:configuration:completionHandler:"
+ "queryItemWithName:value:"
+ "requestWithDeviceName:requiresPairing:requestedFromSettings:"
+ "requestedFromSettings"
+ "setCharacterLockoutExpirationTimestamp:"
+ "setDateFormat:"
+ "setHost:"
+ "setQueryItems:"
+ "setRequestedFromSettings:"
+ "setScheme:"
+ "settings"
+ "settings-navigation://com.apple.Settings.PrivacyAndSecurity/InputAccessories"
+ "shouldShowInternalUI"
+ "stringByAppendingString:"
+ "stringFromDate:"
+ "tap-to-radar"
+ "timeIntervalSinceNow"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v32@0:8q16@24"
+ "yyyy-MM-dd HH:mm:ss"
+ "yyyy.MM.dd_HH-mm-ss"
+ "“%@” Blocked"
- "Allow Control"
- "Cancel"
- "Don't Allow"
- "Error opening settings pane! (error: %@)"
- "Handling input character '%C'... (authorizationRequest: %@)"
- "If you did not plug in a keyboard, this accessory may be attempting to compromise your privacy or harm your device."
- "If you did not plug in an input device, this accessory may be attempting to compromise your privacy or harm your device."
- "Invalid character! (character: '%C')"
- "Not a Keyboard"
- "Not in pairing flow, ignoring input character! (character: '%C')"
- "This accessory has been blocked from controlling your device."
- "This accessory must be approved in Settings before it can control your device."
- "firstObject"
- "lastObject"
- "settings-navigation://com.apple.Settings.PrivacyAndSecurity"
- "“%@” is attempting to control your device. Enter the following keys on this accessory to approve it."

```
