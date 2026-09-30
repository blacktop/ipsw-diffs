## libETLSAHDynamic.dylib

> `/usr/lib/libETLSAHDynamic.dylib`

```diff

 1418.1.0.0.0
-  __TEXT.__text: 0x2500
-  __TEXT.__auth_stubs: 0xd0
+  __TEXT.__text: 0x2244
+  __TEXT.__auth_stubs: 0xc0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x95c
+  __TEXT.__cstring: 0x7fe
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
-  UUID: 5844DFFB-6281-30DA-A718-485B19B6F963
+  UUID: 53613075-8830-3888-8850-1247B88174F2
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
