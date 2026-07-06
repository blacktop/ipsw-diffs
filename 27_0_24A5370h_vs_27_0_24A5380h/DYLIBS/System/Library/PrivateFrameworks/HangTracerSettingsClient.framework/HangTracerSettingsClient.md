## HangTracerSettingsClient

> `/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient`

```diff

-  __TEXT.__text: 0x16a08
-  __TEXT.__objc_methlist: 0xc2c
+  __TEXT.__text: 0x17278
+  __TEXT.__objc_methlist: 0xc94
   __TEXT.__const: 0x20c2
-  __TEXT.__cstring: 0x31a2
+  __TEXT.__cstring: 0x31ce
   __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__oslogstring: 0x54c
+  __TEXT.__oslogstring: 0x60a
   __TEXT.__dlopen_cstrs: 0xaf
   __TEXT.__ustring: 0x822
   __TEXT.__swift5_typeref: 0x4c3

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x194
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__unwind_info: 0x660
+  __TEXT.__unwind_info: 0x670
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd78
+  __DATA_CONST.__const: 0xdc8
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb20
+  __DATA_CONST.__objc_selrefs: 0xb60
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__got: 0x380
   __AUTH_CONST.__const: 0x608
-  __AUTH_CONST.__cfstring: 0x3960
-  __AUTH_CONST.__objc_const: 0x15b0
+  __AUTH_CONST.__cfstring: 0x3980
+  __AUTH_CONST.__objc_const: 0x1670
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x4b0
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0xcc
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0xdc
   __DATA.__data: 0x6f8
   __DATA.__bss: 0x36b0
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 790
-  Symbols:   1750
-  CStrings:  1031
+  Functions: 806
+  Symbols:   1797
+  CStrings:  1041
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[HTHang isBoosted]
+ -[HTHang tailspinPath]
+ -[HTHangReporterService prioritizeTaskWithHangIDAndExpedite:completion:]
+ -[HTHangsDataEntry initWithPath:hangID:creationDate:duration:processBundleID:processPath:processRecord:isBoosted:isBeingProcessed:]
+ -[HTHangsDataEntry isBoosted]
+ -[HTHangsDataFinder hangReporterDoneProcessingTailspin:]
+ -[HTHangsDataFinder initWithLogUpdateCallback:tailspinSavedCallback:tailspinDoneCallback:]
+ -[HTHangsDataFinder setTailspinDoneCallback:]
+ -[HTHangsDataFinder tailspinDoneCallback]
+ GCC_except_table17
+ _OBJC_IVAR_$_HTHang._isBoosted
+ _OBJC_IVAR_$_HTHang._tailspinPath
+ _OBJC_IVAR_$_HTHangsDataEntry._isBoosted
+ _OBJC_IVAR_$_HTHangsDataFinder._tailspinDoneCallback
+ ___72-[HTHangReporterService prioritizeTaskWithHangIDAndExpedite:completion:]_block_invoke
+ ___72-[HTHangReporterService prioritizeTaskWithHangIDAndExpedite:completion:]_block_invoke_2
+ ___72-[HTHangReporterService prioritizeTaskWithHangIDAndExpedite:completion:]_block_invoke_3
+ ___90-[HTHangsDataFinder initWithLogUpdateCallback:tailspinSavedCallback:tailspinDoneCallback:]_block_invoke
+ ___90-[HTHangsDataFinder initWithLogUpdateCallback:tailspinSavedCallback:tailspinDoneCallback:]_block_invoke_2
+ ___90-[HTHangsDataFinder initWithLogUpdateCallback:tailspinSavedCallback:tailspinDoneCallback:]_block_invoke_3
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ _kHTDoneProcessingTailspinNotification
+ _kHTExtendedAttributeIsBoosted
+ _kHTExtendedAttributeTailspinPath
+ _objc_msgSend$initWithLogUpdateCallback:tailspinSavedCallback:tailspinDoneCallback:
+ _objc_msgSend$initWithPath:hangID:creationDate:duration:processBundleID:processPath:processRecord:isBoosted:isBeingProcessed:
+ _objc_msgSend$isBoosted
+ _objc_msgSend$tailspinPath
+ _xpc_dictionary_get_bool
- GCC_except_table16
- ___69-[HTHangsDataFinder initWithLogUpdateCallback:tailspinSavedCallback:]_block_invoke
- ___69-[HTHangsDataFinder initWithLogUpdateCallback:tailspinSavedCallback:]_block_invoke_2
- ___69-[HTHangsDataFinder initWithLogUpdateCallback:tailspinSavedCallback:]_block_invoke_3
- ___72-[HTHangsDataFinder findEventsFilteringDeveloperApps:completionHandler:]_block_invoke_3
- _objc_msgSend$initWithPath:hangID:creationDate:duration:processBundleID:processPath:processRecord:
- _objc_retain_x26
CStrings:
+ "Boost request sent for hangID %@"
+ "Hang UUID is required"
+ "Invalid reply from hangreporter"
+ "boost-task"
+ "handleReporterDidSaveTailspin()"
+ "handleReporterDoneProcessingTailspin()"
+ "hangUUID"
+ "prioritizeTaskWithHangIDAndExpedite: hangID nil"
+ "success"

```
