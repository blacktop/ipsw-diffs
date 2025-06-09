## UserFS

> `/System/Library/PrivateFrameworks/UserFS.framework/UserFS`

```diff

-716.120.2.0.0
-  __TEXT.__text: 0x154c
-  __TEXT.__auth_stubs: 0x270
+741.0.0.0.0
+  __TEXT.__text: 0x16a0
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__const: 0x38
+  __TEXT.__gcc_except_tab: 0x110
   __TEXT.__cstring: 0x21a
-  __TEXT.__oslogstring: 0x14d
+  __TEXT.__oslogstring: 0x178
   __TEXT.__unwind_info: 0xc8
   __TEXT.__objc_classname: 0x1c
   __TEXT.__objc_methname: 0x2a9

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
-  __AUTH_CONST.__auth_got: 0x148
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x90
   __AUTH.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 786A760F-71EE-3823-991E-EBD06C665534
-  Functions: 27
-  Symbols:   148
-  CStrings:  62
+  UUID: F39F1D43-619D-3E15-A1BC-8F1FBC2C739E
+  Functions: 29
+  Symbols:   153
+  CStrings:  64
 
Symbols:
+ -[LiveFSUSBLocalStorageClient loadVolumes:ofType:withError:].cold.2
+ -[LiveFSUSBLocalStorageClient loadVolumes:ofType:withError:].cold.3
+ _objc_autorelease
Functions:
~ -[LiveFSUSBLocalStorageClient loadVolumes:ofType:withError:] : 804 -> 956
CStrings:
+ "connection:error:%@"
+ "volumes:count:0:ENOENT"

```
