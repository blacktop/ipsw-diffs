## XprotectFramework

> `/System/Library/PrivateFrameworks/XprotectFramework.framework/Versions/A/XprotectFramework`

```diff

-211.60.7.0.0
-  __TEXT.__text: 0x9800
+211.100.17.0.0
+  __TEXT.__text: 0x9f50
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0x78c
-  __TEXT.__cstring: 0xd15
+  __TEXT.__objc_methlist: 0x8d0
+  __TEXT.__cstring: 0xd64
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x6d0
-  __TEXT.__gcc_except_tab: 0x3e8
-  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__oslogstring: 0x6f1
+  __TEXT.__gcc_except_tab: 0x440
+  __TEXT.__unwind_info: 0x310
   __TEXT.__objc_classname: 0x184
-  __TEXT.__objc_methname: 0x163e
-  __TEXT.__objc_methtype: 0x73c
-  __TEXT.__objc_stubs: 0x1200
+  __TEXT.__objc_methname: 0x174f
+  __TEXT.__objc_methtype: 0x750
+  __TEXT.__objc_stubs: 0x1260
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x618
+  __DATA_CONST.__objc_selrefs: 0x670
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x1570
+  __AUTH_CONST.__cfstring: 0x1040
+  __AUTH_CONST.__objc_const: 0x1488
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x108
+  __DATA.__objc_ivar: 0x110
   __DATA.__data: 0x240
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libEndpointSecuritySystem.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9A2EF45-7DCA-3C61-8BE9-403387F2F1B9
-  Functions: 229
-  Symbols:   768
-  CStrings:  690
+  UUID: 43E7356B-1921-3D30-A370-641C71B42471
+  Functions: 239
+  Symbols:   786
+  CStrings:  713
 
Symbols:
+ -[XProtectUpdate doUpdate:]
+ -[XProtectUpdateMetadata description]
+ -[XProtectUpdateMetadata initWithVersion:andDate:andPreviousVersion:andSelectedSource:]
+ -[XProtectUpdateMetadata previousVersion]
+ -[XProtectUpdateMetadata selectedSource]
+ -[XProtectUpdateMetadata setDate:]
+ -[XProtectUpdateMetadata setPreviousVersion:]
+ -[XProtectUpdateMetadata setSelectedSource:]
+ -[XProtectUpdateMetadata setVersion:]
+ GCC_except_table19
+ OBJC_IVAR_$_XProtectUpdateMetadata.previousVersion
+ OBJC_IVAR_$_XProtectUpdateMetadata.selectedSource
+ _XProtectUpdateServiceErrorNeedsDefer
+ __22-[XProtectUpdate init]_block_invoke.13
+ __27-[XProtectUpdate doUpdate:]_block_invoke.21
+ __34-[XProtectUpdate prereleaseUpdate]_block_invoke.18
+ __40-[XProtectUpdate updateWithForceOnline:]_block_invoke.17
+ __43-[XProtectUpdate fetchAvailableUpdateInfo:]_block_invoke.19
+ ___27-[XProtectUpdate doUpdate:]_block_invoke
+ __block_literal_global.15
+ _objc_msgSend$code
+ _objc_msgSend$domain
+ _objc_msgSend$runUpdateWithReplyAndMetadata:
- __22-[XProtectUpdate init]_block_invoke.12
- __34-[XProtectUpdate prereleaseUpdate]_block_invoke.17
- __40-[XProtectUpdate updateWithForceOnline:]_block_invoke.16
- __43-[XProtectUpdate fetchAvailableUpdateInfo:]_block_invoke.18
- __block_literal_global.14
CStrings:
+ "@48@0:8@16@24@32@40"
+ "Performed update with status: %@"
+ "T@\"NSDate\",&,N,Vdate"
+ "T@\"NSNumber\",&,N,VpreviousVersion"
+ "T@\"NSNumber\",&,N,VselectedSource"
+ "T@\"NSNumber\",&,N,Vversion"
+ "Version: %@, previous: %@"
+ "XProtectUpdateError"
+ "_previousVersion"
+ "_selectedSource"
+ "code"
+ "doUpdate:"
+ "domain"
+ "initWithVersion:andDate:andPreviousVersion:andSelectedSource:"
+ "previousVersion"
+ "runUpdateWithReplyAndMetadata:"
+ "selectedSource"
+ "setDate:"
+ "setPreviousVersion:"
+ "setSelectedSource:"
+ "setVersion:"
- "T@\"NSDate\",R,N,Vdate"
- "T@\"NSNumber\",R,N,Vversion"

```
