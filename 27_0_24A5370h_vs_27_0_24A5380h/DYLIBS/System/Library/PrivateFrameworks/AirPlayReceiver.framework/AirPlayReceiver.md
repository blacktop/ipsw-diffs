## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-  __TEXT.__text: 0x17d188
+  __TEXT.__text: 0x17d6b4
   __TEXT.__objc_methlist: 0xaec
   __TEXT.__const: 0x275a9
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x848
-  __TEXT.__cstring: 0x338bf
+  __TEXT.__cstring: 0x33c71
   __TEXT.__oslogstring: 0x2eb
-  __TEXT.__unwind_info: 0x16b8
+  __TEXT.__unwind_info: 0x16a0
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2098
+  __DATA_CONST.__const: 0x20b0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x9480
-  __AUTH_CONST.__cfstring: 0xbb80
+  __DATA_CONST.__got: 0x980
+  __AUTH_CONST.__const: 0x9460
+  __AUTH_CONST.__cfstring: 0xbbe0
   __AUTH_CONST.__objc_const: 0x1550
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1e50
+  __AUTH_CONST.__auth_got: 0x1e58
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x174
   __DATA.__data: 0x17d20
-  __DATA.__bss: 0x608
+  __DATA.__bss: 0x5f8
   __DATA.__common: 0xa80
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x310

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1711
-  Symbols:   5406
-  CStrings:  6735
+  Functions: 1708
+  Symbols:   5399
+  CStrings:  6752
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ GCC_except_table1004
+ GCC_except_table1116
+ GCC_except_table1135
+ GCC_except_table1186
+ GCC_except_table1190
+ GCC_except_table1243
+ GCC_except_table1251
+ GCC_except_table1253
+ GCC_except_table1298
+ GCC_except_table1361
+ GCC_except_table1370
+ GCC_except_table215
+ GCC_except_table222
+ GCC_except_table228
+ GCC_except_table417
+ GCC_except_table480
+ GCC_except_table529
+ GCC_except_table587
+ GCC_except_table591
+ GCC_except_table598
+ GCC_except_table606
+ GCC_except_table740
+ _BonjourAdvertiserSetNANPairingClientInfo
+ _audioSessionBufferedHose_setMulticastGroupInfo
+ _kAPReceiverAudioSessionOption_MulticastGroupInfo
- GCC_except_table1005
- GCC_except_table1119
- GCC_except_table1138
- GCC_except_table1189
- GCC_except_table1193
- GCC_except_table1246
- GCC_except_table1254
- GCC_except_table1256
- GCC_except_table1301
- GCC_except_table1364
- GCC_except_table1373
- GCC_except_table217
- GCC_except_table223
- GCC_except_table229
- GCC_except_table418
- GCC_except_table481
- GCC_except_table530
- GCC_except_table588
- GCC_except_table592
- GCC_except_table599
- GCC_except_table607
- GCC_except_table741
- _APTransportConnectionAddEventCallback
- _APTransportConnectionResume
- _CMBaseObjectSetProperty
- __APAdvertiserSetupBonjourAdvertiser.sBonjourAdvertiserSetNANPairingClientInfo
- __APAdvertiserSetupBonjourAdvertiser.sSetNANPairingClientInfoOnce
- ____APAdvertiserSetupBonjourAdvertiser_block_invoke
CStrings:
+ "### Auxiliary screen session already registered [%{ptr}], rejecting new one [%{ptr}]\n"
+ "980.67.2"
+ "Added an auxiliary screen session [%{ptr}] (paired with main [%{ptr}]); sessions array capacity %d\n"
+ "MulticastGroupInfo"
+ "PairedSessionEnded"
+ "Releasing auxiliary screen session; sessions array capacity %d\n"
+ "Terminating paired session [%{ptr}] (partner of [%{ptr}])\n"
+ "[%{ptr}] Auxiliary screen session reusing PWD context [%{ptr}] from primary session [%{ptr}] (clientDeviceID=%llu, protectionBits=0x%x)\n"
+ "[%{ptr}] Auxiliary screen session: clientDeviceID is 0\n"
+ "[%{ptr}] Auxiliary screen session: no primary mirroring session (clientDeviceID=%llu)\n"
+ "[%{ptr}] Auxiliary screen session: primary [%{ptr}] clientDeviceID=%llu mismatch (ours=%llu)\n"
+ "[%{ptr}] Auxiliary screen session: primary [%{ptr}] has not completed PWD key exchange\n"
+ "_AdoptPWDProtectionContextFromPrimaryScreenSession"
+ "isAuxiliaryScreenSession"
+ "multicastGroupInfo"
+ "void _AdoptPWDProtectionContextFromPrimaryScreenSession(AirPlayReceiverSessionRef)"
- "980.63.2"
- "BonjourAdvertiserSetNANPairingClientInfo"

```
