## NetworkScore

> `/System/Library/PrivateFrameworks/NetworkScore.framework/NetworkScore`

```diff

-49.0.0.0.0
-  __TEXT.__text: 0x1b918
-  __TEXT.__auth_stubs: 0x6e0
+49.0.0.0.1
+  __TEXT.__text: 0x1b938
+  __TEXT.__auth_stubs: 0x6f0
   __TEXT.__objc_methlist: 0x8ac
   __TEXT.__const: 0x618
   __TEXT.__gcc_except_tab: 0x19f8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x7d8
   __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__objc_const: 0xb88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7585F968-C7BA-3F45-A669-3091472B43A2
+  UUID: 59CA93A5-FBB0-3C95-BEA6-10B80F6523D9
   Functions: 545
-  Symbols:   1870
+  Symbols:   1861
   CStrings:  645
 
Symbols:
+ _os_variant_has_internal_content
Functions:
~ -[NWSMetricReporter sendHTTPMetrics:onQueue:] : 400 -> 416
~ -[NWSMetricReporter sendStreamMetrics:onQueue:] : 400 -> 416

```
