## FeedbackLogger

> `/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger`

```diff

-3301.13.1.0.0
-  __TEXT.__text: 0xa64c
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0xb70
+3302.18.2.0.0
+  __TEXT.__text: 0xb2c4
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0xc88
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__cstring: 0x170b
-  __TEXT.__oslogstring: 0x1421
-  __TEXT.__unwind_info: 0x2f0
-  __TEXT.__objc_classname: 0xf3
-  __TEXT.__objc_methname: 0x222d
-  __TEXT.__objc_methtype: 0x56e
-  __TEXT.__objc_stubs: 0x1860
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x2d0
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__gcc_except_tab: 0x134
+  __TEXT.__cstring: 0x1737
+  __TEXT.__oslogstring: 0x14cf
+  __TEXT.__unwind_info: 0x330
+  __TEXT.__objc_classname: 0x111
+  __TEXT.__objc_methname: 0x25ff
+  __TEXT.__objc_methtype: 0x64a
+  __TEXT.__objc_stubs: 0x1a40
+  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__const: 0x300
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1460
-  __DATA_CONST.__objc_selrefs: 0x888
+  __DATA_CONST.__objc_const: 0x1608
+  __DATA_CONST.__objc_selrefs: 0x920
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__cfstring: 0x600
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xa8
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0xe8
+  __DATA.__objc_classrefs: 0xc0
+  __DATA.__objc_superrefs: 0x30
+  __DATA.__objc_ivar: 0x100
   __DATA.__data: 0x120
-  __DATA_DIRTY.__const: 0x80
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__const: 0x40
   __DATA_DIRTY.__objc_const: 0x2c8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 9755FD79-E09B-3036-BBA7-03200F90F73B
-  Functions: 266
-  Symbols:   1033
-  CStrings:  765
+  UUID: 66DDBA59-215E-3485-BBC1-CD86DC666835
+  Functions: 292
+  Symbols:   1129
+  CStrings:  808
 
Symbols:
+ +[FLContainerStorePathManager canLookupFeedbackLoggerMachService]
+ -[FLContainerStorePathManager .cxx_destruct]
+ -[FLContainerStorePathManager containerPathForStoreId:]
+ -[FLContainerStorePathManager dealloc]
+ -[FLContainerStorePathManager fbf]
+ -[FLContainerStorePathManager init]
+ -[FLContainerStorePathManager log]
+ -[FLContainerStorePathManager sandboxExtensionTokens]
+ -[FLContainerStorePathManager setFbf:]
+ -[FLContainerStorePathManager setLog:]
+ -[FLContainerStorePathManager setSandboxExtensionTokens:]
+ -[FLContainerStorePathManager setStoreIdToContainerPathMap:]
+ -[FLContainerStorePathManager setStoreIdToLastSandboxExtensionRequestMap:]
+ -[FLContainerStorePathManager storeIdToContainerPathMap]
+ -[FLContainerStorePathManager storeIdToLastSandboxExtensionRequestMap]
+ -[FLLogger __dispatched_databaseConnectionWithStorePath:]
+ -[FLLogger __dispatched_persistentStoreWithId:category:storePath:]
+ -[FLLogger siriReadingStoreForBundleID:directoryPath:]
+ -[FLLoggingContext containerStorePathManager]
+ -[FLLoggingContext pathForStore:category:]
+ -[FLLoggingContext setContainerStorePathManager:]
+ -[FLLoggingContext shouldPersistInGroupContainer:category:]
+ -[FeedbackLoggerFBFClient requestSandboxExtensionForBundleID:completion:]
+ GCC_except_table193
+ GCC_except_table217
+ GCC_except_table272
+ GCC_except_table55
+ GCC_except_table59
+ GCC_except_table75
+ GCC_except_table89
+ _FLMachServiceName
+ _OBJC_CLASS_$_FLContainerStorePathManager
+ _OBJC_CLASS_$_NSArray
+ _OBJC_IVAR_$_FLContainerStorePathManager._fbf
+ _OBJC_IVAR_$_FLContainerStorePathManager._log
+ _OBJC_IVAR_$_FLContainerStorePathManager._sandboxExtensionTokens
+ _OBJC_IVAR_$_FLContainerStorePathManager._storeIdToContainerPathMap
+ _OBJC_IVAR_$_FLContainerStorePathManager._storeIdToLastSandboxExtensionRequestMap
+ _OBJC_IVAR_$_FLLoggingContext._containerStorePathManager
+ _OBJC_METACLASS_$_FLContainerStorePathManager
+ _SANDBOX_CHECK_NO_REPORT
+ __OBJC_$_CLASS_METHODS_FLContainerStorePathManager
+ __OBJC_$_CLASS_PROP_LIST_FLContainerStorePathManager
+ __OBJC_$_INSTANCE_METHODS_FLContainerStorePathManager
+ __OBJC_$_INSTANCE_VARIABLES_FLContainerStorePathManager
+ __OBJC_$_PROP_LIST_FLContainerStorePathManager
+ __OBJC_$_PROP_LIST_FLLoggingContext.99
+ __OBJC_$_PROP_LIST_NSObject.707
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.708
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.709
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.710
+ __OBJC_CLASS_RO_$_FLContainerStorePathManager
+ __OBJC_METACLASS_RO_$_FLContainerStorePathManager
+ ___31-[FeedbackLoggerFBFClient init]_block_invoke.49
+ ___54-[FLLogger siriReadingStoreForBundleID:directoryPath:]_block_invoke
+ ___55-[FLContainerStorePathManager containerPathForStoreId:]_block_invoke
+ ___65+[FLContainerStorePathManager canLookupFeedbackLoggerMachService]_block_invoke
+ ___Block_byref_object_copy_.380
+ ___Block_byref_object_dispose_.381
+ ___block_descriptor_56_e8_32s40s48r_e31_v24?0"NSString"8"NSString"16ls32l8r48l8s40l8
+ ___block_literal_global.398
+ ___block_literal_global.572
+ ___block_literal_global.716
+ __unnamed_array_storage.106
+ _canLookupFeedbackLoggerMachService.canTalkToFBF
+ _canLookupFeedbackLoggerMachService.onceToken
+ _getpid
+ _objc_msgSend$__dispatched_databaseConnectionWithStorePath:
+ _objc_msgSend$__dispatched_persistentStoreWithId:category:storePath:
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$canLookupFeedbackLoggerMachService
+ _objc_msgSend$containerPathForStoreId:
+ _objc_msgSend$containerStorePathManager
+ _objc_msgSend$intValue
+ _objc_msgSend$integerValue
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$pathForStore:category:
+ _objc_msgSend$pathWithComponents:
+ _objc_msgSend$requestSandboxExtensionForBundleID:completion:
+ _objc_msgSend$sandboxExtensionTokens
+ _objc_msgSend$shouldPersistInGroupContainer:category:
+ _objc_msgSend$storeIdToContainerPathMap
+ _objc_msgSend$storeIdToLastSandboxExtensionRequestMap
+ _objc_retain_x25
+ _sandbox_check
+ _sandbox_extension_consume
+ _sandbox_extension_release
- -[FLLogger __dispatched_databaseConnectionWithId:]
- -[FLLogger pathForStore:]
- GCC_except_table191
- GCC_except_table247
- GCC_except_table57
- GCC_except_table71
- GCC_except_table87
- __OBJC_$_PROP_LIST_FLLoggingContext.86
- __OBJC_$_PROP_LIST_NSObject.634
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.635
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.636
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.637
- ___31-[FeedbackLoggerFBFClient init]_block_invoke.47
- ___block_literal_global.507
- ___block_literal_global.643
- __unnamed_array_storage.110
- _objc_msgSend$URLByStandardizingPath
- _objc_msgSend$__dispatched_databaseConnectionWithId:
CStrings:
+ "\x05"
+ "@\"FLContainerStorePathManager\""
+ "@\"FeedbackLoggerFBFClient\""
+ "@\"NSMutableArray\""
+ "@\"NSString\"32@0:8@\"NSString\"16@\"NSNumber\"24"
+ "B32@0:8@\"NSString\"16@\"NSNumber\"24"
+ "B32@0:8@16@24"
+ "FLContainerStorePathManager"
+ "Received persist request for store (%@, %@) for %lu bytes"
+ "T@\"FLContainerStorePathManager\",&,N,V_containerStorePathManager"
+ "T@\"FeedbackLoggerFBFClient\",&,N,V_fbf"
+ "T@\"NSMutableArray\",C,N,V_sandboxExtensionTokens"
+ "T@\"NSMutableDictionary\",C,N,V_storeIdToContainerPathMap"
+ "T@\"NSMutableDictionary\",C,N,V_storeIdToLastSandboxExtensionRequestMap"
+ "TB,R,N"
+ "Throttling repeat request for group container sandbox extension."
+ "Unable to consume group container sandbox extension."
+ "Unable to obtain group container sandbox extension."
+ "__dispatched_databaseConnectionWithStorePath:"
+ "__dispatched_persistentStoreWithId:category:storePath:"
+ "_containerStorePathManager"
+ "_sandboxExtensionTokens"
+ "_storeIdToContainerPathMap"
+ "_storeIdToLastSandboxExtensionRequestMap"
+ "array"
+ "arrayWithObjects:count:"
+ "canLookupFeedbackLoggerMachService"
+ "containerPathForStoreId:"
+ "containerStorePathManager"
+ "intValue"
+ "integerValue"
+ "mach-lookup"
+ "numberWithLongLong:"
+ "pathForStore:category:"
+ "pathWithComponents:"
+ "requestSandboxExtensionForBundleID:completion:"
+ "sandboxExtensionTokens"
+ "setContainerStorePathManager:"
+ "setSandboxExtensionTokens:"
+ "setStoreIdToContainerPathMap:"
+ "setStoreIdToLastSandboxExtensionRequestMap:"
+ "shouldPersistInGroupContainer:category:"
+ "siriReadingStoreForBundleID:directoryPath:"
+ "storeIdToContainerPathMap"
+ "storeIdToLastSandboxExtensionRequestMap"
+ "v24@?0@\"NSString\"8@\"NSString\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSString\">24"
- "Received persist request for store (%@) for %lu bytes"
- "URLByStandardizingPath"
- "__dispatched_databaseConnectionWithId:"
- "pathForStore:"

```
