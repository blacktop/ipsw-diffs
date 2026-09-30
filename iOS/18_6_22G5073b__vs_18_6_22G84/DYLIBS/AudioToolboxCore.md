## AudioToolboxCore

> `/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`

```diff

-1456.701.0.0.0
-  __TEXT.__text: 0x3084f8
+1456.703.0.0.0
+  __TEXT.__text: 0x308514
   __TEXT.__auth_stubs: 0x38b0
   __TEXT.__objc_methlist: 0x3604
   __TEXT.__const: 0x225bd
   __TEXT.__dlopen_cstrs: 0x50a
-  __TEXT.__gcc_except_tab: 0x25e9c
+  __TEXT.__gcc_except_tab: 0x25e98
   __TEXT.__cstring: 0x1b813
-  __TEXT.__oslogstring: 0x1393a
+  __TEXT.__oslogstring: 0x13b0a
   __TEXT.__dof_AudioTool: 0x4f1
   __TEXT.__dof_AUHosting: 0x23c
   __TEXT.__dof_AudioConv: 0x129e

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: C7F7ADB8-7C97-3363-9971-E6B45BB070AB
+  UUID: 9C7FA16D-FCB6-31AA-8560-CDD62B1650A6
   Functions: 11067
   Symbols:   29184
-  CStrings:  9094
+  CStrings:  9099
 
Functions:
~ __ZN12AMRAudioFile14ScanForPacketsExP10DataSourceb : 1004 -> 1016
~ __ZN4acv214CodecConverter11SetPropertyEjjPKv : 1884 -> 1900
CStrings:
+ "%25s:%-5d ASSERTION FAILURE [(!mIsServer) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(inBufferList.size() == outBufferList.size()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mBufferCapacity == 0 || nBytes <= mBufferCapacity) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mBufferMemory == __null) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(nBytes <= buf->mDataByteSize) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(numChannels == OutputFormat().mChannelsPerFrame) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE: "

```
