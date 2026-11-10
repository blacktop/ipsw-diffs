## HomeKitDaemonShared

> `/System/Library/PrivateFrameworks/HomeKitDaemonShared.framework/Versions/A/HomeKitDaemonShared`

```diff

-1493.1.5.4.1
-  __TEXT.__text: 0xd038
-  __TEXT.__objc_methlist: 0xc04
+1520.2.7.4.1
+  __TEXT.__text: 0xd420
+  __TEXT.__objc_methlist: 0xc24
   __TEXT.__const: 0x320
   __TEXT.__constg_swiftt: 0xa0
   __TEXT.__swift5_typeref: 0xbf
   __TEXT.__swift5_fieldmd: 0xa0
   __TEXT.__swift5_types: 0x10
-  __TEXT.__oslogstring: 0x19ef
+  __TEXT.__oslogstring: 0x1b8a
   __TEXT.__swift5_capture: 0x10
   __TEXT.__cstring: 0x52b
   __TEXT.__swift5_reflstr: 0x33

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7b8
+  __DATA_CONST.__objc_selrefs: 0x7d0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__got: 0x1a8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 297
-  Symbols:   805
-  CStrings:  169
+  Functions: 300
+  Symbols:   811
+  CStrings:  175
 
Symbols:
+ -[HMDStatusChannel _shouldRetryDeassertPresence]
+ -[HMDStatusChannel _startDeassertRetryTimer]
+ -[HMDStatusChannel _stopDeassertRetryTimer]
+ _objc_msgSend$_shouldRetryDeassertPresence
+ _objc_msgSend$_startDeassertRetryTimer
+ _objc_msgSend$_stopDeassertRetryTimer
CStrings:
+ "Canceling the pending de-assert retry because a publish was requested"
+ "Not retrying the de-assert because publishing has resumed"
+ "Not retrying the de-assert because the channel is stopped"
+ "[%{public}@] Canceling the pending de-assert retry because a publish was requested"
+ "[%{public}@] Not retrying the de-assert because publishing has resumed"
+ "[%{public}@] Not retrying the de-assert because the channel is stopped"
```
