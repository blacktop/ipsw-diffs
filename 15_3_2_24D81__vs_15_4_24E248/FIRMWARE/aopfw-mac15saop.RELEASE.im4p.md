## aopfw-mac15saop.RELEASE.im4p

> `aopfw-mac15saop.RELEASE.im4p`

```diff

 
-  __TEXT.__text: 0x9b6a8
-  __TEXT.__const: 0x5460
-  __TEXT.__cstring: 0x5c98
+  __TEXT.__text: 0x9b100
+  __TEXT.__const: 0x5408
+  __TEXT.__cstring: 0x5e5b
   __TEXT.__chain_starts: 0x3c
   __DATA._rtk_boot: 0x3000
   __DATA._rtk_page_tables: 0x5000

   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x2ff68
   __DATA.__const: 0x9de0
-  __DATA.__data: 0x9280
-  __DATA._rtk_patchbay: 0x315
+  __DATA.__data: 0x9358
   __DATA._spu_service: 0x3c0
   __DATA._spu_endpoint: 0x48
   __DATA._rtk_power: 0x3b8
+  __DATA._rtk_patchbay: 0x305
   __DATA.__cmevent: 0x330
   __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__gxf_data: 0x10
-  __DATA.__mod_init_func: 0x128
+  __DATA.__mod_init_func: 0x120
   __DATA.__version: 0x8
   __DATA.__constructor: 0x0
-  __DATA._rtk_mtab: 0x640
-  __DATA.__zerofill: 0xb9478
+  __DATA._rtk_mtab: 0x628
+  __DATA.__zerofill: 0xb9360
   __ETEXT.__eh_frame: 0x40
-  __ETEXT.__text: 0x16078
-  __ETEXT.__StaticInit: 0x2c84
+  __ETEXT.__text: 0x16084
+  __ETEXT.__StaticInit: 0x2bb8
   __ETEXT.__const: 0xb61
-  __OS_LOG.__string: 0x1223b
+  __OS_LOG.__string: 0x123f1
   __MISC.__apf_list: 0x70
   __CMA.__cma_log_string: 0x11b3
-  UUID: 7F9F594E-65DD-328D-A29C-856D80BD8F38
-  Functions: 2423
+  UUID: B0C1D4FA-B0E6-3506-97CD-5E57D9BB832C
+  Functions: 2561
   Symbols:   0
-  CStrings:  1862
+  CStrings:  1879
 
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
+ "DescramblerT6030.cpp"
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
