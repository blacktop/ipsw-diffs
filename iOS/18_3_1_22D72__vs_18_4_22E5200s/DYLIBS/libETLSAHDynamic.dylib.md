## libETLSAHDynamic.dylib

> `/usr/lib/libETLSAHDynamic.dylib`

```diff

-1220.0.0.0.0
-  __TEXT.__text: 0x1c10
+1245.0.0.0.0
+  __TEXT.__text: 0x1db4
   __TEXT.__auth_stubs: 0xe0
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x751
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__cstring: 0x8e2
+  __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x80
   __AUTH_CONST.__auth_got: 0x70

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 37
+  Functions: 36
   Symbols:   51
-  CStrings:  62
+  CStrings:  73
 
CStrings:
+ "Command buffer has invalid length %u, which is less than the size of the command header (%u)\n"
+ "Couldn't allocate memory for memory read buffer\n"
+ "ETLSAHCommandCreateHelloResponseExt"
+ "ETLSAHCommandSend"
+ "Error: Given Reserved Length cannot be more than %lu bytes\n"
+ "Got Command of type %u, length %u\n"
+ "Sending command of length %u, type %u\n"
+ "Transport is invalid, max tx packet size = %d\n"
+ "false"
+ "noZLP = %s\n"
+ "true"

```
