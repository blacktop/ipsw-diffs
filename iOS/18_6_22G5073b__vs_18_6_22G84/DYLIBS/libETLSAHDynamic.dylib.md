## libETLSAHDynamic.dylib

> `/usr/lib/libETLSAHDynamic.dylib`

```diff

 1249.1.0.0.0
-  __TEXT.__text: 0x1db4
+  __TEXT.__text: 0x1bdc
   __TEXT.__auth_stubs: 0xe0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x8e2
-  __TEXT.__unwind_info: 0xe0
+  __TEXT.__cstring: 0x751
+  __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x80
   __AUTH_CONST.__auth_got: 0x70

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: CC644837-79D2-34D5-A8B5-CB9CD56224B7
+  UUID: 81636A72-977D-3041-BAC6-D8856D5114E3
   Functions: 36
   Symbols:   52
-  CStrings:  73
+  CStrings:  62
 
Functions:
~ _ETLSAHGetRecordEx : 872 -> 720
~ _ETLSAHCommandReceive : 404 -> 308
~ _ETLSAHCommandSend : 176 -> 112
~ _ETLSAHGetDebugRecordCount : 452 -> 420
~ _ETLSAHCommandExecute : 784 -> 724
~ _ETLSAHCommandCreateHelloResponseExt : 176 -> 108
CStrings:
- "Command buffer has invalid length %u, which is less than the size of the command header (%u)\n"
- "Couldn't allocate memory for memory read buffer\n"
- "ETLSAHCommandCreateHelloResponseExt"
- "ETLSAHCommandSend"
- "Error: Given Reserved Length cannot be more than %lu bytes\n"
- "Got Command of type %u, length %u\n"
- "Sending command of length %u, type %u\n"
- "Transport is invalid, max tx packet size = %d\n"
- "false"
- "noZLP = %s\n"
- "true"

```
