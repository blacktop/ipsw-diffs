## ndoagent

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent`

```diff

-407.25.0.0.0
-  __TEXT.__text: 0x11e34
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x25c0
-  __TEXT.__objc_methlist: 0xa58
-  __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x146b
-  __TEXT.__oslogstring: 0x1e53
-  __TEXT.__objc_classname: 0x233
-  __TEXT.__objc_methname: 0x26cb
-  __TEXT.__objc_methtype: 0x7a5
-  __TEXT.__gcc_except_tab: 0x400
-  __TEXT.__ustring: 0x30
-  __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x440
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x980
-  __DATA_CONST.__cfstring: 0xc20
-  __DATA_CONST.__objc_classlist: 0xa0
+407.106.0.0.0
+  __TEXT.__text: 0x10a04
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_stubs: 0x2200
+  __TEXT.__objc_methlist: 0xa18
+  __TEXT.__const: 0x28
+  __TEXT.__cstring: 0x1381
+  __TEXT.__oslogstring: 0x1df0
+  __TEXT.__objc_classname: 0x204
+  __TEXT.__objc_methname: 0x2505
+  __TEXT.__objc_methtype: 0x7d5
+  __TEXT.__gcc_except_tab: 0x324
+  __TEXT.__unwind_info: 0x3fc
+  __DATA_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x8a8
+  __DATA_CONST.__cfstring: 0x960
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x1c0
-  __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_classrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x4708
-  __DATA.__objc_selrefs: 0xa70
-  __DATA.__objc_ivar: 0x74
-  __DATA.__objc_data: 0x640
+  __DATA.__objc_const: 0x4668
+  __DATA.__objc_selrefs: 0x980
+  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x240
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 337
-  Symbols:   171
-  CStrings:  846
+  Functions: 322
+  Symbols:   155
+  CStrings:  785
 
Symbols:
+ _OBJC_CLASS_$_NDOAppleSupportManager
+ _OBJC_CLASS_$_NDOFollowUpDismissalTracker
- _OBJC_CLASS_$_AMSBag
- _OBJC_CLASS_$_AMSMediaTask
- _OBJC_CLASS_$_ASDPurchaseHistory
- _OBJC_CLASS_$_ASDPurchaseHistoryQuery
- _OBJC_CLASS_$_LSApplicationProxy
- __sl_dlopen
- _abort_report_np
- _dispatch_group_wait
- _free
- _kAppAvailabilityType
- _kAppAvailablityText
- _kAppBundleID
- _kAppIconURL
- _kAppLinkURL
- _kAppTitle
- _kAppVendorName
- _objc_getClass
- _objc_retainAutorelease
CStrings:
+ "%{private}s"
+ "-[NDOAgent clearAllUserInitiatedFollowUpDismissalsWithCompletion:]"
+ "-[NDOAgent clearUserInitiatedFollowUpDismissalForSerialNumber:completion:]"
+ "-[NDOAgent storeUserInitiatedFollowUpDismissalForSerialNumber:completion:]"
+ "XPC activity delay is negative. Scheduling with zero delay (%@)"
+ "clearAllUserInitiatedFollowUpDismissalsWithCompletion:"
+ "clearUserInitiatedFollowUpDismissalForSerialNumber:completion:"
+ "com.apple.NewDeviceOutreach/.ndoagent.policyqueue"
+ "eraseAllFollowUpDismissals"
+ "eraseFollowUpDismissalForDeviceSerial:"
+ "scheduleActivityWithDelegate:forDate:"
+ "storeFollowUpDismissalWithDeviceSerial:"
+ "storeUserInitiatedFollowUpDismissalForSerialNumber:completion:"
+ "v24@0:8@?<v@?>16"
+ "v32@0:8@\"NSString\"16@?<v@?>24"
+ "v32@0:8@16@24"
- "/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework"
- "1"
- "== Apple =="
- "== Apple Support =="
- "?pt=2003&ct=coverage.settings&mt=8"
- "AppStore --> appSupportAvailability %@."
- "AppSupportAvailability"
- "Apple"
- "Apple Support"
- "DOWNLOAD"
- "INSTALLED"
- "Localizable"
- "Lookup for %@ in the App Store failed with error %@"
- "NDOAppleSupportManager"
- "NDOClientConfiguration"
- "OVERRIDE"
- "Q"
- "TQ,V_generalAboutPolicy"
- "UIImage"
- "UIScreen"
- "Unable to find class %s"
- "_applicationIconImageForBundleIdentifier:format:scale:"
- "_generalAboutPolicy"
- "_imageAppropriateForDevice:"
- "absoluteString"
- "addFinishBlock:"
- "alwaysRefreshGeneralAbout"
- "ams_DSID"
- "appState"
- "appSupportAvailability %@ %@ is installed."
- "appSupportAvailability %@ is purchased."
- "applicationProxyForIdentifier:"
- "arrayWithObjects:count:"
- "artistName"
- "artwork"
- "attributes"
- "bagForProfile:profileVersion:"
- "bagSubProfile"
- "bagSubProfileVersion"
- "bundleID"
- "bundleWithPath:"
- "checkAppIsPurchased:"
- "com.apple.newdeviceoutreach.ndoagent.policyqueue"
- "com.apple.preferences.applesupport"
- "developerName"
- "executeQuery:withResultHandler:"
- "firstObject"
- "generalAboutPolicy"
- "initWithConfigDictionary:"
- "initWithType:clientIdentifier:clientVersion:bag:"
- "integerValue"
- "ios"
- "isInstalled"
- "length"
- "localizedName"
- "localizedStringForKey:value:table:"
- "mainScreen"
- "name"
- "newSchedulerWithActivityDelegate:forDate:"
- "perform"
- "platformAttributes"
- "productURL"
- "responseDataItems"
- "scale"
- "setAccountID:"
- "setBundleIDs:"
- "setBundleIdentifiers:"
- "setGeneralAboutPolicy:"
- "softlink:r:path:/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore"
- "title"
- "url"
- "v24@0:8Q16"
- "v24@?0@\"AMSMediaResult\"8@\"NSError\"16"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "vendorName"

```
