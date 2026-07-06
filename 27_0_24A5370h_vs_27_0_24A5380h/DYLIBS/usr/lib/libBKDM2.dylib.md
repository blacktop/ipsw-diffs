## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

```diff

-  __TEXT.__text: 0x7bae0
-  __TEXT.__objc_methlist: 0x5d24
-  __TEXT.__const: 0xd7a8
-  __TEXT.__cstring: 0x6f88
-  __TEXT.__oslogstring: 0x45af
-  __TEXT.__gcc_except_tab: 0x1758
+  __TEXT.__text: 0x7c434
+  __TEXT.__objc_methlist: 0x5d2c
+  __TEXT.__const: 0xd7b8
+  __TEXT.__cstring: 0x703d
+  __TEXT.__oslogstring: 0x465c
+  __TEXT.__gcc_except_tab: 0x177c
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0xdf8
+  __TEXT.__unwind_info: 0xe10
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1580
+  __DATA_CONST.__const: 0x15e8
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d20
+  __DATA_CONST.__objc_selrefs: 0x3d28
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x4a8
   __DATA_CONST.__got: 0x448
-  __AUTH_CONST.__const: 0xbe8
-  __AUTH_CONST.__cfstring: 0x64e0
-  __AUTH_CONST.__objc_const: 0x98c8
+  __AUTH_CONST.__const: 0xc08
+  __AUTH_CONST.__cfstring: 0x65a0
+  __AUTH_CONST.__objc_const: 0x9948
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__auth_got: 0x728
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0xaa0
-  __DATA.__data: 0x898
-  __DATA.__bss: 0x80
-  __DATA_DIRTY.__objc_data: 0x410
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0xab0
+  __DATA.__data: 0x880
+  __DATA.__bss: 0x49
+  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA_DIRTY.__data: 0x14
   __DATA_DIRTY.__common: 0x40
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2884
-  Symbols:   8709
-  CStrings:  2401
+  Functions: 2895
+  Symbols:   8742
+  CStrings:  2419
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
Symbols:
+ +[BLHelper deviceModelString]
+ GCC_except_table218
+ GCC_except_table228
+ GCC_except_table237
+ GCC_except_table241
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table260
+ GCC_except_table262
+ GCC_except_table263
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._secureFaceDetectMatchRetryType
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._secureFaceDetectMessagingQueue
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._secureFaceDetectPeriocularMatchState
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._secureFaceDetectRestartAfterStop
+ _OUTLINED_FUNCTION_59
+ ___29+[BLHelper deviceModelString]_block_invoke
+ ___52-[BiometricKitXPCServerPearl processCoachingStatus:]_block_invoke
+ ___66-[BiometricKitXPCServerPearl processMetadataObjects:fromCameraID:]_block_invoke
+ ___66-[BiometricKitXPCServerPearl processMetadataObjects:fromCameraID:]_block_invoke_2
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_84_e8_32s_e5_v8?0ls32l8
+ _deviceModelString.modelString
+ _deviceModelString.onceToken
+ _objc_msgSend$deviceModelString
- GCC_except_table213
- GCC_except_table232
- GCC_except_table236
- GCC_except_table239
- GCC_except_table242
- GCC_except_table248
- GCC_except_table249
- GCC_except_table255
- GCC_except_table257
- GCC_except_table258
CStrings:
+ "Enroll"
+ "FaceDetect"
+ "HWModelStr"
+ "Match"
+ "Unknown"
+ "_avcStartStopQueue"
+ "_secureFaceDetectInterruptionDispatchSource"
+ "_secureFaceDetectMessagingQueue"
+ "com.apple.pearld.sfdMessaging"
+ "device_model"
+ "processSecureFaceDetectRequestMessage: start:<%{public}@> sequenceNumber:%u matchRetryType:%u periocularMatchState:0x%x\n"
+ "stopSecureFaceDetect: trying to restart after stop\n"

```
