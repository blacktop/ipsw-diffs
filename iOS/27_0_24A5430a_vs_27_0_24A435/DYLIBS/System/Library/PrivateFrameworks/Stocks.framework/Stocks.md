## Stocks

> `/System/Library/PrivateFrameworks/Stocks.framework/Stocks`

```diff

 1555.1.0.0.0
-  __TEXT.__text: 0x497b8
+  __TEXT.__text: 0x497a4
   __TEXT.__objc_methlist: 0x5660
   __TEXT.__const: 0x2f8
   __TEXT.__cstring: 0x247a

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1871
+  Functions: 1873
   Symbols:   5082
   CStrings:  689
 
Functions:
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_1
~ -[StockPlatterViewController updateChartForInterval:completion:].cold.1 : 60 -> 52
~ ___64-[StockPlatterViewController updateChartForInterval:completion:]_block_invoke.cold.1 : 72 -> 64
~ ___64-[StockPlatterViewController updateChartForInterval:completion:]_block_invoke.101.cold.1 : 64 -> 56
~ ___64-[StockPlatterViewController updateChartForInterval:completion:]_block_invoke.103.cold.1 : 64 -> 56
~ -[YQLRequest loadRequest:].cold.1 : 108 -> 100
~ -[YQLRequest loadRequest:].cold.2 : 72 -> 64
~ -[YQLRequest failWithError:].cold.1 : 152 -> 156
~ -[YQLRequest URLSession:task:didCompleteWithError:].cold.1 : 160 -> 164
~ ___48-[SCKDatabase modifyContentsOfZone:withCommand:]_block_invoke.cold.1 : 64 -> 68
~ ___52-[SCKDatabase _fetchZoneChangesForZones:completion:]_block_invoke.93.cold.1 : 88 -> 92
~ ___68-[SCKDatabase _saveZoneToContainer:allowRecoveryAttempt:completion:]_block_invoke_2.104.cold.1 : 120 -> 100
~ ___68-[SCKDatabase _saveZoneToContainer:allowRecoveryAttempt:completion:]_block_invoke_3.107.cold.1 : 120 -> 100
```
