## libETLSAHDynamic.dylib

> `/usr/lib/libETLSAHDynamic.dylib`

```diff

-1397.0.0.0.0
-  __TEXT.__text: 0x2244
-  __TEXT.__auth_stubs: 0xc0
+1399.2.0.0.0
+  __TEXT.__text: 0x2500
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x7fe
+  __TEXT.__cstring: 0x95c
   __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__const: 0x80
-  __AUTH_CONST.__auth_got: 0x60
+  __AUTH_CONST.__auth_got: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libETLDLOADDynamic.dylib
   - /usr/lib/libETLDynamic.dylib

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 295D2E1D-AAF9-3A7C-9CBD-F658067A407F
+  UUID: 31F02A9B-4CE9-3ECD-A2DC-810D780FB365
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
~ _ETLSAHGetRecordEx : 560 -> 656
~ _ETLSAHGetRecordEx64Bit : 572 -> 668
CStrings:
+ "Command buffer has invalid length %u, which is less than the size of the command header (%u)\n"
+ "Couldn't allocate memory for memory read buffer\n"
+ "ETLSAHCommandCreateHelloResponseExt"
+ "ETLSAHCommandSend"
+ "ETLSAHSendReadData"
+ "Error: Given Reserved Length cannot be more than %lu bytes\n"
+ "Got Command of type %u, length %u\n"
+ "Sending command of length %u, type %u\n"

```
