## aopfw-mac15jaop.RELEASE.im4p

> `aopfw-mac15jaop.RELEASE.im4p`

```diff

 
-  __TEXT.__text: 0xa7ec4
-  __TEXT.__const: 0x5440
-  __TEXT.__cstring: 0x5cd0
+  __TEXT.__text: 0xac0d4
+  __TEXT.__const: 0x53d8
+  __TEXT.__cstring: 0x5e7e
   __TEXT.__chain_starts: 0x44
   __DATA._rtk_boot: 0x3000
-  __DATA.__mod_init_func: 0x128
+  __DATA.__mod_init_func: 0x120
   __DATA._rtk_page_tables: 0x5000
   __DATA._spu_stack: 0x2000
   __DATA._rtk_init_stack: 0x2000

   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x2ff68
   __DATA.__const: 0x9dd8
-  __DATA.__data: 0x9140
-  __DATA._rtk_patchbay: 0x315
+  __DATA.__data: 0x9218
   __DATA._spu_service: 0x3c0
   __DATA._spu_endpoint: 0x48
   __DATA._rtk_power: 0x3b8
+  __DATA._rtk_patchbay: 0x305
   __DATA.__cmevent: 0x330
-  __DATA._rtk_mtab: 0x640
+  __DATA._rtk_mtab: 0x628
   __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__gxf_data: 0x10
   __DATA.__version: 0x8
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xb9b98
-  __ETEXT.__StaticInit: 0x2d88
+  __DATA.__zerofill: 0xb9c60
+  __ETEXT.__StaticInit: 0x2cac
   __ETEXT.__eh_frame: 0x40
-  __ETEXT.__text: 0x16054
+  __ETEXT.__text: 0x16060
   __ETEXT.__const: 0xb61
-  __OS_LOG.__string: 0x122f6
+  __OS_LOG.__string: 0x124ac
   __MISC.__apf_list: 0x70
   __CMA.__cma_log_string: 0x11b3
-  UUID: 3DC5E32D-8804-3ED6-9E8F-4563292E1F4E
-  Functions: 2632
+  UUID: FB65DD4F-EAA9-3304-83BA-201FB691D345
+  Functions: 3277
   Symbols:   0
-  CStrings:  1864
+  CStrings:  1880
 
CStrings:
+ "!instance->ap_mbox & !instance->external & instance->is_inbox"
+ "!instance->ap_mbox & instance->external & instance->is_inbox"
+ "+ %s::%s(%d %s)"
+ "- %s::%s(kEndpointWillPowerOff)"
+ "- %s::%s(kEndpointWillPowerOffNoWake)"
+ "18:48:29"
+ "18:57:19"
+ "???"
+ "AppleSPUFirmware-2001.100.83~151"
+ "Cntl"
+ "Mar  7 2025"
+ "RTKitAudioFramework v440.12 (built %s %s) ready!! {%zu nodes}"
+ "Resume"
+ "SMCSensorExchange: Can't find matching service for sensor sample!"
+ "SMCSensorExchange: Could not find %s service, skipping..."
+ "SMCSensorExchange: Expecting %s service but failed to find"
+ "SMCSensorExchange: Missing smc service!"
+ "SMCSensorExchange: SMC lid threshold received, expected %lu bytes, got %lu bytes"
+ "SMCSensorExchange: Unsupported sensor type: 0x%x"
+ "WillHibernate"
+ "aop-audprovr2 v440.4 built %s %s, %c%c%c%c state"
+ "cond \"!(1 > inArgc)\" fail, %s() ln 634, stat %#x"
+ "cond \"!(inArgs->payloadBytes > (inBufferSize - sizeof(struct Interface::SetNodePropertyInputSubPacket)))\" fail, %s() ln 527, stat %#x"
+ "cond \"!(sizeof(RegisterAccess::PacketHeader) + packet->header.addressWidth > inBufferSize)\" fail, %s() ln 563, stat %#x"
+ "cond \"curSt.isSingleStep(reqSt)\" fail, %s() ln 518, stat %#x"
+ "cond \"inPropertyDataSize == sizeof(uint32_t)\" fail, %s() ln 354, stat %#x"
+ "cond \"outSize <= inoutDataSize\" fail, %s() ln 698, stat %#x"
+ "cond \"sizeof(uint32_t) * (count+1) < inoutDataSize\" fail, %s() ln 742, stat %#x"
+ "cond \"validDataBytesSize\" fail, %s() ln 603, stat %#x"
+ "exp \"_processStateChangeRequest(&req)\" fail, %s(), ln 694, stat %#x"
+ "exp \"_processStateChangeRequest(reqPtr)\" fail, %s(), ln 338, stat %#x"
+ "exp \"getProvider()->processCommand(buf, kPacketLen, nullptr, 0)\" fail, %s(), ln 371, stat %#x"
+ "exp \"kIOReturnBadArgument\" fail, %s(), ln 440, stat %#x"
+ "exp \"mImpl.start()\" fail, %s(), ln 297, stat %#x"
+ "exp \"mImpl.systemReady()\" fail, %s(), ln 352, stat %#x"
+ "exp \"pingRet\" fail, %s(), ln 385, stat %#x"
+ "exp \"sLocalInterface.powerStateChange(kProcIdAP, RTKitAudioFramework::kPowerStateOff)\" fail, %s(), ln 619, stat %#x"
+ "exp \"sLocalInterface.powerStateChange(kProcIdAP, RTKitAudioFramework::kPowerStateOn)\" fail, %s(), ln 622, stat %#x"
+ "exp \"setNodeProperty(inNodeId, inPropertyId, inPayload, inArgs->payloadBytes)\" fail, %s(), ln 529, stat %#x"
+ "exp \"super::_setProperty(inProperty, inPropertyData, inPropertyDataSize)\" fail, %s(), ln 391, stat %#x"
+ "fail, stat %#x, %s(), ln 641"
+ "handleHibernationNotification"
+ "instance->ap_mbox & !instance->external & !instance->is_inbox"
+ "instance->ap_mbox & !instance->external & instance->is_inbox"
+ "instance->ap_mbox & instance->external & !instance->is_inbox"
+ "instance->ap_mbox & instance->external & instance->is_inbox"
+ "ptr \"destNode\" is null, cant cont, %s(), ln 882, stat %#x"
+ "ptr \"inBuffer\" is null, cant cont, %s(), ln 422, stat %#x"
+ "ptr \"inBuffer\" is null, cant cont, %s(), ln 459, stat %#x"
+ "ptr \"inPropertyData\" is null, cant cont, %s(), ln 353, stat %#x"
+ "ptr \"inPropertyData\" is null, cant cont, %s(), ln 491, stat %#x"
+ "ptr \"outPropertyData\" is null, cant cont, %s(), ln 790, stat %#x"
+ "ptr \"outPropertySize\" is null, cant cont, %s(), ln 791, stat %#x"
+ "ptr \"pDevice\" is null, cant cont, %s(), ln 496, stat %#x"
+ "ptr \"pNode\" is null, cant cont, %s(), ln 672, stat %#x"
+ "ptr \"pNode\" is null, cant cont, %s(), ln 795, stat %#x"
+ "ptr \"pNode\" is null, cant cont, %s(), ln 831, stat %#x"
- "17:45:56"
- "17:57:42"
- "AppleSPUFirmware-2001.80.4~53"
- "Can't find matching service for sensor sample!"
- "Could not find %s service, skipping..."
- "Dec 13 2024"
- "Missing smc service!"
- "RTKitAudioFramework v420.10 (built %s %s) ready!! {%zu nodes}"
- "SMC lid threshold received, expected %lu bytes, got %lu bytes"
- "Unsupported sensor type: 0x%x"
- "aop-audprovr2 v420.7 built %s %s, %c%c%c%c state"
- "cond \"!(1 > inArgc)\" fail, %s() ln 638, stat %#x"
- "cond \"curSt.isSingleStep(reqSt)\" fail, %s() ln 520, stat %#x"
- "cond \"inPropertyDataSize == sizeof(uint32_t)\" fail, %s() ln 356, stat %#x"
- "cond \"outSize <= inoutDataSize\" fail, %s() ln 697, stat %#x"
- "cond \"sizeof(uint32_t) * (count+1) < inoutDataSize\" fail, %s() ln 741, stat %#x"
- "cond \"validDataBytesSize\" fail, %s() ln 607, stat %#x"
- "exp \"_processStateChangeRequest(&req)\" fail, %s(), ln 696, stat %#x"
- "exp \"_processStateChangeRequest(reqPtr)\" fail, %s(), ln 340, stat %#x"
- "exp \"getProvider()->processCommand(buf, kPacketLen, nullptr, 0)\" fail, %s(), ln 370, stat %#x"
- "exp \"kIOReturnBadArgument\" fail, %s(), ln 439, stat %#x"
- "exp \"mImpl.start()\" fail, %s(), ln 295, stat %#x"
- "exp \"mImpl.systemReady()\" fail, %s(), ln 339, stat %#x"
- "exp \"pingRet\" fail, %s(), ln 387, stat %#x"
- "exp \"sLocalInterface.powerStateChange(kProcIdAP, RTKitAudioFramework::kPowerStateOff)\" fail, %s(), ln 595, stat %#x"
- "exp \"sLocalInterface.powerStateChange(kProcIdAP, RTKitAudioFramework::kPowerStateOn)\" fail, %s(), ln 598, stat %#x"
- "exp \"setNodeProperty(inNodeId, inPropertyId, inPayload, inArgs->payloadBytes)\" fail, %s(), ln 531, stat %#x"
- "exp \"super::_setProperty(inProperty, inPropertyData, inPropertyDataSize)\" fail, %s(), ln 393, stat %#x"
- "fail, stat %#x, %s(), ln 645"
- "ptr \"destNode\" is null, cant cont, %s(), ln 886, stat %#x"
- "ptr \"inBuffer\" is null, cant cont, %s(), ln 408, stat %#x"
- "ptr \"inBuffer\" is null, cant cont, %s(), ln 445, stat %#x"
- "ptr \"inPropertyData\" is null, cant cont, %s(), ln 355, stat %#x"
- "ptr \"inPropertyData\" is null, cant cont, %s(), ln 477, stat %#x"
- "ptr \"outPropertyData\" is null, cant cont, %s(), ln 794, stat %#x"
- "ptr \"outPropertySize\" is null, cant cont, %s(), ln 795, stat %#x"
- "ptr \"pDevice\" is null, cant cont, %s(), ln 482, stat %#x"
- "ptr \"pNode\" is null, cant cont, %s(), ln 676, stat %#x"
- "ptr \"pNode\" is null, cant cont, %s(), ln 799, stat %#x"
- "ptr \"pNode\" is null, cant cont, %s(), ln 835, stat %#x"
- "ptr \"reqPtr\" is null, cant cont, %s(), ln 339, stat %#x"

```
