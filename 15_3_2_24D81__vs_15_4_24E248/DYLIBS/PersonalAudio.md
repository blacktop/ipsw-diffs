## PersonalAudio

> `/System/Library/PrivateFrameworks/PersonalAudio.framework/Versions/A/PersonalAudio`

```diff

-456.6.3.0.0
-  __TEXT.__text: 0x164a4
+456.8.7.0.0
+  __TEXT.__text: 0x16cf0
   __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0xc24
-  __TEXT.__const: 0xd8
+  __TEXT.__objc_methlist: 0xc78
+  __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x44c
-  __TEXT.__cstring: 0x203d
+  __TEXT.__cstring: 0x21f2
   __TEXT.__oslogstring: 0x246
   __TEXT.__dlopen_cstrs: 0x11a
   __TEXT.__unwind_info: 0x548
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x2a76
+  __TEXT.__objc_methname: 0x2b6a
   __TEXT.__objc_methtype: 0x3cc
-  __TEXT.__objc_stubs: 0x29a0
-  __DATA_CONST.__got: 0x168
+  __TEXT.__objc_stubs: 0x2a80
+  __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0x2e8
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xce8
+  __DATA_CONST.__objc_selrefs: 0xd20
   __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x1be0
-  __AUTH_CONST.__objc_const: 0xf50
+  __AUTH_CONST.__cfstring: 0x1dc0
+  __AUTH_CONST.__objc_const: 0xf28
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x98
+  __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0xc0
   __DATA.__bss: 0x168
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9650EF5-965E-36F0-9401-62FB657193DB
-  Functions: 412
-  Symbols:   1131
-  CStrings:  1099
+  UUID: 1BFBE9E4-D351-32FA-AF87-BAD6C9FDB8B4
+  Functions: 423
+  Symbols:   1155
+  CStrings:  1140
 
Symbols:
+ +[PAAccessoryManager sharedInstance].cold.1
+ +[PADatabaseManager sharedManager].cold.1
+ +[PAEnrollment sharedInstance].cold.1
+ +[PAHMSManager sharedInstance].cold.1
+ +[PASettings sharedInstance].cold.1
+ +[PAStimulus louderSinStimulus].cold.1
+ +[PAStimulus musicStimulus].cold.1
+ +[PAStimulus sinStimulus].cold.1
+ -[PAHMSManager hearingAidEnabledByAddress]
+ -[PAHMSManager setHearingAidEnabledByAddress:]
+ -[PASettings keysToSync].cold.1
+ -[PASettings preferenceKeyForSelector:].cold.1
+ OBJC_IVAR_$_PAHMSManager._hearingAidEnabledByAddress
+ _OBJC_CLASS_$_NSConstantArray
+ __39-[PAHMSManager setupHearingModeService]_block_invoke.22
+ __block_literal_global.109
+ __block_literal_global.25
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$additionalInfoForPrefenceUpdate
+ _objc_msgSend$hearingAidEnabledByAddress
+ _objc_msgSend$numberWithChar:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$setHearingAidEnabledByAddress:
+ _objc_msgSend$tone
+ initHMDeviceConfigurations.cold.1
+ initHMServiceClient.cold.1
- __39-[PAHMSManager setupHearingModeService]_block_invoke.19
- __block_literal_global.22
- __block_literal_global.95
CStrings:
+ "%@%@"
+ "-[PAHMSManager hearingAidEnabledForAddress:]_block_invoke"
+ "-[PAHMSManager toggleHearingAidForAddress:]_block_invoke"
+ "Found hearing aid enabled [%@, %@] for %@"
+ "Ignoring config update %d, %d"
+ "Preset dictionary is missing information %@"
+ "Preset dictionary was missing information %@"
+ "Setting hearing aid enabled [%@] for %@"
+ "T@\"NSMutableDictionary\",&,N,V_hearingAidEnabledByAddress"
+ "_UpdateInfo"
+ "_hearingAidEnabledByAddress"
+ "addEntriesFromDictionary:"
+ "additionalInfoForPrefenceUpdate"
+ "hearingAidEnabledByAddress"
+ "loss_01_dBHL"
+ "loss_02_dBHL"
+ "loss_03_dBHL"
+ "loss_04_dBHL"
+ "loss_05_dBHL"
+ "loss_06_dBHL"
+ "loss_07_dBHL"
+ "loss_08_dBHL"
+ "numberWithChar:"
+ "removeObjectsForKeys:"
+ "setHearingAidEnabledByAddress:"
+ "tone"

```
