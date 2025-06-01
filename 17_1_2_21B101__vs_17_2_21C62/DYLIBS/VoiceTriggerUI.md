## VoiceTriggerUI

> `/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`

```diff

-3301.9.1.1.1
-  __TEXT.__text: 0x37e78
+3302.6.2.0.0
+  __TEXT.__text: 0x3846c
   __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x2ef0
+  __TEXT.__objc_methlist: 0x2f50
   __TEXT.__const: 0x654
   __TEXT.__gcc_except_tab: 0x504
-  __TEXT.__cstring: 0x442d
-  __TEXT.__oslogstring: 0x1acd
+  __TEXT.__cstring: 0x453f
+  __TEXT.__oslogstring: 0x1b1e
   __TEXT.__unwind_info: 0xb40
-  __TEXT.__objc_classname: 0x718
-  __TEXT.__objc_methname: 0xb5b8
-  __TEXT.__objc_methtype: 0x2954
-  __TEXT.__objc_stubs: 0x7140
+  __TEXT.__objc_classname: 0x725
+  __TEXT.__objc_methname: 0xb79a
+  __TEXT.__objc_methtype: 0x299b
+  __TEXT.__objc_stubs: 0x7180
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x7f0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9320
-  __DATA_CONST.__objc_selrefs: 0x2310
+  __DATA_CONST.__objc_const: 0x9710
+  __DATA_CONST.__objc_selrefs: 0x2338
   __DATA_CONST.__objc_arraydata: 0x350
   __AUTH_CONST.__cfstring: 0x2440
   __AUTH_CONST.__const: 0xc0

   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__auth_got: 0x360
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_classrefs: 0x3e0
+  __DATA.__objc_classrefs: 0x3e8
   __DATA.__objc_superrefs: 0x100
-  __DATA.__objc_ivar: 0x52c
-  __DATA.__data: 0x8b0
+  __DATA.__objc_ivar: 0x534
+  __DATA.__data: 0x910
   __DATA.__bss: 0x51
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
+  - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriUI.framework/SiriUI
   - /System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C5FB7BA8-7EB8-3133-AF4F-EBF38DDD820C
-  Functions: 1115
-  Symbols:   4330
-  CStrings:  2975
+  UUID: 153F21D7-76C8-34EB-94B0-BE5334198A48
+  Functions: 1123
+  Symbols:   4359
+  CStrings:  3003
 
Symbols:
+ -[VTUIEnrollTrainingViewController scdaCoordinator]
+ -[VTUIEnrollTrainingViewController scdaShouldAbortAnotherDeviceBetter:]
+ -[VTUIEnrollTrainingViewController scdaShouldContinue:]
+ -[VTUIEnrollTrainingViewController setScdaCoordinator:]
+ -[VTUIProximityEnrollTrainingViewController scdaCoordinator]
+ -[VTUIProximityEnrollTrainingViewController scdaShouldAbortAnotherDeviceBetter:]
+ -[VTUIProximityEnrollTrainingViewController scdaShouldContinue:]
+ -[VTUIProximityEnrollTrainingViewController setScdaCoordinator:]
+ GCC_except_table128
+ GCC_except_table139
+ GCC_except_table153
+ GCC_except_table158
+ _OBJC_CLASS_$_SCDACoordinator
+ _OBJC_IVAR_$_VTUIEnrollTrainingViewController._scdaCoordinator
+ _OBJC_IVAR_$_VTUIProximityEnrollTrainingViewController._scdaCoordinator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SCDADelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SCDADelegate
+ __OBJC_$_PROTOCOL_REFS_SCDADelegate
+ __OBJC_LABEL_PROTOCOL_$_SCDADelegate
+ __OBJC_PROTOCOL_$_SCDADelegate
+ ___68-[VTUIEnrollTrainingViewController _processIntroViewContinueAction:]_block_invoke.273
+ ___97-[VTUIProximityEnrollTrainingViewController _showTrainingInstruction:afterDelay:isRetry:animate:]_block_invoke.149
+ ___97-[VTUIProximityEnrollTrainingViewController _showTrainingInstruction:afterDelay:isRetry:animate:]_block_invoke.151
+ ___97-[VTUIProximityEnrollTrainingViewController _showTrainingInstruction:afterDelay:isRetry:animate:]_block_invoke_2.150
+ __unnamed_array_storage.291
+ __unnamed_array_storage.297
+ _objc_msgSend$isSCDAFrameworkEnabled
+ _objc_msgSend$scdaCoordinator
- GCC_except_table126
- GCC_except_table135
- GCC_except_table151
- GCC_except_table154
- ___68-[VTUIEnrollTrainingViewController _processIntroViewContinueAction:]_block_invoke.272
- ___97-[VTUIProximityEnrollTrainingViewController _showTrainingInstruction:afterDelay:isRetry:animate:]_block_invoke.148
- ___97-[VTUIProximityEnrollTrainingViewController _showTrainingInstruction:afterDelay:isRetry:animate:]_block_invoke.150
- ___97-[VTUIProximityEnrollTrainingViewController _showTrainingInstruction:afterDelay:isRetry:animate:]_block_invoke_2.149
- __unnamed_array_storage.289
- __unnamed_array_storage.295
CStrings:
+ "\x01\x14\"\x11\x17\x11$G\x11"
+ "\x01\x14$\x13\x18\x11\x11\"I"
+ "%s #scda abort ignored during training"
+ "%s #scda continue ignored during training"
+ "-[VTUIEnrollTrainingViewController scdaShouldAbortAnotherDeviceBetter:]"
+ "-[VTUIEnrollTrainingViewController scdaShouldContinue:]"
+ "-[VTUIProximityEnrollTrainingViewController scdaShouldAbortAnotherDeviceBetter:]"
+ "-[VTUIProximityEnrollTrainingViewController scdaShouldContinue:]"
+ "@\"SCDACoordinator\""
+ "SCDADelegate"
+ "T@\"SCDACoordinator\",&,N,V_scdaCoordinator"
+ "_scdaCoordinator"
+ "isSCDAFrameworkEnabled"
+ "scdaAdvertisingDidBegin:"
+ "scdaAdvertisingDidEnd:"
+ "scdaAdvertisingWillBeginWithDelay:advertisingInterval:"
+ "scdaCoordinator"
+ "scdaCoordinatorDidHandleEmergency:"
+ "scdaCoordinatorWillHandleEmergency:"
+ "scdaListeningDidBegin:"
+ "scdaListeningDidEnd:"
+ "scdaShouldAbortAnotherDeviceBetter:"
+ "scdaShouldContinue:"
+ "scdaShouldHandleEmergency:"
+ "scdaShouldUnduck:"
+ "scdaWillEndSession:"
+ "scdaWillStartWithSession:"
+ "setScdaCoordinator:"
+ "v24@0:8@\"SCDACoordinator\"16"
+ "v24@0:8@\"SCDASession\"16"
- "\x01\x14\"\x11\x17\x11$F\x11"
- "\x01\x14$\x13\x18\x11\x11\"H"

```
