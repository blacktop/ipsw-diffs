## AppSSOUI

> `/System/Library/PrivateFrameworks/AppSSOUI.framework/AppSSOUI`

```diff

-417.120.4.0.0
-  __TEXT.__text: 0xddc
-  __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_methlist: 0x25c
-  __TEXT.__const: 0xa8
-  __TEXT.__oslogstring: 0xc1
-  __TEXT.__cstring: 0x1ae
-  __TEXT.__unwind_info: 0xb0
-  __TEXT.__objc_classname: 0x6c
-  __TEXT.__objc_methname: 0x664
-  __TEXT.__objc_methtype: 0x24c
-  __TEXT.__objc_stubs: 0x360
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x48
+483.0.6.0.1
+  __TEXT.__text: 0x1744
+  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__objc_methlist: 0x274
+  __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0x10
+  __TEXT.__oslogstring: 0x1b4
+  __TEXT.__cstring: 0x263
+  __TEXT.__dlopen_cstrs: 0x52
+  __TEXT.__unwind_info: 0xd8
+  __TEXT.__objc_classname: 0x6d
+  __TEXT.__objc_methname: 0x75d
+  __TEXT.__objc_methtype: 0x269
+  __TEXT.__objc_stubs: 0x420
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__objc_selrefs: 0x250
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x108
+  __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__objc_const: 0x300
+  __AUTH_CONST.__cfstring: 0x20
+  __AUTH_CONST.__objc_const: 0x340
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_ivar: 0x14
   __DATA.__data: 0x120
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E1C6CE0E-067A-316B-90F5-7EF3D1C4C22D
-  Functions: 23
-  Symbols:   154
-  CStrings:  127
+  UUID: C56C696E-44C0-36DA-BFFE-6A0CF22B9392
+  Functions: 38
+  Symbols:   221
+  CStrings:  153
 
Symbols:
+ -[SOUIAuthorizationViewController dealloc]
+ -[SOUIAuthorizationViewController initWithExtensionViewController:hints:presentViewControllerCompletion:]
+ -[SOUIAuthorizationViewController initWithExtensionViewController:hints:presentViewControllerCompletion:].cold.1
+ -[SOUIAuthorizationViewController loadView].cold.1
+ -[SOUIAuthorizationViewController loadView].cold.2
+ -[SOUIAuthorizationViewController viewDidAppear:].cold.1
+ GCC_except_table4
+ _AppSSOCoreLibraryCore.frameworkLibrary
+ _NSRunLoopCommonModes
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_IVAR_$_SOUIAuthorizationViewController._presentViewControllerCompletionBlock
+ _OBJC_IVAR_$_SOUIAuthorizationViewController._presentViewControllerTimer
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __Block_object_dispose
+ __Unwind_Resume
+ ___105-[SOUIAuthorizationViewController initWithExtensionViewController:hints:presentViewControllerCompletion:]_block_invoke
+ ___105-[SOUIAuthorizationViewController initWithExtensionViewController:hints:presentViewControllerCompletion:]_block_invoke.3
+ ___105-[SOUIAuthorizationViewController initWithExtensionViewController:hints:presentViewControllerCompletion:]_block_invoke.cold.1
+ ___105-[SOUIAuthorizationViewController initWithExtensionViewController:hints:presentViewControllerCompletion:]_block_invoke.cold.2
+ ___AppSSOCoreLibraryCore_block_invoke
+ ___CFConstantStringClassReference
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSTimer"8ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___getSOErrorHelperClass_block_invoke
+ ___getSOErrorHelperClass_block_invoke.cold.1
+ ___objc_personality_v0
+ __dispatch_main_q
+ __os_log_error_impl
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringAppSSOCore
+ _dispatch_async
+ _free
+ _getSOErrorHelperClass.softClass
+ _objc_getClass
+ _objc_msgSend$addTimer:forMode:
+ _objc_msgSend$initWithExtensionViewController:hints:presentViewControllerCompletion:
+ _objc_msgSend$internalErrorWithMessage:
+ _objc_msgSend$invalidate
+ _objc_msgSend$mainRunLoop
+ _objc_msgSend$timerWithTimeInterval:repeats:block:
+ _objc_release_x25
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainBlock
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x8
CStrings:
+ "%s"
+ "-[SOUIAuthorizationViewController dealloc]"
+ "-[SOUIAuthorizationViewController initWithExtensionViewController:hints:presentViewControllerCompletion:]"
+ "1"
+ "@\"NSTimer\""
+ "@40@0:8@16@24@?32"
+ "SOErrorHelper"
+ "Unable to find class %s"
+ "_presentViewControllerCompletionBlock"
+ "_presentViewControllerTimer"
+ "addTimer:forMode:"
+ "added child extension view controller: %{public}@"
+ "adding child extension view controller: %{public}@"
+ "dealloc"
+ "initWithExtensionViewController:hints:presentViewControllerCompletion:"
+ "internalErrorWithMessage:"
+ "invalidate"
+ "mainRunLoop"
+ "presentation timer invoked"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore"
+ "starting presentation timer"
+ "stopping presentation timer"
+ "timed out presenting extension view controller"
+ "timed out presenting extension view controller: %{public}@"
+ "timerWithTimeInterval:repeats:block:"
+ "v16@?0@\"NSTimer\"8"
- "-[SOUIAuthorizationViewController initWithExtensionViewController:hints:]"

```
