## GNSSPassthroughLib

> `/System/Library/Extensions/AppleSPU.kext/PlugIns/GNSSPassthroughLib.plugin/GNSSPassthroughLib`

```diff

-1084.0.0.0.0
-  __TEXT.__text: 0x192c sha256:0df12fd24404139c6bec6f8a715a1faed763dcb41e2f61420e1ca359b600b70d
+1087.0.0.0.0
+  __TEXT.__text: 0x1bdc sha256:2304a17a7b078d2ee8295e475576fe4437f13a32a8ff72a759b2a08fcc46640c
   __TEXT.__const: 0x80 sha256:3a4ed80240117d40744f63c2a73d6586c5b7df3afefb783dd43880a2442dbef7
-  __TEXT.__gcc_except_tab: 0xac sha256:60c99e2d40c4980ae39ffe00bf5ec2e3645fe16a92c5b7bb42a136867e96f401
+  __TEXT.__gcc_except_tab: 0xac sha256:bc56c973d57418b60ba3aa4ef4767247dcc5c8365aa28e894f158da9ab58412f
   __TEXT.__cstring: 0x124 sha256:333c1490458842ba970c4c72e250f0a1af1331a9413ce2354749281f3e93eb05
-  __TEXT.__oslogstring: 0xc1 sha256:27388fe0ec31c0fef01a86f7e7bb81903185e51dd1bcb9210937e54410f15445
-  __TEXT.__unwind_info: 0x168 sha256:e15a37636f82cfaa4a03a0410eded93d57629609f7f18f8dec1756cb75bd644f
+  __TEXT.__oslogstring: 0x2a8 sha256:488c3b6ac9752e5fb89d4c77259fb67306c0c0d671e5938f778f7ef597dabdb9
+  __TEXT.__unwind_info: 0x180 sha256:87dad54315ce7c376d8d1a8ef34cd1d273dfdf8f7085852603b2e4afe29fb9c7
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x20 sha256:1daffd0dfced89c114e54046f39d6460653ee78ab0d6404a80ef2686194dc471
+  __DATA_CONST.__const: 0x20 sha256:c059d44f7c3194e51fd83825f04e9f2aa9039047ae0258f8dbd52b6ccfa64e8c
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x80 sha256:f3a2a625222862453d06ef9cddb3564a378b94a162257effef74d18735fc39d5
+  __AUTH_CONST.__cfstring: 0x80 sha256:de986dfe7ec10d3a7da745d9667516a11da6833531965c75296883e151d85b32
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__data: 0x80 sha256:0c856e0eb221f53f58254f5ca7ff86a8db8c1c8da6fe23c3157a6bc6e36f4668
+  __AUTH.__data: 0x80 sha256:af8320b05292e19bbd81fc1dcc666cc0bceb76b9caef0742e4581d16ad9033d9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 449EE5DA-DEB1-3950-888E-41AE67EBC988
-  Functions: 62
+  UUID: AEAEFA78-B434-3F75-97E3-1C9D3E8711C0
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
