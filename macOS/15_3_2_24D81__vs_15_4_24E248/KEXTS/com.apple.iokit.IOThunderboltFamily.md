## com.apple.iokit.IOThunderboltFamily

> `com.apple.iokit.IOThunderboltFamily`

```diff

-6769.60.11.0.0
-  __TEXT.__cstring: 0x33d2c
-  __TEXT.__os_log: 0x2e110
-  __TEXT.__const: 0x7e4
-  __TEXT_EXEC.__text: 0x1a10d4
+6781.100.4.0.0
+  __TEXT.__cstring: 0x343a6
+  __TEXT.__os_log: 0x2e604
+  __TEXT.__const: 0x7f4
+  __TEXT_EXEC.__text: 0x19ac74
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb1a
   __DATA.__common: 0x1238

   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x3a0
   __DATA_CONST.__mod_term_func: 0x3a0
-  __DATA_CONST.__const: 0x335c8
+  __DATA_CONST.__const: 0x335e8
   __DATA_CONST.__kalloc_type: 0x1d40
   __DATA_CONST.__kalloc_var: 0xaf0
-  UUID: D56B5719-681A-3AB8-8179-0C4A525A295F
-  Functions: 6239
-  Symbols:   9886
-  CStrings:  4795
+  UUID: C1272A12-AA40-34CD-ADD0-19D9E2A5E056
+  Functions: 6194
+  Symbols:   9874
+  CStrings:  4825
 
Symbols:
+ __ZN21IOThunderboltSwitchOS16isLinkUpInternalEP17IOThunderboltPortPb
+ __ZN23IOThunderboltSwitchUSB415configureRouterEv
+ __ZN25IOThunderboltSwitchLegacy16isLinkUpInternalEP17IOThunderboltPortPb
+ __ZZN21IOThunderboltSwitchOS16isLinkUpInternalEP17IOThunderboltPortPbE11_os_log_fmt
+ __ZZN22IOThunderboltSwitchOS221finishConfigureRouterEvE11_os_log_fmt_2
+ __ZZN23IOThunderboltSwitchUSB415configureRouterEvE11_os_log_fmt
+ __ZZN23IOThunderboltSwitchUSB415configureRouterEvE11_os_log_fmt_0
+ __ZZN23IOThunderboltSwitchUSB415configureRouterEvE11_os_log_fmt_1
+ __ZZN23IOThunderboltSwitchUSB415configureRouterEvE11_os_log_fmt_2
+ __ZZN23IOThunderboltSwitchUSB415configureRouterEvE11_os_log_fmt_3
+ __ZZN25IOThunderboltSwitchLegacy16isLinkUpInternalEP17IOThunderboltPortPbE11_os_log_fmt
+ __ZZN25IOThunderboltTunnelDriver14earlyWakeBeginEvE11_os_log_fmt_1
+ __ZZN25IOThunderboltTunnelDriver14lateSleepBeginEvE11_os_log_fmt_1
+ __ZZN25IOThunderboltTunnelDriver17earlyWakeCompleteEvE11_os_log_fmt_0
+ __ZZN25IOThunderboltTunnelDriver17lateSleepCompleteEvE11_os_log_fmt_0
+ __ZZN25IOThunderboltTunnelDriver18decrementScanCountEjjE11_os_log_fmt_0
+ __ZZN25IOThunderboltTunnelDriver18incrementScanCountEjE11_os_log_fmt_0
+ __ZZN25IOThunderboltTunnelDriver24decrementClientScanCountEjjE11_os_log_fmt_0
+ __ZZN25IOThunderboltTunnelDriver24incrementClientScanCountEjE11_os_log_fmt_0
- _ZN19IOThunderboltEEPROM16copyToDROMBufferEPKvm.cold.1
- _ZN21IOThunderboltSwitchOS18readEEPROMInternalEv.cold.1
- _ZN22IOThunderboltFrameList14ensureCapacityEj.cold.1
- _ZN22IOThunderboltFrameList14ensureCapacityEj.cold.2
- _ZN22IOThunderboltFrameList16initWithCapacityEj.cold.1
- _ZN22IOThunderboltLocalNode16publishXDServiceEPcjjjj.cold.1
- _ZN22IOThunderboltLocalNode16publishXDServiceEPcjjjj.cold.2
- _ZN22IOThunderboltLocalNode16publishXDServiceEPcjjjj.cold.3
- _ZN22IOThunderboltLocalNode16publishXDServiceEPcjjjj.cold.4
- _ZN22IOThunderboltLocalNode18unpublishXDServiceEPc.cold.1
- _ZN22IOThunderboltLocalNode18unpublishXDServiceEPc.cold.2
- _ZN22IOThunderboltLocalNode18unpublishXDServiceEPc.cold.3
- _ZN22IOThunderboltLocalNode18unpublishXDServiceEPc.cold.4
- _ZN23IOThunderboltStatistics26ensureRingHistoryAllocatedEt.cold.1
- _ZN24IOThunderboltTracebuffer20allocateTraceHistoryEi.cold.1
- _ZN31IOThunderboltSwitchDelegateACIO18identifyHWRevisionEv.cold.1
- _ZN34IOThunderboltControllerGenericACIO11loadPortMapEv.cold.1
- _ZN34IOThunderboltControllerGenericACIO16loadPortDefaultsEv.cold.1
- _ZN35IOThunderboltXDLocalPropertiesCache16encodeDictionaryEP12OSDictionary.cold.1
- _ZN35IOThunderboltXDLocalPropertiesCache16encodeDictionaryEP12OSDictionary.cold.2
- _ZN35IOThunderboltXDLocalPropertiesCache16encodeDictionaryEP12OSDictionary.cold.3
- _ZN35IOThunderboltXDLocalPropertiesCache16encodeDictionaryEP12OSDictionary.cold.4
- __ZN19IOThunderboltSwitch16isLinkUpInternalEP17IOThunderboltPortPb
- __ZN19IOThunderboltSwitchC1EPK11OSMetaClass
- __ZN19IOThunderboltSwitchC1Ev
- __ZN19IOThunderboltSwitchC2Ev
- __ZZN19IOThunderboltSwitch16isLinkUpInternalEP17IOThunderboltPortPbE11_os_log_fmt
- __ZZN21IOThunderboltSwitchOS10readEEPROMEvE11_os_log_fmt
- __ZZN21IOThunderboltSwitchOS10readEEPROMEvE11_os_log_fmt_0
- __ZZN21IOThunderboltSwitchOS10readEEPROMEvE11_os_log_fmt_1
- __ZZN21IOThunderboltSwitchOS15configureRouterEvE11_os_log_fmt_2
CStrings:
+ "%lldus IOThunderboltSwitch(%x@%llx)::childDeviceScanForPort - invalidate clients #%d route = 0x%llx port = %d\n"
+ "%lldus IOThunderboltSwitch(%x@%llx)::discoverXDomainLinksForPort - invalidate clients #%d route = 0x%llx port = %d\n"
+ "%lldus IOThunderboltSwitch(%x@%llx)::invalidateAllClients - invalidate clients #%d route = 0x%llx port = %d\n"
+ "%lldus IOThunderboltSwitch(%x@%llx)::processChild - invalidate clients #%d route = 0x%llx port = %d\n"
+ "%lldus IOThunderboltSwitch(%x@%llx)::processPlugEvent - invalidate clients #%d route = 0x%llx port = %d\n"
+ "%lldus IOThunderboltSwitch(%x@%llx)::processXDomainChild - invalidate clients #%d route = 0x%llx port = %d\n"
+ "%lldus IOThunderboltSwitch(%x@%llx)::syncTargetAndNegotiatedWidth - invalidate clients #%d route = 0x%llx port = %d\n"
+ "%lldus IOThunderboltSwitchLegacy(%x@%llx)::isLinkUpInternal - child port %d phy state = %d\n"
+ "%lldus IOThunderboltSwitchOS(%x@%llx)::configureRouter - PORT_CS_18 = 0x%08x\n"
+ "%lldus IOThunderboltSwitchOS(%x@%llx)::configureRouter - inUSB4Mode = %d status = 0x%08x\n"
+ "%lldus IOThunderboltSwitchOS(%x@%llx)::configureRouter - upstream port = %d\n"
+ "%lldus IOThunderboltSwitchOS(%x@%llx)::isLinkUpInternal - child port %d phy state = %d\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - config ready - status = 0x%08x\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - data = 0x%08x should_configure = %d - status = 0x%08x\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - write config = 0x%08x - status = 0x%08x\n"
+ "%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - write config valid = 0x%08x - status = 0x%08x\n"
+ "%lldus IOThunderboltSwitchType1(%x@%llx)::preEarlyWake - invalidate clients #%d route = 0x%llx port = %d\n"
+ "%lldus IOThunderboltSwitchType2(%x@%llx)::lateSleepPhase3 - invalidate clients #%d route = 0x%llx port = %d\n"
+ "%lldus IOThunderboltSwitchType3(%x@%llx)::lateSleepPhase3 - invalidate clients #%d route = 0x%llx port = %d\n"
+ "%lldus IOThunderboltSwitchUSB4(%x@%llx)::configureRouter - config ready - status = 0x%08x\n"
+ "%lldus IOThunderboltSwitchUSB4(%x@%llx)::configureRouter - data = 0x%08x should_configure = %d - status = 0x%08x\n"
+ "%lldus IOThunderboltSwitchUSB4(%x@%llx)::configureRouter - router ready - status = 0x%08x\n"
+ "%lldus IOThunderboltSwitchUSB4(%x@%llx)::configureRouter - write config = 0x%08x - status = 0x%08x\n"
+ "%lldus IOThunderboltSwitchUSB4(%x@%llx)::configureRouter - write config valid = 0x%08x - status = 0x%08x\n"
+ "21:12:02"
+ "Mar 19 2025"
- "%lldus IOThunderboltPort(%x@%llx:%x)::configureFromDesciption - WORKAROUND: setting HW BW to %u! spec_version = 0x%x fAdapterType = 0x%08x\n"
- "%lldus IOThunderboltSwitch<%p>(0x%llx)::isLinkUpInternal - child port %d phy state = %d\n"
- "%lldus IOThunderboltSwitchOS(%x@%llx)::configureRouter - config ready - status = 0x%08x\n"
- "%lldus IOThunderboltSwitchOS(%x@%llx)::configureRouter - write config = 0x%08x - status = 0x%08x\n"
- "%lldus IOThunderboltSwitchOS(%x@%llx)::configureRouter - write config valid = 0x%08x - status = 0x%08x\n"
- "%lldus IOThunderboltSwitchOS(%x@%llx)::readEEPROM - PORT_CS_18 = 0x%08x\n"
- "%lldus IOThunderboltSwitchOS(%x@%llx)::readEEPROM - inUSB4Mode = %d status = 0x%08x\n"
- "%lldus IOThunderboltSwitchOS(%x@%llx)::readEEPROM - upstream port = %d\n"
- "0123456789ABCDEF"
- "20:33:58"
- "Jan 10 2025"

```
