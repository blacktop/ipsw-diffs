## usbsmartcardreaderd

> `/System/Library/CryptoTokenKit/usbsmartcardreaderd.slotd/usbsmartcardreaderd`

```diff

-685.60.2.0.0
-  __TEXT.__text: 0x15794
+685.80.2.0.0
+  __TEXT.__text: 0x15a10
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0x2d20
-  __TEXT.__objc_methlist: 0x1480
+  __TEXT.__objc_stubs: 0x2ee0
+  __TEXT.__objc_methlist: 0x1470
   __TEXT.__const: 0x228
-  __TEXT.__objc_classname: 0x1f6
-  __TEXT.__objc_methname: 0x21d2
-  __TEXT.__objc_methtype: 0x859
-  __TEXT.__oslogstring: 0x1221
-  __TEXT.__cstring: 0x15e9
-  __TEXT.__gcc_except_tab: 0x220
+  __TEXT.__objc_classname: 0x1f8
+  __TEXT.__objc_methname: 0x21ed
+  __TEXT.__objc_methtype: 0x863
+  __TEXT.__oslogstring: 0x125e
+  __TEXT.__cstring: 0x17b7
+  __TEXT.__gcc_except_tab: 0x21c
   __TEXT.__unwind_info: 0x574
   __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x780
-  __DATA_CONST.__cfstring: 0x21e0
+  __DATA_CONST.__cfstring: 0x2460
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x3d8
+  __DATA_CONST.__objc_intobj: 0x3f0
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__objc_arrayobj: 0x120
-  __DATA.__objc_const: 0x29c0
-  __DATA.__objc_selrefs: 0xcb8
+  __DATA.__objc_const: 0x29e0
+  __DATA.__objc_selrefs: 0xcc8
   __DATA.__objc_classrefs: 0x158
   __DATA.__objc_superrefs: 0xc0
   __DATA.__objc_ivar: 0xd8

   - /System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3F2061E3-40B1-316B-988B-3F44758FECEC
+  UUID: 5656818B-A454-30FA-953B-6FEF37729A20
   Functions: 639
   Symbols:   143
-  CStrings:  1379
+  CStrings:  1423
 
Symbols:
+ _OBJC_CLASS_$_TKSlotParameters
- _OBJC_CLASS_$_NSLocale
CStrings:
+ ""
+ "I24@0:8Q16"
+ "PINBlockString"
+ "PINByteOffset"
+ "PINFormatStringWithError:"
+ "PINLengthFormatWithError:"
+ "PINMaxExtraDigit"
+ "TKDataView"
+ "The 'PINByteOffset' is ignored by CCID and should be set to 0"
+ "bConfirmPIN: 0x%.2x "
+ "bEntryValidationCondition: 0x%.2x "
+ "bInsertionOffsetNew: 0x%.2x "
+ "bInsertionOffsetOld: 0x%.2x "
+ "bMsgIndex1: 0x%.2x "
+ "bMsgIndex2: 0x%.2x "
+ "bMsgIndex3: 0x%.2x "
+ "bMsgIndex: 0x%.2x "
+ "bNumberMessage: 0x%.2x "
+ "bmFormatString: 0x%.2x "
+ "bmPINBlockString: 0x%.2x "
+ "bmPINLengthFormat: 0x%.2x "
+ "engine escape"
+ "engine:escape:"
+ "initWithMaxBlockSize:"
+ "initWithSlotParameters:"
+ "initialTimeout"
+ "lengthByte: 0x%.2x }"
+ "localeID"
+ "nodeAddressByte: 0x%.2x "
+ "protocolControlByte: 0x%.2x "
+ "securePINChangeSupported"
+ "securePINVerificationSupported"
+ "setDisplayMaxCharracters:"
+ "setDisplayMaxLines:"
+ "setFirmwareVersion:"
+ "setInteractionTimeout:"
+ "setPinValidationCondition:"
+ "setProductID:"
+ "setUint32:at:"
+ "setVendorID:"
+ "slotParameters"
+ "uint32:"
+ "v28@0:8I16Q20"
+ "wLangId: 0x%.4x "
+ "wPINMaxExtraDigit: 0x%.4x "
+ "{ bTimeOut: 0x%.2x "
+ "{ wPINMaxExtraDigit: 0x%.4x "
- "C32@0:8@16^@24"
- "DataView"
- "PINBitOffset"
- "PINBlockByteLength"
- "PINFormatStringFromPINFormat:error:"
- "PINJustification"
- "PINLengthBitOffset"
- "PINLengthBitSize"
- "encoding"
- "engine control"
- "interactionTimeout"
- "langIDFromLocale:"
- "locale"
- "localeIdentifier"
- "maxPINLength"
- "minPINLength"
- "pinBlockStringFromPINFormat:"
- "pinLengthFormatFromPINFormat:error:"
- "pinMaxExtraDigitFromPINFormat:"
- "setMaxInputLength:"
- "setMaxOutputLength:"
- "windowsLocaleCodeFromLocaleIdentifier:"

```
