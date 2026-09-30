## NetworkStatistics

> `/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics`

```diff

-263.40.1.0.0
-  __TEXT.__text: 0x2e230
+263.100.4.0.0
+  __TEXT.__text: 0x30014
   __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x45a0
+  __TEXT.__objc_methlist: 0x45b0
   __TEXT.__cstring: 0x71bd
-  __TEXT.__oslogstring: 0x2378
-  __TEXT.__const: 0x1e0
-  __TEXT.__gcc_except_tab: 0x42c
-  __TEXT.__unwind_info: 0xb00
+  __TEXT.__oslogstring: 0x25f5
+  __TEXT.__const: 0x210
+  __TEXT.__gcc_except_tab: 0x408
+  __TEXT.__unwind_info: 0xbe0
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x83a3
-  __TEXT.__objc_methtype: 0x9345
-  __TEXT.__objc_stubs: 0x4d20
+  __TEXT.__objc_methname: 0x83ae
+  __TEXT.__objc_methtype: 0x95f3
+  __TEXT.__objc_stubs: 0x4d60
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x978
+  __DATA_CONST.__const: 0x9c8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC4F54B9-682A-3922-B144-10C166B100A8
-  Functions: 1605
-  Symbols:   5118
-  CStrings:  3802
+  UUID: 3DAC95DE-1F4D-3412-A86F-554F478B2F86
+  Functions: 1613
+  Symbols:   5138
+  CStrings:  3812
 
Symbols:
+ -[NWStatsConnSource deriveAttribution:descriptor:]
+ -[NWStatsInterfaceRegistry dumpState]
+ -[NWStatsQUICSource deriveAttribution:descriptor:]
+ -[NWStatsTCPSource deriveAttribution:descriptor:]
+ -[NWStatsUDPSource deriveAttribution:descriptor:]
+ GCC_except_table14
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ ___37-[NWStatsInterfaceRegistry dumpState]_block_invoke
+ _objc_msgSend$deriveAttribution:descriptor:
+ _objc_msgSend$dumpState
+ _objc_msgSend$ntstatContext
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
- -[NWStatsConnSource deriveAttribution:]
- -[NWStatsQUICSource deriveAttribution:]
- -[NWStatsTCPSource deriveAttribution:]
- -[NWStatsUDPSource deriveAttribution:]
- GCC_except_table10
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$deriveAttribution:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
CStrings:
+ " ref %6lld --> %{public}@"
+ "NWStatsInterfaceRegistry:\n  Queried interface indexes - %@\n  Looked up machO UUIDs - %@\n  Accumulated interface bytes - %@"
+ "NWStatsManager:\n  Current num sources %d current buf size %d after %d adaptations\n  Source removes %lld after filter %lld after drop %lld\n  No-source removes %lld after filter %lld after drop %lld"
+ "NWStatsManager: %s src-add %lld details open %lld poll %lld event %lld close %lld"
+ "NWStatsManager: monitoring interface %d with srcref %lld threshold %lld"
+ "NWStatsManager: unknown-%d src-add %lld details open %lld poll %lld event %lld close %lld"
+ "NWStatsPollHandler: instance %lld context %lld"
+ "deriveAttribution:descriptor:"
+ "v32@0:8@16^{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]}24"
+ "v32@0:8@16^{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}24"
+ "v32@0:8@16^{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}24"
- "deriveAttribution:"

```
