## GNSSPassthroughLib

> `/System/Library/Extensions/AppleSPU.kext/Contents/PlugIns/GNSSPassthroughLib.plugin/Contents/MacOS/GNSSPassthroughLib`

```diff

-1084.0.0.0.0
-  __TEXT.__text: 0x192c sha256:8c06e1fb12fec65506ca65ef118b1adbe23e7ed30dde8bc8aeb3f8c8000ae150
+1087.0.0.0.0
+  __TEXT.__text: 0x1bdc sha256:ad23fc6154522ce10bdcdda239f43f8564858e8478e6032926ee53abb4b96883
   __TEXT.__const: 0x80 sha256:3a4ed80240117d40744f63c2a73d6586c5b7df3afefb783dd43880a2442dbef7
-  __TEXT.__gcc_except_tab: 0xac sha256:60c99e2d40c4980ae39ffe00bf5ec2e3645fe16a92c5b7bb42a136867e96f401
+  __TEXT.__gcc_except_tab: 0xac sha256:bc56c973d57418b60ba3aa4ef4767247dcc5c8365aa28e894f158da9ab58412f
   __TEXT.__cstring: 0x124 sha256:333c1490458842ba970c4c72e250f0a1af1331a9413ce2354749281f3e93eb05
-  __TEXT.__oslogstring: 0xc1 sha256:27388fe0ec31c0fef01a86f7e7bb81903185e51dd1bcb9210937e54410f15445
-  __TEXT.__unwind_info: 0x160 sha256:423389f8eb6f001b11d272414e0f7da55420c65fb9ab8a275066c3743313709c
+  __TEXT.__oslogstring: 0x2a8 sha256:488c3b6ac9752e5fb89d4c77259fb67306c0c0d671e5938f778f7ef597dabdb9
+  __TEXT.__unwind_info: 0x170 sha256:5a87064020727df4cbba8fafb7c249fdc1efa8cf5aeeef912cca3ad0fe21ffa7
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x20 sha256:a9fb71c49e4378333101507ae2e20324b5c6b847cc51ee44e42db5f63de5de87
+  __DATA_CONST.__const: 0x20 sha256:c1a49fe614121f1ef04a3ddb7e0efd446ded703b70d80acc2f4b53ba595d17ff
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x80 sha256:f6a406d0b9fd8472dff5e9c55a2030e13a45273de4aa24daa743c4ce9f094b0e
+  __AUTH_CONST.__cfstring: 0x80 sha256:2342e3099cb02ec524051c4ca9b051c43a037ad597d4631ee78b1d6f0574e671
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__data: 0x80 sha256:cb3c117f40c7b93d00c20802ef160eb0e09ab958c100b674d205b27b59f30a9b
+  __AUTH.__data: 0x80 sha256:a9f4316c345c3f018804a6eb9aafed6feb9e87ad7ea1a8b2fe6697ce22bab21c
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 674D8563-0480-36B3-9A21-156A91F5ED17
-  Functions: 62
+  UUID: 9A25CC90-C409-3DD6-9FAA-AA7EB0A91C84
+  Functions: 66
   Symbols:   109
-  CStrings:  23
+  CStrings:  31
 
CStrings:
+ "GNSSPassthrough::RegisterDataHandler result %d"
+ "GNSSPassthrough::RegisterEventHandler result %d"
+ "GNSSPassthrough::SetDispatchQueue kIOReturnBadArgument"
+ "GNSSPassthrough::SetDispatchQueue kIOReturnStillOpen"
+ "GNSSPassthrough::_registerDataQueueHandler _dataQueueAddr already set"
+ "GNSSPassthrough::_registerDataQueueHandler _dataQueuePort already set"
+ "GNSSPassthrough::_registerEventQueueHandler _eventQueueAddr already set"
+ "GNSSPassthrough::_registerEventQueueHandler _eventQueuePort already set"

```
