## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x2bb98
+113.0.2.0.0
+  __TEXT.__text: 0x2beb0
   __TEXT.__objc_methlist: 0x1d1c
-  __TEXT.__const: 0xf8
-  __TEXT.__oslogstring: 0x46f3
-  __TEXT.__cstring: 0x2753
-  __TEXT.__gcc_except_tab: 0x86c
+  __TEXT.__const: 0x100
+  __TEXT.__oslogstring: 0x46a2
+  __TEXT.__cstring: 0x278f
+  __TEXT.__gcc_except_tab: 0x880
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x978
+  __TEXT.__unwind_info: 0x998
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1358
+  __DATA_CONST.__const: 0x13a8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0x558
   __DATA_CONST.__got: 0x4e0
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x1960
+  __AUTH_CONST.__cfstring: 0x1980
   __AUTH_CONST.__objc_const: 0x2030
   __AUTH_CONST.__objc_intobj: 0xb28
   __AUTH_CONST.__objc_arrayobj: 0x4e0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 851
-  Symbols:   2346
-  CStrings:  616
+  Functions: 854
+  Symbols:   2349
+  CStrings:  617
 
Symbols:
+ -[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles:]
+ -[DMCEnrollmentFlowController _waitForESSODeclarations:]
+ GCC_except_table165
+ GCC_except_table198
+ GCC_except_table202
+ GCC_except_table212
+ GCC_except_table219
+ GCC_except_table251
+ ___56-[DMCEnrollmentFlowController _waitForESSODeclarations:]_block_invoke
+ ___56-[DMCEnrollmentFlowController _waitForESSODeclarations:]_block_invoke_2
+ ___68-[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles:]_block_invoke
+ ___68-[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ _objc_msgSend$_extensionIDsFromDeclarationProfiles:
+ _objc_msgSend$_waitForESSODeclarations:
+ _objc_msgSend$essoDeclarationsWaitTimeoutWithDefaultValue:
- -[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles]
- -[DMCEnrollmentFlowController _waitForESSODeclarations]
- GCC_except_table189
- GCC_except_table199
- GCC_except_table206
- GCC_except_table213
- GCC_except_table248
- ___55-[DMCEnrollmentFlowController _waitForESSODeclarations]_block_invoke
- ___55-[DMCEnrollmentFlowController _waitForESSODeclarations]_block_invoke_2
- ___67-[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles]_block_invoke
- ___67-[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles]_block_invoke_2
- ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
- _objc_msgSend$_extensionIDsFromDeclarationProfiles
- _objc_msgSend$_waitForESSODeclarations
- _objc_msgSend$isAwaitingConfiguration
CStrings:
+ "wait_for_esso_declarations"
+ "wait_for_esso_declarations_queue"
- "Pending cloud config does not require await configuration. Do not preserve apps."
```
