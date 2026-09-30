## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/Versions/A/AirPlayReceiver`

```diff

-  __TEXT.__text: 0xf9760
+  __TEXT.__text: 0xf9c38
   __TEXT.__objc_methlist: 0xca4
   __TEXT.__const: 0xd4d1
   __TEXT.__dlopen_cstrs: 0x103
   __TEXT.__gcc_except_tab: 0x864
-  __TEXT.__cstring: 0x2f609
+  __TEXT.__cstring: 0x2f99d
   __TEXT.__oslogstring: 0x2eb
-  __TEXT.__unwind_info: 0x1370
+  __TEXT.__unwind_info: 0x1360
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1be0
+  __DATA_CONST.__const: 0x1bf0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x3ec0
-  __AUTH_CONST.__cfstring: 0xb320
+  __DATA_CONST.__got: 0x870
+  __AUTH_CONST.__const: 0x3e80
+  __AUTH_CONST.__cfstring: 0xb380
   __AUTH_CONST.__objc_const: 0x18f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x173b0
-  __DATA.__bss: 0xf70
+  __DATA.__bss: 0xf50
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x5b0
   __DATA_DIRTY.__bss: 0x1f8

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1480
-  Symbols:   3872
-  CStrings:  6265
+  Functions: 1476
+  Symbols:   3865
+  CStrings:  6281
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
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
+ GCC_except_table1042
+ GCC_except_table1061
+ GCC_except_table1112
+ GCC_except_table1168
+ GCC_except_table1176
+ GCC_except_table1178
+ GCC_except_table1222
+ GCC_except_table1284
+ GCC_except_table1293
+ GCC_except_table214
+ GCC_except_table215
+ GCC_except_table221
+ GCC_except_table397
+ GCC_except_table453
+ GCC_except_table477
+ GCC_except_table529
+ GCC_except_table533
+ GCC_except_table540
+ GCC_except_table548
+ GCC_except_table725
+ GCC_except_table737
+ GCC_except_table740
+ GCC_except_table743
+ GCC_except_table751
+ GCC_except_table764
+ GCC_except_table935
+ _BonjourAdvertiserSetNANPairingClientInfo
+ _BonjourAdvertiserSetNANUserID
+ _audioSessionBufferedHose_setMulticastGroupInfo
+ _kAPReceiverAudioSessionOption_MulticastGroupInfo
- APTransportConnectionAddEventCallback
- APTransportConnectionResume
- GCC_except_table1046
- GCC_except_table1065
- GCC_except_table1120
- GCC_except_table1172
- GCC_except_table1180
- GCC_except_table1182
- GCC_except_table1226
- GCC_except_table1288
- GCC_except_table1297
- GCC_except_table216
- GCC_except_table217
- GCC_except_table223
- GCC_except_table399
- GCC_except_table455
- GCC_except_table479
- GCC_except_table531
- GCC_except_table535
- GCC_except_table542
- GCC_except_table550
- GCC_except_table727
- GCC_except_table739
- GCC_except_table742
- GCC_except_table745
- GCC_except_table753
- GCC_except_table768
- GCC_except_table937
- _APAdvertiserSetupBonjourAdvertiser.fn
- _APAdvertiserSetupBonjourAdvertiser.once
- _APAdvertiserSetupBonjourAdvertiser.sBonjourAdvertiserSetNANPairingClientInfo
- _APAdvertiserSetupBonjourAdvertiser.sSetNANPairingClientInfoOnce
- _CMBaseObjectSetProperty
- ____APAdvertiserSetupBonjourAdvertiser_block_invoke
- ____APAdvertiserSetupBonjourAdvertiser_block_invoke_2
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
- "BonjourAdvertiserSetNANUserID"

```
