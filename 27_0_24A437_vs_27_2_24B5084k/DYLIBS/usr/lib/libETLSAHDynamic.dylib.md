## libETLSAHDynamic.dylib

> `/usr/lib/libETLSAHDynamic.dylib`

```diff

-1585.0.0.0.0
-  __TEXT.__text: 0x2250
+1594.0.0.0.0
+  __TEXT.__text: 0x250c
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x7fe
-  __TEXT.__unwind_info: 0x110
+  __TEXT.__cstring: 0x95d
+  __TEXT.__unwind_info: 0x108
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x80
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 41
-  Symbols:   54
-  CStrings:  67
+  Symbols:   55
+  CStrings:  75
 
Symbols:
+ __ETLDebugPrintBinaryVerbose
Functions:
~ _ETLSAHCommandSend : 112 -> 200
~ _ETLSAHSendReadData : 120 -> 160
~ _ETLSAHCommandReceive : 308 -> 400
~ _ETLSAHCommandExecute : 724 -> 832
~ _ETLSAHCommandCreateHelloResponseExt : 108 -> 176
~ _ETLSAHGetDebugRecordCount : 420 -> 476
~ _ETLSAHGetDebugRecordCount64Bit : 416 -> 472
~ _ETLSAHGetRecordEx : 556 -> 652
~ _ETLSAHGetRecordEx64Bit : 568 -> 664
CStrings:
+ "Command buffer has invalid length %u, which is less than the size of the command header (%zu)\n"
+ "Couldn't allocate memory for memory read buffer\n"
+ "ETLSAHCommandCreateHelloResponseExt"
+ "ETLSAHCommandSend"
+ "ETLSAHSendReadData"
+ "Error: Given Reserved Length cannot be more than %lu bytes\n"
+ "Got Command of type %u, length %u\n"
+ "Sending command of length %u, type %u\n"
```
