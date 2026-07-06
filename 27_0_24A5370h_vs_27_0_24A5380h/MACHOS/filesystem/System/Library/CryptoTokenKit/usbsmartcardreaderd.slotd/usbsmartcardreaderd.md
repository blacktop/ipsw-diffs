## usbsmartcardreaderd

> `/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/usbsmartcardreaderd`

```diff

-  __TEXT.__text: 0x15ae8
+  __TEXT.__text: 0x16c74
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_stubs: 0x3000
-  __TEXT.__objc_methlist: 0x16f4
-  __TEXT.__const: 0x2a0
-  __TEXT.__objc_classname: 0x1e7
+  __TEXT.__objc_stubs: 0x3100
+  __TEXT.__objc_methlist: 0x1734
+  __TEXT.__const: 0x2a8
+  __TEXT.__objc_classname: 0x1fc
   __TEXT.__objc_methtype: 0x891
-  __TEXT.__objc_methname: 0x22c9
-  __TEXT.__oslogstring: 0x159b
-  __TEXT.__cstring: 0x15d5
+  __TEXT.__objc_methname: 0x236e
+  __TEXT.__oslogstring: 0x1a90
+  __TEXT.__cstring: 0x15db
   __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__unwind_info: 0x608
-  __DATA_CONST.__const: 0x7e0
-  __DATA_CONST.__cfstring: 0x2120
+  __TEXT.__unwind_info: 0x630
+  __DATA_CONST.__const: 0x808
+  __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0xe0
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
   __DATA_CONST.__auth_got: 0x338
-  __DATA_CONST.__got: 0x120
-  __DATA.__objc_const: 0x26a8
-  __DATA.__objc_selrefs: 0xdc0
+  __DATA_CONST.__got: 0x150
+  __DATA.__objc_const: 0x2700
+  __DATA.__objc_selrefs: 0xde8
   __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x8c0
-  __DATA.__data: 0x190
+  __DATA.__data: 0x1f0
   __DATA.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit

   - /System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 658
+  Functions: 680
   Symbols:   146
-  CStrings:  1400
+  CStrings:  1427
 
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
~ __DATA.__bss : content changed
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
