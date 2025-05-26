## NPTKit

> `/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit`

```diff

-152.0.0.0.0
+155.0.0.0.0
   __TEXT.__text: 0x3bfa0
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_methlist: 0x45d0
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x3b58
+  __TEXT.__cstring: 0x3b74
   __TEXT.__gcc_except_tab: 0x670
   __TEXT.__oslogstring: 0xb97
   __TEXT.__unwind_info: 0x820
-  __TEXT.__objc_classname: 0x3d4
+  __TEXT.__objc_classname: 0x3eb
   __TEXT.__objc_methname: 0xdd8b
-  __TEXT.__objc_methtype: 0x1a23
+  __TEXT.__objc_methtype: 0x1a25
   __TEXT.__objc_stubs: 0x85c0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0xa08
Symbols:
+ +[NPTDLogger client]
+ +[NPTDLogger daemon]
+ +[NetworkPerformanceTesterDClient sharedInstance]
+ -[NetworkPerformanceTesterDClient .cxx_destruct]
+ -[NetworkPerformanceTesterDClient getPrivilegedFileHandleForPacketCapture:]
+ -[NetworkPerformanceTesterDClient getPrivilegedFileHandleForPath:completionHandler:]
+ -[NetworkPerformanceTesterDClient init]
+ -[NetworkPerformanceTesterDClient testServiceWithArguments:completionHandler:]
+ _OBJC_CLASS_$_NPTDLogger
+ _OBJC_CLASS_$_NetworkPerformanceTesterDClient
+ _OBJC_IVAR_$_NetworkPerformanceTesterDClient.connection
+ _OBJC_IVAR_$_NetworkPerformanceTesterDClient.server
+ _OBJC_METACLASS_$_NPTDLogger
+ _OBJC_METACLASS_$_NetworkPerformanceTesterDClient
+ __OBJC_$_CLASS_METHODS_NPTDLogger
+ __OBJC_$_CLASS_METHODS_NetworkPerformanceTesterDClient
+ __OBJC_$_INSTANCE_METHODS_NetworkPerformanceTesterDClient
+ __OBJC_$_INSTANCE_VARIABLES_NetworkPerformanceTesterDClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NPTDServices
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NPTDServices
+ __OBJC_CLASS_PROTOCOLS_$_NetworkPerformanceTesterDClient
+ __OBJC_CLASS_RO_$_NPTDLogger
+ __OBJC_CLASS_RO_$_NetworkPerformanceTesterDClient
+ __OBJC_LABEL_PROTOCOL_$_NPTDServices
+ __OBJC_METACLASS_RO_$_NPTDLogger
+ __OBJC_METACLASS_RO_$_NetworkPerformanceTesterDClient
+ __OBJC_PROTOCOL_$_NPTDServices
+ __OBJC_PROTOCOL_REFERENCE_$_NPTDServices
+ ___39-[NetworkPerformanceTesterDClient init]_block_invoke
+ ___39-[NetworkPerformanceTesterDClient init]_block_invoke_2
+ ___39-[NetworkPerformanceTesterDClient init]_block_invoke_3
+ ___49+[NetworkPerformanceTesterDClient sharedInstance]_block_invoke
+ ___75-[NetworkPerformanceTesterDClient getPrivilegedFileHandleForPacketCapture:]_block_invoke
+ ___78-[NetworkPerformanceTesterDClient testServiceWithArguments:completionHandler:]_block_invoke
+ ___84-[NetworkPerformanceTesterDClient getPrivilegedFileHandleForPath:completionHandler:]_block_invoke
- +[SDLogger client]
- +[SDLogger daemon]
- +[SpeedDClient sharedInstance]
- -[SpeedDClient .cxx_destruct]
- -[SpeedDClient getPrivilegedFileHandleForPacketCapture:]
- -[SpeedDClient getPrivilegedFileHandleForPath:completionHandler:]
- -[SpeedDClient init]
- -[SpeedDClient testServiceWithArguments:completionHandler:]
- _OBJC_CLASS_$_SDLogger
- _OBJC_CLASS_$_SpeedDClient
- _OBJC_IVAR_$_SpeedDClient.connection
- _OBJC_IVAR_$_SpeedDClient.server
- _OBJC_METACLASS_$_SDLogger
- _OBJC_METACLASS_$_SpeedDClient
- __OBJC_$_CLASS_METHODS_SDLogger
- __OBJC_$_CLASS_METHODS_SpeedDClient
- __OBJC_$_INSTANCE_METHODS_SpeedDClient
- __OBJC_$_INSTANCE_VARIABLES_SpeedDClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SDServices
- __OBJC_$_PROTOCOL_METHOD_TYPES_SDServices
- __OBJC_CLASS_PROTOCOLS_$_SpeedDClient
- __OBJC_CLASS_RO_$_SDLogger
- __OBJC_CLASS_RO_$_SpeedDClient
- __OBJC_LABEL_PROTOCOL_$_SDServices
- __OBJC_METACLASS_RO_$_SDLogger
- __OBJC_METACLASS_RO_$_SpeedDClient
- __OBJC_PROTOCOL_$_SDServices
- __OBJC_PROTOCOL_REFERENCE_$_SDServices
- ___20-[SpeedDClient init]_block_invoke
- ___20-[SpeedDClient init]_block_invoke_2
- ___20-[SpeedDClient init]_block_invoke_3
- ___30+[SpeedDClient sharedInstance]_block_invoke
- ___56-[SpeedDClient getPrivilegedFileHandleForPacketCapture:]_block_invoke
- ___59-[SpeedDClient testServiceWithArguments:completionHandler:]_block_invoke
- ___65-[SpeedDClient getPrivilegedFileHandleForPath:completionHandler:]_block_invoke
CStrings:
+ "@\"<NPTDServices>\""
+ "NPTDLogger"
+ "NPTDServices"
+ "NetworkPerformanceTesterDClient"
+ "com.apple.internal.networkperformancetesterd"
- "@\"<SDServices>\""
- "SDLogger"
- "SDServices"
- "SpeedDClient"
- "com.apple.speedd"

```
