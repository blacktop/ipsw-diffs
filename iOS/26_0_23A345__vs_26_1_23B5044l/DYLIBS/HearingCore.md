## HearingCore

> `/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore`

```diff

-495.0.0.0.0
-  __TEXT.__text: 0x79d8
-  __TEXT.__auth_stubs: 0x7a0
+496.2.0.0.0
+  __TEXT.__text: 0x7650
+  __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_methlist: 0x7b8
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0xd39
-  __TEXT.__oslogstring: 0x1e9
-  __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__cstring: 0xa8e
+  __TEXT.__oslogstring: 0x341
+  __TEXT.__gcc_except_tab: 0x130
+  __TEXT.__unwind_info: 0x358
   __TEXT.__objc_classname: 0x80
   __TEXT.__objc_methname: 0x17c5
   __TEXT.__objc_methtype: 0x2f3

   __DATA_CONST.__objc_selrefs: 0x720
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0xdc0
+  __AUTH_CONST.__cfstring: 0xca0
   __AUTH_CONST.__objc_const: 0x988
   __AUTH_CONST.__objc_dictobj: 0x28
   __DATA.__objc_ivar: 0x64
-  __DATA.__common: 0x10
-  __DATA.__bss: 0x139
+  __DATA.__bss: 0x181
   __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__common: 0x40
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F23C387-8431-350F-AF91-62570BEAD100
-  Functions: 277
-  Symbols:   1136
-  CStrings:  603
+  UUID: F9CF5806-E494-31E5-A49D-15F3CEDB845F
+  Functions: 280
+  Symbols:   1135
+  CStrings:  581
 
Symbols:
+ +[HCUtilities deviceIsMultiUser].cold.1
+ -[HCDatabaseManager setupDatabase].cold.1
+ -[HCXPCMessage hasEntitlement:].cold.1
+ _HCLogAudioAccommodations
+ _HCLogAudioAccommodations.__logObj
+ _HCLogAudioAccommodations.cold.1
+ _HCLogAudioAccommodations.onceToken
+ _HCLogComfortSounds
+ _HCLogComfortSounds.__logObj
+ _HCLogComfortSounds.cold.1
+ _HCLogComfortSounds.onceToken
+ _HCLogHearing
+ _HCLogHearing.__logObj
+ _HCLogHearing.cold.1
+ _HCLogHearing.onceToken
+ _HCLogHearingAids
+ _HCLogHearingAids.__logObj
+ _HCLogHearingAids.cold.1
+ _HCLogHearingAids.onceToken
+ _HCLogHearingProtection
+ _HCLogHearingProtection.__logObj
+ _HCLogHearingProtection.cold.1
+ _HCLogHearingProtection.onceToken
+ ___24-[HCServer handleReply:]_block_invoke.7
+ ___HCLogAudioAccommodations_block_invoke
+ ___HCLogComfortSounds_block_invoke
+ ___HCLogHearingAids_block_invoke
+ ___HCLogHearingProtection_block_invoke
+ ___HCLogHearing_block_invoke
+ ___block_literal_global.10
+ ___block_literal_global.140
+ ___block_literal_global.16
+ ___block_literal_global.19
+ ___block_literal_global.22
+ ___block_literal_global.25
+ ___block_literal_global.28
+ ___block_literal_global.31
+ ___block_literal_global.4
+ ___block_literal_global.7
+ ___block_literal_global.83
+ ___block_literal_global.88
+ ___block_literal_global.98
- _CSEngineeringLog
- _CSInitializeLogging
- _CSInitializeLogging.CSLoggingOnceToken
- _CSInitializeLogging.cold.1
- _CSLoggingQueue
- _HAEngineeringLog
- _HAInitializeLogging
- _HAInitializeLogging.HALoggingOnceToken
- _HAInitializeLogging.cold.1
- _HALoggingQueue
- _HCHPEngineeringLog
- _HCHPInitializeLogging
- _HCHPInitializeLogging.CSLoggingOnceToken
- _HCHPInitializeLogging.cold.1
- _HCHPLoggingQueue
- _HearingEngineeringLog
- _HearingInitializeLogging
- _HearingInitializeLogging.HearingLoggingOnceToken
- _HearingInitializeLogging.cold.1
- _HearingLoggingQueue
- _PAEngineeringLog
- _PAInitializeLogging
- _PAInitializeLogging.PALoggingOnceToken
- _PAInitializeLogging.cold.1
- _PALoggingQueue
- ___24-[HCServer handleReply:]_block_invoke.15
- ___CSInitializeLogging_block_invoke
- ___HAInitializeLogging_block_invoke
- ___HCHPInitializeLogging_block_invoke
- ___HearingInitializeLogging_block_invoke
- ___PAInitializeLogging_block_invoke
- ___block_literal_global.102
- ___block_literal_global.108
- ___block_literal_global.150
- ___block_literal_global.17
- ___block_literal_global.21
- ___block_literal_global.24
- ___block_literal_global.27
- ___block_literal_global.36
- ___block_literal_global.5
- ___block_literal_global.9
- ___block_literal_global.97
- _objc_retain_x25
- _objc_retain_x27
CStrings:
+ "HCAudioAccommodations"
+ "HCComfortSounds"
+ "HCHearing"
+ "HCHearingAids"
+ "HCHearingProtection"
- "%s:%d %@"
- "%{public}s"
- "+[HCUtilities deviceIsMultiUser]"
- "+[HCUtilities supportsLEA2]"
- "-[HCDatabaseManager setupDatabase]"
- "-[HCServer resetConnection]"
- "-[HCServer terminateConnectionAndNotify:]"
- "-[HCXPCClient sendMessage:errorBlock:]_block_invoke"
- "-[HCXPCMessage hasEntitlement:]"
- "AudioAccommodations"
- "CSLoggingQueue"
- "ComfortSounds"
- "HALoggingQueue"
- "HCHPLoggingQueue"
- "Hearing"
- "HearingAids"
- "HearingLoggingQueue"
- "HearingProtection"
- "PALoggingQueue"

```
