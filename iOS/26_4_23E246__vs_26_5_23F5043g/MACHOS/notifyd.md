## notifyd

> `/usr/sbin/notifyd`

```diff

-348.100.7.0.0
-  __TEXT.__text: 0xb2b0
-  __TEXT.__auth_stubs: 0x930
+348.120.3.502.1
+  __TEXT.__text: 0xb3fc
+  __TEXT.__auth_stubs: 0x940
   __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x1b94
-  __DATA_CONST.__auth_got: 0x498
+  __TEXT.__cstring: 0x1c56
+  __DATA_CONST.__auth_got: 0x4a0
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0xb30
   __DATA.__data: 0x8

   __DATA.__bss: 0x2d0
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 2C3A1492-064E-3795-9104-84BCFE51D770
-  Functions: 134
-  Symbols:   164
-  CStrings:  279
+  UUID: B96B5BA7-2FC7-3BA2-8DB7-54DBA2BED070
+  Functions: 135
+  Symbols:   165
+  CStrings:  281
 
Symbols:
+ _terminate_with_reason
CStrings:
+ "BUG IN CLIENT OF NOTIFYD: exceeded registration limit. Last registration was for name %s as %s"
+ "Process %d exceeded registration limit (%u), terminating. Last registration was for name %s as %s\n"

```
