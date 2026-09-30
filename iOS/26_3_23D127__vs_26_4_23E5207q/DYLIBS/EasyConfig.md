## EasyConfig

> `/System/Library/PrivateFrameworks/EasyConfig.framework/EasyConfig`

```diff

-810.19.0.0.0
-  __TEXT.__text: 0x4e70
-  __TEXT.__auth_stubs: 0x780
+820.40.0.0.0
+  __TEXT.__text: 0x4f4c
+  __TEXT.__auth_stubs: 0x750
   __TEXT.__objc_methlist: 0x334
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x1028
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__unwind_info: 0x170
   __TEXT.__objc_classname: 0x27
   __TEXT.__objc_methname: 0xa32
   __TEXT.__objc_methtype: 0x5cb

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__cfstring: 0x4a0
   __AUTH_CONST.__objc_const: 0x870
   __AUTH.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35369982-C33C-362E-9927-74D9A90A8B19
+  UUID: 3C9B840E-7CAB-3B15-A740-D0C461A24C21
   Functions: 93
-  Symbols:   471
+  Symbols:   468
   CStrings:  369
 
Symbols:
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x23
- _objc_retain_x8
Functions:
~ -[EasyConfigDevice setDispatchQueue:] : 12 -> 64
~ -[EasyConfigDevice _timeoutTimerStart:block:] : 228 -> 224
~ -[EasyConfigDevice _startBonjourWithTimeout:handler:] : 748 -> 728
~ ___47-[EasyConfigDevice _postProgress:withResponse:]_block_invoke : 356 -> 372
~ ___39-[EasyConfigDevice _postProgress:info:]_block_invoke : 284 -> 296
~ -[EasyConfigDevice _postNote:info:] : 196 -> 188
~ ___35-[EasyConfigDevice _postNote:info:]_block_invoke : 92 -> 96
~ -[EasyConfigDevice _findDevicePostConfigEvent:info:] : 756 -> 760
~ -[EasyConfigDevice _applyConfigStart] : 896 -> 884
~ -[EasyConfigDevice trySetupCode:] : 152 -> 160
~ -[EasyConfigDevice _stop:] : 912 -> 936
~ -[EasyConfigDevice _start] : 992 -> 996
~ -[EasyConfigDevice removed:] : 228 -> 232
~ -[EasyConfigDevice updated:] : 336 -> 444
~ -[EasyConfigDevice init] : 148 -> 156
~ +[EasyConfigDevice supportedScanRecord:] : 212 -> 216
~ _EasyConfigCreateDictionaryFromTLV : 888 -> 904

```
