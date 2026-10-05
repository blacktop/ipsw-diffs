## libETLSAHDynamic.dylib

> `/usr/lib/libETLSAHDynamic.dylib`

```diff

 1594.0.0.0.0
-  __TEXT.__text: 0x250c
+  __TEXT.__text: 0x2250
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x95d
-  __TEXT.__unwind_info: 0x108
+  __TEXT.__cstring: 0x7fe
+  __TEXT.__unwind_info: 0x110
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x80
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 41
-  Symbols:   55
-  CStrings:  75
+  Symbols:   54
+  CStrings:  67
 
Symbols:
- __ETLDebugPrintBinaryVerbose
Functions:
~ _ETLSAHCommandSend : 200 -> 112
~ _ETLSAHSendReadData : 160 -> 120
~ _ETLSAHCommandReceive : 400 -> 308
~ _ETLSAHCommandExecute : 832 -> 724
~ _ETLSAHCommandCreateHelloResponseExt : 176 -> 108
~ _ETLSAHGetDebugRecordCount : 476 -> 420
~ _ETLSAHGetDebugRecordCount64Bit : 472 -> 416
~ _ETLSAHGetRecordEx : 652 -> 556
~ _ETLSAHGetRecordEx64Bit : 664 -> 568
CStrings:
- "Command buffer has invalid length %u, which is less than the size of the command header (%zu)\n"
- "Couldn't allocate memory for memory read buffer\n"
- "ETLSAHCommandCreateHelloResponseExt"
- "ETLSAHCommandSend"
- "ETLSAHSendReadData"
- "Error: Given Reserved Length cannot be more than %lu bytes\n"
- "Got Command of type %u, length %u\n"
- "Sending command of length %u, type %u\n"
```
