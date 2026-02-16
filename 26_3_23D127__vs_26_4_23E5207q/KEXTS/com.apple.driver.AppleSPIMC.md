## com.apple.driver.AppleSPIMC

> `com.apple.driver.AppleSPIMC`

```diff

-34.0.0.0.0
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x1232
-  __TEXT_EXEC.__text: 0x71e0
+37.0.0.0.0
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x1757
+  __TEXT_EXEC.__text: 0x6fc4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x68
   __DATA_CONST.__auth_got: 0x128
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x840
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: B6FE7228-7904-3DFD-AFEA-F3499D71DF95
-  Functions: 124
+  __DATA_CONST.__kalloc_var: 0xa0
+  UUID: E348CB5E-2D8F-3EA0-9252-51C35053B5E2
+  Functions: 131
   Symbols:   0
-  CStrings:  129
+  CStrings:  165
 
CStrings:
+ "%s: %s, %s, direction %#x, status %#x, %#x\n"
+ "%s: %s, %s, status %#x, resid %#x\n"
+ "%s: %s: sleeping...\n"
+ "%s: %s: stopDMACommand error %x\n"
+ "%s: %s: woke %d, status %#x\n"
+ "%s: No hardware delay: pre=%#llX pst=%#llX kCS=%llX CSs=%d ics=%d enabled=%d\n"
+ "%s: USING hardware delay pre: %d post: %d\n"
+ "%s: _spiCommand is NULL\n"
+ "%s: command completed status=0x%08x, time=%lluns\n"
+ "%s: direction %s, status %#x\n"
+ "%s: tx end cmd=%p, status=0x%08x, time=%llxns\n"
+ "%s:%s: %s, %s, direction %#x, status %#x, %#x\n"
+ "%s:%s: %s, %s, status %#x, resid %#x\n"
+ "%s:%s: %s: sleeping...\n"
+ "%s:%s: %s: stopDMACommand error %x\n"
+ "%s:%s: %s: woke %d, status %#x\n"
+ "%s:%s: No hardware delay: pre=%#llX pst=%#llX kCS=%llX CSs=%d ics=%d enabled=%d\n"
+ "%s:%s: SPCON programmed status=0x%08x\n"
+ "%s:%s: Thread timeout premature, dt %lld, status=0x%08x\n"
+ "%s:%s: USING hardware delay pre: %d post: %d\n"
+ "%s:%s: _spiCommand is NULL\n"
+ "%s:%s: active cmd=%p, status=0x%08x\n"
+ "%s:%s: active=%d\n"
+ "%s:%s: command completed status=0x%08x, time=%lluns\n"
+ "%s:%s: direction %s, status %#x\n"
+ "%s:%s: enabled status=0x%08x\n"
+ "%s:%s: idle off\n"
+ "%s:%s: inactive cmd=%p, status=0x%08x\n"
+ "%s:%s: interrupt done break, status=0x%08x\n"
+ "%s:%s: interrupt done, status=0x%08x\n"
+ "%s:%s: rx end/tx start cmd=%p, status=0x%08x\n"
+ "%s:%s: rx start cmd=%p, status=0x%08x\n"
+ "%s:%s: start cmd=%p, status=0x%08x\n"
+ "%s:%s: status=0x%08x, _spiCommandDone=%d\n"
+ "%s:%s: status=0x%08x, _spiConReg=0x%08x, _spiConRegCurrent=0x%08x\n"
+ "%s:%s: thread awakened status=0x%08x, _spiCommandDone=%d\n"
+ "%s:%s: thread timeout, polling status=0x%08x\n"
+ "%s:%s: timeout panicked, status=0x%08x\n"
+ "%s:%s: tx end cmd=%p, status=0x%08x, time=%llxns\n"
+ "(_spiIES != NULL) || (_spiPollCtl.enable != 0)"
+ "(_spiRxCount == 0 || spiCommand->rxBufferMD != NULL) && (_spiTxCount == 0 || spiCommand->txBufferMD != NULL)"
+ "(_spiRxCount == 0) || (_spiRxBuffer != NULL)"
+ "(_spiTxCount == 0) || (_spiTxBuffer != NULL)"
+ "/Library/Caches/com.apple.xbs/CB3FA874-3A29-4F39-BC3C-E055086965E7/TemporaryDirectory.B52OCq/Sources/AppleSPIMC/Kernel/AppleSPIMC.cpp"
+ "1"
+ "_spiRxDMAES != NULL"
+ "_spiTxDMAES != NULL"
+ "autoPollCount != nullptr"
+ "descs != NULL"
+ "descs allocation failed"
+ "disb_intrs_active != nullptr"
+ "disb_intrs_inactive != nullptr"
+ "exec_array != nullptr"
+ "intrTimeouts != nullptr"
+ "multiDesc != NULL"
+ "osn != nullptr"
+ "pollTimeouts != nullptr"
+ "poll_array != nullptr"
+ "poll_hist_count != nullptr"
+ "result == kIOReturnSuccess"
+ "site.IOMemoryDescriptor *"
+ "size_array != nullptr"
+ "spiCommand->rxByteCount <= UINT32_MAX"
+ "spiCommand->spiCompletion.target == NULL"
+ "spiCommand->txByteCount <= UINT32_MAX"
+ "xfer_array != nullptr"
+ "xfer_hist_count != nullptr"
- "%s %s::%s:%d: %s, %s, direction %#x, status %#x, %#x\n"
- "%s %s::%s:%d: %s, %s, status %#x, resid %#x\n"
- "%s %s::%s:%d: %s: sleeping... \n"
- "%s %s::%s:%d: %s: stopDMACommand error %x\n"
- "%s %s::%s:%d: %s: woke %d, status %#x\n"
- "%s %s::%s:%d: No hardware delay: pre%#llX pst%#llX kCS%llX CSs%d ics%d enabled%d\n"
- "%s %s::%s:%d: Thread timeout premature, dt %lld\n"
- "%s %s::%s:%d: USING hardware delay pre: %d post: %d\n"
- "%s %s::%s:%d: Wakeup on command not done\n"
- "%s %s::%s:%d: _spiCommand is NULL\n"
- "%s %s::%s:%d: direction %s, status %#x\n"
- "%s: command completed status=0x%08x, time=%llu\n"
- "%s: interrupt, status=0x%08x\n"
- "%s: tx end cmd=%p, status=0x%08x, time=%lx\n"
- "(_spiIES != nullptr) || (_spiPollCtl.enable != 0)"
- "(_spiRxCount == 0 || spiCommand->rxBufferMD != nullptr) && (_spiTxCount == 0 || spiCommand->txBufferMD != nullptr)"
- "(_spiRxCount == 0) || (_spiRxBuffer != nullptr)"
- "(_spiTxCount == 0) || (_spiTxBuffer != nullptr)"
- "/Library/Caches/com.apple.xbs/Sources/AppleSPIMC/Kernel/AppleSPIMC.cpp"
- "_spiRxDMAES != nullptr"
- "_spiTxDMAES != nullptr"
- "exec_array"
- "multiDesc != nullptr"
- "osn"
- "poll_array"
- "result == 0"
- "size_array"
- "spiCommand->rxByteCount <= 4294967295U"
- "spiCommand->spiCompletion.target == nullptr"
- "spiCommand->txByteCount <= 4294967295U"
- "xfer_array"

```
