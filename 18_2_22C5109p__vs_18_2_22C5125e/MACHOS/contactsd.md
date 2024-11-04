## contactsd

> `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

```diff

-3766.0.0.0.0
-  __TEXT.__text: 0x12e4c
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_stubs: 0x2ec0
-  __TEXT.__objc_methlist: 0xfd0
+3768.1.0.0.0
+  __TEXT.__text: 0x1367c
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_stubs: 0x2fa0
+  __TEXT.__objc_methlist: 0x10c8
   __TEXT.__const: 0x15a
   __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__objc_methname: 0x4000
-  __TEXT.__cstring: 0xf90
-  __TEXT.__objc_classname: 0x2e3
-  __TEXT.__objc_methtype: 0xeb3
+  __TEXT.__objc_methname: 0x40b6
+  __TEXT.__cstring: 0x1060
+  __TEXT.__objc_classname: 0x2fe
+  __TEXT.__objc_methtype: 0xece
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__oslogstring: 0xf58
+  __TEXT.__oslogstring: 0xfd0
   __TEXT.__swift5_typeref: 0x54
   __TEXT.__swift5_fieldmd: 0x20
-  __TEXT.__unwind_info: 0x5f8
-  __DATA_CONST.__auth_got: 0x390
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0xc58
-  __DATA_CONST.__cfstring: 0x6e0
-  __DATA_CONST.__objc_classlist: 0xa0
+  __TEXT.__unwind_info: 0x620
+  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__const: 0xc78
+  __DATA_CONST.__cfstring: 0x780
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2928
-  __DATA.__objc_selrefs: 0xef8
-  __DATA.__objc_ivar: 0xfc
-  __DATA.__objc_data: 0x6b8
+  __DATA.__objc_const: 0x2af8
+  __DATA.__objc_selrefs: 0xf30
+  __DATA.__objc_ivar: 0x110
+  __DATA.__objc_data: 0x708
   __DATA.__data: 0x360
-  __DATA.__bss: 0x180
+  __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 543
-  Symbols:   224
-  CStrings:  952
+  Functions: 566
+  Symbols:   228
+  CStrings:  969
 
Symbols:
+ _CFPreferencesCopyAppValue
+ _CFPreferencesSetAppValue
+ _CNContactStoreSettingsDefaultAppsDidChangeNotification
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
CStrings:
+ "B32@0:8Q16^{__CFString=}24"
+ "CNDefaultAppForMessaging"
+ "CNDefaultAppForPhoneCalls"
+ "SettingsDefaultAppsService"
+ "SettingsDefaultAppsService found settings changed, posting notification."
+ "SettingsDefaultAppsService will perform check."
+ "T@\"SettingsDefaultAppsService\",R"
+ "bundleIdentifier"
+ "checkDefaultAppChanged:forPersistedKey:"
+ "checkForAnyDefaultAppChanged"
+ "com.apple.LaunchServices.database"
+ "com.apple.contactsd.SettingsDefaultAppsService"
+ "com.apple.contactsd.SettingsDefaultAppsService.PerformCheck"
+ "defaultCenter"
+ "postNotificationName:object:"
+ "settingsDefaultApps"

```
