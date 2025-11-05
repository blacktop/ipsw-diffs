## IOFireWireSBP2Lib

> `/System/Library/Extensions/IOFireWireSBP2.kext/Contents/PlugIns/IOFireWireSBP2Lib.plugin/Contents/MacOS/IOFireWireSBP2Lib`

```diff

 452.0.0.0.0
-  __TEXT.__text: 0x3818
+  __TEXT.__text: 0x37b4
   __TEXT.__auth_stubs: 0x1c0
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__const: 0x62

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: CDA2D36C-1C30-3ED2-9760-DA88FA6F50D4
+  UUID: 58148846-41B2-3CF2-9EA1-751224BF85B9
   Functions: 185
   Symbols:   238
   CStrings:  1
Functions:
~ __ZN22IOFireWireSBP2LibLogin4initEjj : 524 -> 520
~ __ZN22IOFireWireSBP2LibLogin23unsolicitedStatusNotifyEiPyi : 168 -> 152
~ __ZN22IOFireWireSBP2LibLogin12statusNotifyEiPyi : 164 -> 140
~ __ZN20IOFireWireSBP2LibLUN4openEv : 76 -> 80
~ __ZN20IOFireWireSBP2LibLUN18openWithSessionRefEP31IOFireWireSessionRefOpaqueStuct : 80 -> 84
~ __ZN20IOFireWireSBP2LibLUN5closeEv : 64 -> 68
~ __ZN20IOFireWireSBP2LibLUN11createLoginE11CFUUIDBytes : 144 -> 140
~ __ZN20IOFireWireSBP2LibLUN13createMgmtORBE11CFUUIDBytes : 152 -> 156
~ __ZN20IOFireWireSBP2LibLUN15messageCallbackEiPyi : 200 -> 156
~ __ZN24IOFireWireSBP2LibMgmtORB4initEjj : 236 -> 232
~ __ZN20IOFireWireSBP2LibORB4initEjj : 108 -> 104
~ __ZN20IOFireWireSBP2LibORB25setCommandBuffersAsRangesEP18FWSBP2VirtualRangejjjj : 348 -> 340
~ __ZN20IOFireWireSBP2LibORB38LSIWorkaroundSetCommandBuffersAsRangesEP18FWSBP2VirtualRangejjjj : 348 -> 340

```
