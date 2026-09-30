## loginsupport

> `/System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport`

```diff

-259.0.0.0.0
-  __TEXT.__text: 0x1a70
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x4b9
+259.5.1.0.0
+  __TEXT.__text: 0x1a64
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x484
   __TEXT.__oslogstring: 0xaf
   __TEXT.__unwind_info: 0xc8
   __TEXT.__objc_methname: 0xc

   __DATA_CONST.__const: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1b0
-  __AUTH_CONST.__const: 0xc8
-  __AUTH_CONST.__cfstring: 0x300
+  __AUTH_CONST.__auth_got: 0x1a0
+  __AUTH_CONST.__const: 0xe8
+  __AUTH_CONST.__cfstring: 0x2e0
   __DATA.__bss: 0x98
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E17461AF-3BCD-371F-8303-9E64DB168069
-  Functions: 31
-  Symbols:   121
-  CStrings:  68
+  UUID: 11521B87-71EA-39A7-92CC-A577D85EDBA5
+  Functions: 36
+  Symbols:   128
+  CStrings:  66
 
Symbols:
+ DBLoggerCreate.cold.1
+ DBLoggingLogWithFormat.cold.1
+ DBLoggingStartWithController.cold.1
+ DBLoggingStopController.cold.1
+ _DBLoggerForController.cold.1
+ _DBLoggerInitialize.onceToken
+ _DBLoggersLock.cold.1
+ ___RegisterForSignal_block_invoke_2.cold.1
+ ____DBLoggerInitialize_block_invoke
+ __block_literal_global.36
+ __block_literal_global.38
+ __block_literal_global.73
+ __block_literal_global.78
+ __block_literal_global.80
- _CFArrayAppendValue
- _CFArrayGetFirstIndexOfValue
- _DBLoggerInitialize.initialized
- __block_literal_global.39
- __block_literal_global.74
- __block_literal_global.79
- __block_literal_global.81
CStrings:
+ "The maximum number (%d) of DBLoggingControllers have been registered"
- "Failed to add the DBLoggingController to the DBLogging"
- "The maximum number (%d) of DBLoggingControllers have be registered"

```
