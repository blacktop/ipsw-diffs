## com.apple.iokit.IODisplayPortFamily

> `com.apple.iokit.IODisplayPortFamily`

```diff

-739.120.3.0.0
-  __TEXT.__cstring: 0x7d78
-  __TEXT.__os_log: 0x950b
+762.0.0.0.0
+  __TEXT.__cstring: 0x8808
+  __TEXT.__os_log: 0xa003
   __TEXT.__const: 0x440
-  __TEXT_EXEC.__text: 0x5bca0
+  __TEXT_EXEC.__text: 0x629f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x550
+  __DATA.__common: 0x5d8
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x540
+  __DATA_CONST.__auth_got: 0x578
   __DATA_CONST.__got: 0x170
-  __DATA_CONST.__mod_init_func: 0x110
-  __DATA_CONST.__mod_term_func: 0x108
-  __DATA_CONST.__const: 0xf8c8
-  __DATA_CONST.__kalloc_type: 0x840
+  __DATA_CONST.__mod_init_func: 0x120
+  __DATA_CONST.__mod_term_func: 0x118
+  __DATA_CONST.__const: 0x119f0
+  __DATA_CONST.__kalloc_type: 0x900
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 38104920-B3DE-3B3E-A5BF-50B4B2FEEBF6
-  Functions: 2355
+  UUID: EAA1F5F5-2421-3F67-9EB8-6EE1AC63269F
+  Functions: 2557
   Symbols:   0
-  CStrings:  1525
+  CStrings:  1640
 
CStrings:
+ "\"%s::%s(0x%llx): deactivate() incomplete %u seconds after displayRelease()! (check DCPEXT)\\n\" @%s:%d"
+ "1211111212221212111112222211111111111122222222222222222222222222222222222"
+ "121111121222121211111222221111111111112222222222222222222222222222222222211122"
+ "1211111212221212111112222211111111111122222222222222222222222222222222222222"
+ "121111121222121211122222111111111122212222212222222122222122222122222222222222222222222222222222222222222222222222211111111121111111122221111112222222222222222222222221"
+ "1211111212221212111222221111111111222122222122222221222221222221222222222222222222222222222222222222222222222222222111111111211111111222211111122222222222222222222222211"
+ "1211111212221212111222221111111111222122222122222221222221222221222222222222222222222222222222222222222222222222222111111111211111111222211111122222222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "121111121222121211122222222222222222222222222222222222221211121111111112222222222222222222222222222222222111111112222222222222222222222222222222222222222222222222222222222"
+ "1211111212221212111222222222222222222222222222222222222212111211111111122222222222222222222222222222222221111111122222222222222222222222222222222222222222222222222222222221112"
+ "1211111212221212112222211"
+ "A44614"
+ "AV Device published %lld..\n"
+ "B16@?0^{IODPTXPort=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^^?^^?^^?^^?i[8I]^{IODPSwitch}^{IOService}^{IODPTXPort}^{IOWorkLoop}^{IOCommandGate}^{IODPTXPortEventLog}^{IOTimerEventSource}^?^?^?^?^{thread_call}B{ActionQueue=[128{Action=C}]CCC}B{IODPTXPortAttributes=Cb1b1b3b3b16{IODPTXPortAddress=b4b4b2b5b1b16}}BBBBBBBBBiBB{?={?=b1b1b6}Cb16b32{?=II}{IOAVTiledDisplayInfo={?={?=[3C]}SI}{?=b1b1b1b1b4}b16b32{?=SSSS}{?=II}{?=II}}{?=IIIIb8b8Cb8}[16C][16c]}Bi}8"
+ "DP Device published %lld..\n"
+ "IOAV[%d] %s<0x%llx>::%s: AV Device published %lld..\n"
+ "IOAV[%d] %s<0x%llx>::%s: DP Device published %lld..\n"
+ "IOAV[%d] %s<0x%llx>::%s: IODPPortAnalyticsCollector::init failed\n"
+ "IOAV[%d] %s<0x%llx>::%s: IODPPortService failed to start\n"
+ "IOAV[%d] %s<0x%llx>::%s: IOTimerEventSource::timerEventSource(...) failed\n"
+ "IOAV[%d] %s<0x%llx>::%s: IOWorkLoop::workLoop() failed\n"
+ "IOAV[%d] %s<0x%llx>::%s: Ignoring %s event, dpTransportAvailable=%s, portActivated=%s\n"
+ "IOAV[%d] %s<0x%llx>::%s: Ignoring %s event, dpTransportAvailable=%s, portActivated=%s, _hpdAsserted=%s\n"
+ "IOAV[%d] %s<0x%llx>::%s: Not able to create Property %s\n"
+ "IOAV[%d] %s<0x%llx>::%s: Passed EDID: data=%p size=%d\n"
+ "IOAV[%d] %s<0x%llx>::%s: Property %s does not exist\n"
+ "IOAV[%d] %s<0x%llx>::%s: Pushing virtual DPCD...\n"
+ "IOAV[%d] %s<0x%llx>::%s: Pushing virtual EDID...\n"
+ "IOAV[%d] %s<0x%llx>::%s: Requesting re-registration of port\n"
+ "IOAV[%d] %s<0x%llx>::%s: Restoring virtual mode %d\n"
+ "IOAV[%d] %s<0x%llx>::%s: Sleeping on commandGate until EDID is available..\n"
+ "IOAV[%d] %s<0x%llx>::%s: Writing Virtual DPCD bytes - address=0x%x, length=%d, index=%d\n"
+ "IOAV[%d] %s<0x%llx>::%s: _waitingVirtualEDID=%d..\n"
+ "IOAV[%d] %s<0x%llx>::%s: _workLoop->addEventSource(_deactivateTimeoutSource) failed\n"
+ "IOAV[%d] %s<0x%llx>::%s: domain%d: connectTo ufp %s,%d to dfp %s,%d ret=0x%08x\n"
+ "IOAV[%d] %s<0x%llx>::%s: failed to allocate IODPPortService\n"
+ "IOAV[%d] %s<0x%llx>::%s: failed to init IODPPortService\n"
+ "IOAV[%d] %s<0x%llx>::%s: message=%s dpTransportAvailable=%s\n"
+ "IOAV[%d] %s<0x%llx>::%s: notice: forwarding inactive sink notification on idle port...\n"
+ "IOAV[%d] %s<0x%llx>::%s: notice: ignoring %s event during system sleep.\n"
+ "IOAV[%d] %s<0x%llx>::%s: notice: ignoring %s event on inactive port.\n"
+ "IOAV[%d] %s<0x%llx>::%s: notice: ignoring DisplayRequest during system sleep.\n"
+ "IOAV[%d] %s<0x%llx>::%s: notice: ignoring IRQ_HPD event during system sleep.\n"
+ "IOAV[%d] %s<0x%llx>::%s: notice: ignoring IRQ_HPD event on inactive port.\n"
+ "IOAV[%d] %s<0x%llx>::%s: releasing display...\n"
+ "IOAV[%d] %s<0x%llx>::%s: setting virtual mode, new=%d, old=%d\n"
+ "IOAV[%d] %s<0x%llx>::%s: superclass ret=0x%08x\n"
+ "IOAV[%d] %s<0x%llx>::%s: synthesizing displayRequest due to !_displayAllocated...\n"
+ "IOAV[%d] %s<0x%llx>::%s: synthesizing hotPlugDetectChangeOccurred due to _hpdAsserted...\n"
+ "IOAV[%d] %s<0x%llx>::%s: synthesizing message=%s: HPD %u->%u\n"
+ "IOAV[%d] %s<0x%llx>::%s: warning: Ignoring port events from transport for virtual mode\n"
+ "IOAV[%d] %s<0x%llx>::%s: warning: failed to read LTTPR ret=0x%08x"
+ "IOAV[%d] %s<0x%llx>::%s: warning: ignoring inactive sink notification on inactive port.\n"
+ "IOAV[%d] %s<0x%llx>::%s: warning: ignoring redundant deactivate()\n"
+ "IOAV[%d] %s<0x%llx>::%s: writing I2C to virtual device i2cAddr=%x, offset=%x, length=%d\n"
+ "IODPHDMIControllerPortUserInterfaceSupported"
+ "IODPPortAnalyticsCollector"
+ "IODPPortAnalyticsCollector::init failed\n"
+ "IODPPortService"
+ "IODPPortService failed to start\n"
+ "IODPPortService.cpp"
+ "IODPPortUserClient"
+ "IODPPortUserInterfaceSupported"
+ "IODPTXVirtualPort"
+ "IODPTXVirtualPort.cpp"
+ "IODPVirtualPortService"
+ "IOTimerEventSource::timerEventSource(...) failed\n"
+ "IOWorkLoop::workLoop() failed\n"
+ "Ignoring %s event, dpTransportAvailable=%s, portActivated=%s\n"
+ "Ignoring %s event, dpTransportAvailable=%s, portActivated=%s, _hpdAsserted=%s\n"
+ "Message"
+ "Not able to create Property %s\n"
+ "Passed EDID: data=%p size=%d\n"
+ "PortNumber"
+ "PortType"
+ "PortVariant"
+ "Property %s does not exist\n"
+ "Pushing virtual DPCD...\n"
+ "Pushing virtual EDID...\n"
+ "Requesting re-registration of port\n"
+ "Restoring virtual mode %d\n"
+ "Sleeping on commandGate until EDID is available..\n"
+ "TunnelActive"
+ "TunnelUse"
+ "Unit"
+ "VirtualMode"
+ "Writing Virtual DPCD bytes - address=0x%x, length=%d, index=%d\n"
+ "_setVirtualEDID"
+ "_waitingVirtualEDID=%d..\n"
+ "_workLoop->addEventSource(_deactivateTimeoutSource) failed\n"
+ "activate_block_invoke"
+ "checkEDIDGated"
+ "checkInitialHPDState_block_invoke"
+ "com.apple.private.ioavfamily.hdmi-port-debug"
+ "deactivateTimeoutOccurred"
+ "deactivate_block_invoke"
+ "domain%d: connectTo ufp %s,%d to dfp %s,%d ret=0x%08x\n"
+ "dprxport"
+ "failed to allocate IODPPortService\n"
+ "failed to init IODPPortService\n"
+ "handleDPSwitchWillSleep"
+ "handleDisplayRequest"
+ "handleStart_block_invoke"
+ "handleStart_block_invoke_2"
+ "handleTransportMessage"
+ "hotPlugDetectChangeOccurred_block_invoke"
+ "interruptRequestOccurred_block_invoke"
+ "message=%s dpTransportAvailable=%s\n"
+ "notice: forwarding inactive sink notification on idle port...\n"
+ "notice: ignoring %s event during system sleep.\n"
+ "notice: ignoring %s event on inactive port.\n"
+ "notice: ignoring DisplayRequest during system sleep.\n"
+ "notice: ignoring IRQ_HPD event during system sleep.\n"
+ "notice: ignoring IRQ_HPD event on inactive port.\n"
+ "port-number"
+ "port-type"
+ "releasing display...\n"
+ "setUserClient"
+ "setVirtualDPCD"
+ "setVirtualMode"
+ "setVirtualMode_block_invoke"
+ "setting virtual mode, new=%d, old=%d\n"
+ "site.IODPPortAnalyticsCollector"
+ "site.IODPPortService"
+ "site.IODPPortUserClient"
+ "site.IODPTXVirtualPort"
+ "site.IODPVirtualPortService"
+ "superclass ret=0x%08x\n"
+ "synthesizing displayRequest due to !_displayAllocated...\n"
+ "synthesizing hotPlugDetectChangeOccurred due to _hpdAsserted...\n"
+ "synthesizing message=%s: HPD %u->%u\n"
+ "transport-index"
+ "v16@?0^{IOTimerEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^vQ^{ExpansionData}}8"
+ "warning: Ignoring port events from transport for virtual mode\n"
+ "warning: failed to read LTTPR ret=0x%08x"
+ "warning: ignoring inactive sink notification on inactive port.\n"
+ "warning: ignoring redundant deactivate()\n"
+ "writeI2C"
+ "writing I2C to virtual device i2cAddr=%x, offset=%x, length=%d\n"
- "121111121222121211111222221111111111112222222222222222222222222222222222"
- "121111121222121211111222221111111111112222222222222222222222222222222222222"
- "12111112122212121112222211111111112221222221222222212222212222212222222222222222222222222222222222222222222222222221111111112111111112222111111222222222222222222221"
- "121111121222121211122222111111111122212222212222222122222122222122222222222222222222222222222222222222222222222222211111111121111111122221111112222222222222222222211"
- "121111121222121211122222111111111122212222212222222122222122222122222222222222222222222222222222222222222222222222211111111121111111122221111112222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "12111112122212121112222222222222222222222222222222222222121112111111111222222222222222222222222222222111111112222222222222222222222222222222222222222222222222222222222"
- "121111121222121211122222222222222222222222222222222222221211121111111112222222222222222222222222222221111111122222222222222222222222222222222222222222222222222222222221"
- "121111121222121211222221"
- "121222221111211112212222222222"
- "B16@?0^{IODPTXPort=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^^?^^?^^?^^?i[8I]^{IODPSwitch}^{IOService}^{IODPTXPort}^{IOWorkLoop}^{IOCommandGate}^{IODPTXPortEventLog}^{IOTimerEventSource}^?^?^?^?^{thread_call}B{ActionQueue=[128{Action=C}]CCC}B{IODPTXPortAttributes=Cb1b1b6b16{IODPTXPortAddress=b4b4b2b5b1b16}}BBBBBBBBBiBB{?={?=b1b1b6}Cb16b32{?=II}{IOAVTiledDisplayInfo={?={?=[3C]}SI}{?=b1b1b1b1b4}b16b32{?=SSSS}{?=II}{?=II}}{?=IIIIb8b8Cb8}[16C][16c]}}8"
- "Failed to init IOPortDPDelegate\n"
- "IOAV[%d] %s<0x%llx>::%s: Failed to init IOPortDPDelegate\n"
- "IOAV[%d] %s<0x%llx>::%s: IOPortDPAnalyticsCollector::init failed\n"
- "IOAV[%d] %s<0x%llx>::%s: IOPortDPDelegate failed to init\n"
- "IOAV[%d] %s<0x%llx>::%s: domain%d: connect ufp %s,%d to dfp %s,%d ret=0x%08x\n"
- "IOPortDPAnalyticsCollector"
- "IOPortDPAnalyticsCollector::init failed\n"
- "IOPortDPDelegate"
- "IOPortDPDelegate failed to init\n"
- "IOPortDPDelegate.cpp"
- "domain%d: connect ufp %s,%d to dfp %s,%d ret=0x%08x\n"
- "site.IOPortDPAnalyticsCollector"
- "site.IOPortDPDelegate"

```
