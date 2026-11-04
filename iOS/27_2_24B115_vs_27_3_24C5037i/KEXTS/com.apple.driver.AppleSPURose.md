## com.apple.driver.AppleSPURose

> `com.apple.driver.AppleSPURose`

```diff

-1087.40.4.0.0
+1087.60.2.0.0
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x23e8
-  __TEXT.__os_log: 0x1d58
-  __TEXT_EXEC.__text: 0x1783c
+  __TEXT.__cstring: 0x2598
+  __TEXT.__os_log: 0x1dfa
+  __TEXT_EXEC.__text: 0x17bfc
   __TEXT_EXEC.__auth_stubs: 0x500
   __DATA.__data: 0x248
   __DATA.__common: 0x268

   __DATA_CONST.__kalloc_type: 0x3c0
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0xd0
-  Functions: 670
+  Functions: 678
   Symbols:   0
-  CStrings:  378
+  CStrings:  386
 
CStrings:
+ "arguments->structureOutputDescriptorSize >= sizeof(RTKitCrashlogInfo)"
+ "arguments->structureOutputDescriptorSize >= sizeof(RoseCoredumpDescriptor)"
+ "arguments->structureOutputSize >= sizeof(RTKitCrashlogInfo)"
+ "arguments->structureOutputSize >= sizeof(RoseCoredumpDescriptor)"
+ "payload != nullptr"
+ "size >= (hdrSize + sizeof(RoseRxPacketHeader))"
+ "size >= sizeof(RTKitOSRxPacketHeader)"
+ "size >= sizeof(RoseErrorReportHeader)"
+ "size >= sizeof(RoseRxPacketHeader)"
- "hdr != nullptr"
```
