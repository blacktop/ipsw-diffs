## NRDUpdated

> `/usr/libexec/NRDUpdated`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0xba48
+2171.100.125.0.3
+  __TEXT.__text: 0xbaa4
   __TEXT.__auth_stubs: 0x660
   __TEXT.__objc_stubs: 0x1b00
-  __TEXT.__objc_methlist: 0x798
+  __TEXT.__objc_methlist: 0xc54
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x10a9
   __TEXT.__gcc_except_tab: 0x1a4

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x1968
-  __DATA.__objc_selrefs: 0x7a0
+  __DATA.__objc_const: 0x10c8
+  __DATA.__objc_selrefs: 0x848
   __DATA.__objc_ivar: 0xa0
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x540

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 267
+  Functions: 271
   Symbols:   2146
   CStrings:  733
 
Symbols:
+ +[NRDUpdateDaemonServerImpl sharedInstance].cold.1
+ __37-[NRDUpdateDCore actionPeriodicScan:]_block_invoke.427
+ __37-[NRDUpdateDCore actionPeriodicScan:]_block_invoke.427.cold.1
+ __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.302
+ __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.302.cold.1
+ __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.307
+ __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.309
+ __47-[NRDUpdateDCore scheduleNRDUpdateBrainReScan:]_block_invoke.459
+ __52-[NRDUpdateDCore scheduleNRDUpdateBrainPeriodicScan]_block_invoke.477
+ __64-[NRDUpdateDaemonServerImpl listener:shouldAcceptNewConnection:]_block_invoke.335
+ __64-[NRDUpdateDaemonServerImpl listener:shouldAcceptNewConnection:]_block_invoke.335.cold.1
+ __block_literal_global.305
+ __block_literal_global.337
+ edt_supports_recoveryos.cold.1
+ nrdSharedLogger.cold.1
- __37-[NRDUpdateDCore actionPeriodicScan:]_block_invoke.424
- __37-[NRDUpdateDCore actionPeriodicScan:]_block_invoke.424.cold.1
- __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.299
- __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.299.cold.1
- __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.303
- __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.304
- __47-[NRDUpdateDCore scheduleNRDUpdateBrainReScan:]_block_invoke.456
- __52-[NRDUpdateDCore scheduleNRDUpdateBrainPeriodicScan]_block_invoke.474
- __64-[NRDUpdateDaemonServerImpl listener:shouldAcceptNewConnection:]_block_invoke.332
- __64-[NRDUpdateDaemonServerImpl listener:shouldAcceptNewConnection:]_block_invoke.332.cold.1
- __block_literal_global.302
- __block_literal_global.331
CStrings:
+ "08:37:22"
+ "Feb 16 2025"
- "04:54:58"
- "Jan 16 2025"

```
