## NewDeviceOutreach

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach`

```diff

-407.25.0.0.0
-  __TEXT.__text: 0x14eac
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x12b0
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x1be0
-  __TEXT.__oslogstring: 0x14f2
-  __TEXT.__gcc_except_tab: 0x410
-  __TEXT.__unwind_info: 0x468
-  __TEXT.__objc_classname: 0x157
-  __TEXT.__objc_methname: 0x4d69
-  __TEXT.__objc_methtype: 0x790
-  __TEXT.__objc_stubs: 0x32a0
+407.106.0.0.0
+  __TEXT.__text: 0x17114
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x1398
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x1e84
+  __TEXT.__oslogstring: 0x1670
+  __TEXT.__gcc_except_tab: 0x4ec
+  __TEXT.__ustring: 0x30
+  __TEXT.__dlopen_cstrs: 0x50
+  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__objc_classname: 0x1b9
+  __TEXT.__objc_methname: 0x51a5
+  __TEXT.__objc_methtype: 0x7bf
+  __TEXT.__objc_stubs: 0x36a0
   __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x738
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__const: 0x7e8
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2f28
-  __DATA_CONST.__objc_selrefs: 0x1020
+  __DATA_CONST.__objc_const: 0x30c8
+  __DATA_CONST.__objc_selrefs: 0x1168
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x188
+  __DATA_CONST.__objc_classrefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x1e60
-  __AUTH_CONST.__objc_const: 0x548
+  __AUTH_CONST.__cfstring: 0x2060
+  __AUTH_CONST.__objc_const: 0x668
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x2c0
-  __AUTH.__objc_data: 0x1e0
+  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x1d4
   __DATA.__data: 0x2a0
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F77B4DCE-AE56-3E7C-A70F-552CF3536F66
-  Functions: 556
-  Symbols:   2030
-  CStrings:  1567
+  UUID: CB4E7AA5-01FE-317E-8A3C-2CF5AAE8F12A
+  Functions: 591
+  Symbols:   2171
+  CStrings:  1667
 
Symbols:
+ +[NDOFollowUpDismissalTracker _dismissedSerialNumberHashes]
+ +[NDOFollowUpDismissalTracker eraseAllFollowUpDismissals]
+ +[NDOFollowUpDismissalTracker eraseFollowUpDismissalForDeviceSerial:]
+ +[NDOFollowUpDismissalTracker followUpIsDismissedForSerial:]
+ +[NDOFollowUpDismissalTracker storeFollowUpDismissalWithDeviceSerial:]
+ +[NDOFollowUpDismissalTracker uniqueIdentfierForSerialNumber:]
+ +[NDOTypeChecking isNotEmptyString:]
+ +[NDOViewModelGenerationHelpers ctaTextWithDevice:]
+ +[NDOViewModelGenerationHelpers ctaTextWithWarranty:forDate:]
+ -[NDOAppleSupportManager _imageAppropriateForDevice:]
+ -[NDOAppleSupportManager appSupportAvailability:withReply:]
+ -[NDOAppleSupportManager checkAppIsPurchased:]
+ -[NDOAppleSupportManager checkIsAvailableInStore:withReply:]
+ -[NDOManager clearAllUserInitiatedFollowUpDismissalsWithReply:]
+ -[NDOManager clearUserInitiatedFollowUpDismissalForSerialNumber:withReply:]
+ -[NDOManager storeUserInitiatedFollowUpDismissalForSerialNumber:withReply:]
+ -[NSMutableURLRequest(AccountHeaders) addStoreLocaleHeaderIfNeeded]
+ -[NSMutableURLRequest(AccountHeaders) storeLocaleWithAccountStore:]
+ -[NSMutableURLRequest(AccountHeaders) storeLocaleWithAccountStore:].cold.1
+ -[NSMutableURLRequest(AccountHeaders) storeLocaleWithAccountStore:].cold.2
+ -[NSMutableURLRequest(AccountHeaders) storeLocale]
+ GCC_except_table11
+ GCC_except_table3
+ GCC_except_table7
+ _OBJC_CLASS_$_AMSBag
+ _OBJC_CLASS_$_AMSMediaTask
+ _OBJC_CLASS_$_ASDPurchaseHistory
+ _OBJC_CLASS_$_ASDPurchaseHistoryQuery
+ _OBJC_CLASS_$_LSApplicationProxy
+ _OBJC_CLASS_$_NDOAppleSupportManager
+ _OBJC_CLASS_$_NDOFollowUpDismissalTracker
+ _OBJC_CLASS_$_NDOTypeChecking
+ _OBJC_CLASS_$_NDOViewModelGenerationHelpers
+ _OBJC_METACLASS_$_NDOAppleSupportManager
+ _OBJC_METACLASS_$_NDOFollowUpDismissalTracker
+ _OBJC_METACLASS_$_NDOTypeChecking
+ _OBJC_METACLASS_$_NDOViewModelGenerationHelpers
+ _UIKitCoreLibrary
+ _UIKitCoreLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_NDOFollowUpDismissalTracker
+ __OBJC_$_CLASS_METHODS_NDOTypeChecking
+ __OBJC_$_CLASS_METHODS_NDOViewModelGenerationHelpers
+ __OBJC_$_INSTANCE_METHODS_NDOAppleSupportManager
+ __OBJC_CLASS_RO_$_NDOAppleSupportManager
+ __OBJC_CLASS_RO_$_NDOFollowUpDismissalTracker
+ __OBJC_CLASS_RO_$_NDOTypeChecking
+ __OBJC_CLASS_RO_$_NDOViewModelGenerationHelpers
+ __OBJC_METACLASS_RO_$_NDOAppleSupportManager
+ __OBJC_METACLASS_RO_$_NDOFollowUpDismissalTracker
+ __OBJC_METACLASS_RO_$_NDOTypeChecking
+ __OBJC_METACLASS_RO_$_NDOViewModelGenerationHelpers
+ ___46-[NDOAppleSupportManager checkAppIsPurchased:]_block_invoke
+ ___58-[NDOFollowUp _postFollowUpWithDevicesInfo:repostAllowed:]_block_invoke.59
+ ___59-[NDOAppleSupportManager appSupportAvailability:withReply:]_block_invoke
+ ___60-[NDOAppleSupportManager checkIsAvailableInStore:withReply:]_block_invoke
+ ___63-[NDOManager clearAllUserInitiatedFollowUpDismissalsWithReply:]_block_invoke
+ ___63-[NDOManager clearAllUserInitiatedFollowUpDismissalsWithReply:]_block_invoke.cold.1
+ ___75-[NDOManager clearUserInitiatedFollowUpDismissalForSerialNumber:withReply:]_block_invoke
+ ___75-[NDOManager clearUserInitiatedFollowUpDismissalForSerialNumber:withReply:]_block_invoke.cold.1
+ ___75-[NDOManager storeUserInitiatedFollowUpDismissalForSerialNumber:withReply:]_block_invoke
+ ___75-[NDOManager storeUserInitiatedFollowUpDismissalForSerialNumber:withReply:]_block_invoke.cold.1
+ ___97-[NDOFollowUp refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:]_block_invoke.103
+ ___UIKitCoreLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40bs_e36_v24?0"AMSMediaResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e30_v32?0"NDODeviceInfo"8Q16^B24ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e30_v32?0"NDODeviceInfo"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48r56r64r72r_e29_v24?0"NSArray"8"NSError"16ls32l8r48l8r56l8r64l8r72l8s40l8
+ ___getUIImageClass_block_invoke
+ ___getUIImageClass_block_invoke.cold.1
+ ___getUIScreenClass_block_invoke
+ ___getUIScreenClass_block_invoke.cold.1
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringUIKitCore
+ _dispatch_group_wait
+ _free
+ _getUIImageClass.softClass
+ _getUIScreenClass.softClass
+ _objc_getClass
+ _objc_msgSend$_applicationIconImageForBundleIdentifier:format:scale:
+ _objc_msgSend$_dismissedSerialNumberHashes
+ _objc_msgSend$absoluteString
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addFinishBlock:
+ _objc_msgSend$addStoreLocaleHeaderIfNeeded
+ _objc_msgSend$ams_DSID
+ _objc_msgSend$ams_activeiTunesAccount
+ _objc_msgSend$ams_localiTunesAccount
+ _objc_msgSend$appState
+ _objc_msgSend$applicationProxyForIdentifier:
+ _objc_msgSend$bagForProfile:profileVersion:
+ _objc_msgSend$bagSubProfile
+ _objc_msgSend$bagSubProfileVersion
+ _objc_msgSend$bundleID
+ _objc_msgSend$checkAppIsPurchased:
+ _objc_msgSend$clearAllUserInitiatedFollowUpDismissalsWithCompletion:
+ _objc_msgSend$clearUserInitiatedFollowUpDismissalForSerialNumber:completion:
+ _objc_msgSend$developerName
+ _objc_msgSend$executeQuery:withResultHandler:
+ _objc_msgSend$followUpIsDismissedForSerial:
+ _objc_msgSend$initWithType:clientIdentifier:clientVersion:bag:
+ _objc_msgSend$intValue
+ _objc_msgSend$isInstalled
+ _objc_msgSend$isNotEmptyString:
+ _objc_msgSend$localizedName
+ _objc_msgSend$mainScreen
+ _objc_msgSend$perform
+ _objc_msgSend$productURL
+ _objc_msgSend$responseDataItems
+ _objc_msgSend$scale
+ _objc_msgSend$setAccountID:
+ _objc_msgSend$setBundleIDs:
+ _objc_msgSend$setBundleIdentifiers:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$storeLocale
+ _objc_msgSend$storeLocaleWithAccountStore:
+ _objc_msgSend$storeUserInitiatedFollowUpDismissalForSerialNumber:completion:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$title
+ _objc_msgSend$vendorName
- -[NSMutableURLRequest(AccountHeaders) addStoreLocaleHeaderIfNeededForAccount:]
- -[NSMutableURLRequest(AccountHeaders) ndo_addOASHeadersWithOfferID:serialNumber:primarySerialNumber:].cold.1
- -[NSMutableURLRequest(AccountHeaders) storeLocaleForAccount:]
- -[NSMutableURLRequest(AccountHeaders) storeLocaleForAccount:].cold.1
- GCC_except_table10
- _OBJC_CLASS_$_AMSAuthenticateOptions
- _OBJC_CLASS_$_AMSAuthenticateTask
- ___58-[NDOFollowUp _postFollowUpWithDevicesInfo:repostAllowed:]_block_invoke.62
- ___97-[NDOFollowUp refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:]_block_invoke.106
- ___block_descriptor_57_e8_32s40s48s_e30_v32?0"NDODeviceInfo"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s56s64s_e30_v32?0"NDODeviceInfo"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
- _objc_msgSend$account
- _objc_msgSend$addStoreLocaleHeaderIfNeededForAccount:
- _objc_msgSend$ams_iTunesAccountForAccount:
- _objc_msgSend$initWithAccount:options:
- _objc_msgSend$performAuthentication
- _objc_msgSend$resultWithError:
- _objc_msgSend$setAuthenticationType:
- _objc_msgSend$setDebugReason:
- _objc_msgSend$storeLocaleForAccount:
CStrings:
+ "%{private}s"
+ "%{public}s - Erasing all follow up dismissals"
+ "%{public}s - Erasing follow up dismissal for device"
+ "%{public}s - Storing follow up dismissal by user %{private}@ "
+ "%{public}s - isDismissedByUser: %d"
+ "%{public}s Failed to determine storefront locale"
+ "%{public}s Invalid storefront locale"
+ "%{public}s No active itunes account. Falling back to local account"
+ "+[NDOFollowUpDismissalTracker eraseAllFollowUpDismissals]"
+ "+[NDOFollowUpDismissalTracker eraseFollowUpDismissalForDeviceSerial:]"
+ "+[NDOFollowUpDismissalTracker followUpIsDismissedForSerial:]"
+ "+[NDOFollowUpDismissalTracker storeFollowUpDismissalWithDeviceSerial:]"
+ "-[NDOManager storeUserInitiatedFollowUpDismissalForSerialNumber:withReply:]"
+ "-[NSMutableURLRequest(AccountHeaders) storeLocaleWithAccountStore:]"
+ "== Apple =="
+ "== Apple Support =="
+ "?pt=2003&ct=coverage.settings&mt=8"
+ "AppStore --> appSupportAvailability %@."
+ "AppSupportAvailability"
+ "Apple"
+ "Apple Support"
+ "Checking for %@ in the App Store"
+ "DOWNLOAD"
+ "F"
+ "INSTALLED"
+ "Lookup for %@ in the App Store failed with error %@"
+ "NDOAppleSupportManager"
+ "NDOFollowUpDismissalTracker"
+ "NDOTypeChecking"
+ "NDOViewModelGenerationHelpers"
+ "OVERRIDE"
+ "UIImage"
+ "UIScreen"
+ "Unable to find class %s"
+ "_applicationIconImageForBundleIdentifier:format:scale:"
+ "_dismissedSerialNumberHashes"
+ "_imageAppropriateForDevice:"
+ "absoluteString"
+ "addEntriesFromDictionary:"
+ "addFinishBlock:"
+ "addStoreLocaleHeaderIfNeeded"
+ "ams_DSID"
+ "ams_activeiTunesAccount"
+ "ams_localiTunesAccount"
+ "appState"
+ "appSupportAvailability %@ %@ is installed."
+ "appSupportAvailability %@ is purchased."
+ "applicationProxyForIdentifier:"
+ "artistName"
+ "artwork"
+ "attributes"
+ "bagForProfile:profileVersion:"
+ "bagSubProfile"
+ "bagSubProfileVersion"
+ "bundleID"
+ "checkAppIsPurchased:"
+ "clearAllUserInitiatedFollowUpDismissalsWithCompletion:"
+ "clearAllUserInitiatedFollowUpDismissalsWithReply:"
+ "clearUserInitiatedFollowUpDismissalForSerialNumber:completion:"
+ "clearUserInitiatedFollowUpDismissalForSerialNumber:withReply:"
+ "com.apple.preferences.applesupport"
+ "ctaTextWithDevice:"
+ "ctaTextWithWarranty:forDate:"
+ "developerName"
+ "eraseAllFollowUpDismissals"
+ "eraseFollowUpDismissalForDeviceSerial:"
+ "executeQuery:withResultHandler:"
+ "followUpIsDismissedForSerial:"
+ "initWithType:clientIdentifier:clientVersion:bag:"
+ "intValue"
+ "ios"
+ "isInstalled"
+ "isNotEmptyString:"
+ "localizedName"
+ "mainScreen"
+ "perform"
+ "platformAttributes"
+ "productURL"
+ "responseDataItems"
+ "scale"
+ "setAccountID:"
+ "setBundleIDs:"
+ "setBundleIdentifiers:"
+ "sharedInstance"
+ "softlink:r:path:/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore"
+ "storeFollowUpDismissalWithDeviceSerial:"
+ "storeLocale"
+ "storeLocaleWithAccountStore:"
+ "storeUserInitiatedFollowUpDismissalForSerialNumber:completion:"
+ "storeUserInitiatedFollowUpDismissalForSerialNumber:withReply:"
+ "timeIntervalSinceDate:"
+ "title"
+ "url"
+ "v24@0:8@?<v@?>16"
+ "v24@?0@\"AMSMediaResult\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?>24"
+ "vendorName"
- "%{public}s: Device eligible for re-post. Re-post the followup for %{private}@"
- "Couldn't find an iTunesAccount"
- "Couldn't find an iTunesAccount with error: %@"
- "Primary iCloud Account is nil!"
- "Retrying with silent authentication to get the itunes store account."
- "account"
- "addStoreLocaleHeaderIfNeededForAccount:"
- "ams_iTunesAccountForAccount:"
- "initWithAccount:options:"
- "performAuthentication"
- "resultWithError:"
- "setAuthenticationType:"
- "setDebugReason:"
- "storeLocaleForAccount:"

```
