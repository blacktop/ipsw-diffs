## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

-1084.40.7.0.0
-  __TEXT.__text: 0x78bd0
+1084.60.3.0.0
+  __TEXT.__text: 0x78ea4
   __TEXT.__objc_methlist: 0x6414
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x7d83
-  __TEXT.__oslogstring: 0xbad9
+  __TEXT.__cstring: 0x7d99
+  __TEXT.__oslogstring: 0xbb20
   __TEXT.__gcc_except_tab: 0xbac
-  __TEXT.__unwind_info: 0x25b0
+  __TEXT.__unwind_info: 0x25c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x178
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f60
+  __DATA_CONST.__objc_selrefs: 0x2f70
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x770
-  __DATA_CONST.__got: 0x7a0
+  __DATA_CONST.__got: 0x7a8
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x6c80
+  __AUTH_CONST.__cfstring: 0x6ca0
   __AUTH_CONST.__objc_const: 0xdbb0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x488

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2827
-  Symbols:   4895
-  CStrings:  1863
+  Functions: 2831
+  Symbols:   4897
+  CStrings:  1865
 
Symbols:
+ -[RBConnectionClient _rbs_clientTrustedForAssertionErrorDetail]
+ -[RBSLegacyAttribute _isOriginatorValidForContext:errorReason:redactForUntrustedClient:]
+ -[RBSLegacyAttribute _isTargetValidForContext:errorReason:redactForUntrustedClient:]
+ _RBSErrorRedactForUntrustedClientKey
- -[RBSLegacyAttribute _isOriginatorValidForContext:errorReason:]
- -[RBSLegacyAttribute _isTargetValidForContext:errorReason:]
CStrings:
+ "Assertion acquisition failed: target process %{public}@ does not exist"
+ "outRedact is required"
```
