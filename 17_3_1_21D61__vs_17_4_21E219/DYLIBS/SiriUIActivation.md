## SiriUIActivation

> `/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation`

```diff

-3302.13.3.1.1
-  __TEXT.__text: 0x15f7c
+3304.61.1.0.0
+  __TEXT.__text: 0x16110
   __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x1138
+  __TEXT.__objc_methlist: 0x1140
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x544
   __TEXT.__cstring: 0x2d72
-  __TEXT.__oslogstring: 0x2b7a
-  __TEXT.__unwind_info: 0x710
+  __TEXT.__oslogstring: 0x2b9a
+  __TEXT.__unwind_info: 0x718
   __TEXT.__objc_classname: 0x2ed
-  __TEXT.__objc_methname: 0x63f9
+  __TEXT.__objc_methname: 0x64fb
   __TEXT.__objc_methtype: 0x10bc
-  __TEXT.__objc_stubs: 0x4660
+  __TEXT.__objc_stubs: 0x46e0
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x858
+  __DATA_CONST.__const: 0x880
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2090
-  __DATA_CONST.__objc_selrefs: 0x1550
+  __DATA_CONST.__objc_const: 0x20d0
+  __DATA_CONST.__objc_selrefs: 0x1578
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x270
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__objc_const: 0x288
   __AUTH_CONST.__cfstring: 0x620

   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x3a8
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x270
-  __DATA.__objc_superrefs: 0x38
   __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x4e0
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 478
-  Symbols:   2069
-  CStrings:  1391
+  Functions: 479
+  Symbols:   2076
+  CStrings:  1397
 
Symbols:
+ -[SiriPresentationViewController siriViewControllerDidReactivateFromFlexibleFollowups]
+ GCC_except_table207
+ GCC_except_table214
+ GCC_except_table219
+ GCC_except_table230
+ GCC_except_table232
+ GCC_except_table234
+ _OBJC_CLASS_$_AFUICarPlayUtilities
+ ___73-[SiriPresentationViewController _clearSiriViewControllerWithCompletion:]_block_invoke.247
+ ___89-[SiriPresentationViewController handleButtonDownFromButtonIdentifier:timestamp:context:]_block_invoke.216
+ ___92-[SiriPresentationViewController _presentationDismissalRequestedWithOptions:withCompletion:]_block_invoke.210
+ ___92-[SiriPresentationViewController _presentationDismissalRequestedWithOptions:withCompletion:]_block_invoke.211
+ ___99-[SiriPresentationViewController _presentSiriViewControllerWithPresentationOptions:requestOptions:]_block_invoke.175
+ ___block_descriptor_56_e8_32s40bs48w_e20_v20?0B8"NSError"12lw48l8s32l8s40l8
+ __unnamed_array_storage.171
+ __unnamed_array_storage.172
+ __unnamed_array_storage.201
+ __unnamed_array_storage.202
+ __unnamed_array_storage.228
+ __unnamed_array_storage.229
+ __unnamed_array_storage.272
+ __unnamed_array_storage.273
+ _objc_msgSend$initWithDeactivationOptions:animated:requestCancellationReason:dismissalReason:
+ _objc_msgSend$setSupportsCarPlayVehicleData:
+ _objc_msgSend$siriRequestDidReactivateForSiriPresentation:
+ _objc_msgSend$supportsCarPlayVehicleData
- GCC_except_table205
- GCC_except_table213
- GCC_except_table218
- GCC_except_table229
- GCC_except_table231
- GCC_except_table233
- _OBJC_CLASS_$_AFUIStarkUtilities
- ___73-[SiriPresentationViewController _clearSiriViewControllerWithCompletion:]_block_invoke.244
- ___89-[SiriPresentationViewController handleButtonDownFromButtonIdentifier:timestamp:context:]_block_invoke.213
- ___92-[SiriPresentationViewController _presentationDismissalRequestedWithOptions:withCompletion:]_block_invoke.207
- ___92-[SiriPresentationViewController _presentationDismissalRequestedWithOptions:withCompletion:]_block_invoke.208
- ___99-[SiriPresentationViewController _presentSiriViewControllerWithPresentationOptions:requestOptions:]_block_invoke.172
- __unnamed_array_storage.168
- __unnamed_array_storage.169
- __unnamed_array_storage.198
- __unnamed_array_storage.199
- __unnamed_array_storage.225
- __unnamed_array_storage.226
- __unnamed_array_storage.269
- __unnamed_array_storage.270
CStrings:
+ "%s #activation #carPlay #carDnd #eyesFree isForStark: %@, carDNDStatus: %@, eyesFree: %@, supportsCarPlayVehicleData: %@"
+ "T@\"NSString\",?,R,C"
+ "initWithDeactivationOptions:animated:requestCancellationReason:dismissalReason:"
+ "setSupportsCarPlayVehicleData:"
+ "siriRequestDidReactivateForSiriPresentation:"
+ "siriViewControllerDidReactivateFromFlexibleFollowups"
+ "supportsCarPlayVehicleData"
- "%s #activation #carPlay #carDnd #eyesFree isForStark: %@, carDNDStatus: %@, eyesFree: %@"

```
