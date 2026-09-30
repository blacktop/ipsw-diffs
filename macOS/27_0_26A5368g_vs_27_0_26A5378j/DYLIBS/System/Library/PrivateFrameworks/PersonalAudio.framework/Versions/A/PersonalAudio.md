## PersonalAudio

> `/System/Library/PrivateFrameworks/PersonalAudio.framework/Versions/A/PersonalAudio`

```diff

-  __TEXT.__text: 0x14960
-  __TEXT.__objc_methlist: 0xea0
+  __TEXT.__text: 0x14a68
+  __TEXT.__objc_methlist: 0xec0
   __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0x348
-  __TEXT.__cstring: 0x11d4
+  __TEXT.__cstring: 0x1204
   __TEXT.__oslogstring: 0xdf8
   __TEXT.__dlopen_cstrs: 0x11a
-  __TEXT.__unwind_info: 0x558
+  __TEXT.__unwind_info: 0x560
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe78
+  __DATA_CONST.__objc_selrefs: 0xe90
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x168
   __AUTH_CONST.__const: 0x850
-  __AUTH_CONST.__cfstring: 0x1480
-  __AUTH_CONST.__objc_const: 0x1088
+  __AUTH_CONST.__cfstring: 0x14a0
+  __AUTH_CONST.__objc_const: 0x1078
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0xb0
+  __DATA.__objc_ivar: 0xac
   __DATA.__data: 0xc0
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 415
-  Symbols:   1134
-  CStrings:  436
+  Functions: 418
+  Symbols:   1136
+  CStrings:  438
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[PADatabaseManager shouldExcludeStoreFromCloudBackup]
+ -[PASettings personalMediaAutomationSkipRouteCheck]
+ -[PASettings setPersonalMediaAutomationSkipRouteCheck:]
+ -[PAStimulus rampTowardTarget:]
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table234
+ GCC_except_table308
+ GCC_except_table323
+ GCC_except_table344
+ GCC_except_table387
+ GCC_except_table397
+ GCC_except_table400
+ GCC_except_table405
+ OBJC_IVAR_$_PAStimulus._state
+ ___31-[PAStimulus rampTowardTarget:]_block_invoke
+ ___block_descriptor_57_e8_32s_e5_v8?0l
+ _objc_msgSend$rampTowardTarget:
- -[PAStimulus rampVolumeUp:]
- GCC_except_table176
- GCC_except_table177
- GCC_except_table232
- GCC_except_table306
- GCC_except_table321
- GCC_except_table342
- GCC_except_table385
- GCC_except_table395
- GCC_except_table398
- GCC_except_table403
- OBJC_IVAR_$_PAStimulus._ramping
- OBJC_IVAR_$_PAStimulus._rampingUp
- ___27-[PAStimulus rampVolumeUp:]_block_invoke
- ___block_descriptor_41_e8_32s_e5_v8?0l
- _objc_msgSend$rampVolumeUp:
CStrings:
+ "PersonalMediaAutomationSkipRouteCheckPreference"

```
