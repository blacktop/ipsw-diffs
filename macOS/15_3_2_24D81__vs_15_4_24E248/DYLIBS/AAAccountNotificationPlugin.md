## AAAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AAAccountNotificationPlugin.bundle/Contents/MacOS/AAAccountNotificationPlugin`

```diff

-1007.230.0.0.0
-  __TEXT.__text: 0x8984
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__objc_methlist: 0x348
+1007.460.0.0.0
+  __TEXT.__text: 0x8754
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__objc_methlist: 0x474
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x5e2
-  __TEXT.__oslogstring: 0x1457
+  __TEXT.__cstring: 0x664
+  __TEXT.__oslogstring: 0x133a
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__objc_classname: 0xd2
-  __TEXT.__objc_methname: 0x15b0
+  __TEXT.__objc_methname: 0x154c
   __TEXT.__objc_methtype: 0x34e
-  __TEXT.__objc_stubs: 0x13e0
-  __DATA_CONST.__got: 0x268
+  __TEXT.__objc_stubs: 0x1340
+  __DATA_CONST.__got: 0x220
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a8
+  __DATA_CONST.__objc_selrefs: 0x648
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x140
+  __AUTH_CONST.__auth_got: 0x130
   __AUTH_CONST.__const: 0x330
   __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x9a8
+  __AUTH_CONST.__objc_const: 0x730
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0xc0
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 551097B3-A486-3C59-BC71-05D4D48DE969
-  Functions: 137
-  Symbols:   146
-  CStrings:  451
+  UUID: AC920CD8-9693-3689-ABCA-ECE1AB6A5821
+  Functions: 135
+  Symbols:   135
+  CStrings:  444
 
Symbols:
+ _OBJC_CLASS_$_AKAccountManager
- _AAPrefsDomain
- _AAPrefsInformationCacheDomain
- _CFPreferencesCopyAppValue
- _CFPreferencesSetAppValue
- _OBJC_CLASS_$_AAPreferences
- _OBJC_CLASS_$_NSFileManager
- _kAAAccountFullName
- _kAAAccountIsSignedInKey
- _kAAAccountUsername
- _kAAProfilePictureCacheURL
- _kCFBooleanFalse
- _kCFBooleanTrue
CStrings:
+ "AAAccountNotificationPlugin - Only one proto account allowed. Rejecting save."
+ "_childConnectRemovalQueue"
+ "_protoAccountRemovalQueue"
+ "clearNonSecureAAPrefsDomain"
+ "com.apple.AAAccountNotificationPlugin.ProtoAccountRemoval"
+ "com.apple.AppleAccount.AAAccountNotificationFollowUp.RemoveChildConnect"
+ "primaryAccountSignInState"
+ "protoAccount"
+ "protoAccountType"
+ "resetAccountInfoToSignedOutState"
+ "sharedInstance"
+ "updateAccountInformationCacheForAppleAccount:"
- "Clear Apple Account Information Properties in AAPrefsDomain."
- "Clear Apple Account Information Properties in CFPreferences"
- "Not setting AppleAccountInformationCache values"
- "Profile picture cache could not be deleted. Error: %@"
- "Profile picture cache deleted successfully."
- "Profile picture cache does not exist."
- "Set Apple Account Information Properties in CFPreferences"
- "_clearAppleAccountInformationProperties:"
- "_clearAppleAccountInformationPropertiesFromAAPrefsDomain"
- "_deleteProfilePictureCache"
- "_getProfilePictureCacheURL"
- "_setAppleAccountInformationProperties:"
- "aa_fullName"
- "defaultManager"
- "fileExistsAtPath:"
- "isAppleAccountInformationCacheEnabled"
- "isSignedIn"
- "localizedDescription"
- "removeItemAtPath:error:"

```
