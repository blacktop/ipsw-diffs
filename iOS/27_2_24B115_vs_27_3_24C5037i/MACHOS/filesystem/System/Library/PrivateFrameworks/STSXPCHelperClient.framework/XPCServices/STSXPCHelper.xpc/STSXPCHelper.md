## STSXPCHelper

> `/System/Library/PrivateFrameworks/STSXPCHelperClient.framework/XPCServices/STSXPCHelper.xpc/STSXPCHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
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

-6.1.3.0.0
-  __TEXT.__text: 0x39b60
+6.2.1.0.0
+  __TEXT.__text: 0x3a0fc
   __TEXT.__auth_stubs: 0xb00
   __TEXT.__delay_helper: 0x114
-  __TEXT.__objc_stubs: 0x46c0
+  __TEXT.__objc_stubs: 0x46e0
   __TEXT.__objc_methlist: 0x28e8
   __TEXT.__const: 0x158
-  __TEXT.__objc_methname: 0x62b7
-  __TEXT.__cstring: 0x9626
+  __TEXT.__objc_methname: 0x62c9
+  __TEXT.__cstring: 0x9841
   __TEXT.__objc_classname: 0x7d7
   __TEXT.__objc_methtype: 0x1f01
-  __TEXT.__gcc_except_tab: 0x7bc
+  __TEXT.__gcc_except_tab: 0x7f0
   __TEXT.__oslogstring: 0xb4e
   __TEXT.__ustring: 0x34c
-  __TEXT.__unwind_info: 0xd40
-  __DATA_CONST.__const: 0xe90
-  __DATA_CONST.__cfstring: 0x5d60
+  __TEXT.__unwind_info: 0xd50
+  __DATA_CONST.__const: 0xfe0
+  __DATA_CONST.__cfstring: 0x5ee0
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc0

   __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x2f0
   __DATA.__objc_const: 0x6228
-  __DATA.__objc_selrefs: 0x17f0
+  __DATA.__objc_selrefs: 0x17f8
   __DATA.__objc_ivar: 0x4e4
   __DATA.__objc_data: 0x1360
   __DATA.__data: 0xa64

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 962
+  Functions: 965
   Symbols:   292
-  CStrings:  2536
+  CStrings:  2561
 
CStrings:
+ "-[STSISO18013Handler _collectExchangeTLVs:length:parentTag:exchangeEvent:display:]"
+ "-[STSISO18013Handler _parseExchangePayload:]"
+ "-[STSISO18013Handler _readerStatusErrorFromExchangeEvent:]"
+ "<%zu bytes>"
+ "EventType"
+ "Invalid address length : %lu"
+ "MailboxAtomicSession"
+ "MailboxRead"
+ "MailboxSet"
+ "MailboxWrite"
+ "Not enough room for TLV in 0x%X: %zu bytes left"
+ "ParseError"
+ "PayloadLength"
+ "ReaderErrorCode"
+ "ReaderFirmwareVersion"
+ "ReaderProductID"
+ "ReaderStatus"
+ "ReaderStatusDescription"
+ "ReaderVendorID"
+ "STS generated event = %@"
+ "StepUpEvent"
+ "Tag%X.%X"
+ "URSKRequested"
+ "UpdateDocument"
+ "arrayWithObjects:"
+ "malformed TLV in 0x%X, %zu bytes left"
- "-[STSISO18013Handler _extractContentFromTag97:]"
```
