## DefaultAppsSettingsUIPlugin

> `/System/Library/PreferenceBundles/DefaultAppsSettingsUIPlugin.bundle/DefaultAppsSettingsUIPlugin`

```diff

-1308.2.4.3.0
-  __TEXT.__text: 0x19e00
-  __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_methlist: 0x98
-  __TEXT.__const: 0xec8
-  __TEXT.__cstring: 0xda4
-  __TEXT.__swift5_typeref: 0x13fa
-  __TEXT.__constg_swiftt: 0x338
-  __TEXT.__swift5_reflstr: 0x4f7
-  __TEXT.__swift5_fieldmd: 0x31c
-  __TEXT.__objc_methname: 0x7f5
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_capture: 0x138
-  __TEXT.__oslogstring: 0x28b
-  __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methtype: 0xd3
-  __TEXT.__unwind_info: 0x698
-  __TEXT.__eh_frame: 0x610
-  __DATA_CONST.__auth_got: 0x7f8
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__auth_ptr: 0x340
-  __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x30
+1308.2.7.101.0
+  __TEXT.__text: 0x1fa98
+  __TEXT.__auth_stubs: 0x1180
+  __TEXT.__objc_methlist: 0xc8
+  __TEXT.__const: 0x10f0
+  __TEXT.__cstring: 0x10b6
+  __TEXT.__swift5_typeref: 0x17a6
+  __TEXT.__swift5_capture: 0x1c4
+  __TEXT.__swift5_reflstr: 0x58a
+  __TEXT.__swift5_assocty: 0x120
+  __TEXT.__constg_swiftt: 0x44c
+  __TEXT.__swift5_fieldmd: 0x3c8
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__oslogstring: 0x28f
+  __TEXT.__objc_methname: 0x8e8
+  __TEXT.__swift5_proto: 0x64
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__objc_classname: 0x59
+  __TEXT.__objc_methtype: 0xea
+  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__eh_frame: 0x730
+  __DATA_CONST.__auth_got: 0x8c0
+  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__auth_ptr: 0x3c8
+  __DATA_CONST.__const: 0x670
+  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0xd68
-  __DATA.__objc_selrefs: 0x170
-  __DATA.__objc_data: 0x310
-  __DATA.__data: 0xc90
-  __DATA.__bss: 0xae0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA.__objc_const: 0xf48
+  __DATA.__objc_selrefs: 0x1e0
+  __DATA.__objc_data: 0x420
+  __DATA.__data: 0xf10
+  __DATA.__bss: 0xdc0
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 551
-  Symbols:   164
-  CStrings:  216
+  Functions: 658
+  Symbols:   183
+  CStrings:  244
 
Symbols:
+ _NSForegroundColorAttributeName
+ _OBJC_CLASS_$_LSObserver
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_UIColor
+ _OBJC_CLASS_$_UIFont
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UINavigationItem
+ _objc_release_x10
+ _objc_release_x27
+ _objc_release_x9
+ _objc_retain_x11
+ _objc_retain_x2
+ _objc_retain_x28
+ _objc_retain_x9
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_bridgeObjectRetain_n
+ _swift_initStackObject
CStrings:
+ " will be used to compose new emails. If you have multiple email apps, you can change the default."
+ " will be used to compose new messages. If you have multiple messaging apps, you can change the default."
+ " will be used to make payments. If you have multiple contactless apps, you can change the default."
+ " will be used to open links and browse the web. If you have multiple browser apps, you can change the default."
+ "DefaultAppsSettingsUIPlugin.Observer"
+ "Footer Text. Param is localized app name."
+ "LSObserverDelegate"
+ "UICTFontTextStyleShortEmphasizedBody"
+ "_TtC27DefaultAppsSettingsUIPlugin16LSChangeObserver"
+ "_TtCC27DefaultAppsSettingsUIPlugin16LSChangeObserverP33_8C266E9A54B8FCC77A7EDD4AE9F2EF1A8Observer"
+ "_available"
+ "_idToProvider"
+ "colorWithAlphaComponent:"
+ "initWithString:attributes:"
+ "labelColor"
+ "lsObserver"
+ "mainQueue"
+ "navigationItem"
+ "observerDidObserveDatabaseChange:"
+ "preferredFontForTextStyle:"
+ "setAttributedText:"
+ "setDelegate:"
+ "setFont:"
+ "setQueue:"
+ "setTitleView:"
+ "startObserving"
+ "stopObserving"
+ "v24@0:8@\"LSObserver\"16"

```
