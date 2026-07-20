## STSXPCHelper

> `/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-6.0.11.0.0
-  __TEXT.__text: 0x39d88
-  __TEXT.__auth_stubs: 0xae0
+6.0.13.0.0
+  __TEXT.__text: 0x3a334
+  __TEXT.__auth_stubs: 0xb00
   __TEXT.__delay_helper: 0x114
-  __TEXT.__objc_stubs: 0x4660
+  __TEXT.__objc_stubs: 0x4680
   __TEXT.__objc_methlist: 0x28d0
-  __TEXT.__const: 0x150
-  __TEXT.__objc_methname: 0x625a
-  __TEXT.__cstring: 0x9207
+  __TEXT.__const: 0x158
+  __TEXT.__objc_methname: 0x6263
+  __TEXT.__cstring: 0x95a4
   __TEXT.__objc_classname: 0x7d7
   __TEXT.__objc_methtype: 0x1eed
   __TEXT.__gcc_except_tab: 0x7c4
-  __TEXT.__oslogstring: 0xb14
-  __TEXT.__unwind_info: 0xae8
+  __TEXT.__oslogstring: 0xb4e
+  __TEXT.__ustring: 0x268
+  __TEXT.__unwind_info: 0xaf0
   __DATA_CONST.__const: 0xe90
-  __DATA_CONST.__cfstring: 0x5b20
+  __DATA_CONST.__cfstring: 0x5d00
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc0

   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x580
+  __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x2e8
   __DATA.__objc_const: 0x61e8
-  __DATA.__objc_selrefs: 0x17d8
+  __DATA.__objc_selrefs: 0x17e0
   __DATA.__objc_ivar: 0x4dc
   __DATA.__objc_data: 0x1360
   __DATA.__data: 0xa64

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 958
-  Symbols:   289
-  CStrings:  2505
+  Symbols:   291
+  CStrings:  2530
 
Symbols:
+ _clock_gettime_nsec_np
+ _dispatch_queue_get_label
Functions:
~ sub_100003700 -> sub_100003750 : 484 -> 524
~ sub_100017d4c -> sub_100017dc4 : 544 -> 1116
~ sub_1000181b8 -> sub_10001846c : 500 -> 692
~ sub_1000183ac -> sub_100018720 : 120 -> 144
~ sub_1000184d4 -> sub_100018860 : 272 -> 228
~ sub_100032d6c -> sub_1000330cc : 108 -> 364
~ sub_100034a2c -> sub_100034e8c : 828 -> 848
~ sub_100034d68 -> sub_1000351dc : 480 -> 772
~ sub_100034f58 -> sub_1000354f0 : 104 -> 204
CStrings:
+ " created DCPresentmentRequest: %@ "
+ "(no label)"
+ "-[ISO18013_3_Central peripheralIsReadyToSendWriteWithoutResponse:]"
+ "-[ISO18013_3_Central writeData:toUUID:]_block_invoke_3"
+ "-[STSISO18013Handler _interpretPresentmentRequest:callback:]"
+ "BT_SendData_BoundaryRace"
+ "Invalidated"
+ "LE: BLESender invalidate, pendingBytes=%lu"
+ "LE: Done TX (frags=%lu bytes=%lu)"
+ "LE: TX frag #%lu size=%lu mtu=%u lastPkt=%d"
+ "LE: anomaly — frag #%lu size=%lu mtu=%u (expected full chunk on non-last)"
+ "LE: canSendWriteWithoutResponse=NO; deferring"
+ "LE: closure invoked, fragSize=%lu canSendWWR=%d"
+ "LE: maximumWriteValueLengthForType=%lu (clamped uint16=%u, cap=%u)"
+ "LE: maximumWriteValueLengthForType=%u exceeds cap; clamping to %u"
+ "LE: parking at frag #%lu (dataIndex=%lu remaining=%lu)"
+ "LE: peripheralReady MISMATCH expected=%@ — dropping spurious ready notification"
+ "LE: peripheralReady peripheral=%@ match=%d senderPresent=%d cbQueue=%s"
+ "LE: spaceIsAvailable invalidated=%d pendingBytes=%lu"
+ "LE: writeData %s"
+ "LE: writeData boundary race — signal observed only on non-blocking poll after %.3fs"
+ "LE: writeData timed out after %.1fs; pendingBytes=%lu — failing write"
+ "LE: writeData unblocked after %.3fs (gotSignal=%d, raceRecovered=%d)"
+ "LE: writeData uuid=%@ peripheralID=%@ delegateIsSelf=%d canSendWWR=%d isConnected=%d hasL2CAP=%d state=%ld dataLen=%lu queue=%s"
+ "LE: writing %lu bytes (mtu=%u)"
+ "completed"
+ "delegate"
+ "elapsed=%.3f"
+ "unblocked by invalidate (failure)"
- "Data unavailable"
- "LE: Read MTU=%d is too large; override to MAX_ATTRIBUTE_SIZE"
- "LE: writing %lu bytes"
- "Session invalidated"
```
