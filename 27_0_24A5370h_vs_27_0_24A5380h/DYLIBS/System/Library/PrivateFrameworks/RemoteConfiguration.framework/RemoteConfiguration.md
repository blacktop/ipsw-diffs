## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration`

```diff

-  __TEXT.__text: 0x2bf84
+  __TEXT.__text: 0x2c030
   __TEXT.__objc_methlist: 0x2ff4
   __TEXT.__const: 0x208
   __TEXT.__gcc_except_tab: 0x6cc

   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b68
+  __DATA_CONST.__objc_selrefs: 0x1b70
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__got: 0x318

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   Functions: 1405
-  Symbols:   4611
+  Symbols:   4612
   CStrings:  829
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _objc_msgSend$initWithArray:copyItems:
Functions:
~ -[RCConfigurationManager _isValidConfigurationResource:configurationSettings:allowedToReachEndpoint:cachePolicy:] : 1024 -> 1040
~ +[RCEndpointResponseProcessing parseEndpointResponseDict:parsingError:configurationSettings:maxAge:loggingPrefix:completion:] : 2168 -> 2256
~ ___183-[RCConfigurationManager _processConfigurationCompletionWithResources:configurationSettings:processedConfigurationDataByRequestKey:processedTreatmentIDs:processedSegmentSetIDs:error:]_block_invoke : 808 -> 876

```
