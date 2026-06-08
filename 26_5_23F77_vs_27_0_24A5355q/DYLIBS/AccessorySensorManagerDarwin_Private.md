## AccessorySensorManagerDarwin_Private

> `/System/Library/PrivateFrameworks/AccessorySensorManagerDarwin_Private.framework/AccessorySensorManagerDarwin_Private`

```diff

-11.28.0.0.0
-  __TEXT.__text: 0x3e0
-  __TEXT.__auth_stubs: 0x110
-  __TEXT.__objc_methlist: 0xd4
+20.26.0.0.1
+  __TEXT.__text: 0xb38
+  __TEXT.__objc_methlist: 0x134
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x6e
-  __TEXT.__unwind_info: 0x88
-  __TEXT.__objc_classname: 0x44
-  __TEXT.__objc_methname: 0x1e5
-  __TEXT.__objc_methtype: 0x7b
-  __TEXT.__objc_stubs: 0x40
-  __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x48
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__cstring: 0x25c
+  __TEXT.__unwind_info: 0xb8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x90
+  __DATA_CONST.__objc_selrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__got: 0x18
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__objc_const: 0x2d8
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x18
+  __AUTH_CONST.__objc_const: 0x430
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x70
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AccessorySensorManagerDefines_Private.framework/AccessorySensorManagerDefines_Private
   - /System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/AccessorySensorManagerServices
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E6847645-78AB-3537-8D91-71E3068EF367
-  Functions: 20
-  Symbols:   101
-  CStrings:  40
+  UUID: FF5A68F3-A05A-3E98-88EE-2E65499E2D31
+  Functions: 30
+  Symbols:   164
+  CStrings:  18
 
Symbols:
+ -[ASMPowerAssertion .cxx_destruct]
+ -[ASMPowerAssertion _resetTimer]
+ -[ASMPowerAssertion _resetTimer].cold.1
+ -[ASMPowerAssertion acquireAssertion]
+ -[ASMPowerAssertion initWithAssertionName:timeout:]
+ -[ASMPowerAssertion invalidate]
+ -[ASMPowerAssertion releaseAssertion]
+ -[ASMPowerAssertion withAssertion:]
+ GCC_except_table2
+ GCC_except_table4
+ _CUDispatchTimerSet
+ _IOPMAssertionDeclareSystemActivity
+ _IOPMAssertionRelease
+ _LogPrintF_safe
+ _OBJC_CLASS_$_ASMPowerAssertion
+ _OBJC_IVAR_$_ASMPowerAssertion._assertionActive
+ _OBJC_IVAR_$_ASMPowerAssertion._assertionID
+ _OBJC_IVAR_$_ASMPowerAssertion._assertionName
+ _OBJC_IVAR_$_ASMPowerAssertion._refCount
+ _OBJC_IVAR_$_ASMPowerAssertion._timeout
+ _OBJC_IVAR_$_ASMPowerAssertion._timeoutTimer
+ _OBJC_METACLASS_$_ASMPowerAssertion
+ __LogCategory_Initialize
+ __OBJC_$_INSTANCE_METHODS_ASMPowerAssertion
+ __OBJC_$_INSTANCE_VARIABLES_ASMPowerAssertion
+ __OBJC_CLASS_RO_$_ASMPowerAssertion
+ __OBJC_METACLASS_RO_$_ASMPowerAssertion
+ __Unwind_Resume
+ ___32-[ASMPowerAssertion _resetTimer]_block_invoke
+ ___37-[ASMPowerAssertion acquireAssertion]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___objc_personality_v0
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_get_global_queue
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _gLogCategory_ASMPowerAssertion
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_resetTimer
+ _objc_msgSend$acquireAssertion
+ _objc_msgSend$copy
+ _objc_msgSend$releaseAssertion
+ _objc_release_x22
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x8
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_terminate
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "-[ASMPowerAssertion _resetTimer]"
+ "-[ASMPowerAssertion acquireAssertion]"
+ "-[ASMPowerAssertion releaseAssertion]"
+ "ASMPowerAssertion"
+ "Acquired power assertion '%@' (id=%u, sleepReverted=%s)"
+ "Acquiring power assertion '%@' (refCount=%lu)"
+ "Auto-releasing power assertion '%@' after %.1fs timeout"
+ "IOPMAssertionDeclareSystemActivity failed: %d"
+ "IOPMAssertionRelease failed: %d"
+ "Released power assertion '%@' (id=%u)"
+ "Releasing power assertion '%@' (refCount=%lu)"
+ "com.apple.AccessorySensorManager"
+ "no"
+ "yes"
- ".cxx_destruct"
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@16@0:8"
- "@?"
- "@?16@0:8"
- "ASMImageProcessingHelper"
- "ASMPolarisResourceProvider"
- "B"
- "T@\"ASMSignpost\",R,N"
- "T@\"NSObject<OS_os_log>\",&,N,V_asmLogInstance"
- "T@?,C,N,V_resourceStartHandler"
- "T@?,C,N,V_resourceStopHandler"
- "_activateCalled"
- "_activateWithExecutionSession:"
- "_asmLogInstance"
- "_currentResourceKeys"
- "_dispatchQueue"
- "_resourceStartHandler"
- "_resourceStopHandler"
- "activateWithExecutionSession:"
- "asmLogInstance"
- "asmSignpostLogger"
- "init"
- "invalidate"
- "resourceStartHandler"
- "resourceStopHandler"
- "setAsmLogInstance:"
- "setResourceStartHandler:"
- "setResourceStopHandler:"
- "sharedInstance"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"

```
