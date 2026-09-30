## libETLSAHDynamic.dylib

> `/usr/lib/libETLSAHDynamic.dylib`

```diff

-1249.1.0.0.0
-  __TEXT.__text: 0x1bdc
-  __TEXT.__auth_stubs: 0xe0
+1371.0.1.0.0
+  __TEXT.__text: 0x23dc
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x751
-  __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__got: 0x8
+  __TEXT.__cstring: 0x91f
+  __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x70
+  __AUTH_CONST.__auth_got: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libETLDLOADDynamic.dylib
   - /usr/lib/libETLDynamic.dylib

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: C5FA4377-A020-3EE3-AED3-9B85225331B6
-  Functions: 36
-  Symbols:   52
-  CStrings:  62
+  UUID: D862AB54-A201-30D0-A76E-20C101F738F9
+  Functions: 41
+  Symbols:   55
+  CStrings:  73
 
Symbols:
+ _ETLSAHCommandCreateMemoryRead64Bit
+ _ETLSAHCommandParseMemoryDebug64Bit
+ _ETLSAHGetDebugRecordCount64Bit
+ _ETLSAHGetDebugTable64Bit
+ _ETLSAHGetRecordEx64Bit
+ __ETLDebugPrintBinaryVerbose
- _CFNumberGetValue
- __ZN12capabilities8coredump17coredumpInterfaceEv
- _kTelephonyUtilTransportConfigMaxPacketSize
CStrings:
+ "Command buffer has invalid length %u, which is less than the size of the command header (%u)\n"
+ "Couldn't allocate memory for memory read buffer\n"
+ "ETLSAHCommandCreateHelloResponseExt"
+ "ETLSAHCommandSend"
+ "ETLSAHGetDebugRecordCount64Bit"
+ "ETLSAHGetDebugTable64Bit"
+ "ETLSAHGetRecordEx64Bit"
+ "ETLSAHSendReadData"
+ "Error: Given Reserved Length cannot be more than %lu bytes\n"
+ "Got Command of type %u, length %u\n"
+ "Read failed. success = %u, read %u of %llu\n"
+ "Sending command of length %u, type %u\n"
- "Received:"

```
