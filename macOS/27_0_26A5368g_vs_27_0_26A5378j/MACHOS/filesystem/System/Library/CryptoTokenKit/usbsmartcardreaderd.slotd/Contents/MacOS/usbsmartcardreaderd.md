## usbsmartcardreaderd

> `/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/Contents/MacOS/usbsmartcardreaderd`

```diff

-  __TEXT.__text: 0x18334
+  __TEXT.__text: 0x19580
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0x3300
-  __TEXT.__objc_methlist: 0x1764
-  __TEXT.__const: 0x2b8
-  __TEXT.__objc_classname: 0x1f5
+  __TEXT.__objc_stubs: 0x3400
+  __TEXT.__objc_methlist: 0x17a4
+  __TEXT.__const: 0x2c0
+  __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methtype: 0x8f0
-  __TEXT.__objc_methname: 0x2520
-  __TEXT.__oslogstring: 0x17e1
-  __TEXT.__cstring: 0x168c
+  __TEXT.__objc_methname: 0x25c5
+  __TEXT.__oslogstring: 0x1cd6
+  __TEXT.__cstring: 0x1692
   __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__unwind_info: 0x648
-  __DATA_CONST.__const: 0x828
-  __DATA_CONST.__cfstring: 0x22a0
+  __TEXT.__unwind_info: 0x670
+  __DATA_CONST.__const: 0x858
+  __DATA_CONST.__cfstring: 0x22c0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_intobj: 0x408
-  __DATA_CONST.__objc_doubleobj: 0x20
+  __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0x138
-  __DATA.__objc_const: 0x2770
-  __DATA.__objc_selrefs: 0xe80
+  __DATA_CONST.__got: 0x170
+  __DATA.__objc_const: 0x27c8
+  __DATA.__objc_selrefs: 0xea8
   __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x910
-  __DATA.__data: 0x190
+  __DATA.__data: 0x1f0
   __DATA.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 698
+  Functions: 720
   Symbols:   126
-  CStrings:  1463
+  CStrings:  1490
 
Sections:
~ __TEXT.__objc_methtype : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_data : content changed
CStrings:
+ "<nil>"
+ "APDU Mapping: unparseable APDU (%lu bytes); rejecting"
+ "ChainableTransmitter"
+ "Inbound chain: assembled payload would exceed cap %lu at frame %lu"
+ "Inbound chain: continuation reply has unexpected messageType (frame %lu)"
+ "Inbound chain: frame count exceeded cap %lu; aborting"
+ "Inbound chain: initial payload %lu bytes exceeds cap %lu"
+ "Inbound chain: state violation at frame %lu bChainParameter=0x%02x"
+ "Inbound chain: unexpected initial bChainParameter=0x%02x"
+ "Message is nil or unexpected type"
+ "Outbound chain frame %lu/%lu (wLevelParameter=0x%04x) failed: %{public}@"
+ "RDR_to_PC_HardwareError: short frame (%lu bytes)"
+ "RDR_to_PC_HardwareError: slot=%u bSeq=%u bHardwareErrorCode=0x%02x"
+ "T1 TPDU Mapping transmit"
+ "Unhandled interrupt-IN message type 0x%02x"
+ "abortChainOnSequence:"
+ "abortSequence: drain deadline (%.1fs) expired without matching SlotStatus terminator (seq=%u)"
+ "abortSequence: drain receive returned 0 bytes (timeout); checking deadline"
+ "abortSequence: drain saw frame for slot %u while aborting slot %u; bailing"
+ "abortSequence: drain saw short/partial reply (%lu bytes, below CCID header); discarding and continuing"
+ "abortSequence: drained matching SlotStatus terminator (seq=%u)"
+ "abortSequence: step 1 control transfer failed (continuing to step 2): %{public}@"
+ "abortSequence: step 2 bulk-OUT short send (%lu of %lu bytes; continuing to step 3)"
+ "dateWithTimeIntervalSinceNow:"
+ "maxOutboundCCIDMessageLength"
+ "sendOutboundChain:maxPayload:outTimeout:inTimeout:transmitted:"
+ "timeIntervalSinceNow"
- "T1 APDU Mapping transmit"

```
