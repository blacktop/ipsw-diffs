## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-  __TEXT.__text: 0x2f498
-  __TEXT.__objc_methlist: 0x30d4
+  __TEXT.__text: 0x2f744
+  __TEXT.__objc_methlist: 0x30fc
   __TEXT.__const: 0x1a8
   __TEXT.__dlopen_cstrs: 0x118
   __TEXT.__gcc_except_tab: 0x3ac
-  __TEXT.__oslogstring: 0x545a
-  __TEXT.__cstring: 0x5db4
+  __TEXT.__oslogstring: 0x54d8
+  __TEXT.__cstring: 0x5dd1
   __TEXT.__unwind_info: 0xd98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1df0
+  __DATA_CONST.__objc_selrefs: 0x1e08
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x2e8
   __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x2e80
-  __AUTH_CONST.__objc_const: 0x5318
+  __AUTH_CONST.__cfstring: 0x2ea0
+  __AUTH_CONST.__objc_const: 0x5338
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x438
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x4f8
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x4fc
   __DATA.__data: 0x5d0
   __DATA.__bss: 0x1b0
-  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1236
-  Symbols:   4273
-  CStrings:  1419
+  Functions: 1240
+  Symbols:   4285
+  CStrings:  1423
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[SCDAAssistantPreferences myriadForceInstrumentationEnabled]
+ -[SCDAPreferences forceInstrumentationEnabled]
+ -[SCDARecord isAnOutgoing]
+ GCC_except_table1013
+ GCC_except_table1034
+ GCC_except_table1098
+ GCC_except_table1129
+ GCC_except_table1141
+ GCC_except_table1216
+ GCC_except_table1217
+ GCC_except_table1223
+ GCC_except_table241
+ GCC_except_table247
+ GCC_except_table505
+ GCC_except_table734
+ GCC_except_table780
+ GCC_except_table849
+ GCC_except_table864
+ GCC_except_table915
+ GCC_except_table922
+ GCC_except_table949
+ GCC_except_table993
+ _OBJC_IVAR_$_SCDACoordinator._forceInstrumentationEnabled
+ ___61-[SCDAAssistantPreferences myriadForceInstrumentationEnabled]_block_invoke
+ _objc_msgSend$forceInstrumentationEnabled
+ _objc_msgSend$isAnOutgoing
+ _objc_msgSend$myriadForceInstrumentationEnabled
- GCC_except_table1010
- GCC_except_table1031
- GCC_except_table1095
- GCC_except_table1123
- GCC_except_table1138
- GCC_except_table1212
- GCC_except_table1213
- GCC_except_table1219
- GCC_except_table240
- GCC_except_table246
- GCC_except_table502
- GCC_except_table731
- GCC_except_table777
- GCC_except_table846
- GCC_except_table861
- GCC_except_table909
- GCC_except_table919
- GCC_except_table946
- GCC_except_table990
Functions:
~ -[SCDACoordinator instrumentationUpdateBoost:value:] : 128 -> 136
~ -[SCDACoordinator _enterState:] : 3600 -> 3688
~ -[SCDACoordinator _readDefaults] : 744 -> 800
+ -[SCDARecord isAnEmergencyHandled]
+ -[SCDAAssistantPreferences myriadForceInstrumentationEnabled]
+ ___52-[SCDAAssistantPreferences disableMyriadBLEActivity]_block_invoke
~ -[SCDACoordinator initWithDelegate:] : 2824 -> 2788
~ ___68-[SCDACoordinator startWatchAdvertisingFromVoiceTriggerWithContext:]_block_invoke : 744 -> 756
~ ___51-[SCDACoordinator startAdvertisingFromInEarTrigger]_block_invoke : 316 -> 456
+ -[SCDAPreferences recencyBoostDecayInterval]
CStrings:
+ "%s #scda Not attempting / applying watch threshold boost because rebalance is enabled. rawAudioGoodnessScore: %u"
+ "%s BTLE trumping from in ear voice trigger"
+ "%s Skipping continuation loop: trigger was outgoing/self"
+ "%s Unexpectedly lowering goodness score %du for in ear trigger"
+ "Myriad Force Instrumentation"
- "%s #scda Not attempting / applying watch threshold boost because rebalance is enabled."
- "%s BTLE in-ear trigger entering election with default goodness"

```
