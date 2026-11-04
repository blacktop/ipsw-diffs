## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

```diff

-430.0.0.0.0
-  __TEXT.__text: 0x17acc
+430.1.0.0.0
+  __TEXT.__text: 0x17e84
   __TEXT.__lazy_helpers: 0x54
   __TEXT.__objc_methlist: 0xb74
-  __TEXT.__const: 0x288
+  __TEXT.__const: 0x268
   __TEXT.__gcc_except_tab: 0x214
-  __TEXT.__cstring: 0x4697
-  __TEXT.__oslogstring: 0x2d1c
+  __TEXT.__cstring: 0x46a7
+  __TEXT.__oslogstring: 0x2de8
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x858
+  __TEXT.__unwind_info: 0x870
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1898
+  __DATA_CONST.__const: 0x18a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__got: 0x1f8
   __AUTH_CONST.__const: 0x5a0
-  __AUTH_CONST.__cfstring: 0x5d20
+  __AUTH_CONST.__cfstring: 0x5d40
   __AUTH_CONST.__objc_const: 0x1cb8
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 607
-  Symbols:   1372
-  CStrings:  1012
+  Functions: 611
+  Symbols:   1377
+  CStrings:  1015
 
Symbols:
+ _HTDurationInBackgroundCPURolesFromSortedArray
+ _HTIsBackgroundCPURoleHang
+ _HTIsCurrentCPURoleBackground
+ _HTIsSiriAIBundleID
+ _kHTSiriAIBundleID
CStrings:
+ "Failed to create state info JSON blob for hang (start %llu, end %llu, state info %@). Returning 0ms background duration."
+ "Hang detected: %.2fs (Siri AI in background CPU role with no visible UI, ignoring)"
+ "com.apple.campo"
```
