## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-  __TEXT.__text: 0x290760
+  __TEXT.__text: 0x29103c
   __TEXT.__auth_stubs: 0x25b0
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x82e33
+  __TEXT.__cstring: 0x8300f
   __TEXT.__const: 0x7f168
   __TEXT.__oslogstring: 0x1f27
-  __TEXT.__unwind_info: 0x5fb8
+  __TEXT.__unwind_info: 0x5fd0
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__const: 0x210e8
+  __DATA_CONST.__const: 0x21100
   __DATA_CONST.__osclassinfo: 0x388
   __DATA_CONST.__auth_got: 0x12d8
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 14163
-  Symbols:   17464
-  CStrings:  13117
+  Functions: 14172
+  Symbols:   17473
+  CStrings:  13125
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__const : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__osclassinfo : content changed
~ __DATA.__data : content changed
Symbols:
+ _ZN24AppleBCMWLANNANInterface24setNAN_MULTICAST_PEER_OPEP32apple80211_nan_multicast_peer_op
+ __ZN24AppleBCMWLANNANInterface24setNAN_MULTICAST_PEER_OPEP32apple80211_nan_multicast_peer_op
+ __ZThn112_N24AppleBCMWLANNANInterface24setNAN_MULTICAST_PEER_OPEP32apple80211_nan_multicast_peer_op
+ __ZThn128_N24AppleBCMWLANNANInterface24setNAN_MULTICAST_PEER_OPEP32apple80211_nan_multicast_peer_op
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1580.63\""
+ "AppleBCMWLANV3_driverkit-1580.63"
+ "Debug: WL_NAN_CMD_CFG_SET_PEER_KEY (mcast_peer) bytestream: "
+ "Jul  1 2026 23:33:59"
+ "[dk] %s@%d:%s invalid operation %u\n"
+ "[dk] %s@%d:%s invalid peer count %u\n"
+ "[dk] %s@%d:%s: op=%u count=%u laddr=%02x:%02x:%02x:%02x:%02x:%02x mcast=%02x:%02x:%02x:%02x:%02x:%02x\n"
+ "[dk] %s@%d:ERROR: Unable to set NAN multicast peer, ret = %d\n"
+ "[dk] %s@%d:Failed to allocate fBackplane lock\n"
+ "setNAN_MULTICAST_PEER_OP"
+ "virtual int32_t AppleBCMWLANNANInterface::setNAN_MULTICAST_PEER_OP(apple80211_nan_multicast_peer_op_t *)"
- "\"AppleBCMWLANV3_driverkit-1580.59\""
- "AppleBCMWLANV3_driverkit-1580.59"
- "Jun 16 2026 21:46:18"

```
