## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-416.125.7.0.0
-  __TEXT.__text: 0x865ec
+416.250.1.0.0
+  __TEXT.__text: 0x86998
   __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x50fc
+  __TEXT.__objc_methlist: 0x510c
   __TEXT.__const: 0x7d0
-  __TEXT.__oslogstring: 0x121ce
+  __TEXT.__oslogstring: 0x1230e
   __TEXT.__cstring: 0xd295
   __TEXT.__gcc_except_tab: 0xa00
   __TEXT.__dlopen_cstrs: 0xb0

   __TEXT.__swift5_capture: 0x200
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__unwind_info: 0x1b38
+  __TEXT.__unwind_info: 0x1b48
   __TEXT.__eh_frame: 0x910
   __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0xe71e
+  __TEXT.__objc_methname: 0xe732
   __TEXT.__objc_methtype: 0x260b
-  __TEXT.__objc_stubs: 0xba20
+  __TEXT.__objc_stubs: 0xba60
   __DATA_CONST.__got: 0xfe8
   __DATA_CONST.__const: 0x2138
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3518
+  __DATA_CONST.__objc_selrefs: 0x3520
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x158

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 18CFD16A-795B-394D-B229-A1FE90A2D68F
-  Functions: 2861
-  Symbols:   9324
-  CStrings:  6099
+  UUID: D209BB62-8363-3721-B74E-4EA3AAF438FE
+  Functions: 2866
+  Symbols:   9336
+  CStrings:  6104
 
Symbols:
+ -[CDPDAnalyticsTransport _transportForEvent:]
+ -[CDPDAnalyticsTransport _transportForEvent:].cold.1
+ -[CDPDAnalyticsTransport _transportForEvent:].cold.2
+ -[CDPDAnalyticsTransport _transportForEvent:].cold.3
+ -[CDPDAnalyticsTransport _transportForEvent:].cold.4
+ _objc_msgSend$_transportForEvent:
+ _objc_msgSend$clientBundleId
CStrings:
+ "Failed to get privacy-compliant transport for clientName: %@, falling back to current transport"
+ "No privacy-compliant routing needed: event.clientName is nil"
+ "No privacy-compliant routing needed: event.clientName matches self.clientName (%@)"
+ "Routing event through privacy-compliant transport for clientName: %@"
+ "_transportForEvent:"

```
