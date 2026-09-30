## ContactsFlowUIPlugin

> `/System/Library/Snippets/UIPlugins/ContactsFlowUIPlugin.bundle/ContactsFlowUIPlugin`

```diff

-3405.9.1.0.0
-  __TEXT.__text: 0x1aa8
+3500.29.2.0.0
+  __TEXT.__text: 0x1be8
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__const: 0xf6
   __TEXT.__cstring: 0x51

   __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   __DATA.__common: 0x18
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/SiriContactsCommon.framework/SiriContactsCommon
   - /System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents
   - /System/Library/PrivateFrameworks/SiriContactsUI.framework/SiriContactsUI
   - /System/Library/PrivateFrameworks/SnippetUI.framework/SnippetUI
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
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
-  UUID: 0F44E52B-28C9-30F0-BE40-3766710CDBEE
-  Functions: 58
-  Symbols:   618
+  UUID: 421DB6BC-FBAB-3A82-92E2-2EA57050E26C
+  Functions: 57
+  Symbols:   601
   CStrings:  5
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swiftVideoToolbox_$_ContactsFlowUIPlugin
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ContactsFlowUIPlugin
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ContactsFlowUIPlugin
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ContactsFlowUIPlugin
- _OUTLINED_FUNCTION_21
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftDataDetection_$_ContactsFlowUIPlugin
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_ContactsFlowUIPlugin
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_ContactsFlowUIPlugin
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_ContactsFlowUIPlugin
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_ContactsFlowUIPlugin
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_ContactsFlowUIPlugin
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_ContactsFlowUIPlugin
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_ContactsFlowUIPlugin
Functions:
~ _$s20ContactsFlowUIPluginAAC7snippet3for4mode5idiom7SwiftUI7AnyViewV04SiriA6Common0A18SnippetPluginModelO_So7VRXModeVSo8VRXIdiomVtKF : 752 -> 872
~ _$s20ContactsFlowUIPluginAAC18makeGetContactView33_8A73C334608F2A23CF34B3B42D75E048LL3for7SwiftUI03AnyG0V04SiriA6Common0eF12SnippetModelV_tF : 1472 -> 1572
~ _$s20ContactsFlowUIPluginAAC27makeGetContactAttributeView33_8A73C334608F2A23CF34B3B42D75E048LL3for7SwiftUI03AnyH0V04SiriA6Common0efG12SnippetModelV_tF : 1472 -> 1572
~ _$s20ContactsFlowUIPluginAAC30makeModifyContactAttributeView33_8A73C334608F2A23CF34B3B42D75E048LL3for7SwiftUI03AnyH0V04SiriA6Common0efG12SnippetModelV_tF : 648 -> 672
+ _$sSo9CNContactC18thumbnailImageData10Foundation0D0VSgvgToTeob_
- _$sSo9CNContactC18thumbnailImageData10Foundation0D0VSgvgToTeob_
~ _OUTLINED_FUNCTION_0 : 48 -> 20
~ _OUTLINED_FUNCTION_4 : 16 -> 32
~ _OUTLINED_FUNCTION_5 : 36 -> 32
~ _OUTLINED_FUNCTION_6 : 36 -> 44
~ _OUTLINED_FUNCTION_7 : 32 -> 16
~ _OUTLINED_FUNCTION_8 : 44 -> 16
~ _OUTLINED_FUNCTION_9 : 28 -> 24
~ _OUTLINED_FUNCTION_10 : 12 -> 24
~ _OUTLINED_FUNCTION_11 : 16 -> 24
~ _OUTLINED_FUNCTION_12 : 16 -> 36
~ _OUTLINED_FUNCTION_13 : 24 -> 20
~ _OUTLINED_FUNCTION_14 : 12 -> 20
~ _OUTLINED_FUNCTION_17 : 20 -> 32

```
