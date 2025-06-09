## IMDMessageServicesAgent

> `/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/IMDMessageServicesAgent`

```diff

-1402.600.41.2.8
-  __TEXT.__text: 0x6f78
+1436.100.6.2.12
+  __TEXT.__text: 0x6e6c
   __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x334
+  __TEXT.__objc_stubs: 0xc80
+  __TEXT.__objc_methlist: 0x32c
   __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x840
+  __TEXT.__gcc_except_tab: 0x790
   __TEXT.__cstring: 0x2ff
-  __TEXT.__oslogstring: 0xe81
-  __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methtype: 0x342
-  __TEXT.__objc_methname: 0xde2
-  __TEXT.__unwind_info: 0x338
+  __TEXT.__oslogstring: 0xd9f
+  __TEXT.__objc_classname: 0x74
+  __TEXT.__objc_methtype: 0x28c
+  __TEXT.__objc_methname: 0xe4c
+  __TEXT.__unwind_info: 0x318
   __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0x360
   __DATA_CONST.__cfstring: 0x300
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x7d0
-  __DATA.__objc_selrefs: 0x350
-  __DATA.__objc_ivar: 0x68
-  __DATA.__objc_data: 0x190
+  __DATA.__objc_const: 0x770
+  __DATA.__objc_selrefs: 0x368
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__objc_data: 0x140
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73E7EAFA-7D92-3EEC-A2EE-8CEB5D42FF0E
+  UUID: E81E9CD0-445A-34C6-BD93-7EFBC610E8FA
   Functions: 119
-  Symbols:   165
-  CStrings:  321
+  Symbols:   166
+  CStrings:  323
 
Symbols:
+ _IMMessageSummaryInfoEncrypted
CStrings:
+ "@24@0:8^{_IMDAttachmentRecordStruct=}16"
+ "@32@0:8^{_IMDMessageRecordStruct={__CFRuntimeBase=QAQ}q^{__CFArray}^{_IMDHandleRecordStruct}^{_IMDHandleRecordStruct}^{__CFArray}^{__CFDictionary}}16^{_IMDChatRecordStruct=}24"
+ "AttachmentHelpers"
+ "Checking pending route  (Default Text App: %@    SMS Enabled: %@    Fallback Enabled: %@   RCSEnabled: %@)"
+ "DowngradeHelpers"
+ "IMDRoutingAgent"
+ "Message (%@) cannot be sent via SMS because it is not the default text app"
+ "Not getting pending routes (isDefaultTextApp:%@  isSMSEnabled:%@  isSMSFallBackEnabled:%@)"
+ "TB,R,N,GisEncrypted,V_encrypted"
+ "^{_IMDChatRecordStruct=}32@0:8@16^{_IMDMessageRecordStruct={__CFRuntimeBase=QAQ}q^{__CFArray}^{_IMDHandleRecordStruct}^{_IMDHandleRecordStruct}^{__CFArray}^{__CFDictionary}}24"
+ "_encrypted"
+ "boolValue"
+ "encrypted"
+ "isEncrypted"
+ "isMessagesTheDefaultTextApp"
+ "messageSummaryInfo"
- "@24@0:8^{_IMDAttachmentRecordStruct={__CFRuntimeBase=QAQ}q^{__CFArray}}16"
- "@32@0:8^{_IMDMessageRecordStruct={__CFRuntimeBase=QAQ}q^{__CFArray}^{_IMDHandleRecordStruct}^{_IMDHandleRecordStruct}^{__CFArray}^{__CFDictionary}}16^{_IMDChatRecordStruct={__CFRuntimeBase=QAQ}q^{__CFArray}^{__CFArray}q^{_IMDMessageRecordStruct}q}24"
- "Checking pending route  (SMS Enabled: %@    Fallback Enabled: %@   RCSEnabled: %@)"
- "Found %d potential SMS downgrade messages"
- "IMDMSARoutingAgent"
- "IMDMSASMSRoutingAgent"
- "Not getting pending routes (isSMSEnabled:%@  isSMSFallBackEnabled:%@)"
- "Undelivered message watermark is %d"
- "Updating undelivered message watermark to %d"
- "Using 2x lower downgrade interval for upper downgrade interval (%f) for message with GUID {%@}"
- "Using upper downgrade interval (%f) for message with GUID {%@}"
- "Watermark (%d) was greater than sequence number (%d) - resetting"
- "^{_IMDChatRecordStruct={__CFRuntimeBase=QAQ}q^{__CFArray}^{__CFArray}q^{_IMDMessageRecordStruct}q}32@0:8@16^{_IMDMessageRecordStruct={__CFRuntimeBase=QAQ}q^{__CFArray}^{_IMDHandleRecordStruct}^{_IMDHandleRecordStruct}^{__CFArray}^{__CFDictionary}}24"
- "smsRoutingAgent"

```
