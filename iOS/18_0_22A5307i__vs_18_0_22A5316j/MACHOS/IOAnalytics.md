## IOAnalytics

> `/System/Library/HIDPlugins/SessionFilters/IOAnalytics.plugin/IOAnalytics`

```diff

-1003.0.0.0.0
-  __TEXT.__text: 0x14938
-  __TEXT.__auth_stubs: 0x660
+1008.0.0.502.1
+  __TEXT.__text: 0x1608c
+  __TEXT.__auth_stubs: 0x670
   __TEXT.__objc_stubs: 0xee0
-  __TEXT.__objc_methlist: 0xbfc
+  __TEXT.__objc_methlist: 0xd1c
   __TEXT.__const: 0x70
-  __TEXT.__objc_methname: 0x1268
-  __TEXT.__cstring: 0x1ac4
-  __TEXT.__oslogstring: 0x1352
-  __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methtype: 0x4ca
+  __TEXT.__objc_methname: 0x12c2
+  __TEXT.__cstring: 0x1c6e
+  __TEXT.__oslogstring: 0x13df
+  __TEXT.__objc_classname: 0x13f
+  __TEXT.__objc_methtype: 0x4dc
   __TEXT.__gcc_except_tab: 0xec
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x408
-  __DATA_CONST.__auth_got: 0x340
+  __TEXT.__unwind_info: 0x430
+  __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0xa28
-  __DATA_CONST.__cfstring: 0x2a20
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__const: 0xa90
+  __DATA_CONST.__cfstring: 0x2c00
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x480
-  __DATA_CONST.__objc_arraydata: 0x98
-  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_arraydata: 0xa0
+  __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x1bd8
-  __DATA.__objc_selrefs: 0x4c8
-  __DATA.__objc_ivar: 0x148
-  __DATA.__objc_data: 0x410
+  __DATA.__objc_const: 0x1df8
+  __DATA.__objc_selrefs: 0x4d8
+  __DATA.__objc_ivar: 0x168
+  __DATA.__objc_data: 0x460
   __DATA.__data: 0x178
   __DATA.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 491
-  Symbols:   3746
-  CStrings:  819
+  Functions: 525
+  Symbols:   3984
+  CStrings:  844
 
Symbols:
+ -[AUVDMAnalytics _handleServiceMatched:].cold.22
+ -[AUVDMAnalytics _handleServiceMatched:].cold.22
+ -[CIOAnalytics _handleServiceMatched:].cold.16
+ -[DPAnalytics _handleServiceMatched:].cold.29
+ -[IOAnalyticsHIDSessionFilter setUsbpdAnalytics:]
+ -[IOAnalyticsHIDSessionFilter setUsbpdAnalytics:]
+ -[IOAnalyticsHIDSessionFilter usbpdAnalytics]
+ -[IOAnalyticsHIDSessionFilter usbpdAnalytics]
+ -[USBAnalytics _handleServiceMatched:].cold.12
+ -[USBAnalytics _handleServiceMatched:].cold.12
+ -[USBPDAnalytics .cxx_destruct]
+ -[USBPDAnalytics .cxx_destruct]
+ -[USBPDAnalytics _handleServiceMatched:]
+ -[USBPDAnalytics _handleServiceMatched:]
+ -[USBPDAnalytics _handleServiceMatched:].cold.1
+ -[USBPDAnalytics _handleServiceMatched:].cold.10
+ -[USBPDAnalytics _handleServiceMatched:].cold.11
+ -[USBPDAnalytics _handleServiceMatched:].cold.2
+ -[USBPDAnalytics _handleServiceMatched:].cold.3
+ -[USBPDAnalytics _handleServiceMatched:].cold.4
+ -[USBPDAnalytics _handleServiceMatched:].cold.4
+ -[USBPDAnalytics _handleServiceMatched:].cold.5
+ -[USBPDAnalytics _handleServiceMatched:].cold.5
+ -[USBPDAnalytics _handleServiceMatched:].cold.6
+ -[USBPDAnalytics _handleServiceMatched:].cold.7
+ -[USBPDAnalytics _handleServiceMatched:].cold.8
+ -[USBPDAnalytics _handleServiceMatched:].cold.9
+ -[USBPDAnalytics _startEventMonitoring]
+ -[USBPDAnalytics _startEventMonitoring]
+ -[USBPDAnalytics _startEventMonitoring].cold.1
+ -[USBPDAnalytics _startEventMonitoring].cold.1
+ -[USBPDAnalytics _startEventMonitoring].cold.2
+ -[USBPDAnalytics _startEventMonitoring].cold.3
+ -[USBPDAnalytics _stopEventMonitoring]
+ -[USBPDAnalytics _stopEventMonitoring]
+ -[USBPDAnalytics analyticsEventsEnabled]
+ -[USBPDAnalytics analyticsEventsEnabled]
+ -[USBPDAnalytics init]
+ -[USBPDAnalytics init]
+ -[USBPDAnalytics ioNotificationPort]
+ -[USBPDAnalytics ioNotificationPort]
+ -[USBPDAnalytics ioServiceMatchingIterator]
+ -[USBPDAnalytics ioServiceMatchingIterator]
+ -[USBPDAnalytics log]
+ -[USBPDAnalytics log]
+ -[USBPDAnalytics monitoring]
+ -[USBPDAnalytics monitoring]
+ -[USBPDAnalytics queue]
+ -[USBPDAnalytics queue]
+ -[USBPDAnalytics setAnalyticsEventsEnabled:]
+ -[USBPDAnalytics setAnalyticsEventsEnabled:]
+ -[USBPDAnalytics setIoNotificationPort:]
+ -[USBPDAnalytics setIoNotificationPort:]
+ -[USBPDAnalytics setIoServiceMatchingIterator:]
+ -[USBPDAnalytics setIoServiceMatchingIterator:]
+ -[USBPDAnalytics setLog:]
+ -[USBPDAnalytics setLog:]
+ -[USBPDAnalytics setMonitoring:]
+ -[USBPDAnalytics setMonitoring:]
+ -[USBPDAnalytics setQueue:]
+ -[USBPDAnalytics setQueue:]
+ -[USBPDAnalytics setStarted:]
+ -[USBPDAnalytics setStarted:]
+ -[USBPDAnalytics start]
+ -[USBPDAnalytics start]
+ -[USBPDAnalytics started]
+ -[USBPDAnalytics started]
+ -[USBPDAnalytics stop]
+ -[USBPDAnalytics stop]
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/IOAnalytics.build/Objects-normal/arm64e/IOAnalyticsConstants_IOPort_Transport_Component_USBPD.o
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/IOAnalytics.build/Objects-normal/arm64e/USBPDAnalytics.o
+ IOAnalyticsConstants_IOPort_Transport_Component_USBPD.m
+ OBJC_IVAR_$_IOAnalyticsHIDSessionFilter._usbpdAnalytics
+ OBJC_IVAR_$_USBPDAnalytics._analyticsEventsEnabled
+ OBJC_IVAR_$_USBPDAnalytics._ioNotificationPort
+ OBJC_IVAR_$_USBPDAnalytics._ioServiceMatchingIterator
+ OBJC_IVAR_$_USBPDAnalytics._log
+ OBJC_IVAR_$_USBPDAnalytics._monitoring
+ OBJC_IVAR_$_USBPDAnalytics._queue
+ OBJC_IVAR_$_USBPDAnalytics._started
+ USBPDAnalytics.m
+ _CFRelease
+ _OBJC_CLASS_$_USBPDAnalytics
+ _OBJC_CLASS_$_USBPDAnalytics
+ _OBJC_METACLASS_$_USBPDAnalytics
+ _OBJC_METACLASS_$_USBPDAnalytics
+ __22-[USBPDAnalytics stop]_block_invoke.cold.1
+ __22-[USBPDAnalytics stop]_block_invoke.cold.1
+ __23-[USBPDAnalytics start]_block_invoke.cold.1
+ __23-[USBPDAnalytics start]_block_invoke.cold.1
+ __OBJC_$_INSTANCE_METHODS_USBPDAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_USBPDAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_USBPDAnalytics
+ __OBJC_$_PROP_LIST_USBPDAnalytics
+ __OBJC_$_PROP_LIST_USBPDAnalytics
+ __OBJC_CLASS_RO_$_USBPDAnalytics
+ __OBJC_CLASS_RO_$_USBPDAnalytics
+ __OBJC_METACLASS_RO_$_USBPDAnalytics
+ __OBJC_METACLASS_RO_$_USBPDAnalytics
+ ___22-[USBPDAnalytics stop]_block_invoke
+ ___22-[USBPDAnalytics stop]_block_invoke
+ ___23-[USBPDAnalytics start]_block_invoke
+ ___23-[USBPDAnalytics start]_block_invoke
+ ___40-[USBPDAnalytics _handleServiceMatched:]_block_invoke
+ ___40-[USBPDAnalytics _handleServiceMatched:]_block_invoke
+ __os_log_fault_impl
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Event_Published
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Event_Published
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_ComponentAddress
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_ComponentAddress
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_ProductID
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_ProductID
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_SOPp_ProductType
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_SOPp_ProductType
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_SpecificationRevision
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_SpecificationRevision
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_CertStat
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_CertStat
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_IDHeader
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_IDHeader
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_Product
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_Product
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_ProductType_1
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_ProductType_1
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_ProductType_2
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_ProductType_2
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_ProductType_3
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VDO_DiscoverIdentity_ProductType_3
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VendorID
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_VendorID
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_bcdDevice
+ _kACCCoreAnalytics_IOPort_Transport_Component_USBPD_Field_bcdDevice
- _objc_retain_x28
CStrings:
+ "\n"
+ "@\"USBPDAnalytics\""
+ "Could not find component address!"
+ "Could not find parent port type and number! (serviceProperties: %!@(MISSING))"
+ "Could not find specification revision!"
+ "IOPortTransportComponentCCUSBPD"
+ "Product Type"
+ "Specification Revision"
+ "T@\"USBPDAnalytics\",&,N,V_usbpdAnalytics"
+ "USBPDAnalytics"
+ "USBPD_ComponentAddress"
+ "USBPD_ProductID"
+ "USBPD_SOPp_ProductType"
+ "USBPD_SpecificationRevision"
+ "USBPD_VDO_DiscoverIdentity_4"
+ "USBPD_VDO_DiscoverIdentity_5"
+ "USBPD_VDO_DiscoverIdentity_6"
+ "USBPD_VDO_DiscoverIdentity_CertStat"
+ "USBPD_VDO_DiscoverIdentity_IDHeader"
+ "USBPD_VDO_DiscoverIdentity_Product"
+ "USBPD_bcdDevice"
+ "VDOs"
+ "_usbpdAnalytics"
+ "com.apple.ioport.transport.component.USBPD.published"
+ "setUsbpdAnalytics:"
+ "usbpdAnalytics"
- "\t"

```
