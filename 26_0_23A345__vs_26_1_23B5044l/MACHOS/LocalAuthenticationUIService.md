## LocalAuthenticationUIService

> `/Applications/LocalAuthenticationUIService.app/LocalAuthenticationUIService`

```diff

-2005.0.61.0.0
-  __TEXT.__text: 0x7487c
-  __TEXT.__auth_stubs: 0x2090
-  __TEXT.__objc_stubs: 0x6420
-  __TEXT.__objc_methlist: 0x434c
+2005.40.31.0.0
+  __TEXT.__text: 0x74a2c
+  __TEXT.__auth_stubs: 0x20b0
+  __TEXT.__objc_stubs: 0x6440
+  __TEXT.__objc_methlist: 0x435c
   __TEXT.__const: 0x2de4
   __TEXT.__objc_classname: 0xa31
-  __TEXT.__objc_methname: 0x9621
+  __TEXT.__objc_methname: 0x9616
   __TEXT.__objc_methtype: 0x2660
-  __TEXT.__gcc_except_tab: 0x908
+  __TEXT.__gcc_except_tab: 0x928
   __TEXT.__cstring: 0x382c
   __TEXT.__oslogstring: 0x24ee
   __TEXT.__swift5_typeref: 0x3496

   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x1ee8
+  __TEXT.__unwind_info: 0x1f00
   __TEXT.__eh_frame: 0x6d0
-  __DATA_CONST.__auth_got: 0x1058
+  __DATA_CONST.__auth_got: 0x1068
   __DATA_CONST.__got: 0xb10
   __DATA_CONST.__auth_ptr: 0x7f0
   __DATA_CONST.__const: 0x3728

   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_intobj: 0x4e0
-  __DATA.__objc_const: 0xeb68
-  __DATA.__objc_selrefs: 0x27d0
-  __DATA.__objc_ivar: 0x358
+  __DATA.__objc_const: 0xeb88
+  __DATA.__objc_selrefs: 0x27d8
+  __DATA.__objc_ivar: 0x35c
   __DATA.__objc_data: 0x2a58
   __DATA.__data: 0x31c0
   __DATA.__bss: 0x1fe0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F5AB6D7A-E42F-3410-92D4-ED437D2392BC
-  Functions: 2902
-  Symbols:   23053
-  CStrings:  2812
+  UUID: 73A58D7C-9D8E-39EA-ACDD-3B66195AFE77
+  Functions: 2904
+  Symbols:   23068
+  CStrings:  2813
 
Symbols:
+ -[FaceIdToastViewController _didAppear]
+ GCC_except_table10
+ GCC_except_table105
+ GCC_except_table22
+ GCC_except_table72
+ GCC_except_table96
+ OBJC_IVAR_$_FaceIdToastViewController._appeared
+ OBJC_IVAR_$_FaceIdToastViewController._secureUIFinishedBlocks
+ _$s25LocalAuthenticationCoreUI28LACUIAngelConnectionListenerC16listenerProvider7managerACSo016LACXPCConnectionG9Providing_p_AA0E8Managing_ptcfc
+ _$s25LocalAuthenticationCoreUI36LACUIAngelConnectionListenerProviderC10domainName015protocolServiceJ0ACSS_SStcfc
+ _$s25LocalAuthenticationCoreUI36LACUIAngelConnectionListenerProviderCMa
+ ___76-[FaceIdToastViewController _dispatchDismissCompletionAfterSecureUIFinished]_block_invoke
+ __block_literal_global.143
+ _objc_msgSend$_didAppear
+ _objc_msgSend$initWithObjects:
- GCC_except_table103
- GCC_except_table15
- GCC_except_table21
- GCC_except_table48
- GCC_except_table9
- GCC_except_table94
- OBJC_IVAR_$_FaceIdToastViewController._didDismissAfterSecureUIFinishedBlock
- _$s25LocalAuthenticationCoreUI28LACUIAngelConnectionListenerC10domainName015protocolServiceI07managerACSS_SSAA0E8Managing_ptcfc
- __block_literal_global.142
- _objc_msgSend$presentingViewController
Functions:
~ -[TransitionViewController _setupConnection] : 1104 -> 1128
~ -[FaceIdToastViewController viewDidAppear:] : 536 -> 504
+ -[FaceIdToastViewController _didAppear]
~ -[FaceIdToastViewController dispatchBlockAfterDidAppear:] : 152 -> 120
~ -[FaceIdToastViewController _shrinkAndRevokeWithCompletion:] : 908 -> 984
~ -[FaceIdToastViewController _dispatchDismissCompletionAfterSecureUIFinished] : 112 -> 204
+ ___76-[FaceIdToastViewController _dispatchDismissCompletionAfterSecureUIFinished]_block_invoke
~ -[FaceIdToastViewController presentableDidAppearAsBanner:] : 624 -> 592
~ _$s28LocalAuthenticationUIService12AppContainerC8assembleyyF : 1004 -> 1044
CStrings:
+ "Face ID glyph did appear"
+ "_didAppear"
+ "_secureUIFinishedBlocks"
+ "initWithObjects:"
- "Face ID glyph will appear"
- "_didDismissAfterSecureUIFinishedBlock"
- "presentingViewController"

```
