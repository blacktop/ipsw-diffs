## SatelliteSMS

> `/System/Library/Messages/PlugIns/SatelliteSMS.imservice/SatelliteSMS`

```diff

-1440.100.7.2.5
-  __TEXT.__text: 0xbacc
-  __TEXT.__auth_stubs: 0xb80
+1443.100.10.1.5
+  __TEXT.__text: 0xbbd8
+  __TEXT.__auth_stubs: 0xb90
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x37c
   __TEXT.__const: 0x3aa
-  __TEXT.__objc_methname: 0x10dc
+  __TEXT.__objc_methname: 0x10f4
   __TEXT.__oslogstring: 0x93f
   __TEXT.__cstring: 0x4f1
   __TEXT.__swift5_typeref: 0x18c

   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_reflstr: 0x43
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__unwind_info: 0x2c0
   __TEXT.__eh_frame: 0x200
-  __DATA_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__auth_got: 0x5d8
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__const: 0x598

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 02AB77E6-9A6C-32B9-9657-6D556A7C65C3
+  UUID: ABD5E78E-F5D6-30CA-A307-B9C05B269382
   Functions: 199
   Symbols:   197
   CStrings:  301
Functions:
~ sub_4584 : 616 -> 624
~ sub_4f00 -> sub_4f08 : 392 -> 648
~ sub_8564 -> sub_866c : 1696 -> 1700
~ sub_a9f4 -> sub_ab00 : 100 -> 72
~ sub_aa58 -> sub_ab48 : 72 -> 152
~ sub_aaa0 -> sub_abe0 : 152 -> 244
~ sub_ab38 -> sub_acd4 : 244 -> 100
CStrings:
+ "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:sourceHandle:destinationHandle:error:"
- "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:handle:error:"

```
