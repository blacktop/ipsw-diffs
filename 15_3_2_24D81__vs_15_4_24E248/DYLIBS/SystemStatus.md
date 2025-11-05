## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/Versions/A/SystemStatus`

```diff

-210.3.2.0.0
-  __TEXT.__text: 0x3d914
+210.4.13.0.0
+  __TEXT.__text: 0x3da24
   __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x46f4
+  __TEXT.__objc_methlist: 0x4cd0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x2aaa
+  __TEXT.__cstring: 0x2b08
   __TEXT.__gcc_except_tab: 0x3ec
-  __TEXT.__oslogstring: 0x1252
-  __TEXT.__unwind_info: 0x15f0
-  __TEXT.__objc_classname: 0x10ed
-  __TEXT.__objc_methname: 0x6694
+  __TEXT.__oslogstring: 0x128e
+  __TEXT.__unwind_info: 0x15d8
+  __TEXT.__objc_classname: 0x10ee
+  __TEXT.__objc_methname: 0x675e
   __TEXT.__objc_methtype: 0x1215
-  __TEXT.__objc_stubs: 0x3f40
+  __TEXT.__objc_stubs: 0x3f80
   __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__const: 0x648
   __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1370
+  __DATA_CONST.__objc_selrefs: 0x1400
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x1580
-  __AUTH_CONST.__cfstring: 0x28e0
-  __AUTH_CONST.__objc_const: 0x9ad8
+  __AUTH_CONST.__cfstring: 0x2920
+  __AUTH_CONST.__objc_const: 0x9128
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x2170
-  __DATA.__objc_ivar: 0x310
+  __DATA.__objc_ivar: 0x314
   __DATA.__data: 0xcc8
   __DATA.__bss: 0x100
   __DATA.__common: 0x40

   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2454C755-85CB-3D07-91EC-466178CD4716
-  Functions: 1892
-  Symbols:   4044
-  CStrings:  2057
+  UUID: E99E97E1-458E-396B-BA90-C9CB54F41233
+  Functions: 1890
+  Symbols:   4048
+  CStrings:  2066
 
Symbols:
+ -[STBackgroundActivityVisualDescriptor prefersToSuppressDefaultUserInteractionHandler]
+ -[STMutableBackgroundActivityVisualDescriptor setPrefersToSuppressDefaultUserInteractionHandler:]
+ -[STStatusDomainPublisherXPCServerHandle _resendDataIfNecessary]
+ GCC_except_table53
+ OBJC_IVAR_$_STBackgroundActivityVisualDescriptor._prefersToSuppressDefaultUserInteractionHandler
+ __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke.69
+ __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke.73
+ __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke.77
+ __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke.82
+ __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke_2.78
+ __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke_2.83
+ __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke_3.84
+ __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke_4.85
+ _objc_msgSend$prefersToSuppressDefaultUserInteractionHandler
+ _objc_msgSend$setPrefersToSuppressDefaultUserInteractionHandler:
- -[STStatusDomainPublisherXPCServerHandle _hasStatusDomainPublisherEntitlement]
- -[STStatusDomainPublisherXPCServerHandle _internalQueue_reregisterForPublishingDomains]
- GCC_except_table52
- __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke.63
- __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke.67
- __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke.71
- __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke.76
- __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke_2.72
- __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke_2.77
- __48-[STBackgroundActivityVisualDescriptor isEqual:]_block_invoke_3.78
- ___84-[STStatusDomainPublisherXPCServerHandle _reregisterForPublishingDomainsIfNecessary]_block_invoke
CStrings:
+ "PrefersToSuppressDefaultUserInteractionHandler"
+ "Server proxy error, resending data if necessary: %{public}@"
+ "TB,R,N,V_prefersToSuppressDefaultUserInteractionHandler"
+ "_prefersToSuppressDefaultUserInteractionHandler"
+ "prefersToSuppressDefaultUserInteractionHandler"
+ "setPrefersToSuppressDefaultUserInteractionHandler:"

```
