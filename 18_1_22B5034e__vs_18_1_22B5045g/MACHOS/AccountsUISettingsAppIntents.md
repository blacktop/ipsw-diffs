## AccountsUISettingsAppIntents

> `/System/Library/ExtensionKit/Extensions/AccountsUISettingsAppIntents.appex/AccountsUISettingsAppIntents`

```diff

 60.0.0.0.0
-  __TEXT.__text: 0x1b8
-  __TEXT.__auth_stubs: 0x60
-  __TEXT.__const: 0x116
-  __TEXT.__swift5_typeref: 0x46
-  __TEXT.__swift5_reflstr: 0xe
-  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__text: 0x60a4
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__const: 0xcf6
+  __TEXT.__cstring: 0x6e6
+  __TEXT.__swift5_typeref: 0x4b6
+  __TEXT.__swift5_reflstr: 0x11b
+  __TEXT.__swift5_assocty: 0x178
+  __TEXT.__constg_swiftt: 0xd0
+  __TEXT.__swift5_fieldmd: 0xb8
+  __TEXT.__objc_methname: 0x9d
+  __TEXT.__swift5_proto: 0xc4
+  __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x28
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x30
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0xd8
+  __TEXT.__unwind_info: 0x360
+  __TEXT.__eh_frame: 0x258
+  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_ptr: 0x4e0
+  __DATA_CONST.__const: 0x3c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x10
-  __DATA.__bss: 0x100
+  __DATA.__objc_selrefs: 0x38
+  __DATA.__data: 0x310
+  __DATA.__common: 0x80
+  __DATA.__bss: 0x1880
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings
+  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8
-  Symbols:   32
-  CStrings:  0
+  Functions: 236
+  Symbols:   85
+  CStrings:  50
 
Symbols:
+ _OBJC_CLASS_$_ACAccountType
+ _swift_allocError
+ _swift_continuation_await
+ _swift_task_alloc
+ __swiftEmptyDictionarySingleton
+ _OBJC_CLASS_$_ACAccountStore
+ __swiftImmortalRefCount
+ _swift_continuation_init
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x8
+ __NSConcreteStackBlock
+ _objc_release_x27
+ _swift_bridgeObjectRetain
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftUIKit
+ _objc_release_x20
+ _swift_once
+ _OBJC_CLASS_$_ACAccount
+ _swift_allocObject
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_task_dealloc
+ _memmove
+ _objc_opt_self
+ _objc_release_x26
+ _swift_bridgeObjectRelease_n
+ _swift_task_switch
+ _objc_release_x19
+ ___chkstk_darwin
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ _objc_release_x22
+ _swift_slowAlloc
+ __swift_FORCE_LOAD_$_swiftCompression
+ _free
+ _malloc_size
+ _objc_msgSend
+ _objc_release_x8
+ _swift_bridgeObjectRelease
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _malloc
+ _objc_retain_x20
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_retain
+ _objc_release_x21
+ _objc_release_x23
+ _swift_errorRelease
+ _swift_getTypeByMangledNameInContext2
+ _swift_release
+ __swiftEmptyArrayStorage
+ _swift_arrayInitWithCopy
+ _swift_getObjCClassMetadata
+ _swift_willThrow
CStrings:
+ "accountWithIdentifier:"
+ "settings-navigation://com.apple.Settings.InternetAccounts/ADD_ACCOUNT"
+ "Add a Calendar Account"
+ "Log in to internet accounts for various first and third party services for use in apps such as Mail, Contacts, and Calendar."
+ "Log into a CardDAV account"
+ "Log into a POP account"
+ "Notes accounts list"
+ "Open an Internet Accountʼs Settings"
+ "Add a Notes Account"
+ "Apps → Contacts → Contacts Accounts → Add Account"
+ "Contacts accounts list"
+ "Log into an IMAP account"
+ "Reminders accounts list"
+ "settings-navigation://com.apple.Settings.InternetAccounts/root"
+ "Apps → Contacts → Contacts Accounts"
+ "List of Internet Accounts"
+ "Log into a Yahoo! account"
+ "Open Internet Accounts List"
+ "monitoredAccountWithIdentifier:"
+ "Go to a specific Internet Accountʼs settings page"
+ "Go to settings for "
+ "Go to the settings for the "
+ "Add a Contacts Account"
+ "Log into an Outlook account"
+ "View the list of internet accounts logged in for various first and third party services for use in apps such as Mail, Contacts, and Calendar."
+ "accountDescription"
+ "accountType"
+ "addAccount"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "Add a Reminders Account"
+ "Apps → Contacts → Contacts Accounts → "
+ "Internet Accounts"
+ "Log into an Internet Account"
+ "Mail accounts list"
+ "settings-navigation://com.apple.Settings.InternetAccounts/"
+ "com.apple.Preferences"
+ "Add a Mail Account"
+ "Calendar accounts list"
+ "Log into an AOL account"
+ "Log into an LDAP account"
+ "Open List of Internet Accounts"
+ "accountsWithAccountTypeIdentifiers:completion:"
+ "identifier"
+ "root"
+ "Log into a CalDAV account"
+ "Log into a Google account"
+ "Log into an Exchange account"
+ "Log into an iCloud account"
+ "com.apple.AccountsUISettings.AppIntents"
+ "defaultStore"

```
