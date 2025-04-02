## IntentsCore

> `/System/Library/PrivateFrameworks/IntentsCore.framework/Versions/A/IntentsCore`

```diff

-3506.0.1.0.0
-  __TEXT.__text: 0x123a4
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0xe3c
+3601.0.0.0.0
+  __TEXT.__text: 0x124d0
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0xe44
   __TEXT.__const: 0x90
   __TEXT.__dlopen_cstrs: 0x16a
   __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__cstring: 0x1a64
+  __TEXT.__cstring: 0x1a58
   __TEXT.__oslogstring: 0x13c2
-  __TEXT.__unwind_info: 0x428
+  __TEXT.__unwind_info: 0x420
   __TEXT.__objc_classname: 0x30b
-  __TEXT.__objc_methname: 0x385f
+  __TEXT.__objc_methname: 0x38c7
   __TEXT.__objc_methtype: 0x7a2
-  __TEXT.__objc_stubs: 0x2ca0
-  __DATA_CONST.__got: 0x368
+  __TEXT.__objc_stubs: 0x2d40
+  __DATA_CONST.__got: 0x370
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc0
+  __DATA_CONST.__objc_selrefs: 0xde8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__const: 0x9f0
-  __AUTH_CONST.__cfstring: 0x5a0
+  __AUTH_CONST.__cfstring: 0x5c0
   __AUTH_CONST.__objc_const: 0x1ec0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 373
-  Symbols:   1289
-  CStrings:  941
+  Symbols:   1294
+  CStrings:  945
 
Symbols:
+ +[INCExtensionProxy _errorAggregation:innerError:]
+ AssistantServicesLibraryCore.frameworkLibrary.686
+ _NSMultipleUnderlyingErrorsKey
+ __52-[INCAppLaunchRequest performWithCompletionHandler:]_block_invoke.56
+ __52-[INCAppLaunchRequest performWithCompletionHandler:]_block_invoke.57
+ __55-[INCExtensionProxy handleIntentWithCompletionHandler:]_block_invoke.50
+ __55-[INCExtensionProxy handleIntentWithCompletionHandler:]_block_invoke.52
+ __56-[INCExtensionProxy confirmIntentWithCompletionHandler:]_block_invoke.37
+ __64-[INCExtensionProxy resolveIntentSlotKeyPath:completionHandler:]_block_invoke.25
+ __65-[INCExtensionProxy resolveIntentSlotKeyPaths:completionHandler:]_block_invoke.33
+ __AssistantServicesLibraryCore_block_invoke.687
+ __Block_byref_object_copy_.459
+ __Block_byref_object_copy_.674
+ __Block_byref_object_dispose_.460
+ __Block_byref_object_dispose_.675
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e42_v16?0"INIntentForwardingActionResponse"8l
+ ___getAFIsPersistentSiriAvailableSymbolLoc_block_invoke
+ __block_literal_global.567
+ __block_literal_global.60
+ __getAFIsPersistentSiriAvailableSymbolLoc_block_invoke.685
+ _objc_msgSend$_code
+ _objc_msgSend$_errorAggregation:innerError:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$underlyingErrors
+ audit_stringAssistantServices.689
+ getAFIsPersistentSiriAvailableSymbolLoc.ptr
+ getAFIsPersistentSiriAvailableSymbolLoc.ptr.684
- AssistantServicesLibraryCore.frameworkLibrary.678
- __52-[INCAppLaunchRequest performWithCompletionHandler:]_block_invoke.58
- __52-[INCAppLaunchRequest performWithCompletionHandler:]_block_invoke.59
- __55-[INCExtensionProxy handleIntentWithCompletionHandler:]_block_invoke.46
- __55-[INCExtensionProxy handleIntentWithCompletionHandler:]_block_invoke.47
- __56-[INCExtensionProxy confirmIntentWithCompletionHandler:]_block_invoke.34
- __64-[INCExtensionProxy resolveIntentSlotKeyPath:completionHandler:]_block_invoke.24
- __65-[INCExtensionProxy resolveIntentSlotKeyPaths:completionHandler:]_block_invoke.30
- __AssistantServicesLibraryCore_block_invoke.679
- __Block_byref_object_copy_.457
- __Block_byref_object_copy_.667
- __Block_byref_object_dispose_.458
- __Block_byref_object_dispose_.668
- ___block_descriptor_64_e8_32s40s48bs56bs_e42_v16?0"INIntentForwardingActionResponse"8l
- ___copy_helper_block_e8_32s40s48b56b
- ___getAFDeviceSupportsSystemAssistantExperienceSymbolLoc_block_invoke
- __block_literal_global.56
- __block_literal_global.569
- __getAFDeviceSupportsSystemAssistantExperienceSymbolLoc_block_invoke.676
- __os_feature_enabled_impl
- audit_stringAssistantServices.681
- getAFDeviceSupportsSystemAssistantExperienceSymbolLoc.ptr
- getAFDeviceSupportsSystemAssistantExperienceSymbolLoc.ptr.675
CStrings:
+ "AFIsPersistentSiriAvailable"
+ "IntentResponseCodeDomain"
+ "_code"
+ "_errorAggregation:innerError:"
+ "arrayByAddingObject:"
+ "initWithDomain:code:userInfo:"
+ "underlyingErrors"
- "AFDeviceSupportsSystemAssistantExperience"
- "SiriUI"
- "persistent_siri"

```
