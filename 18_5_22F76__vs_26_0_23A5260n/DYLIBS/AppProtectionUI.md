## AppProtectionUI

> `/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI`

```diff

-35.2.8.0.0
-  __TEXT.__text: 0x15edc
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0xee0
-  __TEXT.__const: 0x4b8
-  __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__oslogstring: 0x593
-  __TEXT.__cstring: 0x1737
+38.0.0.0.0
+  __TEXT.__text: 0x1812c
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0xf10
+  __TEXT.__const: 0x4d8
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__oslogstring: 0x598
+  __TEXT.__cstring: 0x17d7
   __TEXT.__constg_swiftt: 0x3cc
-  __TEXT.__swift5_typeref: 0x4e2
+  __TEXT.__swift5_typeref: 0x522
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_reflstr: 0x144
   __TEXT.__swift5_fieldmd: 0x218
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x30
-  __TEXT.__swift5_capture: 0x414
+  __TEXT.__swift5_capture: 0x648
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__unwind_info: 0x658
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x280
-  __TEXT.__objc_methname: 0x30f9
-  __TEXT.__objc_methtype: 0xfc6
-  __TEXT.__objc_stubs: 0x1ba0
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x398
+  __TEXT.__objc_methname: 0x3240
+  __TEXT.__objc_methtype: 0xfb3
+  __TEXT.__objc_stubs: 0x1c80
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__const: 0x370
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd48
+  __DATA_CONST.__objc_selrefs: 0xda8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x5c0
-  __AUTH_CONST.__const: 0x11f0
-  __AUTH_CONST.__cfstring: 0x980
-  __AUTH_CONST.__objc_const: 0x1e00
+  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__const: 0x16a0
+  __AUTH_CONST.__cfstring: 0xa00
+  __AUTH_CONST.__objc_const: 0x1e10
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH.__objc_data: 0xa38
+  __AUTH.__data: 0x170
   __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0x678
+  __DATA.__data: 0x698
   __DATA.__bss: 0xc0
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0xb28
-  __DATA_DIRTY.__data: 0x1e0
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__data: 0x70
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B94A1D85-7CC1-3704-AEE3-AADD5BBB067F
-  Functions: 598
-  Symbols:   1501
-  CStrings:  953
+  UUID: 35E8F016-46BE-302F-81FE-925DC642DD3D
+  Functions: 683
+  Symbols:   1577
+  CStrings:  974
 
Symbols:
+ -[APBaseExtensionShieldView initWithLocalizedApplicationName:iconImage:apExtension:]
+ -[APBaseExtensionShieldView initWithLocalizedApplicationName:iconImage:unlockButtonHidden:apExtension:]
+ _APGetAuthenticationMechanismLocKey
+ _OBJC_CLASS_$_UISheetPresentationControllerDetent
+ __PROTOCOLS_APEducationFlowViewController.61
+ ___103-[APBaseExtensionShieldView initWithLocalizedApplicationName:iconImage:unlockButtonHidden:apExtension:]_block_invoke
+ ___103-[APBaseExtensionShieldView initWithLocalizedApplicationName:iconImage:unlockButtonHidden:apExtension:]_block_invoke_2
+ ___36-[APBaseShieldView emergencyTapped:]_block_invoke.86
+ ___36-[APBaseShieldView emergencyTapped:]_block_invoke.86.cold.1
+ ___36-[APBaseShieldView emergencyTapped:]_block_invoke.86.cold.2
+ ___92-[APBaseShieldView initWithLocalizedApplicationName:useHiddenStyle:needEmergencyCallButton:]_block_invoke.59
+ ___92-[APBaseShieldView initWithLocalizedApplicationName:useHiddenStyle:needEmergencyCallButton:]_block_invoke_2.76
+ ___block_literal_global.36
+ ___block_literal_global.41
+ ___block_literal_global.61
+ ___block_literal_global.78
+ ___block_literal_global.84
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AppProtectionUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AppProtectionUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AppProtectionUI
+ _block_copy_helper.106
+ _block_copy_helper.110
+ _block_copy_helper.116
+ _block_copy_helper.122
+ _block_copy_helper.128
+ _block_copy_helper.134
+ _block_copy_helper.138
+ _block_copy_helper.142
+ _block_copy_helper.146
+ _block_copy_helper.150
+ _block_copy_helper.157
+ _block_copy_helper.161
+ _block_copy_helper.165
+ _block_copy_helper.169
+ _block_copy_helper.176
+ _block_copy_helper.180
+ _block_copy_helper.184
+ _block_copy_helper.188
+ _block_copy_helper.201
+ _block_copy_helper.207
+ _block_copy_helper.214
+ _block_copy_helper.22
+ _block_copy_helper.234
+ _block_copy_helper.241
+ _block_copy_helper.248
+ _block_copy_helper.255
+ _block_copy_helper.262
+ _block_copy_helper.269
+ _block_copy_helper.43
+ _block_copy_helper.58
+ _block_copy_helper.65
+ _block_copy_helper.8
+ _block_copy_helper.80
+ _block_copy_helper.86
+ _block_descriptor.10
+ _block_descriptor.108
+ _block_descriptor.112
+ _block_descriptor.118
+ _block_descriptor.124
+ _block_descriptor.130
+ _block_descriptor.136
+ _block_descriptor.140
+ _block_descriptor.144
+ _block_descriptor.148
+ _block_descriptor.152
+ _block_descriptor.159
+ _block_descriptor.163
+ _block_descriptor.167
+ _block_descriptor.171
+ _block_descriptor.178
+ _block_descriptor.182
+ _block_descriptor.186
+ _block_descriptor.190
+ _block_descriptor.203
+ _block_descriptor.209
+ _block_descriptor.216
+ _block_descriptor.236
+ _block_descriptor.24
+ _block_descriptor.243
+ _block_descriptor.250
+ _block_descriptor.257
+ _block_descriptor.264
+ _block_descriptor.271
+ _block_descriptor.45
+ _block_descriptor.60
+ _block_descriptor.67
+ _block_descriptor.82
+ _block_descriptor.88
+ _block_destroy_helper.107
+ _block_destroy_helper.111
+ _block_destroy_helper.117
+ _block_destroy_helper.123
+ _block_destroy_helper.129
+ _block_destroy_helper.135
+ _block_destroy_helper.139
+ _block_destroy_helper.143
+ _block_destroy_helper.147
+ _block_destroy_helper.151
+ _block_destroy_helper.158
+ _block_destroy_helper.162
+ _block_destroy_helper.166
+ _block_destroy_helper.170
+ _block_destroy_helper.177
+ _block_destroy_helper.181
+ _block_destroy_helper.185
+ _block_destroy_helper.189
+ _block_destroy_helper.202
+ _block_destroy_helper.208
+ _block_destroy_helper.215
+ _block_destroy_helper.23
+ _block_destroy_helper.235
+ _block_destroy_helper.242
+ _block_destroy_helper.249
+ _block_destroy_helper.256
+ _block_destroy_helper.263
+ _block_destroy_helper.270
+ _block_destroy_helper.44
+ _block_destroy_helper.59
+ _block_destroy_helper.66
+ _block_destroy_helper.81
+ _block_destroy_helper.87
+ _block_destroy_helper.9
+ _objc_msgSend$initWithImage:
+ _objc_msgSend$initWithLocalizedApplicationName:iconImage:unlockButtonHidden:apExtension:
+ _objc_msgSend$initWithSize:scale:
+ _objc_msgSend$isFirstParty
+ _objc_msgSend$setClipsToBounds:
+ _objc_msgSend$setDrawBorder:
+ _objc_msgSend$stringByAppendingString:
+ _objc_retain_x24
+ _objectdestroy.155Tm
+ _objectdestroy.6Tm
+ _os_variant_has_internal_content
+ _symbolic B0
+ _symbolic SaySo19LSApplicationRecordCG
+ _symbolic xSgXw
+ _symbolic xSgXwz_x_RlzC_____RzlXX 15AppProtectionUI31APRErrorAlertControllerDelegateP
- __PROTOCOLS_APEducationFlowViewController.5
- ___36-[APBaseShieldView emergencyTapped:]_block_invoke.77
- ___36-[APBaseShieldView emergencyTapped:]_block_invoke.77.cold.1
- ___36-[APBaseShieldView emergencyTapped:]_block_invoke.77.cold.2
- ___91-[APBaseExtensionShieldView initWithLocalizedApplicationName:iconImage:unlockButtonHidden:]_block_invoke
- ___91-[APBaseExtensionShieldView initWithLocalizedApplicationName:iconImage:unlockButtonHidden:]_block_invoke_2
- ___92-[APBaseShieldView initWithLocalizedApplicationName:useHiddenStyle:needEmergencyCallButton:]_block_invoke.53
- ___92-[APBaseShieldView initWithLocalizedApplicationName:useHiddenStyle:needEmergencyCallButton:]_block_invoke_2.67
- ___block_literal_global.28
- ___block_literal_global.38
- ___block_literal_global.55
- ___block_literal_global.69
- ___block_literal_global.75
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftDataDetection_$_AppProtectionUI
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_AppProtectionUI
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_AppProtectionUI
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_AppProtectionUI
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_AppProtectionUI
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_AppProtectionUI
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_AppProtectionUI
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_AppProtectionUI
- _block_copy_helper.112
- _block_copy_helper.121
- _block_copy_helper.127
- _block_copy_helper.133
- _block_copy_helper.147
- _block_copy_helper.151
- _block_copy_helper.155
- _block_copy_helper.162
- _block_copy_helper.168
- _block_copy_helper.174
- _block_copy_helper.18
- _block_copy_helper.24
- _block_copy_helper.28
- _block_copy_helper.32
- _block_copy_helper.40
- _block_copy_helper.46
- _block_copy_helper.56
- _block_copy_helper.60
- _block_copy_helper.64
- _block_copy_helper.75
- _block_copy_helper.79
- _block_copy_helper.83
- _block_descriptor.114
- _block_descriptor.123
- _block_descriptor.129
- _block_descriptor.135
- _block_descriptor.149
- _block_descriptor.153
- _block_descriptor.157
- _block_descriptor.164
- _block_descriptor.170
- _block_descriptor.176
- _block_descriptor.20
- _block_descriptor.26
- _block_descriptor.30
- _block_descriptor.34
- _block_descriptor.42
- _block_descriptor.48
- _block_descriptor.58
- _block_descriptor.62
- _block_descriptor.66
- _block_descriptor.77
- _block_descriptor.81
- _block_descriptor.85
- _block_destroy_helper.113
- _block_destroy_helper.122
- _block_destroy_helper.128
- _block_destroy_helper.134
- _block_destroy_helper.148
- _block_destroy_helper.152
- _block_destroy_helper.156
- _block_destroy_helper.163
- _block_destroy_helper.169
- _block_destroy_helper.175
- _block_destroy_helper.19
- _block_destroy_helper.25
- _block_destroy_helper.29
- _block_destroy_helper.33
- _block_destroy_helper.41
- _block_destroy_helper.47
- _block_destroy_helper.57
- _block_destroy_helper.61
- _block_destroy_helper.65
- _block_destroy_helper.76
- _block_destroy_helper.80
- _block_destroy_helper.84
- _objectdestroy.69Tm
CStrings:
+ "@\"UIView\""
+ "APBaseExtensionShieldUnlockButton"
+ "CHANGE_DEFAULT_APP_TO_HIDE"
+ "CHANGE_DEFAULT_BROWSER_TO_HIDE"
+ "CHANGE_DEFAULT_MAIL_CLIENT_TO_HIDE"
+ "CHANGE_DEFAULT_MESSENGER_TO_HIDE"
+ "CHANGE_DEFAULT_PAYMENT_TO_HIDE"
+ "CHANGE_DEFAULT_PHONE_TO_HIDE"
+ "FACE_ID_REQUIRED_TO_OPEN_"
+ "PASSCODE_REQUIRED_TO_OPEN_"
+ "T@\"UIViewController\",N,&,VinitialAlertController"
+ "TOUCH_ID_REQUIRED_TO_OPEN_"
+ "X"
+ "XCTestBundlePath"
+ "appProtectionShieldLabelIdentifier"
+ "appProtectionShieldUnlockButton"
+ "initWithImage:"
+ "initWithLocalizedApplicationName:iconImage:apExtension:"
+ "initWithLocalizedApplicationName:iconImage:unlockButtonHidden:apExtension:"
+ "initWithSize:scale:"
+ "isFirstParty"
+ "prefs:root=PASSCODE#PASSCODE_OFF"
+ "setClipsToBounds:"
+ "setDetents:"
+ "setDrawBorder:"
+ "setInitialAlertController:"
+ "sheetPresentationController"
+ "stringByAppendingString:"
- "@\"APSymbolBadgedAppIconView\""
- "CHANGE_DEFAULT_APP_TO_HIDE_X"
- "CHANGE_DEFAULT_BROWSER_TO_HIDE_X"
- "CHANGE_DEFAULT_MAIL_CLIENT_TO_HIDE_X"
- "CHANGE_DEFAULT_MESSENGER_TO_HIDE_X"
- "CHANGE_DEFAULT_PAYMENT_TO_HIDE_X"
- "CHANGE_DEFAULT_PHONE_TO_HIDE_X"
- "FACE_ID_REQUIRED_TO_OPEN_X"
- "PASSCODE_REQUIRED_TO_OPEN_X"
- "TOUCH_ID_REQUIRED_TO_OPEN_X"
- "XCTestConfigurationFilePath"
- "prefs:root=PASSCODE#CHANGE_PASSCODE"

```
