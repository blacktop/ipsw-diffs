## AudioIntelligencePhoneSettingsUI

> `/System/Library/PrivateFrameworks/AudioIntelligencePhoneSettingsUI.framework/AudioIntelligencePhoneSettingsUI`

```diff

-257.1.0.0.0
-  __TEXT.__text: 0x3360c
-  __TEXT.__objc_methlist: 0x1684
-  __TEXT.__const: 0x1498
+262.0.0.0.0
+  __TEXT.__text: 0x35be4
+  __TEXT.__objc_methlist: 0x171c
+  __TEXT.__const: 0x14c8
   __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__cstring: 0x2171
-  __TEXT.__oslogstring: 0x1556
+  __TEXT.__cstring: 0x2311
+  __TEXT.__oslogstring: 0x1687
   __TEXT.__ustring: 0x10
-  __TEXT.__constg_swiftt: 0xb04
-  __TEXT.__swift5_typeref: 0x21de
+  __TEXT.__constg_swiftt: 0xb3c
+  __TEXT.__swift5_typeref: 0x221e
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x65a
-  __TEXT.__swift5_fieldmd: 0x6e8
-  __TEXT.__swift5_types: 0x7c
+  __TEXT.__swift5_reflstr: 0x65b
+  __TEXT.__swift5_fieldmd: 0x704
+  __TEXT.__swift5_types: 0x80
   __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x78
   __TEXT.__swift5_assocty: 0x128
+  __TEXT.__swift5_capture: 0x480
   __TEXT.__swift5_proto: 0x60
-  __TEXT.__swift5_capture: 0x448
-  __TEXT.__unwind_info: 0x1018
+  __TEXT.__unwind_info: 0x1090
   __TEXT.__eh_frame: 0xb4c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x420
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14d0
+  __DATA_CONST.__objc_selrefs: 0x1548
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x710
-  __AUTH_CONST.__const: 0x11e0
-  __AUTH_CONST.__cfstring: 0xae0
-  __AUTH_CONST.__objc_const: 0x20e0
-  __AUTH_CONST.__auth_got: 0xdc0
-  __AUTH.__objc_data: 0x1300
-  __AUTH.__data: 0x6d0
-  __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0xd40
+  __DATA_CONST.__got: 0x730
+  __AUTH_CONST.__const: 0x12a8
+  __AUTH_CONST.__cfstring: 0xb60
+  __AUTH_CONST.__objc_const: 0x2180
+  __AUTH_CONST.__auth_got: 0xdd0
+  __AUTH.__objc_data: 0x13c0
+  __AUTH.__data: 0x6f0
+  __DATA.__objc_ivar: 0x68
+  __DATA.__data: 0xd58
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1167
-  Symbols:   1031
-  CStrings:  302
+  Functions: 1203
+  Symbols:   1055
+  CStrings:  321
 
Symbols:
+ -[PhoneSettingsController .cxx_destruct]
+ -[PhoneSettingsController _retentionSpecifiers]
+ -[PhoneSettingsController getRetentionDays:]
+ -[PhoneSettingsController privacyPresenter]
+ -[PhoneSettingsController setPrivacyPresenter:]
+ -[PhoneSettingsController setRetentionDays:specifier:]
+ GCC_except_table25
+ GCC_except_table44
+ _OBJC_CLASS_$_OBPrivacyPresenter
+ _OBJC_CLASS_$_PSListItemsController
+ _OBJC_CLASS_$_RetentionListItemsController
+ _OBJC_IVAR_$_PhoneSettingsController._privacyPresenter
+ _OBJC_METACLASS_$_PSListItemsController
+ _OBJC_METACLASS_$_RetentionListItemsController
+ _PSStaticHeaderTextKey
+ _PSStaticTextMessageKey
+ _RSMindPalaceRollingDeletionRetentionDidChangeNotification
+ __CLASS_METHODS_RetentionListItemsController
+ __DATA_RetentionListItemsController
+ __INSTANCE_METHODS_RetentionListItemsController
+ __IVARS_RetentionListItemsController
+ __METACLASS_DATA_RetentionListItemsController
+ _swift_dynamicCast
+ _symbolic So21PSListItemsControllerC
+ _symbolic _____ 10Foundation9IndexPathV
+ _symbolic _____ 32AudioIntelligencePhoneSettingsUI28RetentionListItemsControllerC
+ _symbolic _____SgXw 32AudioIntelligencePhoneSettingsUI28RetentionListItemsControllerC
+ _symbolic _____SgXwz_Xx 32AudioIntelligencePhoneSettingsUI28RetentionListItemsControllerC
- GCC_except_table22
- GCC_except_table41
- _OBJC_CLASS_$_UIApplication
- ___NSDictionary0__struct
CStrings:
+ "AudioIntelligencePhoneSettingsUI/RetentionListItemsController.swift"
+ "KEEP_UNSAVED_RECAPS"
+ "Presenting privacy pane"
+ "RETENTION_1_DAY_ALERT_MESSAGE"
+ "RETENTION_3_DAYS"
+ "RETENTION_3_DAYS_ALERT_MESSAGE"
+ "RETENTION_7_DAYS"
+ "RETENTION_ALERT_CANCEL"
+ "RETENTION_ALERT_DELETE"
+ "RETENTION_ALERT_TITLE"
+ "RETENTION_FOOTER"
+ "RETENTION_GROUP_ID"
+ "RETENTION_ID"
+ "Retention: cancelled, keeping stored value"
+ "Retention: confirmed, writing %ld days"
+ "Retention: ignoring unselectable %ld days"
+ "Retention: no days for row %{public}s, passing through"
+ "Retention: presenting confirmation for %ld days"
+ "Retention: writing %ld days"
+ "com.apple.onboarding.conversationintelligence"
- "https://support.apple.com/en-us/148354"
```
