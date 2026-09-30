## AAAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AAAccountNotificationPlugin.bundle/AAAccountNotificationPlugin`

```diff

-1007.230.0.0.0
-  __TEXT.__text: 0x95f8
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0x378
+1007.456.0.0.0
+  __TEXT.__text: 0x96d4
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__cstring: 0x8d6
-  __TEXT.__oslogstring: 0x1755
+  __TEXT.__cstring: 0x9a4
+  __TEXT.__oslogstring: 0x1676
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__unwind_info: 0x250
   __TEXT.__objc_classname: 0xd2
-  __TEXT.__objc_methname: 0x1907
+  __TEXT.__objc_methname: 0x1973
   __TEXT.__objc_methtype: 0x34e
-  __TEXT.__objc_stubs: 0x1820
-  __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0x420
+  __TEXT.__objc_stubs: 0x1840
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0x428
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b0
+  __DATA_CONST.__objc_selrefs: 0x778
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0x9a8
+  __AUTH_CONST.__objc_const: 0x710
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_ivar: 0x38
   __DATA.__data: 0xc0
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 151
-  Symbols:   189
+  Functions: 153
+  Symbols:   180
   CStrings:  494
 
Symbols:
+ _AAFollowUpIdentifierChildProtoConnect
+ _OBJC_CLASS_$_AKFeatureManager
+ _objc_opt_respondsToSelector
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
+ "\x05"
+ "/System/AppleInternal/Library/Frameworks/SetupAssistant.framework/SetupAssistant"
+ "AAAccountNotificationPlugin - Only one proto account allowed. Rejecting save."
+ "AAAccountNotificationPlugin - proto account removal result %@"
+ "_protoAccountRemovalQueue"
+ "_removeProtoAccount"
+ "clearNonSecureAAPrefsDomain"
+ "com.apple.AAAccountNotificationPlugin.ProtoAccountRemoval"
+ "com.apple.AppleAccount.AAAccountNotificationPlugin-removeProto.txn"
+ "isAgeAttestationPhase1Enabled"
+ "primaryAccountSignInState"
+ "protoAccount"
+ "protoAccountType"
+ "removeProtoAccountWithCompletion:"
+ "resetAccountInfoToSignedOutState"
+ "sharedManager"
+ "updateAccountInfoForProtoAccount:"
+ "updateAccountInfoForRemovedProtoAccountWithStore:"
+ "updateAccountInformationCacheForAppleAccount:"
+ "updateChildProtoConnectFollowupForAccountStore:account:oldAccount:"
- "\x04"
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
