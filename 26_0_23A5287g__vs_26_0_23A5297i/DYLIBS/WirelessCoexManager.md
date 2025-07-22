## WirelessCoexManager

> `/System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager`

```diff

-1832.2.0.0.0
-  __TEXT.__text: 0xa640
+1833.1.0.0.0
+  __TEXT.__text: 0xa810
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x668
+  __TEXT.__objc_methlist: 0x678
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x1c8
-  __TEXT.__cstring: 0x195f
-  __TEXT.__oslogstring: 0x40a
+  __TEXT.__cstring: 0x1974
+  __TEXT.__oslogstring: 0x42a
   __TEXT.__unwind_info: 0x2d8
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x123f
+  __TEXT.__objc_methname: 0x126c
   __TEXT.__objc_methtype: 0x26c
   __TEXT.__objc_stubs: 0xa60
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x728
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x418
+  __DATA_CONST.__objc_selrefs: 0x420
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x2f8
   __AUTH_CONST.__cfstring: 0xe00
-  __AUTH_CONST.__objc_const: 0xd88
+  __AUTH_CONST.__objc_const: 0xda8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0xf4
+  __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x30
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4C26A4A7-E34D-3923-80BB-FAC8A7841B3B
-  Functions: 200
-  Symbols:   749
-  CStrings:  643
+  UUID: 9B2A1A80-0733-30C9-B9D5-EB0CE7275D58
+  Functions: 201
+  Symbols:   752
+  CStrings:  647
 
Symbols:
+ -[WRM_UCMInterface setNANRealTimeEnabled:]
+ GCC_except_table40
+ _OBJC_IVAR_$_WRM_UCMInterface.mIsNanRealTimeEnabled
+ ___29-[WRM_UCMInterface stopTimer]_block_invoke.86
+ ___31-[WRM_UCMInterface startTimer:]_block_invoke.89
+ ___34-[WRM_UCMInterface getInstantLoad]_block_invoke.83
+ ___58-[WRM_UCMInterface getWirelessFrequencyBandUpdatesForMIC:]_block_invoke.130
- GCC_except_table39
- ___29-[WRM_UCMInterface stopTimer]_block_invoke.85
- ___31-[WRM_UCMInterface startTimer:]_block_invoke.88
- ___34-[WRM_UCMInterface getInstantLoad]_block_invoke.82
- ___58-[WRM_UCMInterface getWirelessFrequencyBandUpdatesForMIC:]_block_invoke.129
Functions:
+ -[WRM_UCMInterface setNANRealTimeEnabled:]
CStrings:
+ "Sending NAN RealTime %s from %s"
+ "kWCMP2PNANRealTimeOn"
+ "mIsNanRealTimeEnabled"
+ "setNANRealTimeEnabled:"

```
