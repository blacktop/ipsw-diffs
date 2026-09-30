## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3510.4.2.0.0
-  __TEXT.__text: 0x4f468
+3510.7.1.1.2
+  __TEXT.__text: 0x4f830
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x607c
+  __TEXT.__objc_methlist: 0x60a4
   __TEXT.__const: 0x838
-  __TEXT.__cstring: 0xa14d
-  __TEXT.__oslogstring: 0x6e87
+  __TEXT.__cstring: 0xa1ad
+  __TEXT.__oslogstring: 0x6f5b
   __TEXT.__gcc_except_tab: 0xe5c
   __TEXT.__dlopen_cstrs: 0x1bc
   __TEXT.__swift5_typeref: 0x102

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x1608
+  __TEXT.__unwind_info: 0x1610
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x101d
-  __TEXT.__objc_methname: 0xde24
+  __TEXT.__objc_methname: 0xdf0e
   __TEXT.__objc_methtype: 0x23c9
   __TEXT.__objc_stubs: 0x95c0
   __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0x1670
+  __DATA_CONST.__const: 0x1678
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e28
+  __DATA_CONST.__objc_selrefs: 0x2e40
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a0
-  __DATA_CONST.__objc_arraydata: 0x530
+  __DATA_CONST.__objc_arraydata: 0x540
   __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x5e8
-  __AUTH_CONST.__cfstring: 0x49c0
-  __AUTH_CONST.__objc_const: 0x9cd0
-  __AUTH_CONST.__objc_intobj: 0x960
+  __AUTH_CONST.__cfstring: 0x49e0
+  __AUTH_CONST.__objc_const: 0x9d00
+  __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x1c28
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x674
+  __DATA.__objc_ivar: 0x678
   __DATA.__data: 0xf98
   __DATA.__bss: 0x510
   __DATA_DIRTY.__objc_data: 0x4b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E1BEED92-0CED-3D23-860B-EEA80B383692
-  Functions: 2173
-  Symbols:   7440
-  CStrings:  4556
+  UUID: 58DF4F11-5232-3457-A8A3-98E5CBA8A9A0
+  Functions: 2176
+  Symbols:   7447
+  CStrings:  4567
 
Symbols:
+ -[SASPresentationManager modelExistsForPresentationIdentifier:]
+ -[SiriActivationService pendingSystemAssistantActivationRequest]
+ -[SiriActivationService setPendingSystemAssistantActivationRequest:]
+ _OBJC_IVAR_$_SiriActivationService._pendingSystemAssistantActivationRequest
+ ___block_literal_global.585
+ ___block_literal_global.590
- ___block_literal_global.579
- ___block_literal_global.584
CStrings:
+ "%s  #activation _shouldRejectActivationWithButtonIdentifier - isBlockableButton:%d assertionsAvailable :%d isButtonActivationAllowedBySystemAssistant:%d"
+ "%s #activation dismissing Siri for System assistant request"
+ "%s #activation request is off and we have a pending System Assistant activation %@"
+ "%s Model %@ exists? %@"
+ "-[SASPresentationManager modelExistsForPresentationIdentifier:]"
+ "SystemAssistantActivationRequest"
+ "T@\"SASActivationRequest\",&,N,V_pendingSystemAssistantActivationRequest"
+ "_pendingSystemAssistantActivationRequest"
+ "modelExistsForPresentationIdentifier:"
+ "pendingSystemAssistantActivationRequest"
+ "setPendingSystemAssistantActivationRequest:"
- "%s  #activation _shouldRejectActivationWithButtonIdentifier - isBlockableButton:%d assertionsAvailable :%d"

```
