## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/Versions/A/HearingUtilities`

```diff

-  __TEXT.__text: 0x8e04c
-  __TEXT.__objc_methlist: 0x6ec4
+  __TEXT.__text: 0x8e444
+  __TEXT.__objc_methlist: 0x6ecc
   __TEXT.__const: 0x6b4
   __TEXT.__dlopen_cstrs: 0x3ed
   __TEXT.__constg_swiftt: 0x110

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0xd4
-  __TEXT.__cstring: 0x4b3b
+  __TEXT.__cstring: 0x4b8f
   __TEXT.__swift5_capture: 0x1a8
-  __TEXT.__oslogstring: 0xc69b
-  __TEXT.__gcc_except_tab: 0x1c88
-  __TEXT.__unwind_info: 0x20d8
+  __TEXT.__oslogstring: 0xc99b
+  __TEXT.__gcc_except_tab: 0x1c94
+  __TEXT.__unwind_info: 0x20e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40c8
+  __DATA_CONST.__objc_selrefs: 0x40d0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x2a0
-  __DATA_CONST.__got: 0x578
-  __AUTH_CONST.__const: 0x3c90
-  __AUTH_CONST.__cfstring: 0x47e0
+  __DATA_CONST.__got: 0x580
+  __AUTH_CONST.__const: 0x3cc0
+  __AUTH_CONST.__cfstring: 0x4820
   __AUTH_CONST.__objc_const: 0x8ed8
   __AUTH_CONST.__objc_intobj: 0x648
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x838
-  __AUTH.__objc_data: 0x788
-  __AUTH.__data: 0x78
+  __AUTH.__objc_data: 0x640
+  __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x774
-  __DATA.__data: 0xc00
-  __DATA.__bss: 0x508
-  __DATA_DIRTY.__objc_data: 0x9b0
-  __DATA_DIRTY.__bss: 0x110
+  __DATA.__data: 0xb60
+  __DATA.__bss: 0x4e8
+  __DATA_DIRTY.__objc_data: 0xaf8
+  __DATA_DIRTY.__data: 0xc8
+  __DATA_DIRTY.__bss: 0x130
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3122
-  Symbols:   6780
-  CStrings:  2205
+  Functions: 3123
+  Symbols:   6783
+  CStrings:  2218
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_capture : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
Symbols:
+ -[HUComfortSoundsController scheduleFileWithRetryCount:]
+ GCC_except_table2646
+ GCC_except_table2654
+ GCC_except_table2663
+ GCC_except_table2672
+ GCC_except_table2675
+ GCC_except_table2737
+ GCC_except_table2743
+ GCC_except_table2747
+ GCC_except_table2820
+ GCC_except_table2853
+ ___56-[HUComfortSoundsController scheduleFileWithRetryCount:]_block_invoke
+ ___56-[HUComfortSoundsController scheduleFileWithRetryCount:]_block_invoke_2
+ ___block_descriptor_41_e8_32s_e35_v32?0"AXHearingAidDevice"8Q16^B24l
+ _objc_msgSend$scheduleFileWithRetryCount:
+ _objc_msgSend$stringByAppendingString:
- GCC_except_table2644
- GCC_except_table2653
- GCC_except_table2662
- GCC_except_table2671
- GCC_except_table2674
- GCC_except_table2736
- GCC_except_table2742
- GCC_except_table2746
- GCC_except_table2819
- GCC_except_table2852
- ___41-[HUComfortSoundsController scheduleFile]_block_invoke
- ___41-[HUComfortSoundsController scheduleFile]_block_invoke_2
- _objc_msgSend$isRunning
Functions:
~ -[AXHearingAidDeviceController pairedHearingAidsDidChange] : 2188 -> 2708
~ ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke : 212 -> 448
~ _HearingAidsSendTooManyDisconnectionNotificationForDevice : 328 -> 336
~ _HearingAidsSendTooManyReconnectionFailsNotificationForDevice : 292 -> 284
~ _HearingAidsSendRemovedPairingInfoNotificationForDevice : 292 -> 300
~ -[HUComfortSoundsController scheduleFile] : 1028 -> 8
+ -[HUComfortSoundsController scheduleFileWithRetryCount:]
CStrings:
+ "CentralManager: No peripherals with IDs, unpairing %@"
+ "Error playing node: %@"
+ "Error starting engine (attempt %ld): %@"
+ "HearingAidDevice: Set Paired=YES"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Adding to Loaded and Available device: %@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Adding to persistent device: %@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Available devices:\n%@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Created device for persistent representation\n%@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Found device for persistent representation\n%@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, No peripheral IDs %@, unpairing persistent device\n%@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Persistent devices:\n%@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, isFromiCloud: %d, keepDevicePaired: %d"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, match peripheral IDs, set Paired=YES to connected device: %@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, no peripheral IDs, Disconnecting and Unpairing connected device: %@"
+ "HearingAidTooManyDisconnectionAlertDescription_Generic"
+ "HearingAidTooManyDisconnectionAlertTitle_Generic"
+ "Max retries (%d) reached starting engine: %@. Stopping."
+ "_Generic"
- "CentralManager: No peripherals with identifiers, unpairing %@"
- "Error starting engine %@"
- "HearingAidDevice: Set isPaired to YES"
- "HearingAidDeviceController: pairedHearingAidsDidChange \nPersistent device: %@,\n%@"
- "HearingAidDeviceController: pairedHearingAidsDidChange, No peripheral identifiers %@, unpairing persistent device\n%@"
- "HearingAidDeviceController: pairedHearingAidsDidChange, Updating Persistent/Loaded/Available with device\n%@"
- "HearingAidDeviceGenericLabel"

```
