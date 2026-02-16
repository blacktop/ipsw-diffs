## RemoteManagementStore

> `/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore`

```diff

-585.80.2.0.0
-  __TEXT.__text: 0x3abc4
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_methlist: 0x2360
+585.100.8.0.0
+  __TEXT.__text: 0x3af04
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_methlist: 0x2390
   __TEXT.__const: 0x4cc
-  __TEXT.__cstring: 0x1126
+  __TEXT.__cstring: 0x107c
   __TEXT.__oslogstring: 0x33b7
-  __TEXT.__gcc_except_tab: 0x3c0
+  __TEXT.__gcc_except_tab: 0x3c4
   __TEXT.__swift5_typeref: 0x2bf
   __TEXT.__swift5_fieldmd: 0xa8
   __TEXT.__constg_swiftt: 0x9c

   __TEXT.__swift5_capture: 0x118
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0xe80
-  __TEXT.__eh_frame: 0xae8
-  __TEXT.__objc_classname: 0x68d
-  __TEXT.__objc_methname: 0x6f69
-  __TEXT.__objc_methtype: 0x1679
-  __TEXT.__objc_stubs: 0x4380
+  __TEXT.__unwind_info: 0xef0
+  __TEXT.__eh_frame: 0xaf8
+  __TEXT.__objc_classname: 0x69a
+  __TEXT.__objc_methname: 0x7033
+  __TEXT.__objc_methtype: 0x1754
+  __TEXT.__objc_stubs: 0x4540
   __DATA_CONST.__got: 0x400
   __DATA_CONST.__const: 0xf30
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1520
+  __DATA_CONST.__objc_selrefs: 0x1540
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x660
-  __AUTH_CONST.__const: 0x710
-  __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x35d8
+  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__const: 0x730
+  __AUTH_CONST.__cfstring: 0x1020
+  __AUTH_CONST.__objc_const: 0x3638
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x70
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1a4
-  __DATA.__data: 0x5d0
+  __DATA.__objc_ivar: 0x1ac
+  __DATA.__data: 0x5f0
   __DATA.__bss: 0x540
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xc30

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C24D4F63-7C33-3752-A3C4-80B5E4D148C6
-  Functions: 1316
-  Symbols:   3864
-  CStrings:  1704
+  UUID: 456C424C-234C-3F4F-B033-052F03DFFC88
+  Functions: 1332
+  Symbols:   3949
+  CStrings:  1710
 
Symbols:
+ +[RMStoreUtility currentEnrollmentTypeForStoreType:]
+ +[RMStoreUtility currentScopeForStoreScope:]
+ -[RMConfigurationSubscriberDescription initWithTypes:scopes:]
+ -[RMConfigurationSubscriberDescription scopes]
+ -[RMSubscribedConfigurationReference dynamicDeclaration]
+ _OBJC_IVAR_$_RMConfigurationSubscriberDescription._scopes
+ _OBJC_IVAR_$_RMSubscribedConfigurationReference._dynamicDeclaration
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ ___59-[RMConfigurationSubscriberDescription initWithDictionary:]_block_invoke_2
+ ___block_literal_global.16
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$buildWithCode:description:details:
+ _objc_msgSend$declarationsWithCompletionHandler:
+ _objc_msgSend$init
+ _objc_msgSend$initWithTypes:scopes:
+ _objc_msgSend$isSupervised
+ _objc_msgSend$linkStoreToProfileIdentifier:accountIdentifier:completionHandler:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$newProfileControllerWithPrefix:scope:
+ _objc_msgSend$payloadAppStoreID
+ _objc_msgSend$payloadBundleID
+ _objc_msgSend$payloadManifestURL
+ _objc_msgSend$payloadStandardConfigurations
+ _objc_msgSend$setPayloadStandardConfigurations:
+ _objc_msgSend$waitForActiveAndValidDeclarations:timeout:completionHandler:
+ _swift_bridgeObjectRelease_n
- -[RMConfigurationSubscriberDescription initWithTypes:]
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithTypes:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "Scopes"
+ "T@\"NSArray\",R,C,N,V_scopes"
+ "T@\"RMModelDeclarationBase\",R,N,V_dynamicDeclaration"
+ "_dynamicDeclaration"
+ "_scopes"
+ "currentEnrollmentTypeForStoreType:"
+ "currentScopeForStoreScope:"
+ "dynamicDeclaration"
+ "initWithTypes:scopes:"
+ "q24@0:8q16"
+ "scopes"
- "initWithTypes:"

```
