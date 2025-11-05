## smcupdater

> `/usr/libexec/smcupdater`

```diff

 3.0.0.0.0
-  __TEXT.__text: 0x29aa
+  __TEXT.__text: 0x292a
   __TEXT.__stubs: 0x15c
   __TEXT.__cstring: 0xce7
-  __TEXT.__const: 0x30
+  __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0xe0
   __TEXT.__eh_frame: 0x58
   __DATA_CONST.__got: 0x250

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 67CC4491-CF45-3B30-A14E-74E8CAC708D9
+  UUID: 6F468061-94E9-33A5-923A-B005497D03A4
   Functions: 43
   Symbols:   124
   CStrings:  109
Functions:
~ _callFunction : 178 -> 187
~ _printIOReturn : 222 -> 213
~ _smcrSMCGetKeyFromIndex : 333 -> 334
~ _smcrSMCReadKeyFixAsDouble : 451 -> 437
~ _smcrSMCWriteKeyRaw : 475 -> 480
~ _smcrSMCWriteKeyFixFromDouble : 597 -> 525
~ _parseSmcVersion : 580 -> 577
~ _shouldUpdate : 258 -> 271
~ _CheckSpecialCasesForUpdate : 185 -> 126
~ _main : 3068 -> 3069

```
