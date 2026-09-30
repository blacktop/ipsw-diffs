## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/Versions/A/DMCEnrollmentLibrary`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x2a280
+113.0.2.0.0
+  __TEXT.__text: 0x2a654
   __TEXT.__objc_methlist: 0x1adc
-  __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x3f36
-  __TEXT.__cstring: 0x2464
-  __TEXT.__gcc_except_tab: 0x774
+  __TEXT.__const: 0xf8
+  __TEXT.__oslogstring: 0x3f11
+  __TEXT.__cstring: 0x24af
+  __TEXT.__gcc_except_tab: 0x788
   __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__unwind_info: 0x8e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ad0
+  __DATA_CONST.__objc_selrefs: 0x1ae0
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x548
-  __DATA_CONST.__got: 0x470
-  __AUTH_CONST.__const: 0x1030
-  __AUTH_CONST.__cfstring: 0x1820
+  __DATA_CONST.__got: 0x478
+  __AUTH_CONST.__const: 0x10c0
+  __AUTH_CONST.__cfstring: 0x1860
   __AUTH_CONST.__objc_const: 0x1c20
   __AUTH_CONST.__objc_intobj: 0xb28
   __AUTH_CONST.__objc_arrayobj: 0x4e0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x118
   __DATA.__objc_ivar: 0x168
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x1f0
-  __DATA_DIRTY.__objc_data: 0x1b8
+  __DATA_DIRTY.__objc_data: 0x2d0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 811
-  Symbols:   2134
-  CStrings:  558
+  Functions: 816
+  Symbols:   2147
+  CStrings:  561
 
Symbols:
+ -[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles:]
+ -[DMCEnrollmentFlowController _waitForESSODeclarations:]
+ GCC_except_table191
+ GCC_except_table228
+ GCC_except_table231
+ GCC_except_table245
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table283
+ _DMCHangTracerDirectory
+ _OBJC_CLASS_$_DMCBacktraceLogger
+ __96-[DMCEnrollmentFlowController _installESSODeclarations:chosenBundleID:personaID:enrollmentType:]_block_invoke
+ __96-[DMCEnrollmentFlowController _installESSODeclarations:chosenBundleID:personaID:enrollmentType:]_block_invoke_2
+ ___56-[DMCEnrollmentFlowController _waitForESSODeclarations:]_block_invoke
+ ___56-[DMCEnrollmentFlowController _waitForESSODeclarations:]_block_invoke_2
+ ___68-[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles:]_block_invoke
+ ___68-[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48r
+ ___destroy_helper_block_e8_32s40s48r
+ _dispatch_queue_create
+ _objc_msgSend$_extensionIDsFromDeclarationProfiles:
+ _objc_msgSend$_waitForESSODeclarations:
+ _objc_msgSend$dumpStackshotToPath:fileName:
+ _objc_msgSend$essoDeclarationsWaitTimeoutWithDefaultValue:
+ _objc_msgSend$stringByAppendingString:
- -[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles]
- -[DMCEnrollmentFlowController _waitForESSODeclarations]
- GCC_except_table215
- GCC_except_table218
- GCC_except_table221
- GCC_except_table232
- GCC_except_table239
- GCC_except_table273
- ___55-[DMCEnrollmentFlowController _waitForESSODeclarations]_block_invoke
- ___55-[DMCEnrollmentFlowController _waitForESSODeclarations]_block_invoke_2
- ___67-[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles]_block_invoke
- ___67-[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles]_block_invoke_2
- ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16l
- _objc_msgSend$_extensionIDsFromDeclarationProfiles
- _objc_msgSend$_waitForESSODeclarations
- _objc_msgSend$isAwaitingConfiguration
CStrings:
+ "Task %s hasn't finished within %.1f seconds"
+ "_stackshot.ips"
+ "wait_for_esso_declarations"
+ "wait_for_esso_declarations_queue"
- "Pending cloud config does not require await configuration. Do not preserve apps."
```
