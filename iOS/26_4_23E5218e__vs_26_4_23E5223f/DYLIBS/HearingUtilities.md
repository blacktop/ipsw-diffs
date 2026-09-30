## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-496.15.0.0.0
-  __TEXT.__text: 0x9d1a8
+496.16.0.0.0
+  __TEXT.__text: 0x9d3f8
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x7bdc
+  __TEXT.__objc_methlist: 0x7be4
   __TEXT.__const: 0x402
-  __TEXT.__gcc_except_tab: 0x260c
+  __TEXT.__gcc_except_tab: 0x2618
   __TEXT.__cstring: 0x4cca
-  __TEXT.__oslogstring: 0x944e
+  __TEXT.__oslogstring: 0x9495
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30

   __TEXT.__swift5_reflstr: 0xb
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x29d0
+  __TEXT.__unwind_info: 0x29e0
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0x883
-  __TEXT.__objc_methname: 0x140f4
+  __TEXT.__objc_methname: 0x14124
   __TEXT.__objc_methtype: 0x2275
-  __TEXT.__objc_stubs: 0xeb20
+  __TEXT.__objc_stubs: 0xeb60
   __DATA_CONST.__got: 0x620
   __DATA_CONST.__const: 0x3398
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4910
+  __DATA_CONST.__objc_selrefs: 0x4920
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x3d0
   __AUTH_CONST.__auth_got: 0x878

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DC54E26D-B7E9-3AE7-95FC-4680DC4C8826
-  Functions: 3546
-  Symbols:   11460
-  CStrings:  5920
+  UUID: D4F50356-C0BB-3E9E-BD2F-18945298EF28
+  Functions: 3548
+  Symbols:   11466
+  CStrings:  5923
 
Symbols:
+ -[HUHearingAidSettings _initializeWatchSync]
+ GCC_except_table106
+ ___28-[HUHearingAidSettings init]_block_invoke_2
+ ___block_literal_global.367
+ _objc_msgSend$_initializeWatchSync
+ _objc_msgSend$callStackSymbols
+ _sharedInstance.Settings.364
+ _sharedInstance.onceToken.365
- GCC_except_table104
- GCC_except_table35
- GCC_except_table42
- ___block_literal_global.366
- _sharedInstance.Settings.363
- _sharedInstance.onceToken.364
Functions:
~ -[HUAccessoryHearingSettings setActiveHearingProtectionEnabled:forAddress:] : 436 -> 528
~ -[HUHearingAidSettings init] : 684 -> 804
+ ___28-[HUHearingAidSettings init]_block_invoke_2
+ -[HUHearingAidSettings _initializeWatchSync]
~ -[HUComfortSoundsController scheduleFile] : 940 -> 952
CStrings:
+ "AccessoryHearingSettings: Saving Hearing Protection enabled for %@ = %d -> %d, %@"
+ "HearingAidSettings: missing pushing paired aids to watch: %@"
+ "_initializeWatchSync"
+ "callStackSymbols"
- "AccessoryHearingSettings: Saving Hearing Protection enabled for %@ = %d"

```
