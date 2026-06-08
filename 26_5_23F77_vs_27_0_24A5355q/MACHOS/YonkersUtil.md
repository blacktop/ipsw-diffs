## YonkersUtil

> `/usr/libexec/YonkersUtil`

```diff

-6.72.7.0.0
-  __TEXT.__text: 0x404 sha256:060f5fa608ecf1497d253c286c8798174832126785707a30be1d14e40f0aca8c
-  __TEXT.__auth_stubs: 0xf0 sha256:515fd58d60519cd0635e5181dc8cfb628014513ef99773468b45d876dd6e834c
-  __TEXT.__cstring: 0x137 sha256:07ec38d80201b407b721a81187cd81418c2220aa2b26324686f395402ffa2028
-  __TEXT.__unwind_info: 0x70 sha256:83b1254b07c1388e9bdc41a0216205adefb0e2eb30255ec3d4481d645e2a6e9b
-  __DATA_CONST.__auth_got: 0x78 sha256:38c345cb9cf8745099627a43c391a1581c0c6e90e4af5679a2e9737df975dec9
-  __DATA_CONST.__got: 0x18 sha256:c095fa9c9ac698a092bc2d1f1f19fd962bc2b47d5e911cc6ecc8be364c73a186
-  __DATA_CONST.__const: 0x20 sha256:ebcb5633034f573d23f230beff9861ae9fd673f7b38a21bfb2f3ff45d999c5d4
-  __DATA_CONST.__cfstring: 0xa0 sha256:27c53ff1022800126269232a1b0aa048bd51c62aeffb2c3f681118c3db5c9746
-  __DATA.__data: 0x60 sha256:b541db7b10f9d564102c8b3b584e0e6728557b6104cf2d60417c20cef4ad00ce
+7.113.1.0.0
+  __TEXT.__text: 0x680 sha256:2efbad867d0356fc1864247910afba2d992fea743ae1c7673027e708ec5a6e44
+  __TEXT.__auth_stubs: 0x110 sha256:d306fa3716f9eb6533eb0cd70699706a1a3eaa08d4994ab3d904d5a0117ad18b
+  __TEXT.__cstring: 0x273 sha256:f74485d43191b9d4e427d537ed629e2dc57a3242ddc926b06de4d2117a56d3a3
+  __TEXT.__unwind_info: 0x78 sha256:5ec0895e64580482352909bf3a54f3e0510830806534a348243c69aa2465754d
+  __DATA_CONST.__const: 0x38 sha256:3338a7d385bd8f1d0737f09e105cfd6869568da6cbcd4a7924c6f33e48714b43
+  __DATA_CONST.__cfstring: 0x140 sha256:de8e32dea9cb7868b2252f2679c20cda82cfad1a9b76697c81da9caa6ab2a2b5
+  __DATA_CONST.__auth_got: 0x88 sha256:5379588d64ffd389709190bdc3a806492011d076aca63e0d31f4bd7307efffa5
+  __DATA_CONST.__got: 0x20 sha256:aea25a635b5ab9432fcf441fb3822c117d58d13b04aa34a0157abd264b1597b5
+  __DATA.__data: 0xa0 sha256:1c973516d11b373118219683ce14abdc3597f149a35131c134e10463682be480
   __DATA.__common: 0x4 sha256:df3f619804a92fdb4057192dc43dd748ea778adc52bc498ce80524c014b81119
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
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
