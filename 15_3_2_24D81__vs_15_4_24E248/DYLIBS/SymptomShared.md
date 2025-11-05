## SymptomShared

> `/System/Library/PrivateFrameworks/SymptomShared.framework/Versions/A/SymptomShared`

```diff

-2001.80.5.0.0
-  __TEXT.__text: 0x7338
+2022.100.26.0.0
+  __TEXT.__text: 0x736c
   __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_methlist: 0x9f8
+  __TEXT.__objc_methlist: 0xa44
   __TEXT.__cstring: 0x6fd
-  __TEXT.__gcc_except_tab: 0x1d0
+  __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__const: 0x74
   __TEXT.__oslogstring: 0x5ef
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__unwind_info: 0x258
   __TEXT.__objc_classname: 0xef
   __TEXT.__objc_methname: 0x1a15
   __TEXT.__objc_methtype: 0x2a0

   __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x9a0
-  __AUTH_CONST.__objc_const: 0x15c0
+  __AUTH_CONST.__objc_const: 0x1548
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x370

   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 026BA447-035A-32D7-9BF5-C392FECCD12F
-  Functions: 218
-  Symbols:   686
+  UUID: 1ADEE0A7-524C-3CDC-8B3A-8C66279F1D79
+  Functions: 221
+  Symbols:   690
   CStrings:  616
 
Symbols:
+ +[NWPVar _backgroundQueue].cold.1
+ +[NWPVar _serviceQueue].cold.1
+ GCC_except_table12
+ nwpvarLogHandle.cold.1
Functions:
~ -[NWNetworkOfInterest copyWithZone:] : 248 -> 300
~ _nwpvarLogHandle : 84 -> 68
~ +[NWPVar _serviceQueue] : 84 -> 68
~ +[NWPVar _backgroundQueue] : 84 -> 68
~ ___36+[NWPVar _fetchCheckpoint:isPrefix:]_block_invoke : 704 -> 708
~ -[NWPVarBandit _epsilongreedy_predictValueGivenContext:] : 1628 -> 1616
~ -[NWPVarBandit _ucb_predictValueGivenContext:] : 920 -> 924
~ -[NWPVarBandit predictValueGivenContext:generationId:] : 844 -> 840
~ -[NWPVarBandit setReward:onValue:forPredictionGenerationId:] : 2676 -> 2672

```
