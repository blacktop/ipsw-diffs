## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/A/AuthKitUI`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__dlopen_cstrs`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-554.0.0.0.0
-  __TEXT.__text: 0x113ff4
-  __TEXT.__objc_methlist: 0xbfc8
-  __TEXT.__const: 0xf84
-  __TEXT.__gcc_except_tab: 0xc0c
+555.0.0.0.0
+  __TEXT.__text: 0x1168f0
+  __TEXT.__objc_methlist: 0xc060
+  __TEXT.__const: 0x11a4
   __TEXT.__cstring: 0x68bb
+  __TEXT.__oslogstring: 0x5dd9
+  __TEXT.__gcc_except_tab: 0xc0c
   __TEXT.__dlopen_cstrs: 0x1d1
-  __TEXT.__oslogstring: 0x5ca9
   __TEXT.__ustring: 0x28
-  __TEXT.__constg_swiftt: 0x434
-  __TEXT.__swift5_typeref: 0xa08
-  __TEXT.__swift5_fieldmd: 0x224
-  __TEXT.__swift5_reflstr: 0x18b
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_capture: 0x184
+  __TEXT.__constg_swiftt: 0x4ac
+  __TEXT.__swift5_typeref: 0xa8e
+  __TEXT.__swift5_fieldmd: 0x278
+  __TEXT.__swift5_reflstr: 0x1ab
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_assocty: 0x120
+  __TEXT.__swift5_capture: 0x1bc
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x84
-  __TEXT.__swift5_types: 0x40
+  __TEXT.__swift5_proto: 0x9c
+  __TEXT.__swift5_types: 0x4c
   __TEXT.__swift_as_entry: 0x80
   __TEXT.__swift_as_ret: 0x80
   __TEXT.__swift_as_cont: 0xd0
-  __TEXT.__unwind_info: 0x2918
+  __TEXT.__unwind_info: 0x2998
   __TEXT.__eh_frame: 0x10f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1aa0
-  __DATA_CONST.__objc_classlist: 0x500
+  __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x2d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x70d0
+  __DATA_CONST.__objc_selrefs: 0x7180
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0xeb8
-  __AUTH_CONST.__const: 0x1e98
+  __DATA_CONST.__got: 0xed0
+  __AUTH_CONST.__const: 0x1fe0
   __AUTH_CONST.__cfstring: 0x56e0
-  __AUTH_CONST.__objc_const: 0x1e748
+  __AUTH_CONST.__objc_const: 0x1e800
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0xd80
-  __AUTH.__objc_data: 0x2b50
-  __AUTH.__data: 0x488
-  __DATA.__objc_ivar: 0xd74
-  __DATA.__data: 0x2560
-  __DATA.__bss: 0x1248
+  __AUTH_CONST.__auth_got: 0xdc8
+  __AUTH.__objc_data: 0x2c00
+  __AUTH.__data: 0x4b8
+  __DATA.__objc_ivar: 0xd80
+  __DATA.__data: 0x25c0
+  __DATA.__bss: 0x1548
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x690
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4494
-  Symbols:   10523
-  CStrings:  1446
+  Functions: 4549
+  Symbols:   10581
+  CStrings:  1450
 
Symbols:
+ +[AKIcon monogramWithAppName:size:]
+ -[AKAuthorizationInputPaneViewController _accountDisplayNameForFirstParty]
+ -[AKAuthorizationInputPaneViewController _handleRequestedAuthorization:error:completionHandler:]
+ -[AKAuthorizationRVSWindowController windowDidLoad]
+ -[AKAuthorizationSubPaneConfirmButton _updateAuthorizationButtonEnabledState]
+ -[AKAuthorizationSubPaneConfirmButton authorizationInProgress]
+ -[AKAuthorizationSubPaneConfirmButton finishAuthorizationInProgress]
+ -[AKAuthorizationSubPaneConfirmButton setAuthorizationInProgress:]
+ -[AKIcon _initWithSynthesizedImage:]
+ GCC_except_table125
+ GCC_except_table19
+ OBJC_IVAR_$_AKAuthorizationSubPaneConfirmButton._authorizationAllowed
+ OBJC_IVAR_$_AKAuthorizationSubPaneConfirmButton._authorizationInProgress
+ OBJC_IVAR_$_AKIcon._synthesizedImage
+ _NSFontDescriptorSystemDesignRounded
+ _NSWorkspaceWillPowerOffNotification
+ _OBJC_CLASS_$_AKAuthorizationLoginChoice
+ _OBJC_CLASS_$_AKMonogramRenderer
+ _OBJC_METACLASS_$_AKMonogramRenderer
+ __67-[AKAuthorizationSubPaneConfirmButton _performPasscodeValidations:]_block_invoke
+ __96-[AKAuthorizationInputPaneViewController _handleRequestedAuthorization:error:completionHandler:]_block_invoke
+ __CLASS_METHODS_AKMonogramRenderer
+ __DATA_AKMonogramRenderer
+ __INSTANCE_METHODS_AKMonogramRenderer
+ __METACLASS_DATA_AKMonogramRenderer
+ ___91-[AKAuthorizationInputPaneViewController passwordAuthenticationCompletedWithResults:error:]_block_invoke
+ ___96-[AKAuthorizationInputPaneViewController _handleRequestedAuthorization:error:completionHandler:]_block_invoke
+ ___os_log_helper_16_2_2_8_0_8_64
+ ___swift_memcpy16_8
+ __swift_closure_destructor.45Tm
+ _associated conformance So21NSAttributedStringKeyaSHSCSQ
+ _associated conformance So21NSAttributedStringKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So21NSAttributedStringKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$_accountDisplayNameForFirstParty
+ _objc_msgSend$_handleRequestedAuthorization:error:completionHandler:
+ _objc_msgSend$_initWithSynthesizedImage:
+ _objc_msgSend$_updateAuthorizationButtonEnabledState
+ _objc_msgSend$authorizationInProgress
+ _objc_msgSend$drawAtPoint:
+ _objc_msgSend$finishAuthorizationInProgress
+ _objc_msgSend$fontDescriptor
+ _objc_msgSend$fontDescriptorWithDesign:
+ _objc_msgSend$imageWithSize:flipped:drawingHandler:
+ _objc_msgSend$initWithUser:site:
+ _objc_msgSend$monogramImageForTitle:size:
+ _objc_msgSend$monogramWithAppName:size:
+ _objc_msgSend$notificationCenter
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$setAppleIDAuth:
+ _objc_msgSend$setAuthorizationInProgress:
+ _objc_msgSend$setCreateAppleID:
+ _objc_msgSend$setFill
+ _objc_msgSend$setTitleVisibility:
+ _objc_msgSend$styleMask
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic So8NSStringC
+ _symbolic _____ 12CoreGraphics7CGFloatV
+ _symbolic _____ 9AuthKitUI18AKMonogramRendererC
+ _symbolic _____ So21NSAttributedStringKeya
+ _symbolic _____ So6CGSizeV
+ _symbolic ______ypt So21NSAttributedStringKeya
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC So21NSAttributedStringKeya
+ _symbolic _____y_____ypG s18_DictionaryStorageC So21NSAttributedStringKeya
+ _type_layout_string So21NSAttributedStringKeya
+ _type_layout_string So6CGSizeV
- GCC_except_table120
- GCC_except_table16
- __97-[AKAuthorizationInputPaneViewController _performAuthorizationWithRawPassword:completionHandler:]_block_invoke
- ___97-[AKAuthorizationInputPaneViewController _performAuthorizationWithRawPassword:completionHandler:]_block_invoke_2
- __swift_closure_destructor.41Tm
- _objc_msgSend$isPasscodeAuthorizationInProcess
- _objc_msgSend$setIsPasscodeAuthorizationInProcess:
CStrings:
+ "6"
+ "AKAuthorizationPasswordAuthenticationViewController authenticateWithContext completion fired. self=%p error=%@"
+ "Password authentication presenting in window."
+ "Password authorization already in progress, ignoring repeat activation."
+ "performPasswordAuthenticationForPaneViewController: allocated password VC"
- "5"
```
