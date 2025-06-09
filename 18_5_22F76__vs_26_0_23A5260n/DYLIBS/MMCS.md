## MMCS

> `/System/Library/PrivateFrameworks/MMCS.framework/MMCS`

```diff

-2250.16.0.0.0
-  __TEXT.__text: 0x830e4
-  __TEXT.__auth_stubs: 0x1ca0
+2300.114.0.0.0
+  __TEXT.__text: 0x836c8
+  __TEXT.__auth_stubs: 0x1cc0
   __TEXT.__objc_methlist: 0xc10
   __TEXT.__const: 0x99c
-  __TEXT.__oslogstring: 0x4702
-  __TEXT.__cstring: 0x17814
+  __TEXT.__oslogstring: 0x476c
+  __TEXT.__cstring: 0x178ff
   __TEXT.__gcc_except_tab: 0x714
-  __TEXT.__unwind_info: 0x1540
+  __TEXT.__unwind_info: 0x1510
   __TEXT.__objc_classname: 0x11e
-  __TEXT.__objc_methname: 0x21db
+  __TEXT.__objc_methname: 0x21e3
   __TEXT.__objc_methtype: 0x178b
-  __TEXT.__objc_stubs: 0x1940
+  __TEXT.__objc_stubs: 0x1960
   __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x53e8
+  __DATA_CONST.__const: 0x53c8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b0
+  __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xe60
+  __AUTH_CONST.__auth_got: 0xe70
   __AUTH_CONST.__const: 0x2d10
-  __AUTH_CONST.__cfstring: 0xce80
+  __AUTH_CONST.__cfstring: 0xcf00
   __AUTH_CONST.__objc_const: 0x1240
   __DATA.__objc_ivar: 0xa4
   __DATA.__data: 0x468

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BB6C5547-D28B-3A80-A85A-573228F4F4B1
-  Functions: 2387
-  Symbols:   6215
-  CStrings:  5148
+  UUID: 9248DEE8-4C29-3A26-91E5-07E7ED71877F
+  Functions: 2388
+  Symbols:   6218
+  CStrings:  5158
 
Symbols:
+ _ACSUpdateCachingServerHealth
+ ___block_descriptor_tmp.193
+ ___block_descriptor_tmp.276
+ _kMMCSRequestOptionAllowsUCA
+ _objc_msgSend$_setAllowsUCA:
+ _objc_msgSend$setAllowsUCA:
+ _qos_class_self
- ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_tmp.187
- ___block_descriptor_tmp.270
- _objc_msgSend$setQualityOfService:
CStrings:
+ "Failed to update proxy cache server health with error %@"
+ "Failed to update proxy cache server health with unknown error"
+ "Network activities are not expected to be NULL and an allocation might have failed due to unknown reason."
+ "Request for object %p cancelled. %d requests now in-flight, %ld total requests enqueued"
+ "_setAllowsUCA:"
+ "kMMCSRequestOptionAllowsUCA"
+ "setAllowsUCA:"
- "setQualityOfService:"

```
