## gpudebug

> `/usr/bin/gpudebug`

```diff

-  __TEXT.__text: 0x1fb14
+  __TEXT.__text: 0x1fa58
   __TEXT.__auth_stubs: 0xb40
   __TEXT.__objc_stubs: 0x2820
   __TEXT.__objc_methlist: 0x24d4
   __TEXT.__const: 0xf0
   __TEXT.__oslogstring: 0x1d8
-  __TEXT.__cstring: 0x2cb4
+  __TEXT.__cstring: 0x2c8c
   __TEXT.__objc_methname: 0x3036
   __TEXT.__objc_classname: 0x504
   __TEXT.__objc_methtype: 0xa2e
   __TEXT.__ustring: 0x6a
   __TEXT.__unwind_info: 0x740
   __DATA_CONST.__const: 0x8f0
-  __DATA_CONST.__cfstring: 0x1800
+  __DATA_CONST.__cfstring: 0x17c0
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__auth_got: 0x5a8
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x4610
   __DATA.__objc_selrefs: 0xdb0

   - /usr/lib/libobjc.A.dylib
   Functions: 845
   Symbols:   231
-  CStrings:  1661
+  CStrings:  1657
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
~ __DATA.__common : content changed
Functions:
~ sub_100006bb0 : 3800 -> 3788
~ sub_100007dc4 -> sub_100007db8 : 196 -> 4
~ sub_10000d5e4 -> sub_10000d518 : 268 -> 276
~ sub_10000e828 -> sub_10000e764 : 116 -> 124
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_hash.c:95"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_tables.c:70"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_thread_mutex.c:50"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UnTk0Y/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_hash.c:95"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UnTk0Y/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_tables.c:70"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UnTk0Y/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_thread_mutex.c:50"
- "Profile collecting..."
- "Profile error: %@"

```
