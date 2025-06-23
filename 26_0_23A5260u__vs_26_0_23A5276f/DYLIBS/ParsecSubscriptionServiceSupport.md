## ParsecSubscriptionServiceSupport

> `/System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport`

```diff

-3500.91.2.0.0
-  __TEXT.__text: 0xa7c
-  __TEXT.__auth_stubs: 0x1c0
+3500.98.1.0.0
+  __TEXT.__text: 0x152c
+  __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x33
-  __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0x3a
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0xb8
+  __TEXT.__cstring: 0x15f
+  __TEXT.__dlopen_cstrs: 0x63
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methname: 0x3e8
   __TEXT.__objc_methtype: 0x73
   __TEXT.__objc_stubs: 0x300
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x50
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe8
+  __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x1a0
   __DATA.__objc_ivar: 0x8
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F4B1826-7BEE-37FA-9F55-A1C332CC640A
-  Functions: 19
-  Symbols:   128
-  CStrings:  52
+  UUID: E2EA809F-8775-365D-9E76-C026F415845A
+  Functions: 35
+  Symbols:   191
+  CStrings:  63
 
Symbols:
+ -[PSSSSubscriptionManager unregisterSubscriptionWithInfo:].cold.1
+ -[PSSSSubscriptionManagerInternal getActiveSubscriptionServicesMatchingBundleIdentifiers:domainIdentifiers:maximumExpirationLimit:completionHandler:].cold.1
+ -[PSSSSubscriptionManagerInternal removeSubscriptionServiceForURL:].cold.1
+ -[PSSSSubscriptionManagerInternal removeWebSubscriptionServicesCreatedAfterDate:].cold.1
+ GCC_except_table1
+ GCC_except_table11
+ GCC_except_table14
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table3
+ GCC_except_table4
+ _VideoSubscriberAccountLibrary
+ _VideoSubscriberAccountLibraryCore.frameworkLibrary
+ __Block_object_dispose
+ __Unwind_Resume
+ ___VideoSubscriberAccountLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___getVSSubscriptionClass_block_invoke
+ ___getVSSubscriptionClass_block_invoke.cold.1
+ ___getVSSubscriptionFetchOptionSourcesSymbolLoc_block_invoke
+ ___getVSSubscriptionFetchOptionSubscriptionInfoSymbolLoc_block_invoke
+ ___getVSSubscriptionFetchOptionsForBundleIdentifiersAndDomainNamesSymbolLoc_block_invoke
+ ___getVSSubscriptionFetchOptionsForWebSubscriptionsCreatedAfterDateSymbolLoc_block_invoke
+ ___getVSSubscriptionRegistrationCenterClass_block_invoke
+ ___getVSSubscriptionRegistrationCenterClass_block_invoke.cold.1
+ ___getVSSubscriptionSourceClass_block_invoke
+ ___getVSSubscriptionSourceClass_block_invoke.cold.1
+ ___objc_personality_v0
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringVideoSubscriberAccount
+ _dlerror
+ _dlsym
+ _free
+ _getVSSubscriptionClass
+ _getVSSubscriptionClass.softClass
+ _getVSSubscriptionFetchOptionSourcesSymbolLoc.ptr
+ _getVSSubscriptionFetchOptionSubscriptionInfoSymbolLoc.ptr
+ _getVSSubscriptionFetchOptionsForBundleIdentifiersAndDomainNamesSymbolLoc.ptr
+ _getVSSubscriptionFetchOptionsForWebSubscriptionsCreatedAfterDateSymbolLoc.ptr
+ _getVSSubscriptionRegistrationCenterClass
+ _getVSSubscriptionRegistrationCenterClass.softClass
+ _getVSSubscriptionSourceClass
+ _getVSSubscriptionSourceClass.softClass
+ _objc_autoreleaseReturnValue
+ _objc_getClass
+ _objc_release_x26
+ _objc_retain_x21
+ _objc_retain_x26
+ _objc_retain_x8
+ _objc_retain_x9
- _OBJC_CLASS_$_VSSubscription
- _OBJC_CLASS_$_VSSubscriptionRegistrationCenter
- _OBJC_CLASS_$_VSSubscriptionSource
- _VSSubscriptionFetchOptionSources
- _VSSubscriptionFetchOptionSubscriptionInfo
- _VSSubscriptionFetchOptionsForBundleIdentifiersAndDomainNames
- _VSSubscriptionFetchOptionsForWebSubscriptionsCreatedAfterDate
- _objc_retain_x24
CStrings:
+ "%s"
+ "Unable to find class %s"
+ "VSSubscription"
+ "VSSubscriptionFetchOptionSources"
+ "VSSubscriptionFetchOptionSubscriptionInfo"
+ "VSSubscriptionFetchOptionsForBundleIdentifiersAndDomainNames"
+ "VSSubscriptionFetchOptionsForWebSubscriptionsCreatedAfterDate"
+ "VSSubscriptionRegistrationCenter"
+ "VSSubscriptionSource"
+ "softlink:r:path:/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount"
+ "v8@?0"

```
