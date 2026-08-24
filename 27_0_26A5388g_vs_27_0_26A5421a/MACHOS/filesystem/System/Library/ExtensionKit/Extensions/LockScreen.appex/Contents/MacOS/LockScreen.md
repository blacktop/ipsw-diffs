## LockScreen

> `/System/Library/ExtensionKit/Extensions/LockScreen.appex/Contents/MacOS/LockScreen`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_entry`

```diff

-2027.0.1.0.0
-  __TEXT.__text: 0x33f88
-  __TEXT.__auth_stubs: 0x1410
-  __TEXT.__objc_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x2d4
+2027.0.2.0.0
+  __TEXT.__text: 0x34988
+  __TEXT.__auth_stubs: 0x14c0
+  __TEXT.__objc_stubs: 0x9c0
+  __TEXT.__objc_methlist: 0x17c
   __TEXT.__const: 0x2d24
-  __TEXT.__constg_swiftt: 0x116c
-  __TEXT.__swift5_typeref: 0x2eec
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0xb78
+  __TEXT.__constg_swiftt: 0x10d0
+  __TEXT.__swift5_typeref: 0x2ec8
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0xb68
   __TEXT.__swift5_assocty: 0x1c8
-  __TEXT.__swift5_fieldmd: 0x624
-  __TEXT.__swift5_capture: 0x7ac
+  __TEXT.__swift5_fieldmd: 0x5fc
+  __TEXT.__swift5_capture: 0x804
   __TEXT.__swift5_proto: 0x64
-  __TEXT.__swift5_types: 0x64
-  __TEXT.__objc_classname: 0x2ba
-  __TEXT.__objc_methname: 0x12de
-  __TEXT.__objc_methtype: 0x4b9
-  __TEXT.__cstring: 0x1afa
-  __TEXT.__swift_as_entry: 0x60
-  __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__swift_as_cont: 0x88
+  __TEXT.__swift5_types: 0x5c
+  __TEXT.__objc_classname: 0x24a
+  __TEXT.__objc_methname: 0x10b9
+  __TEXT.__objc_methtype: 0x3ed
+  __TEXT.__cstring: 0x1b9a
+  __TEXT.__swift_as_entry: 0x68
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__swift_as_cont: 0x90
   __TEXT.__swift5_entry: 0x8
   __TEXT.__oslogstring: 0x85
-  __TEXT.__unwind_info: 0xbf8
-  __TEXT.__eh_frame: 0xb58
-  __DATA_CONST.__const: 0x1768
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__unwind_info: 0xc20
+  __TEXT.__eh_frame: 0xc98
+  __DATA_CONST.__const: 0x17e8
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__auth_got: 0xa10
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__auth_ptr: 0x748
-  __DATA.__objc_const: 0xf60
-  __DATA.__objc_selrefs: 0x400
-  __DATA.__objc_data: 0x1e8
-  __DATA.__data: 0x2218
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__auth_got: 0xa68
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__auth_ptr: 0x740
+  __DATA.__objc_const: 0xda0
+  __DATA.__objc_selrefs: 0x318
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x20e8
   __DATA.__bss: 0x1290
-  __DATA.__common: 0x60
+  __DATA.__common: 0x38
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/Versions/A/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/Versions/A/LocalAuthenticationEmbeddedUI
   - /System/Library/Frameworks/SafariServices.framework/Versions/A/SafariServices
   - /System/Library/Frameworks/ScreenSaver.framework/Versions/A/ScreenSaver
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/Versions/A/LocalAuthenticationCredentialServices
   - /System/Library/PrivateFrameworks/LocalAuthenticationUI.framework/Versions/A/LocalAuthenticationUI
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/Settings.framework/Versions/A/Settings

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1181
-  Symbols:   185
-  CStrings:  394
+  Functions: 1186
+  Symbols:   192
+  CStrings:  345
 
Symbols:
+ _LAAuthenticationMechanismAny
+ _LAAuthenticationMechanismUserPassword
+ _LAAuthenticatorAnyAdminOrCurrentUser
+ _MKBDeviceSetGracePeriodWithACM
+ _OBJC_CLASS_$_LAAuthenticationSheetController
+ _OBJC_CLASS_$_LACSSecurePassword
+ _getpwnam_r
+ _strerror
+ _swift_isEscapingClosureAtFileLocation
+ _swift_willThrow
+ _sysconf
- _MKBDeviceSetGracePeriod
- _OBJC_CLASS_$_LAUIAuthenticationSheetController
- _OBJC_METACLASS_$_NSObject
- _objc_msgSendSuper2
CStrings:
+ "Auth failed: auth context is nil."
+ "Auth failed: no evaluation result."
+ "Auth failed: password is not suplied or invalid."
+ "Auth failed: wrong user."
+ "Could not create secure password: "
+ "Could not decode authorized username as UTF-8."
+ "Could not externalize password: "
+ "Could not extract credential: "
+ "Could not resolve UID for authorized user: "
+ "Could not resolve UID for authorized user: no such user."
+ "authenticateInWindow:completion:"
+ "context"
+ "initWithData:error:"
+ "initWithMechanisms:authenticator:"
+ "setAuthenticationMessage:"
+ "setAuthenticationTitle:"
+ "setIsPasswordExtractable:"
+ "setIsUserNameFieldEnabled:"
+ "setSubmitButtonTitle:"
+ "userID"
+ "v16@?0@\"NSData\"8"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "withContextRef:"
- "#16@0:8"
- ". Did authentication finish too early or get terminated?"
- ".cxx_destruct"
- "@\"NSString\"16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "Authentication context is nil. This should never happen."
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Could not extract authorization UID (OSStatus: "
- "Could not find user (uid: "
- "Could not obtain credentials: "
- "LAUIAuthenticationSheetDelegate"
- "NSObject"
- "Obtained empty credentials."
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC10LockScreenP33_B3138C1F326FE9EE806C020159E179D912AuthDelegate"
- "authContext"
- "autorelease"
- "beginSheetForWindow:completion:"
- "class"
- "conformsToProtocol:"
- "controller"
- "dealloc"
- "debugDescription"
- "description"
- "findUserByID:searchParent:"
- "hash"
- "invalidate"
- "isCredentialSet:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "q20@0:8I16"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAuthSubTitleNoTouchID:"
- "setAuthTitle:"
- "setCanAuthenticateAsAnyAdmin:"
- "setDelegate:"
- "setEnableUserNameField:"
- "setPasswordExtractable:"
- "setSkipUserCredentialsVerification:"
- "setTouchIDInhibited:"
- "setUnlockButtonTitle:"
- "setVerifyAdminGroupMembershipForDelegate:"
- "superclass"
- "unverifiedDataEntered(_:completion:)"
- "unverifiedDataEntered:"
- "unverifiedDataEntered:completion:"
- "v20@?0B8@\"NSError\"12"
- "v28@0:8I16@?20"
- "v28@0:8I16@?<v@?q>20"
- "verifyPassword:"
- "zone"
```
