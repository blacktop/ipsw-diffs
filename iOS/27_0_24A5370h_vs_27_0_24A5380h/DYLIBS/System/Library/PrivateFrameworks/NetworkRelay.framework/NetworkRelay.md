## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

```diff

-  __TEXT.__text: 0x78998
-  __TEXT.__objc_methlist: 0x1f1c
+  __TEXT.__text: 0x78c1c
+  __TEXT.__objc_methlist: 0x1f4c
   __TEXT.__const: 0x240
   __TEXT.__gcc_except_tab: 0xb48
-  __TEXT.__cstring: 0xfec4
+  __TEXT.__cstring: 0xffbd
   __TEXT.__oslogstring: 0x13a9
-  __TEXT.__unwind_info: 0x9e8
+  __TEXT.__unwind_info: 0x9f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xce8
+  __DATA_CONST.__const: 0xd10
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1088
+  __DATA_CONST.__objc_selrefs: 0x10a8
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x1f8
-  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__got: 0x280
   __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x5080
-  __AUTH_CONST.__objc_const: 0x50f0
+  __AUTH_CONST.__cfstring: 0x5120
+  __AUTH_CONST.__objc_const: 0x5150
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x548
-  __DATA.__data: 0x208
+  __DATA.__objc_ivar: 0x550
+  __DATA.__data: 0x1f8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x280
-  __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA.__bss: 0x268
+  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__data: 0x20
+  __DATA_DIRTY.__bss: 0xf8
   __DATA_DIRTY.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1041
-  Symbols:   3684
-  CStrings:  2599
+  Functions: 1046
+  Symbols:   3698
+  CStrings:  2612
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ -[NRDeviceMeshParticipantInfo isCurrentRouteThroughPrimaryAssistDevice]
+ -[NRDeviceMeshParticipantInfo setIsCurrentRouteThroughPrimaryAssistDevice:]
+ -[NRDevicePreferences quickRelayPresence]
+ -[NRDevicePreferences setQuickRelayPresence:]
+ GCC_except_table128
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table277
+ GCC_except_table332
+ GCC_except_table357
+ GCC_except_table450
+ GCC_except_table461
+ GCC_except_table697
+ GCC_except_table710
+ GCC_except_table714
+ GCC_except_table718
+ GCC_except_table724
+ GCC_except_table728
+ GCC_except_table732
+ GCC_except_table736
+ GCC_except_table759
+ GCC_except_table762
+ GCC_except_table771
+ GCC_except_table773
+ GCC_except_table775
+ GCC_except_table782
+ GCC_except_table784
+ GCC_except_table835
+ GCC_except_table837
+ GCC_except_table852
+ _OBJC_IVAR_$_NRDeviceMeshParticipantInfo._isCurrentRouteThroughPrimaryAssistDevice
+ _OBJC_IVAR_$_NRDevicePreferences._internalQuickRelayPresence
+ _createStringFromNRQuickRelayPresence
+ _nrXPCKeyDevicePreferencesQuickRelayPresence
+ _objc_msgSend$isCurrentRouteThroughPrimaryAssistDevice
+ _objc_msgSend$setIsCurrentRouteThroughPrimaryAssistDevice:
- GCC_except_table122
- GCC_except_table135
- GCC_except_table137
- GCC_except_table274
- GCC_except_table329
- GCC_except_table354
- GCC_except_table445
- GCC_except_table456
- GCC_except_table692
- GCC_except_table700
- GCC_except_table709
- GCC_except_table713
- GCC_except_table719
- GCC_except_table723
- GCC_except_table727
- GCC_except_table731
- GCC_except_table754
- GCC_except_table757
- GCC_except_table761
- GCC_except_table768
- GCC_except_table770
- GCC_except_table772
- GCC_except_table774
- GCC_except_table830
- GCC_except_table832
- GCC_except_table847
CStrings:
+ "%s%.30s:%-4d %@ setting quick relay presence from %@ to %@"
+ "-[NRDevicePreferences setQuickRelayPresence:]"
+ "DevicePreferencesQuickRelayPresence"
+ "NRMeshParticipantInfo[appID=%@ primaryAssistCapable=%@ selectedAsPrimaryAssist=%@ currentRouteThroughPrimaryAssist=%@]"
+ "invalid"
+ "isCurrentRouteThroughPrimaryAssistDevice"
+ "offline"
+ "online"
+ "unknown"
- "NRMeshParticipantInfo[appID=%@ primaryAssistCapable=%@ selectedAsPrimaryAssist=%@]"

```
