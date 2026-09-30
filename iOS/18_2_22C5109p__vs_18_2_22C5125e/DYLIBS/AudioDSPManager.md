## AudioDSPManager

> `/System/Library/PrivateFrameworks/AudioDSPManager.framework/AudioDSPManager`

```diff

-139.324.0.0.0
-  __TEXT.__text: 0x5a62c
-  __TEXT.__auth_stubs: 0x1170
+139.327.0.0.0
+  __TEXT.__text: 0x5b7c0
+  __TEXT.__auth_stubs: 0x11a0
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x160
-  __TEXT.__gcc_except_tab: 0x55cc
+  __TEXT.__gcc_except_tab: 0x5658
   __TEXT.__const: 0x49e8
-  __TEXT.__cstring: 0x400a
-  __TEXT.__oslogstring: 0x27b2
+  __TEXT.__cstring: 0x3ddb
+  __TEXT.__oslogstring: 0x283a
   __TEXT.__dlopen_cstrs: 0xbf
-  __TEXT.__unwind_info: 0x1ce8
+  __TEXT.__unwind_info: 0x1d38
   __TEXT.__objc_classname: 0x60
   __TEXT.__objc_methname: 0x87e
   __TEXT.__objc_methtype: 0x38dd

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x8d0
+  __AUTH_CONST.__auth_got: 0x8e8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3c58
+  __AUTH_CONST.__const: 0x3c70
   __AUTH_CONST.__cfstring: 0xae0
   __AUTH_CONST.__objc_const: 0x7f8
   __AUTH.__objc_data: 0x50

   __DATA.__data: 0x184
   __DATA.__crash_info: 0x40
   __DATA.__cf_except_bt: 0x2000
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x138
+  __DATA_DIRTY.__bss: 0x140
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1403
-  Symbols:   1810
-  CStrings:  972
+  Functions: 1414
+  Symbols:   1824
+  CStrings:  978
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _os_signpost_enabled
+ _printf
CStrings:
+ "/AppleInternal/Library/BuildRoots/be0cfc50-9601-11ef-b65f-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "/AppleInternal/Library/BuildRoots/be0cfc50-9601-11ef-b65f-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/boost/exception/detail/exception_ptr.hpp"
+ "/Library/Caches/com.apple.xbs/Binaries/AudioDSPManager/install/TempContent/Objects/AudioDSPManager.build/AudioDSPManager.build/DerivedSources/AudioDSPController_C.c"
+ "ADM::Adapt"
+ "ADM::GetControllerEK"
+ "ADM::Negotiate"
+ "ADM::Simulate"
+ "ADM::TBCall::IOStarting"
+ "ADM::TBCall::IOStopped"
+ "ADM::TBCall::PrepareForIO"
+ "ADM::TBCall::Unconfigure"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
- "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "/AppleInternal/Library/BuildRoots/be5905ba-8b8c-11ef-a962-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/boost/exception/detail/exception_ptr.hpp"
- "TB_ASSERT: (audiodsputility_orientationparametervalue__decode(message, &val->values.orientation.field0) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.OrientationParameterValue\""
- "TB_ASSERT: (audiodsputility_parametererror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.ParameterError\""
- "TB_ASSERT: (audiodsputility_parametervalue__decode(message, &result->value.success) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.ParameterValue\""
- "TB_ASSERT: (audiodsputility_processerror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.ProcessError\""
- "TB_ASSERT: (audiodsputility_setuperror__decode(message, &result->value.failure) == TB_ERROR_SUCCESS) && \"failed to decode type: AudioDSPUtility.SetupError\""
- "compiling line %!l(MISSING)u - %!(BADPREC)%!s(MISSING)"

```
