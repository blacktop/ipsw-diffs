## AppleAccountMigrator

> `/System/Library/DataClassMigrators/AppleAccountMigrator.migrator/AppleAccountMigrator`

```diff

-1007.227.1.0.0
-  __TEXT.__text: 0x1b44
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x560
-  __TEXT.__objc_methlist: 0xc8
-  __TEXT.__const: 0x14
-  __TEXT.__cstring: 0x28
-  __TEXT.__objc_methname: 0x49f
-  __TEXT.__oslogstring: 0x6b2
-  __TEXT.__objc_classname: 0x17
+1007.229.4.0.0
+  __TEXT.__text: 0x2240
+  __TEXT.__auth_stubs: 0x220
+  __TEXT.__objc_stubs: 0x6e0
+  __TEXT.__objc_methlist: 0xe0
+  __TEXT.__const: 0x2c
+  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__cstring: 0xff
+  __TEXT.__objc_methname: 0x5ca
+  __TEXT.__oslogstring: 0x748
+  __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0x4a
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__cfstring: 0x80
+  __TEXT.__dlopen_cstrs: 0x56
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0x60
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0xf8
-  __DATA.__objc_selrefs: 0x188
+  __DATA.__objc_selrefs: 0x1e8
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 23
-  Symbols:   53
-  CStrings:  101
+  Functions: 32
+  Symbols:   73
+  CStrings:  127
 
Symbols:
+ _AAPrefsDomain
+ _CFPreferencesSetAppValue
+ _CFPreferencesSynchronize
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSUserDefaults
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ __sl_dlopen
+ _free
+ _kAAAccountFullName
+ _kAAAccountIsSignedInKey
+ _kAAAccountUsername
+ _kAAProfilePictureCacheURL
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _objc_getClass
+ _objc_retainAutorelease
CStrings:
+ "%s"
+ "AppleAccountMigrator.m"
+ "Class getFLFollowUpControllerClass(void)_block_invoke"
+ "Cleared Apple Account Information Properties from AAPrefsDomain."
+ "Did clear Pending secureTerms CFU %d with error: %@"
+ "FLFollowUpController"
+ "No need to clear secureTerms CFU"
+ "SecureTerms"
+ "Unable to find class %s"
+ "_clearAppleAccountInformationCache"
+ "_clearSecureTermsCFU"
+ "boolForKey:"
+ "clearPendingFollowUpItemsWithUniqueIdentifiers:error:"
+ "com.apple.corecdp"
+ "currentHandler"
+ "deletedSecureTermsCFU"
+ "description"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "initWithClientIdentifier:"
+ "setBool:forKey:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp"
+ "standardUserDefaults"
+ "stringWithUTF8String:"
+ "synchronize"
+ "v8@?0"
+ "void *CoreFollowUpLibrary(void)"

```
