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
+ _objc_msgSend
+ _swift_release
+ _swift_bridgeObjectRelease_n
+ _swift_continuation_throwingResumeWithError
+ __swiftImmortalRefCount
+ _swift_getTypeByMangledNameInContext2
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCompression
+ _malloc_size
+ _objc_release_x20
+ _objc_retain_x8
+ _swift_once
+ _OBJC_CLASS_$_ACAccountStore
+ _objc_retainAutoreleasedReturnValue
+ _swift_bridgeObjectRelease
+ _free
+ _swift_errorRelease
+ _swift_willThrow
+ _OBJC_CLASS_$_ACAccount
+ __swift_FORCE_LOAD_$_swiftSpatial
+ _swift_task_alloc
+ _objc_release_x27
+ _OBJC_CLASS_$_ACAccountType
+ _malloc
+ _objc_opt_self
+ _objc_release_x21
+ _objc_retain_x20
+ _swift_slowAlloc
+ ___chkstk_darwin
+ _swift_allocError
+ _swift_bridgeObjectRetain
+ _swift_continuation_throwingResume
+ _swift_retain
+ __NSConcreteStackBlock
+ __swiftEmptyArrayStorage
+ _objc_release_x19
+ _swift_allocObject
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ _memmove
+ _swift_continuation_init
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x8
+ _swift_arrayInitWithCopy
+ _swift_getObjCClassMetadata
+ _swift_task_dealloc
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _objc_release_x26
+ _swift_task_switch
+ __swift_FORCE_LOAD_$_swiftUIKit
+ _swift_continuation_await
CStrings:
+ "View the list of internet accounts logged in for various first and third party services for use in apps such as Mail, Contacts, and Calendar."
+ "Apps → Contacts → Contacts Accounts"
+ "Apps → Contacts → Contacts Accounts → Add Account"
+ "Go to a specific Internet Accountʼs settings page"
+ "Go to settings for "
+ "Log into an LDAP account"
+ "Log into an Outlook account"
+ "Open an Internet Accountʼs Settings"
+ "accountDescription"
+ "Apps → Contacts → Contacts Accounts → "
+ "Contacts accounts list"
+ "Internet Accounts"
+ "Open Internet Accounts List"
+ "accountType"
+ "com.apple.Preferences"
+ "identifier"
+ "Add a Reminders Account"
+ "Go to the settings for the "
+ "Log into a CalDAV account"
+ "Log into a Google account"
+ "Log into a Yahoo! account"
+ "Log into an AOL account"
+ "Log into an Internet Account"
+ "settings-navigation://com.apple.Settings.InternetAccounts/"
+ "Calendar accounts list"
+ "Log in to internet accounts for various first and third party services for use in apps such as Mail, Contacts, and Calendar."
+ "Mail accounts list"
+ "accountsWithAccountTypeIdentifiers:completion:"
+ "addAccount"
+ "Log into an iCloud account"
+ "Open List of Internet Accounts"
+ "accountWithIdentifier:"
+ "monitoredAccountWithIdentifier:"
+ "Add a Contacts Account"
+ "Log into a POP account"
+ "Log into an IMAP account"
+ "Reminders accounts list"
+ "Log into a CardDAV account"
+ "Log into an Exchange account"
+ "Notes accounts list"
+ "defaultStore"
+ "root"
+ "settings-navigation://com.apple.Settings.InternetAccounts/root"
+ "Add a Calendar Account"
+ "Add a Mail Account"
+ "Add a Notes Account"
+ "List of Internet Accounts"
+ "com.apple.AccountsUISettings.AppIntents"
+ "settings-navigation://com.apple.Settings.InternetAccounts/ADD_ACCOUNT"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"

```
