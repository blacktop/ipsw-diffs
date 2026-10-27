## ExchangeSyncExpress

> `/System/Library/PrivateFrameworks/ExchangeSyncExpress.framework/Versions/A/ExchangeSyncExpress`

```diff

-2075.0.0.0.0
-  __TEXT.__text: 0x9b48
+2080.200.61.0.0
+  __TEXT.__text: 0x9e04
   __TEXT.__objc_methlist: 0x834
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x588
-  __TEXT.__cstring: 0x4bc
-  __TEXT.__oslogstring: 0x639
-  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0x5a8
+  __TEXT.__cstring: 0x4bd
+  __TEXT.__oslogstring: 0x715
+  __TEXT.__unwind_info: 0x400
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__got: 0xd8
-  __AUTH_CONST.__const: 0x430
+  __AUTH_CONST.__const: 0x490
   __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0x10f8
+  __AUTH_CONST.__objc_const: 0x1118
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0xb0
+  __DATA.__objc_ivar: 0xb4
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 270
-  Symbols:   619
-  CStrings:  91
+  Symbols:   624
+  CStrings:  92
 
Symbols:
+ -[ESDConnection _serverConnectionInvalidatedForGeneration:]
+ GCC_except_table106
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table128
+ GCC_except_table132
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table149
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table58
+ GCC_except_table76
+ GCC_except_table86
+ GCC_except_table89
+ GCC_except_table91
+ GCC_except_table99
+ OBJC_IVAR_$_ESDConnection._connExchangeGeneration
+ ___59-[ESDConnection _serverConnectionInvalidatedForGeneration:]_block_invoke
+ ___block_descriptor_48_e8_32w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40r_e5_v8?0l
+ _objc_msgSend$_serverConnectionInvalidatedForGeneration:
- -[ESDConnection _serverConnectionInvalidated]
- GCC_except_table105
- GCC_except_table108
- GCC_except_table110
- GCC_except_table112
- GCC_except_table116
- GCC_except_table119
- GCC_except_table123
- GCC_except_table127
- GCC_except_table131
- GCC_except_table142
- GCC_except_table144
- GCC_except_table148
- GCC_except_table152
- GCC_except_table155
- GCC_except_table158
- GCC_except_table50
- GCC_except_table57
- GCC_except_table75
- GCC_except_table85
- GCC_except_table88
- GCC_except_table90
- GCC_except_table98
- _objc_msgSend$_serverConnectionInvalidated
CStrings:
+ "Connection to [%{public}@] interrupted"
+ "Connection to [%{public}@] invalidated; clearing cached connection so the next request reconnects"
+ "Opened a connection to [%{public}@]"
+ "Received account changed: changeType=%ld accountId=%{public}@"
+ "Sent account changed to the daemon: changeType=%ld accountId=%{public}@"
- "\r"
- "Connection to [%@] interrupted"
- "Connection to [%@] invalidated"
- "Received account changed"
```
