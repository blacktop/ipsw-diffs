## languageassetd

> `/usr/libexec/languageassetd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-35.0.0.0.0
-  __TEXT.__text: 0x1900
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_stubs: 0x560
-  __TEXT.__objc_methlist: 0x154
+35.1.1.0.0
+  __TEXT.__text: 0x1c10
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__objc_stubs: 0x620
+  __TEXT.__objc_methlist: 0x1ac
   __TEXT.__cstring: 0x440
-  __TEXT.__const: 0x20
-  __TEXT.__objc_methname: 0x471
-  __TEXT.__oslogstring: 0xbf
+  __TEXT.__const: 0x28
+  __TEXT.__objc_methname: 0x550
+  __TEXT.__oslogstring: 0x11b
   __TEXT.__objc_classname: 0x2e
-  __TEXT.__objc_methtype: 0xc5
+  __TEXT.__objc_methtype: 0xe7
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x150
-  __DATA_CONST.__const: 0x2c0
+  __TEXT.__unwind_info: 0x178
+  __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__auth_got: 0x1c8
   __DATA_CONST.__got: 0x80
-  __DATA.__objc_const: 0x288
-  __DATA.__objc_selrefs: 0x178
-  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_const: 0x2f8
+  __DATA.__objc_selrefs: 0x1b0
+  __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xa0
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 58
-  Symbols:   79
-  CStrings:  112
+  Functions: 68
+  Symbols:   80
+  CStrings:  129
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
CStrings:
+ "Language asset download still failing after %lu attempts; giving up until the next trigger."
+ "Q"
+ "Q16@0:8"
+ "TQ,V_retryCount"
+ "_earliestNextRetry"
+ "_lastReachable"
+ "_retryCount"
+ "d"
+ "isNetworkReachable"
+ "reachabilityDidChangeToFlags:"
+ "retryCount"
+ "retryDownloadIfStillNeeded"
+ "scheduleRetryAfterFailure"
+ "setRetryCount:"
+ "unscheduleReachabilityMonitoring"
+ "v20@0:8I16"
+ "v24@0:8Q16"
```
