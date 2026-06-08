## YonkersUtil

> `/usr/libexec/YonkersUtil`

```diff

-6.72.7.0.0
-  __TEXT.__text: 0x404
-  __TEXT.__auth_stubs: 0xf0
-  __TEXT.__cstring: 0x137
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x78
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x20
-  __DATA_CONST.__cfstring: 0xa0
-  __DATA.__data: 0x60
+7.113.1.0.0
+  __TEXT.__text: 0x680
+  __TEXT.__auth_stubs: 0x110
+  __TEXT.__cstring: 0x273
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__const: 0x38
+  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__got: 0x20
+  __DATA.__data: 0xa0
   __DATA.__common: 0x4
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
-  - /System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: E5CD8831-4C76-37F3-85F9-08C399DD7472
-  Functions: 5
-  Symbols:   21
-  CStrings:  24
+  UUID: 2CEB9F34-1DE6-3C33-9FA4-CFF77169B362
+  Functions: 7
+  Symbols:   24
+  CStrings:  43
 
Symbols:
+ _CFStringCreateWithFormat
+ _optarg
+ _strtoul
CStrings:
+ "\t\t --certData\t\t\t\t\tGet the certification data struct"
+ "\t\t --number\t\t\t\t\tSensor number (< %d) \n"
+ "\t\t --provCertData\t\t\t\tGet the provenance certification data struct"
+ "%s: ERROR: Did not specify which sensor cert data is needed \n"
+ "%s: ERROR: Sensor number out of bounds (sensorNumber = %ld) \n"
+ "%sChipID"
+ "%sECPubKey"
+ "%sECPubKeyHmac"
+ "%sMNS"
+ "%sMacAlgo"
+ "%sProvPubKey"
+ "%sProvPubKeyHmac"
+ "%sPubKey"
+ "%sPubKeyHmac"
+ "%sUID"
+ "Yonkers"
+ "YonkersIR1"
+ "YonkersIR2"
+ "c:p:n:h"
+ "number"
+ "provCertData"
- "\t\t --certData\t\t\t\t\tGet the Yonkers certification data struct"
- "YonkersChipID"
- "YonkersMNS"
- "YonkersPubKey"
- "YonkersPubKeyHmac"
- "YonkersUID"
- "c:h"

```
