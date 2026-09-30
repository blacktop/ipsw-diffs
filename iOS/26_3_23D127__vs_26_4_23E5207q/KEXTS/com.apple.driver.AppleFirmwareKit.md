## com.apple.driver.AppleFirmwareKit

> `com.apple.driver.AppleFirmwareKit`

```diff

-634.80.4.0.0
-  __TEXT.__cstring: 0x4d05
+634.100.47.0.0
+  __TEXT.__cstring: 0x4d3f
   __TEXT.__const: 0xb8
-  __TEXT.__os_log: 0x142e
-  __TEXT_EXEC.__text: 0x49770
+  __TEXT.__os_log: 0x1438
+  __TEXT_EXEC.__text: 0x45534
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x7c8
   __DATA.__bss: 0x20
-  __DATA_CONST.__auth_got: 0x520
+  __DATA_CONST.__auth_got: 0x530
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x118
   __DATA_CONST.__mod_term_func: 0x118
-  __DATA_CONST.__const: 0xfac8
+  __DATA_CONST.__const: 0xfa50
   __DATA_CONST.__kalloc_type: 0x1b40
-  UUID: 6862E907-9BE9-3512-9609-AFD49A4F713D
-  Functions: 2340
+  UUID: 874ADBEB-A06D-382F-8DD1-33B2C5A8DDA0
+  Functions: 2360
   Symbols:   0
-  CStrings:  736
+  CStrings:  735
 
CStrings:
+ "\"0 != size\" @%s:%d"
+ "\"0 != status\" @%s:%d"
+ "\"AFKEPMessage::TypeBuffer == messages[0].type && sizeCheck\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from getData\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid result returned from removeData\" @%s:%d"
+ "\"TB_FATAL: \" \"invalid tag in `[UInt8]` metadata: 0x%x\" @%s:%d"
+ "\"TB_FATAL: \" \"overflow detected when adding\" @%s:%d"
+ "\"afk_mem_get_paddr(this->_rspPayload) == oobHdr.rspAddress\" @%s:%d"
+ "\"messages[0].buffer.size() >= sizeof(*header)\" @%s:%d"
+ "\"nullptr != data\" @%s:%d"
+ "\"nullptr != this->storage.data()\" @%s:%d"
+ "\"oobHdr.rspSize <= this->_oobHdr.rspSize\" @%s:%d"
+ "\"sizeCheck\" @%s:%d"
+ "\"this->_pending.size() + messages[0].buffer.size() <= this->_pending.capacity()\" @%s:%d"
+ "/Library/Caches/com.apple.xbs/4A559DA7-7D27-4973-AF00-F436AD2B74AF/TemporaryDirectory.vGjAJd/Sources/AppleFirmwareKit_kext/src/Kext/AFKFirmwareService.cpp"
+ "1121222221112"
+ "112222211112"
+ "12111112122212121121111211111222111121211112211112222"
+ "[%s:%p] Unknown message '%x'\n"
+ "[AFKEPInterfaceV2:%p]Unexpected Response (pktLen %zu pktType 0x%x commandID:%i)\n"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[64c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "\"0 == remaining\" @%s:%d"
- "\"TB_FATAL: \" \"invalid tag in array metadata: 0x%x\" @%s:%d"
- "\"_storage\" @%s:%d"
- "\"afk_mem_get_paddr(this->_rspPayload) == oobHdr->rspAddress\" @%s:%d"
- "\"messages[0].buffer.size >= sizeof(*header)\" @%s:%d"
- "\"msgsIn[0].buffer.size - sizeof(*header) >= sizeof(*commHeader)\" @%s:%d"
- "\"msgsIn[0].buffer.size >= sizeof(*header)\" @%s:%d"
- "\"pktLen >= sizeof(*header)\" @%s:%d"
- "\"pktLen >= sizeof(*respHeader)\" @%s:%d"
- "\"pktLen >= sizeof(rv->_commandHeader) + sizeof(rv->_oobHdr)\" @%s:%d"
- "\"pktLen >= sizeof(rv->_commandHeader)\" @%s:%d"
- "\"rspSize <= this->_oobHdr.rspSize\" @%s:%d"
- "\"status\" @%s:%d"
- "\"this->_pendingOffset + pktLen <= this->_pendingSize\" @%s:%d"
- "\"valid && pktLen <= 4294967295U\" @%s:%d"
- "/Library/Caches/com.apple.xbs/Sources/AppleFirmwareKit_kext/src/Kext/AFKFirmwareService.cpp"
- "112121222221112"
- "112222211121"
- "1211111212221212112111121111122212121211112211112222"
- "[%s:%p] Unk mess %x\n"
- "[AFKEPInterfaceV2:%p]Unexpected Response (pktLen %i pktType 0x%x commandID:%i)\n"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[41c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"

```
