## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/Versions/A/AutoBugCaptureCore`

```diff

-383.80.2.0.0
-  __TEXT.__text: 0x7c724
-  __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x54d8
-  __TEXT.__cstring: 0x4b90
+383.101.1.0.0
+  __TEXT.__text: 0x7cf28
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__objc_methlist: 0x5b74
+  __TEXT.__cstring: 0x4c1d
   __TEXT.__const: 0x268
-  __TEXT.__oslogstring: 0xe005
-  __TEXT.__gcc_except_tab: 0x108c
+  __TEXT.__oslogstring: 0xe1df
+  __TEXT.__gcc_except_tab: 0x10a4
   __TEXT.__ustring: 0x8
-  __TEXT.diag_actions: 0x545d
-  __TEXT.__unwind_info: 0x15a0
-  __TEXT.__objc_classname: 0x989
-  __TEXT.__objc_methname: 0xd688
-  __TEXT.__objc_methtype: 0x1ab8
-  __TEXT.__objc_stubs: 0x9b80
-  __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0xeb8
-  __DATA_CONST.__objc_classlist: 0x268
+  __TEXT.diag_actions: 0x54c4
+  __TEXT.__unwind_info: 0x15b8
+  __TEXT.__objc_classname: 0x9a5
+  __TEXT.__objc_methname: 0xd712
+  __TEXT.__objc_methtype: 0x1ad6
+  __TEXT.__objc_stubs: 0x9c00
+  __DATA_CONST.__got: 0x4b0
+  __DATA_CONST.__const: 0xed8
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3268
+  __DATA_CONST.__objc_selrefs: 0x3418
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x5b0
-  __AUTH_CONST.__auth_got: 0x6c0
-  __AUTH_CONST.__const: 0x1ec0
-  __AUTH_CONST.__cfstring: 0x6460
-  __AUTH_CONST.__objc_const: 0xc3c8
+  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH_CONST.__const: 0x1ee0
+  __AUTH_CONST.__cfstring: 0x6500
+  __AUTH_CONST.__objc_const: 0xb938
   __AUTH_CONST.__objc_dictobj: 0x4b0
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x1810
-  __DATA.__objc_ivar: 0x624
+  __AUTH.__objc_data: 0x1860
+  __DATA.__objc_ivar: 0x62c
   __DATA.__data: 0xbc0
-  __DATA.__bss: 0x328
-  __DATA.__common: 0x9
+  __DATA.__bss: 0x340
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31911329-9535-385A-8277-1A2D0CB0AF03
-  Functions: 2185
-  Symbols:   5603
-  CStrings:  5547
+  UUID: BCA60DC3-32BA-3BD1-BA59-549A738DE1D2
+  Functions: 2260
+  Symbols:   5718
+  CStrings:  5580
 
Symbols:
+ +[ABCAdministrator sharedInstance].cold.1
+ +[ABCDailyMaintenanceActivity sharedInstance].cold.1
+ +[ABCSemiDailyMaintenanceActivity sharedInstance].cold.1
+ +[ABCWeeklyMaintenanceActivity sharedInstance].cold.1
+ +[AnalyticsAgent sharedInstance].cold.1
+ +[CaseDampeningExceptions setBasebandChipset:]
+ +[CaseDampeningExceptions setProductType:]
+ +[CaseDampeningExceptions setWiFiChipset:]
+ +[DiagnosticsController loggingStateCache].cold.1
+ +[PrimaryInterfaceUtils sharedInstance].cold.1
+ +[WirelessTechnologyProfile sharedInstance].cold.1
+ -[ABCAdministrator startMaintenanceServices].cold.1
+ -[ABCConfigurationManager autoBugCaptureEnabled].cold.1
+ -[ABCConfigurationManager autoBugCaptureEnabled].cold.2
+ -[ABCPreferences has_apple_email].cold.1
+ -[DiagnosticsController _loadLoggingSupport].cold.1
+ -[DiagnosticsServiceImpl listener:shouldAcceptNewConnection:].cold.1
+ -[KernelMsgSignalHandlerSDXC init:]
+ -[KernelMsgSignalHandlerSDXC releaseHandler]
+ -[KernelMsgSignalHandlerSDXC setupListener:]
+ -[NSDictionary(DiagnosticCase) logSignatureDescription].cold.1
+ -[SystemProperties buildVariant].cold.1
+ -[SystemProperties wifiChipset]
+ OBJC_IVAR_$_ABCAdministrator.kernelHandler
+ OBJC_IVAR_$_SystemProperties._wifiChipset
+ _IOIteratorNext
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortSetDispatchQueue
+ _IOObjectRelease
+ _IOServiceAddInterestNotification
+ _IOServiceAddMatchingNotification
+ _IOServiceMatching
+ _OBJC_CLASS_$_KernelMsgSignalHandlerSDXC
+ _OBJC_METACLASS_$_KernelMsgSignalHandlerSDXC
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ServiceInterest
+ _ServiceMatched
+ __60-[DiagnosticsServiceImpl addToSession:events:payload:reply:]_block_invoke.151.cold.1
+ __60-[DiagnosticsServiceImpl addToSession:events:payload:reply:]_block_invoke.cold.1
+ __71-[DiagnosticsServiceImpl requestGroupCaseIdentifierForSignature:reply:]_block_invoke.157.cold.1
+ __71-[DiagnosticsServiceImpl requestGroupCaseIdentifierForSignature:reply:]_block_invoke.157.cold.2
+ __74-[DiagnosticsServiceImpl addSignatureContentForSession:key:content:reply:]_block_invoke.155.cold.1
+ __74-[DiagnosticsServiceImpl addSignatureContentForSession:key:content:reply:]_block_invoke.cold.1
+ __81-[DiagnosticsServiceImpl triggerRemoteSessionForSignature:groupIdentifier:reply:]_block_invoke.cold.1
+ __OBJC_$_INSTANCE_METHODS_KernelMsgSignalHandlerSDXC
+ __OBJC_CLASS_RO_$_KernelMsgSignalHandlerSDXC
+ __OBJC_METACLASS_RO_$_KernelMsgSignalHandlerSDXC
+ ___requestSnapshot_block_invoke
+ __basebandChipset
+ __block_literal_global.33
+ __productType
+ __wifiChipset
+ _adminABC
+ _gNotifyPort
+ _iterator
+ _kIOMainPortDefault
+ _objc_msgSend$init:
+ _objc_msgSend$releaseHandler
+ _objc_msgSend$setProductType:
+ _objc_msgSend$setupListener:
+ adminLogHandle.cold.1
+ analyticsLogHandle.cold.1
+ archiverLogHandle.cold.1
+ basicLogHandle.cold.1
+ casemanagementLogHandle.cold.1
+ configurationLogHandle.cold.1
+ crossdeviceLogHandle.cold.1
+ diagcaseLogHandle.cold.1
+ diagcollectLogHandle.cold.1
+ diagextLogHandle.cold.1
+ diagreportLogHandle.cold.1
+ formattedDateStringForTimeInterval.cold.1
+ formattedDateStringForTimeInterval.cold.2
+ homekitLogHandle.cold.1
+ iso8601date_string_from_NSDate.cold.1
+ liaisonLogHandle.cold.1
+ objectanalyticsHandle.cold.1
+ persistenceLogHandle.cold.1
+ storageLogHandle.cold.1
+ summaryLogHandle.cold.1
+ symptomsLogHandle.cold.1
+ uploadLogHandle.cold.1
+ xpcLogHandle.cold.1
- __block_literal_global.32
- _fmod
CStrings:
+ " StorageKernelSignal: KernelMsgSignalHandler init ++ \n"
+ "@\"KernelMsgSignalHandlerSDXC\""
+ "AppleSDXC"
+ "AppleSDXCSlot"
+ "CardDowntrainError"
+ "Completed startup of KernelMsgSignalHandler"
+ "IOGeneralInterest"
+ "IOServiceFirstMatch"
+ "KernelMsgSignalHandlerSDXC"
+ "ProductName = %@, ProductClass = %@, ProductType = %@, ProductVersion = %@, BuildVersion = %@, BuildPlatform = %@, BuildVariant = %@, basebandCapability = %s, dualSIMCapable = %s, dualSIMEnabled = %s, Baseband Chipset = %@, WiFi Chipset = %@, InternalBuild = %s, FactoryBuild = %s, VendorBuild = %s, CarrierBuild = %s, SeedBuild = %s, CarrierSeedBuild = %s, CustomerSeedBuild = %s, DeviceSerialNumber = %@"
+ "StorageDrivers"
+ "StorageKernelSignal: ABC admin caseManager is Nil"
+ "StorageKernelSignal: ABC admin is Nil"
+ "StorageKernelSignal: Session %{public}@ accepted. (%@)"
+ "StorageKernelSignal: Session %{public}@ was NOT accepted. (Reason code: %d) (%@)"
+ "StorageKernelSignal: downtrain error detected. Triggering ABC\n"
+ "StorageKernelSignal: notification port destroyed\n"
+ "StorageKernelSignal: service matched\n"
+ "T@\"NSString\",R,N,V_wifiChipset"
+ "_wifiChipset"
+ "init:"
+ "kernelHandler"
+ "releaseHandler"
+ "sdxc_listener"
+ "setProductType:"
+ "setWiFiChipset:"
+ "setupListener:"
+ "unavailable"
+ "wifiChipset"
- "."
- "ProductName = %@, ProductClass = %@, ProductType = %@, ProductVersion = %@, BuildVersion = %@, BuildPlatform = %@, BuildVariant = %@, basebandCapability = %s, dualSIMCapable = %s, dualSIMEnabled = %s, Baseband Chipset = %@, InternalBuild = %s, FactoryBuild = %s, VendorBuild = %s, CarrierBuild = %s, SeedBuild = %s, CarrierSeedBuild = %s, CustomerSeedBuild = %s, DeviceSerialNumber = %@"

```
