## MessagesCloudSync

> `/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync`

```diff

-1491.200.73.0.0
-  __TEXT.__text: 0xf84d4
+1491.200.95.0.0
+  __TEXT.__text: 0xf9120
   __TEXT.__objc_methlist: 0xcb0
-  __TEXT.__const: 0x99b0
+  __TEXT.__const: 0x9bc0
   __TEXT.__cstring: 0x3ef1
-  __TEXT.__constg_swiftt: 0x2c34
-  __TEXT.__swift5_typeref: 0x2868
-  __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x307a
-  __TEXT.__swift5_fieldmd: 0x33bc
-  __TEXT.__swift5_assocty: 0x5b8
-  __TEXT.__oslogstring: 0x5a33
-  __TEXT.__swift5_proto: 0x75c
-  __TEXT.__swift5_types: 0x2dc
+  __TEXT.__constg_swiftt: 0x2c60
+  __TEXT.__swift5_typeref: 0x28de
+  __TEXT.__swift5_builtin: 0x154
+  __TEXT.__swift5_reflstr: 0x30aa
+  __TEXT.__swift5_fieldmd: 0x33d8
+  __TEXT.__swift5_assocty: 0x618
+  __TEXT.__oslogstring: 0x5b63
+  __TEXT.__swift5_proto: 0x770
+  __TEXT.__swift5_types: 0x2e0
   __TEXT.__swift5_capture: 0xfd8
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0x90
   __TEXT.__swift_as_entry: 0x458
   __TEXT.__swift_as_ret: 0x520
   __TEXT.__swift_as_cont: 0xa04
-  __TEXT.__unwind_info: 0x4230
+  __TEXT.__unwind_info: 0x4240
   __TEXT.__eh_frame: 0xa354
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1020
+  __DATA_CONST.__objc_selrefs: 0x1048
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x7e0
-  __AUTH_CONST.__const: 0x8e51
+  __AUTH_CONST.__const: 0x8e79
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x2768
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1158
+  __AUTH_CONST.__auth_got: 0x1168
   __AUTH.__objc_data: 0x3d8
   __AUTH.__data: 0x508
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0xf98
+  __DATA.__data: 0xfd8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x618
-  __DATA_DIRTY.__data: 0x27d0
+  __DATA_DIRTY.__data: 0x27c0
   __DATA_DIRTY.__bss: 0x4c80
   __DATA_DIRTY.__common: 0x270
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3896
+  Functions: 3926
   Symbols:   442
-  CStrings:  870
+  CStrings:  872
 
CStrings:
+ "Transfer %s: could not size the record's asset at %s; not adopting the cloud copy"
+ "Transfer %s: could not size the record's asset at %s; not preferring the local copy"
+ "Transfer %s: incoming has unknown pgen state, but local is valid. Incoming stored pgen state %ld, resolved %ld, attributionInfo %s. Existing stored pgen state %ld, resolved %ld, attributionInfo %s"
+ "Transfer %s: local data newer than cloud; marking fieldsToSync %s to update server"
- "Transfer %s: incoming has unknown pgen state, but local progressed past that, it is newer than cloud"
- "Transfer %s: local data newer than cloud; marking dirty to update server"
```
