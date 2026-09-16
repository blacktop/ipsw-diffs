## ContinuitySing

> `/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing`

```diff

-764.22.13.0.0
-  __TEXT.__text: 0x5b55c
-  __TEXT.__objc_methlist: 0x3694
+764.40.4.122.1
+  __TEXT.__text: 0x5bc94
+  __TEXT.__objc_methlist: 0x36fc
   __TEXT.__const: 0xfb4
-  __TEXT.__gcc_except_tab: 0xb98
-  __TEXT.__cstring: 0x61b9
-  __TEXT.__oslogstring: 0x3389
+  __TEXT.__gcc_except_tab: 0xbb8
+  __TEXT.__cstring: 0x62f9
+  __TEXT.__oslogstring: 0x33f9
   __TEXT.__ustring: 0x2a
-  __TEXT.__swift5_typeref: 0x9f6
+  __TEXT.__swift5_typeref: 0x9fa
   __TEXT.__swift5_fieldmd: 0x378
   __TEXT.__constg_swiftt: 0x7a4
   __TEXT.__swift5_reflstr: 0x2da
-  __TEXT.__swift5_capture: 0x344
+  __TEXT.__swift5_capture: 0x374
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x58
   __TEXT.__swift5_types: 0x48

   __TEXT.__swift_as_cont: 0x120
   __TEXT.__swift5_assocty: 0xc8
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x1d98
+  __TEXT.__unwind_info: 0x1dc0
   __TEXT.__eh_frame: 0xf38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x16d0
-  __DATA_CONST.__objc_classlist: 0x2d0
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2af8
+  __DATA_CONST.__objc_selrefs: 0x2b20
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x9d8
-  __AUTH_CONST.__const: 0x1400
-  __AUTH_CONST.__cfstring: 0x2f00
-  __AUTH_CONST.__objc_const: 0x7320
+  __AUTH_CONST.__const: 0x1478
+  __AUTH_CONST.__cfstring: 0x2f20
+  __AUTH_CONST.__objc_const: 0x7408
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0xd70
-  __AUTH.__objc_data: 0x2118
+  __AUTH_CONST.__auth_got: 0xd78
+  __AUTH.__objc_data: 0x2168
   __AUTH.__data: 0x5b8
-  __DATA.__objc_ivar: 0x484
+  __DATA.__objc_ivar: 0x48c
   __DATA.__data: 0x9c8
   __DATA.__common: 0x68
   - /System/Library/Frameworks/AVKit.framework/AVKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1915
-  Symbols:   4138
-  CStrings:  946
+  Functions: 1931
+  Symbols:   4156
+  CStrings:  953
 
Symbols:
+ +[CSDismissOnboardingMessage messageID]
+ -[CSRemoteRequestClient dismissOnboardingHandler]
+ -[CSRemoteRequestClient setDismissOnboardingHandler:]
+ -[CSShieldManager _notifyDismissOnboarding]
+ -[CSShieldViewController _handleRemoteDismissOnboardingRequest]
+ -[CSShieldViewController shieldManagerDidReceiveDismissOnboardingRequest:]
+ GCC_except_table151
+ GCC_except_table157
+ GCC_except_table38
+ GCC_except_table45
+ GCC_except_table49
+ GCC_except_table65
+ GCC_except_table80
+ GCC_except_table83
+ _OBJC_CLASS_$_CSDismissOnboardingMessage
+ _OBJC_IVAR_$_CSRemoteRequestClient._dismissOnboardingHandler
+ _OBJC_IVAR_$_CSShieldViewController._onboardingFlowNavigationController
+ _OBJC_METACLASS_$_CSDismissOnboardingMessage
+ __OBJC_$_CLASS_METHODS_CSDismissOnboardingMessage
+ __OBJC_CLASS_RO_$_CSDismissOnboardingMessage
+ __OBJC_METACLASS_RO_$_CSDismissOnboardingMessage
+ ___43-[CSShieldManager _notifyDismissOnboarding]_block_invoke
+ ___62-[CSShieldManager _bootstrapRequestClientIfNeededAndAvailable]_block_invoke_6
+ _objc_msgSend$_handleRemoteDismissOnboardingRequest
+ _objc_msgSend$_notifyDismissOnboarding
+ _objc_msgSend$setDismissOnboardingHandler:
+ _objc_msgSend$shieldManagerDidReceiveDismissOnboardingRequest:
+ _swift_isEscapingClosureAtFileLocation
+ _symbolic Ig_
- GCC_except_table149
- GCC_except_table15
- GCC_except_table155
- GCC_except_table24
- GCC_except_table30
- GCC_except_table44
- GCC_except_table48
- GCC_except_table64
- GCC_except_table79
- GCC_except_table81
- ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_4
CStrings:
+ "%s: %@ Dismissing onboarding card for remote request"
+ "%s: Received continuity sing dismiss onboarding message %@"
+ "-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_2"
+ "-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_3"
+ "-[CSShieldViewController _handleRemoteDismissOnboardingRequest]"
+ "-[CSShieldViewController shieldManagerDidReceiveDismissOnboardingRequest:]"
+ "com.apple.ContinuitySing.dismissOnboarding"
+ "\xf0\xe1"
- "-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_4"
```
