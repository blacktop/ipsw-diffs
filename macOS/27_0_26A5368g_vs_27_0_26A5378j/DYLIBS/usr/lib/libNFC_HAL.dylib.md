## libNFC_HAL.dylib

> `/usr/lib/libNFC_HAL.dylib`

```diff

-  __TEXT.__text: 0x16ab4
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x2b14
-  __TEXT.__oslogstring: 0x2331
+  __TEXT.__text: 0x168c0
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x2aa7
+  __TEXT.__oslogstring: 0x22b5
   __TEXT.__unwind_info: 0x260
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1f0

   __AUTH_CONST.__const: 0x190
   __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA_DIRTY.__data: 0x2
-  __DATA_DIRTY.__bss: 0x248
+  __DATA.__bss: 0x18
+  __DATA_DIRTY.__data: 0xd
+  __DATA_DIRTY.__bss: 0x230
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libnfshared.dylib
   Functions: 181
   Symbols:   272
-  CStrings:  633
+  CStrings:  628
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
Functions:
~ _phOsalNfc_Timer_Start : 1464 -> 1476
~ _phOsalNfc_Timer_Stop : 576 -> 592
~ _phOsalNfc_Timer_Delete : 640 -> 644
~ _phTmlNfc_Init : 2068 -> 2120
~ _phTmlNfc_Write : 1452 -> 1468
~ sub_2a76eec58 -> sub_2b0d22d54 : 112 -> 108
~ _phTmlNfc_Read : 2416 -> 2444
~ sub_2a76ef638 -> sub_2b0d2374c : 444 -> 428
~ _phTmlNfc_IoCtl : 6520 -> 6496
~ _NFHardwareSerialReadBlockAbort : 328 -> 100
~ _NFHardwareSerialFlush : 940 -> 724
~ sub_2a76fbe1c -> sub_2b0d2fd4c : 892 -> 752
CStrings:
+ "Error : read received after shutdown : %p / %p. Driver context 0x%016llX"
- "%s:%i Read aborted while in progress since %llu."
- "%s:%i Socket is non-blocking"
- "%{public}s:%i Read aborted while in progress since %llu."
- "%{public}s:%i Socket is non-blocking"
- "Error : read received after shutdown : %p / %p. Driver controller type 0x%x, Controller config type %d"
- "NFHardwareSerialReadBlockAbort"

```
