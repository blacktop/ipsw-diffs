## libETLSAHDynamic.dylib

> `/usr/lib/libETLSAHDynamic.dylib`

```diff

-1390.0.0.0.0
-  __TEXT.__text: 0x23dc
-  __TEXT.__auth_stubs: 0xd0
+1391.0.0.0.0
+  __TEXT.__text: 0x2120
+  __TEXT.__auth_stubs: 0xc0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x91f
+  __TEXT.__cstring: 0x7c1
   __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x68
+  __AUTH_CONST.__auth_got: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libETLDLOADDynamic.dylib
   - /usr/lib/libETLDynamic.dylib

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 06C46004-EAFB-3569-A326-86DFB19E796A
+  UUID: D4D2667B-74D4-37BA-A94E-51A1A0FA1D81
   Functions: 41
-  Symbols:   55
-  CStrings:  73
+  Symbols:   54
+  CStrings:  65
 
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
~ _ETLSAHGetRecordEx : 656 -> 560
~ _ETLSAHGetRecordEx64Bit : 668 -> 572
CStrings:
- "Command buffer has invalid length %u, which is less than the size of the command header (%u)\n"
- "Couldn't allocate memory for memory read buffer\n"
- "ETLSAHCommandCreateHelloResponseExt"
- "ETLSAHCommandSend"
- "ETLSAHSendReadData"
- "Error: Given Reserved Length cannot be more than %lu bytes\n"
- "Got Command of type %u, length %u\n"
- "Sending command of length %u, type %u\n"

```
