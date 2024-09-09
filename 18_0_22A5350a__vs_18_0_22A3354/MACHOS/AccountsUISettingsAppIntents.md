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
+ _malloc
+ _objc_release_x27
+ _objc_release_x8
+ __NSConcreteStackBlock
+ __swift_FORCE_LOAD_$_swiftSpatial
+ _swift_task_alloc
+ _swift_arrayInitWithCopy
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ _objc_release_x21
+ _swift_continuation_throwingResume
+ _objc_retain_x8
+ _swift_continuation_throwingResumeWithError
+ _OBJC_CLASS_$_ACAccount
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _swift_continuation_init
+ _swift_once
+ _swift_release
+ _memmove
+ _swift_bridgeObjectRetain
+ _free
+ _objc_retain_x20
+ __swift_FORCE_LOAD_$_swiftCompression
+ _swift_slowAlloc
+ _swift_task_switch
+ __swiftEmptyArrayStorage
+ _objc_msgSend
+ _objc_release_x20
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ __swiftImmortalRefCount
+ _swift_retain
+ _swift_task_dealloc
+ _swift_willThrow
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _objc_release_x23
+ _swift_getObjCClassMetadata
+ _malloc_size
+ _objc_release_x22
+ _swift_allocError
+ _swift_bridgeObjectRelease_n
+ _swift_continuation_await
+ _objc_release_x19
+ _objc_release_x26
+ _swift_bridgeObjectRelease
+ _swift_errorRelease
+ ___chkstk_darwin
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swiftEmptyDictionarySingleton
+ _swift_allocObject
+ _swift_getTypeByMangledNameInContext2
+ _OBJC_CLASS_$_ACAccountStore
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ _OBJC_CLASS_$_ACAccountType
CStrings:
+ "Go to settings for "
+ "Go to the settings for the "
+ "Log into a POP account"
+ "Mail accounts list"
+ "Add a Notes Account"
+ "Log into a Yahoo! account"
+ "Log into an Exchange account"
+ "Open List of Internet Accounts"
+ "accountsWithAccountTypeIdentifiers:completion:"
+ "com.apple.AccountsUISettings.AppIntents"
+ "monitoredAccountWithIdentifier:"
+ "settings-navigation://com.apple.Settings.InternetAccounts/root"
+ "Apps → Contacts → Contacts Accounts → Add Account"
+ "Apps → Contacts → Contacts Accounts → "
+ "Go to a specific Internet Accountʼs settings page"
+ "List of Internet Accounts"
+ "Log into an AOL account"
+ "Log into an Internet Account"
+ "Log into an LDAP account"
+ "Apps → Contacts → Contacts Accounts"
+ "Contacts accounts list"
+ "Log into a Google account"
+ "Open an Internet Accountʼs Settings"
+ "View the list of internet accounts logged in for various first and third party services for use in apps such as Mail, Contacts, and Calendar."
+ "accountDescription"
+ "accountWithIdentifier:"
+ "com.apple.Preferences"
+ "Add a Reminders Account"
+ "settings-navigation://com.apple.Settings.InternetAccounts/"
+ "root"
+ "Log into an Outlook account"
+ "identifier"
+ "settings-navigation://com.apple.Settings.InternetAccounts/ADD_ACCOUNT"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "Internet Accounts"
+ "Calendar accounts list"
+ "Log in to internet accounts for various first and third party services for use in apps such as Mail, Contacts, and Calendar."
+ "Log into a CardDAV account"
+ "Log into an iCloud account"
+ "Notes accounts list"
+ "accountType"
+ "Add a Calendar Account"
+ "Open Internet Accounts List"
+ "Reminders accounts list"
+ "addAccount"
+ "Add a Mail Account"
+ "Log into a CalDAV account"
+ "Log into an IMAP account"
+ "defaultStore"
+ "Add a Contacts Account"

```
