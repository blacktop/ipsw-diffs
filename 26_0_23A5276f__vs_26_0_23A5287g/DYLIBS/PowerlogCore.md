## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-2964.0.40.502.1
-  __TEXT.__text: 0xda1f4
-  __TEXT.__auth_stubs: 0x1ad0
-  __TEXT.__objc_methlist: 0x8848
-  __TEXT.__const: 0x1838
-  __TEXT.__cstring: 0x3a826
-  __TEXT.__oslogstring: 0x7622
+2964.0.64.0.0
+  __TEXT.__text: 0xd9b10
+  __TEXT.__auth_stubs: 0x1ac0
+  __TEXT.__objc_methlist: 0x8860
+  __TEXT.__const: 0x1830
+  __TEXT.__cstring: 0x3a824
+  __TEXT.__oslogstring: 0x76b1
   __TEXT.__gcc_except_tab: 0x28b0
-  __TEXT.__unwind_info: 0x2c98
+  __TEXT.__unwind_info: 0x2d60
   __TEXT.__objc_classname: 0x8a7
-  __TEXT.__objc_methname: 0x12df6
+  __TEXT.__objc_methname: 0x12df7
   __TEXT.__objc_methtype: 0x1890
-  __TEXT.__objc_stubs: 0xf820
+  __TEXT.__objc_stubs: 0xf800
   __DATA_CONST.__got: 0x778
-  __DATA_CONST.__const: 0x2498
+  __DATA_CONST.__const: 0x2470
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50b8
+  __DATA_CONST.__objc_selrefs: 0x50c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2a0
-  __DATA_CONST.__objc_arraydata: 0x3cb90
-  __AUTH_CONST.__auth_got: 0xd80
-  __AUTH_CONST.__const: 0x22a0
-  __AUTH_CONST.__cfstring: 0x5e4c0
-  __AUTH_CONST.__objc_const: 0x90a0
+  __DATA_CONST.__objc_arraydata: 0x3ccc0
+  __AUTH_CONST.__auth_got: 0xd78
+  __AUTH_CONST.__const: 0x22e0
+  __AUTH_CONST.__cfstring: 0x5e6c0
+  __AUTH_CONST.__objc_const: 0x9070
   __AUTH_CONST.__objc_intobj: 0x4800
   __AUTH_CONST.__objc_doubleobj: 0x10c0
-  __AUTH_CONST.__objc_arrayobj: 0x1140
-  __AUTH_CONST.__objc_dictobj: 0xec40
+  __AUTH_CONST.__objc_arrayobj: 0x1158
+  __AUTH_CONST.__objc_dictobj: 0xec90
   __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x634
+  __DATA.__objc_ivar: 0x630
   __DATA.__data: 0x440
-  __DATA.__bss: 0x1749
+  __DATA.__bss: 0x1719
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1b80
   __DATA_DIRTY.__data: 0x24

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 47774592-115E-3E56-A044-9A2CC72ED099
-  Functions: 4510
-  Symbols:   15808
-  CStrings:  29087
+  UUID: 083BA9F8-0DF3-35E9-AD23-426DF5EE0FCE
+  Functions: 4512
+  Symbols:   15793
+  CStrings:  29117
 
Symbols:
+ +[PLPlatform isBasebandMavToAllowSysdiagnoseTrigger]
+ +[PLPlatform isBasebandMavToAllowSysdiagnoseTrigger].cold.1
+ -[PLCoreOperator startServicesForRelay]
+ -[PLCoreService startRelayServices]
+ -[PowerlogCore setupForRelay]
+ -[PowerlogCore setupForRelay].cold.1
+ -[PowerlogCore setupForRelay].cold.2
+ _PLLogRelay
+ _PLLogRelay.__logObj
+ _PLLogRelay.cold.1
+ _PLLogRelay.onceToken
+ ___18-[PLXPCRelay init]_block_invoke.24
+ ___29-[PLXPCRelay relayConnection]_block_invoke.135
+ ___29-[PLXPCRelay relayConnection]_block_invoke.135.cold.1
+ ___29-[PLXPCRelay relayConnection]_block_invoke.135.cold.2
+ ___29-[PLXPCRelay relayConnection]_block_invoke.135.cold.3
+ ___29-[PLXPCRelay relayConnection]_block_invoke.135.cold.4
+ ___29-[PLXPCRelay relayConnection]_block_invoke.141
+ ___29-[PLXPCRelay relayConnection]_block_invoke.148
+ ___29-[PLXPCRelay relayConnection]_block_invoke.154
+ ___29-[PLXPCRelay relayConnection]_block_invoke.166
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.103
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.109
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.118
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.124
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.34
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.40
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.46
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.52
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.64
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.70
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.79
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.85
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.91
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.97
+ ___52+[PLPlatform isBasebandMavToAllowSysdiagnoseTrigger]_block_invoke
+ ___PLLogRelay_block_invoke
+ ___block_literal_global.623
+ _handlePeer:forEvent:.classDebugEnabled.102
+ _handlePeer:forEvent:.classDebugEnabled.108
+ _handlePeer:forEvent:.classDebugEnabled.117
+ _handlePeer:forEvent:.classDebugEnabled.123
+ _handlePeer:forEvent:.classDebugEnabled.33
+ _handlePeer:forEvent:.classDebugEnabled.39
+ _handlePeer:forEvent:.classDebugEnabled.45
+ _handlePeer:forEvent:.classDebugEnabled.51
+ _handlePeer:forEvent:.classDebugEnabled.63
+ _handlePeer:forEvent:.classDebugEnabled.69
+ _handlePeer:forEvent:.classDebugEnabled.78
+ _handlePeer:forEvent:.classDebugEnabled.84
+ _handlePeer:forEvent:.classDebugEnabled.90
+ _handlePeer:forEvent:.classDebugEnabled.96
+ _handlePeer:forEvent:.defaultOnce.101
+ _handlePeer:forEvent:.defaultOnce.107
+ _handlePeer:forEvent:.defaultOnce.116
+ _handlePeer:forEvent:.defaultOnce.122
+ _handlePeer:forEvent:.defaultOnce.32
+ _handlePeer:forEvent:.defaultOnce.38
+ _handlePeer:forEvent:.defaultOnce.44
+ _handlePeer:forEvent:.defaultOnce.50
+ _handlePeer:forEvent:.defaultOnce.62
+ _handlePeer:forEvent:.defaultOnce.68
+ _handlePeer:forEvent:.defaultOnce.77
+ _handlePeer:forEvent:.defaultOnce.83
+ _handlePeer:forEvent:.defaultOnce.89
+ _handlePeer:forEvent:.defaultOnce.95
+ _isBasebandMavToAllowSysdiagnoseTrigger.onceToken
+ _isBasebandMavToAllowSysdiagnoseTrigger.result
+ _objc_msgSend$setupForRelay
+ _objc_msgSend$startRelayServices
+ _relayConnection.classDebugEnabled.159
+ _relayConnection.classDebugEnabled.165
+ _relayConnection.defaultOnce.158
+ _relayConnection.defaultOnce.164
+ _relayConnectionSync_block_invoke.classDebugEnabled.140
+ _relayConnectionSync_block_invoke.classDebugEnabled.147
+ _relayConnectionSync_block_invoke.classDebugEnabled.153
+ _relayConnectionSync_block_invoke.defaultOnce.139
+ _relayConnectionSync_block_invoke.defaultOnce.146
+ _relayConnectionSync_block_invoke.defaultOnce.152
- -[PLXPCRelay setXpcConnection:]
- -[PLXPCRelay startRelay].cold.1
- -[PLXPCRelay stopRelay].cold.1
- -[PLXPCRelay xpcConnection]
- GCC_except_table44
- _OBJC_IVAR_$_PLXPCRelay._xpcConnection
- ___18-[PLXPCRelay init]_block_invoke.20
- ___23-[PLXPCRelay stopRelay]_block_invoke
- ___24-[PLXPCRelay startRelay]_block_invoke
- ___24-[PLXPCRelay startRelay]_block_invoke.30
- ___24-[PLXPCRelay startRelay]_block_invoke.30.cold.1
- ___24-[PLXPCRelay startRelay]_block_invoke.30.cold.2
- ___24-[PLXPCRelay startRelay]_block_invoke.36
- ___24-[PLXPCRelay startRelay]_block_invoke.41
- ___24-[PLXPCRelay startRelay]_block_invoke.41.cold.1
- ___24-[PLXPCRelay startRelay]_block_invoke_2
- ___24-[PLXPCRelay startRelay]_block_invoke_2.42
- ___29-[PLXPCRelay relayConnection]_block_invoke.157
- ___29-[PLXPCRelay relayConnection]_block_invoke.157.cold.1
- ___29-[PLXPCRelay relayConnection]_block_invoke.157.cold.2
- ___29-[PLXPCRelay relayConnection]_block_invoke.157.cold.3
- ___29-[PLXPCRelay relayConnection]_block_invoke.157.cold.4
- ___29-[PLXPCRelay relayConnection]_block_invoke.167
- ___29-[PLXPCRelay relayConnection]_block_invoke.173
- ___29-[PLXPCRelay relayConnection]_block_invoke.179
- ___29-[PLXPCRelay relayConnection]_block_invoke.185
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.102
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.108
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.114
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.120
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.126
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.132
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.141
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.147
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.57
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.63
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.69
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.75
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.87
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.93
- ___block_descriptor_48_e8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
- _handlePeer:forEvent:.classDebugEnabled.101
- _handlePeer:forEvent:.classDebugEnabled.107
- _handlePeer:forEvent:.classDebugEnabled.113
- _handlePeer:forEvent:.classDebugEnabled.119
- _handlePeer:forEvent:.classDebugEnabled.125
- _handlePeer:forEvent:.classDebugEnabled.131
- _handlePeer:forEvent:.classDebugEnabled.140
- _handlePeer:forEvent:.classDebugEnabled.146
- _handlePeer:forEvent:.classDebugEnabled.56
- _handlePeer:forEvent:.classDebugEnabled.62
- _handlePeer:forEvent:.classDebugEnabled.68
- _handlePeer:forEvent:.classDebugEnabled.74
- _handlePeer:forEvent:.classDebugEnabled.86
- _handlePeer:forEvent:.classDebugEnabled.92
- _handlePeer:forEvent:.defaultOnce.100
- _handlePeer:forEvent:.defaultOnce.106
- _handlePeer:forEvent:.defaultOnce.112
- _handlePeer:forEvent:.defaultOnce.118
- _handlePeer:forEvent:.defaultOnce.124
- _handlePeer:forEvent:.defaultOnce.130
- _handlePeer:forEvent:.defaultOnce.139
- _handlePeer:forEvent:.defaultOnce.145
- _handlePeer:forEvent:.defaultOnce.55
- _handlePeer:forEvent:.defaultOnce.61
- _handlePeer:forEvent:.defaultOnce.67
- _handlePeer:forEvent:.defaultOnce.73
- _handlePeer:forEvent:.defaultOnce.85
- _handlePeer:forEvent:.defaultOnce.91
- _objc_msgSend$handlePeer:forEvent:
- _objc_msgSend$setXpcConnection:
- _objc_msgSend$xpcConnection
- _relayConnection.classDebugEnabled.178
- _relayConnection.classDebugEnabled.184
- _relayConnection.defaultOnce.177
- _relayConnection.defaultOnce.183
- _relayConnectionSync_block_invoke.classDebugEnabled.35
- _relayConnectionSync_block_invoke.defaultOnce.34
- _relayConnectionSync_block_invoke_2.classDebugEnabled
- _relayConnectionSync_block_invoke_2.defaultOnce
- _relayConnectionSync_block_invoke_3.classDebugEnabled
- _relayConnectionSync_block_invoke_3.classDebugEnabled.159
- _relayConnectionSync_block_invoke_3.classDebugEnabled.166
- _relayConnectionSync_block_invoke_3.classDebugEnabled.172
- _relayConnectionSync_block_invoke_3.defaultOnce
- _relayConnectionSync_block_invoke_3.defaultOnce.158
- _relayConnectionSync_block_invoke_3.defaultOnce.165
- _relayConnectionSync_block_invoke_3.defaultOnce.171
- _startRelay.classDebugEnabled
- _startRelay.defaultOnce
- _stopRelay.classDebugEnabled
- _stopRelay.defaultOnce
- _xpc_connection_get_context
CStrings:
+ "AdaptiveOCVWeekly"
+ "Done starting services for lite mode relay"
+ "GlassCounts"
+ "ISPIOPState"
+ "Insights"
+ "KeyboardSignposts"
+ "MobileChargingMode"
+ "OCV_selected"
+ "PMPDCSCeiling"
+ "PMPPMCDCSFloor"
+ "PMPPMCSOCFloor"
+ "Qualifiers"
+ "RMSE_ocv_candidates"
+ "Start Powerlog Services for relay"
+ "Starting services for lite mode relay"
+ "Tasking config bools: hasFileToSubmit=%@, PLL=%@, PLL-UPGRADE=%@, MSS=%@, SP=%@, BDC=%@, BG=%@, CE=%@, XC=%@"
+ "UsageSummary"
+ "V_captured"
+ "ccdrift_model_parameter"
+ "com.apple.TextInput"
+ "cover_scores"
+ "data_number"
+ "glass_invalidation_count"
+ "idx_min_rmse"
+ "isBasebandMavToAllowSysdiagnoseTrigger"
+ "max_glass_count"
+ "relay"
+ "setupForRelay"
+ "startRelayServices"
+ "startServicesForRelay"
- "-[PLXPCRelay startRelay]"
- "-[PLXPCRelay startRelay]_block_invoke"
- "-[PLXPCRelay startRelay]_block_invoke_2"
- "-[PLXPCRelay stopRelay]"
- "No powerlog file to submit."
- "Relay: Relay running in aggd with service %s to %s"
- "Relay: XPC error! %@"
- "Relay: closing relay in aggd with service %s to %s"
- "Relay: peer(%d) connected"
- "T@\"NSObject<OS_xpc_object>\",&,V_xpcConnection"
- "XPCRelay_Connection"
- "_xpcConnection"
- "com.apple.powerlog.plxpclogger.xpc"
- "setXpcConnection:"
- "tasking config bools: %@, %@, %@, %@, %@, %@, %@, %@"
- "xpcConnection"

```
